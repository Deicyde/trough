---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.commutator_product_bound, MIPRE.Introspection.two_sided_commutation, MIPRE.Introspection.two_sided_commutation_avg, MIPRE.Introspection.unitaryTwirl_comp, MIPRE.Introspection.composed_twirl_dist_le
statement: formalized
proof: formalized
---

# Combining two approximate commutations

Conditionally on $x$, draw $U_1,U_2$ independently. Suppose both commutators $[M_a^x,U_i^\dagger]$ have average outcome-summed squared state norm $O(\varepsilon)$ and $\mathbb E\|((U_2^\dagger\otimes{I})-({I}\otimes U_2))\psi\|^2=O(\varepsilon)$. Then $[M_a^x,U_1^\dagger U_2^\dagger]$ has the same type of bound. Transfer $U_2$ across the bipartition and back; $\sum_a(M_a^x)^2\leq{I}$ controls the summed transfer errors without an outcome-count factor.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Approximate commutation controls unitary mixing](lem-pauli-unitary-mixing.md)

## Proof

Transfer the second unitary to its commuting mirror on Bob's side, move the first unitary past the measurement, and transfer back. The four-link squared triangle inequality gives coefficients $4,4,8$ for the two commutator errors and the mirror error. The POVM contraction identity controls the outcome sum. Independent conditional averages preserve these coefficients. With an exact mirror, the composed twirl costs at most four times the sum of the two averaged commutator errors.

## Lean

Formalized as [`MIPRE.Introspection.commutator_product_bound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.commutator_product_bound), [`MIPRE.Introspection.two_sided_commutation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.two_sided_commutation), [`MIPRE.Introspection.two_sided_commutation_avg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.two_sided_commutation_avg), [`MIPRE.Introspection.unitaryTwirl_comp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.unitaryTwirl_comp), [`MIPRE.Introspection.composed_twirl_dist_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.composed_twirl_dist_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1432](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1432)
