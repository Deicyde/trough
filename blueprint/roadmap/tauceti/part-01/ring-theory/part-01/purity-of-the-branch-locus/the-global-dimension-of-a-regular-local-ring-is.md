---
declaration: theorem
origin: cited
lean: TauCeti.IsRegularLocalRing.globalDimension_eq_ringKrullDim
statement: formalized
proof: formalized
---

# The global dimension of a regular local ring is its Krull dimension

The upper bound is
Stacks, Proposition 10.110.1 (00O7); the residue field attains it.

```lean
TauCeti.IsRegularLocalRing.globalDimension_eq_ringKrullDim.{v, u} {R : Type u} [CommRing R]
  [IsRegularLocalRing R] [Small.{v, u} R] : TauCeti.globalDimension R = ringKrullDim R
```

## Depends on

- [TauCeti.globalDimension](tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsRegularLocalRing.globalDimension_eq_ringKrullDim`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.html#TauCeti.IsRegularLocalRing.globalDimension_eq_ringKrullDim).

## Sources

- [Tau Ceti documentation: `TauCeti.IsRegularLocalRing.globalDimension_eq_ringKrullDim`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.html#TauCeti.IsRegularLocalRing.globalDimension_eq_ringKrullDim)
- [Source of `TauCeti.IsRegularLocalRing.globalDimension_eq_ringKrullDim` in TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/RegularLocalRing/ProjectiveDimension.lean#L219)
- [Tau Ceti roadmap status: Purity of the branch locus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PurityOfBranchLocus/STATUS.md)
