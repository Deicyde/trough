---
declaration: section
origin: cited
lean: MathlibExt.Analysis.ScottishBook184Wanted.IsSubharmonic, MathlibExt.Analysis.ScottishBook184Wanted.HasSecondPartialDerivatives, MathlibExt.Analysis.ScottishBook184Wanted.saks184_subharmonic_laplacian_nonneg
statement: formalized
---

# Subharmonic functions

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/subharmonic-functions/index.html).

## Subharmonic functions on the plane

A function
$\varphi : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ is subharmonic if it is upper semicontinuous
and, for every point $(a, b)$ of the plane and every radius $r > 0$,

$$
\varphi(a, b) \le \frac{1}{2\pi} \int_0^{2\pi} \varphi(a + r\cos\theta, b + r\sin\theta)\, d\theta.
$$

The integral is taken to be $0$ when the integrand is not integrable over $[0, 2\pi]$, so for
such a circle the condition only says $\varphi(a, b) \le 0$.

Formalized by `MathlibExt.Analysis.ScottishBook184Wanted.IsSubharmonic`, a definition declared in [WantedExt/Analysis/ScottishBook184Wanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook184Wanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/subharmonic-functions/index.html#is-subharmonic).

## Existence of the pure second partial derivatives

A function
$\varphi : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ has second partial derivatives if at every
point of the plane the partial derivatives $\varphi_x$ and $\varphi_y$ exist, and the partial
derivatives $\varphi_{xx} = (\varphi_x)_x$ and $\varphi_{yy} = (\varphi_y)_y$ also exist.

Formalized by `MathlibExt.Analysis.ScottishBook184Wanted.HasSecondPartialDerivatives`, a definition declared in [WantedExt/Analysis/ScottishBook184Wanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook184Wanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/subharmonic-functions/index.html#has-second-partial-derivatives).

## Subharmonic functions with second partial derivatives have nonnegative Laplacian

Let
$\varphi : \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ be subharmonic, and suppose that its
partial derivatives $\varphi_x$, $\varphi_{xx}$, $\varphi_y$ and $\varphi_{yy}$ exist at every
point of the plane. Then $\varphi_{xx}(p) + \varphi_{yy}(p) \ge 0$ for every point $p$ of the
plane.

The point is that this is not immediate outside the (dense) set where the second derivatives
are continuous.

## Sources

- S. Saks, Problem 184 of the Scottish Book; solved by A. Eremenko, "A problem of Stanislaw Saks", Mat. Stud. 52 (2019), 173-175 (arXiv:1911.09530). See the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Analysis.ScottishBook184Wanted.saks184_subharmonic_laplacian_nonneg` is written with `theorem_wanted` in [WantedExt/Analysis/ScottishBook184Wanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/ScottishBook184Wanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/subharmonic-functions/index.html#saks184-subharmonic-laplacian-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subharmonic functions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/potential-theory/subharmonic-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/potential-theory/subharmonic-functions)
