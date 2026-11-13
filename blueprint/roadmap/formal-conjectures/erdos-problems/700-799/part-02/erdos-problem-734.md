---
declaration: theorem
origin: cited
lean: Erdos734.erdos_734
statement: formalized
---

# Erdős Problem 734

> *References:*
> - [erdosproblems.com/734](https://www.erdosproblems.com/734)
> - [Er81] Erdős, P., On the combinatorial problems which I would most like to see solved.
>   Combinatorica (1981), 25-42.
> - [dBEr48] de Bruijn, N. G. and Erdős, P., On a combinatorial problem. Nederl. Akad. Wetensch.,
>   Proc. (1948), 1277--1279 = Indagationes Math. 10, 421--423.

*Quoted from [FormalConjectures/ErdosProblems/734.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/734.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/734](https://www.erdosproblems.com/734).

The file states 1 research or textbook statement: 1 open.

## `Erdos734.erdos_734`

Open: stated without proof.

> Find, for all large $n$, a non-trivial pairwise balanced block design $A_1,\ldots,A_m\subseteq
> \{1,\ldots,n\}$ such that, for all $t$, there are $O(n^{1/2})$ many $i$ such that $\lvert
> A_i\rvert=t$.

```lean
theorem erdos_734 :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ n : ℕ in atTop,
    ∃ H : Finset (Finset (Fin n)), H.IsPairwiseBalancedDesign ∧
      (∀ e ∈ H, e.card < n) ∧ ∀ t : ℕ,
        ({e ∈ H | e.card = t}.card : ℝ) ≤ C * Real.sqrt n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/734.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/734.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/734.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/734.lean)
- [erdosproblems.com/734](https://www.erdosproblems.com/734)
