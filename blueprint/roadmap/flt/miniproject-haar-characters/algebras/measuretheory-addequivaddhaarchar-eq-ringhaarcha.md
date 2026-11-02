---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det, MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det_of_existsListTransvecEtc
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/517
---

# MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det,
    MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det\_of\_existsListTransvecEtc

Assume that there's an $F$-basis for $V$ such that $\phi$ is a product of elementary and diagonal matrices (note that this is automatic if $F$ is a field and mathlib has this). Then $d_V(\phi)=\delta_F(\det(\phi))$, where $\det(\phi)\in F$ is the determinant of $\phi$ as an $F$-linear map.

## Depends on

- [MeasureTheory.ringHaarChar](../initial-definitions/measuretheory-ringhaarchar.md)

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar](../initial-definitions/measuretheory-addequivaddhaarchar.md)

## Proof

The proof is a generalization of [Real.map\_matrix\_volume\_pi\_eq\_smul\_volume\_pi](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Measure/Lebesgue/Basic.html#Real.map_matrix_volume_pi_eq_smul_volume_pi), which crucially uses the induction principle [Matrix.diagonal\_transvection\_induction\_of\_det\_ne\_zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Transvection.html#Matrix.diagonal_transvection_induction_of_det_ne_zero). One checks it explicitly for diagonal matrices and for matrices which are the identity except that one off-diagonal entry is non-zero.

Note: we assume that $F$ is second countable (but it shouldn't be necessary).

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det), [`MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det_of_existsListTransvecEtc`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_eq_ringHaarChar_det_of_existsListTransvecEtc).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 344](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L344)
