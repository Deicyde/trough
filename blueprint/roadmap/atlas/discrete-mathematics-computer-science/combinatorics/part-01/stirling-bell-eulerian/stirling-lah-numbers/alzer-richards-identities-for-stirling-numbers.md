---
declaration: section
origin: cited
lean: MetaMathlibExt.sum_iteratedDeriv_pow_one_sub, MetaMathlibExt.sum_iteratedDeriv_zpow_one_add, MetaMathlibExt.sum_choose_div_choose_mul_stirlingSecond_eq_bernoulli, MetaMathlibExt.sum_choose_div_choose_mul_stirlingSecond_eq_zero, MetaMathlibExt.sum_choose_add_two_div_choose_mul_stirlingSecond, MetaMathlibExt.sum_choose_div_choose_mul_signedStirlingFirst, MetaMathlibExt.sum_eulerNumber_mul_sum_centralPowerSum, MetaMathlibExt.sum_fubiniNumber_mul_sum_alternatingStirling
statement: formalized
---

# Alzer–Richards identities for Stirling numbers

18 results, 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html).

## Alzer–Richards derivative identity for powers of $1 - f$

Let $r, j, n \ge 0$ be
integers and let $f \colon \mathbb{R} \to \mathbb{R}$ be $r$ times continuously differentiable.
Writing $g^{(i)}$ for the $i$-th derivative of a function $g$ and taking powers of $f$ pointwise,
for every real $x$

$$
\sum_{k=0}^{n} (-1)^{k+1} \binom{n+1}{k+1} \bigl(f^{k+1+j}\bigr)^{(r)}(x) =
\sum_{k=0}^{r} \binom{r}{k} \bigl(f^j\bigr)^{(k)}(x) \,
\bigl((1-f)^{n+1} - 1\bigr)^{(r-k)}(x).
$$

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 1, Equation (2).

Stated but not proved: `MetaMathlibExt.sum_iteratedDeriv_pow_one_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-iterated-deriv-pow-one-sub).

## Alzer–Richards derivative identity for powers of $1 + f$

Let $r, j, n \ge 0$ be
integers and let $f \colon \mathbb{R} \to \mathbb{R}$ be $r$ times continuously differentiable
with $f(y) \ne 0$ for every real $y$. Writing $g^{(i)}$ for the $i$-th derivative of a function
$g$ and taking integer powers of $f$ pointwise, for every real $x$

$$
\sum_{k=0}^{n} \binom{n+1}{k+1} \bigl(f^{k+1-j}\bigr)^{(r)}(x) =
\sum_{k=0}^{r} \binom{r}{k} \bigl(1/f^j\bigr)^{(k)}(x) \,
\bigl((1+f)^{n+1} - 1\bigr)^{(r-k)}(x).
$$

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 1, Equation (3).

Stated but not proved: `MetaMathlibExt.sum_iteratedDeriv_zpow_one_add` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-iterated-deriv-zpow-one-add).

## Alternating Stirling sums with $\binom{n+1}{k+1}$ give Bernoulli numbers

Write $S(n, k)$
for the Stirling numbers of the second kind and $B_n$ for the Bernoulli numbers, with
$B_1 = -1/2$. Let $n$ be a natural number. Then for every natural number $r \le n$,

$$
\sum_{k=0}^{n} (-1)^k \frac{\binom{n+1}{k+1}}{\binom{r+k}{k}} S(r+k, k) = B_r,
$$

and

$$
\sum_{k=0}^{n} (-1)^k \frac{\binom{n+1}{k+1}}{\binom{n+1+k}{k}} S(n+1+k, k) =
B_{n+1} - (-1/2)^{n+1} (n+1)!.
$$

The case $r = n$ is Muthumalai's formula.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 2, Equation (4).

Stated but not proved: `MetaMathlibExt.sum_choose_div_choose_mul_stirlingSecond_eq_bernoulli` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-div-choose-mul-stirling-secon).

## Vanishing alternating Stirling sums with $\binom{r+m}{k}$

Write $S(n, k)$ for the
Stirling numbers of the second kind. For every natural number $m \ge 1$ and every natural number
$r$,

$$
\sum_{k=0}^{r+m} (-1)^k \frac{\binom{r+m}{k}}{\binom{r+k}{k}} S(r+k, k) = 0.
$$

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 3, Equation (5).

Stated but not proved: `MetaMathlibExt.sum_choose_div_choose_mul_stirlingSecond_eq_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-div-choose-mul-stirling-secon-2).

## Alternating Stirling sums with $\binom{n+1}{k+2}$

Write $S(n, k)$ for the Stirling
numbers of the second kind and $B_n$ for the Bernoulli numbers, with $B_1 = -1/2$. Let
$n \ge 1$ be a natural number. Then for every natural number $r$ with $1 \le r \le n$,

$$
\sum_{k=0}^{n-1} (-1)^k \frac{\binom{n+1}{k+2}}{\binom{r+k}{k}} S(r+k, k) =
r B_{r-1} + (n + r) B_r,
$$

and

$$
\sum_{k=0}^{n-1} (-1)^k \frac{\binom{n+1}{k+2}}{\binom{n+1+k}{k}} S(n+1+k, k) =
(-1/2)^{n+1} (n+1)! + (n+1) B_n + (2n+1) B_{n+1}.
$$

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 4, Equation (6).

Stated but not proved: `MetaMathlibExt.sum_choose_add_two_div_choose_mul_stirlingSecond` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-add-two-div-choose-mul-stirli).

## Alternating sums of signed Stirling numbers of the first kind

Write $s(n, k)$ for the
signed Stirling numbers of the first kind. For all natural numbers $j$ and $n$ and every natural
number $r \le n$,

$$
\sum_{k=0}^{n+1} (-1)^k \frac{\binom{n+1}{k}}{\binom{k+j+r}{r}} s(k+j+r, k+j) = 0,
$$

and

$$
\sum_{k=0}^{n+1} (-1)^k \frac{\binom{n+1}{k}}{\binom{k+j+n+1}{n+1}} s(k+j+n+1, k+j) =
\frac{(n+1)!}{2^{n+1}}.
$$

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 5, Equation (7).

Stated but not proved: `MetaMathlibExt.sum_choose_div_choose_mul_signedStirlingFirst` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-div-choose-mul-signed-stirlin).

## Alzer–Richards identity for Euler numbers

Let $n \ge 1$ be an integer. For integers
$k, i \ge 0$ let $T(k, i) = 2^{-k} \sum_{j=0}^{k} \binom{k}{j} (k-2j)^i$ (with $0^0 = 1$), and
let $E_k$ be the Euler numbers: $E_k = 0$ for odd $k$, and for even $k$ they are given by
$E_0 = 1$ and $E_{2m} = -\sum_{s=0}^{m-1} \binom{2m}{2s} E_{2s}$ for $m \ge 1$. Then

$$
\sum_{k=0}^{n-1} \binom{n}{k} E_k \sum_{\nu=0}^{n+1} \binom{n+1}{\nu} T(\nu, n-k) +
(2^{n+1} - 1) E_n = \sum_{k=0}^{n} \binom{n+1}{k+1} T(k, n).
$$

With these conventions $1/\cosh x = \sum_{k \ge 0} E_k x^k / k!$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 6.

Stated but not proved: `MetaMathlibExt.sum_eulerNumber_mul_sum_centralPowerSum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-euler-number-mul-sum-central-power-s).

## Alzer–Richards identity for Fubini numbers

Let $n \ge 1$ be an integer, let $a(k)$ be
the $k$-th Fubini (ordered Bell) number and $S(r, j)$ the Stirling numbers of the second kind,
and for integers $r, k \ge 0$ let
$A(r, k) = \sum_{j=0}^{k} (-1)^j \binom{k}{j} j! \, S(r, j)$. Then

$$
\sum_{k=0}^{n-1} \binom{n}{k} a(k) \sum_{\nu=0}^{n+1} \binom{n+1}{\nu} A(n-k, \nu) +
(2^{n+1} - 1) a(n) = \sum_{k=0}^{n} \binom{n+1}{k+1} A(n, k).
$$

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 7, Equation (8).

Stated but not proved: `MetaMathlibExt.sum_fubiniNumber_mul_sum_alternatingStirling` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-fubini-number-mul-sum-alternating-st).

## Sabar's identity for complex arguments

For a complex number $w$ and a natural number $j$
write $\binom{w}{j} = w(w-1)\cdots(w-j+1)/j!$. For every natural number $p \ge 1$ and every
complex number $z$,

$$
z^p - z(z-1)\cdots(z-p+1) =
\sum_{k=0}^{p-1} (-1)^{p-k-1} k^p \binom{z}{k} \binom{z-k-1}{p-k-1}.
$$

Sabar proved this formula for natural numbers $z = n \ge p$; here it is extended to complex $z$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 8, Equation (9).

Stated but not proved: `MetaMathlibExt.pow_sub_descPochhammer_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#pow-sub-desc-pochhammer-eq-sum-choose).

## A reciprocal-sum identity for generalized binomial coefficients

For a complex number $w$
and a natural number $j$ write $\binom{w}{j} = w(w-1)\cdots(w-j+1)/j!$. Let $p \ge 1$ be a
natural number and let $z$ be a complex number with $z \ne k$ for every natural number $k < p$.
Then

$$
p z^{p-1} - z^p \sum_{k=0}^{p-1} \frac{1}{z-k} =
\sum_{k=0}^{p-1} \frac{(-1)^{p-k} k^p}{z-k} \binom{z}{k} \binom{z-k-1}{p-k-1}.
$$

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Corollary 1, Equation (10).

Stated but not proved: `MetaMathlibExt.mul_pow_pred_sub_pow_mul_sum_inv_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#mul-pow-pred-sub-pow-mul-sum-inv-eq-sum).

## The Alzer–Richards binomial sum as a ${}_3F_2$ series

Let $m \ge 1$ be an integer and
let $p, x$ be complex numbers with $p \ne -j$ and $x \ne -j$ for every integer $j$ with
$1 \le j \le \lfloor m/2 \rfloor$. Write $\binom{z}{k} = z(z-1)\cdots(z-k+1)/k!$ for complex $z$
and $(z)_n = z(z+1)\cdots(z+n-1)$ for the rising factorial. Then

$$
\sum_{k=0}^{\lfloor m/2 \rfloor} \frac{\binom{m-k}{k} \binom{m+x}{m-k}}{2^{2k} \binom{k+p}{k}} =
\frac{(x+1)_m}{m!} \sum_{n=0}^{\lfloor m/2 \rfloor}
\frac{(-m/2)_n \, ((1-m)/2)_n}{(p+1)_n \, (x+1)_n}.
$$

The sum on the right is the terminating hypergeometric series
${}_3F_2(-m/2, (1-m)/2, 1; p+1, x+1; 1)$, written out up to $n = \lfloor m/2 \rfloor$, beyond
which its terms vanish.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 9 (i), Equation (15).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_choose_div_choose_eq_hypergeometric3F2` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-mul-choose-div-choose-eq-hype).

## A binomial sum as a terminating ${}_2F_1$ series

Write
$x^{\overline{n}} = x(x+1)\cdots(x+n-1)$ for the rising factorial of a complex number $x$, and
$\binom{w}{k} = w(w-1)\cdots(w-k+1)/k!$ for a complex number $w$ and a natural number $k$. Let
$m$ and $\nu$ be natural numbers with $1 \le \nu \le \lfloor m/2 \rfloor$, and let $p$ be a
complex number with $p \ne -j$ for every natural number $j$ with $1 \le j \le \lfloor m/2 \rfloor$.
Then

$$
\sum_{k=0}^{\lfloor m/2 \rfloor} \frac{\binom{m-k}{k} \binom{m-\nu}{m-k}}{2^{2k} \binom{k+p}{k}} =
\frac{(m-\nu)!}{2^{2\nu} \, m!} \cdot \frac{(-m)^{\overline{2\nu}}}{(p+1)^{\overline{\nu}}}
\sum_{n=0}^{\lfloor m/2 \rfloor - \nu}
\frac{(\nu - m/2)^{\overline{n}} \, (\nu - (m-1)/2)^{\overline{n}}}
{(\nu + p + 1)^{\overline{n}} \, n!}.
$$

The last sum is the terminating hypergeometric series
${}_2F_1(\nu - m/2, \nu - (m-1)/2; \nu + p + 1; 1)$, whose terms vanish beyond
$n = \lfloor m/2 \rfloor - \nu$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Theorem 9 (ii), Equation (16).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_choose_div_choose_eq_hypergeometric2F1` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-mul-choose-div-choose-eq-hype-2).

## Closed form of the Alzer–Richards binomial sum for even $m$

Let $m \ge 2$ be an even
integer and $x$ a complex number, and write $\binom{z}{k} = z(z-1)\cdots(z-k+1)/k!$ for complex
$z$. Put

$$
S(x) = \sum_{k=0}^{m/2} \frac{\binom{m-k}{k} \binom{m+x}{m-k}}{2^{2k} \binom{k-m/2-1/2}{k}}.
$$

If $x \ne -m/2$, then $S(x) = \frac{x}{x+m/2} \binom{x+m}{m}$; if $x = -m/2$, then
$S(x) = \frac{(-1)^{m/2}}{2^m \binom{(m-1)/2}{m/2}}$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Corollary 2 (i), Equation (19).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_choose_div_choose_of_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-mul-choose-div-choose-of-even).

## Closed form of the Alzer–Richards binomial sum for odd $m$

Let $m$ be an odd positive
integer and $x$ a complex number, and write $\binom{z}{k} = z(z-1)\cdots(z-k+1)/k!$ for complex
$z$. Put

$$
S(x) = \sum_{k=0}^{(m-1)/2} \frac{\binom{m-k}{k} \binom{m+x}{m-k}}{2^{2k} \binom{k-m/2-1}{k}}.
$$

If $x \ne (1-m)/2$, then $S(x) = \frac{x}{x+(m-1)/2} \binom{x+m}{m}$; if $x = (1-m)/2$, then
$S(x) = \frac{(-1)^{(m-1)/2} (m+1)}{2^m \binom{m/2}{(m-1)/2}}$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Corollary 2 (ii), Equation (20).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_choose_div_choose_of_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-mul-choose-div-choose-of-odd).

## Closed form of the shifted Alzer–Richards binomial sum

Let $m \ge 1$ be an integer and
$x$ a complex number, write $\binom{z}{k} = z(z-1)\cdots(z-k+1)/k!$ for complex $z$, and assume
$\binom{k-m+1/2-x}{k} \ne 0$ for $0 \le k \le \lfloor m/2 \rfloor$. Put

$$
S(x) = \sum_{k=0}^{\lfloor m/2 \rfloor}
\frac{\binom{m-k}{k} \binom{m+x}{m-k}}{2^{2k} \binom{k-m+1/2-x}{k}}.
$$

If $x \ne -m/2$ and $x \ne (1-m)/2$, then
$S(x) = \frac{x (x+m-1/2)}{(x+m/2)(x+(m-1)/2)} \binom{x+m}{m}$. If $m$ is even and
$x = -m/2$, then $S(x) = \frac{(-1)^{m/2}}{2^m \binom{(m-3)/2}{m/2}}$. If $m$ is odd and
$x = (1-m)/2$, then $S(x) = \frac{(-1)^{(m-1)/2} (m+1)}{2^m \binom{m/2-1}{(m-1)/2}}$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Corollary 2 (iii), Equation (21).

Stated but not proved: `MetaMathlibExt.sum_choose_mul_choose_div_choose_shifted` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#sum-choose-mul-choose-div-choose-shifted).

## Derivatives at zero of powers of $(1 - e^x)/x$

Write $S(n, k)$ for the Stirling numbers
of the second kind. Let $f : \mathbb{R} \to \mathbb{R}$ satisfy $f(0) = -1$ and
$f(x) = (1 - e^x)/x$ for every $x \ne 0$. Then for all natural numbers $k$ and $r$, the $r$-th
derivative of $f^k$ at $0$ equals $(-1)^k S(r+k, k) / \binom{r+k}{k}$.

This is the expansion recorded in Gradshteyn and Ryzhik, p. 1047.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Lemma 1.

Stated but not proved: `MetaMathlibExt.iteratedDeriv_pow_one_sub_exp_div_self_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 276](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L276). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#iterated-deriv-pow-one-sub-exp-div-self).

## Derivatives of $x/(1 - e^x)$ at zero

Write $B_k$ for the $k$-th Bernoulli number,
with the convention $B_1 = -1/2$. Let $f : \mathbb{R} \to \mathbb{R}$ satisfy $f(0) = -1$ and
$f(x) = (1 - e^x)/x$ for every $x \ne 0$. Then for every natural number $k$, the $k$-th
derivative of $1/f$ at $0$ equals $-B_k$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Lemma 2.

Stated but not proved: `MetaMathlibExt.iteratedDeriv_inv_one_sub_exp_div_self_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#iterated-deriv-inv-one-sub-exp-div-self).

## Derivatives at zero of $(1 + (1 - e^x)/x)^{n+1}$

Let $f : \mathbb{R} \to \mathbb{R}$
satisfy $f(0) = -1$ and $f(x) = (1 - e^x)/x$ for every $x \ne 0$, and let $n$ be a natural
number. Then for every natural number $r \le n$, the $r$-th derivative of $(1 + f)^{n+1}$ at $0$
is $0$, and the $(n+1)$-th derivative of $(1 + f)^{n+1}$ at $0$ equals $(-1/2)^{n+1} (n+1)!$.

## Sources

- Horst Alzer and Kendall C. Richards, *Extensions of Some Combinatorial Identities and Various Related Results*, INTEGERS 25 (2025), Article A61, Lemma 3, Equation (26).

Stated but not proved: `MetaMathlibExt.iteratedDeriv_one_add_one_sub_exp_div_self_pow_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/AlzerRichardsIdentitiesWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html#iterated-deriv-one-add-one-sub-exp-div-s).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alzer–Richards identities for Stirling numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/stirling-lah-numbers/alzer-richards-identities-for-stirling-numbers)
