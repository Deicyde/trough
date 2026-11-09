---
declaration: theorem
origin: cited
lean: Erdos330.erdos_330_statement
statement: formalized
---

# Erdős Problem 330

> *Reference:* [erdosproblems.com/330](https://www.erdosproblems.com/330)

*Quoted from [FormalConjectures/ErdosProblems/330.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/330.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/330](https://www.erdosproblems.com/330).

The file states 1 research or textbook statement: 1 solved.

## `Erdos330.erdos_330_statement`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/a5ffc87b3d684fc00ea906b9e746c283740da900/problems/330/Erdos330.lean](https://github.com/Jayyhk/erdos-lean/blob/a5ffc87b3d684fc00ea906b9e746c283740da900/problems/330/Erdos330.lean).

> Does there exist a minimal basis $A \subset \mathbb{N}$ with positive density
> such that, for any $n \in A$, the (upper) density of integers which
> cannot be represented without using $n$ is positive?
>
> Neither set is asked to have a density, only to have positive upper density, so
> `Set.upperDensity` is used for both rather than `Set.HasPosDensity`. As with many of Erdős'
> questions "positive density" here most likely means positive upper density, and in [Er80] he
> considers either the lower or the upper density for the integers not representable without a
> fixed `n`. Requiring the density to exist would ask a strictly harder question than the one
> posed. See #3979.
>
> Such a set exists, so the answer is yes. The linked proof gives one of order `2`.

```lean
theorem erdos_330_statement :
    ∃ (A : Set ℕ), ∃ h, MinAsymptoticAddBasisOfOrder A h ∧
    0 < A.upperDensity ∧ ∀ n ∈ A, 0 < (UnrepWithout A n h).upperDensity
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/330.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/330.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/330.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/330.lean)
- [erdosproblems.com/330](https://www.erdosproblems.com/330)
