---
declaration: theorem
origin: cited
lean: TauCeti.exists_card_le_card_add_of_hasDerivAt
statement: formalized
proof: formalized
---

# Iterated Rolle's theorem

Let `F (n + 1)` be the derivative of `F n` for every `n < k`.
Then every finite set `Z` of zeros of `F 0` has at most `k` more points than some finite set of
zeros of `F k`.

```lean
TauCeti.exists_card_le_card_add_of_hasDerivAt {F : ℕ → ℝ → ℝ} {k : ℕ}
  (hF : ∀ n < k, ∀ (x : ℝ), HasDerivAt (F n) (F (n + 1) x) x) {Z : Finset ℝ}
  (hZ : ∀ x ∈ Z, F 0 x = 0) : ∃ Z', (∀ x ∈ Z', F k x = 0) ∧ Z.card ≤ Z'.card + k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rolle's theorem for finitely many zeros](rolles-theorem-for-finitely-many-zeros.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_card_le_card_add_of_hasDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalExtr/Rolle.html#TauCeti.exists_card_le_card_add_of_hasDerivAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_card_le_card_add_of_hasDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalExtr/Rolle.html#TauCeti.exists_card_le_card_add_of_hasDerivAt)
- [Source of `TauCeti.exists_card_le_card_add_of_hasDerivAt` in TauCeti/Analysis/Calculus/LocalExtr/Rolle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/LocalExtr/Rolle.lean#L93)
