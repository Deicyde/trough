---
declaration: section
origin: cited
lean: MetaMathlibExt.spherical_law_of_cosines_general, MetaMathlibExt.spherical_law_of_cosines
statement: formalized
proof: formalized
---

# Spherical law of cosines

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/spherical-law-of-cosines/index.html).

## Spherical law of cosines, general form

Write $x \cdot y = \sum_{i=1}^{3} x_i y_i$ for the
dot product and $\lVert x \rVert = \sqrt{x \cdot x}$ for the Euclidean norm on $\mathbb{R}^3$. Let
$u, v, w \in \mathbb{R}^3$ be unit vectors and let $a, b, c, C$ be real numbers with $0 < a < \pi$
and $0 < b < \pi$. Suppose that $v \cdot w = \cos a$, $u \cdot w = \cos b$, $u \cdot v = \cos c$
and

$$
\cos C = \frac{u \cdot v - (u \cdot w)(v \cdot w)}
{\lVert u - (u \cdot w)\, w \rVert \, \lVert v - (v \cdot w)\, w \rVert}.
$$

Then $\cos c = \cos a \cos b + \sin a \sin b \cos C$.

Only $a$ and $b$ need to lie in $(0, \pi)$: $c$ and $C$ enter only through their cosines. The
quotient above is the cosine of the angle at $w$ between the great-circle arcs from $w$ to $u$
and from $w$ to $v$.

Formalized by `MetaMathlibExt.spherical_law_of_cosines_general`, a theorem declared in [MathlibExt/Geometry/Spherical/SphericalLawOfCosines.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Spherical/SphericalLawOfCosines.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/spherical-law-of-cosines/index.html#spherical-law-of-cosines-general).

## Spherical law of cosines

Write $x \cdot y = \sum_{i=1}^{3} x_i y_i$ for the dot product
and $\lVert x \rVert = \sqrt{x \cdot x}$ for the Euclidean norm on $\mathbb{R}^3$. Let
$u, v, w \in \mathbb{R}^3$ be unit vectors and let $a, b, c, C$ be real numbers, each strictly
between $0$ and $\pi$. Suppose that $v \cdot w = \cos a$, $u \cdot w = \cos b$,
$u \cdot v = \cos c$ and

$$
\cos C = \frac{u \cdot v - (u \cdot w)(v \cdot w)}
{\lVert u - (u \cdot w)\, w \rVert \, \lVert v - (v \cdot w)\, w \rVert}.
$$

Then $\cos c = \cos a \cos b + \sin a \sin b \cos C$.

Geometrically, $u$, $v$, $w$ are the vertices of a spherical triangle on the unit sphere, $a$,
$b$, $c$ are the lengths of the sides opposite $u$, $v$, $w$, and $C$ is the angle at $w$,
opposite the side $c$.

## Sources

- https://en.wikipedia.org/wiki/Spherical_law_of_cosines. It follows from `spherical_law_of_cosines_general`; the hypotheses `hc` and `hC` are unused and keep the source's shape.

Formalized by `MetaMathlibExt.spherical_law_of_cosines`, a theorem declared in [MathlibExt/Geometry/Spherical/SphericalLawOfCosines.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Spherical/SphericalLawOfCosines.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/spherical-law-of-cosines/index.html#spherical-law-of-cosines).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spherical law of cosines](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/solid-and-spherical/spherical-law-of-cosines/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/solid-and-spherical/spherical-law-of-cosines)
