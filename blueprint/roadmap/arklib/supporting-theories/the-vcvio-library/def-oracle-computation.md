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

- [ArkLib blueprint: vcv/defs.tex, line 42](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/vcv/defs.tex#L42)
