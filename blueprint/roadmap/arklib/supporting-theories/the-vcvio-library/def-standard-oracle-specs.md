---
declaration: definition
origin: cited
lean: OracleSpec.emptySpec, coinSpec, unifSpec
statement: formalized
---

# Standard Oracle Specifications

- $A \to_{\mathsf{o}} B$: oracles that take inputs in $A$ and answer every query in $B$.
- `emptySpec`, written $[]_{\mathsf{o}}$: no oracles.
- `coinSpec` $= \mathsf{Unit} \to_{\mathsf{o}} \mathsf{Bool}$: a coin-flipping oracle.
- `unifSpec`: indexed by $n \in \mathbb{N}$, the query $n$ is answered in $\mathsf{Fin}\ (n+1) = \{0, \ldots, n\}$; with uniform answers it samples uniformly from this set.

Specifications combine by disjoint sum $\mathsf{spec}_1 + \mathsf{spec}_2$.

## Depends on

- [Specification of Oracles](def-oracle-spec.md)

## Lean

Formalized as [`OracleSpec.emptySpec`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleSpec.emptySpec), [`coinSpec`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/coinSpec), [`unifSpec`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/unifSpec).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 23](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L23)
