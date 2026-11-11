---
declaration: section
origin: cited
lean: MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.IsConvexBody, MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.IsHyperplane, MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.conjecture, MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.conjecture_holds
statement: formalized
---

# Hyperplane slicing problem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hyperplane-slicing-problem/index.html).

## Convex bodies in $\mathbb{R}^n$

A set $K$ in the $n$-dimensional Euclidean space
$\mathbb{R}^n$ is a convex body when it is convex, compact and has nonempty interior.

## Sources

- `OWR-12337-001` (DOI 10.4171/owr/2013/09): "convex body `K ⊆ ℝⁿ`".

Formalized by `MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.IsConvexBody`, a definition declared in [WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hyperplane-slicing-problem/index.html#is-convex-body).

## Hyperplanes in $\mathbb{R}^n$

A set $H$ in the $n$-dimensional Euclidean space
$\mathbb{R}^n$ is a hyperplane when $H = \{x \in \mathbb{R}^n : f(x) = t\}$ for some nonzero
linear functional $f \colon \mathbb{R}^n \to \mathbb{R}$ and some $t \in \mathbb{R}$.

## Sources

- `OWR-12337-001` (DOI 10.4171/owr/2013/09): "hyperplane section".

Formalized by `MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.IsHyperplane`, a definition declared in [WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hyperplane-slicing-problem/index.html#is-hyperplane).

## Hyperplane slicing conjecture

The statement that there is a constant $c > 0$ such that
for every $n \ge 1$ and every convex body $K \subseteq \mathbb{R}^n$ (a convex compact set with
nonempty interior) of Lebesgue volume $1$ there exist a hyperplane $H \subseteq \mathbb{R}^n$ (a
set $\{x : f(x) = t\}$ for a nonzero linear functional $f$ on $\mathbb{R}^n$ and some
$t \in \mathbb{R}$) and an isometry $\varphi \colon \mathbb{R}^{n-1} \to \mathbb{R}^n$ with image
$H$ such that the $(n-1)$-dimensional Lebesgue volume of $\varphi^{-1}(K \cap H)$ is at least $c$.

## Sources

- `OWR-12337-001` (DOI 10.4171/owr/2013/09), where it is posed as an open problem; it has since been resolved.

Formalized by `MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.conjecture`, a definition declared in [WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hyperplane-slicing-problem/index.html#conjecture).

## Hyperplane slicing theorem

There is a constant $c > 0$ such that for every $n \ge 1$ and
every convex body $K \subseteq \mathbb{R}^n$ (a convex compact set with nonempty interior) of
Lebesgue volume $1$ there exist a hyperplane $H \subseteq \mathbb{R}^n$ (a set
$\{x : f(x) = t\}$ for a nonzero linear functional $f$ on $\mathbb{R}^n$ and some
$t \in \mathbb{R}$) and an isometry $\varphi \colon \mathbb{R}^{n-1} \to \mathbb{R}^n$ with image
$H$ such that the $(n-1)$-dimensional Lebesgue volume of $\varphi^{-1}(K \cap H)$ is at least $c$.

This is Bourgain's slicing conjecture, proved by Klartag and Lehec building on Guan's bound
(Theorem 1.1); equivalently, the isotropic constant of convex bodies is bounded by a universal
constant.

## Sources

- B. Klartag, J. Lehec, Affirmative resolution of Bourgain's slicing problem using Guan's bound, Geometric and Functional Analysis (2025), arXiv:2412.15044, https://arxiv.org/abs/2412.15044.

Stated but not proved: `MathlibExt.Geometry.HyperplaneSlicingUniversalWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Geometry/HyperplaneSlicingUniversalWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hyperplane-slicing-problem/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperplane slicing problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/hyperplane-slicing-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/convex-geometry/hyperplane-slicing-problem)
