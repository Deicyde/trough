---
declaration: theorem
origin: cited
lean: TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow, TauCeti.isSolvable_of_card_dvd_prime_pow_mul_prime_pow
statement: formalized
proof: formalized
---

# Burnside's `pᵃqᵇ` theorem

a finite group of order `pᵃqᵇ`, for primes `p` and `q`, is
solvable.

```lean
TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow.{u} {G : Type u} [Group G] [Finite G]
  {p q : ℕ} (hp : Nat.Prime p) (hq : Nat.Prime q) {a b : ℕ} (h : Nat.card G = p ^ a * q ^ b) :
  Group.IsSolvable G
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's vanishing theorem](burnsides-vanishing-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Solvable.html#TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow).

## Other forms

**Burnside's `pᵃqᵇ` theorem, in the form the induction runs in.** Formalized in Tau Ceti as [`TauCeti.isSolvable_of_card_dvd_prime_pow_mul_prime_pow`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Solvable.html#TauCeti.isSolvable_of_card_dvd_prime_pow_mul_prime_pow).

```lean
TauCeti.isSolvable_of_card_dvd_prime_pow_mul_prime_pow.{u} {G : Type u} [Group G] [Finite G]
  {p q : ℕ} (hp : Nat.Prime p) (hq : Nat.Prime q) {a b : ℕ} (h : Nat.card G ∣ p ^ a * q ^ b) :
  Group.IsSolvable G
```

## Sources

- [Tau Ceti documentation: `TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/Solvable.html#TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow)
- [Source of `TauCeti.isSolvable_of_card_eq_prime_pow_mul_prime_pow` in TauCeti/RepresentationTheory/CharacterTable/Solvable.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/CharacterTable/Solvable.lean#L217)
