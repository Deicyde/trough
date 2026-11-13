---
declaration: theorem
origin: cited
lean: Erdos294.erdos_294, Erdos294.erdos_294.variants.erdos_graham_upper
statement: formalized
---

# Erdős Problem 294

> *References:*
> - [erdosproblems.com/294](https://www.erdosproblems.com/294)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [LiSa24] Liu, Y. and Sawhney, M., *On further questions regarding unit fractions*.
>   [arXiv:2404.07113](https://arxiv.org/abs/2404.07113) (2024).

*Quoted from [FormalConjectures/ErdosProblems/294.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/294.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/294](https://www.erdosproblems.com/294).

The file states 2 research or textbook statements: 2 solved. It also has 2 API statements, counted here but not shown.

## `Erdos294.erdos_294`

Solved: stated here without proof.

> Let $N\geq 1$ and let $t(N)$ be the least integer $t$ such that there is no solution to
>
> $$1=\frac{1}{n_1}+\cdots+\frac{1}{n_k}$$
>
> with $t=n_1\lt \cdots \lt n_k\leq N$. Estimate $t(N)$.
>
> Solved by Liu and Sawhney [LiSa24, Theorem 1.6] (up to $(\log\log N)^{O(1)}$), who proved that
>
> $$\frac{N}{(\log N)(\log\log N)^3(\log\log\log N)^{O(1)}}\ll t(N) \ll \frac{N}{\log N}.$$
>
> The unspecified $O(1)$ exponent is the real number `K`.

```lean
theorem erdos_294 :
    (∃ K : ℝ, (fun N : ℕ => (N : ℝ) / (Real.log N * Real.log (Real.log N) ^ 3 *
        Real.log (Real.log (Real.log N)) ^ K)) ≪ (fun N : ℕ => (t N : ℝ))) ∧
    ((fun N : ℕ => (t N : ℝ)) ≪ (fun N : ℕ => (N : ℝ) / Real.log N))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/294.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/294.lean#L71).

## `Erdos294.erdos_294.variants.erdos_graham_upper`

Solved: stated here without proof.

> Erdős and Graham [ErGr80, p. 35] could show that $t(N)\ll\frac{N}{\log N}$. They gave no proof;
> one is in [LiSa24, Section 4].

```lean
theorem erdos_294.variants.erdos_graham_upper :
    (fun N : ℕ => (t N : ℝ)) ≪ (fun N : ℕ => (N : ℝ) / Real.log N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/294.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/294.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/294.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/294.lean)
- [erdosproblems.com/294](https://www.erdosproblems.com/294)
