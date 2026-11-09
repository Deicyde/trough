# Banach-Steinhaus theorem

This is the standard Banach-Steinhaus theorem, or Uniform Boundedness Principle.
If a family of continuous linear maps from a Banach space into a normed space is pointwise
bounded, then the norms of these linear maps are uniformly bounded.

See also `WithSeminorms.banach_steinhaus` for the general statement in barrelled spaces.

```lean
banach_steinhaus.{u_1, u_2, u_3, u_4, u_5} {E : Type u_1} {F : Type u_2} {𝕜 : Type u_3}
  {𝕜₂ : Type u_4} [SeminormedAddCommGroup E] [SeminormedAddCommGroup F] [NontriviallyNormedField 𝕜]
  [NontriviallyNormedField 𝕜₂] [NormedSpace 𝕜 E] [NormedSpace 𝕜₂ F] {σ₁₂ : 𝕜 →+* 𝕜₂}
  [RingHomIsometric σ₁₂] {ι : Type u_5} [CompleteSpace E] {g : ι → E →SL[σ₁₂] F}
  (h : ∀ (x : E), ∃ C, ∀ (i : ι), ‖(g i) x‖ ≤ C) : ∃ C', ∀ (i : ι), ‖g i‖ ≤ C'
```

## Depends on

- [Completeness](../../topology/uniform-notions/completeness.md)
- [Continuous linear map](../../topology/topological-algebra/continuous-linear-map.md)
- [Normed vector space over a normed field](normed-vector-space-over-a-normed-field.md)

## Proof depends on

- [Baire theorem](../../topology/metric-spaces/baire-theorem.md)
- [The Triangle Inequality](../../../hundred-theorems/part-04/the-triangle-inequality.md)
- [Topological module](../../topology/topological-algebra/topological-module.md)
- [Topology on a normed vector space](topology-on-a-normed-vector-space.md)

## Sources

- [Mathlib documentation: `banach_steinhaus`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Normed/Operator/BanachSteinhaus.html#banach_steinhaus)
- [Source of `banach_steinhaus` in Mathlib/Analysis/Normed/Operator/BanachSteinhaus.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Normed/Operator/BanachSteinhaus.lean#L35)
- [Mathlib overview: Analysis › Normed vector spaces/Banach spaces](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L285)
- [1000+ theorems list: Q1426292](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/1000.yaml#L1682)
- [1000+ theorems project: Q1426292](https://1000-plus.github.io/all.html?length=-1#Q1426292)
- [Wikipedia: Banach–Steinhaus theorem](https://en.wikipedia.org/wiki/Banach%E2%80%93Steinhaus_theorem)
- [Wikidata: Q1426292](https://www.wikidata.org/wiki/Q1426292)
