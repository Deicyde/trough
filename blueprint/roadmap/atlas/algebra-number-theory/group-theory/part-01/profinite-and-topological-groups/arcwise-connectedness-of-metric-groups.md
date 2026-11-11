---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.ScottishBook160Part2Wanted.IsHausdorffConnected, MathlibExt.GroupTheory.ScottishBook160Part2Wanted.IsArcwiseConnected, MathlibExt.GroupTheory.ScottishBook160Part2Wanted.ScottishBookProblem160Part2Claim, MathlibExt.GroupTheory.ScottishBook160Part2Wanted.scottishBook160Part2_refuted
statement: formalized
---

# Arcwise connectedness of metric groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/arcwise-connectedness-of-metric-groups/index.html).

## Connectedness in the sense of Hausdorff

A topological space $G$ is connected in the
sense of Hausdorff when it is not the union of two disjoint nonempty closed subsets.

The empty space satisfies this condition.

Formalized by `MathlibExt.GroupTheory.ScottishBook160Part2Wanted.IsHausdorffConnected`, a definition declared in [WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/arcwise-connectedness-of-metric-groups/index.html#is-hausdorff-connected).

## Arcwise connected space

A topological space $G$ is arcwise connected when for any two
points $x, y \in G$ there is a continuous map $\gamma \colon \mathbb{R} \to G$ with
$\gamma(0) = x$ and $\gamma(1) = y$.

Restricting $\gamma$ to $[0, 1]$ gives a path from $x$ to $y$, and every such path extends
to $\mathbb{R}$, so this says that any two points are joined by a path; the path need not be
injective.

Formalized by `MathlibExt.GroupTheory.ScottishBook160Part2Wanted.IsArcwiseConnected`, a definition declared in [WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/arcwise-connectedness-of-metric-groups/index.html#is-arcwise-connected).

## Claim of Scottish Book Problem 160, part (2)

The claim that every metric group $G$
(a group with a metric for which multiplication and inversion are continuous) that is
connected in the sense of Hausdorff is arcwise connected.

Formalized by `MathlibExt.GroupTheory.ScottishBook160Part2Wanted.ScottishBookProblem160Part2Claim`, a definition declared in [WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/arcwise-connectedness-of-metric-groups/index.html#scottish-book-problem160-part2-claim).

## Connected metric groups need not be arcwise connected

The claim of part (2) of Scottish
Book Problem 160 is false: there is a metric group $G$ (a group with a metric for which
multiplication and inversion are continuous) that is connected in the sense of Hausdorff but
not arcwise connected, that is, there are points $x, y \in G$ such that no continuous map
$\gamma \colon \mathbb{R} \to G$ has $\gamma(0) = x$ and $\gamma(1) = y$.

The $p$-adic solenoid, the inverse limit of circles under $z \mapsto z^p$, is such a group:
it is a compact connected metrizable topological group that is not path connected.

## Sources

- Encyclopedia of Mathematics, "Solenoid" (inverse-limit construction with `fᵢ (z) = z ^ nᵢ`, a topological group, a one-dimensional continuum); E. Hewitt and K. A. Ross, Abstract Harmonic Analysis I (1979), cited there; solenoids are compact metrizable spaces that are connected but not path connected.

Stated but not proved: `MathlibExt.GroupTheory.ScottishBook160Part2Wanted.scottishBook160Part2_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/ScottishBook160Part2Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/arcwise-connectedness-of-metric-groups/index.html#scottish-book160-part2-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arcwise connectedness of metric groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/arcwise-connectedness-of-metric-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/arcwise-connectedness-of-metric-groups)
