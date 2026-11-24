---
declaration: definition
origin: cited
lean: OracleComp
statement: formalized
---

# Oracle Computation

An oracle computation `OracleComp spec` $\alpha$ is a program that makes queries to the oracles of `spec` and returns a value of type $\alpha$. It is the free monad of the polynomial functor of `spec`, so every computation either

- returns a value without making any queries (`pure`), or
- makes one query $t$ and continues with a function of the answer in `spec.Range t` (`queryBind`).

There is no failure constructor. Computations that may fail are written in `OptionT (OracleComp spec)`. Computations whose only oracle is `unifSpec` are called probabilistic computations, `ProbComp`.

## Depends on

- [Specification of Oracles](def-oracle-spec.md)

## Lean

Formalized as [`OracleComp`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/OracleComp).

## Sources

- [ArkLib blueprint: vcv/defs.tex, line 42](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/vcv/defs.tex#L42)
