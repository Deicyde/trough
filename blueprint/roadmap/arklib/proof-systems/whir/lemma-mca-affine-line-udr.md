---
declaration: lemma
origin: cited
lean: ProximityGap.mcaError_le_epsCa_of_two_mul_lt_dist
statement: formalized
---

# Affine-line case

Let $\mathcal{C}\subseteq\mathbb{F}^{\mathcal{L}}$ be a linear code with minimum (absolute) distance $d_{\mathcal{C}}$, and let $\mathsf{Gen}(\alpha)=(1,\alpha)$ be the affine-line generator. For every $\delta>0$ with $2\delta|\mathcal{L}|\lt d_{\mathcal{C}}$,

$$
\mathsf{mcaError}(\mathsf{Gen},\mathcal{C},\delta)\le\mathsf{caError}(\mathsf{Gen},\mathcal{C},\delta,\delta).
$$

## Depends on

- [proximity_generator](def-proximity-generator.md)
- [gen_mutual_corr_agreement](def-gen-mutual-corr-agreement.md)

## Lean

Stated as [`ProximityGap.mcaError_le_epsCa_of_two_mul_lt_dist`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.mcaError_le_epsCa_of_two_mul_lt_dist); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 76](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L76)
