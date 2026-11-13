---
declaration: theorem
origin: cited
lean: Erdos710.erdos_710, Erdos710.erdos_710.variants.lower_bound, Erdos710.erdos_710.variants.upper_bound
statement: formalized
---

# Erdős Problem 710

> *References:*
> - [erdosproblems.com/710](https://www.erdosproblems.com/710)
> - [ErPo80] Erdős, P. and Pomerance, C., *Matching the natural numbers up to $n$ with distinct
>   multiples in another interval*. Nederl. Akad. Wetensch. Indag. Math. 42 (1980), 147-161.
>   [PDF](https://www.renyi.hu/~p_erdos/1980-13.pdf)

*Quoted from [FormalConjectures/ErdosProblems/710.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/710.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/710](https://www.erdosproblems.com/710).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement and 2 API statements, counted here but not shown.

## `Erdos710.erdos_710`

Open: stated without proof.

> Let $f(n)$ be minimal such that in $(n,n+f(n))$ there exist distinct integers $a_1,\ldots,a_n$
> such that $k\mid a_k$ for all $1\leq k\leq n$. Obtain an asymptotic formula for $f(n)$.

```lean
theorem erdos_710 : (fun n ↦ (f n : ℝ)) ~[atTop] erdos_710.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/710.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/710.lean#L79).

## `Erdos710.erdos_710.variants.lower_bound`

Solved: stated here without proof.

> Erdős and Pomerance [ErPo80] proved
>
> $$\left(\frac{2}{\sqrt{e}}+o(1)\right)n\left(\frac{\log n}{\log\log n}\right)^{1/2}
> \leq f(n) \leq (1.7398\cdots+o(1))n(\log n)^{1/2}.$$
>
> This is the lower bound [ErPo80, Theorem 2].

```lean
theorem erdos_710.variants.lower_bound :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (2 / Real.sqrt (Real.exp 1) - ε) * n *
        Real.sqrt (Real.log n / Real.log (Real.log n)) ≤ (f n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/710.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/710.lean#L90).

## `Erdos710.erdos_710.variants.upper_bound`

Solved: stated here without proof.

> Erdős and Pomerance [ErPo80] proved
>
> $$\left(\frac{2}{\sqrt{e}}+o(1)\right)n\left(\frac{\log n}{\log\log n}\right)^{1/2}
> \leq f(n) \leq (1.7398\cdots+o(1))n(\log n)^{1/2}.$$
>
> This is the upper bound. Here $1.7398\cdots = \sqrt{r}/(1-r)$, where $r$ is the solution of
> $e^{-r} = r$ [ErPo80, (11), p. 154].

```lean
theorem erdos_710.variants.upper_bound :
    ∃ r : ℝ, Real.exp (-r) = r ∧ ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (f n : ℝ) ≤ (Real.sqrt r / (1 - r) + ε) * n * Real.sqrt (Real.log n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/710.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/710.lean#L105).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/710.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/710.lean)
- [erdosproblems.com/710](https://www.erdosproblems.com/710)
