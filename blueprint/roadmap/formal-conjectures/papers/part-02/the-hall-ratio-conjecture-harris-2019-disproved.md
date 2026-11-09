---
declaration: theorem
origin: cited
lean: HallRatioConjecture.hall_ratio_conjecture, HallRatioConjecture.hall_ratio_conjecture.variants.hallRatio_le_fractionalChromaticNumber, HallRatioConjecture.hall_ratio_conjecture.variants.unbounded
statement: formalized
---

# The Hall ratio conjecture (Harris 2019) — disproved

> *References:*
> * [Ha19] Harris, D. G. (2019). "Some results on chromatic number as a function of triangle
>   count." *SIAM J. Discrete Math.* 33, pp. 546--563.
> * [DOW20] Dvořák, Z., Ossona de Mendez, P. and Wu, H. (2020). "1-subdivisions, the fractional
>   chromatic number and the Hall ratio." *Combinatorica* 40, pp. 759--774.
>   [arXiv:1812.07327](https://arxiv.org/abs/1812.07327)
> * [BLMNPV22] Blumenthal, A., Lidický, B., Martin, R. R., Norin, S., Pfender, F. and Volec, J.
>   (2022). "Counterexamples to a conjecture of Harris on Hall ratio." *SIAM J. Discrete Math.*
>   36, pp. 1678--1686. [arXiv:1811.11116](https://arxiv.org/abs/1811.11116)
> * [SU97] Scheinerman, E. R. and Ullman, D. H. (1997). *Fractional Graph Theory.* Wiley.

*Quoted from [FormalConjectures/Paper/HallRatioConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HallRatioConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved.

## `HallRatioConjecture.hall_ratio_conjecture`

Solved: stated here without proof.

> **The Hall ratio conjecture (Harris 2019) — disproved.**
>
> Harris conjectured that the fractional chromatic number is bounded by a constant multiple of the
> Hall ratio: there is a constant $C$ with $\chi_f(G) \le C\,\rho(G)$ for every graph $G$. This
> is **false**: Dvořák, Ossona de Mendez and Wu [DOW20] and, independently, Blumenthal, Lidický,
> Martin, Norin, Pfender and Volec [BLMNPV22] constructed graphs with $\chi_f / \rho$
> arbitrarily large.

```lean
theorem hall_ratio_conjecture : ¬
    ∃ C : ℝ, ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V),
      G.fractionalChromaticNumber ≤ C * hallRatio G
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/HallRatioConjecture.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HallRatioConjecture.lean#L60).

## `HallRatioConjecture.hall_ratio_conjecture.variants.hallRatio_le_fractionalChromaticNumber`

Solved: stated here without proof.

> **The Hall ratio is a lower bound for the fractional chromatic number.**
>
> For every graph, $\rho(G) \le \chi_f(G)$ (see [SU97]); the conjecture asked for an inequality in
> the other direction up to a constant.

```lean
theorem hall_ratio_conjecture.variants.hallRatio_le_fractionalChromaticNumber
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) :
    hallRatio G ≤ G.fractionalChromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/HallRatioConjecture.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HallRatioConjecture.lean#L72).

## `HallRatioConjecture.hall_ratio_conjecture.variants.unbounded`

Solved: stated here without proof.

> **Unbounded ratio (Dvořák–Ossona de Mendez–Wu 2020; Blumenthal et al. 2022).**
>
> For every $C$ there is a graph with $\chi_f(G) > C\,\rho(G)$.
>
> *References:* [DOW20], [BLMNPV22].

```lean
theorem hall_ratio_conjecture.variants.unbounded (C : ℝ) :
    ∃ (V : Type) (_ : Fintype V) (_ : DecidableEq V) (G : SimpleGraph V),
      C * hallRatio G < G.fractionalChromaticNumber
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/HallRatioConjecture.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HallRatioConjecture.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/HallRatioConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HallRatioConjecture.lean)
- [arXiv:1812.07327](https://arxiv.org/abs/1812.07327)
