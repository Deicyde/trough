---
declaration: definition
origin: cited
lean: Verifier.StateFunction.liftContext, Verifier.KnowledgeStateFunction.liftContext
statement: formalized
---

# State Function Lifting

The lifted state function holds when the outer input statement is in its language or the inner state function holds at the projected statement.

The lifted knowledge state function carries a pair of witnesses: the outer output witness and the current inner witness. It holds when the inner knowledge state function holds at the projected statement for the carried inner witness, or when every inner input witness lifts, using the carried outer output witness and the inverse witness lens, to a valid outer input witness. The second disjunct is the shortcut of the knowledge-soundness lens condition; it is not membership of the outer statement in a language.

## Depends on

- [State Function](../../definitions/part-02/def-state-function.md)
- [Knowledge State Function](../../definitions/part-02/def-knowledge-state-function.md)
- [Statement Lens](../part-01/def-statement-lens.md)

## Lean

Formalized as [`Verifier.StateFunction.liftContext`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.StateFunction.liftContext), [`Verifier.KnowledgeStateFunction.liftContext`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.KnowledgeStateFunction.liftContext).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 482](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L482)
