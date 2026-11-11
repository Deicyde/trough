---
declaration: section
origin: cited
lean: MetaMathlibExt.kFibonacci_mul_eq_repdigit_iff, MetaMathlibExt.kFibonacci_repdigit_index_lt, MetaMathlibExt.one_div_partialQuotient_bound_mul_lt_abs_mul_sub
statement: formalized
---

# Repdigit products of k-Fibonacci numbers

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-products-of-k-fibonacci-numbers/index.html).

## Products of two $k$-Fibonacci numbers that are repdigits

Let $k \ge 3$ and let
$(F_n)_{n \ge 2-k}$ be the $k$-generalized Fibonacci sequence, given by
$F_{2-k} = \dots = F_0 = 0$, $F_1 = 1$ and $F_n = F_{n-1} + F_{n-2} + \dots + F_{n-k}$
for $n \ge 2$. Let $a, \ell, m, n$ be natural numbers with $3 \le m \le n$, $\ell \ge 2$ and
$1 \le a \le 9$. Then $F_n F_m = a (10^\ell - 1)/9$ (the $\ell$-digit repdigit with digit $a$)
if and only if $(a, k, \ell, m, n) = (8, 3, 2, 3, 8)$; indeed $F_8 F_3 = 44 \cdot 2 = 88$ for
$k = 3$.

## Sources

- Safia Seffah, Salah Eddine Rihane, and Alain Togbé, *On an Equation Involving Repdigits and Products of Two k-Fibonacci Numbers*, INTEGERS 25 (2025), Article A55, Theorem 1.

Stated but not proved: `MetaMathlibExt.kFibonacci_mul_eq_repdigit_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciRepdigitProductWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KFibonacciRepdigitProductWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-products-of-k-fibonacci-numbers/index.html#k-fibonacci-mul-eq-repdigit-iff).

## Index bound for repdigit products of $k$-Fibonacci numbers

Let $k \ge 3$ and let
$(F_n)_{n \ge 2-k}$ be the $k$-generalized Fibonacci sequence, given by
$F_{2-k} = \dots = F_0 = 0$, $F_1 = 1$ and $F_n = F_{n-1} + F_{n-2} + \dots + F_{n-k}$
for $n \ge 2$. Let $a, \ell, m, n$ be natural numbers with $3 \le m \le n$, $\ell \ge 2$,
$1 \le a \le 9$ and $n \ge k + 2$. If $F_n F_m = a (10^\ell - 1)/9$, then
$n < 1.64 \cdot 10^{29} k^8 (\log k)^5$, where $\log$ is the natural logarithm.

## Sources

- Safia Seffah, Salah Eddine Rihane, and Alain Togbé, *On an Equation Involving Repdigits and Products of Two k-Fibonacci Numbers*, INTEGERS 25 (2025), Article A55, Lemma 5.

Stated but not proved: `MetaMathlibExt.kFibonacci_repdigit_index_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciRepdigitProductWanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KFibonacciRepdigitProductWanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-products-of-k-fibonacci-numbers/index.html#k-fibonacci-repdigit-index-lt).

## Partial-quotient lower bound for rational approximation

Let $\gamma$ be an irrational real
number with continued fraction $[a_0; a_1, a_2, \dots]$, so that $a_0 = \lfloor \gamma \rfloor$,
and let $q_0 = 1, q_1, q_2, \dots$ be the denominators of its convergents. Let $M \ge 1$ and
$N \ge 0$ be integers with $q_N \le M < q_{N+1}$, and let $A$ be a real number with $a_i \le A$
for $0 \le i \le N + 1$. Then $|x \gamma - y| > 1/((A + 2) x)$ for all integers $x, y$ with
$0 < x < M$.

Taking $A = \max(a_0, \dots, a_{N+1})$ gives the strongest bound.

## Sources

- Safia Seffah, Salah Eddine Rihane, and Alain Togbé, *On an Equation Involving Repdigits and Products of Two k-Fibonacci Numbers*, INTEGERS 25 (2025), Article A55, Lemma 2.

Stated but not proved: `MetaMathlibExt.one_div_partialQuotient_bound_mul_lt_abs_mul_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/KFibonacciRepdigitProductWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KFibonacciRepdigitProductWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-products-of-k-fibonacci-numbers/index.html#one-div-partial-quotient-bound-mul-lt-ab).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Repdigit products of k-Fibonacci numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-products-of-k-fibonacci-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/repdigit-products-of-k-fibonacci-numbers)
