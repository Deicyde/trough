---
declaration: theorem
origin: cited
lean: TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division, TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring
statement: formalized
proof: formalized
---

# Kedlaya's Hilbert basis theorem for restricted power series

**Kedlaya's Hilbert basis theorem for restricted power series**, the argument of Kedlaya's
Theorem 3.2 for an abstract Euclidean normed ring.
Let `R` be a complete ring with a multiplicative ultrametric norm, and `deg : R → ℕ`
a degree such that `deg y = deg x` whenever `‖x - y‖ < ‖x‖`, and such that for `x ≠ 0` every `y`
can be divided as `y = z * x + w` with `‖w‖ ≤ ‖y‖` and either `w = 0` or `deg w < deg x`. Then
for finitely many variables and all positive radii `c`, the ring of restricted power series
with its Gauss norm at the radii `c` is left noetherian.

```lean
TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division.{u_1, u_2} {σ : Type u_1}
  {R : Type u_2} [NormedRing R] [IsUltrametricDist R] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)]
  [NormMulClass R] [CompleteSpace R] [Finite σ] (deg : R → ℕ)
  (hdeg : ∀ (x y : R), ‖x - y‖ < ‖x‖ → deg y = deg x)
  (hdiv : ∀ (x y : R), x ≠ 0 → ∃ z w, y = z * x + w ∧ ‖w‖ ≤ ‖y‖ ∧ (w = 0 ∨ deg w < deg x)) :
  IsNoetherianRing ↥(MvPowerSeries.IsRestricted.subring c)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Groebner.html#TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division).

## Other forms

**Kedlaya's Hilbert basis theorem for `A^r` (Kedlaya, Theorem 3.2).** Formalized in Tau Ceti as [`TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/RadiusRing.html#TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring).

```lean
TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring.{u_1, u_2, u_3} (p : ℕ)
  [Fact (Nat.Prime p)] {K : Type u_1} {O : Type u_2} [Field K] [CommRing O] [Algebra O K]
  {v : Valuation K NNReal} {ϖ : O} [CharP O p] [PerfectRing O p] (hv : v.Integers O) (hϖ : ϖ ≠ 0)
  (hϖ' : v ((algebraMap O K) ϖ) < 1) {ρ : NNReal} (hρ : ρ ∈ Set.Ioo 0 1) {σ : Type u_3} [Finite σ]
  {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] : IsNoetherianRing ↥(MvPowerSeries.IsRestricted.subring c)
```

## Sources

- [Tau Ceti documentation: `TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Groebner.html#TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division)
- [Source of `TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Groebner.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Groebner.lean#L561)
