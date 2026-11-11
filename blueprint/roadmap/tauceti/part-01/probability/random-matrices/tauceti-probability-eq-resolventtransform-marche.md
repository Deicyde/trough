---
declaration: theorem
origin: cited
lean: TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff
statement: formalized
proof: formalized
---

# TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff

In the upper half-plane, the resolvent transform of `marchenkoPastur y` is the unique root of
`y * z * (w * w) + (z + y - 1) * w + 1 = 0` with positive imaginary part.

```lean
TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff {y : NNReal} {z : ℂ} (hz : 0 < z.im)
  {w : ℂ} :
  w = MeasureTheory.resolventTransform (TauCeti.Probability.marchenkoPastur y) z ↔
    0 < w.im ∧ ↑↑y * z * (w * w) + (z + ↑↑y - 1) * w + 1 = 0
```

## Depends on

- [TauCeti.Probability.marchenkoPastur](tauceti-probability-marchenkopastur.md)

## Proof depends on

- [TauCeti.Probability.semicircleReal](tauceti-probability-semicirclereal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MarchenkoPastur/ResolventTransform.html#TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MarchenkoPastur/ResolventTransform.html#TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff)
- [Source of `TauCeti.Probability.eq_resolventTransform_marchenkoPastur_iff` in TauCeti/Probability/Distributions/MarchenkoPastur/ResolventTransform.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/Distributions/MarchenkoPastur/ResolventTransform.lean#L220)
- [Tau Ceti roadmap status: Random matrices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RandomMatrices/STATUS.md)
