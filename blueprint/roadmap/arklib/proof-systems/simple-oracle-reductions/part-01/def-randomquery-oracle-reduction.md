---
declaration: definition
origin: cited
lean: RandomQuery.oracleReduction
statement: formalized
---

# RandomQuery Oracle Reduction

Fix a type $M$ with an oracle interface and two maps $f, g$ that send a statement $x$ and oracle statements $\mathsf{o}$ to elements $f(x, \mathsf{o}), g(x, \mathsf{o}) \in M$. The RandomQuery reduction is:

- **Protocol specification**: $\mathsf{pSpec} := [(\mathsf{V \!\!\rightarrow\!\! P}, \mathsf{Query})]$ (single challenge from verifier)
- **Input relation**: $R_{\mathsf{in}}((x, \mathsf{o}), ()) := (f(x, \mathsf{o}) = g(x, \mathsf{o}))$
- **Verifier**: Samples a random query $q$ and sends it to the prover
- **Prover**: Receives $q$, performs no computation
- **Output relation**: $R_{\mathsf{out}}(((q, x), \mathsf{o}), ()) := (\mathsf{answer}(f(x, \mathsf{o}), q) = \mathsf{answer}(g(x, \mathsf{o}), q))$

Taking $f$ and $g$ to be two oracle statements gives the test of equality between two oracles; taking $g$ to be a value read from the statement checks a claimed query response.

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)

## Lean

Formalized as [`RandomQuery.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RandomQuery.oracleReduction).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 130](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L130)
