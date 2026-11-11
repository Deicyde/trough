---
declaration: section
origin: cited
lean: MetaMathlibExt.realIntervalSet, MetaMathlibExt.card_realIntervalSet, MetaMathlibExt.realAPSet, MetaMathlibExt.card_realAPSet, MetaMathlibExt.IsMSTDSet, MetaMathlibExt.not_isMSTDSet_singleton, MetaMathlibExt.not_isMSTDSet_union_two_ap, MetaMathlibExt.not_isMSTDSet_intervalAP_nat_of_le_two_mul_sub_two
statement: formalized
---

# Unions of two progressions are not sum-dominant

33 results, 6 proved and 27 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html).

## Initial integer interval

For a natural number $n$, $I_n = \{0, 1, \ldots, n - 1\}$ is
the set of the first $n$ natural numbers, viewed as a finite set of real numbers; $I_0$ is empty.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Section 1.

Formalized by `MetaMathlibExt.realIntervalSet`, a definition declared in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#real-interval-set).

## Size of the interval $I_n$

For every natural number $n$, the set
$I_n = \{0, 1, \dots, n - 1\}$ of real numbers has exactly $n$ elements.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Section 1.

Formalized by `MetaMathlibExt.card_realIntervalSet`, a theorem declared in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#card-real-interval-set).

## Finite arithmetic progression

For a real number $x$, a natural number $m$ and a real
number $d$, $J(x, m, d)$ is the finite set of real numbers
$\{x + i d : i = 0, 1, \ldots, m\}$, that is, $x, x + d, \ldots, x + m d$.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Section 1.

Formalized by `MetaMathlibExt.realAPSet`, a definition declared in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#real-apset).

## Size of the progression $J(x, m, d)$

For a real number $x$, a natural number $m$ and a
real number $d \ne 0$, the progression $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$ has exactly
$m + 1$ elements.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Section 1.

Formalized by `MetaMathlibExt.card_realAPSet`, a theorem declared in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#card-real-apset).

## MSTD set

A finite set $A$ of real numbers is an *MSTD set* (more sums than differences)
when its difference set has fewer elements than its sumset: $|A - A| < |A + A|$, where
$A + A = \{a + b : a, b \in A\}$ and $A - A = \{a - b : a, b \in A\}$.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Section 1.

Formalized by `MetaMathlibExt.IsMSTDSet`, a definition declared in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#is-mstdset).

## A single point is not an MSTD set

For every real number $a$, the set $\{a\}$ is not an
MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Section 1.

Formalized by `MetaMathlibExt.not_isMSTDSet_singleton`, a theorem declared in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-singleton).

## The union of two separated arithmetic progressions is not an MSTD set

For real numbers
$x, d$ and a natural number $m$, write $J(x, m, d) = \{x + i d : i = 0, 1, \ldots, m\}$. Let
$a, b, d_1, d_2$ be real numbers with $d_1 > 0$ and $d_2 > 0$, and let $m_1, m_2$ be natural
numbers with $a + m_1 d_1 < b$, so that the largest element of $J(a, m_1, d_1)$ is less than the
smallest element of $J(b, m_2, d_2)$. Then $J(a, m_1, d_1) \cup J(b, m_2, d_2)$ is not an MSTD
set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Theorem 1.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_union_two_ap` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-union-two-ap).

## Interval plus integer progression starting in $(n + 1, 2n - 2)$ is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. For natural numbers $n \ge 3$, $m \ge 2$, $d \ge 2$ and $x$ with
$n + 1 \le x \le 2n - 2$, the set $I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 1.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_nat_of_le_two_mul_sub_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-nat-of-le-two).

## Interval plus integer progression starting at $2n - 1$ or later is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. For natural numbers $n \ge 3$, $m \ge 2$, $d \ge 2$ and $x \ge 2n - 1$, the set
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 2.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_nat_of_two_mul_sub_one_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-nat-of-two-mu).

## Interval plus integer progression starting after the interval is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. For natural numbers $n \ge 3$, $m \ge 2$, $d \ge 2$ and $x > n - 1$, the set
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 3.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_nat_of_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-nat-of-lt).

## Interval plus irrational-step progression with natural start is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. For natural numbers $n \ge 3$, $m \ge 2$ and $x \ge n + 1$, and a positive
irrational real number $d$, the set $I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 4.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_irrational_diff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-irrational-di).

## An interval and a later natural-start progression with few terms or large step are not MSTD

Let $n \ge 3$, $m$ and $x$ be natural numbers with $x \ge n + 1$, and let $d = s + p/q$, where
$s, p, q$ are natural numbers with $0 < p < q$ and $\gcd(p, q) = 1$. Suppose that either
$2 \le m \le q - 1$, or $m \ge q$ and $qd > n - 1$. Write $I_n = \{0, 1, \dots, n - 1\}$ and
$J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then $I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 5.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_rat_diff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-rat-diff).

## An interval and a later progression with natural start and small step are not MSTD

Let
$n \ge 3$, $m$ and $x$ be natural numbers with $x \ge n + 1$, and let $d = s + p/q$, where
$s, p, q$ are natural numbers with $0 < p < q$ and $\gcd(p, q) = 1$. Suppose that $m \ge q$ and
$qd \le n - 1$. Write $I_n = \{0, 1, \dots, n - 1\}$ and
$J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then $I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 6.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_rat_diff_of_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-rat-diff-of-l).

## Interval plus irrational-step progression avoiding the naturals is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. Let $n \ge 3$ and $m$ be natural numbers, $d$ a positive irrational real number
and $x > n - 1$ a real number such that none of $x + id$ for $i = 0, 1, \dots, m$ is a natural
number. Then $I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 7.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_irrational_of_forall_not_nat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-irrational-of).

## At most one nonnegative integer point on a progression with irrational difference

Let $x$
and $d$ be real numbers with $d$ irrational. If $i$ and $j$ are natural numbers such that $x + id$
and $x + jd$ are both nonnegative integers, then $i = j$.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 8.

Stated but not proved: `MetaMathlibExt.eq_of_add_mul_irrational_mem_nat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#eq-of-add-mul-irrational-mem-nat).

## Interval plus irrational-step progression meeting the naturals is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. Let $n \ge 3$ and $m$ be natural numbers, $d$ a positive irrational real number
and $x > n - 1$ a real number that is not a natural number, and suppose that $x + jd$ is a
natural number for some integer $j$ with $1 \le j \le m$. Then $I_n \cup J(x, m, d)$ is not
an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 9.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_irrational_of_exists_nat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-irrational-of-2).

## An interval and a later rational-step progression with no integer term are not MSTD

Let
$n \ge 3$ and $m$ be natural numbers, let $x > n - 1$ be a real number that is not a natural
number, and let $d = s + p/q$, where $s, p, q$ are natural numbers with $0 < p < q$ and
$\gcd(p, q) = 1$. Suppose that $x + id$ is not a natural number for any natural number $i \le m$,
and that either $2 \le m \le q - 1$, or $m \ge q$ and $qd > n - 1$. Write
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 10.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_real_rat_diff_of_forall_not_nat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-real-rat-diff).

## Uniqueness of a nonnegative integer point for a rational difference

Let $x$ be a real
number, let $s, p, q$ be natural numbers with $0 < p < q$ and $\gcd(p, q) = 1$, and let
$d = s + p/q$. If $i, j \in \{1, \dots, q - 1\}$ and $x + id$ and $x + jd$ are both nonnegative
integers, then $i = j$.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 11.

Stated but not proved: `MetaMathlibExt.eq_of_add_mul_rat_mem_nat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#eq-of-add-mul-rat-mem-nat).

## An interval and a later rational-step progression with an integer term are not MSTD

Let
$n \ge 3$ and $m$ be natural numbers, let $x > n - 1$ be a real number that is not a natural
number, and let $d = s + p/q$, where $s, p, q$ are natural numbers with $0 < p < q$ and
$\gcd(p, q) = 1$. Suppose that $x + jd$ is a natural number for some natural number $j$ with
$1 \le j \le q - 1$, and that either $2 \le m \le q - 1$, or $m \ge q$ and $qd > n - 1$. Write
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 12.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_real_rat_diff_of_exists_nat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-real-rat-diff-2).

## An interval and a later progression with non-integer start and small step are not MSTD

Let $n \ge 3$ and $m$ be natural numbers, let $x > n - 1$ be a real number that is not a natural
number, and let $d = s + p/q$, where $s, p, q$ are natural numbers with $0 < p < q$ and
$\gcd(p, q) = 1$. Suppose that $m \ge q$ and $qd \le n - 1$. Write
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 13.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_real_rat_diff_of_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-real-rat-diff-3).

## Interval plus integer progression starting inside the interval is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. For natural numbers $n \ge 3$, $m \ge 2$, $d \ge 2$ and $x \le n - 1$, the set
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 14.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_nat_of_le_sub_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-nat-of-le-sub).

## An interval and an overlapping progression with small integer step are not MSTD

Let
$n \ge 3$, $m \ge 2$ and $d$ be natural numbers with $2 \le d \le n - 1$, and let $x$ be a real
number with $0 < x < n - 1$ such that either $x$ is irrational or $x = s + p/q$ for natural
numbers $s, p, q$ with $0 < p < q$, $q \ne 2$ and $\gcd(p, q) = 1$. Write
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 15.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_overlap_of_den_ne_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-overlap-of-de).

## Interval plus integer-step progression with half-integer start is not MSTD

Let
$I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. Let $n \ge 3$, $m \ge 2$, $s$ and $d$ be natural numbers with
$2 \le d \le n - 1$, and let $x = s + 1/2$. If $x < n - 1$, then $I_n \cup J(x, m, d)$ is not an
MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 16.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_overlap_half` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-overlap-half).

## Interval plus progression with non-integer start and integer step at least $n$ is not MSTD

Let $n \ge 3$, $m \ge 2$ and $d \ge n$ be natural numbers, and let $x$ be a real number with
$0 < x < n - 1$ that is not a natural number. Write $I_n = \{0, 1, \dots, n - 1\}$ and
$J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then $I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 17.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_overlap_large_diff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-overlap-large).

## An interval and an overlapping progression with incompatible start and step are not MSTD

Let $n \ge 3$ and $m \ge 2$ be natural numbers, and let $x$ and $d$ be real numbers with
$0 < x < n - 1$. Write $I_n = \{0, 1, \dots, n - 1\}$ and
$J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Suppose that one of the following holds:
(i) $x$ is irrational, and $d$ is rational but not a positive integer; (ii) $x$ is rational but
not a natural number, and $d$ is irrational; (iii) there are natural numbers
$s_1, s_2, p_1, p_2, q_1, q_2$ with $p_1 > 0$, $p_2 > 0$,
$\gcd(p_1, q_1) = \gcd(p_2, q_2) = \gcd(q_1, q_2) = 1$ and $q_1 \ge 3$ such that
$x = s_1 + p_1/q_1$ and $d = s_2 + p_2/q_2$, and $d$ is not a natural number. Then
$I_n \cup J(x, m, d)$ is not an MSTD set. Here the natural numbers include $0$.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 19.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_overlap_of_coprime_den` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-overlap-of-co).

## Uniqueness of integer points when the denominators share a factor

Let
$s_1, s_2, p_1, p_2, q_1, q_2$ be natural numbers with $p_1, p_2 > 0$, $\gcd(p_1, q_1) = 1$,
$\gcd(p_2, q_2) = 1$ and $\gcd(q_1, q_2) > 1$, and let $x = s_1 + p_1/q_1$ and
$d = s_2 + p_2/q_2$. For indices $i, i', j, j' \in \{1, \dots, q_2 - 1\}$: if $x + id$ and
$x + i'd$ are both nonnegative integers then $i = i'$; if $2x + jd$ and $2x + j'd$ are both
nonnegative integers then $j = j'$; and if $x + id$ and $2x + jd$ are both nonnegative integers
then $i \ne j$.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 20.

Stated but not proved: `MetaMathlibExt.add_mul_mem_nat_unique_of_one_lt_gcd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#add-mul-mem-nat-unique-of-one-lt-gcd).

## An interval and an overlapping progression whose denominators share a factor are not MSTD

Let $n \ge 3$ and $m \ge 2$ be natural numbers, and let $s_1, s_2, p_1, p_2, q_1, q_2$ be natural
numbers with $p_1 > 0$, $p_2 > 0$, $\gcd(p_1, q_1) = \gcd(p_2, q_2) = 1$ and $\gcd(q_1, q_2) > 1$.
Let $x = s_1 + p_1/q_1$ and $d = s_2 + p_2/q_2$, where a fraction with denominator $0$ is read as
$0$, and suppose that $x < n - 1 < d$. Write $I_n = \{0, 1, \dots, n - 1\}$ and
$J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$. Then $I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 21.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_overlap_of_one_lt_gcd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-overlap-of-on).

## No integer points for a half-integer start and an odd denominator

Let $s_1, s_2, p_2, q_2$
be natural numbers with $q_2$ odd, and let $x = s_1 + 1/2$ and $d = s_2 + p_2/q_2$. Then
$x + id$ is not a nonnegative integer for any natural number $i$.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 22.

Stated but not proved: `MetaMathlibExt.add_mul_not_mem_nat_of_half` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 358](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L358). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#add-mul-not-mem-nat-of-half).

## Interval plus progression with half-integer start and odd-denominator step is not MSTD

Let $I_n = \{0, 1, \dots, n - 1\}$ and $J(x, m, d) = \{x + id : i = 0, 1, \dots, m\}$, as finite
sets of reals. Let $n \ge 3$, $m \ge 2$, $s_1$, $s_2$ and $p_2$ be natural numbers and $q_2$ an
odd natural number, and let $x = s_1 + 1/2$ and $d = s_2 + p_2/q_2$. If $x < n - 1 < d$, then
$I_n \cup J(x, m, d)$ is not an MSTD set.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 23.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_intervalAP_overlap_half_odd_den` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-interval-ap-overlap-half-2).

## Two overlapping progressions with rational ratios, outside two open cases, are not MSTD

For real numbers $x, d$ and a natural number $m$, write
$J(x, m, d) = \{x + id : i = 0, 1, \ldots, m\}$. Let $x_1, x_2, d_1, d_2$ be real numbers with
$d_1 > 0$, let $m_1, m_2$ be natural numbers with $x_2 < x_1 + m_1 d_1$, and let
$s_1, s_2, p_1, p_2, q_1, q_2$ be natural numbers with $p_1, p_2, q_1, q_2 > 0$,
$\gcd(p_1, q_1) = \gcd(p_2, q_2) = 1$, $(x_2 - x_1)/d_1 = s_1 + p_1/q_1$ and
$d_2/d_1 = s_2 + p_2/q_2$. Suppose that neither of the following holds: (i) $\gcd(q_1, q_2) > 1$
and $0 < d_2 < (m_1 - 1) d_1$; (ii) $q_1 = 2$, $\gcd(2, q_2) = 1$ and $0 < d_2 < (m_1 - 1) d_1$.
Then $J(x_1, m_1, d_1) \cup J(x_2, m_2, d_2)$ is not an MSTD set.

Since $d_1 > 0$ and $d_2/d_1 = s_2 + p_2/q_2 > 0$, also $d_2 > 0$, so the condition
$x_2 < x_1 + m_1 d_1$ says that the smallest element of $J(x_2, m_2, d_2)$ is less than the largest
element of $J(x_1, m_1, d_1)$. Cases (i) and (ii) are the two cases the source leaves open.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Theorem 2.

Stated but not proved: `MetaMathlibExt.not_isMSTDSet_union_two_ap_overlap` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#not-is-mstdset-union-two-ap-overlap).

## No nonnegative integer points for an irrational start and a rational difference

Let
$x$ be an irrational real number and $d$ a rational number. Then for all natural numbers $i$ and
$j$, neither $x + id$ nor $2x + jd$ is a nonnegative integer.

The paper assumes $d \in \mathbb{Q} \setminus \mathbb{N}$; the claim holds for every rational $d$,
so that restriction is not stated.

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 18.

Stated but not proved: `MetaMathlibExt.add_mul_not_mem_nat_of_irrational_of_rat` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#add-mul-not-mem-nat-of-irrational-of-rat).

## Nonnegative integer points for a rational start and an irrational difference

Let $x$ be
a rational number that is not a nonnegative integer, and let $d$ be an irrational real number.
Then $x + id$ is not a nonnegative integer for any natural number $i$, and $2x + jd$ is not a
nonnegative integer for any natural number $j \ge 1$.

As printed, the paper's Lemma 18 (ii) also claims $2x + 0 \cdot d \notin \mathbb{N}$, which fails
at $x = 1/2$ (where $2x = 1$); the paper's proof ("then $d \in \mathbb{Q}$") covers only $j \ge 1$,
and the condition that the denominator of $x$ be at least $3$ is attached only to part (iii).

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 18.

Stated but not proved: `MetaMathlibExt.add_mul_not_mem_nat_of_rat_of_irrational` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#add-mul-not-mem-nat-of-rat-of-irrational).

## No integer points for coprime denominators, the first at least 3

Let
$s_1, s_2, p_1, p_2, q_1, q_2$ be natural numbers with $\gcd(p_1, q_1) = 1$, $\gcd(q_1, q_2) = 1$
and $q_1 \ge 3$, and let $x = s_1 + p_1/q_1$ and $d = s_2 + p_2/q_2$. Then for all natural numbers
$i$ and $j$, neither $x + id$ nor $2x + jd$ is a nonnegative integer.

The paper's further hypotheses ($p_1, p_2, q_2 > 0$, $\gcd(p_2, q_2) = 1$, $d \notin \mathbb{N}$)
are not needed and are not stated ($p_1 > 0$ and $q_2 > 0$ already follow from the two coprimality
conditions and $q_1 \ge 3$).

## Sources

- Manish Kumar, Mohan, and Ram Krishna Pandey, *The Union of Two Arithmetic Progressions with Different Common Differences Is Not an MSTD Set*, INTEGERS 26 (2026), Article A58, Lemma 18.

Stated but not proved: `MetaMathlibExt.add_mul_not_mem_nat_of_coprime_den` is written with `theorem_wanted` in [WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean, line 428](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Additive/UnionTwoAPNotMSTDWanted.lean#L428). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html#add-mul-not-mem-nat-of-coprime-den).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unions of two progressions are not sum-dominant](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/more-sums-than-differences/unions-of-two-progressions-are-not-sum-dominant)
