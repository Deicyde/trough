---
declaration: section
origin: cited
lean: MathlibExt.Biology.StatisticalGenetics.ProximalContamination.mmChiSq, MathlibExt.Biology.StatisticalGenetics.ProximalContamination.inv_add_smul_vecMulVec_mulVec, MathlibExt.Biology.StatisticalGenetics.ProximalContamination.mmChiSq_add_smul_vecMulVec, MathlibExt.Biology.StatisticalGenetics.ProximalContamination.mmChiSq_add_smul_vecMulVec_le
statement: formalized
proof: formalized
---

# Proximal contamination in mixed-model association

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/proximal-contamination-in-mixed-model-associatio/index.html).

## Mixed-model association chi-squared statistic

The mixed-model (generalized-least-squares score) statistic
`χ²(V) = (xᵀ V⁻¹ y)² / (xᵀ V⁻¹ x)` of the marker `x` for the phenotype `y` under the phenotypic
covariance `V`. For positive definite `V` and `x ≠ 0` the denominator is positive.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ProximalContamination.mmChiSq`, a definition declared in [MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/proximal-contamination-in-mixed-model-associatio/index.html#mm-chi-sq).

## Sherman–Morrison applied to the candidate marker

For positive definite `V₀` and
`c ≥ 0`, `(V₀ + c x xᵀ)⁻¹ x = (1 + c xᵀ V₀⁻¹ x)⁻¹ • V₀⁻¹ x`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ProximalContamination.inv_add_smul_vecMulVec_mulVec`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/proximal-contamination-in-mixed-model-associatio/index.html#inv-add-smul-vec-mul-vec-mul-vec).

## Proximal contamination

Including the candidate marker `x` in the covariance,
`V = V₀ + c x xᵀ` with `V₀` positive definite and `c ≥ 0`, divides the mixed-model statistic by
`1 + c xᵀ V₀⁻¹ x`, for every phenotype vector `y`:
`χ²(V₀ + c x xᵀ) = χ²(V₀) / (1 + c xᵀ V₀⁻¹ x)`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ProximalContamination.mmChiSq_add_smul_vecMulVec`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/proximal-contamination-in-mixed-model-associatio/index.html#mm-chi-sq-add-smul-vec-mul-vec).

## Including the marker in the covariance never increases the statistic

Including the candidate marker in the covariance never increases the mixed-model
statistic: `χ²(V₀ + c x xᵀ) ≤ χ²(V₀)` for positive definite `V₀` and `c ≥ 0`.

Formalized by `MathlibExt.Biology.StatisticalGenetics.ProximalContamination.mmChiSq_add_smul_vecMulVec_le`, a theorem declared in [MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/StatisticalGenetics/ProximalContamination.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/proximal-contamination-in-mixed-model-associatio/index.html#mm-chi-sq-add-smul-vec-mul-vec-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Proximal contamination in mixed-model association](https://deicyde.github.io/atlas-lean/roadmap/Biology/statistical-genetics/proximal-contamination-in-mixed-model-associatio/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/statistical-genetics/proximal-contamination-in-mixed-model-associatio)
