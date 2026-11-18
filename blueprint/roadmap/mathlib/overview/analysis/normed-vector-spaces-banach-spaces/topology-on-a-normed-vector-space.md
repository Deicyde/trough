# Topology on a normed vector space

Mathlib states this as `NormSMulClass.toIsBoundedSMul`.

```lean
NormSMulClass.toIsBoundedSMul.{u_1, u_2} {α : Type u_1} {β : Type u_2} [SeminormedRing α]
  [SeminormedAddCommGroup β] [_root_.Module α β] [NormSMulClass α β] : IsBoundedSMul α β
```

## Depends on

- [Bornology](../topological-vector-spaces/bornology.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Order](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)

## Sources

- [Mathlib documentation: `NormSMulClass.toIsBoundedSMul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/MulAction.html#NormSMulClass.toIsBoundedSMul)
- [Source of `NormSMulClass.toIsBoundedSMul` in Mathlib/Analysis/Normed/MulAction.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/Normed/MulAction.lean#L182)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L280)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L423)
