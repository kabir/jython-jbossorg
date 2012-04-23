package org.thobe.compiler.sea;

public class ExceptionValue extends Value {
    ExceptionValue() {
        super(null);
        throw new UnsupportedOperationException(
                "How should exceptions be created?");
    }
}
