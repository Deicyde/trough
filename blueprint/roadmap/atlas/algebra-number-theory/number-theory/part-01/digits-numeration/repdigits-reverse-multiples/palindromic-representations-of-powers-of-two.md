---
declaration: section
origin: cited
lean: MetaMathlibExt.minPalindromicBase, MetaMathlibExt.HasBinomialForm, MetaMathlibExt.minPalindromicBase_two, MetaMathlibExt.hasBinomialForm_16_2023, MetaMathlibExt.minPalindromicBase_eq_pred, MetaMathlibExt.digits_mul_one_add_pow, MetaMathlibExt.hasBinomialForm_two_pow, MetaMathlibExt.binomialForm_two_pow_base
statement: formalized
---

# Palindromic representations of powers of two

18 results, 4 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html).

## Minimum palindromic base

For a natural number $N$, $b(N)$ is the smallest base $b \ge 2$
in which $N$ is a palindrome, that is, in which the base-$b$ digits of $N$ read the same forwards
and backwards. Such a base exists: $0$ has no digits and is a palindrome in every base, and for
$N \ge 1$ the number $N$ is written with the single digit $N$ in base $N + 1$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Section 1.

Formalized by `MetaMathlibExt.minPalindromicBase`, a definition declared in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#min-palindromic-base).

## Binomial form

A natural number $N$ has a base-$b$ representation in binomial form if
there are natural numbers $\alpha \ge 1$ and $k \ge 1$ such that the base-$b$ digits of $N$, from
the most significant to the least significant, are
$\alpha\binom{k}{k}, \alpha\binom{k}{k-1}, \dots, \alpha\binom{k}{0}$.

The one-digit case $k = 0$ is excluded as degenerate.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Section 1 (definition of binomial form).

Formalized by `MetaMathlibExt.HasBinomialForm`, a definition declared in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#has-binomial-form).

## The minimum palindromic base of two

The smallest base $b \ge 2$ in which the number $2$
is a palindrome is $b(2) = 3$: in base $2$ the number $2$ is written $(1, 0)_2$, which is not a
palindrome, while in base $3$ it is the one-digit palindrome $(2)_3$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Table 1.

Formalized by `MetaMathlibExt.minPalindromicBase_two`, a theorem declared in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#min-palindromic-base-two).

## The binomial form of 2023 in base 16

The number $2023$ has a base-$16$ representation in
binomial form: its base-$16$ digits are $7, 14, 7$, that is
$7\binom{2}{2}, 7\binom{2}{1}, 7\binom{2}{0}$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Section 1.

Formalized by `MetaMathlibExt.hasBinomialForm_16_2023`, a theorem declared in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#has-binomial-form-16-2023).

## Brown's theorem on minimal palindromic base one less than the number

Let $N \ge 1$ be a
natural number and let $b(N)$ be the smallest base $b \ge 2$ in which $N$ is a palindrome. If
$b(N) = N - 1$, then $N \in \{3, 4, 6\}$, or $N > 6$ and $N$ is prime.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 1, credited to K. Brown.

Stated but not proved: `MetaMathlibExt.minPalindromicBase_eq_pred` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#min-palindromic-base-eq-pred).

## Digits of a multiple of a power of one more than the base

Let $\alpha \ge 1$, $k$ and $b$
be natural numbers with $\alpha\binom{k}{\lceil k/2 \rceil} < b$. Then the base-$b$
representation of $\alpha(1 + b)^k$ has exactly the $k + 1$ digits
$\alpha\binom{k}{k}, \alpha\binom{k}{k-1}, \dots, \alpha\binom{k}{0}$, from the most significant
to the least significant.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Lemma 1.

Stated but not proved: `MetaMathlibExt.digits_mul_one_add_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#digits-mul-one-add-pow).

## Sufficient condition for a binomial form of a power of 2

Let $n$, $x$, $k$ and $r$ be
natural numbers with $k \ge 1$, $n = xk + r$ and $2^r\binom{k}{\lceil k/2 \rceil} < 2^x - 1$.
Then $2^n$ has a base-$(2^x - 1)$ representation in binomial form.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Corollary 1.

Stated but not proved: `MetaMathlibExt.hasBinomialForm_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#has-binomial-form-two-pow).

## Bases of binomial forms of powers of 2

Let $n$, $b \ge 2$, $\alpha \ge 1$ and $k \ge 1$
be natural numbers. If the base-$b$ digits of $2^n$, from the most significant to the least
significant, are $\alpha\binom{k}{k}, \alpha\binom{k}{k-1}, \dots, \alpha\binom{k}{0}$, then
$b = 2^x - 1$ for some natural number $x \le n$, and $\alpha = 2^i$ for some natural number $i$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Lemma 2.

Stated but not proved: `MetaMathlibExt.binomialForm_two_pow_base` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#binomial-form-two-pow-base).

## Even-length palindromes are divisible by the base plus one

Let $b \ge 2$ and let $N$ be a
natural number whose base-$b$ digits form a palindrome with an even number of digits. Then
$b + 1$ divides $N$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Lemma 3.

Stated but not proved: `MetaMathlibExt.succ_dvd_of_palindrome_even_length` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#succ-dvd-of-palindrome-even-length).

## Even-length palindromic powers of 2 have base one less than a power of 2

Let $n$ and
$b \ge 2$ be natural numbers. If the base-$b$ representation of $2^n$ is a palindrome with an
even number of digits, then $b = 2^x - 1$ for some natural number $x$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Corollary 2.

Stated but not proved: `MetaMathlibExt.base_eq_two_pow_sub_one_of_palindrome` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#base-eq-two-pow-sub-one-of-palindrome).

## Three-digit palindromic powers of two

Let $n$ be a natural number, let $b \ge 2$ be a
base, and let $c = 2^n \bmod b$. The base-$b$ representation of $2^n$ is a palindrome with exactly
three digits if and only if $b^2 + 1 \le 2^n \le b^3 - 1$, $c \ne 0$, and
$\frac{1}{b} \lfloor 2^n / b \rfloor - \frac{b - 1}{b} \le c \le
\frac{1}{b} \lfloor 2^n / b \rfloor$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 2.

Stated but not proved: `MetaMathlibExt.three_digit_palindrome_two_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#three-digit-palindrome-two-pow-iff).

## Three-digit binomial forms of powers of two

Let $n$ and $\alpha \ge 1$ be natural numbers
and let $b \ge 2$ be a base. The base-$b$ representation of $2^n$ is
$(\alpha, 2\alpha, \alpha)_b$ if and only if there is a natural number $i$ with $3i + 2 < n$,
$n \equiv i \pmod 2$, $\alpha = 2^i$ and $b = 2^{(n - i)/2} - 1$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 3.

Stated but not proved: `MetaMathlibExt.three_digit_binomialForm_two_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#three-digit-binomial-form-two-pow-iff).

## Three-digit representations of powers of two with outer digits one

Let $n$ be a natural
number and $b \ge 2$ a base. There is a digit $c \ne 2$ such that the base-$b$ representation of
$2^n$ is $(1, c, 1)_b$, that is, $2^n = 1 + cb + b^2$ with $0 \le c < b$, if and only if
(i) $2^n - 1 = kb$ for some natural number $k$ with $b \le k \le 2b - 1$, and (ii) it is not the
case that $n$ is even and $b = 2^{n/2} - 1$.

The excluded digit $c = 2$ gives the binomial form $(1, 2, 1)_b = (b + 1)^2$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 4.

Stated but not proved: `MetaMathlibExt.one_c_one_two_pow_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#one-c-one-two-pow-iff).

## Palindromic powers of two in a base one less than a power of two

Let $x \ge 2$ and
$n \ge 1$ be natural numbers, let $b = 2^x - 1$, and suppose that the base-$b$ representation
$2^n = (c_k, \dots, c_0)_b$ is a palindrome with $k + 1$ digits. Then (1) $n > k(x - 1)$; and
(2) if $n = kx + r$ for a natural number $r$, and either $k \le x - r$, or $3 \le k \le x - r + 1$
and $x \ge 3$, then $c_i = 2^r \binom{k}{i}$ for $i = 0, \dots, k$, that is, the representation
is the binomial form $2^r (\binom{k}{k}, \dots, \binom{k}{0})_b$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Lemma 4.

Stated but not proved: `MetaMathlibExt.palindrome_two_pow_base_two_pow_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#palindrome-two-pow-base-two-pow-sub-one).

## Powers of 2 have binomial forms in small bases

For every natural number $n \ge 2$ there
are natural numbers $y$ and $b$ with $y \le \lceil \sqrt{2n} \rceil + 1$ and $2 \le b \le 2^y - 1$
such that $2^n$ has a base-$b$ representation in binomial form.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 5.

Stated but not proved: `MetaMathlibExt.exists_small_base_binomialForm_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#exists-small-base-binomial-form-two-pow).

## Even-length palindromic prime powers have base one less than a power of the prime

Let
$p$ be a prime and let $n$ and $b \ge 2$ be natural numbers. If the base-$b$ representation of
$p^n$ is a palindrome with an even number of digits, then $b = p^x - 1$ for some natural number
$x$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 6.

Stated but not proved: `MetaMathlibExt.base_eq_prime_pow_sub_one_of_palindrome` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#base-eq-prime-pow-sub-one-of-palindrome).

## Digits of a power of the base and of its successor

Let $z \ge 2$ and $n$ be natural
numbers. Then the base-$z$ digits of $z^n$ are a $1$ followed by $n$ zeros, and, if $n \ge 1$,
the base-$z$ digits of $z^n + 1$ are a $1$, then $n - 1$ zeros, then a $1$.

Part (III) of the source theorem is omitted: as printed ($z^n - 1 = (1, 1, \dots, 1)_z$) it is
false for $z \ge 3$, for example $3^2 - 1 = 8 = (2, 2)_3$.

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 7, parts (I) and (II).

Stated but not proved: `MetaMathlibExt.digits_pow_and_pow_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#digits-pow-and-pow-add-one).

## The Nagell–Ljunggren equation in natural numbers (Bugeaud–Mihăilescu)

Let $x, y, n, q$
be natural numbers with $x \ge 2$, $y \ge 2$, $n \ge 3$ and $q \ge 2$ such that
$(x^n - 1)/(x - 1) = y^q$. If $q = 2$, or $3 \mid n$, or $4 \mid n$, or $q = 3$ and
$n \not\equiv 5 \pmod 6$, then $(x, y, n, q)$ is one of $(3, 11, 5, 2)$, $(7, 20, 4, 2)$ and
$(18, 7, 3, 3)$; these are $11^2 = (1,1,1,1,1)_3$, $20^2 = (1,1,1,1)_7$ and $7^3 = (1,1,1)_{18}$.

The ranges $x, y \ge 2$, $n \ge 3$, $q \ge 2$ are the standard ones for this equation (not
displayed in the paper).

## Sources

- D. L. Kreher and D. R. Stinson, *On Minimum-Base Palindromic Representations of Powers of 2*, INTEGERS 24 (2024), Article A69, Theorem 8, quoting Bugeaud and Mihăilescu.

Stated but not proved: `MetaMathlibExt.nagell_ljunggren_solutions` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/MinBasePalindromeWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html#nagell-ljunggren-solutions).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Palindromic representations of powers of two](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/repdigits-reverse-multiples/palindromic-representations-of-powers-of-two)
