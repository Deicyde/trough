---
declaration: theorem
origin: cited
lean: TauCeti.bochnerMeasure_mul
statement: formalized
proof: formalized
---

# Products become convolutions

The Bochner measure of the product of two continuous
positive-definite functions is the convolution of their Bochner measures.

```lean
TauCeti.bochnerMeasure_mul.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] {F H : V → ℂ} (hFcont : Continuous F)
  (hFpd : TauCeti.IsPositiveDefiniteSub F) (hHcont : Continuous H)
  (hHpd : TauCeti.IsPositiveDefiniteSub H) :
  (TauCeti.bochnerMeasure fun v => F v * H v) =
    (TauCeti.bochnerMeasure F).conv (TauCeti.bochnerMeasure H)
```

## Depends on

- [The representing measure of Bochner's theorem](the-representing-measure-of-bochners-theorem.md)

## Proof depends on

- [Bochner's theorem](bochners-theorem.md)
- [Converse half of Bochner's theorem](converse-half-of-bochners-theorem.md)
- [Uniqueness half of Bochner's theorem](../../part-03/bochner/uniqueness-half-of-bochners-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bochnerMeasure_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/Operations.html#TauCeti.bochnerMeasure_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.bochnerMeasure_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/Operations.html#TauCeti.bochnerMeasure_mul)
- [Source of `TauCeti.bochnerMeasure_mul` in TauCeti/Analysis/Bochner/Operations.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Bochner/Operations.lean#L65)
- [Tau Ceti roadmap status: One-parameter semigroups, completely monotone and positive-definite functions, and Bochner-type representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/OneParameterSemigroups/STATUS.md)
