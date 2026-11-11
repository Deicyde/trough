---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.NormalizationTranslation.hasFunctionalEquation_iff
statement: formalized
proof: formalized
---

# The functional equation in the two normalizations

The analytic card has its
functional equation `Λ_an(s) = ε conj Λ_an(1 - conj s)` exactly when the arithmetic card has a
unit root number, a polar divisor symmetric under `s ↦ w + 1 - conj s`, and the functional
equation `Λ_ar(s) = ε conj Λ_ar(w + 1 - conj s)` at every `s` at which neither `s` nor
`w + 1 - conj s` is a pole. The symmetry of the polar divisor is a separate clause: it is not
implied by the other two.

```lean
TauCeti.LFunctions.NormalizationTranslation.hasFunctionalEquation_iff
  (T : TauCeti.LFunctions.NormalizationTranslation) :
  T.analytic.HasFunctionalEquation ↔
    ‖T.arithmetic.rootNumber‖ = 1 ∧
      (∀ (s : ℂ),
          T.arithmetic.polarOrder (↑T.weight + 1 - (starRingEnd ℂ) s) = T.arithmetic.polarOrder s) ∧
        ∀ (s : ℂ),
          T.arithmetic.polarOrder s = 0 →
            T.arithmetic.polarOrder (↑T.weight + 1 - (starRingEnd ℂ) s) = 0 →
              T.arithmetic.completed s =
                T.arithmetic.rootNumber * T.arithmetic.dual.completed (↑T.weight + 1 - s)
```

## Depends on

- [Completed L-function data in the analytic normalization](completed-l-function-data-in-the-analytic-normal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.NormalizationTranslation.hasFunctionalEquation_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Data/Normalization.html#TauCeti.LFunctions.NormalizationTranslation.hasFunctionalEquation_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.NormalizationTranslation.hasFunctionalEquation_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Data/Normalization.html#TauCeti.LFunctions.NormalizationTranslation.hasFunctionalEquation_iff)
- [Source of `TauCeti.LFunctions.NormalizationTranslation.hasFunctionalEquation_iff` in TauCeti/NumberTheory/LFunctions/Data/Normalization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LFunctions/Data/Normalization.lean#L389)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LFunctions/STATUS.md)
