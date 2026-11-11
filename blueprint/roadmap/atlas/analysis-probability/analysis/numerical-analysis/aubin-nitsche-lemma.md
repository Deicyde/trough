---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.AubinNitsche.isCoercive_flip, MathlibExt.Analysis.InnerProductSpace.AubinNitsche.exists_adjointSolution, MathlibExt.Analysis.InnerProductSpace.AubinNitsche.aubinNitsche_pointwise, MathlibExt.Analysis.InnerProductSpace.AubinNitsche.aubinNitsche_core, MathlibExt.Analysis.InnerProductSpace.AubinNitsche.adjointSolution_norm_le, MathlibExt.Analysis.InnerProductSpace.AubinNitsche.aubinNitsche_rate
statement: formalized
proof: formalized
---

# Aubin–Nitsche lemma

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html).

## Transpose of a coercive bilinear form is coercive

The transpose of a coercive bilinear form is coercive with the
same constant, since `B.flip u u = B u u`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.AubinNitsche.isCoercive_flip`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html#is-coercive-flip).

## Existence for the adjoint problem

If `B` is coercive, then
for every `e : H` there is `z : H` with `B v z = ⟪J e, J v⟫_ℝ` for
all `v : H`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.AubinNitsche.exists_adjointSolution`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html#exists-adjoint-solution).

## Aubin–Nitsche lemma, pointwise form

If `e` satisfies Galerkin
orthogonality against `Vh` and `z` solves the adjoint problem, then
for every competitor `zh ∈ Vh`,
`‖J e‖² ≤ ‖B‖ * ‖e‖ * ‖z - zh‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.AubinNitsche.aubinNitsche_pointwise`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html#aubin-nitsche-pointwise).

## Aubin–Nitsche lemma, infimum form

With the same hypotheses,
`‖J e‖² ≤ ‖B‖ * ‖e‖ * Metric.infDist z Vh`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.AubinNitsche.aubinNitsche_core`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html#aubin-nitsche-core).

## Adjoint stability

If `B` is coercive with constant `α` and
`‖J‖ ≤ Cemb`, then the adjoint solution satisfies
`α * ‖z‖ ≤ Cemb * ‖J e‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.AubinNitsche.adjointSolution_norm_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html#adjoint-solution-norm-le).

## Aubin–Nitsche lemma, rate form

If in addition the adjoint
solution is approximable in `Vh` with `‖z - zh‖ ≤ Capp * h * ‖z‖`
for some `zh ∈ Vh`, then the weak-norm error gains the factor `h`:
`α * ‖J e‖ ≤ ‖B‖ * Cemb * Capp * h * ‖e‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.AubinNitsche.aubinNitsche_rate`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/AubinNitsche.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html#aubin-nitsche-rate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Aubin–Nitsche lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/numerical-analysis/aubin-nitsche-lemma)
