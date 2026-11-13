---
declaration: section
origin: cited
lean: MetaMathlibExt.multiplicative_additive_on_squares, MetaMathlibExt.consecutiveSquareSums_kAdditiveUniqueness, MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.IsSumTwoPositiveTriangular, MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_classification, MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_eq_id_le_21, MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_zero_of_three_ne_zero, MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_zero_of_five_ne_zero, MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_zero_of_all_zero
statement: formalized
---

# Additive uniqueness of multiplicative functions

38 results, 1 proved and 37 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html).

## Multiplicative functions additive on pairs of squares

Let $f$ be a complex-valued
multiplicative arithmetic function (so $f(1) = 1$ and $f(ab) = f(a) f(b)$ for coprime $a$ and
$b$) such that $f(m^2 + n^2) = f(m^2) + f(n^2)$ for all positive integers $m$ and $n$. Then
$f(4)$ is $0$ or $4$; $f(q^{2k}) = f(q^2)^k$ for all positive integers $q$ and $k$; and if
$f(4) = 4$, then $f(m^2) = m^2$ for every positive integer $m$.

The source also assumes $f \ne 0$, which follows from $f(1) = 1$.

## Sources

- Elchin Hasanalizade, *On the k-Additive Uniqueness of Sums of Consecutive Squares for Multiplicative Functions*, INTEGERS 25 (2025), Article A40, Theorem 1.

Stated but not proved: `MetaMathlibExt.multiplicative_additive_on_squares` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ConsecutiveSquareSumsAdditiveUniquenessWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ConsecutiveSquareSumsAdditiveUniquenessWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-on-squares).

## Sums of consecutive squares form a $k$-additive uniqueness set for every $k \ge 2$

Let
$k \ge 2$, and call a natural number a sum of consecutive squares if it equals
$(n+1)^2 + (n+2)^2 + \dots + m^2$ for some natural numbers $n < m$. Let $f$ be a complex-valued
multiplicative arithmetic function (so $f(1) = 1$ and $f(ab) = f(a) f(b)$ for coprime $a$ and
$b$). If $f(x_1 + \dots + x_k) = f(x_1) + \dots + f(x_k)$ for all sums of consecutive squares
$x_1, \dots, x_k$, then $f(n) = n$ for every natural number $n$.

## Sources

- Elchin Hasanalizade, *On the k-Additive Uniqueness of Sums of Consecutive Squares for Multiplicative Functions*, INTEGERS 25 (2025), Article A40, Theorem 2.

Stated but not proved: `MetaMathlibExt.consecutiveSquareSums_kAdditiveUniqueness` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ConsecutiveSquareSumsAdditiveUniquenessWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ConsecutiveSquareSumsAdditiveUniquenessWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#consecutive-square-sums-k-additive-uniqu).

## Sums of two positive triangular numbers

A natural number $n$ is a sum of two positive
triangular numbers if there are natural numbers $a \ge 1$ and $b \ge 1$ with
$2n = a(a+1) + b(b+1)$, that is, $n = \frac{a(a+1)}{2} + \frac{b(b+1)}{2}$.

Formalized by `MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.IsSumTwoPositiveTriangular`, a definition declared in [WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#is-sum-two-positive-triangular).

## Park's theorem on multiplicative functions additive on sums of two triangular numbers

Let $f$ be a multiplicative arithmetic function with values in $\mathbb{C}$ (so $f$ is defined on
the natural numbers with $f(0) = 0$) such that $f(a + b) = f(a) + f(b)$ whenever $a$ and $b$ are
both sums of two positive triangular numbers. Then either $f(n) = n$ for every natural number
$n$, or $f(n) = 0$ for every natural number $n \notin \{1, 3, 5\}$ and $f(3) f(5) = 0$.

## Sources

- Poo-Sung Park, "Multiplicative Functions Additive on the Sums of Two Positive Triangular Numbers", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_classification` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-on-sum-two-trian).

## Park's Lemma 2: the identity up to 21 when the value at 2 is nonzero

Let $f$ be a
multiplicative arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$
whenever $a$ and $b$ are both sums of two positive triangular numbers. If $f(2) \neq 0$, then
$f(n) = n$ for every natural number $n \le 21$.

## Sources

- Poo-Sung Park, "Multiplicative Functions Additive on the Sums of Two Positive Triangular Numbers", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_eq_id_le_21` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-on-sum-two-trian-2).

## Park's Lemma 3: vanishing from 4 to 21 when the value at 2 is zero and at 3 is not

Let
$f$ be a multiplicative arithmetic function with values in $\mathbb{C}$ such that
$f(a + b) = f(a) + f(b)$ whenever $a$ and $b$ are both sums of two positive triangular numbers.
If $f(2) = 0$ and $f(3) \neq 0$, then $f(n) = 0$ for every natural number $n$ with
$4 \le n \le 21$.

## Sources

- Poo-Sung Park, "Multiplicative Functions Additive on the Sums of Two Positive Triangular Numbers", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_zero_of_three_ne_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-on-sum-two-trian-3).

## Park's Lemma 4: vanishing from 2 to 21 except at 5

Let $f$ be a multiplicative
arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$ whenever
$a$ and $b$ are both sums of two positive triangular numbers. If $f(2) = 0$ and $f(5) \neq 0$,
then $f(n) = 0$ for every natural number $n$ with $2 \le n \le 21$ and $n \neq 5$.

## Sources

- Poo-Sung Park, "Multiplicative Functions Additive on the Sums of Two Positive Triangular Numbers", Lemma 4.

Stated but not proved: `MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_zero_of_five_ne_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-on-sum-two-trian-4).

## Park's Lemma 5: vanishing from 2 to 21 when the values at 2, 3 and 5 are zero

Let $f$
be a multiplicative arithmetic function with values in $\mathbb{C}$ such that
$f(a + b) = f(a) + f(b)$ whenever $a$ and $b$ are both sums of two positive triangular numbers.
If $f(2) = f(3) = f(5) = 0$, then $f(n) = 0$ for every natural number $n$ with $2 \le n \le 21$.

## Sources

- Poo-Sung Park, "Multiplicative Functions Additive on the Sums of Two Positive Triangular Numbers", Lemma 5.

Stated but not proved: `MathlibExt.NumberTheory.ArithmeticFunction.MultiplicativeTriangularAdditiveWanted.multiplicative_additive_on_sum_two_triangular_zero_of_all_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/MultiplicativeTriangularAdditiveWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-on-sum-two-trian-5).

## Additive uniqueness of generalized nonagonal numbers

Let $f$ be a multiplicative
arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$ for all
positive integers $a$ and $b$ that are generalized nonagonal numbers, that is, $2a = m(7m - 5)$
and $2b = k(7k - 5)$ for some integers $m$ and $k$. Then $f(n) = n$ for every natural number $n$.

## Sources

- Poo-Sung Park, *On the Additive Uniqueness of Generalized Nonagonal Numbers for Multiplicative Functions*, INTEGERS 25 (2025), Article A99, Theorem 1.

Stated but not proved: `MetaMathlibExt.multiplicative_nonagonal_additive_eq_id` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-nonagonal-additive-eq-id).

## Nonagonal additive uniqueness: the values up to 11

Let $f$ be a multiplicative
arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$ for all
positive integers $a$ and $b$ that are generalized nonagonal numbers, that is, $2a = m(7m - 5)$
and $2b = k(7k - 5)$ for some integers $m$ and $k$. Then $f(n) = n$ for every integer $n$ with
$1 \le n \le 11$.

## Sources

- Poo-Sung Park, *On the Additive Uniqueness of Generalized Nonagonal Numbers for Multiplicative Functions*, INTEGERS 25 (2025), Article A99, Lemma 1.

Stated but not proved: `MetaMathlibExt.multiplicative_nonagonal_additive_eq_self_of_le_eleven` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-nonagonal-additive-eq-sel).

## Nonagonal additive uniqueness: the step at powers of 3

Let $f$ be a multiplicative
arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$ for all
positive integers $a$ and $b$ that are generalized nonagonal numbers, that is, $2a = m(7m - 5)$
and $2b = k(7k - 5)$ for some integers $m$ and $k$. Let $r$ be a natural number and put
$\alpha(x) = \frac{14}{17} \cdot \frac{2}{3} x - \frac{12}{17}$. If $f(n) = n$ for every natural
number $n < \alpha(3^r)$, then $f(3^r) = 3^r$.

## Sources

- Poo-Sung Park, *On the Additive Uniqueness of Generalized Nonagonal Numbers for Multiplicative Functions*, INTEGERS 25 (2025), Article A99, Theorem 2.

Stated but not proved: `MetaMathlibExt.multiplicative_nonagonal_additive_three_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-nonagonal-additive-three).

## Nonagonal additive uniqueness: the step at powers of 5

Let $f$ be a multiplicative
arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$ for all
positive integers $a$ and $b$ that are generalized nonagonal numbers, that is, $2a = m(7m - 5)$
and $2b = k(7k - 5)$ for some integers $m$ and $k$. Let $r \ge 3$ be a natural number and put
$\beta(x) = x/4$. If $f(n) = n$ for every natural number $n \le \beta(5^r)$, then $f(5^r) = 5^r$.

## Sources

- Poo-Sung Park, *On the Additive Uniqueness of Generalized Nonagonal Numbers for Multiplicative Functions*, INTEGERS 25 (2025), Article A99, Theorem 3.

Stated but not proved: `MetaMathlibExt.multiplicative_nonagonal_additive_five_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-nonagonal-additive-five-p).

## Nonagonal additive uniqueness: the step at powers of 7

Let $f$ be a multiplicative
arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$ for all
positive integers $a$ and $b$ that are generalized nonagonal numbers, that is, $2a = m(7m - 5)$
and $2b = k(7k - 5)$ for some integers $m$ and $k$. Let $r$ be a natural number. If $f(n) = n$
for every natural number $n < 7^r$, then $f(7^r) = 7^r$.

## Sources

- Poo-Sung Park, *On the Additive Uniqueness of Generalized Nonagonal Numbers for Multiplicative Functions*, INTEGERS 25 (2025), Article A99, Theorem 4.

Stated but not proved: `MetaMathlibExt.multiplicative_nonagonal_additive_seven_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-nonagonal-additive-seven).

## Nonagonal additive uniqueness: the step at powers of 2

Let $f$ be a multiplicative
arithmetic function with values in $\mathbb{C}$ such that $f(a + b) = f(a) + f(b)$ for all
positive integers $a$ and $b$ that are generalized nonagonal numbers, that is, $2a = m(7m - 5)$
and $2b = k(7k - 5)$ for some integers $m$ and $k$. Let $r$ be a natural number. If $f(n) = n$
for every natural number $n < 2^r$, then $f(2^r) = 2^r$.

## Sources

- Poo-Sung Park, *On the Additive Uniqueness of Generalized Nonagonal Numbers for Multiplicative Functions*, INTEGERS 25 (2025), Article A99, Theorem 5.

Stated but not proved: `MetaMathlibExt.multiplicative_nonagonal_additive_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/NonagonalAdditiveUniquenessWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-nonagonal-additive-two-po).

## Parallelogram uniqueness of squares for multiplicative functions

Let $f$ be a
complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$, and suppose $f(4) \ne 0$. Then $f(n) = n^2$ for every natural number $n$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Theorem 1.

Stated but not proved: `MetaMathlibExt.multiplicative_parallelogram_squares_eq_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-parallelogram-squares-eq).

## Multiplicative parallelogram solutions vanishing at 4

Let $f$ be a complex-valued
multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$, and suppose $f(4) = 0$. Then one of the following holds:
(1) for every natural number $n$, $f(n) = 0$ if $n \equiv 0 \pmod 4$, $f(n) = 4$ if
$n \equiv 2 \pmod 4$, and $f(n) = 1$ otherwise;
(2) $f(2) = 4$, $f(2^r) = 0$ for every $r \ge 2$, and $f(p^r) = \left(\frac{-1}{p}\right)^r p^r$
for every odd prime $p$ and every $r \ge 1$, where $\left(\frac{-1}{p}\right)$ is the Jacobi
symbol.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Theorem 2.

Stated but not proved: `MetaMathlibExt.multiplicative_parallelogram_squares_of_f_four_eq_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-parallelogram-squares-of).

## Values of a parallelogram-equation multiplicative function at powers of two

Let $f$ be
a complex-valued multiplicative arithmetic function such that
$f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers $m > n \ge 1$. If $f(4) = 0$,
then $f(2^r) = 0$ for every integer $r \ge 2$. If $f(4) \ne 0$, then $f(2^r) = 2^{2r}$ for every
integer $r \ge 1$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Theorem 3.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_two_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-two-pow).

## Parallelogram induction: the value at p² + 1

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p$ is odd and $f(p) = p^2$, then $f(p^2 + 1) = (p^2 + 1)^2$.

The hypothesis $p \ne 2$ is needed: the function with $f(n) = 0$ if $4 \mid n$, $f(n) = 4$ if
$n \equiv 2 \pmod 4$ and $f(n) = 1$ otherwise satisfies the hypotheses for $p = 2$, but
$f(5) = 1$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Lemma 1.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_sq_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-sq-add-one).

## Parallelogram induction: the values at p + 2 and (p + 2)²

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p \equiv 3 \pmod 4$, then $f(p + 2) = (p + 2)^2$ and $f((p + 2)^2) = (p + 2)^4$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Lemma 2.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_add_two` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-add-two).

## Parallelogram induction: the values at k² + 1 and 4k² + 1

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p = 4k - 1$ for a natural number $k$, then $f(k^2 + 1) = (k^2 + 1)^2$ and
$f(4k^2 + 1) = (4k^2 + 1)^2$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Lemma 3.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_k_sq_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-k-sq-add-on).

## Parallelogram induction: the value at 5k + 3

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p = 4k - 1$ for a natural number $k$ with $4 \nmid k$, and $p \ge 19$, then
$f(5k + 3) = (5k + 3)^2$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Lemma 4.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_five_k_add_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-five-k-add).

## Parallelogram induction: the value at 6k + 1

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p = 4k - 1$ for a natural number $k$ with $k \not\equiv 3 \pmod 4$, and $p \ge 19$,
then $f(6k + 1) = (6k + 1)^2$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Lemma 5.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_six_k_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-six-k-add-o).

## Parallelogram induction: odd prime powers

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p$ is odd and $f(p) = p^2$, then $f(p^r) = p^{2r}$ for every integer $r \ge 2$.

The hypothesis $p \ne 2$ is needed: the function with $f(n) = 0$ if $4 \mid n$, $f(n) = 4$ if
$n \equiv 2 \pmod 4$ and $f(n) = 1$ otherwise satisfies the hypotheses for $p = 2$, but
$f(4) = 0$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Theorem 4.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_prime_pow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-prime-pow).

## Parallelogram induction: primes congruent to 1 mod 4

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p \equiv 1 \pmod 4$, then $f(p) = p^2$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Theorem 5.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_prime_one_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 190](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L190). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-prime-one-m).

## Parallelogram induction: primes congruent to 3 mod 4 from 19 on

Let $f$ be a complex-valued multiplicative arithmetic function
(so $f(0) = 0$) such that $f(m^2 + n^2) + f(m^2 - n^2) = 2f(m^2) + 2f(n^2)$ for all integers
$m > n \ge 1$.
Let $p$ be a prime such that $f(q^s) = q^{2s}$ for every prime $q < p$ and every integer
$s \ge 1$.
If $p = 4k - 1$ for some natural number $k$ and $p \ge 19$, then $f(p) = p^2$.

## Sources

- Poo-Sung Park, *On the Parallelogram Uniqueness of Square Numbers for Multiplicative Functions*, INTEGERS 24 (2024), Article A108, Theorem 6.

Stated but not proved: `MetaMathlibExt.parallelogram_multiplicative_prime_three_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/ParallelogramSquareUniquenessWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#parallelogram-multiplicative-prime-three).

## A square–triangular number identity

Let $t_v = v(v + 1)/2$ denote the $v$-th triangular
number. For every natural number $n \ge 2$, $n^2 + t_{n-2} = (n - 1)^2 + t_n$.

## Sources

- Mingyu Kim and Poo-Sung Park, *An Additive Uniqueness Pair of Sets for Multiplicative Functions: Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A103, Lemma 1.

Stated but not proved: `MetaMathlibExt.sq_add_triangular_sub_two_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#sq-add-triangular-sub-two-eq).

## Square–triangular additivity fixes small squares

Let $t_v = v(v + 1)/2$ denote the
$v$-th triangular number, and let $f$ be a complex-valued multiplicative arithmetic function
with $f(u^2 + t_v) = f(u^2) + f(t_v)$ for all positive integers $u$ and $v$. Let $N \ge 3$ be an
integer such that $f(n) = n$ for every integer $n$ with $1 \le n \le N - 1$. Then
$f(m^2) = m^2$ for every integer $m$ with $1 \le m \le N - 2$.

## Sources

- Mingyu Kim and Poo-Sung Park, *An Additive Uniqueness Pair of Sets for Multiplicative Functions: Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A103, Lemma 2.

Stated but not proved: `MetaMathlibExt.multiplicative_sq_triangular_additive_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-sq-triangular-additive-sq).

## Square–triangular additivity fixes odd powers of two

Let $t_v = v(v + 1)/2$ denote the
$v$-th triangular number, and let $f$ be a complex-valued multiplicative arithmetic function
with $f(u^2 + t_v) = f(u^2) + f(t_v)$ for all positive integers $u$ and $v$. Let $N \ge 4$ be an
integer such that $f(n) = n$ for every integer $n$ with $1 \le n \le N - 1$. Then
$f(2^{2k-1}) = 2^{2k-1}$ for every positive integer $k$ with $2k \le N - 2$.

## Sources

- Mingyu Kim and Poo-Sung Park, *An Additive Uniqueness Pair of Sets for Multiplicative Functions: Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A103, Lemma 3.

Stated but not proved: `MetaMathlibExt.multiplicative_sq_triangular_additive_two_pow_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-sq-triangular-additive-tw).

## Squares and triangular numbers are an additive uniqueness pair

Let $t_v = v(v + 1)/2$
denote the $v$-th triangular number. If $f$ is a complex-valued multiplicative arithmetic
function with $f(u^2 + t_v) = f(u^2) + f(t_v)$ for all positive integers $u$ and $v$, then
$f(n) = n$ for every natural number $n$.

## Sources

- Mingyu Kim and Poo-Sung Park, *An Additive Uniqueness Pair of Sets for Multiplicative Functions: Squares and Triangular Numbers*, INTEGERS 26 (2026), Article A103, Theorem 1.

Stated but not proved: `MetaMathlibExt.multiplicative_sq_triangular_additive_eq_id` is written with `theorem_wanted` in [WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/ArithmeticFunction/SquareTriangularAdditiveUniquenessWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-sq-triangular-additive-eq).

## Dubouis's theorem on sums of nonzero squares

Let $m \ge 4$ and let $n$ be a positive
integer. Then $n$ is a sum of $m$ squares of positive integers if and only if $n$ does not lie in
the exceptional set $E_m$, where
$E_4 = \{1, 3, 5, 9, 11, 17, 29, 41\} \cup \{2 \cdot 4^r, 6 \cdot 4^r, 14 \cdot 4^r : r \ge 0\}$,
$E_5 = \{1, 2, 3, 4, 6, 7, 9, 10, 12, 15, 18, 33\}$, and for $m \ge 6$,
$E_m = \{1, \dots, m - 1\} \cup \{m + 1, m + 2, m + 4, m + 5, m + 7, m + 10, m + 13\}$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Lemma 1, quoting Dubouis (1911).

Stated but not proved: `MetaMathlibExt.sum_nonzero_squares_iff_not_mem_exceptional` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#sum-nonzero-squares-iff-not-mem-exceptio).

## Sums of six and of eight nonzero squares

Every integer $n \ge 20$ is a sum of $6$
squares of positive integers, and every integer $n \ge 22$ is a sum of $8$ squares of positive
integers.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Corollary 1, as extracted inside the Lemma 1 record.

Stated but not proved: `MetaMathlibExt.sum_six_and_eight_nonzero_squares` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#sum-six-and-eight-nonzero-squares).

## Small values of a multiplicative function 3-additive on sums of two squares

Let
$E_2 = \{a^2 + b^2 : a, b \ge 1\}$ be the set of sums of two squares of positive integers. If $f$
is a complex-valued multiplicative function with $f(2) \ne 0$ such that
$f(A_1 + A_2 + A_3) = f(A_1) + f(A_2) + f(A_3)$ for all $A_1, A_2, A_3 \in E_2$, then $f(2) = 2$,
$f(3) = 3$ and $f(5) = 5$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Lemma 2.

Stated but not proved: `MetaMathlibExt.multiplicative_three_additive_two_squares_base` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-three-additive-two-square).

## Small values of a multiplicative function 4-additive on sums of two squares

Let
$E_2 = \{a^2 + b^2 : a, b \ge 1\}$ be the set of sums of two squares of positive integers. If $f$
is a complex-valued multiplicative function with $f(2) \ne 0$ such that
$f(A_1 + A_2 + A_3 + A_4) = f(A_1) + f(A_2) + f(A_3) + f(A_4)$ for all $A_1, \dots, A_4 \in E_2$,
then $f(n) = n$ for every $n \in \{2, 3, 4, 5, 6, 7, 8, 10\}$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Lemma 3.

Stated but not proved: `MetaMathlibExt.multiplicative_four_additive_two_squares_base` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-four-additive-two-squares).

## Multiplicative functions additive on six or eight paired squares and nonzero at $2$ are the identity

**Multiplicative functions additive on six or eight paired squares and nonzero at $2$ are
the identity.** Let $k \in \{3, 4\}$ and let $f$ be a complex-valued multiplicative function
with $f(2) \ne 0$ such that

$$f\Big(\sum_{j=1}^{k} (x_j^2 + y_j^2)\Big) = \sum_{j=1}^{k} f(x_j^2 + y_j^2)$$

for all positive integers $x_1, \dots, x_k, y_1, \dots, y_k$. Then $f(n) = n$ for every positive
integer $n$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Theorem 1.

Stated but not proved: `MetaMathlibExt.multiplicative_additive_paired_squares_eq_id_of_three_or_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-paired-squares-e).

## Dichotomy for multiplicative functions additive on paired squares

Let $k \ge 5$ and
let $f$ be a complex-valued multiplicative function such that

$$f\Big(\sum_{j=1}^{k} (x_j^2 + y_j^2)\Big) = \sum_{j=1}^{k} f(x_j^2 + y_j^2)$$

for all positive integers $x_1, \dots, x_k, y_1, \dots, y_k$. Then either $f(n) = n$ for every
positive integer $n$, or $f(n) = 0$ for every positive integer $n$ that is of the form $a^2 + b^2$
with integers $a, b \ge 1$, or of the form $2k + t$ with $t \in \{0, 3, 6, 8, 9, 11, 12\}$, or
satisfies $n \ge 2k + 14$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Theorem 2.

Stated but not proved: `MetaMathlibExt.multiplicative_additive_paired_squares_dichotomy` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-paired-squares-d).

## A nonzero value in the vanishing range of the dichotomy forces the identity

Let
$k \ge 5$ and let $f$ be a complex-valued multiplicative function such that

$$f\Big(\sum_{j=1}^{k} (x_j^2 + y_j^2)\Big) = \sum_{j=1}^{k} f(x_j^2 + y_j^2)$$

for all positive integers $x_1, \dots, x_k, y_1, \dots, y_k$. Suppose that $f(\beta) \ne 0$ for some
positive integer $\beta$ that is of the form $a^2 + b^2$ with integers $a, b \ge 1$, or of the
form $2k + t$ with $t \in \{0, 3, 6, 8, 9, 11, 12\}$, or satisfies $\beta \ge 2k + 14$. Then
$f(n) = n$ for every positive integer $n$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Corollary 2.

Stated but not proved: `MetaMathlibExt.multiplicative_additive_paired_squares_eq_id_of_ne_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-paired-squares-e-2).

## Multiplicative functions additive on six paired squares and nonzero at $2$ are the identity

**Multiplicative functions additive on six paired squares and nonzero at $2$ are the
identity.** Let $f$ be a complex-valued multiplicative function with $f(2) \ne 0$ such that

$$f\Big(\sum_{j=1}^{3} (x_j^2 + y_j^2)\Big) = \sum_{j=1}^{3} f(x_j^2 + y_j^2)$$

for all positive integers $x_1, x_2, x_3, y_1, y_2, y_3$. Then $f(n) = n$ for every positive
integer $n$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Theorem 3.

Stated but not proved: `MetaMathlibExt.multiplicative_additive_six_squares_eq_id` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-six-squares-eq-i).

## Multiplicative functions additive on eight paired squares and nonzero at $2$ are the identity

**Multiplicative functions additive on eight paired squares and nonzero at $2$ are the
identity.** Let $f$ be a complex-valued multiplicative function with $f(2) \ne 0$ such that

$$f\Big(\sum_{j=1}^{4} (x_j^2 + y_j^2)\Big) = \sum_{j=1}^{4} f(x_j^2 + y_j^2)$$

for all positive integers $x_1, \dots, x_4, y_1, \dots, y_4$. Then $f(n) = n$ for every positive
integer $n$.

## Sources

- Jewel Mahajan, *Multiplicative Functions Additive on Partitions of 2k Nonzero Squares*, INTEGERS 26 (2026), Article A121, Theorem 4.

Stated but not proved: `MetaMathlibExt.multiplicative_additive_eight_squares_eq_id` is written with `theorem_wanted` in [WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/MultiplicativeAdditivePairedSquaresWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html#multiplicative-additive-eight-squares-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Additive uniqueness of multiplicative functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/multiplicative-functions/additive-uniqueness-of-multiplicative-functions)
