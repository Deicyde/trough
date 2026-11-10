---
declaration: theorem
origin: cited
lean: Erdos421.erdos_421
statement: formalized
---

# Erdős Problem 421

> *References:*
> - [erdosproblems.com/421](https://www.erdosproblems.com/421)
> - [Pratt26] K. Pratt, [A proof of Erdős Problem 421](https://www.erdosproblems.com/static/421-Pratt.pdf).

*Quoted from [FormalConjectures/ErdosProblems/421.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/421.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/421](https://www.erdosproblems.com/421).

The file states 1 research or textbook statement: 1 solved.

## `Erdos421.erdos_421`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos421.lean#L121](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos421.lean#L121).

> There exists a sequence $1 \le d_1 < d_2 < \dots$ with density 1 such that all products
> $\prod_{u \le i \le v} d_i$ are distinct. This was solved affirmatively; see [Pratt26].

```lean
theorem erdos_421 :
    ∃ (d : ℕ → ℕ), StrictMono d ∧ 1 ≤ d 0 ∧ HasDensity (Set.range d) 1 ∧
    {(u, v) : ℕ × ℕ | u ≤ v}.InjOn fun (u, v) => ∏ i ∈ Finset.Icc u v, d i
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/421.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/421.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/421.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/421.lean)
- [erdosproblems.com/421](https://www.erdosproblems.com/421)
