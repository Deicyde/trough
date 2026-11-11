---
declaration: section
origin: cited
lean: MathlibExt.Biology.CancerGenomics.Absolute.mixCopy, MathlibExt.Biology.CancerGenomics.Absolute.copyRatio, MathlibExt.Biology.CancerGenomics.Absolute.slope, MathlibExt.Biology.CancerGenomics.Absolute.intercept, MathlibExt.Biology.CancerGenomics.Absolute.somaticAF, MathlibExt.Biology.CancerGenomics.Absolute.germlineAF, MathlibExt.Biology.CancerGenomics.Absolute.scaledPurity, MathlibExt.Biology.CancerGenomics.Absolute.mixCopy_pos
statement: formalized
proof: formalized
---

# Tumour purity, ploidy and copy-ratio algebra

26 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html).

## Average absolute copy number of a tumor sample

Average absolute copy number `α q + 2 (1 - α)` of a locus with copy number `q` in the cancer
cells, in a sample of purity `α` whose normal cells are diploid (Carter et al. 2012). With
`q = τ` this is the sample ploidy `D` of Eq. 1; with the local copy number it is `D_s` of
Eq. 2.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.mixCopy`, a definition declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#mix-copy).

## Relative copy ratio

Relative copy ratio `R = (α q + 2 (1 - α)) / (α τ + 2 (1 - α))` of a locus with copy number
`q`, purity `α` and cancer-cell ploidy `τ` (Carter et al. 2012, Eq. 1).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.copyRatio`, a definition declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#copy-ratio).

## Copy-ratio slope

The copy-ratio slope `α / D` of Eq. 1 (Carter et al. 2012), the copy ratio of one extra
copy per cancer cell.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.slope`, a definition declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#slope).

## Copy-ratio intercept

The copy-ratio intercept `2 (1 - α) / D` of Eq. 1 (Carter et al. 2012), the copy ratio of a
homozygously deleted locus.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.intercept`, a definition declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#intercept).

## Expected allelic fraction of a somatic mutation

Expected allelic fraction `α s / (α q + 2 (1 - α))` of a clonal somatic point mutation with
multiplicity `s` (copies per cancer cell) at a locus of copy number `q` (Carter et al. 2012,
Eq. 2; Eq. 10 is `s = 1`).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF`, a definition declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af).

## Expected allelic fraction of a germline variant

Expected allelic fraction `((1 - α) + α g) / (α q + 2 (1 - α))` of a heterozygous germline
variant present in `g` copies per cancer cell at a locus of copy number `q` (Carter et al.
2012, Eq. 11).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.germlineAF`, a definition declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#germline-af).

## Rescaled purity

The purity `α / (m - (m - 1) α)` that, together with all copy numbers multiplied by `m`,
reproduces the copy ratios and allelic fractions of purity `α` (derived from Carter et al.
2012, Eqs. 1, 2, 11).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.scaledPurity`, a definition declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#scaled-purity).

## Positivity of the mixture copy number

The mixture copy number is positive in the biological domain `0 ≤ α ≤ 1`, `0 < q`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.mixCopy_pos`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#mix-copy-pos).

## Eq. 1 is affine in `q`

`R = (α / D) q + 2 (1 - α) / D`, for all real arguments.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.copyRatio_eq_slope_mul_add_intercept`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#copy-ratio-eq-slope-mul-add-intercept).

## Calibrated copy ratios have mean `1`

If the segment weights `w` sum to one and the
ploidy is the weighted mean copy number `τ = ∑ w q`, the weighted mean copy ratio is `1`
(Carter et al. 2012, Methods: "correctly calibrated copy-ratio data always has mean = 1").

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.sum_mul_copyRatio_eq_one`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#sum-mul-copy-ratio-eq-one).

## Allelic fractions are determined by the copy-ratio slope

**Allelic fractions are determined by the copy-ratio slope** (Carter et al. 2012, Eq. 2):
`α s / D_s = (α / D) s / R`, whenever `D ≠ 0`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF_eq_slope_mul_div_copyRatio`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af-eq-slope-mul-div-copy-ratio).

## Purity from copy-ratio slope and intercept

Inverse of Eq. 1, purity: `α = 2 b / (2 b + δ)` for the slope `b` and intercept `δ`, when
`0 < α ≤ 1` and `0 < τ`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.purity_eq`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#purity-eq).

## Ploidy from copy-ratio slope and intercept

Inverse of Eq. 1, ploidy: `τ = (1 - δ) / b` for the slope `b` and intercept `δ`, when
`0 < α ≤ 1` and `0 < τ`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.ploidy_eq`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#ploidy-eq).

## Purity and ploidy are identifiable from the slope and intercept of Eq. 1

The map
`(α, τ) ↦ (α / D, 2 (1 - α) / D)` is a bijection from `{0 < α ≤ 1, 0 < τ}` onto
`{0 < b, 0 ≤ δ < 1}`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.bijOn_slope_intercept`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#bij-on-slope-intercept).

## Positivity of the rescaled purity denominator

The denominator `m - (m - 1) α = m (1 - α) + α` of the rescaled purity is positive for
`m > 0` and `0 ≤ α ≤ 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.scaledPurity_denom_pos`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#scaled-purity-denom-pos).

## Rescaled purity lies in (0, 1)

The rescaled purity is again a purity: `0 ≤ α / (m - (m - 1) α) ≤ 1` for `m > 0` and
`0 ≤ α ≤ 1`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.scaledPurity_mem`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#scaled-purity-mem).

## Ploidy-scaling non-identifiability, copy ratios

Scaling every copy number and the
ploidy by `m > 0` and the purity to `α / (m - (m - 1) α)` leaves every copy ratio of Eq. 1
unchanged.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.copyRatio_scale`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#copy-ratio-scale).

## Ploidy-scaling non-identifiability, somatic allelic fractions

**Ploidy-scaling non-identifiability, somatic allelic fractions** (Eq. 2): with copy
number and multiplicity both scaled by `m > 0` and the purity rescaled, the allelic fraction is
unchanged.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF_scale`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af-scale).

## Ploidy-scaling non-identifiability, germline allelic fractions

**Ploidy-scaling non-identifiability, germline allelic fractions** (Eq. 11): with copy
number and germline multiplicity both scaled by `m > 0` and the purity rescaled, the allelic
fraction is unchanged.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.germlineAF_scale`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#germline-af-scale).

## Rescaled purity differs from the original purity

The rescaled solution is a genuinely different purity: for `0 < α < 1` and `m ≠ 1`,
`α / (m - (m - 1) α) ≠ α`.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.scaledPurity_ne`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#scaled-purity-ne).

## Genome doubling

Doubling every copy number and the ploidy and replacing the purity by
`α / (2 - α)` reproduces every copy ratio (the `m = 2` case of `copyRatio_scale`).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.copyRatio_doubling`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#copy-ratio-doubling).

## Nonnegativity of somatic allelic fractions

Somatic allelic fractions are nonnegative in the biological domain.

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF_nonneg`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af-nonneg).

## Somatic allelic fraction is at most one

A somatic allelic fraction is at most one when the multiplicity does not exceed the copy
number (`s ≤ q`).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF_le_one`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 305](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L305). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af-le-one).

## Somatic allelic fraction increases with purity

The somatic allelic fraction increases with the purity (`0 ≤ s`, `0 < q`).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF_mono_purity`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af-mono-purity).

## Somatic allelic fraction decreases with copy number

The somatic allelic fraction decreases with the local copy number (`0 ≤ α ≤ 1`,
`0 ≤ s`, `0 < q ≤ q'`).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF_anti_copy`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af-anti-copy).

## Somatic allelic fraction increases with multiplicity

The somatic allelic fraction increases with the multiplicity (`0 ≤ α ≤ 1`, `0 < q`).

Formalized by `MathlibExt.Biology.CancerGenomics.Absolute.somaticAF_mono_mult`, a theorem declared in [MathlibExt/Biology/CancerGenomics/Absolute.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/CancerGenomics/Absolute.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html#somatic-af-mono-mult).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tumour purity, ploidy and copy-ratio algebra](https://deicyde.github.io/atlas-lean/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/cancer-genomics/tumour-purity-ploidy-and-copy-ratio-algebra)
