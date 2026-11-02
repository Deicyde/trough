---
declaration: class
origin: cited
mathlib: true
mathlib_declaration: NormedAddTorsor
mathlib_file: Mathlib/Analysis/Normed/Group/AddTorsor.lean
---

# Euclidean affine space

A `NormedAddTorsor V P` is a torsor of an additive seminormed group
action by a `SeminormedAddCommGroup V` on points `P`. We bundle the pseudometric space
structure and require the distance to be the same as results from the
norm (which in fact implies the distance yields a pseudometric space, but
bundling just the distance and using an instance for the pseudometric space
results in type class problems).

```lean
NormedAddTorsor.{u_1, u_2} (V : outParam (Type u_1)) (P : Type u_2) [SeminormedAddCommGroup V]
  [PseudoMetricSpace P] : Type (max u_1 u_2)
```

## Depends on

- [Affine space](affine-space.md)
- [Bornology](../../analysis/topological-vector-spaces/bornology.md)
- [Order (Real numbers)](../../../undergraduate/single-variable-real-analysis/real-numbers/order.md)
- [Uniform space](../../topology/uniform-notions/uniform-space.md)

## Sources

- [Mathlib documentation: `NormedAddTorsor`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Group/AddTorsor.html#NormedAddTorsor)
- [Source of `NormedAddTorsor` in Mathlib/Analysis/Normed/Group/AddTorsor.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Normed/Group/AddTorsor.lean#L31)
- [Mathlib overview: Geometry › Affine and Euclidean geometry](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L436)
