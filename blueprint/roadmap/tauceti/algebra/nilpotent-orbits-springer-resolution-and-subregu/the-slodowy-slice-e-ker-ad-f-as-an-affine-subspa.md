---
declaration: def
origin: cited
lean: TauCeti.slodowySlice
statement: formalized
---

# The Slodowy slice `e + ker (ad f)`, as an affine subspace of `L`

When `(h, e, f)` is an
`sl₂` triple in a finite-dimensional Lie algebra over a field of characteristic zero, its direction
`ker (ad f)` is complementary to `[L, e]` (`IsSl2Triple.isCompl_range_ad_e_ker_ad_f`). For `f = 0`,
in particular in the degenerate case `e = f = 0`, it is all of `L`
(`TauCeti.slodowySlice_zero_right`).

```lean
TauCeti.slodowySlice.{u_1, u_2} (R : Type u_1) {L : Type u_2} [CommRing R] [LieRing L]
  [LieAlgebra R L] (e f : L) : AffineSubspace R L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.slodowySlice`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.html#TauCeti.slodowySlice).

## Sources

- [Tau Ceti documentation: `TauCeti.slodowySlice`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.html#TauCeti.slodowySlice)
- [Source of `TauCeti.slodowySlice` in TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Sl2/SlodowySlice/Basic.lean#L89)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
