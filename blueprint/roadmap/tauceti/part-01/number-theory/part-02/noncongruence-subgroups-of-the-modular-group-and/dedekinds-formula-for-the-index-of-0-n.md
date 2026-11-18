---
declaration: theorem
origin: cited
lean: CongruenceSubgroup.Gamma0_index_mul_prod_primeFactors
statement: formalized
proof: formalized
---

# Dedekind's formula for the index of `Γ₀(N)`

`[SL₂(ℤ) : Γ₀(N)] = N ∏_{p ∣ N} (1 + 1/p)`, with the denominators cleared.

At level zero both sides vanish, since `Γ₀(0)` has infinite index.
The proof is adapted from Mathlib's `Nat.totient_mul_prod_primeFactors`.

```lean
CongruenceSubgroup.Gamma0_index_mul_prod_primeFactors {N : ℕ} :
  (CongruenceSubgroup.Gamma0 N).index * ∏ p ∈ N.primeFactors, p = N * ∏ p ∈ N.primeFactors, (p + 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CongruenceSubgroup.Gamma0_index_mul_prod_primeFactors`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Basic.html#CongruenceSubgroup.Gamma0_index_mul_prod_primeFactors).

## Sources

- [Tau Ceti documentation: `CongruenceSubgroup.Gamma0_index_mul_prod_primeFactors`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Basic.html#CongruenceSubgroup.Gamma0_index_mul_prod_primeFactors)
- [Source of `CongruenceSubgroup.Gamma0_index_mul_prod_primeFactors` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Basic.lean#L1114)
