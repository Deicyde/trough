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
- [Source of `TauCeti.IsRegularLocalRing.isCohenMacaulay` in TauCeti/RingTheory/RegularLocalRing/CohenMacaulay.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/RegularLocalRing/CohenMacaulay.lean#L123)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LocalPurity/STATUS.md)
