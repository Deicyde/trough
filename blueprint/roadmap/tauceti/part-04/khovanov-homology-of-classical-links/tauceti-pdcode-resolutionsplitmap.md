---
declaration: def
origin: cited
lean: TauCeti.PDCode.resolutionSplitMap
statement: formalized
---

# TauCeti.PDCode.resolutionSplitMap

Comultiplication on the circle through `c`, splitting it into the two circles of the target
through `c`, and identity on every other factor of the actual resolved-circle tensor. The
one-circle source condition follows from the target count.

```lean
TauCeti.PDCode.resolutionSplitMap.{u} {n : ℕ} (D : TauCeti.PDCode n) {s t : Fin n → Bool}
  {c : Fin n} (hst : ∀ (j : Fin n), j ≠ c → s j = t j) (hc : s c ≠ t c)
  (ht : (D.circlesAt t c).card = 2) (R : Type u) [CommSemiring R] :
  TauCeti.Khovanov.CircleTensor R (D.ResolvedCircle s) →ₗ[R]
    TauCeti.Khovanov.CircleTensor R (D.ResolvedCircle t)
```

## Depends on

- [TauCeti.Khovanov.CircleTensor](tauceti-khovanov-circletensor.md)
- [TauCeti.Khovanov.fiberwiseSplit](tauceti-khovanov-fiberwisesplit.md)

## Proof depends on

- [Two states differing exactly at a crossing do not both have two circles through it](two-states-differing-exactly-at-a-crossing-do-no.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.resolutionSplitMap`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Resolution/Split.html#TauCeti.PDCode.resolutionSplitMap).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.resolutionSplitMap`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Khovanov/Resolution/Split.html#TauCeti.PDCode.resolutionSplitMap)
- [Source of `TauCeti.PDCode.resolutionSplitMap` in TauCeti/KnotTheory/Khovanov/Resolution/Split.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Khovanov/Resolution/Split.lean#L54)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/KhovanovHomology/STATUS.md)
