---
declaration: section
origin: cited
lean: EuclideanGeometry.IsLocalDefiningFunction, EuclideanGeometry.IsLocalDefiningFunction.mem, EuclideanGeometry.levelSetSecondFundamentalForm, EuclideanGeometry.levelSetMeanCurvature, EuclideanGeometry.levelSetSecondFundamentalForm_smul, EuclideanGeometry.levelSetMeanCurvature_smul, EuclideanGeometry.levelSetMeanCurvature_smul_of_pos, EuclideanGeometry.levelSetMeanCurvature_neg
statement: formalized
proof: formalized
---

# Curvature of hypersurfaces

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html).

## Local defining function

Let $E$ be a real inner product space, $S \subseteq E$,
$\rho : E \to \mathbb{R}$ and $p \in E$. Then $\rho$ is a local defining function of $S$ at $p$
when $\rho(p) = 0$, $\rho$ is of class $C^2$ at $p$, its differential $D\rho(p)$ is nonzero, and
for all $x$ in some neighborhood of $p$, $x \in S$ if and only if $\rho(x) = 0$. In particular
$p \in S$.

Every point of a $C^2$ hypersurface has local defining functions, and every point of a regular
level set of a $C^2$ function is of this form.

Formalized by `EuclideanGeometry.IsLocalDefiningFunction`, a definition declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#is-local-defining-function).

## A point with a local defining function lies in the set

Let $E$ be a real inner product
space, $S \subseteq E$, $\rho : E \to \mathbb{R}$ and $p \in E$. If $\rho$ is a local defining
function of $S$ at $p$, then $p \in S$.

Formalized by `EuclideanGeometry.IsLocalDefiningFunction.mem`, a theorem declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#mem).

## Second fundamental form of a level set

Let $E$ be a finite-dimensional real inner
product space, $\rho : E \to \mathbb{R}$ and $p \in E$. Write $\nabla\rho(p)$ for the gradient of
$\rho$ at $p$ and $D^2\rho(p)$ for the second derivative of $\rho$ at $p$ (a bilinear form on
$E$). The second fundamental form at $p$ of the level set of $\rho$ through $p$, with respect to
the unit normal $\nabla\rho(p) / \|\nabla\rho(p)\|$, is defined for all $u, v \in E$ by
$\mathrm{II}(u, v) = D^2\rho(p)(u, v) / \|\nabla\rho(p)\|$, and it is $0$ when $\nabla\rho(p) = 0$.
When $\rho$ is $C^2$ near $p$ and $\nabla\rho(p) \neq 0$, for tangent vectors $u$, $v$ (orthogonal
to $\nabla\rho(p)$) it equals $\langle D_u \nu, v \rangle$ for the unit normal field
$\nu = \nabla\rho / \|\nabla\rho\|$.

The formula is the second fundamental form (independent of the defining function, up to the sign
fixed by the normal) only for tangent $u$ and $v$: two defining functions of the same hyperplane
can give different values on the normal vector.

Formalized by `EuclideanGeometry.levelSetSecondFundamentalForm`, a definition declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-second-fundamental-form).

## Mean curvature of a level set

Let $E$ be a finite-dimensional real inner product space,
$\rho : E \to \mathbb{R}$ and $p \in E$. Write $\nabla\rho(p)$ for the gradient of $\rho$ at $p$,
$D^2\rho(p)$ for the second derivative of $\rho$ at $p$ (a bilinear form on $E$), and
$\Delta\rho(p) = \sum_i D^2\rho(p)(e_i, e_i)$ for a fixed orthonormal basis $(e_i)$ of $E$. The
mean curvature at $p$ of the level set of $\rho$ through $p$, with respect to the unit normal
$\nu = \nabla\rho(p) / \|\nabla\rho(p)\|$, is
$H = (\Delta\rho(p) - D^2\rho(p)(\nu, \nu)) / \|\nabla\rho(p)\|$, and $H = 0$ when
$\nabla\rho(p) = 0$.

This is the trace of the second fundamental form on the tangent hyperplane $\nabla\rho(p)^\perp$,
the sum of the principal curvatures, and it equals
$\operatorname{div}(\nabla\rho / \|\nabla\rho\|)(p)$ when $\rho$ is $C^2$ near $p$ and
$\nabla\rho(p) \neq 0$. Since $D^2\rho(p)$ is bilinear, $\Delta\rho(p)$ does not depend on the
choice of orthonormal basis.

Formalized by `EuclideanGeometry.levelSetMeanCurvature`, a definition declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-mean-curvature).

## Second fundamental form under rescaling of the defining function

Let $E$ be a
finite-dimensional real inner product space. For every $\rho : E \to \mathbb{R}$, all
$p, u, v \in E$ and every real $c \neq 0$, the second fundamental form at $p$ of the level set of
$c\rho$ through $p$, evaluated at $(u, v)$, equals $c / |c|$ (the sign of $c$) times the second
fundamental form at $p$ of the level set of $\rho$ through $p$, evaluated at $(u, v)$.

Formalized by `EuclideanGeometry.levelSetSecondFundamentalForm_smul`, a theorem declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-second-fundamental-form-smul).

## Mean curvature under rescaling of the defining function

Let $E$ be a finite-dimensional
real inner product space. For every $\rho : E \to \mathbb{R}$, every $p \in E$ and every real
$c \neq 0$, the mean curvature at $p$ of the level set of $c\rho$ through $p$ equals $c / |c|$
(the sign of $c$) times the mean curvature at $p$ of the level set of $\rho$ through $p$.

Formalized by `EuclideanGeometry.levelSetMeanCurvature_smul`, a theorem declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-mean-curvature-smul).

## Positive rescaling preserves the mean curvature

Let $E$ be a finite-dimensional real
inner product space. For every $\rho : E \to \mathbb{R}$, every $p \in E$ and every real $c > 0$,
the mean curvature at $p$ of the level set of $c\rho$ through $p$ equals the mean curvature at $p$
of the level set of $\rho$ through $p$.

Formalized by `EuclideanGeometry.levelSetMeanCurvature_smul_of_pos`, a theorem declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-mean-curvature-smul-of-pos).

## Reversing the normal negates the mean curvature

Let $E$ be a finite-dimensional real
inner product space. For every $\rho : E \to \mathbb{R}$ and every $p \in E$, the mean curvature
at $p$ of the level set of $-\rho$ through $p$ is the negative of the mean curvature at $p$ of the
level set of $\rho$ through $p$: replacing $\rho$ by $-\rho$ reverses the unit normal and changes
the sign of the mean curvature.

Formalized by `EuclideanGeometry.levelSetMeanCurvature_neg`, a theorem declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-mean-curvature-neg).

## Mean curvature of the unit sphere

Let $E$ be a finite-dimensional real inner product
space of dimension $n$. For every $p \in E$ with $\|p\| = 1$, the mean curvature at $p$ of the
level set of $\rho(x) = \|x\|^2 - 1$ through $p$ is $n - 1$. That is, the unit sphere of $E$ has
mean curvature $n - 1$ with respect to the outward normal, the mean curvature being the sum (not
the average) of the principal curvatures.

Formalized by `EuclideanGeometry.levelSetMeanCurvature_sphere`, a theorem declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-mean-curvature-sphere).

## Hyperplanes have zero mean curvature

Let $E$ be a finite-dimensional real inner product
space. For all $a \in E$, $c \in \mathbb{R}$ and $p \in E$, the mean curvature at $p$ of the level
set of $\rho(x) = \langle a, x \rangle - c$ through $p$ is $0$. In particular, for $a \neq 0$ the
hyperplane $\{x \mid \langle a, x \rangle = c\}$ has mean curvature $0$ at each of its points.

Formalized by `EuclideanGeometry.levelSetMeanCurvature_affine`, a theorem declared in [MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/HypersurfaceCurvature.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html#level-set-mean-curvature-affine).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Curvature of hypersurfaces](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/curves-and-surfaces/curvature-of-hypersurfaces)
