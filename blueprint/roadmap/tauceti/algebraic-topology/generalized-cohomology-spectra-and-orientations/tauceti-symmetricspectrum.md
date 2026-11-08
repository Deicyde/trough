---
declaration: abbrev
origin: cited
lean: TauCeti.SymmetricSpectrum
statement: formalized
---

# TauCeti.SymmetricSpectrum

Symmetric spectra of pointed simplicial sets: the modules over the commutative monoid
`SymmetricSequence.sphere` of symmetric sequences. A symmetric spectrum is a symmetric sequence
`X` with an action `S ⊗ X ⟶ X` for the Day convolution product, satisfying the unit and
associativity laws.

```lean
TauCeti.SymmetricSpectrum : Type 1
```

## Depends on

- [TauCeti.PointedSSet.instBraidedFiniteBijectionSmashPowFunctor](tauceti-pointedsset-instbraidedfinitebijectionsm.md)
- [TauCeti.SymmetricSequence](tauceti-symmetricsequence.md)

## Proof depends on

- [TauCeti.PointedSSet.monoidalClosed](tauceti-pointedsset-monoidalclosed.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymmetricSpectrum`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/SymmetricSpectrum.html#TauCeti.SymmetricSpectrum).

## Sources

- [Tau Ceti documentation: `TauCeti.SymmetricSpectrum`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/SymmetricSpectrum.html#TauCeti.SymmetricSpectrum)
- [Source of `TauCeti.SymmetricSpectrum` in TauCeti/AlgebraicTopology/Spectra/SymmetricSpectrum.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Spectra/SymmetricSpectrum.lean#L88)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
