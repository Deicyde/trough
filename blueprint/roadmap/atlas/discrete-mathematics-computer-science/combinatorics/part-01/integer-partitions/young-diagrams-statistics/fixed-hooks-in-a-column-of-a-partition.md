---
declaration: section
origin: cited
lean: MetaMathlibExt.partitionColLen, MetaMathlibExt.partitionRowLen, MetaMathlibExt.partitionHookLength, MetaMathlibExt.IsFixedColumnHook, MetaMathlibExt.partition4431, MetaMathlibExt.partition4431_row_col, MetaMathlibExt.partition4431_hookLength, MetaMathlibExt.partition4431_isFixedColumnHook
statement: formalized
---

# Fixed hooks in a column of a partition

21 results, 8 proved and 13 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html).

## Column lengths of a partition

For a partition $\lambda$ of $n$ and a natural number $j$,
the column length $\lambda'_j$ is the number of parts of $\lambda$, counted with multiplicity, that
are at least $j$. For $j \ge 1$ this is the length of the $j$-th column of the Young diagram of
$\lambda$, with columns numbered from $1$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Section 1 (`λ'`, the conjugate partition).

Formalized by `MetaMathlibExt.partitionColLen`, a definition declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#partition-col-len).

## Row lengths of a partition

For a partition $\lambda$ of $n$ and a natural number $s$, the
row length $\lambda_s$ is the number of $j \in \{1, \dots, n\}$ whose column length $\lambda'_j$ is
at least $s$. For $s \ge 1$ this is the $s$-th largest part of $\lambda$ (rows are numbered from
$1$), and it is $0$ when $\lambda$ has fewer than $s$ parts.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Section 1 (`λ = (λ₁, λ₂, …)` weakly decreasing).

Formalized by `MetaMathlibExt.partitionRowLen`, a definition declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#partition-row-len).

## Hook length of a square of a partition

For a partition $\lambda$ of $n$ and natural numbers
$s$ and $m$, the hook length of the square in row $s$ and column $m$ is the integer
$h_{s,m}(\lambda) = \lambda_s + \lambda'_m - s - m + 1$, where $\lambda_s$ is the $s$-th row length
and $\lambda'_m$ the $m$-th column length of $\lambda$ (rows and columns are numbered from $1$).
The integer is given by this formula for all $s$ and $m$, also when $(s, m)$ is not a square of
the Young diagram.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Section 1.

Formalized by `MetaMathlibExt.partitionHookLength`, a definition declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#partition-hook-length).

## Fixed hooks in a column of a partition

Let $\lambda$ be a partition of $n$, let $m$ and $s$
be natural numbers and let $h$ be an integer. The partition $\lambda$ has an $h$-fixed hook in
column $m$ at row $s$ if the square $(s, m)$ lies in the Young diagram of $\lambda$, that is,
$s \ge 1$ and $1 \le m \le \lambda_s$, and its hook length is $h_{s,m}(\lambda) = s + h$. In other
words, the $s$-th term of the sequence $h_{1,m}(\lambda), h_{2,m}(\lambda), \dots$ of hook lengths
in column $m$ is an $h$-fixed point.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Section 1 (an `h`-fixed point of the sequence `h_{1,m}(λ), h_{2,m}(λ), …`; Figure 2: `h_{m,s} = s + h` at part `λ_s`).

Formalized by `MetaMathlibExt.IsFixedColumnHook`, a definition declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#is-fixed-column-hook).

## The partition $(4, 4, 3, 1)$ of $12$

The partition of $12$ whose parts are $4$, $4$, $3$
and $1$; it is the example partition drawn in Figure 1 of the source.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Figure 1.

Formalized by `MetaMathlibExt.partition4431`, a definition declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#partition4431).

## Row and column lengths of the partition $(4, 4, 3, 1)$

For the partition
$\lambda = (4, 4, 3, 1)$ of $12$, the row lengths are $\lambda_1 = 4$, $\lambda_2 = 4$,
$\lambda_3 = 3$, $\lambda_4 = 1$ and $\lambda_5 = 0$, and the column lengths are $\lambda'_1 = 4$,
$\lambda'_2 = 3$, $\lambda'_3 = 3$, $\lambda'_4 = 2$ and $\lambda'_5 = 0$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Figure 1.

Formalized by `MetaMathlibExt.partition4431_row_col`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#partition4431-row-col).

## Hook lengths of the partition $(4, 4, 3, 1)$

For the partition $\lambda = (4, 4, 3, 1)$ of
$12$, write $h_{s,m}$ for the hook length of the square in row $s$ and column $m$. Along the first
row $h_{1,1} = 7$, $h_{1,2} = 5$, $h_{1,3} = 4$ and $h_{1,4} = 2$; down the first column
$h_{2,1} = 6$, $h_{3,1} = 4$ and $h_{4,1} = 1$; and on the diagonal $h_{2,2} = 4$ and
$h_{3,3} = 1$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Figure 1.

Formalized by `MetaMathlibExt.partition4431_hookLength`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#partition4431-hook-length).

## Fixed hooks in the partition $(4, 4, 3, 1)$

Let $\lambda = (4, 4, 3, 1)$, a partition of
$12$. Then $\lambda$ has a $1$-fixed hook in column $1$ at row $3$ (its hook length is
$h_{3,1} = 4 = 3 + 1$), $\lambda$ has no $0$-fixed hook in column $1$ at row $4$ (its hook length
is $h_{4,1} = 1 \ne 4 + 0$), and $\lambda$ has no $(-3)$-fixed hook in column $3$ at row $4$ (the
square $(4, 3)$ lies outside the Young diagram, since $\lambda_4 = 1 < 3$).

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Figure 1.

Formalized by `MetaMathlibExt.partition4431_isFixedColumnHook`, a theorem declared in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#partition4431-is-fixed-column-hook).

## Zero-fixed hooks in column $m$ and two-colored partitions

Let $n$ and $m \ge 1$ be
natural numbers.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
The number of partitions of $n$ that have a $0$-fixed hook in column $m$ at some row $r \le n$
equals the number of triples $(\mu, \nu, L)$ such that, for some $a \le n$, $\mu$ is a partition
of $a$, $\nu$ is a partition of $n - a$ all of whose parts are at most $m - 1$, and $L$ is a part
of $\mu$ that occurs exactly $L + m - 1$ times in $\mu$ while none of $L + 1, \dots, L + 2m - 2$
is a part of $\mu$.

The pair $(\mu, \nu)$ is a partition of $n$ in which the parts $1, \dots, m - 1$ come in two
colors, $\mu$ collecting the parts of the first color.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 1.

Stated but not proved: `MetaMathlibExt.card_zeroFixedColumnHook_eq_twoColor_count` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#card-zero-fixed-column-hook-eq-two-color).

## Fixed hooks in column $m$ arising from parts of size $m$

Let $n$ and $m \ge 1$ be
natural numbers and let $h$ be an integer.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
Count the partitions $\lambda$ of $n$ that have an $h$-fixed hook in column $m$ at some row
$r \le n$ with $\lambda_r = m$. If $n - mh \ge 0$, this number equals the number of partitions of
$n - mh$ in which $m$ occurs as a part exactly once, none of $m + 1, \dots, 2m - 1$ is a part,
and at least $-h$ parts, counted with multiplicity, are at least $2m$. If $n - mh < 0$, the
number is $0$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 2.

Stated but not proved: `MetaMathlibExt.card_fixedColumnHook_part_eq_column` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#card-fixed-column-hook-part-eq-column).

## Generating function for column-$m$ hooks of size $k$

Let $n$, $m \ge 1$ and $k \ge 1$
be natural numbers. For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part
($0$ if it has fewer than $r$ parts), $\lambda'_m$ for the number of its parts that are at least
$m$, and $h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square
$(r, m)$. Let $H$ be the number of pairs $(\lambda, r)$ of a partition $\lambda$ of $n$ and a row
$1 \le r \le n$ with $m \le \lambda_r$ and $h_{r,m}(\lambda) = k$. In $\mathbb{Q}[[q]]$ write
$(a;q)_j = \prod_{i=0}^{j-1} (1 - a q^i)$ for $j \in \mathbb{N}$ and
$(a;q)_\infty = \prod_{i \ge 0} (1 - a q^i)$, so that $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$ and
$(q^m;q)_j = \prod_{i=0}^{j-1} (1 - q^{m+i})$, and let $P = \prod_{i=0}^{n} (1 - q^{k+i})^{-1}$.
Then $H$ is the coefficient of $q^n$ in

$$
P \sum_{l=1}^{k} \frac{q^{km - (l-1)(m-1)} (q^m;q)_{l-1}}{(q;q)_{l-1} (q;q)_{k-l}},
$$

and $H$ is also the coefficient of $q^n$ in

$$
q^{m+k-1} P \sum_{l=1}^{k} \frac{q^{(m-1)(k-l)} (q^m;q)_{l-1}}{(q;q)_{l-1} (q;q)_{k-l}}.
$$

$P$ is $1/(q^k;q)_\infty$ truncated after $n + 1$ factors, which changes no coefficient below
$q^{n+1}$; the exponent $km - (l-1)(m-1)$ is at least $k + m - 1$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 4.

Stated but not proved: `MetaMathlibExt.columnHook_size_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#column-hook-size-gen-fun).

## Limit of the fixed-hook generating functions

Let $m \ge 2$ be a natural number and work
in $\mathbb{Q}[[q]]$. For $j \in \mathbb{N}$ write $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$ and
$(q^m;q)_j = \prod_{i=0}^{j-1} (1 - q^{m+i})$. Then for every natural number $n$ there is a $K$
such that for every $k \ge K$ the coefficient of $q^n$ in

$$
\frac{q^{m-1}}{\prod_{i=0}^{n} (1 - q^{k+i})}
\sum_{l=1}^{k} \frac{q^{(m-1)(k-l)} (q^m;q)_{l-1}}{(q;q)_{l-1} (q;q)_{k-l}}
$$

equals the coefficient of $q^n$ in

$$
\frac{q^{m-1}}{(1 - q^{m-1}) (q;q)_{n+1}}.
$$

This is the coefficientwise ($q$-adic) form of the limit

$$
\lim_{k \to \infty} \frac{q^{m-1}}{(q^k;q)_\infty}
\sum_{l=1}^{k} \frac{q^{(m-1)(k-l)} (q^m;q)_{l-1}}{(q;q)_{l-1} (q;q)_{k-l}}
= \frac{q^{m-1}}{(1 - q^{m-1}) (q;q)_\infty},
$$

where $(a;q)_\infty = \prod_{i \ge 0} (1 - a q^i)$: for the coefficient of $q^n$, the products
$(q^k;q)_\infty$ and $(q;q)_\infty$ are replaced by their first $n + 1$ factors, which changes no
coefficient below $q^{n+1}$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 5.

Stated but not proved: `MetaMathlibExt.columnHook_size_genFun_limit` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#column-hook-size-gen-fun-limit).

## Partitions with a fixed first-column hook arising from a part of given size

Let $n$ and $k$
be natural numbers with $k \ge 1$ and let $h < k$ be an integer. The number of partitions
$\lambda$ of $n$ that have an $h$-fixed hook in column $1$ at some row $s$ with $\lambda_s = k$ is
the coefficient of $q^n$ in

$$\sum_{s=0}^{n} \frac{q^{s(k+1)+k(k-h)}}{(q;q)_{s+k-h-1}} \binom{s+k-1}{k-1}_q,$$

where $(q;q)_j = \prod_{i\lt j} (1 - q^{i+1})$ is the finite $q$-Pochhammer symbol and
$\binom{a}{b}_q$ is the Gaussian binomial coefficient.

The $s$-th term has no monomial below $q^s$, so the count is also the coefficient of $q^n$ in the
full series over all $s \ge 0$. Under $s \mapsto s + k - h$ that series is the paper's
$\sum_{s \ge k-h} q^{(k+1)(s-1)+h+1} \binom{s+h-1}{k-1}_q / (q;q)_{s-1}$, whose lower limit
$k - h$ is a positive row index.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 6.

Stated but not proved: `MetaMathlibExt.fixedFirstColumnHook_part_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-first-column-hook-part-gen-fun).

## Generating function for fixed column hooks from a part of size $k$

Let $n$, $m \ge 1$
and $k \ge m$ be natural numbers and let $h$ be an integer with $h + m \le k$.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
The number of partitions $\lambda$ of $n$ that have an $h$-fixed hook in column $m$ at some row
$r \le n$ with $\lambda_r = k$ equals the coefficient of $q^n$ in

$$
\sum_{s=0}^{n} \frac{q^{s(k+m) + k(k-h-m+1)}}{(q;q)_{s+k-h-m} (q;q)_{m-1}}
\binom{s+k-m}{k-m}_q,
$$

where $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$ and $\binom{a}{b}_q$ is the Gaussian binomial
coefficient.

The $s$-th term has no monomial below $q^s$, so this is also the coefficient of $q^n$ in the
sum over all $s \ge 0$. The $s$-th term of that sum is the term with index $s + k - h - m + 1$
of the source's first form

$$
\sum_{s \ge k-h-m+1} \frac{q^{s(k+m) + m(h-k+m-1)}}{(q;q)_{s-1} (q;q)_{m-1}}
\binom{s+h-1}{k-m}_q,
$$

whose lower limit $k - h - m + 1$ is a positive row index.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 7.

Stated but not proved: `MetaMathlibExt.fixedColumnHook_part_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-column-hook-part-gen-fun).

## Odd partitions with a fixed hook in a given column arising from an odd part

Let $n$, $m$
and $k$ be natural numbers with $1 \le m \le k$ and $k$ odd, and let $h$ be an integer with
$h \le k - m$. Count the partitions $\lambda$ of $n$ into odd parts that have an $h$-fixed hook in
column $m$ at some row $s$ with $\lambda_s = k$. Write $(q^2;q^2)_j = \prod_{i\lt j} (1 - q^{2i+2})$
and $(q;q^2)_j = \prod_{i\lt j} (1 - q^{2i+1})$, write $\binom{a}{b}_{q^2}$ for the Gaussian binomial
coefficient in $q^2$, and put $s_t = k - h - m + 1 + t$ for $t \ge 0$. If $m$ is odd, the count is
the coefficient of $q^n$ in

$$\sum_{t=0}^{n} \frac{q^{s_t(k+m)+m(m+h-k-1)}}{(q^2;q^2)_{s_t-1}\,(q;q^2)_{(m-1)/2}}
\binom{t+(k-m)/2}{t}_{q^2},$$

and if $m$ is even, it is the coefficient of $q^n$ in

$$\sum_{t=0}^{n} \frac{q^{s_t(k+m+1)+(m+1)(h-k)+m^2-1}}{(q^2;q^2)_{s_t-1}\,(q;q^2)_{m/2}}
\binom{t+(k-m-1)/2}{t}_{q^2}.$$

Here $s_t \ge 1$, the exponents are positive, and the halves $(k-m)/2$ and $(k-m-1)/2$ are
integers. The $t$-th term has no monomial below $q^t$, so the count is also the coefficient of
$q^n$ in the full series over all $s = s_t \ge k - h - m + 1$; in the paper's notation the bottom
index of the Gaussian binomial is $j = s + h - k + m - 1 = t$.

Corrected reading: as printed, the Gaussian binomials are $\binom{s+h-k+(k-m)/2}{s+h-k}_{q^2}$ and
the even-$m$ exponent is $s(k+m+1)+m(h-k+m)+h-k+1$, which is larger by $2$. Both are slips in
reindexing $k + m - 1 \mapsto k$ the $m = 1$ formula in the paper's proof (its binomial index
$s + h - k$ becomes $s + h - k + m - 1$, and its displayed even-$m$ exponent simplifies to the
one stated here). As printed the statement is false: for $m = k = 3$, $h = 0$, the partition
$(3)$ of $3$ has the $0$-fixed hook $h_{1,3} = 1$, but the printed series has no $q^3$ term (its
first term is $q^{15}$); for $m = 2$, $k = 3$, $h = 0$ the count for $n = 6$ is $1$ and the
printed series has no $q^6$ term.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 8, corrected per its proof.

Stated but not proved: `MetaMathlibExt.fixedColumnHook_part_odd_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-column-hook-part-odd-gen-fun).

## Fixed column hooks from a part of size $k$ in distinct partitions

Let $n$, $m \ge 1$
and $k \ge m$ be natural numbers and let $h$ be an integer with $h + m \le k$.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
The number of partitions $\lambda$ of $n$ into distinct parts that have an $h$-fixed hook in
column $m$ at some row $r \le n$ with $\lambda_r = k$ equals the coefficient of $q^n$ in

$$
\sum_{s=0}^{k-m} q^{s(k+m) + k(k-h-m+1) + \binom{s+k-m+1-h}{2} + \binom{s}{2}}
\frac{(-q;q)_{m-1}}{(q;q)_{s+k-h-m}} \binom{k-m}{s}_q,
$$

where $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$, $(-q;q)_j = \prod_{i=1}^{j} (1 + q^i)$ and
$\binom{a}{b}_q$ is the Gaussian binomial coefficient.

The denominator $(q;q)_{s+k-h-m}$ follows the journal version. The arXiv version
(arXiv:2406.08609) prints $(q;q)_{k-h-1}$, which is false: for $m = 1$, $k = 2$, $h = 0$ the
number of such partitions of $12$ is $3$, but the coefficient of $q^{12}$ is $2$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 9.

Stated but not proved: `MetaMathlibExt.fixedColumnHook_part_distinct_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-column-hook-part-distinct-gen-fun).

## Partitions with a fixed first-column hook of given size

Let $n$ and $k$ be natural numbers
with $k \ge 1$ and let $h < k$ be an integer. The number of partitions $\lambda$ of $n$ that have an
$h$-fixed hook in column $1$ at some row $s$ whose hook length is $h_{s,1}(\lambda) = k$ is the
coefficient of $q^n$ in

$$\sum_{l=1}^{k} \frac{q^{k+l(k-h-1)}}{(q;q)_{k-h-1}} \binom{k-1}{l-1}_q,$$

where $(q;q)_j = \prod_{i\lt j} (1 - q^{i+1})$ is the finite $q$-Pochhammer symbol and
$\binom{a}{b}_q$ is the Gaussian binomial coefficient.

Such a hook sits in row $s = k - h \ge 1$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 10.

Stated but not proved: `MetaMathlibExt.fixedFirstColumnHook_hook_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-first-column-hook-hook-gen-fun).

## Generating function for fixed column hooks of size $k$

Let $n$, $m \ge 1$ and $k \ge 1$
be natural numbers and let $h < k$ be an integer.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
The number of partitions $\lambda$ of $n$ that have an $h$-fixed hook in column $m$ at some row
$r \le n$ with $h_{r,m}(\lambda) = k$ equals the coefficient of $q^n$ in

$$
\sum_{l=1}^{k} \frac{q^{(m-1)(2k-h-l) + k + l(k-h-1)}}{(q;q)_{k-h-1} (q;q)_{m-1}}
\binom{k-1}{l-1}_q,
$$

where $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$ and $\binom{a}{b}_q$ is the Gaussian binomial
coefficient.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 11.

Stated but not proved: `MetaMathlibExt.fixedColumnHook_hook_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-column-hook-hook-gen-fun).

## Generating function for fixed column hooks of size $k$ in odd partitions

Let $n$,
$m \ge 1$ and $k \ge 1$ be natural numbers and let $h < k$ be an integer.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
In $\mathbb{Q}[[q]]$ write $(q^2;q^2)_j = \prod_{i=1}^{j} (1 - q^{2i})$ and
$(q;q^2)_j = \prod_{i=0}^{j-1} (1 - q^{2i+1})$, and let $\binom{a}{b}_{q^2}$ be the Gaussian
binomial coefficient in $q^2$. Let $N$ be the number of partitions $\lambda$ of $n$ into odd
parts that have an $h$-fixed hook in column $m$ at some row $r \le n$ with
$h_{r,m}(\lambda) = k$. If $m$ is odd, $N$ is the coefficient of $q^n$ in

$$
\sum_{l} \frac{q^{k + l(k-h-1) + (m-1)(2k-h-l)}}{(q^2;q^2)_{k-h-1} (q;q^2)_{(m-1)/2}}
\binom{k-l+(l-1)/2}{k-l}_{q^2},
$$

the sum running over the odd $l$ with $1 \le l \le k$. If $m$ is even, $N$ is the coefficient
of $q^n$ in

$$
\sum_{l} \frac{q^{k + l(k-h-1) + (m-1)(2k-h-l) + (k-l)}}{(q^2;q^2)_{k-h-1} (q;q^2)_{m/2}}
\binom{k-l+(l-2)/2}{k-l}_{q^2},
$$

the sum running over the even $l$ with $1 \le l \le k$.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 12.

Stated but not proved: `MetaMathlibExt.fixedColumnHook_hook_odd_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-column-hook-hook-odd-gen-fun).

## Generating function for fixed column hooks of size $k$ in distinct partitions

Let $n$,
$m \ge 1$ and $k \ge 1$ be natural numbers and let $h < k$ be an integer.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
The number of partitions $\lambda$ of $n$ into distinct parts that have an $h$-fixed hook in
column $m$ at some row $r \le n$ with $h_{r,m}(\lambda) = k$ equals the coefficient of $q^n$ in

$$
\sum_{l=\lceil (k+1)/2 \rceil}^{k}
q^{k + l(k-h-1) + (m-1)(2k-h-l) + \binom{k-h}{2} + \binom{k-l}{2}}
\frac{(-q;q)_{m-1}}{(q;q)_{k-h-1}} \binom{l-1}{k-l}_q,
$$

where $(q;q)_j = \prod_{i=1}^{j} (1 - q^i)$, $(-q;q)_j = \prod_{i=1}^{j} (1 + q^i)$ and
$\binom{a}{b}_q$ is the Gaussian binomial coefficient.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 13.

Stated but not proved: `MetaMathlibExt.fixedColumnHook_hook_distinct_genFun` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-column-hook-hook-distinct-gen-fun).

## Fixed column hooks of size $k$ in odd distinct partitions, even column

Let $n$, $m$ and
$k \ge 1$ be natural numbers with $m \ge 1$ even, and let $h < k$ be an integer.
For a partition $\lambda$, write $\lambda_r$ for its $r$-th largest part ($0$ if it has fewer
than $r$ parts), $\lambda'_m$ for the number of its parts that are at least $m$, and
$h_{r,m}(\lambda) = \lambda_r + \lambda'_m - r - m + 1$ for the hook length of the square $(r, m)$.
The partition $\lambda$ has an $h$-fixed hook in column $m$ at row $r$ when $r \ge 1$,
$m \le \lambda_r$ and $h_{r,m}(\lambda) = r + h$.
The number of partitions $\lambda$ of $n$ into distinct odd parts that have an $h$-fixed hook in
column $m$ at some row $r \le n$ with $h_{r,m}(\lambda) = k$ equals the coefficient of $q^n$ in

$$
\sum_{l} q^{k - l + (m-1)(2k-h-l) + k + l(k-h-1) + 2\binom{k-h}{2} + 2\binom{k-l}{2}}
\frac{(-q;q^2)_{m/2}}{(q^2;q^2)_{k-h-1}} \binom{k - l + (3l-2k-2)/2}{k-l}_{q^2},
$$

the sum running over the even $l$ with $\lceil 2k/3 \rceil \le l \le k$, where
$(q^2;q^2)_j = \prod_{i=1}^{j} (1 - q^{2i})$, $(-q;q^2)_j = \prod_{i=0}^{j-1} (1 + q^{2i+1})$
and $\binom{a}{b}_{q^2}$ is the Gaussian binomial coefficient in $q^2$.

On the range of summation the top index $k - l + (3l-2k-2)/2 = (l-2)/2$ is a nonnegative
integer. Only even $m$ is stated: for odd $m$ the source prints the top index
$k - l + (3l-2k)/2$ over odd $l$, which is not an integer.

## Sources

- Philip Cuthbertson, *Fixed Hooks in Arbitrary Columns of Partitions*, INTEGERS 25 (2025), Article A28, Theorem 14, even `m`.

Stated but not proved: `MetaMathlibExt.fixedColumnHook_hook_oddDistinct_genFun_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/FixedColumnHooksWanted.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html#fixed-column-hook-hook-odd-distinct-gen).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fixed hooks in a column of a partition](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/integer-partitions/young-diagrams-statistics/fixed-hooks-in-a-column-of-a-partition)
