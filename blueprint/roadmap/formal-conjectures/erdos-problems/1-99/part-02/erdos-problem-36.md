---
declaration: theorem
origin: cited
lean: Erdos36.minimum_overlap.variants.lower.erdos_1955, Erdos36.minimum_overlap.variants.lower.scherk_1955, Erdos36.minimum_overlap.variants.lower.swierczkowski_1958, Erdos36.minimum_overlap.variants.lower.haugland_1996, Erdos36.minimum_overlap.variants.lower.white_2022, Erdos36.minimum_overlap.variants.upper.erdos_1955, Erdos36.minimum_overlap.variants.upper.MRS_1956, Erdos36.minimum_overlap.variants.upper.haugland_1996, Erdos36.minimum_overlap.variants.upper.haugland_2022, Erdos36.erdos_36.variants.lower, Erdos36.erdos_36.variants.upper, Erdos36.erdos_36.variants.exists, Erdos36.erdos_36
statement: formalized
---

# Erdős Problem 36

> *References:*
>  - [erdosproblems.com/36](https://www.erdosproblems.com/36)
>  - [Wikipedial: Minimum overlap problem](https://en.wikipedia.org/wiki/Minimum_overlap_problem)

*Quoted from [FormalConjectures/ErdosProblems/36.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/36](https://www.erdosproblems.com/36).

The file states 13 research or textbook statements: 3 open, 9 solved and 1 textbook result. It also has 5 test statements, counted here but not shown.

## `Erdos36.minimum_overlap.variants.lower.erdos_1955`

Textbook result, stated without proof. A Lean proof is at [https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L52](https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L52).

> A lower bound of $\frac 1 4$.
> See [Some remarks on number theory (in Hebrew)](https://users.renyi.hu/~p_erdos/1955-13.pdf)
> by *Paul Erdős*, Riveon Lematematika 9, p.45-48,1955

```lean
theorem minimum_overlap.variants.lower.erdos_1955 :
    (1 : ℝ) / 4 ≤ atTop.liminf MinOverlapQuotient
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 269](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L269).

## `Erdos36.minimum_overlap.variants.lower.scherk_1955`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L56](https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L56).

> A lower bound of $1 - frac{1}{\sqrt 2}$.
> Scherk (written communication), see
> [On the minimal overlap problem of Erdös](https://eudml.org/doc/206397)
> by *Leo Moser*, Аста Аrithmetica V, p. 117-119, 1959

```lean
theorem minimum_overlap.variants.lower.scherk_1955 :
    1 - (√2)⁻¹ < atTop.liminf MinOverlapQuotient
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 282](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L282).

## `Erdos36.minimum_overlap.variants.lower.swierczkowski_1958`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L60](https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L60).

> A lower bound of $\frac{4 - \sqrt{6}}{5}$.
> See [On the intersection of a linear set with the translation of its complement](https://bibliotekanauki.pl/articles/969027)
> by *Stanisław Świerczkowski1*, Colloquium Mathematicum 5(2), p. 185-197, 1958

```lean
theorem minimum_overlap.variants.lower.swierczkowski_1958 :
    (4 - 6 ^ ((1 : ℝ) / 2)) / 5 < atTop.liminf MinOverlapQuotient
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 295](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L295).

## `Erdos36.minimum_overlap.variants.lower.haugland_1996`

Solved: stated here without proof.

> A lower bound of $\sqrt{4 - \sqrt{15}}$.

```lean
theorem minimum_overlap.variants.lower.haugland_1996 :
    (4 - 15 ^((1 : ℝ) / 2)) ^ ((1 : ℝ) / 2) < atTop.liminf MinOverlapQuotient
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 303](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L303).

## `Erdos36.minimum_overlap.variants.lower.white_2022`

Solved: stated here without proof.

> A lower bound of $0.379005$: the minimum overlap constant is at least $0.379005$.
> See [Erdős' minimum overlap problem](https://arxiv.org/abs/2201.05704)
> by *Ethan Patrick White*, 2022

```lean
theorem minimum_overlap.variants.lower.white_2022 :
    0.379005 ≤ atTop.liminf MinOverlapQuotient
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 313](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L313).

## `Erdos36.minimum_overlap.variants.upper.erdos_1955`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L68](https://github.com/linrock/math-proofs/blob/22db103d7b6109baca46f2623a7287b965a56936/erdos-36/Solution.lean#L68).

> The example (with $N$ even), $A = \{\frac N 2 + 1, \dots, \frac{3N}{2}\}$
> shows an upper bound of $\frac 1 2$.

```lean
theorem minimum_overlap.variants.upper.erdos_1955 :
    atTop.limsup MinOverlapQuotient ≤ (1 : ℝ) / 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 324](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L324).

## `Erdos36.minimum_overlap.variants.upper.MRS_1956`

Solved: stated here without proof.

> An upper bound of $\frac 2 5$.
> See [Minimal overlapping under translation.](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society/volume-62/issue-6)
> by *T. S. Motzkin*, *K. E. Ralston* and *J. L. Selfridge*,
> in "The summer meeting in Seattle" by *V. L. Klee Jr.*, Bull. Amer. Math. Soc.62, p. 558, 1956

```lean
theorem minimum_overlap.variants.upper.MRS_1956 :
    atTop.limsup MinOverlapQuotient ≤ (2 : ℝ) / 5
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 335](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L335).

## `Erdos36.minimum_overlap.variants.upper.haugland_1996`

Solved: stated here without proof.

> An upper bound of $0.38200298812318988$.
> See [Advances in the Minimum Overlap Problem](https://doi.org/10.1006%2Fjnth.1996.0064)
> by *Jan Kristian Haugland*, Journal of Number Theory Volume 58, Issue 1, p 71-78, 1996

```lean
theorem minimum_overlap.variants.upper.haugland_1996 :
    atTop.limsup MinOverlapQuotient ≤ 0.38200298812318988
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 345](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L345).

## `Erdos36.minimum_overlap.variants.upper.haugland_2022`

Solved: stated here without proof.

> An upper bound of $0.3809268534330870$.
> See [The minimum overlap problem](https://www.neutreeko.net/mop/index.htm)
> by *Jan Kristian Haugland*

```lean
theorem minimum_overlap.variants.upper.haugland_2022 :
    atTop.limsup MinOverlapQuotient ≤ 0.3809268534330870
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 355](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L355).

## `Erdos36.erdos_36.variants.lower`

Open: stated without proof.

> Find a better lower bound!

```lean
theorem erdos_36.variants.lower:
    ∃ (c : ℝ), 0.379005 < c ∧ c ≤ atTop.liminf MinOverlapQuotient ∧ c =
      erdos_36.variants.lower.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 364](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L364).

## `Erdos36.erdos_36.variants.upper`

Open: stated without proof.

> Find a better upper bound!

```lean
theorem erdos_36.variants.upper :
    ∃ (c : ℝ), c < 0.380926853433087 ∧ atTop.limsup MinOverlapQuotient ≤ c ∧ c =
      erdos_36.variants.upper.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 375](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L375).

## `Erdos36.erdos_36.variants.exists`

Solved: stated here without proof.

> The limit of `MinOverlapQuotient` exists and it is less than $0.385694$.

```lean
theorem erdos_36.variants.exists : ∃ c, atTop.Tendsto MinOverlapQuotient (𝓝 c) ∧ c < 0.385694
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 384](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L384).

## `Erdos36.erdos_36`

Open: stated without proof.

> Find the value of the limit of `MinOverlapQuotient`!

```lean
theorem erdos_36 : atTop.Tendsto MinOverlapQuotient (𝓝 erdos_36.answer)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/36.lean, line 393](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean#L393).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/36.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/36.lean)
- [erdosproblems.com/36](https://www.erdosproblems.com/36)
