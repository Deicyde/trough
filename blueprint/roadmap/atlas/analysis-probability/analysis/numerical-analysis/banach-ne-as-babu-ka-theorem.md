---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.IsInfSup, MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.IsNondegenerate, MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.norm_apply_eq_iSup, MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.isInfSup_iff, MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.bilinearFormSharp, MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharp_antilipschitz, MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharp_ker_eq_bot, MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharp_isClosed_range
statement: formalized
proof: formalized
---

# Banach–Nečas–Babuška theorem

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html).

## Inf-sup condition

The **inf–sup condition**: there is `β > 0` such that
`β * ‖x‖ ≤ ‖B x‖` for every `x`. The right-hand side is the dual norm of the
functional `B x`, i.e. `sup_{‖y‖ ≤ 1} |B x y|` (see `norm_apply_eq_iSup`).

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.IsInfSup`, an abbreviation declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#is-inf-sup).

## Nondegeneracy in the second variable

The only `y` annihilated by every
`B x` is `y = 0`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.IsNondegenerate`, an abbreviation declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#is-nondegenerate).

## Dual norm as a supremum over the unit ball

The dual norm is the supremum over the closed unit ball.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.norm_apply_eq_iSup`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#norm-apply-eq-i-sup).

## Inf-sup condition in supremum form

The inf–sup condition in classical supremum form.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.isInfSup_iff`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#is-inf-sup-iff).

## Operator associated to a bounded bilinear form

The operator `E →L[ℝ] F` associated to a bounded bilinear form
`B : E →L[ℝ] F →L[ℝ] ℝ`, characterized by `⟪bilinearFormSharp B x, y⟫ = B x y`.
This is the two-space analogue of Mathlib's `continuousLinearMapOfBilin`
(which is stated for `E = F`).

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.bilinearFormSharp`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#bilinear-form-sharp).

## Inf-sup condition makes the associated operator antilipschitz

The inf–sup condition makes `bilinearFormSharp B` antilipschitz.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharp_antilipschitz`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#sharp-antilipschitz).

## Inf-sup condition makes the associated operator injective

The inf–sup condition makes `bilinearFormSharp B` injective.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharp_ker_eq_bot`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#sharp-ker-eq-bot).

## Inf-sup condition makes the associated operator's range closed

The inf–sup condition makes the range of `bilinearFormSharp B` closed.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharp_isClosed_range`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#sharp-is-closed-range).

## Inf-sup and nondegeneracy make the associated operator surjective

The inf–sup condition plus nondegeneracy make `bilinearFormSharp B`
surjective: the orthogonal complement of its range is trivial, and a closed
subspace of a Hilbert space with trivial orthogonal complement is everything.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharp_range_eq_top`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#sharp-range-eq-top).

## Banach–Nečas–Babuška isomorphism

The **Banach–Nečas–Babuška isomorphism**: the operator associated to a
bilinear form satisfying the inf–sup condition and nondegeneracy is a
continuous linear equivalence.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharpEquiv`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#sharp-equiv).

## Banach–Nečas–Babuška isomorphism is characterized by the form

The equivalence `sharpEquiv` is characterized by the bilinear form.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.sharpEquiv_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#sharp-equiv-apply).

## Norm of the Banach–Nečas–Babuška isomorphism applied to a vector

The norm of `sharpEquiv` applied to `x` is the dual norm of `B x`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.norm_sharpEquiv_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#norm-sharp-equiv-apply).

## Pointwise inverse bound for the Banach–Nečas–Babuška isomorphism

Pointwise inverse bound for `sharpEquiv`: the inverse operator is bounded
by `β⁻¹` when `β` is an inf–sup constant.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.norm_sharpEquiv_symm_apply_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#norm-sharp-equiv-symm-apply-le).

## Operator-norm bound for the inverse Banach–Nečas–Babuška isomorphism

Operator-norm bound for the inverse: `‖(sharpEquiv)⁻¹‖ ≤ β⁻¹`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.norm_sharpEquiv_symm_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#norm-sharp-equiv-symm-le).

## Banach–Nečas–Babuška theorem

The **Banach–Nečas–Babuška theorem**: a bilinear form satisfying the
inf–sup condition and nondegeneracy is itself a continuous linear equivalence
`E ≃L[ℝ] (F →L[ℝ] ℝ)`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.continuousLinearEquivOfBilinearForm`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#continuous-linear-equiv-of-bilinear-form).

## Banach–Nečas–Babuška equivalence acts as the bilinear form

The equivalence `continuousLinearEquivOfBilinearForm` acts as `B`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.continuousLinearEquivOfBilinearForm_apply`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#continuous-linear-equiv-of-bilinear-form-2).

## Unique solvability of the inf-sup variational problem

The variational problem `B x y = φ y` for all `y` has a unique solution.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.exists_unique_apply_eq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#exists-unique-apply-eq).

## Stability bound for the inf-sup variational problem

The variational problem has a solution with the stability bound
`‖x‖ ≤ β⁻¹ * ‖φ‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.BanachNecasBabuska.exists_apply_eq_and_norm_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/BanachNecasBabuska.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html#exists-apply-eq-and-norm-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Banach–Nečas–Babuška theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/numerical-analysis/banach-ne-as-babu-ka-theorem)
