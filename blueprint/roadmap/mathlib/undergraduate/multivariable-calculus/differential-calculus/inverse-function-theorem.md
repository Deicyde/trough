---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: HasStrictDerivAt.to_localInverse
mathlib_file: Mathlib/Analysis/Calculus/InverseFunctionTheorem/Deriv.lean
---

# Inverse function theorem

Mathlib states this as `HasStrictDerivAt.to_localInverse`.

```lean
HasStrictDerivAt.to_localInverse.{u_1} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] [CompleteSpace 𝕜]
  {f : 𝕜 → 𝕜} {f' a : 𝕜} (hf : HasStrictDerivAt f f' a) (hf' : f' ≠ 0) :
  HasStrictDerivAt (HasStrictDerivAt.localInverse f f' a hf hf') f'⁻¹ (f a)
```

## Depends on

- [Completeness](../../../overview/topology/uniform-notions/completeness.md)
- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)
- [Field $\R$ of real numbers](../../ring-theory/field-theory/part-01/field-of-real-numbers.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Normed vector space over a normed field](../../../overview/analysis/normed-vector-spaces-banach-spaces/normed-vector-space-over-a-normed-field.md)
- [Ordered ring](../../../overview/general-algebra/rings/ordered-ring.md)
- [Ring structure $\Z$](../../ring-theory/fundamentals/ring-structure.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)
- [Topological ring](../../../overview/topology/topological-algebra/topological-ring.md)

## Proof depends on

- [Inverse function theorem](../../../overview/analysis/differentiability/inverse-function-theorem.md)

## Sources

- [Mathlib documentation: `HasStrictDerivAt.to_localInverse`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/InverseFunctionTheorem/Deriv.html#HasStrictDerivAt.to_localInverse)
- [Source of `HasStrictDerivAt.to_localInverse` in Mathlib/Analysis/Calculus/InverseFunctionTheorem/Deriv.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Calculus/InverseFunctionTheorem/Deriv.lean#L50)
- [Mathlib undergraduate list: Multivariable calculus › Differential calculus](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L473)
