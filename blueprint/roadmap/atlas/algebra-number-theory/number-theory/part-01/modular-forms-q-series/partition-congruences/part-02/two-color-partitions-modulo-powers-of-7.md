---
declaration: section
origin: cited
lean: MetaMathlibExt.twoColorMultiplePartitionCount, MetaMathlibExt.twoColorMultiplePartitionCount_of_lt, MetaMathlibExt.twoColorMultiplePartitionCount_zero, MetaMathlibExt.twoColorMultiplePartitionCount_seven_pow_congr, MetaMathlibExt.garvanMTable, MetaMathlibExt.garvanM, MetaMathlibExt.garvanM_one, MetaMathlibExt.garvanM_eight_three
statement: formalized
---

# Two-color partitions modulo powers of 7

23 results, 14 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html).

## Two-color partitions with one color restricted to multiples

For natural numbers $\ell$
and $n$, let $p(m)$ be the number of partitions of $m$, and define

$$
p_{1,\ell}(n) = \sum_{j=0}^{\lfloor n/\ell \rfloor} p(n - \ell j)\, p(j).
$$

For $\ell > 0$ this is the number of 2-color partitions of $n$ in which the parts of the second
color are multiples of $\ell$, that is, the coefficient of $q^n$ in $1/(f_1 f_\ell)$, where
$f_m = \prod_{j \ge 1} (1 - q^{mj})$. For $\ell = 0$ the bound $\lfloor n/0 \rfloor$ is taken to
be $0$, so $p_{1,0}(n) = p(n)$; this is a convention with no generating-function meaning. The
source uses $\ell = 7^k$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.twoColorMultiplePartitionCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#two-color-multiple-partition-count).

## Two-color partitions below the modulus

Let $p_{1,\ell}(n)$ be the number of 2-color
partitions of $n$ in which the parts of the second color are multiples of $\ell$, and $p(n)$ the
number of partitions of $n$. For all natural numbers $\ell$ and $n$ with $n < \ell$, the second
color is unavailable and $p_{1,\ell}(n) = p(n)$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.twoColorMultiplePartitionCount_of_lt`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#two-color-multiple-partition-count-of-lt).

## The two-color partition count at zero

For every natural number $\ell$, including
$\ell = 0$, the two-color partition count $p_{1,\ell}$ satisfies $p_{1,\ell}(0) = 1$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.twoColorMultiplePartitionCount_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#two-color-multiple-partition-count-zero).

## Congruences for two-color partitions modulo powers of 7

For all natural numbers $n$,
$\beta$ and $k \ge 1$, the two-color partition count $p_{1,\ell}$ satisfies

$$
p_{1,7^{2k-1}}(7^{2k+\beta-1} n + (16 \cdot 7^{2k+\beta-1} + 7^{2k-1} + 1)/24)
\equiv 0 \pmod{7^k},
$$



$$
p_{1,7^{2k}}(7^{2k+2\beta-1} n + (10 \cdot 7^{2k+2\beta-1} + 7^{2k} + 1)/24)
\equiv 0 \pmod{7^{k+\beta}},
$$



$$
p_{1,7^{2k}}(7^{2k+2\beta} n + (22 \cdot 7^{2k+2\beta} + 7^{2k} + 1)/24)
\equiv 0 \pmod{7^{k+\beta+1}},
$$

and, for each $r \in \{3, 4, 6\}$,

$$
p_{1,7^{2k}}(7^{2k+2\beta+1} n + ((24r + 22) \cdot 7^{2k+2\beta} + 7^{2k} + 1)/24)
\equiv 0 \pmod{7^{k+\beta+2}}.
$$

Each numerator is divisible by $24$, so every division above is exact.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Theorem 1, congruences (6)-(9).

Stated but not proved: `MetaMathlibExt.twoColorMultiplePartitionCount_seven_pow_congr` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#two-color-multiple-partition-count-seven).

## Tabulated rows of Garvan's matrix

For $1 \le i \le 7$ and $j \ge 1$, the value at
$(i, j)$ is the $j$-th entry of row $i$ in the list below, and $0$ if row $i$ has fewer than
$j$ entries (row $i$ has $2i$ entries). The value is $0$ if $i = 0$, $j = 0$ or $i > 7$.

- Row $1$: $7, 7^2$.
- Row $2$: $10, 9 \cdot 7^2, 2 \cdot 7^4, 7^5$.
- Row $3$: $3, 114 \cdot 7, 85 \cdot 7^3, 24 \cdot 7^5, 3 \cdot 7^7, 7^8$.
- Row $4$: $0, 82 \cdot 7, 176 \cdot 7^3, 845 \cdot 7^4, 272 \cdot 7^6, 46 \cdot 7^8,
  4 \cdot 7^{10}, 7^{11}$.
- Row $5$: $0, 190, 1265 \cdot 7^2, 1895 \cdot 7^4, 1233 \cdot 7^6, 3025 \cdot 7^7,
  620 \cdot 7^9, 75 \cdot 7^{11}, 5 \cdot 7^{13}, 7^{14}$.
- Row $6$: $0, 27, 736 \cdot 7^2, 16782 \cdot 7^3, 20424 \cdot 7^5, 12825 \cdot 7^7,
  4770 \cdot 7^9, 7830 \cdot 7^{10}, 1178 \cdot 7^{12}, 111 \cdot 7^{14}, 6 \cdot 7^{16},
  7^{17}$.
- Row $7$: $0, 1, 253 \cdot 7^2, 1902 \cdot 7^4, 4246 \cdot 7^6, 31540 \cdot 7^7,
  19302 \cdot 7^9, 7501 \cdot 7^{11}, 1944 \cdot 7^{13}, 2397 \cdot 7^{14}, 285 \cdot 7^{16},
  22 \cdot 7^{18}, 7^{20}, 7^{20}$.

These are rows $1$ to $7$ of Garvan's matrix as printed in Tables 1 and 2 of the source.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1, Tables 1 and 2.

Formalized by `MetaMathlibExt.garvanMTable`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-mtable).

## Garvan's matrix

Garvan's matrix $(m_{i,j})_{i,j \ge 1}$ is the array of natural
numbers defined as follows. For $1 \le i \le 7$, $m_{i,j}$ is the entry in row $i$ and column
$j$ of the tabulated rows of Garvan's matrix (Tables 1 and 2 of the source), and $0$ beyond the
printed columns. For $i \ge 8$, $m_{i,1} = m_{i,2} = 0$ and, for $j \ge 3$,

$$m_{i,j} = 7m_{i-3,j-1} + 35m_{i-2,j-1} + 49m_{i-1,j-1} + m_{i-7,j-2} + 7m_{i-6,j-2} +
21m_{i-5,j-2} + 49m_{i-4,j-2} + 147m_{i-3,j-2} + 343m_{i-2,j-2} + 343m_{i-1,j-2}.$$

Entries with $i = 0$ or $j = 0$ are set to $0$.

Lemma 1 of the source identifies these numbers as the coefficients of Garvan's modular
expansion; that identity is a separate statement and is not part of this definition.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.garvanM`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-m).

## Initial entries of the first row of Garvan's matrix

The first two entries of the first
row of Garvan's matrix $(m_{i,j})$ are $m_{1,1} = 7$ and $m_{1,2} = 7^2 = 49$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1, Table 1.

Formalized by `MetaMathlibExt.garvanM_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-m-one).

## The first recurrence value of Garvan's matrix

The entry of Garvan's matrix
$(m_{i,j})$ in row $8$ and column $3$, the first entry computed by the recurrence rather than
read from the tables, is $m_{8,3} = 2464$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.garvanM_eight_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-m-eight-three).

## Recurrence for Garvan's matrix

For all natural numbers $i \ge 8$ and $j \ge 3$, the
entries of Garvan's matrix $(m_{i,j})$ satisfy

$$m_{i,j} = 7m_{i-3,j-1} + 35m_{i-2,j-1} + 49m_{i-1,j-1} + m_{i-7,j-2} + 7m_{i-6,j-2} +
21m_{i-5,j-2} + 49m_{i-4,j-2} + 147m_{i-3,j-2} + 343m_{i-2,j-2} + 343m_{i-1,j-2}.$$

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.garvanM_rec`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-m-rec).

## Garvan's coefficient vectors

Let $(m_{i,j})$ be Garvan's matrix. Garvan's coefficient
vectors $x_k = (x_{k,1}, x_{k,2}, \dots)$ for $k \ge 1$ are defined by $x_{1,1} = 7$,
$x_{1,2} = 7^2$ and $x_{1,i} = 0$ for $i \ge 3$, and, for $k \ge 1$ and $i \ge 1$, by

$$x_{k+1,i} = \sum_{j=1}^{7^k} x_{k,j}\, m_{4j,j+i}$$

if $k$ is odd and

$$x_{k+1,i} = \sum_{j=1}^{7^k} x_{k,j}\, m_{4j+1,j+i}$$

if $k$ is even. Values at index $0$ are conventions outside the source's range.

The source sums over all $j \ge 1$; the cut at $7^k$ loses nothing, since $m_{i,j} = 0$ for
$j > 2i$, so the largest index of a nonzero entry of $x_{k+1}$ is at most $7$ times that of
$x_k$ plus $2$, which stays below $7^{k+1}$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.garvanX`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-x).

## Initial entries of Garvan's first coefficient vector

The first of Garvan's coefficient
vectors, $x_1$, has entries $x_{1,1} = 7$, $x_{1,2} = 7^2 = 49$ and $x_{1,3} = 0$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Section 1.

Formalized by `MetaMathlibExt.garvanX_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-x-one).

## Coefficient vectors for odd powers of 7

For $k \ge 1$ and $\beta \ge 1$ the vectors
$y^{(2k-1)}_\beta = (y^{(2k-1)}_{\beta,1}, y^{(2k-1)}_{\beta,2}, \dots)$ are built from Garvan's
vector $x_{2k-1}$ and Garvan's matrix $m_{i,j}$: $y^{(2k-1)}_{1,j} = x_{2k-1,j}$ and

$$y^{(2k-1)}_{\beta+1,j} = \sum_{i=1}^{7^{2k+\beta-2}} y^{(2k-1)}_{\beta,i}\, m_{4i+1,i+j}.$$

The index $\beta = 0$ gives $0$, and for $k = 0$ every entry is $0$.

The sum over $i$ stops at $7^{2k+\beta-2}$, above the support of $y^{(2k-1)}_\beta$ (each step
maps support $s$ into $7s + 2$).

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Theorem 2.

Formalized by `MetaMathlibExt.garvanYOdd`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-yodd).

## Initial coefficient vector for odd powers of 7

For all natural numbers $k$ and $j$,
the first coefficient vector of Theorem 2 agrees with Garvan's coefficient vector $x_{2k-1}$:
$y^{(2k-1)}_{1,j} = x_{2k-1,j}$. For $k = 0$ the index $2k - 1$ is read as $0$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Theorem 2.

Formalized by `MetaMathlibExt.garvanYOdd_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-yodd-one).

## Coefficient vectors for even powers of 7

Let $(m_{i,j})$ be Garvan's matrix and
$x_k$ Garvan's coefficient vectors, and fix $k \ge 1$. The coefficient vectors
$y^{(2k)}_\beta = (y^{(2k)}_{\beta,1}, y^{(2k)}_{\beta,2}, \dots)$ of Theorem 3, $\beta \ge 1$,
are defined by $y^{(2k)}_{1,j} = x_{2k-1,j}$ and, for $\beta \ge 1$,

$$y^{(2k)}_{\beta+1,j} = \sum_{i=1}^{7^{2k+\beta-2}} y^{(2k)}_{\beta,i}\, m_{4i,i+j}$$

if $\beta$ is odd and

$$y^{(2k)}_{\beta+1,j} = \sum_{i=1}^{7^{2k+\beta-2}} y^{(2k)}_{\beta,i}\, m_{4i+2,i+j}$$

if $\beta$ is even. The definition also assigns conventional values for $k = 0$ and
$\beta = 0$.

The source sums over all $i \ge 1$; the cut at $7^{2k+\beta-2}$ lies above the support of
$y^{(2k)}_\beta$, since each step maps the largest index $s$ of a nonzero entry to at most
$7s + 4$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Theorem 3.

Formalized by `MetaMathlibExt.garvanYEven`, a definition declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-yeven).

## Initial coefficient vector for even powers of 7

For all natural numbers $k$ and $j$,
the first coefficient vector of Theorem 3 agrees with Garvan's coefficient vector $x_{2k-1}$:
$y^{(2k)}_{1,j} = x_{2k-1,j}$. For $k = 0$ the index $2k - 1$ is read as $0$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Theorem 3.

Formalized by `MetaMathlibExt.garvanYEven_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#garvan-yeven-one).

## Garvan's huffing identities for powers of $\xi$

Let
$f_k = \prod_{n \ge 1} (1 - q^{kn})$ in $\mathbb{Q}[[q]]$, let $H$ be the huffing operator
$H\bigl(\sum_n p_n q^n\bigr) = \sum_n p_{7n} q^{7n}$, and let $m_{i,j}$ be Garvan's matrix. Write
$\xi^{-a} = q^{2a} f_{49}^a / f_1^a$ and $T^{-b} = q^{7b} f_{49}^{4b} / f_7^{4b}$ for the
negative powers of $\xi = f_1 / (q^2 f_{49})$ and $T = f_7^4 / (q^7 f_{49}^4)$, which are formal
power series. For every $i \ge 1$,

$$H(\xi^{-i}) = \sum_{j=1}^{2i} m_{i,j}\, T^{-j}$$

and

$$H(\xi^{-4i}) = \sum_{j=1}^{7i} m_{4i,i+j}\, T^{-i-j}.$$

These are identities of formal power series over $\mathbb{Q}$. The sums stop at $j = 2i$,
resp. $j = 7i$, beyond which the coefficients $m$ vanish.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Lemma 1.

Stated but not proved: `MetaMathlibExt.huffing_xi_inv_pow_eq_sum_garvanM` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#huffing-xi-inv-pow-eq-sum-garvan-m).

## Huffing identities for three eta quotients

Let
$f_k = \prod_{n \ge 1} (1 - q^{kn})$ in $\mathbb{Q}[[q]]$, let $H$ be the huffing operator
$H\bigl(\sum_n p_n q^n\bigr) = \sum_n p_{7n} q^{7n}$, and let $m_{i,j}$ be Garvan's matrix. For
every $i \ge 1$,

$$H\Bigl(\frac{q^{i+2} f_7^{4i}}{f_1^{4i+1}}\Bigr)
= \sum_{j=1}^{7i+4} m_{4i+1,i+j}\, \frac{q^{7j} f_{49}^{4j-1}}{f_7^{4j}},$$



$$H\Bigl(\frac{q^{i+4} f_7^{4i}}{f_1^{4i+2}}\Bigr)
= \sum_{j=1}^{7i+4} m_{4i+2,i+j}\, \frac{q^{7j} f_{49}^{4j-2}}{f_7^{4j}},$$



$$H\Bigl(\frac{q^{i} f_7^{4i}}{f_1^{4i}}\Bigr)
= \sum_{j=1}^{7i+4} m_{4i,i+j}\, \frac{q^{7j} f_{49}^{4j}}{f_7^{4j}}.$$

These are identities of formal power series over $\mathbb{Q}$. The sums stop at $j = 7i + 4$,
beyond which the coefficients $m$ vanish.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Lemma 2.

Stated but not proved: `MetaMathlibExt.huffing_eta_quotients_eq_sum_garvanM` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#huffing-eta-quotients-eq-sum-garvan-m).

## Garvan's 7-adic bounds for the matrix $m_{i,j}$

Let $m_{i,j}$ be Garvan's matrix. For
all $i, j \ge 1$, $7^{\lfloor (7j - 2i - 1)/4 \rfloor}$ divides $m_{i,j}$, and in particular
$7^{\lfloor (7j - i - 1)/4 \rfloor}$ divides $m_{4i,i+j}$, $7^{\lfloor (7j - i - 3)/4 \rfloor}$
divides $m_{4i+1,i+j}$ and $7^{\lfloor (7j - i - 5)/4 \rfloor}$ divides $m_{4i+2,i+j}$. A negative
exponent is replaced by $0$, which gives the same statement.

The paper states the bounds as $\pi(n) \ge e$ for the $7$-adic valuation $\pi$ (with
$\pi(0) = \infty$), which is the divisibility $7^e \mid n$. Its bracket is read as the floor: the
ceiling reading fails, since $m_{2,1} = 10$ is not divisible by $7^{\lceil 2/4 \rceil} = 7$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Lemma 3.

Stated but not proved: `MetaMathlibExt.seven_pow_dvd_garvanM` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#seven-pow-dvd-garvan-m).

## Garvan's 7-adic bounds for the vectors $x_k$

Let $x_k = (x_{k,1}, x_{k,2}, \dots)$ be
Garvan's coefficient vectors and $\pi$ the $7$-adic valuation. Then $\pi(x_{1,1}) = 1$,
$\pi(x_{1,2}) = 2$, and for all $k, j \ge 1$, $7^{k + 1 + \lfloor (7j-4)/4 \rfloor}$ divides
$x_{2k+1,j}$ and $7^{k + 1 + \lfloor (7j-6)/4 \rfloor}$ divides $x_{2k,j}$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Lemma 4.

Stated but not proved: `MetaMathlibExt.seven_pow_dvd_garvanX` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#seven-pow-dvd-garvan-x).

## 7-adic bounds for the vectors $y^{(2k)}_\beta$

Let $y^{(2k)}_\beta$ be the coefficient
vectors for even powers of $7$, built from Garvan's vectors and matrix. For all $k, j \ge 1$ and
$\beta \ge 0$, $7^{k + \beta + \lfloor (7j-7)/4 \rfloor}$ divides $y^{(2k)}_{2\beta+1,j}$ and
$7^{k + \beta + 1 + \lfloor (7j-7)/4 \rfloor}$ divides $y^{(2k)}_{2\beta+2,j}$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Lemma 5.

Stated but not proved: `MetaMathlibExt.seven_pow_dvd_garvanYEven` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#seven-pow-dvd-garvan-yeven).

## 7-adic bounds for the vectors $y^{(2k-1)}_\beta$

Let $y^{(2k-1)}_\beta$ be the
coefficient vectors for odd powers of $7$, built from Garvan's vectors and matrix. For all
$k, j \ge 1$ and $\beta \ge 0$, $7^{k + \lfloor (7j-7)/4 \rfloor}$ divides $y^{(2k-1)}_{\beta+1,j}$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Lemma 6.

Stated but not proved: `MetaMathlibExt.seven_pow_dvd_garvanYOdd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 301](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L301). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#seven-pow-dvd-garvan-yodd).

## Generating functions for $p_{1,7^{2k-1}}$ on progressions

Let $p_{1,\ell}(n)$ be the
number of 2-color partitions of $n$ in which the parts of the second color are multiples of
$\ell$, let $f_k = \prod_{n \ge 1} (1 - q^{kn})$ in $\mathbb{Q}[[q]]$, and let $y^{(2k-1)}_\beta$
be the coefficient vectors for odd powers of $7$. For all $k \ge 1$ and $\beta \ge 0$, with
$N = 7^{2k+\beta-1}$,

$$\sum_{n \ge 0} p_{1,7^{2k-1}}\Bigl(N n + \frac{16 N + 7^{2k-1} + 1}{24}\Bigr) q^n
= \sum_{i=1}^{N} y^{(2k-1)}_{\beta+1,i}\, q^{i-1} \frac{f_7^{4i-1}}{f_1^{4i+1}}$$

as formal power series over $\mathbb{Q}$.

The numerator $16 N + 7^{2k-1} + 1$ is divisible by $24$. The sum over $i$ stops at $N$, above
the support of $y^{(2k-1)}_{\beta+1}$.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Theorem 2.

Stated but not proved: `MetaMathlibExt.twoColorMultiplePartitionCount_seven_pow_odd_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#two-color-multiple-partition-count-seven-2).

## Generating functions for $p_{1,7^{2k}}$ on progressions

Let $p_{1,\ell}(n)$ be the
number of 2-color partitions of $n$ in which the parts of the second color are multiples of
$\ell$, let $f_k = \prod_{n \ge 1} (1 - q^{kn})$ in $\mathbb{Q}[[q]]$, and let $y^{(2k)}_\beta$ be
the coefficient vectors for even powers of $7$. For all $k \ge 1$ and $\beta \ge 0$, with
$N = 7^{2k+2\beta-1}$,

$$\sum_{n \ge 0} p_{1,7^{2k}}\Bigl(N n + \frac{10 N + 7^{2k} + 1}{24}\Bigr) q^n
= \sum_{i=1}^{7N} y^{(2k)}_{2\beta+1,i}\, q^{i-1} \frac{f_7^{4i-2}}{f_1^{4i}}$$

and

$$\sum_{n \ge 0} p_{1,7^{2k}}\Bigl(7N n + \frac{22 \cdot 7N + 7^{2k} + 1}{24}\Bigr) q^n
= \sum_{j=1}^{49N} y^{(2k)}_{2\beta+2,j}\, q^{j-1} \frac{f_7^{4j}}{f_1^{4j+2}}$$

as formal power series over $\mathbb{Q}$.

Both numerators are divisible by $24$. The sums stop at $7N$, resp. $49N$, above the supports of
the vectors.

## Sources

- D. S. Gireesh, C. Shivashankar, and B. Hemanthkumar, *On 2-Color Partitions in Which the Parts of One Color Are Restricted to Multiples of 7^k*, INTEGERS 26 (2026), Article A94, Theorem 3.

Stated but not proved: `MetaMathlibExt.twoColorMultiplePartitionCount_seven_pow_even_generatingFunction` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/Partition/TwoColorSevenPowerPartitionWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html#two-color-multiple-partition-count-seven-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Two-color partitions modulo powers of 7](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/partition-congruences/two-color-partitions-modulo-powers-of-7)
