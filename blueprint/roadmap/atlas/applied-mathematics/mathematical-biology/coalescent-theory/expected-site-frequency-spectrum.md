---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.mergeBlocks, MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.blockPairs, MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.randomJoining, MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.joinStep, MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.sfsLength, MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.exists_finset_randomJoining, MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.joinStep_iterate_count, MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.sum_blockCount_mul_inv_choose_two
statement: formalized
proof: formalized
---

# Expected site frequency spectrum

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html).

## Random joining on block sizes

## Merging two blocks of a block-size list

Merge the blocks at positions `i < j` of the block-size list `b`: remove both and append a
block of size `b[i] + b[j]`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.mergeBlocks`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#merge-blocks).

## Unordered pairs of blocks

The unordered pairs of positions `i < j` among `k` blocks.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.blockPairs`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#block-pairs).

## Random-joining law on block-size lists

The **random-joining** law: `randomJoining m b ps` is the probability that `m` steps of
random joining started from the block-size list `b` visit the list of block-size lists `ps`
(starting with `b` itself). Each step merges a pair of blocks chosen uniformly among all
pairs; the process stops once fewer than two blocks remain.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.randomJoining`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#random-joining).

## Transition operator of random joining

The transition operator of random joining acting on a statistic `g` of block-size lists:
the average of `g` over the lists obtained from `b` by merging a uniformly chosen pair of
blocks (`g []` once fewer than two blocks remain). By `exists_finset_randomJoining`, its `j`-th
iterate at `b` is the expectation of `g` at step `j` of random joining started from `b`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.joinStep`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#join-step).

## Total branch length subtending i sample copies

The total length of the branches subtending exactly `i` of the `n` sample copies, for the
block-size history `ps` (entry `n - k` lists the block sizes while there are `k` lineages)
and holding times `T`: `∑_{k=2}^{n} #{blocks of size i among k} · T k`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.sfsLength`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#sfs-length).

## Random joining has finite support and iterates the join step

The random-joining law has finite support, and the expectation of a statistic of the
`j`-th visited list (`j ≤ m`) is the `j`-th iterate of `joinStep`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.exists_finset_randomJoining`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#exists-finset-random-joining).

## Expected number of blocks of size `i`

**Expected number of blocks of size `i`** when `k` blocks remain, for random joining
started from `n` singletons: `k · C(n-i-1, k-2) / C(n-1, k-1)` (Fu 1995; Griffiths–Tavaré
1998). Equivalently, a given one of the `k` blocks has size `i` with probability
`C(n-i-1, k-2) / C(n-1, k-1)`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.joinStep_iterate_count`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 532](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L532). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#join-step-iterate-count).

## Expected block counts weighted by coalescence times sum to $2/i$

Summing the expected block counts against `E T_k = (k.choose 2)⁻¹` gives `2 / i`:
`∑_{k=2}^{n} k C(n-i-1, k-2) / C(n-1, k-1) · (k.choose 2)⁻¹ = 2 / i` for `1 ≤ i < n`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.sum_blockCount_mul_inv_choose_two`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#sum-block-count-mul-inv-choose-two).

## Expected site frequency spectrum

**Expected site frequency spectrum** (Fu 1995). Let the genealogy of a sample of `n` gene
copies consist of Kingman holding times `K.T` and an independent block-size history `τ` with
the random-joining law. If, given the genealogy (the σ-algebra generated by `τ` and the
holding times), the number `ξ i` of sites whose derived allele is carried by exactly `i`
copies is integrable and has conditional mean `(θ / 2) L_i` (neutral infinite-sites mutation,
`θ = 4Nu`), then `E ξ_i = θ / i` for `1 ≤ i ≤ n - 1`. (Integrability matters: Mathlib's
conditional expectation of a non-integrable function is `0`.)

## Sources

- Fu (1995); Griffiths & Tavaré (1998). Proves the deferred entry `integral_sfs`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Coalescent.SiteFrequencySpectrum.integral_sfs`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean, line 667](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Coalescent/SiteFrequencySpectrum.lean#L667). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html#integral-sfs).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Expected site frequency spectrum](https://deicyde.github.io/atlas-lean/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/coalescent-theory/expected-site-frequency-spectrum)
