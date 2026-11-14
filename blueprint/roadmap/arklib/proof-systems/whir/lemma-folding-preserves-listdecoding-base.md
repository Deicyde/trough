---
declaration: lemma
origin: cited
lean: ProximityGap.folding_reflects_balls
statement: formalized
---

# folding_preserves_listdecoding_base

Denote $\mathcal{C}' := \mathcal{C}^{(1)} = \mathrm{RS}[\mathbb{F}, \mathcal{L}^{2}, 2^{m - 1}]$, and suppose that $\mathsf{Gen}(2;\alpha)=(1,\alpha)$ has mutual correlated agreement for $\mathcal{C}'$ with error $\mathsf{err}^\star$. Then for every $f : \mathcal{L} \to \mathbb{F}$ and $\delta \in (0, 1 - \rho(\mathcal{C}'))$,

$$
\Pr_{\alpha \leftarrow \mathbb{F}} \left[
\mathrm{Fold_S}(\Lambda_{r}(\mathcal{C}, 0, k, f, \delta), \alpha)
\neq \Lambda_{r}(\mathcal{C}', 1, k, \mathrm{Fold}(f, \alpha), \delta)
\right] \le \mathsf{err}^\star(\delta).
$$

## Depends on

- [list_close_codewords_block](def-list-close-codewords-block.md)
- [fold_k](def-fold-k.md)

## Lean

Stated as [`ProximityGap.folding_reflects_balls`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.folding_reflects_balls); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 331](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L331)
