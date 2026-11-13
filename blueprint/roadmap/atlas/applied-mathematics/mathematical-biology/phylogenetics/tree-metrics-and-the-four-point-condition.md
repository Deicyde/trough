---
declaration: section
origin: cited
lean: MathlibExt.Biology.Phylogenetics.Buneman.IsTreeMetric, MathlibExt.Biology.Phylogenetics.Buneman.FourPointCondition, MathlibExt.Biology.Phylogenetics.Buneman.IsTreeMetric.fourPointCondition, MathlibExt.Biology.Phylogenetics.Buneman.isTreeMetric_of_fourPointCondition, MathlibExt.Biology.Phylogenetics.Buneman.isTreeMetric_iff_fourPointCondition
statement: formalized
proof: formalized
---

# Tree metrics and the four-point condition

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition/index.html).

## Tree metric

`d` is a **tree metric**: there are a finite tree `G` on a vertex type `V`, positive edge
lengths `w`, and a placement `ι` of the taxa on vertices such that `d x y` is the total length
of the (unique) path from `ι x` to `ι y`.

Formalized by `MathlibExt.Biology.Phylogenetics.Buneman.IsTreeMetric`, a definition declared in [MathlibExt/Biology/Phylogenetics/Buneman.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/Buneman.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition/index.html#is-tree-metric).

## Four-point condition

The **four-point condition**: `d x y + d z t ≤ max (d x z + d y t) (d x t + d y z)`.

Formalized by `MathlibExt.Biology.Phylogenetics.Buneman.FourPointCondition`, a definition declared in [MathlibExt/Biology/Phylogenetics/Buneman.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/Buneman.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition/index.html#four-point-condition).

## Tree metrics satisfy the four-point condition

**Tree metrics satisfy the four-point condition** (the easy direction of Buneman's
theorem).

## Sources

- Buneman (1974); Semple & Steel (2003), Theorem 7.2.6.

Formalized by `MathlibExt.Biology.Phylogenetics.Buneman.IsTreeMetric.fourPointCondition`, a theorem declared in [MathlibExt/Biology/Phylogenetics/Buneman.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/Buneman.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition/index.html#four-point-condition-2).

## Buneman's theorem, converse direction

A symmetric dissimilarity on a finite set that
vanishes on the diagonal and satisfies the four-point condition is a tree metric.

## Sources

- Buneman (1974); Semple & Steel (2003), Theorem 7.2.6.

Formalized by `MathlibExt.Biology.Phylogenetics.Buneman.isTreeMetric_of_fourPointCondition`, a theorem declared in [MathlibExt/Biology/Phylogenetics/Buneman.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/Buneman.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition/index.html#is-tree-metric-of-four-point-condition).

## Buneman's four-point theorem

A symmetric dissimilarity on a finite set that vanishes on
the diagonal is a tree metric if and only if it satisfies the four-point condition.

## Sources

- Buneman (1974); Semple & Steel (2003), Theorem 7.2.6.

Formalized by `MathlibExt.Biology.Phylogenetics.Buneman.isTreeMetric_iff_fourPointCondition`, a theorem declared in [MathlibExt/Biology/Phylogenetics/Buneman.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Biology/Phylogenetics/Buneman.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition/index.html#is-tree-metric-iff-four-point-condition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tree metrics and the four-point condition](https://deicyde.github.io/atlas-lean/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/phylogenetics/tree-metrics-and-the-four-point-condition)
