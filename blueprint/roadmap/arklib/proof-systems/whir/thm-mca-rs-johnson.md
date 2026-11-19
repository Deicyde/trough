---
declaration: theorem
origin: cited
lean: RSCode.isMCAGenerator_univariatePowersGenerator, RSCode.reedSolomonMCAError
statement: formalized
---

# Mutual correlated agreement up to the Johnson bound

Let $\mathcal{C} := \mathrm{RS}[\mathbb{F}, \mathcal{L}, d]$ with $d\ge1$, block length $n=|\mathcal{L}|$ and rate $\rho$, and let $\mathsf{Gen}(\mathsf{par}\ell;\alpha)=(1,\alpha,\ldots,\alpha^{\mathsf{par}\ell-1})$ with $\mathsf{par}\ell\ge1$. For every integer $s\ge3$, $\mathsf{Gen}$ has mutual correlated agreement for $\mathcal{C}$ with error

$$
\mathsf{err}^\star(\delta)=
\begin{cases}
\dfrac{(\mathsf{par}\ell-1)\, n^2\,(s+\frac12)^7}{3\,\rho^{3/2}\,|\mathbb{F}|}
& \text{if } \delta\le 1-\left(1+\frac{1}{2s}\right)\sqrt{\rho},\\[8pt]
1 & \text{otherwise.}
\end{cases}
$$

## Depends on

- [gen_mutual_corr_agreement](def-gen-mutual-corr-agreement.md)
- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)

## Lean

Stated as [`RSCode.isMCAGenerator_univariatePowersGenerator`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RSCode.isMCAGenerator_univariatePowersGenerator), [`RSCode.reedSolomonMCAError`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/RSCode.reedSolomonMCAError); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 109](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L109)
