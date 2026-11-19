---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.IsMarkovTrace.forall_map_star_mul_self_nonneg_iff, TauCeti.TemperleyLieb.markovTrace_nonneg_iff
statement: formalized
proof: formalized
---

# Jones's positivity theorem

For `δ > 0`, the Hermitian forms `(x, y) ↦ tr n (x⋆ * y)` of a
Markov trace are positive semidefinite on every number of strands exactly when `δ` is an admissible
loop parameter, `δ = 2 cos (π / m)` for some `m ≥ 3` or `δ ≥ 2`.

```lean
TauCeti.TemperleyLieb.IsMarkovTrace.forall_map_star_mul_self_nonneg_iff {δ : ℝ}
  [Fact (IsSelfAdjoint ↑δ)] {tr : (n : ℕ) → TauCeti.TemperleyLieb ℂ (↑δ) n →ₗ[ℂ] ℂ}
  (htr : TauCeti.TemperleyLieb.IsMarkovTrace ℂ (↑δ) tr) (hδ : 0 < δ) :
  (∀ (n : ℕ) (x : TauCeti.TemperleyLieb ℂ (↑δ) n), 0 ≤ (tr n) (star x * x)) ↔
    δ ∈ TauCeti.TemperleyLieb.jonesLoopParameters
```

## Depends on

- [TauCeti.TemperleyLieb.instStarRing](../../part-01/subfactors-jones-index-and-planar-standard-invar/tauceti-temperleylieb-inststarring.md)

## Proof depends on

- [TauCeti.qInt_two_mul_cos_floor_add_one_neg](../../part-01/subfactors-jones-index-and-planar-standard-invar/tauceti-qint-two-mul-cos-floor-add-one-neg.md)
- [TauCeti.qInt_two_mul_cos_pi_div_eq_zero](../../part-01/subfactors-jones-index-and-planar-standard-invar/tauceti-qint-two-mul-cos-pi-div-eq-zero.md)
- [TauCeti.qInt_two_mul_cos_pos_of_le_floor](../../part-01/subfactors-jones-index-and-planar-standard-invar/tauceti-qint-two-mul-cos-pos-of-le-floor.md)
- [TauCeti.TemperleyLieb.IsMarkovTrace.eq_markovTrace](../../part-01/temperley-lieb-diagrams-categories-and-algebras/tauceti-temperleylieb-ismarkovtrace-eq-markovtra.md)
- [TauCeti.TemperleyLieb.map_star_iff](../../part-01/subfactors-jones-index-and-planar-standard-invar/tauceti-temperleylieb-map-star-iff.md)
- [TauCeti.TemperleyLieb.strandIncl_star](../../part-01/subfactors-jones-index-and-planar-standard-invar/tauceti-temperleylieb-strandincl-star.md)
- [The tower normal form](../../part-01/temperley-lieb-diagrams-categories-and-algebras/the-tower-normal-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.IsMarkovTrace.forall_map_star_mul_self_nonneg_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Positivity.html#TauCeti.TemperleyLieb.IsMarkovTrace.forall_map_star_mul_self_nonneg_iff).

## Other forms

**Jones's positivity theorem for the spin-model trace.** Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.markovTrace_nonneg_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Positivity.html#TauCeti.TemperleyLieb.markovTrace_nonneg_iff).

```lean
TauCeti.TemperleyLieb.markovTrace_nonneg_iff {δ : ℝ} [Fact (IsSelfAdjoint ↑δ)] (hδ : 0 < δ) (q : ℂˣ)
  (hq : ↑δ = -(↑q + ↑q⁻¹)) :
  (∀ (n : ℕ) (x : TauCeti.TemperleyLieb ℂ (↑δ) n),
      0 ≤ (TauCeti.TemperleyLieb.markovTrace q hq) (star x * x)) ↔
    δ ∈ TauCeti.TemperleyLieb.jonesLoopParameters
```

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.IsMarkovTrace.forall_map_star_mul_self_nonneg_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/Positivity.html#TauCeti.TemperleyLieb.IsMarkovTrace.forall_map_star_mul_self_nonneg_iff)
- [Source of `TauCeti.TemperleyLieb.IsMarkovTrace.forall_map_star_mul_self_nonneg_iff` in TauCeti/Algebra/TemperleyLieb/Positivity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TemperleyLieb/Positivity.lean#L275)
