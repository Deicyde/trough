---
declaration: definition
origin: cited
lean: ProtocolSpec.Transcript, ProtocolSpec.FullTranscript, ProtocolSpec.Messages, ProtocolSpec.Challenges
statement: formalized
---

# Protocol Transcript

Given protocol specification $\mathsf{pSpec} : \mathsf{ProtocolSpec}\ n$, we define:

- A *transcript* up to round $k : \mathsf{Fin}\ (n + 1)$ is an element of type

    $$
    \mathsf{Transcript}\ k\ \mathsf{pSpec} := (i : \mathsf{Fin}\ k) \to \mathsf{pSpec}.\mathsf{Type}\ (\uparrow i : \mathsf{Fin}\ n)
    $$

    where $\uparrow i : \mathsf{Fin}\ n$ denotes casting $i : \mathsf{Fin}\ k$ to $\mathsf{Fin}\ n$ (valid since $k \leq n + 1$).

- A *full transcript* is $\mathsf{FullTranscript}\ \mathsf{pSpec} := (i : \mathsf{Fin}\ n) \to \mathsf{pSpec}.\mathsf{Type}\ i$.

- The type of all *messages* from prover to verifier is

    $$
    \mathsf{pSpec}.\mathsf{Messages} := \prod_{i : \mathsf{pSpec}.\mathsf{MessageIdx}} \mathsf{pSpec}.\mathsf{Message}\ i
    $$

- The type of all *challenges* from verifier to prover is

    $$
    \mathsf{pSpec}.\mathsf{Challenges} := \prod_{i : \mathsf{pSpec}.\mathsf{ChallengeIdx}} \mathsf{pSpec}.\mathsf{Challenge}\ i
    $$

## Depends on

- [Protocol Specification](def-protocol-spec.md)
- [Protocol Specification Components](def-protocol-spec-components.md)

## Lean

Formalized as [`ProtocolSpec.Transcript`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.Transcript), [`ProtocolSpec.FullTranscript`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.FullTranscript), [`ProtocolSpec.Messages`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.Messages), [`ProtocolSpec.Challenges`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.Challenges).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 134](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/defs.tex#L134)
