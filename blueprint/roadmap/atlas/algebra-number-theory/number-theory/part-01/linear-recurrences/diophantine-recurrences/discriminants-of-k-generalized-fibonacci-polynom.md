---
declaration: section
origin: cited
lean: MetaMathlibExt.abs_discr_kGeneralizedFibonacciPolynomial_mem_iff, MetaMathlibExt.kGeneralizedFibonacci_discr_eq_index_bounds, MetaMathlibExt.kGeneralizedFibonacci_discr_eq_bounds
statement: formalized
---

# Discriminants of k-generalized Fibonacci polynomials

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/discriminants-of-k-generalized-fibonacci-polynom/index.html).

## When the absolute discriminant of a $k$-generalized Fibonacci polynomial is a $k$-generalized Fibonacci number

**When the absolute discriminant of a $k$-generalized Fibonacci polynomial is a
$k$-generalized Fibonacci number.** Let $k \ge 2$ be a natural number and let
$F : \mathbb{Z} \to \mathbb{Z}$ satisfy $F(n) = 0$ for every integer $n$ with
$2 - k \le n \le 0$, $F(1) = 1$, and $F(n) = F(n-1) + F(n-2) + \cdots + F(n-k)$ for every
integer $n \ge 2$, so that $F(n)$ for $n \ge 0$ is the $k$-generalized Fibonacci sequence. Then
the absolute value of the discriminant of the polynomial
$X^k - X^{k-1} - \cdots - X - 1 \in \mathbb{Z}[X]$ equals $F(n)$ for some natural number $n$ if
and only if $k = 2$ or $k = 3$.

For $k = 2$ the absolute value of the discriminant is $5 = F(5)$, and for $k = 3$ it is
$44 = F(8)$. The paper prints the target set as $\{F_n\}$; that it means the $k$-generalized
sequence follows from its Lemma 1 and from Batte and Luca's restatement of this theorem
(arXiv 2504.02514, Introduction). With the classical Fibonacci numbers the case $k = 3$ would
fail, since $44$ is not a Fibonacci number.

## Sources

- Florian Luca, *On the Discriminant of the k-Generalized Fibonacci Polynomial, II*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 1.

Stated but not proved: `MetaMathlibExt.abs_discr_kGeneralizedFibonacciPolynomial_mem_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/KGeneralizedFibonacciDiscriminantWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KGeneralizedFibonacciDiscriminantWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/discriminants-of-k-generalized-fibonacci-polynom/index.html#abs-discr-k-generalized-fibonacci-polyno).

## Bounds on the index in Luca's discriminant equation

Let $k > 100$ be a natural number
and let $F : \mathbb{Z} \to \mathbb{Z}$ satisfy $F(n) = 0$ for every integer $n$ with
$2 - k \le n \le 0$, $F(1) = 1$, and $F(n) = F(n-1) + F(n-2) + \cdots + F(n-k)$ for every
integer $n \ge 2$ (the $k$-generalized Fibonacci sequence). Write
$L = (k \log k - 2 \log(k-1)) / \log 2$, where $\log$ is the natural logarithm. If a natural
number $n$ satisfies $F(n)\,(k-1)^2 = 2^{k+1} k^k - (k+1)^{k+1}$, then
$k + 1.99 + L < n < k + 3.01 + L$.

The equation is the paper's equation (7),
$F(n) = (2^{k+1} k^k - (k+1)^{k+1}) / (k-1)^2$, multiplied by $(k-1)^2$.

## Sources

- Florian Luca, *On the Discriminant of the k-Generalized Fibonacci Polynomial, II*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 1. Equation (7) is written after multiplying by `(k-1)^2`; `F^{(k)}` is given by its defining properties as in `abs_discr_kGeneralizedFibonacciPolynomial_mem_iff`. By Theorem 1 the equation has no solution with `k > 100`, so this intermediate bound is implied by that statement.

Stated but not proved: `MetaMathlibExt.kGeneralizedFibonacci_discr_eq_index_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/KGeneralizedFibonacciDiscriminantWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KGeneralizedFibonacciDiscriminantWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/discriminants-of-k-generalized-fibonacci-polynom/index.html#k-generalized-fibonacci-discr-eq-index-b).

## Absolute bounds on solutions of Luca's discriminant equation

Let $k > 100$ be a natural
number and let $F : \mathbb{Z} \to \mathbb{Z}$ satisfy $F(n) = 0$ for every integer $n$ with
$2 - k \le n \le 0$, $F(1) = 1$, and $F(n) = F(n-1) + F(n-2) + \cdots + F(n-k)$ for every
integer $n \ge 2$ (the $k$-generalized Fibonacci sequence). If a natural number $n$ satisfies
$F(n)\,(k-1)^2 = 2^{k+1} k^k - (k+1)^{k+1}$, then $k < 2 \cdot 10^{16}$ and
$n < 1.5 \cdot 10^{18}$.

The equation is the paper's equation (7) multiplied by $(k-1)^2$.

## Sources

- Florian Luca, *On the Discriminant of the k-Generalized Fibonacci Polynomial, II*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 2. Equation (7) is written after multiplying by `(k-1)^2`, as in `kGeneralizedFibonacci_discr_eq_index_bounds`; by Theorem 1 the hypotheses are never met.

Stated but not proved: `MetaMathlibExt.kGeneralizedFibonacci_discr_eq_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/KGeneralizedFibonacciDiscriminantWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/KGeneralizedFibonacciDiscriminantWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/discriminants-of-k-generalized-fibonacci-polynom/index.html#k-generalized-fibonacci-discr-eq-bounds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discriminants of k-generalized Fibonacci polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/discriminants-of-k-generalized-fibonacci-polynom/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/discriminants-of-k-generalized-fibonacci-polynom)
