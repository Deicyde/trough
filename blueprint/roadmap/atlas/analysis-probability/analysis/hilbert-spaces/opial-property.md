---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.Opial.bddAbove_norm_of_weakly_tendsto, MathlibExt.Analysis.InnerProductSpace.Opial.tendsto_re_inner_sub_of_weakly_tendsto, MathlibExt.Analysis.InnerProductSpace.Opial.opial_liminf_sq, MathlibExt.Analysis.InnerProductSpace.Opial.opial_liminf
statement: formalized
proof: formalized
---

# Opial property

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/opial-property/index.html).

## Weakly convergent sequences are norm-bounded

A weakly convergent sequence is norm-bounded (Banach–Steinhaus applied
to the evaluation maps on the dual space).

Formalized by `MathlibExt.Analysis.InnerProductSpace.Opial.bddAbove_norm_of_weakly_tendsto`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Opial.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Opial.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/opial-property/index.html#bdd-above-norm-of-weakly-tendsto).

## Cross term vanishes under weak convergence

The cross term in the squared-norm identity tends to `0` under weak
convergence, via the Fréchet–Riesz representation of the functional
`z ↦ ⟪x - y, z⟫`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Opial.tendsto_re_inner_sub_of_weakly_tendsto`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Opial.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Opial.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/opial-property/index.html#tendsto-re-inner-sub-of-weakly-tendsto).

## Opial's property, squared-norm form

If `u n ⇀ x` weakly and
`y ≠ x`, then `liminf ‖u n - x‖² < liminf ‖u n - y‖²`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Opial.opial_liminf_sq`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Opial.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Opial.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/opial-property/index.html#opial-liminf-sq).

## Opial's property

If `u n ⇀ x` weakly and `y ≠ x`, then
`liminf ‖u n - x‖ < liminf ‖u n - y‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.Opial.opial_liminf`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/Opial.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/Opial.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/opial-property/index.html#opial-liminf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Opial property](https://deicyde.github.io/atlas-lean/roadmap/Analysis/hilbert-spaces/opial-property/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/hilbert-spaces/opial-property)
