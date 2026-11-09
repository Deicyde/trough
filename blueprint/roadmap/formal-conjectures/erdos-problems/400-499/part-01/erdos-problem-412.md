---
declaration: theorem
origin: cited
lean: Erdos412.erdos_412
statement: formalized
---

# Erdős Problem 412

> *Reference:* [erdosproblems.com/412](https://www.erdosproblems.com/412)
>
> Reviewed by @b-mehta on 2025-05-27

*Quoted from [FormalConjectures/ErdosProblems/412.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/412.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/412](https://www.erdosproblems.com/412).

The file states 1 research or textbook statement: 1 open.

## `Erdos412.erdos_412`

Open: stated without proof.

> Let $σ_1(n)=σ(n)$, the sum of divisors function, and $σ_k(n) = σ(σ_{k-1}(n))$.
> Is it true that, for every $m, n ≥ 2$, there exist some $i, j$ such that $σ_i(m) = σ_j(n)$?

```lean
theorem erdos_412 : ∀ᵉ (m ≥ 2) (n ≥ 2), ∃ i j, (σ 1)^[i] m = (σ 1)^[j] n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/412.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/412.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/412.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/412.lean)
- [erdosproblems.com/412](https://www.erdosproblems.com/412)
