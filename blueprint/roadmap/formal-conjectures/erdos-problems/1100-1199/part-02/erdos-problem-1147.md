---
declaration: theorem
origin: cited
lean: Erdos1147.erdos_1147, Erdos1147.erdos_1147.variants.sqrt_two, Erdos1147.erdos_1147.variants.almost_every
statement: formalized
---

# Erdős Problem 1147

> *References:*
> - [erdosproblems.com/1147](https://www.erdosproblems.com/1147)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference "Paul
>   Erdős and his mathematics", Budapest, July 1999 (1999).
> - [Ko16b] Konieczny, Jakub, *Sets of recurrence as bases for the positive integers*. Acta Arith.
>   (2016), 309-338.

*Quoted from [FormalConjectures/ErdosProblems/1147.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1147.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1147](https://www.erdosproblems.com/1147).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1147.erdos_1147`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1147.lean#L538](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1147.lean#L538).

> Let $\alpha>0$ be an irrational number. Is the set
> $$A=\left\{ n\geq 1: \| \alpha n^2\| < \frac{1}{\log n}\right\},$$
> where $\|\cdot\|$ denotes the distance to the nearest integer, an additive basis of order $2$?
>
> This was disproved by Konieczny [Ko16b], and is false both for almost every $\alpha>0$, and also
> is false specifically for $\alpha=\sqrt{2}$.
>
> More generally, given any $\epsilon(n)\to 0$, the set
> $A=\{ n\geq 1: \| \alpha n^2\| < \epsilon(n)\}$ is not an additive basis of order $2$ for almost
> every $\alpha>0$.

```lean
theorem erdos_1147 : ¬ ∀ α : ℝ, 0 < α → Irrational α →
    (recurrenceSet α fun n ↦ 1 / Real.log n).IsAsymptoticAddBasisOfOrder 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1147.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1147.lean#L56).

## `Erdos1147.erdos_1147.variants.sqrt_two`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1147.lean#L531](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos1147.lean#L531).

> Konieczny [Ko16b] showed that the set is not an additive basis of order $2$ for
> $\alpha=\sqrt{2}$.

```lean
theorem erdos_1147.variants.sqrt_two :
    ¬ (recurrenceSet (√2) fun n ↦ 1 / Real.log n).IsAsymptoticAddBasisOfOrder 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1147.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1147.lean#L65).

## `Erdos1147.erdos_1147.variants.almost_every`

Solved: stated here without proof.

> Konieczny [Ko16b] showed that, given any $\epsilon(n)\to 0$, the set
> $\{ n\geq 1: \| \alpha n^2\| < \epsilon(n)\}$ is not an additive basis of order $2$ for almost
> every $\alpha>0$.

```lean
theorem erdos_1147.variants.almost_every : ∀ ε : ℕ → ℝ, Tendsto ε atTop (nhds 0) →
    ∀ᵐ α : ℝ, 0 < α → ¬ (recurrenceSet α ε).IsAsymptoticAddBasisOfOrder 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1147.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1147.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1147.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1147.lean)
- [erdosproblems.com/1147](https://www.erdosproblems.com/1147)
