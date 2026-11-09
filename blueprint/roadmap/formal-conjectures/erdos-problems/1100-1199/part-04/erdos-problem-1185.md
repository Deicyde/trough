---
declaration: theorem
origin: cited
lean: Erdos1185.erdos_1185, Erdos1185.erdos_1185.variants.k_three
statement: formalized
---

# Erdős Problem 1185

> *References:*
> - [erdosproblems.com/1185](https://www.erdosproblems.com/1185)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115. [PDF](https://www.renyi.hu/~p_erdos/1980-03.pdf)
> - [Fu81] Furstenberg, H., *Recurrence in ergodic theory and combinatorial number theory*.
>   M. B. Porter Lectures, Princeton University Press (1981), xi+203.

*Quoted from [FormalConjectures/ErdosProblems/1185.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1185.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1185](https://www.erdosproblems.com/1185).

The file states 2 research or textbook statements: 2 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1185.erdos_1185`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1185.lean#L922](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1185.lean#L922).

> Let $\delta>0$ and $k\geq 3$. Is it true that there exists $m\geq 1$ (depending only on $\delta$
> and $k$) such that, for all large $N$, if $A,B\subseteq \{1,\ldots,N\}$ with
> $\lvert A\rvert \geq \delta N$ and $\lvert B\rvert \geq m$ then there is a non-trivial $k$-term
> arithmetic progression in $A$ whose common difference is in $B-B$?
>
> A problem of Erdős and Mauldin [Er80, p. 92], who ask the case $k=3$ and say that the same
> probably holds for $k$ terms. The answer is no, already for $k=3$: to disprove it suffices to give
> an infinite set $B$ such that $B-B$ is not $2$-intersective (a set $S$ is $k$-intersective if
> every subset of $\mathbb{N}$ with positive density contains an arithmetic progression of length
> $k+1$ whose common difference is in $S$), which was provided by Furstenberg [Fu81]. The statement
> below is the negation of the claim for all $\delta>0$ and $k\geq 3$, with $m$ chosen before the
> threshold $N_0$ for "large $N$".

```lean
theorem erdos_1185 :
    ¬ (∀ δ : ℝ, 0 < δ → ∀ k : ℕ, 3 ≤ k →
      ∃ m : ℕ, 1 ≤ m ∧ ∃ N₀ : ℕ, ∀ N : ℕ, N₀ ≤ N →
        ∀ A B : Finset ℕ, A ⊆ Finset.Icc 1 N → B ⊆ Finset.Icc 1 N →
          δ * (N : ℝ) ≤ (A.card : ℝ) → m ≤ B.card → HasAPWithStepInDiff k A B)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1185.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1185.lean#L68).

## `Erdos1185.erdos_1185.variants.k_three`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1185.lean#L843](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1185.lean#L843).

> The answer is already negative for $k=3$: there is a density $\delta>0$ such that for every
> $m\geq 1$ and every $N_0$ there are $N\geq N_0$ and $A,B\subseteq\{1,\ldots,N\}$ with
> $\lvert A\rvert\geq\delta N$, $\lvert B\rvert\geq m$, and no non-trivial $3$-term arithmetic
> progression in $A$ whose common difference is in $B-B$.

```lean
theorem erdos_1185.variants.k_three :
    ∃ δ : ℝ, 0 < δ ∧ ∀ m : ℕ, 1 ≤ m → ∀ N₀ : ℕ, ∃ N : ℕ, ∃ A B : Finset ℕ,
      N₀ ≤ N ∧ A ⊆ Finset.Icc 1 N ∧ B ⊆ Finset.Icc 1 N ∧
        δ * (N : ℝ) ≤ (A.card : ℝ) ∧ m ≤ B.card ∧ ¬ HasAPWithStepInDiff 3 A B
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1185.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1185.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1185.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1185.lean)
- [erdosproblems.com/1185](https://www.erdosproblems.com/1185)
