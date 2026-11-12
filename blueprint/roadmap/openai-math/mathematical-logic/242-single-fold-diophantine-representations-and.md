---
declaration: section
origin: cited
lean: OAI.SingleFold.main
statement: formalized
proof: formalized
---

# 242. Single-fold Diophantine representations and undecidability under an at-most-one-solution promise

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Every recursively enumerable set of tuples of natural numbers has a Diophantine representation with exactly one auxiliary solution for each member and none for nonmembers. This proves the single-fold conjecture and hence the finite-fold conjecture. Diophantine solvability over the nonnegative integers remains undecidable even with an at-most-one-solution promise.

## Single-fold Diophantine representations

Every recursively enumerable set of natural-number tuples has a polynomial Diophantine representation with exactly one complete auxiliary tuple for each member. This proves the single-fold conjecture and, consequently, the finite-fold conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Single-fold-Diophantine-representations-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The single-fold Diophantine conjecture asks whether every recursively enumerable set has a polynomial representation with a unique auxiliary witness for each member. The formalization establishes this for every recursively enumerable subset of $\mathbb N^n$, $n\ge1$: an integer polynomial has exactly one complete natural-number witness tuple for members and none for nonmembers.

The consequence that solvability remains undecidable under an at-most-one-solution promise is not separately formalized.

## Lean: Single-fold Diophantine representations

Stated in [SingleFold.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SingleFold.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main : MainStatement
```

Proved in [lean/OAI/NumberTheory/SingleFold/Main.lean, line 21](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/NumberTheory/SingleFold/Main.lean#L21).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/242.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/242.md)
