---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum, MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.arrayR, MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.arrayU, MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.faulhaberB, MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.faulhaberC, MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.thmQ, MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.pow_mul_powerSum_even_eq_sum, MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum_even_div_iff_odd
statement: formalized
---

# Faulhaber coefficients and sums of powers

18 results, 6 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html).

## Power sums

For natural numbers $k$ and $n$, the power sum $S_k(n)$ is the rational
number $\sum_{i=1}^{n} i^k = 1^k + 2^k + \cdots + n^k$, which is $0$ when $n = 0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#power-sum).

## The array $R(k, m)$

For natural numbers $k$ and $m$, $R(k, m)$ is the integer
$\sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.arrayR`, a definition declared in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#array-r).

## The array $U(k, m)$

For natural numbers $k$ and $m$, $U(k, m)$ is the rational number
$\frac{2}{(2m)!} \sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.arrayU`, a definition declared in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#array-u).

## The Faulhaber coefficients $b_{k,r}$

For natural numbers $p$ and $q$, let
$R(p, q) = \sum_{j=0}^{q} (-1)^j \binom{2q}{j} (q - j)^{2p}$, and for natural numbers $q$
and $s$ let $\mathrm{Ps}_q^{(s)}$ be the Legendre–Stirling number of the first kind, the
coefficient of $x^s$ in $\prod_{i=0}^{q-1} (x - i(i+1))$. For natural numbers $k$ and $r$,
$b_{k,r}$ is the rational number
$\sum_{m=r}^{k} \frac{3 \cdot 2^r}{(2m+1)!}\, R(k, m)\, \mathrm{Ps}_m^{(r)}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.faulhaberB`, a definition declared in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#faulhaber-b).

## The Faulhaber coefficients $c_{k,r}$

For natural numbers $p$ and $q$, let
$R(p, q) = \sum_{j=0}^{q} (-1)^j \binom{2q}{j} (q - j)^{2p}$, and for natural numbers $q$
and $s$ let $\mathrm{Ps}_q^{(s)}$ be the Legendre–Stirling number of the first kind, the
coefficient of $x^s$ in $\prod_{i=0}^{q-1} (x - i(i+1))$. For natural numbers $k$ and $r$,
$c_{k,r}$ is the rational number
$\sum_{m=r}^{k} \frac{2^{r+1}}{(2m+2)!\,(m+1)}\, R(k+1, m+1)\, \mathrm{Ps}_{m+1}^{(r+1)}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.faulhaberC`, a definition declared in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#faulhaber-c).

## The polynomials $Q_{k,m}$ of Theorem 10

For natural numbers $k$, $m$ and $n$, write
$R(a, b) = \sum_{i=0}^{b} (-1)^i \binom{2b}{i} (b - i)^{2a}$ for the array of OEIS A304330.
The rational number $Q_{k,m}(n)$ is $n^{2k-1}$ if $m = 1$, and otherwise

$$Q_{k,m}(n) = 2 \sum_{j=m}^{k} \binom{2k-1}{2j-2} R(j-1, m-1) \, n^{2k-2j+1}.$$

Differences of natural numbers such as $2k - 1$ and $m - 1$ are truncated at $0$.

Formalized by `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.thmQ`, a definition declared in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#thm-q).

## Even power sums in terms of $\binom{2n+m+1}{2m+1}$

For natural numbers $k \ge 1$ and
$n$, write $S_{2k}(n) = 1^{2k} + 2^{2k} + \dots + n^{2k}$ and
$R(k, m) = \sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$. Then
$2^{2k} S_{2k}(n) = \sum_{m=1}^{k} R(k, m) \binom{2n+m+1}{2m+1}$.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.pow_mul_powerSum_even_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#pow-mul-power-sum-even-eq-sum).

## Knuth's correspondence between even and odd power sums

Let $k \ge 1$ be a natural
number, let $(a_m)_{m \ge 0}$ be a sequence of real numbers, and write
$S_j(n) = 1^j + 2^j + \dots + n^j$. Then
$\frac{S_{2k}(n)}{2n+1} = \sum_{m=1}^{k} a_m \binom{n+m}{2m}$ for every natural number $n$
if and only if $S_{2k-1}(n) = \sum_{m=1}^{k} \frac{2m+1}{m}\, a_m \binom{n+m}{2m}$ for every
natural number $n$.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Proposition 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum_even_div_iff_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#power-sum-even-div-iff-odd).

## Knuth's formula for even power sums

For natural numbers $k \ge 1$ and $n$, write
$S_{2k}(n) = 1^{2k} + 2^{2k} + \dots + n^{2k}$ and
$R(k, m) = \sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$. Then
$S_{2k}(n) = \sum_{m=1}^{k} R(k, m)\, \frac{2n+1}{2m+1} \binom{n+m}{2m}$.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Proposition 3.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum_even_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#power-sum-even-eq-sum).

## Knuth's binomial formula for the odd power sums

For all natural numbers $k \ge 1$ and
$n$, the power sum $S_{2k-1}(n) = 1^{2k-1} + 2^{2k-1} + \cdots + n^{2k-1}$ satisfies

$$S_{2k-1}(n) = \sum_{m=1}^{k} R(k, m) \cdot \frac{1}{m} \binom{n + m}{2m},$$

where $R(k, m) = \sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$ is the array of OEIS A304330.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Proposition 3.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum_odd_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#power-sum-odd-eq-sum).

## Sum of $2i \binom{2i+k-1}{2k-1}$

For all natural numbers $k \ge 1$ and $n \ge 1$,

$$\sum_{i=1}^{n} 2i \binom{2i + k - 1}{2k - 1} = k \binom{2n + k + 1}{2k + 1}.$$

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Lemma 4.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.sum_two_mul_choose_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#sum-two-mul-choose-eq).

## Inversion formula for the arrays $u(k, m)$ and $U(k, m)$ (Butzer et al.)

For natural
numbers $k$ and $m$, let $u(k, m)$ be the first-kind Jacobi–Stirling number $J(k, m; 0)$, the
coefficient of $x^m$ in $\prod_{i=0}^{k-1} (x - i^2)$, and let
$U(k, m) = \frac{2}{(2m)!} \sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$. For all sequences
$(a_k)_{k \ge 0}$ and $(b_k)_{k \ge 0}$ of real numbers, $a_k = \sum_{m=1}^{k} u(k, m)\, b_m$
holds for every $k \ge 1$ if and only if $b_k = \sum_{m=1}^{k} U(k, m)\, a_m$ holds for every
$k \ge 1$.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Lemma 5.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.inversion_uU` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#inversion-u-u).

## Closed form for the array $R(k, m)$

Let $k$ and $m$ be natural numbers with
$1 \le m \le k$, and let $R(k, m) = \sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$. Then

$$R(k, m) = 2^{2k+m-1}\, m! \sum_{b} \frac{(2k)!}{b_1! \cdots b_k!}
\prod_{r=1}^{k} \left(\frac{1}{4^r (2r)!}\right)^{b_r},$$

where the sum runs over all $k$-tuples $b = (b_1, \dots, b_k)$ of natural numbers with
$b_1 + 2 b_2 + \dots + k b_k = k$ and $b_1 + \dots + b_k = m$ (each such $b_r$ is at most $k$).

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Corollary 6.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.arrayR_eq_closedForm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#array-r-eq-closed-form).

## Sum of $i \binom{i+k-1}{2k-1}$

For all natural numbers $k \ge 1$ and $n \ge 1$,

$$\sum_{i=1}^{n} i \binom{i + k - 1}{2k - 1} = \frac{k(2n + 1)}{2k + 1} \binom{n + k}{2k}.$$

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Lemma 7.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.sum_mul_choose_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#sum-mul-choose-eq).

## Odd power sums in terms of $\binom{n+m}{2m-1}$

For natural numbers $k \ge 1$ and $n$,
write $S_{2k-1}(n) = 1^{2k-1} + 2^{2k-1} + \dots + n^{2k-1}$, let
$R(p, q) = \sum_{j=0}^{q} (-1)^j \binom{2q}{j} (q - j)^{2p}$, and let $Q_{k,1}(n) = n^{2k-1}$ and
$Q_{k,m}(n) = 2 \sum_{j=m}^{k} \binom{2k-1}{2j-2} R(j-1, m-1)\, n^{2k-2j+1}$ for $m \ge 2$. Then
$2^{2k-1} S_{2k-1}(n) = \sum_{m=1}^{k} Q_{k,m}(n) \binom{n+m}{2m-1}$.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Theorem 10.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.pow_mul_powerSum_odd_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#pow-mul-power-sum-odd-eq-sum).

## Faulhaber form of the even power sums

For all natural numbers $k \ge 1$ and $n$,
writing $S_j(n) = 1^j + 2^j + \cdots + n^j$ for the power sums and $b_{k,r}$ for the Faulhaber
coefficients of Proposition 12, the rational numbers satisfy
$S_{2k}(n) = S_2(n) \sum_{r=1}^{k} b_{k,r} \, S_1(n)^{r-1}$.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Proposition 12.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum_even_faulhaber` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#power-sum-even-faulhaber).

## Faulhaber form of the odd power sums

For all natural numbers $k \ge 1$ and $n$,
writing $S_j(n) = 1^j + 2^j + \cdots + n^j$ for the power sums and $c_{k,r}$ for the Faulhaber
coefficients of Proposition 12, the rational numbers satisfy
$S_{2k+1}(n) = S_1(n)^2 \sum_{r=1}^{k} c_{k,r} \, S_1(n)^{r-1}$.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Proposition 12.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.powerSum_odd_faulhaber` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#power-sum-odd-faulhaber).

## Vanishing alternating sum of the A304330 array

For every natural number $k \ge 2$,

$$\sum_{m=1}^{k} (-1)^m \frac{((m-1)!)^2}{(2m)!} R(k, m) = 0,$$

where $R(k, m) = \sum_{j=0}^{m} (-1)^j \binom{2m}{j} (m - j)^{2k}$ is the array of OEIS A304330.

## Sources

- José L. Cereceda, "Sums of Powers of Integers and the Sequence A304330", Proposition 15.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.SumsOfPowersA304330Wanted.sum_neg_factorial_sq_div_arrayR_eq_zero` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/SumsOfPowersA304330Wanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html#sum-neg-factorial-sq-div-array-r-eq-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Faulhaber coefficients and sums of powers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/faulhaber-coefficients-and-sums-of-powers)
