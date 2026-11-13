---
declaration: section
origin: cited
lean: MathlibExt.Geometry.FourManifoldNotSmoothWanted.Geometry.four_manifold_not_smooth, MathlibExt.Geometry.Manifold.CollarNeighborhoodWanted.topological_collar_neighborhood_of_smooth_manifold_with_boundary, MathlibExt.Geometry.Manifold.HadamardGlobalInverseWanted.hadamard_caccioppoli_global_inverse, MathlibExt.Geometry.Manifold.HairyBallWanted.hairyBall_even_sphere_ambient, MathlibExt.Geometry.Manifold.TubularNeighborhoodWanted.tubular_smoothRetraction
statement: formalized
---

# Differential topology: its own results

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/index.html).

Smooth manifolds and smooth maps between them: immersions, submersions, transversality, Morse theory, neighbourhood theorems and smooth structures.

## A closed simply connected topological 4-manifold with no smooth structure

There
exists a compact, Hausdorff, simply connected topological space $M$ that admits an atlas of
charts modelled on $\mathbb{R}^4$, such that no atlas of charts on $M$ modelled on $\mathbb{R}^4$
makes $M$ a smooth ($C^\infty$) manifold.

## Sources

-. Problem `four_manifold_not_smooth` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.FourManifoldNotSmoothWanted.Geometry.four_manifold_not_smooth` is written with `theorem_wanted` in [WantedExt/Geometry/FourManifoldNotSmoothWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/FourManifoldNotSmoothWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/index.html#four-manifold-not-smooth).

## Collar neighborhood theorem (topological form)

Let $n \ge 1$ and let $M$ be a Hausdorff,
second-countable smooth ($C^\infty$) manifold with boundary modeled on the closed half-space
$\{x \in \mathbb{R}^n : x_1 \ge 0\}$, and let $\partial M$ be its boundary. Then there is an open
embedding $c : \partial M \times [0, 1) \to M$ such that $c(b, 0) = b$ for every $b \in \partial M$.

Proof: Local chart collars are glued by Brown's external-collar construction, following Hatcher,
*Algebraic Topology*, Proposition 3.42, and the locally finite extension of Connelly (1971).

## Sources

- M. Hirsch, Differential Topology, GTM 33; J. Lee, Introduction to Smooth Manifolds, 2nd ed.; Kosinski, Differential Manifolds; Lean states topological collar `IsOpenEmbedding` corollary for `EuclideanHalfSpace` model.

Formalized by `MathlibExt.Geometry.Manifold.CollarNeighborhoodWanted.topological_collar_neighborhood_of_smooth_manifold_with_boundary`, a theorem declared in [MathlibExt/Geometry/Manifold/CollarNeighborhood.lean, line 2766](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/CollarNeighborhood.lean#L2766). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/index.html#topological-collar-neighborhood-of-smoot).

## Hadamard–Caccioppoli global inverse theorem

Let $n \in \mathbb{N}$ and let
$f : \mathbb{R}^n \to \mathbb{R}^n$ be a proper map that is a $C^\infty$ local diffeomorphism.
Then $f$ is a global $C^\infty$ diffeomorphism: there is a $C^\infty$ diffeomorphism
$\Phi : \mathbb{R}^n \to \mathbb{R}^n$ whose underlying map is $f$.

## Sources

- J. Hadamard, Bull. Soc. Math. France 34 (1906) 71–84; R. Caccioppoli, Rend. Sem. Mat. Univ. Padova 3 (1932); F.-C. Plastock, Trans. Amer. Math. Soc. 200 (1974) extension to Banach spaces; J. Lee, Riemannian Manifolds? Lean states Euclidean `ℝⁿ = EuclideanSpace ℝ (Fin n)` specialization with `IsProperMap` and `IsLocalDiffeomorph` hypotheses.

Formalized by `MathlibExt.Geometry.Manifold.HadamardGlobalInverseWanted.hadamard_caccioppoli_global_inverse`, a theorem declared in [MathlibExt/Geometry/Manifold/HadamardGlobalInverse.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/HadamardGlobalInverse.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/index.html#hadamard-caccioppoli-global-inverse).

## Hairy ball theorem

Let $k \in \mathbb{N}$ and let $E$ be a real inner product space of
dimension $2k + 1$, with unit sphere $S = \{x \in E : \|x\| = 1\}$. If $f : S \to E$ is
continuous and $\langle f(x), x \rangle = 0$ for every $x \in S$, then $f(x) = 0$ for some
$x \in S$.

## Sources

- H. Poincaré proved the 2-sphere case in 1885 and L. E. J. Brouwer extended it to higher even-dimensional spheres in 1912; J. Milnor, Topology from the Differentiable Viewpoint hairy ball; Guillemin-Pollack, Differential Topology; Lean states even-sphere ambient finite-dimensional inner-product specialization via `inner = 0`.

Formalized by `MathlibExt.Geometry.Manifold.HairyBallWanted.hairyBall_even_sphere_ambient`, a theorem declared in [MathlibExt/Geometry/Manifold/HairyBall.lean, line 1298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/HairyBall.lean#L1298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/index.html#hairy-ball-even-sphere-ambient).

## Smooth retraction onto a closed embedded manifold in $\mathbb{R}^n$

Let $M$ be a Hausdorff,
second-countable smooth ($C^\infty$) manifold without boundary, modelled on a finite-dimensional
real normed space, and let $e \colon M \to \mathbb{R}^n$ be a smooth embedding (a $C^\infty$
immersion that is a topological embedding) whose image $e(M)$ is closed in $\mathbb{R}^n$. Then
there exist an open set $U \subseteq \mathbb{R}^n$ containing $e(M)$ and a $C^\infty$ map
$r \colon U \to M$ such that $r(e(x)) = x$ for every $x \in M$.

## Sources

- Tubular neighborhood theorem; M. Hirsch, Differential Topology; J. Lee, Introduction to Smooth Manifolds; Lean states smooth-retraction corollary for closed embedding into `EuclideanSpace ℝ (Fin n)` via `Opens`.

Formalized by `MathlibExt.Geometry.Manifold.TubularNeighborhoodWanted.tubular_smoothRetraction`, a theorem declared in [MathlibExt/Geometry/Manifold/TubularNeighborhood.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/TubularNeighborhood.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/index.html#tubular-smooth-retraction).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Differential topology](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/differential-topology)
