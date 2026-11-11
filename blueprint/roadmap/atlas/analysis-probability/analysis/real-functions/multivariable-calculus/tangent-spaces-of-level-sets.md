---
declaration: section
origin: cited
lean: MetaMathlibExt.levelSet_tangent_vel_of_curve, HasStrictFDerivAt.exists_levelSet_curve, MetaMathlibExt.levelSet_curve_of_tangent_vel
statement: formalized
proof: formalized
---

# Tangent spaces of level sets

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/tangent-spaces-of-level-sets/index.html).

## Velocities of curves in a level set lie in the kernel of the derivative

Let $E$ be a
real normed space, $c \in \mathbb{R}$, and $f : E \to \mathbb{R}$ a function differentiable at
$x \in E$. If a curve $\gamma : \mathbb{R} \to E$ satisfies $\gamma(0) = x$, has derivative $v$ at
$0$, and satisfies $f(\gamma(t)) = c$ for all $t \in \mathbb{R}$, then $Df(x)v = 0$.

Proof: Apply the chain rule to `f ∘ γ`, then compare its derivative with that of the constant
function determined by the level-set equation.

## Sources

- J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Theorem 5.12; https://en.wikipedia.org/wiki/Tangent_space.

Formalized by `MetaMathlibExt.levelSet_tangent_vel_of_curve`, a theorem declared in [MathlibExt/Analysis/Calculus/TangentSpaceLevelSet.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/TangentSpaceLevelSet.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/tangent-spaces-of-level-sets/index.html#level-set-tangent-vel-of-curve).

## Kernel vectors are velocities of local curves in a level set

Let $E$ be a real Banach
space and let $f : E \to \mathbb{R}$ have a strict derivative $f'$ at $x \in E$, a continuous
linear map $E \to \mathbb{R}$ that is surjective. Then for every $v \in E$ with $f'(v) = 0$ there
is a curve $\varphi : \mathbb{R} \to E$ with $\varphi(0) = x$ and $\varphi'(0) = v$ such that
$f(\varphi(t)) = f(x)$ for all $t$ in some neighbourhood of $0$.

Formalized by `HasStrictFDerivAt.exists_levelSet_curve`, a theorem declared in [MathlibExt/Analysis/Calculus/TangentSpaceLevelSet.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/TangentSpaceLevelSet.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/tangent-spaces-of-level-sets/index.html#exists-level-set-curve).

## Kernel vectors are velocities of curves in a regular level set

Let $E$ be a real
Banach space, $f : E \to \mathbb{R}$ a $C^1$ function, $c \in \mathbb{R}$, and $x \in E$ a point
with $f(x) = c$ at which the derivative $Df(x) : E \to \mathbb{R}$ is surjective. Then for every
$v \in E$ with $Df(x)v = 0$ there is a curve $\gamma : \mathbb{R} \to E$ with $\gamma(0) = x$,
$\gamma'(0) = v$ and $f(\gamma(t)) = c$ for all $t \in \mathbb{R}$.

Proof: Use the implicit function theorem to construct a local curve tangent to the kernel vector,
then compose it with a bounded arctangent reparametrization to obtain a curve on all of `ℝ`
(implicit function theorem, Banach space version:
https://en.wikipedia.org/wiki/Implicit_function_theorem).

## Sources

- J. M. Lee, Introduction to Smooth Manifolds, 2nd ed., Theorem 5.12.

Formalized by `MetaMathlibExt.levelSet_curve_of_tangent_vel`, a theorem declared in [MathlibExt/Analysis/Calculus/TangentSpaceLevelSet.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Calculus/TangentSpaceLevelSet.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/tangent-spaces-of-level-sets/index.html#level-set-curve-of-tangent-vel).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tangent spaces of level sets](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/multivariable-calculus/tangent-spaces-of-level-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/real-functions/multivariable-calculus/tangent-spaces-of-level-sets)
