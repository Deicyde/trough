---
declaration: lemma
origin: cited
lean: MeanValueProblem.mean_value_problem, MeanValueProblem.mean_value_problem_leq_4, MeanValueProblem.mean_value_problem_of_real_roots, MeanValueProblem.mean_value_problem_of_roots_same_norm
statement: formalized
---

# Mean value problem

> *Reference:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Mean_value_problem)
> - [The fundamental theorem of algebra and complexity theory](https://www.ams.org/journals/bull/1981-04-01/S0273-0979-1981-14858-8/)
> by Steve Smale
>
> Given a complex polynomial $p$ of degree $d ≥ 2$ and a complex number $z$
> there is a critical point $c$ of $p$, such that $|p(z)-p(c)|/|z-c| ≤ K* |p'(z)|$ for $K=1$.
>
>
> The conjecture has been proven for:
> * `K = 4`
>   [The fundamental theorem of algebra and complexity theory](https://www.ams.org/journals/bull/1981-04-01/S0273-0979-1981-14858-8/)
>   by *Steve Smale*
> * `K = (d-1)/d` at a point $z$ if the normalised polynomial $p(X + z) - p(z)$ has only real
>   roots, or if all its nonzero roots have the same norm.
>   [Critical points and values of complex polynomials](https://doi.org/10.1016/0885-064X(89)90019-8)
>   by *David Tischler*

*Quoted from [FormalConjectures/Wikipedia/MeanValueProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeanValueProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved.

## `MeanValueProblem.mean_value_problem`

Open: stated without proof.

> Given a complex polynomial $p$ of degree $d ≥ 2$ and a complex number $z$
> there is a critical point $c$ of $p$, such that $|p(z)-p(c)|/|z-c| ≤ |p'(z)|$.

```lean
lemma mean_value_problem (p : Polynomial ℂ) (hp : 2 ≤ p.degree) (z : ℂ) (K : ℝ):
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ ‖p.derivative.eval z‖
```

Category `research open`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/MeanValueProblem.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeanValueProblem.lean#L52).

## `MeanValueProblem.mean_value_problem_leq_4`

Solved: stated here without proof.

> The following weaker version of the mean value problem has been proven.
> Given a complex polynomial $p$ of degree $d ≥ 2$ and a complex number $z$
> there a critical point $c$ of $p$, such that $|p(z)-p(c)|/|z-c| ≤ 4|p'(z)|$.

```lean
lemma mean_value_problem_leq_4 (p : Polynomial ℂ) (hp : 2 ≤ p.degree) (z : ℂ) (K : ℝ):
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ 4 *‖p.derivative.eval z‖
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/MeanValueProblem.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeanValueProblem.lean#L63).

## `MeanValueProblem.mean_value_problem_of_real_roots`

Solved: stated here without proof.

> The following tighter bound depending on the degree $d$ of the polynomial $p$ has been shown by
> Tischler. Let $z$ be a complex number such that the normalised polynomial $p(X + z) - p(z)$ has
> only real roots, i.e. every $x$ with $p(x) = p(z)$ satisfies
> $\operatorname{Im} x = \operatorname{Im} z$. Then there is a critical point $c$ of $p$ such that
> $|p(z)-p(c)|/|z-c| \le (d-1)/d \cdot |p'(z)|$.

```lean
lemma mean_value_problem_of_real_roots (p : Polynomial ℂ) (hp : 2 ≤ p.natDegree) (z : ℂ)
    (h : ∀ x : ℂ, p.eval x = p.eval z → x.im = z.im) (K : ℝ) :
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ (p.natDegree - 1)/ p.natDegree * ‖p.derivative.eval z‖
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/MeanValueProblem.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeanValueProblem.lean#L77).

## `MeanValueProblem.mean_value_problem_of_roots_same_norm`

Solved: stated here without proof.

> The following tighter bound depending on the degree $d$ of the polynomial $p$ has been shown by
> Tischler. Let $z$ be a complex number such that all nonzero roots of the normalised polynomial
> $p(X + z) - p(z)$ have the same norm, i.e. all $x \ne z$ with $p(x) = p(z)$ have the same
> distance to $z$. Then there is a critical point $c$ of $p$ such that
> $|p(z) - p(c)|/|z-c| \le (d-1)/d \cdot |p'(z)|$.

```lean
lemma mean_value_problem_of_roots_same_norm (p : Polynomial ℂ) (hp : 2 ≤ p.natDegree) (z : ℂ)
    (h : ∀ x y : ℂ, p.eval x = p.eval z → p.eval y = p.eval z → x ≠ z → y ≠ z →
      ‖x - z‖ = ‖y - z‖) (K : ℝ) :
    ∃ c : ℂ, p.derivative.eval c = 0 ∧
      ‖p.eval z - p.eval c‖ / ‖z - c‖ ≤ (p.natDegree - 1)/ p.natDegree * ‖p.derivative.eval z‖
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/MeanValueProblem.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeanValueProblem.lean#L92).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/MeanValueProblem.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/MeanValueProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Mean_value_problem)
