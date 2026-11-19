---
declaration: lemma
origin: cited
lean: ProximityGap.rs_mcaError_le_of_le_relUDR
statement: formalized
---

# mca_rs_udr

Let $\mathcal{C} := \mathrm{RS}[\mathbb{F}, \mathcal{L}, d]$ be a Reed Solomon code with minimum distance $d_{\mathcal{C}}$, and let $\mathsf{Gen}(\alpha)=(1,\alpha)$. For every $\delta$ with $0\lt \delta\le\frac{(d_{\mathcal{C}}-1)/2}{|\mathcal{L}|}$ (the relative unique-decoding radius),

$$
\mathsf{mcaError}(\mathsf{Gen},\mathcal{C},\delta)\le\frac{|\mathcal{L}|}{|\mathbb{F}|}.
$$

## Depends on

- [Affine-line case](lemma-mca-affine-line-udr.md)
- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)

## Lean

Stated as [`ProximityGap.rs_mcaError_le_of_le_relUDR`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.rs_mcaError_le_of_le_relUDR); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 88](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L88)
