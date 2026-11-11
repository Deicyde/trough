---
declaration: theorem
origin: cited
lean: TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq
statement: formalized
proof: formalized
---

# Weyl's lemma for `\bar∂`

A distributional solution with finite-dimensional complex
coefficients agrees almost everywhere on its domain with a holomorphic function.

```lean
TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq.{u_1} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {μ : MeasureTheory.Measure ℂ}
  {Ω : TopologicalSpace.Opens ℂ} {u : ℂ → F} [FiniteDimensional ℂ F] [μ.IsAddHaarMeasure]
  (h : TauCeti.HasWeakConjWirtingerDerivOn μ Ω u 0) :
  ∃ v, DifferentiableOn ℂ v ↑Ω ∧ u =ᵐ[μ.restrict ↑Ω] v
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weyl's lemma for continuous functions](../../part-03/inner-product-space/part-03/weyls-lemma-for-continuous-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Weyl.html#TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Weyl.html#TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq)
- [Source of `TauCeti.HasWeakConjWirtingerDerivOn.exists_differentiableOn_ae_eq` in TauCeti/Analysis/Complex/Wirtinger/Weyl.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Wirtinger/Weyl.lean#L99)
- [Tau Ceti roadmap status: Elliptic analysis of pseudoholomorphic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PseudoholomorphicCurveAnalysis/STATUS.md)
