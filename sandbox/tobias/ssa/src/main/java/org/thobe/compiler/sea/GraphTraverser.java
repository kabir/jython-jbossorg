package org.thobe.compiler.sea;

abstract class GraphTraverser {
    abstract class SelectTraverser {
        abstract void onCase(Integer key, Node node);

        abstract void otherwise(Node node);

        abstract Node done();
    }

    abstract SelectTraverser select(SwitchNode original, Value select);

    abstract Node selection(IfNode original, Value predicate,
            Node trueSuccessor, Node falseSuccessor);

    abstract Node returnValue(ReturnNode original, Value value);

    abstract Node store(StoreNode original, Variable variable, Value value);

    abstract Node raiseException(ThrowNode original,
            ExceptionValue exception);

    abstract Node invoke(InvocationNode original,
            InvocationType invocation, Value[] arguments);

    abstract Node load(LoadNode original, Variable variable);

    abstract Node phi(PhiNode original, Node[] array);

    abstract Node array(ArrayNode original, Value[] content);
}
