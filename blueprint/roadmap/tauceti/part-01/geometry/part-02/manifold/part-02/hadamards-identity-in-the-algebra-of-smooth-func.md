---
declaration: theorem
origin: cited
lean: TauCeti.sub_algebraMap_eq_sum_mul_sub_algebraMap
statement: formalized
proof: formalized
---

# Hadamard's identity in the algebra of smooth functions

A pointwise factorization of
`g - g x` through the functions `c i`, with coefficients `a i`, is an identity between the bundled
smooth maps themselves, the constants appearing as the images of `algebraMap`.

This is the pointwise-to-bundled transport: the hypothesis speaks of values, the conclusion of
elements of `C^n⟮I, M; 𝕜⟯`, and the two are related by evaluation being a ring homomorphism.

```lean
TauCeti.sub_algebraMap_eq_sum_mul_sub_algebraMap.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3}
  [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u_4} [TopologicalSpace M]
  [ChartedSpace H M] {n : WithTop ℕ∞} {ι : Type u_5} [Fintype ι] (x : M)
  (g : ContMDiffMap I (modelWithCornersSelf 𝕜 𝕜) M 𝕜 n)
  (a c : ι → ContMDiffMap I (modelWithCornersSelf 𝕜 𝕜) M 𝕜 n)
  (h : ∀ (y : M), g y - g x = ∑ i, (a i) y * ((c i) y - (c i) x)) :
  g - (algebraMap 𝕜 (ContMDiffMap I (modelWithCornersSelf 𝕜 𝕜) M 𝕜 n)) (g x) =
    ∑ i, a i * (c i - (algebraMap 𝕜 (ContMDiffMap I (modelWithCornersSelf 𝕜 𝕜) M 𝕜 n)) ((c i) x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sub_algebraMap_eq_sum_mul_sub_algebraMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Algebra/SmoothFunctions.html#TauCeti.sub_algebraMap_eq_sum_mul_sub_algebraMap).

## Sources

- [Tau Ceti documentation: `TauCeti.sub_algebraMap_eq_sum_mul_sub_algebraMap`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Algebra/SmoothFunctions.html#TauCeti.sub_algebraMap_eq_sum_mul_sub_algebraMap)
- [Source of `TauCeti.sub_algebraMap_eq_sum_mul_sub_algebraMap` in TauCeti/Geometry/Manifold/Algebra/SmoothFunctions.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Algebra/SmoothFunctions.lean#L203)
