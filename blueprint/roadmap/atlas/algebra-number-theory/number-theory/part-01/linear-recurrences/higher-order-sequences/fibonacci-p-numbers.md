---
declaration: section
origin: cited
lean: MetaMathlibExt.fibonacciP, MetaMathlibExt.fibonacciP_zero, MetaMathlibExt.fibonacciP_eq_one, MetaMathlibExt.fibonacciP_rec, MetaMathlibExt.fibonacciP_one, MetaMathlibExt.honsberger_fibonacciP
statement: formalized
proof: formalized
---

# Fibonacci p-numbers

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html).

## Fibonacci p-numbers

For a natural number $p$, the Fibonacci $p$-numbers are the
natural numbers $F_p(r)$, $r \in \mathbb{N}$, given by $F_p(0) = 0$, $F_p(r) = 1$ for
$1 \le r \le p$, and $F_p(r) = F_p(r-1) + F_p(r-p-1)$ for $r > p$.

## Sources

- Lines 79-85. From <https://cs.uwaterloo.ca/journals/JIS/VOL27/Kuhapatanakul/kuha13.tex>. Excludes the downstream generalized Leonardo identity and the separate finite-sum identity.

Formalized by `MetaMathlibExt.fibonacciP`, a definition declared in [MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html#fibonacci-p).

## Zeroth Fibonacci p-number

For every natural number $p$, the Fibonacci $p$-number
$F_p(0)$ equals $0$.

Formalized by `MetaMathlibExt.fibonacciP_zero`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html#fibonacci-p-zero).

## Initial Fibonacci p-numbers equal one

For all natural numbers $p$ and $r$ with
$1 \le r \le p$, the Fibonacci $p$-number $F_p(r)$ equals $1$.

Formalized by `MetaMathlibExt.fibonacciP_eq_one`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html#fibonacci-p-eq-one).

## Recurrence for Fibonacci p-numbers

For all natural numbers $p$ and $r$ with $p < r$,
the Fibonacci $p$-numbers satisfy $F_p(r) = F_p(r-1) + F_p(r-p-1)$.

Formalized by `MetaMathlibExt.fibonacciP_rec`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html#fibonacci-p-rec).

## Fibonacci 1-numbers are the Fibonacci numbers

For every natural number $n$, the
Fibonacci $1$-number $F_1(n)$ equals the $n$-th Fibonacci number $f_n$, where $f_0 = 0$,
$f_1 = 1$ and $f_{k+2} = f_{k+1} + f_k$.

Formalized by `MetaMathlibExt.fibonacciP_one`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html#fibonacci-p-one).

## Honsberger identity for Fibonacci p-numbers

Let $p$, $m$ and $n$ be positive integers
with $p \le m + 1$ and $p \le n + 2$, and write $F_p(r)$ for the Fibonacci $p$-numbers. Suppose
that $F_p(0) = 0$, that $F_p(r) = 1$ for $1 \le r \le p$, and that
$F_p(r) = F_p(r-1) + F_p(r-p-1)$ for $r > p$ (these hold by definition). Then

$$F_p(m+1)\,F_p(n+2) + \sum_{i=1}^{p} F_p(m+1-i)\,F_p(n+i+1-p) = F_p(m+n+2).$$

All indices in the sum are natural numbers, since $i \le p \le m + 1$ and
$n + i + 1 \ge n + 2 \ge p$.

Proof: by strong induction on $m$ from a uniform form of the recurrence, with a telescoping
base case.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL27/Kuhapatanakul/kuha13.tex>, lines 425-449. Excludes the downstream generalized Leonardo identity and the separate finite-sum identity. Definition from lines 79-85.

Formalized by `MetaMathlibExt.honsberger_fibonacciP`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/HonsbergerFibonacciP.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html#honsberger-fibonacci-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci p-numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/higher-order-sequences/fibonacci-p-numbers)
