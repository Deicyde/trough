---
declaration: theorem
origin: cited
lean: Erdos1162.erdos_1162, Erdos1162.erdos_1162.variants.pyber, Erdos1162.erdos_1162.variants.roney_dougal_tracey, Erdos1162.erdos_1162.variants.roney_dougal_tracey_bounds
statement: formalized
---

# Erdős Problem 1162

> *References:*
> - [erdosproblems.com/1162](https://www.erdosproblems.com/1162)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).
> - [Py93] Pyber, L., *Asymptotic results for permutation groups*. Groups and computation
>   (New Brunswick, NJ, 1991), DIMACS Ser. Discrete Math. Theoret. Comput. Sci. 11 (1993),
>   197-219.
> - [RoTr25] Roney-Dougal, C. M. and Tracey, G., *Subgroups of symmetric groups: enumeration and
>   asymptotic properties*. [arXiv:2503.05416](https://arxiv.org/abs/2503.05416) (2025).

*Quoted from [FormalConjectures/ErdosProblems/1162.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1162.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1162](https://www.erdosproblems.com/1162).

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1162.erdos_1162`

Open: stated without proof.

> Give an asymptotic formula for the number of subgroups of $S_n$. Is there a statistical theorem
> on their order?
>
> A problem of Erdős and Turán [Va99, 5.73]. We state the first question: `erdos_1162.answer` is a
> function asymptotically equivalent to the number $f(n)$ of subgroups of $S_n$ (an explicit
> formula is intended, not $f$ itself). The second question is too vague to state.

```lean
theorem erdos_1162 :
    (fun n : ℕ ↦ (f n : ℝ)) ~[atTop] erdos_1162.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1162.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1162.lean#L61).

## `Erdos1162.erdos_1162.variants.pyber`

Solved: stated here without proof.

> Pyber [Py93] proved that
>
> $$\log f(n)\asymp n^2.$$

```lean
theorem erdos_1162.variants.pyber :
    (fun n : ℕ ↦ Real.log (f n : ℝ)) =Θ[atTop] fun n : ℕ ↦ (n : ℝ) ^ 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1162.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1162.lean#L70).

## `Erdos1162.erdos_1162.variants.roney_dougal_tracey`

Solved: stated here without proof.

> Roney-Dougal and Tracey [RoTr25] have proved that
>
> $$\log f(n)=\left(\frac{1}{16}+o(1)\right)n^2.$$
>
> Here $\log$ is the logarithm to base $2$, as in [RoTr25].

```lean
theorem erdos_1162.variants.roney_dougal_tracey :
    (fun n : ℕ ↦ Real.logb 2 (f n : ℝ)) ~[atTop] fun n : ℕ ↦ (n : ℝ) ^ 2 / 16
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1162.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1162.lean#L80).

## `Erdos1162.erdos_1162.variants.roney_dougal_tracey_bounds`

Solved: stated here without proof.

> Roney-Dougal and Tracey [RoTr25, Theorem 1] proved that there are absolute constants
> $\alpha>0$ and $\beta$ such that for all integers $n>1$
>
> $$2^{n^2/16+\alpha n\log n}\leq f(n)\leq 2^{n^2/16+\beta n^{3/2}},$$
>
> where $\log$ is the logarithm to base $2$. This implies the previous variant.

```lean
theorem erdos_1162.variants.roney_dougal_tracey_bounds :
    ∃ α > (0 : ℝ), ∃ β : ℝ, ∀ n : ℕ, 1 < n →
      (2 : ℝ) ^ ((n : ℝ) ^ 2 / 16 + α * n * Real.logb 2 n) ≤ f n ∧
        (f n : ℝ) ≤ (2 : ℝ) ^ ((n : ℝ) ^ 2 / 16 + β * (n : ℝ) ^ ((3 : ℝ) / 2))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1162.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1162.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1162.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1162.lean)
- [erdosproblems.com/1162](https://www.erdosproblems.com/1162)
