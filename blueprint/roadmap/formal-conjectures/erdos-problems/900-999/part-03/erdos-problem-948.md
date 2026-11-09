---
declaration: theorem
origin: cited
lean: Erdos948.erdos_948, Erdos948.erdos_948.variants.monochromatic
statement: formalized
---

# Erdős Problem 948

> *References:*
> - [erdosproblems.com/948](https://www.erdosproblems.com/948)
> - [Er77c] Erdős, Paul, *Problems and results on combinatorial number theory. III*. Number theory day
>   (Proc. Conf., Rockefeller Univ., New York, 1976) (1977), 43-72.
> - [ErGa91] Erdős, P. and Galvin, F., *Some Ramsey-type theorems*. Discrete Math. 87 (1991),
>   261–269.

*Quoted from [FormalConjectures/ErdosProblems/948.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/948.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/948](https://www.erdosproblems.com/948).

The file states 2 research or textbook statements: 2 solved.

## `Erdos948.erdos_948`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos948.lean#L451](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos948.lean#L451).

> Is there a function $f(n)$ and a $k$ such that in any $k$-colouring of the integers there exists a
> sequence $a_1 < a_2 < \cdots$ such that $a_n < f(n)$ for infinitely many $n$ and the set
>
> $$\left\{ \sum_{i \in S} a_i : \textrm{finite nonempty } S \right\}$$
>
> does not contain all colours?
>
> A question of Erdős [Er77c] and Erdős and Galvin [ErGa91]. The answer is no: GPT-5.5 Pro (prompted
> by Price) showed that for every $f$ there is a colouring of the integers such that the finite sums
> of every such sequence use all colours. The linked formal proof (Codex and GPT-5.6 Sol) gives, for
> every $f$ and $k \ge 1$, a colouring $c : \mathbb{Z} \to \{0, \ldots, k - 1\}$ such that for every
> strictly increasing $a$ with $a_n < f(n)$ infinitely often and every colour, some nonempty finite
> sum of the $a_i$ has that colour.

```lean
theorem erdos_948 :
    ¬ ∃ (f : ℕ → ℕ) (k : ℕ), 0 < k ∧ ∀ colouring : ℤ → Fin k,
      ∃ a : ℕ → ℤ, StrictMono a ∧ {n | a n < f n}.Infinite ∧
        ∃ c : Fin k, ∀ S : Finset ℕ, S.Nonempty → colouring (∑ i ∈ S, a i) ≠ c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/948.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/948.lean#L52).

## `Erdos948.erdos_948.variants.monochromatic`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos948.lean#L451](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos948.lean#L451).

> The original question asks for the set of finite sums to be monochromatic. Galvin showed that
> this fails for $k = 2$, and it fails for every $k \ge 2$ by the negative answer to `erdos_948`.

```lean
theorem erdos_948.variants.monochromatic :
    ¬ ∃ (f : ℕ → ℕ) (k : ℕ), 2 ≤ k ∧ ∀ colouring : ℤ → Fin k,
      ∃ a : ℕ → ℤ, StrictMono a ∧ {n | a n < f n}.Infinite ∧
        ∃ c : Fin k, ∀ S : Finset ℕ, S.Nonempty → colouring (∑ i ∈ S, a i) = c
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/948.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/948.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/948.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/948.lean)
- [erdosproblems.com/948](https://www.erdosproblems.com/948)
