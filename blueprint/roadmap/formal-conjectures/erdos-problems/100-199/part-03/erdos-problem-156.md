---
declaration: theorem
origin: cited
lean: Erdos156.erdos_156, Erdos156.erdos_156.variants.greedy_lower_bound, Erdos156.erdos_156.variants.ruzsa_upper_bound
statement: formalized
---

# Erdős Problem 156

> *References:*
> - [erdosproblems.com/156](https://www.erdosproblems.com/156)
> - [ESS94] Erdős, P. and Sárközy, A. and Sós, T., On Sum Sets of Sidon Sets, I. Journal of Number
>   Theory (1994), 329-347.
> - [Ru98b] Ruzsa, Imre Z., A small maximal Sidon set. Ramanujan J. (1998), 55-58.

*Quoted from [FormalConjectures/ErdosProblems/156.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/156.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/156](https://www.erdosproblems.com/156).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos156.erdos_156`

Open: stated without proof.

> Does there exist a maximal Sidon set $A\subset \{1,\ldots,N\}$ of size $O(N^{1/3})$?
>
> A question of Erdős, Sárközy, and Sós [ESS94].

```lean
theorem erdos_156 :
    (fun N ↦ (minMaximalSidonSet N : ℝ)) =O[atTop] (fun N ↦ (N : ℝ) ^ (1 / 3 : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/156.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/156.lean#L50).

## `Erdos156.erdos_156.variants.greedy_lower_bound`

Solved: stated here without proof.

> It is easy to prove that the greedy construction of a maximal Sidon set in $\{1,\ldots,N\}$ has size
> $\gg N^{1/3}$.

```lean
theorem erdos_156.variants.greedy_lower_bound :
    (fun N ↦ ((Finset.greedySidonBelow N).card : ℝ)) ≫ (fun N ↦ (N : ℝ) ^ (1 / 3 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/156.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/156.lean#L65).

## `Erdos156.erdos_156.variants.ruzsa_upper_bound`

Solved: stated here without proof.

> Ruzsa [Ru98b] constructed a maximal Sidon set of size $\ll (N\log N)^{1/3}$.

```lean
theorem erdos_156.variants.ruzsa_upper_bound :
    (fun N ↦ (minMaximalSidonSet N : ℝ)) ≪
      (fun N ↦ ((N : ℝ) * Real.log N) ^ (1 / 3 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/156.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/156.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/156.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/156.lean)
- [erdosproblems.com/156](https://www.erdosproblems.com/156)
