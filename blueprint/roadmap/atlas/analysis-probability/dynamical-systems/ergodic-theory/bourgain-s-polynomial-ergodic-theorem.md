---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.BourgainErgodicWanted.Dynamics.BourgainErgodic.IsIntegerPolynomialSequence, MathlibExt.Dynamics.BourgainErgodicWanted.Dynamics.BourgainErgodic.polynomialErgodicAverage, MathlibExt.Dynamics.BourgainErgodicWanted.Dynamics.BourgainErgodic.bourgain_polynomial_ergodic
statement: formalized
---

# Bourgain's polynomial ergodic theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bourgain-s-polynomial-ergodic-theorem/index.html).

## Integer polynomial sequences

A sequence $a : \mathbb{N} \to \mathbb{N}$ is an integer
polynomial sequence if there is a polynomial $P$ with integer coefficients such that
$P(n) \ge 0$ and $a(n) = P(n)$ for every $n \in \mathbb{N}$.

Formalized by `MathlibExt.Dynamics.BourgainErgodicWanted.Dynamics.BourgainErgodic.IsIntegerPolynomialSequence`, a definition declared in [WantedExt/Dynamics/BourgainErgodicWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/BourgainErgodicWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bourgain-s-polynomial-ergodic-theorem/index.html#is-integer-polynomial-sequence).

## Polynomial ergodic averages

Given a sequence $a : \mathbb{N} \to \mathbb{N}$, a map
$T : X \to X$, a function $f : X \to \mathbb{R}$, $n \in \mathbb{N}$ and $x \in X$, the $n$-th
polynomial ergodic average of $f$ at $x$ is

$$\frac{1}{n} \sum_{k=0}^{n-1} f\bigl(T^{a(k)}(x)\bigr),$$

where $T^{a(k)}$ is the $a(k)$-fold iterate of $T$; for $n = 0$ the average is $0$.

Formalized by `MathlibExt.Dynamics.BourgainErgodicWanted.Dynamics.BourgainErgodic.polynomialErgodicAverage`, a definition declared in [WantedExt/Dynamics/BourgainErgodicWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/BourgainErgodicWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bourgain-s-polynomial-ergodic-theorem/index.html#polynomial-ergodic-average).

## Bourgain's polynomial ergodic theorem

Let $(X, \mu)$ be a probability space, let
$T : X \to X$ be a measure-preserving map, let $a : \mathbb{N} \to \mathbb{N}$ be an integer
polynomial sequence, and let $f : X \to \mathbb{R}$ be a function in $L^p(\mu)$ for some
$p$ with $1 < p < \infty$. Then there is a function $F : X \to \mathbb{R}$ such that for
$\mu$-almost every $x \in X$ the polynomial ergodic averages
$\frac{1}{n} \sum_{k=0}^{n-1} f(T^{a(k)}(x))$, $n \ge 1$, where $T^{a(k)}$ is the $a(k)$-fold
iterate of $T$, converge to $F(x)$ as $n \to \infty$.

## Sources

- J. Bourgain, *Pointwise ergodic theorems for arithmetic sets*, Publ. Math. IHÉS 69 (1989). Knill, *Some fundamental theorems in mathematics*, §173. Problem `bourgain_polynomial_ergodic` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.BourgainErgodicWanted.Dynamics.BourgainErgodic.bourgain_polynomial_ergodic` is written with `theorem_wanted` in [WantedExt/Dynamics/BourgainErgodicWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/BourgainErgodicWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bourgain-s-polynomial-ergodic-theorem/index.html#bourgain-polynomial-ergodic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bourgain's polynomial ergodic theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/bourgain-s-polynomial-ergodic-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/ergodic-theory/bourgain-s-polynomial-ergodic-theorem)
