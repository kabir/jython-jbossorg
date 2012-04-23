package org.thobe.mlvm.test.inti;

import java.dyn.InterfaceImplementor;
import java.dyn.InterfaceInjector;
import java.dyn.MethodHandle;
import java.dyn.MethodHandles;
import java.dyn.MethodType;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.Arrays;

import junit.framework.Assert;

import org.junit.Test;
import org.objectweb.asm.ClassVisitor;
import org.objectweb.asm.ClassWriter;
import org.objectweb.asm.MethodVisitor;
import org.objectweb.asm.Opcodes;
import org.objectweb.asm.Type;

public class GeneratedTests {
    private static final int V1_7 = Opcodes.V1_6;
    private static final int ACC_INJECTABLE = Opcodes.ACC_VOLATILE;

    private static class Loader extends ClassLoader {
        private static final Loader instance = new Loader();

        public static Class<?> load(ClassData data) {
            return instance.defineClass(data.name, data.bytes, 0,
                    data.bytes.length);
        }
    }

    private static abstract class ClassData {
        private static final int WRITER_FLAGS = 0;
        final String name;
        final byte[] bytes;

        public ClassData(String name, int access, Class<?>... interfaces) {
            this.name = GeneratedTests.class.getPackage().getName() + "."
                    + name;
            String[] ifaces;
            if (interfaces == null || interfaces.length == 0) {
                ifaces = null;
            } else {
                ifaces = new String[interfaces.length];
                for (int i = 0; i < interfaces.length; i++) {
                    ifaces[i] = Type.getInternalName(interfaces[i]);
                }
            }
            ClassWriter result = new ClassWriter(WRITER_FLAGS);
            result.visit(V1_7, access, this.name.replace('.', '/'), null,
                    "java/lang/Object", ifaces);
            generate(result);
            result.visitEnd();
            this.bytes = result.toByteArray();
        }

        abstract void generate(ClassVisitor cls);
    }

    static final InterfaceInjector INJECTOR = new InterfaceInjector() {
        @Override
        protected InterfaceImplementor inject(Class<?> iface,
                final Class<?> target) {
            System.out.println("Attempting to inject " + iface + " into "
                    + target);
            return new InterfaceImplementor() {
                public MethodHandle getImplementation(String name,
                        MethodType type) {
                    System.out.println("Injecting method " + name);
                    try {
                        Method injectedMethod = GeneratedTests.class.getMethod(
                                "injectedTarget", target);
                        return MethodHandles.unreflect(injectedMethod);
                    } catch (Exception e) {
                        return null;
                    }
                }
            };
        }
    };
    private static volatile boolean invoked;

    /* Can be injected into String */
    public static void injectedTarget(String s) {
        invoked = true;
    }

    private static final Class<?> INJECTABLE = Loader.load(new ClassData(
            "InjectableInterface", Opcodes.ACC_INTERFACE + ACC_INJECTABLE) {
        @Override
        void generate(ClassVisitor cls) {
            // Class initializer
            generateSetInjector(cls.visitMethod(Opcodes.ACC_PUBLIC
                    + Opcodes.ACC_STATIC, "<clinit>", "()V", null, null));
            // interface method to be injected
            cls.visitMethod(Opcodes.ACC_PUBLIC + Opcodes.ACC_ABSTRACT,
                    "injectedMethod", "()V", null, null).visitEnd();
        }

        private void generateSetInjector(MethodVisitor clinit) {
            Type injector = Type.getType(InterfaceInjector.class);
            clinit.visitCode();
            clinit.visitFieldInsn(Opcodes.GETSTATIC,
                    Type.getInternalName(GeneratedTests.class), "INJECTOR",
                    injector.getInternalName());
            clinit.visitMethodInsn(Opcodes.INVOKESTATIC,
                    injector.getInternalName(), "setInjector", "("
                            + injector.getDescriptor() + ")V");
            clinit.visitMaxs(1, 0);
            clinit.visitEnd();
        }
    });

    private static final Class<?> TEST_EXECUTOR = Loader.load(new ClassData(
            "TestExecutor", 0) {
        @Override
        void generate(ClassVisitor cls) {
            for (Method m : GeneratedTests.class.getDeclaredMethods()) {
                if (m.isAnnotationPresent(Test.class)) {
                    MethodVisitor mv = cls.visitMethod(Opcodes.ACC_STATIC
                            + Opcodes.ACC_PUBLIC, m.getName(),
                            "(Ljava/lang/Object;)V", null, null);
                    try {
                        Method generator = GeneratedTests.class.getMethod(
                                "generate_" + m.getName(), MethodVisitor.class);
                        generator.invoke(null, mv);
                    } catch (Exception e) {
                        generateDefaultTestBody(mv);
                    }
                }
            }
        }

        private void generateDefaultTestBody(MethodVisitor mv) {
            mv.visitCode();
            mv.visitMaxs(0, 0);
            mv.visitEnd();
        }
    });

    @Test
    public void testInvokeInterface() throws Exception {
        performTest(true, "Invoke injected interface on java.lang.String");
    }

    public static void generate_testInvokeInterface(MethodVisitor mv) {
        mv.visitCode();
        mv.visitVarInsn(Opcodes.AALOAD, 0);
        mv.visitMethodInsn(Opcodes.INVOKEINTERFACE,
                Type.getInternalName(INJECTABLE), "injectedMethod", "()V");
        mv.visitMaxs(0, 0);
        mv.visitEnd();
    }

    @Test
    public void testCast() throws Exception {

    }

    @Test
    public void testIsInstance() throws Exception {

    }

    @Test
    public void testInjectIntoArray() throws Exception {

    }

    @Test
    public void testFailedInjection() throws Exception {

    }

    @Test
    public void testNestedInjection() throws Exception {
        // requires custom injector
    }

    @Test
    public void testExceptionInInjection() throws Exception {
        // requires custom injector
    }

    private static void performTest(boolean invocationExpected, Object arg)
            throws Exception {
        String testName = new Exception().getStackTrace()[1].getMethodName();
        Method testMethod = TEST_EXECUTOR.getMethod(testName, Object.class);
        System.out.println("Executing " + testName);
        invoked = false;
        try {
            testMethod.invoke(null, arg);
        } catch (InvocationTargetException e) {
            throw (Exception) e.getCause();
        } finally {
            System.out.println();
        }
        if (invocationExpected) {
            Assert.assertTrue(
                    "Expected invocation of injected method not performed",
                    invoked);
        } else {
            Assert.assertFalse("Unexpected invocation of injected method",
                    invoked);
        }
    }

}
