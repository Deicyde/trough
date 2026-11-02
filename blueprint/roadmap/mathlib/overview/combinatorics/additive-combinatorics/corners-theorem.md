---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: corners_theorem_nat
mathlib_file: Mathlib/Combinatorics/Additive/Corner/Roth.lean
---

# Corners theorem

The **corners theorem** for `ℕ`.

The maximum density of a corner-free set in `{1, ..., n} × {1, ..., n}` goes to zero as `n` tends to
infinity.

```lean
corners_theorem_nat {n : ℕ} {ε : ℝ} (hε : 0 < ε) (hn : cornersTheoremBound (ε / 9) ≤ n)
  (A : Finset (ℕ × ℕ)) (hAn : A ⊆ Finset.range n ×ˢ Finset.range n) (hAε : ε * ↑n ^ 2 ≤ ↑A.card) :
  ¬IsCornerFree ↑A
```

## Depends on

- [Logarithm](../../analysis/special-functions/logarithm.md)

## Proof depends on

- [Affine space](../../geometry/affine-and-euclidean-geometry/affine-space.md)
- [Characteristic zero](../../general-algebra/field-theory/characteristic-zero.md)
- [Freiman homomorphisms](freiman-homomorphisms.md)
- [Simple graph](../graph-theory/simple-graph.md)

## Sources

- [Mathlib documentation: `corners_theorem_nat`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/Corner/Roth.html#corners_theorem_nat)
- [Source of `corners_theorem_nat` in Mathlib/Combinatorics/Additive/Corner/Roth.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Combinatorics/Additive/Corner/Roth.lean#L96)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L541)
- [1000+ theorems list: Q5171652](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L3080)
- [1000+ theorems project: Q5171652](https://1000-plus.github.io/all.html?length=-1#Q5171652)
- [Wikipedia: Corners theorem](https://en.wikipedia.org/wiki/Corners_theorem)
- [Wikidata: Q5171652](https://www.wikidata.org/wiki/Q5171652)
