---
declaration: definition
origin: cited
lean: ProtocolSpec.FullTranscript.append
statement: formalized
---

# Full Transcript Append

Given full transcripts $T_1 : \mathsf{FullTranscript}\ \mathsf{pSpec}_1$ and $T_2 : \mathsf{FullTranscript}\ \mathsf{pSpec}_2$, their sequential composition is:

$$
T_1 \mathrel{++_\mathsf{t}} T_2 : \mathsf{FullTranscript}\ (\mathsf{pSpec}_1 \mathrel{++_\mathsf{p}} \mathsf{pSpec}_2)
$$

## Depends on

- [Protocol Transcript](../../definitions/part-01/def-transcript.md)

## Lean

Formalized as [`ProtocolSpec.FullTranscript.append`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProtocolSpec.FullTranscript.append).

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 23](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L23)
