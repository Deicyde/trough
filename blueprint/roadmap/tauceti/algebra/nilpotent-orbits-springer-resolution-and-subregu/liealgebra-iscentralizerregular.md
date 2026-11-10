---
declaration: def
origin: cited
lean: LieAlgebra.IsCentralizerRegular
statement: formalized
---

# LieAlgebra.IsCentralizerRegular

An element `x` of a Lie algebra is **regular** when its centralizer `ker (ad x)` has minimal
dimension among the centralizers of all elements. The dimension is the cardinal `Module.rank`, so
that an infinite-dimensional centralizer is never smaller than a finite-dimensional one. Over a
field of characteristic zero this is the dimension of the group centralizer `C_G(x)` when the Lie
algebra is that of an affine algebraic group `G`. This differs from Mathlib's
`LieAlgebra.IsRegular`, which asks that the coefficient of index `LieAlgebra.rank` of the
characteristic polynomial of `ad x` be nonzero, and from minimality of the dimension of the Engel
subalgebra, the generalized `0`-eigenspace of `ad x`.

```lean
LieAlgebra.IsCentralizerRegular.{u, u_1} (K : Type u_1) {L : Type u} [Field K] [LieRing L]
  [LieAlgebra K L] (x : L) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LieAlgebra.IsCentralizerRegular`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/Regular.html#LieAlgebra.IsCentralizerRegular).

## Sources

- [Tau Ceti documentation: `LieAlgebra.IsCentralizerRegular`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/AdjointAction/Regular.html#LieAlgebra.IsCentralizerRegular)
- [Source of `LieAlgebra.IsCentralizerRegular` in TauCeti/Algebra/Lie/AdjointAction/Regular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/AdjointAction/Regular.lean#L94)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
