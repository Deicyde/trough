---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Assembly.Omnitig.Multigraph, Cslib.Bioinformatics.Assembly.Omnitig.IsWalk, Cslib.Bioinformatics.Assembly.Omnitig.IsPath, Cslib.Bioinformatics.Assembly.Omnitig.IsCircularCovering, Cslib.Bioinformatics.Assembly.Omnitig.IsCircularSubwalk, Cslib.Bioinformatics.Assembly.Omnitig.IsSafe, Cslib.Bioinformatics.Assembly.Omnitig.IsOmnitig, Cslib.Bioinformatics.Assembly.Omnitig.IsOmnitig.isSafe
statement: formalized
proof: formalized
---

# Omnitigs and safe walks in genome assembly

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html).

## Directed multigraph

A directed multigraph given by the source and target of each edge.

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.Multigraph`, a structure declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#multigraph).

## Walk in a directed multigraph

A list of edges is a walk when consecutive edges are incident (head to tail).

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.IsWalk`, a definition declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-walk).

## Path in a directed multigraph

A path: a nonempty walk whose nodes `src e₀, tgt e₀, …, tgt e_ℓ` are distinct, except that
the first and last node may coincide.

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.IsPath`, a definition declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-path).

## Circular edge-covering walk

A circular edge-covering walk: a nonempty closed walk through every edge.

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.IsCircularCovering`, a definition declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-circular-covering).

## Subwalk of a circular walk

`w` is a subwalk of the circular walk `A`: it is read off `A` from some start position,
wrapping around (possibly several times).

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.IsCircularSubwalk`, a definition declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-circular-subwalk).

## Safe walk in a multigraph

Safe walk: a subwalk of every circular edge-covering walk.

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.IsSafe`, a definition declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-safe).

## Omnitig

Omnitig (Tomescu–Medvedev, Definition 5): for all `1 ≤ i ≤ j ≤ t` (`t + 1 = w.length`),
no path from `v_j = src e_j` to `v_i = src e_i` has first edge `≠ e_j` and last edge
`≠ e_{i-1}`.

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.IsOmnitig`, a definition declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-omnitig).

## Omnitigs are safe walks

Omnitigs are safe (Theorem 1, (2) ⇒ (1)).

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.IsOmnitig.isSafe`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 785](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L785). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-safe-2).

## Safe walks are omnitigs

Safe walks are omnitigs (Theorem 1, (1) ⇒ (2)), when a circular edge-covering walk exists
(otherwise every walk is vacuously safe).

Formalized by `Cslib.Bioinformatics.Assembly.Omnitig.isOmnitig_of_isSafe`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/Omnitig.lean, line 803](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/Assembly/Omnitig.lean#L803). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html#is-omnitig-of-is-safe).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Omnitigs and safe walks in genome assembly](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/bioinformatics/omnitigs-and-safe-walks-in-genome-assembly)
