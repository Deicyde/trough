---
declaration: section
origin: cited
lean: MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.axisAlignedRectangleCorners, MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.rectangleCorners, MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.IsInscribedRectangle, MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.aspectRatio, MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.X, MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.theorem_1, MathlibExt.Geometry.RectangularPegProblemWanted.RectangularPegProblem.R, MathlibExt.Geometry.RectangularPegProblemWanted.RectangularPegProblem.theorem_1
statement: formalized
---

# Inscribed rectangle problem

8 results, 6 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html).

## Axis-aligned rectangle

For points $a = (a_1, a_2)$ and $b = (b_1, b_2)$ of $\mathbb{R}^2$,
the axis-aligned (possibly degenerate) rectangle with opposite corners $a$ and $b$ is the list of
its four vertices $(a_1, a_2)$, $(b_1, a_2)$, $(b_1, b_2)$, $(a_1, b_2)$, in this order.

Formalized by `MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.axisAlignedRectangleCorners`, a definition declared in [WantedExt/Geometry/InscribedRectanglesWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/InscribedRectanglesWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#axis-aligned-rectangle-corners).

## Rotated rectangle

For points $a, b \in \mathbb{R}^2$ and an angle $\theta \in \mathbb{R}$,
the rotated rectangle given by $a$, $b$ and $\theta$ is the list of four points obtained by applying
the rotation $(x, y) \mapsto (x \cos\theta + y \sin\theta, -x \sin\theta + y \cos\theta)$ about the
origin to each vertex, in order, of the axis-aligned rectangle with opposite corners $a$ and $b$.

Formalized by `MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.rectangleCorners`, a definition declared in [WantedExt/Geometry/InscribedRectanglesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/InscribedRectanglesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#rectangle-corners).

## Inscribed rectangle

Let $\gamma$ be a map from the unit circle to $\mathbb{R}^2$. For
points $a, b \in \mathbb{R}^2$ and an angle $\theta \in \mathbb{R}$, the rotated rectangle given by
$a$, $b$ and $\theta$ is inscribed in $\gamma$ when its four vertices are pairwise distinct and
each lies in the image of $\gamma$.

The map $\gamma$ need not be smooth, or even a Jordan curve, for this definition.

Formalized by `MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.IsInscribedRectangle`, a definition declared in [WantedExt/Geometry/InscribedRectanglesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/InscribedRectanglesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#is-inscribed-rectangle).

## Aspect ratio

For points $a = (a_1, a_2)$ and $b = (b_1, b_2)$ of $\mathbb{R}^2$, the
aspect ratio of the axis-aligned rectangle with opposite corners $a$ and $b$ is
$|a_1 - b_1| / |a_2 - b_2|$, the ratio of its horizontal side length to its vertical side
length; it is $0$ when $a_2 = b_2$.

Formalized by `MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.aspectRatio`, a definition declared in [WantedExt/Geometry/InscribedRectanglesWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/InscribedRectanglesWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#aspect-ratio).

## Aspect-ratio parameters of inscribed rectangles

For a map $\gamma$ from the unit circle
to $\mathbb{R}^2$, let $X(\gamma)$ be the set of all $r \in [0, 1]$ for which there are points
$a, b \in \mathbb{R}^2$ and an angle $\theta \in \mathbb{R}$ such that the rotated rectangle given
by $a$, $b$ and $\theta$ is inscribed in $\gamma$ and the axis-aligned rectangle with opposite
corners $a$ and $b$ has aspect ratio $\tan(r\pi/4)$.

Formalized by `MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.X`, a definition declared in [WantedExt/Geometry/InscribedRectanglesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/InscribedRectanglesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#x).

## Hugelmeyer's theorem on aspect ratios of inscribed rectangles

Let $\gamma$ be a smooth Jordan
curve, that is, a map from the unit circle to $\mathbb{R}^2$ that is a $C^\infty$ immersion and a
topological embedding, and let $X$ be the set of all $r \in [0, 1]$ such that some rectangle
inscribed in $\gamma$ has aspect ratio $\tan(r\pi/4)$. Then the Lebesgue measure of $X$ is at
least $1/3$.

## Sources

- C. Hugelmeyer, `Inscribed rectangles in a smooth Jordan curve attain at least one third of all aspect ratios`, Annals of Math, 194 (2) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_inscribed_rectangles` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.InscribedRectanglesWanted.InscribedRectangles.theorem_1` is written with `theorem_wanted` in [WantedExt/Geometry/InscribedRectanglesWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/InscribedRectanglesWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#theorem-1).

## Rotated rectangle with given opposite corners

For $z, w \in \mathbb{C}$ and an angle
$\theta$, $R(z, w, \theta)$ is the list of four points $z e^{i\theta}$,
$(\operatorname{Re} w + i \operatorname{Im} z) e^{i\theta}$, $w e^{i\theta}$,
$(\operatorname{Re} z + i \operatorname{Im} w) e^{i\theta}$: the vertices, in order, of the
axis-parallel rectangle with opposite corners $z$ and $w$, rotated about the origin by $\theta$.
The rectangle is degenerate when $z$ and $w$ have the same real part or the same imaginary
part.

Formalized by `MathlibExt.Geometry.RectangularPegProblemWanted.RectangularPegProblem.R`, a definition declared in [WantedExt/Geometry/RectangularPegProblemWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/RectangularPegProblemWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#r).

## Rectangular peg theorem (Greene–Lobb)

Let $\gamma : S^1 \to \mathbb{C}$ be a $C^\infty$
embedding of the unit circle (a smooth Jordan curve in the plane). For $z, w \in \mathbb{C}$ and
an angle $\theta$, write $R(z, w, \theta)$ for the list of the four points $z e^{i\theta}$,
$(\operatorname{Re} w + i \operatorname{Im} z) e^{i\theta}$, $w e^{i\theta}$,
$(\operatorname{Re} z + i \operatorname{Im} w) e^{i\theta}$, in this order: the vertices of the
(possibly degenerate) axis-parallel rectangle with opposite corners $z$ and $w$, rotated about
the origin by $\theta$. Then for all $z$, $w$, $\theta$ there exist $z'$, $w'$, $\theta'$ such
that $R(z, w, \theta)$ is similar to $R(z', w', \theta')$, meaning that for some real $r > 0$
the distance between the $i$-th and $j$-th vertices of $R(z, w, \theta)$ is $r$ times the
distance between the $i$-th and $j$-th vertices of $R(z', w', \theta')$ for all $i, j$, and all
four vertices of $R(z', w', \theta')$ lie on $\gamma$.

## Sources

- J. E. Greene and A. Lobb, `The rectangular peg problem`, Annals of Math, 194 (2) 2021. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_rectangular_peg_problem` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Geometry.RectangularPegProblemWanted.RectangularPegProblem.theorem_1` is written with `theorem_wanted` in [WantedExt/Geometry/RectangularPegProblemWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Geometry/RectangularPegProblemWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html#theorem-1-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inscribed rectangle problem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/curves-and-surfaces/inscribed-rectangle-problem)
