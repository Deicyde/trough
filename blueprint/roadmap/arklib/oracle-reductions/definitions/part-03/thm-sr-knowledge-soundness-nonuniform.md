---
declaration: theorem
origin: cited
lean: Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness_nonuniform, Interaction.Oracle.Security.MeasuredKnowledgeCertificate.stateRestoration_oracle_knowledge_soundness_nonuniform
statement: formalized
proof: formalized
---

# State-Restoration Knowledge Soundness with Per-Round Errors

Under the hypotheses of [State-Restoration Knowledge Soundness](thm-sr-knowledge-soundness.md) for the closed-oracle variant, but with local error $\epsilon_j$ at round $j$, the bound becomes

$$
Q \cdot \max_j \epsilon_j + \sum_{j} \epsilon_j .
$$

For a measured knowledge certificate whose challenge schedule has these errors and whose stage budgets are at most $B$ on every input in $Z$, the same bound holds together with the stage budget $B$ for the same named extractor.

## Depends on

- [State-Restoration Knowledge Soundness](thm-sr-knowledge-soundness.md)

## Proof

Charge each queried key the error of its round. The adversary's at most $Q$ queries cost at most $Q \cdot \max_j \epsilon_j$, and completion queries one key per round, costing $\sum_j \epsilon_j$.

## Lean

Formalized as [`Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness_nonuniform`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness_nonuniform), [`Interaction.Oracle.Security.MeasuredKnowledgeCertificate.stateRestoration_oracle_knowledge_soundness_nonuniform`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.MeasuredKnowledgeCertificate.stateRestoration_oracle_knowledge_soundness_nonuniform).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 995](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L995)
