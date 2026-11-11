---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook157Wanted.HasZeroDensityAtRight, MathlibExt.Analysis.ScottishBook157Wanted.ApproxContinuousAt, MathlibExt.Analysis.ScottishBook157Wanted.HasPositiveUpperRightApproxDeriv, MathlibExt.Analysis.ScottishBook157Wanted.wardApproximatelyContinuousPositiveDerivMonotone
statement: formalized
---

# Approximate derivatives and monotonicity

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/approximate-derivatives-and-monotonicity/index.html).

## Right density zero at the origin

A set $S \subseteq \mathbb{R}$ has right-hand density
$0$ at $0$ if the Lebesgue outer measure of $S \cap (0, \delta]$, divided by $\delta$, tends to
$0$ as $\delta \to 0^+$.

Formalized by `MathlibExt.Analysis.ScottishBook157Wanted.HasZeroDensityAtRight`, a definition declared in [WantedExt/Analysis/ScottishBook157Wanted.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook157Wanted.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/approximate-derivatives-and-monotonicity/index.html#has-zero-density-at-right).

## Approximate continuity

A function $f \colon \mathbb{R} \to \mathbb{R}$ is approximately
continuous at $x$ if, for every $\varepsilon > 0$, the set
$S_\varepsilon = \{y : |f(y) - f(x)| < \varepsilon\}$ has density $1$ at $x$: the Lebesgue outer
measure of $S_\varepsilon \cap (x - \delta, x + \delta)$, divided by $2\delta$, tends to $1$ as
$\delta \to 0^+$.

Formalized by `MathlibExt.Analysis.ScottishBook157Wanted.ApproxContinuousAt`, a definition declared in [WantedExt/Analysis/ScottishBook157Wanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook157Wanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/approximate-derivatives-and-monotonicity/index.html#approx-continuous-at).

## Positive upper right approximate derivative

The upper right-hand approximate derivative
of $f \colon \mathbb{R} \to \mathbb{R}$ at $x$ is positive: there are $a > 0$ and $\varepsilon > 0$
such that for every $\delta > 0$ there is $\delta' \in (0, \delta]$ for which the Lebesgue outer
measure of $\{h \in (0, \delta'] : (f(x + h) - f(x))/h > a\}$ is at least $\varepsilon \delta'$.

Equivalently, the approximate upper limit of the difference quotient $(f(x + h) - f(x))/h$ as
$h \to 0^+$, which neglects sets of $h$ of right density $0$ at $0$, is positive.

Formalized by `MathlibExt.Analysis.ScottishBook157Wanted.HasPositiveUpperRightApproxDeriv`, a definition declared in [WantedExt/Analysis/ScottishBook157Wanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook157Wanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/approximate-derivatives-and-monotonicity/index.html#has-positive-upper-right-approx-deriv).

## Approximate derivative test for monotonicity (Scottish Book Problem 157)

Let
$f \colon \mathbb{R} \to \mathbb{R}$ be approximately continuous at every point, and suppose that
at every point $x$ the upper right-hand approximate derivative of $f$ is positive. Then $f$ is
monotone nondecreasing.

## Sources

- A. J. (Gus) Ward, Problem 157 of the Scottish Book; solved affirmatively by D. Ornstein, "A characterization of monotone functions", Illinois J. Math. 15 (1971), 73-76, and by R. O'Malley (1975), whose theorem on approximate maxima yields an immediate positive solution; see K. Beanland, P. Humke, T. Richards, "On Scottish Book Problem 157", Real Anal. Exchange 41(2) (2016), 331-346.

Stated but not proved: `MathlibExt.Analysis.ScottishBook157Wanted.wardApproximatelyContinuousPositiveDerivMonotone` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook157Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/ScottishBook157Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/approximate-derivatives-and-monotonicity/index.html#ward-approximately-continuous-positive-d).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Approximate derivatives and monotonicity](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/approximate-derivatives-and-monotonicity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/approximate-derivatives-and-monotonicity)
