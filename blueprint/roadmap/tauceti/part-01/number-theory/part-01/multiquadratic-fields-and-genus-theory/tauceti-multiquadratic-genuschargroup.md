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
- [Source of `TauCeti.Multiquadratic.genusCharGroup` in TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Multiquadratic/Legendre/PrimeDiscriminant/Dirichlet/Group.lean#L218)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/Multiquadratic/STATUS.md)
