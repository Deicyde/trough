---
declaration: section
origin: cited
lean: MathlibExt.Probability.LegendreTransform.legendreTransform, MathlibExt.Probability.LegendreTransform.legendreTransform_eq_iSup, MathlibExt.Probability.LegendreTransform.le_legendreTransform, MathlibExt.Probability.LegendreTransform.legendreTransform_antitone, MathlibExt.Probability.LegendreTransform.convex_epi_legendreTransform, MathlibExt.Probability.LegendreTransform.convexOn_legendreTransform, MathlibExt.Probability.LegendreTransform.legendreTransform_legendreTransform_le, MathlibExt.Probability.LegendreTransform.legendreTransform_norm_sq_div_two
statement: formalized
proof: formalized
---

# Legendre transform

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html).

## Legendre transform

Let $d \in \mathbb{N}$, give $\mathbb{R}^d$ its standard inner product,
and let $\Lambda : \mathbb{R}^d \to [-\infty, \infty]$. The Legendre transform of $\Lambda$ at
$x \in \mathbb{R}^d$ is the Fenchel conjugate of $\Lambda$ at the linear functional
$y \mapsto \langle x, y \rangle$, that is, the extended real number
$\Lambda^*(x) = \sup_{y \in \mathbb{R}^d} \big(\langle x, y \rangle - \Lambda(y)\big)$.

Formalized by `MathlibExt.Probability.LegendreTransform.legendreTransform`, a definition declared in [MathlibExt/Probability/LegendreTransform.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#legendre-transform).

## Supremum formula for the Legendre transform

Let $d \in \mathbb{N}$ and let
$\Lambda : \mathbb{R}^d \to [-\infty, \infty]$. For every $x \in \mathbb{R}^d$, the Legendre
transform $\Lambda^*$ of $\Lambda$ satisfies
$\Lambda^*(x) = \sup_{l \in \mathbb{R}^d} \big(\langle l, x \rangle - \Lambda(l)\big)$.

Formalized by `MathlibExt.Probability.LegendreTransform.legendreTransform_eq_iSup`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#legendre-transform-eq-i-sup).

## Fenchel–Young inequality for the Legendre transform

Let $d \in \mathbb{N}$ and let
$\Lambda : \mathbb{R}^d \to [-\infty, \infty]$, with Legendre transform $\Lambda^*$. For all
$x, l \in \mathbb{R}^d$, we have $\langle l, x \rangle - \Lambda(l) \le \Lambda^*(x)$ in
$[-\infty, \infty]$.

Formalized by `MathlibExt.Probability.LegendreTransform.le_legendreTransform`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#le-legendre-transform).

## The Legendre transform is order-reversing

Let $d \in \mathbb{N}$ and let
$\Lambda_1, \Lambda_2 : \mathbb{R}^d \to [-\infty, \infty]$, with Legendre transforms
$\Lambda_1^*$ and $\Lambda_2^*$. If $\Lambda_1(y) \le \Lambda_2(y)$ for every
$y \in \mathbb{R}^d$, then $\Lambda_2^*(x) \le \Lambda_1^*(x)$ for every $x \in \mathbb{R}^d$.

Formalized by `MathlibExt.Probability.LegendreTransform.legendreTransform_antitone`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#legendre-transform-antitone).

## The epigraph of the Legendre transform is convex

Let $d \in \mathbb{N}$ and let
$\Lambda : \mathbb{R}^d \to [-\infty, \infty]$, with Legendre transform $\Lambda^*$. Then the
set $\{(x, t) \in \mathbb{R}^d \times \mathbb{R} : \Lambda^*(x) \le t\}$ is convex.

Formalized by `MathlibExt.Probability.LegendreTransform.convex_epi_legendreTransform`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#convex-epi-legendre-transform).

## A finite Legendre transform is convex

Let $d \in \mathbb{N}$ and let
$\Lambda : \mathbb{R}^d \to [-\infty, \infty]$, with Legendre transform $\Lambda^*$. If
$\Lambda^*(x)$ is a real number for every $x \in \mathbb{R}^d$, then $\Lambda^*$, viewed as a
function $\mathbb{R}^d \to \mathbb{R}$, is convex on $\mathbb{R}^d$.

Formalized by `MathlibExt.Probability.LegendreTransform.convexOn_legendreTransform`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#convex-on-legendre-transform).

## The double Legendre transform lies below the function

Let $d \in \mathbb{N}$ and let
$\Lambda : \mathbb{R}^d \to [-\infty, \infty]$ be a function that never takes the value
$-\infty$, with Legendre transform $\Lambda^*$. Then the Legendre transform $\Lambda^{**}$ of
$\Lambda^*$ satisfies $\Lambda^{**}(x) \le \Lambda(x)$ for every $x \in \mathbb{R}^d$.

The proof bounds $\Lambda^{**}$ by the Fenchel biconjugate of $\Lambda$.

Formalized by `MathlibExt.Probability.LegendreTransform.legendreTransform_legendreTransform_le`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#legendre-transform-legendre-transform-le).

## The half squared norm is its own Legendre transform

Let $d \in \mathbb{N}$ and let
$q : \mathbb{R}^d \to [-\infty, \infty]$ be $q(y) = \|y\|^2 / 2$, where $\|\cdot\|$ is the
Euclidean norm. Its Legendre transform $q^*$ satisfies $q^*(x) = \|x\|^2 / 2$ for every
$x \in \mathbb{R}^d$; in particular every value of $q^*$ is finite.

Formalized by `MathlibExt.Probability.LegendreTransform.legendreTransform_norm_sq_div_two`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#legendre-transform-norm-sq-div-two).

## Legendre transform of the zero function at the origin

Let $d \in \mathbb{N}$ and let
$\Lambda : \mathbb{R}^d \to [-\infty, \infty]$ be the zero function. Its Legendre transform
$\Lambda^*$ satisfies $\Lambda^*(0) = 0$.

Formalized by `MathlibExt.Probability.LegendreTransform.legendreTransform_zero`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#legendre-transform-zero).

## Legendre transform of the zero function away from the origin

Let $d \in \mathbb{N}$
and let $\Lambda : \mathbb{R}^d \to [-\infty, \infty]$ be the zero function. Its Legendre
transform $\Lambda^*$ satisfies $\Lambda^*(x) = +\infty$ for every nonzero $x \in \mathbb{R}^d$.

Formalized by `MathlibExt.Probability.LegendreTransform.legendreTransform_zero_of_ne`, a theorem declared in [MathlibExt/Probability/LegendreTransform.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/LegendreTransform.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html#legendre-transform-zero-of-ne).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Legendre transform](https://deicyde.github.io/atlas-lean/roadmap/Probability/large-deviations/legendre-transform/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/large-deviations/legendre-transform)
