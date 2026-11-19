---
declaration: definition
origin: cited
lean: CoreDefinitions.IsMCA, CoreDefinitions.mcaError, CoreDefinitions.IsMCAGenerator
statement: formalized
---

# gen_mutual_corr_agreement

Let $\mathcal{C}$ be a linear code. We say that $\mathsf{Gen}$ be a proximity generator with mutual correlated agreement with proximity bounds ${\mathsf{B}}^\star$ and $\mathsf{err}^\star$, if for $f_0,\ldots,f_{\mathsf{par}\ell-1}:\mathcal{L}\rightarrow\mathbb{F}$ and $\delta\in(0,1-{\mathsf{B}}^\star(\mathcal{C},\mathsf{par}\ell))$ the following holds.

$$
\Pr_{(r_0, \ldots, r_{\mathsf{par}\ell-1}) \leftarrow \mathsf{Gen}(\mathsf{par}\ell)} \left[
\exists S \subseteq \mathcal{L} \;\; s.t.\;\;
\begin{array}{l}
|S| \geq (1 - \delta) \cdot |\mathcal{L}| \\
\land\; \exists u \in \mathcal{C}, u(S) = \sum_{j \in [0,(\mathsf{par}\ell-1)]} r_j \cdot f_j(S) \\
\land\; \exists i \in [0,(\mathsf{par}\ell-1)], \forall u' \in \mathcal{C}, u'(S) \neq f_i(S)
\end{array}\right]
\leq \mathsf{err}^\star(\mathcal{C}, \mathsf{par}\ell, \delta).
$$

In the formalization, $\mathsf{IsMCA}$ is the event in brackets for one seed, $\mathsf{mcaError}(\mathsf{Gen},\mathcal{C},\delta)$ is the supremum of its probability over all families $(f_0,\ldots,f_{\mathsf{par}\ell-1})$, and $\mathsf{IsMCAGenerator}(\mathsf{Gen},\mathsf{err}^\star,\mathcal{C})$ asserts $\mathsf{mcaError}(\mathsf{Gen},\mathcal{C},\delta)\le\mathsf{err}^\star(\delta)$ for every $\delta\in[0,1]$. A proximity bound is expressed by letting $\mathsf{err}^\star$ be $1$ beyond it.

## Depends on

- [proximity_generator](def-proximity-generator.md)

## Lean

Formalized as [`CoreDefinitions.IsMCA`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CoreDefinitions.IsMCA), [`CoreDefinitions.mcaError`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CoreDefinitions.mcaError), [`CoreDefinitions.IsMCAGenerator`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/CoreDefinitions.IsMCAGenerator).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 46](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L46)
