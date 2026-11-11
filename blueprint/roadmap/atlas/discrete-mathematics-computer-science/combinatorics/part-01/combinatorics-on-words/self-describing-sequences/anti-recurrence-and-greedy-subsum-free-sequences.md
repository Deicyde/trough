---
declaration: section
origin: cited
lean: MetaMathlibExt.antiTribonacciMex, MetaMathlibExt.antiTribonacciMex_example, MetaMathlibExt.antiTribonacciMex_pos, MetaMathlibExt.antiTribonacciMex_notMem, MetaMathlibExt.antiTribonacciMex_le_of_notMem, MetaMathlibExt.antiTribonacciState, MetaMathlibExt.antiTribonacciA, MetaMathlibExt.antiTribonacciB
statement: formalized
---

# Anti-recurrence and greedy subsum-free sequences

63 results, 42 proved and 21 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html).

## Least positive integer missing from a finite set

For a finite set $s$ of natural numbers,
this is the least positive integer not in $s$ (the source's $\mathrm{mex}$ over the positive
integers, used to build the anti-Tribonacci sequence). It always lies among $1, \dots, |s| + 1$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciMex`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-mex).

## Mex of $\{1, 2, 3, 6\}$

The least positive integer not in $\{1, 2, 3, 6\}$ is $4$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciMex_example`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-mex-example).

## The mex of a finite set is positive

Write $\mathrm{mex}(s)$ for the least positive integer
not in a finite set $s$ of natural numbers. For every such $s$, $\mathrm{mex}(s) > 0$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciMex_pos`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-mex-pos).

## The mex of a finite set lies outside the set

Write $\mathrm{mex}(s)$ for the least positive
integer not in a finite set $s$ of natural numbers. For every such $s$, $\mathrm{mex}(s) \notin s$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciMex_notMem`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-mex-not-mem).

## The mex is at most every missing positive integer

Write $\mathrm{mex}(s)$ for the least
positive integer not in a finite set $s$ of natural numbers. If $m$ is a positive integer with
$m \notin s$, then $\mathrm{mex}(s) \le m$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciMex_le_of_notMem`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-mex-le-of-not-mem).

## Anti-Tribonacci construction

Write $\mathrm{mex}(U)$ for the least positive integer not in
a finite set $U$ of natural numbers. Set $(A_1, B_1, C_1, D_1) = (1, 2, 3, 6)$ and
$U_1 = \{1, 2, 3, 6\}$. For $k \ge 1$ let $A_{k+1} = \mathrm{mex}(U_k)$,
$B_{k+1} = \mathrm{mex}(U_k \cup \{A_{k+1}\})$,
$C_{k+1} = \mathrm{mex}(U_k \cup \{A_{k+1}, B_{k+1}\})$, $D_{k+1} = A_{k+1} + B_{k+1} + C_{k+1}$
and $U_{k+1} = U_k \cup \{A_{k+1}, B_{k+1}, C_{k+1}, D_{k+1}\}$. Entry $n$ of the construction is
the pair $((A_{n+1}, B_{n+1}, C_{n+1}, D_{n+1}), U_{n+1})$, where $U_{n+1}$ is the set of all
values used so far.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciState`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-state).

## First summands of the anti-Tribonacci construction

For $n \ge 1$, $A_n$ is the first
entry of the $n$-th quadruple $(A_n, B_n, C_n, D_n)$ of the anti-Tribonacci construction:
$A_1 = 1$, and for $n \ge 2$, $A_n$ is the least positive integer that is not among the values
$A_k$, $B_k$, $C_k$, $D_k$ with $1 \le k < n$. At $n = 0$ the definition gives $A_0 = A_1 = 1$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciA`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-a).

## Second summands of the anti-Tribonacci construction

For $n \ge 1$, $B_n$ is the second
entry of the $n$-th quadruple $(A_n, B_n, C_n, D_n)$ of the anti-Tribonacci construction:
$B_1 = 2$, and for $n \ge 2$, $B_n$ is the second smallest positive integer that is not among
the values $A_k$, $B_k$, $C_k$, $D_k$ with $1 \le k < n$. At $n = 0$ the definition gives
$B_0 = B_1 = 2$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciB`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-b).

## Third summands of the anti-Tribonacci construction

For $n \ge 1$, $C_n$ is the third
entry of the $n$-th quadruple $(A_n, B_n, C_n, D_n)$ of the anti-Tribonacci construction:
$C_1 = 3$, and for $n \ge 2$, $C_n$ is the third smallest positive integer that is not among
the values $A_k$, $B_k$, $C_k$, $D_k$ with $1 \le k < n$. At $n = 0$ the definition gives
$C_0 = C_1 = 3$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciC`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-c).

## Anti-Tribonacci numbers

For $n \ge 1$, the anti-Tribonacci number $D_n$ (OEIS A265389) is
the fourth entry of the $n$-th quadruple $(A_n, B_n, C_n, D_n)$ of the anti-Tribonacci
construction, so $D_n = A_n + B_n + C_n$ and $D_1 = 6$. At $n = 0$ the definition gives
$D_0 = D_1 = 6$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciD`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-d).

## First anti-Tribonacci numbers

Writing $D_n$ for the $n$-th anti-Tribonacci number,
the first four anti-Tribonacci numbers are $D_1 = 6$, $D_2 = 16$, $D_3 = 27$ and $D_4 = 36$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiTribonacciD_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-tribonacci-d-small).

## Members of a greedy $3$-subsumfree sequence below a bound

For natural numbers $x$, $y$
and $z$ (the source takes $x < y < z$), let $S_{x,y,z}$ consist of $x$, $y$, $z$ and every natural
number $n > z$ that is not a sum $a + b + c$ of members $a < b < c$ of $S_{x,y,z}$ smaller than
$n$. This definition gives, for each natural number $m$, the finite set of members of $S_{x,y,z}$
below $m$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 6.

Formalized by `MetaMathlibExt.greedySubsumfreeBelow`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#greedy-subsumfree-below).

## First members of $S_{1,2,3}$

The members of the greedy $3$-subsumfree sequence
$S_{1,2,3}$ below $26$ are exactly $1, 2, 3, 4, 5, 13, 14, 15, 25$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 6.

Formalized by `MetaMathlibExt.greedySubsumfreeBelow_one_two_three`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#greedy-subsumfree-below-one-two-three).

## Hajdu–Tijdeman–Varga theorem on $(x-1)^c (x+1)^d$ modulo $3$

Let $c$ and $d$ be natural
numbers. If none of the coefficients of $x^0, x^1, \dots, x^{c+d}$ in the integer polynomial
$(x-1)^c (x+1)^d$ is divisible by $3$, then there are natural numbers $i > j$ such that $c + d + 1$
equals $3^j$, $2 \cdot 3^j$, $3^i + 3^j$ or $2 \cdot 3^i + 3^j$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Theorem 10 (`jis-2025-25.3.8-thm-10`), citing Hajdu, Tijdeman, and Varga.

Stated but not proved: `MetaMathlibExt.coeff_not_dvd_three_shape` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#coeff-not-dvd-three-shape).

## Kimberling's conjecture on the anti-Tribonacci sequence

Let $A_1 = 1$, $B_1 = 2$,
$C_1 = 3$ and $D_1 = 6$, and for $n \ge 1$ let $A_{n+1} < B_{n+1} < C_{n+1}$ be the three
smallest positive integers that are not among $A_i, B_i, C_i, D_i$ for $i \le n$, and
$D_{n+1} = A_{n+1} + B_{n+1} + C_{n+1}$ (the $D_n$ are the anti-Tribonacci numbers). For every
integer $n \ge 1$, $0 \le 10n - 6 - 3A_n \le 2$, $0 \le 10n - 2 - 3B_n \le 3$,
$0 \le 10n + 1 - 3C_n \le 3$ and $0 \le 10n - 3 - D_n \le 2$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Theorem 12 (`jis-2025-25.3.8-thm-12`).

Stated but not proved: `MetaMathlibExt.kimberling_antiTribonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#kimberling-anti-tribonacci).

## Membership in three greedy 3-subsumfree sequences

For $x < y < z$, the greedy
$3$-subsumfree sequence $S_{x,y,z}$ consists of $x$, $y$, $z$ and every $m > z$ that is not the
sum of three different members of $S_{x,y,z}$ smaller than $m$. For every positive integer $n$:
$n \in S_{1,2,3}$ if and only if $n \in \{1, 5, 13\}$ or $n \bmod 23 \in \{2, 3, 4, 14, 15\}$;
$n \in S_{1,3,4}$ if and only if $n \in \{1, 7, 19\}$ or
$n \bmod 33 \in \{3, 4, 5, 6, 20, 21, 22\}$; and $n \in S_{1,4,5}$ if and only if
$n \in \{1, 9, 25\}$ or $n \bmod 43 \in \{4, 5, 6, 7, 8, 26, 27, 28, 29\}$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Theorem 15 (`jis-2025-25.3.8-thm-15`).

Stated but not proved: `MetaMathlibExt.mem_greedySubsumfree_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 220](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L220). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#mem-greedy-subsumfree-iff).

## Unsums of upper Wythoff numbers

A positive integer $p$ is an *upper Wythoff number* when
the letter at index $p - 1$ (indices start at $0$) of the infinite Fibonacci word
$0100101001001\ldots$ is $1$; that is, the upper Wythoff numbers are the positions of the letter
$1$ in the Fibonacci word counted from one. A positive integer $x$ is an *unsum* (OEIS A260317)
if there are no upper Wythoff numbers $p < q$ with $p + q = x$.

The source writes the Fibonacci word over the letters $a$ and $b$; its letter $b$ is the letter
$1$ here.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2, defining unsums as the members of OEIS A260317.

Formalized by `MetaMathlibExt.IsUpperWythoffUnsum`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#is-upper-wythoff-unsum).

## The upper Wythoff numbers below 30

The positive integers $p < 30$ such that the letter at
index $p - 1$ (indices start at $0$) of the infinite Fibonacci word is $1$, that is, the upper
Wythoff numbers below $30$, are exactly $2, 5, 7, 10, 13, 15, 18, 20, 23, 26, 28$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoff_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 284](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L284). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-small).

## The unsums up to 21

The unsums (OEIS A260317) that are at most $21$ are exactly
$1, 2, 3, 4, 5, 6, 8, 10, 11, 13, 14, 16, 19, 21$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.isUpperWythoffUnsum_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#is-upper-wythoff-unsum-small).

## Gaps between unsums

Let $a_1 < a_2 < \cdots$ be the unsums (OEIS A260317): the
positive integers that are not a sum $p + q$ of upper Wythoff numbers $p < q$. For $i \ge 0$,
the $i$-th gap between consecutive unsums (counted from zero) is $a_{i+2} - a_{i+1}$; this
is OEIS A260311 shifted by one.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoffUnsumGap`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-gap).

## The first thirteen gaps between unsums

Let $a_1 < a_2 < \cdots$ be the unsums
(OEIS A260317) and let $g_i = a_{i+2} - a_{i+1}$ for $i \ge 0$. Then the gaps
$g_0, g_1, \dots, g_{12}$ are $1, 1, 1, 1, 1, 2, 2, 1, 2, 1, 2, 3, 2$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoffUnsumGap_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-gap-small).

## Markers among the unsum gaps

A natural number $i$ is a *marker* if $i \ge 10$ and the
$i$-th gap between consecutive unsums of upper Wythoff numbers (counted from zero) equals $2$.

The source marks the entries $2$ of A260311 that follow the irregular prefix $1111122121$ of
length ten.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.IsUpperWythoffUnsumMarker`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#is-upper-wythoff-unsum-marker).

## Markers in the gaps between unsums

Call a gap index $i$ a marker if $i \ge 10$ and the
$i$-th gap between consecutive unsums (counted from zero) equals $2$. For $j \ge 0$, the
$j$-th marker is the $j$-th marker in increasing order, counted from zero, so the $0$-th
marker is the smallest one.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoffUnsumMarker`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-marker).

## Words between markers in the unsum gap sequence

Let $g_0, g_1, g_2, \ldots$ be the
gaps between consecutive unsums, and call an index $i \ge 10$ with $g_i = 2$ a marker. Let
$m_0 < m_1 < m_2 < \cdots$ be the markers in increasing order. For each $j$, the $j$-th word
between markers is $g_{m_j + 1} g_{m_j + 2} \cdots g_{m_{j+1} - 1}$, the word of the gaps
strictly between the $j$-th and the $(j+1)$-th marker.

The source writes the gap sequence after its prefix as $2 W_1 2 W_1 2 W_2 2 W_2 2 W_3 2 \cdots$,
so these words are $W_1, W_1, W_2, W_2, \ldots$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoffUnsumWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 380](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L380). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-word).

## The words $W_i$ of the unsum gap sequence

For $i \ge 1$, the word $W_i$ is the word of
gaps strictly between the $(2i-2)$-th and $(2i-1)$-th markers of the unsum gap sequence, with
markers counted from zero; for $i = 0$ the definition gives the same word as for $i = 1$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoffUnsumPalindrome`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-palindrome).

## The first two markers

Call a gap index $i$ a marker if $i \ge 10$ and the $i$-th gap
between consecutive unsums (counted from zero) equals $2$. The smallest marker is $10$ and
the second smallest is $12$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoffUnsumMarker_zero_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 403](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L403). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-marker-zero-one).

## The first palindrome

Let $g_k$ be the $k$-th gap between consecutive unsums
(OEIS A260317), counted from zero, and let $m_0 < m_1 < \cdots$ be the markers, the indices
$k \ge 10$ with $g_k = 2$, in increasing order. The word $W_1$ of the gaps $g_k$ with
$m_0 < k < m_1$, in increasing order of $k$, consists of the single digit $3$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 2.

Formalized by `MetaMathlibExt.upperWythoffUnsumPalindrome_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 435](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L435). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-palindrome-one).

## The last gap of size one between unsums

Let $a_1 < a_2 < \cdots$ be the unsums
(OEIS A260317), and for $i \ge 0$ let $g_i = a_{i+2} - a_{i+1}$ be the $i$-th gap between
consecutive unsums, counted from zero. Then $g_9 = 1$, and $g_i \ne 1$ for every $i \ge 10$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 1 (`jis-2025-25.3.8-lem-1`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumGap_ne_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 447](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L447). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-gap-ne-one).

## Digit sums between markers are two less than Fibonacci numbers

For every $j$, the digit
sum of the $j$-th word between markers of the unsum gap sequence, plus $2$, is a Fibonacci
number: it equals $F_m$ for some natural number $m$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 2 (`jis-2025-25.3.8-lem-2`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumWord_sum_add_two_isFib` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 456](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L456). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-word-sum-add-two-is).

## Digit sums of the words between markers

Let $F_n$ be the Fibonacci numbers, with
$F_0 = 0$ and $F_1 = 1$. For every $j$ (words counted from zero), the digit sum of the $j$-th
word between markers of the unsum gap sequence, plus $2$, equals $F_{\lfloor j/2 \rfloor + 5}$.

So the digit sums are $3, 3, 6, 6, 11, \ldots$; adding the preceding marker digit $2$ gives
$F_5, F_5, F_6, F_6, F_7, \ldots$, which is how the source's Lemma 3 must be read, since the
bare digit sum of the first word is $3 \ne F_5 = 5$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 3 (`jis-2025-25.3.8-lem-3`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumWord_sum_add_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 468](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L468). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-word-sum-add-two).

## The gap words are palindromes

Let $g_k$ be the $k$-th gap between
consecutive unsums (OEIS A260317), counted from zero, and let $m_0 < m_1 < \cdots$ be the
markers, the indices $k \ge 10$ with $g_k = 2$, in increasing order. For $i \ge 1$ let $W_i$
be the word of the gaps $g_k$ with $m_{2i-2} < k < m_{2i-1}$, in increasing order of $k$. Then
for every $i \ge 1$, the word $W_i$ read backwards is $W_i$ itself.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 4 (`jis-2025-25.3.8-lem-4`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumPalindrome_reverse` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 476](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L476). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-palindrome-reverse).

## The palindromes begin and end with the digit 3

Let $g_k$ be the $k$-th gap between
consecutive unsums (OEIS A260317), counted from zero, and let $m_0 < m_1 < \cdots$ be the
markers, the indices $k \ge 10$ with $g_k = 2$, in increasing order. For $i \ge 1$ let $W_i$
be the word of the gaps $g_k$ with $m_{2i-2} < k < m_{2i-1}$, in increasing order of $k$. Then
for every $i \ge 1$, the word $W_i$ is nonempty, its first digit is $3$, and its last digit
is $3$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 5 (`jis-2025-25.3.8-lem-5`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumPalindrome_head_getLast` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 484](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L484). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-palindrome-head-get).

## A word $3V3$ between markers is followed by a word starting with $3V$

Let $V$ be a
finite word of natural numbers, and suppose that the $j$-th word between markers of the unsum
gap sequence is $3V3$. Then $3V$ is a prefix of the $(j+1)$-th word between markers, and if the
$(j+1)$-th word has the same digit sum as the $j$-th word, then the two words are equal.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 6 (`jis-2025-25.3.8-lem-6`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumWord_prefix_next` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 494](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L494). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-word-prefix-next).

## When one palindrome is a prefix of the next

Let $g_k$ be the $k$-th gap between
consecutive unsums (OEIS A260317), counted from zero, and let $m_0 < m_1 < \cdots$ be the
markers, the indices $k \ge 10$ with $g_k = 2$, in increasing order. For $i \ge 1$ let $W_i$
be the word of the gaps $g_k$ with $m_{2i-2} < k < m_{2i-1}$, in increasing order of $k$. Then
for every $i \ge 1$, the word $W_i$ is a prefix of $W_{i+1}$ if and only if $i$ is odd.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 7 (`jis-2025-25.3.8-lem-7`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumPalindrome_isPrefix_succ_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-palindrome-is-prefix).

## Recursion for the words $W_i$ of the unsum gap sequence

For each $i$ let $V_i$ be the
word $W_i$ with its first and last digit removed, write $|W|$ for the length of a word $W$, and
denote concatenation of words by juxtaposition. For every $i \ge 2$: if $i$ is odd, then
$W_{i+1} = W_i \, 5 \, V_{i-1} \, 3$; if $i$ is even, then $W_{i+1} = 3 \, V_i \, 5 \, W_{i-1}$;
and in both cases $|W_{i+1}| = |W_i| + |W_{i-1}|$. Moreover $|W_1| = 1$, $|W_2| = 2$, and
$|W_i| = F_{i+1}$ for every $i \ge 1$, where $F_m$ is the $m$-th Fibonacci number ($F_0 = 0$,
$F_1 = 1$).

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 8 (`jis-2025-25.3.8-lem-8`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumPalindrome_succ` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 516](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L516). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-palindrome-succ).

## The words $W_i$ converge to $3$ followed by the coded Fibonacci word

Let
$u_0 u_1 u_2 \cdots$ be the infinite Fibonacci word over $\{0, 1\}$, indexed from $0$, and let
$\mathbf{V}$ be the infinite word obtained from it by replacing each $0$ by $5$ and each
$1$ by $3$. Then the words $W_i$ of the unsum gap sequence converge to the infinite word
$3\mathbf{V}$: for every $k \ge 0$ there is $N$ such that for every $i \ge N$ the word $W_i$ has
more than $k$ digits and its digit at position $k$ (counted from zero) is the digit of
$3\mathbf{V}$ at position $k$, that is, $3$ if $k = 0$, and for $k \ge 1$ it is $3$ if
$u_{k-1} = 1$ and $5$ if $u_{k-1} = 0$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Lemma 9 (`jis-2025-25.3.8-lem-9`).

Stated but not proved: `MetaMathlibExt.upperWythoffUnsumPalindrome_tendsto` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 535](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L535). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#upper-wythoff-unsum-palindrome-tendsto).

## Iterates of the period-doubling substitution

Write the period-doubling substitution
$a \mapsto ab$, $b \mapsto aa$ over the letters $a = 1$ and $b = 0$, so that it sends $1$ to $10$
and $0$ to $11$. The $n$-th period-doubling iterate is the word obtained by applying this
substitution $n$ times to the one-letter word $1$; the iterates begin $1$, $10$, $1011$,
$10111010$, and their limit is the period-doubling word (Walnut's PD).

The source's prose takes $a = 0$ and $b = 1$, but its Walnut definition `antifib`
(`PD[k]=@1` gives $9 + 10k$) and its displayed anti-Fibonacci numbers $0, 3, 9, 13, \ldots$ need
the first letter of PD to be $1$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.periodDoublingWord`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 547](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L547). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#period-doubling-word).

## The period-doubling word

For a natural number $k$, the letter at index $k$ (indices start
at $0$) of the period-doubling word is the letter at index $k$ of the word obtained by applying
the period-doubling substitution $1 \mapsto 10$, $0 \mapsto 11$ to the one-letter word $1$ a total
of $\lfloor \log_2 k \rfloor + 1$ times, where $\lfloor \log_2 0 \rfloor$ is taken to be $0$.
That word has length $2^{\lfloor \log_2 k \rfloor + 1} \le 2k + 2$, so it contains index $k$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.periodDoubling`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#period-doubling).

## Length of the period-doubling iterates

For every natural number $n$, the word obtained by
applying the period-doubling substitution $1 \mapsto 10$, $0 \mapsto 11$ to the one-letter word
$1$ a total of $n$ times has length $2^n$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.length_periodDoublingWord`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 565](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L565). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#length-period-doubling-word).

## Letters of the period-doubling iterates

Let $w_m$ be the word obtained by applying the
period-doubling substitution $1 \mapsto 10$, $0 \mapsto 11$ to the one-letter word $1$ a total of
$m$ times. For all natural numbers $m$ and $k$ with $k < 2^m$, the letter of $w_m$ at index $k$
(indices start at $0$) equals the letter of the period-doubling word at index $k$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.periodDoublingWord_getD`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#period-doubling-word-get-d).

## First letters of the period-doubling word

The letters at indices $0, 1, \ldots, 7$ of the
period-doubling word (the fixed point of $1 \mapsto 10$, $0 \mapsto 11$ that starts with $1$) are
$1, 0, 1, 1, 1, 0, 1, 0$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.periodDoubling_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 624](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L624). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#period-doubling-small).

## The anti-Fibonacci construction

For each $n \ge 0$, entry $n$ of the construction is the
triple $(A_{n+1}, B_{n+1}, C_{n+1})$ of natural numbers together with the finite set $U_{n+1}$ of
values used so far. Entry $0$ is $(1, 2, 3)$ with $U_1 = \{1, 2, 3\}$. For $n \ge 1$, $A_{n+1}$ is
the least positive integer not in $U_n$, $B_{n+1}$ is the least positive integer not in
$U_n \cup \{A_{n+1}\}$, $C_{n+1} = A_{n+1} + B_{n+1}$, and
$U_{n+1} = U_n \cup \{A_{n+1}, B_{n+1}, C_{n+1}\}$.

The $C_n$ are the anti-Fibonacci numbers (OEIS A075326 without its initial $0$) and the missing
numbers $A_1, B_1, A_2, B_2, \dots$ are the non-anti-Fibonacci numbers $Y_1, Y_2, \dots$
(OEIS A249031).

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiFibonacciState`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 637](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L637). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-fibonacci-state).

## First summands of the anti-Fibonacci construction

For $n \ge 1$, $A_n$ is the first
entry of the $n$-th triple $(A_n, B_n, C_n)$ of the anti-Fibonacci construction: $A_1 = 1$, and
for $n \ge 2$, $A_n$ is the least positive integer that is not among the values $A_k$, $B_k$,
$C_k$ with $1 \le k < n$. At $n = 0$ the definition gives $A_0 = A_1 = 1$.

In the source's notation $A_n = Y_{2n-1}$, where $Y_1 < Y_2 < \dots$ are the non-anti-Fibonacci
numbers.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiFibonacciA`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 650](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L650). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-fibonacci-a).

## Second summands of the anti-Fibonacci construction

For $n \ge 1$, $B_n$ is the second
entry of the $n$-th triple $(A_n, B_n, C_n)$ of the anti-Fibonacci construction: $B_1 = 2$, and
for $n \ge 2$, $B_n$ is the second smallest positive integer that is not among the values $A_k$,
$B_k$, $C_k$ with $1 \le k < n$. At $n = 0$ the definition gives $B_0 = B_1 = 2$.

In the source's notation $B_n = Y_{2n}$, where $Y_1 < Y_2 < \dots$ are the non-anti-Fibonacci
numbers.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiFibonacciB`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-fibonacci-b).

## Anti-Fibonacci numbers

For $n \ge 1$, the anti-Fibonacci number $X_n = C_n$ is the third
entry of the $n$-th triple $(A_n, B_n, C_n)$ of the anti-Fibonacci construction, so
$C_n = A_n + B_n$ and $C_1 = 3$. At $n = 0$ the definition gives $C_0 = C_1 = 3$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiFibonacciC`, a definition declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-fibonacci-c).

## First anti-Fibonacci and non-anti-Fibonacci numbers

In the anti-Fibonacci construction
with triples $(A_n, B_n, C_n)$, the first four anti-Fibonacci numbers are $C_1 = 3$, $C_2 = 9$,
$C_3 = 13$ and $C_4 = 18$, and $(A_1, B_1) = (1, 2)$, $(A_2, B_2) = (4, 5)$,
$(A_3, B_3) = (6, 7)$ and $(A_4, B_4) = (8, 10)$.

Since $A_1, B_1, A_2, B_2, \dots$ are the non-anti-Fibonacci numbers, the first eight
non-anti-Fibonacci numbers are $1, 2, 4, 5, 6, 7, 8, 10$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Section 4.

Formalized by `MetaMathlibExt.antiFibonacci_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-fibonacci-small).

## Zaslavsky's formulas for the anti-Fibonacci numbers

Let $A_1 = 1$, $B_1 = 2$,
$C_1 = 3$, and for $n \ge 1$ let $A_{n+1} < B_{n+1}$ be the two smallest positive integers not
among $A_1, B_1, C_1, \ldots, A_n, B_n, C_n$ and $C_{n+1} = A_{n+1} + B_{n+1}$. Let
$\mathrm{PD}[0], \mathrm{PD}[1], \ldots$ be the letters of the period-doubling word, the fixed
point of $1 \mapsto 10$, $0 \mapsto 11$ starting with $1$. Then for every $k \ge 0$,
$C_{2k+1} = 10k + 3$, $C_{2k+2} = 10k + 8 + \mathrm{PD}[k]$, $A_{2k+1} = 5k + 1$,
$B_{2k+1} = 5k + 2$, $A_{2k+2} = 5k + 3 + \mathrm{PD}[k]$, and $B_{2k+2} = 5(k + 1)$.

In the source's notation the anti-Fibonacci numbers are $X_n = C_n$ and the
non-anti-Fibonacci numbers are $Y_{2n-1} = A_n$ and $Y_{2n} = B_n$, so the formulas read
$X_{2k+1} = 10k + 3$, $X_{2k+2} = 10k + 8 + \mathrm{PD}[k]$, $Y_{4k+1} = 5k + 1$,
$Y_{4k+2} = 5k + 2$, $Y_{4k+3} = 5k + 3 + \mathrm{PD}[k]$ and $Y_{4k+4} = 5(k + 1)$ (the
source's $Y_{4k} = 5k$ for $k \ge 1$). The source's prose writes the period-doubling word
over letters $a, b$ with $a = 0$, but its Walnut code and its values $X_2 = 9$ and $Y_3 = 4$
need $\mathrm{PD}[0] = 1$.

## Sources

- Bosma, Bruin, Fokkink, Grube, Reuijl, and Tromp, *Using Walnut to Solve Problems from the OEIS*, Journal of Integer Sequences 28 (2025), Article 25.3.8, Theorem 11 (`jis-2025-25.3.8-thm-11`), due to Zaslavsky.

Stated but not proved: `MetaMathlibExt.zaslavsky_antiFibonacci` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean, line 687](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/WalnutOeisProblemsWanted.lean#L687). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#zaslavsky-anti-fibonacci).

## Block of successive mex values

For a natural number $m$ and a finite set $s$ of natural
numbers, the mex block of length $m$ from $s$ is the list $(x_1, \dots, x_m)$ in which each $x_j$
is the least positive integer not in $s \cup \{x_1, \dots, x_{j-1}\}$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 2 (proof of Lemma 2, the mex rule).

Formalized by `MetaMathlibExt.antiRecurrenceBlock`, a definition declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-block).

## State of the anti-recurrence construction

Let $a = (a_1, \dots, a_k)$ be a finite list of
natural numbers. The state at step $0$ is the pair of the empty list and the empty set. If the
state at step $n$ has set $S$, then the state at step $n + 1$ is the pair $(\beta, S')$, where
$\beta = (x_1, \dots, x_k)$ is the mex block of length $k$ from $S$ (each $x_j$ is the least
positive integer not in $S \cup \{x_1, \dots, x_{j-1}\}$) and
$S' = S \cup \{x_1, \dots, x_k\} \cup \{a_1 x_1 + \dots + a_k x_k\}$.

In the notation of the source, for $n \ge 1$ the block at step $n$ is
$(B_{(n-1)k+1}, \dots, B_{nk})$ and the set at step $n$ is
$\{B_1, \dots, B_{nk}\} \cup \{A_1, \dots, A_n\}$, where the $B_m$ are the non-anti-recurrence
numbers and the $A_m$ are the anti-recurrence numbers of $a$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 2 (definition of anti-recurrence sequences and Lemma 2).

Formalized by `MetaMathlibExt.antiRecurrenceState`, a definition declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-state).

## Anti-recurrence numbers

Let $a = (a_1, \dots, a_k)$ be a linear form with natural number
coefficients. The non-anti-recurrence numbers $B_1, B_2, \dots$ are produced in blocks of $k$ by
the mex rule, and each block $B_{(n-1)k+1}, \dots, B_{nk}$ generates the anti-recurrence number
$A_n = \sum_{j=1}^{k} a_j B_{(n-1)k+j}$. Here $B_m$ is the least positive integer that differs
from $B_1, \dots, B_{m-1}$ and from the anti-recurrence numbers of earlier blocks. By convention
$A_0 = 0$, following Hofstadter.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 2 (definition of anti-recurrence sequences).

Formalized by `MetaMathlibExt.antiRecurrence`, a definition declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence).

## Non-anti-recurrence numbers

Let $a = (a_1, \dots, a_k)$ be a linear form with natural
number coefficients. Its non-anti-recurrence numbers $B_1, B_2, \dots$ are produced in blocks of
$k$ by the mex rule: for $n \ge 1$, each of $B_{(n-1)k+1}, \dots, B_{nk}$ in turn is the least
positive integer not among $B_1, \dots, B_{(n-1)k}$, the anti-recurrence numbers
$A_1, \dots, A_{n-1}$ and the earlier entries of its block, and then
$A_n = a_1 B_{(n-1)k+1} + \dots + a_k B_{nk}$. For $k = 2$ the subsequences $B^1_n = B_{2n-1}$
and $B^2_n = B_{2n}$ are the paper's $B^1$ and $B^2$.

By Lemma 2 of the source, for a positive form with $k > 1$ the numbers $B_m$ are the positive
integers that are not anti-recurrence numbers, listed in increasing order.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 2 (definition of anti-recurrence sequences).

Formalized by `MetaMathlibExt.antiRecurrenceComplement`, a definition declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-complement).

## First anti-Fibonacci anti-recurrence numbers

The anti-recurrence numbers
$A_1, A_2, A_3, A_4$ of the linear form $(1, 1)$ are $3, 9, 13, 18$, and the first four
anti-Fibonacci numbers $C_1, C_2, C_3, C_4$ of the Walnut anti-Fibonacci construction
(OEIS A075326) are also $3, 9, 13, 18$; so the two sequences agree for $1 \le n \le 4$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 1.

Formalized by `MetaMathlibExt.antiRecurrence_antiFibonacci_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-anti-fibonacci-small).

## First anti-Pell numbers

The anti-recurrence numbers $A_1, A_2, A_3, A_4$ of the linear
form $(1, 2)$, the anti-Pell numbers (OEIS A304502), are $5, 11, 20, 26$, and its first eight
non-anti-recurrence numbers $B_1, \dots, B_8$ are $1, 2, 3, 4, 6, 7, 8, 9$ (so
$B^1_n = B_{2n-1}$ starts $1, 3, 6, 8$ and $B^2_n = B_{2n}$ starts $2, 4, 7, 9$).

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 3.

Formalized by `MetaMathlibExt.antiRecurrence_antiPell_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-anti-pell-small).

## First anti-Jacobsthal numbers

The anti-recurrence numbers $A_1, A_2, A_3, A_4$ of the
linear form $(2, 1)$, the anti-Jacobsthal numbers (OEIS A304499), are $4, 11, 19, 25$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 3.

Formalized by `MetaMathlibExt.antiRecurrence_antiJacobsthal_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-anti-jacobsthal-small).

## First anti-Tribonacci anti-recurrence numbers

The anti-recurrence numbers
$A_1, A_2, A_3, A_4$ of the linear form $(1, 1, 1)$ are $6, 16, 27, 36$, and the first four
anti-Tribonacci numbers $D_1, D_2, D_3, D_4$ of the Walnut anti-Tribonacci construction
(OEIS A265389) are also $6, 16, 27, 36$; so the two sequences agree for $1 \le n \le 4$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Section 4.

Formalized by `MetaMathlibExt.antiRecurrence_antiTribonacci_small`, a theorem declared in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-anti-tribonacci-small).

## Gaps between successive anti-recurrence numbers

Let $a = (a_1, \dots, a_k)$ be a linear
form with positive integer coefficients and $k > 1$, let $\tau = a_1 + \dots + a_k$ be its trace,
and let $A_n$ and $B_m$ be the anti-recurrence and non-anti-recurrence numbers of $a$; for
$m \ge 1$, block $m$ consists of $B_{(m-1)k+1}, \dots, B_{mk}$, and it is an interval when
$B_{mk} = B_{(m-1)k+1} + k - 1$. Then for every $n \ge 1$ we have $A_{n+1} \ge A_n + k\tau$.
Equality holds if $B_{(n-1)k+1+j} = B_{(n-1)k+1} + j$ for every $j$ with $0 \le j < 2k$, that
is, if $B_{(n-1)k+1}, \dots, B_{(n+1)k}$ are consecutive integers. The inequality is strict if
exactly one of the blocks $n$ and $n + 1$ is an interval.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Lemma 1.

Stated but not proved: `MetaMathlibExt.antiRecurrence_add_length_mul_sum_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-add-length-mul-sum-le).

## Characterization of anti-recurrence sequences

Let $a = (a_1, \dots, a_k)$ be a linear
form with positive integer coefficients and $k > 1$, with anti-recurrence numbers
$A_1, A_2, \dots$ and non-anti-recurrence numbers $B_1, B_2, \dots$. Let $(x_i)_{i \ge 0}$ and
$(y_i)_{i \ge 0}$ be sequences of natural numbers. Then $x$ and $y$ are strictly increasing, every
$y_i$ is positive, every positive integer is a term of exactly one of $x$ and $y$, and
$x_i = \sum_{j=1}^{k} a_j y_{ik+j-1}$ for all $i$, if and only if $x_i = A_{i+1}$ and
$y_i = B_{i+1}$ for all $i$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Lemma 2.

Stated but not proved: `MetaMathlibExt.antiRecurrence_unique` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-unique).

## Intervals and residues of the anti-$k$-bonacci numbers

Let $k > 1$, let $A_n$ be the
anti-recurrence numbers of the linear form $(1, \dots, 1)$ of length $k$, and put
$i = \lfloor k/2 \rfloor$ and $\kappa = k^2 + 1$. Then for every $n \ge 1$, $A_n$ lies in the
interval $[\kappa(n - 1) + 1, \kappa n]$, and $A_n \equiv ik + c \pmod{\kappa}$ for some natural
number $c$ with $1 \le c \le k$ if $k$ is even and $i + 1 \le c \le i + k$ if $k$ is odd.

The paper attaches the condition $k > 2$ to $\kappa$; it is not needed, since $k = 2$ is the
anti-Fibonacci case (Zaslavsky's formula $A_n = 5n - 2 + PD_{n-1}$, with $PD$ the
period-doubling sequence).

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Lemma 3.

Stated but not proved: `MetaMathlibExt.antiBonacci_mem_Icc_and_modEq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-bonacci-mem-icc-and-mod-eq).

## Lower bound for the first anti-recurrence number

Let $a = (a_1, \dots, a_k)$ be a linear
form with positive integer coefficients, of trace $\tau = a_1 + \dots + a_k$, and let $A_1$ be its
first anti-recurrence number. Then $\tau + (k - 1)k/2 \le A_1$, and the inequality is strict if
and only if $a_j > 1$ for some $j$ with $2 \le j \le k$.

This corrects the printed strictness condition ("$k > 2$ and not anti-bonacci"), which fails for
$a = (2, 1, 1)$: there $A_1 = 2 + 2 + 3 = 7 = \tau + 3$. The correction follows the paper's
proof, $A_1 = \tau + \sum_j (j - 1) a_j$. The paper's hypothesis $k > 1$ is not needed.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Lemma 4.

Stated but not proved: `MetaMathlibExt.antiRecurrence_one_ge` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-one-ge).

## Interval location of anti-recurrence numbers for bounded forms

Let
$a = (a_1, \dots, a_k)$ be a linear form with positive integer coefficients and $k > 1$, of trace
$\tau = a_1 + \dots + a_k$, with anti-recurrence numbers $A_1, A_2, \dots$ and non-anti-recurrence
numbers $B_1, B_2, \dots$, and let $\kappa = k\tau + 1$. Suppose that $a$ is $A_1$-bounded, that
is, $A_1 \le (k - 1)\tau + 2$. Then for every $n \ge 1$, $A_n$ lies in the interval
$I_n = [\kappa(n - 1) + 1, \kappa n]$, and the first $k$ numbers of $I_n$ are non-anti-recurrence
numbers: $B_{(n-1)k\tau + j} = \kappa(n - 1) + j$ for $1 \le j \le k$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Lemma 5.

Stated but not proved: `MetaMathlibExt.antiRecurrence_mem_Icc_of_bounded` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-mem-icc-of-bounded).

## Kimberling's bounds for the anti-Pell numbers

Let $A_n$ be the anti-recurrence numbers
of the linear form $a = (1, 2)$ (the anti-Pell numbers), let $B_m$ be its non-anti-recurrence
numbers, and put $B^1_n = B_{2n-1}$ and $B^2_n = B_{2n}$. Then for every $n \ge 1$ we have
$0 \le A_n - 7n + 3 \le 2$, $0 \le 3B^1_n - 7n + 6 \le 3$ and $0 \le 3B^2_n - 7n + 2 \le 3$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Theorem 1.

Stated but not proved: `MetaMathlibExt.antiPell_kimberling_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-pell-kimberling-bounds).

## Kimberling's bounds for the anti-Jacobsthal numbers

Let $A_n$ be the anti-recurrence
numbers of the linear form $a = (2, 1)$ (the anti-Jacobsthal numbers), let $B_m$ be its
non-anti-recurrence numbers, and put $B^1_n = B_{2n-1}$ and $B^2_n = B_{2n}$. Then for every
$n \ge 1$ we have $0 \le A_n - 7n + 4 \le 3$, $0 \le 3B^1_n - 7n + 6 \le 4$ and
$0 \le 3B^2_n - 7n + 2 \le 3$.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Theorem 2.

Stated but not proved: `MetaMathlibExt.antiJacobsthal_kimberling_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-jacobsthal-kimberling-bounds).

## Bounded anti-recurrence sequences are automatic up to a linear term

Let
$a = (a_1, \dots, a_k)$ be a linear form with positive integer coefficients and $k > 1$, of trace
$\tau = a_1 + \dots + a_k$, with anti-recurrence numbers $A_1, A_2, \dots$, and let
$\kappa = k\tau + 1$. If $a$ is $A_1$-bounded, that is, $A_1 \le (k - 1)\tau + 2$, then the
integer sequence $n \mapsto A_{n+1} - \kappa(n + 1)$, indexed from $n = 0$, is $\tau$-automatic:
$\tau \ge 2$ and its $\tau$-kernel is finite.

Automaticity is stated through Eilenberg's characterization by a finite kernel, in place of the
paper's definition by a finite automaton with output.

## Sources

- Robbert Fokkink and Gandhar Joshi, *Anti-Recurrence Sequences*, INTEGERS 26 (2026), Article A24, Theorem 4.

Stated but not proved: `MetaMathlibExt.antiRecurrence_sub_isKAutomatic_of_bounded` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/AntiRecurrenceWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html#anti-recurrence-sub-is-kautomatic-of-bou).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Anti-recurrence and greedy subsum-free sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/anti-recurrence-and-greedy-subsum-free-sequences)
