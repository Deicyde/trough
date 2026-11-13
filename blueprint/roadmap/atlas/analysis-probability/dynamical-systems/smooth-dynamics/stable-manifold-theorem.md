---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.E, MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.complexEigenvalues, MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.IsHyperbolicLinear, MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.stable_unstable_manifolds_exist
statement: formalized
---

# Stable manifold theorem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/stable-manifold-theorem/index.html).

## Euclidean space $\mathbb{R}^n$ for local stable and unstable sets

For a natural number
$n$, this is the space $\mathbb{R}^n$ of real $n$-tuples with the Euclidean inner product and
norm.

Formalized by `MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.E`, an abbreviation declared in [WantedExt/Dynamics/StableUnstableManifoldsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/StableUnstableManifoldsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/stable-manifold-theorem/index.html#e).

## Complex eigenvalues of a real linear map

For a continuous linear map $L$ from
$\mathbb{R}^n$ to itself, the complex eigenvalues of $L$ form the multiset of complex roots of the
characteristic polynomial of $L$, each counted with its multiplicity as a root.

Formalized by `MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.complexEigenvalues`, a definition declared in [WantedExt/Dynamics/StableUnstableManifoldsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/StableUnstableManifoldsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/stable-manifold-theorem/index.html#complex-eigenvalues).

## Hyperbolic linear map

A continuous linear map $L$ from $\mathbb{R}^n$ to itself is
hyperbolic when none of its complex eigenvalues lies on the unit circle, that is, every complex
root $\mu$ of the characteristic polynomial of $L$ satisfies $|\mu| \ne 1$.

Formalized by `MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.IsHyperbolicLinear`, a definition declared in [WantedExt/Dynamics/StableUnstableManifoldsWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/StableUnstableManifoldsWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/stable-manifold-theorem/index.html#is-hyperbolic-linear).

## Local stable and unstable sets at a hyperbolic fixed point

Let $f : \mathbb{R}^n \to
\mathbb{R}^n$ be continuously differentiable on a neighbourhood of a point $x_0$ with
$f(x_0) = x_0$, and suppose that the derivative $Df(x_0)$ is invertible and hyperbolic. Then
there is an open set $U$ containing $x_0$ such that the local stable set
$W^s = \{x : f^k(x) \in U \text{ for all } k \ge 0 \text{ and } f^k(x) \to x_0 \text{ as }
k \to \infty\}$ and the local unstable set $W^u$, consisting of the points $x$ for which there
is a sequence $(y_k)_{k \ge 0}$ in $U$ with $y_0 = x$, $f(y_{k+1}) = y_k$ for all $k$ and
$y_k \to x_0$, satisfy $W^s \cap W^u = \{x_0\}$.

This is only the set-level part of the Hadamard–Perron theorem: it does not assert that $W^s$
and $W^u$ are $C^1$ submanifolds tangent to the stable and unstable subspaces of $Df(x_0)$.

## Sources

- J. Hadamard, 'Sur l'itération et les solutions asymptotiques des équations différentielles', Bull. Soc. Math. France 29 (1901); O. Perron, 'Über Stabilität und asymptotisches Verhalten der Integrale von Differentialgleichungssystemen', Math. Z. 29 (1929) 129–160. Listed as §104 in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `stable_unstable_manifolds` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.StableUnstableManifoldsWanted.Dynamics.StableUnstableManifoldsProblem.stable_unstable_manifolds_exist` is written with `theorem_wanted` in [WantedExt/Dynamics/StableUnstableManifoldsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/StableUnstableManifoldsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/stable-manifold-theorem/index.html#stable-unstable-manifolds-exist).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Stable manifold theorem](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/smooth-dynamics/stable-manifold-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/smooth-dynamics/stable-manifold-theorem)
