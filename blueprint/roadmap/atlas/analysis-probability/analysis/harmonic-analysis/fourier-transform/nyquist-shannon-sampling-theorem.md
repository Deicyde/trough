---
declaration: section
origin: cited
lean: MathlibExt.Analysis.NyquistShannonWanted.Analysis.NyquistShannon.sinc, MathlibExt.Analysis.NyquistShannonWanted.Analysis.NyquistShannon.FourierSupportedInNyquist, MathlibExt.Analysis.NyquistShannonWanted.Analysis.NyquistShannon.nyquist_shannon_sampling
statement: formalized
---

# Nyquist–Shannon sampling theorem

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/nyquist-shannon-sampling-theorem/index.html).

## Unnormalised cardinal sine

The function $\operatorname{sinc} \colon \mathbb{R} \to
\mathbb{C}$ is defined by $\operatorname{sinc}(x) = \frac{\sin x}{x}$ for $x \neq 0$ and
$\operatorname{sinc}(0) = 1$, the value that removes the singularity at $0$. Its values are real.

The Whittaker–Shannon interpolation formula evaluates $\operatorname{sinc}$ at $0$ at the integer
sample points, so the value at $0$ is part of the definition.

Formalized by `MathlibExt.Analysis.NyquistShannonWanted.Analysis.NyquistShannon.sinc`, a definition declared in [WantedExt/Analysis/NyquistShannonWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/NyquistShannonWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/nyquist-shannon-sampling-theorem/index.html#sinc).

## Fourier support in the Nyquist band

A Schwartz function
$f \colon \mathbb{R} \to \mathbb{C}$ has Fourier support in the Nyquist band when its Fourier
transform $\hat f(\xi) = \int_{\mathbb{R}} f(x)\, e^{-2\pi i x \xi}\, dx$ vanishes at every real
$\xi$ outside the closed interval $[-\frac12, \frac12]$.

Formalized by `MathlibExt.Analysis.NyquistShannonWanted.Analysis.NyquistShannon.FourierSupportedInNyquist`, a definition declared in [WantedExt/Analysis/NyquistShannonWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/NyquistShannonWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/nyquist-shannon-sampling-theorem/index.html#fourier-supported-in-nyquist).

## Nyquist–Shannon sampling theorem (Whittaker–Shannon interpolation formula)

Let
$\operatorname{sinc}(x) = \frac{\sin x}{x}$ for real $x \neq 0$ and $\operatorname{sinc}(0) = 1$,
and let $f \colon \mathbb{R} \to \mathbb{C}$ be a Schwartz function whose Fourier transform
$\hat f(\xi) = \int_{\mathbb{R}} f(x)\, e^{-2\pi i x \xi}\, dx$ vanishes at every real $\xi$
outside $[-\frac12, \frac12]$. Then for every real $t$ the series
$\sum_{n \in \mathbb{Z}} f(n) \operatorname{sinc}(\pi(n - t))$ is summable over $\mathbb{Z}$
(unconditionally convergent) and

$$
f(t) = \sum_{n \in \mathbb{Z}} f(n) \operatorname{sinc}(\pi(n - t)).
$$

## Sources

- C. E. Shannon, *Communication in the presence of noise*, Proc. IRE 37 (1949); H. Nyquist (1928); E. T. Whittaker (1915). Knill, *Some fundamental theorems in mathematics*, §179. Problem `nyquist_shannon_sampling` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.NyquistShannonWanted.Analysis.NyquistShannon.nyquist_shannon_sampling` is written with `theorem_wanted` in [WantedExt/Analysis/NyquistShannonWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/NyquistShannonWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/nyquist-shannon-sampling-theorem/index.html#nyquist-shannon-sampling).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nyquist–Shannon sampling theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/nyquist-shannon-sampling-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/nyquist-shannon-sampling-theorem)
