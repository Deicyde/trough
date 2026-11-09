---
declaration: theorem
origin: cited
lean: Erdos345.erdos_345, Erdos345.kthPowers_isAddComplete
statement: formalized
---

# Erdős Problem 345

> *References:*
> - [erdosproblems.com/345](https://www.erdosproblems.com/345)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980), p. 55.
> - [Ki17] Kim, D., *On the largest integer that is not a sum of distinct positive nth powers*.
>   Journal of Integer Sequences 20 (2017), Article 17.7.5.
>   [arXiv:1610.02439](https://arxiv.org/abs/1610.02439)

*Quoted from [FormalConjectures/ErdosProblems/345.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/345.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/345](https://www.erdosproblems.com/345).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `Erdos345.erdos_345`

Open: stated without proof.

> Let $A\subseteq \mathbb{N}$ be a complete sequence, and define the threshold of completeness
> $T(A)$ to be the least integer $m$ such that all $n\geq m$ are in
>
> $$P(A) = \left\{\sum_{n\in B}n : B\subseteq A\textrm{ finite }\right\}$$
>
> (the existence of $T(A)$ is guaranteed by completeness).
>
> Is it true that there are infinitely many $k$ such that $T(n^k)>T(n^{k+1})$?
>
> Here $T(n^k)$ means the threshold of the positive $k$-th powers. Least-threshold witnesses
> ensure that the thresholds exist. We restrict to $k\geq 1$, since the zeroth powers form
> $\{1\}$, which is incomplete. Positive powers are complete [Ki17].

```lean
theorem erdos_345 :
    {k : ℕ | 0 < k ∧ ∃ a b : ℕ, IsLeast (thresholds (kthPowers k)) a ∧
      IsLeast (thresholds (kthPowers (k + 1))) b ∧ b < a}.Infinite
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/345.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/345.lean#L55).

## `Erdos345.kthPowers_isAddComplete`

Solved: stated here without proof.

> Every set of positive $k$-th powers with $k\geq 1$ is complete [Ki17].

```lean
theorem kthPowers_isAddComplete : ∀ k : ℕ, 0 < k → IsAddComplete (kthPowers k)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/345.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/345.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/345.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/345.lean)
- [erdosproblems.com/345](https://www.erdosproblems.com/345)
