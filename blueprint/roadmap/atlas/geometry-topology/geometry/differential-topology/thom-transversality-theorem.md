---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Manifold.ThomTransversalityWanted.thom_transversality_uniform_approx_regular_value_zero, MathlibExt.Geometry.Manifold.ThomTransversalityWanted.thom_transversality_compact_source_uniform_approx_regular_value_zero
statement: formalized
proof: formalized
---

# Thom transversality theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/thom-transversality-theorem/index.html).

## Approximation by maps having zero as a regular value

Let $M$ be a Hausdorff,
second-countable smooth manifold without boundary modelled on a finite-dimensional real normed
space, let $f : M \to \mathbb{R}^n$ be $C^\infty$, and let $\varepsilon > 0$. Then there is a
$C^\infty$ map $g : M \to \mathbb{R}^n$ such that $\lVert f(x) - g(x) \rVert < \varepsilon$ for
every $x \in M$ (Euclidean norm) and $0$ is a regular value of $g$, that is, the manifold
derivative of $g$ at $x$ is surjective for every $x \in M$ with $g(x) = 0$.

No compactness is needed.

Formalized by `MathlibExt.Geometry.Manifold.ThomTransversalityWanted.thom_transversality_uniform_approx_regular_value_zero`, a theorem declared in [MathlibExt/Geometry/Manifold/ThomTransversality.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ThomTransversality.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/thom-transversality-theorem/index.html#thom-transversality-uniform-approx-regul).

## Approximation by maps having zero as a regular value, compact case

Let $M$ be a compact,
Hausdorff, second-countable smooth manifold without boundary modelled on a finite-dimensional real
normed space, let $f : M \to \mathbb{R}^n$ be $C^\infty$, and let $\varepsilon > 0$. Then there is
a $C^\infty$ map $g : M \to \mathbb{R}^n$ such that $\lVert f(x) - g(x) \rVert < \varepsilon$ for
every $x \in M$ (Euclidean norm) and $0$ is a regular value of $g$, that is, the manifold
derivative of $g$ at $x$ is surjective for every $x \in M$ with $g(x) = 0$.

## Sources

- R. Thom, Comment. Math. Helv. 28 (1954) 17–86 transversality; M. Hirsch, Differential Topology; Guillemin-Pollack, Differential Topology; J. Lee, ISMs; Lean states compact-source uniform-approx regular-value-zero corollary.

Formalized by `MathlibExt.Geometry.Manifold.ThomTransversalityWanted.thom_transversality_compact_source_uniform_approx_regular_value_zero`, a theorem declared in [MathlibExt/Geometry/Manifold/ThomTransversality.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Manifold/ThomTransversality.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/thom-transversality-theorem/index.html#thom-transversality-compact-source-unifo).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Thom transversality theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/differential-topology/thom-transversality-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/differential-topology/thom-transversality-theorem)
