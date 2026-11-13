---
declaration: section
origin: cited
lean: MetaMathlibExt.napoleon_theorem_general, MetaMathlibExt.napoleon_theorem
statement: formalized
proof: formalized
---

# Napoleon's theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/napoleon-s-theorem/index.html).

## Napoleon's theorem, general form

Let $A$, $B$, $C$, $A_2$, $B_2$, $C_2$ be points of the
Euclidean plane $\mathbb{R}^2$ with $|BA_2| = |CA_2| = |BC|$, $|CB_2| = |AB_2| = |CA|$ and
$|AC_2| = |BC_2| = |AB|$, such that $A_2$ and $A$ lie strictly on opposite sides of the line
$BC$, $B_2$ and $B$ lie strictly on opposite sides of the line $CA$, and $C_2$ and $C$ lie
strictly on opposite sides of the line $AB$. Let $G_1 = \frac{1}{3}(B + C + A_2)$,
$G_2 = \frac{1}{3}(C + A + B_2)$ and $G_3 = \frac{1}{3}(A + B + C_2)$. Then
$|G_1G_2| = |G_2G_3| = |G_3G_1| > 0$.

Thus the centroids $G_1$, $G_2$, $G_3$ of the equilateral triangles erected outward on the sides
of $ABC$ form a nondegenerate equilateral triangle; the hypotheses force $A$, $B$, $C$ to be
non-collinear. Opposite sides are expressed by signed areas, for instance
$((C - B) \times (A - B)) \, ((C - B) \times (A_2 - B)) < 0$, where
$(x, y) \times (x', y') = x y' - y x'$.

Formalized by `MetaMathlibExt.napoleon_theorem_general`, a theorem declared in [MathlibExt/Geometry/Euclidean/NapoleonTheorem.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/NapoleonTheorem.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/napoleon-s-theorem/index.html#napoleon-theorem-general).

## Napoleon's theorem

Let $A$, $B$, $C$ be pairwise distinct, non-collinear points of the
Euclidean plane $\mathbb{R}^2$, and let $A_2$, $B_2$, $C_2$ be points with
$|BA_2| = |CA_2| = |BC|$, $|CB_2| = |AB_2| = |CA|$ and $|AC_2| = |BC_2| = |AB|$, such that $A_2$
and $A$ lie strictly on opposite sides of the line $BC$, $B_2$ and $B$ lie strictly on opposite
sides of the line $CA$, and $C_2$ and $C$ lie strictly on opposite sides of the line $AB$. Let
$G_1 = \frac{1}{3}(B + C + A_2)$, $G_2 = \frac{1}{3}(C + A + B_2)$ and
$G_3 = \frac{1}{3}(A + B + C_2)$. Then $|G_1G_2| = |G_2G_3| = |G_3G_1|$.

That is, the centroids of the equilateral triangles erected outward on the sides of $ABC$ are
pairwise equidistant. Non-collinearity is stated as $(B - A) \times (C - A) \ne 0$ and opposite
sides by signed areas, for instance $((C - B) \times (A - B)) \, ((C - B) \times (A_2 - B)) < 0$,
where $(x, y) \times (x', y') = x y' - y x'$.

## Sources

- https://en.wikipedia.org/wiki/Napoleon%27s_theorem (statement id `napoleon-s1`; raw: "Outer equilateral-triangle centers on any triangle form an equilateral triangle."). It follows from `napoleon_theorem_general`, which also shows the common distance is positive; the hypotheses `A ≠ B`, `B ≠ C`, `C ≠ A` and nondegeneracy are unused and keep the source's shape.

Formalized by `MetaMathlibExt.napoleon_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/NapoleonTheorem.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Geometry/Euclidean/NapoleonTheorem.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/napoleon-s-theorem/index.html#napoleon-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Napoleon's theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/napoleon-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/napoleon-s-theorem)
