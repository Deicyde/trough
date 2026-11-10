---
declaration: def
origin: cited
lean: TauCeti.complexProjectiveZeroLocus
statement: formalized
---

# TauCeti.complexProjectiveZeroLocus

The common zero locus of a family of polynomials in `N` variables, as a set of complex lines
in `ℂ^N`: a line belongs to it when every polynomial of the family vanishes at every vector of
the line. The line of `L` is `L.submodule`, which is the underlying submodule of
`Projectivization.equivSubmodule ℂ (Fin N → ℂ) L`.

```lean
TauCeti.complexProjectiveZeroLocus.{u_1} {N : ℕ} {ι : Type u_1} (p : ι → MvPolynomial (Fin N) ℂ) :
  Set (Projectivization ℂ (Fin N → ℂ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.complexProjectiveZeroLocus`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/ZeroLocus.html#TauCeti.complexProjectiveZeroLocus).

## Sources

- [Tau Ceti documentation: `TauCeti.complexProjectiveZeroLocus`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Projectivization/ZeroLocus.html#TauCeti.complexProjectiveZeroLocus)
- [Source of `TauCeti.complexProjectiveZeroLocus` in TauCeti/LinearAlgebra/Projectivization/ZeroLocus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Projectivization/ZeroLocus.lean#L71)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
