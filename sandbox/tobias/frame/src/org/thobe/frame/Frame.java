/*
 * JVM Call Frame Introspection Library Copyright (c) 2008 Tobias Ivarsson
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
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
package org.thobe.frame;

import java.lang.reflect.Method;
import java.lang.reflect.Modifier;
import java.util.Collections;
import java.util.Map;
import java.util.HashMap;

public final class Frame {
    public static boolean isAvailable() {
        return active;
    }

    // Construction
    public static Frame getFrame(int depth) {
        if (!active) {
            throw new UnsupportedOperationException();
        }
        return buildFrame(depth + 2);
    }

    public static Frame[] getFrames() {
        if (!active) {
            throw new UnsupportedOperationException();
        }
        return buildStackTraceFrames(2);
    }

    public static ThreadFrames[] getAllThreadsFrames(int maxDepth) {
        if (!active) {
            throw new UnsupportedOperationException();
        }
        return ThreadFrames.buildStackTraceFrames(maxDepth);
    }

    public static ThreadFrames[] getThreadsFrames(int maxDepth,
            Thread... threads) {
        if (!active) {
            throw new UnsupportedOperationException();
        }
        return ThreadFrames.buildStackTraceFramesFor(threads, maxDepth);
    }

    // Content access
    public Method getMethod() {
        return method;
    }

    public boolean isNative() {
        return (method.getModifiers() & Modifier.NATIVE) != 0;
    }

    public boolean couldLocalsBeLoaded() {
        return locals != null;
    }

    public Object getThis() {
        if ((method.getModifiers() & Modifier.STATIC) != 0) {
            return null;
        }
        return localThis;
    }

    public String getName(int offset) {
        if (locals == null) {
            throw new RuntimeException("Frame has no accessible locals.");
        }
        if (locals[offset] != null) {
            return locals[offset].name;
        } else {
            throw new IllegalArgumentException("Local variable " + offset
                    + " is not live.");
        }
    }

    public boolean hasLiveLocal(String name) {
        return namedLocals.containsKey(name);
    }

    public String getSignature(int offset) {
        if (locals == null) {
            throw new RuntimeException("Frame has no accessible locals.");
        }
        if (locals[offset] != null) {
            return locals[offset].signature;
        } else {
            throw new IllegalArgumentException("Local variable " + offset
                    + " is not live.");
        }
    }

    public String getSignature(String name) {
        if (locals == null) {
            throw new RuntimeException("Frame has no accessible locals.");
        }
        LocalVariable local = namedLocals.get(name);
        if (local != null) {
            return local.signature;
        } else {
            throw new IllegalArgumentException("No live local variable named "
                    + name);
        }
    }

    public String getGenericSignature(int offset) {
        if (locals == null) {
            throw new RuntimeException("Frame has no accessible locals.");
        }
        if (locals[offset] != null) {
            return locals[offset].generic_signature;
        } else {
            throw new IllegalArgumentException("Local variable " + offset
                    + " is not live.");
        }
    }

    public String getGenericSignature(String name) {
        if (locals == null) {
            throw new RuntimeException("Frame has no accessible locals.");
        }
        LocalVariable local = namedLocals.get(name);
        if (local != null) {
            return local.generic_signature;
        } else {
            throw new IllegalArgumentException("No live local variable named "
                    + name);
        }
    }

    public int getLocalsCount() {
        return locals != null ? locals.length : 0;
    }

    public boolean isLocalLive(int offset) {
        if (locals == null) {
            throw new RuntimeException("Frame has no accessible locals.");
        }
        return locals[offset].live;
    }

    public Object getLocal(int offset) {
        if (locals == null) {
            throw new RuntimeException("Frame has no accessible locals.");
        }
        if (locals[offset] != null) {
            return locals[offset].value;
        } else {
            throw new IllegalArgumentException("Local variable " + offset
                    + " is not live.");
        }
    }

    public Object getLocal(String name) {
        return null;
    }

    public Iterable<String> getLocalNames() {
        return Collections.unmodifiableSet(namedLocals.keySet());
    }

    public boolean hasLineNumber() {
        return linenumber > -1;
    }

    public int getLineNumber() {
        if (isNative()) {
            throw new RuntimeException(
                    "Cannot get line number from frame of native method.");
        } else {
            return linenumber;
        }
    }

    public int getLocation() {
        if (isNative()) {
            throw new RuntimeException(
                    "Cannot get line number from frame of native method.");
        } else {
            return location;
        }
    }

    public static final class ThreadFrames {
        private final Thread thread;
        private final Frame[] frames;

        public Thread getThread() {
            return thread;
        }

        public boolean hasStack() {
            return frames != null;
        }

        public int getStackDepth() {
            return frames == null ? 0 : frames.length;
        }

        public Frame getFrame(int depth) {
            return frames[depth];
        }

        private ThreadFrames(Thread thread, Frame[] frames) {
            this.thread = thread;
            this.frames = frames;
        }

        private static native ThreadFrames[] buildStackTraceFrames(int maxDepth);

        private static native ThreadFrames[] buildStackTraceFramesFor(
                Thread[] threads, int maxDepth);
    }

    private final Method method;
    private final Object localThis;
    private final LocalVariable[] locals;
    private final int location;
    private final int linenumber;
    private final Map<String, LocalVariable> namedLocals = new HashMap<String, LocalVariable>();

    private Frame(Method method, Object localThis, LocalVariable[] locals,
            int pos, int lineno) {
        this.method = method;
        this.localThis = localThis;
        this.locals = locals;
        this.location = pos;
        this.linenumber = lineno;
        if (locals != null) {
            for (LocalVariable local : locals) {
                if (local != null) {
                    namedLocals.put(local.name, local);
                }
            }
        }
    }

    private static final class LocalVariable {
        final boolean live;
        final String name;
        final String signature;
        final String generic_signature;
        final Object value;

        private LocalVariable(String name, String signature,
                String generic_signature, Object value) {
            this.live = true;
            this.name = name;
            this.signature = signature;
            this.generic_signature = generic_signature;
            this.value = value;
        }

        private LocalVariable(String name, String signature,
                String generic_signature) {
            this.live = false;
            this.name = name;
            this.signature = signature;
            this.generic_signature = generic_signature;
            this.value = null;
        }
    }

    private static native Frame buildFrame(int depth);

    private static native Frame[] buildStackTraceFrames(int startDepth);

    private static native boolean setupNative();

    private static final String NATIVE_LIBRARY_NAME = "frameintrospect";
    private static final boolean active;

    static {
        System.loadLibrary(NATIVE_LIBRARY_NAME);
        active = setupNative();
    }
}
