---
declaration: theorem
origin: cited
lean: VoronovskajaTypeFormula.voronovskaja_theorem.bernstein_operators, VoronovskajaTypeFormula.voronovskaja_theorem.bezier_bernstein_operators
statement: formalized
---

# Voronovskaja-type Formula for the Bezier Variant of the Bernstein Operators

> The Bézier-type Bernstein operators $B_{n,\alpha}$ for $\alpha > 0$ are defined for
> $f : [0,1] \to \mathbb{R}$ by
>
> $$
> (B_{n,\alpha} f)(x)
>   = \sum_{k=0}^n f\!\left(\frac{k}{n}\right)
>     \left( J_{n,k}(x)^{\alpha} - J_{n,k+1}(x)^{\alpha} \right),
> $$
>
> where
>
> $$
> J_{n,k}(x) = \sum_{j=k}^n p_{n,j}(x),
> \qquad
> p_{n,j}(x) = \binom{n}{j} x^j(1-x)^{n-j},
> $$
>
> and $J_{n,n+1}(x) = 0$.
>
> In the classical case $\alpha = 1$, these operators reduce to the usual Bernstein operators.
> For $f$ which are $C^2$ on $[0,1]$, one has the classical Voronovskaja
> asymptotic formula
>
> $$
> \lim_{n \to \infty} n\bigl( B_{n,1} f(x) - f(x) \bigr)
>     = \tfrac{1}{2} x(1-x) f''(x).
> $$
>
> ## Known Results
> * For $\alpha = 1$, the asymptotics are completely understood.
> * Numerical experiments indicate that for $\alpha \neq 1$ the quantity
>
> $$
>         \sqrt{n}\,\bigl( B_{n,\alpha} f(x) - f(x) \bigr)
>     $$
>
> may converge to a non-zero limit.
>
> ## The Problem
> Determine the asymptotic behaviour of the Bézier-type Bernstein operators for $\alpha > 0$,
> $\alpha \neq 1$:
> \textbf{Existence of the limit:}
>     Prove (or disprove) the existence of the limit
>
> $$
>         \lim_{n \to \infty}
>         \sqrt{n}\,\bigl( B_{n,\alpha} f(x) - f(x) \bigr),
>     $$
>
> at least for sufficiently smooth functions $f$.
>     \textbf{Explicit form of the limit:}
>     If the limit exists, determine an explicit expression for it in terms of $f$, $x$, and $\alpha$.
>
> ## Provenance
>
> The limit formula recorded here, together with the elementary identities and the endpoint
> reduction in this file, was first proposed by *Samuel Schlesinger*. The first complete proof
> is the Lean 4 formalisation by *Kenta Kitamura*
> ([KitaKen1 on GitHub](https://github.com/KitaKen1)) in [K26], which is linked from
> `voronovskaja_theorem.bezier_bernstein_operators`.
>
> *References:*
>
> * [Voronovskaja-type Formula for the Bézier Variant of the Bernstein Operators](https://www.math.bas.bg/mathmod/Proceedings_CTF/CTF-2010/files_CTF-2010/Open_problems.pdf),
>   by *Ulrich Abel*, in *Constructive Theory of Functions, Sozopol 2010*.
> * [K26] [A Formal Conjectures Bézier--Bernstein Theorem in
>   Lean](https://github.com/KitaKen1/bezier-bernstein-voronovskaja-lean), by *Kenta Kitamura*.

*Quoted from [FormalConjectures/Paper/VoronovskajaTypeFormula.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/VoronovskajaTypeFormula.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 21 API statements, counted here but not shown.

## `VoronovskajaTypeFormula.voronovskaja_theorem.bernstein_operators`

Solved: stated here without proof.

> Classical Voronovskaja theorem (α = 1).
>
> For functions $f$ that are $C^2$ on $[0,1]$, the limit:
>
> $$
> n\bigl( B_n f(x) - f(x) \bigr)
> \;\longrightarrow\;
> \frac{1}{2}\, x(1 - x)\, f''(x)
> $$

```lean
theorem voronovskaja_theorem.bernstein_operators
    (f : ℝ → ℝ) (x : ℝ) (hx : x ∈ I)
    (hf : ContDiffOn ℝ 2 f I) :
    let f'' : ℝ := iteratedDerivWithin 2 f I x
    Tendsto (fun (n : ℕ) => (n : ℝ) * (bezierBernstein n 1 f x - f x))
    atTop
    (𝓝 ((1 / 2) * x * (1 - x) * f''))
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [40 Sequences, series, summability](../../by-subject/part-02/40-sequences-series-summability/README.md), [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Paper/VoronovskajaTypeFormula.lean, line 448](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/VoronovskajaTypeFormula.lean#L448).

## `VoronovskajaTypeFormula.voronovskaja_theorem.bezier_bernstein_operators`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/bezier-bernstein-voronovskaja-lean/blob/3f35c631d215b3841242275bf3ed2c59ea153a2d/Voronovskaja.lean](https://github.com/KitaKen1/bezier-bernstein-voronovskaja-lean/blob/3f35c631d215b3841242275bf3ed2c59ea153a2d/Voronovskaja.lean).

> Voronovskaja-type formula for Bézier--Bernstein operators with shape parameter
> $\alpha > 0$, $\alpha \neq 1$.
>
> The source asks for sufficiently smooth functions. This concrete version uses
> `ContDiffOn ℝ 2 f I` as a readable baseline regularity assumption; since the
> domain is the compact interval $[0,1]$, this also explains why no separate
> boundedness assumption is included here.
>
> The limit exists and equals $\mu(\alpha)\,\sqrt{x(1-x)}\,f'(x)$, where
> $\mu(\alpha) = \int_0^\infty \bigl( (1 - \Phi(t))^{\alpha}
> - (1 - \Phi(t)^{\alpha}) \bigr)\,dt$ and $\Phi$ is the standard normal
> distribution function.
>
> Informal proof: the weights
> $w_{n,k} = J_{n,k}(x)^{\alpha} - J_{n,k+1}(x)^{\alpha}$ are nonnegative and sum
> to $1$, so the quadratic Taylor bound for $f \in C^2$ gives
>
> $$
> B_{n,\alpha} f(x) - f(x)
>   = \sum_{k=0}^{n} \bigl( f(k/n) - f(x) \bigr) w_{n,k}
>   = f'(x) \sum_{k=0}^{n} (k/n - x)\, w_{n,k}
>     + O\Bigl( \sum_{k=0}^{n} (k/n - x)^2 w_{n,k} \Bigr).
> $$
>
> The two sums on the right satisfy
>
> $$
> \sqrt{n} \sum_{k=0}^{n} (k/n - x)\, w_{n,k}
>   \longrightarrow \mu(\alpha)\,\sqrt{x(1-x)},
> \qquad
> \sqrt{n} \sum_{k=0}^{n} (k/n - x)^2 w_{n,k} \longrightarrow 0,
> $$
>
> so multiplying by $\sqrt{n}$ gives the stated limit.
>
> The linked formal proof is a self-contained Lean 4 formalisation by *Kenta Kitamura*
> ([KitaKen1 on GitHub](https://github.com/KitaKen1)); see [K26].

```lean
theorem voronovskaja_theorem.bezier_bernstein_operators
    (α : ℝ) (hα_pos : 0 < α) (hα : α ≠ 1)
    (f : ℝ → ℝ) (x : ℝ) (hx : x ∈ I)
    (hf : ContDiffOn ℝ 2 f I) :
    Tendsto (fun n : ℕ => Real.sqrt n * (bezierBernstein n α f x - f x)) atTop
      (𝓝 ((voronovskaja_theorem.bezier_bernstein_operators.answer :
        ℝ → (ℝ → ℝ) → ℝ → ℝ) α f x))
```

Category `research solved`; AMS [26 Real functions](../../by-subject/part-01/26-real-functions/README.md), [40 Sequences, series, summability](../../by-subject/part-02/40-sequences-series-summability/README.md), [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Paper/VoronovskajaTypeFormula.lean, line 498](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/VoronovskajaTypeFormula.lean#L498).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/VoronovskajaTypeFormula.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/VoronovskajaTypeFormula.lean)
- [Voronovskaja-type Formula for the Bézier Variant of the Bernstein Operators](https://www.math.bas.bg/mathmod/Proceedings_CTF/CTF-2010/files_CTF-2010/Open_problems.pdf)
