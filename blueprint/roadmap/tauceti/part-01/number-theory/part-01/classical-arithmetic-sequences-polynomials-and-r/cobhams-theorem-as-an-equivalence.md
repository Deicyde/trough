---
declaration: theorem
origin: cited
lean: TauCeti.isAutomatic_and_isAutomatic_iff, TauCeti.IsAutomatic.exists_periodic_tail
statement: formalized
proof: formalized
---

# Cobham's theorem, as an equivalence

For multiplicatively independent bases `k, l ≥ 2`,
a sequence is both `k`-automatic and `l`-automatic exactly when it is eventually periodic.

```lean
TauCeti.isAutomatic_and_isAutomatic_iff.{u} {k l : ℕ} [NeZero k] [NeZero l] {Δ : Type u} {a : ℕ → Δ}
  (hk : 2 ≤ k) (hl : 2 ≤ l) (hind : ∀ (m n : ℕ), 0 < m → 0 < n → k ^ m ≠ l ^ n) :
  TauCeti.IsAutomatic k a ∧ TauCeti.IsAutomatic l a ↔
    ∃ N p, 0 < p ∧ ∀ (t : ℕ), N ≤ t → a (t + p) = a t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isAutomatic_and_isAutomatic_iff`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Cobham.html#TauCeti.isAutomatic_and_isAutomatic_iff).

## Other forms

**Cobham's theorem.** Formalized in Tau Ceti as [`TauCeti.IsAutomatic.exists_periodic_tail`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Cobham.html#TauCeti.IsAutomatic.exists_periodic_tail).

```lean
TauCeti.IsAutomatic.exists_periodic_tail.{u} {k l : ℕ} [NeZero k] [NeZero l] {Δ : Type u}
  {a : ℕ → Δ} (hk : 2 ≤ k) (hl : 2 ≤ l) (hind : ∀ (m n : ℕ), 0 < m → 0 < n → k ^ m ≠ l ^ n)
  (hak : TauCeti.IsAutomatic k a) (hal : TauCeti.IsAutomatic l a) :
  ∃ N p, 0 < p ∧ ∀ (t : ℕ), N ≤ t → a (t + p) = a t
```

## Sources

- [Tau Ceti documentation: `TauCeti.isAutomatic_and_isAutomatic_iff`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Cobham.html#TauCeti.isAutomatic_and_isAutomatic_iff)
- [Source of `TauCeti.isAutomatic_and_isAutomatic_iff` in TauCeti/Computability/AutomaticSequence/Cobham.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/AutomaticSequence/Cobham.lean#L108)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
