---
declaration: section
origin: cited
lean: MetaMathlibExt.josephus, MetaMathlibExt.josephus_one, MetaMathlibExt.josephus_succ, MetaMathlibExt.josephus_range, MetaMathlibExt.josephusThreeFixedPoint, MetaMathlibExt.josephusThreeGap, MetaMathlibExt.baseThreeHalvesDigits, MetaMathlibExt.baseThreeHalvesDigits_four
statement: formalized
---

# Josephus problem

39 results, 22 proved and 17 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html).

## Josephus survivor function

For natural numbers $k$ and $n$, the Josephus function
$J_k(n)$ is defined by recursion on $n$: $J_k(0) = 0$ and
$J_k(n+1) = ((J_k(n) + k - 1) \bmod (n+1)) + 1$, where subtraction of natural numbers is
truncated at $0$.

For $k \ge 2$ and $n \ge 1$, $J_k(n)$ is the one-based position of the sole survivor when every
$k$-th person is eliminated from a circle of $n$ people; the value $J_k(0) = 0$ only anchors the
recursion.

Formalized by `MetaMathlibExt.josephus`, a definition declared in [MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus).

## The Josephus function at one

For every natural number $k \ge 2$, the Josephus function
$J_k$ for elimination step $k$ satisfies $J_k(1) = 1$.

Formalized by `MetaMathlibExt.josephus_one`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-one).

## Euler recurrence for the Josephus function

For all natural numbers $k \ge 2$ and
$n \ge 1$, the Josephus function $J_k$ for elimination step $k$ satisfies
$J_k(n+1) = ((J_k(n) + k - 1) \bmod (n+1)) + 1$.

Formalized by `MetaMathlibExt.josephus_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-succ).

## Range of the Josephus function

For all natural numbers $k \ge 2$ and $n \ge 1$, the
Josephus function $J_k$ for elimination step $k$ satisfies $1 \le J_k(n) \le n$.

Formalized by `MetaMathlibExt.josephus_range`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/JosephusFunction.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-range).

## Enumeration of the positive fixed points of $J_3$

Let $J_3$ be the Josephus function
with step $3$. For $\ell \in \mathbb{N}$, $n_\ell$ is the $\ell$-th element, in increasing order
and counting from $\ell = 0$, of the set of natural numbers $n \ge 1$ with $J_3(n) = n$. Thus
$n_\ell$ is the paper's $n_p^{(\ell+1)}$.

If this set has at most $\ell$ elements, then $n_\ell = 0$ by convention.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.josephusThreeFixedPoint`, a definition declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point).

## Gaps between consecutive positive fixed points of $J_3$

Let $J_3$ be the Josephus
function with step $3$ and let $n_\ell$ be the $\ell$-th natural number $n \ge 1$ with
$J_3(n) = n$, in increasing order and counting from $\ell = 0$. For $\ell \in \mathbb{N}$, the gap
$g_\ell$ is the number of natural numbers $n$ with $n_\ell < n < n_{\ell+1}$ and
$J_3(n) + 1 = n$, that is, the number of pure high extremal points strictly between $n_\ell$ and
$n_{\ell+1}$. Thus $g_\ell$ is the paper's $\bar m_{\ell+1}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.josephusThreeGap`, a definition declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-gap).

## Base-3/2 digits

The base-$3/2$ digit list of a natural number $N$, least significant
digit first, is defined by recursion on $N$: the list of $0$ is empty, and for $N \ge 1$ it is
the digit $d = 2N \bmod 3$ followed by the base-$3/2$ digit list of $(2N - d)/3$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.baseThreeHalvesDigits`, a definition declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#base-three-halves-digits).

## Base-3/2 digits of four

The base-$3/2$ digit list of $4$, written least significant
digit first, is $(2, 1, 2)$; written most significant digit first, this is the paper's
$(212)_{3/2}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.baseThreeHalvesDigits_four`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#base-three-halves-digits-four).

## Base-3/2 digits of thirteen

The base-$3/2$ digit list of $13$, written least
significant digit first, is $(2, 1, 1, 0, 1, 2)$; written most significant digit first, this
is the paper's $(210112)_{3/2}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.baseThreeHalvesDigits_thirteen`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#base-three-halves-digits-thirteen).

## Value of the base-3/2 digits

For every natural number $N$, if
$(d_0, d_1, \dots, d_{k-1})$ is the base-$3/2$ digit list of $N$, least significant digit first,
then in $\mathbb{Q}$

$$2N = \sum_{i=0}^{k-1} d_i \left(\frac{3}{2}\right)^i.$$

Equivalently, the paper's expansion $\frac{1}{2} \sum_{i} d_i (3/2)^i$ has value $N$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.baseThreeHalvesDigits_value`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#base-three-halves-digits-value).

## Base-3/2 digits are at most two

For every natural number $N$, every digit $d$ in the
base-$3/2$ digit list of $N$ satisfies $d < 3$, that is, $d \in \{0, 1, 2\}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.baseThreeHalvesDigits_lt_three`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#base-three-halves-digits-lt-three).

## The first positive fixed point of $J_3$ is $1$

Let $J_3$ be the Josephus function with
step $3$ and let $n_\ell$ be the $\ell$-th natural number $n \ge 1$ with $J_3(n) = n$, in
increasing order and counting from $\ell = 0$. Then $n_0 = 1$; this is the paper's $n_p^{(1)}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.josephusThreeFixedPoint_zero`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-zero).

## Second positive fixed point of the Josephus function for step three

Let $J_3$ be the
Josephus function with elimination step $3$. The second smallest positive integer $n$ with
$J_3(n) = n$ is $2$; in the zero-indexed enumeration $n_0 < n_1 < \cdots$ of these fixed points,
$n_1 = 2$, the paper's $n_p^{(2)}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.josephusThreeFixedPoint_one`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-one).

## The third positive fixed point of $J_3$ is $13$

Let $J_3$ be the Josephus function with
step $3$ and let $n_\ell$ be the $\ell$-th natural number $n \ge 1$ with $J_3(n) = n$, in
increasing order and counting from $\ell = 0$. Then $n_2 = 13$; this is the paper's $n_p^{(3)}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.josephusThreeFixedPoint_two`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-two).

## The second gap between positive fixed points of $J_3$ is $3$

Let $J_3$ be the Josephus
function with step $3$, let $n_\ell$ be the $\ell$-th natural number $n \ge 1$ with
$J_3(n) = n$ (in increasing order, counting from $\ell = 0$), and let $g_\ell$ be the number of
natural numbers $n$ with $n_\ell < n < n_{\ell+1}$ and $J_3(n) + 1 = n$. Then $g_1 = 3$; this is
the paper's $\bar m_2 = 3$.

Here $n_1 = 2$ and $n_2 = 13$, and the three pure high extremal points counted are $3$, $5$ and $8$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Formalized by `MetaMathlibExt.josephusThreeGap_one`, a theorem declared in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-gap-one).

## Base-3/2 digits of the next Josephus fixed point, gap zero

Let $J_3$ be the Josephus
function with elimination step $3$, let $n_\ell$ be the $\ell$-th positive fixed point of $J_3$
in increasing order (counting from $\ell = 0$), and let $m_\ell$ be the number of integers $n$
with $n_\ell < n < n_{\ell+1}$ and $J_3(n) + 1 = n$ (the pure high extremal points between
them). For every $\ell$, if $m_\ell = 0$, then the base-$3/2$ digit list of $n_{\ell+1}$, least
significant digit first, is the digit $1$ followed by the digit list of $n_\ell$.

This is part (i) of the cited Theorem 1.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Stated but not proved: `MetaMathlibExt.josephusThreeFixedPoint_digits_of_gap_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-digits-of-gap).

## Base-3/2 digits of the next Josephus fixed point, gap one

Let $J_3$ be the Josephus
function with elimination step $3$, let $n_\ell$ be the $\ell$-th positive fixed point of $J_3$
in increasing order (counting from $\ell = 0$), and let $m_\ell$ be the number of integers $n$
with $n_\ell < n < n_{\ell+1}$ and $J_3(n) + 1 = n$ (the pure high extremal points between
them). For every $\ell$, if $m_\ell = 1$, then the base-$3/2$ digit list of $n_{\ell+1}$, least
significant digit first, is the digits $2, 0$ followed by the digit list of $n_\ell$.

This is part (ii) of the cited Theorem 1.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Stated but not proved: `MetaMathlibExt.josephusThreeFixedPoint_digits_of_gap_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-digits-of-gap-2).

## Base-3/2 digits of the next Josephus fixed point, gap at least two

Let $J_3$ be the
Josephus function with elimination step $3$, let $n_\ell$ be the $\ell$-th positive fixed point
of $J_3$ in increasing order (counting from $\ell = 0$), and let $m_\ell$ be the number of
integers $n$ with $n_\ell < n < n_{\ell+1}$ and $J_3(n) + 1 = n$ (the pure high extremal points
between them). For every $\ell$, if $m_\ell \ge 2$, then the base-$3/2$ digit list of
$n_{\ell+1}$, least significant digit first, is the digit $2$, then $m_\ell - 1$ digits equal to
$1$, then the digit $0$, followed by the digit list of $n_\ell$.

Written most significant digit first, this appends to the digits of $n_\ell$ a $0$, then
$m_\ell - 1$ ones, then a $2$. This is part (iii) of the cited Theorem 1.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Stated but not proved: `MetaMathlibExt.josephusThreeFixedPoint_digits_of_gap_at_least_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-digits-of-gap-3).

## Digit count of consecutive Josephus fixed points

Let $J_3$ be the Josephus function
with elimination step $3$, let $n_\ell$ be the $\ell$-th positive fixed point of $J_3$ in
increasing order (counting from $\ell = 0$), and let $m_\ell$ be the number of integers $n$ with
$n_\ell < n < n_{\ell+1}$ and $J_3(n) + 1 = n$ (the pure high extremal points between them).
For every $\ell$, the base-$3/2$ digit list of $n_{\ell+1}$ has exactly $m_\ell + 1$ more digits
than the base-$3/2$ digit list of $n_\ell$.

This is part (iv) of the cited Theorem 1.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *Fixed Points of the Josephus Function via Fractional Base Expansions*, INTEGERS 26 (2026), Article A54, Theorem 1.

Stated but not proved: `MetaMathlibExt.josephusThreeFixedPoint_digits_length` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusBaseThreeHalvesWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-digits-length).

## High extremal points of the Josephus function $J_3$

A natural number $n$ is a high
extremal point of the Josephus function $J_3$ (elimination step $3$) when $n \ge 1$ and either
$J_3(n) = n$ or $J_3(n) = n - 1$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Section 1, Definition (Extremal and Fixed points).

Formalized by `MetaMathlibExt.IsJosephusThreeHighExtremal`, a definition declared in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#is-josephus-three-high-extremal).

## Fixed points of the Josephus function $J_3$

A natural number $n$ is a fixed point of the
Josephus function $J_3$ (elimination step $3$) when $n \ge 1$ and $J_3(n) = n$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Section 1, Definition (Extremal and Fixed points).

Formalized by `MetaMathlibExt.IsJosephusThreeFixedPoint`, a definition declared in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#is-josephus-three-fixed-point).

## $3$ is a high extremal point but not a fixed point of $J_3$

The number $3$ is a high
extremal point of the Josephus function $J_3$ (elimination step $3$) and is not a fixed point of
$J_3$; indeed $J_3(3) = 2$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Section 1, Definition (Extremal and Fixed points).

Formalized by `MetaMathlibExt.isJosephusThreeHighExtremal_three`, a theorem declared in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#is-josephus-three-high-extremal-three).

## $4$ is not a high extremal point of $J_3$

The number $4$ is not a high extremal point of
the Josephus function $J_3$ (elimination step $3$).

Indeed $J_3(4) = 1$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Section 1, Definition (Extremal and Fixed points).

Formalized by `MetaMathlibExt.not_isJosephusThreeHighExtremal_four`, a theorem declared in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#not-is-josephus-three-high-extremal-four).

## $13$ is a fixed point of $J_3$

The number $13$ is a fixed point of the Josephus function
$J_3$ (elimination step $3$), that is, $J_3(13) = 13$.

It is the third fixed point of $J_3$, after $1$ and $2$; the statement records only that $13$ is
a fixed point.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Section 2, Table 1.

Formalized by `MetaMathlibExt.isJosephusThreeFixedPoint_thirteen`, a theorem declared in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#is-josephus-three-fixed-point-thirteen).

## Successive high extremal points of $J_3$

For every natural number $i$, let $a$ and $b$ be
the $(i+1)$-th and $(i+2)$-th smallest high extremal points of the Josephus function $J_3$, and
put $f = a - J_3(a)$, $f' = b - J_3(b)$ and $r = a \bmod 2$. If $(f, r) = (1, 0)$, then
$2b = 3a + 2$ and $f' = 0$; if $(f, r) = (1, 1)$, then $2b = 3a + 1$ and $f' = 1$; if
$(f, r) = (0, 0)$, then $2b = 3a$ and $f' = 1$; if $(f, r) = (0, 1)$, then $2b = 3a + 1$ and
$f' = 0$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Theorem 1.

Stated but not proved: `MetaMathlibExt.josephusThree_highExtremal_succ_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-high-extremal-succ-cases).

## Unified recurrences for consecutive high extremal points of $J_3$

For every natural
number $i$, let $a$ and $b$ be the $(i+1)$-th and $(i+2)$-th smallest high extremal points of the
Josephus function $J_3$. In the integers, put $r = a \bmod 2$, $f = a - J_3(a)$ and
$s = \lfloor (3a + 2 - r)/2 \rfloor \bmod 2$. Then

$$2b = 3a + 1 + (1 - r)(2f - 1), \qquad 2J_3(b) = 3a + (2 - 3r)(2f - 1),$$



$$b - J_3(b) = f - (1 - r)(2f - 1), \qquad b \bmod 2 = s - (1 - r)(1 - f)(2s - 1).$$

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Lemma 1.

Stated but not proved: `MetaMathlibExt.josephusThree_highExtremal_recurrences` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-high-extremal-recurrences).

## Recurrence for consecutive fixed points of $J_3$

For every natural number $\ell$, let $a$
and $b$ be the $(\ell+1)$-th and $(\ell+2)$-th smallest fixed points of the Josephus function
$J_3$, and let $m = \nu_2(3a + 2)$ be the $2$-adic valuation of $3a + 2$. Then exactly $m$
natural numbers $n$ with $a < n < b$ satisfy $J_3(n) = n - 1$ (the pure high extremal points
between $a$ and $b$), and $2^{m+1} b + 2^m = 3^m (3a + 2)$, that is,
$b = (3^m (3a + 2) - 2^m) / 2^{m+1}$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Theorem 2.

Stated but not proved: `MetaMathlibExt.josephusThree_fixedPoint_recurrence` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-fixed-point-recurrence).

## The Josephus function between consecutive fixed points

For every natural number $\ell$,
let $a$ and $b$ be the $(\ell+1)$-th and $(\ell+2)$-th smallest fixed points of the Josephus
function $J_3$, and let $m = \nu_2(3a + 2)$ be the $2$-adic valuation of $3a + 2$. For every
natural number $n$ with $a + 1 \le n \le b$, put
$\mathfrak{m} = \lceil \log_{3/2}((2n + 1)/(3a + 2)) \rceil$; then, in the real numbers,

$$J_3(n) = 3n + 1 - \left(\tfrac{2}{3}\right)^{m - \mathfrak{m}} (2b + 1).$$

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, *On the Recurrence Formula for Fixed Points of the Josephus Function*, INTEGERS 24 (2024), Article A115, Theorem 3.

Stated but not proved: `MetaMathlibExt.josephusThree_eq_of_mem_fixedPoint_interval` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusFixedPointRecurrenceWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-three-eq-of-mem-fixed-point-int).

## Low extremal point of the Josephus function

For natural numbers $k$ and $m$, the point
$m$ is a low extremal point of the Josephus function $J_k$ if $1 \le J_k(m) \le k - 1$, where
$k - 1$ is truncated at $0$.

Formalized by `MathlibExt.NumberTheory.JosephusWanted.IsLowExtremal`, a definition declared in [WantedExt/NumberTheory/JosephusWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#is-low-extremal).

## High extremal point of the Josephus function

For natural numbers $k$ and $m$, the point
$m$ is a high extremal point of the Josephus function $J_k$ if $m + 1$ is a low extremal point
of $J_k$, that is, if $1 \le J_k(m + 1) \le k - 1$.

Formalized by `MathlibExt.NumberTheory.JosephusWanted.IsHighExtremal`, a definition declared in [WantedExt/NumberTheory/JosephusWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#is-high-extremal).

## Josephus recurrence by number of wrap-arounds

Let $k \ge 2$ and $n \ge 1$ be natural
numbers, let $J_k$ be the Josephus function and write $p = J_k(n)$. If $\ell$ is a natural
number with $\ell(n+1) + 1 \le p + k \le (\ell+1)(n+1)$, then $J_k(n+1) = p + k - \ell(n+1)$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.josephus_succ_eq_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-succ-eq-sub).

## The Josephus function just after a fixed point

Let $k \ge 2$ and $n_p \ge 1$ be natural
numbers with $J_k(n_p) = n_p$, where $J_k$ is the Josephus function. Then $J_k(n_p + 1)$ is
determined as follows: (i) if $k \le n_p + 1$, then $J_k(n_p + 1) = k - 1$; (ii) if
$k = \ell(n_p + 1) + 1$ for some natural number $\ell \ge 1$, then $J_k(n_p + 1) = n_p + 1$;
(iii) if $k = \ell(n_p + 1) + k_1$ for some natural numbers $\ell \ge 1$ and $k_1$ with
$2 \le k_1 \le n_p$, then $J_k(n_p + 1) = k_1 - 1$; (iv) if $k = (\ell + 1)(n_p + 1)$ for some
natural number $\ell \ge 1$, then $J_k(n_p + 1) = n_p$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Proposition 4.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.josephus_fixed_succ_cases` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-fixed-succ-cases).

## Josephus fixed points detected by the next value

Let $k \ge 2$ and $n_p$ be natural
numbers with $n_p \ge k - 1$, and let $J_k$ be the Josephus function. Then $J_k(n_p) = n_p$ if
and only if $J_k(n_p + 1) = k - 1$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Proposition 4.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.josephus_eq_self_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-eq-self-iff).

## Linear growth of the Josephus function before a wrap-around

Let $k \ge 2$, $n \ge 1$
and $m$ be natural numbers, let $J_k$ be the Josephus function and write $p = J_k(n)$. If
$p + km \le n + m$, then $J_k(n + m) = p + km$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Lemma 6.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.josephus_add_eq_of_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-add-eq-of-le).

## The Josephus function at the first wrap-around

Let $k \ge 2$, $n \ge 1$ and $m$ be
natural numbers and let $J_k$ be the Josephus function. Suppose that $m$ is the least natural
number with $J_k(n) + km > n + m$, and that moreover $J_k(n) + km \le 2(n + m)$. Then
$J_k(n + m) = J_k(n) + km - (n + m)$.

The second hypothesis, which allows only one wrap-around, is not in the printed lemma; without it
the statement fails at $k = 4$, $n = 1$, $m = 1$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Lemma 6.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.josephus_add_eq_sub_of_minimal` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-add-eq-sub-of-minimal).

## Extremal points of the Josephus function near $2k - 2$

Let $k \ge 2$ be a natural
number and let $J_k$ be the Josephus function; call $m$ low extremal if $1 \le J_k(m) \le k - 1$,
and high extremal if $m + 1$ is low extremal. If $J_k(2k - 2) \le k - 1$, then $2k - 3$ is high
extremal and $2k - 2$ is low extremal. If $J_k(2k - 2) > k - 1$, then $2k - 2$ is high extremal
and $2k - 1$ is low extremal. In particular, $2k - 2$ is always a low or a high extremal point.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Corollary 7.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.extremal_two_mul_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#extremal-two-mul-sub).

## Linear-step bound at a low extremal point

Let $k \ge 2$ and $n$ be natural numbers, let
$J_k$ be the Josephus function, write $j = J_k(n+1)$, and suppose $j \le k - 1$. Then for every
natural number $m$, $j + km \le n + 1 + m$ holds if and only if
$m \le \lfloor (n - (j - 1)) / (k - 1) \rfloor$. Moreover, if $k - 2 + j \le n$, then
$\lfloor (n - (j - 1)) / (k - 1) \rfloor \ge 1$.

Since $1 \le J_k(n+1) \le n + 1$, the hypothesis says $j \in [1, k - 1]$, that is, $n + 1$ is a
low extremal point in the paper's sense, and none of the subtractions above is truncated.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Lemma 8.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.shift_le_iff_le_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#shift-le-iff-le-div).

## Linear growth of the Josephus function after a high extremal point

Let $k \ge 2$ and
$n_e \ge 2k - 3$ be natural numbers such that $n_e$ is a high extremal point of the Josephus
function $J_k$, that is, $1 \le J_k(n_e + 1) \le k - 1$, and write $j = J_k(n_e + 1)$. Then
$J_k(n_e + 1 + m) = j + km$ for every natural number
$m \le \lfloor (n_e - (j - 1)) / (k - 1) \rfloor$.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Theorem 9.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.josephus_add_eq_of_high` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#josephus-add-eq-of-high).

## The Josephus function has infinitely many fixed points

For every natural number
$k \ge 2$, the set of natural numbers $n$ with $J_k(n) = n$ is infinite, where $J_k$ is the
Josephus function.

## Sources

- Yunier Bello-Cruz and Roy Quintero-Contreras, "Analytical Study and Efficient Evaluation of the Josephus Function", Theorem 13.

Stated but not proved: `MathlibExt.NumberTheory.JosephusWanted.infinite_fixedPoints` is written with `theorem_wanted` in [WantedExt/NumberTheory/JosephusWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/JosephusWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html#infinite-fixed-points).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Josephus problem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential/josephus-problem)
