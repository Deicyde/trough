---
declaration: theorem
origin: cited
lean: Erdos851.erdos_851.variants.romanoff, Erdos851.erdos_851
statement: formalized
---

# Erdős Problem 851

> *References:*
> - [erdosproblems.com/851](https://www.erdosproblems.com/851)
> - [Pr26] D. Price and GPT-5.2 Pro, [Erdős problem 851](https://www.overleaf.com/read/svgbjzpxxppv#4eea7e) (2026)

*Quoted from [FormalConjectures/ErdosProblems/851.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/851.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/851](https://www.erdosproblems.com/851).

The file states 2 research or textbook statements: 2 solved.

## `Erdos851.erdos_851.variants.romanoff`

Solved: stated here without proof.

> The set of integers of the form `2^k+p` (where `p` is prime) has positive lower density.

```lean
theorem erdos_851.variants.romanoff : 0 < Set.lowerDensity twoPowAddPrimeSet
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/851.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/851.lean#L45).

## `Erdos851.erdos_851`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos851.lean#L37](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos851.lean#L37).

> Let $\epsilon > 0$. Is there some $r \ll_\epsilon 1$ such that the density of integers of the
> form $2^k+n$, where $k \geq 0$ and $n$ has at most $r$ prime divisors, is at least $1-\epsilon$?
>
> This was proved affirmatively by Price and GPT-5.2 Pro [Pr26].

```lean
theorem erdos_851 (ε : ℝ) (hε : ε ∈ Set.Ioo 0 1) : ∃ r,
    1 - ε ≤ (TwoPowAddSet r).lowerDensity
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/851.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/851.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/851.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/851.lean)
- [erdosproblems.com/851](https://www.erdosproblems.com/851)
