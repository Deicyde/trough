---
declaration: theorem
origin: cited
lean: Erdos195.erdos_195, Erdos195.erdos_195.variants.leq_5_bound, Erdos195.erdos_195.variants.leq_4_bound
statement: formalized
---

# Erdős Problem 195

> *References:*
> - [erdosproblems.com/195](https://www.erdosproblems.com/195)
> - [Ad22] Adenwalla, S., Avoiding Monotone Arithmetic Progressions in Permutations of Integers.
>   arXiv:2211.04451 (2022).
> - [Ge19] Geneson, Jesse, Forbidden arithmetic progressions in permutations of subsets of the
>   integers. Discrete Math. (2019), 1489-1491.

*Quoted from [FormalConjectures/ErdosProblems/195.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/195.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/195](https://www.erdosproblems.com/195).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos195.erdos_195`

Open: stated without proof.

> What is the largest $k$ such that in any permutation of $\mathbb{Z}$ there must exist a
> monotone $k$-term arithmetic progression $x_1 < \cdots < x_k$?
>
> Here a permutation of $\mathbb{Z}$ is a one-sided arrangement $a_1, a_2, a_3, \ldots$ of the
> integers, i.e. a bijection $\mathbb{N} \to \mathbb{Z}$, and a monotone $k$-term arithmetic
> progression is a subsequence $a_{i_1}, \ldots, a_{i_k}$ with $i_1 < \cdots < i_k$ forming an
> increasing or decreasing arithmetic progression.

```lean
theorem erdos_195 :
    erdos_195.answer = sSup {k : ℕ | ∀ f : ℕ ≃ ℤ, HasMonotoneAP f k}
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/195.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/195.lean#L47).

## `Erdos195.erdos_195.variants.leq_5_bound`

Solved: stated here without proof.

> Geneson [Ge19] proved that k ≤ 5.

```lean
theorem erdos_195.variants.leq_5_bound :
    5 ≥ sSup {k : ℕ | ∀ f : ℕ ≃ ℤ, HasMonotoneAP f k}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/195.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/195.lean#L55).

## `Erdos195.erdos_195.variants.leq_4_bound`

Solved: stated here without proof.

> Adenwalla [Ad22] proved that k ≤ 4.

```lean
theorem erdos_195.variants.leq_4_bound :
    4 ≥ sSup {k : ℕ | ∀ f : ℕ ≃ ℤ, HasMonotoneAP f k}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/195.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/195.lean#L63).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/195.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/195.lean)
- [erdosproblems.com/195](https://www.erdosproblems.com/195)
