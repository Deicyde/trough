---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: NormSMulClass.toIsBoundedSMul
mathlib_file: Mathlib/Analysis/Normed/MulAction.lean
---

# Topology on a normed vector space

Mathlib states this as `NormSMulClass.toIsBoundedSMul`.

```lean
NormSMulClass.toIsBoundedSMul.{u_1, u_2} {α : Type u_1} {β : Type u_2} [SeminormedRing α]
  [SeminormedAddCommGroup β] [_root_.Module α β] [NormSMulClass α β] : IsBoundedSMul α β
```

## Depends on

- [Bornology](../topological-vector-spaces/bornology.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../topology/uniform-notions/uniform-space.md)

## Proof depends on

- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Ordered ring](../../general-algebra/rings/ordered-ring.md)
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Product of rings](../../../undergraduate/ring-theory/fundamentals/product-of-rings.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure-z.md)

## Sources

- [Mathlib documentation: `NormSMulClass.toIsBoundedSMul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/MulAction.html#NormSMulClass.toIsBoundedSMul)
- [Source of `NormSMulClass.toIsBoundedSMul` in Mathlib/Analysis/Normed/MulAction.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/MulAction.lean#L162)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L280)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L423)
