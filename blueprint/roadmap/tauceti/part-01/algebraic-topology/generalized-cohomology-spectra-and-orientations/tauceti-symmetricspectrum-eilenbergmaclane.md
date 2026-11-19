---
declaration: abbrev
origin: cited
lean: TauCeti.SymmetricSpectrum.eilenbergMacLane
statement: formalized
---

# TauCeti.SymmetricSpectrum.eilenbergMacLane

The Eilenberg–MacLane symmetric spectrum `HR`: the commutative monoid `n ↦ R~[Sⁿ]` of
symmetric sequences, regarded as a module over the sphere by restricting scalars along the unit
`S ⟶ HR`. It is a commutative ring spectrum, a commutative monoid for the smash product over the
sphere, through the instances `Mod.monObjComapRegular` and `Mod.isCommMonObjComapRegular`.

```lean
TauCeti.SymmetricSpectrum.eilenbergMacLane (R : Type) [CommRing R] : TauCeti.SymmetricSpectrum
```

## Depends on

- [TauCeti.SymmetricSpectrum](tauceti-symmetricspectrum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymmetricSpectrum.eilenbergMacLane`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/EilenbergMacLane.html#TauCeti.SymmetricSpectrum.eilenbergMacLane).

## Sources

- [Tau Ceti documentation: `TauCeti.SymmetricSpectrum.eilenbergMacLane`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Spectra/EilenbergMacLane.html#TauCeti.SymmetricSpectrum.eilenbergMacLane)
- [Source of `TauCeti.SymmetricSpectrum.eilenbergMacLane` in TauCeti/AlgebraicTopology/Spectra/EilenbergMacLane.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Spectra/EilenbergMacLane.lean#L133)
- [Tau Ceti roadmap status: Generalized cohomology, spectra and orientations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeneralizedCohomology/STATUS.md)
