---
declaration: section
origin: cited
lean: MetaMathlibExt.IsGeneralizedRascalTriangle, MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.wordAscents, MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalZ, MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.RascalWord, MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalGen, MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalGenZ, MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.IsAscentSeq, MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.Avoids001210
statement: formalized
---

# Rascal triangle

37 results, 10 proved and 27 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html).

## Generalized rascal triangle

An integer array $T(r, k)$, indexed by natural numbers $r$
and $k$, is a generalized rascal triangle when there exist integers $c$, $d$, $d_1$, $d_2$ such
that $T(r, k) = c + k\,d_1 + r\,d_2 + r k\,d$ for all natural numbers $r$ and $k$.

Formalized by `MetaMathlibExt.IsGeneralizedRascalTriangle`, a definition declared in [MathlibExt/Combinatorics/Enumerative/GeneralizedRascalTriangle.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/GeneralizedRascalTriangle.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#is-generalized-rascal-triangle).

## Number of ascents of a word

For a finite word
$w = w_1 w_2 \cdots w_n$ of natural numbers, the number of ascents
of $w$ is the number of indices $i$ with $1 \le i < n$ and
$w_i < w_{i+1}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.wordAscents`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#word-ascents).

## Rascal numbers on the integers

For integers $n$ and $k$, the Rascal number $R_{n,k}$ is
$k(n-k) + 1$ if $0 \le k \le n$, and $0$ otherwise.

Gibbs and Miceli define $R_{n,k}$ by the diamond recurrence of Angorro et al., with value $0$
outside $0 \le k \le n$; Angorro et al. proved that it equals $k(n-k) + 1$ in that range.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalZ`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-z).

## Binary words with few ascents

For natural numbers $j$, $k$ and $n$, $B^{(j)}_k(n)$ is
the set of words $w$ of length $n$ over the alphabet $\{0, 1\}$ with exactly $k$ ones and at most
$j$ ascents, an ascent being a position $i$ with $w_i < w_{i+1}$, that is, a $0$ immediately
followed by a $1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.RascalWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-word).

## Generalized Rascal numbers

For natural numbers $j$, $k$ and $n$, the generalized Rascal
number $R^{(j)}_{n,k}$ is the number of binary words of length $n$ with exactly $k$ ones and at
most $j$ ascents, that is, the number of elements of $B^{(j)}_k(n)$; an ascent is a position at
which a $0$ is immediately followed by a $1$.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalGen`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-gen).

## Generalized Rascal numbers at integer indices

For a natural number $j$ and integers $n$
and $k$, $R^{(j)}_{n,k}$ is the generalized Rascal number of $n$ and $k$ (the number of binary
words of length $n$ with exactly $k$ ones and at most $j$ ascents) when $0 \le k \le n$, and $0$
otherwise.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalGenZ`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-gen-z).

## Ascent sequences

A finite sequence $w_1 w_2 \cdots w_n$ of natural numbers is an
ascent sequence when $w_1 = 0$ (if $n \ge 1$) and
$w_i \le \operatorname{asc}(w_1 \cdots w_{i-1}) + 1$ for every $1 \le i \le n$, where
$\operatorname{asc}(v)$ counts the positions $j$ with $v_j < v_{j+1}$. In particular the empty
sequence is an ascent sequence.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.IsAscentSeq`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#is-ascent-seq).

## Avoiding the patterns 001 and 210

A finite sequence $w$ of natural numbers avoids
$001$ and $210$ when it has no subsequence $x, x, y$ with $x < y$ and no subsequence $x, y, z$
with $x > y > z$. Subsequences need not consist of consecutive entries.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.Avoids001210`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#avoids001210).

## Ascent sequences avoiding 001 and 210

For natural numbers $n$ and $k$, this is the set
of ascent sequences $w$ of length $n$ that avoid the patterns $001$ and $210$ and have exactly
$k$ ascents, an ascent of $w$ being a position $i$ with $w_i < w_{i+1}$.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.AscentSeqAvoid`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#ascent-seq-avoid).

## Number of ascent sequences avoiding 001 and 210

For natural numbers $n$ and $k$, this
counts the ascent sequences of length $n$ with exactly $k$ ascents that avoid the patterns
$001$ and $210$.

Formalized by `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.apkCard`, a definition declared in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#apk-card).

## Rascal numbers count binary words with at most one ascent

For all integers $n$ and $k$,
$R_{n,k} = b_k(n)$, where $R_{n,k}$ is the Rascal number and $b_k(n)$ is the number of binary
words of length $n$ with exactly $k$ ones and at most one ascent (taken to be $0$ unless
$0 \le k \le n$).

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalZ_eq_rascalGenZ_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-z-eq-rascal-gen-z-one).

## Symmetry of Rascal numbers

For integers $n$ and $k$ with $0 \le k \le n$, the Rascal
numbers satisfy $R_{n,k} = R_{n,n-k}$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 2.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalZ_symm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-z-symm).

## Binary words with a prefix of ones and a suffix of zeros

Let $n, k, \ell, u$ be natural
numbers with $\ell \le k$ and $k + u \le n$, and let $B_k(n)$ be the set of binary words $w$ of
length $n$ with exactly $k$ ones and at most one ascent (a position $i$ with $w_i < w_{i+1}$).
The number of words in $B_k(n)$ whose first $\ell$ letters are all $1$ and whose last $u$
letters are all $0$ equals the Rascal number $R_{n-u-\ell, k-\ell}$, where
$R_{a,b} = b(a-b) + 1$ for $0 \le b \le a$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Lemma 3.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.card_prefixOnes_suffixZeros` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#card-prefix-ones-suffix-zeros).

## Fleron's recurrence for Rascal numbers

For integers $n$ and $k$ with $n \ge 2$ and
$0 < k < n$, the Rascal numbers $R_{n,k}$ satisfy
$R_{n,k} = R_{n-1,k} + R_{n-1,k-1} - R_{n-2,k-1} + 1$.

The hypothesis $0 < k < n$ is needed: at $k = 0$ or $k = n$ the right side equals $2$ while
$R_{n,k} = 1$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 4.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalZ_fleron` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-z-fleron).

## Generalized diamond recurrence for Rascal numbers

For integers $n$, $k$, $\ell$, $u$
with $\ell \ge 0$, $u \ge 0$ and $\ell \le k \le n - u$, the Rascal numbers satisfy
$R_{n,k} R_{n-u-\ell,k-\ell} = R_{n-u,k} R_{n-\ell,k-\ell} + u\ell$.

Since $R_{n-u-\ell,k-\ell} \ge 1$ under these hypotheses, this is the paper's formula
$R_{n,k} = (R_{n-u,k} R_{n-\ell,k-\ell} + u\ell) / R_{n-u-\ell,k-\ell}$ cleared of denominators.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 5.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalZ_mul_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-z-mul-eq).

## Row-shift identity for the Rascal numbers

For integers $n$, $m$ and $k$ with $m \ge 0$
and $0 \le k \le n$,

$$R_{n+m,k} = R_{n,k} + R_{m+k,k} - 1,$$

where $R_{a,b}$ denotes the Rascal numbers, which vanish unless $0 \le b \le a$.

The hypothesis $k \le n$, absent from the printed statement, is needed: for $n = 0$, $m = 1$ and
$k = 2$ the left side is $R_{1,2} = 0$ while the right side is $0 + 3 - 1 = 2$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 6.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalZ_add_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-z-add-eq).

## Diagonal recurrence for Rascal numbers

For integers $n$ and $k$ with $0 < k < n$,

$$k R_{n-1,k-1} - 1 = (k-1) R_{n,k},$$

where $R_{a,b}$ is the Rascal number, equal to $b(a-b) + 1$ for $0 \le b \le a$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 7.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.mul_rascalZ_sub_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#mul-rascal-z-sub-one).

## Row sums of the Rascal triangle

For every natural number
$n$, the Rascal numbers $R_{n,k} = k(n-k) + 1$ ($0 \le k \le n$)
satisfy $\sum_{k=0}^{n} R_{n,k} = \binom{n+1}{3} + n + 1$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 8.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalZ_row` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-z-row).

## Column sums of the Rascal triangle

For all natural numbers
$k$ and $r$, the Rascal numbers $R_{n,k} = k(n-k) + 1$
($0 \le k \le n$) satisfy
$\sum_{i=0}^{r} R_{k+i,k} = k \binom{r+1}{2} + r + 1$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 9.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalZ_column` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-z-column).

## Binomial-weighted row sums of the Rascal triangle

For
every natural number $n$, the Rascal numbers
$R_{n,k} = k(n-k) + 1$ ($0 \le k \le n$) satisfy
$2 \sum_{k=0}^{n} \binom{n}{k} R_{n,k} = 2^n \binom{n}{2} + 2^{n+1}$.

The paper prints the exponent $n - 2$ where the correct exponent
is $n - 1$ in $\sum_{k} \binom{n}{k} R_{n,k} = 2^{n-1} \binom{n}{2} + 2^n$
(at $n = 2$ the sum is $6$, not $5$); the identity is stated
doubled so that no exponent is negative at $n = 0$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 10.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.two_mul_sum_choose_mul_rascalZ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#two-mul-sum-choose-mul-rascal-z).

## Sum of the interior Rascal numbers

For every natural
number $n \ge 2$, the Rascal numbers $R_{i,j} = j(i-j) + 1$
($0 \le j \le i$) satisfy
$\sum_{i=1}^{n} \sum_{j=1}^{i-1} R_{i,j} = \binom{n+2}{4} + \binom{n}{2}$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 11.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_sum_rascalZ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-sum-rascal-z).

## Vanishing higher finite differences of Rascal numbers

For natural numbers $n$, $k$ and
$r$ with $k \le n$ and $r \ge 2$, the Rascal numbers satisfy
$\sum_{j=0}^{r} (-1)^{r-j} \binom{r}{j} R_{n+j,k} = 0$.

For $k \le n$ the value $R_{n+j,k}$ is a linear function of $j$, and the sum is its $r$-th
finite difference.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 12.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_negOnePow_choose_rascalZ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-neg-one-pow-choose-rascal-z).

## Alternating row sums of the Rascal triangle, odd rows

For every natural number $m$, the Rascal numbers
$R_{n,k} = k(n-k) + 1$ ($0 \le k \le n$) satisfy
$\sum_{k=0}^{2m+1} (-1)^k R_{2m+1,k} = 0$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 13.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalZ_alternating_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-z-alternating-odd).

## Alternating row sums of Rascal numbers on even rows

For every natural number $m$, the
Rascal numbers satisfy $\sum_{k=0}^{2m} (-1)^k R_{2m,k} = 1 - m$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 13.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalZ_alternating_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-z-alternating-even).

## Subset-sum expansion of the product of the shifted Rascal numbers

For natural numbers
$m$ and $n$ with $1 \le m \le n$, writing $[m] = \{1, \dots, m\}$,

$$\prod_{k=1}^{m} (R_{n,k} - 1) = \sum_{S \subseteq [m]} (-1)^{m-|S|} \prod_{i \in S} R_{n,i},$$

where $R_{n,k}$ denotes the Rascal numbers.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 14.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.prod_rascalZ_sub_one_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#prod-rascal-z-sub-one-eq-sum).

## Closed form for the product of the shifted Rascal numbers

For natural numbers $m$ and
$n$ with $1 \le m \le n$,

$$\prod_{k=1}^{m} (R_{n,k} - 1) = m! \, (n-1)^{\underline{m}},$$

where $R_{n,k}$ denotes the Rascal numbers and $x^{\underline{m}} = x(x-1)\cdots(x-m+1)$ is the
falling factorial.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 14.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.prod_rascalZ_sub_one_eq_factorial_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#prod-rascal-z-sub-one-eq-factorial-mul).

## Binomial coefficients from products of Rascal numbers

For natural numbers $n$ and $m$
with $1 \le m \le n$,

$$(m!)^2 \binom{n-1}{m} = \prod_{k=1}^{m} (R_{n,k} - 1),$$

where $R_{n,k} = k(n-k) + 1$ is the Rascal number for $0 \le k \le n$.

Equivalently, $\frac{1}{(m!)^2} \prod_{k=1}^{m} (R_{n,k} - 1) = \binom{n-1}{m}$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Corollary 15.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.factorial_sq_mul_choose_eq_prod` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#factorial-sq-mul-choose-eq-prod).

## Shape of ascent sequences avoiding 001 and 210

Let $n$ and $k$ be natural numbers and
let $w$ be an ascent sequence of length $n$ with exactly $k$ ascents that avoids the patterns
$001$ and $210$. Then either $w$ consists of $0, 1, \ldots, k-1$ followed by $n - k$ copies of
$k$, or there are natural numbers $x$ and $y$ with $1 \le y < n - k$ and $x < k$ such that $w$
consists of $0, 1, \ldots, k-1$, followed by $y$ copies of $k$, followed by $n - k - y$ copies
of $x$. When $k = 0$ the initial part $0, 1, \ldots, k-1$ is empty.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Lemma 16.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.ascentSeqAvoid_form` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#ascent-seq-avoid-form).

## Ascent sequences avoiding 001 and 210 are counted by Rascal numbers

For all natural
numbers $n$ and $k$, the number of ascent sequences of length $n + 1$ with exactly $k$ ascents
that avoid the patterns $001$ and $210$ equals the Rascal number $R_{n,k}$, which is
$k(n-k) + 1$ when $k \le n$ and $0$ when $k > n$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 17.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.apkCard_succ_eq_rascalZ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#apk-card-succ-eq-rascal-z).

## Generalized Fleron recurrence

Let $j \ge 1$ be a natural number and let $n$ and $k$ be
integers with $n \ge 2$ and $0 \le k \le n$. Then

$$R^{(j)}_{n,k} = R^{(j)}_{n-1,k} + R^{(j)}_{n-1,k-1} - R^{(j)}_{n-2,k-1} + R^{(j-1)}_{n-2,k-1},$$

where $R^{(i)}_{a,b}$ is the generalized Rascal number for integer indices, taken to be $0$ unless
$0 \le b \le a$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 18.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalGenZ_fleron` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-gen-z-fleron).

## Generalized Rascal numbers as sums of products of binomial coefficients

For all natural
numbers $j$, $n$ and $k$ with $k \le n$, the generalized Rascal number $R^{(j)}_{n,k}$, the
number of binary words of length $n$ with exactly $k$ ones and at most $j$ ascents (positions
where a $0$ is immediately followed by a $1$), equals
$\sum_{i=0}^{j} \binom{k}{i} \binom{n-k}{i}$.

The hypothesis $k \le n$ is needed: for $k > n$ the left side is $0$, while the right side,
with $n - k$ read as $0$, is $1$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 19.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalGen_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 335](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L335). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-gen-eq-sum).

## Row sums of generalized Rascal numbers

Write $R^{(j)}_{n,k}$ for the number of binary
words of length $n$ with exactly $k$ ones and at most $j$ ascents (positions where a $0$ is
immediately followed by a $1$). For all natural numbers $j$ and $n$,
$\sum_{k=0}^{n} R^{(j)}_{n,k} = \sum_{k=0}^{2j+1} \binom{n}{k}$, where $\binom{n}{k} = 0$ for
$k > n$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 20.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalGen_row` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 345](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L345). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-gen-row).

## A power-of-two row sum of generalized Rascal numbers

Write $R^{(j)}_{n,k}$ for the number
of binary words of length $n$ with exactly $k$ ones and at most $j$ ascents (positions where a
$0$ is immediately followed by a $1$). For every natural number $j$,
$\sum_{k=0}^{4j+3} R^{(j)}_{4j+3,k} = 2^{4j+2}$.

This was Conjecture 7.5 of Gregory et al.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Corollary 21.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalGen_four_mul_add_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-gen-four-mul-add-three).

## Forward differences of generalized Rascal row sums

Fix a natural number $j$. For natural
numbers $n$ and $k$ let $R^{(j)}_{n,k}$ be the number of binary words of length $n$ with exactly
$k$ ones and at most $j$ ascents, and let $S(n) = \sum_{k=0}^{n} R^{(j)}_{n,k}$. Then
$(\Delta^{2j+1} S)(n) = 1$ for every natural number $n$, where $\Delta$ is the forward
difference $(\Delta a)(n) = a(n+1) - a(n)$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Corollary 22.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.iterate_forwardDiff_sum_rascalGen` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 364](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L364). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#iterate-forward-diff-sum-rascal-gen).

## Alternating row sums of generalized Rascal numbers vanish on odd rows

Write
$R^{(j)}_{n,k}$ for the number of binary words of length $n$ with exactly $k$ ones and at most
$j$ ascents (positions where a $0$ is immediately followed by a $1$). For all natural numbers
$j$ and $m$, $\sum_{k=0}^{2m+1} (-1)^k R^{(j)}_{2m+1,k} = 0$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 23.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalGen_alternating_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 374](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L374). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-gen-alternating-odd).

## Alternating row sums of generalized Rascal numbers on even rows

Write $R^{(j)}_{n,k}$ for
the number of binary words of length $n$ with exactly $k$ ones and at most $j$ ascents
(positions where a $0$ is immediately followed by a $1$). For natural numbers $j$ and $m$ with
$m \ge 1$, $\sum_{k=0}^{2m} (-1)^k R^{(j)}_{2m,k} = (-1)^j \binom{m-1}{j}$, and for $m = 0$ the
sum equals $1$.

This is the paper's formula with the convention $\binom{-1}{j} = (-1)^j$ at $m = 0$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 23.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.sum_rascalGen_alternating_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#sum-rascal-gen-alternating-even).

## Generalized Rascal numbers count subsets with few small elements

For all natural numbers
$j$, $n$ and $k$, the generalized Rascal number $R^{(j)}_{n,k}$ equals the number of $k$-element
subsets of $\{0, 1, \dots, n-1\}$ that have at most $j$ elements smaller than $n - k$.

Shifting by one, these are the $k$-element subsets of $\{1, \dots, n\}$ meeting
$\{1, \dots, n-k\}$ in at most $j$ elements, which is Gregory et al.'s interpretation of
$\binom{n}{k}_j$.

## Sources

- Amelia Gibbs and Brian K. Miceli, "Two Combinatorial Interpretations of Rascal Numbers", Theorem 24.

Stated but not proved: `MathlibExt.Combinatorics.Enumerative.RascalNumbersWanted.rascalGen_eq_card_subset` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean, line 399](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/RascalNumbersWanted.lean#L399). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html#rascal-gen-eq-card-subset).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rascal triangle](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/rascal-triangle)
