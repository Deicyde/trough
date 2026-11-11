---
declaration: def
origin: cited
lean: ZLattice.level
statement: formalized
---

# ZLattice.level

The level of a lattice `L`: the least `N > 0` such that `N ‖x‖² / 2` is an integer for every
`x` in the dual lattice. For an even lattice this is the order of the discriminant quadratic form
`‖x‖² / 2 mod ℤ` on `L^∨ ⧸ L`. The definition is the unguarded infimum, so it has a value on every
lattice; `level_dvd_iff` characterizes it in general, and `IsIntegral.level_pos` shows that it is
positive for a full integral lattice.

```lean
ZLattice.level.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  (L : Submodule ℤ E) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.level`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Level.html#ZLattice.level).

## Sources

- [Tau Ceti documentation: `ZLattice.level`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Level.html#ZLattice.level)
- [Source of `ZLattice.level` in TauCeti/Algebra/Module/ZLattice/Level.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/Level.lean#L121)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
