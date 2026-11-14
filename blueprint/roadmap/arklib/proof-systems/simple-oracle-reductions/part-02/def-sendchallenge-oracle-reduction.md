---
declaration: definition
origin: cited
lean: SendChallenge.oracleReduction, SendChallenge.foldBlockStructure
statement: formalized
---

# SendChallenge Oracle Reduction

Fix a challenge alphabet $C$ and a length $\ell$. The SendChallenge reduction is a one-round protocol with no witness and no check:

- **Protocol specification**: $\mathsf{pSpec} := [(\mathsf{V \!\!\rightarrow\!\! P}, C^{\ell})]$
- **Verifier**: Samples $c \in C^{\ell}$ and appends it to the statement; the oracle statements pass through
- **Output statement**: $(\mathsf{stmt}, c)$

A lone challenge round has nothing to extract, so it has no security statement of its own. Its verifier is pure, so it can be a left factor of a coordinate-wise special-soundness composition, where it contributes one challenge round with $\ell$ coordinates over $C$ and soundness parameter $2$.

## Depends on

- [Interactive Oracle Reduction](../../../oracle-reductions/definitions/part-01/def-oracle-reduction.md)

## Lean

Formalized as [`SendChallenge.oracleReduction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendChallenge.oracleReduction), [`SendChallenge.foldBlockStructure`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/SendChallenge.foldBlockStructure).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 290](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L290)
