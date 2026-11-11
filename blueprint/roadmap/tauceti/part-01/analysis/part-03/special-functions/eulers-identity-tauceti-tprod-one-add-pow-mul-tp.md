---
declaration: theorem
origin: cited
lean: TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd
statement: formalized
proof: formalized
---

# Euler's identity (`TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd`)

**Euler's identity** `∏_{n ≥ 1} (1 + qⁿ) ∏_{n ≥ 0} (1 - q^{2n+1}) = 1` for `‖q‖ < 1`. Comparing
coefficients, partitions into distinct parts and partitions into odd parts are equinumerous.

```lean
TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd.{u_1} {𝕜 : Type u_1} [NormedField 𝕜]
  [CompleteSpace 𝕜] {q : 𝕜} (hq : ‖q‖ < 1) :
  (∏' (n : ℕ), (1 + q ^ (n + 1))) * ∏' (n : ℕ), (1 - q ^ (2 * n + 1)) = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/QPochhammer.html#TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd).

## Sources

- [Tau Ceti documentation: `TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/QPochhammer.html#TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd)
- [Source of `TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd` in TauCeti/Analysis/SpecialFunctions/QPochhammer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/QPochhammer.lean#L381)
