---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CeaLemma.restrictBilin, MathlibExt.Analysis.InnerProductSpace.CeaLemma.isCoercive_restrictBilin, MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution, MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_spec, MathlibExt.Analysis.InnerProductSpace.CeaLemma.eq_of_forall_bilin, MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_eq_of_forall, MathlibExt.Analysis.InnerProductSpace.CeaLemma.exists_variationalSolution, MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution
statement: formalized
proof: formalized
---

# Céa's lemma

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html).

## Restriction of a bilinear form to a subspace

Restriction of a bounded bilinear form to a submodule.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.restrictBilin`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#restrict-bilin).

## Coercivity passes to restrictions to subspaces

Coercivity is inherited by restriction to a submodule.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.isCoercive_restrictBilin`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#is-coercive-restrict-bilin).

## Solution of a coercive variational problem

The solution of the variational problem `B u w = L w` for all `w`,
obtained from the Lax–Milgram equivalence and the Riesz representation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#variational-solution).

## Variational solution satisfies the variational equation

The variational solution satisfies the variational equation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_spec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#variational-solution-spec).

## Uniqueness for coercive variational problems

Uniqueness for the variational problem: two vectors satisfying the same
variational equation agree, by coercivity.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.eq_of_forall_bilin`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#eq-of-forall-bilin).

## Variational solution is the unique solution

The variational solution is the unique solution of the variational
equation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_eq_of_forall`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#variational-solution-eq-of-forall).

## Existence of a variational solution

Existence for the variational problem, in bare existential form.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.exists_variationalSolution`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#exists-variational-solution).

## Galerkin solution

The Galerkin solution in `W`: the solution of the variational problem
for the restricted form and the restricted functional.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-solution).

## Galerkin solution satisfies the Galerkin equations

The Galerkin solution satisfies the Galerkin equations.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution_spec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-solution-spec).

## Galerkin solution is the unique solution of the Galerkin equations

The Galerkin solution is the unique element of `W` satisfying the
Galerkin equations.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution_eq_of_forall`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-solution-eq-of-forall).

## Existence of a Galerkin solution

Existence for the Galerkin problem, in bare existential form.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.exists_galerkinSolution`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#exists-galerkin-solution).

## Galerkin orthogonality

Galerkin orthogonality: the error `u - u_h` is `B`-orthogonal to `W`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkin_orthogonality`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-orthogonality).

## Céa's lemma

**Céa's lemma** (pointwise form): the Galerkin error is bounded by
`(‖B‖ / α)` times the distance from `u` to any element `v` of `W`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_sub_galerkinSolution_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-sub-galerkin-solution-le).

## Céa's lemma

**Céa's lemma** (infimum form): the Galerkin error is bounded by
`(‖B‖ / α)` times the best-approximation error `⨅ v : W, ‖u - v‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_sub_galerkinSolution_le_iInf`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-sub-galerkin-solution-le-i-inf).

## Stability bound for the variational solution

Stability of the variational solution: `‖u‖ ≤ ‖L‖ / α`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_variationalSolution_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-variational-solution-le).

## Stability bound for the Galerkin solution

Stability of the Galerkin solution: `‖u_h‖ ≤ ‖L‖ / α`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_galerkinSolution_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-galerkin-solution-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Céa's lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/numerical-analysis/c-a-s-lemma)
