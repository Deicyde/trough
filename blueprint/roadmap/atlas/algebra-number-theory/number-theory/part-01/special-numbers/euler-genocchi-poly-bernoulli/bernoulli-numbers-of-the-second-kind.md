---
declaration: section
origin: cited
lean: MetaMathlibExt.bernoulliSecondPowerSeries, MetaMathlibExt.bernoulliSecond, MetaMathlibExt.bernoulliSecondPowerSeries_eq, MetaMathlibExt.bernoulliSecond_eq, MetaMathlibExt.bernoulliSecondPowerSeries_mul_mk, MetaMathlibExt.sum_antidiagonal_bernoulliSecondPowerSeries_coeff, MetaMathlibExt.bernoulliSecond_div_factorial_eq, MetaMathlibExt.bernoulli_second_kind_asymptotic
statement: formalized
---

# Bernoulli numbers of the second kind

21 results, 8 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html).

## Generating function of the Bernoulli numbers of the second kind

Let $G(t)$ be the
inverse, in the ring $\mathbb{Q}[[t]]$ of formal power series, of the series
$\sum_{n \ge 0} \frac{(-1)^n}{n + 1} t^n$, which is invertible because its constant
coefficient is $1$.

Analytically this series is $\log(1 + t) / t$, so $G(t) = t / \log(1 + t)$; the logarithm
itself is not invertible, having zero constant coefficient.

Formalized by `MetaMathlibExt.bernoulliSecondPowerSeries`, a definition declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-power-series).

## Bernoulli numbers of the second kind

For a natural number $n$, the Bernoulli number of
the second kind $B_n^*$ is the rational number $n!$ times the coefficient of $t^n$ in
$G(t) \in \mathbb{Q}[[t]]$, the inverse of the formal power series
$\sum_{k \ge 0} \frac{(-1)^k}{k + 1} t^k$. Thus $G(t) = \sum_{n \ge 0} B_n^* t^n / n!$.

Analytically $G(t) = t / \log(1 + t)$; this is Roman's normalization, with $B_0^* = 1$,
$B_1^* = 1/2$ and $B_2^* = -1/6$.

Formalized by `MetaMathlibExt.bernoulliSecond`, a definition declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second).

## Generating function of the Bernoulli numbers of the second kind as an inverse

The
generating function $G(t)$ of the Bernoulli numbers of the second kind equals the inverse, in
the ring $\mathbb{Q}[[t]]$ of formal power series, of the series
$\sum_{n \ge 0} \frac{(-1)^n}{n + 1} t^n$.

Formalized by `MetaMathlibExt.bernoulliSecondPowerSeries_eq`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-power-series-eq).

## Bernoulli numbers of the second kind as scaled coefficients

For every natural number
$n$, the Bernoulli number of the second kind $B_n^*$ equals $n!$ times the coefficient of $t^n$
in the generating function $G(t) \in \mathbb{Q}[[t]]$ of the Bernoulli numbers of the second
kind.

Formalized by `MetaMathlibExt.bernoulliSecond_eq`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-eq).

## Defining identity of the generating function of the Bernoulli numbers of the second kind

**Defining identity of the generating function of the Bernoulli numbers of the second
kind.** In the ring $\mathbb{Q}[[t]]$ of formal power series, the generating function $G(t)$ of
the Bernoulli numbers of the second kind satisfies
$G(t) \cdot \sum_{n \ge 0} \frac{(-1)^n}{n + 1} t^n = 1$.

Analytically, $\sum_{n \ge 0} \frac{(-1)^n}{n + 1} t^n = \log(1 + t) / t$.

Formalized by `MetaMathlibExt.bernoulliSecondPowerSeries_mul_mk`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-power-series-mul-mk).

## Coefficient identity for the generating function of the Bernoulli numbers of the second kind

**Coefficient identity for the generating function of the Bernoulli numbers of the second
kind.** Let $g_i$ be the coefficient of $t^i$ in the generating function $G(t) \in \mathbb{Q}[[t]]$
of the Bernoulli numbers of the second kind. For every natural number $n$, the sum of
$g_i \cdot (-1)^j / (j + 1)$ over all pairs $(i, j)$ of natural numbers with $i + j = n$ equals
$1$ if $n = 0$ and $0$ if $n \ge 1$.

Formalized by `MetaMathlibExt.sum_antidiagonal_bernoulliSecondPowerSeries_coeff`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#sum-antidiagonal-bernoulli-second-power).

## Recurrence for the Bernoulli numbers of the second kind

For every natural number
$n \ge 1$, the Bernoulli numbers of the second kind $B_k^*$ satisfy
$B_n^* / n! = -\sum_{k=0}^{n-1} (B_k^* / k!) \cdot (-1)^{n-k} / (n - k + 1)$.

Formalized by `MetaMathlibExt.bernoulliSecond_div_factorial_eq`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKind.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-div-factorial-eq).

## Asymptotic expansion of the Bernoulli numbers of the second kind

For a natural number
$n$ let $b_n = \frac{1}{n!} \int_0^1 x (x - 1) \cdots (x - n + 1) dx$, and for a natural
number $k$ let $\beta_k$ be $(-1)^k$ times the $(k + 1)$-th derivative of $1 / \Gamma$ at $0$.
Then for every natural number $m$, as $n \to \infty$,

$$b_n - \frac{(-1)^{n+1}}{n (\log n)^2} \sum_{k=0}^{m} \frac{\beta_k}{(\log n)^k} =
o\left(\frac{1}{n (\log n)^{m+2}}\right).$$

The main term $(-1)^{n+1} / (n (\log n)^2)$ is Steffensen's approximation, as noted in the
source.

## Sources

- Gergő Nemes, "An Asymptotic Expansion for the Bernoulli Numbers of the Second Kind," Journal of Integer Sequences 14 (2011), Article 11.4.8, Theorem, equations, lines 124–133, https://cs.uwaterloo.ca/journals/JIS/VOL14/Nemes/nemes4.tex

Formalized by `MetaMathlibExt.bernoulli_second_kind_asymptotic`, a theorem declared in [MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKindAsymptotic.lean, line 709](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Bernoulli/BernoulliSecondKindAsymptotic.lean#L709). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-kind-asymptotic).

## Bernoulli polynomials in the falling-factorial basis

Let $B_m$ be the Bernoulli numbers
(with $B_1 = -1/2$), $B_n(X) = \sum_{i=0}^{n} \binom{n}{i} B_i X^{n-i}$ the Bernoulli
polynomials over $\mathbb{Q}$, $S(m, j)$ the Stirling numbers of the second kind and
$X^{\underline{k}} = X(X-1)\cdots(X-k+1)$ the falling factorial. For every natural number
$n$, in $\mathbb{Q}[X]$,

$$B_n(X) = B_n + \sum_{k=1}^{n} \frac{n}{k} \, S(n-1, k-1) \, X^{\underline{k}}.$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.bernoulli_poly_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-poly-eq).

## Bernoulli numbers in terms of Bernoulli numbers of the second kind

Let $B_m$ be the
Bernoulli numbers (with $B_1 = -1/2$), $B_m^*$ the Bernoulli numbers of the second kind and
$S(m, j)$ the Stirling numbers of the second kind. For every natural number $n \ge 1$,

$$B_n = -\sum_{k=1}^{n} \frac{n}{k} \, S(n-1, k-1) \, B_k^*.$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Corollary 2.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.bernoulli_eq_neg_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-eq-neg-sum).

## Stirling inversion

Let $s(m, j)$ be the signed Stirling numbers of the first kind and
$S(m, j)$ the Stirling numbers of the second kind. For all sequences $(u_n)_{n \ge 0}$ and
$(v_n)_{n \ge 0}$ of rational numbers, $u_n = \sum_{k=0}^{n} s(n, k) \, v_k$ for every natural
number $n$ if and only if $v_n = \sum_{k=0}^{n} S(n, k) \, u_k$ for every natural number $n$.

The paper states this for sequences of complex numbers.

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.stirling_inversion_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#stirling-inversion-iff).

## Bernoulli numbers of the second kind in terms of Bernoulli numbers

Let $B_m$ be the
Bernoulli numbers (with $B_1 = -1/2$), $B_m^*$ the Bernoulli numbers of the second kind and
$s(m, j)$ the signed Stirling numbers of the first kind. For every natural number $n \ge 1$,

$$B_n^* = -\sum_{k=1}^{n} \frac{n}{k} \, s(n-1, k-1) \, B_k.$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.bernoulliSecond_eq_neg_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-eq-neg-sum).

## Falling factorials in the Bernoulli polynomial basis

Let $B_m^*$ be the Bernoulli
numbers of the second kind, $B_k(X)$ the Bernoulli polynomials over $\mathbb{Q}$ (so that
$B_1(X) = X - 1/2$), $s(m, j)$ the signed Stirling numbers of the first kind and
$X^{\underline{n}} = X(X-1)\cdots(X-n+1)$ the falling factorial. For every natural number
$n$, in $\mathbb{Q}[X]$,

$$X^{\underline{n}} = B_n^* + \sum_{k=1}^{n} \frac{n}{k} \, s(n-1, k-1) \, B_k(X).$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Theorem 5.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.descPochhammer_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#desc-pochhammer-eq).

## Shifted Stirling convolution formula for Bernoulli numbers

For natural numbers $k$ and $n$
with $1 \le k \le n$, write $S(m,j)$ for the Stirling numbers of the second kind, $s(m,j)$ for
the signed Stirling numbers of the first kind, and $B_m$ for the Bernoulli numbers with
$B_1 = -\tfrac12$. Then, in $\mathbb{Q}$,

$$
\sum_{i=k}^{n} \frac{S(n-1,i-1)\, s(i,k)}{i} = \frac{1}{n} \binom{n}{k} B_{n-k}.
$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Corollary 7.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.sum_stirlingSecond_signed_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#sum-stirling-second-signed-div).

## Bernoulli numbers via Stirling numbers of the second kind

Let $B_m$ be the Bernoulli
numbers (with $B_1 = -1/2$) and $S(m, j)$ the Stirling numbers of the second kind. For every
natural number $n$,

$$B_n = \sum_{i=0}^{n} (-1)^i \, \frac{i!}{i+1} \, S(n, i).$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Corollary 9.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.bernoulli_eq_sum_stirlingSecond` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-eq-sum-stirling-second).

## Unshifted Stirling convolution formula for Bernoulli numbers

For natural numbers $k$
and $n$ with $1 \le k \le n$, write $S(m,j)$ for the Stirling numbers of the second kind,
$s(m,j)$ for the signed Stirling numbers of the first kind, and $B_m$ for the Bernoulli numbers
with $B_1 = -\tfrac12$. Then, in $\mathbb{Q}$,

$$
\sum_{i=k}^{n} \frac{S(n,i)\, s(i,k)}{i} = \frac{1}{n} \binom{n}{k} B_{n-k} + \delta_{n-1,k},
$$

where $\delta_{n-1,k}$ is $1$ if $k = n - 1$ and $0$ otherwise.

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Corollary 10.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.sum_stirlingSecond_signed_div_delta` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#sum-stirling-second-signed-div-delta).

## Bernoulli numbers of the second kind via Stirling numbers of the first kind

Let $B_m^*$
be the Bernoulli numbers of the second kind and $s(m, j)$ the signed Stirling numbers of the
first kind. For every natural number $n$,

$$B_n^* = \sum_{i=0}^{n} \frac{s(n, i)}{i+1}.$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Proposition 11.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.bernoulliSecond_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#bernoulli-second-eq-sum).

## Shifted Stirling convolution as a Bernoulli number of the second kind

Let $s(m, j)$ be
the signed Stirling numbers of the first kind, $S(m, j)$ the Stirling numbers of the second kind
and $B_m^*$ the Bernoulli numbers of the second kind. For all natural numbers $n$ and $k$ with
$1 \le k \le n$,

$$\sum_{i=k}^{n} \frac{s(n-1, i-1) \, S(i, k)}{i} = \frac{1}{n} \binom{n}{k} \, B_{n-k}^*.$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Theorem 13.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.sum_signed_stirlingSecond_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#sum-signed-stirling-second-div).

## Stirling convolution as a sum of Bernoulli numbers of the second kind

Let $s(m, j)$ be
the signed Stirling numbers of the first kind, $S(m, j)$ the Stirling numbers of the second kind
and $B_m^*$ the Bernoulli numbers of the second kind. For all natural numbers $n$ and $k$ with
$1 \le k \le n$,

$$\sum_{i=k}^{n} \frac{s(n, i) \, S(i, k)}{i} =
(-1)^{n-k} \, \frac{(n-1)!}{k!} \sum_{l=0}^{n-k} \frac{(-1)^l}{l!} \, B_l^*.$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Corollary 15.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.sum_signed_stirlingSecond_div_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#sum-signed-stirling-second-div-eq).

## Weighted alternating sums of Stirling numbers of the second kind

For natural numbers
$r \ge 1$ and $n$, write $S(n,k)$ for the Stirling numbers of the second kind, $c(r,j)$ for the
unsigned Stirling numbers of the first kind, and $B_m$ for the Bernoulli numbers with
$B_1 = -\tfrac12$. Then, in $\mathbb{Q}$,

$$
\sum_{k=0}^{n} (-1)^k \frac{k!}{k+r} S(n,k) = \frac{1}{(r-1)!} \sum_{k=0}^{r-1} c(r,k+1) B_{n+k}.
$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Theorem 17.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.sum_stirlingSecond_div_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#sum-stirling-second-div-add).

## Sums of signed Stirling numbers of the first kind with shifted reciprocal weights

Let
$s(m, j)$ be the signed Stirling numbers of the first kind, $S(m, j)$ the Stirling numbers of
the second kind and $B_m^*$ the Bernoulli numbers of the second kind. Let $r \ge 1$ and $n$ be
natural numbers, and for $0 \le k \le r - 1$ set
$\lambda_{r,n,k} = \sum_{l=0}^{r-1-k} \binom{r-1}{l} \, S(r-1-l, k) \, n^l$ (with $0^0 = 1$).
Then

$$\sum_{k=0}^{n} \frac{s(n, k)}{k + r} = \sum_{k=0}^{r-1} \lambda_{r,n,k} \, B_{n+k}^*.$$

## Sources

- Bakir Farhi, "Formulas Involving Bernoulli and Stirling Numbers of Both Kinds", Theorem 19.

Stated but not proved: `MathlibExt.NumberTheory.BernoulliSecondKindWanted.sum_signed_div_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/BernoulliSecondKindWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BernoulliSecondKindWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html#sum-signed-div-add).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bernoulli numbers of the second kind](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/euler-genocchi-poly-bernoulli/bernoulli-numbers-of-the-second-kind)
