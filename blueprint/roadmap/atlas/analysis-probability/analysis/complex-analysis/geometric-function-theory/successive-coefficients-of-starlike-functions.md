---
declaration: section
origin: cited
lean: MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.IsInClassS, MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.IsStarlike, MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.conjecture, MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.conjecture_holds
statement: formalized
---

# Successive coefficients of starlike functions

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/successive-coefficients-of-starlike-functions/index.html).

## Normalized univalent functions (the class $S$)

A function $f : \mathbb{C} \to \mathbb{C}$
is in the class $S$ when it is analytic on the open unit disc $\mathbb{D} = \{z : |z| < 1\}$,
satisfies $f(0) = 0$ and $f'(0) = 1$, and is injective on $\mathbb{D}$.

## Sources

- Hayman and Lingham, Research Problems in Function Theory (2018), Problem 6.46, https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.IsInClassS`, a definition declared in [WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/successive-coefficients-of-starlike-functions/index.html#is-in-class-s).

## Starlike functions on the unit disc

A function $f : \mathbb{C} \to \mathbb{C}$ is
starlike when it is analytic on the open unit disc $\mathbb{D} = \{z : |z| < 1\}$ and, for every
$z \ne 0$ in $\mathbb{D}$, $f(z) \ne 0$ and $\operatorname{Re}\bigl(z f'(z) / f(z)\bigr) > 0$.

## Sources

- Hayman, Research Problems in Function Theory (2018), Problem 6.46, https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.IsStarlike`, a definition declared in [WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/successive-coefficients-of-starlike-functions/index.html#is-starlike).

## Hayman's successive coefficient problem for starlike functions

The statement that for
every function $f : \mathbb{C} \to \mathbb{C}$ in the class $S$ (analytic on the open unit disc
$\mathbb{D} = \{z : |z| < 1\}$, with $f(0) = 0$ and $f'(0) = 1$, and injective on $\mathbb{D}$)
that is moreover starlike ($\operatorname{Re}\bigl(z f'(z) / f(z)\bigr) > 0$ for every $z \ne 0$
in $\mathbb{D}$), the Taylor coefficients $a_n = f^{(n)}(0) / n!$ of $f$ at $0$ satisfy
$\bigl| |a_{n+1}| - |a_n| \bigr| \le 1$ for every natural number $n \ge 1$.

## Sources

- Hayman and Lingham, Research Problems in Function Theory (2018), Problem 6.46, https://arxiv.org/abs/1809.07200.

Formalized by `MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.conjecture`, a definition declared in [WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/successive-coefficients-of-starlike-functions/index.html#conjecture).

## Leung's theorem on successive coefficients of starlike functions

Let
$f : \mathbb{C} \to \mathbb{C}$ be analytic on the open unit disc $\mathbb{D} = \{z : |z| < 1\}$,
with $f(0) = 0$ and $f'(0) = 1$, injective on $\mathbb{D}$, and starlike, meaning that
$\operatorname{Re}\bigl(z f'(z) / f(z)\bigr) > 0$ for every $z \ne 0$ in $\mathbb{D}$. Let
$a_n = f^{(n)}(0) / n!$ be the Taylor coefficients of $f$ at $0$. Then
$\bigl| |a_{n+1}| - |a_n| \bigr| \le 1$ for every natural number $n \ge 1$.

This answers Problem 6.46 of Hayman and Lingham, Research Problems in Function Theory (2018),
affirmatively. It was proved by Y. Leung (Bull. London Math. Soc. 10 (1978), 193-196) and
independently by D. H. Hamilton.

## Sources

- Moduli difference of initial inverse logarithmic coefficients for starlike and convex functions (2026), arXiv:2603.17600, https://arxiv.org/abs/2603.17600.

Stated but not proved: `MathlibExt.Analysis.StarlikeCoefficientSuccessiveDifferenceWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/StarlikeCoefficientSuccessiveDifferenceWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/successive-coefficients-of-starlike-functions/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Successive coefficients of starlike functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/successive-coefficients-of-starlike-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/successive-coefficients-of-starlike-functions)
