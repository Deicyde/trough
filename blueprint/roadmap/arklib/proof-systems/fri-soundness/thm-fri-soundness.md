---
declaration: theorem
origin: cited
lean: Fri.Spec.soundness, Fri.Spec.soundness_proximity, Fri.Spec.rbr_soundness
statement: formalized
proof: formalized
---

# fri-soundness

The specified FRI oracle reduction has round-by-round error equal to the powers-MCA error at each folding challenge and $(1-\min\{\theta,\delta\})^t$ at its final query-vector challenge. Its ordinary soundness error is the sum of these errors, against every adaptive prover. More strongly, this bounds any acceptance when the input has distance at least $\delta$ from its initial code.

## Depends on

- [fri-folding-error](thm-fri-folding-error.md)
- [fri-query-error](thm-fri-query-error.md)

## Proof

Use the actual protocol transcript, including the retained committed words and the terminal polynomial. A persistent state records that the input is valid or a bad challenge has occurred. Prover messages cannot create this state. The conditional probability of each fresh bad event is bounded by the appropriate folding or query theorem. The executable verifier accepts exactly the final query event, including the terminal degree guard, so it rejects whenever the persistent state is false. This supplies round-by-round soundness through ArkLib's fixed-prefix interface. Separately, induction over the actual stateful prover execution accumulates the conditional errors and proves ordinary soundness.

## Lean

Formalized as [`Fri.Spec.soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.soundness), [`Fri.Spec.soundness_proximity`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.soundness_proximity), [`Fri.Spec.rbr_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.rbr_soundness).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 100](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L100)
