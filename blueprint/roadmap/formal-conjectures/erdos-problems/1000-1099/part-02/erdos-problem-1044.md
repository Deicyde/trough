---
declaration: theorem
origin: cited
lean: Erdos1044.erdos_1044, Erdos1044.erdos_1044.variants.infimum_eq_two, Erdos1044.erdos_1044.variants.fixed_degree, Erdos1044.erdos_1044.variants.fixed_degree_of_le_two
statement: formalized
---

# Erdős Problem 1044

> *References:*
> - [erdosproblems.com/1044](https://www.erdosproblems.com/1044)
> - [EHP58] Erdős, P. and Herzog, F. and Piranian, G., *Metric properties of polynomials*.
>   J. Analyse Math. (1958), 125-148.
> - [Ta26] Tang, Quanyu, *On Erdős Problem 1044* (2026),
>   [github.com/QuanyuTang/erdos-problem-1044](https://github.com/QuanyuTang/erdos-problem-1044).

*Quoted from [FormalConjectures/ErdosProblems/1044.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1044.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1044](https://www.erdosproblems.com/1044).

The file states 4 research or textbook statements: 1 open and 3 solved.

## `Erdos1044.erdos_1044`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1044.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1044.lean).

> Let $f(z)=\prod_{i=1}^n(z-z_i)\in\mathbb{C}[x]$ where $\lvert z_i\rvert\leq 1$ for all $i$.
> If $\Lambda(f)$ is the maximum of the lengths of the boundaries of the connected components of
>
> $$
> \{ z: \lvert f(z)\rvert<1\}
> $$
>
> then determine the infimum of $\Lambda(f)$.
>
> A problem of Erdős, Herzog, and Piranian [EHP58].
>
> This has been resolved by Tang, who proved that the infimum of $\Lambda(f)$ over all such $f$
> is $2$.

```lean
theorem erdos_1044 :
    IsGLB {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ maxBoundaryLength f = L} erdos_1044.answer
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1044.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1044.lean#L71).

## `Erdos1044.erdos_1044.variants.infimum_eq_two`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1044.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1044.lean).

> This has been resolved by Tang, who proved that the infimum of $\Lambda(f)$ over all such $f$
> is $2$.

```lean
theorem erdos_1044.variants.infimum_eq_two :
    IsGLB {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ maxBoundaryLength f = L} 2
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1044.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1044.lean#L81).

## `Erdos1044.erdos_1044.variants.fixed_degree`

Open: stated without proof.

> Tang also suggests that, if the degree $n$ is fixed, then the infimum over all such $f$ of
> degree $n$ is attained by $f_n(z)=z^n-1$.

```lean
theorem erdos_1044.variants.fixed_degree (n : ℕ) (hn : 0 < n) :
    IsLeast {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ f.natDegree = n ∧ maxBoundaryLength f = L}
      (maxBoundaryLength (X ^ n - 1))
```

Category `research open`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1044.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1044.lean#L90).

## `Erdos1044.erdos_1044.variants.fixed_degree_of_le_two`

Solved: stated here without proof.

> Tang also suggests that, if the degree $n$ is fixed, then the infimum over all such $f$ of
> degree $n$ is attained by $f_n(z)=z^n-1$ (and proves this for $n=1$ and $n=2$).

```lean
theorem erdos_1044.variants.fixed_degree_of_le_two (n : ℕ) (hn : n = 1 ∨ n = 2) :
    IsLeast {L : ℝ≥0∞ | ∃ f : ℂ[X], IsAdmissible f ∧ f.natDegree = n ∧ maxBoundaryLength f = L}
      (maxBoundaryLength (X ^ n - 1))
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1044.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1044.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1044.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1044.lean)
- [erdosproblems.com/1044](https://www.erdosproblems.com/1044)
