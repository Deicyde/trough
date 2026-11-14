---
declaration: theorem
origin: cited
lean: RandomQuery.oracleVerifier_rbrKnowledgeSoundness
statement: formalized
---

# RandomQuery Knowledge Soundness

Suppose that whenever $f(x, \mathsf{o}) \neq g(x, \mathsf{o})$, a uniformly random query $q$ satisfies $\mathsf{answer}(f(x, \mathsf{o}), q) = \mathsf{answer}(g(x, \mathsf{o}), q)$ with probability at most $\varepsilon$. Then the RandomQuery oracle reduction satisfies fixed-prefix round-by-round knowledge soundness with error $\varepsilon$.

## Depends on

- [RandomQuery Oracle Reduction](def-randomquery-oracle-reduction.md)

## Lean

Stated as [`RandomQuery.oracleVerifier_rbrKnowledgeSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RandomQuery.oracleVerifier_rbrKnowledgeSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 153](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L153)
