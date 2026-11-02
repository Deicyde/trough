---
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: WeakBilin.instTopologicalSpace
mathlib_file: Mathlib/Topology/Algebra/Module/Spaces/WeakBilin.lean
---

# Weak-* topology for dualities

Mathlib states this as `WeakBilin.instTopologicalSpace`.

```lean
WeakBilin.instTopologicalSpace.{u_2, u_4, u_5} {𝕜 : Type u_2} {E : Type u_4} {F : Type u_5}
  [TopologicalSpace 𝕜] [CommSemiring 𝕜] [AddCommMonoid E] [_root_.Module 𝕜 E] [AddCommMonoid F]
  [_root_.Module 𝕜 F] (B : E →ₗ[𝕜] F →ₗ[𝕜] 𝕜) : TopologicalSpace (WeakBilin B)
```

## Depends on

- [Associative algebra over a commutative ring](../../general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Induced topology](../../topology/general-topology/part-01/induced-topology.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `WeakBilin.instTopologicalSpace`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Topology/Algebra/Module/Spaces/WeakBilin.html#WeakBilin.instTopologicalSpace)
- [Source of `WeakBilin.instTopologicalSpace` in Mathlib/Topology/Algebra/Module/Spaces/WeakBilin.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Topology/Algebra/Module/Spaces/WeakBilin.lean#L93)
- [Mathlib overview: Analysis › Topological vector spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L276)
