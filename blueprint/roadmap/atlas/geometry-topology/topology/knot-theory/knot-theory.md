---
declaration: section
origin: cited
lean: MathlibExt.Topology.ChiralWanted.KnotTheory.exists_chiral_knot, MetaMathlibExt.oesper_weaving_three_determinant
statement: formalized
---

# Knot theory: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/index.html).

Embeddings of circles in three-space up to ambient isotopy: knot and link diagrams, chirality, slice knots, and geometric invariants such as ropelength, distortion and quadrisecants.

## Existence of a chiral knot

There exists an oriented smooth knot $K$ in $\mathbb{R}^3$
that is chiral: it is not ambient-isotopic, as an oriented knot, to its mirror image $r \circ K$,
where $r(x, y, z) = (x, y, -z)$ is the reflection through the $xy$-plane.

## Sources

- Classical; see https://en.wikipedia.org/wiki/Chirality_(mathematics) and https://en.wikipedia.org/wiki/Trefoil_knot. Problem `exists_chiral_knot` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Topology.ChiralWanted.KnotTheory.exists_chiral_knot` is written with `theorem_wanted` in [WantedExt/Topology/ChiralWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Topology/ChiralWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/index.html#exists-chiral-knot).

## Oesper's determinant formula for three-strand weaving knots

Let $k \ge 1$ be an integer,
let $F_i$ be the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$), let
$C_j = \sum_{i=1}^{j} (-1)^{i+1} F_i$ for $j \ge 0$, and let $M$ be the $3 \times 3$ integer
matrix with rows $(2, -1, 0)$, $(0, 0, 1)$ and $(-1, 0, 2)$. Then the absolute value of the
determinant of the $2 \times 2$ matrix obtained from $M^k - I$ by deleting its first row and
first column equals $-(C_{2k-2} + 1) C_{2k} + C_{2k-1}^2$.

Here $M$ is the base-word matrix of the spiral knot $S(3, k, (1, -1))$, which is the
three-strand weaving knot $W(k, 3)$, and the left-hand side is the determinant of this knot:
the cofactor minors of $M^k - I$ agree up to sign, so taking the absolute value gives the
nonnegative knot determinant.

## Sources

- Seong Ju Kim, Ryan Stees, and Laura Taalman, "Sequences of Spiral Knot Determinants", Journal of Integer Sequences 19 (2016), Article 16.1.4, lines 409-412: https://cs.uwaterloo.ca/journals/JIS/VOL19/Stees/stees4.tex The formula is attributed to L. Oesper, "p-colorings of weaving knots" (preprint).

Formalized by `MetaMathlibExt.oesper_weaving_three_determinant`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/OesperWeavingDeterminant.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/OesperWeavingDeterminant.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/index.html#oesper-weaving-three-determinant).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Knot theory](https://deicyde.github.io/atlas-lean/roadmap/Topology/knot-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/knot-theory)
