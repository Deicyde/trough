---
declaration: definition
origin: cited
lean: Domain.CosetFftDomain.twoNthRoot
statement: formalized
---

# extract

Let $\mathsf{extract}:\mathcal{L}^{2^{k+1}}\rightarrow \mathcal{L}^{2^k}$ be a function. There exists $x \in \mathcal{L}$, such that $y = x^{2^{k+1}}\in\mathcal{L}^{2^{k+1}}$. Then $\mathsf{extract}$ returns $z = \sqrt{y} = x^{2^k}\in\mathcal{L}^{2^k}$ such that $y = z^2$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Domain.CosetFftDomain.twoNthRoot`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Domain.CosetFftDomain.twoNthRoot).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 212](https://github.com/Verified-zkEVM/ArkLib/blob/e9bcc82d3d33a1814822b9b9e6b135bc80d614ee/blueprint/src/proof_systems/whir.tex#L212)
