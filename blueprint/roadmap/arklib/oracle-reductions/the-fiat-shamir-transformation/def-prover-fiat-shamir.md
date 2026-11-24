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

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 81](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/fiat_shamir.tex#L81)
