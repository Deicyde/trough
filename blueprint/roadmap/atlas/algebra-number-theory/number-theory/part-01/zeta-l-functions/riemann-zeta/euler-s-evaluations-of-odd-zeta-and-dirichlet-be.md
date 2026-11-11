---
declaration: section
origin: cited
lean: MetaMathlibExt.hasSum_one_div_odd_pow, MetaMathlibExt.dirichletBeta_two_mul_add_one, MetaMathlibExt.tendsto_integral_sinc_pow, MetaMathlibExt.tendsto_sum_sin_pow_div_pow
statement: formalized
---

# Euler's evaluations of odd zeta and Dirichlet beta series

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/euler-s-evaluations-of-odd-zeta-and-dirichlet-be/index.html).

## Zeta series over odd denominators

Let $\zeta$ be the Riemann zeta function. For every
natural number $k \ge 2$, the series $\sum_{n \ge 0} 1/(2n+1)^k$ converges in $\mathbb{C}$ and

$$\sum_{n=0}^{\infty} \frac{1}{(2n+1)^k} = \Bigl(1 - \frac{1}{2^k}\Bigr) \zeta(k).$$

The source writes this as $\sum_{n \ge 1} 1/(2n-1)^k = (1 - 2^{-k}) \zeta(k)$ for integers
$k > 1$.

## Sources

- Jan W. H. Swanepoel, *A Short Simple Probabilistic Proof of a Well Known Identity and the Derivation of Related New Identities Involving the Bernoulli Numbers and the Euler Numbers*, INTEGERS 25 (2025), Article A50, Proposition 2, Equation (11), citing its reference [20].

Stated but not proved: `MetaMathlibExt.hasSum_one_div_odd_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/euler-s-evaluations-of-odd-zeta-and-dirichlet-be/index.html#has-sum-one-div-odd-pow).

## Dirichlet beta at odd positive integers

Let $\beta$ be the Dirichlet $L$-function of the
nontrivial character modulo $4$, which for $\operatorname{Re} s > 1$ is the series
$\beta(s) = \sum_{n \ge 1} (-1)^{n-1}/(2n-1)^s$, and let $E_0 = 1, E_2 = -1, E_4 = 5,
E_6 = -61, \dots$ be the even-index Euler numbers. Then for every natural number $m$,

$$\beta(2m+1) = \frac{\pi^{2m+1} \, |E_{2m}|}{2^{2m+2} \, (2m)!}.$$

For example $\beta(1) = \pi/4$, $\beta(3) = \pi^3/32$, $\beta(5) = 5\pi^5/1536$ and
$\beta(7) = 61\pi^7/184320$. With $k = 2m+2$ this is the source's Equation (12),
$\beta(k-1) = (\pi/2)^{k-1} |E_{k-2}| / (2 (k-2)!)$ for even $k \ge 2$. At $s = 1$ the series
converges only conditionally, and its sum is the value of the $L$-function there.

## Sources

- Jan W. H. Swanepoel, *A Short Simple Probabilistic Proof of a Well Known Identity and the Derivation of Related New Identities Involving the Bernoulli Numbers and the Euler Numbers*, INTEGERS 25 (2025), Article A50, Proposition 3, Equation (12), citing its references [3], [6].

Stated but not proved: `MetaMathlibExt.dirichletBeta_two_mul_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/euler-s-evaluations-of-odd-zeta-and-dirichlet-be/index.html#dirichlet-beta-two-mul-add-one).

## Integrals of powers of $\sin x / x$

For every natural number $k \ge 1$, the improper
integral $\lim_{R \to \infty} \int_0^R (\sin x / x)^k \, dx$ exists and

$$
\lim_{R \to \infty} \int_0^R \Bigl(\frac{\sin x}{x}\Bigr)^k dx =
\frac{\pi}{2^k (k-1)!} \sum_{i=0}^{\lfloor k/2 \rfloor} (-1)^i \binom{k}{i} (k-2i)^{k-1}.
$$

For $k = 1$ the integral converges only conditionally, hence the limit over $R$.

## Sources

- Jan W. H. Swanepoel, *A Short Simple Probabilistic Proof of a Well Known Identity and the Derivation of Related New Identities Involving the Bernoulli Numbers and the Euler Numbers*, INTEGERS 25 (2025), Article A50, Theorem 1.

Stated but not proved: `MetaMathlibExt.tendsto_integral_sinc_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/euler-s-evaluations-of-odd-zeta-and-dirichlet-be/index.html#tendsto-integral-sinc-pow).

## Sums of powers of $\sin(nt)/n$

Let $k \ge 1$ be a natural number, suppose that the
limit $L = \lim_{R \to \infty} \int_0^R (\sin x / x)^k \, dx$ exists, and let $t$ be a real
number with $0 < t < 2\pi$ if $k = 1$ and $0 \le t \le 2\pi/k$ if $k \ge 2$. Then the partial
sums of $\sum_{n \ge 1} \sin^k(nt)/n^k$ converge and

$$\sum_{n=1}^{\infty} \frac{\sin^k(nt)}{n^k} = t^{k-1} L - \frac{t^k}{2}.$$

The source writes $L$ as $\pi I_k$, with $I_k$ the normalized integral of its Theorem 1. For
$k = 1$ the series converges only conditionally.

## Sources

- Jan W. H. Swanepoel, *A Short Simple Probabilistic Proof of a Well Known Identity and the Derivation of Related New Identities Involving the Bernoulli Numbers and the Euler Numbers*, INTEGERS 25 (2025), Article A50, Proposition 4, quoting its reference [18].

Stated but not proved: `MetaMathlibExt.tendsto_sum_sin_pow_div_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OddZetaDirichletBetaEulerWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/euler-s-evaluations-of-odd-zeta-and-dirichlet-be/index.html#tendsto-sum-sin-pow-div-pow).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler's evaluations of odd zeta and Dirichlet beta series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/euler-s-evaluations-of-odd-zeta-and-dirichlet-be/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/riemann-zeta/euler-s-evaluations-of-odd-zeta-and-dirichlet-be)
