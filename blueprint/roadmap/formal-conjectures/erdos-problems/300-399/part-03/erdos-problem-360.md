---
declaration: theorem
origin: cited
lean: Erdos360.erdos_360, Erdos360.erdos_360.variants.alon_erdos, Erdos360.erdos_360.variants.vu
statement: formalized
---

# Erdős Problem 360

> *References:*
> - [erdosproblems.com/360](https://www.erdosproblems.com/360)
> - [AlEr96] Alon, Noga and Erdős, Paul, *Sure monochromatic subset sums*. Acta Arith. 74 (1996),
>   269-272.
> - [CFP21] Conlon, D. and Fox, J. and Pham, H. T., *Subset sums, completeness and colorings*.
>   [arXiv:2104.14766](https://arxiv.org/abs/2104.14766) (2021).
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathématique (1980).
> - [Vu07] Vu, Van H., *Some new results on subset sums*. J. Number Theory 124 (2007), 229-233.

*Quoted from [FormalConjectures/ErdosProblems/360.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/360.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/360](https://www.erdosproblems.com/360).

The file states 3 research or textbook statements: 3 solved.

## `Erdos360.erdos_360`

Solved: stated here without proof.

> Let $f(n)$ be minimal such that $\{1,\ldots,n-1\}$ can be partitioned into $f(n)$ classes so that
> $n$ cannot be expressed as a sum of distinct elements from the same class. How fast does $f(n)$
> grow?
>
> A problem of Erdős and Graham [ErGr80]. Conlon, Fox, and Pham [CFP21, Theorem 1.5] determined
> the order of growth of $f(n)$ up to a multiplicative constant, proving
>
> $$f(n) \asymp \frac{n^{1/3}(n/\phi(n))}{(\log n)^{1/3}(\log\log n)^{2/3}}.$$
>
> Here $\phi$ is Euler's totient function, and the statement is asymptotic ($n \to \infty$).

```lean
theorem erdos_360 : (fun n : ℕ ↦ (f n : ℝ)) =Θ[atTop] erdos_360.answer
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/360.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/360.lean#L67).

## `Erdos360.erdos_360.variants.alon_erdos`

Solved: stated here without proof.

> Alon and Erdős [AlEr96] proved that $f(n) = n^{1/3+o(1)}$, and more precisely
>
> $$\frac{n^{1/3}}{(\log n)^{4/3}}\ll f(n) \ll
>   \frac{n^{1/3}}{(\log n)^{1/3}}(\log\log n)^{1/3}.$$
>
> This is the two-sided bound, which implies the first claim.

```lean
theorem erdos_360.variants.alon_erdos :
    (fun n : ℕ ↦ (n : ℝ) ^ (1 / 3 : ℝ) / Real.log n ^ (4 / 3 : ℝ)) =O[atTop]
        (fun n : ℕ ↦ (f n : ℝ)) ∧
    (fun n : ℕ ↦ (f n : ℝ)) =O[atTop]
        (fun n : ℕ ↦ (n : ℝ) ^ (1 / 3 : ℝ) / Real.log n ^ (1 / 3 : ℝ) *
          Real.log (Real.log n) ^ (1 / 3 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/360.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/360.lean#L77).

## `Erdos360.erdos_360.variants.vu`

Solved: stated here without proof.

> Vu [Vu07] improved the lower bound to
>
> $$f(n) \gg \frac{n^{1/3}}{\log n}.$$

```lean
theorem erdos_360.variants.vu :
    (fun n : ℕ ↦ (n : ℝ) ^ (1 / 3 : ℝ) / Real.log n) =O[atTop] (fun n : ℕ ↦ (f n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/360.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/360.lean#L90).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/360.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/360.lean)
- [erdosproblems.com/360](https://www.erdosproblems.com/360)
