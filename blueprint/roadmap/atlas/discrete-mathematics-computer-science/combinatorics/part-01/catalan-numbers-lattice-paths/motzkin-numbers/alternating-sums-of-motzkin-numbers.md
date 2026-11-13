---
declaration: section
origin: cited
lean: MetaMathlibExt.riordanNumber_even_logConvex, MetaMathlibExt.motzkinAlternatingSum, MetaMathlibExt.motzkinAlternatingSum_zero, MetaMathlibExt.motzkinAlternatingSum_succ, MetaMathlibExt.motzkinAlternatingSum_one_two, MetaMathlibExt.fibonacciAlternatingSum, MetaMathlibExt.fibonacciAlternatingSum_zero, MetaMathlibExt.fibonacciAlternatingSum_succ
statement: formalized
---

# Alternating sums of Motzkin numbers

12 results, 7 proved and 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html).

## Log-convexity of the even-indexed Riordan numbers

Let $r_n$ denote the $n$-th Riordan
number. The even-indexed Riordan numbers $r_0, r_2, r_4, \dots$ form a log-convex sequence: for
every natural number $n$,

$$r_{2n+2}^2 \le r_{2n} \, r_{2n+4}.$$

The Riordan numbers begin $1, 0, 1, 1, 3, 6, 15, \dots$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Corollary 1.

Stated but not proved: `MetaMathlibExt.riordanNumber_even_logConvex` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#riordan-number-even-log-convex).

## Alternating sums of Motzkin numbers

Let $M_k$ denote the $k$-th Motzkin number. For a
natural number $n$, the $n$-th alternating Motzkin sum is the integer

$$T_n = \sum_{k=0}^{n} (-1)^{n-k} M_k.$$

It is OEIS A187306, which begins $1, 0, 2, 2, 7, 14, 37, \dots$

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Equation (2).

Formalized by `MetaMathlibExt.motzkinAlternatingSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#motzkin-alternating-sum).

## The alternating Motzkin sum at 0

Let $M_k$ denote the $k$-th Motzkin number and let
$T_n = \sum_{k=0}^{n} (-1)^{n-k} M_k$. Then $T_0 = 1$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Table 2.

Formalized by `MetaMathlibExt.motzkinAlternatingSum_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#motzkin-alternating-sum-zero).

## Recurrence for alternating Motzkin sums

Let $M_k$ denote the $k$-th Motzkin number and
let $T_n = \sum_{k=0}^{n} (-1)^{n-k} M_k$. For every natural number $n$, $T_{n+1} = M_{n+1} - T_n$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Equation (2).

Formalized by `MetaMathlibExt.motzkinAlternatingSum_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#motzkin-alternating-sum-succ).

## Alternating Motzkin sums at 1 and 2

Let $M_k$ denote the $k$-th Motzkin number and let
$T_n = \sum_{k=0}^{n} (-1)^{n-k} M_k$. Then $T_1 = 0$ and $T_2 = 2$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Table 2.

Formalized by `MetaMathlibExt.motzkinAlternatingSum_one_two`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#motzkin-alternating-sum-one-two).

## Alternating sums of Fibonacci numbers

Let $F_k$ denote the $k$-th Fibonacci number,
with $F_0 = 0$ and $F_1 = 1$. For a natural number $n$, the $n$-th alternating Fibonacci sum is
the integer

$$W_n = \sum_{k=0}^{n} (-1)^{n-k} F_k.$$

The sequence begins $0, 1, 0, 2, 1, 4, 4, 9, \dots$

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Equation (9).

Formalized by `MetaMathlibExt.fibonacciAlternatingSum`, a definition declared in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#fibonacci-alternating-sum).

## The alternating Fibonacci sum at 0

Let $F_k$ denote the $k$-th Fibonacci number, with
$F_0 = 0$ and $F_1 = 1$, and let $W_n = \sum_{k=0}^{n} (-1)^{n-k} F_k$. Then $W_0 = 0$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Table 3.

Formalized by `MetaMathlibExt.fibonacciAlternatingSum_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#fibonacci-alternating-sum-zero).

## Recurrence for alternating Fibonacci sums

Let $F_k$ denote the $k$-th Fibonacci
number, with $F_0 = 0$ and $F_1 = 1$, and let $W_n = \sum_{k=0}^{n} (-1)^{n-k} F_k$. For every
natural number $n$, $W_{n+1} = F_{n+1} - W_n$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Equation (9).

Formalized by `MetaMathlibExt.fibonacciAlternatingSum_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#fibonacci-alternating-sum-succ).

## The alternating Motzkin sums are eventually log-balanced and tempered

Let $M_k$ denote
the $k$-th Motzkin number and let $T_n = \sum_{k=0}^{n} (-1)^{n-k} M_k$. For every natural
number $n \ge 9$,

$$T_n^2 \le T_{n-1} T_{n+1} \quad\text{and}\quad n T_{n-1} T_{n+1} \le (n+1) T_n^2,$$

and for every natural number $n \ge 6$,

$$n T_n^2 \le (n+1) T_{n-1} T_{n+1} \quad\text{and}\quad n T_{n-1} T_{n+1} \le (n+1) T_n^2.$$

Following Došlić, a positive sequence $(z_n)_{n \ge N}$ is log-balanced if it is log-convex,
$z_n^2 \le z_{n-1} z_{n+1}$, and $(z_n/n!)$ is log-concave, $n z_{n-1} z_{n+1} \le (n+1) z_n^2$,
for every $n \ge N + 1$; it is tempered if its quotients $x_n = z_{n+1}/z_n$ satisfy
$\frac{n}{n+1} x_{n-1} \le x_n \le \frac{n+1}{n} x_{n-1}$ for every $n \ge N + 1$. So the two
parts say that $(T_n)_{n \ge 8}$ is log-balanced and $(T_n)_{n \ge 5}$ is tempered, with the
inequalities cleared of denominators (all terms are positive here) and the factorials and
quotient weights using the original index $n$, as in the paper's proofs.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Theorem 1.

Stated but not proved: `MetaMathlibExt.motzkinAlternatingSum_logBalanced_tempered` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#motzkin-alternating-sum-log-balanced-tem).

## Products of consecutive alternating Motzkin sums are eventually log-convex and log-balanced

**Products of consecutive alternating Motzkin sums are eventually log-convex and
log-balanced.** Let $M_k$ denote the $k$-th Motzkin number, let
$T_n = \sum_{k=0}^{n} (-1)^{n-k} M_k$ and let $P_n = T_n T_{n+1}$. For every natural number
$n \ge 7$, $P_n^2 \le P_{n-1} P_{n+1}$; and for every natural number $n \ge 10$,
$P_n^2 \le P_{n-1} P_{n+1}$ and $n P_{n-1} P_{n+1} \le (n+1) P_n^2$.

Following Došlić, a positive sequence $(z_n)_{n \ge N}$ is log-convex if
$z_n^2 \le z_{n-1} z_{n+1}$ for every $n \ge N + 1$, and log-balanced if moreover $(z_n/n!)$ is
log-concave, $n z_{n-1} z_{n+1} \le (n+1) z_n^2$, for every $n \ge N + 1$. So the two parts say
that $(P_n)_{n \ge 6}$ is log-convex and $(P_n)_{n \ge 9}$ is log-balanced.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Theorem 2.

Stated but not proved: `MetaMathlibExt.motzkinAlternatingSum_mul_succ_logConvex_logBalanced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#motzkin-alternating-sum-mul-succ-log-con).

## Log-balancedness of Motzkin numbers plus their alternating sums

Let $M_n$ denote the
$n$-th Motzkin number, let $T_n = \sum_{k=0}^{n} (-1)^{n-k} M_k$ be the alternating sum of
Motzkin numbers, and put $z_n = M_n + T_n$. Then the sequence $(z_n)_{n \ge 6}$ is log-balanced:
for every natural number $n \ge 7$,

$$z_n^2 \le z_{n-1} \, z_{n+1} \quad\text{and}\quad n \, z_{n-1} \, z_{n+1} \le (n+1) \, z_n^2.$$

The first inequality is log-convexity; for positive terms the second is log-concavity of
$z_n / n!$ with denominators cleared, the factorial using the original index $n$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Theorem 3.

Stated but not proved: `MetaMathlibExt.motzkinNumber_add_motzkinAlternatingSum_logBalanced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#motzkin-number-add-motzkin-alternating-s).

## The alternating Fibonacci sums are eventually tempered

Let $F_k$ denote the $k$-th
Fibonacci number, with $F_0 = 0$ and $F_1 = 1$, and let $W_n = \sum_{k=0}^{n} (-1)^{n-k} F_k$.
For every natural number $n \ge 12$,

$$n W_n^2 \le (n+1) W_{n-1} W_{n+1} \quad\text{and}\quad n W_{n-1} W_{n+1} \le (n+1) W_n^2.$$

These are the conditions $\frac{n}{n+1} x_{n-1} \le x_n \le \frac{n+1}{n} x_{n-1}$ on the
quotients $x_n = W_{n+1}/W_n$, cleared of denominators (all terms are positive here), so the
sequence $(W_n)_{n \ge 11}$ is tempered, with the conditions imposed at every index $n \ge 12$.

## Sources

- Feng-Zhen Zhao, *The Log-Balancedness of the Sequence for the Alternating Sums of Motzkin Numbers*, INTEGERS 26 (2026), Article A55, Theorem 4.

Stated but not proved: `MetaMathlibExt.fibonacciAlternatingSum_tempered` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/MotzkinAlternatingSumsWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html#fibonacci-alternating-sum-tempered).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Alternating sums of Motzkin numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/alternating-sums-of-motzkin-numbers)
