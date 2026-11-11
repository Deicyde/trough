---
declaration: section
origin: cited
lean: MathlibExt.Analysis.HaymanRobertson39Wanted.haymanUnitDisc, MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsSchlicht, MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsStarlike, MathlibExt.Analysis.HaymanRobertson39Wanted.haymanHasRealCoeffs, MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsCloseToConvex, MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsOddSqrt, MathlibExt.Analysis.HaymanRobertson39Wanted.haymanOddSqrtCoeff, MathlibExt.Analysis.HaymanRobertson39Wanted.haymanRobertsonBound
statement: formalized
---

# Robertson's conjecture on odd univalent functions

10 results, 9 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html).

## Open unit disc

The open unit disc $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ in the
complex plane.

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanUnitDisc`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-unit-disc).

## Normalized univalent functions (class $S$)

A function $f : \mathbb{C} \to \mathbb{C}$
belongs to the class $S$ when it is analytic at every point of the open unit disc
$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$, injective on $\mathbb{D}$, and satisfies $f(0) = 0$
and $f'(0) = 1$.

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsSchlicht`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-is-schlicht).

## Starlike univalent functions

A function $f : \mathbb{C} \to \mathbb{C}$ is starlike when it
belongs to the class $S$ (analytic at every point of the open unit disc
$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$, injective on $\mathbb{D}$, $f(0) = 0$ and
$f'(0) = 1$) and $\operatorname{Re}\bigl(z f'(z) / f(z)\bigr) > 0$ for every $z \in \mathbb{D}$
with $z \ne 0$.

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsStarlike`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-is-starlike).

## Real Taylor coefficients at the origin

A function $f : \mathbb{C} \to \mathbb{C}$ has real
Taylor coefficients at $0$ when, for every natural number $n$, the value $f^{(n)}(0)$ of its $n$-th
iterated derivative at $0$ is real (equivalently, every Taylor coefficient $f^{(n)}(0)/n!$ is real).

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanHasRealCoeffs`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-has-real-coeffs).

## Close-to-convex functions

A function $f : \mathbb{C} \to \mathbb{C}$ is close-to-convex
when it belongs to the class $S$ (analytic at every point of the open unit disc
$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$, injective on $\mathbb{D}$, $f(0) = 0$ and
$f'(0) = 1$) and there are a starlike function $g$ and a real number $\alpha$ such that
$\operatorname{Re}\bigl(e^{i\alpha} z f'(z) / g(z)\bigr) > 0$ for every $z \in \mathbb{D}$ with
$z \ne 0$. Here $g$ is starlike when it belongs to $S$ and
$\operatorname{Re}\bigl(z g'(z) / g(z)\bigr) > 0$ for every $z \in \mathbb{D}$ with $z \ne 0$.

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsCloseToConvex`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-is-close-to-convex).

## Normalized odd square roots

Given $f : \mathbb{C} \to \mathbb{C}$, a function
$h : \mathbb{C} \to \mathbb{C}$ is a normalized odd square root $h(z) = f(z^2)^{1/2}$ when, on the
open unit disc $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$, $h$ is analytic at every point and
satisfies $h(z)^2 = f(z^2)$ and $h(-z) = -h(z)$ for all $z \in \mathbb{D}$, and moreover $h(0) = 0$
and $h'(0) = 1$.

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanIsOddSqrt`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-is-odd-sqrt).

## Taylor coefficients at the origin

For a function $h : \mathbb{C} \to \mathbb{C}$ and a
natural number $n$, $c_n(h) = h^{(n)}(0) / n!$, where $h^{(n)}$ is the $n$-th iterated derivative
of $h$. For $h$ analytic near $0$ this is the $n$-th Taylor coefficient of $h$ at $0$; Robertson's
problem uses it at odd $n$.

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanOddSqrtCoeff`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-odd-sqrt-coeff).

## Robertson's bound

For a function $h : \mathbb{C} \to \mathbb{C}$ with Taylor coefficients
$c_k = h^{(k)}(0)/k!$ at $0$ and a natural number $n$, the Robertson bound for $h$ at $n$ is the
inequality $|c_1|^2 + |c_3|^2 + \dots + |c_{2n-1}|^2 \le n$ (for $n = 0$ the sum is empty).

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.haymanRobertsonBound`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#hayman-robertson-bound).

## Robertson's conjecture for real-coefficient and close-to-convex functions

Let
$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$. The statement that for all functions
$f, h : \mathbb{C} \to \mathbb{C}$ such that $f$ belongs to the class $S$ (analytic at every point
of $\mathbb{D}$, injective on $\mathbb{D}$, $f(0) = 0$ and $f'(0) = 1$), $h$ is a normalized odd
square root of $f(z^2)$ (analytic at every point of $\mathbb{D}$, with $h(z)^2 = f(z^2)$ and
$h(-z) = -h(z)$ for all $z \in \mathbb{D}$, $h(0) = 0$ and $h'(0) = 1$), and $f$ has real Taylor
coefficients at $0$ or is close-to-convex, the Taylor coefficients $c_k = h^{(k)}(0)/k!$ of $h$ at
$0$ satisfy $|c_1|^2 + |c_3|^2 + \dots + |c_{2n-1}|^2 \le n$ for every integer $n \ge 1$.

Resolved true: de Branges (1985) proved the bound for every function in $S$ via the Milin
conjecture.

## Sources

- AMR-022-6039, Hayman Problem 6.39, arXiv:1809.07200.

Formalized by `MathlibExt.Analysis.HaymanRobertson39Wanted.conjecture`, a definition declared in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#conjecture).

## Robertson's conjecture holds for real-coefficient and close-to-convex functions

Let
$\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$. For all functions $f, h : \mathbb{C} \to \mathbb{C}$
such that $f$ belongs to the class $S$ (analytic at every point of $\mathbb{D}$, injective on
$\mathbb{D}$, $f(0) = 0$ and $f'(0) = 1$), $h$ is a normalized odd square root of $f(z^2)$ (analytic
at every point of $\mathbb{D}$, with $h(z)^2 = f(z^2)$ and $h(-z) = -h(z)$ for all
$z \in \mathbb{D}$, $h(0) = 0$ and $h'(0) = 1$), and $f$ has real Taylor coefficients at $0$ or is
close-to-convex, the Taylor coefficients $c_k = h^{(k)}(0)/k!$ of $h$ at $0$ satisfy
$|c_1|^2 + |c_3|^2 + \dots + |c_{2n-1}|^2 \le n$ for every integer $n \ge 1$.

De Branges' 1985 proof of the Milin conjecture implies the Robertson bound for every normalized
univalent function, hence for the real-coefficient and close-to-convex subclasses formalized here.

## Sources

- de Branges, L., A proof of the Bieberbach conjecture, Acta Math. 154 (1985), 137-152, https://doi.org/10.1007/BF02392821.

Stated but not proved: `MathlibExt.Analysis.HaymanRobertson39Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/HaymanRobertson39Wanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/HaymanRobertson39Wanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Robertson's conjecture on odd univalent functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/robertson-s-conjecture-on-odd-univalent-function)
