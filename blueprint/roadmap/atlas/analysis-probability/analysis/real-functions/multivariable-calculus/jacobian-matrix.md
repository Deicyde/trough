---
declaration: section
origin: cited
lean: MetaMathlibExt.jacobianMatrix, MetaMathlibExt.jacobianMatrix_apply, MetaMathlibExt.jacobianMatrix_apply_of_differentiableAt, MetaMathlibExt.jacobianMatrix_eq_toMatrix'_fderiv, MetaMathlibExt.jacobianMatrix_fun_mulVec, MetaMathlibExt.jacobianMatrix_mulVec_eq_fderiv, MetaMathlibExt.jacobianMatrix_comp
statement: formalized
proof: formalized
---

# Jacobian matrix

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html).

## Jacobian matrix

For $f : \mathbb{R}^m \to \mathbb{R}^n$ and $x \in \mathbb{R}^m$, the
Jacobian matrix of $f$ at $x$ is the $n \times m$ real matrix whose $(i, j)$ entry is the partial
derivative of the $i$-th component $f_i$ of $f$ in the $j$-th coordinate direction at $x$: the
derivative at $t = 0$ of $t \mapsto f_i(x + t e_j)$, where $e_j$ is the $j$-th standard basis
vector of $\mathbb{R}^m$. A partial derivative that does not exist is taken to be $0$.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9; stable ref https://en.wikipedia.org/wiki/Jacobian_matrix_and_determinant.

Formalized by `MetaMathlibExt.jacobianMatrix`, a definition declared in [MathlibExt/Analysis/Calculus/Jacobian.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Jacobian.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html#jacobian-matrix).

## Entries of the Jacobian matrix are partial derivatives

Let
$f : \mathbb{R}^m \to \mathbb{R}^n$ and $x \in \mathbb{R}^m$. For every row index $i$ and column
index $j$, the $(i, j)$ entry of the Jacobian matrix of $f$ at $x$ is the derivative at $t = 0$
of $t \mapsto f_i(x + t e_j)$, where $f_i$ is the $i$-th component of $f$ and $e_j$ is the
$j$-th standard basis vector of $\mathbb{R}^m$. This derivative is taken to be $0$ when it does
not exist.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9.

Formalized by `MetaMathlibExt.jacobianMatrix_apply`, a theorem declared in [MathlibExt/Analysis/Calculus/Jacobian.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Jacobian.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html#jacobian-matrix-apply).

## Jacobian entries at a point of differentiability

Let $f : \mathbb{R}^m \to \mathbb{R}^n$
be differentiable at $x \in \mathbb{R}^m$. Then for every row index $i$ and column index $j$, the
$(i, j)$ entry of the Jacobian matrix of $f$ at $x$ is the $i$-th coordinate of $Df(x)\, e_j$,
where $Df(x)$ is the Fréchet derivative of $f$ at $x$ and $e_j$ is the $j$-th standard basis
vector of $\mathbb{R}^m$.

Formalized by `MetaMathlibExt.jacobianMatrix_apply_of_differentiableAt`, a theorem declared in [MathlibExt/Analysis/Calculus/Jacobian.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Jacobian.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html#jacobian-matrix-apply-of-differentiable).

## The Jacobian is the matrix of the derivative

Let $f : \mathbb{R}^m \to \mathbb{R}^n$ be
differentiable at $x \in \mathbb{R}^m$. Then the Jacobian matrix of $f$ at $x$ is the matrix, in
the standard bases of $\mathbb{R}^m$ and $\mathbb{R}^n$, of the Fréchet derivative of $f$ at $x$,
viewed as a linear map $\mathbb{R}^m \to \mathbb{R}^n$.

Formalized by `MetaMathlibExt.jacobianMatrix_eq_toMatrix'_fderiv`, a theorem declared in [MathlibExt/Analysis/Calculus/Jacobian.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Jacobian.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html#jacobian-matrix-eq-to-matrix-fderiv).

## Jacobian of a linear map given by a matrix

Let $M$ be a real $n \times m$ matrix. At every
point $x \in \mathbb{R}^m$, the Jacobian matrix of the map $y \mapsto M y$ from $\mathbb{R}^m$ to
$\mathbb{R}^n$ is $M$.

Formalized by `MetaMathlibExt.jacobianMatrix_fun_mulVec`, a theorem declared in [MathlibExt/Analysis/Calculus/Jacobian.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Jacobian.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html#jacobian-matrix-fun-mul-vec).

## The Jacobian matrix computes the derivative

Let $f : \mathbb{R}^m \to \mathbb{R}^n$ be
differentiable at $x \in \mathbb{R}^m$, and let $J$ be the Jacobian matrix of $f$ at $x$. Then for
every $v \in \mathbb{R}^m$, the product $J v$ equals $Df(x)\, v$, the Fréchet derivative of $f$ at
$x$ applied to $v$.

Proof: The Jacobian is the matrix of the Fréchet derivative (Wikipedia, "Jacobian matrix and
determinant": it represents the total derivative), and multiplying a vector by the matrix of a
linear map applies the map to that vector.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9.

Formalized by `MetaMathlibExt.jacobianMatrix_mulVec_eq_fderiv`, a theorem declared in [MathlibExt/Analysis/Calculus/Jacobian.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Jacobian.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html#jacobian-matrix-mul-vec-eq-fderiv).

## Chain rule for Jacobian matrices

Let $f : \mathbb{R}^m \to \mathbb{R}^n$,
$g : \mathbb{R}^n \to \mathbb{R}^p$ and $x \in \mathbb{R}^m$, and write $J_h(y)$ for the Jacobian
matrix of $h$ at $y$. If $f$ is differentiable at $x$ and $g$ is differentiable at $f(x)$, then
$J_{g \circ f}(x) = J_g(f(x))\, J_f(x)$, a product of a $p \times n$ and an $n \times m$ matrix.

Proof: As in Wikipedia, "Jacobian matrix and determinant" (chain rule), write each Jacobian as
the matrix of the Fréchet derivative, then use the chain rule for Fréchet derivatives and the
fact that the matrix of a composition of linear maps is the product of their matrices.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Theorem 9.15.

Formalized by `MetaMathlibExt.jacobianMatrix_comp`, a theorem declared in [MathlibExt/Analysis/Calculus/Jacobian.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Jacobian.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html#jacobian-matrix-comp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobian matrix](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/jacobian-matrix)
