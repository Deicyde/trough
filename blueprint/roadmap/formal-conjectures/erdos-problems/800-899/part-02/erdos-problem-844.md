---
declaration: theorem
origin: cited
lean: Erdos844.erdos_844
statement: formalized
---

# Erdős Problem 844

> *References:*
> - [erdosproblems.com/844](https://www.erdosproblems.com/844)
> - [AMS25] Alexeev, B., Mixon, D. and Sawin, W., *The independence and clique cover numbers of the
>   squarefree graph*. arXiv:2507.01928 (2025).
> - [Ch74] Chvátal, V., *Intersecting families of edges in hypergraphs having the hereditary
>   property*. (1974), 61-66.

*Quoted from [FormalConjectures/ErdosProblems/844.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/844.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/844](https://www.erdosproblems.com/844).

The file states 1 research or textbook statement: 1 solved.

## `Erdos844.erdos_844`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/JohnEdwardJennings/e32f2c412b0225091e7519d60741bd2d/raw/7d811ea413e2f7c0c0442749958aaac421eb6807/Erdos844.lean](https://gist.githubusercontent.com/JohnEdwardJennings/e32f2c412b0225091e7519d60741bd2d/raw/7d811ea413e2f7c0c0442749958aaac421eb6807/Erdos844.lean).

> Let $A\subseteq \{1,\ldots,N\}$ be such that, for all $a,b\in A$, the product $ab$ is not
> squarefree.
>
> Is the maximum size of such an $A$ achieved by taking $A$ to be the set of even numbers and
> odd non-squarefree numbers?
>
> A problem of Erdős and Sárközy.
>
> Weisenberg has provided the following positive proof. It is clear that such a maximal $A$ must
> contain all non-squarefree numbers. It therefore suffices to find the largest size of a subset
> of all squarefree numbers in $\{1,\ldots,N\}$ such that any two have at least one prime factor
> in common. By the result of Chvátal [Ch74] discussed in [701] this is maximised by the set of
> all even squarefree numbers.
>
> An alternative proof was independently found by Alexeev, Mixon, and Sawin [AMS25].
>
> This was formalized in Lean by Jennings using Aristotle.

```lean
theorem erdos_844 : ∀ N : ℕ,
    IsGreatest {k : ℕ | ∃ A ⊆ Finset.Icc 1 N,
      (∀ a ∈ A, ∀ b ∈ A, ¬ Squarefree (a * b)) ∧ A.card = k}
      (evenOrOddNonSquarefree N).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/844.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/844.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/844.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/844.lean)
- [erdosproblems.com/844](https://www.erdosproblems.com/844)
