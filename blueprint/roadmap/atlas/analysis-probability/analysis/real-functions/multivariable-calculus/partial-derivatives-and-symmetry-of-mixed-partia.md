---
declaration: section
origin: cited
lean: MetaMathlibExt.partialDeriv, MetaMathlibExt.partialDeriv_spec, MetaMathlibExt.partialDeriv_eq_fderiv_apply, MetaMathlibExt.partialDeriv_eq_fderiv_apply_of_differentiable, MetaMathlibExt.partialDeriv_partialDeriv_eq_fderiv_fderiv, MetaMathlibExt.iterated_partialDeriv_commute
statement: formalized
proof: formalized
---

# Partial derivatives and symmetry of mixed partials

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html).

## Partial derivative along a coordinate axis

For $f : \mathbb{R}^n \to \mathbb{R}$ and a
coordinate index $i$, let $e_i$ be the $i$-th standard basis vector. The partial derivative
$\partial_i f : \mathbb{R}^n \to \mathbb{R}$ sends $x$ to the derivative at $t = 0$ of
$t \mapsto f(x + t e_i)$, taken to be $0$ when this function is not differentiable at $0$.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9; stable ref https://en.wikipedia.org/wiki/Partial_derivative.

Formalized by `MetaMathlibExt.partialDeriv`, a definition declared in [MathlibExt/Analysis/Calculus/HigherPartials.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/HigherPartials.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html#partial-deriv).

## Partial derivative as the derivative of a coordinate slice

For
$f : \mathbb{R}^n \to \mathbb{R}$, a coordinate index $i$ and a point $x \in \mathbb{R}^n$, let
$e_i$ be the $i$-th standard basis vector. The partial derivative of $f$ along the $i$-th
coordinate axis at $x$ equals the derivative at $t = 0$ of the one-variable function
$t \mapsto f(x + t e_i)$, taken to be $0$ when that function is not differentiable at $0$.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9.

Formalized by `MetaMathlibExt.partialDeriv_spec`, a theorem declared in [MathlibExt/Analysis/Calculus/HigherPartials.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/HigherPartials.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html#partial-deriv-spec).

## Partial derivative as a Fréchet derivative

Let $f : \mathbb{R}^n \to \mathbb{R}$ be
differentiable at a point $x$, and let $e_i$ be the $i$-th standard basis vector of
$\mathbb{R}^n$. Then the partial derivative of $f$ along the $i$-th coordinate axis at $x$ equals
$Df(x)\,e_i$, the Fréchet derivative of $f$ at $x$ applied to $e_i$.

The proof differentiates $f$ along the line $t \mapsto x + t e_i$ by the chain rule.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Ch. 9.

Formalized by `MetaMathlibExt.partialDeriv_eq_fderiv_apply`, a theorem declared in [MathlibExt/Analysis/Calculus/HigherPartials.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/HigherPartials.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html#partial-deriv-eq-fderiv-apply).

## Partial derivative function of a differentiable function

Let
$f : \mathbb{R}^n \to \mathbb{R}$ be differentiable and let $e_i$ be the $i$-th standard basis
vector of $\mathbb{R}^n$. Then the partial derivative $\partial_i f$ of $f$ along the $i$-th
coordinate axis is the function $x \mapsto Df(x)\,e_i$, where $Df(x)$ is the Fréchet derivative
of $f$ at $x$.

Formalized by `MetaMathlibExt.partialDeriv_eq_fderiv_apply_of_differentiable`, a theorem declared in [MathlibExt/Analysis/Calculus/HigherPartials.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/HigherPartials.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html#partial-deriv-eq-fderiv-apply-of-differe).

## Mixed partial derivatives via the second Fréchet derivative

Let
$f : \mathbb{R}^n \to \mathbb{R}$ be twice continuously differentiable, write $e_k$ for the $k$-th
standard basis vector of $\mathbb{R}^n$ and $\partial_k g$ for the partial derivative of a
function $g$ along the $k$-th coordinate axis, and let $Df$ be the Fréchet derivative of $f$,
a map from $\mathbb{R}^n$ to the linear maps $\mathbb{R}^n \to \mathbb{R}$. Then for all coordinate
indices $i, j$ and every $x \in \mathbb{R}^n$,
$\partial_j (\partial_i f)(x) = \big(D(Df)(x)\,e_j\big)\,e_i$, where $D(Df)(x)$ is the Fréchet
derivative of $Df$ at $x$.

Formalized by `MetaMathlibExt.partialDeriv_partialDeriv_eq_fderiv_fderiv`, a theorem declared in [MathlibExt/Analysis/Calculus/HigherPartials.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/HigherPartials.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html#partial-deriv-partial-deriv-eq-fderiv-fd).

## Symmetry of mixed partial derivatives (Clairaut's theorem)

For a function
$g : \mathbb{R}^n \to \mathbb{R}$, write $\partial_i g$ for its partial derivative along the
$i$-th coordinate axis. If $f : \mathbb{R}^n \to \mathbb{R}$ is twice continuously
differentiable, then for all coordinate indices $i, j$ and every point $x \in \mathbb{R}^n$,
$\partial_j (\partial_i f)(x) = \partial_i (\partial_j f)(x)$.

The proof writes both mixed partials as values of the second Fréchet derivative of $f$ at $x$
and applies Schwarz's theorem on the symmetry of second derivatives.

## Sources

- W. Rudin, Principles of Mathematical Analysis, 3rd ed., Theorem 9.41 (pp. 235–236).

Formalized by `MetaMathlibExt.iterated_partialDeriv_commute`, a theorem declared in [MathlibExt/Analysis/Calculus/HigherPartials.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/HigherPartials.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html#iterated-partial-deriv-commute).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partial derivatives and symmetry of mixed partials](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/partial-derivatives-and-symmetry-of-mixed-partia)
