---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.coarse_joint_commutator_bound, MIPRE.Introspection.productStage_mixing_premises, MIPRE.Introspection.exists_product_stage_of_coarse_tests
statement: formalized
proof: formalized
---

# Product-form stage from coarse tests

For a current projective measurement on register $V$, two actual opposite-party coarse joint PVMs provide the tested $Z$ and $X$ marginals. A common sampling marginal provides the remaining linear-readout consistency. If the sum of these six averaged errors is at most $\varepsilon$ and $16\varepsilon\leq1$, the stage constructs actual POVMs on the residual register obtained by removing $U$ from $V$, with product-form squared-distance error at most $224\sqrt{\varepsilon}$. Commutator estimates are conclusions of the coarse tests, rather than hypotheses. The prefix-conditioned identification and iteration across all CL levels remain separate obligations.

## Depends on

- [Pauli mixing with a retained classical fibre](../part-02/lem-pauli-mixing.md)
- [Sampling and hiding subtest estimates](../part-03/lem-intro-subtest-estimates.md)
- [The register model](../../downstream-results/part-03/def-register-model.md)

## Proof

Apply commutation analysis to each coarse joint PVM, and combine the two sampling comparisons on the same side. The resulting mixing premises are bounded by $16\varepsilon$. Apply ambient Pauli mixing on the actual nested registers and simplify $56\sqrt{16\varepsilon}$.

## Lean

Formalized as [`MIPRE.Introspection.coarse_joint_commutator_bound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.coarse_joint_commutator_bound), [`MIPRE.Introspection.productStage_mixing_premises`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.productStage_mixing_premises), [`MIPRE.Introspection.exists_product_stage_of_coarse_tests`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.exists_product_stage_of_coarse_tests).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 2491](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L2491)
