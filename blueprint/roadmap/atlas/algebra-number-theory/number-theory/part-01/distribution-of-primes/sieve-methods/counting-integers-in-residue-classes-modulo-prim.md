---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.onesDiagDet, MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.borderedOnesDiag, MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.borderedOnesDiagDet, MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.firstPrimes, MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.residueHitCount, MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.availableCount, MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.freeCount, MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.occupiedCount
statement: formalized
---

# Counting integers in residue classes modulo primes

20 results, 8 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html).

## Ones-diagonal determinant

For natural numbers $p_1, \dots, p_k$, the determinant
$A_k(p_1, \dots, p_k)$ is the determinant of the $k \times k$ integer matrix with
$p_1, \dots, p_k$ on the diagonal and $1$ in every other entry.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.onesDiagDet`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#ones-diag-det).

## Bordered ones-diagonal matrix

For natural numbers $p_1, \dots, p_k$, the
$(k+1) \times (k+1)$ integer matrix whose first row consists of ones and whose row $i + 1$, for
$1 \le i \le k$, has $p_i$ in column $i$ and $1$ in every other column. Equivalently, it is the
$k \times k$ matrix with diagonal entries $p_1, \dots, p_k$ and all other entries $1$, with a
column of ones appended on the right and then a row of ones placed on top.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.borderedOnesDiag`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#bordered-ones-diag).

## Bordered ones-diagonal determinant

For natural numbers $p_1, \dots, p_k$, the integer
$F_k(p_1, \dots, p_k)$ is $(-1)^k$ times the determinant of the bordered ones-diagonal matrix of
$p_1, \dots, p_k$: the $(k+1) \times (k+1)$ integer matrix whose first row consists of ones and
whose row $i + 1$, for $1 \le i \le k$, has $p_i$ in column $i$ and $1$ in every other column.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.borderedOnesDiagDet`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#bordered-ones-diag-det).

## The first primes

For a natural number $k$, the $k$-tuple whose entry with index $i$, for
$0 \le i < k$, is the $(i+1)$-st prime; that is, the first $k$ primes $2, 3, 5, \dots$ in
increasing order.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.firstPrimes`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#first-primes).

## Residue hit count

For natural numbers $p_1, \dots, p_k$, $r_1, \dots, r_k$ and $n$, the
residue hit count $\gamma(n)$ is the number of indices $i$ with $n \equiv r_i \pmod{p_i}$, that
is, the number of the residue classes $r_i \bmod p_i$ that contain $n$.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.residueHitCount`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#residue-hit-count).

## Number of available integers

For natural numbers $p_1, \dots, p_k$ and $r_1, \dots, r_k$,
let $\gamma(n)$ be the number of indices $i$ with $n \equiv r_i \pmod{p_i}$, and call $n$ available
if $\gamma(n) \le 1$. This is the number of available integers $n$ with
$1 \le n \le p_1 p_2 \cdots p_k$. For the first $k$ primes it is the count written
$\mathrm{av}(k)$.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.availableCount`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#available-count).

## Free count

For natural numbers $p_1, \dots, p_k$ and $r_1, \dots, r_k$, let $\gamma(n)$
be the number of indices $i$ with $n \equiv r_i \pmod{p_i}$. The free count is the number of
integers $n$ with $1 \le n \le p_1 \cdots p_k$ and $\gamma(n) = 0$.

When $p_1, \dots, p_k$ are the first $k$ primes, this is the count $\mathrm{free}(k)$ of
Pausinger's paper.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.freeCount`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#free-count).

## Occupied count

For natural numbers $p_1, \dots, p_k$ and $r_1, \dots, r_k$, let
$\gamma(n)$ be the number of indices $i$ with $n \equiv r_i \pmod{p_i}$. The occupied count is
the number of integers $n$ with $1 \le n \le p_1 \cdots p_k$ and $\gamma(n) > 1$.

When $p_1, \dots, p_k$ are the first $k$ primes, this is the count $\mathrm{occ}(k)$ of
Pausinger's paper.

Formalized by `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.occupiedCount`, a definition declared in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#occupied-count).

## Recurrence for the bordered determinants of the first primes

Let $k \ge 2$ and let
$p_1, \dots, p_k$ be the first $k$ primes. For $m \le k$ let $f_m = F_m(p_1, \dots, p_m)$, where
$F_m(p_1, \dots, p_m)$ is $(-1)^m$ times the determinant of the $(m+1) \times (m+1)$ matrix whose
first row consists of ones and whose row $i + 1$, for $1 \le i \le m$, has $p_i$ in column $i$ and
$1$ in every other column. Then $f_k = (p_k - 1) f_{k-1}$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.borderedOnesDiagDet_firstPrimes_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#bordered-ones-diag-det-first-primes-recu).

## Lemma 2, determinant recurrence

Let $p_1 < p_2 < \cdots$ be the primes in increasing
order. For $m \ge 0$ let $a_m$ be the determinant of the $m \times m$ integer matrix with
$p_1, \dots, p_m$ on the diagonal and $1$ in every other entry, and let $f_m = (-1)^m \det B_m$,
where $B_m$ is the $(m+1) \times (m+1)$ integer matrix whose first row consists of ones and
whose row $i + 1$, for $1 \le i \le m$, has $p_i$ in column $i$ and $1$ in every other column.
Then for every $k \ge 2$, $a_k = f_{k-1} + (p_k - 1) \cdot a_{k-1}$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.onesDiagDet_firstPrimes_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#ones-diag-det-first-primes-recurrence).

## Lemma 3, occupied recurrence

Let $k \ge 1$, let $p_1 < p_2 < \cdots$ be the primes in
increasing order, and let $r_1, \dots, r_{k+1}$ be natural numbers. For $m \in \{k, k + 1\}$
write $P_m = p_1 \cdots p_m$, let $\gamma_m(n)$ be the number of $i \le m$ with
$n \equiv r_i \pmod{p_i}$, let $\mathrm{occ}(m)$ be the number of integers $n$ with
$1 \le n \le P_m$ and $\gamma_m(n) > 1$, and let $\mathrm{free}(m)$ be the number of those with
$\gamma_m(n) = 0$. Then
$\mathrm{occ}(k+1) + \mathrm{free}(k) = P_k + (p_{k+1} - 1) \cdot \mathrm{occ}(k)$.

In the paper's form this reads
$\mathrm{occ}(k+1) = P_k + (p_{k+1} - 1) \cdot \mathrm{occ}(k) - \mathrm{free}(k)$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.occupiedCount_firstPrimes_succ_add_free` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#occupied-count-first-primes-succ-add-fre).

## Lemma 3, free recurrence

Let $k \ge 1$, let $p_1 < p_2 < \cdots$ be the primes in
increasing order, and let $r_1, \dots, r_{k+1}$ be natural numbers. For $m \in \{k, k + 1\}$
write $\mathrm{free}(m)$ for the number of integers $n$ with $1 \le n \le p_1 \cdots p_m$ such
that $n \not\equiv r_i \pmod{p_i}$ for every $i \le m$. Then
$\mathrm{free}(k+1) = (p_{k+1} - 1) \cdot \mathrm{free}(k)$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.freeCount_firstPrimes_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#free-count-first-primes-succ).

## Recurrence for the number of available integers

Let $k \ge 1$, let $p_1, \dots, p_{k+1}$
be the first $k + 1$ primes, and let $r_1, \dots, r_{k+1}$ be any natural numbers. For $m = k$ and
$m = k + 1$, call an integer $n$ free if $n \not\equiv r_i \pmod{p_i}$ for every $i \le m$, and
available if $n \equiv r_i \pmod{p_i}$ for at most one $i \le m$; let $\mathrm{av}(m)$ and
$\mathrm{free}(m)$ be the numbers of available and of free integers $n$ with
$1 \le n \le p_1 \cdots p_m$. Then
$\mathrm{av}(k+1) = (p_{k+1} - 1) \cdot \mathrm{av}(k) + \mathrm{free}(k)$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 4.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.availableCount_firstPrimes_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#available-count-first-primes-succ).

## Available integers for the first primes

Let $k$ be a natural number, let
$p_1, \dots, p_k$ be the first $k$ primes, and let $r_1, \dots, r_k$ be any natural numbers. Call an
integer $n$ available if $n \equiv r_i \pmod{p_i}$ holds for at most one index $i$. Then the number
of available integers $n$ with $1 \le n \le p_1 p_2 \cdots p_k$ equals
$a_k = A_k(p_1, \dots, p_k)$, the determinant of the $k \times k$ matrix with diagonal entries
$p_1, \dots, p_k$ and all other entries $1$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.availableCount_firstPrimes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#available-count-first-primes).

## Theorem 1, free count

Let $k$ be a natural number, let $p_1 < \cdots < p_k$ be the
first $k$ primes and let $r_1, \dots, r_k$ be natural numbers. Then the number of integers $n$
with $1 \le n \le p_1 \cdots p_k$ such that $n \not\equiv r_i \pmod{p_i}$ for every $i$ equals
$f_k = (-1)^k \det B$, where $B$ is the $(k+1) \times (k+1)$ integer matrix whose first row
consists of ones and whose row $i + 1$, for $1 \le i \le k$, has $p_i$ in column $i$ and $1$ in
every other column.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.freeCount_firstPrimes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#free-count-first-primes).

## Available integers for two distinct primes

Let $p \ne q$ be primes and let $r_1, r_2$ be
any natural numbers. Call an integer $n$ available if it satisfies at most one of the congruences
$n \equiv r_1 \pmod p$ and $n \equiv r_2 \pmod q$. Then the number of available integers $n$ with
$1 \le n \le pq$ equals $A_2(p, q)$, the determinant of the $2 \times 2$ matrix with diagonal
entries $p, q$ and both other entries $1$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.availableCount_two_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#available-count-two-primes).

## Lemma 5, free count

Let $p$ and $q$ be distinct primes and let $r_1, r_2$ be natural
numbers. Then the number of integers $n$ with $1 \le n \le pq$ such that
$n \not\equiv r_1 \pmod p$ and $n \not\equiv r_2 \pmod q$ equals $F_2(p, q)$, where

$$F_2(p, q) = \det \begin{pmatrix} 1 & 1 & 1 \\ p & 1 & 1 \\ 1 & q & 1 \end{pmatrix}.$$

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.freeCount_two_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#free-count-two-primes).

## Available integers for three distinct primes

Let $p$, $q$, $s$ be pairwise distinct
primes and let $r_1, r_2, r_3$ be any natural numbers. Call an integer $n$ available if it satisfies
at most one of the congruences $n \equiv r_1 \pmod p$, $n \equiv r_2 \pmod q$ and
$n \equiv r_3 \pmod s$. Then the number of available integers $n$ with $1 \le n \le pqs$ equals
$A_3(p, q, s)$, the determinant of the $3 \times 3$ matrix with diagonal entries $p, q, s$ and all
other entries $1$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Lemma 6.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.availableCount_three_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#available-count-three-primes).

## Available integers for distinct primes

Let $k \ge 2$, let $p_1, \dots, p_k$ be pairwise
distinct primes, and let $r_1, \dots, r_k$ be any natural numbers. Call an integer $n$ available if
$n \equiv r_i \pmod{p_i}$ holds for at most one index $i$. Then the number of available integers $n$
with $1 \le n \le p_1 p_2 \cdots p_k$ equals $A_k(p_1, \dots, p_k)$, the determinant of the
$k \times k$ matrix with diagonal entries $p_1, \dots, p_k$ and all other entries $1$.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.availableCount_distinct_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#available-count-distinct-primes).

## Theorem 2, free count

Let $k \ge 2$, let $p_1, \dots, p_k$ be distinct primes and
let $r_1, \dots, r_k$ be natural numbers. Then the number of integers $n$ with
$1 \le n \le p_1 p_2 \cdots p_k$ such that $n \not\equiv r_i \pmod{p_i}$ for every $i$ equals
$F_k(p_1, \dots, p_k) = (-1)^k \det B$, where $B$ is the $(k+1) \times (k+1)$ integer matrix
whose first row consists of ones and whose row $i + 1$, for $1 \le i \le k$, has $p_i$ in
column $i$ and $1$ in every other column.

## Sources

- Florian Pausinger, "Counting Appearances of Integers in Sets of Arithmetic Progressions", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.CountingAppearancesProgressionsWanted.freeCount_distinct_primes` is written with `theorem_wanted` in [WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/CountingAppearancesProgressionsWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html#free-count-distinct-primes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Counting integers in residue classes modulo primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/sieve-methods/counting-integers-in-residue-classes-modulo-prim)
