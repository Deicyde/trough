---
declaration: theorem
origin: cited
lean: TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring, TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division
statement: formalized
proof: formalized
---

# Kedlaya's Hilbert basis theorem for `A^r` (Kedlaya, Theorem 3.2)

For finitely many
variables and all positive radii `c`, the ring `A^r{T/c}` of restricted power series over the
radius ring with its Gauss norm is noetherian.

```lean
TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring.{u_1, u_2, u_3} (p : ℕ)
  [Fact (Nat.Prime p)] {K : Type u_1} {O : Type u_2} [Field K] [CommRing O] [Algebra O K]
  {v : Valuation K NNReal} {ϖ : O} [CharP O p] [PerfectRing O p] (hv : v.Integers O) (hϖ : ϖ ≠ 0)
  (hϖ' : v ((algebraMap O K) ϖ) < 1) {ρ : NNReal} (hρ : ρ ∈ Set.Ioo 0 1) {σ : Type u_3} [Finite σ]
  {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)] : IsNoetherianRing ↥(MvPowerSeries.IsRestricted.subring c)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/RadiusRing.html#TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring).

## Other forms

**Kedlaya's Hilbert basis theorem for restricted power series, the argument of Kedlaya's Theorem 3.2 for an abstract Euclidean normed ring.** Formalized in Tau Ceti as [`TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/Groebner.html#TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division).

```lean
TauCeti.MvPowerSeries.isNoetherianRing_isRestricted_subring_of_division.{u_1, u_2} {σ : Type u_1}
  {R : Type u_2} [NormedRing R] [IsUltrametricDist R] {c : σ → ℝ} [∀ (i : σ), Fact (0 < c i)]
  [NormMulClass R] [CompleteSpace R] [Finite σ] (deg : R → ℕ)
  (hdeg : ∀ (x y : R), ‖x - y‖ < ‖x‖ → deg y = deg x)
  (hdiv : ∀ (x y : R), x ≠ 0 → ∃ z w, y = z * x + w ∧ ‖w‖ ≤ ‖y‖ ∧ (w = 0 ∨ deg w < deg x)) :
  IsNoetherianRing ↥(MvPowerSeries.IsRestricted.subring c)
```

## Sources

- [Tau Ceti documentation: `TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/RadiusRing.html#TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring)
- [Source of `TauCeti.WittVector.RadiusRing.isNoetherianRing_isRestricted_subring` in TauCeti/RingTheory/MvPowerSeries/TateAlgebra/RadiusRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPowerSeries/TateAlgebra/RadiusRing.lean#L49)
