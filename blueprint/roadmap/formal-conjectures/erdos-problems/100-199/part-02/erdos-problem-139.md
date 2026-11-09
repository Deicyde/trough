---
declaration: theorem
origin: cited
lean: Erdos139.erdos_139
statement: formalized
---

# Erdős Problem 139

> *Reference:* [erdosproblems.com/139](https://www.erdosproblems.com/139)

*Quoted from [FormalConjectures/ErdosProblems/139.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/139.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/139](https://www.erdosproblems.com/139).

The file states 1 research or textbook statement: 1 solved.

## `Erdos139.erdos_139`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos139.lean#L36](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos139.lean#L36).

> **Erdős Problem 139**:
> Let $r_k(N)$ be the size of the largest subset of ${1,...,N}$ which does not contain a non-trivial
> $k$-term arithmetic progression. Prove that $r_k(N) = o(N)$.

```lean
theorem erdos_139 (k : ℕ) (hk : 1 < k) :
    Filter.Tendsto (fun N => (r k N / N : ℝ)) Filter.atTop (𝓝 0)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/139.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/139.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/139.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/139.lean)
- [erdosproblems.com/139](https://www.erdosproblems.com/139)
