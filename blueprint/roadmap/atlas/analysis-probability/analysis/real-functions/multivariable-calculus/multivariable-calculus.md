---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.UnitNormCurveDerivOrthogonalWanted.inner_deriv_self_eq_zero_of_norm_eq_one, MathlibExt.Analysis.Calculus.ImplicitFunctionExpExampleWanted.exists_implicit_function_sq_mul_add_exp_add, MathlibExt.MeasureTheory.Geometry.SphericalCoordinatesWanted.integral_comp_spherical_symm, MathlibExt.Analysis.Calculus.EqualPartialsFactorSumWanted.exists_continuous_mul_add_of_fderiv_eq, MetaMathlibExt.greens_theorem, MathlibExt.Analysis.Calculus.SmoothVanishingOnAxesBoundWanted.exists_abs_le_mul_abs_mul_abs_of_contDiff_of_eq_zero_on_axes, MathlibExt.Analysis.Calculus.TaylorLittleoRemainderWanted.taylor_isLittleO_multivariable
statement: formalized
---

# Multivariable calculus: its own results

7 results, 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html).

Functions on R^n: partial derivatives, gradients, Jacobians, Hessians, implicit functions, regular level sets and tangent spaces, curve length, Green's theorem, multivariable Taylor expansions and counterexamples about mixed partials or continuity at the origin.

## A unit-norm curve in $\mathbb{R}^3$ is orthogonal to its derivative

Let
$f : \mathbb{R} \to \mathbb{R}^3$ be a differentiable map such that $\|f(t)\| = 1$ for every real
$t$, where $\|\cdot\|$ is the Euclidean norm. Then $\langle f'(t), f(t) \rangle = 0$ for every
real $t$, where $\langle \cdot, \cdot \rangle$ is the standard inner product on $\mathbb{R}^3$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of one variable), problem `ma_proofbench_l1_49`.

Stated but not proved: `MathlibExt.Analysis.Calculus.UnitNormCurveDerivOrthogonalWanted.inner_deriv_self_eq_zero_of_norm_eq_one` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/UnitNormCurveDerivOrthogonalWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/UnitNormCurveDerivOrthogonalWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html#inner-deriv-self-eq-zero-of-norm-eq-one).

## An implicit function for $x^2y_1+e^x+y_2=0$ near $(1,-1)$

Let
$f(x,y_1,y_2)=x^2y_1+e^x+y_2$ on $\mathbb{R}^3$. Then there are an open set
$U\subseteq\mathbb{R}^2$ containing $(1,-1)$ and a function $g : \mathbb{R}^2 \to \mathbb{R}$,
differentiable on $U$, with $g(1,-1)=0$ and $f(g(y_1,y_2),y_1,y_2)=0$ for all $(y_1,y_2)\in U$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of several variables), problem `ma_proofbench_l1_43`.

Stated but not proved: `MathlibExt.Analysis.Calculus.ImplicitFunctionExpExampleWanted.exists_implicit_function_sq_mul_add_exp_add` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/ImplicitFunctionExpExampleWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/ImplicitFunctionExpExampleWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html#exists-implicit-function-sq-mul-add-exp).

## Change of variables to spherical coordinates

Let $E$ be a real Banach space and let
$f \colon \mathbb{R}^3 \to E$ be any function. Then the integral of $f$ over $\mathbb{R}^3$
equals the integral over the set of $(r, \theta, \varphi) \in \mathbb{R}^3$ with $r > 0$,
$0 < \theta < 2\pi$ and $0 < \varphi < \pi$ of
$r^2 \sin\varphi \cdot f(r \sin\varphi \cos\theta,\, r \sin\varphi \sin\theta,\, r \cos\varphi)$,
both integrals being Bochner integrals with respect to Lebesgue measure.

No integrability hypothesis is assumed; as usual for Bochner integrals, a non-integrable
function has integral $0$. This is the three-dimensional analogue of the polar-coordinate
change of variables.

## Sources

- W. Rudin, *Real and Complex Analysis*, 3rd ed., Ch. 8, Exercise 4 (spherical coordinates in `ℝ³`).
- https://en.wikipedia.org/wiki/Spherical_coordinate_system#Integration_and_differentiation_in_spherical_coordinates

Stated but not proved: `MathlibExt.MeasureTheory.Geometry.SphericalCoordinatesWanted.integral_comp_spherical_symm` is written with `theorem_wanted` in [WantedExt/MeasureTheory/Geometry/SphericalCoordinatesWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/MeasureTheory/Geometry/SphericalCoordinatesWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html#integral-comp-spherical-symm).

## Equal partial derivatives give a factor $x+y$

Let $f : \mathbb{R}^2 \to \mathbb{R}$ be
continuously differentiable with $\partial_1 f = \partial_2 f$ on $\mathbb{R}^2$ and $f(0,0)=0$.
Then there is a continuous $g : \mathbb{R}^2 \to \mathbb{R}$ with $f(x,y)=g(x,y)\,(x+y)$ for all
$(x,y)\in\mathbb{R}^2$.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level I (Real functions; Functions of several variables), problem `ma_proofbench_l1_02`.

Stated but not proved: `MathlibExt.Analysis.Calculus.EqualPartialsFactorSumWanted.exists_continuous_mul_add_of_fderiv_eq` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/EqualPartialsFactorSumWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/EqualPartialsFactorSumWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html#exists-continuous-mul-add-of-fderiv-eq).

## Green's theorem

Let $U \subseteq \mathbb{R}^2$ be open, let $D \subseteq U$ be bounded and
measurable, and let $L, M : \mathbb{R}^2 \to \mathbb{R}$ be continuously differentiable on $U$.
Let $a\lt b$ and let $\gamma=(\gamma_1,\gamma_2) : \mathbb{R} \to \mathbb{R}^2$ be continuous on
$[a,b]$, with $\gamma(a)=\gamma(b)$, injective on $[a,b)$, with $\gamma(t)\ne\gamma(a)$ for
$a\lt t\lt b$, with image $\gamma([a,b])$ equal to the boundary of $D$, and with $\gamma(t)\in U$ for
all $t\in[a,b]$. Suppose there is a finite set $S\subseteq[a,b]$ containing $a$ and $b$ such that
$\gamma$ is continuously differentiable on $[a,b]\setminus S$ and on $[u,v]$ for any two
consecutive points $u\lt v$ of $S$, and such that for every $t\in(a,b)\setminus S$ we have
$\gamma'(t)\ne0$ and, for some $\delta>0$, $\gamma(t)+\varepsilon(-\gamma_2'(t),\gamma_1'(t))\in D$
for all $0\lt \varepsilon\lt \delta$ (so $D$ lies to the left of the curve). Then

$$
\int_a^b \bigl(L(\gamma(t))\,\gamma_1'(t)+M(\gamma(t))\,\gamma_2'(t)\bigr)\,dt
=\int_D \Bigl(\frac{\partial M}{\partial x}-\frac{\partial L}{\partial y}\Bigr)\,d(x,y).
$$

## Sources

- https://en.wikipedia.org/wiki/Green%27s_theorem.

Stated but not proved: `MetaMathlibExt.greens_theorem` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/GreensTheoremWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/GreensTheoremWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html#greens-theorem).

## Smooth functions vanishing on the axes are $O(|x|\,|y|)$ near the origin

Let
$f : \mathbb{R}^2 \to \mathbb{R}$ be infinitely differentiable with $f(x,y) = 0$ whenever $xy = 0$.
Then there is a constant $C > 0$ such that $|f(x,y)| \le C\,|x|\,|y|$ for all real $x$ and $y$ with
$|x| < 1$ and $|y| < 1$, that is, on the open unit ball of $\mathbb{R}^2$ for the maximum norm.

## Sources

- MA-ProofBench (L. Pu et al., arXiv:2606.13782), Level II (Real functions; Functions of several variables), problem `ma_proofbench_l2_01`.

Stated but not proved: `MathlibExt.Analysis.Calculus.SmoothVanishingOnAxesBoundWanted.exists_abs_le_mul_abs_mul_abs_of_contDiff_of_eq_zero_on_axes` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/SmoothVanishingOnAxesBoundWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/SmoothVanishingOnAxesBoundWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html#exists-abs-le-mul-abs-mul-abs-of-cont-di).

## Taylor's theorem with little-o remainder in several variables

Let $E$ and $F$ be normed
vector spaces over $\mathbb{R}$, let $n$ be a natural number, and let $f : E \to F$ be $n$ times
continuously differentiable on a neighbourhood of a point $x_0 \in E$. Write $D^k f(x_0)$ for the
$k$-th Fréchet derivative of $f$ at $x_0$, a continuous $k$-linear map from $E^k$ to $F$. Then, as
$x$ tends to $x_0$,

$$f(x) - \sum_{k=0}^{n} \frac{1}{k!}\, D^k f(x_0)(x - x_0, \ldots, x - x_0) =
o\bigl(\|x - x_0\|^n\bigr).$$

## Sources

- The integral-remainder form exists as `map_add_eq_sum_add_integral_iteratedFDeriv`.
- H. Cartan, *Differential Calculus*, Ch. III, Taylor's formula with remainder.
- https://en.wikipedia.org/wiki/Taylor%27s_theorem#Taylor's_theorem_in_several_variables

Stated but not proved: `MathlibExt.Analysis.Calculus.TaylorLittleoRemainderWanted.taylor_isLittleO_multivariable` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/TaylorLittleoRemainderWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/Calculus/TaylorLittleoRemainderWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html#taylor-is-little-o-multivariable).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multivariable calculus](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/multivariable-calculus)
