---
declaration: section
origin: cited
lean: ODE.existsUnique_hasDerivAt_eq_continuousLinearMap, HasDerivAt.det_of_mul, MathlibExt.Analysis.ODE.LinearSystemFundamentalMatrixWanted.fundamental_matrix_linear_system, MathlibExt.Analysis.ODE.LinearSystemFundamentalMatrixWanted.fundamental_matrix_liouville_det
statement: formalized
proof: formalized
---

# Linear systems and fundamental matrices

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/linear-systems-and-fundamental-matrices/index.html).

## Global existence and uniqueness for homogeneous linear ODEs

Let $E$ be a real Banach
space, write $L(E)$ for the space of continuous linear maps $E \to E$ with the operator norm,
let $B : \mathbb{R} \to L(E)$ be continuous, and let $t_0 \in \mathbb{R}$ and $x_0 \in E$. Then
there is exactly one function $x : \mathbb{R} \to E$ with $x(t_0) = x_0$ such that $x$ is
differentiable at every $t \in \mathbb{R}$ with $x'(t) = B(t)\,x(t)$.

Formalized by `ODE.existsUnique_hasDerivAt_eq_continuousLinearMap`, a theorem declared in [MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/linear-systems-and-fundamental-matrices/index.html#exists-unique-has-deriv-at-eq-continuous).

## Jacobi's formula when the derivative is a left multiple of the matrix

Let
$n \in \mathbb{N}$, let $A$ be a real $n \times n$ matrix, let
$\Phi : \mathbb{R} \to \mathbb{R}^{n \times n}$, and let $t \in \mathbb{R}$. If $\Phi$ is
differentiable at $t$ with $\Phi'(t) = A \Phi(t)$, then $s \mapsto \det \Phi(s)$ is
differentiable at $t$ with derivative $\operatorname{tr}(A) \det \Phi(t)$.

Formalized by `HasDerivAt.det_of_mul`, a theorem declared in [MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/linear-systems-and-fundamental-matrices/index.html#det-of-mul).

## Fundamental matrix of a linear system

Let $n \in \mathbb{N}$, let
$A : \mathbb{R} \to \mathbb{R}^{n \times n}$ be continuous, let $t_0 \in \mathbb{R}$, and write $I$
for the $n \times n$ identity matrix. Then there is a function
$\Phi : \mathbb{R} \to \mathbb{R}^{n \times n}$ with $\Phi(t_0) = I$, $\Phi'(t) = A(t) \Phi(t)$ and
$\det \Phi(t) \ne 0$ for every $t \in \mathbb{R}$, such that for every $x_0 \in \mathbb{R}^n$
the function $x(t) = \Phi(t) x_0$ satisfies $x(t_0) = x_0$ and $x'(t) = A(t) x(t)$ for every
$t \in \mathbb{R}$, and every $y : \mathbb{R} \to \mathbb{R}^n$ with $y(t_0) = x_0$ and
$y'(t) = A(t) y(t)$ for every $t \in \mathbb{R}$ equals $x$.

Proof: Global solutions are patched from clamped-time systems using Teschl, Theorem 3.9, then
assembled into the principal matrix solution of (3.83) and Theorem 3.10. Liouville's formula gives
invertibility as in (3.88)-(3.89).

## Sources

- G. Teschl, Ordinary Differential Equations and Dynamical Systems, Section 3.4; stable ref https://en.wikipedia.org/wiki/Fundamental_matrix_(linear_differential_equation).

Formalized by `MathlibExt.Analysis.ODE.LinearSystemFundamentalMatrixWanted.fundamental_matrix_linear_system`, a theorem declared in [MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/linear-systems-and-fundamental-matrices/index.html#fundamental-matrix-linear-system).

## Liouville's formula for the principal matrix solution

Let $n \in \mathbb{N}$, let
$A : \mathbb{R} \to \mathbb{R}^{n \times n}$ be continuous, let $t_0 \in \mathbb{R}$, write $I$ for
the $n \times n$ identity matrix, and let $\Phi : \mathbb{R} \to \mathbb{R}^{n \times n}$ satisfy
$\Phi(t_0) = I$ and $\Phi'(t) = A(t) \Phi(t)$ for every $t \in \mathbb{R}$. Then for every
$t \in \mathbb{R}$,
$\det \Phi(t) = \det \Phi(t_0) \exp\left(\int_{t_0}^{t} \operatorname{tr} A(s)\, ds\right)$.

Proof: Jacobi's formula follows from the determinant's first-order term; an integrating factor then
gives Teschl, Lemma 3.11, formula (3.91).

## Sources

- G. Teschl, Ordinary Differential Equations and Dynamical Systems, Section 3.4; https://en.wikipedia.org/wiki/Abel%27s_identity.

Formalized by `MathlibExt.Analysis.ODE.LinearSystemFundamentalMatrixWanted.fundamental_matrix_liouville_det`, a theorem declared in [MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean, line 379](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/LinearSystemFundamentalMatrix.lean#L379). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/linear-systems-and-fundamental-matrices/index.html#fundamental-matrix-liouville-det).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear systems and fundamental matrices](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/linear-systems-and-fundamental-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/ordinary-differential-equations/linear-systems-and-fundamental-matrices)
