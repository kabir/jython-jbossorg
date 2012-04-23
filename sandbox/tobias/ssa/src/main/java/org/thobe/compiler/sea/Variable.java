package org.thobe.compiler.sea;

public abstract class Variable {
    private final String name;

    Variable(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + "[" + name + "]";
    }
}
