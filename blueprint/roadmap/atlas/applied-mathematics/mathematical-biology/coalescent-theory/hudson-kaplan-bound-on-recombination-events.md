---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.FourGametes, Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.carriers, Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.Separates, Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.IsBreakpointSet, Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.IsDisjointFamily, Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.sweepStep, Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.sweep, Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.rm
statement: formalized
proof: formalized
---

# Hudson–Kaplan bound on recombination events

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html).

## Four-gamete condition for two sites

Sites `i` and `j` show all four gametes: for every pair of alleles `(a, b)` some haplotype
carries `a` at `i` and `b` at `j`. This reuses
`Cslib.Bioinformatics.Phylogenetics.Splits.FourGametes` applied to the site columns
`(M · i)` and `(M · j)`; it is not a second definition of the four-gamete predicate.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.FourGametes`, an abbreviation declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#four-gametes).

## Haplotypes carrying an allele at a site

The haplotypes carrying allele `a` at site `i`; when `a` is the derived allele this is the
clade defined by the mutation at `i`.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.carriers`, a definition declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#carriers).

## Breakpoint separating two sites

A breakpoint `g` (a cut immediately to the left of site `g`) separates sites `i` and `j`
when `i < g ≤ j`.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.Separates`, a definition declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#separates).

## Valid set of recombination breakpoints

A set `B` of breakpoints is valid for the sample `M` when it separates every pair of sites
`i < j` showing all four gametes.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.IsBreakpointSet`, a definition declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#is-breakpoint-set).

## Disjoint family of four-gamete intervals

A family `F` of site pairs `(i, j)` consists of four-gamete intervals (`i < j`, all four
gametes at `i` and `j`) that are pairwise disjoint: of two distinct intervals, one ends at or
before the start of the other, so no breakpoint separates both.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.IsDisjointFamily`, a definition declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#is-disjoint-family).

## One step of the Hudson–Kaplan sweep

One step of the sweep at right endpoint `j`. The list `acc` holds the intervals kept so far,
most recent first; the next interval must start at or after the right end of the most recent
one (at or after site `0` if none was kept). Among the admissible four-gamete intervals ending
at `j`, the shortest one is kept.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.sweepStep`, a definition declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#sweep-step).

## Hudson–Kaplan left-to-right sweep

The intervals kept by Hudson and Kaplan's left-to-right sweep, most recent first.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.sweep`, a definition declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#sweep).

## Hudson and Kaplan's `R_m`

The number of intervals kept by the sweep.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.rm`, a definition declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#rm).

## Intervals kept by the Hudson–Kaplan sweep are distinct

The intervals kept by the sweep are distinct.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.nodup_sweep`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#nodup-sweep).

## Hudson–Kaplan sweep yields disjoint four-gamete intervals

The intervals kept by the sweep are pairwise disjoint four-gamete intervals.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.isDisjointFamily_sweep`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#is-disjoint-family-sweep).

## Sweep cuts form a valid breakpoint set

Cutting immediately to the left of the right endpoint of every kept interval gives a valid
breakpoint set.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.isBreakpointSet_sweep`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#is-breakpoint-set-sweep).

## The sweep yields exactly $R_m$ distinct breakpoints

The right endpoints of the kept intervals are distinct, so there are `R_m` of them.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.card_sweep_snd`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#card-sweep-snd).

## Validity of the bound

**Validity of the bound** (Hudson–Kaplan 1985): a valid breakpoint set has at least as
many points as any family of pairwise disjoint four-gamete intervals, since each interval needs
its own breakpoint.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.card_le_card_of_isBreakpointSet`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#card-le-card-of-is-breakpoint-set).

## `R_m` is a lower bound

**`R_m` is a lower bound** (Hudson–Kaplan 1985): every valid breakpoint set has at least
`R_m` points.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.rm_le_card_of_isBreakpointSet`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#rm-le-card-of-is-breakpoint-set).

## $R_m$ is the minimum size of a valid breakpoint set

The bound is attained: some valid breakpoint set has exactly `R_m` points, so `R_m` is the
minimum size of a valid breakpoint set.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.exists_isBreakpointSet_card_eq_rm`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#exists-is-breakpoint-set-card-eq-rm).

## Greedy optimality

No family of pairwise disjoint four-gamete intervals has more than
`R_m` members.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.card_le_rm`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#card-le-rm).

## $R_m$ is the maximum number of disjoint four-gamete intervals

The sweep attains the maximum: `R_m` is the largest size of a family of pairwise disjoint
four-gamete intervals.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.exists_isDisjointFamily_card_eq_rm`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#exists-is-disjoint-family-card-eq-rm).

## Characterization of site pairs failing the four-gamete test

Two sites miss one of the four gametes exactly when, for some choice of the alleles `a` at
`i` and `b` at `j` (the derived alleles), the carrier sets are nested or disjoint, as two clades
of one rooted tree are.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.not_fourGametes_iff`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#not-four-gametes-iff).

## Hudson and Kaplan's bound for tree-like blocks

Suppose the breakpoints `B` cut the
sequence into blocks such that, within a block, the derived-allele clades of every two sites are
nested or disjoint for some choice of the derived alleles (as for sites whose mutations sit on
one tree under the infinite-sites model). Then there are at least `R_m` breakpoints.

Formalized by `Cslib.Bioinformatics.PopulationGenetics.HudsonKaplan.rm_le_card_of_nested_or_disjoint`, a theorem declared in [CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Bioinformatics/PopulationGenetics/HudsonKaplan.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html#rm-le-card-of-nested-or-disjoint).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hudson–Kaplan bound on recombination events](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/hudson-kaplan-bound-on-recombination-events)
