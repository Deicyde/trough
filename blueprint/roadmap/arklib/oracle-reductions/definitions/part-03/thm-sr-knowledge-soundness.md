---
declaration: theorem
origin: cited
lean: Interaction.Oracle.Security.StateRestoration.stateRestoration_knowledge_soundness, Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness, Interaction.Oracle.Security.StateRestoration.stateRestoration_knowledge_soundness_privateCoins, Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness_privateCoins
statement: formalized
proof: formalized
---

# State-Restoration Knowledge Soundness

Fix a set $Z$ of permitted inputs and an error $\epsilon$. Suppose that, for every $z \in Z$, the interaction-layer round-by-round extractor for $z$ is prover preserving and locally bounded with error $\epsilon$ at every round. Suppose also that its input knowledge state is the input relation $R_{\text{in}}(z, \cdot)$, and that its terminal knowledge state on every completed path is the output relation $R_{\text{out}}$ of the verifier's output on that path, after a named equivalence between the adversary's witness type and the terminal witness type.

Then for every state-restoration adversary making at most $Q$ queries, the probability that the selected input $z$ lies in $Z$, the output witness $w$ is valid for the verifier's actual output, and the input witness extracted backward from $w$ along the completed path is invalid for $R_{\text{in}}(z, \cdot)$, is at most

$$
(Q + k) \cdot \epsilon .
$$

The extractor is the named backward map, not an existentially chosen witness. The same bound holds for the closed-oracle variant, where a rejection is never a valid output, and, with private coins of the adversary sampled before the game, for both variants.

## Depends on

- [State-Restoration Experiment](def-sr-experiment.md)
- [Round-by-Round Knowledge Certificate in the Interaction Layer](def-interaction-knowledge-certificate.md)

## Proof

If extraction fails on a valid terminal witness, the completed path contains a challenge at which the knowledge state switches from invalid to valid. Its key was queried by the adversary or by completion. The key's knowledge state depends only on strictly earlier keys, so resampling its answer leaves that state unchanged, and the local bound gives probability at most $\epsilon$ for each of the at most $Q + k$ queries.

## Lean

Formalized as [`Interaction.Oracle.Security.StateRestoration.stateRestoration_knowledge_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.stateRestoration_knowledge_soundness), [`Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness), [`Interaction.Oracle.Security.StateRestoration.stateRestoration_knowledge_soundness_privateCoins`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.stateRestoration_knowledge_soundness_privateCoins), [`Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness_privateCoins`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.stateRestoration_oracle_knowledge_soundness_privateCoins).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 960](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L960)
