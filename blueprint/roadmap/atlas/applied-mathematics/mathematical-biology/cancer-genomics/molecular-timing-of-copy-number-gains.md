---
declaration: section
origin: cited
lean: MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory, MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.finalCopies, MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.amplified, MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.expectedCount, MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.sum_mul_expectedCount, MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.sum_expectedCount_amplified, MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.finalCopies_pos, MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.rate_eq
statement: formalized
proof: formalized
---

# Molecular timing of copy-number gains

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html).

## Mutation Timing

## Copy-number gain history

A single copy-number event on a region: `copies` original copies, of which copy `i` has
`desc i` copies after the event (`0` if lost, `2` if duplicated).

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory`, a structure declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#gain-history).

## Copy number after a copy-number event

The copy number `c₁ = ∑ i, desc i` after the event.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.finalCopies`, a definition declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#final-copies).

## Number of amplified copies

The number of original copies amplified by the event (`desc i ≥ 2`).

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.amplified`, a definition declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#amplified).

## Expected number of mutations of a given multiplicity

Expected number of mutations of multiplicity `m`:
`μ t #{i | desc i = m} + [m = 1] μ c₁ (1 - t)` (per-copy rate `μ`, event at time `t` of the
normalized history `[0, 1]`).

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.expectedCount`, a definition declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#expected-count).

## The multiplicity-weighted total is time-invariant

`∑_m m E_m = μ c₁`, summing over
all multiplicities up to a bound `B ≥ max(1, max_i desc i)`.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.sum_mul_expectedCount`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#sum-mul-expected-count).

## Expected count of mutations on amplified copies

The mutations of multiplicity at least two number `μ t #{i | desc i ≥ 2}` in expectation:
they all arose before the event, on an amplified copy.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.sum_expectedCount_amplified`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#sum-expected-count-amplified).

## Positive copy number after an amplifying event

An event that amplifies some copy leaves a positive copy number.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.finalCopies_pos`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#final-copies-pos).

## The mutation rate from the spectrum

`μ = ∑_m m E_m / c₁` (`c₁ > 0`).

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.rate_eq`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#rate-eq).

## The timing closed form

When some copy is amplified and `μ ≠ 0`,
`t = c₁ ∑_{m ≥ 2} E_m / (#{i | desc i ≥ 2} ∑_m m E_m)`.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.timing_eq`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#timing-eq).

## Identifiability

If some copy is amplified, two parameter pairs `(μ, t)`, `(μ', t')`
with `μ, μ' ≠ 0` and the same expected multiplicity spectrum are equal.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.expectedCount_injective`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#expected-count-injective).

## Single-copy gain

A single-copy gain `1 + 1 → 2 + 1`: one copy duplicated, the other kept.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.singleGain`, a definition declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#single-gain).

## Copy-neutral loss of heterozygosity

Copy-neutral loss of heterozygosity `1 + 1 → 2 + 0`: one copy duplicated, the other lost.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.cnLOH`, a definition declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#cn-loh).

## Whole-genome doubling event

Whole-genome doubling of a diploid region `1 + 1 → 2 + 2`.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.wgd`, a definition declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#wgd).

## Single gain

**Single gain** (`2 + 1`): `t = 3 E₂ / (E₁ + 2 E₂)`, for `μ ≠ 0`.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.singleGain_timing`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#single-gain-timing).

## Copy-neutral LOH

**Copy-neutral LOH** (`2 + 0`): `t = 2 E₂ / (E₁ + 2 E₂)`, for `μ ≠ 0`.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.cnLOH_timing`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#cn-loh-timing).

## Whole-genome doubling

**Whole-genome doubling** (`2 + 2`): `t = 2 E₂ / (E₁ + 2 E₂)`, for `μ ≠ 0`.

Formalized by `MathlibExt.Biology.CancerGenomics.MutationTiming.GainHistory.wgd_timing`, a theorem declared in [MathlibExt/Biology/CancerGenomics/MutationTiming.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/MutationTiming.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html#wgd-timing).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Molecular timing of copy-number gains](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/cancer-genomics/molecular-timing-of-copy-number-gains)
