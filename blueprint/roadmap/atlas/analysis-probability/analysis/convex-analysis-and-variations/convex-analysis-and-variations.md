---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.ConvexOnIffAboveTangentWanted.convexOn_iff_forall_le_add_fderivWithin, MathlibExt.Analysis.Convex.KarushKuhnTucker.karush_kuhn_tucker_inequality
statement: formalized
---

# Convex analysis and calculus of variations: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/index.html).

Convex functions and sets in analysis and optimization: Fenchel conjugates, polar sets, Moreau decomposition, convex projections, KKT conditions, gradient descent rates, Stampacchia, Tikhonov regularization, Euler–Lagrange, mountain pass and Ekeland principles; linear programming goes to convex geometry.

## Convexity via the tangent-plane inequality

Let $E$ be a real Banach space, let
$X \subseteq E$ be an open convex set, and let $f \colon E \to \mathbb{R}$ be twice continuously
differentiable on $X$. Then $f$ is convex on $X$ if and only if
$f(x) \ge f(a) + Df(a)(x - a)$ for all $a, x \in X$, where $Df(a)$ is the Fréchet derivative of
$f$ at $a$ within $X$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Functional analysis; Measures, integration, derivative, holomorphy), problem `ma_proofbench_l1_95`.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ConvexOnIffAboveTangentWanted.convexOn_iff_forall_le_add_fderivWithin` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ConvexOnIffAboveTangentWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ConvexOnIffAboveTangentWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/index.html#convex-on-iff-forall-le-add-fderiv-withi).

## Karush–Kuhn–Tucker conditions for inequality constraints

Let $E$ be a finite-dimensional
real normed space, let $f \colon E \to \mathbb{R}$ and $g_1, \dots, g_m \colon E \to \mathbb{R}$,
and let $x \in E$ be a point at which $f$ and every $g_i$ are differentiable; write $D$ for
the Fréchet derivative at $x$. Suppose that $x$ is feasible, that is $g_i(x) \le 0$ for every
$i$; that $x$ is a local minimizer of $f$ on the feasible set
$\{y \in E : g_i(y) \le 0 \text{ for every } i\}$; and that the derivatives $Dg_i(x)$ of the
active constraints, those $i$ with $g_i(x) = 0$, are linearly independent. Then there exist
multipliers $\lambda_1, \dots, \lambda_m \ge 0$ such that $\lambda_i g_i(x) = 0$ for every $i$
and $Df(x) + \sum_{i=1}^m \lambda_i Dg_i(x) = 0$.

## Sources

- W. Karush, Minima of Functions of Several Variables with Inequalities as Side Conditions (M.Sc. thesis, Univ. Chicago, 1939); H. W. Kuhn and A. W. Tucker, Nonlinear Programming, Proc. Second Berkeley Symposium (1951), 481–492, DOI 10.1525/9780520411586-036.

Formalized by `MathlibExt.Analysis.Convex.KarushKuhnTucker.karush_kuhn_tucker_inequality`, a theorem declared in [MathlibExt/Analysis/Convex/KarushKuhnTucker.lean, line 232](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/KarushKuhnTucker.lean#L232). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/index.html#karush-kuhn-tucker-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Convex analysis and calculus of variations](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations)
