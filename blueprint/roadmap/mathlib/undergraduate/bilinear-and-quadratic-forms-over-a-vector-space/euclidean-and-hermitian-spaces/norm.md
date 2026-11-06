# Norm

(Semi)norm constructed from a `PreInnerProductSpace.Core` structure, defined to be the square
root of the scalar product.

```lean
InnerProductSpace.Core.toNorm.{u_1, u_3} {𝕜 : Type u_1} {F : Type u_3} [RCLike 𝕜] [AddCommGroup F]
  [_root_.Module 𝕜 F] [c : PreInnerProductSpace.Core 𝕜 F] : Norm F
```

## Depends on

- [Associative algebra over a commutative ring](../../../overview/general-algebra/algebras-over-a-ring/associative-algebra-over-a-commutative-ring.md)
- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Metric space](../../../overview/topology/metric-spaces/metric-space.md)

## Sources

- [Mathlib documentation: `InnerProductSpace.Core.toNorm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Defs.html#InnerProductSpace.Core.toNorm)
- [Source of `InnerProductSpace.Core.toNorm` in Mathlib/Analysis/InnerProductSpace/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Defs.lean#L376)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Euclidean and Hermitian spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L220)
