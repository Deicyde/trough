---
declaration: theorem
origin: cited
lean: Erdos860.erdos_860, Erdos860.erdos_860.variants.erdos_pomerance_upper, Erdos860.erdos_860.variants.erdos_selfridge_lower, Erdos860.erdos_860.variants.ruzsa
statement: formalized
---

# Erdős Problem 860

> *References:*
> - [erdosproblems.com/860](https://www.erdosproblems.com/860)
> - [ErPo80] Erdős, P. and Pomerance, C., *Matching the natural numbers up to $n$ with distinct
>   multiples in another interval*. Nederl. Akad. Wetensch. Indag. Math. 42 (1980), 147-161.
>   [PDF](https://www.renyi.hu/~p_erdos/1980-13.pdf)
> - [Er92c] Erdős, P., *Some of my forgotten problems in number theory*. Hardy-Ramanujan J. 15
>   (1992), 34-50. [PDF](https://hrj.episciences.org/125/pdf)

*Quoted from [FormalConjectures/ErdosProblems/860.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/860.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/860](https://www.erdosproblems.com/860).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos860.erdos_860`

Open: stated without proof.

> Let $h(n)$ be such that, for any $m\geq 1$, in the interval $(m,m+h(n))$ there exist distinct
> integers $a_i$ for $1\leq i\leq \pi(n)$ such that $p_i\mid a_i$, where $p_i$ denotes the $i$th
> prime.
>
> Estimate $h(n)$.

```lean
theorem erdos_860 : (fun n ↦ (h n : ℝ)) =Θ[atTop] erdos_860.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/860.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/860.lean#L69).

## `Erdos860.erdos_860.variants.erdos_pomerance_upper`

Solved: stated here without proof.

> Erdős and Pomerance [ErPo80] proved that
>
> $$h(n) \ll \frac{n^{3/2}}{(\log n)^{1/2}}.$$

```lean
theorem erdos_860.variants.erdos_pomerance_upper :
    (fun n : ℕ ↦ (h n : ℝ)) =O[atTop]
      fun n : ℕ ↦ (n : ℝ) ^ (3 / 2 : ℝ) / Real.sqrt (Real.log n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/860.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/860.lean#L77).

## `Erdos860.erdos_860.variants.erdos_selfridge_lower`

Solved: stated here without proof.

> Erdős and Selfridge proved $h(n)>(3-o(1))n$.
>
> [ErPo80, (19), p. 159] states this as $\limsup h(n)/n \geq 3$, that is, it holds for infinitely
> many $n$. We state that form.

```lean
theorem erdos_860.variants.erdos_selfridge_lower :
    ∀ ε > (0 : ℝ), ∃ᶠ n : ℕ in atTop, (3 - ε) * n ≤ (h n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/860.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/860.lean#L89).

## `Erdos860.erdos_860.variants.ruzsa`

Solved: stated here without proof.

> Ruzsa proved $h(n)/n\to \infty$, as reported in [Er92c, p. 36].

```lean
theorem erdos_860.variants.ruzsa :
    Tendsto (fun n : ℕ ↦ (h n : ℝ) / n) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/860.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/860.lean#L97).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/860.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/860.lean)
- [erdosproblems.com/860](https://www.erdosproblems.com/860)
