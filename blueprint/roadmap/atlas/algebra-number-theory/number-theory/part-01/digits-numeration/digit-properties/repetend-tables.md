---
declaration: section
origin: cited
lean: MetaMathlibExt.digit_add_mul_modulus_eq, MetaMathlibExt.totient_dvd_card_orderOf_eq, MetaMathlibExt.card_orderOf_eq_totient_classification, MetaMathlibExt.card_orderOf_eq_two_eq_two_pow_sub_one, MetaMathlibExt.orderOf_eq_six_ne_small_residues, MetaMathlibExt.sign_balance_shifted_linear_residues, MetaMathlibExt.repetend_block_sum_eq, MetaMathlibExt.long_division_remainder_expansion
statement: formalized
---

# Repetend tables

41 results, 41 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html).

## Raising the base by multiples of $n$ shifts repetend digits linearly

Let $m$ and $j$ be
natural numbers, $n \ge 1$ and $b \ge 2$. For a base $B$ write
$d_j(B) = \lfloor m B^{j+1} / n \rfloor \bmod B$ for the $j$-th base-$B$ digit of $m/n$. Then
there is a natural number $c < n$ such that $d_j(b + tn) = d_j(b) + tc$ for every natural number
$t$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Corollary 3.

Stated but not proved: `MetaMathlibExt.digit_add_mul_modulus_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#digit-add-mul-modulus-eq).

## The number of units of order $L$ is a multiple of $\varphi(L)$

For natural numbers
$n \ge 1$ and $L$, the number $E(L, n)$ of elements of order $L$ in the unit group
$(\mathbb{Z}/n\mathbb{Z})^\times$ is divisible by Euler's totient $\varphi(L)$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Corollary 4.

Stated but not proved: `MetaMathlibExt.totient_dvd_card_orderOf_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#totient-dvd-card-order-of-eq).

## Moduli with exactly $\varphi(L)$ units of even order $L$

Let $n \ge 1$ and let $L \ge 2$
be even. If the number of elements of multiplicative order $L$ in
$(\mathbb{Z}/n\mathbb{Z})^\times$ equals $\varphi(L)$, then either $n = 4$ and $L = 2$, or $n = tq$
for some $t \in \{1, 2\}$ and some odd prime power $q$ with $L \mid \varphi(q)$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Corollary 5.

Stated but not proved: `MetaMathlibExt.card_orderOf_eq_totient_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#card-order-of-eq-totient-classification).

## Elements of order two modulo $n$

For every $n \ge 1$, the number of elements of
multiplicative order $2$ in $(\mathbb{Z}/n\mathbb{Z})^\times$ is $2^k - 1$ for some natural
number $k$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Corollary 6.

Stated but not proved: `MetaMathlibExt.card_orderOf_eq_two_eq_two_pow_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#card-order-of-eq-two-eq-two-pow-sub-one).

## Order-six elements modulo a power of a prime congruent to $1$ mod $6$

Let $p$ be a prime
with $p \equiv 1 \pmod 6$, let $k \ge 1$ and put $n = p^k$. If $b \in \mathbb{Z}/n\mathbb{Z}$ has
multiplicative order $6$, then $b \ne 0$, $2b \ne 1$, $b \ne 1$, $b \ne -1$ and $b \ne 2$ in
$\mathbb{Z}/n\mathbb{Z}$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 16.

Stated but not proved: `MetaMathlibExt.orderOf_eq_six_ne_small_residues` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#order-of-eq-six-ne-small-residues).

## Sign balance for differences of shifted linear residues

Let $p$ be prime, $j \ge 1$ and
$Q = p^j$. Let $g_1, g_2, f_1, f_2$ be natural numbers with $g_1, g_2 < Q$ and $f_1 \le f_2 < Q$
such that $p$ divides none of $g_1$, $g_2$, $g_2 - g_1$, and let $e_1, e_2$ be reals with
$0 < e_1 < e_2 < 1$. For natural $z$ put $c_i(z) = ((g_i z + f_i) \bmod Q) + e_i$ and
$d(z) = c_2(z) - c_1(z)$. Then (a) among $1 \le z \le Q - 1$, the number of $z$ with $d(z) > 0$
equals the number with $d(z) < 0$; and (b) if $f_1 \equiv 0 \pmod p$ or
$f_1 \equiv f_2 \pmod p$, the same holds among the $z$ with $1 \le z \le Q - 1$ and $p \nmid z$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 7.

Stated but not proved: `MetaMathlibExt.sign_balance_shifted_linear_residues` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#sign-balance-shifted-linear-residues).

## Block sums of a repetend

Let $B \ge 2$, $N$, $x < N$, $d \ge 1$ and $k \ge 1$ be natural
numbers, and let $a_i = \lfloor xB^{i+1}/N \rfloor \bmod B$ be the $i$-th base-$B$ digit of $x/N$.
Suppose $a_{i+dk} = a_i$ for every natural number $i$. Let
$S = \sum_{j\lt d} \sum_{i\lt k} a_{jk+i} B^{k-1-i}$ be the sum of the first $d$ blocks of $k$ digits,
each read as a base-$B$ number, and let $R = \sum_{j\lt d} (xB^{jk} \bmod N)$. Then
$SN = R(B^k - 1)$, and if $B^k - 1$ is coprime to $N$, then $B^k - 1$ divides $S$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 9.

Stated but not proved: `MetaMathlibExt.repetend_block_sum_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-block-sum-eq).

## Long division of a proper fraction

Let $m < n$ be natural numbers and $b \ge 1$. For
$j \ge 0$ let $c_j = m b^j \bmod n$ (the remainders of the long division of $m/n$ in base $b$) and
$r_j = \lfloor b c_j / n \rfloor$ (its digits). Then for every $k \ge 0$

$$\frac{m}{n} = \sum_{i\lt k} \frac{r_i}{b^{i+1}} + \frac{c_k}{n b^k},$$

and $r_j n = b c_j - c_{j+1}$ for every $j \ge 0$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 5.

Stated but not proved: `MetaMathlibExt.long_division_remainder_expansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#long-division-remainder-expansion).

## The last repetend digit is nonzero

Let $n \ge 2$ and let $b \ge 2$ be prime to $n$,
with multiplicative order $L$ modulo $n$ (the repetend length of $1/n$ in base $b$). Then the
digit $\lfloor b^{(L-1)+1}/n \rfloor \bmod b$ of $1/n$ at position $L - 1$ is not $0$.

This holds for every such base, not only for the small bases $b < n$ that form the rows of the
paper's table.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 25.

Stated but not proved: `MetaMathlibExt.repetend_last_digit_ne_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-last-digit-ne-zero).

## A constraint on $b^2 + un$ between $2$ and $n - 2$

Let $n$ and $b$ be natural numbers and
$u$ an integer, and put $b_2 = b^2 + un$. If $2 \le b_2 \le n - 2$, then $b \ne u + 1$.

The paper states this for a small base $b$; here $b$ is any natural number.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 31.

Stated but not proved: `MetaMathlibExt.ne_add_one_of_sq_add_mul_mem` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#ne-add-one-of-sq-add-mul-mem).

## Long-division remainders and small bases of prime order

Let $n$ and $L$ be primes and
let $b$ be a natural number of multiplicative order $L$ modulo $n$. Suppose $m = 1$, or
$2 \le m \le n - 1$ and $m$ has multiplicative order $L$ modulo $n$. Then removing $1$ from the
set of remainders $\{m b^j \bmod n : 0 \le j < L\}$ leaves exactly the set of integers $a$ with
$2 \le a \le n - 1$ whose multiplicative order modulo $n$ is $L$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Corollary 2.

Stated but not proved: `MetaMathlibExt.long_division_remainders_erase_one_eq_small_bases` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#long-division-remainders-erase-one-eq-sm).

## Small bases of order greater than two come in pairs

For every natural number $n$ and
every $L > 2$, the number of integers $b$ with $1 \le b < n$ and $\gcd(b, n) = 1$ whose
multiplicative order modulo $n$ is $L$ is even.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 3.

Stated but not proved: `MetaMathlibExt.even_card_small_bases_orderOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#even-card-small-bases-order-of).

## Repetend digits are symmetric under inverse indices

Let $n, b, x, j, j'$ be natural
numbers and $L \ge 1$, and suppose $b$ has multiplicative order $L$ modulo $n$. For $y, c \ge 0$
put $b_y = b^y \bmod n$ and $r_{y,c} = \lfloor b_y^{c+1}/n \rfloor \bmod b_y$, the $c$-th digit
of $1/n$ in base $b_y$. If $\gcd(j, L) = 1$ and $j j' \equiv 1 \pmod L$, then
$r_{xj, j'} = r_{x, j}$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 6.

Stated but not proved: `MetaMathlibExt.repetend_digit_pow_mul_eq_of_mul_modEq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-digit-pow-mul-eq-of-mul-mod-eq).

## Columns $j$ and $j^{-1}$ of a repetend table match

Let $n$ and $L \ge 1$ be natural
numbers, and consider the repetend table of $1/n$ whose rows are the natural numbers $1 \le b < n$
coprime to $n$ of multiplicative order $L$ modulo $n$, and whose column $j$ holds the digits
$\lfloor b^{j+1}/n \rfloor \bmod b$. If $j$ and $j'$ are natural numbers with $j$ coprime to $L$,
$j^2 \not\equiv 1 \pmod L$ and $jj' \equiv 1 \pmod L$, then columns $j$ and $j'$ are equal as
multisets.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 2.

Stated but not proved: `MetaMathlibExt.repetend_column_eq_column_of_mul_modEq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-column-eq-column-of-mul-mod-eq).

## Units modulo $L$ whose square is not $1$

Let $L \ge 1$, let $e$ be the exponent of $2$
in $L$ and let $f$ be the number of distinct odd prime factors of $L$. Then the number of
integers $0 \le j < L$ with $\gcd(j, L) = 1$ and $j^2 \not\equiv 1 \pmod{L}$ is
$\varphi(L) - 2^{f + g(e)}$, where $g(e) = \max(0, \min(2, e - 1))$.

In the paper these $j$ index the Class A columns of a repetend table.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_coprime_not_sq_modEq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#card-coprime-not-sq-mod-eq-one).

## The last column pairs a base with its inverse

Let $n$ and $L \ge 1$ be natural numbers
and let $b < n$ have multiplicative order $L$ modulo $n$. Put $b' = b^{L-1} \bmod n$, the inverse
of $b$ modulo $n$. Then $b$ and $b'$ have the same digit in column $L - 1$:
$\lfloor b'^{L}/n \rfloor \bmod b' = \lfloor b^{L}/n \rfloor \bmod b$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 2.

Stated but not proved: `MetaMathlibExt.repetend_last_column_inv_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-last-column-inv-eq).

## Class B matched columns of repetend tables

Let $a \ge 1$ and $L = 12a + 6$, let $p$ be a
prime with $p \equiv 1 \pmod L$, let $k \ge 1$ and $n = p^k$, and let $b$ be a natural number of
multiplicative order $L$ modulo $n$; write $b_i = b^i \bmod n$. Let the rows be the integers $c$
with $1 \le c < n$, $\gcd(c, n) = 1$ and multiplicative order $L$ modulo $n$, and let column $j$
be the multiset of the digits $\lfloor c^{j+1}/n \rfloor \bmod c$ over these rows. Then
$\lfloor (b_i + b_{i + L/3} + b_{i + 2L/3})/n \rfloor = 1$ for every $0 \le i < L$ coprime to $L$
if and only if columns $2a + 1$ and $4a + 2$ are equal and columns $8a + 4$ and $10a + 5$ are
equal.

The proportion conjectured in the source is not stated here.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 4.

Stated but not proved: `MetaMathlibExt.repetend_columns_match_iff_triple_sum_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-match-iff-triple-sum-eq).

## Differences of repetend digits

Let $n \ge 1$ and $b$ be natural numbers with
$\gcd(b, n) = 1$. For $x, j \ge 0$ put $b_x = b^x \bmod n$ and
$r_{x,j} = \lfloor b_x^{j+1}/n \rfloor \bmod b_x$. Then for all natural numbers $y, m, d, e$,

$$n (r_{ym,e} - r_{y,d}) = b_{ym} b_{yme} - b_{ym(e+1)} - b_y b_{yd} + b_{y(d+1)}.$$

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 7.

Stated but not proved: `MetaMathlibExt.repetend_digit_sub_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-digit-sub-eq).

## The $p$-adic valuation of $B^2 - B + 1$ for a base of order $6p^j$

Let $p$ be a prime
with $p \equiv 1 \pmod 6$, let $i$ and $j$ be natural numbers with $j \ge 1$ and $i \ge 2j$, and
let $B$ be a natural number whose multiplicative order modulo $p^i$ is $6p^j$. Then the $p$-adic
valuation of $B^2 - B + 1$ is exactly $i - j$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 8.

Stated but not proved: `MetaMathlibExt.padicValNat_sq_sub_add_one_of_orderOf_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#padic-val-nat-sq-sub-add-one-of-order-of).

## A power of $B$ equal to $B - 1$ modulo $p^i$

Let $p$ be a prime with $p \equiv 1 \pmod 6$,
let $i$ and $j$ be natural numbers with $j \ge 1$ and $i \ge 2j$, put $n = p^i$ and $Q = p^j$, and
let $B < n$ be a natural number whose multiplicative order modulo $n$ is $6Q$. Let $z < 6Q$ be a
natural number with $z \equiv 2 \pmod 6$ such that $zB \equiv 1 \pmod Q$ or
$z \equiv 1 - B \pmod Q$. Then $B^z \bmod n = B - 1$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 9.

Stated but not proved: `MetaMathlibExt.pow_mod_eq_sub_one_of_orderOf_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 256](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L256). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#pow-mod-eq-sub-one-of-order-of-eq).

## Powers of a base of order $6p^j$ modulo $p^j$ depend only on the exponent modulo $6$

Let
$p$ be a prime, let $i$ and $j$ be natural numbers with $j \ge 1$ and $i \ge 2j$, and let $b$ be a
natural number whose multiplicative order modulo $p^i$ is $6p^j$. If $y$ and $s$ are natural
numbers with $y \equiv s \pmod 6$, then $b^y \equiv b^s \pmod{p^j}$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 10.

Stated but not proved: `MetaMathlibExt.pow_modEq_pow_of_modEq_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#pow-mod-eq-pow-of-mod-eq-six).

## Powers of $b^y \bmod p^i$ that differ by one

Let $p$ be a prime with $p \equiv 1 \pmod 6$,
let $i$ and $j$ be natural numbers with $j \ge 1$ and $i \ge 2j$, put $n = p^i$ and $Q = p^j$, and
let $b$ be a natural number whose multiplicative order modulo $n$ is $6Q$. Let $f \in \{1, -1\}$,
let $y$ be a natural number with $y \equiv s \pmod 6$ for some $s \in \{1, -1\}$, and put $e = 1$
if $sf = 1$ and $e = 5$ if $sf = -1$. Let $d$ be a natural number with $d \equiv 2f \pmod 6$, and
let $k < 6Q$ be a natural number with $k \equiv f \pmod 6$ and $k \equiv b^e d \pmod Q$. Then, with
$B = b^y \bmod n$, we have $B^k \bmod n = (B^d \bmod n) + 1$.

Here $b^5$ stands for $b^{-1}$ modulo $Q$, as $b^6 \equiv 1 \pmod Q$, so $b^e$ is $b^{sf}$ modulo
$Q$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 11.

Stated but not proved: `MetaMathlibExt.pow_mod_eq_pow_mod_add_one_of_crt` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 278](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L278). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#pow-mod-eq-pow-mod-add-one-of-crt).

## Relations among the powers $B^{zp^j} \bmod p^i$ for a base of order $6p^j$

Let $p$ be a
prime with $p \equiv 1 \pmod 6$, let $i$ and $j$ be natural numbers, put $n = p^i$ and $Q = p^j$,
and let $B$ be a natural number whose multiplicative order modulo $n$ is $6Q$. Write
$B_z = B^z \bmod n$. Then $B_{2Q} = B_Q - 1$, $B_{4Q} = B_{5Q} - 1$, $B_Q + B_{5Q} = n + 1$ and
$B_{3Q} = n - 1$; moreover $Q^2 \equiv Q \pmod{6Q}$.

Since $B^{6Q} \equiv 1 \pmod n$, the residues $B_{5Q}$ and $B_{4Q}$ are those of $B^{-Q}$ and
$B^{-2Q}$. The paper assumes $j \ge 1$ and $i \ge 2j$; these are not needed here.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 13.

Stated but not proved: `MetaMathlibExt.pow_mod_relations_of_orderOf_eq_six_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#pow-mod-relations-of-order-of-eq-six-mul).

## Digit differences for a base of order $6p^j$ modulo $p^i$

Let $p$ be a prime with
$p \equiv 1 \pmod 6$, let $i$ and $j$ be natural numbers, and put $n = p^i$ and $Q = p^j$. Let
$B < n$ be a natural number whose multiplicative order modulo $n$ is $6Q$, let $f \in \{1, -1\}$,
and let $d$ and $e$ be natural numbers with $d \equiv 2fQ \pmod{6Q}$ and $e \equiv fQ \pmod{6Q}$.
For natural $s$ write $r_s = \lfloor B^{s+1}/n \rfloor \bmod B$ for the $s$-th base-$B$ digit of
$1/n$, and put $D = n(r_e - r_d)$. Then $D = B + (B^{d+1} \bmod n) - (B^{e+1} \bmod n)$, and
$D = 0$ or $D = n$.

The statement is made for all natural numbers $i$ and $j$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 14.

Stated but not proved: `MetaMathlibExt.repetend_digit_sub_mem_zero_n` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-digit-sub-mem-zero-n).

## Class C matched columns of repetend tables

Let $p$ be a prime with $p \equiv 1 \pmod 6$,
let $j \ge 1$ and $i \ge 2j$, and put $n = p^i$, $Q = p^j$ and $L = 6Q$. Let $b$ be a natural
number of multiplicative order $L$ modulo $n$, and let $d, e < L$ be natural numbers with
$d \equiv b^2 \pmod Q$, $e \equiv b^4 \pmod Q$ and $d \equiv e \equiv 4 \pmod 6$. Let the rows be
the integers $c$ with $1 \le c < n$, $\gcd(c, n) = 1$ and multiplicative order $L$ modulo $n$, and
let column $s$ be the multiset of the digits $\lfloor c^{s+1}/n \rfloor \bmod c$ over these rows.
Then columns $d$ and $e$ are equal.

Theorem 6 of the source also says when the digit difference between these columns is $0$; that
clause is not stated here.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 6.

Stated but not proved: `MetaMathlibExt.repetend_columns_eq_of_crt_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 325](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L325). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-eq-of-crt-sq).

## Repetend tables of length at most $2$ have no matched columns

Let $n$ and $L \le 2$ be
natural numbers, let the rows be the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and
multiplicative order $L$ modulo $n$, and let column $j$ be the multiset of the digits
$\lfloor b^{j+1}/n \rfloor \bmod b$ over these rows. If there is at least one row, then for all
distinct $i, j < L$ columns $i$ and $j$ are different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 26.

Stated but not proved: `MetaMathlibExt.repetend_columns_ne_of_le_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-ne-of-le-two).

## Repetend tables with one or three rows have no matched columns

For natural numbers $n$
and $L$, let the rows be the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and multiplicative
order $L$ modulo $n$, and let column $j$ be the multiset of the digits
$\lfloor b^{j+1}/n \rfloor \bmod b$ over these rows. If there are exactly one or exactly three
rows, then for all distinct $i, j < L$ columns $i$ and $j$ are different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 27.

Stated but not proved: `MetaMathlibExt.repetend_columns_ne_of_card_eq_one_or_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-ne-of-card-eq-one-or-th).

## Matching columns of a two-row repetend table

Let $n$ and $L$ be natural numbers and let
$B$ be the set of integers $c$ with $1 \le c < n$, $\gcd(c, n) = 1$ and multiplicative order $L$
modulo $n$. For $c \in B$ and $k \ge 0$ let $r_k(c) = \lfloor c^{k+1}/n \rfloor \bmod c$, and let
$C_k$ be the multiset of the $r_k(c)$ over $c \in B$. Suppose $B$ has exactly two elements, $b$
and $b' \ne b$, and put $D_k = r_k(b') - r_k(b)$. Then for all $i, j \ge 0$ with $C_i = C_j$,
$D_i = D_j$ or $D_i = -D_j$, and the sum of the elements of $C_i$ equals that of $C_j$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 28.

Stated but not proved: `MetaMathlibExt.repetend_digit_diff_of_columns_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-digit-diff-of-columns-eq).

## Half-period symmetry of the repetend of $1/n$

Let $n$ be a natural number whose unit
group $(\mathbb{Z}/n\mathbb{Z})^\times$ is cyclic, let $L > 0$ be even, and let $b < n$ be a
natural number whose multiplicative order modulo $n$ is $L$. For natural numbers $m$ write
$b_m = b^m \bmod n$ and $r_m = \lfloor b^{m+1}/n \rfloor \bmod b$, the $m$-th base-$b$ digit of
$1/n$. Then for every natural number $j$ we have $b_{j+L/2} = n - b_j$ and
$r_j + r_{j+L/2} = r_{L/2}$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 29.

Stated but not proved: `MetaMathlibExt.pow_add_half_mod_eq_and_digit_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#pow-add-half-mod-eq-and-digit-add).

## Two-row repetend tables of length $3$ have no matched columns

For a natural number $n$,
let the rows be the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and multiplicative order $3$
modulo $n$, and let column $j$ be the multiset of the digits $\lfloor b^{j+1}/n \rfloor \bmod b$
over these rows. If there are exactly two rows, then for all distinct $i, j < 3$ columns $i$ and
$j$ are different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 30.

Stated but not proved: `MetaMathlibExt.repetend_columns_ne_of_card_two_of_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 382](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L382). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-ne-of-card-two-of-three).

## Two-row repetend tables of length $4$ have no matched columns

For a natural number $n$,
let the rows be the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and multiplicative order $4$
modulo $n$, and let column $j$ be the multiset of the digits $\lfloor b^{j+1}/n \rfloor \bmod b$
over these rows. If there are exactly two rows, then for all distinct $i, j < 4$ columns $i$ and
$j$ are different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 32.

Stated but not proved: `MetaMathlibExt.repetend_columns_ne_of_card_two_of_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-ne-of-card-two-of-four).

## Moduli with exactly two small bases of order six

Let $n$ be a natural number. If exactly
two integers $b$ with $1 \le b < n$ and $\gcd(b, n) = 1$ have multiplicative order $6$ modulo $n$,
then either $n = 3^k t \ge 9$ for some natural number $k$ and some $t \in \{1, 2\}$, or
$n = p^k t$ for some prime $p \equiv 1 \pmod 6$, some $k \ge 1$ and some $t \in \{1, 2\}$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 33.

Stated but not proved: `MetaMathlibExt.eq_of_card_small_bases_orderOf_six_eq_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#eq-of-card-small-bases-order-of-six-eq-t).

## Order-$6$ repetend tables of $3^k t$ have no matched columns

Let $k \ge 2$ and
$t \in \{1, 2\}$, and put $n = 3^k t$. Let the rows be the integers $b$ with $1 \le b < n$,
$\gcd(b, n) = 1$ and multiplicative order $6$ modulo $n$, and let column $j$ be the multiset of
the digits $\lfloor b^{j+1}/n \rfloor \bmod b$ over these rows. Then for all distinct $i, j < 6$
columns $i$ and $j$ are different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 34.

Stated but not proved: `MetaMathlibExt.repetend_columns_ne_of_three_pow_of_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-ne-of-three-pow-of-six).

## Powers of a base of order $6$ modulo $tp^k$

Let $p$ be a prime with $p \equiv 1 \pmod 6$,
let $k \ge 1$ and $t \in \{1, 2\}$ be natural numbers, and put $n = tp^k$. Let $b_1 < n$ be a
natural number whose multiplicative order modulo $n$ is $6$, write $b_m = b_1^m \bmod n$, and put
$H = 0$ if $t = 1$, $H = p^k$ if $t = 2$ and $b_1 < p^k$, and $H = -p^k$ if $t = 2$ and
$b_1 \ge p^k$. Then $b_2 = b_1 - 1 + H$, $b_3 = n - 1$, $b_4 = n - b_1$ and
$b_5 = n - b_1 + 1 - H$, and there is an integer $u$ with $b_1^2 = un + b_1 - 1 + H$,
$b_2^2 = un - b_1 + (H + 2b_1 - 1)H$ and $b_1 b_2 = un - 1 + (b_1 + 1)H$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 35.

Stated but not proved: `MetaMathlibExt.pow_mod_eqs_of_orderOf_eq_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#pow-mod-eqs-of-order-of-eq-six).

## Digit differences between the rows $b_1$ and $b_1^5$ of the order-$6$ table

Let
$p \equiv 1 \pmod 6$ be prime, $k \ge 1$, $t \in \{1, 2\}$ and $n = t p^k$, and let $b_1 < n$
have multiplicative order $6$ modulo $n$. Put $H = 0$ if $t = 1$, $H = p^k$ if $t = 2$ and
$b_1 < p^k$, and $H = -p^k$ if $t = 2$ and $b_1 \ge p^k$. Let $b_5 = b_1^5 \bmod n$ and, for
$i \ge 0$, $D_i = r_i(b_5) - r_i(b_1)$, where $r_i(c) = \lfloor c^{i+1}/n \rfloor \bmod c$. Then
$D_0 = D_5 = 0$, $D_2 = n - b_1 - (b_1^2 \bmod n) = 1 - 2 b_1 + n - H$,
$n D_1 = (n - H) D_2$, $D_3 = D_2$ and $n D_4 = H D_2$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 36.

Stated but not proved: `MetaMathlibExt.repetend_digit_diffs_of_orderOf_eq_six` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-digit-diffs-of-order-of-eq-six).

## Columns $0$ and $5$ of the order-$6$ repetend table of $t p^k$ differ

Let $p$ be a prime
with $p \equiv 1 \pmod 6$, let $k \ge 1$ and $t \in \{1, 2\}$, and put $n = t p^k$. Let the rows be
the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and multiplicative order $6$ modulo $n$, and
let column $j$ be the multiset of the digits $\lfloor b^{j+1}/n \rfloor \bmod b$ over these rows.
Then columns $0$ and $5$ are different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 37.

Stated but not proved: `MetaMathlibExt.repetend_column_zero_ne_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-column-zero-ne-five).

## Columns $1$, $2$, $3$ of the order-$6$ repetend table differ from columns $0$ and $5$

Let
$p \equiv 1 \pmod 6$ be prime, $k \ge 1$, $t \in \{1, 2\}$ and $n = t p^k$, and let $B$ be the set
of integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and multiplicative order $6$ modulo $n$. For
$c \ge 0$ let column $c$ be the multiset of the digits $\lfloor b^{c+1}/n \rfloor \bmod b$ over
$b \in B$. Then for every $i \in \{1, 2, 3\}$ and $j \in \{0, 5\}$, columns $i$ and $j$ are
different multisets.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 38.

Stated but not proved: `MetaMathlibExt.repetend_columns_one_to_three_ne_zero_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-one-to-three-ne-zero-fi).

## Column $4$ of the order-$6$ repetend table of $t p^k$ differs from columns $0$ and $5$

Let $p$ be a prime with $p \equiv 1 \pmod 6$, let $k \ge 1$ and $t \in \{1, 2\}$, and put
$n = t p^k$. Let the rows be the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and
multiplicative order $6$ modulo $n$, and let column $j$ be the multiset of the digits
$\lfloor b^{j+1}/n \rfloor \bmod b$ over these rows. Then column $4$ is different from column $0$
and from column $5$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 39.

Stated but not proved: `MetaMathlibExt.repetend_column_four_ne_zero_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-column-four-ne-zero-five).

## Columns $1$ to $4$ of the order-$6$ repetend table of $t p^k$ are pairwise different

Let
$p$ be a prime with $p \equiv 1 \pmod 6$, let $k \ge 1$ and $t \in \{1, 2\}$, and put $n = t p^k$.
Let the rows be the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and multiplicative order $6$
modulo $n$, and let column $j$ be the multiset of the digits $\lfloor b^{j+1}/n \rfloor \bmod b$
over these rows. Then for all distinct $i, j \in \{1, 2, 3, 4\}$ columns $i$ and $j$ are
different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 40.

Stated but not proved: `MetaMathlibExt.repetend_columns_one_to_four_pairwise_ne` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 490](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L490). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-one-to-four-pairwise-ne).

## Repetend tables with at most three rows have no matched columns

For natural numbers $n$
and $L$, let the rows be the integers $b$ with $1 \le b < n$, $\gcd(b, n) = 1$ and multiplicative
order $L$ modulo $n$, and let column $j$ be the multiset of the digits
$\lfloor b^{j+1}/n \rfloor \bmod b$ over these rows. If there are at least one and at most three
rows, then for all distinct $i, j < L$ columns $i$ and $j$ are different.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Theorem 12.

Stated but not proved: `MetaMathlibExt.repetend_columns_ne_of_card_le_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 502](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L502). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#repetend-columns-ne-of-card-le-three).

## Tail bound for sums of inverse powers

For natural numbers $m \ge 2$ and $s \ge 1$,
$\sum_{n = s+1}^{\infty} n^{-m} < \dfrac{1}{(m-1)\, s^{m-1}}$.

## Sources

- R. J. Booth and D. J. Horton, *Matched Column Sets in Repetend Tables*, INTEGERS 25 (2025), Article A26, Lemma 42.

Stated but not proved: `MetaMathlibExt.tsum_inv_pow_succ_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/RepetendTableWanted.lean, line 511](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RepetendTableWanted.lean#L511). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html#tsum-inv-pow-succ-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Repetend tables](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/repetend-tables)
