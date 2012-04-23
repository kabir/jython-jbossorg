package java.dyn;

public interface InterfaceImplementor {
    MethodHandle getImplementation(String name, MethodType type);
}
