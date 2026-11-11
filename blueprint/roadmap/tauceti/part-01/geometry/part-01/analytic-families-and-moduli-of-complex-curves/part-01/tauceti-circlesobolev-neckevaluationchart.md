---
declaration: def
origin: cited
lean: TauCeti.CircleSobolev.neckEvaluationChart
statement: formalized
---

# TauCeti.CircleSobolev.neckEvaluationChart

A local ambient coordinate change at the node, retaining all parameters. Its inverse is
holomorphic as a germ. No smallness of the constant logarithmic modes is required.

```lean
TauCeti.CircleSobolev.neckEvaluationChart.{u_1} {s : ℝ} {A : Type u_1} [NormedAddCommGroup A]
  [NormedSpace ℂ A] {p : (ℂ × ℂ) × A → TauCeti.CircleSobolev s ℂ × TauCeti.CircleSobolev s ℂ}
  {t : A} [CompleteSpace A] (hp : AnalyticAt ℂ p (0, t)) :
  OpenPartialHomeomorph ((ℂ × ℂ) × A) ((ℂ × ℂ) × A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.neckEvaluationChart`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Plumbing/Inverse.html#TauCeti.CircleSobolev.neckEvaluationChart).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.neckEvaluationChart`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Plumbing/Inverse.html#TauCeti.CircleSobolev.neckEvaluationChart)
- [Source of `TauCeti.CircleSobolev.neckEvaluationChart` in TauCeti/Analysis/Sobolev/Circle/Plumbing/Inverse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Sobolev/Circle/Plumbing/Inverse.lean#L120)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
