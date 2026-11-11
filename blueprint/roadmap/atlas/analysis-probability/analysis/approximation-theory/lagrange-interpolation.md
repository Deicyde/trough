---
declaration: section
origin: cited
lean: Lagrange.evalBasis, Lagrange.lebesgueFunction, Lagrange.evalInterpolant, Lagrange.evalBasis_self, Lagrange.evalBasis_of_ne, Lagrange.evalInterpolant_at_node, Lagrange.lebesgueFunction_at_node
statement: formalized
proof: formalized
---

# Lagrange interpolation

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html).

## Evaluated Lagrange basis polynomial

For real nodes $x_0, \dots, x_{n-1}$, an index
$k < n$ and a real number $t$, the value at $t$ of the $k$-th Lagrange basis polynomial is
$\ell_k(t) = \prod_{j \ne k} (x_k - x_j)^{-1} (t - x_j)$, the product running over the indices
$j < n$ with $j \ne k$.

The inverse follows the convention $0^{-1} = 0$, so $\ell_k$ is identically $0$ when some other
node equals $x_k$.

Formalized by `Lagrange.evalBasis`, a definition declared in [MathlibExt/Analysis/Polynomial/Lagrange.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Polynomial/Lagrange.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html#eval-basis).

## Lebesgue function

For real nodes $x_0, \dots, x_{n-1}$ and a real number $t$, the
Lebesgue function of the nodes at $t$ is $L_n(t) = \sum_{k < n} |\ell_k(t)|$, where $\ell_k$ is
the $k$-th evaluated Lagrange basis polynomial for these nodes.

Formalized by `Lagrange.lebesgueFunction`, a definition declared in [MathlibExt/Analysis/Polynomial/Lagrange.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Polynomial/Lagrange.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html#lebesgue-function).

## Lagrange interpolant

For real nodes $x_0, \dots, x_{n-1}$, a function
$f : \mathbb{R} \to \mathbb{R}$ and a real number $t$, the Lagrange interpolant of $f$ at $t$ is
$\mathcal{L}^n f(t) = \sum_{k < n} f(x_k)\, \ell_k(t)$, where $\ell_k$ is the $k$-th evaluated
Lagrange basis polynomial for these nodes.

Formalized by `Lagrange.evalInterpolant`, a definition declared in [MathlibExt/Analysis/Polynomial/Lagrange.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Polynomial/Lagrange.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html#eval-interpolant).

## Lagrange basis polynomials equal one at their own node

If the real nodes
$x_0, \dots, x_{n-1}$ are pairwise distinct, then $\ell_k(x_k) = 1$ for every $k < n$, where
$\ell_k$ is the $k$-th evaluated Lagrange basis polynomial for these nodes.

Formalized by `Lagrange.evalBasis_self`, a theorem declared in [MathlibExt/Analysis/Polynomial/Lagrange.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Polynomial/Lagrange.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html#eval-basis-self).

## Lagrange basis polynomials vanish at the other nodes

For real nodes
$x_0, \dots, x_{n-1}$ and indices $k \ne j$ below $n$, the $k$-th evaluated Lagrange basis
polynomial $\ell_k$ for these nodes satisfies $\ell_k(x_j) = 0$.

The nodes need not be distinct.

Formalized by `Lagrange.evalBasis_of_ne`, a theorem declared in [MathlibExt/Analysis/Polynomial/Lagrange.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Polynomial/Lagrange.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html#eval-basis-of-ne).

## The Lagrange interpolant matches the function at the nodes

If the real nodes
$x_0, \dots, x_{n-1}$ are pairwise distinct, then for every function $f : \mathbb{R} \to \mathbb{R}$
and every $j < n$, the Lagrange interpolant of $f$ on these nodes satisfies
$\mathcal{L}^n f(x_j) = f(x_j)$.

Formalized by `Lagrange.evalInterpolant_at_node`, a theorem declared in [MathlibExt/Analysis/Polynomial/Lagrange.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Polynomial/Lagrange.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html#eval-interpolant-at-node).

## The Lebesgue function equals one at the nodes

If the real nodes $x_0, \dots, x_{n-1}$
are pairwise distinct, then their Lebesgue function satisfies $L_n(x_j) = 1$ for every $j < n$.

Formalized by `Lagrange.lebesgueFunction_at_node`, a theorem declared in [MathlibExt/Analysis/Polynomial/Lagrange.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Polynomial/Lagrange.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html#lebesgue-function-at-node).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lagrange interpolation](https://deicyde.github.io/atlas-lean/roadmap/Analysis/approximation-theory/lagrange-interpolation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/approximation-theory/lagrange-interpolation)
