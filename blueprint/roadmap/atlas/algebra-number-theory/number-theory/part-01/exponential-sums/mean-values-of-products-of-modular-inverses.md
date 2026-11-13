---
declaration: section
origin: cited
lean: MetaMathlibExt.modularProductSum, MetaMathlibExt.modularProductSum_two_three_one, MetaMathlibExt.modularProductSum_one_five_three, MetaMathlibExt.xuZhangConstant, MetaMathlibExt.xuZhangConstant_prime, MetaMathlibExt.modularProductSum_explicit_estimate, MetaMathlibExt.modularProductSum_odd_estimate, MetaMathlibExt.modularProductSum_two_explicit_estimate
statement: formalized
---

# Mean values of products of modular inverses

18 results, 5 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html).

## The modular product sum $S_k(n, m)$

For natural numbers $k$, $n$ and $m$, the modular
product sum $S_k(n, m)$ is the natural number

$$S_k(n, m) = \sum a_1 a_2 \cdots a_k,$$

the sum running over all $k$-tuples $(a_1, \dots, a_k) \in \{1, \dots, n\}^k$ such that every
$a_j$ is coprime to $n$ and $a_1 a_2 \cdots a_k \equiv m \pmod n$. For $k = 2$ and $m = 1$ this is
the sum of the products $a \bar{a}$, where $a$ runs over the numbers in $\{1, \dots, n\}$ coprime
to $n$ and $\bar{a} \in \{1, \dots, n\}$ is the inverse of $a$ modulo $n$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, equation (2).

Formalized by `MetaMathlibExt.modularProductSum`, a definition declared in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum).

## The modular product sum $S_2(3, 1)$

The modular product sum satisfies $S_2(3, 1) = 5$:
the pairs $(a_1, a_2) \in \{1, 2, 3\}^2$ of numbers coprime to $3$ with $a_1 a_2 \equiv 1 \pmod 3$
are $(1, 1)$ and $(2, 2)$, and $1 \cdot 1 + 2 \cdot 2 = 5$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, equation (2).

Formalized by `MetaMathlibExt.modularProductSum_two_three_one`, a theorem declared in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum-two-three-one).

## The modular product sum $S_1(5, 3)$

The modular product sum satisfies $S_1(5, 3) = 3$:
the only $a \in \{1, \dots, 5\}$ coprime to $5$ with $a \equiv 3 \pmod 5$ is $a = 3$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, equation (2).

Formalized by `MetaMathlibExt.modularProductSum_one_five_three`, a theorem declared in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum-one-five-three).

## Xu–Zhang constant

For a natural number $q$, the Xu–Zhang constant $C_q$ is the product
over the prime factors $p$ of $q$, with $p^\alpha$ the exact power of $p$ dividing $q$,

$$C_q = \prod_{p^\alpha \parallel q} \left(1 + \frac{2p^3 + p^2 - 1}{(p^2 + 1)(p^2 + p + 1)} -
\frac{1}{p^{3(\alpha - 1)} (p^2 + p + 1)}\right).$$

For $q = 1$, and by convention for $q = 0$, there are no prime factors, so $C_0 = C_1 = 1$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, equation (4), quoting Z. Xu and W. Zhang, *Fourth power mean of character sums*, Acta Arith. 135 (2008), Lemma 9.

Formalized by `MetaMathlibExt.xuZhangConstant`, a definition declared in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#xu-zhang-constant).

## Xu–Zhang constant at a prime

For every prime $p$, the Xu–Zhang constant of $p$ is

$$C_p = 1 + \frac{2p^3 + p^2 - 1}{(p^2 + 1)(p^2 + p + 1)} - \frac{1}{p^2 + p + 1}.$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, equation (4).

Formalized by `MetaMathlibExt.xuZhangConstant_prime`, a theorem declared in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#xu-zhang-constant-prime).

## Explicit estimate for the modular product sum $S_k(n, m)$

Let $\varphi$ be Euler's
totient function and $S_k(n, m)$ the modular product sum. For all natural numbers $k \ge 3$,
$n \ge 2$ and $m$ with $\gcd(m, n) = 1$,

$$\left| S_k(n, m) - \frac{n^k \varphi(n)^{k-1}}{2^k} \right| \le
(2\sqrt{3})^k \, n^{3k/2} (\log n)^k.$$

The paper also assumes $m \ge 1$, which follows from $\gcd(m, n) = 1$ and $n \ge 2$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Theorem 1.

Stated but not proved: `MetaMathlibExt.modularProductSum_explicit_estimate` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum-explicit-estimate).

## Estimate for the modular product sum $S_k(n, m)$ at odd moduli

Let $\varphi$ be Euler's
totient function and $S_k(n, m)$ the modular product sum. For every natural number $k \ge 4$
there is a real constant $C_k$ such that for every odd natural number $n \ge 3$ and every natural
number $m$ with $\gcd(m, n) = 1$,

$$\left| S_k(n, m) - \frac{n^k \varphi(n)^{k-1}}{2^k} \right| \le
C_k \, n^{3(k-2)/2} \varphi(n)^3 (\log n)^{k-4} (\log \log n)^2.$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Theorem 2.

Stated but not proved: `MetaMathlibExt.modularProductSum_odd_estimate` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum-odd-estimate).

## Explicit estimate for the modular product sum $S_2(n, m)$

Let $\varphi$ be Euler's
totient function, $\tau(n)$ the number of divisors of $n$,
$\sigma_{1/2}(n) = \sum_{d \mid n} \sqrt{d}$ and $S_2(n, m)$ the modular product sum. For all
natural numbers $n \ge 2$ and $m$ with $\gcd(m, n) = 1$,

$$\left| S_2(n, m) - \frac{n^2 \varphi(n)}{4} \right| \le
n^2 \sigma_{1/2}(n) \bigl(\tau(n) \log(en)\bigr)^2 + \frac{n \varphi(n)}{4}.$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Theorem 3.

Stated but not proved: `MetaMathlibExt.modularProductSum_two_explicit_estimate` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum-two-explicit-estimat).

## Mean square of the error in the modular product sum $S_2(n, m)$

Let $\varphi$ be Euler's
totient function, $S_2(n, m)$ the modular product sum and $C_n$ the Xu–Zhang constant of $n$.
For every real $\varepsilon > 0$ there is a real constant $C$ such that for every odd natural
number $n \ge 3$,

$$\left| \sum_{1 \le m \le n,\ \gcd(m, n) = 1}
\left( S_2(n, m) - \frac{n^2 \varphi(n)}{4} \right)^2 -
\frac{5 C_n}{144} \bigl(n \varphi(n)\bigr)^3 \right| \le C n^{5 + \varepsilon}.$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Theorem 4.

Stated but not proved: `MetaMathlibExt.modularProductSum_two_mean_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum-two-mean-square).

## Large values of the error in the modular product sum $S_2(n, m)$

Let $\varphi$ be Euler's
totient function and $S_2(n, m)$ the modular product sum. There are a real number $c > 0$ and a
natural number $N$ such that every odd natural number $n \ge N$ admits a natural number $m$ with
$1 \le m \le n$ and $\gcd(m, n) = 1$ for which

$$\left| S_2(n, m) - \frac{n^2 \varphi(n)}{4} \right| \ge c \, n^{3/2} \varphi(n).$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Theorem 4.

Stated but not proved: `MetaMathlibExt.modularProductSum_two_error_large` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#modular-product-sum-two-error-large).

## Xu–Zhang twisted fourth moment of weighted character sums

Let $\varphi$ be Euler's totient
function and $C_q$ the Xu–Zhang constant of $q$. For every natural number $\ell$ and every real
$\varepsilon > 0$ there is a real constant $C$ such that for every odd natural number $q \ge 3$,

$$\left| \sum_{\chi \bmod q,\ \chi(-1) = -1} \overline{\chi(2^\ell)}
\left| \sum_{a=1}^{q} a \, \chi(a) \right|^4 -
\frac{C_q (3\ell + 5) q^3 \varphi(q)^4}{72 \cdot 2^{\ell + 1}} \right| \le C q^{6 + \varepsilon},$$

where $\chi$ runs over the complex Dirichlet characters modulo $q$ with $\chi(-1) = -1$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Lemma 1 (journal PDF p. 4), quoting Z. Xu and W. Zhang, *Fourth power mean of character sums*, Acta Arith. 135 (2008), Lemma 9.

Stated but not proved: `MetaMathlibExt.odd_character_twisted_weighted_sum_fourth_moment` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#odd-character-twisted-weighted-sum-fourt).

## Fourth moment of weighted odd character sums

There is a real constant $C$ such that for
every odd integer $n \ge 3$,

$$\sum_{\chi \text{ odd}} \Bigl|\sum_{a=1}^{n} a\, \chi(a)\Bigr|^4 \le
C\, n^3 \varphi(n)^4 (\log\log n)^2,$$

where $\chi$ runs over the odd Dirichlet characters modulo $n$ (those with $\chi(-1) = -1$) and
$\varphi$ is Euler's totient function.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Corollary 1.

Stated but not proved: `MetaMathlibExt.odd_character_weighted_sum_fourth_moment` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#odd-character-weighted-sum-fourth-moment).

## Bound for a weighted Kloosterman-type sum

Let $n \ge 1$ and $k \ge 1$ be integers and let
$m$ be a natural number coprime to $n$. Write $e_n(x) = e^{2\pi i x / n}$, and for $a$ coprime to
$n$ let $\bar a \in \{0, \dots, n - 1\}$ be the inverse of $a$ modulo $n$. Then

$$\Bigl|\sum_{1 \le a \le n,\ \gcd(a, n) = 1} a\, e_n(k m \bar a)\Bigr| \le
2 n^{3/2} \tau(n) \sqrt{\gcd(n, k)} \log(e n),$$

where $\tau(n)$ is the number of positive divisors of $n$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Lemma 2.

Stated but not proved: `MetaMathlibExt.weighted_kloosterman_sum_bound` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#weighted-kloosterman-sum-bound).

## Weighted sum of an additive character

Let $q \ge 2$, let $k$ be a natural number not
divisible by $q$, and write $e_q(x) = e^{2\pi i x / q}$. Then

$$\sum_{b=1}^{q-1} b\, e_q(-kb) = -\frac{q}{1 - e_q(-k)}.$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Lemma 3.

Stated but not proved: `MetaMathlibExt.sum_mul_additive_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#sum-mul-additive-character).

## Weighted additive character sum over reduced residues

For a positive integer $r$ and an
integer $x$ write $e_r(x) = \exp(2\pi i x / r)$, and let $\mu$ be the Möbius function. For all
natural numbers $n \ge 2$ and $k \ge 1$,

$$\sum_{1 \le b \le n,\ \gcd(b, n) = 1} b \, e_n(-kb)
= -n \sum_{d \mid n,\ (n/d) \nmid k} \frac{\mu(d)}{1 - e_{n/d}(-k)} +
\frac{n}{2} \sum_{d \mid n,\ d < n,\ (n/d) \mid k} \mu(d) \left(\frac{n}{d} - 1\right).$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Lemma 4.

Stated but not proved: `MetaMathlibExt.coprime_sum_mul_additive_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#coprime-sum-mul-additive-character).

## Splitting a sum by greatest common divisor

For every function
$f : \mathbb{N} \to \mathbb{C}$ and every natural number $n$,

$$\sum_{k=1}^{n} f(k) = \sum_{d \mid n} \sum_{1 \le h \le n/d,\ \gcd(n/d, h) = 1} f(hd).$$

Here $d$ runs over the positive divisors of $n$, and $0$ is taken to have none, so for $n = 0$
both sides are empty sums.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Lemma 5.

Stated but not proved: `MetaMathlibExt.sum_Icc_eq_sum_divisors_coprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#sum-icc-eq-sum-divisors-coprime).

## Sum of reciprocal distances from roots of unity to 1

Let $q \ge 2$ and $\ell \ge 1$ be
integers, let $s \in \{1, -1\}$, and write $e_q(x) = e^{2\pi i x / q}$. Then

$$\sum_{0 \le a < q,\ q \nmid a\ell} \frac{1}{|1 - e_q(s a \ell)|} \le
\frac{q}{2} \log \frac{e q}{2 \gcd(\ell, q)} < \frac{q}{2} \log(e q).$$

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Lemma 6.

Stated but not proved: `MetaMathlibExt.sum_inv_norm_one_sub_additive_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#sum-inv-norm-one-sub-additive-character).

## Gcd-weighted sum of reciprocal distances from roots of unity to 1

Let $n \ge 2$, let $d$
be a divisor of $n$, and write $e_m(x) = e^{2\pi i x / m}$. Then

$$\sum_{1 \le k \le n-1,\ (n/d) \nmid k} \frac{\sqrt{\gcd(n, k)}}{|1 - e_{n/d}(-k)|} \le
\frac{1}{2} \sqrt{n}\, \sigma_{1/2}(n) \log(e n),$$

where $\sigma_{1/2}(n) = \sum_{\delta \mid n} \sqrt{\delta}$.

## Sources

- O. Bordellès and L. Tóth, *Mean Values of the Product of an Integer and Its Modular Inverse*, INTEGERS 24 (2024), Article A33, Lemma 7.

Stated but not proved: `MetaMathlibExt.sum_sqrt_gcd_div_norm_one_sub_additive_character` is written with `theorem_wanted` in [WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ModularInverseProductMeanWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html#sum-sqrt-gcd-div-norm-one-sub-additive-c).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mean values of products of modular inverses](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/exponential-sums/mean-values-of-products-of-modular-inverses)
