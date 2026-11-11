---
declaration: section
origin: cited
lean: ContDiff.exists_localGraph_of_surjective_fderiv, MathlibExt.Geometry.Manifold.LocalGraphWanted.regularLevelSet_localGraph, ContDiff.isImmersion_graph, MathlibExt.Geometry.Manifold.LocalParametrizationWanted.regularLevelSet_localParametrization
statement: formalized
proof: formalized
---

# Regular level sets

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/regular-level-sets/index.html).

## Local graph form of a level set near a regular point

Let $E$, $G$ and $F$ be
finite-dimensional real normed spaces with $\dim E = \dim G + \dim F$, let $f \colon E \to F$ be
a $C^1$ map and let $x_0 \in E$ be a point at which the derivative $Df(x_0)$ is surjective. Then
there exist a continuous linear isomorphism $e \colon E \to G \times F$, a neighbourhood $U$ in
$G$ of the first component of $e(x_0)$, a map $g \colon G \to F$ that is $C^1$ on $U$, and a
neighbourhood $V$ of $x_0$ such that a point $x \in V$ satisfies $f(x) = f(x_0)$ if and only if
$e(x) = (u, g(u))$ for some $u \in U$.

Formalized by `ContDiff.exists_localGraph_of_surjective_fderiv`, a theorem declared in [MathlibExt/Geometry/Manifold/LocalGraph.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/LocalGraph.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/regular-level-sets/index.html#exists-local-graph-of-surjective-fderiv).

## Regular level sets are locally graphs

Let $f \colon \mathbb{R}^{k+m} \to \mathbb{R}^m$ be a
$C^1$ map and let $x_0 \in \mathbb{R}^{k+m}$ be a point at which the derivative $Df(x_0)$ is
surjective. Then there exist a linear isomorphism
$e \colon \mathbb{R}^{k+m} \to \mathbb{R}^k \times \mathbb{R}^m$, a neighbourhood $U$ in
$\mathbb{R}^k$ of the first component of $e(x_0)$, a map $g \colon \mathbb{R}^k \to \mathbb{R}^m$
that is $C^1$ on $U$, and a neighbourhood $V$ of $x_0$ such that a point $x \in V$ satisfies
$f(x) = f(x_0)$ if and only if $e(x) = (u, g(u))$ for some $u \in U$.

Proof: A projection onto the derivative kernel supplies adapted linear coordinates. The
product-space implicit function theorem then identifies the level set with a local `C¹` graph
(https://en.wikipedia.org/wiki/Implicit_function_theorem).

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4 (rank theorem).

Formalized by `MathlibExt.Geometry.Manifold.LocalGraphWanted.regularLevelSet_localGraph`, a theorem declared in [MathlibExt/Geometry/Manifold/LocalGraph.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/LocalGraph.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/regular-level-sets/index.html#regular-level-set-local-graph).

## Graph maps are immersions

Let $E$ and $F$ be real normed spaces, let
$n \in \mathbb{N} \cup \{\infty, \omega\}$ and let $h \colon E \to F$ be a $C^n$ map. Then the
graph map $x \mapsto (x, h(x))$ from $E$ to $E \times F$ is a $C^n$ immersion, where $E$ and
$E \times F$ are regarded as manifolds modelled on themselves.

Formalized by `ContDiff.isImmersion_graph`, a theorem declared in [MathlibExt/Geometry/Manifold/LocalParametrization.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/LocalParametrization.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/regular-level-sets/index.html#is-immersion-graph).

## Regular level sets are locally parametrized by immersions

Let
$f \colon \mathbb{R}^{k+m} \to \mathbb{R}^m$ be a $C^1$ map and let $x_0 \in \mathbb{R}^{k+m}$ be a
point at which the derivative $Df(x_0)$ is surjective. Then there exist an open set
$U \subseteq \mathbb{R}^k$, a point $u_0 \in U$, a map $\varphi \colon \mathbb{R}^k \to
\mathbb{R}^{k+m}$ that is $C^1$ and a $C^1$ immersion on all of $\mathbb{R}^k$, and a
neighbourhood $V$ of $x_0$ such that $\varphi(u_0) = x_0$ and
$\varphi(U \cap \varphi^{-1}(V)) = V \cap f^{-1}(f(x_0))$.

Proof: Apply the implicit function theorem in adapted linear coordinates, then use a smooth bump
to extend the local graphing function globally. A shear chart makes its graph map an immersion.

## Sources

- J. Lee, Introduction to Smooth Manifolds, 2nd ed., Ch. 4 (rank theorem).

Formalized by `MathlibExt.Geometry.Manifold.LocalParametrizationWanted.regularLevelSet_localParametrization`, a theorem declared in [MathlibExt/Geometry/Manifold/LocalParametrization.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Manifold/LocalParametrization.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/regular-level-sets/index.html#regular-level-set-local-parametrization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular level sets](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/regular-level-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/differential-topology/regular-level-sets)
