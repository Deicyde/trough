---
declaration: theorem
origin: cited
lean: TauCeti.bochner_charFun_probabilityMeasure
statement: formalized
proof: formalized
---

# The Bochner–Khinchin theorem

A function `F` on a finite-dimensional real inner-product
space is continuous, positive definite and normalized by `F 0 = 1` if and only if it is the
characteristic function of a unique Borel probability measure.

```lean
TauCeti.bochner_charFun_probabilityMeasure.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ) :
  Continuous F ∧ TauCeti.IsPositiveDefiniteSub F ∧ F 0 = 1 ↔
    ∃! μ, MeasureTheory.IsProbabilityMeasure μ ∧ MeasureTheory.charFun μ = F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Bochner's theorem](../one-parameter-semigroups-completely-monotone-and/bochners-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bochner_charFun_probabilityMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/CharFun/Bochner.html#TauCeti.bochner_charFun_probabilityMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.bochner_charFun_probabilityMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/CharFun/Bochner.html#TauCeti.bochner_charFun_probabilityMeasure)
- [Source of `TauCeti.bochner_charFun_probabilityMeasure` in TauCeti/Analysis/Bochner/CharFun/Bochner.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/CharFun/Bochner.lean#L81)
