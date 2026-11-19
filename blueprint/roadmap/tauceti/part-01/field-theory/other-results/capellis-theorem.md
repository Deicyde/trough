---
declaration: theorem
origin: cited
lean: TauCeti.X_pow_sub_C_irreducible_iff_forall_prime, TauCeti.X_pow_sub_C_irreducible_of_forall_prime
statement: formalized
proof: formalized
---

# Capelli's theorem

Over any field `K` and for `n ≠ 0`, the binomial `Xⁿ - a` is
irreducible if and only if `a` is not a `p`-th power for any prime `p ∣ n` and, when `4 ∣ n`,
`a` is not of the form `-4b⁴`. For odd `n` this is Mathlib's
`irreducible_X_pow_sub_C_iff_forall_prime_of_odd`.

```lean
TauCeti.X_pow_sub_C_irreducible_iff_forall_prime.{u_1} {K : Type u_1} [Field K] {n : ℕ} (hn : n ≠ 0)
  {a : K} :
  Irreducible (Polynomial.X ^ n - Polynomial.C a) ↔
    (∀ (p : ℕ), Nat.Prime p → p ∣ n → ∀ (b : K), b ^ p ≠ a) ∧ (4 ∣ n → ∀ (b : K), -4 * b ^ 4 ≠ a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The two-power case of Capelli's theorem](the-two-power-case-of-capellis-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.X_pow_sub_C_irreducible_iff_forall_prime`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Kummer/Capelli.html#TauCeti.X_pow_sub_C_irreducible_iff_forall_prime).

## Other forms

**Capelli's theorem, sufficiency.** Formalized in Tau Ceti as [`TauCeti.X_pow_sub_C_irreducible_of_forall_prime`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Kummer/Capelli.html#TauCeti.X_pow_sub_C_irreducible_of_forall_prime).

```lean
TauCeti.X_pow_sub_C_irreducible_of_forall_prime.{u_1} {K : Type u_1} [Field K] {n : ℕ} (hn : n ≠ 0)
  {a : K} (ha : ∀ (p : ℕ), Nat.Prime p → p ∣ n → ∀ (b : K), b ^ p ≠ a)
  (ha' : 4 ∣ n → ∀ (b : K), -4 * b ^ 4 ≠ a) : Irreducible (Polynomial.X ^ n - Polynomial.C a)
```

## Sources

- [Tau Ceti documentation: `TauCeti.X_pow_sub_C_irreducible_iff_forall_prime`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Kummer/Capelli.html#TauCeti.X_pow_sub_C_irreducible_iff_forall_prime)
- [Source of `TauCeti.X_pow_sub_C_irreducible_iff_forall_prime` in TauCeti/FieldTheory/Kummer/Capelli.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/Kummer/Capelli.lean#L191)
