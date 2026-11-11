---
declaration: theorem
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.ramificationIdx_mul_multiplicity_differentIdeal_fixedField
statement: formalized
proof: formalized
---

# The different exponent of a fixed field from its permutation action

The ramification
index over the selected prime of `Lᴴ` times its different exponent is the sum, over the lower
ramification groups at `Q`, of the numbers of elements outside `H`.

```lean
IsDedekindDomain.HeightOneSpectrum.ramificationIdx_mul_multiplicity_differentIdeal_fixedField.{u_1,
    u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L]
  [IsGalois K L] (w : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers L))
  (H : Subgroup Gal(L/K)) :
  w.asIdeal.ramificationIdx (NumberField.RingOfIntegers ↥(IntermediateField.fixedField H)) *
      multiplicity
        (IsDedekindDomain.HeightOneSpectrum.under
            (NumberField.RingOfIntegers ↥(IntermediateField.fixedField H)) w).asIdeal
        (differentIdeal (NumberField.RingOfIntegers K)
          (NumberField.RingOfIntegers ↥(IntermediateField.fixedField H))) =
    ∑ᶠ (i : ℕ),
      (Nat.card ↥(Ideal.ramificationGroup Gal(L/K) w.asIdeal i) -
        Nat.card ↥(Ideal.ramificationGroup Gal(L/K) w.asIdeal i ⊓ H))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert's formula for a number-field different exponent](hilberts-formula-for-a-number-field-different-ex.md)

## Lean

Formalized in Tau Ceti as [`IsDedekindDomain.HeightOneSpectrum.ramificationIdx_mul_multiplicity_differentIdeal_fixedField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Permutation.html#IsDedekindDomain.HeightOneSpectrum.ramificationIdx_mul_multiplicity_differentIdeal_fixedField).

## Sources

- [Tau Ceti documentation: `IsDedekindDomain.HeightOneSpectrum.ramificationIdx_mul_multiplicity_differentIdeal_fixedField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Permutation.html#IsDedekindDomain.HeightOneSpectrum.ramificationIdx_mul_multiplicity_differentIdeal_fixedField)
- [Source of `IsDedekindDomain.HeightOneSpectrum.ramificationIdx_mul_multiplicity_differentIdeal_fixedField` in TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Permutation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/LocalGlobal/Different/Permutation.lean#L101)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/NumberFieldArithmetic/STATUS.md)
