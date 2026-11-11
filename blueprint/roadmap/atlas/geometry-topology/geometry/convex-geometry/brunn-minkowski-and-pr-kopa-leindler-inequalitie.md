---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.Integral.PrekopaLeindlerWanted.prekopa_leindler, MathlibExt.MeasureTheory.Geometry.BrunnMinkowskiWanted.brunn_minkowski
statement: formalized
proof: formalized
---

# Brunn–Minkowski and Prékopa–Leindler inequalities

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/brunn-minkowski-and-pr-kopa-leindler-inequalitie/index.html).

## Prékopa–Leindler inequality

Let $n \ge 0$ and $0 < t < 1$, and let
$f, g, h : \mathbb{R}^n \to [0, \infty]$ be Borel measurable functions on Euclidean space
$\mathbb{R}^n$ such that $f(x)^{1-t} g(y)^t \le h((1-t)x + ty)$ for all $x, y \in \mathbb{R}^n$.
Then, with all integrals taken over $\mathbb{R}^n$ against Lebesgue measure,

$$\Big(\int f(x)\,dx\Big)^{1-t} \Big(\int g(x)\,dx\Big)^{t} \le \int h(x)\,dx.$$

## Sources

- A. Prékopa, Acta Sci. Math. 32 (1971), 301–316; H. J. Brascamp and E. Lieb, J. Funct. Anal. 22 (1976), 366–389, DOI 10.1016/0022-1236(76)90004-5.

Formalized by `MathlibExt.MeasureTheory.Integral.PrekopaLeindlerWanted.prekopa_leindler`, a theorem declared in [MathlibExt/MeasureTheory/Integral/PrekopaLeindler.lean, line 1521](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Integral/PrekopaLeindler.lean#L1521). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/brunn-minkowski-and-pr-kopa-leindler-inequalitie/index.html#prekopa-leindler).

## Brunn–Minkowski inequality

Let $n \ge 1$, let $A$ and $B$ be nonempty compact subsets of
$\mathbb{R}^n$, let $A + B = \{a + b : a \in A,\ b \in B\}$ be their Minkowski sum, and let
$\mathrm{vol}$ denote Lebesgue measure on $\mathbb{R}^n$. Then

$$\mathrm{vol}(A + B)^{1/n} \ge \mathrm{vol}(A)^{1/n} + \mathrm{vol}(B)^{1/n}.$$

## Sources

- H. Brunn, Über Ovale und Eiflächen (1887); H. Minkowski, Geometrie der Zahlen (1896); modern formulation R. J. Gardner, Bull. AMS 39 (2002), 355–406, DOI 10.1090/S0273-0979-02-00941-2.

Formalized by `MathlibExt.MeasureTheory.Geometry.BrunnMinkowskiWanted.brunn_minkowski`, a theorem declared in [MathlibExt/MeasureTheory/Geometry/BrunnMinkowski.lean, line 336](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/MeasureTheory/Geometry/BrunnMinkowski.lean#L336). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/brunn-minkowski-and-pr-kopa-leindler-inequalitie/index.html#brunn-minkowski).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brunn–Minkowski and Prékopa–Leindler inequalities](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/brunn-minkowski-and-pr-kopa-leindler-inequalitie/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/convex-geometry/brunn-minkowski-and-pr-kopa-leindler-inequalitie)
