---
declaration: theorem
origin: cited
lean: RiemannZetaMoments.moment_isEquiv, RiemannZetaMoments.moment_isEquiv₁, RiemannZetaMoments.moment_isEquiv₂, RiemannZetaMoments.moment_isEquiv₃, RiemannZetaMoments.moment_isEquiv₄, RiemannZetaMoments.moment_isEquivₖ
statement: formalized
---

# Moments of the Riemann zeta function on the critical line

> The moments $\frac{1}{T}\int_0^T |\zeta(1/2 + it)|^{2k}\,dt$ are conjectured to be asymptotic
> to $c_k (\log T)^{k^2}$ for some constants $c_k$. This is a theorem for $k = 1$
> (Hardy–Littlewood, $c_1 = 1$) and $k = 2$ (Ingham, $c_2 = 1/(2\pi^2)$), and these are the only
> proven cases. Conrey–Ghosh and Conrey–Gonek conjectured $c_3 = 42 a_3 / 9!$ and
> $c_4 = 24024 a_4 / 16!$, with $a_k$ the arithmetic factor
> $a_k = \prod_p (1 - 1/p)^{k^2} \sum_{m \ge 0} \binom{m+k-1}{m}^2 p^{-m}$;
> Keating–Snaith conjectured $c_k = a_k f_k$ with $f_k = \prod_{j=0}^{k-1} j!/(j+k)!$ from random
> matrix theory, recovering $g_k = (k^2)!\,f_k = 1, 2, 42, 24024$.
>
> The statements and constants below are taken from §3.4.5 of [Co26].
>
> *References:*
> - [Co26] A. Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*,
>   [arXiv:2602.04022](https://arxiv.org/abs/2602.04022), §3.4.5.
> - [In26] A. E. Ingham, *Mean-value theorems in the theory of the Riemann zeta-function*,
>   Proc. London Math. Soc. 27 (1926), 273–300.
> - [CG98] J. B. Conrey, A. Ghosh, *A conjecture for the sixth power moment of the Riemann
>   zeta-function*, Internat. Math. Res. Notices 1998, no. 15, 775–780.
> - [CGo01] J. B. Conrey, S. Gonek, *High moments of the Riemann zeta-function*, Duke Math. J.
>   107 (2001), no. 3, 577–604.
> - [KS00] J. P. Keating, N. C. Snaith, *Random matrix theory and $\zeta(1/2+it)$*, Commun. Math.
>   Phys. 214 (2000), no. 1, 57–89.

*Quoted from [FormalConjectures/Paper/RiemannZetaMoments.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 4 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `RiemannZetaMoments.moment_isEquiv`

Open: stated without proof.

> The asymptotic behaviour of the $k$th moment of the Riemann zeta function
> is conjectured to be
> $$
>   \frac{1}{T}\int_0^T |\zeta(1/2 + it)|^{2k}dt \sim c_k \log(T)^{k^2},
> $$
> for some constant $c_k$.

```lean
theorem moment_isEquiv (k : ℕ) : ∃ c > (0 : ℝ),
    moment k ~[atTop] fun T ↦ c * T.log ^ (k ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaMoments.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean#L70).

## `RiemannZetaMoments.moment_isEquiv₁`

Solved: stated here without proof.

> The asymptotic behaviour of the first moment of the Riemann zeta function was proved by
> Hardy and Littlewood, where $c_1 = 1$ [Co26, §3.4.5].

```lean
theorem moment_isEquiv₁ : moment 1 ~[atTop] fun T ↦ T.log
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaMoments.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean#L77).

## `RiemannZetaMoments.moment_isEquiv₂`

Solved: stated here without proof.

> The asymptotic behaviour of the second moment of the Riemann zeta function was proved by
> Ingham [In26], where $c_2 = 1/(2\pi^2)$.

```lean
theorem moment_isEquiv₂ : moment 2 ~[atTop] fun T ↦ (1 / (2 * π ^ 2)) * T.log ^ 4
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaMoments.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean#L83).

## `RiemannZetaMoments.moment_isEquiv₃`

Open: stated without proof.

> The constant in the asymptotic formula for the 3rd zeta moment is conjectured
> to be $42a_3/9!$ [CG98].

```lean
theorem moment_isEquiv₃ : moment 3 ~[atTop] fun T ↦ 42 * arithmeticFactor 3 / 9 ! * T.log ^ 9
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaMoments.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean#L109).

## `RiemannZetaMoments.moment_isEquiv₄`

Open: stated without proof.

> The constant in the asymptotic formula for the 4th zeta moment is conjectured to
> be $24024a_4/16!$ [CGo01].

```lean
theorem moment_isEquiv₄ :
    moment 4 ~[atTop] fun T ↦ 24024 * arithmeticFactor 4 / 16 ! * T.log ^ 16
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaMoments.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean#L115).

## `RiemannZetaMoments.moment_isEquivₖ`

Open: stated without proof.

> The Keating–Snaith conjecture [KS00] for the $k$th moment of the Riemann zeta function,
> provides the value of $c_k$ in the asymptotic formula [Co26, §3.4.5].

```lean
theorem moment_isEquivₖ (k : ℕ) : moment k ~[atTop]
    fun T ↦ (arithmeticFactor k * ∏ j ∈ Finset.range k, (j ! : ℝ) / (j + k) !) *
      T.log ^ (k ^ 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/RiemannZetaMoments.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean#L122).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/RiemannZetaMoments.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/RiemannZetaMoments.lean)
- [arXiv:2602.04022](https://arxiv.org/abs/2602.04022)
