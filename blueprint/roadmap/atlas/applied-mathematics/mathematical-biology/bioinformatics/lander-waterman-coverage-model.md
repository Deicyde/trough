---
declaration: section
origin: cited
lean: Cslib.Bioinformatics.Assembly.LanderWaterman.Covers, Cslib.Bioinformatics.Assembly.LanderWaterman.depth, Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount, Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount_eq_uniformOfFinset, Cslib.Bioinformatics.Assembly.LanderWaterman.card_uncovered, Cslib.Bioinformatics.Assembly.LanderWaterman.card_depth_eq, Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount_uncovered, Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount_depth_eq
statement: formalized
proof: formalized
---

# Lander–Waterman coverage model

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html).

## Read covering a base of a circular genome

A read of length `L` starting at position `s` of a circular genome of length `G` covers base
`x` when `x` is one of `s, s + 1, …, s + L - 1 (mod G)`, i.e. `(x - s) mod G < L`.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.Covers`, a definition declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#covers).

## Depth of coverage of a base

The depth of coverage of base `x`: the number of reads covering it.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.depth`, a definition declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#depth).

## Normalized count of read start tuples

The totalized normalized count `|E| / G ^ N` of a set of start tuples.
For `0 < G`, this is the probability when the `N` start positions are independent and uniform
on `Fin G`. If `G = 0` and `N > 0`, the sample space is empty and this value is zero, so it is
not a probability law. For `N = 0`, there is one empty start tuple, even when `G = 0`.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount`, a definition declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#normalized-count).

## Normalized count agrees with the totalized uniform measure

`normalizedCount` agrees with Mathlib's totalized uniform measure on all start tuples.
This measure is a probability law only when the sample space is nonempty.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount_eq_uniformOfFinset`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#normalized-count-eq-uniform-of-finset).

## Exact coverage count

For `L ≤ G`, base `x` is uncovered by all `N` reads for exactly
`(G - L) ^ N` of the `G ^ N` start tuples.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.card_uncovered`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#card-uncovered).

## Exact depth law (count form)

For `L ≤ G`, base `x` is covered by exactly `k` reads for
`N.choose k * L ^ k * (G - L) ^ (N - k)` of the start tuples.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.card_depth_eq`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#card-depth-eq).

## Exact uncovered probability

**Exact uncovered probability** (Clarke–Carbon, Lander–Waterman, circular genome):
`(1 - L / G) ^ N` for `L ≤ G`.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount_uncovered`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#normalized-count-uncovered).

## Exact depth law

The depth at a fixed base is binomial with `N` trials and success
probability `L / G`, for `L ≤ G`.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.normalizedCount_depth_eq`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#normalized-count-depth-eq).

## Lander–Waterman limit for the uncovered fraction

With read length `L` fixed, genome
lengths `G N ≥ L`, and coverage `N L / G_N → c` as the number of reads `N → ∞`, the probability
that a given base is uncovered tends to `e^{-c}`.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.tendsto_normalizedCount_uncovered`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#tendsto-normalized-count-uncovered).

## The coverage depth tends to Poisson(`c`)

Under the hypotheses of
`tendsto_normalizedCount_uncovered`, the probability that a given base is covered by exactly `k`
reads tends to `e^{-c} c^k / k.factorial`.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.tendsto_normalizedCount_depth`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 255](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L255). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#tendsto-normalized-count-depth).

## Read with no successor

Read `j` has no successor when no other read starts in the `L - 1` positions after it,
`starts j + 1, …, starts j + L - 1 (mod G)` (reads starting at the same position are not
successors of each other). In Lander and Waterman's terms such a read is counted as ending
an island, but several no-successor reads can lie in one island, so this is not the island
count.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.NoSuccessor`, a definition declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 270](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L270). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#no-successor).

## Count of no-successor reads (exact)

For `L ≤ G`, summed over the
reads, the number of start tuples in which read `j` has no successor is
`N * G * (G - (L - 1)) ^ (N - 1)`. This counts no-successor reads, not island ends:
a start tuple can have several no-successor reads in one island.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.sum_card_noSuccessor`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#sum-card-no-successor).

## Expected number of no-successor reads (exact)

For `0 < G` and `L ≤ G`, the
expected number of reads with no successor is `N (1 - (L - 1) / G) ^ (N - 1)`.
The `0 < G` hypothesis is essential: at `G = 0` and `N > 0`, the right-hand expression is
`N` while the sum of totalized normalized counts is zero.

Formalized by `Cslib.Bioinformatics.Assembly.LanderWaterman.expected_noSuccessor`, a theorem declared in [CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean, line 375](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Bioinformatics/Assembly/LanderWaterman.lean#L375). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html#expected-no-successor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lander–Waterman coverage model](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/lander-waterman-coverage-model/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/lander-waterman-coverage-model)
