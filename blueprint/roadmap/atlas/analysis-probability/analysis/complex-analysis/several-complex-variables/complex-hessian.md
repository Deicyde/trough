---
declaration: section
origin: cited
lean: MetaMathlibExt.realHessian, MetaMathlibExt.complexHessian, MetaMathlibExt.realHessian_const, MetaMathlibExt.complexHessian_const
statement: formalized
proof: formalized
---

# Complex Hessian

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/complex-hessian/index.html).

## Real Hessian

For a function $u : \mathbb{C}^n \to \mathbb{R}$, with $\mathbb{C}^n$
viewed as a real normed space, write $Du(w)$ for the real Fréchet derivative of $u$ at $w$. For
points $z, a, b \in \mathbb{C}^n$, the real Hessian $D^2u(z)(a, b)$ is the real number obtained
by taking the real Fréchet derivative at $z$ of the map $w \mapsto Du(w)$, applying it to $a$,
and applying the result to $b$.

As usual in Mathlib, a derivative that does not exist is taken to be zero.

Formalized by `MetaMathlibExt.realHessian`, a definition declared in [MathlibExt/Analysis/Complex/ComplexHessian.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/ComplexHessian.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/complex-hessian/index.html#real-hessian).

## Complex Hessian

Let $u : \mathbb{C}^n \to \mathbb{R}$ and $z \in \mathbb{C}^n$, write
$e_1, \dots, e_n$ for the standard basis of $\mathbb{C}^n$, write $i$ for the imaginary unit, and
for $a, b \in \mathbb{C}^n$ write $D^2u(z)(a, b)$ for the real Hessian of $u$ at $z$. The complex
Hessian of $u$ at $z$ is the $n \times n$ complex matrix whose $(j, k)$ entry is

$$
u_{j\bar k}(z) = \frac{D^2u(z)(e_j, e_k) + D^2u(z)(i e_j, i e_k) +
i \left(D^2u(z)(e_j, i e_k) - D^2u(z)(i e_j, e_k)\right)}{4}.
$$

When $u$ is of class $C^2$, in real coordinates $z_j = x_j + i y_j$ this is
$\partial^2 u / \partial z_j \partial \bar z_k =
(u_{x_j x_k} + u_{y_j y_k} + i (u_{x_j y_k} - u_{y_j x_k})) / 4$.

Formalized by `MetaMathlibExt.complexHessian`, a definition declared in [MathlibExt/Analysis/Complex/ComplexHessian.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/ComplexHessian.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/complex-hessian/index.html#complex-hessian).

## Constant functions have zero real Hessian

For every real constant $c$, the function
$u : \mathbb{C}^n \to \mathbb{R}$ with constant value $c$ has real Hessian $D^2u(z)(a, b) = 0$ for
all $z, a, b \in \mathbb{C}^n$.

Formalized by `MetaMathlibExt.realHessian_const`, a theorem declared in [MathlibExt/Analysis/Complex/ComplexHessian.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/ComplexHessian.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/complex-hessian/index.html#real-hessian-const).

## Constant functions have zero complex Hessian

For every real constant $c$, the function
$u : \mathbb{C}^n \to \mathbb{R}$ with constant value $c$ has complex Hessian equal to the zero
$n \times n$ matrix at every point $z \in \mathbb{C}^n$.

Formalized by `MetaMathlibExt.complexHessian_const`, a theorem declared in [MathlibExt/Analysis/Complex/ComplexHessian.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Complex/ComplexHessian.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/complex-hessian/index.html#complex-hessian-const).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complex Hessian](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/several-complex-variables/complex-hessian/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/complex-analysis/several-complex-variables/complex-hessian)
