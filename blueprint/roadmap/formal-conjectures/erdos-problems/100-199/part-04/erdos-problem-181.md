---
declaration: theorem
origin: cited
lean: Erdos181.erdos_181
statement: formalized
---

# Erdős Problem 181

> *References:*
> - [erdosproblems.com/181](https://www.erdosproblems.com/181)
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [Ti22] Tikhomirov, K., *A remark on the Ramsey number of the hypercube*. arXiv:2208.14568 (2022).
> - [OpenAI26] OpenAI, *The hypercube Ramsey number has linear order*. OpenAI Math Release preprint
>   (September 2026).
>   [github.com/openai/math](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-hypercube-Ramsey-number-has-linear-order-September-23-2026/paper.pdf)

*Quoted from [FormalConjectures/ErdosProblems/181.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/181.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/181](https://www.erdosproblems.com/181).

The file states 1 research or textbook statement: 1 solved.

## `Erdos181.erdos_181`

Solved: stated here; a Lean proof is at [https://github.com/cadamcat/hypercube-ramsey-lean4/blob/ad206e1bf8240c28b538dfe72f10364cbc1591da/HypercubeRamsey/Main.lean#L14](https://github.com/cadamcat/hypercube-ramsey-lean4/blob/ad206e1bf8240c28b538dfe72f10364cbc1591da/HypercubeRamsey/Main.lean#L14).

> Let $Q_n$ be the $n$-dimensional hypercube graph (so that $Q_n$ has $2^n$ vertices and
> $n2^{n-1}$ edges). Prove that $$R(Q_n) \ll 2^n.$$

```lean
theorem erdos_181 :
    ∃ C > (0 : ℝ), ∀ n : ℕ,
      (diagonalGraphRamsey (hypercube n) : ℝ) ≤ C * 2 ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/181.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/181.lean#L46).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/181.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/181.lean)
- [erdosproblems.com/181](https://www.erdosproblems.com/181)
