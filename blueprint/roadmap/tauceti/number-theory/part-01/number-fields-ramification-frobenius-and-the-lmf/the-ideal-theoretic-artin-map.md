---
declaration: def
origin: cited
lean: TauCeti.NumberFieldArithmetic.artinHomAway
statement: formalized
---

# The ideal-theoretic Artin map

The multiplicative extension of `artinElementAway` along
the unique factorization of an invertible fractional ideal, on the group of fractional ideals
with multiplicity zero at every prime of `S`.

```lean
TauCeti.NumberFieldArithmetic.artinHomAway.{u_1, u_2} {K : Type u_1} [Field K] [NumberField K]
  {L : Type u_2} [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (hab : ∀ (σ τ : Gal(L/K)), Commute σ τ)
  (S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)))
  (hur :
    ∀ v ∉ S,
      ∀ (Q : Ideal (NumberField.RingOfIntegers L)) [inst : Q.IsPrime] [Q.LiesOver v.asIdeal],
        Algebra.IsUnramifiedAt (NumberField.RingOfIntegers K) Q) :
  ↥(TauCeti.NumberFieldArithmetic.idealsAway K S) →* Gal(L/K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberFieldArithmetic.artinHomAway`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Ideal/ArtinMap.html#TauCeti.NumberFieldArithmetic.artinHomAway).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberFieldArithmetic.artinHomAway`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Ideal/ArtinMap.html#TauCeti.NumberFieldArithmetic.artinHomAway)
- [Source of `TauCeti.NumberFieldArithmetic.artinHomAway` in TauCeti/NumberTheory/NumberField/Ideal/ArtinMap.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Ideal/ArtinMap.lean#L178)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/NumberFieldArithmetic/STATUS.md)
