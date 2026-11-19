---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.QuestionType.card, MIPRE.Introspection.QuestionType.esize_aux_le, MIPRE.Introspection.TypeGraph.symmetric, MIPRE.Introspection.TypeGraph.adj_pauli, MIPRE.Introspection.TypeGraph.adj_different_roles_iff, MIPRE.Introspection.TypeGraph.adj_pauli_aux_iff, MIPRE.Introspection.TypeGraph.adj_hide_hide_iff, MIPRE.Introspection.TypeGraph.edges_nonempty, MIPRE.Introspection.TypeGraph.detyping_factor_of_pauli_card, MIPRE.Introspection.TypedPresentation.family_exactlyOn, MIPRE.Introspection.TypedPresentation.marginal_aux, MIPRE.Introspection.TypedPresentation.linear_aux, MIPRE.Introspection.TypedPresentation.factor_aux, MIPRE.Introspection.TypedPresentation.joint_aux_zero, MIPRE.Introspection.TypedPresentation.mu_cross_introspect, MIPRE.Introspection.TypedPresentation.failAt_cross_introspect_le
statement: formalized
proof: formalized
---

# Introspection type graph and typed CL family

Given the finite Pauli type graph and its distinguished $X,Z$ vertices, construct the introspection graph with both hiding chains, the sampling and reading edges, the cross-introspection edge and all loops. It has $|T_{\mathrm{Pauli}}|+2\ell+6$ vertices, hence $2\ell+32$ when the Pauli graph has $26$ vertices. Its type encoding uses binary hiding indices. Retain the supplied three-level Pauli CL family; every auxiliary type has the zero presentation with a full factor partition. The cross-introspection edge asks the two zero-content questions with probability exactly the inverse number of ordered edges. Its conditional failure is at most the edge count times the whole typed game's failure.

## Depends on

- [The introspective verifier](def-intro-verifier.md)
- [Finite-game detyping soundness](lem-detype-game-soundness.md)

## Proof

The graph is the symmetric closure of the explicit oriented chains and Pauli edges. Constructor case analysis proves the edge classifications. Summing the uniform common-seed law over the zero auxiliary presentations gives the exact edge probability; nonnegativity bounds its contribution to the total failure. This supplies the graph and CL family. The uniform Pauli sampler and the introspective decision program are supplied by Lemmas [The canonical sampler at every index](../part-06/lem-intro-canonical-sampler.md) and [Executable quotient hiding and the finite decision kernel](../part-06/lem-intro-quotient-kernel.md).

## Lean

Formalized as [`MIPRE.Introspection.QuestionType.card`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.QuestionType.card), [`MIPRE.Introspection.QuestionType.esize_aux_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.QuestionType.esize_aux_le), [`MIPRE.Introspection.TypeGraph.symmetric`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.symmetric), [`MIPRE.Introspection.TypeGraph.adj_pauli`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.adj_pauli), [`MIPRE.Introspection.TypeGraph.adj_different_roles_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.adj_different_roles_iff), [`MIPRE.Introspection.TypeGraph.adj_pauli_aux_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.adj_pauli_aux_iff), [`MIPRE.Introspection.TypeGraph.adj_hide_hide_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.adj_hide_hide_iff), [`MIPRE.Introspection.TypeGraph.edges_nonempty`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.edges_nonempty), [`MIPRE.Introspection.TypeGraph.detyping_factor_of_pauli_card`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypeGraph.detyping_factor_of_pauli_card), [`MIPRE.Introspection.TypedPresentation.family_exactlyOn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.family_exactlyOn), [`MIPRE.Introspection.TypedPresentation.marginal_aux`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.marginal_aux), [`MIPRE.Introspection.TypedPresentation.linear_aux`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.linear_aux), [`MIPRE.Introspection.TypedPresentation.factor_aux`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.factor_aux), [`MIPRE.Introspection.TypedPresentation.joint_aux_zero`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.joint_aux_zero), [`MIPRE.Introspection.TypedPresentation.mu_cross_introspect`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.mu_cross_introspect), [`MIPRE.Introspection.TypedPresentation.failAt_cross_introspect_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.TypedPresentation.failAt_cross_introspect_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1051](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1051)
