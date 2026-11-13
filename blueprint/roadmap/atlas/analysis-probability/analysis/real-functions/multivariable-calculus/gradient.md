---
declaration: section
origin: cited
lean: Real.dotL, Real.hasGradientAt_ofLp, Real.hasDerivAt_line_of_hasFDerivAt, MetaMathlibExt.gradient_comp
statement: formalized
proof: formalized
---

# Gradient

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/gradient/index.html).

## The dot product with a fixed vector

For a finite type $\iota$ and a vector
$x \in \mathbb{R}^\iota$, this is the map $v \mapsto v \cdot x = \sum_{i \in \iota} v_i x_i$,
as a continuous linear functional $\mathbb{R}^\iota \to \mathbb{R}$.

Formalized by `Real.dotL`, a definition declared in [MathlibExt/Analysis/Calculus/DotProductGradient.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/DotProductGradient.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/gradient/index.html#dot-l).

## A Fréchet derivative given by a dot product is a gradient

Let $\iota$ be a finite type,
let $f : \mathbb{R}^\iota \to \mathbb{R}$ and $g, z \in \mathbb{R}^\iota$, and suppose that, for the
sup norm on $\mathbb{R}^\iota$, $f$ is Fréchet differentiable at $z$ with derivative
$v \mapsto v \cdot g$. Then $f$, viewed as a function on the Euclidean space $\mathbb{R}^\iota$ with
inner product $\langle v, w \rangle = \sum_{i \in \iota} v_i w_i$, has gradient $g$ at $z$.

Formalized by `Real.hasGradientAt_ofLp`, a theorem declared in [MathlibExt/Analysis/Calculus/DotProductGradient.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/DotProductGradient.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/gradient/index.html#has-gradient-at-of-lp).

## Directional derivative from the gradient

Let $\iota$ be a finite type, let
$f : \mathbb{R}^\iota \to \mathbb{R}$ and $g, z \in \mathbb{R}^\iota$, and suppose $f$ is Fréchet
differentiable at $z$ with derivative $w \mapsto w \cdot g$. Then for every
$v \in \mathbb{R}^\iota$, the function $t \mapsto f(z + t v)$ on $\mathbb{R}$ has derivative
$v \cdot g$ at $t = 0$.

Formalized by `Real.hasDerivAt_line_of_hasFDerivAt`, a theorem declared in [MathlibExt/Analysis/Calculus/DotProductGradient.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/DotProductGradient.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/gradient/index.html#has-deriv-at-line-of-has-fderiv-at).

## The chain rule for gradients

Let $E$ and $F$ be real Hilbert spaces, let $g : E \to F$
be differentiable at $x \in E$, and let $f : F \to \mathbb{R}$ be differentiable at $g(x)$. Then
$\nabla (f \circ g)(x) = Dg(x)^* \, \nabla f(g(x))$, where $Dg(x) : E \to F$ is the Fréchet
derivative of $g$ at $x$ and $Dg(x)^*$ is its adjoint.

Formalized by `MetaMathlibExt.gradient_comp`, a theorem declared in [MathlibExt/Analysis/Calculus/Gradient.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Calculus/Gradient.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/gradient/index.html#gradient-comp).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gradient](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/gradient/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/gradient)
