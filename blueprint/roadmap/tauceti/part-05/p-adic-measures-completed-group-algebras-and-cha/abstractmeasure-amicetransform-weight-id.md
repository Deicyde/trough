---
declaration: theorem
origin: cited
lean: AbstractMeasure.amiceTransform_weight_id
statement: formalized
proof: formalized
---

# AbstractMeasure.amiceTransform\_weight\_id

For `ℤ_p`-valued measures, multiplication by `x` acts on the Amice transform as the Mahler
derivation: `A (x μ) = (1 + T) d/dT A_μ`.

```lean
AbstractMeasure.amiceTransform_weight_id {p : ℕ} [Fact (Nat.Prime p)]
  (μ : AbstractMeasure ℤ_[p] ℤ_[p] ℤ_[p]) :
  AbstractMeasure.amiceTransform ((AbstractMeasure.weight (ContinuousMap.id ℤ_[p])) μ) =
    (PowerSeries.mahlerDerivation ℤ_[p]) (AbstractMeasure.amiceTransform μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.amiceTransform_weight_id`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Moments.html#AbstractMeasure.amiceTransform_weight_id).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.amiceTransform_weight_id`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Moments.html#AbstractMeasure.amiceTransform_weight_id)
- [Source of `AbstractMeasure.amiceTransform_weight_id` in TauCeti/NumberTheory/Padics/Measure/Moments.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Measure/Moments.lean#L141)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
