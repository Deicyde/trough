---
declaration: section
origin: cited
lean: MetaMathlibExt.dickman_ge_rpow_neg_mul, MetaMathlibExt.exists_norm_logDeriv_riemannZeta_le_inv_norm_add, MetaMathlibExt.abs_sum_inv_primes_sub_meisselMertensConstant_le, MetaMathlibExt.log_log_add_le_sum_inv_primes_le, MetaMathlibExt.sum_abs_cos_sub_div_primes_le, MetaMathlibExt.re_sum_div_primes_cpow_le, MetaMathlibExt.norm_LSeries_le_exp_nu₂_mul_exp_re_sum_primes, MetaMathlibExt.tsum_rpow_neg_primes_gt_exp_inv_le
statement: formalized
---

# Explicit Mertens-type prime sum estimates

8 results, 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html).

## Explicit lower bound for the Dickman function

Let $\rho$ be a Dickman–de Bruijn
function. Then $\rho(x) \ge x^{-1.42 x}$ for every real $x \ge 1$.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Lemma 2.

Stated but not proved: `MetaMathlibExt.dickman_ge_rpow_neg_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#dickman-ge-rpow-neg-mul).

## Logarithmic derivative of the zeta function near its pole

Let $\zeta$ be the Riemann zeta
function. There are real numbers $C$ and $\alpha_0 > 0$ such that for all real $\alpha$ and $\tau$
with $0 < \alpha < \alpha_0$ and $|\tau| \le 1/2$, the point $s = 1 + \alpha + i\tau$ satisfies
$|\zeta'(s)/\zeta(s)| \le 1/|s - 1| + C$.

This is the estimate $|\zeta'(s)/\zeta(s)| \le 1/|s - 1| + O(1)$ as $\alpha \to 0^+$, uniformly
in $|\tau| \le 1/2$.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Lemma 3.

Stated but not proved: `MetaMathlibExt.exists_norm_logDeriv_riemannZeta_le_inv_norm_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#exists-norm-log-deriv-riemann-zeta-le-in).

## Mertens' second theorem with the Rosser–Schoenfeld error term

Let $M$ be the
Meissel–Mertens constant. Then $0.2614 \le M < 0.2615$, and for every real $x > 1$,
$\left|\sum_{p \le x} 1/p - \log \log x - M\right| \le 1/(\log x)^2$, where the sum runs over the
primes $p \le x$.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Proposition 1.

Stated but not proved: `MetaMathlibExt.abs_sum_inv_primes_sub_meisselMertensConstant_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#abs-sum-inv-primes-sub-meissel-mertens-c).

## Two-sided explicit Mertens bound

For every real $x \ge 2$,
$\log \log x + 0.2614 \le \sum_{p \le x} 1/p \le \log \log x + 0.8666$, where the sum runs over
the primes $p \le x$.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Proposition 2.

Stated but not proved: `MetaMathlibExt.log_log_add_le_sum_inv_primes_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#log-log-add-le-sum-inv-primes-le).

## Explicit bound for a cosine-weighted sum over primes

Let $K$ be a real number with
$\frac{1}{2\pi} \int_0^{2\pi} |\cos t - K| \, dt = 1 - K$ (this equation has exactly one real
solution, $K \approx 0.3286$). Then for every real $\alpha$ with $0 < \alpha \le 1$ and every real
$\tau$, $\sum_{p \le e^{1/\alpha}} |\cos(\tau \log p) - K|/p \le (1 - K) \log(1/\alpha) +
(2 + 2K) \log \log(|\tau| + 3) + 7.28$, where the sum runs over the primes $p \le e^{1/\alpha}$.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Lemma 7.

Stated but not proved: `MetaMathlibExt.sum_abs_cos_sub_div_primes_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#sum-abs-cos-sub-div-primes-le).

## Upper bound for twisted prime sums with real coefficients

Throughout, sums over $p$ run
over primes. Let $K$ be a real number with
$\frac{1}{2\pi} \int_0^{2\pi} |\cos t - K| \, dt = 1 - K$. Let $g$ be a real-valued function on
the natural numbers with $|g(p)| \le 1$ for every prime $p$, let $\alpha$ be a real number with
$0 < \alpha \le 1$, put $x = e^{1/\alpha}$, and let $\lambda$ be a real number with
$\sum_{p \le x} (1 - g(p))/p = \lambda \sum_{p \le x} 1/p$. Let $M$ be the Meissel–Mertens
constant and $M'(x) = \sum_{p \le x} 1/p - \log \log x - M$. Then for every real $\tau$,
$\operatorname{Re} \sum_{p \le x} g(p)/p^{1 + i\tau}$ is at most
$(1 - K\lambda) \log(1/\alpha) + (2 + 2K) \log \log(|\tau| + 3) + 7.28 +
(K - K\lambda)(M + M'(x))$.

The paper prints $(2 + 2K)(\log \log |\tau| + 3)$; its proof applies Lemma 7, which has
$\log \log(|\tau| + 3)$, and the printed form fails at $\alpha = 1$, $g \equiv 1$,
$\tau = 1.0001$. The paper allows $\alpha \in [0, 1]$; here $\alpha > 0$, where $e^{1/\alpha}$
is defined.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Lemma 8.

Stated but not proved: `MetaMathlibExt.re_sum_div_primes_cpow_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#re-sum-div-primes-cpow-le).

## Bound for a Dirichlet series by its prime sum

Let $g$ be a complex-valued completely
multiplicative arithmetic function with $g(1) = 1$ and $|g(n)| \le 1$ for every $n$, and let
$F(s) = \sum_{n \ge 1} g(n) n^{-s}$ be its Dirichlet series. Let
$\nu_2 = \sum_p (-\log(1 - 1/p) - 1/p)$, summed over all primes $p$. Then $\nu_2 \le 0.316$, and
for every complex $s$ with $\operatorname{Re} s > 1$,
$|F(s)| \le e^{\nu_2} \exp(\operatorname{Re} \sum_p g(p) p^{-s})$, where $p$ runs over the primes.

In the paper $\nu_2 = \gamma - M$, with $\gamma$ the Euler–Mascheroni constant and $M$ the
Meissel–Mertens constant; the prime series above is the form of $\nu_2$ used in its proof.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Lemma 9.

Stated but not proved: `MetaMathlibExt.norm_LSeries_le_exp_nu₂_mul_exp_re_sum_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#norm-lseries-le-exp-nu-mul-exp-re-sum-pr).

## Uniform tail bound for the prime zeta series

For every real $\alpha$ with
$0 < \alpha \le 1$, $\sum_{p > e^{1/\alpha}} p^{-(1 + \alpha)} \le 0.9235$, where the sum runs
over the primes $p > e^{1/\alpha}$.

## Sources

- Matteo Bordignon and Forrest J. Francis, *Explicit Improvements to the Burgess Bound via Pólya--Vinogradov*, INTEGERS 24 (2024), Article A66, Lemma 10.

Stated but not proved: `MetaMathlibExt.tsum_rpow_neg_primes_gt_exp_inv_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BurgessPolyaVinogradovWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html#tsum-rpow-neg-primes-gt-exp-inv-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Explicit Mertens-type prime sum estimates](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/explicit-mertens-type-prime-sum-estimates)
