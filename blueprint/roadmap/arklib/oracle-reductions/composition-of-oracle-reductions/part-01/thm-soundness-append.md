---
declaration: theorem
origin: cited
lean: Verifier.append_soundness
statement: formalized
---

# Soundness Preservation under Append

Suppose $V_1$ is guarded and sound with error $\epsilon_1$ from the initial distribution $\mu$, and $V_2$ is sound with error $\epsilon_2$ from every deterministic shared state. Then $V_1.\mathsf{append}\ V_2$ is sound from $\mu$ with error $\epsilon_1 + \epsilon_2$. The second verifier needs no guard. Some restriction is necessary: a later verifier that queries the shared oracle can be steered by the prover's queries in an earlier stage. The every-state hypothesis is needed because the intermediate statement is chosen after oracle answers; it holds for lazily sampled oracles and fails for states that hide a secret from the prover.

## Depends on

- [Guarded Verifier](../../definitions/part-02/def-guarded-verifier.md)
- [Soundness](../../definitions/part-02/def-soundness.md)
- [Verifier Append](def-verifier-append.md)

## Lean

Stated as [`Verifier.append_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.append_soundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/composition.tex, line 157](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/oracle_reductions/composition.tex#L157)
