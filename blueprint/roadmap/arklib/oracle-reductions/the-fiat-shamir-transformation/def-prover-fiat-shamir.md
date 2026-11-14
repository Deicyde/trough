---
declaration: definition
origin: cited
lean: Prover.fiatShamir
statement: formalized
---

# Fiat-Shamir Prover Transformation

Given an interactive prover $P$ for $\mathsf{pSpec}$, the transformation produces a non-interactive prover

$$
P.\mathsf{fiatShamir} : \mathsf{NonInteractiveProver}\ (\forall i, \mathsf{pSpec}.\mathsf{Message}\ i)\ (\mathsf{oSpec} \mathrel{+} \mathsf{srChallengeOracle}\ \mathsf{StmtIn}\ \mathsf{pSpec})\ \mathsf{StmtIn}\ \mathsf{WitIn}\ \mathsf{StmtOut}\ \mathsf{WitOut} .
$$

Its state at round $0$ pairs the statement with $P$'s initial state; afterwards it is $P$'s final state. Its single message is the vector of all of $P$'s messages, computed by $\mathsf{runToRoundFS}$ up to the last round. It receives no challenges and outputs through $P$'s output function.

## Depends on

- [Fiat-Shamir Prover Execution](def-prover-run-to-round-fs.md)

## Lean

Formalized as [`Prover.fiatShamir`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.fiatShamir).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 81](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L81)
