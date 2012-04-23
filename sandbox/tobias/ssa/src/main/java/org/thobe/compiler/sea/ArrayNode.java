package org.thobe.compiler.sea;

import java.util.Arrays;

final class ArrayNode extends ValueNode {
    private final Value[] content;

    ArrayNode(Value[] content) {
        this.content = content;
    }

    @Override
    public Value result() {
        throw new UnsupportedOperationException("Not implemented");
    }

    @Override
    Node accept(GraphTraverser traverser) {
        return traverser.array(this, content).traverse(traverser);
    }

    @Override
    public String toString() {
        return "Array:[" + Arrays.toString(content) + "]";
    }
}
