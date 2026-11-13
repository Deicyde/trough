---
declaration: section
origin: cited
lean: OAI.DoublingHilbert.main, OAI.CompactBanach.main
statement: formalized
proof: formalized
---

# 098. Compact counterexamples to bi-Lipschitz dimension reduction

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Every infinite-dimensional real Banach space contains a compact doubling set that admits no bi-Lipschitz embedding into any finite-dimensional normed space. The doubling constant is universal. This answers the Lang–Plaut problem negatively, even for compact subsets of Hilbert space.

## A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding

Every infinite-dimensional real Banach space contains a compact doubling subset that admits no bi-Lipschitz embedding into any finite-dimensional real normed space. The doubling constant has a universal bound, independent of the ambient Banach space. This answers the Lang–Plaut problem negatively, even for compact subsets of Hilbert space.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalized result gives a doubling subset of real $\ell_2$, with doubling constant at most $76800$, that admits no bi-Lipschitz embedding into any finite-dimensional Euclidean space at any finite distortion. A companion gives one universal doubling constant such that every infinite-dimensional real Banach space contains a compact doubling subset with no bi-Lipschitz embedding into any finite-dimensional normed space.

## Lean: Doubling Hilbert subset without finite-dimensional embedding

```lean
theorem main : ∃ S : Set RealL2,
    DoublingAtMost S 76800 ∧
      ∀ k : ℕ, 0 < k → ¬ AdmitsBiLipschitzEmbedding S k
```

Stated in [DoublingHilbert.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DoublingHilbert.lean#L23). Proved in [lean/OAI/Geometry/DoublingHilbert/Main.lean, line 57](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/DoublingHilbert/Main.lean#L57). formalization.yaml lists it as one of the repository's main results.

## Lean: Compact counterexamples in infinite-dimensional Banach spaces

```lean
theorem main : ∃ Λ : ℕ, ∀ (B : Type u) [NormedAddCommGroup B] [NormedSpace ℝ B]
    [CompleteSpace B], ¬ FiniteDimensional ℝ B →
    ∃ K : Set B, IsCompact K ∧ DoublingAtMost K Λ ∧
      ∀ (E : Type v) [NormedAddCommGroup E] [NormedSpace ℝ E]
        [FiniteDimensional ℝ E], ¬ AdmitsBiLipschitzEmbedding K E
```

Stated in [CompactBanach.lean, line 25](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/CompactBanach.lean#L25). Proved in [lean/OAI/Geometry/DoublingHilbert/CompactBanach.lean, line 20](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Geometry/DoublingHilbert/CompactBanach.lean#L20). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/098.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/098.md)
