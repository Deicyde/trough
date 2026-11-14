---
declaration: theorem
origin: cited
lean: ProximityGap.iterated_folding_reflects_balls
statement: formalized
proof: formalized
---

# folding_preserves_listdecoding

Suppose that for each $i\lt k$ the generator $\mathsf{Gen}(2; \alpha) = (1, \alpha)$ has mutual correlated agreement for $\mathcal{C}^{(i+1)}$ with error $\mathsf{err}^\star_i$. Then for every $f : \mathcal{L} \to \mathbb{F}$ and every $\delta \in (0,1]$ with $\delta<1-\rho(\mathcal{C}^{(i+1)})$ for each $i\lt k$,

$$
\Pr_{\vec\alpha \leftarrow \mathbb{F}^k} \left[
\mathrm{Fold_S}(\Lambda_{r}(\mathcal{C}, 0, k, f, \delta), \vec\alpha)
\neq \Lambda(\mathcal{C}^{(k)}, \mathrm{Fold}(f, \vec\alpha), \delta)
\right] \le \sum_{i\lt k}\mathsf{err}^\star_i(\delta).
$$

## Depends on

- [folding_preserves_listdecoding_base](lemma-folding-preserves-listdecoding-base.md)
- [folding_preserves_listdecoding_bound](lemma-folding-preserves-listdecoding-bound.md)

## Proof

Apply Lemma [folding_preserves_listdecoding_base](lemma-folding-preserves-listdecoding-base.md) to each of the $k$ independent folding rounds and take a union bound.

## Lean

Formalized as [`ProximityGap.iterated_folding_reflects_balls`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.iterated_folding_reflects_balls).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 311](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L311)
