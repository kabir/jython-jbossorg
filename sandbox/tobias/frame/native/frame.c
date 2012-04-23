/*
 * JVM Call Frame Introspection Library
 * Copyright (c) 2008 Tobias Ivarsson
 *
 * Licensed for use under "The MIT License":
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
#include "jvmti.h"
#include "callframes.h"

const jint ACC_STATIC = 8;

typedef struct {
  jvmtiEnv *jvmti;
} GlobalAgentData;

static GlobalAgentData *globalData = NULL;

jint throwException(JNIEnv *env, const char *name, const char *msg) {
  jclass clazz;
  clazz = (*env)->FindClass(env, name);
  return (*env)->ThrowNew(env, clazz, msg);
}

jvmtiEnv *getJvmToolingInterface(JavaVM *jvm) {
  int err;
  jvmtiEnv *jvmti;
  if (!jvm) {
    return NULL;
  }
  err = (*jvm)->GetEnv(jvm, (void **)&jvmti, JVMTI_VERSION_1_0);
  if (err != JNI_OK) {
    return NULL;
  }
  return jvmti;
}

jboolean InitializeAgent(JavaVM *jvm) {
  static GlobalAgentData data;
  if (!globalData) {
    (void)memset(&data, 0, sizeof(data));
    globalData = &data;
    globalData->jvmti = getJvmToolingInterface(jvm);
  }
  if (globalData->jvmti) {
    return JNI_TRUE;
  } else {
    return JNI_FALSE;
  }
}

/*
 * Agent load method.
 */
JNIEXPORT jint JNICALL 
Agent_OnLoad(JavaVM *jvm, char *options, void *reserved)
{
  jvmtiCapabilities capa;
  jvmtiError tiErr;
  if (InitializeAgent(jvm)) {
    (void)memset(&capa, 0, sizeof(capa));
    capa.can_access_local_variables = 1;
    tiErr = (*(globalData->jvmti))->AddCapabilities(globalData->jvmti, &capa);
    if (tiErr != JVMTI_ERROR_NONE) {
      if (tiErr == JVMTI_ERROR_NOT_AVAILABLE) {
	printf("ERROR: The can_access_local_variables capability is not available.");
      } else {
	printf("ERROR: JVMTI error code: 0x%x\n", tiErr);
      }
    }
  } else {
    printf("ERROR: Could not load JVM Tooling Interface.\n");
  }
  return 0;
}

JavaVM *getJavaVM(JNIEnv *env) {
  int err;
  JavaVM *jvm;
  err = (*env)->GetJavaVM(env, &jvm);
  if (err != 0) {
    throwException(env, "java/lang/RuntimeException", // TODO: better exception
		   "Could not access the JavaVM.");
    return NULL;
  }
  return jvm;
}

/*
 * Class:     org_thobe_frame_Frame
 * Method:    setupNative
 * Signature: ()Z
 *
 * Set up all the requirements of the native library.
 */
JNIEXPORT jboolean JNICALL
Java_org_thobe_frame_Frame_setupNative(JNIEnv *env, jclass cls)
{
  jvmtiCapabilities capa;
  jvmtiError tiErr;
  if (!InitializeAgent(getJavaVM(env))) return JNI_FALSE;
  (void)memset(&capa, 0, sizeof(capa));
  tiErr = (*(globalData->jvmti))->GetCapabilities(globalData->jvmti, &capa);
  if (!tiErr) {
    if (capa.can_get_line_numbers && capa.can_access_local_variables) {
      return JNI_TRUE;
    }
    (void)memset(&capa, 0, sizeof(capa));
    capa.can_access_local_variables = 1;
    capa.can_get_line_numbers = 1;
    tiErr = (*(globalData->jvmti))->AddCapabilities(globalData->jvmti, &capa);
    if (tiErr == JVMTI_ERROR_NONE) {
      return JNI_TRUE;
    } else {
      return JNI_FALSE;
    }
  } else {
    return JNI_FALSE;
  }
}

jobject getLocalValue(JNIEnv *env, jthread thread, jint depth,
		      jvmtiLocalVariableEntry *table, int index) {
  jobject result;
  jint iVal;
  jfloat fVal;
  jdouble dVal;
  jlong jVal;
  jvmtiError tiErr;
  jclass reflectClass;
  jmethodID valueOf;
  // Retreive
  switch (table[index].signature[0]) {
  case '[': // Array
  case 'L': // Object
    tiErr = (*(globalData->jvmti))->GetLocalObject(globalData->jvmti, thread,
						   depth, table[index].slot,
						   &result);
    break;
  case 'J': // long
    tiErr = (*(globalData->jvmti))->GetLocalLong(globalData->jvmti, thread,
						 depth, table[index].slot,
						 &jVal);
    break;
  case 'F': // float
    tiErr = (*(globalData->jvmti))->GetLocalFloat(globalData->jvmti, thread,
						  depth, table[index].slot,
						  &fVal);
    break;
  case 'D': // double
    tiErr = (*(globalData->jvmti))->GetLocalDouble(globalData->jvmti, thread,
						   depth, table[index].slot,
						   &dVal);
    break;
    // Integer types
  case 'I': // int
  case 'S': // short
  case 'C': // char
  case 'B': // byte
  case 'Z': // boolean
    tiErr = (*(globalData->jvmti))->GetLocalInt(globalData->jvmti, thread,
						depth, table[index].slot,
						&iVal);
    break;
    // error type
  default:
    return NULL;
  }
  if (tiErr != JVMTI_ERROR_NONE) {
    return NULL;
  }
  // Box primitives
  switch (table[index].signature[0]) {
  case 'J': // long
    reflectClass = (*env)->FindClass(env, "java/lang/Long");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(J)Ljava/lang/Long;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, jVal);
    break;
  case 'F': // float
    reflectClass = (*env)->FindClass(env, "java/lang/Float");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(F)Ljava/lang/Float;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, fVal);
    break;
  case 'D': // double
    reflectClass = (*env)->FindClass(env, "java/lang/Double");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(D)Ljava/lang/Double;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, dVal);
    break;
    // INTEGER TYPES
  case 'I': // int
    reflectClass = (*env)->FindClass(env, "java/lang/Integer");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(I)Ljava/lang/Integer;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, iVal);
    break;
  case 'S': // short
    reflectClass = (*env)->FindClass(env, "java/lang/Short");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(S)Ljava/lang/Short;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, iVal);
    break;
  case 'C': // char
    reflectClass = (*env)->FindClass(env, "java/lang/Character");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(C)Ljava/lang/Character;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, iVal);
    break;
  case 'B': // byte
    reflectClass = (*env)->FindClass(env, "java/lang/Byte");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(B)Ljava/lang/Byte;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, iVal);
    break;
  case 'Z': // boolean
    reflectClass = (*env)->FindClass(env, "java/lang/Boolean");
    valueOf = (*env)->GetStaticMethodID(env, reflectClass, "valueOf",
					"(Z)Ljava/lang/Boolean;");
    result = (*env)->CallStaticObjectMethod(env, reflectClass, valueOf, iVal);
    break;
  default:  // jobject
    break;
  }
  return result;
}

void makeLocalVariable(JNIEnv *env, jthread thread, jint depth,
		       jclass localClass, jmethodID live, jmethodID dead,
		       jlocation location, jobjectArray locals,
		       jvmtiLocalVariableEntry *table, int index) {
  jstring name;
  jstring sig;
  jstring gensig;
  jobject value;
  jobject local;
  name = (*env)->NewStringUTF(env, table[index].name);
  sig = (*env)->NewStringUTF(env, table[index].signature);
  if (table[index].generic_signature) {
    gensig = (*env)->NewStringUTF(env, table[index].generic_signature);
  } else {
    gensig = NULL;
  }
  if (location >= table[index].start_location
      && location <= (table[index].start_location + table[index].length)) {
    value = getLocalValue(env, thread, depth, table, index);
    local = (*env)->NewObject(env, localClass, live,  name, sig, gensig, value);
  } else {
    local = (*env)->NewObject(env, localClass, dead,  name, sig, gensig);
  }
  (*env)->SetObjectArrayElement(env, locals, index, local);
}

jobject makeFrameObject(JNIEnv *env, jmethodID method, jobject this,
			jobjectArray locals, jint pos, jint lineno) {
  jvmtiError tiErr;
  jclass methodClass;
  jint modifiers;
  jobject frameMethod;
  jclass frameClass;
  jmethodID ctor;
  tiErr = (*(globalData->jvmti))->GetMethodDeclaringClass(globalData->jvmti,
							  method, &methodClass);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/RuntimeException", // TODO: better exception
		   "Could not get the declaring class of the method.");
    return NULL;
  }
  tiErr = (*(globalData->jvmti))->GetMethodModifiers(globalData->jvmti,
						     method, &modifiers);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/RuntimeException", // TODO: better exception
		   "Could not get the modifiers of the method.");
    return NULL;
  }
  frameMethod = (*env)->ToReflectedMethod(env, methodClass, method,
					  modifiers & ACC_STATIC);
  if (frameMethod == NULL) {
    return NULL; // ToReflectedMethod raised an exception
  }
  frameClass = (*env)->FindClass(env, "org/thobe/frame/Frame");
  if (frameClass == NULL) {
    return NULL;
  }
  ctor = (*env)->GetMethodID(env, frameClass, "<init>",
"(Ljava/lang/reflect/Method;Ljava/lang/Object;[Lorg/thobe/frame/Frame$LocalVariable;II)V");
  if (ctor == NULL) {
    return NULL;
  }
  return (*env)->NewObject(env, frameClass, ctor,
			   frameMethod, this, locals, pos, lineno);
}

jobject buildFrame(JNIEnv *env, jthread thread, jint depth, jboolean get_locals,
		   jmethodID method, jlocation location) {
  jvmtiError tiErr;
  jvmtiLocalVariableEntry *table;
  jvmtiLineNumberEntry* lnnotable;
  jint num_entries;
  jobject this;
  jobjectArray locals;
  jint lineno;
  jclass localClass;
  jmethodID liveCtor;
  jmethodID deadCtor;
  int i;
  this = NULL;
  if (get_locals) {
    tiErr = (*(globalData->jvmti))->GetLocalVariableTable(globalData->jvmti,
							  method,
							  &num_entries, &table);
  } else {
    // If the information wasn't requested, it's absent; handle as same case
    tiErr = JVMTI_ERROR_ABSENT_INFORMATION;
  }
  if (tiErr != JVMTI_ERROR_NONE) {
    locals = NULL;
    switch(tiErr) {
      // Pass cases
    case JVMTI_ERROR_ABSENT_INFORMATION:
    case JVMTI_ERROR_NATIVE_METHOD:
      break;
      // Error cases
    case JVMTI_ERROR_MUST_POSSESS_CAPABILITY:
      throwException(env, "java/lang/RuntimeException",
		     "access_local_variables capability not enabled.");
      return NULL;
    case JVMTI_ERROR_INVALID_METHODID:
      throwException(env, "java/lang/IllegalArgumentException",
		     "Illegal jmethodID.");
      return NULL;
    case JVMTI_ERROR_NULL_POINTER:
      throwException(env, "java/lang/NullPointerException",
		     "passed null to GetLocalVariableTable().");
      return NULL;
    default:
      throwException(env, "java/lang/RuntimeException", "Unknown JVMTI Error.");
      return NULL;
    }
  } else {
    localClass = (*env)->FindClass(env, "org/thobe/frame/Frame$LocalVariable");
    liveCtor = (*env)->GetMethodID(env, localClass, "<init>",
"(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/Object;)V");
    deadCtor = (*env)->GetMethodID(env, localClass, "<init>",
"(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V");
    locals = (*env)->NewObjectArray(env, num_entries, localClass, NULL);
    for (i = 0; i < num_entries; i++) {
      makeLocalVariable(env, thread, depth, localClass, liveCtor, deadCtor,
			location, locals, table, i);
    }
    (*(globalData->jvmti))->Deallocate(globalData->jvmti, table);
  }
  if (get_locals) {
    tiErr = (*(globalData->jvmti))->GetLocalObject(globalData->jvmti, thread,
						   depth, 0, &this);
    if (tiErr != JVMTI_ERROR_NONE) {
      this = NULL;
    }
  }
  tiErr = (*(globalData->jvmti))->GetLineNumberTable(globalData->jvmti, method,
						     &num_entries, &lnnotable);
  if (tiErr != JVMTI_ERROR_NONE) {
    lineno = -1; // Not retreived
  } else {
    for (i = 0; i < num_entries; i++) {
      if (location < lnnotable->start_location) break;
      lineno = lnnotable->line_number;
    }
    (*(globalData->jvmti))->Deallocate(globalData->jvmti, lnnotable);
  }
  return makeFrameObject(env, method, this, locals, location, lineno);
}

/*
 * Class:     org_thobe_frame_Frame
 * Method:    buildFrame
 * Signature: (I)Lorg/thobe/frame/Frame;
 *
 * Return the frame in the current thread at the specified depth.
 */
JNIEXPORT jobject JNICALL
Java_org_thobe_frame_Frame_buildFrame(JNIEnv *env, jclass cls, jint depth)
{
  jmethodID method;
  jlocation location;
  jvmtiError tiErr;
  tiErr = (*(globalData->jvmti))->GetFrameLocation(globalData->jvmti,
						   NULL, depth,
						   &method, &location);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/RuntimeException", // TODO: better exception
		   "Could not get the frame location");
    return NULL;
  }
  return buildFrame(env, NULL/*current thread*/, depth, JNI_TRUE,
		    method, location);
}

jobjectArray buildStackTraceFrames(JNIEnv *env, jthread thread,
				   jint startDepth, jboolean includeLocals)
{
  jclass resultClass;
  jint i;
  jvmtiFrameInfo* frames;
  jint count;
  jvmtiError tiErr;
  jobjectArray result;
  jobject frame;
  tiErr = (*(globalData->jvmti))->GetFrameCount(globalData->jvmti, thread, &i);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/RuntimeException",
		   "Could not get the frame count.");
    return NULL;
  }
  tiErr = (*(globalData->jvmti))->Allocate(globalData->jvmti,
					   i*sizeof(jvmtiFrameInfo), &frames);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/RuntimeException",
		   "Could not allocate frame buffer.");
    return NULL;
  }
  tiErr = (*(globalData->jvmti))->GetStackTrace(globalData->jvmti, thread,
						startDepth, i,
						frames, &count);
  if (tiErr != JVMTI_ERROR_NONE) {
    (*(globalData->jvmti))->Deallocate(globalData->jvmti, frames);
    throwException(env, "java/lang/RuntimeException",
		   "Could not get stack trace.");
    return NULL;
  }
  resultClass = (*env)->FindClass(env, "org/thobe/frame/Frame");
  result = (*env)->NewObjectArray(env, count, resultClass, NULL);
  if (result == NULL) {
    (*(globalData->jvmti))->Deallocate(globalData->jvmti, frames);
    return NULL; // OutOfMemory
  }
  for (i = 0; i < count; i++) {
    frame = buildFrame(env, thread, startDepth + i, includeLocals,
		       frames[i].method, frames[i].location);
    if (frame == NULL) {
      (*(globalData->jvmti))->Deallocate(globalData->jvmti, frames);
      throwException(env, "java/lang/RuntimeException",
		     "Error accessing frame object.");
      return NULL;
    }
    (*env)->SetObjectArrayElement(env, result, i, frame);
  }
  (*(globalData->jvmti))->Deallocate(globalData->jvmti, frames); 
  return result;
}

/*
 * Class:     org_thobe_frame_Frame
 * Method:    buildStackTraceFrames
 * Signature: (I)[Lorg/thobe/frame/Frame;
 *
 * Return the entire stack trace of frames for the current thread.
 */
JNIEXPORT jobjectArray JNICALL
Java_org_thobe_frame_Frame_buildStackTraceFrames(JNIEnv *env,
						 jclass resultClass,
						 jint startDepth)
{
  return buildStackTraceFrames(env, NULL, startDepth, JNI_TRUE);
}

jobjectArray buildStackTraces(JNIEnv *env,
			      jvmtiStackInfo* stacks, jint num_threads) {
  jclass frameCls;
  jclass traceCls;
  jmethodID traceCtor;
  jint i, j;
  jobjectArray frames;
  jobject frame;
  jobject trace;
  jobjectArray result;

  frameCls = (*env)->FindClass(env, "org/thobe/frame/Frame");
  traceCls = (*env)->FindClass(env, "org/thobe/frame/Frame$ThreadFrames");
  traceCtor = (*env)->GetMethodID(env, traceCls, "<init>",
		      "(Ljava/lang/Thread;[Lorg/thobe/frame/Frame;)V");

  result = (*env)->NewObjectArray(env, num_threads, traceCls, NULL);
  if (result == NULL) {
    return NULL; // OutOfMemory
  }
  for (i = 0; i < num_threads; i++) {
    frames = (*env)->NewObjectArray(env, stacks[i].frame_count, frameCls, NULL);
    if (frames == NULL) {
      return NULL; // OutOfMemory
    }
    for (j = 0; j < stacks[i].frame_count; j++) {
      frame = buildFrame(env, stacks[i].thread, j, JNI_FALSE,
			 stacks[i].frame_buffer[j].method,
			 stacks[i].frame_buffer[j].location);
      if (frame == NULL) {
	return NULL; // Exception
      }
      (*env)->SetObjectArrayElement(env, frames, j, frame);
    }
    trace = (*env)->NewObject(env,traceCls,traceCtor, stacks[i].thread, frames);
    if (trace == NULL) {
      return NULL; // OutOfMemory
    }
    (*env)->SetObjectArrayElement(env, result, i, trace);
  }
  return result;
}

/*
 * Class:     org_thobe_frame_Frame_ThreadFrames
 * Method:    buildStackTraceFrames
 * Signature: (I)[Lorg/thobe/frame/Frame$ThreadFrames;
 *
 * Return the entire stack trace of frames for all active threads.
 */
JNIEXPORT jobjectArray JNICALL
Java_org_thobe_frame_Frame_00024ThreadFrames_buildStackTraceFrames(JNIEnv *env,
								   jclass cls,
								   jint depth)
{
  jint num_threads;
  jvmtiStackInfo* stacks;
  jobjectArray result;
  jvmtiError tiErr;
  tiErr = (*(globalData->jvmti))->GetAllStackTraces(globalData->jvmti, depth,
						    &stacks, &num_threads);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/RuntimeException",
		   "Could not access thread states.");
    return NULL;
  }
  result = buildStackTraces(env, stacks, num_threads);
  (*(globalData->jvmti))->Deallocate(globalData->jvmti, stacks);
  return result;
}

/*
 * Class:     org_thobe_frame_Frame_ThreadFrames
 * Method:    buildStackTraceFramesFor
 * Signature: ([Ljava/lang/Thread;I)[Lorg/thobe/frame/Frame$ThreadFrames;
 *
 * Return the entire stack trace of the frames for the specified threads.
 */
JNIEXPORT jobjectArray JNICALL
Java_org_thobe_frame_Frame_00024ThreadFrames_buildStackTraceFramesFor
(JNIEnv *env, jclass cls, jobjectArray threads, jint depth)
{
  jsize num_threads;
  jsize i;
  jthread *thread_list;
  jvmtiStackInfo* stacks;
  jobjectArray result;
  jvmtiError tiErr;
  num_threads = (*env)->GetArrayLength(env, threads);
  tiErr = (*(globalData->jvmti))->Allocate(globalData->jvmti,
					   num_threads*sizeof(jthread),
					   &thread_list);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/OutOfMemoryError",
		   "Could not allocate thread list.");
    return NULL;
  }
  for (i = 0; i < num_threads; i++) {
    thread_list[i] = (jthread)(*env)->GetObjectArrayElement(env, threads, i);
  }
  tiErr = (*(globalData->jvmti))->GetThreadListStackTraces(globalData->jvmti,
							   num_threads,
							   thread_list, depth,
							   &stacks);
  (*(globalData->jvmti))->Deallocate(globalData->jvmti, thread_list);
  if (tiErr != JVMTI_ERROR_NONE) {
    throwException(env, "java/lang/RuntimeException",
		   "Could not access thread states.");
    return NULL;
  }
  result = buildStackTraces(env, stacks, num_threads);
  (*(globalData->jvmti))->Deallocate(globalData->jvmti, stacks);
  return result;
}
