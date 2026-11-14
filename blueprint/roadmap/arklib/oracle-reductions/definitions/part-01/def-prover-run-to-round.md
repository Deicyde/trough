---
declaration: definition
origin: cited
lean: Prover.runToRound, Prover.processRound
statement: formalized
---

# Prover Execution to Round

The execution of a prover up to round $i : \mathsf{Fin}(n+1)$ is defined inductively:

$$
\mathsf{Prover}.\mathsf{runToRound}(i, \mathsf{stmt}, \mathsf{wit}) :=
$$

$$
\mathsf{Fin}.\mathsf{induction}(
$$

$$
\quad \mathsf{pure}(\langle \mathsf{default}, \mathsf{prover}.\mathsf{input}(\mathsf{stmt}, \mathsf{wit}) \rangle),
$$

$$
\quad \mathsf{prover}.\mathsf{processRound},
$$

$$
\quad i
$$

$$
)
$$

where $\mathsf{processRound}$ handles individual rounds by either:

- **Verifier Challenge** ($\mathsf{pSpec}.\mathsf{dir}(j) = \mathsf{V\_to\_P}$): Query for a challenge and update prover state
- **Prover Message** ($\mathsf{pSpec}.\mathsf{dir}(j) = \mathsf{P\_to\_V}$): Generate message via $\mathsf{sendMessage}$ and update state

Returns the transcript up to round $i$ and the prover's state after round $i$.

## Depends on

- [Type Signature of a Prover](def-prover.md)
- [Protocol Specification](def-protocol-spec.md)
- [Protocol Transcript](def-transcript.md)

## Lean

Formalized as [`Prover.runToRound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.runToRound), [`Prover.processRound`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Prover.processRound).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 327](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L327)
