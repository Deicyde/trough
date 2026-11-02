---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: inner_mul_inner_self_le, norm_inner_le_norm
mathlib_file: Mathlib/Analysis/InnerProductSpace/Basic.lean
---

# Cauchy-Schwarz inequality

Mathlib records this with 2 declarations.

`inner_mul_inner_self_le`: **Cauchy–Schwarz inequality**.

```lean
inner_mul_inner_self_le.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [SeminormedAddCommGroup E] [InnerProductSpace 𝕜 E] (x y : E) :
  ‖inner 𝕜 x y‖ * ‖inner 𝕜 y x‖ ≤ RCLike.re (inner 𝕜 x x) * RCLike.re (inner 𝕜 y y)
```

`norm_inner_le_norm`: Cauchy–Schwarz inequality with norm

```lean
norm_inner_le_norm.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [SeminormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] (x y : E) : ‖inner 𝕜 x y‖ ≤ ‖x‖ * ‖y‖
```

## Depends on

- [Inner product space, over $R$ or $C$](inner-product-space-over-r-or-c.md)

## Proof depends on

- [Ball](../../topology/metric-spaces/ball.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Finite set](../../data-structures/sets/finite-set.md)
- [Group](../../general-algebra/group-theory/part-01/group.md)
- [Homeomorphisms](../../../undergraduate/topology/topology-and-metric-spaces/homeomorphisms.md)
- [Invertible elements](../../../undergraduate/ring-theory/divisibility-in-integral-domains/invertible-elements.md)
- [Norm](../../../undergraduate/bilinear-and-quadratic-forms-over-a-vector-space/euclidean-and-hermitian-spaces/norm.md)
- [Order topology](../../topology/topological-algebra/order-topology.md)
- [Product of rings](../../../undergraduate/ring-theory/fundamentals/product-of-rings.md)
- [Ring structure $\Z$](../../../undergraduate/ring-theory/fundamentals/ring-structure.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topological ring](../../topology/topological-algebra/topological-ring.md)

## Sources

- [Mathlib documentation: `inner_mul_inner_self_le`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Basic.html#inner_mul_inner_self_le)
- [Source of `inner_mul_inner_self_le` in Mathlib/Analysis/InnerProductSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Basic.lean#L279)
- [Mathlib documentation: `norm_inner_le_norm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/InnerProductSpace/Basic.html#norm_inner_le_norm)
- [Source of `norm_inner_le_norm` in Mathlib/Analysis/InnerProductSpace/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/InnerProductSpace/Basic.lean#L454)
- [Mathlib overview: Analysis › Hilbert spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L295)
- [Mathlib undergraduate list: Bilinear and Quadratic Forms Over a Vector Space › Euclidean and Hermitian spaces](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L219)
- [Freek Wiedijk's 100 theorems, no. 78](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/100.yaml#L395)
