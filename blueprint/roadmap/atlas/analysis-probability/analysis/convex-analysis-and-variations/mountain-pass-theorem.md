---
declaration: section
origin: cited
lean: MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.IsCriticalPoint, MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.PalaisSmale, MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.MountainRange, MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.mountainPassLevel, MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.mountain_pass
statement: formalized
---

# Mountain pass theorem

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem/index.html).

## Critical point

Let $E$ be a real Banach space and $f : E \to \mathbb{R}$. A point
$x \in E$ is a critical point of $f$ when the Fréchet derivative of $f$ at $x$ vanishes,
$f'(x) = 0$. Here $f'(x)$ is taken to be $0$ when $f$ is not differentiable at $x$, so such
points are critical as well.

Formalized by `MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.IsCriticalPoint`, a definition declared in [WantedExt/Analysis/MountainPassWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/MountainPassWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem/index.html#is-critical-point).

## Palais–Smale condition

Let $E$ be a real Banach space. A function $f : E \to \mathbb{R}$
satisfies the Palais–Smale condition when every sequence $(u_k)$ in $E$ such that $(f(u_k))$ is
bounded and the Fréchet derivatives $f'(u_k)$ tend to $0$ in operator norm has a subsequence
converging in $E$. Here $f'(x)$ is taken to be $0$ at points where $f$ is not differentiable.

Formalized by `MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.PalaisSmale`, a definition declared in [WantedExt/Analysis/MountainPassWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/MountainPassWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem/index.html#palais-smale).

## Mountain range

Let $E$ be a real Banach space, $f : E \to \mathbb{R}$, $a, b \in E$ and
$\varepsilon, r \in \mathbb{R}$. The points $a$ and $b$ are separated by a mountain range of $f$
at height $\varepsilon$ and radius $r$ when $f(a) = 0$, $\varepsilon > 0$, $r > 0$,
$f(y) \ge \varepsilon$ for every $y \in E$ with $\|y - a\| = r$, $\|b - a\| > r$ and
$f(b) \le 0$.

Formalized by `MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.MountainRange`, a definition declared in [WantedExt/Analysis/MountainPassWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/MountainPassWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem/index.html#mountain-range).

## Mountain pass level

Let $E$ be a real Banach space, $f : E \to \mathbb{R}$ and
$a, b \in E$. The mountain pass level of $f$ between $a$ and $b$ is

$$
c = \inf_{\gamma} \sup_{t \in [0, 1]} f(\gamma(t)),
$$

the infimum taken over all continuous paths $\gamma : [0, 1] \to E$ with $\gamma(0) = a$ and
$\gamma(1) = b$. Suprema and infima are taken in $\mathbb{R}$, where a family that is unbounded
on the relevant side has supremum or infimum $0$ by convention.

Formalized by `MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.mountainPassLevel`, a definition declared in [WantedExt/Analysis/MountainPassWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/MountainPassWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem/index.html#mountain-pass-level).

## Mountain pass theorem

Let $E$ be a real Banach space and let $f : E \to \mathbb{R}$ be
continuously differentiable and satisfy the Palais–Smale condition. Let $a, b \in E$ and let
$\varepsilon, r$ be real numbers such that $a$ and $b$ are separated by a mountain range of $f$
at height $\varepsilon$ and radius $r$: $f(a) = 0$, $\varepsilon > 0$, $r > 0$,
$f(y) \ge \varepsilon$ for every $y$ with $\|y - a\| = r$, $\|b - a\| > r$ and $f(b) \le 0$.
Then the mountain pass level $c$ of $f$ between $a$ and $b$ satisfies $c \ge \varepsilon$, and
$f$ has a critical point $x$ with $f(x) = c$.

## Sources

- A. Ambrosetti and P.H. Rabinowitz, 'Dual variational methods in critical point theory and applications', J. Funct. Anal. 14 (1973) 349–381. Listed as §119 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `mountain_pass` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.MountainPassWanted.Analysis.MountainPassProblem.mountain_pass` is written with `theorem_wanted` in [WantedExt/Analysis/MountainPassWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/MountainPassWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem/index.html#mountain-pass).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mountain pass theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations/mountain-pass-theorem)
