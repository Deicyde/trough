---
declaration: theorem
origin: cited
lean: Sumcheck.Interaction.Native.execute_perfectCompleteness, Sumcheck.Interaction.Native.execute_soundness
statement: formalized
---

# Interaction-layer sum-check security

Over any commutative semiring and for any challenge distribution, from a true claim about a polynomial of individual degree at most $d$, the honest execution returns a true evaluation claim with probability $1$. Over a finite field $\mathbb{F}$, from a false claim with $k$ rounds remaining and uniform challenges, every prover strategy makes the output claim true with probability at most $k \cdot d / |\mathbb{F}|$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Stated as [`Sumcheck.Interaction.Native.execute_perfectCompleteness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Interaction.Native.execute_perfectCompleteness), [`Sumcheck.Interaction.Native.execute_soundness`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Sumcheck.Interaction.Native.execute_soundness); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/sumcheck.tex, line 273](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/sumcheck.tex#L273)
