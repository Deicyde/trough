---
declaration: section
origin: cited
lean: MetaMathlibExt.tribonacciInt_neg_ten, MetaMathlibExt.brocardRamanujan_not_tribonacci, MetaMathlibExt.brocardRamanujan_not_tetranacci, MetaMathlibExt.tribonacci_padicValInt_fortySeven
statement: formalized
---

# Brocard–Ramanujan equation in recurrence sequences

4 results, 1 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/brocard-ramanujan-equation-in-recurrence-sequenc/index.html).

## The Tribonacci number of index $-10$

Let $(T_n)_{n \in \mathbb{Z}}$ be the two-sided
Tribonacci sequence, determined by $T_0 = 0$, $T_1 = T_2 = 1$ and
$T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for all integers $n$. Then $T_{-10} = 5$.

Since $4! + 1 = 5^2$, the equation $m! + 1 = T_n^2$ has a solution once negative indices $n$ are
allowed.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Theorem 1 normalization note.

Formalized by `MetaMathlibExt.tribonacciInt_neg_ten`, a theorem declared in [WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/brocard-ramanujan-equation-in-recurrence-sequenc/index.html#tribonacci-int-neg-ten).

## The Brocard–Ramanujan equation has no Tribonacci solutions

Let $(T_n)_{n \ge 0}$ be the
Tribonacci sequence, given by $T_0 = T_1 = 0$, $T_2 = 1$ and $T_{n+3} = T_{n+2} + T_{n+1} + T_n$
for $n \ge 0$. For all natural numbers $m$ and $n$, $m! + 1 \ne T_n^2$.

Only nonnegative indices are allowed: the extension of the Tribonacci sequence to negative indices
by the same recurrence takes the value $5$, and $4! + 1 = 5^2$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Theorem 1.

Stated but not proved: `MetaMathlibExt.brocardRamanujan_not_tribonacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/brocard-ramanujan-equation-in-recurrence-sequenc/index.html#brocard-ramanujan-not-tribonacci).

## The Brocard–Ramanujan equation has no Tetranacci solutions

Let $(Q_n)_{n \ge 0}$ be the
Tetranacci sequence, given by $Q_0 = Q_1 = Q_2 = 0$, $Q_3 = 1$ and
$Q_{n+4} = Q_{n+3} + Q_{n+2} + Q_{n+1} + Q_n$ for $n \ge 0$. For all natural numbers $m$ and $n$,
$m! + 1 \ne Q_n^2$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Theorem 2.

Stated but not proved: `MetaMathlibExt.brocardRamanujan_not_tetranacci` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/brocard-ramanujan-equation-in-recurrence-sequenc/index.html#brocard-ramanujan-not-tetranacci).

## The $47$-adic valuation of Tribonacci numbers near $\pm 1$

Let $(T_n)_{n \in \mathbb{Z}}$
be the two-sided Tribonacci sequence, determined by $T_0 = 0$, $T_1 = T_2 = 1$ and
$T_{n+3} = T_{n+2} + T_{n+1} + T_n$ for all integers $n$. Let $\nu_{47}$ be the $47$-adic
valuation on the integers, with the convention $\nu_{47}(0) = 0$, and let
$J = \{1, 2, -2, -3, -7\}$. First, $T_j = 1$ or $T_j = -1$ for every $j \in J$. Second, for every
$j \in J$ and every nonzero integer $r$, $\nu_{47}(T_{46r+j} - T_j) = 1 + \nu_{47}(r)$. Third, for
every integer $n$ that is not of the form $46r + j$ with $j \in J$ and $r \in \mathbb{Z}$, neither
$T_n - 1$ nor $T_n + 1$ is divisible by $47$.

The condition $r \ne 0$ is needed because $\nu_{47}(0)$ is $0$ here, whereas the paper uses an
infinite valuation at $0$.

## Sources

- Paul Thomas Young, *On the Brocard-Ramanujan Equation with Tribonacci and Tetranacci Numbers*, INTEGERS 24 (2024), Article A92, Proposition 1.

Stated but not proved: `MetaMathlibExt.tribonacci_padicValInt_fortySeven` is written with `theorem_wanted` in [WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/BrocardRamanujanTribonacciWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/brocard-ramanujan-equation-in-recurrence-sequenc/index.html#tribonacci-padic-val-int-forty-seven).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Brocard–Ramanujan equation in recurrence sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/brocard-ramanujan-equation-in-recurrence-sequenc/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/brocard-ramanujan-equation-in-recurrence-sequenc)
