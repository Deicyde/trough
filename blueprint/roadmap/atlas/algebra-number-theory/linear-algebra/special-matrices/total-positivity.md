---
declaration: section
origin: cited
lean: MetaMathlibExt.Matrix.HasNonnegativeMinors, MetaMathlibExt.Matrix.HasPositiveMinors, MetaMathlibExt.Matrix.HasPositiveMinors.entry_pos, MetaMathlibExt.hasPositiveMinors_iff_initial_minors_pos, MetaMathlibExt.generalizedPFibonacci, MetaMathlibExt.generalizedPFibonacci_zero_one, MetaMathlibExt.generalizedPFibonacci_two_p, MetaMathlibExt.generalizedHyperFibonacci
statement: formalized
---

# Total positivity

20 results, 8 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html).

## Matrices with nonnegative minors

Let $\iota$ and $\kappa$ be linearly ordered types and
let $M$ be a real matrix with rows indexed by $\iota$ and columns indexed by $\kappa$. Then $M$
has nonnegative minors when, for every $k \in \mathbb{N}$ and all strictly increasing maps
$r \colon \{0, \dots, k-1\} \to \iota$ and $c \colon \{0, \dots, k-1\} \to \kappa$, the
$k \times k$ submatrix $(M_{r(a), c(b)})_{a, b < k}$ has nonnegative determinant. The case
$k = 0$, the empty minor, is included.

## Sources

- Ming-Jian Ding and Jiang Zeng, "Some New Results on the Minuscule Polynomials of Type A", Journal of Integer Sequences 28 (2025), Article 25.1.2, "Total positivity of the coefficient matrix" section, definition at lines 638–639 (used by the Schoenberg–Edrei lemma, line 654), <https://cs.uwaterloo.ca/journals/JIS/VOL28/Zeng/zeng26.tex>.

Formalized by `MetaMathlibExt.Matrix.HasNonnegativeMinors`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/NonnegativeMinors.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/NonnegativeMinors.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#has-nonnegative-minors).

## Matrices with positive minors

A real matrix $M$ whose rows and columns are indexed by
linearly ordered sets $R$ and $C$ has positive minors (is totally positive) when, for every
natural number $k$ and all strictly increasing maps $r : \{1, \dots, k\} \to R$ and
$c : \{1, \dots, k\} \to C$, the $k \times k$ submatrix $(M_{r(a), c(b)})_{1 \le a, b \le k}$ has
positive determinant. The case $k = 0$ is the empty minor, whose determinant is $1$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Section 1 (total positivity).

Formalized by `MetaMathlibExt.Matrix.HasPositiveMinors`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/PositiveMinors.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PositiveMinors.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#has-positive-minors).

## Entries of a matrix with positive minors are positive

Let $M$ be a real matrix whose rows
and columns are indexed by linearly ordered sets $R$ and $C$. If $M$ has positive minors, then
$M_{ij} > 0$ for all $i \in R$ and $j \in C$; these entries are the $1 \times 1$ minors of $M$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Section 1 (total positivity).

Formalized by `MetaMathlibExt.Matrix.HasPositiveMinors.entry_pos`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PositiveMinors.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/LinearAlgebra/Matrix/PositiveMinors.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#entry-pos).

## Gasca–Peña criterion for total positivity

Let $A$ be a real $n \times n$ matrix whose
rows and columns are indexed by $0, \dots, n - 1$. Then $A$ is totally positive (has positive
minors) if and only if all its initial minors are positive: for all natural numbers $k$, $i_0$
and $j_0$ with $i_0 + k \le n$, $j_0 + k \le n$ and $i_0 = 0$ or $j_0 = 0$, the $k \times k$
submatrix of $A$ with rows $i_0, \dots, i_0 + k - 1$ and columns $j_0, \dots, j_0 + k - 1$ has
positive determinant.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Theorem 3, quoting Gasca and Peña (`jis-2026-26.2.5-thm-3`).

Stated but not proved: `MetaMathlibExt.hasPositiveMinors_iff_initial_minors_pos` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#has-positive-minors-iff-initial-minors-p).

## Generalized $p$-Fibonacci sequence

For integers $p$, $a$ and $b$, the generalized
Fibonacci sequence $(W_{p,n})_{n \ge 0}$ of integers is defined by $W_{p,0} = a$, $W_{p,1} = b$
and $W_{p,n} = p W_{p,n-1} + W_{p,n-2}$ for $n \ge 2$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Section 1, recurrence (1).

Formalized by `MetaMathlibExt.generalizedPFibonacci`, a definition declared in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-pfibonacci).

## $p$-Fibonacci numbers as a Lucas sequence

For every integer $p$, the generalized
Fibonacci sequence $W_{p,n}$ with initial values $a = 0$ and $b = 1$ (the $p$-Fibonacci numbers
$F_{p,n}$) is the Lucas sequence $U(p, -1)$: $W_{p,n} = U_n(p, -1)$ for every natural number $n$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Section 1, remark after recurrence (1) (`p`-Fibonacci numbers `F_{p,n}`).

Formalized by `MetaMathlibExt.generalizedPFibonacci_zero_one`, a theorem declared in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-pfibonacci-zero-one).

## $p$-Lucas numbers as a companion Lucas sequence

For every integer $p$, the generalized
Fibonacci sequence $W_{p,n}$ with initial values $a = 2$ and $b = p$ (the $p$-Lucas numbers
$L_{p,n}$) is the companion Lucas sequence $V(p, -1)$: $W_{p,n} = V_n(p, -1)$ for every natural
number $n$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Section 1, remark after recurrence (1) (`p`-Lucas numbers `L_{p,n}`).

Formalized by `MetaMathlibExt.generalizedPFibonacci_two_p`, a theorem declared in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-pfibonacci-two-p).

## Generalized hyper-Fibonacci numbers

Let $p, a, b$ be integers and let $W_{p,n}$ denote the
generalized Fibonacci sequence, with $W_{p,0} = a$, $W_{p,1} = b$ and
$W_{p,n+2} = p W_{p,n+1} + W_{p,n}$. The generalized hyper-Fibonacci numbers $W^{(r)}_{p,n}$, for
natural numbers $r$ and $n$, are the integers defined by $W^{(0)}_{p,n} = W_{p,n}$ and, for
$r \ge 1$, by $W^{(r)}_{p,n} = \sum_{k=0}^{n} p^{n-k} W^{(r-1)}_{p,k}$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Section 1, definition (2).

Formalized by `MetaMathlibExt.generalizedHyperFibonacci`, a definition declared in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci).

## Initial values of generalized hyper-Fibonacci numbers

Let $p, a, b$ be integers and let
$W^{(r)}_{p,n}$ denote the generalized hyper-Fibonacci numbers. For every natural number $r$,
$W^{(r)}_{p,0} = a$ and $W^{(r)}_{p,1} = p \cdot a \cdot r + b$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Section 1, definition (2) (initial values).

Formalized by `MetaMathlibExt.generalizedHyperFibonacci_zero_one`, a theorem declared in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-zero-one).

## Recurrence for generalized hyper-Fibonacci numbers

Let $p, a, b$ be integers and let
$W^{(r)}_{p,n}$ denote the generalized hyper-Fibonacci numbers. For all natural numbers $r \ge 1$
and $n \ge 1$, $W^{(r)}_{p,n} = p W^{(r)}_{p,n-1} + W^{(r-1)}_{p,n}$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Lemma 5, identity (3), quoting Ait-Amrane et al. (`jis-2026-26.2.5-lem-5`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_succ_succ` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-succ-succ).

## A binomial-sum formula for generalized hyper-Fibonacci numbers

Let $p, a, b$ be integers
with $p \ne 0$, let $W_{p,n}$ denote the generalized Fibonacci sequence and $W^{(r)}_{p,n}$ the
generalized hyper-Fibonacci numbers. For all natural numbers $r$ and $n$ with $1 \le r \le n$, the
following identity of rational numbers holds:

$$
W^{(r)}_{p,n-r} = W_{p,n+r} - \frac{p^n}{p^{r-1}} \sum_{k=0}^{r-1} \binom{n-k-1}{r-k-1} W_{p,2k+1}.
$$

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Lemma 5, identity (4), quoting Ait-Amrane et al. (`jis-2026-26.2.5-lem-5`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_sub_eq_sub` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-sub-eq-sub).

## Hankel determinants of generalized hyper-Fibonacci numbers

Let $p, a, b$ be integers, let
$W^{(r)}_{p,n}$ denote the generalized hyper-Fibonacci numbers and put $\Delta = a^2 + pab - b^2$.
For all natural numbers $r$ and $n$, the $(r+2) \times (r+2)$ Hankel matrix
$H_{r,n} = (W^{(r)}_{p,n+i+j})_{0 \le i, j \le r+1}$ has determinant
$\det H_{r,n} = (-1)^{n+1+\lfloor (r+3)/2 \rfloor} p^{nr+r^2} b^r \Delta$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Proposition 7, quoting Ait-Amrane et al. (`jis-2026-26.2.5-prop-7`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_hankel_det` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-hankel-det).

## Eventual positivity of hyper-Fibonacci Toeplitz determinants

Let $p, a, b$ be integers
with $p \ge 1$, $a \ge 0$ and $b > 0$, and let $W^{(r)}_{p,n}$ denote the generalized
hyper-Fibonacci numbers. For every natural number $m \ge 1$ there is a natural number $N$ such
that for every $n \ge N$ the $m \times m$ Toeplitz matrix with entry $W^{(m-1)}_{p,n+i-j}$ in row
$i$ and column $j$ ($0 \le i, j < m$) has positive determinant.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Theorem 8 (`jis-2026-26.2.5-thm-8`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_toeplitz_det_eventually_pos` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-toeplitz-det).

## Eventual positivity of lower-order hyper-Fibonacci Toeplitz determinants

Let $p, a, b$ be
integers with $p \ge 1$, $a \ge 0$ and $b > 0$, and let $W^{(r)}_{p,n}$ denote the generalized
hyper-Fibonacci numbers. For natural numbers $r$, $m$ and $n$ write $T^{(r)}_{m,n}$ for the
$m \times m$ Toeplitz matrix with entry $W^{(r)}_{p,n+i-j}$ in row $i$ and column $j$
($0 \le i, j < m$). If $r \ge 1$ and $1 \le m \le r + 1$, then there is a natural number $N$ such
that $\det T^{(r)}_{m,n} > 0$ for every $n \ge N$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Corollary 9 (`jis-2026-26.2.5-cor-9`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_toeplitz_det_eventually_pos_of_le` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-toeplitz-det-2).

## Eventual log-concavity of generalized hyper-Fibonacci numbers

Let $p, a, b$ be integers
with $p \ge 1$, $a \ge 0$ and $b > 0$, let $W^{(r)}_{p,n}$ denote the generalized hyper-Fibonacci
numbers, and let $r \ge 1$ be a natural number. Then there is a natural number $N$ such that for
every $n \ge N$ we have $W^{(r)}_{p,n} > 0$ and
$W^{(r)}_{p,n} W^{(r)}_{p,n+2} \le (W^{(r)}_{p,n+1})^2$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Corollary 10 (`jis-2026-26.2.5-cor-10`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_eventually_logConcave` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-eventually-l).

## Eventual log-concavity of hyper $p$-Fibonacci and hyper $p$-Lucas numbers

Let
$p \ge 1$ be an integer and $r \ge 1$ a natural number, and let $F_{p,n}^{(r)}$ and
$L_{p,n}^{(r)}$ be the generalized hyper-Fibonacci numbers $W_{p,n}^{(r)}$ with initial values
$(a, b) = (0, 1)$ and $(a, b) = (2, p)$ respectively (the hyper $p$-Fibonacci and hyper
$p$-Lucas numbers). Both sequences are eventually log-concave: there is $N$ such that for all
$n \ge N$, $F_{p,n}^{(r)} > 0$ and $F_{p,n}^{(r)} F_{p,n+2}^{(r)} \le (F_{p,n+1}^{(r)})^2$, and
there is $N'$ such that for all $n \ge N'$, $L_{p,n}^{(r)} > 0$ and
$L_{p,n}^{(r)} L_{p,n+2}^{(r)} \le (L_{p,n+1}^{(r)})^2$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Corollary 11 (`jis-2026-26.2.5-cor-11`).

Stated but not proved: `MetaMathlibExt.hyperPFibonacci_hyperPLucas_eventually_logConcave` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#hyper-pfibonacci-hyper-plucas-eventually).

## Eventual total positivity of hyper-Fibonacci Toeplitz matrices

Let $p, a, b$ be integers
with $p \ge 1$, $a \ge 0$ and $b > 0$, put $\Delta = a^2 + pab - b^2$, let $W^{(r)}_{p,n}$
denote the generalized hyper-Fibonacci numbers, and let $r \ge 1$ be a natural number. For a
natural number $s$ write $T_s$ for the real $(r+2) \times (r+2)$ Toeplitz matrix with entry
$W^{(r)}_{p,s+i-j}$ in row $i$ and column $j$ ($0 \le i, j \le r+1$). If $\Delta > 0$, there is a
natural number $N$ such that $T_{2n}$ has positive minors (is totally positive) for every
$n \ge N$; if $\Delta < 0$, there is a natural number $N$ such that $T_{2n+1}$ has positive
minors for every $n \ge N$.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Theorem 12 (`jis-2026-26.2.5-thm-12`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_toeplitz_hasPositiveMinors` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-toeplitz-has).

## Eventually positive bounded-order minors of hyper-Fibonacci Toeplitz matrices

Let
$p, a, b$ be integers with $p \ge 1$, $a \ge 0$ and $b > 0$, let $W^{(r)}_{p,n}$ denote the
generalized hyper-Fibonacci numbers, and let $r \ge 1$ be a natural number. For a natural number
$n$ let $T_n$ be the real $(r+2) \times (r+2)$ Toeplitz matrix with entry $W^{(r)}_{p,n+i-j}$ in
row $i$ and column $j$ ($0 \le i, j \le r+1$). Then there is a natural number $N$ such that for
every $n \ge N$, every natural number $k \le r + 1$ and all strictly increasing maps
$\rho, \gamma : \{0, \dots, k-1\} \to \{0, \dots, r+1\}$, the $k \times k$ submatrix
$((T_n)_{\rho(u), \gamma(v)})_{0 \le u, v < k}$ has positive determinant; that is, every minor
of $T_n$ of order at most $r + 1$ is positive.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Corollary 13 (`jis-2026-26.2.5-cor-13`).

Stated but not proved: `MetaMathlibExt.generalizedHyperFibonacci_toeplitz_positiveMinors_le` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#generalized-hyper-fibonacci-toeplitz-pos).

## Total positivity of hyper $p$-Fibonacci Toeplitz matrices

Let $p \ge 1$ be an integer
and $r \ge 1$ a natural number, and let $F_{p,n}^{(r)}$ be the hyper $p$-Fibonacci numbers, the
generalized hyper-Fibonacci numbers $W_{p,n}^{(r)}$ with initial values $a = 0$ and $b = 1$.
Consider real $(r + 2) \times (r + 2)$ matrices with rows and columns indexed by
$0, \dots, r + 1$. For all sufficiently large $n$, the Toeplitz matrix with entry
$F_{p,2n+1+i-j}^{(r)}$ in row $i$ and column $j$ is totally positive. Moreover, for all
sufficiently large $n$, the Toeplitz matrix with entry $F_{p,n+i-j}^{(r)}$ in row $i$ and
column $j$ is $\mathrm{TP}_{r+1}$: each of its minors of order at most $r + 1$ is positive.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Corollary 14 (`jis-2026-26.2.5-cor-14`).

Stated but not proved: `MetaMathlibExt.hyperPFibonacci_toeplitz_hasPositiveMinors` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#hyper-pfibonacci-toeplitz-has-positive-m).

## Total positivity of hyper $p$-Lucas Toeplitz matrices

Let $p \ge 1$ be an integer and
$r \ge 1$ a natural number, and let $L_{p,n}^{(r)}$ be the hyper $p$-Lucas numbers, the
generalized hyper-Fibonacci numbers $W_{p,n}^{(r)}$ with initial values $a = 2$ and $b = p$.
Consider real $(r + 2) \times (r + 2)$ matrices with rows and columns indexed by
$0, \dots, r + 1$. For all sufficiently large $n$, the Toeplitz matrix with entry
$L_{p,2n+i-j}^{(r)}$ in row $i$ and column $j$ is totally positive. Moreover, for all
sufficiently large $n$, the Toeplitz matrix with entry $L_{p,n+i-j}^{(r)}$ in row $i$ and
column $j$ is $\mathrm{TP}_{r+1}$: each of its minors of order at most $r + 1$ is positive.

## Sources

- Abdelhak Taane, Ihab-Eddine Djellas and Mohammed Mekkaoui, *Total Positivity of Toeplitz Matrices Involving Generalized Hyper-Fibonacci Numbers*, Journal of Integer Sequences 29 (2026), Article 26.2.5, Corollary 15 (`jis-2026-26.2.5-cor-15`).

Stated but not proved: `MetaMathlibExt.hyperPLucas_toeplitz_hasPositiveMinors` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/LinearAlgebra/TotallyPositiveInitialMinorsWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html#hyper-plucas-toeplitz-has-positive-minor).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Total positivity](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/special-matrices/total-positivity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/LinearAlgebra/special-matrices/total-positivity)
