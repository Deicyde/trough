---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.Sqrt2.regulator_le_four_mul_absLogHeight₁_one_add, TauCeti.NumberField.Units.regulator_le_prod_sum_abs_logEmbedding, TauCeti.NumberField.Units.regOfFamily_le_prod_sum_abs_logEmbedding, TauCeti.NumberField.Units.regOfFamily_le_prod_sum_mult_mul_abs_log, TauCeti.NumberField.Units.regulator_le_prod_sum_mult_mul_abs_log
statement: formalized
proof: formalized
---

# Hadamard's bound at `ℚ(√2)`

The regulator is at most `(2d) ^ r = 4` times the absolute
logarithmic height of the fundamental unit; here `log (1 + √2) ≤ 4 · log (1 + √2) / 2`.

```lean
TauCeti.NumberField.Sqrt2.regulator_le_four_mul_absLogHeight₁_one_add.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {θ : NumberField.RingOfIntegers K} (hmin : minpoly ℤ θ = Polynomial.X ^ 2 - 2)
  (hgen : ℚ[↑θ] = ⊤) : NumberField.Units.regulator K ≤ 4 * NumberField.absLogHeight₁ ↑(1 + θ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hadamard's bound, `ℓ¹` row form](../../part-01/heights-units-and-s-units-of-number-fields/part-01/hadamards-bound-l1-row-form.md)
- [Soundness of unit-candidate elimination](../../part-01/number-fields-ramification-frobenius-and-the-lmf/soundness-of-unit-candidate-elimination.md)

## Informally uses

- [TauCeti.NumberField.Units.regulator_le_prod_absLogHeight₁](../../part-01/heights-units-and-s-units-of-number-fields/part-01/tauceti-numberfield-units-regulator-le-prod-absl.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.Sqrt2.regulator_le_four_mul_absLogHeight₁_one_add`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/WorkedExamples/Sqrt2/Units.html#TauCeti.NumberField.Sqrt2.regulator_le_four_mul_absLogHeight%E2%82%81_one_add).

## Other forms

**Hadamard's bound for the regulator.** Formalized in Tau Ceti as [`TauCeti.NumberField.Units.regulator_le_prod_sum_abs_logEmbedding`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Regulator/Basic.html#TauCeti.NumberField.Units.regulator_le_prod_sum_abs_logEmbedding).

```lean
TauCeti.NumberField.Units.regulator_le_prod_sum_abs_logEmbedding.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {ε : Fin (NumberField.Units.rank K) → (NumberField.RingOfIntegers K)ˣ}
  (hε : Subgroup.closure (Set.range ε) ⊔ NumberField.Units.torsion K = ⊤) :
  NumberField.Units.regulator K ≤
    ∏ i, ∑ w, |(NumberField.Units.logEmbedding K) (Additive.ofMul (ε i)) w|
```

**Hadamard's bound for the regulator of a family.** Formalized in Tau Ceti as [`TauCeti.NumberField.Units.regOfFamily_le_prod_sum_abs_logEmbedding`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Regulator/Basic.html#TauCeti.NumberField.Units.regOfFamily_le_prod_sum_abs_logEmbedding).

```lean
TauCeti.NumberField.Units.regOfFamily_le_prod_sum_abs_logEmbedding.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (u : Fin (NumberField.Units.rank K) → (NumberField.RingOfIntegers K)ˣ) :
  NumberField.Units.regOfFamily u ≤
    ∏ i, ∑ w, |(NumberField.Units.logEmbedding K) (Additive.ofMul (u i)) w|
```

**Hadamard's bound for the regulator of a family, over all places.** Formalized in Tau Ceti as [`TauCeti.NumberField.Units.regOfFamily_le_prod_sum_mult_mul_abs_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Regulator/Basic.html#TauCeti.NumberField.Units.regOfFamily_le_prod_sum_mult_mul_abs_log).

```lean
TauCeti.NumberField.Units.regOfFamily_le_prod_sum_mult_mul_abs_log.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (u : Fin (NumberField.Units.rank K) → (NumberField.RingOfIntegers K)ˣ) :
  NumberField.Units.regOfFamily u ≤
    ∏ i, ∑ w, ↑w.mult * |Real.log (w ((algebraMap (NumberField.RingOfIntegers K) K) ↑(u i)))|
```

**Hadamard's bound for the regulator, over all places.** Formalized in Tau Ceti as [`TauCeti.NumberField.Units.regulator_le_prod_sum_mult_mul_abs_log`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Units/Regulator/Basic.html#TauCeti.NumberField.Units.regulator_le_prod_sum_mult_mul_abs_log).

```lean
TauCeti.NumberField.Units.regulator_le_prod_sum_mult_mul_abs_log.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {ε : Fin (NumberField.Units.rank K) → (NumberField.RingOfIntegers K)ˣ}
  (hε : Subgroup.closure (Set.range ε) ⊔ NumberField.Units.torsion K = ⊤) :
  NumberField.Units.regulator K ≤
    ∏ i, ∑ w, ↑w.mult * |Real.log (w ((algebraMap (NumberField.RingOfIntegers K) K) ↑(ε i)))|
```

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.Sqrt2.regulator_le_four_mul_absLogHeight₁_one_add`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/WorkedExamples/Sqrt2/Units.html#TauCeti.NumberField.Sqrt2.regulator_le_four_mul_absLogHeight%E2%82%81_one_add)
- [Source of `TauCeti.NumberField.Sqrt2.regulator_le_four_mul_absLogHeight₁_one_add` in TauCeti/NumberTheory/NumberField/WorkedExamples/Sqrt2/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/WorkedExamples/Sqrt2/Units.lean#L165)
