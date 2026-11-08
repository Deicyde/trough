---
declaration: theorem
origin: cited
lean: TauCeti.lintegral_add_mul_klDiv_eq_mul_klDiv_tilted
statement: formalized
proof: formalized
---

# The Gibbs identity

For probability measures `μ` and `ν`, a cost `c` finite
`μ.prod ν`-almost everywhere, and a positive temperature `ε`, every probability measure `π` on
`X × Y` satisfies `∫ c dπ + ε * klDiv π (μ ⊗ ν) = ε * klDiv π R - ε * log Z`, where
`Z = ∫ e^{-c/ε} d(μ ⊗ ν)` and `R = Z⁻¹ e^{-c/ε} (μ ⊗ ν)` is the Gibbs measure, written as the
tilted measure `(μ.prod ν).tilted fun z ↦ -((c z).toReal / ε)`. Both sides may be `∞`.

```lean
TauCeti.lintegral_add_mul_klDiv_eq_mul_klDiv_tilted.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [MeasurableSpace X] [MeasurableSpace Y] {c : X × Y → ENNReal} {ε : NNReal}
  {π : MeasureTheory.Measure (X × Y)} {μ : MeasureTheory.Measure X} {ν : MeasureTheory.Measure Y}
  [MeasureTheory.IsProbabilityMeasure μ] [MeasureTheory.IsProbabilityMeasure ν]
  [MeasureTheory.IsProbabilityMeasure π] (hc : AEMeasurable c (μ.prod ν))
  (hc_top : ∀ᵐ (z : X × Y) ∂μ.prod ν, c z ≠ ⊤) (hε : ε ≠ 0) :
  ∫⁻ (z : X × Y), c z ∂π + ↑ε * InformationTheory.klDiv π (μ.prod ν) =
    ↑ε * InformationTheory.klDiv π ((μ.prod ν).tilted fun z => -((c z).toReal / ↑ε)) +
      ↑ε * ENNReal.ofReal (-Real.log (∫ (z : X × Y), Real.exp (-((c z).toReal / ↑ε)) ∂μ.prod ν))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lintegral_add_mul_klDiv_eq_mul_klDiv_tilted`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.html#TauCeti.lintegral_add_mul_klDiv_eq_mul_klDiv_tilted).

## Sources

- [Tau Ceti documentation: `TauCeti.lintegral_add_mul_klDiv_eq_mul_klDiv_tilted`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.html#TauCeti.lintegral_add_mul_klDiv_eq_mul_klDiv_tilted)
- [Source of `TauCeti.lintegral_add_mul_klDiv_eq_mul_klDiv_tilted` in TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/OptimalTransport/Entropic/Basic.lean#L522)
