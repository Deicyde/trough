---
declaration: theorem
origin: cited
lean: MultivariableMahlerMeasure.lawton_multivariable_mahler_measure_limit, MultivariableMahlerMeasure.smyth_three_variable_linear_mahler_measure, MultivariableMahlerMeasure.boyd_mahler_measure_set_closed_conjecture, MultivariableMahlerMeasure.boyd_mahler_measure_strict_hierarchy_conjecture
statement: formalized
---

# Lawton's Multivariable Mahler Limit and Boyd's Range Conjectures

> Given a nonzero polynomial $P \in \mathbb{C}[X_0, \dots, X_{n-1}]$, its logarithmic Mahler measure
> integrates $\log \|P\|$ across the complex unit $n$-torus $\mathbb{T}^n$:
>
> $$m(P) = \int_{[0, 1]^n}
>   \log \|P(e^{2\pi i \theta_0}, \dots, e^{2\pi i \theta_{n-1}})\| \, d\theta.$$
>
> David W. Boyd (1981) conjectured—and Wayne M. Lawton (1983) proved—that $m(P)$ equals the limit of
> specialized univariate measures $m(P(t^{r_0}, \dots, t^{r_{n-1}}))$ once the shortest nonzero
> integer relation norm $q(r) = \min \{ \max_j |s_j| : s \in \mathbb{Z}^n \setminus \{0\},
> \sum_j s_j r_j = 0 \}$ grows unboundedly. Writing $L_n$ for the values $m(P)$ over nonzero
> $P \in \mathbb{Z}[X_0, \dots, X_{n-1}]$ and $L_\infty = \bigcup_n L_n$, Boyd conjectured both that
> $L_\infty$ is closed in $\mathbb{R}$ (which implies
> `LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem`) and that
> $L_1 \subsetneq L_2 \subsetneq L_3 \subsetneq \cdots$. Christopher J. Smyth (1981) established
> $m(1 + X_0 + X_1 + X_2) = \frac{7}{2\pi^2} \zeta(3)$.
>
> *References:*
> - [Wikipedia: Mahler measure](https://en.wikipedia.org/wiki/Mahler_measure)
> - D. W. Boyd (1981), Canad. Math. Bull. **24**, no. 4, 453–469, DOI: `10.4153/cmb-1981-069-5`.
> - C. J. Smyth (1981), Bull. Austral. Math. Soc. **23**, no. 1, 49–63.
> - W. M. Lawton (1983), J. Number Theory **16**, no. 3, 356–362,
>   DOI: `10.1016/0022-314X(83)90063-X`.

*Quoted from [FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 3 test statements and 1 API statement, counted here but not shown.

## `MultivariableMahlerMeasure.lawton_multivariable_mahler_measure_limit`

Solved: stated here without proof.

> **Lawton's Multivariable Limit Theorem** (conjectured by Boyd 1981, proved by Lawton 1983):
> for every nonzero $P \in \mathbb{C}[X_0, \dots, X_{n-1}]$ and $\varepsilon > 0$, some threshold
> $B \in \mathbb{N}$ ensures $|m(P(t^{r_0}, \dots, t^{r_{n-1}})) - m(P)| < \varepsilon$ whenever
> $q(r) > B$.

```lean
theorem lawton_multivariable_mahler_measure_limit {n : ℕ} (P : MvPolynomial (Fin n) ℂ)
    (hP : P ≠ 0) (ε : ℝ) (hε : 0 < ε) :
    ∃ B : ℕ, ∀ r : Fin n → ℤ, HasNoShortRelation B r →
      |univariateSpecLogMahler P r - logMahlerMeasure P| < ε
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean#L115).

## `MultivariableMahlerMeasure.smyth_three_variable_linear_mahler_measure`

Solved: stated here without proof.

> **Smyth's Linear Mahler Formula** (1981): $1 + X_0 + X_1 + X_2$ has logarithmic measure
> $\frac{7}{2\pi^2} \zeta(3)$.

```lean
theorem smyth_three_variable_linear_mahler_measure :
    logMahlerMeasure
        (1 + MvPolynomial.X 0 + MvPolynomial.X 1 + MvPolynomial.X 2 : MvPolynomial (Fin 3) ℂ) =
      7 / (2 * Real.pi ^ 2) * (riemannZeta 3).re
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean#L124).

## `MultivariableMahlerMeasure.boyd_mahler_measure_set_closed_conjecture`

Open: stated without proof.

> **Boyd's Closedness Conjecture** (1981): $L_\infty = \bigcup_{n \in \mathbb{N}} L_n$ (which
> equals $\bigcup_{n \ge 1} L_n$ since $L_0 \subseteq L_1$ via constant polynomials) is closed inside
> $\mathbb{R}$. This implies `LehmerMahlerMeasureProblem.lehmer_mahler_measure_problem`.

```lean
theorem boyd_mahler_measure_set_closed_conjecture :
    IsClosed (⋃ n, intLogMahlerSet n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean#L134).

## `MultivariableMahlerMeasure.boyd_mahler_measure_strict_hierarchy_conjecture`

Open: stated without proof.

> **Boyd's Strict Hierarchy Conjecture** (1981): every dimension $n \ge 1$ satisfies the strict
> inclusion $L_n \subsetneq L_{n + 1}$ (note $n = 0$ is excluded because $L_0 \subsetneq L_1$ holds
> unconditionally).

```lean
theorem boyd_mahler_measure_strict_hierarchy_conjecture {n : ℕ} (hn : 1 ≤ n) :
    intLogMahlerSet n ⊂ intLogMahlerSet (n + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean#L142).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/MultivariableMahlerMeasure.lean)
- [Wikipedia: Mahler measure](https://en.wikipedia.org/wiki/Mahler_measure)
