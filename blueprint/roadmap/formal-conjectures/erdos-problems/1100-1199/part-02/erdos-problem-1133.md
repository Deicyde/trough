---
declaration: theorem
origin: cited
lean: Erdos1133.erdos_1133, Erdos1133.erdos_1133.variants.weaker
statement: formalized
---

# Erdős Problem 1133

> *References:*
> - [erdosproblems.com/1133](https://www.erdosproblems.com/1133)
> - [Er67] Erdős, P., Problems and results on the convergence and divergence properties of the
>   Lagrange interpolation polynomials and some extremal problems. Mathematica (Cluj) (1967), 65-73.
> - [Ya26] Yang, J.-Q., *Erdős's Robust Polynomial Interpolation Problem: the Optimal Exponential
>   Scale*. [arXiv:2609.14769](https://arxiv.org/abs/2609.14769) (2026).

*Quoted from [FormalConjectures/ErdosProblems/1133.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1133.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1133](https://www.erdosproblems.com/1133).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1133.erdos_1133`

Solved: stated here without proof.

> Let $C>0$. There exists $\epsilon>0$ such that if $n$ is sufficiently large the following holds.
>
> For any $x_1,\ldots,x_n\in [-1,1]$ there exist $y_1,\ldots,y_n\in [-1,1]$ such that, if $P$ is a
> polynomial of degree $m<(1+\epsilon)n$ with $P(x_i)=y_i$ for at least $(1-\epsilon)n$ many
> $1\leq i\leq n$, then
>
> $$\max_{x\in [-1,1]}\lvert P(x)\rvert >C.$$
>
> Yang [Ya26, Theorem 2.1] proved this, including repeated nodes, by taking $\rho=0$.

```lean
theorem erdos_1133 :
    ∀ C > (0 : ℝ), ∃ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∀ x : Fin n → Icc (-1 : ℝ) 1,
        ∃ y : Fin n → Icc (-1 : ℝ) 1,
          ∀ P : Polynomial ℝ,
            (P.natDegree : ℝ) < (1 + ε) * (n : ℝ) →
            ((Finset.univ.filter (fun i ↦ P.eval (x i : ℝ) = (y i : ℝ))).card : ℝ) ≥
              (1 - ε) * (n : ℝ) →
            ∃ z ∈ Icc (-1 : ℝ) 1, |P.eval z| > C
```

Category `research solved`; AMS [26 Real functions](../../../by-subject/part-01/26-real-functions/README.md), [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1133.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1133.lean#L47).

## `Erdos1133.erdos_1133.variants.weaker`

Solved: stated here without proof.

> Erdős proved that, for any $C>0$, there exists $\epsilon>0$ such that if $n$ is sufficiently
> large and $m=\lfloor (1+\epsilon)n\rfloor$ then for any $x_1,\ldots,x_m\in [-1,1]$ there is a
> polynomial $P$ of degree $n$ such that $\lvert P(x_i)\rvert\leq 1$ for $1\leq i\leq m$ and
> $\max_{x\in [-1,1]}\lvert P(x)\rvert>C$. The robust interpolation statement above also implies
> this result. Erdős in [Er67] could not prove the robust statement even for $m=n$.

```lean
theorem erdos_1133.variants.weaker :
    ∀ C > (0 : ℝ), ∃ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      let m := ⌊(1 + ε) * (n : ℝ)⌋₊;
      ∀ x : Fin m → Icc (-1 : ℝ) 1,
        ∃ P : Polynomial ℝ,
          P.natDegree = n ∧
          (∀ i : Fin m, |P.eval (x i : ℝ)| ≤ 1) ∧
          ∃ z ∈ Icc (-1 : ℝ) 1, |P.eval z| > C
```

Category `research solved`; AMS [26 Real functions](../../../by-subject/part-01/26-real-functions/README.md), [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1133.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1133.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1133.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1133.lean)
- [erdosproblems.com/1133](https://www.erdosproblems.com/1133)
