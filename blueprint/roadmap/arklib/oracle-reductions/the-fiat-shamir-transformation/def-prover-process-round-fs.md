---
declaration: definition
origin: cited
lean: Prover.processRoundFS
statement: formalized
---

# Fiat-Shamir Round Processing

Given the prover messages so far, the input statement and the prover state before round $j$, $\mathsf{processRoundFS}\ j$ computes the same data after round $j$:

- If $j$ is a challenge round, it queries the challenge oracle at $\langle j, (x, m) \rangle$, where $x$ is the statement and $m$ the messages so far, and passes the answer to the prover's $\mathsf{receiveChallenge}$.
- If $j$ is a message round, it runs the prover's $\mathsf{sendMessage}$ and appends the message.

Only prover messages are accumulated; challenges are not stored.

## Depends on

- [Challenge Oracle Specification](def-fiat-shamir-spec.md)

## Lean

Formalized as [`Prover.processRoundFS`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.processRoundFS).

## Sources

- [ArkLib blueprint: oracle_reductions/fiat_shamir.tex, line 53](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/fiat_shamir.tex#L53)
