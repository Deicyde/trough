---
declaration: section
origin: cited
lean: Asymptotics.isEquivalent_id_of_monotoneOn_of_tendsto_integral_sub_div_sq, newman_tauberian, MetaMathlibExt.silverman_toeplitz, MathlibExt.Analysis.Fourier.WienerWanted.wiener_tauberian_L1
statement: formalized
proof: formalized
---

# Summability and Tauberian theorems: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/index.html).

Matrix summability methods (Silverman–Toeplitz, Cesàro means, permanent methods) and Tauberian theorems of Tauber, Hardy–Littlewood, Wiener and Newman.

## Integral criterion for asymptotic equivalence to the identity

Let $f$ be a real function
on $\mathbb{R}$ that is nondecreasing on $[1, \infty)$, and suppose that the integral
$\int_1^x (f(t) - t) / t^2 \, dt$ converges to a finite limit as $x \to \infty$. Then
$f(x) \sim x$ as $x \to \infty$.

No monotonicity is assumed below $1$.

## Sources

- ATLAS `NumberTheoryI` Lemma 16.8.

Formalized by `Asymptotics.isEquivalent_id_of_monotoneOn_of_tendsto_integral_sub_div_sq`, a theorem declared in [MathlibExt/Analysis/Asymptotics/MonotoneIntegralCriterion.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Asymptotics/MonotoneIntegralCriterion.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/index.html#is-equivalent-id-of-monotone-on-of-tends).

## Newman's Tauberian theorem

Let $f : \mathbb{R} \to \mathbb{C}$ be almost everywhere
strongly measurable on $(0, \infty)$ and bounded on $[0, \infty)$: for some real $B \ge 0$,
$|f(t)| \le B$ for all $t \ge 0$. Let $G : \mathbb{C} \to \mathbb{C}$ be analytic at every point
of the closed half-plane $\{s : \operatorname{Re} s \ge 0\}$, and suppose that for every $s$
with $\operatorname{Re} s > 0$ the Laplace transform of $f$ converges at $s$ and equals $G(s)$.
Then $\int_0^T f(t)\,dt \to G(0)$ as $T \to \infty$.

Formalized by `newman_tauberian`, a theorem declared in [MathlibExt/Analysis/LaplaceTransform/NewmanTauberian.lean, line 1597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/LaplaceTransform/NewmanTauberian.lean#L1597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/index.html#newman-tauberian).

## Silverman–Toeplitz theorem (sufficiency)

Let $(a_{nk})_{n, k \ge 0}$ be an infinite
matrix of complex numbers. Suppose that there is a real $C$ such that for every $n$ the series
$\sum_k |a_{nk}|$ converges with sum at most $C$, that $a_{nk} \to 0$ as $n \to \infty$ for every
$k$, and that $\sum_k a_{nk} \to 1$ as $n \to \infty$. Then for every sequence $(x_k)$ of complex
numbers converging to $L$, the series $\sum_k a_{nk} x_k$ converges absolutely for every $n$, and
$\sum_k a_{nk} x_k \to L$ as $n \to \infty$.

## Sources

- https://en.wikipedia.org/wiki/Silverman%E2%80%93Toeplitz_theorem.

Formalized by `MetaMathlibExt.silverman_toeplitz`, a theorem declared in [MathlibExt/Analysis/Series/SilvermanToeplitz.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Series/SilvermanToeplitz.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/index.html#silverman-toeplitz).

## Wiener's Tauberian theorem on $L^1(\mathbb{R})$

Let $f : \mathbb{R} \to \mathbb{C}$ be
Lebesgue integrable, and suppose that its Fourier transform
$\hat f(w) = \int_{\mathbb{R}} e^{-2\pi i x w} f(x)\,dx$ vanishes at no real $w$. Then for every
Lebesgue integrable $g : \mathbb{R} \to \mathbb{C}$ and every $\varepsilon > 0$ there are a finite
set $S \subset \mathbb{R}$ and coefficients $c_t \in \mathbb{C}$ for $t \in S$ such that the
function $h(x) = g(x) - \sum_{t \in S} c_t f(x - t)$ is integrable and
$\int_{\mathbb{R}} |h(x)|\,dx < \varepsilon$. In other words, the translates of $f$ span a dense
subspace of $L^1(\mathbb{R})$.

## Sources

- N. Wiener, Ann. of Math. 33 (1932) 1–100, DOI 10.2307/1968102, Thm I; Rudin, Fourier Analysis on Groups

Formalized by `MathlibExt.Analysis.Fourier.WienerWanted.wiener_tauberian_L1`, a theorem declared in [MathlibExt/Analysis/Fourier/WienerTauberian.lean, line 1898](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Fourier/WienerTauberian.lean#L1898). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/index.html#wiener-tauberian-l1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Summability and Tauberian theorems](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/sequences-and-series/summability)
