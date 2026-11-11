---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.BauerFike.norm_ringInverse_sub_smul_one_le, MathlibExt.Analysis.InnerProductSpace.BauerFike.infDist_le_norm_of_mem_spectrum_add, MathlibExt.Analysis.InnerProductSpace.BauerFike.exists_mem_spectrum_norm_sub_le, MathlibExt.Analysis.InnerProductSpace.BauerFike.hausdorffDist_spectrum_le_of_isSelfAdjoint
statement: formalized
proof: formalized
---

# Bauer–Fike theorem

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/bauer-fike-theorem/index.html).

## Resolvent norm bound for a normal operator

The resolvent norm bound for a normal operator: if `z` lies outside the
spectrum of a normal `A`, then `‖(z • 1 - A)⁻¹‖ ≤ 1 / dist z (spectrum ℂ A)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BauerFike.norm_ringInverse_sub_smul_one_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BauerFike.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BauerFike.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/bauer-fike-theorem/index.html#norm-ring-inverse-sub-smul-one-le).

## Bauer–Fike theorem

The Bauer–Fike theorem: every point of the spectrum of `A + E` lies
within `‖E‖` of the spectrum of a normal operator `A`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BauerFike.infDist_le_norm_of_mem_spectrum_add`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BauerFike.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BauerFike.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/bauer-fike-theorem/index.html#inf-dist-le-norm-of-mem-spectrum-add).

## Attained form of the Bauer–Fike theorem

The attained form of Bauer–Fike: some eigenvalue-like point of the
spectrum of `A` is within `‖E‖` of `μ`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BauerFike.exists_mem_spectrum_norm_sub_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BauerFike.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BauerFike.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/bauer-fike-theorem/index.html#exists-mem-spectrum-norm-sub-le).

## Hausdorff distance between spectra of self-adjoint perturbations

For self-adjoint `A` and `A + E`, the Hausdorff distance of the two
spectra is at most `‖E‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BauerFike.hausdorffDist_spectrum_le_of_isSelfAdjoint`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BauerFike.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BauerFike.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/bauer-fike-theorem/index.html#hausdorff-dist-spectrum-le-of-is-self-ad).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bauer–Fike theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/eigenvalue-inequalities/bauer-fike-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/eigenvalue-inequalities/bauer-fike-theorem)
