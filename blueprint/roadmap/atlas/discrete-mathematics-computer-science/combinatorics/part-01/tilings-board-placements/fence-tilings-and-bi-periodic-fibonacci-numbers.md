---
declaration: section
origin: cited
lean: MetaMathlibExt.biPeriodicFibonacciSq, MetaMathlibExt.biPeriodicFibonacciSq_zero, MetaMathlibExt.biPeriodicFibonacciSq_one, MetaMathlibExt.biPeriodicFibonacciSq_two, MetaMathlibExt.biPeriodicFibonacciSq_add_three, MetaMathlibExt.fenceTilings, MetaMathlibExt.fenceTilingWeight, MetaMathlibExt.fenceTilingSum
statement: formalized
---

# Fence tilings and bi-periodic Fibonacci numbers

24 results, 15 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html).

## Bi-periodic Fibonacci numbers squared

For elements $a$ and $b$ of a field $K$, the
bi-periodic Fibonacci numbers squared $q^2_n \in K$ ($n \ge 0$) are defined by $q^2_0 = 0$,
$q^2_1 = 1$, $q^2_2 = a^2$ and, for $n \ge 3$,

$$
q^2_n = \frac{a}{b}(ab+1)\,q^2_{n-1} + (ab+1)\,q^2_{n-2} - \frac{a}{b}\,q^2_{n-3}
$$

if $n$ is even, and

$$
q^2_n = \frac{b}{a}(ab+1)\,q^2_{n-1} + (ab+1)\,q^2_{n-2} - \frac{b}{a}\,q^2_{n-3}
$$

if $n$ is odd.

Division by zero gives $0$, so the sequence is defined for all $a$ and $b$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Definition 1.1.

Formalized by `MetaMathlibExt.biPeriodicFibonacciSq`, a definition declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#bi-periodic-fibonacci-sq).

## Zeroth bi-periodic Fibonacci number squared

For elements $a$ and $b$ of a field $K$, the
bi-periodic Fibonacci number squared $q^2_0$ equals $0$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Definition 1.1.

Formalized by `MetaMathlibExt.biPeriodicFibonacciSq_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#bi-periodic-fibonacci-sq-zero).

## First bi-periodic Fibonacci number squared

For elements $a$ and $b$ of a field $K$, the
bi-periodic Fibonacci number squared $q^2_1$ equals $1$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Definition 1.1.

Formalized by `MetaMathlibExt.biPeriodicFibonacciSq_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#bi-periodic-fibonacci-sq-one).

## Second bi-periodic Fibonacci number squared

For elements $a$ and $b$ of a field $K$, the
bi-periodic Fibonacci number squared $q^2_2$ equals $a^2$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Definition 1.1.

Formalized by `MetaMathlibExt.biPeriodicFibonacciSq_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#bi-periodic-fibonacci-sq-two).

## Recurrence for the bi-periodic Fibonacci numbers squared

For elements $a$ and $b$ of a
field $K$ and every $n \ge 0$, the bi-periodic Fibonacci numbers squared $q^2_m$ satisfy

$$
q^2_{n+3} = \frac{a}{b}(ab+1)\,q^2_{n+2} + (ab+1)\,q^2_{n+1} - \frac{a}{b}\,q^2_n
$$

if $n + 3$ is even, and

$$
q^2_{n+3} = \frac{b}{a}(ab+1)\,q^2_{n+2} + (ab+1)\,q^2_{n+1} - \frac{b}{a}\,q^2_n
$$

if $n + 3$ is odd.

Division by zero gives $0$, so this holds for all $a$ and $b$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Definition 1.1, (1.1).

Formalized by `MetaMathlibExt.biPeriodicFibonacciSq_add_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#bi-periodic-fibonacci-sq-add-three).

## Fence tilings of a board

Number the half-cells of an $n$-board $0, \dots, 2n - 1$. The
tilings of the $n$-board by half-squares and $(1/2, 1/2)$-fences are encoded as the sets $F$ of
fence positions $k < 2n - 2$ (the fence at $k$ has posts on half-cells $k$ and $k + 2$) whose
posts are pairwise disjoint, that is, $k + 2 \notin F$ for every $k \in F$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Section 2.

Formalized by `MetaMathlibExt.fenceTilings`, a definition declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tilings).

## Weight of a fence tiling

Let $a$, $b$ be elements of a commutative semiring, let $n \ge 0$,
and let $F$ be a finite set of natural numbers (fence positions; the fence at $k$ has posts on
half-cells $k$ and $k + 2$). The weight of $F$ on the $n$-board is the product, over the
half-cells $h \in \{0, \dots, 2n - 1\}$ that neither lie in $F$ nor equal $k + 2$ for some
$k \in F$, of $a$ if $\lfloor h/2 \rfloor$ is even (a half-square in the odd cell
$\lfloor h/2 \rfloor + 1$) and of $b$ otherwise (a half-square in an even cell).

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Section 2.

Formalized by `MetaMathlibExt.fenceTilingWeight`, a definition declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tiling-weight).

## Weighted count of fence tilings

Let $a$, $b$ be elements of a commutative semiring and
$n \ge 0$. The weighted number $S_n$ of tilings of an $n$-board by half-squares and
$(1/2, 1/2)$-fences is the sum, over all fence tilings $F$ of the $n$-board, of the weight of $F$,
in which a half-square weighs $a$ in an odd cell and $b$ in an even cell and fences weigh $1$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Section 2 (before Lemma 2.1).

Formalized by `MetaMathlibExt.fenceTilingSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tiling-sum).

## Weighted fence tilings of the empty board

For elements $a$ and $b$ of a commutative
semiring $R$, the weighted number $S_0$ of tilings of the $0$-board by half-squares and
$(1/2, 1/2)$-fences equals $1$: the only tiling is the empty one.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, proof of Lemma 2.1.

Formalized by `MetaMathlibExt.fenceTilingSum_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tiling-sum-zero).

## Weighted fence tilings of the one-cell board

For elements $a$ and $b$ of a commutative
semiring $R$, the weighted number $S_1$ of tilings of a $1$-board by half-squares and
$(1/2, 1/2)$-fences, a half-square weighing $a$ in an odd cell and $b$ in an even cell, equals
$a^2$: the only tiling has two half-squares in cell $1$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, proof of Theorem 2.2.

Formalized by `MetaMathlibExt.fenceTilingSum_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tiling-sum-one).

## Weighted count of bifence-free fence tilings

Let $a$, $b$ be elements of a commutative
semiring and $n \ge 0$. Two fences at positions $k$ and $k + 1$ form a bifence. The weighted number
$C_n$ of tilings with no bifence is the sum of the weights, with half-square weights $a$ and $b$,
of the fence tilings $F$ of the $n$-board with no bifence, that is, with $k + 1 \notin F$ for every
$k \in F$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 3.15.

Formalized by `MetaMathlibExt.noBifenceTilingSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#no-bifence-tiling-sum).

## Tilings of the empty board with no bifence

For all elements $a$, $b$ of a commutative
semiring, the weighted number $C_0$ of tilings of the $0$-board with no bifence, with half-square
weights $a$ and $b$, equals $1$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 3.15.

Formalized by `MetaMathlibExt.noBifenceTilingSum_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#no-bifence-tiling-sum-zero).

## Weighted tilings with no free bifence

For elements $a$, $b$ of a commutative semiring
and $n \ge 0$, number the cells of an $n$-board $1, \dots, n$ and its $2n$ half-cells
$0, \dots, 2n - 1$, half-cell $h$ lying in cell $\lfloor h/2 \rfloor + 1$. A
$(1/2, 1/2)$-fence at position $k$ has its posts on half-cells $k$ and $k + 2$. Then $R_n$ is
the sum of the weights of the tilings of the board by half-squares and such fences that contain
no free bifence, that is, no two fences at positions $k$ and $k + 1$ with $k$ even. The weight
of a tiling is the product over its half-squares of $a$ for a half-square in an odd cell and
$b$ for one in an even cell.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 3.13.

Formalized by `MetaMathlibExt.noFreeBifenceTilingSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#no-free-bifence-tiling-sum).

## Tilings of the empty board with no free bifence

For all elements $a$, $b$ of a
commutative semiring, the weighted number $R_0$ of tilings of the $0$-board by half-squares and
$(1/2, 1/2)$-fences with no free bifence, with half-squares weighted by $a$ and $b$, equals $1$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 3.13.

Formalized by `MetaMathlibExt.noFreeBifenceTilingSum_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#no-free-bifence-tiling-sum-zero).

## Tilings of the one-cell board with no free bifence

For all elements $a$, $b$ of a
commutative semiring, the weighted number $R_1$ of tilings of the $1$-board with no free bifence,
with half-square weights $a$ and $b$, equals $a^2$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 3.13.

Formalized by `MetaMathlibExt.noFreeBifenceTilingSum_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#no-free-bifence-tiling-sum-one).

## Recurrence for weighted fence tilings of even boards

Let $a$ and $b$ be elements of a
commutative semiring $R$, and let $S_m$ be the weighted number of tilings of an $m$-board, with
cells numbered $1, \dots, m$, by half-squares and $(1/2, 1/2)$-fences, a half-square weighing $a$
in an odd cell and $b$ in an even cell. Then for every even $n \ge 2$,

$$
S_n = b^2 S_{n-1} + (2ab+1) S_{n-2} +
2ab \sum_{j=2}^{n/2} S_{n-2j} + 2b^2 \sum_{j=1}^{n/2-1} S_{n-2j-1}.
$$

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 2.1, (2.1).

Stated but not proved: `MetaMathlibExt.fenceTilingSum_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tiling-sum-even).

## Recurrence for weighted fence tilings of odd boards

Let $a$ and $b$ be elements of a
commutative semiring $R$, and let $S_m$ be the weighted number of tilings of an $m$-board, with
cells numbered $1, \dots, m$, by half-squares and $(1/2, 1/2)$-fences, a half-square weighing $a$
in an odd cell and $b$ in an even cell. Then for every odd $n \ge 3$,

$$
S_n = a^2 S_{n-1} + (2ab+1) S_{n-2} +
2ab \sum_{j=2}^{(n-1)/2} S_{n-2j} + 2a^2 \sum_{j=1}^{(n-1)/2} S_{n-2j-1}.
$$

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 2.1, (2.1).

Stated but not proved: `MetaMathlibExt.fenceTilingSum_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tiling-sum-odd).

## Fence tilings and the bi-periodic Fibonacci numbers squared

Let $a$ and $b$ be nonzero
elements of a field $K$. For every $n \ge 0$, let $S_n$ be the weighted number of tilings of an
$n$-board, with cells numbered $1, \dots, n$, by half-squares and $(1/2, 1/2)$-fences, a
half-square weighing $a$ in an odd cell and $b$ in an even cell. Then $S_n$ equals the
bi-periodic Fibonacci number squared $q^2_{n+1}$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Theorem 2.2.

Stated but not proved: `MetaMathlibExt.fenceTilingSum_eq_biPeriodicFibonacciSq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fence-tiling-sum-eq-bi-periodic-fibonacc).

## Squared Fibonacci numbers as a double binomial sum

Let $F_k$ denote the Fibonacci
numbers ($F_0 = 0$, $F_1 = 1$). For every natural number $n$,

$$
F_{n+1}^2 = \sum_{i=0}^{\lfloor 2n/3 \rfloor} \sum_{j=0}^{i} \binom{i}{j} \binom{2n-3i}{j} 2^j.
$$

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Corollary 3.3.

Stated but not proved: `MetaMathlibExt.fib_succ_sq_eq_sum_choose_mul_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 241](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L241). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fib-succ-sq-eq-sum-choose-mul-choose).

## Sum of squared Fibonacci numbers from three consecutive squares

Let $F_j$ denote the
$j$-th Fibonacci number, with $F_0 = 0$ and $F_1 = 1$. For every integer $n \ge 3$,

$$2 \sum_{j=1}^{n-2} F_j^2 = F_n^2 - F_{n-1}^2 - F_{n-2}^2.$$

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Corollary 3.5.

Stated but not proved: `MetaMathlibExt.two_mul_sum_fib_sq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#two-mul-sum-fib-sq).

## Squared Fibonacci numbers as weighted sums of squares

Let $F_k$ denote the Fibonacci
numbers ($F_0 = 0$, $F_1 = 1$) and let $\xi(m) = m \bmod 2$. For every natural number $n \ge 1$,

$$
F_{n+1}^2 - \xi(n+1) = \sum_{k=1}^{n} (n-k+1) F_k^2 = \sum_{k=1}^{n} k F_{n-k+1}^2.
$$

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Corollary 3.10.

Stated but not proved: `MetaMathlibExt.fib_succ_sq_sub_parity_eq_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 262](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L262). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fib-succ-sq-sub-parity-eq-sum).

## Addition formula for squared Fibonacci numbers

Let $F_k$ denote the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$). For all natural numbers $m \ge 1$ and $n \ge 2$,

$$
F_{m+n}^2 = F_{m+1}^2 F_n^2 + F_m^2 F_{n-1}^2 +
2 \left(\sum_{i=1}^{m} F_i^2\right) \left(\sum_{j=1}^{n-1} F_j^2\right).
$$

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Corollary 3.12.

Stated but not proved: `MetaMathlibExt.fib_add_sq_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#fib-add-sq-eq).

## Recurrence for weighted tilings with no free bifence

Let $a$ and $b$ be nonzero elements
of a field, and let $R_n$ be the weighted number of tilings of an $n$-board by half-squares and
$(1/2, 1/2)$-fences with no free bifence, where a half-square has weight $a$ in an odd cell and
$b$ in an even cell (cells numbered $1, \dots, n$). For every $n \ge 2$,

$$R_n = \frac{b}{a}(ab + 1) R_{n-1} + ab\, R_{n-2}$$

if $n$ is even, and

$$R_n = \frac{a}{b}(ab + 1) R_{n-1} + ab\, R_{n-2}$$

if $n$ is odd.

The initial values are $R_0 = 1$ and $R_1 = a^2$.

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 3.13.

Stated but not proved: `MetaMathlibExt.noFreeBifenceTilingSum_rec` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#no-free-bifence-tiling-sum-rec).

## Closed formula for bifence-free fence tilings

Let $a$, $b$ be nonzero elements of a field
and let $\xi(n) = n \bmod 2$. For every natural number $n$, the weighted number $C_n$ of tilings of
the $n$-board by half-squares and $(1/2, 1/2)$-fences with no bifence, with half-square weights
$a$ and $b$, is

$$
C_n = \left(\frac{a}{b}\right)^{\xi(n)}
\sum_{i=0}^{\lfloor 2n/3 \rfloor} \binom{2n-2i}{i} (ab)^{n-i}.
$$

## Sources

- Nassima Belaggoun and Hacène Belbachir, *Combinatorial Identities for the Bi-Periodic Fibonacci Numbers Squared*, The Fibonacci Quarterly 62 (2024), Article belaggoun01132024, Lemma 3.15.

Stated but not proved: `MetaMathlibExt.noBifenceTilingSum_eq_sum_choose` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/BiPeriodicFibonacciSquaredWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html#no-bifence-tiling-sum-eq-sum-choose).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fence tilings and bi-periodic Fibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/tilings-board-placements/fence-tilings-and-bi-periodic-fibonacci-numbers)
