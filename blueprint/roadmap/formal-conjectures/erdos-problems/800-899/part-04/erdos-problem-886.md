---
declaration: theorem
origin: cited
lean: Erdos886.erdos_886, Erdos886.erdos_886.variants.rosenfeld_infinite, Erdos886.erdos_886.variants.rosenfeld_bound
statement: formalized
---

# Erdős Problem 886

> *References:*
> - [erdosproblems.com/886](https://www.erdosproblems.com/886)
> - [ErRo97] Erdős, Paul and Rosenfeld, Moshe, The factor-difference set of integers. Acta Arith.
>   (1997), 353--359.

*Quoted from [FormalConjectures/ErdosProblems/886.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/886.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/886](https://www.erdosproblems.com/886).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos886.erdos_886`

Open: stated without proof.

> Let $\epsilon>0$. Is it true that, for all large $n$, the number of divisors of $n$ in
> $(n^{1/2},n^{1/2}+n^{1/2-\epsilon})$ is $O_\epsilon(1)$?
>
> Erdős attributes this conjecture to Ruzsa.

```lean
theorem erdos_886 :
    ∀ ε > 0, ∃ K : ℕ, ∀ᶠ n in atTop, (Erdos886Divisors n ε 1).card ≤ K
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/886.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/886.lean#L49).

## `Erdos886.erdos_886.variants.rosenfeld_infinite`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/4a1f92f2aca5f32edb0c681f1e8fdca88b5d9494/erdos-886/Solution.lean#L38](https://github.com/linrock/math-proofs/blob/4a1f92f2aca5f32edb0c681f1e8fdca88b5d9494/erdos-886/Solution.lean#L38).

> Erdős and Rosenfeld [ErRo97] proved that there are infinitely many $n$ such that there are
> four divisors of $n$ in $(n^{1/2},n^{1/2}+16n^{1/4})$.

```lean
theorem erdos_886.variants.rosenfeld_infinite :
    Set.Infinite {n | 4 ≤ (Erdos886Divisors n (1/4) 16).card}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/886.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/886.lean#L60).

## `Erdos886.erdos_886.variants.rosenfeld_bound`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/4a1f92f2aca5f32edb0c681f1e8fdca88b5d9494/erdos-886/Solution.lean#L45](https://github.com/linrock/math-proofs/blob/4a1f92f2aca5f32edb0c681f1e8fdca88b5d9494/erdos-886/Solution.lean#L45).

> Erdős and Rosenfeld [ErRo97] proved that, for any constant $C>0$, all large $n$ have at most
> $1+C^2$ many divisors in $[n^{1/2}, n^{1/2}+Cn^{1/4}]$.

```lean
theorem erdos_886.variants.rosenfeld_bound :
    ∀ C > 0, ∀ᶠ (n : ℕ) in atTop,
    ((divisors n).filter (fun (d : ℕ) =>
      (n : ℝ) ^ (1 / 2 : ℝ) ≤ (d : ℝ) ∧ (d : ℝ) ≤ (n : ℝ) ^ (1 / 2 : ℝ) + C * (n : ℝ) ^ (1 / 4 : ℝ))).card
      ≤ 1 + C ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/886.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/886.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/886.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/886.lean)
- [erdosproblems.com/886](https://www.erdosproblems.com/886)
