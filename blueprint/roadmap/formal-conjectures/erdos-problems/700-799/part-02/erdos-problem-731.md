---
declaration: theorem
origin: cited
lean: Erdos731.erdos_731, Erdos731.erdos_731.variants.egrs75
statement: formalized
---

# Erdős Problem 731

> *References:*
> - [erdosproblems.com/731](https://www.erdosproblems.com/731)
> - [EGRS75] Erdős, P. and Graham, R. L. and Ruzsa, I. Z. and Straus, E. G.,
>   *On the prime factors of $\binom{2n}{n}$*. Math. Comp. 29 (1975), 83-92.
>   [PDF](https://www.renyi.hu/~p_erdos/1975-27.pdf)

*Quoted from [FormalConjectures/ErdosProblems/731.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/731.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/731](https://www.erdosproblems.com/731).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos731.erdos_731`

Open: stated without proof.

> Find some reasonable function $f(n)$ such that, for almost all integers $n$, the least integer
> $m$ such that $m\nmid \binom{2n}{n}$ satisfies
>
> $$m\sim f(n).$$
>
> Here "almost all" means natural density $1$, and $m \sim f(n)$ means that for every
> $\varepsilon>0$ the set of $n$ with $|m/f(n)-1|\lt \varepsilon$ has density $1$.

```lean
theorem erdos_731 : ∀ ε > (0 : ℝ),
    {n : ℕ | |(leastNonDivisor n : ℝ) / erdos_731.answer n - 1| < ε}.HasDensity 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/731.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/731.lean#L72).

## `Erdos731.erdos_731.variants.egrs75`

Solved: stated here without proof.

> A problem of Erdős, Graham, Ruzsa, and Straus [EGRS75], who say it is 'not hard to show that',
> for almost all $n$, the minimal such $m$ satisfies
>
> $$m=\exp((\log n)^{1/2+o(1)}).$$
>
> [EGRS75, (8), p. 91] states this as: for every $\varepsilon>0$, for all $n$ outside a set of
> density $0$, $\exp((\log n)^{1/2-\varepsilon}) < m < \exp((\log n)^{1/2+\varepsilon})$.

```lean
theorem erdos_731.variants.egrs75 : ∀ ε > (0 : ℝ),
    {n : ℕ | Real.exp (Real.log n ^ ((1 : ℝ) / 2 - ε)) < (leastNonDivisor n : ℝ) ∧
      (leastNonDivisor n : ℝ) < Real.exp (Real.log n ^ ((1 : ℝ) / 2 + ε))}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/731.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/731.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/731.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/731.lean)
- [erdosproblems.com/731](https://www.erdosproblems.com/731)
