---
declaration: section
origin: cited
lean: MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.SamplePath, MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.neutralKernel, MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.neutralKernel_add, MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.rawMeasure, MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.rawProcess, MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_eval_rawMeasure, MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_eval_zero_rawMeasure, MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_pair_rawMeasure_of_lt
statement: formalized
proof: formalized
---

# Construction of the neutral Wright–Fisher diffusion

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html).

## Canonical sample paths of the raw Wright–Fisher process

Canonical sample paths before continuous modification.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.SamplePath`, an abbreviation declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#sample-path).

## Neutral Wright–Fisher transition kernel at nonnegative time

The neutral Wright--Fisher transition kernel at nonnegative time.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.neutralKernel`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#neutral-kernel).

## Chapman–Kolmogorov for the nonnegative-time Wright–Fisher kernel

Chapman--Kolmogorov for the nonnegative-time specialization.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.neutralKernel_add`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#neutral-kernel-add).

## Canonical path measure of the raw Wright–Fisher process

The canonical probability measure on `NNReal → I`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.rawMeasure`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#raw-measure).

## Raw Wright–Fisher coordinate process

The raw real-valued coordinate process, normalized at time zero on every
sample rather than merely almost surely.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.rawProcess`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#raw-process).

## One-time marginals of the raw Wright–Fisher path measure

One-time marginals of the canonical raw path measure.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_eval_rawMeasure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#map-eval-raw-measure).

## Time-zero marginal of the raw path measure is the initial state

The time-zero coordinate of the canonical path law is the prescribed
initial state.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_eval_zero_rawMeasure`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#map-eval-zero-raw-measure).

## Two-time law of the raw Wright–Fisher path measure

The ordered two-time law is the first marginal followed by the
transition over the time gap.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_pair_rawMeasure_of_lt`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#map-pair-raw-measure-of-lt).

## Normalized raw process agrees with the coordinates almost surely

Exact normalization changes no fixed-time law.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.rawProcess_ae_eq_coordinate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#raw-process-ae-eq-coordinate).

## Kolmogorov constant for the Wright–Fisher continuity bound

The explicit Kolmogorov constant `3/16`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.kolmogorovConstant`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 437](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L437). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#kolmogorov-constant).

## Kolmogorov continuity condition for the raw Wright–Fisher process

The normalized raw coordinate process satisfies the explicit fourth-moment
Kolmogorov condition with `p=4`, `q=2`, and `M=3/16`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.isKolmogorovProcess_rawProcess`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#is-kolmogorov-process-raw-process).

## Continuous realization of the raw Wright–Fisher process

A selected continuous modification of the raw Wright--Fisher process,
with all pathwise properties stated on every sample.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.ContinuousRealization`, a structure declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#continuous-realization).

## Continuous modification selected by Kolmogorov's theorem

The continuous modification selected by Kolmogorov's theorem.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.continuousRealization`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#continuous-realization-2).

## Continuous modified Wright–Fisher process

The concrete continuous process used by the final realization.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.modifiedProcess`, a definition declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#modified-process).

## Modified process has the raw finite-dimensional laws

The modified process has the raw finite-dimensional laws, proved on each
finite set by intersecting its fixed-time modification events.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_restrict_modified_eq_raw`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 546](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L546). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#map-restrict-modified-eq-raw).

## Modified process has the canonical coordinate laws

The modified finite-dimensional laws also equal the original canonical
coordinate laws after coercion from `I` to `ℝ`.

Formalized by `MathlibExt.Biology.PopulationGenetics.Diffusion.NeutralWrightFisherRaw.map_restrict_modified_eq_coordinate`, a theorem declared in [MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean, line 556](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/PopulationGenetics/Diffusion/NeutralWrightFisherRaw.lean#L556). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html#map-restrict-modified-eq-coordinate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Construction of the neutral Wright–Fisher diffusion](https://deicyde.github.io/atlas-lean/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/population-genetics/diffusion-theory/construction-of-the-neutral-wright-fisher-diffus)
