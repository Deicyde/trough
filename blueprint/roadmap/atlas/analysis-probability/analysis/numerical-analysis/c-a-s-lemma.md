---
declaration: section
origin: cited
lean: MathlibExt.Analysis.InnerProductSpace.CeaLemma.restrictBilin, MathlibExt.Analysis.InnerProductSpace.CeaLemma.isCoercive_restrictBilin, MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution, MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_spec, MathlibExt.Analysis.InnerProductSpace.CeaLemma.eq_of_forall_bilin, MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_eq_of_forall, MathlibExt.Analysis.InnerProductSpace.CeaLemma.exists_variationalSolution, MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution
statement: formalized
proof: formalized
---

# Céa's lemma

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html).

## Restriction of a bilinear form to a subspace

Restriction of a bounded bilinear form to a submodule.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.restrictBilin`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#restrict-bilin).

## Coercivity passes to restrictions to subspaces

Coercivity is inherited by restriction to a submodule.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.isCoercive_restrictBilin`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#is-coercive-restrict-bilin).

## Solution of a coercive variational problem

The solution of the variational problem `B u w = L w` for all `w`,
obtained from the Lax–Milgram equivalence and the Riesz representation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#variational-solution).

## Variational solution satisfies the variational equation

The variational solution satisfies the variational equation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_spec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#variational-solution-spec).

## Uniqueness for coercive variational problems

Uniqueness for the variational problem: two vectors satisfying the same
variational equation agree, by coercivity.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.eq_of_forall_bilin`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#eq-of-forall-bilin).

## Variational solution is the unique solution

The variational solution is the unique solution of the variational
equation.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.variationalSolution_eq_of_forall`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#variational-solution-eq-of-forall).

## Existence of a variational solution

Existence for the variational problem, in bare existential form.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.exists_variationalSolution`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#exists-variational-solution).

## Galerkin solution

The Galerkin solution in `W`: the solution of the variational problem
for the restricted form and the restricted functional.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution`, a definition declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-solution).

## Galerkin solution satisfies the Galerkin equations

The Galerkin solution satisfies the Galerkin equations.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution_spec`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-solution-spec).

## Galerkin solution is the unique solution of the Galerkin equations

The Galerkin solution is the unique element of `W` satisfying the
Galerkin equations.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkinSolution_eq_of_forall`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-solution-eq-of-forall).

## Existence of a Galerkin solution

Existence for the Galerkin problem, in bare existential form.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.exists_galerkinSolution`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#exists-galerkin-solution).

## Galerkin orthogonality

Galerkin orthogonality: the error `u - u_h` is `B`-orthogonal to `W`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.galerkin_orthogonality`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#galerkin-orthogonality).

## Céa's lemma

**Céa's lemma** (pointwise form): the Galerkin error is bounded by
`(‖B‖ / α)` times the distance from `u` to any element `v` of `W`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_sub_galerkinSolution_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-sub-galerkin-solution-le).

## Céa's lemma

**Céa's lemma** (infimum form): the Galerkin error is bounded by
`(‖B‖ / α)` times the best-approximation error `⨅ v : W, ‖u - v‖`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_sub_galerkinSolution_le_iInf`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-sub-galerkin-solution-le-i-inf).

## Stability bound for the variational solution

Stability of the variational solution: `‖u‖ ≤ ‖L‖ / α`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_variationalSolution_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-variational-solution-le).

## Stability bound for the Galerkin solution

Stability of the Galerkin solution: `‖u_h‖ ≤ ‖L‖ / α`.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CeaLemma.norm_galerkinSolution_le`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/InnerProductSpace/CeaLemma.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html#norm-galerkin-solution-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Céa's lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/numerical-analysis/c-a-s-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/numerical-analysis/c-a-s-lemma)
