---
declaration: theorem
origin: cited
lean: Erdos684.erdos_684.upper_bound, Erdos684.erdos_684.lower_bound
statement: formalized
---

# Erdős Problem 684

> *References:*
> - [erdosproblems.com/684](https://www.erdosproblems.com/684)
> - [APSSV26] Alexeev, B., Putterman, M., Sawhney, M., Sellke, M., and Valiant, G.,
>   *Short proofs in combinatorics and number theory*. arXiv:2603.29961 (2026), Theorem 2.1.

*Quoted from [FormalConjectures/ErdosProblems/684.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/684.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/684](https://www.erdosproblems.com/684).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos684.erdos_684.upper_bound`

Solved: stated here; a Lean proof is at [https://github.com/AItoBit/erdos-684-elementary-bounds/blob/a59cf65171b19dc7785b767d3b88ad8ef754f3eb/Solution.lean](https://github.com/AItoBit/erdos-684-elementary-bounds/blob/a59cf65171b19dc7785b767d3b88ad8ef754f3eb/Solution.lean).

> Let $f(n)$ be the smallest $0 \leq k \leq n$ for which the factor of
> $\binom{n}{k}$ supported on primes at most $k$ exceeds $n^2$. Give bounds for $f(n)$.
>
> An internal OpenAI model [APSSV26] has given an elementary argument which shows
> $f(n) \ll (\log n)^2$. This statement gives the nonoptimal constant $514$.
> The existence formulation avoids defining the minimum for small inputs.

```lean
theorem erdos_684.upper_bound :
    ∀ᶠ n : ℕ in atTop, ∃ k ≤ n,
      (k : ℝ) ≤ 514 * (log (n : ℝ)) ^ 2 ∧ n ^ 2 < smallPrimePart n k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/684.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/684.lean#L52).

## `Erdos684.erdos_684.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/AItoBit/erdos-684-elementary-bounds/blob/a59cf65171b19dc7785b767d3b88ad8ef754f3eb/Erdos684/Lower.lean](https://github.com/AItoBit/erdos-684-elementary-bounds/blob/a59cf65171b19dc7785b767d3b88ad8ef754f3eb/Erdos684/Lower.lean).

> The elementary argument of an internal OpenAI model [APSSV26] constructs arbitrarily
> large $n$ such that $f(n) \geq (1/2-o(1))\log n$. The following weaker form has coefficient
> $1/8$: for arbitrarily large $n>1$, the small-prime part equals one for every
> $k \leq (\log n)/8$.

```lean
theorem erdos_684.lower_bound :
    ∃ᶠ n : ℕ in atTop, 1 < n ∧
      ∀ k : ℕ, (k : ℝ) ≤ log (n : ℝ) / 8 → smallPrimePart n k = 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/684.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/684.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/684.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/684.lean)
- [erdosproblems.com/684](https://www.erdosproblems.com/684)
