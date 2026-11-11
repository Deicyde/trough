---
declaration: section
origin: cited
lean: MetaMathlibExt.moebius_fixedPoint_eq_iff, MetaMathlibExt.moebius_dual_endpoint_ne_neg_one, MetaMathlibExt.moebius_dual_central_equations, MetaMathlibExt.moebius_naturalDual_singular
statement: formalized
---

# Natural duals of Möbius maps

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/natural-duals-of-m-bius-maps/index.html).

## Fixed points of a Moebius dual branch

Let $\beta, \gamma, \eta$ be real numbers with
$\beta \ne 2$ and $3 - 2\beta + (2 - \beta)\eta \ne 0$. Then
$(-2 + 2\beta + \gamma + (-1 + \beta + \gamma)\eta)/(3 - 2\beta + (2 - \beta)\eta) = \eta$
if and only if $\eta = -1$ or $\eta = (-2 + 2\beta + \gamma)/(2 - \beta)$.

The paper's further side conditions on $\beta$ and $\gamma$ are not used.

## Sources

- Fritz Schweiger, *A Remark on Singular Duals of Moebius Maps*, INTEGERS 24 (2024), Article A17, Lemma 1.

Stated but not proved: `MetaMathlibExt.moebius_fixedPoint_eq_iff` is written with `theorem_wanted` in [WantedExt/Dynamics/MoebiusSingularDualWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoebiusSingularDualWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/natural-duals-of-m-bius-maps/index.html#moebius-fixed-point-eq-iff).

## Moebius dual branches disagree at −1

Let $\alpha, \beta, \delta$ be real numbers with
$\alpha > 0$, $\beta < 1$ and $\delta \ge 0$, and define the dual branches
$V^\#_{\alpha\delta}(y) = (2\alpha\delta - 1 + \alpha\delta y)/(2\alpha + 1 + \alpha y)$ and
$V^\#_{\beta\delta}(y) = (2\delta - 2\beta\delta - 1 + (\delta - \beta\delta - 1) y)/
(3 - 2\beta + (2 - \beta) y)$. Then $V^\#_{\beta\delta}(-1) \ne V^\#_{\alpha\delta}(-1)$.

Equality would force $\delta = -1$.

## Sources

- Fritz Schweiger, *A Remark on Singular Duals of Moebius Maps*, INTEGERS 24 (2024), Article A17, Lemma 2.

Stated but not proved: `MetaMathlibExt.moebius_dual_endpoint_ne_neg_one` is written with `theorem_wanted` in [WantedExt/Dynamics/MoebiusSingularDualWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoebiusSingularDualWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/natural-duals-of-m-bius-maps/index.html#moebius-dual-endpoint-ne-neg-one).

## Central equations for natural duals of Moebius maps

Let $\alpha, \beta, \gamma, \delta$
and $\xi$ be real numbers with $\alpha > 0$, $\beta < 1$, $\gamma > -1$ and $\delta \ge 0$. Define
the dual branches
$V^\#_{\alpha\gamma}(y) = (\gamma - 2\alpha - \alpha y)/(2\alpha + 1 + \alpha y)$,
$V^\#_{\alpha\delta}(y) = (2\alpha\delta - 1 + \alpha\delta y)/(2\alpha + 1 + \alpha y)$,
$V^\#_{\beta\gamma}(y) = (2\beta + \gamma - 2 + (\beta + \gamma - 1) y)/
(3 - 2\beta + (2 - \beta) y)$ and
$V^\#_{\beta\delta}(y) = (2\delta - 2\beta\delta - 1 + (\delta - \beta\delta - 1) y)/
(3 - 2\beta + (2 - \beta) y)$, and put $\eta = (-2 + 2\beta + \gamma)/(2 - \beta)$. Suppose that
$3 - 2\beta + (2 - \beta)\xi \ne 0$, $2\alpha + 1 + \alpha\xi \ne 0$,
$V^\#_{\beta\gamma}(\xi) = V^\#_{\beta\delta}(\xi)$ and
$V^\#_{\alpha\delta}(\xi) = V^\#_{\alpha\gamma}(\xi)$. Then
$\alpha + \alpha\delta + \delta = \beta + \gamma + \beta\delta$; and if moreover
$2\alpha + 1 + \alpha\eta \ne 0$ and $\xi = V^\#_{\alpha\gamma}(\eta)$, then
$\alpha^2\gamma + \alpha^2\gamma\delta + 2\alpha + \beta + \beta\gamma + 2\alpha^2 +
2\alpha^2\delta + 4\alpha\delta + 2\alpha\gamma\delta = 2 + \alpha\gamma^2 + 2\gamma +
2\alpha\beta + \alpha\gamma + \alpha\beta\gamma + \alpha\beta\gamma\delta + 2\alpha\beta\delta$.

## Sources

- Fritz Schweiger, *A Remark on Singular Duals of Moebius Maps*, INTEGERS 24 (2024), Article A17, Lemma 3.

Stated but not proved: `MetaMathlibExt.moebius_dual_central_equations` is written with `theorem_wanted` in [WantedExt/Dynamics/MoebiusSingularDualWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoebiusSingularDualWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/natural-duals-of-m-bius-maps/index.html#moebius-dual-central-equations).

## Singularity of natural duals of Moebius maps (algebraic form)

Let
$\alpha, \beta, \gamma, \delta$ be real numbers with $\alpha > 0$, $\beta < 1$, $\gamma > -1$ and
$\delta \ge 0$. Define the dual branches
$V^\#_{\alpha\gamma}(y) = (\gamma - 2\alpha - \alpha y)/(2\alpha + 1 + \alpha y)$,
$V^\#_{\alpha\delta}(y) = (2\alpha\delta - 1 + \alpha\delta y)/(2\alpha + 1 + \alpha y)$,
$V^\#_{\beta\gamma}(y) = (2\beta + \gamma - 2 + (\beta + \gamma - 1) y)/
(3 - 2\beta + (2 - \beta) y)$ and
$V^\#_{\beta\delta}(y) = (2\delta - 2\beta\delta - 1 + (\delta - \beta\delta - 1) y)/
(3 - 2\beta + (2 - \beta) y)$, and put $\eta = (-2 + 2\beta + \gamma)/(2 - \beta)$ and
$\xi = V^\#_{\alpha\gamma}(\eta)$. If $2\alpha + 1 + \alpha\eta \ne 0$,
$3 - 2\beta + (2 - \beta)\xi \ne 0$, $2\alpha + 1 + \alpha\xi \ne 0$,
$V^\#_{\beta\gamma}(\xi) = V^\#_{\beta\delta}(\xi)$ and
$V^\#_{\alpha\delta}(\xi) = V^\#_{\alpha\gamma}(\xi)$, then $\xi = \eta$.

Here $\eta$ is a fixed point of $V^\#_{\beta\gamma}$, and $\xi = \eta$ says that the natural dual
$[\eta, \xi]$ reduces to a single point.

## Sources

- Fritz Schweiger, *A Remark on Singular Duals of Moebius Maps*, INTEGERS 24 (2024), Article A17, Theorem 1.

Stated but not proved: `MetaMathlibExt.moebius_naturalDual_singular` is written with `theorem_wanted` in [WantedExt/Dynamics/MoebiusSingularDualWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/MoebiusSingularDualWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/natural-duals-of-m-bius-maps/index.html#moebius-natural-dual-singular).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Natural duals of Möbius maps](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/low-dimensional-dynamics/natural-duals-of-m-bius-maps/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/low-dimensional-dynamics/natural-duals-of-m-bius-maps)
