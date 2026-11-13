---
declaration: section
origin: cited
lean: MathlibExt.Geometry.EllipticBilliard602Wanted.conjecture, MathlibExt.Geometry.EllipticBilliard602Wanted.conjecture_holds, MathlibExt.Geometry.ScottishBook147Wanted.billiardUnfoldingDiagonalLemma
statement: formalized
---

# Mathematical billiards

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/mathematical-billiards/index.html).

## Elliptic billiard invariant $k_{602}$

Write $|XY|$ for the distance between points $X$
and $Y$ of the Euclidean plane. For every natural number $N$, all points $O, f_1, f_2$ of the
plane and all reals $a, a_c$ with $O = \frac{1}{2}(f_1 + f_2)$, $|f_1 f_2| < a$,
$|f_1 f_2| < a_c$ and $a_c < a$, there is a real number $C$ with the following property. Let
$P_0, P_1, P_2, \dots$ be points of the plane such that $|P_i f_1| + |P_i f_2| = a$ and
$P_{i+N} = P_i$ for every $i$, and such that for every $i < N$ the points $P_i$ and $P_{i+1}$
are distinct and the line $P_i P_{i+1}$ contains exactly one point $X$ with
$|X f_1| + |X f_2| = a_c$. For $i < N$ let $Q_{1,i}$ and $Q_{2,i}$ be points of the line
$P_i P_{i+1}$ closest to $f_1$ and to $f_2$ respectively. Then

$$\prod_{i\lt N} |f_1 Q_{1,i}| \cdot \prod_{i\lt N} |f_2 Q_{2,i}| = C.$$

In words: the vertices lie on the ellipse with foci $f_1, f_2$ and major axis $a$, every side
is tangent to the confocal caustic with major axis $a_c$, and $Q_{j,i}$ is the foot of the
perpendicular from $f_j$ to the $i$-th side.

## Sources

- [AMR-050-0031] Reznik, Garcia and Koiller, Eighty New Invariants of N-Periodics in the Elliptic Billiard (2021), Table row $k_{602}$, arXiv:2004.12497.

Formalized by `MathlibExt.Geometry.EllipticBilliard602Wanted.conjecture`, a definition declared in [WantedExt/Geometry/EllipticBilliard602Wanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/EllipticBilliard602Wanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/mathematical-billiards/index.html#conjecture).

## Bialy–Tabachnikov: $k_{602}$ is invariant

The elliptic billiard invariant $k_{602}$
conjecture holds. Write $|XY|$ for the distance between points $X$ and $Y$. For every natural
number $N$, all points $O, f_1, f_2$ of the Euclidean plane and all reals $a, a_c$ with
$O = \frac{1}{2}(f_1 + f_2)$, $|f_1 f_2| < a$, $|f_1 f_2| < a_c$ and $a_c < a$, there is a real
number $C$ with the following property. Let $P_0, P_1, P_2, \dots$ be points of the plane such
that $|P_i f_1| + |P_i f_2| = a$ and $P_{i+N} = P_i$ for every $i$, and such that for every
$i < N$ the points $P_i$ and $P_{i+1}$ are distinct and the line $P_i P_{i+1}$ contains exactly
one point $X$ with $|X f_1| + |X f_2| = a_c$. For $i < N$ let $Q_{1,i}$ and $Q_{2,i}$ be any
points of the line $P_i P_{i+1}$ closest to $f_1$ and to $f_2$ respectively. Then
$\prod_{i\lt N} |f_1 Q_{1,i}| \cdot \prod_{i\lt N} |f_2 Q_{2,i}| = C$.

Bialy and Tabachnikov (Lemma 4.2) show that for each side tangent to the confocal caustic with
semi-minor axis $b$ the two focal distances multiply to $b^2$, so the common value is $b^{2N}$.

## Sources

- M. Bialy, S. Tabachnikov, Dan Reznik's identities and more, European Journal of Mathematics (2020), arXiv:2001.08469, https://arxiv.org/abs/2001.08469.

Stated but not proved: `MathlibExt.Geometry.EllipticBilliard602Wanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Geometry/EllipticBilliard602Wanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/EllipticBilliard602Wanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/mathematical-billiards/index.html#conjecture-holds).

## Lattice step of the billiard unfolding in a rectangle

For a natural number $j$, let
$\varepsilon_j = 1$ if $j$ is odd and $\varepsilon_j = 0$ if $j$ is even. Let $a, b > 0$ be real
numbers with $a n = b m$ for some positive integers $m, n$. Then there are a real number $t > 0$
and natural numbers $k > 0$, $l > 0$ and $N$ such that $t = k a = l b$, $N + 2 = k + l$, $k$ and
$l$ are coprime, and the point $(\varepsilon_k a, \varepsilon_l b)$ is one of $(a, 0)$, $(0, b)$,
$(a, b)$.

In the billiard argument for the $a \times b$ rectangle, the unfolded diagonal from the
corner $(0, 0)$ first meets a corner of the tiling at $(t, t)$ (coprimality is the first-hit
condition), $N$ counts the reflections, and folding back yields the corner
$(\varepsilon_k a, \varepsilon_l b)$. This lemma covers only that lattice step; it does not
formalize the reflected trajectory and does not prove Problem 147.

## Sources

- H. Auerbach and S. Mazur, Problem 147 of the Scottish Book; the typescript labels the entry Theorem (Problem Mazur). Elementary unfolding argument for polygonal billiards, see e.g. S. Tabachnikov, Geometry and Billiards.

Stated but not proved: `MathlibExt.Geometry.ScottishBook147Wanted.billiardUnfoldingDiagonalLemma` is written with `theorem_wanted` in [WantedExt/Geometry/ScottishBook147Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/ScottishBook147Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/mathematical-billiards/index.html#billiard-unfolding-diagonal-lemma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mathematical billiards](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/circles-and-conics/mathematical-billiards/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/circles-and-conics/mathematical-billiards)
