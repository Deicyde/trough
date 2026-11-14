---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.stateSqNorm_mul_of_isometry, MIPRE.Introspection.unitaryTwirl_dist_le, MIPRE.Introspection.unitaryTwirl_outcome_dist_le
statement: formalized
proof: formalized
---

# Approximate commutation controls unitary mixing

Let $M_a^x$ be POVMs, $\psi$ a unit bipartite vector and $\mu_x$ a conditional unitary distribution. For $\mathrm T_{\mu_x}(M)=\mathbb E_U UMU^\dagger$, put $\delta=\mathbb E_x\mathbb E_U\sum_a \|([M_a^x,U^\dagger]\otimes{I})\psi\|^2$. Then $\mathbb E_x\sum_a \|((\mathrm T_{\mu_x}(M_a^x)-M_a^x)\otimes{I})\psi\|^2\leq\delta$. Jensen and left-unitary invariance of the norm suffice; invariance of the state under $U$ is not a hypothesis.

## Depends on

- [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)

## Proof

Write each conjugation error as $U[M,U^\dagger]$. Left multiplication by $U$ preserves the squared state norm, and convexity bounds the squared norm of the average by the average of the squared norms. Sum over outcomes and average questions. The Lean estimate has constant one and holds for arbitrary operator families and arbitrary state vectors.

## Lean

Formalized as [`MIPRE.Introspection.stateSqNorm_mul_of_isometry`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.stateSqNorm_mul_of_isometry), [`MIPRE.Introspection.unitaryTwirl_dist_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.unitaryTwirl_dist_le), [`MIPRE.Introspection.unitaryTwirl_outcome_dist_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.unitaryTwirl_outcome_dist_le).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1405](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1405)
