---
declaration: theorem
origin: cited
lean: TauCeti.IsRegularLocalRing.isCohenMacaulay
statement: formalized
proof: formalized
---

# A regular local ring is Cohen–Macaulay

Stacks, Lemma 10.106.3 (00NQ).

```lean
TauCeti.IsRegularLocalRing.isCohenMacaulay.{u} {R : Type u} [CommRing R] [IsRegularLocalRing R] :
  Module.IsCohenMacaulay R R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRegularLocalRing.isCohenMacaulay`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/CohenMacaulay.html#TauCeti.IsRegularLocalRing.isCohenMacaulay).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRegularLocalRing.isCohenMacaulay`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/CohenMacaulay.html#TauCeti.IsRegularLocalRing.isCohenMacaulay)
- [Source of `TauCeti.IsRegularLocalRing.isCohenMacaulay` in TauCeti/RingTheory/RegularLocalRing/CohenMacaulay.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/RegularLocalRing/CohenMacaulay.lean#L123)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/LocalPurity/STATUS.md)
