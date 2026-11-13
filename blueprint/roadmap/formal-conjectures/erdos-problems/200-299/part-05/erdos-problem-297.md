---
declaration: theorem
origin: cited
lean: Erdos297.erdos_297, Erdos297.erdos_297.variants.steinerberger, Erdos297.erdos_297.variants.general
statement: formalized
---

# Erdős Problem 297

> *References:*
> - [erdosproblems.com/297](https://www.erdosproblems.com/297)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [CFHMPSV24] Conlon, D., Fox, J., He, X., Mubayi, D., Pham, H. T., Suk, A. and Verstraëte, J.,
>   *A question of Erdős and Graham on Egyptian fractions*. arXiv:2404.16016 (2024).
> - [LiSa24] Liu, Y. P. and Sawhney, M., *On further questions regarding unit fractions*.
>   arXiv:2404.07113 (2024).
> - [St24] Steinerberger, S., *On a problem involving unit fractions*. arXiv:2403.17041 (2024).

*Quoted from [FormalConjectures/ErdosProblems/297.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/297.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/297](https://www.erdosproblems.com/297).

The file states 3 research or textbook statements: 3 solved. It also has 3 test statements, counted here but not shown.

## `Erdos297.erdos_297`

Solved: stated here without proof.

> Let $N\geq 1$. How many $A\subseteq \{1,\ldots,N\}$ are there such that
> $\sum_{n\in A}\frac{1}{n}=1$?
>
> Liu and Sawhney [LiSa24] proved that the count is $2^{(0.91\cdots+o(1))N}$, where $0.91\cdots$ is
> an explicit number defined as the solution to a certain integral equation; independently the same
> asymptotic was proved by Conlon, Fox, He, Mubayi, Pham, Suk, and Verstraëte [CFHMPSV24]. We
> formalise the question as asking for the exponential growth rate
> $\lim_{N\to\infty} \frac{1}{N}\log_2 \#\{A\}$. The first conjunct is the existence and
> uniqueness of $\lambda^*$, which [LiSa24] state with the theorem.

```lean
theorem erdos_297 : (∃! l : ℝ, massIntegral l = 1) ∧
    Tendsto (fun N : ℕ => Real.logb 2 (count 1 N) / N) atTop (𝓝 erdos_297.answer)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/297.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/297.lean#L87).

## `Erdos297.erdos_297.variants.steinerberger`

Solved: stated here without proof.

> Steinerberger [St24] proved that, for $N$ sufficiently large, the number of
> $A \subseteq \{1, \ldots, N\}$ with $\sum_{n\in A}\frac{1}{n} \leq 1$ is at most $2^{0.93N}$.

```lean
theorem erdos_297.variants.steinerberger : ∀ᶠ N : ℕ in atTop,
    ({A ∈ (Finset.Icc 1 N).powerset | ∑ n ∈ A, (1 / (n : ℕ) : ℚ) ≤ 1}.card : ℝ) ≤
      2 ^ (0.93 * N : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/297.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/297.lean#L96).

## `Erdos297.erdos_297.variants.general`

Solved: stated here without proof.

> Conlon, Fox, He, Mubayi, Pham, Suk, and Verstraëte [CFHMPSV24] prove more generally, for any
> $x\in \mathbb{Q}_{>0}$, that the number of $A\subseteq \{1,\ldots,N\}$ such that
> $\sum_{n\in A}\frac{1}{n}=x$ is $2^{(c_x + o(1))N}$, with $c_x$ as in `exponentOf`.

```lean
theorem erdos_297.variants.general (x : ℚ) (hx : 0 < x) : (∃! l : ℝ, massIntegral l = x) ∧
    Tendsto (fun N : ℕ => Real.logb 2 (count x N) / N) atTop (𝓝 (exponentOf x))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/297.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/297.lean#L114).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/297.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/297.lean)
- [erdosproblems.com/297](https://www.erdosproblems.com/297)
