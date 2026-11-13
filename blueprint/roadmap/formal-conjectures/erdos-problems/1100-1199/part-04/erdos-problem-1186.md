---
declaration: theorem
origin: cited
lean: Erdos1186.erdos_1186, Erdos1186.erdos_1186.variants.van_der_waerden, Erdos1186.erdos_1186.variants.probabilistic, Erdos1186.erdos_1186.variants.prs_bounds, Erdos1186.erdos_1186.variants.prs_conjecture
statement: formalized
---

# Erdős Problem 1186

> *References:*
> - [erdosproblems.com/1186](https://www.erdosproblems.com/1186)
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   (1980), 89-115. [PDF](https://www.renyi.hu/~p_erdos/1980-03.pdf)
> - [PRS08] Parrilo, Pablo A. and Robertson, Aaron and Saracino, Dan, *On the asymptotic minimum
>   number of monochromatic 3-term arithmetic progressions*. J. Combin. Theory Ser. A (2008),
>   185-192. [arXiv:math/0609532](https://arxiv.org/abs/math/0609532)

*Quoted from [FormalConjectures/ErdosProblems/1186.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1186.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1186](https://www.erdosproblems.com/1186).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos1186.erdos_1186`

Open: stated without proof.

> Let $\delta_k$ be such that in any $2$-colouring of $\{1,\ldots,n\}$ there exist at least
> $(\delta_k+o(1))n^2$ many monochromatic $k$-term arithmetic progressions. Give reasonable bounds
> (or even an asymptotic formula) for $\delta_k$.
>
> We read "reasonable bounds" as determining the order of magnitude of $\delta_k$ as $k \to \infty$.

```lean
theorem erdos_1186 : δ =Θ[atTop] erdos_1186.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1186.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1186.lean#L92).

## `Erdos1186.erdos_1186.variants.van_der_waerden`

Solved: stated here without proof.

> Van der Waerden's theorem implies $\delta_k\gg_k 1$.
>
> For fixed $k$ this says $\delta_k > 0$.

```lean
theorem erdos_1186.variants.van_der_waerden (k : ℕ) (hk : 2 ≤ k) : 0 < δ k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1186.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1186.lean#L101).

## `Erdos1186.erdos_1186.variants.probabilistic`

Solved: stated here without proof.

> The probabilistic method implies
>
> $$\delta_k \leq \frac{1}{(k-1)2^{k}}.$$

```lean
theorem erdos_1186.variants.probabilistic (k : ℕ) (hk : 2 ≤ k) :
    δ k ≤ 1 / (((k : ℝ) - 1) * 2 ^ k)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1186.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1186.lean#L109).

## `Erdos1186.erdos_1186.variants.prs_bounds`

Solved: stated here without proof.

> Parrilo, Robertson, and Saracino [PRS08] have proved
>
> $$0.0511\approx \frac{1675}{32768}\leq \delta_3 \leq \frac{117}{2192}\approx 0.0533,$$
>
> and conjectured the upper bound is correct.

```lean
theorem erdos_1186.variants.prs_bounds : 1675 / 32768 ≤ δ 3 ∧ δ 3 ≤ 117 / 2192
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1186.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1186.lean#L119).

## `Erdos1186.erdos_1186.variants.prs_conjecture`

Open: stated without proof.

> Parrilo, Robertson, and Saracino [PRS08] have proved
>
> $$0.0511\approx \frac{1675}{32768}\leq \delta_3 \leq \frac{117}{2192}\approx 0.0533,$$
>
> and conjectured the upper bound is correct.
>
> This is the conjecture $\delta_3 = \frac{117}{2192}$.

```lean
theorem erdos_1186.variants.prs_conjecture : δ 3 = 117 / 2192
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1186.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1186.lean#L130).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1186.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1186.lean)
- [erdosproblems.com/1186](https://www.erdosproblems.com/1186)
