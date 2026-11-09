---
declaration: theorem
origin: cited
lean: SatoTateConjecture.satoTate_conjecture
statement: formalized
---

# Sato–Tate conjecture

> The **Sato–Tate conjecture** describes the distribution of the normalized Frobenius traces
> $a_p(E)/(2\sqrt{p})$ of a non-CM elliptic curve $E$ over $\mathbb{Q}$, as $p$ ranges over
> the primes of good reduction: they equidistribute in $[-1,1]$ with respect to the
> **Sato–Tate measure**
> $$
> \frac{2}{\pi}\sqrt{1-x^2}\,dx.
> $$
>
> Originally conjectured independently by Mikio Sato and John Tate around 1960, it is
> now a theorem: the case of elliptic curves over totally real fields with nonintegral
> $j$-invariant was established through the work of Clozel, Harris, and Taylor [CHT08],
> Taylor [Tay08], and Harris, Shepherd-Barron, and Taylor [HST10]. The remaining non-CM
> case was settled by Barnet-Lamb, Geraghty, Harris, and Taylor [BGHT11]. In particular,
> it holds unconditionally for every non-CM elliptic curve over $\mathbb{Q}$.
>
> We use `ModularityConjecture.WeierstrassCurve.ap`, which agrees with the Frobenius
> trace at every prime where the supplied Weierstrass equation has integral
> coefficients and nonsingular reduction. Only finitely many primes are exceptional.
> Including these primes does not change the limiting density, so the formal
> statement averages over all primes below $N$.
>
> The non-CM hypothesis is expressed using the classification of rational CM
> $j$-invariants. Complex multiplication here means complex multiplication over
> $\overline{\mathbb{Q}}$.
>
> ## References
>
> - [CHT08] L. Clozel, M. Harris, R. Taylor, *Automorphy for some $l$-adic lifts of
>   automorphic mod $l$ Galois representations*, Publications Mathématiques de l'IHÉS
>   108 (2008), 1–181. https://doi.org/10.1007/s10240-008-0016-1
> - [Tay08] R. Taylor, *Automorphy for some $l$-adic lifts of automorphic mod $l$
>   Galois representations. II*, Publications Mathématiques de l'IHÉS
>   108 (2008), 183–239. https://doi.org/10.1007/s10240-008-0015-2
> - [HST10] M. Harris, N. Shepherd-Barron, R. Taylor, *A family of Calabi-Yau varieties
>   and potential automorphy*, Annals of Mathematics 171 (2010), no. 2, 779–813.
>   https://doi.org/10.4007/annals.2010.171.779
> - [BGHT11] T. Barnet-Lamb, D. Geraghty, M. Harris, R. Taylor, *A family of Calabi-Yau
>   varieties and potential automorphy II*, Publications of the Research Institute
>   for Mathematical Sciences 47 (2011), no. 1, 29–98.
>   https://doi.org/10.2977/PRIMS/31
> - [Wikipedia](https://en.wikipedia.org/wiki/Sato%E2%80%93Tate_conjecture)

*Quoted from [FormalConjectures/Wikipedia/SatoTateConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SatoTateConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `SatoTateConjecture.satoTate_conjecture`

Solved: stated here without proof.

> **The Sato–Tate conjecture**: for a non-CM elliptic curve $E$ over $\mathbb{Q}$ and
> $-1 \le a \le b \le 1$, the proportion of primes $p < N$ whose normalized coefficient
> belongs to $[a,b]$ tends to
> $$
> \frac{2}{\pi}\int_a^b \sqrt{1-x^2}\,dx
> $$
> as $N \to \infty$.
>
> The finitely many primes where the supplied equation fails to have integral
> coefficients and nonsingular reduction do not affect this limit.
>
> Established through the work of Clozel–Harris–Taylor [CHT08], Taylor [Tay08],
> Harris–Shepherd-Barron–Taylor [HST10], and
> Barnet-Lamb–Geraghty–Harris–Taylor [BGHT11].

```lean
theorem satoTate_conjecture
    (E : WeierstrassCurve ℚ) [E.IsElliptic] (hCM : ¬ HasCM E)
    (a b : ℝ) (ha : -1 ≤ a) (hab : a ≤ b) (hb : b ≤ 1) :
    Filter.Tendsto
      (fun N : ℕ ↦
        (primeCountInInterval E a b N : ℝ) /
          ((Nat.primesBelow N).card : ℝ))
      Filter.atTop
      (nhds (satoTateMeasure a b))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/SatoTateConjecture.lean, line 169](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SatoTateConjecture.lean#L169).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SatoTateConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SatoTateConjecture.lean)
