---
declaration: definition
origin: cited
lean: ProtocolSpec
statement: formalized
---

# Protocol Specification

A protocol specification for an $n$-message (oracle) reduction, is an element of the following type:

$$
\begin{aligned}
\mathsf{ProtocolSpec}\ n &:= \mathsf{Fin}\ n \to \mathsf{Direction} \times \mathsf{Type}.
\end{aligned}
$$

In the above, $\mathsf{Direction} := \{ \mathsf{P \!\!\rightarrow\!\! V}, \mathsf{V \!\!\rightarrow\!\! P} \}$ is the type of possible directions of messages, and $\mathsf{Fin}\ n := \{ i : \mathbb{N} \mathbin{/\!/} i < n \}$ is the type of all natural numbers less than $n$.

In other words, for each step $i$ of interaction, the protocol specification describes the *direction* of the message sent in that step, i.e., whether it is from the prover or from the verifier. It also describes the *type* of that message.

In the oracle setting, we also expect an oracle interface for each message from the prover to the verifier.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`ProtocolSpec`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 101](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L101)
