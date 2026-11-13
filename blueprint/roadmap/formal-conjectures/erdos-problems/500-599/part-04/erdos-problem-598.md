---
declaration: theorem
origin: cited
lean: Erdos598.erdos_598
statement: formalized
---

# Erdős Problem 598

> *Reference:* [erdosproblems.com/598](https://www.erdosproblems.com/598)

*Quoted from [FormalConjectures/ErdosProblems/598.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/598.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/598](https://www.erdosproblems.com/598).

The file states 1 research or textbook statement: 1 open.

## `Erdos598.erdos_598`

Open: stated without proof.

> **Erdős Problem 598:**
> Let $m$ be an infinite cardinal and $\kappa$ be the successor cardinal of $2^{\aleph_0}$.
> Can one colour the countable subsets of $m$ using $\kappa$ many colours so that every
> $X \subseteq m$ with $|X| = \kappa$ contains subsets of all possible colours?

```lean
theorem erdos_598 :
    ∀ (m : Type*) [Infinite m],
    ∃ c : { s : Set m // s.Countable } → κ.out,
    ∀ X : Set m, #X = κ →
    c '' { s : { sub : Set m // sub.Countable } | s.1 ⊆ X } = Set.univ
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/598.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/598.lean#L44).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/598.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/598.lean)
- [erdosproblems.com/598](https://www.erdosproblems.com/598)
