---
declaration: lemma
origin: cited
lean: Combine.combine_theorem
statement: formalized
---

# combine

Let $d^*\ge1$ be a target degree, $f_0,\ldots,f_{m-1}:\mathcal{L}\rightarrow\mathbb{F}$ be functions, $0\leq d_0,\ldots,d_{m-1}\leq d^*$ be degrees, $\delta\in(0,\min{\{1-{\mathsf{B}}^*(\rho),1-\rho-1/|\mathcal{L}|\}})$ be a distance parameter, where $\rho=d^*/|\mathcal{L}|$. If

$$
\Pr_{r\gets\mathbb{F}}[\Delta(\mathsf{Combine}(d^*,r,(f_0,d_0),\ldots,(f_{m-1},d_{m-1})),\mathrm{RS}[\mathbb{F},\mathcal{L},d^*])\le\delta]>\mathsf{err}^*(d^*,\rho,\delta,m\cdot(d^*+1)-\sum_{i=0}^{m-1}d_i),
$$

then there exists $S\subseteq \mathcal{L}$ with $|S|\geq(1-\delta)\cdot|\mathcal{L}|$, and

$$
\forall i\in\{0,\ldots,m-1\},\exists u\in\mathrm{RS}[\mathbb{F},\mathcal{L},d_i], f_i(S)=u(S).
$$

Note that this implies $\Delta(f_i,\mathrm{RS}[\mathbb{F},\mathcal{L},d_i])\le\delta$ for every $i$. Above, ${\mathsf{B}}^*$ and ${\mathsf{err}}^*$ are the proximity bound and error (respectively) described in the proximity gap theorem.

## Depends on

- [Reed-Solomon Code](../../supporting-theories/coding-theory/def-reed-solomon-code.md)
- [combine](def-combine.md)
- [deg_corr](def-deg-corr.md)
- [proximity_gap](thm-proximity-gap.md)

## Lean

Stated as [`Combine.combine_theorem`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Combine.combine_theorem); the blueprint marks no proof of it as formalized.

## Sources

- [ArkLib blueprint: proof_systems/stir.tex, line 258](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/stir.tex#L258)
