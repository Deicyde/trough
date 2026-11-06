# Topological vector bundle

The space `Bundle.TotalSpace F E` (for `E : B → Type*` such that each `E x` is a topological
vector space) has a topological vector space structure with fiber `F` (denoted with
`VectorBundle R F E`) if around every point there is a fiber bundle trivialization which is linear
in the fibers.

```lean
VectorBundle.{u_1, u_2, u_3, u_4} (R : Type u_1) {B : Type u_2} (F : Type u_3) (E : B → Type u_4)
  [NontriviallyNormedField R] [(x : B) → AddCommMonoid (E x)] [(x : B) → _root_.Module R (E x)]
  [NormedAddCommGroup F] [NormedSpace R F] [TopologicalSpace B]
  [TopologicalSpace (Bundle.TotalSpace F E)] [(x : B) → TopologicalSpace (E x)] [FiberBundle F E] :
  Prop
```

## Depends on

- [Continuous linear map](../../topological-algebra/continuous-linear-map.md)
- [Normed vector space over a normed field](../../../analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Topological fiber bundle](topological-fiber-bundle.md)

## Sources

- [Mathlib documentation: `VectorBundle`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/VectorBundle/Basic.html#VectorBundle)
- [Source of `VectorBundle` in Mathlib/Topology/VectorBundle/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/VectorBundle/Basic.lean#L371)
- [Mathlib overview: Topology › General topology](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L234)
