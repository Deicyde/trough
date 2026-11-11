---
declaration: theorem
origin: cited
lean: TauCeti.lt_pow_sub_pow_div_add_pow
statement: formalized
proof: formalized
---

# TauCeti.lt_pow_sub_pow_div_add_pow

Outside `(a, b, n) = (2, 1, 3)`, every positive integral power of
`(a ^ n - b ^ n) / (a + b)` exceeds `n`, for positive natural bases `b < a` and `n ≥ 3`.

```lean
TauCeti.lt_pow_sub_pow_div_add_pow.{u_1} {K : Type u_1} [Field K] [LinearOrder K]
  [IsStrictOrderedRing K] {a b n k : ℕ} (hb : 0 < b) (hba : b < a) (hn : 3 ≤ n)
  (hex : ¬(a = 2 ∧ b = 1 ∧ n = 3)) (hk : 0 < k) : ↑n < ((↑a ^ n - ↑b ^ n) / (↑a + ↑b)) ^ k
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.lt_pow_sub_pow_div_add_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/Estimates.html#TauCeti.lt_pow_sub_pow_div_add_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.lt_pow_sub_pow_div_add_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/PrimitivePrimeDivisors/Estimates.html#TauCeti.lt_pow_sub_pow_div_add_pow)
- [Source of `TauCeti.lt_pow_sub_pow_div_add_pow` in TauCeti/NumberTheory/PrimitivePrimeDivisors/Estimates.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/PrimitivePrimeDivisors/Estimates.lean#L64)
- [Tau Ceti roadmap status: Primitive prime divisors and the Bang–Zsigmondy theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PrimitivePrimeDivisors/STATUS.md)
