---
declaration: section
origin: cited
lean: MeasureTheory.lintegral_mul_eq_of_normalized_smul, MeasureTheory.integrable_mul_iff_of_normalized_smul, MeasureTheory.integral_mul_eq_of_normalized_smul, MeasureTheory.integral_mul_eq_of_normalized_subgroup, MeasureTheory.exists_continuous_cutoff_of_isClosedEmbedding, MeasureTheory.exists_continuous_cutoff_of_subset_mul, MeasureTheory.exists_hasCompactSupport_integral_subgroup_translate_eq_one_of_subset_mul, MeasureTheory.integrable_mul_of_integral_subgroup_translate_eq_one
statement: formalized
proof: formalized
---

# Bruhat functions

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html).

## Orbit-normalized weights give equal nonnegative integrals

Nonnegative integrals of an invariant function agree for orbit-normalized
weights. Normalization is needed only where the function is nonzero, and the
common integral is allowed to be infinite.

Formalized by `MeasureTheory.lintegral_mul_eq_of_normalized_smul`, a theorem declared in [MathlibExt/MeasureTheory/Group/ActionCutoff.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/ActionCutoff.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#lintegral-mul-eq-of-normalized-smul).

## Integrability is independent of the orbit-normalized weight

Integrability of an invariant complex function times a nonnegative real
weight is independent of the weight when both orbit averages are one on the
function's support. Neither weighted function is required to be integrable.

Formalized by `MeasureTheory.integrable_mul_iff_of_normalized_smul`, a theorem declared in [MathlibExt/MeasureTheory/Group/ActionCutoff.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/ActionCutoff.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#integrable-mul-iff-of-normalized-smul).

## Orbit-normalized cutoffs give equal complex integrals

Weighted integrals of an invariant complex function agree for nonnegative
orbit-normalized cutoffs. If one weighted function is not integrable, neither
is the other, and both Bochner integrals are zero.

Formalized by `MeasureTheory.integral_mul_eq_of_normalized_smul`, a theorem declared in [MathlibExt/MeasureTheory/Group/ActionCutoff.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/ActionCutoff.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#integral-mul-eq-of-normalized-smul).

## Subgroup-normalized weights give equal integrals

Subgroup-normalized nonnegative weights give the same integral of an
invariant complex function. This measure-theoretic statement requires neither
a closed subgroup nor compact supports nor a bounded function.

Formalized by `MeasureTheory.integral_mul_eq_of_normalized_subgroup`, a theorem declared in [MathlibExt/MeasureTheory/Group/ActionCutoff.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/ActionCutoff.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#integral-mul-eq-of-normalized-subgroup).

## Continuous cutoff for a closed-embedding homomorphism

A continuous nonnegative compactly supported cutoff normalized on every
left orbit meeting `K`, for a closed-embedding homomorphism `ι`. The measure
may have any scale. No Hausdorff or countability hypotheses are required.

Formalized by `MeasureTheory.exists_continuous_cutoff_of_isClosedEmbedding`, a theorem declared in [MathlibExt/MeasureTheory/Group/BruhatSection.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/BruhatSection.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#exists-continuous-cutoff-of-is-closed-em).

## Continuous Bruhat cutoff for a closed subgroup

A continuous nonnegative compactly supported Bruhat cutoff for a closed
subgroup, normalized on any subset of the saturation of a compact set.

Formalized by `MeasureTheory.exists_continuous_cutoff_of_subset_mul`, a theorem declared in [MathlibExt/MeasureTheory/Group/BruhatSection.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/BruhatSection.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#exists-continuous-cutoff-of-subset-mul).

## Existence of a Bruhat section for a closed subgroup

A Bruhat section: given a closed subgroup `T` of a locally compact group
and a set `E` contained in `T * C` for compact `C`, there is a compactly
supported nonnegative measurable function `w` whose integral over each
`T`-translate meeting `E` equals `1`.

Use `exists_continuous_cutoff_of_subset_mul` when continuity or boundedness is
needed. These functions normalize subgroup integrals; they are not sections
of the quotient map.

Formalized by `MeasureTheory.exists_hasCompactSupport_integral_subgroup_translate_eq_one_of_subset_mul`, a theorem declared in [MathlibExt/MeasureTheory/Group/BruhatSection.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/BruhatSection.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#exists-has-compact-support-integral-subg).

## Bounded invariant functions are integrable against normalized cutoffs

A bounded measurable `T`-invariant complex function is integrable against
any nonnegative measurable compactly supported weight whose `T`-average is
one wherever the function is nonzero. The weight need not be bounded.

Formalized by `MeasureTheory.integrable_mul_of_integral_subgroup_translate_eq_one`, a theorem declared in [MathlibExt/MeasureTheory/Group/CutoffIndependence.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/CutoffIndependence.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#integrable-mul-of-integral-subgroup-tran).

## Cutoff independence of integrals of bounded invariant functions

The integral of a bounded measurable `T`-invariant complex function
against a nonnegative measurable compactly supported cutoff does not depend
on the cutoff, when each cutoff has subgroup integral one on the support of
that function. Normalization is not required outside its support.

The more general `integral_mul_eq_of_normalized_subgroup` does not require
boundedness or compact support; the hypotheses here also guarantee
integrability by `integrable_mul_of_integral_subgroup_translate_eq_one`.

Formalized by `MeasureTheory.integral_mul_eq_integral_mul_of_integral_subgroup_translate_eq_one`, a theorem declared in [MathlibExt/MeasureTheory/Group/CutoffIndependence.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/CutoffIndependence.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#integral-mul-eq-integral-mul-of-integral).

## Positive common integral of cocompact subgroup cutoffs

A compact cocompactness witness gives a continuous normalized cutoff and
a positive common integral for all nonnegative measurable compactly supported
normalized cutoffs. Every such cutoff is genuinely integrable, even when it
is not bounded. Neither the ambient group nor the subgroup must be Hausdorff.

Formalized by `MeasureTheory.exists_pos_integral_cutoff_of_cocompact`, a theorem declared in [MathlibExt/MeasureTheory/Group/CutoffMass.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/CutoffMass.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#exists-pos-integral-cutoff-of-cocompact).

## Existence of a locally constant normalized subgroup cutoff

A compact set in a topological group with a compact open subgroup has a
nonnegative locally constant cutoff whose integral over every left
`T`-orbit meeting that set is one, for a closed commutative subgroup `T`.
The same compactly supported function works simultaneously on all of
`T * Ω`. The Haar measure need not have any prescribed normalization.

Formalized by `MeasureTheory.exists_isLocallyConstant_integral_subgroup_mul_eq_one`, a theorem declared in [MathlibExt/MeasureTheory/Group/LocallyConstantCutoff.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Group/LocallyConstantCutoff.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html#exists-is-locally-constant-integral-subg).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bruhat functions](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/haar-measure/bruhat-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/haar-measure/bruhat-functions)
