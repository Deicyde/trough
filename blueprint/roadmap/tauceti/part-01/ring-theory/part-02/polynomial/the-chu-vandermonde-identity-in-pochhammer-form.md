---
declaration: theorem
origin: cited
lean: TauCeti.sum_neg_one_pow_mul_choose_ascPochhammer
statement: formalized
proof: formalized
---

# The Chu–Vandermonde identity in Pochhammer form

`∑ₖ (−1)ᵏ C(n, k) (b)ₖ (c + k)ₙ₋ₖ = (c − b)ₙ`. It is Mathlib's `Ring.descPochhammer_smeval_add`
at `r = −b`, `s = c + n − 1`, rewritten with ascending Pochhammer symbols.

```lean
TauCeti.sum_neg_one_pow_mul_choose_ascPochhammer.{u_1} {R : Type u_1} [CommRing R] (n : ℕ)
  (b c : R) :
  ∑ k ∈ Finset.range (n + 1),
      (-1) ^ k * ↑(n.choose k) * Polynomial.eval b (ascPochhammer R k) *
        Polynomial.eval (c + ↑k) (ascPochhammer R (n - k)) =
    Polynomial.eval (c - b) (ascPochhammer R n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_neg_one_pow_mul_choose_ascPochhammer`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Pochhammer.html#TauCeti.sum_neg_one_pow_mul_choose_ascPochhammer).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_neg_one_pow_mul_choose_ascPochhammer`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Pochhammer.html#TauCeti.sum_neg_one_pow_mul_choose_ascPochhammer)
- [Source of `TauCeti.sum_neg_one_pow_mul_choose_ascPochhammer` in TauCeti/RingTheory/Polynomial/Pochhammer.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Polynomial/Pochhammer.lean#L352)
