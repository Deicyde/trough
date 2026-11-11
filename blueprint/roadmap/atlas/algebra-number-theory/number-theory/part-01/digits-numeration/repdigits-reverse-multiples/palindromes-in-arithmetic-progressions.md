---
declaration: section
origin: cited
lean: MetaMathlibExt.floor_add_floor_neg_and_floor_add_eq, MetaMathlibExt.palindromeAPCount, MetaMathlibExt.palindromicHalfCopy, MetaMathlibExt.digitSumCongruenceCount, MetaMathlibExt.palindromeAPCount_small, MetaMathlibExt.palindromicHalfCopy_example, MetaMathlibExt.digitSumCongruenceCount_small, MetaMathlibExt.digitSumCongruenceCount_of_modEq_one
statement: formalized
---

# Palindromes in arithmetic progressions

13 results, 6 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html).

## Two floor-function identities

For every real number $x$, the sum
$\lfloor x \rfloor + \lfloor -x \rfloor$ equals $0$ if $x$ is an integer and $-1$ otherwise.
For all real numbers $x$ and $y$, $\lfloor x + y \rfloor = \lfloor x \rfloor + \lfloor y \rfloor$ if
$(x - \lfloor x \rfloor) + (y - \lfloor y \rfloor) < 1$, and
$\lfloor x + y \rfloor = \lfloor x \rfloor + \lfloor y \rfloor + 1$ otherwise.

These are parts (iii) and (v) of the cited lemma; its remaining parts are not restated here.

## Sources

- Kritkhajohn Onphaeng, Tammatada Khemaratchatakumthorn, Phakhinkon Napp Phunphayap and Prapanpong Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Lemma 6 (`jis-2024-24.4.8-lem-6`).

Stated but not proved: `MetaMathlibExt.floor_add_floor_neg_and_floor_add_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#floor-add-floor-neg-and-floor-add-eq).

## Palindromes in an arithmetic progression

For natural numbers $b$, $m$, $q$ and $r$,
$A_b(m, q, r)$ is the number of base-$b$ palindromes $n$ with $1 \le n \le m$ and
$n \equiv r \pmod q$, where a natural number is a base-$b$ palindrome when its string of base-$b$
digits reads the same in both directions.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Section 1.

Formalized by `MetaMathlibExt.palindromeAPCount`, a definition declared in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindrome-apcount).

## Palindromic half copy

For natural numbers $b$ and $m \ge 1$, write
$m = (a_k a_{k-1} \cdots a_0)_b$ for the base-$b$ digits of $m$. The palindromic half copy of $m$
is $C_b(m) = \sum_{j=0}^{k} a_{\max(j, k - j)} b^j$: the $b$-adic palindrome with the same number
of digits as $m$ whose upper digits $a_k, \dots, a_{\lceil k/2 \rceil}$ are those of $m$ and whose
lower digits mirror them. For $m = 0$, which has no digits, $C_b(0) = 0$.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Definition 1.

Formalized by `MetaMathlibExt.palindromicHalfCopy`, a definition declared in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindromic-half-copy).

## Digit-sum congruence count

For natural numbers $b$, $k$, $q$, $x$, $y$ and an integer $r$,
$N_b(k, q, r, x, y)$ is the number of tuples $(x_1, \dots, x_k)$ of natural numbers with
$x \le x_1 < y$ and $x_i < b$ for $2 \le i \le k$ such that $x_1 + \dots + x_k \equiv r \pmod q$.
The count is meant for $k \ge 1$; for $k = 0$ it is defined to equal its value for $k = 1$, the
number of natural numbers $x_1$ with $x \le x_1 < y$ and $x_1 \equiv r \pmod q$.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Definition 3.

Formalized by `MetaMathlibExt.digitSumCongruenceCount`, a definition declared in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#digit-sum-congruence-count).

## Two small palindrome counts

Write $A_b(m, q, r)$ for the number of base-$b$ palindromes
$n$ with $1 \le n \le m$ and $n \equiv r \pmod q$. Then $A_{10}(100, 1, 0) = 18$, the palindromes
being $1, \dots, 9$ and $11, 22, \dots, 99$, and $A_2(9, 2, 1) = 5$, the odd base-$2$ palindromes
up to $9$ being $1$, $3 = (11)_2$, $5 = (101)_2$, $7 = (111)_2$ and $9 = (1001)_2$.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Section 1.

Formalized by `MetaMathlibExt.palindromeAPCount_small`, a theorem declared in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindrome-apcount-small).

## Palindromic half copies of $5570$ in bases $5$ and $8$

Write $C_b(m)$ for the
palindromic half copy of $m$ in base $b$. For $m = 5570 = (134240)_5 = (12702)_8$,
$C_5(m) = (134431)_5 = 5616$ and $C_8(m) = (12721)_8 = 5585$.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Definition 1 (example).

Formalized by `MetaMathlibExt.palindromicHalfCopy_example`, a theorem declared in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindromic-half-copy-example).

## A small value of the digit-sum congruence count

In the notation $N_b(k, q, r, x, y)$
of the digit-sum congruence count, $N_3(2, 2, 0, 0, 3) = 5$: exactly five pairs $(x_1, x_2)$ of
natural numbers with $x_1, x_2 < 3$ have even sum.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Definition 3.

Formalized by `MetaMathlibExt.digitSumCongruenceCount_small`, a theorem declared in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#digit-sum-congruence-count-small).

## Counting digit tuples by their sum modulo a divisor of the base minus one

Let $a$, $b$,
$k$ and $q$ be natural numbers, all at least $1$, with $b \equiv 1 \pmod q$, and let $r$ be an
integer. For natural numbers $x$ and $y$ write $N_b(k, q, r, x, y)$ for the number of tuples
$(x_1, \dots, x_k)$ of natural numbers with $x \le x_1 < y$, $x_i < b$ for $2 \le i \le k$, and
$x_1 + \dots + x_k \equiv r \pmod q$. Write $[P]$ for $1$ if $P$ holds and $0$ otherwise,
$\lfloor a/q \rfloor$ for the integer part of $a/q$, and $r \bmod q$ and $a \bmod q$ for the least
nonnegative residues modulo $q$. Then, as rational numbers,

$$N_b(k, q, r, 0, b) = \frac{b^k - 1}{q} + [r \equiv 0 \pmod q],$$



$$N_b(k, q, r, 1, b) = \frac{b^k - b^{k-1}}{q},$$



$$N_b(k, q, r, 0, a) = \frac{a (b^{k-1} - 1)}{q} + \lfloor a/q \rfloor + [r \bmod q < a \bmod q],$$



$$N_b(k, q, r, 1, a) = \frac{(a - 1)(b^{k-1} - 1)}{q} + \lfloor a/q \rfloor +
[r \bmod q < a \bmod q] - [r \equiv 0 \pmod q].$$

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Lemma 5.

Stated but not proved: `MetaMathlibExt.digitSumCongruenceCount_of_modEq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#digit-sum-congruence-count-of-mod-eq-one).

## Palindromes in residue classes modulo a divisor of the base

Let $b \ge 2$, $m \ge 1$ and
$q \ge 1$ be natural numbers with $q \mid b$. Write $m = (a_k a_{k-1} \cdots a_0)_b$ in base $b$,
with leading digit $a_k$. Write $A_b(m, q, r)$ for the number of base-$b$ palindromes $n$ with
$1 \le n \le m$ and $n \equiv r \pmod q$, $C_b(m)$ for the palindromic half copy of $m$, and
$[P]$ for $1$ if $P$ holds and $0$ otherwise. Put

$$\alpha = \frac{b^{\lceil k/2 \rceil} + b^{\lfloor k/2 \rfloor} - 2}{b - 1}, \quad
S = \sum_{i=1}^{\lfloor k/2 \rfloor} a_{k-i} b^{\lfloor k/2 \rfloor - i}, \quad
\delta = [C_b(m) \le m].$$

Then, as rational numbers,

$$A_b(m, q, 0) = \left(\frac{b}{q} - 1\right) \alpha +
\left\lfloor \frac{a_k - 1}{q} \right\rfloor b^{\lfloor k/2 \rfloor} +
[a_k \equiv 0 \pmod q] (S + \delta),$$

and for every natural number $r$ with $r \bmod q > 0$,

$$A_b(m, q, r) = \frac{b \alpha}{q} +
\left\lceil \frac{a_k - (r \bmod q)}{q} \right\rceil b^{\lfloor k/2 \rfloor} +
[a_k \equiv r \pmod q] (S + \delta).$$

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Theorem 7.

Stated but not proved: `MetaMathlibExt.palindromeAPCount_of_dvd_base` is written with `theorem_wanted` in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindrome-apcount-of-dvd-base).

## Counting palindromes up to $m$ and by parity

Let $b \ge 2$ and $m \ge 1$, and write
$m = (a_k a_{k-1} \cdots a_0)_b$ in base $b$, with leading digit $a_k \ne 0$. For natural numbers
$q$ and $r$, let $A_b(m, q, r)$ be the number of $b$-adic palindromes $n$ with $1 \le n \le m$
and $n \equiv r \pmod q$, and let $C_b(m)$ be the palindromic half copy of $m$. Put $\delta = 1$
if $C_b(m) \le m$ and $\delta = 0$ otherwise. Then
$A_b(m, 1, 0) = b^{\lceil k/2 \rceil} +
\sum_{i=0}^{\lfloor k/2 \rfloor} a_{k-i} b^{\lfloor k/2 \rfloor - i} + \delta - 2$.
If moreover $b$ is even, let
$\alpha = (b^{\lceil k/2 \rceil} + b^{\lfloor k/2 \rfloor} - 2)/(b - 1)$ and
$S = \sum_{i=1}^{\lfloor k/2 \rfloor} a_{k-i} b^{\lfloor k/2 \rfloor - i}$, let $\varepsilon_0 = 1$
if $a_k$ is even and $\varepsilon_0 = 0$ otherwise, and let $\varepsilon_1 = 1 - \varepsilon_0$.
Then $A_b(m, 2, 0) = (b/2 - 1)\alpha + \lfloor (a_k - 1)/2 \rfloor b^{\lfloor k/2 \rfloor} +
\varepsilon_0 (S + \delta)$ and
$A_b(m, 2, 1) = b\alpha/2 + \lceil (a_k - 1)/2 \rceil b^{\lfloor k/2 \rfloor} +
\varepsilon_1 (S + \delta)$.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Corollary 8.

Stated but not proved: `MetaMathlibExt.palindromeCount_closed_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindrome-count-closed-form).

## Palindromes in residue classes modulo a divisor of the base minus one

Let $b \ge 2$,
$m \ge 1$ and $q \ge 1$ be natural numbers with $b \equiv 1 \pmod q$, and let $r$ be a natural
number with $r < q$. Write $m = (a_k a_{k-1} \cdots a_0)_b$ in base $b$. Write $A_b(m, q, r)$ for
the number of base-$b$ palindromes $n$ with $1 \le n \le m$ and $n \equiv r \pmod q$, $C_b(m)$
for the palindromic half copy of $m$, $[P]$ for $1$ if $P$ holds and $0$ otherwise, and
$t \bmod d$ for the least nonnegative residue of an integer $t$ modulo a positive integer $d$.
For $j \ge 0$ define integers $s_j$ and $r_j$ as follows. If $q$ is even and $2j \ne k$, let
$s_j = a_{k-j} \bmod (q/2)$ and
$r_j = \bigl(\lfloor r/2 \rfloor - \sum_{i=0}^{j-1} a_{k-i}\bigr) \bmod (q/2)$. If $q$ is odd
and $2j \ne k$, let $s_j = a_{k-j} \bmod q$ and
$r_j = \bigl(\frac{q+1}{2} r - \sum_{i=0}^{j-1} a_{k-i}\bigr) \bmod q$. If $2j = k$, let
$s_j = a_{k-j} \bmod q$ and $r_j = \bigl(r - 2 \sum_{i=0}^{k/2-1} a_{k-i}\bigr) \bmod q$. Put
$\delta = [C_b(m) \le m] \, [r_{\lfloor k/2 \rfloor} = s_{\lfloor k/2 \rfloor}]$ and

$$m_1^* = \sum_{j=0}^{\lfloor (k-1)/2 \rfloor}
\left( \frac{2 a_{k-j} b^{\lfloor (k-1)/2 \rfloor - j} - 2 s_j}{q} + [r_j < s_j] \right),$$



$$m_2^* = \sum_{j=0}^{\lfloor k/2 \rfloor - 1}
\frac{a_{k-j} (b - 1) b^{\lfloor k/2 \rfloor - j - 1}}{q},$$



$$m_3^* = \sum_{j=0}^{\lfloor k/2 \rfloor - 1}
\left( \frac{a_{k-j} (b + 1) b^{\lfloor k/2 \rfloor - j - 1} - 2 s_j}{q} + [r_j < s_j] \right).$$

Then, as rational numbers, if $q$ is odd,

$$A_b(m, q, r) = \frac{b^{\lfloor (k+1)/2 \rfloor} - 1}{q} +
\sum_{j=0}^{\lfloor k/2 \rfloor} \left( \left\lfloor \frac{a_{k-j} b^{\lfloor k/2 \rfloor - j}}{q}
\right\rfloor + [r_j < s_j] \right) - [r = 0] + \delta,$$

and if $q$ is even, $A_b(m, q, r)$ equals $(b - 1) b^{(k-1)/2}/q$ when $k$ and $r$ are odd,
$((b + 1) b^{(k-1)/2} - 2)/q + m_1^* - [r = 0] + \delta$ when $k$ is odd and $r$ is even,
$\lfloor a_{k/2}/q \rfloor + m_2^* + [r_{k/2} < s_{k/2}] + \delta$ when $k$ is even and $r$ is
odd, and $2(b^{k/2} - 1)/q + \lfloor a_{k/2}/q \rfloor + m_3^* - [r = 0] +
[r_{k/2} < s_{k/2}] + \delta$ when $k$ and $r$ are both even.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Theorem 9.

Stated but not proved: `MetaMathlibExt.palindromeAPCount_of_modEq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindrome-apcount-of-mod-eq-one).

## Palindromes up to a power of the base in residue classes

Let $b \ge 2$, $k \ge 1$ and
$q \ge 1$ be natural numbers and let $r$ be a natural number with $r < q$. Write $A_b(m, q, r)$
for the number of base-$b$ palindromes $n$ with $1 \le n \le m$ and $n \equiv r \pmod q$, and
$[r = 0]$ for $1$ if $r = 0$ and $0$ otherwise. If $q \mid b$, then

$$A_b(b^k, q, r) = \left(\frac{b}{q} - [r = 0]\right)
\frac{b^{\lceil k/2 \rceil} + b^{\lfloor k/2 \rfloor} - 2}{b - 1}.$$

If $b \equiv 1 \pmod q$, then $A_b(b^k, q, r)$ equals
$(b^{\lceil k/2 \rceil} + b^{\lfloor k/2 \rfloor} - 2)/q$ if $q$ is odd,
$(b - 1) b^{\lfloor (k-1)/2 \rfloor}/q$ if $q$ is even and $r$ is odd, and
$((b + 1) b^{\lfloor (k-1)/2 \rfloor} + 2 b^{\lfloor k/2 \rfloor} - 4)/q$ if $q$ and $r$ are both
even. All these identities hold as identities of rational numbers.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Corollary 11.

Stated but not proved: `MetaMathlibExt.palindromeAPCount_base_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#palindrome-apcount-base-pow).

## Palindromes in residue classes: a logarithmic error bound

Let $b \ge 2$ be a natural
number, let $q$ be an odd natural number with $b \equiv 1 \pmod q$, and let $r$ be a natural
number with $r < q$. For natural numbers $m$, $q'$ and $r'$, write $A_b(m, q', r')$ for the number
of base-$b$ palindromes $n$ with $1 \le n \le m$ and $n \equiv r' \pmod{q'}$; thus $A_b(m, 1, 0)$
is the number of all base-$b$ palindromes in $[1, m]$. Then for every natural number $m \ge 1$,

$$\left| A_b(m, q, r) - \frac{A_b(m, 1, 0)}{q} \right| \le \frac{\log m}{2 \log b} + 2,$$

where $\log$ is the natural logarithm.

## Sources

- K. Onphaeng, T. Khemaratchatakumthorn, P. N. Phunphayap and P. Pongsriiam, *Exact Formulas for the Number of Palindromes in Certain Arithmetic Progressions*, Journal of Integer Sequences 27 (2024), Article 24.4.8, Corollary 12.

Stated but not proved: `MetaMathlibExt.abs_palindromeAPCount_sub_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PalindromesArithmeticProgressionsWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html#abs-palindrome-apcount-sub-le).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Palindromes in arithmetic progressions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromes-in-arithmetic-progressions)
