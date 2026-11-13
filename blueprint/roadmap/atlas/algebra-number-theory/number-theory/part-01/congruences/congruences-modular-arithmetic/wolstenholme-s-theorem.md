---
declaration: section
origin: cited
lean: ZMod.carlitz_sum_inv_block_Ico_eq_zero_of_five_le, MathlibExt.NumberTheory.Wolstenholme.wolstenholme, MetaMathlibExt.wolstenholme_harmonic_power_sum, MetaMathlibExt.coeff_add_one_pow_mul_X_pow_add_one_pow, MetaMathlibExt.ringChoose_neg_mul_mul_eq, MetaMathlibExt.choose_mul_prime_prime_harmonic_congr, MetaMathlibExt.ringChoose_mul_prime_sub_one_mul_congr, MetaMathlibExt.norm_choose_nsmul_coeff_le
statement: formalized
---

# Wolstenholme's theorem

23 results, 3 proved and 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html).

## Carlitz's block harmonic congruence

Let $p \ge 5$ be a prime and let $k \in \mathbb{N}$.
Then in $\mathbb{Z}/p^2\mathbb{Z}$

$$\sum_{r=1}^{p-1} (kp + r)^{-1} = 0.$$

Each $kp + r$ with $1 \le r \le p - 1$ is prime to $p$, so these inverses are genuine inverses
modulo $p^2$.

Cited original: L. Carlitz, "A note on Wolstenholme's theorem", American
Mathematical Monthly 61 (1954), 174–176.

## Sources

- Jerry Metzger and Thomas Richards, "A Prisoner Problem Variation", <https://cs.uwaterloo.ca/journals/JIS/VOL18/Metzger/metz1.tex>, lines 657–662.

Formalized by `ZMod.carlitz_sum_inv_block_Ico_eq_zero_of_five_le`, a theorem declared in [MathlibExt/NumberTheory/CarlitzBlockHarmonic.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/CarlitzBlockHarmonic.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#carlitz-sum-inv-block-ico-eq-zero-of-fiv).

## Wolstenholme's theorem

If $p \ge 5$ is prime, then $\sum_{k=1}^{p-1} k^{-1} = 0$ in
$\mathbb{Z}/p^2\mathbb{Z}$, where $k^{-1}$ is the inverse of $k$ modulo $p^2$.

Formalized by `MathlibExt.NumberTheory.Wolstenholme.wolstenholme`, a theorem declared in [MathlibExt/NumberTheory/Wolstenholme.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Wolstenholme.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#wolstenholme).

## Wolstenholme's congruence for odd powers

Let $\nu \ge 1$ be odd and let $p$ be a prime with
$p \ge \nu + 4$. Then in $\mathbb{Z}/p^2\mathbb{Z}$

$$
\sum_{t=1}^{p-1} (t^{\nu})^{-1} = 0,
$$

where each $t^{\nu}$ is invertible modulo $p^2$ because $1 \le t < p$.

For $\nu = 1$ this is Wolstenholme's congruence of 1862; the general statement is Theorem 131 of
Hardy and Wright and was first studied by Leudesdorf.

## Sources

- Christian Ballot, "On a Congruence of Kimball and Webb Involving Lucas Sequences," Journal of Integer Sequences 17 (2014), Article 14.1.3, Theorem, lines 94–99, https://cs.uwaterloo.ca/journals/JIS/VOL17/Ballot/ballot7.tex

Formalized by `MetaMathlibExt.wolstenholme_harmonic_power_sum`, a theorem declared in [MathlibExt/NumberTheory/WolstenholmePowerSums.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/WolstenholmePowerSums.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#wolstenholme-harmonic-power-sum).

## Coefficients of $(x + 1)^{jp} (x^p + 1)^{n-j}$

Let $n$, $j$ and $k$ be natural numbers and
$p$ a positive integer, and let $d = \max(n - j, 0)$. Then the coefficient of $x^{kp}$ in the
polynomial $(x + 1)^{jp} (x^p + 1)^{d}$ is

$$\sum_{s=0}^{\min(j, k)} \binom{jp}{sp} \binom{d}{k - s}.$$

The source takes $p$ prime; here $p$ is any positive integer.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Lemma 2.

Stated but not proved: `MetaMathlibExt.coeff_add_one_pow_mul_X_pow_add_one_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#coeff-add-one-pow-mul-x-pow-add-one-pow).

## Binomial coefficients with upper index $-np$

Let $p$, $n$ and $k$ be natural numbers
with $p \ge 1$ and $k \ge 1$. For an integer $x$ and a natural number $r$ write
$\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$. Then

$$
\binom{-np}{kp} = (-1)^{kp} \, \frac{n}{k} \binom{(n+k)p - 1}{kp - 1} =
(-1)^{kp} \, \frac{n}{n+k} \binom{(n+k)p}{kp}.
$$

The paper takes $p$ prime.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Lemma 5.

Stated but not proved: `MetaMathlibExt.ringChoose_neg_mul_mul_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-neg-mul-mul-eq).

## Congruences for $\binom{tp}{p}$ modulo $p^5$, $p^6$ and $p^7$

Let $p \ge 11$ be a prime
and $t$ a natural number. Write $H_{p-1}^{(r)} = \sum_{j=1}^{p-1} 1/j^r$ for the harmonic number of
order $r$ and $H_{p-1}(1, 1) = \sum_{1 \le i < j \le p-1} 1/(ij)$. For rational numbers $x$, $y$
and a natural number $s$, write $x \equiv y \pmod{p^s}$ when $x = y$ or $v_p(x - y) \ge s$, where
$v_p$ is the $p$-adic valuation on $\mathbb{Q}$. Then

$$\binom{tp}{p} \equiv t + (-t^5 + 2t^4 - t^2) \, p \, H_{p-1}^{(1)} +
t^3 (t-1)^2 p^2 H_{p-1}(1, 1) \pmod{p^7},$$



$$\binom{tp}{p} \equiv t + (-t^5 + 2t^4 - t^2) \, p \, H_{p-1}^{(1)} -
\frac{t^3 (t-1)^2}{2} \, p^2 H_{p-1}^{(2)} \pmod{p^6},$$

and

$$\binom{tp}{p} \equiv t + t^2 (t-1) \, p \, H_{p-1}^{(1)} \pmod{p^5}.$$

The double sum $H_{p-1}(1, 1)$ is taken over $i < j$; under this reading the first two
congruences agree modulo $p^6$.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Theorem 10.

Stated but not proved: `MetaMathlibExt.choose_mul_prime_prime_harmonic_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#choose-mul-prime-prime-harmonic-congr).

## Congruences modulo $p^7$ for $\binom{\alpha p - 1}{p - 1} \binom{(\alpha + 1)p - 1}{p - 1}$ and $\binom{2p - 1}{p - 1}^{-1}$

**Congruences modulo $p^7$ for $\binom{\alpha p - 1}{p - 1} \binom{(\alpha + 1)p - 1}{p - 1}$
and $\binom{2p - 1}{p - 1}^{-1}$.** Let $p \ge 11$ be a prime and let $\alpha$ be an integer. For
an integer $x$ and a natural number $r$ write $\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, let
$H_{p-1}^{(r)} = \sum_{j=1}^{p-1} 1/j^r$ be the harmonic number of order $r$, and let $v_p$ be the
$p$-adic valuation on $\mathbb{Q}$. Put

$$
X = \binom{\alpha p - 1}{p - 1} \binom{(\alpha + 1)p - 1}{p - 1} - 1 +
(\alpha p)^2 H_{p-1}^{(2)} - \frac{(\alpha p)^4}{2} \Big(\big(H_{p-1}^{(2)}\big)^2 -
H_{p-1}^{(4)}\Big)
$$

and

$$
Y = \binom{2p - 1}{p - 1}^{-1} - 1 - p^2 H_{p-1}^{(2)} -
\frac{p^4}{2} \Big(\big(H_{p-1}^{(2)}\big)^2 + H_{p-1}^{(4)}\Big).
$$

Then either $X = 0$ or $v_p(X) \ge 7$, and either $Y = 0$ or $v_p(Y) \ge 7$.

The paper allows $\alpha \in \mathbb{Z}_p$; only integers $\alpha$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Theorem 13.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_one_mul_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-one-mul-congr).

## Coefficient bound for the divided derivatives $D^n/n!$

Let $p$ be a prime and $B$ a
normed vector space over $\mathbb{Q}_p$ whose norm is ultrametric. Let $(a_k)_{k \ge 0}$ be a
sequence in $B$ and $C$ a real number with $\|a_k\| \le C$ for every $k$. Then for all natural
numbers $n$ and $k$,

$$\Big\| \binom{k+n}{n} a_{k+n} \Big\| \le C.$$

The vectors $\binom{k+n}{n} a_{k+n}$ are the coefficients of $D^n f / n!$ for
$f = \sum_k a_k t^k$, so this is the coefficientwise form of the bound $\|D^n / n!\| \le 1$ on
the Tate algebra $B\{t\}$ with the sup norm.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Lemma 1.

Stated but not proved: `MetaMathlibExt.norm_choose_nsmul_coeff_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#norm-choose-nsmul-coeff-le).

## Higher $p$-adic mean value theorem

Let $p$ be a prime, let $|\cdot|$ be the $p$-adic
absolute value on $\mathbb{Q}_p$, and let $B$ be a normed vector space over $\mathbb{Q}_p$ whose
norm is ultrametric. Let $N$ and $m$ be natural numbers with $1 \le m \le p$, let
$f(t) = \sum_{j\lt N} a_j t^j$ be a polynomial with coefficients $a_j \in B$, and let
$t, h \in \mathbb{Q}_p$ with $|t| \le 1$. Suppose that $|h| \le p^{-1/(p-m)}$ if $m < p$, that
$|h| \le p^{-1/p}$ if $m = p$, and that $C \ge 0$ is a real number with
$\|j(j-1)\cdots(j-m+1) \, a_j\| \le C$ for every $j < N$. Then

$$\Big\| f(t+h) - \sum_{q\lt m} \sum_{q \le j < N} \binom{j}{q} t^{j-q} h^q a_j \Big\| \le
\Big| \frac{h^m}{m} \Big| \, C.$$

The inner sum $\sum_{q \le j < N} \binom{j}{q} t^{j-q} a_j$ is $f^{(q)}(t)/q!$, and the least
admissible $C$ is the sup of the norms of the coefficients of $f^{(m)}$.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Theorem 1.

Stated but not proved: `MetaMathlibExt.norm_sub_taylor_le_of_norm_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#norm-sub-taylor-le-of-norm-le).

## Congruence form of the higher $p$-adic mean value theorem

Let $p$ be a prime, let
$|\cdot|$ be the $p$-adic absolute value on $\mathbb{Q}_p$, and let $B$ be a normed vector space
over $\mathbb{Q}_p$ whose norm is ultrametric. Let $N$ and $m$ be natural numbers with
$1 \le m \le p$, let $f(t) = \sum_{j\lt N} a_j t^j$ with $a_j \in B$, let $t, h \in \mathbb{Q}_p$
with $|t| \le 1$, and let $w$ be a real number with
$\|j(j-1)\cdots(j-m+1) \, a_j\| \le p^{-w}$ for every $j < N$. Write

$$R = \Big\| f(t+h) - \sum_{q\lt m} \sum_{q \le j < N} \binom{j}{q} t^{j-q} h^q a_j \Big\|$$

and let $v_p(h)$ be the $p$-adic valuation of $h$, taken to be $0$ when $h = 0$. Then
$R \le p^{-(m v_p(h) + w)}$ if $m < p$ and $v_p(h) \ge 1/(p-m)$;
$R \le p^{-(p v_p(h) + w - 1)}$ if $m = p$ and $v_p(h) \ge 1/p$; and $R = 0$ if $h = 0$.

Reading a congruence modulo $p^v$ in $B$ as norm at most $p^{-v}$, the first two bounds say
$f(t+h) \equiv \sum_{q\lt m} f^{(q)}(t) h^q / q!$ modulo $p^{m v_p(h) + w}$ and
$p^{p v_p(h) + w - 1}$ respectively.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Theorem 2.

Stated but not proved: `MetaMathlibExt.norm_sub_taylor_le_zpow_valuation` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#norm-sub-taylor-le-zpow-valuation).

## Alternating binomial sum identities

For an integer $x$ and a natural number $r$ write
$\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$ for the generalized binomial coefficient. Let $m$, $n$
and $k$ be natural numbers. Then for every natural number $j \le m$,

$$\sum_{s=j}^{m} (-1)^{s-j} \binom{n}{s} \binom{s}{j} = (-1)^{m-j} \binom{n}{j} \binom{n-j-1}{m-j}
= \binom{n}{j} \binom{m-n}{m-j},$$

and

$$\sum_{j=0}^{m} (-1)^{m-j} \binom{n}{j} \binom{n-j-1}{m-j} \binom{n-j}{k} =
\binom{n}{k} \binom{m-k}{m},$$



$$\sum_{j=0}^{\min(m, k)} (-1)^{m-j} \binom{n}{j} \binom{n-j-1}{m-j} \binom{n-j}{k-j} =
\binom{n}{k} \binom{k+m-n}{m}.$$

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Lemma 3.

Stated but not proved: `MetaMathlibExt.alternating_choose_sum_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#alternating-choose-sum-identities).

## The general congruence for $\binom{np}{kp}$

Let $p$ be a prime, let $m$ and $k$ be
natural numbers with $m + 1 < p$, and let $n$ be an integer. For an integer $x$ and a natural
number $r$ write $\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and let $v_p$ be the $p$-adic
valuation on $\mathbb{Q}$. For natural numbers $j$ and $l$ put

$$
c_j = \sum_{s=0}^{\min(j, k)} \binom{jp}{sp} \binom{n-j}{k-s}, \qquad
d_l = \binom{n}{l} \sum_{j=0}^{l} (-1)^{l-j} \binom{l}{j} c_j,
$$

and let $X = \binom{np}{kp} - \binom{n}{k} - (d_1 + \cdots + d_m)$. Then either $X = 0$, or
$\binom{n}{m+1} \ne 0$ and $v_p(X) \ge m + 1 + v_p\big(\binom{n}{m+1}\big)$. That is,
$\binom{np}{kp} - \binom{n}{k} \equiv d_1 + \cdots + d_m$ modulo $p^{m+1+v_p(\binom{n}{m+1})}$,
with equality when $\binom{n}{m+1} = 0$.

The paper allows $n \in \mathbb{Z}_p$; only integers $n$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Theorem 3.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_sum_d` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-sum-d).

## Congruence for $\binom{np}{kp}$ with the coefficients $\bar C_{ji}$

Let $p$ be a prime,
let $m$ and $k$ be natural numbers with $m + 1 < p$, and let $n$ be an integer. For an integer
$x$ and a natural number $r$ write $\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and set
$\binom{x}{r} = 0$ for negative $r$. Let

$$\bar C_{00} = \left( \binom{m-k}{m} + \binom{k+m-n}{m} + (-1)^{m+1} \binom{n-1}{m} - 1 \right)
\binom{n}{k},$$

let $\bar C_{ji} = \binom{n}{j} \binom{m-n}{m-j} \binom{n-j}{k-i}$, and let

$$X = \binom{np}{kp} - \binom{n}{k} - \bar C_{00} -
\sum_{1 \le i < j \le m} \bar C_{ji} \binom{jp}{ip}.$$

Then either $X = 0$, or $\binom{n}{m+1} \ne 0$ and
$v_p(X) \ge m + 1 + v_p\big(\binom{n}{m+1}\big)$, where $v_p$ is the $p$-adic valuation on
$\mathbb{Q}$. With $v_p(0) = \infty$ this says $X \equiv 0 \pmod{p^{m+1+v_p(\binom{n}{m+1})}}$.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Lemma 4.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_cbar` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-cbar).

## The congruence for $\binom{np}{kp}$ with symmetrized coefficients

Let $p$ be a prime,
let $m$ and $k$ be natural numbers with $m + 1 < p$, and let $n$ be an integer. For an integer
$x$ and a natural number $r$ write $\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, for a rational
number $x$ write $(x)_r = x(x-1)\cdots(x-r+1)$ for the falling factorial, and let $v_p$ be the
$p$-adic valuation on $\mathbb{Q}$. Put

$$
C'_{00} = \left(\binom{m-k}{m} + \binom{k+m-n}{m} + (-1)^{m+1} \binom{n-1}{m} - 1\right)
\binom{n}{k}
$$

and, for $2 \le j \le m$ and $1 \le i \le \lfloor j/2 \rfloor$,

$$
C'_{ji} = \varepsilon_{ji} \, \frac{(n-k)_{j-i} \, (k)_i + (n-k)_i \, (k)_{j-i}}{j!}
\binom{m-n}{m-j} \binom{n}{k},
$$

where $\varepsilon_{ji} = 1/2$ if $j = 2i$ and $\varepsilon_{ji} = 1$ otherwise. Let

$$
X = \binom{np}{kp} - \binom{n}{k} - C'_{00} -
\sum_{j=2}^{m} \sum_{i=1}^{\lfloor j/2 \rfloor} C'_{ji} \binom{jp}{ip}.
$$

Then either $X = 0$, or $\binom{n}{m+1} \ne 0$ and
$v_p(X) \ge m + 1 + v_p\big(\binom{n}{m+1}\big)$. That is, $\binom{np}{kp} - \binom{n}{k}$ is
congruent to $C'_{00} + \sum_{j, i} C'_{ji} \binom{jp}{ip}$ modulo
$p^{m+1+v_p(\binom{n}{m+1})}$, and equal to it when $\binom{n}{m+1} = 0$.

The paper allows $n \in \mathbb{Z}_p$; only integers $n$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Theorem 4.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_cprime` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 271](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L271). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-cprime).

## Divisibility of the polynomial parts by $k(n-k)/2$

Let $m$ be a natural number and $n$ an
integer. For an integer $x$ and a natural number $r$ write $\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$,
and for a rational number $x$ write $(x)_r = x(x-1)\cdots(x-r+1)$ for the falling factorial. Then
there is a polynomial $Q \in \mathbb{Q}[X]$ such that for every natural number $k$

$$\binom{m-k}{m} + \binom{k+m-n}{m} + (-1)^{m+1} \binom{n-1}{m} - 1 = \frac{k(n-k)}{2} \, Q(k),$$

and for all natural numbers $i$ and $j$ with $1 \le i < j$ there is a polynomial
$Q \in \mathbb{Q}[X]$ such that for every natural number $k$

$$\frac{(n-k)_{j-i} \, (k)_i + (n-k)_i \, (k)_{j-i}}{j!} \binom{m-n}{\max(m-j, 0)} =
\frac{k(n-k)}{2} \, Q(k).$$

For $j \le m$ the left-hand sides are the polynomial parts of the coefficients
$C'_{00}(m, n, k)$ and $C'_{ji}(m, n, k)$ of Theorem 4 (the halving at $j = 2i$ does not affect
divisibility); agreement at every natural number $k$ amounts to divisibility by $k(n-k)/2$
in $\mathbb{Q}[k]$.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Proposition 1.

Stated but not proved: `MetaMathlibExt.exists_polynomial_part_eq_mul_half_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#exists-polynomial-part-eq-mul-half-mul).

## The congruence for $\binom{np}{kp}$ modulo $p^3$

Let $p \ge 5$ be a prime, let $k$ be a
natural number and let $n$ be an integer. For an integer $x$ and a natural number $r$ write
$\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and let $v_p$ be the $p$-adic valuation on
$\mathbb{Q}$. Let

$$
X = \binom{np}{kp} - \binom{n}{k} - \frac{k(n-k)}{2} \binom{n}{k} \left(\binom{2p}{p} - 2\right).
$$

Then either $X = 0$, or $\binom{n}{3} \ne 0$ and $v_p(X) \ge 3 + v_p\big(\binom{n}{3}\big)$; that
is, $X \equiv 0 \pmod{p^{3+v_p(\binom{n}{3})}}$, and $X = 0$ when $\binom{n}{3} = 0$.

The paper allows $n \in \mathbb{Z}_p$; only integers $n$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Proposition 2.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_pow_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-pow-thre).

## Equivalent forms of Wolstenholme's congruence

Let $p \ge 5$ be a prime and let $n$ and
$k$ be natural numbers. Then the congruences $\binom{2p}{p} \equiv 2$, $\binom{np}{p} \equiv n$ and
$\binom{np}{kp} \equiv \binom{n}{k}$ modulo $p^3$ are equivalent.

By Wolstenholme's theorem all three hold for every such $p$.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Corollary 2.

Stated but not proved: `MetaMathlibExt.choose_two_mul_prime_congr_iff_pow_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#choose-two-mul-prime-congr-iff-pow-three).

## The congruence for $\binom{np}{kp}$ modulo $p^4$ via $\binom{2p}{p}$ and $\binom{3p}{p}$

Let $p \ge 7$ be a prime, let $k$ be a natural number and let $n$ be an integer. For an integer
$x$ and a natural number $r$ write $\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and let $v_p$ be
the $p$-adic valuation on $\mathbb{Q}$. Let

$$
X = \binom{np}{kp} - \binom{n}{k} - \frac{k(n-k)}{2} \binom{n}{k} \left((n - 4) +
(3 - n) \binom{2p}{p} + \frac{n - 2}{3} \binom{3p}{p}\right).
$$

Then either $X = 0$, or $\binom{n}{4} \ne 0$ and $v_p(X) \ge 4 + v_p\big(\binom{n}{4}\big)$; that
is, $X \equiv 0 \pmod{p^{4+v_p(\binom{n}{4})}}$, and $X = 0$ when $\binom{n}{4} = 0$.

The paper allows $n \in \mathbb{Z}_p$; only integers $n$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Proposition 3.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_pow_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-pow-four).

## The congruence for $\binom{np}{kp}$ modulo $p^4$ via $\binom{2p}{p}$ alone

Let
$p \ge 7$ be a prime, let $k$ be a natural number and let $n$ be an integer. For an integer $x$
and a natural number $r$ write $\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and let $v_p$ be the
$p$-adic valuation on $\mathbb{Q}$, with the convention $v_p(0) = 0$. Let

$$
X = \binom{np}{kp} - \binom{n}{k} - \frac{nk(n-k)}{4} \binom{n}{k} \left(\binom{2p}{p} - 2\right).
$$

Then either $X = 0$ or $v_p(X) \ge 4 + v_p\big(\binom{n}{4}\big)$. In particular, when
$\binom{n}{4} = 0$, that is $n \in \{0, 1, 2, 3\}$, the conclusion is only that $X = 0$ or
$v_p(X) \ge 4$.

Equality cannot be demanded when $\binom{n}{4} = 0$: for $p = 7$, $n = 3$ and $k = 1$ one has
$X = 100842 = 6 \cdot 7^5$. The paper allows $n \in \mathbb{Z}_p$; only integers $n$ are covered
here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Theorem 6.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_pow_four_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 366](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L366). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-pow-four-2).

## The congruence for $\binom{np}{kp}$ modulo $p^5$

Let $p \ge 11$ be a prime, let $k$ be a
natural number and let $n$ be an integer. For an integer $x$ and a natural number $r$ write
$\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and let $v_p$ be the $p$-adic valuation on
$\mathbb{Q}$. Put $C_{00} = -(k^2 - kn + 2n^2 - 15n + 35)/6$, $C_{21} = (n-4)(n-3)/2$,
$C_{31} = (n-2)(4-n)/3$, $C_{41} = (2k^2 - 2kn + n^2 - 3n + 4)/12$ and
$C_{42} = (n-k-1)(k-1)/12$, and let

$$
X = \binom{np}{kp} - \binom{n}{k} - \frac{k(n-k)}{2} \binom{n}{k} \Big(C_{00} +
C_{21} \binom{2p}{p} + C_{31} \binom{3p}{p} + C_{41} \binom{4p}{p} + C_{42} \binom{4p}{2p}\Big).
$$

Then either $X = 0$, or $\binom{n}{5} \ne 0$ and $v_p(X) \ge 5 + v_p\big(\binom{n}{5}\big)$; that
is, $X \equiv 0 \pmod{p^{5+v_p(\binom{n}{5})}}$, and $X = 0$ when $\binom{n}{5} = 0$.

The paper allows $n \in \mathbb{Z}_p$; only integers $n$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Proposition 4.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_pow_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-pow-five).

## The congruence for $\binom{np}{kp}$ modulo $p^6$

Let $p \ge 11$ be a prime, let $k$ be a
natural number and let $n$ be an integer. For an integer $x$ and a natural number $r$ write
$\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and let $v_p$ be the $p$-adic valuation on
$\mathbb{Q}$. Put $C_{00} = (n-6)(n^2 - nk - 6n + k^2 + 15)/12$,
$C_{21} = (5-n)(4-n)(3-n)/6$, $C_{31} = (n-2)(n-5)(n-4)/6$,
$C_{41} = (2k^2 - 2kn + n^2 - 3n + 4)(5-n)/12$, $C_{42} = (k+1-n)(k-1)(n-5)/12$,
$C_{51} = (n-4)(3k^2 - 3kn + n^2 - 2n + 3)/60$ and $C_{52} = (n-k-1)(k-1)(n-4)/60$, and let

$$
X = \binom{np}{kp} - \binom{n}{k} - \frac{k(n-k)}{2} \binom{n}{k} \Big(C_{00} +
\sum_{j=2}^{5} \sum_{i=1}^{\lfloor j/2 \rfloor} C_{ji} \binom{jp}{ip}\Big).
$$

Then either $X = 0$, or $\binom{n}{6} \ne 0$ and $v_p(X) \ge 6 + v_p\big(\binom{n}{6}\big)$; that
is, $X \equiv 0 \pmod{p^{6+v_p(\binom{n}{6})}}$, and $X = 0$ when $\binom{n}{6} = 0$.

The paper allows $n \in \mathbb{Z}_p$; only integers $n$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Proposition 5.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_pow_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-pow-six).

## The congruence for $\binom{np}{kp}$ modulo $p^7$

Let $p \ge 11$ be a prime, let $k$ be a
natural number and let $n$ be an integer. For an integer $x$ and a natural number $r$ write
$\binom{x}{r} = x(x-1)\cdots(x-r+1)/r!$, and let $v_p$ be the $p$-adic valuation on
$\mathbb{Q}$. Put

$$
C_{00} = -\frac{1}{360} \big(2k^4 - 4k^3 n + 11k^2 n^2 - 9k n^3 + 6n^4 - 105k^2 n + 105k n^2 -
105n^3 + 350k^2 - 350kn + 700n^2 - 2205n + 3248\big),
$$

$C_{21} = (6-n)(5-n)(4-n)(3-n)/24$, $C_{31} = (n-2)(6-n)(5-n)(4-n)/18$,
$C_{41} = (6-n)(5-n)(2k^2 - 2kn + n^2 - 3n + 4)/24$,
$C_{42} = (n-k-1)(k-1)(6-n)(5-n)/24$,
$C_{51} = (4-n)(n-6)(3k^2 - 3kn + n^2 - 2n + 3)/60$,
$C_{52} = (k+1-n)(k-1)(n-4)(n-6)/60$,

$$
C_{61} = \frac{1}{360} \big(2k^4 - 4k^3 n + 6k^2 n^2 - 4k n^3 + n^4 - 30k^2 n + 30k n^2 -
10n^3 + 70k^2 - 70kn + 35n^2 - 50n + 48\big),
$$

$C_{62} = (n-k-1)(k-1)(2k^2 - 2kn + n^2 - 5n + 12)/360$ and
$C_{63} = (n-k-1)(n-k-2)(k-1)(k-2)/360$, and let

$$
X = \binom{np}{kp} - \binom{n}{k} - \frac{k(n-k)}{2} \binom{n}{k} \Big(C_{00} +
\sum_{j=2}^{6} \sum_{i=1}^{\lfloor j/2 \rfloor} C_{ji} \binom{jp}{ip}\Big).
$$

Then either $X = 0$, or $\binom{n}{7} \ne 0$ and $v_p(X) \ge 7 + v_p\big(\binom{n}{7}\big)$; that
is, $X \equiv 0 \pmod{p^{7+v_p(\binom{n}{7})}}$, and $X = 0$ when $\binom{n}{7} = 0$.

Two coefficients differ from the printed paper and follow its Definition 1 and Theorem 4:
$C_{00}$ has the prefactor $-1/360$ (printed $-1/720$), and $C_{63}$ has the factor
$(n-k-1)(n-k-2)$ (printed $(k-n-1)(k-n-2)$). With the printed values the congruence fails
already modulo $p$, for instance at $p = 11$, $n = 7$, $k = 1$. The paper allows
$n \in \mathbb{Z}_p$; only integers $n$ are covered here.

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Proposition 6.

Stated but not proved: `MetaMathlibExt.ringChoose_mul_prime_sub_congr_pow_seven` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#ring-choose-mul-prime-sub-congr-pow-seve).

## $\binom{np}{mp}$ as a quotient of products

Let $p$ be a prime and let $m$ and $n$ be
natural numbers with $1 \le m \le n$. Then

$$\binom{np}{mp} = \frac{\binom{n}{m} \prod_{j=0}^{m-1} \binom{(n-m+j+1)p-1}{p-1}}
{\prod_{j=0}^{m-1} \binom{(j+1)p-1}{p-1}} = \frac{\prod_{j=0}^{m-1} \binom{(n-m+j+1)p}{p}}
{\prod_{j=0}^{m-1} \binom{(j+1)p}{p}}.$$

## Sources

- Walid Kehila, *An Extension of Wolstenholme's Theorem by Binomial Coefficients*, INTEGERS 26 (2026), Article A32, Lemma 6.

Stated but not proved: `MetaMathlibExt.choose_mul_prime_eq_prod_div_prod` is written with `theorem_wanted` in [WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/WolstenholmeBinomialExtensionWanted.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html#choose-mul-prime-eq-prod-div-prod).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Wolstenholme's theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/congruences/congruences-modular-arithmetic/wolstenholme-s-theorem)
