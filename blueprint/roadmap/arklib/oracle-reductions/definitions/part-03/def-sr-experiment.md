---
declaration: definition
origin: cited
lean: Interaction.Oracle.Security.StateRestoration.Key, Interaction.Oracle.Security.StateRestoration.oracleSpec, Interaction.Oracle.Security.StateRestoration.restoredExecution, Interaction.Oracle.Security.StateRestoration.verificationGame, Interaction.Oracle.Security.StateRestoration.closedVerificationGame
statement: formalized
---

# State-Restoration Experiment

A **restoration key** for round $j$ consists of an input, the prover messages of rounds $1, \ldots, j$, and a salt for each of those rounds. Earlier verifier challenges are not part of the key. The challenge oracle answers each key with a challenge of that round, and is implemented as a lazily sampled random oracle starting from an empty cache.

A **state-restoration adversary** is an oracle computation against this challenge oracle that makes at most $Q$ queries in total and returns an input $z$, a prover message and salt for every round, and an output witness $w$. The experiment then completes the selected transcript by querying the same oracle once per round (so at most $Q + k$ queries are made in all), and runs the verifier on the completed path. In the closed-oracle variant, the verifier returns either a rejection or an oracle claim, whose behavior is observed through the accumulated oracle handler of the same path.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Interaction.Oracle.Security.StateRestoration.Key`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.Key), [`Interaction.Oracle.Security.StateRestoration.oracleSpec`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.oracleSpec), [`Interaction.Oracle.Security.StateRestoration.restoredExecution`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.restoredExecution), [`Interaction.Oracle.Security.StateRestoration.verificationGame`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.verificationGame), [`Interaction.Oracle.Security.StateRestoration.closedVerificationGame`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Interaction.Oracle.Security.StateRestoration.closedVerificationGame).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 917](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L917)
