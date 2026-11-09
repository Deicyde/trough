---
declaration: theorem
origin: cited
lean: Erdos1211.erdos_1211
statement: formalized
---

# Erdős Problem 1211

> *References:*
> - [erdosproblems.com/1211](https://www.erdosproblems.com/1211)
> - [CFP22] Conlon, David and Fox, Jacob and Pham, Huy Tuan, *The upper logarithmic density of
>   monochromatic subset sums*. Mathematika 68 (2022), 1292--1301.
>   [arXiv:2105.15195](https://arxiv.org/abs/2105.15195)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115. [PDF](https://www.renyi.hu/~p_erdos/1980-03.pdf)

*Quoted from [FormalConjectures/ErdosProblems/1211.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1211.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1211](https://www.erdosproblems.com/1211).

The file states 1 research or textbook statement: 1 solved. It also has 2 API statements, counted here but not shown.

## `Erdos1211.erdos_1211`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1211.lean#L401](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1211.lean#L401).

> Let $\mathbb{N}=A\cup B$ where $A$ and $B$ are disjoint. Let $S(A)$ be those integers which are the
> sum of finitely many distinct elements of $A$, and similarly for $S(B)$.
>
> If
>
> $$
> \overline{\delta}(X)=\limsup_{x\to \infty}\frac{1}{\log x}
>   \sum_{\substack{n\in X\\ n\lt x}}\frac{1}{n}
> $$
>
> is the upper logarithmic density of $X$ then how large must
>
> $$\max(\overline{\delta}(S(A)),\overline{\delta}(S(B)))$$
>
> be?
>
> A question of Erdős [Er80]. Conlon, Fox, and Pham [CFP22, Theorem 1] proved that the least
> possible value of $\max(\overline{\delta}(S(A)),\overline{\delta}(S(B)))$ is
> $\frac{2+\sqrt{3}}{4}\approx 0.93301$, and that it is attained.

```lean
theorem erdos_1211 :
    (∀ A B : Set ℕ, IsNatPartition A B → erdos_1211.answer ≤ partitionValue A B) ∧
      ∃ A B : Set ℕ, IsNatPartition A B ∧ partitionValue A B = erdos_1211.answer
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1211.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1211.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1211.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1211.lean)
- [erdosproblems.com/1211](https://www.erdosproblems.com/1211)
