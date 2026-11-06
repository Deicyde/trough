# Continuous linear map

Continuous linear maps between modules. We only put the type classes that are necessary for the
definition, although in applications `M` and `M₂` will be topological modules over the topological
ring `R`.

```lean
ContinuousLinearMap.{u_1, u_2, u_3, u_4} {R : Type u_1} {S : Type u_2} [Semiring R] [Semiring S]
  (σ : R →+* S) (M : Type u_3) [TopologicalSpace M] [AddCommMonoid M] (M₂ : Type u_4)
  [TopologicalSpace M₂] [AddCommMonoid M₂] [_root_.Module R M] [_root_.Module S M₂] :
  Type (max u_3 u_4)
```

## Depends on

- [Continuous function](../general-topology/part-01/continuous-function.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `ContinuousLinearMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/ContinuousLinearMap/Basic.html#ContinuousLinearMap)
- [Source of `ContinuousLinearMap` in Mathlib/Topology/Algebra/Module/ContinuousLinearMap/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Module/ContinuousLinearMap/Basic.lean#L57)
- [Mathlib overview: Topology › Topological algebra](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L257)
- [Mathlib undergraduate list: Topology › Normed vector spaces on $\R$ and $\C$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L429)
