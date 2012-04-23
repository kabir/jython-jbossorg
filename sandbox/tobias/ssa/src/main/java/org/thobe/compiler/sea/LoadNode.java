package org.thobe.compiler.sea;

class LoadNode extends ValueNode {
    private final Variable variable;

    LoadNode(Variable variable) {
        this.variable = variable;
    }

    private StoreNode defined;
    private final Value result = new Value(this) {
    };

    @Override
    public Value result() {
        return result;
    }

    @Override
    Node accept(GraphTraverser traverser) {
        return traverser.load(this, variable).traverse(traverser);
    }

    @Override
    public String toString() {
        return "LoadNode[" + variable + "]";
    }
}
