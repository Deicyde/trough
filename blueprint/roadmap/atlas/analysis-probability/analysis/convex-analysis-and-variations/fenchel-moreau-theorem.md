---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Convex.FenchelMoreau.fenchelConj, MathlibExt.Analysis.Convex.FenchelMoreau.fenchelBiconj, MathlibExt.Analysis.Convex.FenchelMoreau.isClosed_epi_real, MathlibExt.Analysis.Convex.FenchelMoreau.biconj_le, MathlibExt.Analysis.Convex.FenchelMoreau.fenchel_moreau
statement: formalized
proof: formalized
---

# Fenchel–Moreau theorem

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem/index.html).

## Fenchel conjugate

Let $E$ be a real vector space with a topology and let
$f : E \to [-\infty, \infty]$. The Fenchel conjugate of $f$ at a continuous linear functional
$L : E \to \mathbb{R}$ is the extended real number $f^*(L) = \sup_{y \in E} \big(L(y) - f(y)\big)$.

Formalized by `MathlibExt.Analysis.Convex.FenchelMoreau.fenchelConj`, a definition declared in [MathlibExt/Analysis/Convex/FenchelMoreau.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/FenchelMoreau.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem/index.html#fenchel-conj).

## Fenchel biconjugate

Let $E$ be a real vector space with a topology and let
$f : E \to [-\infty, \infty]$. The biconjugate of $f$ at $x \in E$ is the extended real number
$f^{**}(x) = \sup_L \big(L(x) - f^*(L)\big)$, where $L$ ranges over the continuous linear
functionals $E \to \mathbb{R}$ and $f^*$ is the Fenchel conjugate of $f$.

Formalized by `MathlibExt.Analysis.Convex.FenchelMoreau.fenchelBiconj`, a definition declared in [MathlibExt/Analysis/Convex/FenchelMoreau.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/FenchelMoreau.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem/index.html#fenchel-biconj).

## Lower semicontinuous functions have closed epigraphs

Let $E$ be a topological space and
let $f : E \to [-\infty, \infty]$ be lower semicontinuous. Then the set
$\{(x, r) \in E \times \mathbb{R} : f(x) \le r\}$ is closed in $E \times \mathbb{R}$.

Formalized by `MathlibExt.Analysis.Convex.FenchelMoreau.isClosed_epi_real`, a theorem declared in [MathlibExt/Analysis/Convex/FenchelMoreau.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/FenchelMoreau.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem/index.html#is-closed-epi-real).

## The biconjugate lies below the function

Let $E$ be a real vector space with a topology
and let $f : E \to [-\infty, \infty]$ never take the value $-\infty$. Then $f^{**}(x) \le f(x)$
for every $x \in E$, where $f^{**}$ is the Fenchel biconjugate of $f$.

This is the easy direction of the Fenchel–Moreau theorem.

Formalized by `MathlibExt.Analysis.Convex.FenchelMoreau.biconj_le`, a theorem declared in [MathlibExt/Analysis/Convex/FenchelMoreau.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/FenchelMoreau.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem/index.html#biconj-le).

## Fenchel–Moreau theorem

Let $E$ be a locally convex real topological vector space, not
necessarily Hausdorff. Let $f : E \to [-\infty, \infty]$ be lower semicontinuous, never equal to
$-\infty$, not identically $+\infty$, and convex in the sense that the set
$\{(x, r) \in E \times \mathbb{R} : f(x) \le r\}$ is convex. Then for every $x \in E$,
$f(x) = \sup_L \big(L(x) - \sup_{y \in E} (L(y) - f(y))\big)$, where $L$ ranges over the
continuous linear functionals $E \to \mathbb{R}$; that is, $f$ equals its Fenchel biconjugate.

## Sources

- Werner Fenchel, *Convex Cones, Sets, and Functions: From Notes by D. W. Blackett of Lectures at Princeton University, 1951*, Princeton University Department of Mathematics, 1953, Open Library OL1430688W; and Jean-Jacques Moreau, "Fonctions convexes duales et points proximaux," C. R. Acad. Sci. Paris 255 (1962), 2897–2899, zbMATH 0118.10502.

Formalized by `MathlibExt.Analysis.Convex.FenchelMoreau.fenchel_moreau`, a theorem declared in [MathlibExt/Analysis/Convex/FenchelMoreau.lean, line 633](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Convex/FenchelMoreau.lean#L633). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem/index.html#fenchel-moreau).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fenchel–Moreau theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/convex-analysis-and-variations/fenchel-moreau-theorem)
