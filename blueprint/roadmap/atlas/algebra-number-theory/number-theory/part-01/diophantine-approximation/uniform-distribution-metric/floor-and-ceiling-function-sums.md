---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.AlternatingFloorSqrtSumWanted.alternating_sum_floor_sqrt_mul, MetaMathlibExt.sum_ceil_add_div_eq_ceil_mul_add, MetaMathlibExt.inclExclLikeSum, MetaMathlibExt.inclExclLikeSum_one, MetaMathlibExt.inclExclLikeSum_two, MetaMathlibExt.tverbergSum, MetaMathlibExt.tverbergSum_zero, MetaMathlibExt.tverbergSum_one
statement: formalized
---

# Floor and ceiling function sums

26 results, 6 proved and 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html).

## An alternating sum of floors of square roots

For every odd positive integer $n$,
$\sum_{j=1}^{n} (-1)^{j+1} \lfloor \sqrt{jn} \rfloor = (n+1)/2$.

## Sources

- Marc Chamberland and Karl Dilcher, "An Alternating Sum of the Floor Function of Square Roots", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.AlternatingFloorSqrtSumWanted.alternating_sum_floor_sqrt_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/AlternatingFloorSqrtSumWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AlternatingFloorSqrtSumWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#alternating-sum-floor-sqrt-mul).

## Ceiling analogue of Hermite's identity

For every real number $x$ and every natural
number $n$, $\sum_{k=1}^{n} \lceil x + k/n \rceil = \lceil n x \rceil + n$.

The paper assumes $n \ge 1$; for $n = 0$ both sides are $0$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 6.

Stated but not proved: `MetaMathlibExt.sum_ceil_add_div_eq_ceil_mul_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#sum-ceil-add-div-eq-ceil-mul-add).

## Inclusion-exclusion-like sum

For a function $F : \mathbb{R} \to \mathbb{Z}$ and real
numbers $x_1, \dots, x_n$, the inclusion-exclusion-like sum is the integer
$g^{(F)}(x_1, \dots, x_n) = \sum_T (-1)^{|T| - 1} F\left(\sum_{i \in T} x_i\right)$, where $T$
ranges over the nonempty subsets of $\{1, \dots, n\}$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Definitions 2 and 3.

Formalized by `MetaMathlibExt.inclExclLikeSum`, a definition declared in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum).

## The inclusion-exclusion-like sum in one variable

For every function
$F : \mathbb{R} \to \mathbb{Z}$ and every real $x$, the inclusion-exclusion-like sum of $F$ in the
single variable $x$ is $g^{(F)}(x) = F(x)$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Definitions 2 and 3.

Formalized by `MetaMathlibExt.inclExclLikeSum_one`, a theorem declared in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-one).

## The inclusion-exclusion-like sum in two variables

For every function
$F : \mathbb{R} \to \mathbb{Z}$ and all real numbers $x$ and $y$,
$g^{(F)}(x, y) = F(x) + F(y) - F(x + y)$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Definitions 2 and 3.

Formalized by `MetaMathlibExt.inclExclLikeSum_two`, a theorem declared in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-two).

## Tverberg's sum

Let $F : \mathbb{R} \to \mathbb{Z}$, let $a = (a_1, \dots, a_\ell)$ be a
tuple of integers, let $m$ be a natural number and let $k$ be an integer. Tverberg's sum is
$f^{(F)}(a, m, k) = \sum_{T \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |T|}
F((k + \sum_{i \in T} a_i) / m)$, where the division is in $\mathbb{R}$ (with $x / 0 = 0$).

The paper takes $F = \lfloor \cdot \rfloor$ in Definition 1, and $F = \lceil \cdot \rceil$,
$x \mapsto \lfloor x + 1/2 \rfloor$ or $x \mapsto \lceil x - 1/2 \rceil$ in Section 1 and
Definition 3.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Definitions 1 and 3.

Formalized by `MetaMathlibExt.tverbergSum`, a definition declared in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum).

## Tverberg's sum of the empty tuple

For every function $F : \mathbb{R} \to \mathbb{Z}$,
every natural number $m$ and every integer $k$, Tverberg's sum of the empty tuple of integers is
$f^{(F)}(\emptyset, m, k) = F(k / m)$, where $k / m$ is division in $\mathbb{R}$ (with $x / 0 = 0$).

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Definitions 1 and 3.

Formalized by `MetaMathlibExt.tverbergSum_zero`, a theorem declared in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-zero).

## Tverberg's sum of a single integer

For every function $F : \mathbb{R} \to \mathbb{Z}$,
all integers $a$ and $k$ and every natural number $m$, Tverberg's sum of $F$ for the one-element
family $(a)$, modulus $m$ and shift $k$ equals $F((k + a)/m) - F(k/m)$, with $x/0 = 0$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Definitions 1 and 3.

Formalized by `MetaMathlibExt.tverbergSum_one`, a theorem declared in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-one).

## Relations and periodicity of the inclusion-exclusion-like sums

Let $n \ge 2$ and write
$g_1$, $g_2$, $g_3$, $g_4$ for the inclusion-exclusion-like sums $g^{(F)}$ with $F$ the floor
function $\lfloor y \rfloor$, the ceiling function $\lceil y \rceil$, the nearest-integer function
$\lfloor y + 1/2 \rfloor$ (ties rounded up) and $\lceil y - 1/2 \rceil$ (ties rounded down),
respectively. For every $x = (x_1, \dots, x_n) \in \mathbb{R}^n$:
(i) $g_3(x) = g_1(x) - g_1(x_1, \dots, x_n, 1/2)$;
(ii) $g_4(x) = g_2(x) - g_2(x_1, \dots, x_n, -1/2)$;
(iii) for each $j \in \{1, 2, 3, 4\}$, each index $i$ and each integer $q$, adding $q$ to $x_i$
does not change $g_j(x)$.

Parts (i) and (ii) also hold for $n < 2$; part (iii) fails for $n = 1$, where
$g_1(x) = \lfloor x \rfloor$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 1.

Stated but not proved: `MetaMathlibExt.inclExclLikeSum_relations_and_periodic` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-relations-and-periodi).

## Tverberg's sum in terms of the inclusion-exclusion-like sum

Let $F$ be one of
$\lfloor \cdot \rfloor$, $\lceil \cdot \rceil$, $r^+(y) = \lfloor y + 1/2 \rfloor$ and
$r^-(y) = \lceil y - 1/2 \rceil$. For real numbers $x_1, \dots, x_n$ let
$g(x_1, \dots, x_n) =
\sum_{\emptyset \ne U \subseteq \{1, \dots, n\}} (-1)^{|U| - 1} F(\sum_{i \in U} x_i)$
be the inclusion-exclusion-like sum of $F$. For every natural number $\ell$, integers
$a_1, \dots, a_\ell$, a natural number $m$ and an integer $k$, let
$f(a, m, k) =
\sum_{U \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |U|} F((k + \sum_{i \in U} a_i)/m)$
be Tverberg's sum of $F$, with $x/0 = 0$. Then
$f(a, m, 0) = (-1)^{\ell+1} g(a_1/m, \dots, a_\ell/m)$ and
$f(a, m, k) = (-1)^{\ell} g(a_1/m, \dots, a_\ell/m, k/m) + (-1)^{\ell+1} g(a_1/m, \dots, a_\ell/m)$.

The paper assumes $\ell \ge 2$ and $m \ge 1$; the identities hold without these hypotheses.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 2.

Stated but not proved: `MetaMathlibExt.tverbergSum_eq_inclExclLikeSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-eq-incl-excl-like-sum).

## Periodicity of Tverberg's sum

Let $\ell \ge 2$ and let $F$ be one of
$\lfloor \cdot \rfloor$, $\lceil \cdot \rceil$, $r^+(y) = \lfloor y + 1/2 \rfloor$ and
$r^-(y) = \lceil y - 1/2 \rceil$.
For integers $a_1, \dots, a_\ell$, a natural number $m$ and an integer $k$, let
$f(a, m, k) =
\sum_{U \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |U|} F((k + \sum_{i \in U} a_i)/m)$
be Tverberg's sum of $F$, with $x/0 = 0$. For every index $i$ and every integer $q$, replacing
$a_i$ by $a_i + q m$ does not change $f(a, m, k)$, and $f(a, m, k + q m) = f(a, m, k)$.

The hypothesis $\ell \ge 2$ is needed: for $\ell = 1$, $F = \lfloor \cdot \rfloor$ and $m \ge 1$,
$f((a), m, k) = \lfloor (k + a)/m \rfloor - \lfloor k/m \rfloor$ increases by $q$ when $a$ is
replaced by $a + q m$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 3.

Stated but not proved: `MetaMathlibExt.tverbergSum_periodic` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-periodic).

## Sharp bounds for Tverberg's floor sum

Let $\ell \ge 2$ and let $F = \lfloor \cdot \rfloor$.
For integers $a_1, \dots, a_\ell$, a natural number $m$ and an integer $k$, let
$f(a, m, k) =
\sum_{U \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |U|} F((k + \sum_{i \in U} a_i)/m)$
be Tverberg's sum of $F$, with $x/0 = 0$. Then $-2^{\ell-2} \le f(a, m, k) \le 2^{\ell-2}$ for
all such $a$, $m$ and $k$. Both bounds are attained: for every integer $r \ge 1$, if $a_i = r$
for all $i$ and $m = 2r$, then $f(a, m, 0) = (-1)^{\ell} 2^{\ell-2}$ and
$f(a, m, r) = (-1)^{\ell+1} 2^{\ell-2}$.

This bound is due to Onphaeng and Pongsriiam. The paper states the equality cases separately for
odd and even $\ell$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 4.

Stated but not proved: `MetaMathlibExt.tverbergSum_floor_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-floor-bounds).

## Extrema of the floor inclusion-exclusion-like sum

Let $n \ge 2$ and let $g_1$ be the
inclusion-exclusion-like sum $g^{(F)}$ in $n$ real variables with $F$ the floor function. Then
$-2^{n-2} \le g_1(x) \le 2^{n-2} - 1$ for every $x \in \mathbb{R}^n$; the minimum $-2^{n-2}$ is
attained at the point with all coordinates $1/2$, and the maximum $2^{n-2} - 1$ at the point with
all coordinates $1/2 - 1/n^2$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 5.

Stated but not proved: `MetaMathlibExt.inclExclLikeSum_floor_extrema` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-floor-extrema).

## Vanishing and periodicity of partial Tverberg sums

Let $\ell \ge 2$, let
$a = (a_1, \dots, a_\ell)$ be integers and let $m$ be a natural number. Let $F$ be one of
$\lfloor \cdot \rfloor$, $\lceil \cdot \rceil$, $r^+(y) = \lfloor y + 1/2 \rfloor$ and
$r^-(y) = \lceil y - 1/2 \rceil$, and for an integer $k$ let
$f^F(a, k) =
\sum_{U \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |U|} F((k + \sum_{i \in U} a_i)/m)$
be Tverberg's sum, with $x/0 = 0$. For natural $K$ put $S^F(a, K) = \sum_{k=0}^{K} f^F(a, k)$
and $T^F(a, K) = \sum_{k=1}^{K} f^F(a, k)$, and for an index $i$ and an integer $p$ let $a'$ be
$a$ with $a_i$ replaced by $a_i + p m$. Then:
(i) $\sum_{k=0}^{m-1} f^F(a, k) = 0$ (an empty sum when $m = 0$);
(ii) $S^F(a, K + q m) = S^F(a, K)$ for all natural $K$ and $q$, and $S^F(a', K) = S^F(a, K)$
for every natural $K$, every index $i$ and every integer $p$;
(iii) if $F$ is $\lceil \cdot \rceil$ or $r^-$, then $T^F(a, m) = 0$,
$T^F(a, K + q m) = T^F(a, K)$ for all natural $K$ and $q$, and $T^F(a', K) = T^F(a, K)$ for
every natural $K$, every index $i$ and every integer $p$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 7.

Stated but not proved: `MetaMathlibExt.tverbergPartialSum_vanish_and_periodic` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-partial-sum-vanish-and-periodic).

## Floor and ceiling of a quotient plus one half

For every integer $q$ and every positive
integer $m$, $\lfloor q/m + 1/2 \rfloor = \lfloor (q + \lfloor m/2 \rfloor)/m \rfloor$ and
$\lceil q/m + 1/2 \rceil = \lceil (q + \lceil m/2 \rceil)/m \rceil$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Lemma 8.

Stated but not proved: `MetaMathlibExt.floor_ceil_div_add_half` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#floor-ceil-div-add-half).

## Extrema of the ceiling inclusion-exclusion-like sum

Let $n \ge 2$ and let $g_2$ be the
inclusion-exclusion-like sum $g^{(F)}$ in $n$ real variables with $F$ the ceiling function. Then
$-2^{n-2} + 1 \le g_2(x) \le 2^{n-2}$ for every $x \in \mathbb{R}^n$; the minimum $-2^{n-2} + 1$
is attained at the point with all coordinates $1/2 + 1/n^2$, and the maximum $2^{n-2}$ at the
point with all coordinates $1/2$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 1.

Stated but not proved: `MetaMathlibExt.inclExclLikeSum_ceil_extrema` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-ceil-extrema).

## Extrema of the round-half-up inclusion-exclusion-like sum

Let $n \ge 2$ and let $g_3$ be
the inclusion-exclusion-like sum $g^{(F)}$ in $n$ real variables with
$F(y) = \lfloor y + 1/2 \rfloor$, the nearest integer to $y$ with ties rounded up. Then
$-2^{n-2} \le g_3(x) \le 2^{n-2}$ for every $x \in \mathbb{R}^n$; the minimum $-2^{n-2}$ is
attained at the point with all coordinates $1/2 - 1/n^2$, and the maximum $2^{n-2}$ at the point
with all coordinates $1/2$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 2.

Stated but not proved: `MetaMathlibExt.inclExclLikeSum_round_extrema` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-round-extrema).

## Extrema of the round-half-down inclusion-exclusion-like sum

Let $n \ge 2$ and let $g_4$
be the inclusion-exclusion-like sum $g^{(F)}$ in $n$ real variables with
$F(y) = \lceil y - 1/2 \rceil$, the nearest integer to $y$ with ties rounded down. Then
$-2^{n-2} \le g_4(x) \le 2^{n-2}$ for every $x \in \mathbb{R}^n$; the minimum $-2^{n-2}$ is
attained at the point with all coordinates $1/2$, and the maximum $2^{n-2}$ at the point with all
coordinates $1/2 + 1/n^2$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 3.

Stated but not proved: `MetaMathlibExt.inclExclLikeSum_roundDown_extrema` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-round-down-extrema).

## Bounds for the four inclusion-exclusion-like sums

Let $n \ge 2$ and write $g_1$, $g_2$,
$g_3$, $g_4$ for the inclusion-exclusion-like sums $g^{(F)}$ in $n$ real variables with $F$ the
floor function $\lfloor y \rfloor$, the ceiling function $\lceil y \rceil$, the nearest-integer
function $\lfloor y + 1/2 \rfloor$ (ties rounded up) and $\lceil y - 1/2 \rceil$ (ties rounded
down), respectively. Then for every $x \in \mathbb{R}^n$,
$-2^{n-2} \le g_1(x) \le 2^{n-2} - 1$, $-2^{n-2} + 1 \le g_2(x) \le 2^{n-2}$,
$-2^{n-2} \le g_3(x) \le 2^{n-2}$ and $-2^{n-2} \le g_4(x) \le 2^{n-2}$. At the point with all
coordinates $1/2$, $g_1 = g_4 = -2^{n-2}$ and $g_2 = g_3 = 2^{n-2}$. At the point with all
coordinates $1/2 - 1/n^2$, $g_1 = 2^{n-2} - 1 = -g_3 - 1$. At the point with all coordinates
$1/2 + 1/n^2$, $g_2 = -2^{n-2} + 1 = -g_4 + 1$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Corollary 1.

Stated but not proved: `MetaMathlibExt.inclExclLikeSum_bounds_summary` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#incl-excl-like-sum-bounds-summary).

## Sharp bounds for Tverberg's ceiling sum

Let $\ell \ge 2$ and let $F = \lceil \cdot \rceil$.
For integers $a_1, \dots, a_\ell$, a natural number $m$ and an integer $k$, let
$f(a, m, k) =
\sum_{U \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |U|} F((k + \sum_{i \in U} a_i)/m)$
be Tverberg's sum of $F$, with $x/0 = 0$. Then $-2^{\ell-2} \le f(a, m, k) \le 2^{\ell-2}$ for
all such $a$, $m$ and $k$. Both bounds are attained: for every integer $r \ge 1$, if $a_i = r$
for all $i$ and $m = 2r$, then $f(a, m, 0) = (-1)^{\ell+1} 2^{\ell-2}$ and
$f(a, m, r) = (-1)^{\ell} 2^{\ell-2}$.

The paper states the equality cases separately for odd and even $\ell$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 4.

Stated but not proved: `MetaMathlibExt.tverbergSum_ceil_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 300](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L300). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-ceil-bounds).

## Sharp bounds for Tverberg's sum with rounding half up

Let $\ell \ge 2$ and let $F$ be
rounding to the nearest integer with ties rounded up, $F(y) = \lfloor y + 1/2 \rfloor$.
For integers $a_1, \dots, a_\ell$, a natural number $m$ and an integer $k$, let
$f(a, m, k) =
\sum_{U \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |U|} F((k + \sum_{i \in U} a_i)/m)$
be Tverberg's sum of $F$, with $x/0 = 0$. Then $-2^{\ell-2} \le f(a, m, k) \le 2^{\ell-2}$ for
all such $a$, $m$ and $k$. Both bounds are attained: for every integer $r \ge 1$, if $a_i = r$
for all $i$ and $m = 2r$, then $f(a, m, 0) = (-1)^{\ell+1} 2^{\ell-2}$ and
$f(a, m, r) = (-1)^{\ell} 2^{\ell-2}$.

The paper states the equality cases separately for odd and even $\ell$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 5.

Stated but not proved: `MetaMathlibExt.tverbergSum_round_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-round-bounds).

## Sharp bounds for Tverberg's sum with rounding half down

Let $\ell \ge 2$ and let $F$ be
rounding to the nearest integer with ties rounded down, $F(y) = \lceil y - 1/2 \rceil$.
For integers $a_1, \dots, a_\ell$, a natural number $m$ and an integer $k$, let
$f(a, m, k) =
\sum_{U \subseteq \{1, \dots, \ell\}} (-1)^{\ell - |U|} F((k + \sum_{i \in U} a_i)/m)$
be Tverberg's sum of $F$, with $x/0 = 0$. Then $-2^{\ell-2} \le f(a, m, k) \le 2^{\ell-2}$ for
all such $a$, $m$ and $k$. Both bounds are attained: for every integer $r \ge 1$, if $a_i = r$
for all $i$ and $m = 2r$, then $f(a, m, 0) = (-1)^{\ell} 2^{\ell-2}$ and
$f(a, m, r) = (-1)^{\ell+1} 2^{\ell-2}$.

The paper states the equality cases separately for odd and even $\ell$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 6.

Stated but not proved: `MetaMathlibExt.tverbergSum_roundDown_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-sum-round-down-bounds).

## Sharp bounds for two-term tail sums of Tverberg's ceiling sum

For integers $a, b$ and
natural numbers $m, K$, let
$T(a, b, m, K) = \sum_{k=1}^{K} f^{(\lceil \cdot \rceil)}((a, b), m, k)$, where
$f^{(\lceil \cdot \rceil)}$ is Tverberg's sum with $F$ the ceiling function. Then
$0 \le T(a, b, m, K) \le \lfloor m/2 \rfloor$ for all such $a, b, m, K$. Moreover, for every
natural number $r$, $T(r, r, 2r, 2r) = 0$ and $T(r, r, 2r, r) = r$.

The paper assumes $m, K \ge 1$; for $m = 0$ or $K = 0$ the sum is $0$, so these hypotheses are
not needed.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 7.

Stated but not proved: `MetaMathlibExt.tverbergTailSum_ceil_two_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-tail-sum-ceil-two-bounds).

## Bounds for tail sums of Tverberg's ceiling sum

Let $\ell \ge 2$. For a tuple
$a = (a_1, \dots, a_\ell)$ of integers and natural numbers $m, K$, let
$T(a, m, K) = \sum_{k=1}^{K} f^{(\lceil \cdot \rceil)}(a, m, k)$, where $f^{(\lceil \cdot \rceil)}$
is Tverberg's sum with $F$ the ceiling function. Then
$-2^{\ell-2} \lfloor m/2 \rfloor \le T(a, m, K) \le 2^{\ell-2} \lfloor m/2 \rfloor$ for all such
$a, m, K$. Moreover, for every natural number $r$, if $a_i = r$ for every $i$, then
$T(a, 2r, r) = (-1)^\ell \, 2^{\ell-2} \, r$.

Theorem 8 as recorded asserts this equality for every $K$, which is false: for $\ell = 3$, $m = 2$,
$a_i = 1$ and $K = 2$ the sum is $0$, not $-2$. The paper's proof establishes it at $K = m/2$,
which is what is stated here.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 8.

Stated but not proved: `MetaMathlibExt.tverbergTailSum_ceil_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-tail-sum-ceil-bounds).

## Bounds for partial Tverberg sums of two integers under rounding half up

Let
$r^+(y) = \lfloor y + 1/2 \rfloor$ be rounding to the nearest integer with ties rounded up. For
integers $a, b, k$ and a natural number $m$, let
$f(a, b; m, k) = r^+(k/m) - r^+((k + a)/m) - r^+((k + b)/m) + r^+((k + a + b)/m)$ be
Tverberg's sum of $r^+$ at $(a, b)$, with $x/0 = 0$. For all integers $a, b$ and natural
numbers $m, K$,
$-\lfloor m/2 \rfloor \le \sum_{k=0}^{K} f(a, b; m, k) \le \lfloor m/2 \rfloor$. The lower bound
is attained: for every natural number $r$,
$\sum_{k=0}^{r} f(r + 1, r + 1; 2(r + 1), k) = -(r + 1)$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 9.

Stated but not proved: `MetaMathlibExt.tverbergPartialSum_round_two_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-partial-sum-round-two-bounds).

## Bounds for two-term tail sums of Tverberg's sum with half-down rounding

Let
$r^-(x) = \lceil x - 1/2 \rceil$. For integers $a, b$ and natural numbers $m, K$, let
$T(a, b, m, K) = \sum_{k=1}^{K} f^{(r^-)}((a, b), m, k)$, where $f^{(r^-)}$ is Tverberg's sum
with $F = r^-$. Then $-\lfloor m/2 \rfloor \le T(a, b, m, K) \le \lfloor m/2 \rfloor$ for all
such $a, b, m, K$, and the lower bound is attained: for every natural number $r$,
$T(r, r, 2r, r) = -r$.

The paper assumes $m, K \ge 1$ and states attainment as an existence claim; here it is stated
through the witness of the paper's proof, and the claims hold trivially at $m = 0$ or $K = 0$.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Prapanpong Pongsriiam, *Inequalities for Inclusion-Exclusion-Like Sums Involving the Ceiling and the Nearest Integer Functions*, INTEGERS 25 (2025), Article A45, Theorem 10.

Stated but not proved: `MetaMathlibExt.tverbergTailSum_roundDown_two_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CeilingHermiteIdentityWanted.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html#tverberg-tail-sum-round-down-two-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Floor and ceiling function sums](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/floor-and-ceiling-function-sums)
