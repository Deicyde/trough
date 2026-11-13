---
declaration: section
origin: cited
lean: MathlibExt.Geometry.Convex.ColorfulCaratheodoryWanted.colorful_caratheodory_finrank, MathlibExt.Geometry.Convex.ColorfulCaratheodoryWanted.colorful_caratheodory, MathlibExt.Geometry.Convex.ColorfulCaratheodoryWanted.exists_colorful_mem_convexHull
statement: formalized
proof: formalized
---

# Colorful Carathéodory theorem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/colorful-carath-odory-theorem/index.html).

## Colorful Carathéodory theorem in finite-dimensional inner product spaces

Let $V$ be a
finite-dimensional real inner product space of dimension $n$, and let $S_0, \dots, S_n$ be
finite subsets of $V$ such that $0$ lies in the convex hull of each $S_l$. Then there are
points $t_0 \in S_0, \dots, t_n \in S_n$ such that $0$ lies in the convex hull of
$\{t_0, \dots, t_n\}$.

## Sources

- I. Barany, Discrete Math. 40 (1982), 141-152, DOI 10.1016/0012-365X(82)90115-7.

Formalized by `MathlibExt.Geometry.Convex.ColorfulCaratheodoryWanted.colorful_caratheodory_finrank`, a theorem declared in [MathlibExt/Geometry/Convex/ColorfulCaratheodory.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/ColorfulCaratheodory.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/colorful-carath-odory-theorem/index.html#colorful-caratheodory-finrank).

## Colorful Carathéodory theorem for finite sets

Let $d \ge 0$ and let $S_0, \dots, S_d$ be
finite subsets of the Euclidean space $\mathbb{R}^d$ such that the origin lies in the convex hull
of each $S_i$. Then there are points $c_0 \in S_0, \dots, c_d \in S_d$ such that the origin lies
in the convex hull of $\{c_0, \dots, c_d\}$.

## Sources

- I. Barany, Discrete Math. 40 (1982), 141-152, DOI 10.1016/0012-365X(82)90115-7.

Formalized by `MathlibExt.Geometry.Convex.ColorfulCaratheodoryWanted.colorful_caratheodory`, a theorem declared in [MathlibExt/Geometry/Convex/ColorfulCaratheodory.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/ColorfulCaratheodory.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/colorful-carath-odory-theorem/index.html#colorful-caratheodory).

## Colorful Carathéodory theorem

Let $d \ge 0$ and let $S_0, \dots, S_d$ be subsets of the
Euclidean space $\mathbb{R}^d$ such that the origin lies in the convex hull of each $S_i$. Then
there are points $c_0 \in S_0, \dots, c_d \in S_d$ such that the origin lies in the convex hull of
$\{c_0, \dots, c_d\}$.

## Sources

- I. Barany, Discrete Math. 40 (1982), 141-152, DOI 10.1016/0012-365X(82)90115-7.

Formalized by `MathlibExt.Geometry.Convex.ColorfulCaratheodoryWanted.exists_colorful_mem_convexHull`, a theorem declared in [MathlibExt/Geometry/Convex/ColorfulCaratheodory.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Convex/ColorfulCaratheodory.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/colorful-carath-odory-theorem/index.html#exists-colorful-mem-convex-hull).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Colorful Carathéodory theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/convex-geometry/colorful-carath-odory-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/convex-geometry/colorful-carath-odory-theorem)
