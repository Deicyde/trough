---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.multiplicity_relDiscr_fixedField_eq_sum
statement: formalized
proof: formalized
---

# The relative discriminant coefficient of a fixed field from double cosets

Sum the
group-theoretic contributions over `H \ Gal(L/K) / D(Q)`, using any choice of representatives.
The formula holds at ramified primes as well as unramified ones, including wild ramification.

```lean
TauCeti.NumberField.multiplicity_relDiscr_fixedField_eq_sum.{u_1, u_2} (K : Type u_1) (L : Type u_2)
  [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))
  (w : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers L))
  [w.asIdeal.LiesOver v.asIdeal] (H : Subgroup Gal(L/K))
  (r : DoubleCoset.Quotient ↑H ↑(MulAction.stabilizer Gal(L/K) w.asIdeal) → Gal(L/K))
  (hr :
    ∀ (q : DoubleCoset.Quotient ↑H ↑(MulAction.stabilizer Gal(L/K) w.asIdeal)),
      DoubleCoset.mk H (MulAction.stabilizer Gal(L/K) w.asIdeal) (r q) = q) :
  multiplicity v.asIdeal
      (TauCeti.relDiscr (NumberField.RingOfIntegers K)
        (NumberField.RingOfIntegers ↥(IntermediateField.fixedField H))) =
    ∑ᶠ (q : DoubleCoset.Quotient ↑H ↑(MulAction.stabilizer Gal(L/K) w.asIdeal)),
      H.relIndex (MulAut.conj (r q) • MulAction.stabilizer Gal(L/K) w.asIdeal) /
          H.relIndex (MulAut.conj (r q) • Ideal.inertia Gal(L/K) w.asIdeal) *
        ((∑ᶠ (i : ℕ),
            (Nat.card ↥(Ideal.ramificationGroup Gal(L/K) w.asIdeal i) -
              Nat.card ↥(MulAut.conj (r q) • Ideal.ramificationGroup Gal(L/K) w.asIdeal i ⊓ H))) /
          Nat.card ↥(MulAut.conj (r q) • Ideal.inertia Gal(L/K) w.asIdeal ⊓ H))
```

## Depends on

- [TauCeti.relDiscr](tauceti-reldiscr.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [The different exponent of a fixed field from its permutation action](the-different-exponent-of-a-fixed-field-from-its.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.multiplicity_relDiscr_fixedField_eq_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Discriminant/FixedField.html#TauCeti.NumberField.multiplicity_relDiscr_fixedField_eq_sum).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.multiplicity_relDiscr_fixedField_eq_sum`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Discriminant/FixedField.html#TauCeti.NumberField.multiplicity_relDiscr_fixedField_eq_sum)
- [Source of `TauCeti.NumberField.multiplicity_relDiscr_fixedField_eq_sum` in TauCeti/NumberTheory/NumberField/Discriminant/FixedField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Discriminant/FixedField.lean#L106)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/NumberFieldArithmetic/STATUS.md)
