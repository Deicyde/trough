---
declaration: section
origin: cited
lean: MetaMathlibExt.bFreeIndicator, MetaMathlibExt.bFreeIndicator_apply, MetaMathlibExt.bFreeIndicator_one, MetaMathlibExt.bFreeIndicator_prime_pow, MetaMathlibExt.sum_pow_mul_pow_add_eq, MetaMathlibExt.dirichletConvolution_mul_eq_sum_gcd, MetaMathlibExt.sum_dirichletConvolution_mul_eq, MetaMathlibExt.sum_mul_dirichletConvolution_eq_sum_moebius
statement: formalized
---

# Weighted sums of Dirichlet convolutions

14 results, 4 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html).

## Indicator of $B_\kappa$-free integers

Let $\kappa$ be a function from the natural numbers
to the natural numbers (only its values $\kappa(p)$ at primes $p$ matter) and let $B_\kappa$ be
the set of prime powers $p^{\kappa(p)}$. A natural number $n$ is $B_\kappa$-free if $n \ge 1$ and
no $p^{\kappa(p)}$ with $p$ prime divides $n$. The indicator $q_{B_\kappa}$ is the integer-valued
arithmetic function with $q_{B_\kappa}(n) = 1$ if $n$ is $B_\kappa$-free and
$q_{B_\kappa}(n) = 0$ otherwise.

The paper indexes the exponents by the position of the prime ($b_i = p_i^{\kappa_i}$); here
$\kappa$ is indexed by the prime itself. For constant $\kappa = k$ this is the indicator $q_k$ of
$k$-free integers.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Equations (2), (11), (12).

Formalized by `MetaMathlibExt.bFreeIndicator`, a definition declared in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-indicator).

## Values of the $B_\kappa$-free indicator

Let $\kappa$ be a function from the natural
numbers to the natural numbers. For every natural number $n$, the indicator $q_{B_\kappa}$ of
$B_\kappa$-free integers satisfies $q_{B_\kappa}(n) = 1$ if $n \ne 0$ and no $p^{\kappa(p)}$ with
$p$ prime divides $n$, and $q_{B_\kappa}(n) = 0$ otherwise.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Equations (11), (12).

Formalized by `MetaMathlibExt.bFreeIndicator_apply`, a theorem declared in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-indicator-apply).

## The integer $1$ is $B_\kappa$-free

Let $\kappa$ be a function from the natural numbers
to the natural numbers with $\kappa(p) \ge 1$ for every prime $p$. Then the indicator
$q_{B_\kappa}$ of $B_\kappa$-free integers satisfies $q_{B_\kappa}(1) = 1$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Equation (12).

Formalized by `MetaMathlibExt.bFreeIndicator_one`, a theorem declared in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-indicator-one).

## The prime power $p^{\kappa(p)}$ is not $B_\kappa$-free

Let $\kappa$ be a function from
the natural numbers to the natural numbers and let $p$ be a prime. Then the indicator
$q_{B_\kappa}$ of $B_\kappa$-free integers satisfies $q_{B_\kappa}(p^{\kappa(p)}) = 0$.

No positivity of $\kappa(p)$ is assumed; for $\kappa(p) = 0$ the statement is
$q_{B_\kappa}(1) = 0$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Equation (12).

Formalized by `MetaMathlibExt.bFreeIndicator_prime_pow`, a theorem declared in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-indicator-prime-pow).

## Product formula for homogeneous sums of powers

Let $R$ be a commutative ring, let
$a, b \in R$ and let $\tau, \xi$ be natural numbers. Then

$$
\sum_{j=0}^{\tau+\xi} a^j b^{\tau+\xi-j} =
\left(\sum_{j=0}^{\tau} a^j b^{\tau-j}\right) \left(\sum_{i=0}^{\xi} a^i b^{\xi-i}\right) -
ab \left(\sum_{j=0}^{\tau-1} a^j b^{\tau-1-j}\right)
\left(\sum_{i=0}^{\xi-1} a^i b^{\xi-1-i}\right),
$$

where a sum with upper limit $-1$ is zero.

In the source, $a$ and $b$ are the values $u(n)$ and $v(n)$ of complex arithmetic functions.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Lemma 1, Equation (16).

Stated but not proved: `MetaMathlibExt.sum_pow_mul_pow_add_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#sum-pow-mul-pow-add-eq).

## Gcd expansion of a convolution of completely multiplicative functions at a product

Let
$u$ and $v$ be complex-valued completely multiplicative arithmetic functions, meaning
$u(mn) = u(m) u(n)$ and $v(mn) = v(m) v(n)$ for all natural numbers $m$ and $n$. Let $u * v$ be
their Dirichlet convolution and $\mu$ the Möbius function. Then for all natural numbers $r$ and
$s$,

$$(u * v)(rs) = \sum_{m \mid \gcd(r, s)} \mu(m) u(m) v(m) (u * v)(r/m) (u * v)(s/m),$$

the sum running over the positive divisors $m$ of $\gcd(r, s)$ (it is empty when $r = s = 0$).

The paper takes $r, s$ positive; the identity also holds (both sides vanish) when $r$ or $s$
is $0$, so no positivity hypothesis is imposed.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Lemma 2, Equation (17).

Stated but not proved: `MetaMathlibExt.dirichletConvolution_mul_eq_sum_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#dirichlet-convolution-mul-eq-sum-gcd).

## Sums of a Dirichlet convolution over multiples of $r$

Let $u$ and $v$ be completely
multiplicative arithmetic functions with complex values, let $u * v$ be their Dirichlet
convolution, let $\mu$ be the Möbius function, and for real $y$ put
$D(y) = \sum_{1 \le j \le y} (u * v)(j)$. Then for every natural number $r$ and every real $x$,

$$
\sum_{1 \le j \le x/r} (u * v)(rj) =
\sum_{d \mid r} u(d)\, v(r/d) \sum_{m \mid d} \mu(m)\, v(m)\, D\left(\frac{x}{mr}\right),
$$

where $d$ and $m$ run over positive divisors and $x/0 = 0$, so both sides vanish for $r = 0$.

Both sides also vanish for $x < 1$; the source assumes $r \ge 1$ and $x \ge 1$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Lemma 3, Equation (20).

Stated but not proved: `MetaMathlibExt.sum_dirichletConvolution_mul_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#sum-dirichlet-convolution-mul-eq).

## Möbius expansion of weighted sums of a Dirichlet convolution

Let $w$, $u$ and $v$ be
arithmetic functions with complex values, let $*$ denote Dirichlet convolution, let $\mu$ be the
Möbius function and put $g = w * \mu$. Then for every real $x$,

$$
\sum_{1 \le j \le x} w(j)\, (u * v)(j) =
\sum_{1 \le r \le x} g(r) \sum_{1 \le j \le x/r} (u * v)(rj),
$$

where $j$ and $r$ run over positive integers.

Both sides vanish for $x < 1$; the source assumes $x \ge 1$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Lemma 4.

Stated but not proved: `MetaMathlibExt.sum_mul_dirichletConvolution_eq_sum_moebius` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#sum-mul-dirichlet-convolution-eq-sum-moe).

## Weighted summation of Dirichlet convolutions

Let $u$ and $v$ be completely
multiplicative arithmetic functions with complex values, let $w$ be any arithmetic function with
complex values, let $*$ denote Dirichlet convolution, let $\mu$ be the Möbius function, put
$g = w * \mu$, and for real $y$ put $D(y) = \sum_{1 \le j \le y} (u * v)(j)$. Then for every
real $x$,

$$
\sum_{1 \le j \le x} w(j)\, (u * v)(j) =
\sum_{1 \le r \le x} g(r) \sum_{d \mid r} u(d)\, v(r/d) \sum_{m \mid d} \mu(m)\, v(m)\,
D\left(\frac{x}{mr}\right),
$$

where $r$, $d$ and $m$ run over positive integers.

Both sides vanish for $x < 1$; the source assumes $x \ge 1$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Theorem 1, Equation (8).

Stated but not proved: `MetaMathlibExt.weighted_sum_dirichletConvolution_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#weighted-sum-dirichlet-convolution-eq).

## The $B_\kappa$-free indicator convolved with the Möbius function

Let $\kappa$ be a
function from the natural numbers to the natural numbers with $\kappa(p) \ge 1$ for every prime
$p$, let $q_{B_\kappa}$ be the indicator of $B_\kappa$-free integers, let $\mu$ be the Möbius
function and let $*$ denote Dirichlet convolution. Let $n \ge 1$ be a natural number with prime
factorization $n = \prod_p p^{e_p}$. If $\kappa(p)$ divides $e_p$ for every prime $p$, then
$(q_{B_\kappa} * \mu)(n) = \mu(n^{1/\kappa})$, where $n^{1/\kappa} = \prod_p p^{e_p/\kappa(p)}$;
otherwise $(q_{B_\kappa} * \mu)(n) = 0$.

The source indexes the exponents by the position of the prime ($\kappa_i$ for the $i$-th prime
$p_i$) and requires $b_i = p_i^{\kappa_i} > 1$, which is the hypothesis $\kappa(p) \ge 1$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Lemma 5, Equation (22).

Stated but not proved: `MetaMathlibExt.bFreeIndicator_mul_moebius_apply` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-indicator-mul-moebius-apply).

## The $B_\kappa$-free indicator twisted by the principal character, convolved with $\mu$

Let $\kappa$ be a function from the natural numbers to the natural numbers with $\kappa(p) \ge 1$
for every prime $p$, let $\xi$ be a natural number, let $q_{B_\kappa}$ be the indicator of
$B_\kappa$-free integers and let $\mu$ be the Möbius function. Put $w(d) = q_{B_\kappa}(d)$ if
$\gcd(d, \xi) = 1$ and $w(d) = 0$ otherwise, so that $w = q_{B_\kappa} \chi_\xi$ with $\chi_\xi$
the principal character modulo $\xi$, and let $(w * \mu)(n) = \sum_{d \mid n} w(d) \mu(n/d)$, the
sum running over the positive divisors $d$ of $n$ (it is empty for $n = 0$). For $r \ge 1$ with
prime factorization $r = \prod_p p^{e_p}$ write $r^\kappa = \prod_p p^{\kappa(p) e_p}$, and set
$0^\kappa = 1$. Then for every natural number $n$ with $(w * \mu)(n) \ne 0$ there are natural
numbers $\ell$ and $r$ with $\ell \mid \xi$, $\gcd(r, \xi) = 1$ and $n = \ell r^\kappa$. Moreover,
for all natural numbers $\ell$ and $r$ with $\ell \mid \xi$, $\gcd(r, \xi) = 1$ and $r \ge 1$,
$(w * \mu)(\ell r^\kappa) = \mu(\ell) \mu(r)$.

The hypothesis $r \ge 1$ in the evaluation is needed: for $r = 0$ the formula is false. No
positivity of $\xi$ is assumed.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Lemma 6, Equation (23).

Stated but not proved: `MetaMathlibExt.bFreeCoprimeIndicator_mul_moebius` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-coprime-indicator-mul-moebius).

## Asymptotic for the divisor function summed over $k$-free integers

Let $k \ge 2$ be a
natural number, let $q_k$ be the indicator of $k$-free integers (the indicator of
$B_\kappa$-free integers for the constant function $\kappa = k$), let $\tau(n)$ be the number of
positive divisors of $n$, let $\gamma$ be the Euler–Mascheroni constant, let
$\Delta(x) = \sum_{1 \le n \le x} \tau(n) - x \log x - (2\gamma - 1) x$ be the Dirichlet divisor
error term, and put

$$c_k = \prod_p \Bigl(1 - \frac{k + 1}{p^k} + \frac{k}{p^{k+1}}\Bigr),$$

the product running over all primes $p$. Then there is a real constant $\beta_k$ such that
$E(x) = \sum_{1 \le n \le x} q_k(n) \tau(n) - c_k x \log x - \beta_k x$ satisfies the following
as $x \to \infty$. If $k \le 3$, then $E(x) = O(x^{1/k + \varepsilon})$ for every
$\varepsilon > 0$. If $k \ge 4$, then for every real $\eta \ge 1/4$ with $\Delta(x) = O(x^\eta)$,
$E(x) = O(x^{\eta + \varepsilon})$ for every $\varepsilon > 0$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Corollary 1.

Stated but not proved: `MetaMathlibExt.kFree_divisor_sum_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#k-free-divisor-sum-asymptotic).

## Asymptotic for the divisor function summed over $B_\kappa$-free integers

Let $\kappa$ be
a function from the natural numbers to the natural numbers and let $K \ge 2$ be the minimum of
$\kappa(p)$ over the primes $p$: $\kappa(p) \ge K$ for every prime $p$, with equality for some
prime. Let $q_{B_\kappa}$ be the indicator of $B_\kappa$-free integers, $\tau(n)$ the number of
positive divisors of $n$, $\gamma$ the Euler–Mascheroni constant and
$\Delta(x) = \sum_{1 \le n \le x} \tau(n) - x \log x - (2\gamma - 1) x$ the Dirichlet divisor
error term, and put

$$C_\kappa = \prod_p \Bigl(1 - \frac{\kappa(p) + 1}{p^{\kappa(p)}} +
\frac{\kappa(p)}{p^{\kappa(p)+1}}\Bigr),$$

the product running over all primes $p$. Then there is a real constant $\beta_\kappa$ such that
$E(x) = \sum_{1 \le n \le x} q_{B_\kappa}(n) \tau(n) - C_\kappa x \log x - \beta_\kappa x$
satisfies the following as $x \to \infty$. If $K \le 3$, then $E(x) = O(x^{1/K + \varepsilon})$
for every $\varepsilon > 0$. If $K \ge 4$, then for every real $\eta \ge 1/4$ with
$\Delta(x) = O(x^\eta)$, $E(x) = O(x^{\eta + \varepsilon})$ for every $\varepsilon > 0$.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Corollary 2.

Stated but not proved: `MetaMathlibExt.bFree_divisor_sum_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-divisor-sum-asymptotic).

## Asymptotic for the divisor function summed over $B_\kappa$-free integers in a progression

Let $\kappa$ be a function from the natural numbers to the natural numbers and let $K$ be the
minimum of $\kappa(p)$ over the primes $p$: $\kappa(p) \ge K$ for every prime $p$, with equality
for some prime. Assume $K \ge 2$ and $K \ne 3$. Let $a$ and $\xi$ be natural numbers with
$a < \xi$ and $\gcd(a, \xi) = 1$. Let $q_{B_\kappa}$ be the indicator of $B_\kappa$-free
integers, $\tau(n)$ the number of positive divisors of $n$ and $\varphi$ Euler's totient
function, and put

$$C_{\kappa,\xi} = \prod_{p \nmid \xi} \Bigl(1 - \frac{\kappa(p) + 1}{p^{\kappa(p)}} +
\frac{\kappa(p)}{p^{\kappa(p)+1}}\Bigr),$$

the product running over the primes $p$ that do not divide $\xi$. Let $\eta = 1/2$ if $K = 2$
and $\eta = 1/3$ if $K \ge 4$. Then there is a real constant $\tilde c$ such that for every
$\varepsilon > 0$, as $x \to \infty$,

$$\sum_{\substack{1 \le n \le x \\ n \equiv a \pmod{\xi}}} q_{B_\kappa}(n) \tau(n) =
\frac{\varphi(\xi)}{\xi^2} C_{\kappa,\xi} \, x \log x + \tilde c x + O(x^{\eta + \varepsilon}).$$

The case $K = 3$ is not covered by the paper's statement and is excluded.

## Sources

- André Pierro de Camargo, *Weighted Summation of Dirichlet Convolutions and Applications to Some Divisor Problems over k-Free and B-Free Integers*, INTEGERS 24 (2024), Article A75, Corollary 3, Equation (15).

Stated but not proved: `MetaMathlibExt.bFree_divisor_sum_progression_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WeightedDirichletConvolutionWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html#b-free-divisor-sum-progression-asymptoti).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weighted sums of Dirichlet convolutions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/weighted-sums-of-dirichlet-convolutions)
