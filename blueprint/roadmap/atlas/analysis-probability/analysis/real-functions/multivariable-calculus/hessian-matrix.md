---
declaration: section
origin: cited
lean: MetaMathlibExt.hessianMatrix, MetaMathlibExt.hessianMatrix_apply, MetaMathlibExt.hessianMatrix_eq_fderiv_fderiv, MetaMathlibExt.hessianMatrix_symmetric, IsLocalMin.deriv_deriv_nonneg, MetaMathlibExt.isLocalMin_hessian_quadratic_nonneg
statement: formalized
proof: formalized
---

# Hessian matrix

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html).

## Hessian matrix

For a function $f : \mathbb{R}^n \to \mathbb{R}$ and a point
$x \in \mathbb{R}^n$, the Hessian matrix of $f$ at $x$ is the $n \times n$ real matrix whose
$(i, j)$ entry is $\frac{d}{ds}\big|_{s=0} \frac{d}{dt}\big|_{t=0} f(x + s e_i + t e_j)$, where
$e_1, \dots, e_n$ is the standard basis of $\mathbb{R}^n$ and a derivative that does not exist is
taken to be $0$.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9; stable ref https://en.wikipedia.org/wiki/Hessian_matrix.

Formalized by `MetaMathlibExt.hessianMatrix`, a definition declared in [MathlibExt/Analysis/Calculus/Hessian.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Hessian.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html#hessian-matrix).

## Entries of the Hessian matrix

For $f : \mathbb{R}^n \to \mathbb{R}$, a point
$x \in \mathbb{R}^n$ and indices $i, j$, the $(i, j)$ entry of the Hessian matrix of $f$ at $x$ is
$\frac{d}{ds}\big|_{s=0} \frac{d}{dt}\big|_{t=0} f(x + s e_i + t e_j)$, where $e_1, \dots, e_n$ is
the standard basis of $\mathbb{R}^n$ and a derivative that does not exist is taken to be $0$:
differentiate first along $e_j$, then along $e_i$.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9.

Formalized by `MetaMathlibExt.hessianMatrix_apply`, a theorem declared in [MathlibExt/Analysis/Calculus/Hessian.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Hessian.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html#hessian-matrix-apply).

## Hessian entries as second Fréchet derivatives

Let $f : \mathbb{R}^n \to \mathbb{R}$ be
twice continuously differentiable and let $x \in \mathbb{R}^n$. For all indices $i, j$, the
$(i, j)$ entry of the Hessian matrix of $f$ at $x$ equals $D(Df)(x)(e_i)(e_j)$, the derivative of
the Fréchet derivative $Df$ at $x$ in the direction $e_i$, applied to $e_j$, where
$e_1, \dots, e_n$ is the standard basis of $\mathbb{R}^n$.

Formalized by `MetaMathlibExt.hessianMatrix_eq_fderiv_fderiv`, a theorem declared in [MathlibExt/Analysis/Calculus/Hessian.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Hessian.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html#hessian-matrix-eq-fderiv-fderiv).

## Symmetry of the Hessian

If $f : \mathbb{R}^n \to \mathbb{R}$ is twice continuously
differentiable, then for every $x \in \mathbb{R}^n$ the Hessian matrix of $f$ at $x$ is symmetric:
it equals its transpose.

Proof: Rewrite the matrix entries as evaluations of the second Fréchet derivative and apply
Schwarz's theorem on the symmetry of second derivatives, as proved in Mathlib, following
Wikipedia's “Symmetry of second derivatives”.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Theorem 9.41 (pp. 235–236).

Formalized by `MetaMathlibExt.hessianMatrix_symmetric`, a theorem declared in [MathlibExt/Analysis/Calculus/Hessian.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Hessian.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html#hessian-matrix-symmetric).

## The second derivative is nonnegative at a local minimum

Let $g : \mathbb{R} \to \mathbb{R}$
be twice continuously differentiable. If $g$ has a local minimum at $x$, then $g''(x) \ge 0$.

This is the necessary direction of the one-variable second derivative test.

Formalized by `IsLocalMin.deriv_deriv_nonneg`, a theorem declared in [MathlibExt/Analysis/Calculus/Hessian.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Hessian.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html#deriv-deriv-nonneg).

## Second-derivative test, necessary condition

Let $f : \mathbb{R}^n \to \mathbb{R}$ be twice
continuously differentiable and let $x$ be a local minimum of $f$. Then the Hessian quadratic
form of $f$ at $x$ is nonnegative: writing $H$ for the Hessian matrix of $f$ at $x$, every
$v \in \mathbb{R}^n$ satisfies $\sum_{i, j} v_i H_{ij} v_j \ge 0$.

Proof: Restrict the function to the affine line through $x$ in direction $v$, apply the necessary
direction of the one-variable second derivative test, then expand the second Fréchet derivative in
the standard basis. The one-variable step argues by contradiction as in the proof of the
second-derivative test in Wikipedia's “Derivative test”: a negative second derivative makes the
first derivative negative just right of the critical point, so the function decreases there.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9.

Formalized by `MetaMathlibExt.isLocalMin_hessian_quadratic_nonneg`, a theorem declared in [MathlibExt/Analysis/Calculus/Hessian.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/Hessian.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html#is-local-min-hessian-quadratic-nonneg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hessian matrix](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/hessian-matrix)
