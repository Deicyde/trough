---
declaration: theorem
origin: cited
lean: TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one
statement: formalized
proof: formalized
---

# Serre's lemma (`TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one`)

Let `p` be a prime and `A` a ring with no `p`-torsion in which only `0` is
divisible by every power of `p`. An element of finite order of `A` that is congruent to `1` modulo
`p ^ k`, with `p ^ k ≥ 3`, is equal to `1`.

```lean
TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one.{u_1} {A : Type u_1} [Ring A] {p : ℕ}
  (hp : Nat.Prime p) (hreg : IsLeftRegular ↑p) (hsep : ∀ (x : A), (∀ (j : ℕ), ↑p ^ j ∣ x) → x = 0)
  {k : ℕ} (hk : 3 ≤ p ^ k) {a : A} (ha : IsOfFinOrder a) (hdvd : ↑p ^ k ∣ a - 1) : a = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/RootsOfUnity/Congruence.html#TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one).

## Sources

- [Tau Ceti documentation: `TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/RootsOfUnity/Congruence.html#TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one)
- [Source of `TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one` in TauCeti/RingTheory/RootsOfUnity/Congruence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/RootsOfUnity/Congruence.lean#L134)
