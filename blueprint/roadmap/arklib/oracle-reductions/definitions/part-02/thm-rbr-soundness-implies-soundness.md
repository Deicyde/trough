---
declaration: theorem
origin: cited
lean: Verifier.GuardedForm.soundness_of_rbrSoundness
statement: formalized
---

# RBR Soundness Implies Soundness

For a verifier with a guarded form, round-by-round soundness with error function $\epsilon$ implies soundness with error $\sum_i \epsilon(i)$, where the sum is over all challenge rounds $i$, for arbitrary shared-oracle state and provers.

## Depends on

- [Round-by-Round Soundness](def-round-by-round-soundness.md)
- [Soundness](def-soundness.md)
- [Guarded Verifier](def-guarded-verifier.md)

## Lean

Stated as [`Verifier.GuardedForm.soundness_of_rbrSoundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Verifier.GuardedForm.soundness_of_rbrSoundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: oracle_reductions/defs.tex, line 791](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/oracle_reductions/defs.tex#L791)
