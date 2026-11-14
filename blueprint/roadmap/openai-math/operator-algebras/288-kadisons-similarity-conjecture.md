---
declaration: section
origin: cited
lean: OAI.KadisonSimilarity.universalCommutatorTheorem, OAI.KadisonSimilarity.universalHyperreflexivity, OAI.KadisonSimilarity.similarityTheorem, OAI.Kadison.uniform_commutator
statement: formalized
proof: formalized
---

# 288. Kadison's similarity conjecture

1 manuscript and 4 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Kadison's similarity conjecture: every bounded complex-linear unital algebra homomorphism from a unital complex $C^{∗}$-algebra to operators on a Hilbert space becomes a $*$-homomorphism after conjugation by a bounded invertible operator.

## Kadison's similarity theorem through uniform derivation estimates

We prove that every bounded complex-linear unital algebra homomorphism from a unital complex $C^{∗}$-algebra into the bounded operators on an arbitrary Hilbert space is similar to a $*$-homomorphism. This resolves Kadison's similarity conjecture positively. We also obtain one universal hyperreflexivity constant for all unital von Neumann algebras on arbitrary complex Hilbert spaces.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Kadisons-similarity-theorem-through-uniform-derivation-estimates-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Kadison's similarity problem asks whether every bounded unital homomorphism from a unital complex $C^*$-algebra into operators on a Hilbert space is similar to a $*$-homomorphism. The formalization proves this for arbitrary Hilbert spaces. It also gives one universal hyperreflexivity constant for all unital von Neumann algebras.

The linked commutator estimate is uniform over all finite matrix amplifications: its constant is independent of the algebra, Hilbert space, and amplification size. This is the quantitative derivation estimate supporting the similarity result.

## Lean: Kadison's similarity theorem and uniform hyperreflexivity

```lean
theorem universalCommutatorTheorem : UniversalCommutatorTheorem.{u}
```

Stated in [KadisonSimilarity.lean, line 107](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KadisonSimilarity.lean#L107). Proved in [lean/OAI/Analysis/KadisonSimilarity/UnconditionalMain.lean, line 19](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/KadisonSimilarity/UnconditionalMain.lean#L19).

```lean
theorem universalHyperreflexivity : UniversalHyperreflexivity.{u} universalConstant
```

Stated in [KadisonSimilarity.lean, line 111](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KadisonSimilarity.lean#L111). Proved in [lean/OAI/Analysis/KadisonSimilarity/UnconditionalMain.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/KadisonSimilarity/UnconditionalMain.lean#L23).

```lean
theorem similarityTheorem : SimilarityTheorem.{u,v}
```

Stated in [KadisonSimilarity.lean, line 115](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/KadisonSimilarity.lean#L115). Proved in [lean/OAI/Analysis/KadisonSimilarity/UnconditionalSimilarity.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/KadisonSimilarity/UnconditionalSimilarity.lean#L16).

## Lean: Uniform amplified commutator estimate

```lean
theorem uniform_commutator :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ (K : Type u) [NormedAddCommGroup K] [InnerProductSpace ℂ K]
      [CompleteSpace K] (P : VonNeumannAlgebra K) (Y : K →L[ℂ] K)
      (h : ℕ), 1 ≤ h → ∀ (X : Matrix (Fin h) (Fin h) (K →L[ℂ] K)),
      (∀ i j, X i j ∈ P) →
      ‖diagonalAmplification h Y * matrixOperator h X -
        matrixOperator h X * diagonalAmplification h Y‖ ≤
        C * commutatorSeminorm P Y * ‖matrixOperator h X‖
```

Stated in [UniformCommutator.lean, line 26](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/UniformCommutator.lean#L26). Proved in [lean/OAI/Analysis/Commutator/UniversalMain.lean, line 16](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Commutator/UniversalMain.lean#L16).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/288.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/288.md)
