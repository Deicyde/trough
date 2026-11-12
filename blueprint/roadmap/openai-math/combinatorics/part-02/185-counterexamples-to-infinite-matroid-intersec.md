---
declaration: section
origin: cited
lean: OAI.InfiniteMatroidCounterexample.main, OAI.InfiniteMatroidCounterexample.partitional_intersection_counterexample, OAI.InfiniteMatroidCounterexample.separate_covering_packing_counterexamples
statement: formalized
proof: formalized
---

# 185. Counterexamples to infinite matroid intersection and packing/covering

1 manuscript and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Disproves the unrestricted infinite matroid intersection and packing/covering conjectures in ZFC, using two self-dual partitional matroids on a countably infinite ground set. The same examples answer Joó’s partitional-matroid question negatively. They are neither finitary nor cofinitary, so Nash-Williams’ original finitary conjecture remains outside the result.

## A Counterexample to the Infinite Matroid Packing/Covering Conjecture

We construct in ZFC two self-dual partitional matroids on a countably infinite common ground set that admit neither a packing/covering partition nor an intersection witness. This disproves the unrestricted infinite matroid packing/covering and intersection conjectures and answers Joó's question for two partitional matroids negatively. The examples are neither finitary nor cofinitary.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-Counterexample-to-the-Infinite-Matroid-Packing-Covering-Conjecture-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The infinite matroid packing/covering conjecture predicts a partition of a common ground set into parts admitting the corresponding packing and covering. The formalization constructs two self-dual partitional matroids on one countably infinite ground set that admit neither an independent covering nor a packing/covering partition. The same pair has no intersection witness, so it also refutes the unrestricted infinite matroid intersection conjecture.

Separate formalized consequences give counterexamples to the individual covering and packing conjectures. The construction is in ordinary set theory with Choice and assumes no finitary restriction on the matroids.

## Lean: Infinite matroid packing/covering counterexample

Stated in [InfiniteMatroid.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InfiniteMatroid.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main :
    Countable E ∧ Infinite E ∧
    ∃ M₀ M₁ : Matroid E,
      M₀.E = Set.univ ∧ M₁.E = Set.univ ∧
      M₀.dual = M₀ ∧ M₁.dual = M₁ ∧
      (∀ I₀ I₁ : Set E, M₀.Indep I₀ → M₁.Indep I₁ → I₀ ∪ I₁ ≠ Set.univ) ∧
      ¬ HasPackingCovering M₀ M₁
```

Proved in [lean/OAI/Combinatorics/InfiniteMatroid/Main.lean, line 12](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/InfiniteMatroid/Main.lean#L12).

## Lean: Partitional intersection, covering, and packing counterexamples

Stated in [InfiniteMatroidCorollaries.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/InfiniteMatroidCorollaries.lean).

```lean
theorem partitional_intersection_counterexample :
    Countable E ∧ Infinite E ∧
    ∃ Q : Matroid E0, Q.E = univ ∧ Q.dual = Q ∧ IsUniform Q ∧
      let M₀ := rayMatroid Q false
      let M₁ := rayMatroid Q true
      M₀.E = univ ∧ M₁.E = univ ∧ M₀.dual = M₀ ∧ M₁.dual = M₁ ∧
      IsPartitional M₀ ∧ IsPartitional M₁ ∧
      (∀ I₀ I₁ : Set E, M₀.Indep I₀ → M₁.Indep I₁ → I₀ ∪ I₁ ≠ univ) ∧
      ¬ HasPackingCovering M₀ M₁ ∧ ¬ HasIntersection M₀ M₁
```

Proved in [lean/OAI/Combinatorics/InfiniteMatroid/Corollaries.lean, line 11](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/InfiniteMatroid/Corollaries.lean#L11).

```lean
theorem separate_covering_packing_counterexamples :
    (∃ (F : Set E) (M : Bool → Matroid E),
      (∀ i, (M i).E = F) ∧ ¬ CoveringConjectureFor F M) ∧
    (∃ (F : Set E) (M : Bool → Matroid E),
      (∀ i, (M i).E = F) ∧ ¬ PackingConjectureFor F M)
```

Proved in [lean/OAI/Combinatorics/InfiniteMatroid/SeparateCounterexamples.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/InfiniteMatroid/SeparateCounterexamples.lean#L10).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/185.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/185.md)
