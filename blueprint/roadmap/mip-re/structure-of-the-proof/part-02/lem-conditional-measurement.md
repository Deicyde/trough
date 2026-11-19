---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.stateSqNorm_expVec_kron, MIPRE.Introspection.conditional_sqNorm, MIPRE.Introspection.conditional_commutator, MIPRE.Introspection.conditional_sqNorm_sum, MIPRE.Introspection.conditional_commutator_sum, MIPRE.Introspection.submeasurement_agreement_dist, MIPRE.Introspection.conditional_consistency
statement: formalized
proof: formalized
---

# Conditioning on part of a question

On a state that factors as a question part times an answer part, a projective measurement of the question part induces a distribution on it, and consistency or commutation statements about the unconditioned measurements transfer to the measurements conditioned on the sampled question. In particular, if $\sum_{x, y, z} \langle\psi| A^y_{x, z} \otimes B_{x, y, z} |\psi\rangle \geq 1 - \delta$ with $\{B_{x,y,z}\}$ projective, then ${I} \otimes B_{x, y, z} \approx_\delta A^y_{x, z} \otimes B_{x, y}$.

## Depends on

- [The expanded state, and an inert ancilla](../../foundations/part-02/def-expanded-state.md)

## Proof depends on

- [The ancilla extension](../../downstream-results/part-02/lem-ancilla-extension.md)

## Proof

On a product state, the squared norm of a tensor-product operator factors. The question factor is exactly the probability weight. This gives exact conditioning and commutator identities, also for outcome-dependent tensor decompositions. For conditional consistency, the operators $A^y_{x,z}\otimes B_{x,y}$ form a positive submeasurement. Expand its distance from ${I}\otimes B_{x,y,z}$, use projectivity to identify the cross term with the agreement probability, and bound each diagonal sum by one. The literal summed squared-distance bound is $2\delta$.

## Lean

Formalized as [`MIPRE.Introspection.stateSqNorm_expVec_kron`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stateSqNorm_expVec_kron), [`MIPRE.Introspection.conditional_sqNorm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_sqNorm), [`MIPRE.Introspection.conditional_commutator`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_commutator), [`MIPRE.Introspection.conditional_sqNorm_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_sqNorm_sum), [`MIPRE.Introspection.conditional_commutator_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_commutator_sum), [`MIPRE.Introspection.submeasurement_agreement_dist`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.submeasurement_agreement_dist), [`MIPRE.Introspection.conditional_consistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.conditional_consistency).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1598](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1598)
