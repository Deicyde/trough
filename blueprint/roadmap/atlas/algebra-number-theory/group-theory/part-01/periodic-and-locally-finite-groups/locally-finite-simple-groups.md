---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.IsLocallyFinite, MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.IsCompositionSeries, MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.locallyFiniteSimpleIsAbsolutelySimple, MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.locallyFiniteSimpleIsAbsolutelySimple_refuted
statement: formalized
---

# Locally finite simple groups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/locally-finite-simple-groups/index.html).

## Locally finite group

A group $G$ is locally finite when every subgroup of $G$ generated
by finitely many elements is finite.

Formalized by `MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.IsLocallyFinite`, a definition declared in [WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/locally-finite-simple-groups/index.html#is-locally-finite).

## Composition series in Kurosh's sense

A set $S$ of subgroups of a group $G$ is a
composition series of $G$ when it contains the trivial subgroup and $G$, it is totally ordered by
inclusion, it contains the join and the intersection of every subset of $S$, and for every jump
$A < B$ of $S$ (members $A \subsetneq B$ of $S$ with no member of $S$ strictly between them) $A$
is normal in $B$ and the quotient $B / A$ is a simple group.

Formalized by `MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.IsCompositionSeries`, a definition declared in [WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/locally-finite-simple-groups/index.html#is-composition-series).

## Absolute simplicity of locally finite simple groups (Kourovka 11.108)

The statement,
asked by R. Phillips, that every locally finite simple group $G$ is absolutely simple: every
composition series of $G$ in Kurosh's sense consists of the trivial subgroup and $G$ alone.

Formalized by `MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.locallyFiniteSimpleIsAbsolutelySimple`, a definition declared in [WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/locally-finite-simple-groups/index.html#locally-finite-simple-is-absolutely-simp).

## Locally finite simple groups need not be absolutely simple

There is a locally finite simple
group $G$ with a composition series, in Kurosh's sense, other than the series consisting of the
trivial subgroup and $G$ alone. That is, the statement of Kourovka Problem 11.108, that every
locally finite simple group is absolutely simple, is false.

The Kourovka Archive answers 11.108 "No, not every", citing Meierfrankenfeld (1995), whose
Section 6 constructs countable locally finite simple groups $G$ that are not absolutely simple,
with an ascending series $M_1 \trianglelefteq M_2 \trianglelefteq \cdots$ of proper subgroups
whose union is $G$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 11.108 (R. Phillips); resolution: U. Meierfrankenfeld, Non-finitary locally finite simple groups, in: Proc. Int. Conf. Finite and Locally Finite Groups, Istanbul, 1994, Kluwer, 1995, 189-212, Section 6, countable locally finite simple groups that are not absolutely simple; Kourovka Archive, Problem 11.108 ("No, not every"), https://users.math.msu.edu/users/meierfra/Preprints/Nflfsg/nflfsg.pdf.

Stated but not proved: `MathlibExt.GroupTheory.LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.locallyFiniteSimpleIsAbsolutelySimple_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/LocallyFiniteSimpleAbsolutelySimpleKourovka11Problem108Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/locally-finite-simple-groups/index.html#locally-finite-simple-is-absolutely-simp-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Locally finite simple groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/periodic-and-locally-finite-groups/locally-finite-simple-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/periodic-and-locally-finite-groups/locally-finite-simple-groups)
