---
declaration: theorem
origin: cited
lean: TauCeti.IsAutomatic.exists_periodic_tail, TauCeti.isAutomatic_and_isAutomatic_iff
statement: formalized
proof: formalized
---

# Cobham's theorem

Let `k, l ≥ 2` be multiplicatively independent, that is,
`k ^ m ≠ l ^ n` for all `m, n ≥ 1`. A sequence that is both `k`-automatic and `l`-automatic is
eventually periodic: there are `N` and `p > 0` with `a (t + p) = a t` for every `t ≥ N`.

```lean
TauCeti.IsAutomatic.exists_periodic_tail.{u} {k l : ℕ} [NeZero k] [NeZero l] {Δ : Type u}
  {a : ℕ → Δ} (hk : 2 ≤ k) (hl : 2 ≤ l) (hind : ∀ (m n : ℕ), 0 < m → 0 < n → k ^ m ≠ l ^ n)
  (hak : TauCeti.IsAutomatic k a) (hal : TauCeti.IsAutomatic l a) :
  ∃ N p, 0 < p ∧ ∀ (t : ℕ), N ≤ t → a (t + p) = a t
```

## Depends on

- [TauCeti.IsAutomatic](../../number-theory/part-01/classical-arithmetic-sequences-polynomials-and-r/tauceti-isautomatic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsAutomatic.exists_periodic_tail`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Cobham.html#TauCeti.IsAutomatic.exists_periodic_tail).

## Other forms

**Cobham's theorem, as an equivalence.** Formalized in Tau Ceti as [`TauCeti.isAutomatic_and_isAutomatic_iff`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Cobham.html#TauCeti.isAutomatic_and_isAutomatic_iff).

```lean
TauCeti.isAutomatic_and_isAutomatic_iff.{u} {k l : ℕ} [NeZero k] [NeZero l] {Δ : Type u} {a : ℕ → Δ}
  (hk : 2 ≤ k) (hl : 2 ≤ l) (hind : ∀ (m n : ℕ), 0 < m → 0 < n → k ^ m ≠ l ^ n) :
  TauCeti.IsAutomatic k a ∧ TauCeti.IsAutomatic l a ↔
    ∃ N p, 0 < p ∧ ∀ (t : ℕ), N ≤ t → a (t + p) = a t
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsAutomatic.exists_periodic_tail`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Cobham.html#TauCeti.IsAutomatic.exists_periodic_tail)
- [Source of `TauCeti.IsAutomatic.exists_periodic_tail` in TauCeti/Computability/AutomaticSequence/Cobham.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/AutomaticSequence/Cobham.lean#L85)
