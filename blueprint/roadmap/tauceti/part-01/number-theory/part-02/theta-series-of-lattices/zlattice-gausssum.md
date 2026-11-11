---
declaration: def
origin: cited
lean: ZLattice.gaussSum
statement: formalized
---

# ZLattice.gaussSum

The Gauss sum `G_L(a, c) = ∑_{y ∈ L / cL} e(a ‖y‖² / (2c))` of an even lattice `L`.

```lean
ZLattice.gaussSum.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  (L : Submodule ℤ E) (hL : ZLattice.IsEven L) (a : ℤ) (c : ℕ)
  [Fintype (↥L ⧸ (↑c • L).submoduleOf L)] : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.gaussSum`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/GaussSum.html#ZLattice.gaussSum).

## Sources

- [Tau Ceti documentation: `ZLattice.gaussSum`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/GaussSum.html#ZLattice.gaussSum)
- [Source of `ZLattice.gaussSum` in TauCeti/Algebra/Module/ZLattice/GaussSum.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/GaussSum.lean#L189)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
