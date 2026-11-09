---
declaration: theorem
origin: cited
lean: Erdos656.erdos_656
statement: formalized
---

# Erdős Problem 656

> *References:*
> - [erdosproblems.com/656](https://www.erdosproblems.com/656)
> - [Er75b] Erdős, Paul, *Problems and results in combinatorial number theory*. Journées
>   Arithmétiques de Bordeaux (Conf., Univ. Bordeaux, Bordeaux, 1974) (1975), 295-310.
> - [KMRR24] Kra, B., Moreira, J., Richter, F. K. and Robertson, D., *A proof of Erdős's $B+B+t$
>   conjecture*. Commun. Am. Math. Soc. 4 (2024), 480-494.
>   [arXiv:2206.12377](https://arxiv.org/abs/2206.12377)

*Quoted from [FormalConjectures/ErdosProblems/656.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/656.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/656](https://www.erdosproblems.com/656).

The file states 1 research or textbook statement: 1 solved.

## `Erdos656.erdos_656`

Solved: stated here without proof.

> Let $A\subset \mathbb{N}$ be a set with positive upper density. Must there exist an infinite set
> $B\subseteq A$ and integer $t$ such that
> $$\{b_1+b_2: b_1\neq b_2\in B\}+t\subseteq A?$$
>
> Erdős [Er75b] posed this as a candidate for a density version of Hindman's theorem. This is true,
> and was proved by Kra, Moreira, Richter, and Robertson [KMRR24, Theorem 1.2 (i)], even for sets of
> positive upper Banach density and with $t \geq 0$.
>
> The inclusion says that every $b_1+b_2+t$ is an element of `A`, as an integer.

```lean
theorem erdos_656 :
    ∀ A : Set ℕ, 0 < A.upperDensity →
      ∃ B ⊆ A, B.Infinite ∧ ∃ t : ℤ, ∀ b₁ ∈ B, ∀ b₂ ∈ B, b₁ ≠ b₂ →
        ∃ a ∈ A, (a : ℤ) = b₁ + b₂ + t
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/656.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/656.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/656.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/656.lean)
- [erdosproblems.com/656](https://www.erdosproblems.com/656)
