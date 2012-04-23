package org.thobe.compiler.sea;

public abstract class VariableFactory {
    VariableFactory() {
    }

    public abstract void createLocalVariable(String local);

    public abstract void createCellVariable(String var);

    public abstract void createParameter(String param);
}
