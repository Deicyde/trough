---
declaration: theorem
origin: cited
lean: Erdos248.erdos_248
statement: formalized
---

# Erdős Problem 248

> *References:*
> - [erdosproblems.com/248](https://www.erdosproblems.com/248)
> - [TaTe25] T. Tao and J. Teräväinen, Quantitative correlations and some problems on prime factors of consecutive integers. arXiv:2512.01739 (2025).

*Quoted from [FormalConjectures/ErdosProblems/248.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/248.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/248](https://www.erdosproblems.com/248).

The file states 1 research or textbook statement: 1 solved.

## `Erdos248.erdos_248`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos248.lean#L47](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos248.lean#L47).

> Are there infinitely many $n$ such that $\omega(n + k) \ll k$ for all $k \geq 1$?
> Here $\omega(n)$ is the number of distinct prime divisors of $n$.

```lean
theorem erdos_248 : (∃ C > (0 : ℝ), { n | ∀ k ≥ 1, ω (n + k) ≤ C * k }.Infinite)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/248.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/248.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/248.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/248.lean)
- [erdosproblems.com/248](https://www.erdosproblems.com/248)
