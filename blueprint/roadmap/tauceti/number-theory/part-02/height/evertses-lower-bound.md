---
declaration: theorem
origin: cited
lean: TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm, TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm_of_mem_rootSet
statement: formalized
proof: formalized
---

# Evertse's lower bound

A nonzero algebraic number `z ∈ ℂ` of degree `d` satisfies
`den(z) ^ d * house(z) ^ (d - 1) * ‖z‖ ≥ 1`.

```lean
TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm {z : ℂ} (hz : IsAlgebraic ℚ z)
  (hz0 : z ≠ 0) :
  1 ≤
    ↑(Algebra.natDenominator z) ^ (minpoly ℚ z).natDegree *
        TauCeti.house z ^ ((minpoly ℚ z).natDegree - 1) *
      ‖z‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Denominator.html#TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm).

## Other forms

**Evertse's lower bound for the conjugates of an algebraic number.** Formalized in Tau Ceti as [`TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm_of_mem_rootSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Denominator.html#TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm_of_mem_rootSet).

```lean
TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm_of_mem_rootSet.{u_1} {K : Type u_1}
  [Field K] [CharZero K] {z : K} {w : ℂ} (hz : IsAlgebraic ℚ z) (hz0 : z ≠ 0)
  (hw : w ∈ (minpoly ℚ z).rootSet ℂ) :
  1 ≤
    ↑(Algebra.natDenominator z) ^ (minpoly ℚ z).natDegree *
        TauCeti.house z ^ ((minpoly ℚ z).natDegree - 1) *
      ‖w‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Height/Denominator.html#TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm)
- [Source of `TauCeti.one_le_natDenominator_pow_mul_house_pow_mul_norm` in TauCeti/NumberTheory/Height/Denominator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Height/Denominator.lean#L131)
