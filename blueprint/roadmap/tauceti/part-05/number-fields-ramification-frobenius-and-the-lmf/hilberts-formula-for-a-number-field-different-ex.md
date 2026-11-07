---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one
statement: formalized
proof: formalized
---

# Hilbert's formula for a number-field different exponent

For a finite Galois extension
`L/K`, the multiplicity of a prime `w` in the global different is the sum of the orders of the
nonnegative-index lower ramification groups, minus one in each degree.

```lean
IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one.{u_1,
    u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L]
  (w : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers L)) [IsGalois K L] :
  multiplicity w.asIdeal
      (differentIdeal (NumberField.RingOfIntegers K) (NumberField.RingOfIntegers L)) =
    ∑ᶠ (i : ℕ), (Nat.card ↥(Ideal.ramificationGroup Gal(L/K) w.asIdeal i) - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The semi-local decomposition](the-semi-local-decomposition.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.html#IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one).

## Sources

- [Tau Ceti documentation: `IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.html#IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one)
- [Source of `IsDedekindDomain.HeightOneSpectrum.multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one` in TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Exponent.lean#L236)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/NumberFieldArithmetic/STATUS.md)
