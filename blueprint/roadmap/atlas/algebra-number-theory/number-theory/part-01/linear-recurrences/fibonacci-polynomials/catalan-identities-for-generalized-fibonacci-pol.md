---
declaration: section
origin: cited
lean: MetaMathlibExt.gfp_fib_eq_sum_choose, MetaMathlibExt.gfp_lucas_eq_sum_choose, MetaMathlibExt.choose_sub_sub_one_eq_two_zpow_mul_sum, MetaMathlibExt.choose_two_mul_add_one_eq_alternating_sum, MetaMathlibExt.choose_two_mul_eq_alternating_sum, MetaMathlibExt.gfp_fib_catalan, MetaMathlibExt.gfp_lucas_catalan, MetaMathlibExt.alternating_sum_choose_mul_choose_sub
statement: formalized
---

# Catalan identities for generalized Fibonacci polynomials

16 results, 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html).

## Explicit formula for Fibonacci-type generalized Fibonacci polynomials

Let $d$ and $g$ be
polynomials with integer coefficients, and let $F_n$ be the generalized Fibonacci polynomials
defined by $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = d F_{n+1} + g F_n$. Then for every $n \ge 1$,

$$F_n = \sum_{i=0}^{\lfloor (n-1)/2 \rfloor} \binom{n-i-1}{i} d^{n-2i-1} g^i.$$

The source quotes this formula from Flórez and Saunders.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Lemma 3.1 (1).

Stated but not proved: `MetaMathlibExt.gfp_fib_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#gfp-fib-eq-sum-choose).

## Explicit formula for Lucas-type generalized Fibonacci polynomials

Let $\alpha$ and $p_0$
be integers with $\alpha p_0 = 2$, let $p_1$ and $g$ be polynomials with integer coefficients, and
put $d = \alpha p_1$. Let $L_n$ be the generalized Fibonacci polynomials defined by $L_0 = p_0$,
$L_1 = p_1$ and $L_{n+2} = d L_{n+1} + g L_n$. Then for every $n \ge 1$, writing
$c_i = \lfloor n \binom{n-i}{i} / (n-i) \rfloor$,

$$\alpha L_n = \sum_{i=0}^{\lfloor n/2 \rfloor} c_i \, d^{n-2i} g^i.$$

The quotient $n \binom{n-i}{i} / (n-i)$ is always an integer, so the floor does not change it;
the source writes the coefficient as $\frac{n}{n-i} \binom{n-i}{i}$ and quotes the formula from
Flórez and Saunders.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Lemma 3.1 (2).

Stated but not proved: `MetaMathlibExt.gfp_lucas_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#gfp-lucas-eq-sum-choose).

## Webb–Parberry binomial identity

For natural numbers $m < n$,

$$\binom{n-m-1}{m} = 2^{2m-n+1} \sum_{j=m}^{\lfloor (n-1)/2 \rfloor} \binom{j}{m} \binom{n}{2j+1},$$

an identity of rational numbers in which the exponent $2m-n+1$ may be negative.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Lemma 3.2 (1).

Stated but not proved: `MetaMathlibExt.choose_sub_sub_one_eq_two_zpow_mul_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#choose-sub-sub-one-eq-two-zpow-mul-sum).

## Binomial coefficients of odd lower index as an alternating sum

For natural numbers $n$
and $k$ with $k < \lfloor (n-1)/2 \rfloor$,

$$\binom{n}{2k+1} = \sum_{i=k}^{\lfloor (n-1)/2 \rfloor} (-1)^{i-k} \, 2^{n-2i-1}
  \binom{n-i-1}{i} \binom{i}{k}.$$

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Lemma 3.2 (2).

Stated but not proved: `MetaMathlibExt.choose_two_mul_add_one_eq_alternating_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#choose-two-mul-add-one-eq-alternating-su).

## Binomial coefficients of even lower index as an alternating sum

For natural numbers $n$
and $k$ with $k < \lfloor n/2 \rfloor$,

$$\binom{n}{2k} = n \sum_{i=k}^{\lfloor n/2 \rfloor} \frac{(-1)^{i-k}}{n-i} \, 2^{n-2i-1}
  \binom{n-i}{i} \binom{i}{k},$$

an identity of rational numbers in which the exponent $n-2i-1$ may be $-1$.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Lemma 3.2 (3).

Stated but not proved: `MetaMathlibExt.choose_two_mul_eq_alternating_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#choose-two-mul-eq-alternating-sum).

## Catalan identity for Fibonacci-type generalized Fibonacci polynomials

Let $d$ and $g$ be
polynomials with integer coefficients, and let $F_n$ be the generalized Fibonacci polynomials
defined by $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = d F_{n+1} + g F_n$. Then for every natural number
$n$ (for $n = 0$ both sides are $0$),

$$2^{n-1} F_n = \sum_{i=0}^{\lfloor (n-1)/2 \rfloor} \binom{n}{2i+1} d^{n-2i-1} (4g + d^2)^i.$$

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Theorem 3.3 (1).

Stated but not proved: `MetaMathlibExt.gfp_fib_catalan` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#gfp-fib-catalan).

## Catalan identity for Lucas-type generalized Fibonacci polynomials

Let $\alpha$ and $p_0$
be integers with $\alpha p_0 = 2$, let $p_1$ and $g$ be polynomials with integer coefficients, and
put $d = \alpha p_1$. Let $L_n$ be the generalized Fibonacci polynomials defined by $L_0 = p_0$,
$L_1 = p_1$ and $L_{n+2} = d L_{n+1} + g L_n$. Then for every natural number $n$,

$$2^n \alpha L_n = 2 \sum_{i=0}^{\lfloor n/2 \rfloor} \binom{n}{2i} d^{n-2i} (4g + d^2)^i.$$

Dividing both sides by $2$ gives the source's form, with $\alpha 2^{n-1} L_n$ on the left; the
factor $2$ is cleared so that $n = 0$ is included.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Theorem 3.3 (2).

Stated but not proved: `MetaMathlibExt.gfp_lucas_catalan` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#gfp-lucas-catalan).

## Alternating sum of shifted binomial coefficients

Let $\ell$, $n$, $j$ and $s$ be natural
numbers with $1 \le \ell \le n$, $j \ge 1$ and $\ell j + s \le n$. Then

$$\sum_{i=0}^{\ell} (-1)^i \binom{\ell}{i} \binom{n-i}{\ell j+s} = \binom{n-\ell}{\ell(j-1)+s}.$$

The paper states this for $\lfloor (1-s)/\ell \rfloor \le j \le \lfloor (n-s)/\ell \rfloor$; only
$j \ge 1$ is stated here, since for $j \le 0$ the right side can have a negative lower index. For
$j \ge 1$ the bound $j \le \lfloor (n-s)/\ell \rfloor$ is the condition $\ell j + s \le n$.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Lemma 4.1.

Stated but not proved: `MetaMathlibExt.alternating_sum_choose_mul_choose_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#alternating-sum-choose-mul-choose-sub).

## Recurrence for the floor-exponent binomial sums

Let $R$ be a commutative ring, $t \in R$
and $\ell \ge 1$ an integer, and for $m \ge 0$ let
$T_\ell(m; t) = \sum_{j=0}^{m} \binom{m}{j} t^{\lfloor j/\ell \rfloor}$. Then for every integer
$n \ge 0$,

$$\sum_{i=0}^{\ell} (-1)^i \binom{\ell}{i} T_\ell(n+\ell-i; t) - t\, T_\ell(n; t) = 0.$$

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Theorem 4.2.

Stated but not proved: `MetaMathlibExt.floorPowBinomialSum_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#floor-pow-binomial-sum-recurrence).

## Alternating sum of binomial row sums

For all natural numbers $\ell$ and $n$,

$$\sum_{i=0}^{n} (-1)^i \binom{\ell}{i} \sum_{j=0}^{n-i} \binom{n-i}{j}
  = \sum_{i=0}^{n} (-1)^i \binom{i+\ell-n-1}{i},$$

where on the right $\binom{a}{i} = a(a-1)\cdots(a-i+1)/i!$ is the binomial coefficient with
integer upper index $a$. For $n < \ell$ the upper index $i + \ell - n - 1$ is nonnegative and this
is the ordinary binomial coefficient, the case used in Theorem 4.4.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Lemma 4.3.

Stated but not proved: `MetaMathlibExt.alternating_choose_mul_sum_choose` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#alternating-choose-mul-sum-choose).

## Generating function of the floor-exponent binomial sums

Let $R$ be a commutative ring,
$t \in R$ and $\ell \ge 1$ an integer, and for $n \ge 0$ let
$T_\ell(n; t) = \sum_{i=0}^{n} \binom{n}{i} t^{\lfloor i/\ell \rfloor}$. Then in the ring $R[[x]]$
of formal power series,

$$\Big(\sum_{n \ge 0} T_\ell(n; t)\, x^n\Big) \big((1-x)^\ell - t x^\ell\big)
  = \sum_{k=0}^{\ell-1} \Big(\sum_{i=0}^{k} (-1)^i \binom{i+\ell-k-1}{i}\Big) x^k.$$

So the generating function of the $T_\ell(n; t)$ is this polynomial divided by the series
$(1-x)^\ell - t x^\ell$, which is invertible since its constant term is $1$.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Theorem 4.4.

Stated but not proved: `MetaMathlibExt.floorPowBinomialSum_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#floor-pow-binomial-sum-generating-functi).

## Generating function of the binomial section sums

Let $R$ be a commutative ring, $t \in R$,
and let $\ell$ and $s$ be natural numbers with $s < \ell$. Put
$T_{\ell,s}(n; t) = \sum_{i=0}^{n} \binom{n}{\ell i + s} t^i$. Then, as formal power series in $x$
over $R$,

$$\Big( \sum_{n \ge 0} T_{\ell,s}(n; t) x^n \Big) \big( (1-x)^\ell - t x^\ell \big) =
\sum_{k=0}^{\ell-1} \Big( \sum_{i=0}^{k} (-1)^i \binom{\ell}{i} \sum_{r=0}^{k} \binom{k-i}{r\ell+s}
t^r \Big) x^k.$$

That is, the generating function of $T_{\ell,s}(n; t)$ is this polynomial divided by
$(1-x)^\ell - t x^\ell$.

The printed numerator in the source has $t^t$, a typo for $t^r$ ($r$ is the summation index), and
the range $s < \ell$ is the one of (4.4). For $s \ge \ell$ the identity fails: for $\ell = 1$,
$s = 1$, $t = 2$ the left side is $x/(1-x)$ and the right side is $0$.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Theorem 4.5.

Stated but not proved: `MetaMathlibExt.sectionBinomialSum_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#section-binomial-sum-generating-function).

## Integral representation of Fibonacci-type generalized Fibonacci polynomials

Let $d$ and
$g$ be polynomials with integer coefficients, and let $F_n$ be the generalized Fibonacci
polynomials defined by $F_0 = 0$, $F_1 = 1$ and $F_{n+2} = d F_{n+1} + g F_n$. If $x$ is a real
number with $d(x)^2 + 4 g(x) \ge 0$, then for every $n \ge 2$,

$$F_n(x) = \frac{n}{2^n} \int_{-1}^{1} \left( d(x) + y \sqrt{d(x)^2 + 4 g(x)} \right)^{n-1} dy.$$

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Proposition 5.1.

Stated but not proved: `MetaMathlibExt.gfp_fib_eval_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#gfp-fib-eval-eq-integral).

## Stewart's integral formula for the Fibonacci numbers

For every integer $n \ge 1$, the
$n$-th Fibonacci number $F_n$ (with $F_0 = 0$ and $F_1 = 1$) satisfies

$$F_n = \frac{n}{2^n} \int_{-1}^{1} \left(1 + y\sqrt{5}\right)^{n-1} dy.$$

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Corollary 5.1.

Stated but not proved: `MetaMathlibExt.fib_eq_integral_one_add_mul_sqrt_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#fib-eq-integral-one-add-mul-sqrt-five).

## Binomial sum of generalized Fibonacci polynomials as an integral

Let $d$ and $g$ be
polynomials with integer coefficients, let $F_m$ be the generalized Fibonacci polynomials with
$F_0 = 0$, $F_1 = 1$ and $F_{m+2} = d F_{m+1} + g F_m$, and let $x$ be a real number with
$d(x)^2 + 4 g(x) \ge 0$ and $g(x) \ne 0$. Let $\Phi \colon \mathbb{Z} \to \mathbb{R}$ satisfy
$\Phi(m) = F_m(x)$ for $m \ge 0$ and $\Phi(m+2) = d(x) \Phi(m+1) + g(x) \Phi(m)$ for every integer
$m$. Then for every real $k \ge 2$ and every integer $n \ge 1$,

$$\sum_{i=0}^{n} (-1)^{n+1} \binom{n}{i} (k+1)^i (k-1)^{n-i} g(x)^i \, \Phi(n-2i)
  = n \int_{-k}^{k} \Big(y \sqrt{d(x)^2 + 4 g(x)} + d(x)\Big)^{n-1} dy.$$

The extension $\Phi$ of $m \mapsto F_m(x)$ to negative indices exists only when $g(x) \ne 0$: if
$g(x) = 0$, the recurrence at $m = -1$ forces $F_1(x) = d(x) F_0(x) = 0$.

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Proposition 5.2.

Stated but not proved: `MetaMathlibExt.gfp_fib_binomial_sum_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#gfp-fib-binomial-sum-eq-integral).

## Binomial sum of Fibonacci numbers as an integral

Let $F \colon \mathbb{Z} \to \mathbb{R}$
be a function whose value $F_m$ at every $m \ge 0$ is the $m$-th Fibonacci number (with $F_0 = 0$
and $F_1 = 1$) and which satisfies $F_{m+2} = F_{m+1} + F_m$ for every integer $m$. Then for every
real $k \ge 2$ and every integer $n \ge 1$,

$$\sum_{i=0}^{n} (-1)^{n+1} \binom{n}{i} (k+1)^i (k-1)^{n-i} F_{n-2i}
  = n \int_{-k}^{k} (\sqrt{5}\, y + 1)^{n-1} \, dy.$$

## Sources

- Maribel Diaz Noguera, Rigoberto Flórez, José L. Ramírez, and Martha Romero Rojas, *Catalan Identities for Generalized Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article florez11012023, Corollary 5.2.

Stated but not proved: `MetaMathlibExt.fib_binomial_sum_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/GFPCatalanIdentitiesWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html#fib-binomial-sum-eq-integral).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Catalan identities for generalized Fibonacci polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/catalan-identities-for-generalized-fibonacci-pol)
