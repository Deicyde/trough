---
declaration: def
origin: cited
lean: PositiveLinearMap.law
statement: formalized
---

# PositiveLinearMap.law

The **law** `μ_a` of an element `a` of a C⋆-algebra with respect to a positive linear
functional `φ`: for selfadjoint `a`, the finite Borel measure on `ℝ`, concentrated on
`spectrum ℝ a` (`law_compl_spectrum`), with `∫ f dμ_a = φ (cfc f a)` for every `f` continuous on
the spectrum (`ofReal_integral_law`), and characterized by this property (`eq_law_iff`). For `a`
not selfadjoint it is the zero measure (`law_of_not_isSelfAdjoint`).

```lean
PositiveLinearMap.law.{u_1} {A : Type u_1} [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
  (φ : A →ₚ[ℂ] ℂ) (a : A) : MeasureTheory.Measure ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PositiveLinearMap.law`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.law).

## Sources

- [Tau Ceti documentation: `PositiveLinearMap.law`](https://taucetiproject.org/docs/TauCeti/Probability/FreeProbability/Law/Basic.html#PositiveLinearMap.law)
- [Source of `PositiveLinearMap.law` in TauCeti/Probability/FreeProbability/Law/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Probability/FreeProbability/Law/Basic.lean#L124)
- [Tau Ceti roadmap status: Free probability, free products, and random matrix models](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeProbability/STATUS.md)
