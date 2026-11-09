---
declaration: theorem
origin: cited
lean: AbstractMeasure.existsUnique_integral_iff_norm_le_one
statement: formalized
proof: formalized
---

# The integral dual unit ball

A `ℚ_p`-valued measure on `ℤ_p` has operator norm at most `1`
exactly when there is a unique `ℤ_p`-valued measure `μ` with `ν (f) = μ (f)` for every
`ℤ_p`-valued test function `f`.

```lean
AbstractMeasure.existsUnique_integral_iff_norm_le_one {p : ℕ} [Fact (Nat.Prime p)]
  (ν : AbstractMeasure ℤ_[p] ℚ_[p] ℚ_[p]) :
  (∃! μ,
      ∀ (f : C(ℤ_[p], ℤ_[p])),
        ν ({ toFun := fun x => ↑x, continuous_toFun := ⋯ }.comp f) = ↑(μ f)) ↔
    ‖AbstractMeasure.toCLMEquiv ν‖ ≤ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Extension of coefficients from the unit ball](../../../ring-theory/part-01/p-adic-measures-completed-group-algebras-and-cha/part-01/extension-of-coefficients-from-the-unit-ball.md)

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.existsUnique_integral_iff_norm_le_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/IntegralUnitBall.html#AbstractMeasure.existsUnique_integral_iff_norm_le_one).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.existsUnique_integral_iff_norm_le_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/IntegralUnitBall.html#AbstractMeasure.existsUnique_integral_iff_norm_le_one)
- [Source of `AbstractMeasure.existsUnique_integral_iff_norm_le_one` in TauCeti/NumberTheory/Padics/Measure/IntegralUnitBall.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Measure/IntegralUnitBall.lean#L81)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
