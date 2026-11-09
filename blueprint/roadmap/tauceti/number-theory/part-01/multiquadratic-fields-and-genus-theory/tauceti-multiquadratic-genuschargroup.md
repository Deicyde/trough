---
declaration: def
origin: cited
lean: TauCeti.Multiquadratic.genusCharGroup
statement: formalized
---

# TauCeti.Multiquadratic.genusCharGroup

The subgroup of common-level Dirichlet characters obtained by taking products over subsets of
the prime-discriminant factors.

```lean
TauCeti.Multiquadratic.genusCharGroup (s : Finset ℤ)
  (hs : ∀ P ∈ s, TauCeti.Multiquadratic.IsPrimeDiscriminant P) :
  Subgroup (DirichletCharacter ℤ (∏ P ∈ s, P).natAbs)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.genusCharGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Group.html#TauCeti.Multiquadratic.genusCharGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.genusCharGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Group.html#TauCeti.Multiquadratic.genusCharGroup)
- [Source of `TauCeti.Multiquadratic.genusCharGroup` in TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Group.lean#L217)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Multiquadratic/STATUS.md)
