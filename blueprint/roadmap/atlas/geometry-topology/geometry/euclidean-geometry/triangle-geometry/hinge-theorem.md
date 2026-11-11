---
declaration: section
origin: cited
lean: MetaMathlibExt.hinge_theorem_of_inner_lt, MetaMathlibExt.hinge_theorem
statement: formalized
proof: formalized
---

# Hinge theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/hinge-theorem/index.html).

## Hinge theorem in inner product spaces

Let $V$ be a real inner product space and let
$A, B, C, D, E, F \in V$. If $\|B - A\| = \|E - D\|$, $\|C - A\| = \|F - D\|$ and
$\langle B - A, C - A \rangle < \langle E - D, F - D \rangle$, then $\|F - E\| < \|C - B\|$.

Proof: Expand both squared opposite sides by the law of cosines and compare them.

## Sources

- Euclid's *Elements*, Book I, Proposition 24.

Formalized by `MetaMathlibExt.hinge_theorem_of_inner_lt`, a theorem declared in [MathlibExt/Geometry/Euclidean/Hinge.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Hinge.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/hinge-theorem/index.html#hinge-theorem-of-inner-lt).

## Hinge theorem

Let $A, B, C$ and $D, E, F$ be two triples of pairwise distinct points of
the Euclidean plane $\mathbb{R}^2$ forming nondegenerate triangles: $C - A$ is not a real
multiple of $B - A$, and $F - D$ is not a real multiple of $E - D$. Write $XY$ for the distance
between points $X$ and $Y$. If $AB = DE$, $AC = DF$ and
$\langle B - A, C - A \rangle < \langle E - D, F - D \rangle$, that is, the angle at $A$ is
larger than the angle at $D$, then $EF < BC$.

Proof: The vector law of cosines compares the squared opposite sides, following Euclid's
*Elements*, Book I, Proposition 24.

## Sources

- Euclid's Elements, Book I, Proposition 24 (https://mathcs.clarku.edu/~djoyce/elements/bookI/propI24.html); see also https://en.wikipedia.org/wiki/Hinge_theorem.

Formalized by `MetaMathlibExt.hinge_theorem`, a theorem declared in [MathlibExt/Geometry/Euclidean/Hinge.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Geometry/Euclidean/Hinge.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/hinge-theorem/index.html#hinge-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hinge theorem](https://deicyde.github.io/atlas-lean/roadmap/Geometry/euclidean-geometry/triangle-geometry/hinge-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Geometry/euclidean-geometry/triangle-geometry/hinge-theorem)
