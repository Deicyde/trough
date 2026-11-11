---
declaration: section
origin: cited
lean: MetaMathlibExt.fib_odd_mul_goldenRatio, MetaMathlibExt.exists_odd_fib_representation, MetaMathlibExt.pellNumber_odd_mul_one_add_sqrt_two, MetaMathlibExt.exists_two_pell_halfCompanion_representation, MetaMathlibExt.exists_pell_halfCompanion_representation, MetaMathlibExt.bronzeLucasParams, MetaMathlibExt.lucasU_bronzeLucasParams_add_two, MetaMathlibExt.lucasU_bronzeLucasParams_values
statement: formalized
---

# Numeration by Fibonacci and Pell numbers

26 results, 10 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html).

## Odd-indexed Fibonacci numbers times the golden ratio

Let $F_n$ be the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$) and $\varphi = (1 + \sqrt 5)/2$ the golden
ratio. For every natural number $k$,
$F_{2k+1} \varphi = F_{2k+2} + \left((\sqrt 5 - 1)/2\right)^{2k+1}$ and
$F_{2k+1} (1 + \varphi) = F_{2k+3} + \left((\sqrt 5 - 1)/2\right)^{2k+1}$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Proposition 1.

Stated but not proved: `MetaMathlibExt.fib_odd_mul_goldenRatio` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#fib-odd-mul-golden-ratio).

## Numeration by odd-indexed Fibonacci numbers

Let $F_n$ be the Fibonacci numbers
($F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$). For every positive integer $t$ there are a
natural number $n$ and natural numbers $a_0, a_1, a_2, \dots$ such that
$F_{2n+1} \le t < F_{2n+3}$, $t = \sum_{k=0}^{n} a_k F_{2k+1}$, $a_0 \le 1$, $a_k \le 2$ for
every $k \ge 1$, $a_1 = 2$ and $a_0 = 1$ do not both hold, and for no $k$ do $a_{k+1} = 2$ and
$a_k = 2$ both hold.

Here $a_k$ is the coefficient the paper calls $a_{2k+1}$; the last two conditions exclude the
digit patterns $2F_3 + F_1$ and $2F_{2k+3} + 2F_{2k+1}$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 1.

Stated but not proved: `MetaMathlibExt.exists_odd_fib_representation` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#exists-odd-fib-representation).

## Odd Pell and even Pell–Lucas numbers times $1 + \sqrt 2$

Let $P_n$ be the Pell numbers and
$H_n$ the Pell–Lucas numbers ($H_0 = H_1 = 1$, $H_{n+2} = 2H_{n+1} + H_n$). For every natural
number $k$, $P_{2k+1}(1 + \sqrt 2) = P_{2k+2} + (\sqrt 2 - 1)^{2k+1}$ and
$H_{2k}(1 + \sqrt 2) = H_{2k+1} + \sqrt 2\,(\sqrt 2 - 1)^{2k}$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Proposition 2 (1), (2).

Stated but not proved: `MetaMathlibExt.pellNumber_odd_mul_one_add_sqrt_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#pell-number-odd-mul-one-add-sqrt-two).

## Numeration by doubled Pell and half-companion Pell numbers

Let $P_n$ be the Pell numbers
($P_0 = 0$, $P_1 = 1$, $P_{n+2} = 2P_{n+1} + P_n$) and $H_n$ the half-companion Pell numbers
($H_0 = H_1 = 1$, $H_{n+2} = 2H_{n+1} + H_n$), and let $R_k = 2P_k$ for odd $k$ and
$R_k = H_k$ for even $k$. Then for every positive integer $t$ there are a natural number $n$ and
natural numbers $a_0, a_1, a_2, \dots$ such that $R_n \le t < R_{n+1}$,
$t = \sum_{k=0}^{n} a_k R_k$, $a_0 \le 1$, $a_0 = 0$ if $a_1 = 1$, $a_{2k} \le 3$ and
$a_{2k+1} \le 1$ for every $k \ge 0$, $a_{2k+2} < 3$ whenever $a_{2k} = 3$ ($k \ge 0$), and
$a_{2k-1} = a_{2k+1} = 0$ and $a_{2k-2} < 3$ whenever $a_{2k} = 3$ with $k \ge 1$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 4.

Stated but not proved: `MetaMathlibExt.exists_two_pell_halfCompanion_representation` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#exists-two-pell-half-companion-represent).

## Numeration by Pell and half-companion Pell numbers

Let $P_n$ be the Pell numbers
($P_0 = 0$, $P_1 = 1$, $P_{n+2} = 2P_{n+1} + P_n$) and $H_n$ the half-companion Pell numbers
($H_0 = H_1 = 1$, $H_{n+2} = 2H_{n+1} + H_n$), and let $R_k = P_k$ for odd $k$ and
$R_k = H_k$ for even $k$. Then for every positive integer $t$ there are a natural number $n \ge 1$
and natural numbers $a_0, a_1, a_2, \dots$ such that $R_n \le t < R_{n+1}$,
$t = \sum_{k=1}^{n} a_k R_k$, $a_1 \le 2$, $a_2 = 0$ if $a_1 = 2$, $a_{2k+1} \le 3$ and
$a_{2k} \le 1$ for every $k \ge 0$, and for every $k \ge 1$ with $a_{2k+1} = 3$ we have
$a_{2k} = a_{2k+2} = 0$, $a_{2k-1} < 3$ and $a_{2k+3} < 3$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 5.

Stated but not proved: `MetaMathlibExt.exists_pell_halfCompanion_representation` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#exists-pell-half-companion-representatio).

## Bronze Lucas parameters

The bronze Lucas parameters are the Lucas sequence parameters
$(P, Q) = (3, -1)$. The Lucas sequence $U(3, -1)$ is the sequence of bronze numbers $B_n$, with
$B_0 = 0$, $B_1 = 1$ and $B_{n+2} = 3B_{n+1} + B_n$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4 (bronze numbers).

Formalized by `MetaMathlibExt.bronzeLucasParams`, a definition declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-lucas-params).

## Recurrence of the bronze numbers

Let $B_n$ be the bronze numbers, the terms of the Lucas
sequence $U(3, -1)$. For every natural number $n$, $B_{n+2} = 3B_{n+1} + B_n$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4 (bronze numbers).

Formalized by `MetaMathlibExt.lucasU_bronzeLucasParams_add_two`, a theorem declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#lucas-u-bronze-lucas-params-add-two).

## The first bronze numbers

Let $B_n$ be the bronze numbers, the terms of the Lucas sequence
$U(3, -1)$. Then $B_0, B_1, B_2, B_3, B_4, B_5$ are $0, 1, 3, 10, 33, 109$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4 (bronze numbers).

Formalized by `MetaMathlibExt.lucasU_bronzeLucasParams_values`, a theorem declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#lucas-u-bronze-lucas-params-values).

## Companion bronze numbers of the first type

Let $B_n$ denote the bronze numbers, the
Lucas sequence $U(3, -1)$: $B_0 = 0$, $B_1 = 1$ and $B_{n+2} = 3B_{n+1} + B_n$. For every
natural number $n$, the $n$-th companion bronze number of the first type is the integer
$C_n = B_{n+1} - 2B_n$.

Thus $C_0 = C_1 = 1$, $C_{n+2} = 3C_{n+1} + C_n$, and $C_n = B_n + B_{n-1}$ for $n \ge 1$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4 (companion bronze numbers of the first type).

Formalized by `MetaMathlibExt.bronzeCompanionFirst`, a definition declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-companion-first).

## Companion bronze numbers of the second type

Let $B_n$ denote the bronze numbers, the
Lucas sequence $U(3, -1)$: $B_0 = 0$, $B_1 = 1$ and $B_{n+2} = 3B_{n+1} + B_n$. For every
natural number $n$, the $n$-th companion bronze number of the second type is the integer
$D_n = B_{n+1} - B_n$.

Thus $D_0 = 1$, $D_1 = 2$, $D_{n+2} = 3D_{n+1} + D_n$, and $D_n = 2B_n + B_{n-1}$ for $n \ge 1$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4 (companion bronze numbers of the second type).

Formalized by `MetaMathlibExt.bronzeCompanionSecond`, a definition declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-companion-second).

## Recurrence for the companion bronze numbers of the first type

For every natural number
$n$, the companion bronze numbers $C_n$ of the first type satisfy $C_{n+2} = 3C_{n+1} + C_n$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4.

Formalized by `MetaMathlibExt.bronzeCompanionFirst_add_two`, a theorem declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-companion-first-add-two).

## Recurrence for the companion bronze numbers of the second type

For every natural number
$n$, the companion bronze numbers $D_n$ of the second type satisfy $D_{n+2} = 3D_{n+1} + D_n$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4.

Formalized by `MetaMathlibExt.bronzeCompanionSecond_add_two`, a theorem declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-companion-second-add-two).

## Initial companion bronze numbers

The companion bronze numbers $C_n$ of the first type
satisfy $(C_0, C_1, C_2, C_3, C_4) = (1, 1, 4, 13, 43)$, and the companion bronze numbers $D_n$
of the second type satisfy $(D_0, D_1, D_2, D_3, D_4) = (1, 2, 7, 23, 76)$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 4.

Formalized by `MetaMathlibExt.bronzeCompanion_values`, a theorem declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-companion-values).

## Moves of the Beatty octal game

Let $\alpha$ and $\beta$ be real numbers. In the Beatty
octal game for $\alpha$ and $\beta$, a move takes a heap of $n$ tokens to a heap of $m$ tokens
exactly when one of the following holds: $n \ge 1$, $n = \lfloor k\alpha \rfloor$ for some
integer $k \ge 1$, and $m = 0$ (the whole heap is removed); or $m = n - i$ for some natural
number $i$ with $1 \le i < n$ and $i = \lfloor k\beta \rfloor$ for some integer $k \ge 1$
(removing $i$ tokens leaves a nonempty heap).

When $\alpha$ and $\beta$ are complementary, so that every $i \ge 1$ lies in exactly one of the
Beatty sequences $\{\lfloor k\alpha \rfloor : k \ge 1\}$ and
$\{\lfloor k\beta \rfloor : k \ge 1\}$, this is the octal game with code
$0{\cdot}d_1 d_2 d_3 \ldots$, where $d_i = 1$ if $i$ lies in the first sequence and $d_i = 2$ if
$i$ lies in the second.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 1.1 (octal codes) and the codes of the gold, silver and bronze games in Sections 2, 3, 4.

Formalized by `MetaMathlibExt.beattyOctalMove`, a definition declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#beatty-octal-move).

## Moves of a Beatty octal game decrease the heap

For all real numbers $\alpha$, $\beta$
and all natural numbers $n$, $m$: if a move of the Beatty octal game for $\alpha$ and $\beta$
takes a heap of $n$ tokens to a heap of $m$ tokens, then $m < n$.

Consequently every play of the game terminates.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Section 1.1.

Formalized by `MetaMathlibExt.beattyOctalMove_lt`, a theorem declared in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#beatty-octal-move-lt).

## Floor of greedy odd-Fibonacci sums times $\varphi$ and $1 + \varphi$

Let $F_n$ be the
Fibonacci numbers ($F_0 = 0$, $F_1 = 1$, $F_{n+2} = F_{n+1} + F_n$) and
$\varphi = (1 + \sqrt 5)/2$ the golden ratio. Let $n$ be a natural number and $a_0, a_1, \dots$
natural numbers such that $\sum_{k=0}^{m-1} a_k F_{2k+1} < F_{2m+1}$ for every $m \le n + 1$, and
let $t = \sum_{k=0}^{n} a_k F_{2k+1}$. Then
$\lfloor t \varphi \rfloor = \sum_{k=0}^{n} a_k F_{2k+2}$ and
$\lfloor t (1 + \varphi) \rfloor = \sum_{k=0}^{n} a_k F_{2k+3}$.

The hypothesis says that the $a_k$ are the digits of the greedy representation of Theorem 1
(here $a_k$ is the paper's $a_{2k+1}$); $n$ need not be minimal and $t = 0$ is allowed.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 2.

Stated but not proved: `MetaMathlibExt.floor_greedy_odd_fib_sum_mul_goldenRatio` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#floor-greedy-odd-fib-sum-mul-golden-rati).

## P-positions of the gold game

Let $\varphi$ be the golden ratio and $F_n$ the Fibonacci
numbers ($F_1 = F_2 = 1$). In the gold game a heap of $n$ tokens may be removed entirely when
$n = \lfloor k\varphi \rfloor$ for some integer $k \ge 1$, and $i$ tokens may be removed from a
heap of $n > i$ tokens, leaving $n - i$, when $i = \lfloor k(1 + \varphi) \rfloor$ for some
integer $k \ge 1$ (the Beatty octal moves for $\varphi$ and $1 + \varphi$). Let $S$ be the set of
natural numbers consisting of $0$ and the $F_{2k+1}$ for $k \ge 1$, that is $0, 2, 5, 13, 34, \dots$
Then $S$ is stable: no move leads from a heap size in $S$ to a heap size in $S$. And $S$ is
absorbing: from every heap size outside $S$ some move leads to a heap size in $S$.

Since every move shrinks the heap, a stable and absorbing set is the set of P-positions, so the
P-positions of the gold game are exactly the heap sizes in $S$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 3.

Stated but not proved: `MetaMathlibExt.goldGame_pPositions` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#gold-game-p-positions).

## Floor of greedy Pell sums times $1 + \sqrt 2$

Let $P_n$ be the Pell numbers ($P_0 = 0$,
$P_1 = 1$, $P_{n+2} = 2P_{n+1} + P_n$) and $H_n$ the half-companion Pell numbers
($H_0 = H_1 = 1$, $H_{n+2} = 2H_{n+1} + H_n$). Let $R_k = P_k$ and $R'_k = H_k$ for odd $k$, and
$R_k = H_k$ and $R'_k = P_k$ for even $k$. Let $n$ be a natural number and $a_1, a_2, \dots$
natural numbers such that $\sum_{k=1}^{m-1} a_k R_k < R_m$ for every $1 \le m \le n + 1$, and let
$t = \sum_{k=1}^{n} a_k R_k$. Then $\lfloor t (1 + \sqrt 2) \rfloor = \sum_{k=1}^{n} a_k R'_{k+1}$.

The hypothesis says that the $a_k$ are the digits of the greedy representation of Theorem 5;
$n$ need not be minimal.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 6 (1).

Stated but not proved: `MetaMathlibExt.floor_greedy_pell_halfCompanion_sum_mul_one_add_sqrt_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 243](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L243). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#floor-greedy-pell-half-companion-sum-mul).

## Floor of greedy sums of $2P_k$ and $H_k$ times $(2 + \sqrt 2)/2$

Let $P_k$ be the Pell
numbers and $H_k$ the Pell–Lucas numbers ($H_0 = H_1 = 1$, $H_{k+2} = 2H_{k+1} + H_k$). Put
$R_k = 2P_k$ and $R'_k = P_k$ for odd $k$, and $R_k = R'_k = H_k$ for even $k$. Let $n$ be a
natural number and $a_0, a_1, \dots$ natural numbers such that $\sum_{k\lt m} a_k R_k < R_m$ for
every $m \le n + 1$, and let $t = \sum_{k=0}^{n} a_k R_k$. Then
$\lfloor t(2 + \sqrt 2)/2 \rfloor = \sum_{k=0}^{n} a_k R'_{k+1}$.

The hypothesis says that the $a_k$ are the digits of the greedy representation of $t$ by the
$R_k$; $n$ need not be minimal.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 6 (2).

Stated but not proved: `MetaMathlibExt.floor_greedy_two_pell_halfCompanion_sum_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 258](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L258). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#floor-greedy-two-pell-half-companion-sum).

## P-positions of the silver game

Let $P_n$ be the Pell numbers and $H_n$ the Pell–Lucas
numbers ($H_0 = H_1 = 1$, $H_{n+2} = 2H_{n+1} + H_n$). In the silver game a heap of $n$ tokens
may be removed entirely when $n = \lfloor k(1 + \sqrt 2) \rfloor$ for some integer $k \ge 1$, and
$i$ tokens may be removed from a heap of $n > i$ tokens, leaving $n - i$, when
$i = \lfloor k(2 + \sqrt 2)/2 \rfloor$ for some integer $k \ge 1$ (the Beatty octal moves for
$1 + \sqrt 2$ and $(2 + \sqrt 2)/2$). Let $S$ be the set of natural numbers consisting of $0$ and
the $P_{2k+1}$ and $H_{2k+2}$ for $k \ge 0$, that is $0, 1, 3, 5, 17, 29, 99, \dots$ Then $S$ is
stable: no move leads from a heap size in $S$ to a heap size in $S$. And $S$ is absorbing: from
every heap size outside $S$ some move leads to a heap size in $S$.

Since every move shrinks the heap, a stable and absorbing set is the set of P-positions, so the
P-positions of the silver game are exactly the heap sizes in $S$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 7.

Stated but not proved: `MetaMathlibExt.silverGame_pPositions` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#silver-game-p-positions).

## Metallic identities for the bronze numbers

Let $\alpha = (3 + \sqrt{13})/2$,
$\beta = (5 + \sqrt{13})/6$ and $\gamma = (\sqrt{13} - 3)/2$, let $B_n$ be the bronze numbers,
and let $C_n$ and $D_n$ be the companion bronze numbers of the first and second type. For every
natural number $k$, the following hold in $\mathbb{R}$:
(1) $B_{2k+1}\alpha = B_{2k+2} + \gamma^{2k+1}$;
(2) $C_{2k}\alpha = C_{2k+1} + \frac{13 + \sqrt{13}}{2\sqrt{13}}\gamma^{2k}$;
(3) $D_{2k}\alpha = D_{2k+1} + \frac{13 - \sqrt{13}}{2\sqrt{13}}\gamma^{2k}$;
(4) $3B_{2k+1}\beta = C_{2k+2} + \frac{13 - 3\sqrt{13}}{2\sqrt{13}}\gamma^{2k}$;
(5) $(B_{2k+1} + C_{2k+2})\beta = D_{2k+2} + \frac{65 - 17\sqrt{13}}{6\sqrt{13}}\gamma^{2k}$;
(6) $D_{2k}\beta = B_{2k+1} + \frac{13 - \sqrt{13}}{6\sqrt{13}}\gamma^{2k}$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Proposition 3.

Stated but not proved: `MetaMathlibExt.bronze_mul_metallic_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-mul-metallic-identities).

## Mixed bronze numeration

Let $B_n$ be the bronze numbers ($B_0 = 0$, $B_1 = 1$,
$B_{n+2} = 3B_{n+1} + B_n$, the Lucas sequence $U(3, -1)$), and let $C_n = B_{n+1} - 2B_n$ and
$D_n = B_{n+1} - B_n$ be the companion bronze numbers of the first and second type. Let $R$ be
the integer sequence with $R_{3m} = D_{2m}$, $R_{3m+1} = 3B_{2m+1}$ and
$R_{3m+2} = B_{2m+1} + C_{2m+2}$ for all $m \ge 0$. Then for every positive integer $t$ there are
a natural number $n$ and natural numbers $a_0, a_1, a_2, \dots$ such that $R_n \le t < R_{n+1}$,
$t = \sum_{k=0}^{n} a_k R_k$, $a_k = 0$ for every $k > n$, and: (3) $a_0 \le 2$, and
$a_0 \le 1$ if $a_1 = 1$ or $a_2 = 1$; (4) for every $k > 0$, $a_k \le 4$ if $3 \mid k$ and
$a_k \le 1$ otherwise; (5) for every $k$ with $a_k = 4$, $a_{k-1} = a_{k+1} = 0$,
$a_{k-3} < 4$ and $a_{k+3} < 4$; (6) for every $m \ge 0$, if $a_{3m+1} = 1$ then
$a_{3m+2} = 0$, and if $a_{3m+2} = 1$ then $a_{3m+1} = 0$; (7) for every $m \ge 1$ with
$a_{3m} = 3$, if $a_{3m+1} = 1$ or $a_{3m+2} = 1$ then $a_{3m-1} = a_{3m-2} = 0$, and if
$a_{3m-1} = 1$ or $a_{3m-2} = 1$ then $a_{3m+1} = a_{3m+2} = 0$.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 8.

Stated but not proved: `MetaMathlibExt.exists_mixed_bronze_representation` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#exists-mixed-bronze-representation).

## Numeration by bronze and companion bronze numbers

Let $B_n$ be the bronze numbers
($B_0 = 0$, $B_1 = 1$, $B_{n+2} = 3B_{n+1} + B_n$, the Lucas sequence $U(3, -1)$), and let
$C_n = B_{n+1} - 2B_n$ and $D_n = B_{n+1} - B_n$ be the companion bronze numbers of the first and
second type. Let $R$ be the integer sequence with $R_{3m+1} = B_{2m+1}$, $R_{3m+2} = C_{2m+2}$
and $R_{3m} = D_{2m}$ for all $m \ge 0$. Then for every positive integer $t$ there are a natural
number $n \ge 1$ and natural numbers $a_0, a_1, a_2, \dots$ such that $R_n \le t < R_{n+1}$,
$t = \sum_{k=1}^{n} a_k R_k$, $a_k = 0$ for every $k > n$, and: (3) $a_1 \le 3$, and
$a_2 = a_3 = 0$ if $a_1 = 3$; (4) for every $k > 1$, $a_k \le 4$ if $k \equiv 1 \pmod 3$ and
$a_k \le 1$ otherwise; (5) for every $k$ with $a_k = 4$, $a_{k-1} = a_{k+1} = 0$, $a_{k-3} < 4$
and $a_{k+3} < 4$, where an index below $0$ is read as $0$.

The paper's conditions (6) and (7) are omitted: no representation of $50$ satisfies (6)
together with (2)–(5), and the greedy representation $410 = 3B_5 + D_4 + D_2$
($327 + 76 + 7$; digits $a_7 = 3$, $a_6 = 1$, $a_3 = 1$) violates (7).

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 9 (1)–(5).

Stated but not proved: `MetaMathlibExt.exists_bronze_companion_representation` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#exists-bronze-companion-representation).

## Floor of greedy bronze sums times $(3 + \sqrt{13})/2$

Let $B_n$ be the bronze numbers
($B_0 = 0$, $B_1 = 1$, $B_{n+2} = 3B_{n+1} + B_n$, the Lucas sequence $U(3, -1)$), and let
$C_n = B_{n+1} - 2B_n$ and $D_n = B_{n+1} - B_n$ be the companion bronze numbers of the first and
second type. Let $R$ and $R'$ be the integer sequences with $R_{3m+1} = B_{2m+1}$,
$R_{3m+2} = C_{2m+2}$, $R_{3m} = D_{2m}$ and $R'_{3m+1} = D_{2m+1}$, $R'_{3m+2} = B_{2m+2}$,
$R'_{3m} = C_{2m+1}$ for all $m \ge 0$. Let $n$ be a natural number and $a_1, a_2, \dots$ natural
numbers such that $\sum_{k=1}^{m-1} a_k R_k < R_m$ for every $1 \le m \le n + 1$, and let
$t = \sum_{k=1}^{n} a_k R_k$. Then
$\lfloor t (3 + \sqrt{13})/2 \rfloor = \sum_{k=1}^{n} a_k R'_{k+1}$.

The hypothesis says that the $a_k$ are the digits of the greedy representation of Theorem 9;
$n$ need not be minimal.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 10 (1).

Stated but not proved: `MetaMathlibExt.floor_greedy_bronze_companion_sum_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#floor-greedy-bronze-companion-sum-mul).

## Floor of greedy mixed bronze sums times $(5 + \sqrt{13})/6$

Let $B_n$ be the bronze
numbers ($B_0 = 0$, $B_1 = 1$, $B_{n+2} = 3B_{n+1} + B_n$, the Lucas sequence $U(3, -1)$), and let
$C_n = B_{n+1} - 2B_n$ and $D_n = B_{n+1} - B_n$ be the companion bronze numbers of the first and
second type. Let $R$ and $R'$ be the integer sequences with $R_{3m} = D_{2m}$,
$R_{3m+1} = 3B_{2m+1}$, $R_{3m+2} = B_{2m+1} + C_{2m+2}$ and $R'_{3m} = D_{2m}$,
$R'_{3m+1} = B_{2m+1}$, $R'_{3m+2} = C_{2m+2}$ for all $m \ge 0$. Let $n$ be a natural number
and $a_0, a_1, a_2, \dots$ natural numbers such that $\sum_{k=0}^{m-1} a_k R_k < R_m$ for every
$m \le n + 1$, and let $t = \sum_{k=0}^{n} a_k R_k$. Then
$\lfloor t (5 + \sqrt{13})/6 \rfloor = \sum_{k=0}^{n} a_k R'_{k+1}$.

The hypothesis says that the $a_k$ are the digits of the greedy representation of Theorem 8;
$n$ need not be minimal.

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 10 (2).

Stated but not proved: `MetaMathlibExt.floor_greedy_mixed_bronze_sum_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#floor-greedy-mixed-bronze-sum-mul).

## P-positions of the bronze game

Let $\alpha = (3 + \sqrt{13})/2$ and
$\beta = (5 + \sqrt{13})/6$, let $B_n$ be the bronze numbers, and let $C_n$ and $D_n$ be the
companion bronze numbers of the first and second type. Let $P$ be the set of natural numbers
$x$ such that $x = 0$ or $x \in \{B_{2k+1}, C_{2k+2}, D_{2k+2}\}$ for some natural number $k$.
Then, in the Beatty octal game for $\alpha$ and $\beta$, no move takes a heap whose size lies
in $P$ to a heap whose size lies in $P$, and from every heap whose size is not in $P$ some move
leads to a heap whose size lies in $P$.

So $P$ is stable and absorbing for the moves of the game; since every move decreases the heap,
this determines $P$ as the set of P-positions, the heap sizes from which the previous player
wins: $0, B_1, C_2, D_2, B_3, C_4, D_4, \ldots$

## Sources

- Michael Fisher, Keith Hazen, and Craig Tennenhouse, *Olympic Games: Three Impartial Games with Infinite Octal Codes*, INTEGERS 24 (2024), Article G3, Theorem 11.

Stated but not proved: `MetaMathlibExt.bronzeGame_pPositions` is written with `theorem_wanted` in [WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OlympicGamesNumerationWanted.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html#bronze-game-p-positions).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Numeration by Fibonacci and Pell numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/numeration-automatic/numeration-by-fibonacci-and-pell-numbers)
