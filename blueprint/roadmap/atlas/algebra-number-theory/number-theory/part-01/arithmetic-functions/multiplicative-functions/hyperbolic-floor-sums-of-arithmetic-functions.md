---
declaration: section
origin: cited
lean: MetaMathlibExt.summable_abs_mul_log_pow_div_sub, MetaMathlibExt.hyperbolic_floor_sum_asymptotic, MetaMathlibExt.hyperbolic_floor_sum_asymptotic_additive
statement: formalized
---

# Hyperbolic floor sums of arithmetic functions

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/hyperbolic-floor-sums-of-arithmetic-functions/index.html).

## Absolute convergence of a log-weighted difference series

Let $f$ be a real function on
the natural numbers with $f(n) = O(n^\alpha)$ as $n \to \infty$ for some real $\alpha$ with
$0 \le \alpha < 1$. Then for every natural number $i$ the series

$$\sum_{n \ge 1} f(n) \left( \frac{(\log n)^i}{n} - \frac{(\log (n+1))^i}{n+1} \right)$$

converges absolutely.

## Sources

- Meselem Karras and Mihoub Bouderbala, *Hyperbolic Summation Involving Certain Arithmetic Functions and the Integer Part Function*, INTEGERS 26 (2026), Article A37, Lemma 1.

Stated but not proved: `MetaMathlibExt.summable_abs_mul_log_pow_div_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/HyperbolicFloorSumWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/HyperbolicFloorSumWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/hyperbolic-floor-sums-of-arithmetic-functions/index.html#summable-abs-mul-log-pow-div-sub).

## Asymptotics of hyperbolic floor sums

Let $r \ge 2$ and let $\tau_r(n)$ be the number of
ordered factorizations $n = n_1 \cdots n_r$ of $n$ into $r$ positive factors. Let
$P(t) = \sum_j a_j t^j$ be a real polynomial with
$\sum_{1 \le n \le x} \tau_r(n) - x P(\log x) = O(x^{1 - 1/r} (\log x)^{r-2})$ as $x \to \infty$.
Let $f$ be a nonnegative real function on the natural numbers such that, for some real $\alpha$
with $0 \le \alpha < 1$, $f(n) = O(n^\alpha)$ as $n \to \infty$, and, for some real $\beta \ge 0$,
$\sum_{1 \le n \le x} f(n) = O(x (\log \log x)^\beta)$ as $x \to \infty$. For $i \ge 0$ let

$$C_i = \sum_{n \ge 1} f(n) \left( \frac{(\log n)^i}{n} - \frac{(\log (n+1))^i}{n+1} \right).$$

Then, as $x \to \infty$,

$$\sum_{1 \le n \le x} f(\lfloor x/n \rfloor) \, \tau_r(n) = x \sum_{j=0}^{r-1} \sum_{i=0}^{j}
\binom{j}{i} (-1)^i a_j C_i (\log x)^{j-i} + O(x (\log x)^{r-2} (\log \log x)^\beta).$$

The hypothesis $f \ge 0$ is not in the source: its proof bounds the error sum
$\sum_{d \le x} f(d) \, O((x/d)^{1-1/r} (\log (x/d))^{r-2})$ through $\sum_{n \le x} f(n)$,
which controls it only for nonnegative $f$.

## Sources

- Meselem Karras and Mihoub Bouderbala, *Hyperbolic Summation Involving Certain Arithmetic Functions and the Integer Part Function*, INTEGERS 26 (2026), Article A37, Theorem 1.

Stated but not proved: `MetaMathlibExt.hyperbolic_floor_sum_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/HyperbolicFloorSumWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/HyperbolicFloorSumWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/hyperbolic-floor-sums-of-arithmetic-functions/index.html#hyperbolic-floor-sum-asymptotic).

## Hyperbolic floor sums of additive functions of prime exponents

Let $r \ge 2$ and let
$\tau_r(n)$ be the number of ordered factorizations $n = n_1 \cdots n_r$ of $n$ into $r$ positive
factors. Let $P(t) = \sum_j a_j t^j$ be a real polynomial with
$\sum_{1 \le n \le x} \tau_r(n) - x P(\log x) = O(x^{1 - 1/r} (\log x)^{r-2})$ as $x \to \infty$.
Let $g$ be a real function on the natural numbers with $g(1) \ne 0$ and $g(a) = O(2^{a/2})$ as
$a \to \infty$. For $n \ge 1$ let $f(n) = \sum_{p \mid n} g(v_p(n))$, the sum over the primes $p$
dividing $n$, where $v_p(n)$ is the exponent of $p$ in $n$, and for $i \ge 0$ let

$$C_i = \sum_{n \ge 1} f(n) \left( \frac{(\log n)^i}{n} - \frac{(\log (n+1))^i}{n+1} \right).$$

Then, as $x \to \infty$,

$$\sum_{1 \le n \le x} f(\lfloor x/n \rfloor) \, \tau_r(n) = x \sum_{j=0}^{r-1} \sum_{i=0}^{j}
\binom{j}{i} (-1)^i a_j C_i (\log x)^{j-i} + O(x (\log x)^{r-2} \log \log x).$$

Since $f(n)$ sums only over the primes dividing $n$, the source's convention $g(0) = 0$ is not
needed.

## Sources

- Meselem Karras and Mihoub Bouderbala, *Hyperbolic Summation Involving Certain Arithmetic Functions and the Integer Part Function*, INTEGERS 26 (2026), Article A37, Proposition 1.

Stated but not proved: `MetaMathlibExt.hyperbolic_floor_sum_asymptotic_additive` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/HyperbolicFloorSumWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/HyperbolicFloorSumWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/hyperbolic-floor-sums-of-arithmetic-functions/index.html#hyperbolic-floor-sum-asymptotic-additive).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hyperbolic floor sums of arithmetic functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/hyperbolic-floor-sums-of-arithmetic-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/hyperbolic-floor-sums-of-arithmetic-functions)
