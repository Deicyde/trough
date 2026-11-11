---
declaration: def
origin: cited
lean: TauCeti.Algebra.IsTamelyRamifiedWRT
statement: formalized
---

# TauCeti.Algebra.IsTamelyRamifiedWRT

`L` is **tamely ramified with respect to the local ring `A`**: every maximal ideal of the
integral closure of `A` in `L` has separable residue field extension over the residue field of
`A`, and a ramification index invertible in that residue field. This is Stacks' notion for `A` a
discrete valuation ring and `L` a finite separable extension of its fraction field.

```lean
TauCeti.Algebra.IsTamelyRamifiedWRT.{u_1, u_2} (A : Type u_1) (L : Type u_2) [CommRing A]
  [IsLocalRing A] [Field L] [Algebra A L] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.IsTamelyRamifiedWRT`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.html#TauCeti.Algebra.IsTamelyRamifiedWRT).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.IsTamelyRamifiedWRT`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.html#TauCeti.Algebra.IsTamelyRamifiedWRT)
- [Source of `TauCeti.Algebra.IsTamelyRamifiedWRT` in TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DiscreteValuationRing/TamelyRamified.lean#L98)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
