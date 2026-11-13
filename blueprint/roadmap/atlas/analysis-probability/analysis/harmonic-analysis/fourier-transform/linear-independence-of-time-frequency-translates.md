---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FourFunctionHRTWanted.modulationOne, MathlibExt.Analysis.FourFunctionHRTWanted.conjecture, MathlibExt.Analysis.FourFunctionHRTWanted.conjecture_holds
statement: formalized
---

# Linear independence of time–frequency translates

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/linear-independence-of-time-frequency-translates/index.html).

## Frequency-one modulation factor

The function $\mathbb{R} \to \mathbb{C}$ given by
$x \mapsto e^{2\pi i x}$; multiplying a function by it modulates that function by frequency one.

Formalized by `MathlibExt.Analysis.FourFunctionHRTWanted.modulationOne`, a definition declared in [WantedExt/Analysis/FourFunctionHRTWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FourFunctionHRTWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/linear-independence-of-time-frequency-translates/index.html#modulation-one).

## A four-function case of the HRT conjecture

For every function
$g : \mathbb{R} \to \mathbb{C}$ in $L^2(\mathbb{R})$ that is not zero almost everywhere, the four
functions $g(x)$, $g(x - 1)$, $g(x - \sqrt{2})$ and $e^{2\pi i x} g(x)$ are linearly independent:
whenever $c_0, c_1, c_2, c_3 \in \mathbb{C}$ satisfy
$c_0 g(x) + c_1 g(x - 1) + c_2 g(x - \sqrt{2}) + c_3 e^{2\pi i x} g(x) = 0$ for almost every
$x \in \mathbb{R}$, we have $c_0 = c_1 = c_2 = c_3 = 0$.

Formalized by `MathlibExt.Analysis.FourFunctionHRTWanted.conjecture`, a definition declared in [WantedExt/Analysis/FourFunctionHRTWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FourFunctionHRTWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/linear-independence-of-time-frequency-translates/index.html#conjecture).

## A four-function case of the HRT conjecture holds

For every function
$g : \mathbb{R} \to \mathbb{C}$ in $L^2(\mathbb{R})$ that is not zero almost everywhere, the four
functions $g(x)$, $g(x - 1)$, $g(x - \sqrt{2})$ and $e^{2\pi i x} g(x)$ are linearly independent:
whenever $c_0, c_1, c_2, c_3 \in \mathbb{C}$ satisfy
$c_0 g(x) + c_1 g(x - 1) + c_2 g(x - \sqrt{2}) + c_3 e^{2\pi i x} g(x) = 0$ for almost every
$x \in \mathbb{R}$, then $c_0 = c_1 = c_2 = c_3 = 0$.

This case was proved by Demeter (Theorem 1.4(b)); Liu (Theorem 1.1(b)) states it for the
time-frequency configuration $\{(0,0),(a,0),(b,0),(0,1)\}$ with $a = 1$ and $b = \sqrt{2}$.

## Sources

- Ciprian Demeter, Linear independence of time frequency translates for special configurations, Math. Res. Lett. 17 (2010) 761-779, arXiv:1006.0732, https://arxiv.org/abs/1006.0732; Wencai Liu, Proof of the HRT conjecture for almost every (1,3) configuration, J. Fourier Anal. Appl. (2019), arXiv:1609.08230, https://arxiv.org/abs/1609.08230.

Stated but not proved: `MathlibExt.Analysis.FourFunctionHRTWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/FourFunctionHRTWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/FourFunctionHRTWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/linear-independence-of-time-frequency-translates/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear independence of time–frequency translates](https://deicyde.github.io/atlas-lean/roadmap/Analysis/harmonic-analysis/fourier-transform/linear-independence-of-time-frequency-translates/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/harmonic-analysis/fourier-transform/linear-independence-of-time-frequency-translates)
