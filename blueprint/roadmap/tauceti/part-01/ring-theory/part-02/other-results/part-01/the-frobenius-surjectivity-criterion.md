---
declaration: theorem
origin: cited
lean: TauCeti.tfae_forall_exists_dvd_sub_pow
statement: formalized
proof: formalized
---

# The Frobenius surjectivity criterion

**The Frobenius surjectivity criterion** (Bhatt–Morrow–Scholze, *Integral p-adic Hodge
theory*, Lemma 3.9). In a `π`-adically complete and separated ring `A` with `π ^ p ∣ p`, the
following are equivalent: every element of `A` is a `p`-th power modulo `π ^ p`, modulo `p`, and
modulo `π p`.

```lean
TauCeti.tfae_forall_exists_dvd_sub_pow.{u_1} {A : Type u_1} [CommRing A] (π : A) {p : ℕ}
  [Fact (Nat.Prime p)] [IsHausdorff (Ideal.span {π}) A] [IsPrecomplete (Ideal.span {π}) A]
  (h : π ^ p ∣ ↑p) :
  [∀ (x : A), ∃ y, π ^ p ∣ x - y ^ p, ∀ (x : A), ∃ y, ↑p ∣ x - y ^ p,
      ∀ (x : A), ∃ y, π * ↑p ∣ x - y ^ p].TFAE
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tfae_forall_exists_dvd_sub_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicCompletion/Frobenius.html#TauCeti.tfae_forall_exists_dvd_sub_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.tfae_forall_exists_dvd_sub_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicCompletion/Frobenius.html#TauCeti.tfae_forall_exists_dvd_sub_pow)
- [Source of `TauCeti.tfae_forall_exists_dvd_sub_pow` in TauCeti/RingTheory/AdicCompletion/Frobenius.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/AdicCompletion/Frobenius.lean#L136)
