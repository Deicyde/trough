---
declaration: definition
origin: cited
lean: OracleInterface.distanceLE
statement: formalized
---

# Oracle Distance

The oracle interface on $M$ has oracle distance at most $d$ if every two distinct $a \neq b$ in $M$ agree on at most $d$ queries:

$$
|\{q : \mathsf{Query} \mid \mathsf{answer}(a, q) = \mathsf{answer}(b, q)\}| \leq d.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`OracleInterface.distanceLE`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleInterface.distanceLE).

## Sources

- [ArkLib blueprint: proof_systems/simple_protocols.tex, line 162](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/simple_protocols.tex#L162)
