---
declaration: theorem
origin: cited
lean: Chebyshev.abs_sum_primesLE_log_div_sub_log_le, Chebyshev.abs_sum_primesLE_filter_lt_log_div_sub_log_le, Chebyshev.abs_sum_vonMangoldt_div_sub_log_le
statement: formalized
proof: formalized
---

# Mertens' first theorem

For every real `x ≥ 1`,
`|∑_{p ≤ x} log p / p - log x| ≤ log 4 + 4`.

```lean
Chebyshev.abs_sum_primesLE_log_div_sub_log_le {x : ℝ} (hx : 1 ≤ x) :
  |∑ p ∈ ⌊x⌋₊.primesLE, Real.log ↑p / ↑p - Real.log x| ≤ Real.log 4 + 4
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chebyshev's identity](../../part-01/analytic-number-theory-part-i/chebyshevs-identity.md)

## Lean

Formalized in Tau Ceti as [`Chebyshev.abs_sum_primesLE_log_div_sub_log_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.abs_sum_primesLE_log_div_sub_log_le).

## Other forms

**Mertens' first theorem, strict cutoff.** Formalized in Tau Ceti as [`Chebyshev.abs_sum_primesLE_filter_lt_log_div_sub_log_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.abs_sum_primesLE_filter_lt_log_div_sub_log_le).

```lean
Chebyshev.abs_sum_primesLE_filter_lt_log_div_sub_log_le {x : ℝ} (hx : 1 ≤ x) :
  |∑ p ∈ ⌊x⌋₊.primesLE with ↑p < x, Real.log ↑p / ↑p - Real.log x| ≤ Real.log 4 + 4
```

**Mertens' first theorem, von Mangoldt form.** Formalized in Tau Ceti as [`Chebyshev.abs_sum_vonMangoldt_div_sub_log_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.abs_sum_vonMangoldt_div_sub_log_le).

```lean
Chebyshev.abs_sum_vonMangoldt_div_sub_log_le {x : ℝ} (hx : 1 ≤ x) :
  |∑ n ∈ Finset.Ioc 0 ⌊x⌋₊, ArithmeticFunction.vonMangoldt n / ↑n - Real.log x| ≤ Real.log 4 + 4
```

## Sources

- [Tau Ceti documentation: `Chebyshev.abs_sum_primesLE_log_div_sub_log_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebyshev/Mertens.html#Chebyshev.abs_sum_primesLE_log_div_sub_log_le)
- [Source of `Chebyshev.abs_sum_primesLE_log_div_sub_log_le` in TauCeti/NumberTheory/Chebyshev/Mertens.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Chebyshev/Mertens.lean#L209)
