package java.dyn;

public abstract class InterfaceInjector {
    protected abstract InterfaceImplementor inject(Class<?> iface,
            Class<?> target);
}
