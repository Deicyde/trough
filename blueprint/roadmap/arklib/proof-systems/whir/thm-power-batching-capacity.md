---
declaration: theorem
origin: cited
lean: ReedSolomon.exists_capacity_powerBatchingAgreement
statement: formalized
---

# Power-batching agreement up to capacity

For every $\eta>0$ there are $N\ge4$, $d\in\mathbb{N}$, $\nu\lt N$ and $C>0$, depending only on $\eta$, with the following property. These constants differ from those of Theorem [Mutual correlated agreement up to capacity, for lines and affine spaces](thm-mca-rs-capacity.md). Let $\mathsf{par}\ell\ge2$, $n\ge N$, $k>0$ and an integer $A$ with $A\ge k+\eta n$. Let $\mathbb{F}$ be a field such that $k=1$, or $\mathbb{F}$ has characteristic $0$, or its characteristic is larger than $\max(k-1,\nu)$. Let $\mathcal{L}\subseteq\mathbb{F}$ have $n$ elements, and let $f_0,\ldots,f_{\mathsf{par}\ell-1}:\mathcal{L}\to\mathbb{F}$. Then there is a set of at most $(\mathsf{par}\ell-1)\,C\,n^{d+1}$ exceptional challenges $z\in\mathbb{F}$. For every $z$ outside it and every polynomial $Q$ of degree less than $k$ that agrees with $\sum_{t}z^t f_t$ on at least $A$ points, there are polynomials $P_0,\ldots,P_{\mathsf{par}\ell-1}$ of degree less than $k$ with $Q=\sum_t z^t P_t$, and the agreement set of $Q$ is the set of points where every $P_t$ agrees with $f_t$. The field may be infinite. This is ([Dao et al. 2026](https://eprint.iacr.org/2026/2056)), Corollary 7.3. It is an exact agreement statement, not a bound on $\mathsf{mcaError}$ of the powers generator.

## Depends on

- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)

## Lean

Stated as [`ReedSolomon.exists_capacity_powerBatchingAgreement`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReedSolomon.exists_capacity_powerBatchingAgreement); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 148](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L148)
