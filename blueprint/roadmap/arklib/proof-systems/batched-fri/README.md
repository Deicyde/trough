# Batched FRI

Batched FRI tests $m+1$ words for proximity to one Reed–Solomon code by a single FRI run on a random linear combination. Keep the notation of the previous section: $\omega$ is a smooth coset FFT domain $D$ of size $2^n$ over a finite field of odd characteristic, $s_0,\ldots,s_k\geq 1$ are the folding exponents, $d\geq 1$ is the final degree bound, $l$ is the number of queries, and $d_0:=2^{\sum_i s_i}\,d\leq 2^n$ is the initial degree bound. Write $C_0=\mathrm{RS}(D,d_0)$. A generator $G:S\to\mathbb{F}^{m+1}$ supplies the batching coefficients from a seed in a sampleable type $S$.

- [Batched FRI relation and reduction](def-batched-fri.md)
- [Batched FRI soundness](thm-batched-fri-soundness.md)
- [Batched FRI completeness](thm-batched-fri-completeness.md)

The generator hypothesis is discharged for four generators. Write $\rho$ for the rate of $C_0$, and $\varepsilon_{\mathrm{BCIKS}}(\delta)$ for the error that equals $2^n/|\mathbb{F}|$ when $\delta\leq(1-\rho)/2$, equals $d_0^2/\bigl((2\min\{1-\sqrt\rho-\delta,\sqrt\rho/20\})^7|\mathbb{F}|\bigr)$ when $(1-\rho)/2\lt \delta<1-\sqrt\rho$, and is $0$ otherwise.

- [Batched FRI with concrete generators](thm-batched-fri-generators.md)

Knowledge soundness of Batched FRI is not formalized: the batching round has no extractor.
