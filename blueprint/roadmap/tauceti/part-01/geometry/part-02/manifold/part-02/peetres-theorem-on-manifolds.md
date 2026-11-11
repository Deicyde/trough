---
declaration: theorem
origin: cited
lean: LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow, LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq
statement: formalized
proof: formalized
---

# Peetre's theorem on manifolds

Let `P` be a linear map from smooth functions `M → ℝ` to
functions `M → G`, local on the open set `U` (`(P f) x = 0` whenever `f` vanishes near `x ∈ U`)
and with `P f` continuous on `U` for every `f`. Then `P` has locally finite order: for every
compact `K ⊆ U` there is `r` such that `(P f) x = 0` whenever `x ∈ K` and `f` is a finite sum of
products of `r + 1` smooth functions vanishing at `x`. No continuity of `P` is assumed.

```lean
LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow.{u_1, u_2, u_3, u_4} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] {G : Type u_4}
  [NormedAddCommGroup G] [NormedSpace ℝ G]
  (P : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤ →ₗ[ℝ] M → G) {U : Set M} (hU : IsOpen U)
  (hloc :
    ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ∀ x ∈ U, ⇑f =ᶠ[nhds x] 0 → P f x = 0)
  (hcont : ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ContinuousOn (P f) U)
  {K : Set M} (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r, ∀ x ∈ K, ∀ f ∈ TauCeti.smoothVanishingIdeal I x ^ (r + 1), P f x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's lemma](hadamards-lemma.md)
- [Peetre's theorem](../../../../analysis/part-02/calculus/part-02/peetres-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre.html#LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow).

## Other forms

**Peetre's theorem on manifolds, in jet form.** Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre.html#LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq).

```lean
LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_comp_extChartAt_symm_eq.{u_1, u_2, u_3, u_4}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] {G : Type u_4}
  [NormedAddCommGroup G] [NormedSpace ℝ G]
  (P : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤ →ₗ[ℝ] M → G) {U : Set M} (hU : IsOpen U)
  (hloc :
    ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ∀ x ∈ U, ⇑f =ᶠ[nhds x] 0 → P f x = 0)
  (hcont : ∀ (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤), ContinuousOn (P f) U)
  {K : Set M} (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r,
    ∀ x ∈ K,
      ∀ (f g : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤),
        (∀ k ≤ r,
            iteratedFDeriv ℝ k (⇑f ∘ ↑(extChartAt I x).symm) (↑(extChartAt I x) x) =
              iteratedFDeriv ℝ k (⇑g ∘ ↑(extChartAt I x).symm) (↑(extChartAt I x) x)) →
          P f x = P g x
```

## Sources

- [Tau Ceti documentation: `LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre.html#LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow)
- [Source of `LinearMap.exists_apply_eq_zero_of_mem_smoothVanishingIdeal_pow` in TauCeti/Geometry/Manifold/DifferentialOperator/Peetre.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/DifferentialOperator/Peetre.lean#L164)
