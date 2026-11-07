---
declaration: def
origin: cited
lean: ZLattice.representationNumber
statement: formalized
---

# ZLattice.representationNumber

The representation number `r_L(t)`: the number of vectors of `L` of squared norm `t`. For a
discrete `L` in a proper space every shell is finite, so this is a genuine count.

```lean
ZLattice.representationNumber.{u_1} {E : Type u_1} [NormedAddCommGroup E] (L : Submodule ℤ E)
  (t : ℝ) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.representationNumber`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Shell.html#ZLattice.representationNumber).

## Sources

- [Tau Ceti documentation: `ZLattice.representationNumber`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Shell.html#ZLattice.representationNumber)
- [Source of `ZLattice.representationNumber` in TauCeti/Algebra/Module/ZLattice/Shell.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Shell.lean#L97)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ThetaSeries/STATUS.md)
