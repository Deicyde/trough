---
declaration: section
origin: cited
lean: ZMod.invDFT_mul_dft
statement: formalized
proof: formalized
---

# Discrete Fourier analysis: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/index.html).

Fourier analysis on finite abelian groups and the Boolean cube: DFT and FFT, Plancherel, finite uncertainty, Young and Hausdorff–Young, Riesz–Thorin on finite sets, influences and noise operators.

## Convolution theorem for the discrete Fourier transform

Let $n \ge 1$. For
$\varphi : \mathbb{Z}/n\mathbb{Z} \to \mathbb{C}$ write
$\hat\varphi(k) = \sum_{j \in \mathbb{Z}/n\mathbb{Z}} e^{-2\pi i jk/n} \varphi(j)$ for its discrete
Fourier transform, and let $\mathcal{F}^{-1}$ be the inverse of the map
$\varphi \mapsto \hat\varphi$. Then for all $f, g : \mathbb{Z}/n\mathbb{Z} \to \mathbb{C}$ and every
$t \in \mathbb{Z}/n\mathbb{Z}$, the value at $t$ of $\mathcal{F}^{-1}$ applied to
$k \mapsto \hat f(k)\,\hat g(k)$ equals the circular convolution
$\sum_{j \in \mathbb{Z}/n\mathbb{Z}} f(j)\,g(t - j)$.

## Sources

- MIT 6.046J Spring 2015 Lecture 3, polynomial product theorem, cyclic form.

Formalized by `ZMod.invDFT_mul_dft`, a theorem declared in [MathlibExt/Analysis/Fourier/ZModConvolution.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/ZModConvolution.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/index.html#inv-dft-mul-dft).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrete Fourier analysis](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/discrete-fourier-analysis)
