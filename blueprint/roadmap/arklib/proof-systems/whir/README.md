# WHIR

## Tools for Reed Solomon codes

### Mutual Correlated Agreement as a Proximity Generator

- [proximity_generator](def-proximity-generator.md)
- [gen_mutual_corr_agreement](def-gen-mutual-corr-agreement.md)
- [Affine-line case](lemma-mca-affine-line-udr.md)
- [mca_rs_udr](lemma-mca-rs-udr.md)

**Remark.** ([Arnon et al. 2024](https://eprint.iacr.org/2024/1586)) states Lemma [mca_rs_udr](lemma-mca-rs-udr.md) for every $\mathsf{par}\ell$: the generator $\mathsf{Gen}(\mathsf{par}\ell; \alpha) = (1, \alpha, \ldots, \alpha^{\mathsf{par}\ell - 1})$ has mutual correlated agreement for $\mathrm{RS}[\mathbb{F}, \mathcal{L}, 2^m]$ with proximity bound ${\mathsf{B}}^\star(\mathcal{C}, \mathsf{par}\ell) := \frac{1 + \rho}{2}$ and error $\mathsf{err}^\star(\mathcal{C}, \mathsf{par}\ell, \delta) = \frac{(\mathsf{par}\ell - 1) \cdot 2^m}{\rho \cdot |\mathbb{F}|}$. Only the case $\mathsf{par}\ell=2$ is formalized; there the error is $2^m/(\rho|\mathbb{F}|)=|\mathcal{L}|/|\mathbb{F}|$.

- [Mutual correlated agreement up to the Johnson bound](thm-mca-rs-johnson.md)
- [Mutual correlated agreement up to capacity, for lines and affine spaces](thm-mca-rs-capacity.md)
- [Power-batching agreement up to capacity](thm-power-batching-capacity.md)

**Remark (Conjecture of (Arnon et al. 2024), not formalized).** The function $\mathsf{Gen}(\mathsf{par}\ell; \alpha) := (1, \alpha, \ldots, \alpha^{\mathsf{par}\ell - 1})$ is conjectured to be a proximity generator with mutual correlated agreement for every smooth Reed Solomon code $\mathcal{C} := \mathrm{RS}[\mathbb{F}, \mathcal{L}, 2^m]$ (with rate $\rho := 2^m / |\mathcal{L}|$), with the following parameters:

1. *Up to the Johnson bound:* ${\mathsf{B}}^\star(\mathcal{C}, \mathsf{par}\ell) := \sqrt{\rho},$ *and*

    $$
    \mathsf{err}^\star(\mathcal{C}, \mathsf{par}\ell, \delta) := \frac{(\mathsf{par}\ell - 1) \cdot 2^m}{|\mathbb{F}| \cdot \left( 2 \cdot \min\left\{1 - \sqrt{\rho} - \delta, \frac{\sqrt{\rho}}{20} \right\} \right)^7}.
    $$

2. *Up to capacity:* ${\mathsf{B}}^\star(\mathcal{C}, \mathsf{par}\ell) := \rho$, *and there exist constants $c_1, c_2, c_3 \in \mathbb{N}$ such that for every $\eta > 0$ and $0 < \delta < 1 - \rho - \eta$:*

    $$
    \mathsf{err}^\star(\mathcal{C}, \mathsf{par}\ell, \delta) := \frac{(\mathsf{par}\ell - 1)^{c_2} \cdot \delta^{c_2}}{\eta^{c_1} \cdot \rho^{c_1 + c_2} \cdot |\mathbb{F}|}.
    $$

Neither part is formalized in this form. Theorem [Mutual correlated agreement up to the Johnson bound](thm-mca-rs-johnson.md) proves a Johnson-range bound whose error grows with $n^2$ and whose radius is $1-(1+\frac{1}{2s})\sqrt{\rho}$. Theorem [Mutual correlated agreement up to capacity, for lines and affine spaces](thm-mca-rs-capacity.md) proves a capacity-range bound for $\mathsf{par}\ell=2$ (lines) and for affine spaces; its error grows polynomially with $n$, and it requires the characteristic condition above. For powers with $\mathsf{par}\ell>2$, Theorem [Power-batching agreement up to capacity](thm-power-batching-capacity.md) proves exact power-batching agreement up to capacity, under its own constants and a stronger characteristic condition. The library does not state that result as a bound on the MCA error of the powers generator.

### Folding univariate functions

In this subsection $\mathcal{L}$ is a smooth coset FFT domain of size $2^n$. The formalization represents a function on $\mathcal{L}^{2^i}$ as a word indexed by $\{0,\ldots,2^{n-i}-1\}$ over the subdomain $\mathcal{L}^{2^i}$.

- [extract](def-extract.md)
- [foldf](def-foldf.md)
- [fold_k](def-fold-k.md)
- [fold_fg](lemma-fold-fg.md)

### Block relative distance

- [block](def-block.md)

For $0\le i\le m$ write $\mathcal{C}^{(i)} := \mathrm{RS}[\mathbb{F}, \mathcal{L}^{2^i}, 2^{m-i}]$ for the smooth Reed Solomon code on the folded domain $\mathcal{L}^{2^i}$. In the block definitions below, the words and the code always live on the same domain $\mathcal{L}^{2^i}$.

- [block_rel_distance](def-block-rel-distance.md)
- [min_block_rel_distance](def-min-block-rel-distance.md)

Note that $\Delta_{r}(\mathcal{C}^{(0)}, 0, 0, f, g) = \Delta(f, g)$. We define the block list decoding of a codeword.

- [list_close_codewords_block](def-list-close-codewords-block.md)
- [block_rel_distance](lemma-block-rel-distance.md)

### Folding preserves list decoding

Throughout, $\mathcal{C} = \mathcal{C}^{(0)} = \mathrm{RS}[\mathbb{F}, \mathcal{L}, 2^m]$ with $\mathcal{L}$ a smooth coset FFT domain of size $2^n$, $1 \le k \leq m\le n$, and $\mathcal{C}^{(i)}$ as defined above. The formalization bounds the failure probabilities with a mutual-correlated-agreement error that is total in $\delta$, so it needs only $\delta<1-\rho(\mathcal{C}^{(i)})$ where ([Arnon et al. 2024](https://eprint.iacr.org/2024/1586)) assumes $\delta<1-{\mathsf{B}}^\star(\mathcal{C}^{(i)},2)$. Every regime of ([Arnon et al. 2024](https://eprint.iacr.org/2024/1586)) has ${\mathsf{B}}^\star\ge\rho$, so the paper's range implies this one.

- [folding_preserves_listdecoding](thm-folding-preserves-listdecoding.md)
- [folding_preserves_listdecoding_base](lemma-folding-preserves-listdecoding-base.md)
- [folding_preserves_listdecoding_bound](lemma-folding-preserves-listdecoding-bound.md)
