---
declaration: definition
origin: cited
lean: GeneratorBatch.oracleReduction
statement: formalized
---

# Generator Batching

Fix $d > 0$ and a generator $G : S \to \mathbb{F}^k$. The input is a family of $k$ polynomial oracles $f_1, \ldots, f_k$ of natural degree strictly less than $d$, with no witness.

- **Input relation**: every $f_i$ vanishes on $H$
- **Protocol specification**: The verifier sends a uniformly random seed $s \in S$; there are no prover messages
- **Output oracle statement**: The batched polynomial $\sum_{i} G(s)_i \cdot f_i$, whose evaluations are simulated by querying each $f_i$ at the same point
- **Output relation**: The input relation of the quotient zero test for the batched polynomial

The batched output is supplied to the quotient zero test under that test's inclusive budget of degree at most $d$.

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)
- [Quotient Zero Test](def-quotient-zero-test.md)

## Lean

Formalized as [`GeneratorBatch.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/GeneratorBatch.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 232](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L232)
