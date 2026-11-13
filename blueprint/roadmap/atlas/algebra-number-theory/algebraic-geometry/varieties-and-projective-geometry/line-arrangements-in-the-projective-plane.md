---
declaration: section
origin: cited
lean: Projectivization.eq_cross_iff, LineArrangement, LineArrangement.multiplicity, LineArrangement.singularPoints, LineArrangement.mem_singularPoints_iff_exists, LineArrangement.mem_singularPoints_iff, LineArrangement.multiplicity_le_card, LineArrangement.singularPoints_nonempty
statement: formalized
proof: formalized
---

# Line arrangements in the projective plane

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html).

## Two distinct lines meet in their cross product

Let $K$ be a field and let $v \ne w$ be
two distinct points of the projective plane $\mathbb{P}(K^3)$. Call two points orthogonal when
the dot product of representative vectors in $K^3$ vanishes, and let $v \times w$ be the point
spanned by the cross product of representatives of $v$ and $w$, which is nonzero since
$v \ne w$. Then a point $p$ equals $v \times w$ if and only if $p$ is orthogonal to both $v$
and $w$. Reading points as coordinate vectors of lines, this says that two distinct lines meet
exactly in their cross product, and dually that two distinct points lie on exactly one line.

Formalized by `Projectivization.eq_cross_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#eq-cross-iff).

## Line arrangement

A line arrangement in the projective plane over a field $K$ is a finite
set of at least two lines, each line recorded by its coordinate vector, a point of the dual
projective plane $\mathbb{P}(K^3)$.

A point $p$ lies on the line with coordinate vector $\ell$ when the dot product of
representatives of $p$ and $\ell$ vanishes.

Formalized by `LineArrangement`, a structure declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#line-arrangement).

## Multiplicity of a point in a line arrangement

Let $A$ be a line arrangement in the
projective plane over a field. The multiplicity $m_p$ of a point $p$ in $A$ is the number of
lines of $A$ through $p$, that is, of lines of $A$ whose coordinate vector has zero dot product
with a representative of $p$.

Formalized by `LineArrangement.multiplicity`, a definition declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#multiplicity).

## Singular points of a line arrangement

The singular points of a line arrangement $A$ in
the projective plane over a field form the finite set of intersection points of pairs of distinct
lines of $A$, where two distinct lines with coordinate vectors $\ell$ and $\ell'$ meet in the
point spanned by the cross product $\ell \times \ell'$ of their representatives.

Formalized by `LineArrangement.singularPoints`, a definition declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#singular-points).

## Singular points lie on two distinct lines

Let $A$ be a line arrangement in the projective
plane over a field. A point $p$ is a singular point of $A$ if and only if there are two distinct
lines of $A$ that both pass through $p$.

Formalized by `LineArrangement.mem_singularPoints_iff_exists`, a theorem declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#mem-singular-points-iff-exists).

## Singular points are the points of multiplicity at least two

Let $A$ be a line
arrangement in the projective plane over a field. A point $p$ is a singular point of $A$ if and
only if its multiplicity $m_p$ in $A$, the number of lines of $A$ through $p$, satisfies
$m_p \ge 2$.

Formalized by `LineArrangement.mem_singularPoints_iff`, a theorem declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#mem-singular-points-iff).

## Multiplicity is at most the number of lines

Let $A$ be an arrangement of $d$ lines in
the projective plane over a field. Every point $p$ has multiplicity $m_p \le d$ in $A$.

Formalized by `LineArrangement.multiplicity_le_card`, a theorem declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#multiplicity-le-card).

## Every line arrangement has a singular point

Every line arrangement in the projective
plane over a field has at least one singular point, since any two of its distinct lines meet.

Formalized by `LineArrangement.singularPoints_nonempty`, a theorem declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#singular-points-nonempty).

## Harbourne constant of a line arrangement

Let $A$ be an arrangement of $d$ lines in the
projective plane over a field, let $S$ be its set of singular points, with $s$ elements, and let
$m_p$ be the multiplicity of a point $p$ in $A$. The Harbourne constant of $A$ is the real number

$$H(A) = \frac{d^2 - \sum_{p \in S} m_p^2}{s}.$$

Every arrangement has a singular point, so $s \ge 1$. The number $H(A)$ is the self-intersection
of the strict transform of the arrangement on the blow-up of its singular points, divided by $s$.

Formalized by `LineArrangement.hConstant`, a definition declared in [MathlibExt/AlgebraicGeometry/LineArrangement.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/AlgebraicGeometry/LineArrangement.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html#h-constant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Line arrangements in the projective plane](https://deicyde.github.io/atlas-lean/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/AlgebraicGeometry/varieties-and-projective-geometry/line-arrangements-in-the-projective-plane)
