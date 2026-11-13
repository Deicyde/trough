---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Euclidean.BeckmanQuarlesWanted.beckman_quarles
statement: formalized
proof: formalized
---

# Isometries and crystallographic groups: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/index.html).

Distance-preserving maps of Euclidean space, their classification, and discrete symmetry groups such as wallpaper and space groups.

## Beckman–Quarles theorem

Let $n \ge 2$ and let $f : \mathbb{R}^n \to \mathbb{R}^n$ be a map of
$n$-dimensional real Euclidean space such that $\lVert f(x) - f(y) \rVert = 1$ whenever
$\lVert x - y \rVert = 1$. Then $f$ is an isometry, that is,
$\lVert f(x) - f(y) \rVert = \lVert x - y \rVert$ for all $x, y \in \mathbb{R}^n$.

Surjectivity of $f$ is neither assumed nor concluded.

## Sources

- F. S. Beckman and D. A. Quarles Jr., On isometries of Euclidean spaces, Proc. Amer. Math. Soc. 4 (1953) 810–815 original theorem; standard formulation for `ℝ^n, n ≥ 2`.

Formalized by `MathlibExt.Geometry.Euclidean.BeckmanQuarlesWanted.beckman_quarles`, a theorem declared in [MathlibExt/Geometry/Euclidean/BeckmanQuarles.lean, line 2234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/BeckmanQuarles.lean#L2234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/index.html#beckman-quarles).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Isometries and crystallographic groups](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/isometries-and-symmetry)
