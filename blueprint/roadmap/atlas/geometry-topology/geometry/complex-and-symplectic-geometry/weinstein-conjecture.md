---
declaration: section
origin: cited
lean: MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.OneForm, MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.TwoForm, MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.SmoothVectorField, MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsExteriorDerivative, MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsContactForm3, MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsReebVectorField, MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsIntegralCurve, MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.HasClosedReebOrbit
statement: formalized
---

# Weinstein conjecture

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html).

## Smooth one-forms

Let $M$ be a smooth manifold (possibly with boundary or corners).
A smooth one-form on $M$ is a smooth section of the cotangent bundle of $M$: a smooth choice of
a linear map $\alpha_x : T_xM \to \mathbb{R}$ at each point $x \in M$.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.OneForm`, an abbreviation declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#one-form).

## Two-forms as fields of bilinear forms

Let $M$ be a smooth manifold (possibly with
boundary or corners). A two-form on $M$ is here a smooth section of the bundle whose fiber at
$x \in M$ is the space of bilinear maps $T_xM \times T_xM \to \mathbb{R}$; antisymmetry is not
required.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.TwoForm`, an abbreviation declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#two-form).

## Smooth vector fields

Let $M$ be a smooth manifold (possibly with boundary or
corners). A smooth vector field on $M$ is a smooth section of the tangent bundle of $M$: a smooth
choice of a tangent vector $X_x \in T_xM$ at each point $x \in M$.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.SmoothVectorField`, an abbreviation declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#smooth-vector-field).

## Exterior derivative of a one-form

A two-form $d\alpha$ on $M$ is the exterior derivative
of a one-form $\alpha$ on $M$ when, for all smooth vector fields $X, Y$ on $M$ and every point
$x \in M$,

$$
d\alpha_x(X_x, Y_x) = X_x\big(\alpha(Y)\big) - Y_x\big(\alpha(X)\big) - \alpha_x\big([X, Y]_x\big),
$$

where $\alpha(Y)$ is the function $y \mapsto \alpha_y(Y_y)$, $X_x(f)$ is the derivative of a
function $f$ at $x$ in the direction $X_x$, and $[X, Y]$ is the Lie bracket of $X$ and $Y$.

This coordinate-free identity determines $d\alpha$ uniquely.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsExteriorDerivative`, a definition declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#is-exterior-derivative).

## Contact condition for a one-form

Let $\alpha$ be a one-form and $d\alpha$ a two-form on
$M$. The pair satisfies the contact condition when $d\alpha$ is the exterior derivative of
$\alpha$ and, at every point $x \in M$, the covector $\alpha_x$ is nonzero and there are tangent
vectors $u, v \in T_xM$ with $\alpha_x(u) = \alpha_x(v) = 0$ and $d\alpha_x(u, v) \ne 0$.

When $M$ has dimension $3$, this says that $\alpha$ vanishes nowhere and $d\alpha$ is
nondegenerate on the plane $\ker \alpha_x$, which is equivalent to $\alpha \wedge d\alpha$
vanishing nowhere.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsContactForm3`, a definition declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#is-contact-form3).

## Reeb vector fields

Let $\alpha$ be a one-form and $d\alpha$ a two-form on $M$. An
assignment $R$ of a tangent vector $R(x) \in T_xM$ to each point $x \in M$ is a Reeb vector field
for $(\alpha, d\alpha)$ when, at every point $x \in M$, $\alpha_x(R(x)) = 1$ and
$d\alpha_x(R(x), v) = 0$ for all $v \in T_xM$.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsReebVectorField`, a definition declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#is-reeb-vector-field).

## Integral curves

Let $M$ be a smooth manifold (possibly with boundary or corners) and let
$R$ assign to each point $x \in M$ a tangent vector $R(x) \in T_xM$. A curve
$\gamma : \mathbb{R} \to M$ is an integral curve of $R$ when $\gamma$ is smooth and
$\gamma'(t) = R(\gamma(t))$ for every $t \in \mathbb{R}$.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.IsIntegralCurve`, a definition declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#is-integral-curve).

## Vector fields with a closed orbit

Let $M$ be a smooth manifold (possibly with boundary or
corners) and let $R$ assign to each point $x \in M$ a tangent vector $R(x) \in T_xM$. We say that
$R$ has a closed orbit when there are a curve $\gamma : \mathbb{R} \to M$ and a real number
$T > 0$ such that $\gamma$ is $T$-periodic, $\gamma$ is a smooth integral curve of $R$, and
$\gamma$ is not constant.

The main theorem applies this to a Reeb vector field, whence the name closed Reeb orbit.

Formalized by `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.HasClosedReebOrbit`, a definition declared in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#has-closed-reeb-orbit).

## Weinstein conjecture in dimension three (Taubes)

Let $M$ be a nonempty compact Hausdorff
smooth manifold without boundary, modelled on a real vector space of dimension $3$. Let $\alpha$
be a smooth one-form and $d\alpha$ a smooth two-form on $M$ satisfying the contact condition:
$d\alpha$ is the exterior derivative of $\alpha$ and, at every point $x$, $\alpha_x \ne 0$ and
$d\alpha_x(u, v) \ne 0$ for some $u, v \in \ker \alpha_x$. Let $R$ be a Reeb vector field for
$(\alpha, d\alpha)$. Then $R$ has a closed orbit: a nonconstant smooth integral curve of $R$
that is periodic with some positive period.

## Sources

- C.H. Taubes, 'The Seiberg–Witten equations and the Weinstein conjecture', Geom. Topol. 11 (2007) 2117–2202; arXiv:math/0611007. Conjecture: A. Weinstein, 'On the hypotheses of Rabinowitz' periodic orbit theorems', J. Differential Equations 33 (1979) 353–358. §141 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `weinstein_conjecture_dim3` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.WeinsteinConjecture3DWanted.Geometry.WeinsteinConjecture3DProblem.weinstein_conjecture_dim_three` is written with `theorem_wanted` in [WantedExt/Geometry/WeinsteinConjecture3DWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/WeinsteinConjecture3DWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html#weinstein-conjecture-dim-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weinstein conjecture](https://deicyde.github.io/atlas-lean/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/complex-and-symplectic-geometry/weinstein-conjecture)
