# A Fourier-analytic proof of the Wiener-Ikehara theorem

The Fourier transform of an absolutely integrable function $\psi: \mathbb{R} \to \mathbb{C}$ is defined by the formula

$$
\hat \psi(u) := \int_\mathbb{R} e(-tu) \psi(t)\ dt
$$

where $e(\theta) := e^{2\pi i \theta}$.

Let $f: \mathbb{N} \to \mathbb{C}$ be an arithmetic function such that $\sum_{n=1}^\infty \frac{|f(n)|}{n^\sigma} < \infty$ for all $\sigma>1$. Then the Dirichlet series

$$
F(s) := \sum_{n=1}^\infty \frac{f(n)}{n^s}
$$

is absolutely convergent for $\sigma>1$.

- [first-fourier](first-fourier.md)
- [second-fourier](second-fourier.md)

Now let $A \in \mathbb{C}$, and suppose that there is a continuous function $G(s)$ defined on $\mathrm{Re} s \geq 1$ such that $G(s) = F(s) - \frac{A}{s-1}$ whenever $\mathrm{Re} s > 1$. We also make the Chebyshev-type hypothesis

$$
\sum_{n \leq x} |f(n)| \ll x\qquad\text{(1)}
$$

for all $x \geq 1$ (this hypothesis is not strictly necessary, but simplifies the arguments and can be obtained fairly easily in applications).

- [Preliminary decay bound I](prelim-decay.md)
- [Preliminary decay bound II](prelim-decay-2.md)
- [Preliminary decay bound III](prelim-decay-3.md)
- [Decay bound, alternate form](decay-alt.md)
- [Decay bounds](decay.md)
- [Limiting Fourier identity](limiting.md)
- [Corollary of limiting identity](limiting-cor.md)
- [Smooth Urysohn lemma](smooth-ury.md)
- [Limiting identity for Schwartz functions](schwarz-id.md)
- [Bijectivity of Fourier transform](bij.md)
- [Smoothed Wiener-Ikehara](wienerikeharasmooth.md)

Now we add the hypothesis that $f(n) \geq 0$ for all $n$.

- [Wiener-Ikehara in an interval](wienerikeharainterval.md)
- [Wiener-Ikehara Theorem (1)](wienerikehara.md)
