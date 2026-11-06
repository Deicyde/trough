# Dual of a normed space

The *strong dual* of a topological vector space `M` over a ring `R`. This is the space of
continuous linear functionals and is equipped with the topology of uniform convergence
on bounded subsets. `StrongDual R M` is an abbreviation for `M →L[R] R`.

```lean
StrongDual.{u_1, u_2} (R : Type u_1) [Semiring R] [TopologicalSpace R] (M : Type u_2)
  [TopologicalSpace M] [AddCommMonoid M] [_root_.Module R M] : Type (max u_1 u_2)
```

## Depends on

- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)

## Sources

- [Mathlib documentation: `StrongDual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/ContinuousLinearMap/Basic.html#StrongDual)
- [Source of `StrongDual` in Mathlib/Topology/Algebra/Module/ContinuousLinearMap/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Module/ContinuousLinearMap/Basic.lean#L93)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L289)
- [Mathlib undergraduate list: Topology › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L440)
