---
declaration: definition
origin: cited
lean: ProximityGap.caError
statement: formalized
---

# proximity_generator

Let $\mathcal{C}\subseteq \mathbb{F}^{\mathcal{L}}$ be a linear code. We say that $\mathsf{Gen}$ is a proximity generator for $\mathcal{C}$ with proximity bounds ${\mathsf{B}}$ and $\mathsf{err}$ if the following implication holds for $f_0,\ldots,f_{\mathsf{par}\ell-1} : \mathcal{L} \rightarrow \mathbb{F}$ and $\delta\in(0,1-{\mathsf{B}}(\rho,\mathsf{par}\ell))$. If

$$
\begin{aligned}
\Pr_{r_0,\ldots,r_{\mathsf{par}\ell-1}\leftarrow \mathsf{Gen}}[\Delta(\sum_{i\in[0,(\mathsf{par}\ell-1)]} r_i \cdot f_i, \mathcal{C}) \le \delta] > err(\mathcal{C},\mathsf{par}\ell,\delta),
\end{aligned}
$$

then there exists $S\subseteq \mathcal{L}$, $|S|\ge(1-\delta)\cdot|\mathcal{L}|$, and $\forall i \in [0, (\mathsf{par}\ell-1)]$, $\exists u \in \mathcal{C}, \forall x \in S$, $f_i(x)=u(x)$.

The formalization records the least admissible error as a function: the correlated-agreement error $\mathsf{caError}(\mathsf{Gen},\mathcal{C},\delta,\delta)$ is the supremum, over word stacks $(f_0,\ldots,f_{\mathsf{par}\ell-1})$ that are not jointly $\delta$-close to $\mathcal{C}$, of the probability above. Thus $\mathsf{Gen}$ is a proximity generator with error $\mathsf{err}$ at $\delta$ exactly when $\mathsf{caError}(\mathsf{Gen},\mathcal{C},\delta,\delta)\le\mathsf{err}(\mathcal{C},\mathsf{par}\ell,\delta)$.

## Depends on

- [Linear Code](../../supporting-theories/coding-theory/def-linear-code.md)
- [Distance from a Code](../../supporting-theories/coding-theory/def-distance-from-code.md)

## Lean

Formalized as [`ProximityGap.caError`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ProximityGap.caError).

## Sources

- [ArkLib blueprint: proof_systems/whir.tex, line 11](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/whir.tex#L11)
