---
declaration: theorem
origin: cited
lean: ReedSolomon.exists_capacity_mcaError
statement: formalized
---

# Mutual correlated agreement up to capacity, for lines and affine spaces

For every $\eta>0$ there are $N\ge4$, $d\in\mathbb{N}$ and $C>0$, depending only on $\eta$, with the following property. Let $n\ge N$ and $0\lt k\le n$, let $\mathbb{F}$ be a finite field whose characteristic is $0$ or larger than $k-1$, let $\mathcal{L}\subseteq\mathbb{F}$ have $n$ elements, and let $\delta:=1-k/n-\eta$. Then

$$
\mathsf{mcaError}((1,\alpha),\mathrm{RS}[\mathbb{F},\mathcal{L},k],\delta)\le
\frac{C\,n^{d+1}}{|\mathbb{F}|},
$$

and for every $s\in\mathbb{N}$ the affine-space generator $(\alpha_1,\ldots,\alpha_s)\mapsto(1,\alpha_1,\ldots,\alpha_s)$ satisfies

$$
\mathsf{mcaError}((1,\alpha_1,\ldots,\alpha_s),\mathrm{RS}[\mathbb{F},\mathcal{L},k],\delta)\le
\frac{C\,n^{d+1}}{|\mathbb{F}|-1}.
$$

This is ([Dao et al. 2026](https://eprint.iacr.org/2026/2056)), Theorem 6.9 and Corollary 7.2.

## Depends on

- [gen_mutual_corr_agreement](def-gen-mutual-corr-agreement.md)
- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)

## Lean

Stated as [`ReedSolomon.exists_capacity_mcaError`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReedSolomon.exists_capacity_mcaError); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 127](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L127)
