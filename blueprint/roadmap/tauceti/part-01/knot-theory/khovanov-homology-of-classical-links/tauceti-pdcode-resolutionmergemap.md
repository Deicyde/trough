---
declaration: def
origin: cited
lean: TauCeti.PDCode.resolutionMergeMap
statement: formalized
---

# TauCeti.PDCode.resolutionMergeMap

Multiplication on the two circles merged at `c`, and identity on every other factor of the
actual resolved-circle tensor. The one-circle target condition follows from the source count.

```lean
TauCeti.PDCode.resolutionMergeMap.{u} {n : ℕ} (D : TauCeti.PDCode n) {s t : Fin n → Bool}
  {c : Fin n} (hst : ∀ (j : Fin n), j ≠ c → s j = t j) (hc : s c ≠ t c)
  (hs : (D.circlesAt s c).card = 2) (R : Type u) [CommSemiring R] :
  TauCeti.Khovanov.CircleTensor R (D.ResolvedCircle s) →ₐ[R]
    TauCeti.Khovanov.CircleTensor R (D.ResolvedCircle t)
```

## Depends on

- [TauCeti.Khovanov.CircleTensor](tauceti-khovanov-circletensor.md)

## Proof depends on

- [Two states differing exactly at a crossing do not both have two circles through it](two-states-differing-exactly-at-a-crossing-do-no.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.resolutionMergeMap`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Merge.html#TauCeti.PDCode.resolutionMergeMap).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.resolutionMergeMap`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Merge.html#TauCeti.PDCode.resolutionMergeMap)
- [Source of `TauCeti.PDCode.resolutionMergeMap` in TauCeti/KnotTheory/Khovanov/Merge.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Khovanov/Merge.lean#L49)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/KhovanovHomology/STATUS.md)
