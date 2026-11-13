---
declaration: theorem
origin: cited
lean: Erdos862.erdos_862.parts.i, Erdos862.erdos_862.parts.ii, Erdos862.erdos_862.variants.lower_bound
statement: formalized
---

# Erdős Problem 862

> *References:*
> - [erdosproblems.com/862](https://www.erdosproblems.com/862)
> - [Er92c] Erdős, P., *Some of my forgotten problems in number theory*. Hardy-Ramanujan J. (1992),
>   34-50.
> - [SaTh15] Saxton, David and Thomason, Andrew, *Hypergraph containers*. Invent. Math. (2015),
>   925-992.

*Quoted from [FormalConjectures/ErdosProblems/862.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/862.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/862](https://www.erdosproblems.com/862).

The file states 3 research or textbook statements: 3 solved.

## `Erdos862.erdos_862.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos862.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos862.lean).

> Let $A_1(N)$ be the number of maximal Sidon subsets of $\{1,\ldots,N\}$. Is it true that
>
> $$A_1(N) < 2^{o(N^{1/2})}?$$
>
> A problem of Cameron and Erdős. This is resolved as a consequence of results of Saxton and
> Thomason [SaTh15] - they prove that the number of Sidon sets in $\{1,\ldots,N\}$ is at least
> $2^{(1.16+o(1))N^{1/2}}$. Since each Sidon set is contained in a maximal Sidon set, and each
> maximal Sidon set contains at most $2^{(1+o(1))N^{1/2}}$ Sidon sets, it follows that
>
> $$A_1(N) \geq 2^{(0.16+o(1))N^{1/2}}.$$

```lean
theorem erdos_862.parts.i :
    ¬ (fun N : ℕ => Real.logb 2 (numMaximalSidonSets N : ℝ)) =o[atTop]
      (fun N : ℕ => (N : ℝ) ^ (1 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/862.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/862.lean#L55).

## `Erdos862.erdos_862.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos862.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos862.lean).

> Let $A_1(N)$ be the number of maximal Sidon subsets of $\{1,\ldots,N\}$. Is it true that
>
> $$A_1(N) > 2^{N^c}$$
>
> for some constant $c>0$?
>
> A problem of Cameron and Erdős. This is resolved as a consequence of results of Saxton and
> Thomason [SaTh15] - they prove that the number of Sidon sets in $\{1,\ldots,N\}$ is at least
> $2^{(1.16+o(1))N^{1/2}}$. Since each Sidon set is contained in a maximal Sidon set, and each
> maximal Sidon set contains at most $2^{(1+o(1))N^{1/2}}$ Sidon sets, it follows that
>
> $$A_1(N) \geq 2^{(0.16+o(1))N^{1/2}}.$$

```lean
theorem erdos_862.parts.ii :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ N : ℕ in atTop,
      (2 : ℝ) ^ ((N : ℝ) ^ c) < (numMaximalSidonSets N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/862.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/862.lean#L73).

## `Erdos862.erdos_862.variants.lower_bound`

Solved: stated here without proof.

> This is resolved as a consequence of results of Saxton and Thomason [SaTh15] - they prove that
> the number of Sidon sets in $\{1,\ldots,N\}$ is at least $2^{(1.16+o(1))N^{1/2}}$. Since each
> Sidon set is contained in a maximal Sidon set, and each maximal Sidon set contains at most
> $2^{(1+o(1))N^{1/2}}$ Sidon sets, it follows that
>
> $$A_1(N) \geq 2^{(0.16+o(1))N^{1/2}}.$$

```lean
theorem erdos_862.variants.lower_bound (ε : ℝ) (hε : 0 < ε) :
    ∀ᶠ N : ℕ in atTop,
      (2 : ℝ) ^ (((0.16 : ℝ) - ε) * (N : ℝ) ^ (1 / 2 : ℝ)) ≤ (numMaximalSidonSets N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/862.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/862.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/862.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/862.lean)
- [erdosproblems.com/862](https://www.erdosproblems.com/862)
