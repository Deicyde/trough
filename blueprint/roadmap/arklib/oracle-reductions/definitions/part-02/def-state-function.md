---
declaration: definition
origin: cited
lean: Verifier.StateFunction
statement: formalized
---

# State Function

A **(deterministic) state function** for a verifier, with respect to input language $L_{\text{in}}$ and output language $L_{\text{out}}$, consists of a function that maps partial transcripts to boolean values, satisfying:

- For all input statements not in the language, the state function is false for the empty transcript
- If the state function is false for a partial transcript, and the next message is from the prover to the verifier, then the state function is also false for the new partial transcript regardless of the message
- If the state function is false for a full transcript, the verifier will not output a statement in the output language

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Verifier.StateFunction`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.StateFunction).

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 640](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L640)
