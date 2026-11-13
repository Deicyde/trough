---
declaration: section
origin: cited
lean: MetaMathlibExt.restrictedCombinations, MetaMathlibExt.restrictedCombinationCount, MetaMathlibExt.restrictedCombinationTotal, MetaMathlibExt.restrictedCombinationCount_empty, MetaMathlibExt.restrictedCombinationTotal_singleton_one_four, MetaMathlibExt.restrictedCombinationCount_one_q_eq_card_windowedAdjacentSwapPerms, MetaMathlibExt.restrictedCombinationTotal_one_four_genFun, MetaMathlibExt.restrictedCombinationTotal_one_five_genFun
statement: formalized
---

# Combinations without specified separations

35 results, 21 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html).

## Restricted combinations

For a finite set $Q$ of natural numbers and $n, k \ge 0$, the
restricted combinations are the $k$-element subsets $s$ of $\{1, \dots, n\}$ such that
$b - a \notin Q$ for all $a, b \in s$ with $a < b$. Since only distinct elements are compared,
whether $0 \in Q$ makes no difference.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedCombinations`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combinations).

## Number of restricted combinations

For a finite set $Q$ of natural numbers and natural
numbers $n$ and $k$, $S^Q_{n,k}$ is the number of $k$-subsets of $\{1, \dots, n\}$ in which no
two distinct elements differ by an element of $Q$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedCombinationCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-count).

## Number of subsets avoiding a set of differences

For a finite set $Q$ of natural numbers
and $n \ge 0$, $S^Q_n$ is the number of subsets of $\{1, \dots, n\}$ in which no two distinct
elements differ by an element of $Q$. That is, $S^Q_n = \sum_{k=0}^{n} S^Q_{n,k}$, where
$S^Q_{n,k}$ is the number of such subsets with $k$ elements.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedCombinationTotal`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-total).

## Restricted combinations with no forbidden differences

For all natural numbers $n$ and
$k$, the number $S^{\emptyset}_{n,k}$ of $k$-subsets of $\{1, \dots, n\}$ in which no two
elements differ by an element of the empty set is the binomial coefficient $\binom{n}{k}$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedCombinationCount_empty`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-count-empty).

## Subsets of $\{1, 2, 3, 4\}$ with no two consecutive elements

There are exactly $8$
subsets of $\{1, 2, 3, 4\}$ in which no two elements differ by $1$.

This is the case $n = 4$ of the identity $S^{\{1\}}_n = F_{n+2}$, where $S^{\{1\}}_n$ is the
number of subsets of $\{1, \dots, n\}$ in which no two elements differ by $1$ and $F_m$ is the
$m$-th Fibonacci number ($F_1 = F_2 = 1$): $F_6 = 8$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1 (`S^{1}_n = F_{n+2}`).

Formalized by `MetaMathlibExt.restrictedCombinationTotal_singleton_one_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-total-singleton-o).

## Forbidden differences 1 and q and windowed adjacent-swap permutations

For all natural
numbers $q$, $n$ and $k$, the number of $k$-subsets of $\{1, \dots, n\}$ in which no two
distinct elements differ by $1$ or by $q$ equals the number of permutations $\pi$ of
$\{0, 1, \dots, n\}$ such that $|\pi(i) - i| \le 1$ for every $i$; for every $i_0 \ge 0$ with
$i_0 + q \le n + 1$, all $i, j$ with $i_0 \le i, j < i_0 + q$ satisfy
$\pi(i) \le \pi(j) + q$ (every window of $q$ consecutive values has maximum minus minimum
at most $q$); and $\pi$ has exactly $k$ excedances (points $i$ with $\pi(i) > i$).

The paper takes $q \ge 2$; for $q \le 1$ the statement reduces to the case $Q = \{1\}$. The
condition $|\pi(i) - i| \le 1$ cannot be dropped: for $q = n = 2$ all $6$ permutations of
$\{0, 1, 2\}$ satisfy the window condition, while only $3$ subsets of $\{1, 2\}$ have no two
elements differing by $1$ or $2$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Theorem 8.

Stated but not proved: `MetaMathlibExt.restrictedCombinationCount_one_q_eq_card_windowedAdjacentSwapPerms` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-count-one-q-eq-ca).

## Generating function for subsets avoiding differences 1 and 4

Let $S^{\{1,4\}}_n$ be the
number of subsets of $\{1, \dots, n\}$ in which no two elements differ by $1$ or by $4$. Then,
in the ring $\mathbb{Z}[[x]]$ of formal power series,

$$\Bigl(\sum_{n \ge 0} S^{\{1,4\}}_n x^n\Bigr)(1 - x - x^3 + x^4 - 2x^5 + x^6 - x^7) =
1 + x + x^2 + x^3 + 2x^4 + x^6.$$

This is the paper's formula for $\sum_{n \ge 0} S^{\{1,4\}}_n x^n$ as a quotient of the two
polynomials, with the denominator cleared.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Proposition 9.

Stated but not proved: `MetaMathlibExt.restrictedCombinationTotal_one_four_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-total-one-four-ge).

## Generating function for subsets avoiding differences 1 and 5

Let $S^{\{1,5\}}_n$ be the
number of subsets of $\{1, \dots, n\}$ in which no two elements differ by $1$ or by $5$. Then,
in the ring $\mathbb{Z}[[x]]$ of formal power series,

$$\Bigl(\sum_{n \ge 0} S^{\{1,5\}}_n x^n\Bigr)
(1 - x^2 - x^3 - x^4 + x^5 - x^6 - x^7 - x^8 - x^{10}) =
1 + 2x + 2x^2 + 2x^3 + 2x^4 + 4x^5 + 3x^6 + 2x^7 + x^8 + x^9.$$

This is the paper's formula for $\sum_{n \ge 0} S^{\{1,5\}}_n x^n$ as a quotient of the two
polynomials, with the denominator cleared.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Proposition 10.

Stated but not proved: `MetaMathlibExt.restrictedCombinationTotal_one_five_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-total-one-five-ge).

## Generating function for subsets avoiding differences 1 and 6

Let $S^{\{1,6\}}_n$ be the
number of subsets of $\{1, \dots, n\}$ in which no two elements differ by $1$ or by $6$. Then,
in the ring $\mathbb{Z}[[x]]$ of formal power series,

$$\Bigl(\sum_{n \ge 0} S^{\{1,6\}}_n x^n\Bigr)
(1 - x - x^4 - x^5 + 2x^6 - 4x^7 + 2x^8 - 2x^{10} + 2x^{11} - 4x^{12} + 3x^{13} - x^{14} +
2x^{16} - x^{17} + x^{18}) =
1 + x + x^2 + 2x^3 + 2x^4 + 2x^5 + 5x^6 + 3x^8 + 2x^9 - x^{10} + x^{11} - 4x^{12} - x^{13} -
2x^{14} - 2x^{15} - x^{17}.$$

This is the paper's formula for $\sum_{n \ge 0} S^{\{1,6\}}_n x^n$ as a quotient of a polynomial
of degree $17$ by a polynomial of degree $18$, with the denominator cleared.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Proposition 11.

Stated but not proved: `MetaMathlibExt.restrictedCombinationTotal_one_six_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-total-one-six-gen).

## Forbidden differences m, 2m, …, jm and strongly restricted permutations

For natural
numbers $m \ge 1$, $j \ge 1$, $n$ and $k$, the number of $k$-subsets of $\{1, \dots, n\}$ in
which no two elements differ by an element of $\{m, 2m, \dots, jm\}$ equals the number of
permutations $\pi$ of $\{0, 1, \dots, n + jm - 1\}$ such that $\pi(i) - i \in \{-m, 0, jm\}$ for
every $i$ and $\pi$ has exactly $k$ excedances (points $i$ with $\pi(i) > i$).

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Theorem 13.

Stated but not proved: `MetaMathlibExt.restrictedCombinationCount_multiples_eq_card_strongPerms` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-count-multiples-e).

## The $(1,t)$-bonacci polynomials

Fix a natural number $s$ and put $t = s + 1$. The
$(1,t)$-bonacci polynomials $f^{(t)}_n(x)$, $n \ge 0$, are the polynomials with natural-number
coefficients defined by $f^{(t)}_0(x) = 1$ and, for every $n \ge 0$,
$f^{(t)}_{n+1}(x) = f^{(t)}_n(x) + x \, f^{(t)}_{n-s}(x)$ if $s \le n$ and
$f^{(t)}_{n+1}(x) = f^{(t)}_n(x)$ if $n < s$.

Equivalently, $f^{(t)}_n(x) = f^{(t)}_{n-1}(x) + x \, f^{(t)}_{n-t}(x) + \delta_{n,0}$ with
$f^{(t)}_n(x) = 0$ for $n < 0$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 3.2.

Formalized by `MetaMathlibExt.oneTBonacciPolynomial`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#one-tbonacci-polynomial).

## Initial value of the $(1,t)$-bonacci polynomials

For every natural number $s$, the
$(1,s+1)$-bonacci polynomial of index $0$ is $f^{(s+1)}_0(x) = 1$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 3.2.

Formalized by `MetaMathlibExt.oneTBonacciPolynomial_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#one-tbonacci-polynomial-zero).

## Recurrence for the $(1,t)$-bonacci polynomials

For all natural numbers $s$ and $n$ with
$s \le n$, the $(1,s+1)$-bonacci polynomials $f^{(s+1)}_m(x)$, $m \ge 0$, satisfy
$f^{(s+1)}_{n+1}(x) = f^{(s+1)}_n(x) + x \, f^{(s+1)}_{n-s}(x)$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 3.2.

Formalized by `MetaMathlibExt.oneTBonacciPolynomial_succ_of_le`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#one-tbonacci-polynomial-succ-of-le).

## The $(1,t)$-bonacci polynomials below the recurrence range

For all natural numbers $s$
and $n$ with $n < s$, the $(1,s+1)$-bonacci polynomials $f^{(s+1)}_m(x)$, $m \ge 0$, satisfy
$f^{(s+1)}_{n+1}(x) = f^{(s+1)}_n(x)$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 3.2.

Formalized by `MetaMathlibExt.oneTBonacciPolynomial_succ_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#one-tbonacci-polynomial-succ-of-lt).

## Counting strongly restricted permutations with displacements $-m$, $0$, $jm$

Let
$m, j, i, r$ be natural numbers with $j \ge 1$ and $r < m$, and let $F_j$ be the Fibonacci
$j$-numbers: $F_j(0) = 0$, $F_j(n) = 1$ for $1 \le n \le j$, and
$F_j(n) = F_j(n-1) + F_j(n-j-1)$ for $n > j$. Then the number of permutations $\pi$ of
$\{0, 1, \dots, im + r - 1\}$ such that $\pi(x) - x \in \{-m, 0, jm\}$ for every $x$ equals
$F_j(i+1)^{m-r} \, F_j(i+2)^r$.

In the paper's notation this is
$P^{\{-m,0,jm\}}_{im+r} = (f^{(j+1)}_i)^{m-r} (f^{(j+1)}_{i+1})^r$, where the
$(1,t)$-bonacci numbers $f^{(t)}_n$ satisfy $f^{(j+1)}_n = F_j(n+1)$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Corollary 14.

Stated but not proved: `MetaMathlibExt.card_strongPerms_multiples_eq_fibonacciP` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#card-strong-perms-multiples-eq-fibonacci).

## Excedances of strongly restricted permutations with displacements $-m$, $0$, $jm$

Let
$m, j, i, r, k$ be natural numbers with $j \ge 1$ and $r < m$, and let $f_n(x)$ be the
$(1, j+1)$-bonacci polynomials with natural-number coefficients: $f_0(x) = 1$, and
$f_{n+1}(x) = f_n(x) + x f_{n-j}(x)$ if $n \ge j$, $f_{n+1}(x) = f_n(x)$ if $n < j$. Then the
number of permutations $\pi$ of $\{0, 1, \dots, im + r - 1\}$ with $\pi(a) - a \in \{-m, 0, jm\}$
for every $a$ and with exactly $k$ excedances (points $a$ with $\pi(a) > a$) equals the
coefficient of $x^k$ in $f_i(x)^{m-r} f_{i+1}(x)^r$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Corollary 14.

Stated but not proved: `MetaMathlibExt.card_strongPerms_multiples_excedance_eq_coeff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#card-strong-perms-multiples-excedance-eq).

## Combinations avoiding an interval of differences with one value removed

Let $p$, $q$
and $n$ be natural numbers with $p < q < 2p$, let $Q = \{1, \dots, q\} \setminus \{p\}$, and let
$S^Q_n$ be the number of subsets of $\{1, \dots, n\}$ in which no two elements differ by an
element of $Q$. Then $S^Q_n$ is the number of compositions of $n + q$ in which every part is
either $1$ or of the form $q + 1 + jp$ for some integer $j \ge 0$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Theorem 19.

Stated but not proved: `MetaMathlibExt.restrictedCombinationTotal_Icc_erase_eq_card_compositions` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-total-icc-erase-e).

## Well-based sets

A finite set $Q$ of natural numbers is well based (Kitaev;
Valyuzhenich) if for every $x \in Q$ and every natural number $a$ with $0 < a < x$, at least one
of $a$ and $x - a$ lies in $Q$.

The empty set is well based, as in the paper's equivalent formulation. For a nonempty set $Q$
of positive integers the condition forces $1 \in Q$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 5.1.

Formalized by `MetaMathlibExt.IsWellBased`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#is-well-based).

## The set $\{1, \dots, q\}$ is well based

For every natural number $q$, the set
$\{1, 2, \dots, q\}$ is well based.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 5.1.

Formalized by `MetaMathlibExt.isWellBased_Icc`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#is-well-based-icc).

## The set $\{1, 3, 4\}$ is not well based

The set $\{1, 3, 4\}$ is not well based: in
$4 = 2 + 2$ neither part lies in the set.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 5.1.

Formalized by `MetaMathlibExt.not_isWellBased_one_three_four`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#not-is-well-based-one-three-four).

## Shift set of a binary subword

For natural numbers $\omega$ and $l$, the shift set of
$\omega$ with length $l$ is the set of $j \in \{1, \dots, l - 1\}$ with
$\lfloor \omega / 2^j \rfloor \ne \omega \bmod 2^{l-j}$. When $\omega < 2^l$ is read as a binary
word of length $l$, this says that the leftmost $l - j$ bits of $\omega$ differ from its rightmost
$l - j$ bits.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Theorem 21.

Formalized by `MetaMathlibExt.subwordShiftSet`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#subword-shift-set).

## Shift set of the subword 1010

The shift set of the binary subword $1010$ of length $4$
(the number $10$) is $\{1, 3\}$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 5.1 (OEIS list after Theorem 21).

Formalized by `MetaMathlibExt.subwordShiftSet_1010`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#subword-shift-set-1010).

## Subword shift sets are well based

Let $l$ be a natural number and $\omega$ a binary word
of length $l$, read as a natural number $\omega < 2^l$. Then the set $Q$ of those
$j \in \{1, \dots, l-1\}$ for which the leftmost $l - j$ bits of $\omega$ differ from its
rightmost $l - j$ bits, that is $\lfloor \omega / 2^j \rfloor \ne \omega \bmod 2^{l-j}$, is well
based.

This is the well-based part of Theorem 22 of the paper. Its further claim, that no integer
linear combination of the elements $p_i$ of $\{1, \dots, q\} \setminus Q$ lies in $Q$ (with $q$
the largest element of $Q$), is omitted: for $\omega = 010100101$ and $l = 9$ one gets
$Q = \{1, 2, 3, 4, 6, 8\}$, $q = 8$, $p_1 = 5$, $p_2 = 7$, and $p_2 - p_1 = 2 \in Q$. The side
condition $q = l - 1$ of Theorem 21 is not needed.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Theorem 22.

Stated but not proved: `MetaMathlibExt.isWellBased_subwordShiftSet` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#is-well-based-subword-shift-set).

## Bivariate generating function for well-based forbidden differences

Let $Q$ be a finite
set of positive integers that is well based, and write $S^Q_{n,k}$ for the number of $k$-subsets
of $\{1, \dots, n\}$ in which no two elements differ by an element of $Q$. In the ring
$\mathbb{Z}[y][[x]]$ of formal power series in $x$ with coefficients in $\mathbb{Z}[y]$, let
$g(x, y) = \sum_{n \ge 0} \sum_{k=0}^{n} S^Q_{n,k} \, y^k x^n$ and
$c = 1 + \sum_{q \in Q} x^q y$. Then $g(x, y) \, \bigl((1 - x) \, c - x y\bigr) = c$; since
$(1 - x) c - x y$ has constant term $1$, this says $g = c / ((1 - x) c - x y)$.

The empty set counts as well based, so the case $Q = \emptyset$, where $g = 1/(1 - x - xy)$,
is included.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Corollary 24.

Stated but not proved: `MetaMathlibExt.restrictedCombination_bivariate_genFun_of_isWellBased` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-bivariate-gen-fun).

## Restricted-overlap tilings

Let $Q$ be a finite set of natural numbers and let $q$ be its
largest element ($q = 0$ if $Q$ is empty). The $Q$-comb is a piece of length $q + 1$ whose cell
$0$ and cells $j \in Q$ are teeth and whose other cells are gaps. A restricted-overlap tiling of an
$n$-board (cells $0, \dots, n - 1$) with squares and $k$ $Q$-combs is recorded by the set $P$ of
the start cells of its combs, with squares filling the cells that no tooth covers. The
restricted-overlap tilings are the $k$-element sets $P$ of natural numbers $s$ with $s + q < n$
(each comb fits on the board) such that $s \ne s' + j$ for all $s, s' \in P$ and all nonzero
$j \in Q$ (no comb's leftmost cell is covered by a non-leftmost tooth of another comb).

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedOverlapTilings`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-overlap-tilings).

## Number of restricted-overlap tilings

For a finite set $Q$ of natural numbers and natural
numbers $n$ and $k$, $B^Q_{n,k}$ is the number of restricted-overlap tilings of an $n$-board with
squares and $k$ $Q$-combs.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedOverlapTilingCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-overlap-tiling-count).

## Two dominoes on a 4-board

For $Q = \{1\}$ the $Q$-comb is a domino, and the number
$B^{\{1\}}_{4,2}$ of restricted-overlap tilings of a $4$-board with squares and two $Q$-combs is
$1$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedOverlapTilingCount_singleton_one_four_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-overlap-tiling-count-singleto).

## Two interlocking $\{2\}$-combs on a 4-board

For $Q = \{2\}$, there is exactly one
restricted-overlap tiling of a $4$-board with squares and two $Q$-combs.

Here the $Q$-comb has length $3$, with teeth in cells $0$ and $2$ and a gap in cell $1$; in
the unique tiling the two combs start in cells $0$ and $1$ and interlock.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.restrictedOverlapTilingCount_singleton_two_four_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-overlap-tiling-count-singleto-2).

## Restricted combinations and restricted-overlap tilings

Let $Q$ be a finite set of
natural numbers and let $q$ be its largest element ($q = 0$ if $Q$ is empty). Write
$S^Q_{n,k}$ for the number of $k$-subsets of $\{1, \dots, n\}$ in which no two distinct
elements differ by an element of $Q$, $S^Q_n = \sum_{k=0}^{n} S^Q_{n,k}$, and $B^Q_{m,k}$ for
the number of restricted-overlap tilings of an $m$-board with squares and $k$ $Q$-combs. Then
for all natural numbers $n$ and $k$, $S^Q_{n,k} = B^Q_{n+q,k}$ and
$S^Q_n = \sum_{j=0}^{n+q} B^Q_{n+q,j}$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Theorem 1.

Stated but not proved: `MetaMathlibExt.restrictedCombinationCount_eq_restrictedOverlapTilingCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 381](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L381). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-count-eq-restrict).

## Generating functions of restricted combinations and restricted-overlap tilings

Let $Q$
be a finite set of natural numbers and let $q$ be its largest element ($q = 0$ if $Q$ is empty).
Write $S^Q_{n,k}$ for the number of $k$-subsets of $\{1, \dots, n\}$ in which no two elements
differ by an element of $Q$, and $B^Q_{n,k}$ for the number of restricted-overlap tilings of an
$n$-board with squares and $k$ $Q$-combs. In the ring $\mathbb{Z}[y][[x]]$ of power series in
$x$ with coefficients in $\mathbb{Z}[y]$, let
$g^Q(x, y) = \sum_{n \ge 0} \sum_{k=0}^{n} S^Q_{n,k} x^n y^k$ and
$G(x, y) = \sum_{n \ge 0} \sum_{k=0}^{n} B^Q_{n,k} x^n y^k$. Then

$$x^q g^Q(x, y) = G(x, y) - \sum_{n=0}^{q-1} x^n.$$

This is the paper's formula $g^Q = \bigl(G - (1 - x^q)/(1 - x)\bigr)/x^q$ with the denominators
cleared.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Corollary 7.

Stated but not proved: `MetaMathlibExt.restrictedCombination_genFun_eq_tiling_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-gen-fun-eq-tiling).

## Fence tilings and strongly restricted permutations

Let $D$ be a finite set of integers
and $n$ a natural number. Number the cells of an $n$-board $0, 1, \dots, n-1$ and give cell $i$
a left slot $2i$ and a right slot $2i + 1$. A fence $(s, g)$, with $s$ and $g$ natural numbers,
has teeth in slots $s$ and $s + 1 + 2g$. A tiling is a finite set of fences such that every
fence $(s, g)$ in it satisfies $s + 1 + 2g < 2n$ and either $s$ is even and $g \in D$, or $s$ is
odd and $-g - 1 \in D$, and such that every slot $x < 2n$ is a tooth of exactly one of its
fences. A tiling $t$ and a permutation $\pi$ of $\{0, 1, \dots, n-1\}$ are compatible if for
every cell $i$ and every fence $(s, g) \in t$: if $s = 2i$ then $\pi(i) = i + g$, and if
$s + 1 + 2g = 2i$ then $\pi(i) = i - g - 1$. Then for every tiling $t$ there is exactly one
permutation $\pi$ with $\pi(i) - i \in D$ for all $i$ that is compatible with $t$, and for every
permutation $\pi$ with $\pi(i) - i \in D$ for all $i$ there is exactly one tiling compatible
with $\pi$.

The lemma is due to Edwards and Allen (2015); the fences are $(\tfrac12, g)$-fences.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Lemma 12.

Stated but not proved: `MetaMathlibExt.fenceTiling_strongPerm_bijection` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 413](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L413). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#fence-tiling-strong-perm-bijection).

## Metatiles with at most two combs

Let $Q$ be a finite set of natural numbers and $q$ its
largest element ($q = 0$ for $Q = \emptyset$). The set $Q$ has metatiles with at most two combs
if for all natural numbers $N$ and $k$ and every restricted-overlap tiling of an $N$-board with
squares and $k$ $Q$-combs, with set $P$ of comb start cells, any three combs $a < b < c$ in $P$
are separated by a boundary: there is a natural number $j$ with $a < j \le c$ such that no comb
$s \in P$ satisfies $s < j \le s + q$.

A metatile is a gapless grouping of tiles that cannot be split into smaller gapless groupings.
The boundary before cell $j$ separates two metatiles exactly when no tile straddles it, that is,
when no comb $s \in P$ has $s < j \le s + q$ (squares never straddle a boundary). So the
condition says that every metatile of every such tiling contains at most two combs.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1 (metatiles) and Lemma 15.

Formalized by `MetaMathlibExt.MetatilesHaveAtMostTwoCombs`, a definition declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 438](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L438). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#metatiles-have-at-most-two-combs).

## For $Q = \emptyset$, metatiles have at most two combs

For $Q = \emptyset$, every metatile
of every restricted-overlap tiling with squares and $Q$-combs contains at most two combs.

Here the $Q$-comb is a single cell, so no tile straddles a cell boundary and every metatile is a
single tile.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.metatilesHaveAtMostTwoCombs_empty`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 448](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L448). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#metatiles-have-at-most-two-combs-empty).

## For $Q = \{3\}$, a metatile can contain three combs

For $Q = \{3\}$ it is not true that
every metatile of every restricted-overlap tiling with squares and $Q$-combs contains at most
two combs.

Here the $Q$-comb is a $(1,2,1)$-comb, and combs starting at cells $0, 1, 2$ of a $6$-board form
a single metatile with three combs.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Section 1.

Formalized by `MetaMathlibExt.not_metatilesHaveAtMostTwoCombs_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#not-metatiles-have-at-most-two-combs-thr).

## Restricted combinations counted by compositions

Let $Q$ be a finite set of natural
numbers whose largest element $q$ is positive, and let $S^Q_n$ be the number of subsets of
$\{1, \dots, n\}$ in which no two elements differ by an element of $Q$. Then the following are
equivalent: (i) there is a finite set $A$ of natural numbers such that, for every $n \ge 0$,
$S^Q_n$ is the number of compositions of $n + q$ with all parts in $A$; (ii) every metatile of
every restricted-overlap tiling with squares and $Q$-combs contains at most two combs.
Moreover, if (ii) holds, then for every $n \ge 0$, $S^Q_n$ is the number of compositions of
$n + q$ in which every part is $1$, $q + 1$, or $q + 1 + p$ for some
$p \in \{1, \dots, q\} \setminus Q$.

## Sources

- Michael A. Allen, *Connections Between Combinations Without Specified Separations and Strongly Restricted Permutations, Compositions, and Bit Strings*, Journal of Integer Sequences 28 (2025), Article 25.3.7, Lemma 15.

Stated but not proved: `MetaMathlibExt.restrictedCombinationTotal_eq_card_compositions_iff_metatiles` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/RestrictedCombinationsWanted.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html#restricted-combination-total-eq-card-com).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Combinations without specified separations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/elementary-enumeration/combinations-without-specified-separations)
