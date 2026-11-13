---
declaration: theorem
origin: cited
lean: Erdos623.erdos_623
statement: formalized
---

# Erdős Problem 623

> *Reference:* [erdosproblems.com/623](https://www.erdosproblems.com/623)

*Quoted from [FormalConjectures/ErdosProblems/623.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/623.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/623](https://www.erdosproblems.com/623).

The file states 1 research or textbook statement: 1 open.

## `Erdos623.erdos_623`

Open: stated without proof.

> Let $X$ be a set of cardinality $\aleph_\omega$ and $f$ be a function from the finite subsets of
> $X$ to $X$ such that $f(A)\not\in A$ for all $A$. Must there exist an infinite $Y\subseteq X$
> that is independent - that is, for all finite $B\subset Y$ we have $f(B)\not\in Y$?

```lean
theorem erdos_623 : ∀ (X : Type u) (hX : #X = ℵ_ ω)
    (f : Finset X → X), (∀ A : Finset X, f A ∉ A) →
    (∃ Y : Set X, Set.Infinite Y ∧ (∀ (B : Finset X), ↑B ⊆ Y → f B ∉ Y))
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/623.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/623.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/623.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/623.lean)
- [erdosproblems.com/623](https://www.erdosproblems.com/623)
