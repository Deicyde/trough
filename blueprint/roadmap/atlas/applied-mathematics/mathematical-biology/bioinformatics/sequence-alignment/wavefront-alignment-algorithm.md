---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.LinearPenalties, Cslib.Algorithms.Lean.LinearPenalties.columnCost, Cslib.Algorithms.Lean.LinearPenalties.cost, Cslib.Algorithms.Lean.Wavefront.maxOffset, Cslib.Algorithms.Lean.Wavefront.extend, Cslib.Algorithms.Lean.Wavefront.slide, Cslib.Algorithms.Lean.Wavefront.wavefrontAux, Cslib.Algorithms.Lean.Wavefront.wavefront
statement: formalized
proof: formalized
---

# Wavefront alignment algorithm

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html).

## Linear Penalties

## Linear gap penalties

Linear gap penalties: match `0`, mismatch `mismatch ≥ 1`, each gap column `gap ≥ 1`.

Formalized by `Cslib.Algorithms.Lean.LinearPenalties`, a structure declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#linear-penalties).

## Cost of an alignment column under linear gap penalties

The cost of one alignment column.

Formalized by `Cslib.Algorithms.Lean.LinearPenalties.columnCost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#column-cost).

## Cost of an alignment under linear gap penalties

The cost of an alignment: the sum of its column costs.

Formalized by `Cslib.Algorithms.Lean.LinearPenalties.cost`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#cost).

## Largest valid offset on a diagonal

The largest valid offset on diagonal `k`: `h ≤ |ys|` and `v = h - k ≤ |xs|`.

Formalized by `Cslib.Algorithms.Lean.Wavefront.maxOffset`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#max-offset).

## Fuelled extension of matches along a diagonal

Follow matching letters along diagonal `k` from offset `h`, with fuel.

Formalized by `Cslib.Algorithms.Lean.Wavefront.extend`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#extend).

## Match extension (slide) along a diagonal

The match extension ("slide") along diagonal `k` from offset `h`.

Formalized by `Cslib.Algorithms.Lean.Wavefront.slide`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#slide).

## Fuelled wavefront recurrence

The wavefront recurrence with fuel (fuel `s + 1` suffices; see `wavefront`).
`none` stands for an unreachable diagonal. Offsets proposed by an operation are clamped to the
largest valid offset of the target diagonal before sliding.

Formalized by `Cslib.Algorithms.Lean.Wavefront.wavefrontAux`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#wavefront-aux).

## Furthest-reaching wavefront offset

The furthest-reaching offset of score `s` on diagonal `k = h - v`.

Formalized by `Cslib.Algorithms.Lean.Wavefront.wavefront`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#wavefront).

## Soundness of the wavefront algorithm

Soundness: a wavefront offset is a valid cell of its diagonal, reachable by an alignment
of the corresponding prefixes with cost at most `s`.

Formalized by `Cslib.Algorithms.Lean.Wavefront.wavefront_sound`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#wavefront-sound).

## Completeness of the wavefront algorithm

Completeness: every alignment of a pair of prefixes is dominated on its diagonal by the
wavefront of its exact cost.

Formalized by `Cslib.Algorithms.Lean.Wavefront.wavefront_complete`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 695](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L695). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#wavefront-complete).

## Exactness of the wavefront alignment algorithm

The wavefront algorithm is exact: the end cell is reached by some score `s' ≤ s` iff some
alignment of `xs` and `ys` costs at most `s`. Hence the least such `s` is the optimal cost.

Formalized by `Cslib.Algorithms.Lean.Wavefront.exists_wavefront_end_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 798](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L798). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#exists-wavefront-end-iff).

## Substitution score from linear gap penalties

The substitution score in the maximization convention of `nwScore`: `0` for a match and
`-mismatch` for a mismatch (the gap score is `-gap`).

Formalized by `Cslib.Algorithms.Lean.LinearPenalties.score`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 826](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L826). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#score).

## Alignment score is the negated linear-penalty cost

Scores are negated costs.

Formalized by `Cslib.Algorithms.Lean.LinearPenalties.alignmentScore_eq_neg_cost`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 829](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L829). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#alignment-score-eq-neg-cost).

## The wavefront algorithm computes the optimal alignment cost

The end cell is reached by
some score `s' ≤ s` iff `s` is at least the optimal Needleman–Wunsch cost.

Formalized by `Cslib.Algorithms.Lean.Wavefront.exists_wavefront_end_iff_nwScore`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean, line 852](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/DynamicProgramming/WavefrontAlignment.lean#L852). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html#exists-wavefront-end-iff-nw-score).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wavefront alignment algorithm](https://deicyde.github.io/atlas-lean/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Biology/bioinformatics/sequence-alignment/wavefront-alignment-algorithm)
