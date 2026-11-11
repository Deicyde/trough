---
declaration: section
origin: cited
lean: MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.rootMult, MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.poleMult, MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.rootMultSph, MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.IsBoundedValueDistribution, MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.conjecture, MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.conjecture_refuted
statement: formalized
---

# Turán's three-value problem

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html).

## Multiplicity of a root of $f = w$

Let $f : \mathbb{C} \to \mathbb{C}$ and
$w, z \in \mathbb{C}$. The multiplicity of $z$ as a root of the equation $f = w$ is an extended
natural number: it is $\infty$ if $f(t) = w$ for every $t \neq z$ in some neighbourhood of $z$;
otherwise it is $n$ if $f - w$ has meromorphic order $n \ge 0$ at $z$, and it is $0$ if that
order is negative or $f - w$ is not meromorphic at $z$.

It depends only on the values of $f$ on a punctured neighbourhood of $z$, so changing $f(z)$
does not change it. It is $0$ when $f$ has a pole at $z$, and when $f - w$ is analytic at $z$
with $f(z) \neq w$.

## Sources

- Hayman - Research Problems in Function Theory (2018), Problem 2.28 [AMR-022-2028], <https://arxiv.org/abs/1809.07200>.

Formalized by `MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.rootMult`, a definition declared in [WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html#root-mult).

## Multiplicity of a pole

Let $f : \mathbb{C} \to \mathbb{C}$ and $z \in \mathbb{C}$. The
multiplicity of $z$ as a pole of $f$, that is, the multiplicity of the value $\infty$ at $z$, is
$-n$ if $f$ has finite meromorphic order $n < 0$ at $z$, and $0$ otherwise. In particular it is
$0$ unless $f$ has a pole at $z$.

## Sources

- Hayman - Research Problems in Function Theory (2018), Problem 2.28 [AMR-022-2028], <https://arxiv.org/abs/1809.07200>.

Formalized by `MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.poleMult`, a definition declared in [WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html#pole-mult).

## Multiplicity of a value on the Riemann sphere

Let $f : \mathbb{C} \to \mathbb{C}$ and
$z \in \mathbb{C}$, and let $w$ be a point of the Riemann sphere $\mathbb{C} \cup \{\infty\}$.
The multiplicity of $w$ as a value of $f$ at $z$ is the multiplicity of $z$ as a root of
$f = w$ when $w$ is finite, and the multiplicity of $z$ as a pole of $f$ when $w = \infty$.

## Sources

- Hayman - Research Problems in Function Theory (2018), Problem 2.28 [AMR-022-2028], <https://arxiv.org/abs/1809.07200>.

Formalized by `MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.rootMultSph`, a definition declared in [WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html#root-mult-sph).

## Bounded value distribution

A function $f : \mathbb{C} \to \mathbb{C}$ has bounded value
distribution if for every real $r > 0$ there is a natural number $C$ such that, for every value
$w$ of the Riemann sphere $\mathbb{C} \cup \{\infty\}$ and every open disc of radius $r$, the
multiplicities of $w$ as a value of $f$ at the points of any finite subset of the disc add up
to at most $C$.

The source states this for functions meromorphic in the plane; the definition itself does not
assume meromorphy.

## Sources

- Hayman - Research Problems in Function Theory (2018), Problem 2.28 [AMR-022-2028], <https://arxiv.org/abs/1809.07200>.

Formalized by `MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.IsBoundedValueDistribution`, a definition declared in [WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html#is-bounded-value-distribution).

## Turán's three-value question

The statement that every function
$f : \mathbb{C} \to \mathbb{C}$ with the following properties has bounded value distribution:
$f$ is meromorphic on $\mathbb{C}$; for every $w \in \mathbb{C}$ there is a point at which
$f - w$ has finite meromorphic order; and there are three distinct values $w_1, w_2, w_3$ of
the Riemann sphere $\mathbb{C} \cup \{\infty\}$ such that for every real $r > 0$ there is a
natural number $C$ for which, for each $i$ and every open disc of radius $r$, the
multiplicities of $w_i$ as a value of $f$ at the points of any finite subset of the disc add
up to at most $C$.

## Sources

- Hayman - Research Problems in Function Theory (2018), Problem 2.28 [AMR-022-2028], <https://arxiv.org/abs/1809.07200>, question by P. Turán.

Formalized by `MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.conjecture`, a definition declared in [WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html#conjecture).

## Turán's three-value question has a negative answer

There is a function
$f : \mathbb{C} \to \mathbb{C}$, meromorphic on $\mathbb{C}$, such that for every $w \in \mathbb{C}$
there is a point at which $f - w$ has finite meromorphic order, together with three distinct
values $w_1, w_2, w_3$ of the Riemann sphere $\mathbb{C} \cup \{\infty\}$ such that for every real
$r > 0$ there is a natural number $C$ for which, for each $i$ and every open disc of radius $r$,
the multiplicities of $w_i$ as a value of $f$ at the points of any finite subset of the disc add
up to at most $C$; and yet $f$ does not have bounded value distribution.

A. A. Gol'dberg (Izv. Vyssh. Uchebn. Zaved. Mat. 1972) answered Turan's question negatively, as
recorded in Hayman-Lingham Update 2.28; the Weierstrass sigma-function is another
counterexample: it has boundedly many $w$-points per disc for every bounded set of $w$ but has
order $2$, so it does not have bounded value distribution.

## Sources

- W. K. Hayman and E. F. Lingham, Research Problems in Function Theory (2018), arXiv:1809.07200, https://arxiv.org/abs/1809.07200.

Stated but not proved: `MathlibExt.Analysis.TuranThreeValueBoundedDistributionWanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/TuranThreeValueBoundedDistributionWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Turán's three-value problem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/entire-functions/tur-n-s-three-value-problem)
