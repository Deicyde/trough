---
declaration: theorem
origin: cited
lean: TauCeti.Probability.integral_pow_marchenkoPastur
statement: formalized
proof: formalized
---

# Noncrossing-partition moment formula for the Marchenko–Pastur law

For every `k : ℕ`,
`∫ x ^ k d(marchenkoPastur y) = ∑_{π ∈ NC(Fin k)} y ^ (k - |π|)`.

```lean
TauCeti.Probability.integral_pow_marchenkoPastur (y : NNReal) (k : ℕ) :
  ∫ (x : ℝ), x ^ k ∂TauCeti.Probability.marchenkoPastur y = ∑ π, ↑y ^ (k - (↑π).parts.card)
```

## Depends on

- [TauCeti.Probability.marchenkoPastur](tauceti-probability-marchenkopastur.md)

## Proof depends on

- [TauCeti.Probability.semicircleReal](tauceti-probability-semicirclereal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.integral_pow_marchenkoPastur`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MarchenkoPastur/Moments.html#TauCeti.Probability.integral_pow_marchenkoPastur).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.integral_pow_marchenkoPastur`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MarchenkoPastur/Moments.html#TauCeti.Probability.integral_pow_marchenkoPastur)
- [Source of `TauCeti.Probability.integral_pow_marchenkoPastur` in TauCeti/Probability/Distributions/MarchenkoPastur/Moments.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/MarchenkoPastur/Moments.lean#L329)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
