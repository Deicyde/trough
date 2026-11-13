---
declaration: theorem
origin: cited
lean: Erdos14.erdos_14.parts.i, Erdos14.erdos_14.parts.ii
statement: formalized
---

# Erdős Problem 14

> *Reference:* [erdosproblems.com/14](https://www.erdosproblems.com/14)

*Quoted from [FormalConjectures/ErdosProblems/14.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/14.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/14](https://www.erdosproblems.com/14).

The file states 2 research or textbook statements: 2 open.

## `Erdos14.erdos_14.parts.i`

Open: stated without proof.

> Let $A ⊆ \mathbb{N}$. Let $B ⊆ \mathbb{N}$ be the set of integers which are representable
> in exactly one way as the sum of two elements from $A$. Is it true that for all
> $\epsilon > 0$ and large $N$, $|\{1,\ldots,N\} \setminus B| \gg_\epsilon N^{1/2 - \epsilon}$?

```lean
theorem erdos_14.parts.i :
    ∀ A, ∀ ε > 0, nonUniqueSumCount A ≫ almostSquareRoot ε
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/14.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/14.lean#L54).

## `Erdos14.erdos_14.parts.ii`

Open: stated without proof.

> Is it possible that $|\{1,\ldots,N\} \setminus B| = o(N^\frac{1}{2})$?

```lean
theorem erdos_14.parts.ii :
    ∃ (A : Set ℕ), IsLittleO atTop (nonUniqueSumCount A) squareRoot
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/14.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/14.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/14.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/14.lean)
- [erdosproblems.com/14](https://www.erdosproblems.com/14)
