package java.dyn;

import java.lang.reflect.Method;

public class MethodHandles {
    private MethodHandles() {
    }

    public static MethodHandle unreflect(Method reflected) {
        return new MethodHandle(reflected);
    }
}
