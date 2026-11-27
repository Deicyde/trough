---
declaration: theorem
origin: cited
lean: DensityHypothesis.density_hypothesis_zeta_zeros, DensityHypothesis.guth_maynard_zero_density
statement: formalized
---

# Density hypothesis for Riemann zeta zeros

> For $\frac{1}{2} \le \sigma \le 1$ and $T \ge 2$, let $N(\sigma, T)$ count the zeros
> $\rho = \beta + i\gamma$ of $\zeta(s)$ (with multiplicity) inside $\sigma \le \beta \le 1$ and
> $0 < \gamma \le T$. (Classical sources often count $|\gamma| \le T$; by conjugate symmetry of
> $\zeta(s)$ and nonvanishing on $\mathbb{R} \cap [1/2, 1]$, this differs only by a factor of $2$ and
> leaves $O_\varepsilon$ bounds unchanged.) The Density Hypothesis states that
> $N(\sigma, T) = O_\varepsilon(T^{2(1 - \sigma) + \varepsilon})$ uniformly over
> $\frac{1}{2} \le \sigma \le 1$ for every $\varepsilon > 0$. Either the Riemann Hypothesis or
> Lindelöf's hypothesis implies this estimate. Unconditional bounds of the shape
> $N(\sigma, T) = O_\varepsilon(T^{A(\sigma)(1 - \sigma) + \varepsilon})$ were proved by Ingham
> (1940) with $A(\sigma) = \frac{3}{2 - \sigma}$, Huxley (1972) with
> $A(\sigma) = \frac{3}{3\sigma - 1}$, and Guth and Maynard (2024) with
> $A(\sigma) = \frac{15}{5\sigma + 3}$; combining Ingham's bound for $\sigma \le \frac{7}{10}$ with
> Guth and Maynard's bound for $\sigma \ge \frac{7}{10}$ yields the uniform exponent $\frac{30}{13}$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis#The_density_hypothesis)
> - A. E. Ingham, *On the estimation of $N(\sigma, T)$*, Quart. J. Math. Oxford Ser. **11** (1940),
>   DOI: `10.1093/qmath/os-11.1.201`.
> - M. N. Huxley, *On the difference between consecutive primes*, Invent. Math. **15** (1972),
>   164–170.
> - L. Guth and J. Maynard, *New large value estimates for Dirichlet polynomials*, arXiv:2405.20552
>   (2024).

*Quoted from [FormalConjectures/Wikipedia/DensityHypothesis.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DensityHypothesis.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 test statement and 4 API statements, counted here but not shown.

## `DensityHypothesis.density_hypothesis_zeta_zeros`

Open: stated without proof.

> Density Hypothesis: for every $\varepsilon > 0$, there exists $C > 0$ such that
> $N(\sigma, T) \le C \, T^{2(1 - \sigma) + \varepsilon}$ for all $\frac{1}{2} \le \sigma \le 1$
> and $T \ge 2$.

```lean
theorem density_hypothesis_zeta_zeros (ε : ℝ) (hε : 0 < ε) :
    ∃ C : ℝ, 0 < C ∧ ∀ σ T : ℝ, 1 / 2 ≤ σ → σ ≤ 1 → 2 ≤ T →
      (zetaZeroCount σ T : ℝ) ≤ C * T ^ (2 * (1 - σ) + ε)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/DensityHypothesis.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DensityHypothesis.lean#L101).

## `DensityHypothesis.guth_maynard_zero_density`

Solved: stated here without proof.

> Guth–Maynard zero-density bound (2024): for every $\varepsilon > 0$, there exists $C > 0$ such
> that $N(\sigma, T) \le C \, T^{\frac{30}{13}(1 - \sigma) + \varepsilon}$ for all
> $\frac{1}{2} \le \sigma \le 1$ and $T \ge 2$.

```lean
theorem guth_maynard_zero_density (ε : ℝ) (hε : 0 < ε) :
    ∃ C : ℝ, 0 < C ∧ ∀ σ T : ℝ, 1 / 2 ≤ σ → σ ≤ 1 → 2 ≤ T →
      (zetaZeroCount σ T : ℝ) ≤ C * T ^ ((30 / 13 : ℝ) * (1 - σ) + ε)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/DensityHypothesis.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DensityHypothesis.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/DensityHypothesis.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/DensityHypothesis.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Lindel%C3%B6f_hypothesis#The_density_hypothesis)
