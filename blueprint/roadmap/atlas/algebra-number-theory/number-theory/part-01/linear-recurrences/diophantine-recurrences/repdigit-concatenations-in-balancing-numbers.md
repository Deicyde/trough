---
declaration: section
origin: cited
lean: MetaMathlibExt.balancingNum, MetaMathlibExt.balancingNum_two, MetaMathlibExt.balancingNum_three, MetaMathlibExt.lucasBalancingNum, MetaMathlibExt.lucasBalancingNum_two, MetaMathlibExt.lucasBalancingNum_three, MetaMathlibExt.IsRepdigit, MetaMathlibExt.isRepdigit_eleven
statement: formalized
---

# Repdigit concatenations in balancing numbers

21 results, 15 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html).

## Balancing numbers

The balancing numbers are the integers $B_n$ for $n \in \mathbb{N}$
defined by $B_0 = 0$, $B_1 = 1$ and $B_{n+2} = 6 B_{n+1} - B_n$ for all $n$.

## Sources

- standard definition used in "Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits" (Integers 2025, A15); the values `B_2 = 6`, `B_3 = 35` are those displayed in its Theorem 2.

Formalized by `MetaMathlibExt.balancingNum`, a definition declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#balancing-num).

## The balancing number $B_2$ is $6$

The balancing number $B_2$ equals $6$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 2.

Formalized by `MetaMathlibExt.balancingNum_two`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#balancing-num-two).

## The balancing number $B_3$ is $35$

The balancing number $B_3$ equals $35$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 2.

Formalized by `MetaMathlibExt.balancingNum_three`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#balancing-num-three).

## Lucas-balancing numbers (shifted indexing)

The sequence of integers $(C_n)_{n \ge 0}$
defined by $C_0 = 3$, $C_1 = 1$ and $C_{n+2} = 6 C_{n+1} - C_n$ for all $n \ge 0$.

This is the indexing of Mohapatra, Bhoi and Panda, forced by the values $C_2 = 3$ and
$C_3 = 17$ displayed in their Theorem 3: for $n \ge 1$, $C_n$ is the usual Lucas-balancing
number $c_{n-1}$, where $c_0 = 1$, $c_1 = 3$ and $c_{n+2} = 6 c_{n+1} - c_n$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 3.

Formalized by `MetaMathlibExt.lucasBalancingNum`, a definition declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#lucas-balancing-num).

## The Lucas-balancing number $C_2$ is $3$

For the Lucas-balancing numbers defined by
$C_0 = 3$, $C_1 = 1$ and $C_{n+2} = 6C_{n+1} - C_n$, we have $C_2 = 3$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 3.

Formalized by `MetaMathlibExt.lucasBalancingNum_two`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#lucas-balancing-num-two).

## The Lucas-balancing number $C_3$ is $17$

For the Lucas-balancing numbers defined by
$C_0 = 3$, $C_1 = 1$ and $C_{n+2} = 6C_{n+1} - C_n$, we have $C_3 = 17$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 3.

Formalized by `MetaMathlibExt.lucasBalancingNum_three`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#lucas-balancing-num-three).

## Decimal repdigits

A natural number $n$ is a repdigit if there are natural numbers $d$
and $m$ with $1 \le d \le 9$ and $m \ge 1$ such that $9n = d(10^m - 1)$. Equivalently, $n$ is
the positive integer whose decimal expansion consists of $m$ copies of the digit $d$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Section 1 (definition of repdigit).

Formalized by `MetaMathlibExt.IsRepdigit`, a definition declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-repdigit).

## Eleven is a repdigit

The number $11$ is a repdigit.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 2.

Formalized by `MetaMathlibExt.isRepdigit_eleven`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-repdigit-eleven).

## Nonzero single digits are repdigits

Every natural number $d$ with $1 \le d \le 9$ is a
repdigit.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Section 1 (definition of repdigit).

Formalized by `MetaMathlibExt.isRepdigit_of_le`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-repdigit-of-le).

## Concatenations of two decimal repdigits

A natural number $n$ is a concatenation of two
repdigits if there are digits $d_1, d_2$ with $1 \le d_1 \le 9$, $0 \le d_2 \le 9$ and
$d_1 \ne d_2$, and block lengths $m_1, m_2 \ge 1$, such that the decimal expansion of $n$ is
$m_1$ copies of $d_1$ followed by $m_2$ copies of $d_2$; that is,
$9n = d_1 (10^{m_1} - 1) 10^{m_2} + d_2 (10^{m_2} - 1)$. Equivalently, the decimal expansion of
$n$ has exactly two runs of equal digits.

Because of the condition $d_1 \ne d_2$, a repdigit such as $99$ is not a concatenation of two
repdigits.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemmas 3 and 5.

Formalized by `MetaMathlibExt.IsConcatTwoRepdigits`, a definition declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-concat-two-repdigits).

## Concatenations of three decimal repdigits

A natural number $n$ is a concatenation of
three repdigits if there are digits $d_1, d_2, d_3$ with $1 \le d_1 \le 9$, $0 \le d_2 \le 9$,
$0 \le d_3 \le 9$, $d_1 \ne d_2$ and $d_2 \ne d_3$, and block lengths $m_1, m_2, m_3 \ge 1$, such
that the decimal expansion of $n$ is $m_1$ copies of $d_1$, then $m_2$ copies of $d_2$, then $m_3$
copies of $d_3$; that is,

$$9n = d_1 (10^{m_1} - 1) 10^{m_2 + m_3} + d_2 (10^{m_2} - 1) 10^{m_3} + d_3 (10^{m_3} - 1).$$

Equivalently, the decimal expansion of $n$ has exactly three runs of equal digits.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemmas 4 and 6.

Formalized by `MetaMathlibExt.IsConcatThreeRepdigits`, a definition declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-concat-three-repdigits).

## $35$ is a concatenation of two repdigits

The number $35$, whose decimal expansion consists
of the one-digit blocks $3$ and $5$, is a concatenation of two repdigits.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemma 3.

Formalized by `MetaMathlibExt.isConcatTwoRepdigits_thirtyFive`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-concat-two-repdigits-thirty-five).

## $204$ is a concatenation of three repdigits

The number $204$, whose decimal expansion
consists of the one-digit blocks $2$, $0$ and $4$, is a concatenation of three repdigits.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemma 4.

Formalized by `MetaMathlibExt.isConcatThreeRepdigits_twoZeroFour`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-concat-three-repdigits-two-zero-four).

## Differences of two repdigits

A natural number $n$ is a difference of two repdigits if
there are repdigits $a$ and $b$ with $a = n + b$, that is, $n = a - b$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorems 2 and 3.

Formalized by `MetaMathlibExt.IsRepdigitDiff`, a definition declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-repdigit-diff).

## Six is a difference of two repdigits

The number $6$ is a difference of two repdigits:
$6 = 11 - 5$, where $11$ and $5$ are repdigits.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 2.

Formalized by `MetaMathlibExt.isRepdigitDiff_six`, a theorem declared in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#is-repdigit-diff-six).

## Balancing numbers that are concatenations of two repdigits

For every natural number $k$,
if the balancing number $B_k$ is a concatenation of two repdigits, then $B_k = 35$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemma 3.

Stated but not proved: `MetaMathlibExt.balancingNum_concatTwoRepdigits` is written with `theorem_wanted` in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#balancing-num-concat-two-repdigits).

## Balancing numbers that are concatenations of three repdigits

For every natural number
$k$, if the balancing number $B_k$ is a concatenation of three repdigits, then $B_k = 204$ or
$B_k = 1189$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemma 4.

Stated but not proved: `MetaMathlibExt.balancingNum_concatThreeRepdigits` is written with `theorem_wanted` in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#balancing-num-concat-three-repdigits).

## Lucas-balancing numbers that are concatenations of two repdigits

For every natural
number $k$, if the decimal expansion of the Lucas-balancing number $C_k$ consists of exactly two
runs of equal digits, that is, $C_k$ is a block of one repeated digit followed by a block of a
different repeated digit, then $C_k = 17$ or $C_k = 577$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemma 5.

Stated but not proved: `MetaMathlibExt.lucasBalancingNum_concatTwoRepdigits` is written with `theorem_wanted` in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#lucas-balancing-num-concat-two-repdigits).

## Lucas-balancing numbers that are concatenations of three repdigits

For every natural
number $k$, if the decimal expansion of the Lucas-balancing number $C_k$ consists of exactly
three runs of equal digits, that is, $C_k$ is three blocks of repeated digits in which adjacent
blocks have different digits, then $C_k = 3363$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Lemma 6.

Stated but not proved: `MetaMathlibExt.lucasBalancingNum_concatThreeRepdigits` is written with `theorem_wanted` in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#lucas-balancing-num-concat-three-repdigi).

## Balancing numbers that are differences of two repdigits

Let $k \ge 2$ be a natural
number. If the balancing number $B_k$ is a difference of two repdigits, then $B_k = 6$ or
$B_k = 35$.

The hypothesis $k \ge 2$ excludes $B_0 = 0 = 1 - 1$ and $B_1 = 1 = 2 - 1$, which are also
differences of two repdigits.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 2.

Stated but not proved: `MetaMathlibExt.balancingNum_repdigitDiff` is written with `theorem_wanted` in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#balancing-num-repdigit-diff).

## Lucas-balancing numbers that are differences of two repdigits

For every natural
number $k \ge 2$, if the Lucas-balancing number $C_k$ is a difference of two repdigits, then
$C_k = 3$ or $C_k = 17$.

Both values occur: $C_2 = 3 = 11 - 8$ and $C_3 = 17 = 22 - 5$. The hypothesis $k \ge 2$ excludes
$C_1 = 1 = 2 - 1$.

## Sources

- Mohapatra, Bhoi and Panda, *Balancing and Lucas-Balancing Numbers as the Difference of Two Repdigits*, INTEGERS 25 (2025), Article A15, Theorem 3.

Stated but not proved: `MetaMathlibExt.lucasBalancingNum_repdigitDiff` is written with `theorem_wanted` in [WantedExt/NumberTheory/BalancingRepdigitWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/BalancingRepdigitWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html#lucas-balancing-num-repdigit-diff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Repdigit concatenations in balancing numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-concatenations-in-balancing-numbers)
