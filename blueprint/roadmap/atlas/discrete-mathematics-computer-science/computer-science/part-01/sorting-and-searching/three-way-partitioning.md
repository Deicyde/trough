---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.ThreeWayPartition, Cslib.Algorithms.Lean.TimeM.partition3, Cslib.Algorithms.Lean.TimeM.partition3_time, Cslib.Algorithms.Lean.TimeM.partition3_correct, Cslib.Algorithms.Lean.TimeM.partition3_below_eq_filter, Cslib.Algorithms.Lean.TimeM.partition3_equal_eq_filter, Cslib.Algorithms.Lean.TimeM.partition3_above_eq_filter, Cslib.Algorithms.Lean.TimeM.partition3_length
statement: formalized
proof: formalized
---

# Three-way partitioning

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html).

## Three-way partition record

A three-way partition over a type $\alpha$ consists of three
lists over $\alpha$, called below, equal and above. They are meant to hold the elements strictly
below, equal to, and strictly above a pivot; the record itself imposes no condition on them.

Formalized by `Cslib.Algorithms.Lean.TimeM.ThreeWayPartition`, a structure declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#three-way-partition).

## Stable three-way partition

Let $p$ be an element of a linearly ordered type $\alpha$. The
three-way partition of a list over $\alpha$ around $p$, together with the time it is charged, is
defined by recursion on the list. The empty list gives three empty lists at no cost. For a list
with head $x$ and tail $xs$, one unit of time is charged for comparing $x$ with $p$, the tail $xs$
is partitioned, and $x$ is put at the front of its below list if $x < p$, of its equal list if
$x = p$, and of its above list if $p < x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#partition3).

## Cost of the stable three-way partition

For every element $p$ of a linearly ordered type
$\alpha$ and every list $xs$ over $\alpha$, the time charged by the stable three-way partition of
$xs$ around $p$ equals the length of $xs$: one unit for each comparison, one comparison per
element.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#partition3-time).

## Correctness of the stable three-way partition

Let $p$ be an element of a linearly ordered
type $\alpha$, let $xs$ be a list over $\alpha$, and let $B$, $E$ and $A$ be the below, equal and
above lists of the stable three-way partition of $xs$ around $p$. Then the concatenation $B$, $E$,
$A$ is a permutation of $xs$, every element $x$ of $B$ satisfies $x < p$, every element of $E$
equals $p$, and every element $x$ of $A$ satisfies $p < x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_correct`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#partition3-correct).

## The below list of a three-way partition is a filter

For every element $p$ of a linearly
ordered type $\alpha$ and every list $xs$ over $\alpha$, the below list of the stable three-way
partition of $xs$ around $p$ is the list of the elements $x$ of $xs$ with $x < p$, in their order
in $xs$ and with their multiplicities.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_below_eq_filter`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#partition3-below-eq-filter).

## The equal list of a three-way partition is a filter

For every element $p$ of a linearly
ordered type $\alpha$ and every list $xs$ over $\alpha$, the equal list of the stable three-way
partition of $xs$ around $p$ is the list of the elements $x$ of $xs$ with $x = p$, in their order
in $xs$ and with their multiplicities.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_equal_eq_filter`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#partition3-equal-eq-filter).

## The above list of a three-way partition is a filter

For every element $p$ of a linearly
ordered type $\alpha$ and every list $xs$ over $\alpha$, the above list of the stable three-way
partition of $xs$ around $p$ is the list of the elements $x$ of $xs$ with $p < x$, in their order
in $xs$ and with their multiplicities.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_above_eq_filter`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#partition3-above-eq-filter).

## Sizes of the three parts of a three-way partition

For every element $p$ of a linearly
ordered type $\alpha$ and every list $xs$ over $\alpha$, the lengths of the below, equal and above
lists of the stable three-way partition of $xs$ around $p$ add up to the length of $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.partition3_length`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Partition.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Partition.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html#partition3-length).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Three-way partitioning](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/three-way-partitioning)
