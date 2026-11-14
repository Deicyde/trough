---
declaration: section
origin: cited
lean: OAI.NaimarkZFC.main
statement: formalized
proof: formalized
---

# 297. A ZFC counterexample to Naimark's problem

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Gives an alternative to [Tanaka's ZFC construction](https://arxiv.org/abs/2609.26930v1) of a unital infinite-dimensional simple complex $C^{∗}$-algebra with a faithful tracial state and exactly one nonzero irreducible representation up to unitary equivalence. Thus the unrestricted compact-operator characterization fails without additional set-theoretic assumptions; the counterexample is nonseparable.

## A counterexample to Naimark's problem in ZFC

We construct in ZFC a unital infinite-dimensional simple complex $C^{∗}$-algebra with a faithful tracial state whose nonzero irreducible representations are all unitarily equivalent. This gives a negative answer to Naimark's problem without additional set-theoretic assumptions.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-counterexample-to-Naimarks-problem-in-ZFC-September-24-2026/naimark-counterexample-zfc.pdf); the Lean below formalizes results from it.

## The Lean formalization

Naimark's problem asks whether a $C^*$-algebra whose nonzero irreducible representations are all unitarily equivalent must be an algebra of compact operators. The formalization gives a counterexample in ZFC: a unital infinite-dimensional simple complex $C^*$-algebra with a faithful tracial state has that uniqueness property for irreducible representations but is not isomorphic to the compact operators on any Hilbert space. No additional set-theoretic assumption is used.

## Lean: Counterexample to Naimark's problem in ZFC

```lean
theorem main :
    ∃ (A : Type u) (_ : CStarAlgebra A),
      IsSimpleCStar A ∧ ¬ FiniteDimensional ℂ A ∧
      (∃ τ : A →L[ℂ] ℂ, IsFaithfulTracialState τ) ∧
      HasUniqueIrreducibleRepresentation.{u, v, w} A ∧
      ∀ (H : Type v) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H],
        ¬ IsIsomorphicToCompacts A H
```

Stated in [Naimark.lean, line 44](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Naimark.lean#L44). Proved in [lean/OAI/Analysis/Naimark/Tracial.lean, line 243](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/Naimark/Tracial.lean#L243).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/297.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/297.md)
