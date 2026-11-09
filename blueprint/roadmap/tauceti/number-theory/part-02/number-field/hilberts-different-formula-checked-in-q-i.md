---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.GaussianRationals.finsum_card_ramificationGroup_sub_one_eq_two
statement: formalized
proof: formalized
---

# Hilbert's different formula, checked in `ℚ(i)`

the sum `Σ_{i ≥ 0} (#G_i − 1)` over the
ramification groups of the prime above `2` is the different exponent `v_𝔭(𝔡) = 2`, as the
general `multiplicity_differentIdeal_eq_finsum_card_ramificationGroup_sub_one` predicts.

```lean
TauCeti.NumberField.GaussianRationals.finsum_card_ramificationGroup_sub_one_eq_two.{u_1}
  {K : Type u_1} [Field K] [NumberField K] {θ : NumberField.RingOfIntegers K}
  (hmin : minpoly ℤ θ = Polynomial.X ^ 2 + 1) (hgen : ℚ[↑θ] = ⊤)
  (𝔭 : Ideal (NumberField.RingOfIntegers K)) [𝔭.IsPrime] [𝔭.LiesOver (Ideal.span {2})] :
  ∑ᶠ (i : ℕ), (Nat.card ↥(Ideal.ramificationGroup Gal(K/ℚ) 𝔭 i) - 1) = 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert's formula for a number-field different exponent](../../part-01/number-fields-ramification-frobenius-and-the-lmf/hilberts-formula-for-a-number-field-different-ex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.GaussianRationals.finsum_card_ramificationGroup_sub_one_eq_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/WorkedExamples/GaussianRationals/Ramification/Group.html#TauCeti.NumberField.GaussianRationals.finsum_card_ramificationGroup_sub_one_eq_two).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.GaussianRationals.finsum_card_ramificationGroup_sub_one_eq_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/WorkedExamples/GaussianRationals/Ramification/Group.html#TauCeti.NumberField.GaussianRationals.finsum_card_ramificationGroup_sub_one_eq_two)
- [Source of `TauCeti.NumberField.GaussianRationals.finsum_card_ramificationGroup_sub_one_eq_two` in TauCeti/NumberTheory/NumberField/WorkedExamples/GaussianRationals/Ramification/Group.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/WorkedExamples/GaussianRationals/Ramification/Group.lean#L129)
