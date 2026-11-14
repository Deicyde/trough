---
declaration: definition
origin: cited
lean: Fri.FoldingAgreementFailure
statement: formalized
---

# fri-folding-failure

For a tradeoff parameter $\theta$, a challenge $\alpha$ is bad if there exists $T\subseteq D'$ of size at least $(1-\theta)|D'|$ such that the folded word agrees with $C'$ on $T$, but no codeword in $C$ agrees with $f$ on the whole preimage of $T$. The parameter $\theta$ is independent of the input distance.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Fri.FoldingAgreementFailure`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.FoldingAgreementFailure).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 31](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L31)
