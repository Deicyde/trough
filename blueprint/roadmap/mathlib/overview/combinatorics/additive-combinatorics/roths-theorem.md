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
- [Permutation group of a type](../../general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Regularity lemma](../graph-theory/regularity-lemma.md)
- [Triangle counting lemma](../graph-theory/triangle-counting-lemma.md)

## Sources

- [Mathlib documentation: `roth_3ap_theorem_nat`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Combinatorics/Additive/Corner/Roth.html#roth_3ap_theorem_nat)
- [Source of `roth_3ap_theorem_nat` in Mathlib/Combinatorics/Additive/Corner/Roth.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Combinatorics/Additive/Corner/Roth.lean#L155)
- [Mathlib overview: Combinatorics › Additive combinatorics](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/overview.yaml#L540)
