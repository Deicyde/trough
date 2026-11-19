---
declaration: theorem
origin: cited
lean: Chebyshev.exists_abs_sum_primesLE_one_div_sub_log_log_sub_le, Chebyshev.exists_abs_sum_vonMangoldt_div_mul_log_sub_log_log_sub_le
statement: formalized
proof: formalized
---

# Mertens' second theorem

There is a constant `B` such that for every real `x ≥ 2`,
`|∑_{p ≤ x} 1 / p - log log x - B| ≤ 2 (log 4 + 4) / log x`, the sum running over the primes in
`Nat.primesLE ⌊x⌋₊`. The constant is `TauCeti.LFunctions.mertensConstant ℚ`
(`TauCeti.LFunctions.abs_sum_primesLE_one_div_sub_log_log_sub_mertensConstant_le`).

```lean
Chebyshev.exists_abs_sum_primesLE_one_div_sub_log_log_sub_le :
  ∃ B,
    ∀ (x : ℝ),
      2 ≤ x →
        |∑ p ∈ ⌊x⌋₊.primesLE, 1 / ↑p - Real.log (Real.log x) - B| ≤
          2 * (Real.log 4 + 4) / Real.log x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Mertens' first theorem](mertens-first-theorem.md)

## Lean

Formalized in Tau Ceti as [`Chebyshev.exists_abs_sum_primesLE_one_div_sub_log_log_sub_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.exists_abs_sum_primesLE_one_div_sub_log_log_sub_le).

## Other forms

**Mertens' second theorem in von Mangoldt form.** Formalized in Tau Ceti as [`Chebyshev.exists_abs_sum_vonMangoldt_div_mul_log_sub_log_log_sub_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.exists_abs_sum_vonMangoldt_div_mul_log_sub_log_log_sub_le).

```lean
Chebyshev.exists_abs_sum_vonMangoldt_div_mul_log_sub_log_log_sub_le :
  ∃ B,
    ∀ (x : ℝ),
      2 ≤ x →
        |∑ n ∈ Finset.Icc 2 ⌊x⌋₊, ArithmeticFunction.vonMangoldt n / (↑n * Real.log ↑n) -
                Real.log (Real.log x) -
              B| ≤
          2 * (Real.log 4 + 4) / Real.log x
```

## Sources

- [Tau Ceti documentation: `Chebyshev.exists_abs_sum_primesLE_one_div_sub_log_log_sub_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.exists_abs_sum_primesLE_one_div_sub_log_log_sub_le)
- [Source of `Chebyshev.exists_abs_sum_primesLE_one_div_sub_log_log_sub_le` in TauCeti/NumberTheory/Chebyshev/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebyshev/Mertens.lean#L382)
