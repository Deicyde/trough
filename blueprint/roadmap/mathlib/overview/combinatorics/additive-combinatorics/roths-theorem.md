---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: roth_3ap_theorem_nat
mathlib_file: Mathlib/Combinatorics/Additive/Corner/Roth.lean
---

# Roth's theorem

**Roth's theorem** for `ℕ`.

The maximum density of a 3AP-free set in `{1, ..., n}` goes to zero as `n` tends to infinity.

```lean
roth_3ap_theorem_nat {n : ℕ} (ε : ℝ) (hε : 0 < ε) (hG : cornersTheoremBound (ε / 3) ≤ n)
  (A : Finset ℕ) (hAn : A ⊆ Finset.range n) (hAε : ε * ↑n ≤ ↑A.card) : ¬ThreeAPFree ↑A
```

## Depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Sets without arithmetic progressions](sets-without-arithmetic-progressions.md)

## Proof depends on

- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Freiman homomorphisms](freiman-homomorphisms.md)
- [Regularity lemma](../graph-theory/regularity-lemma.md)
- [Triangle counting lemma](../graph-theory/triangle-counting-lemma.md)

## Sources

- [Mathlib documentation: `roth_3ap_theorem_nat`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/Corner/Roth.html#roth_3ap_theorem_nat)
- [Source of `roth_3ap_theorem_nat` in Mathlib/Combinatorics/Additive/Corner/Roth.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/Corner/Roth.lean#L155)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L540)
