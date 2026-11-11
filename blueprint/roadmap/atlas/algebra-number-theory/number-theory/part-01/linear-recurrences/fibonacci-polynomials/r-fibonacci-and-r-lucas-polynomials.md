---
declaration: section
origin: cited
lean: MetaMathlibExt.rFibonacciPolynomial, MetaMathlibExt.rFibonacciPolynomial_zero, MetaMathlibExt.rFibonacciPolynomial_succ_of_lt, MetaMathlibExt.rFibonacciPolynomial_succ_of_le, MetaMathlibExt.rFibonacciPolynomial_one_one_one, MetaMathlibExt.sum_pow_mul_rFibonacciPolynomial, MetaMathlibExt.sum_rFibonacciPolynomial, MetaMathlibExt.sum_neg_one_pow_mul_rFibonacciPolynomial
statement: formalized
---

# r-Fibonacci and r-Lucas polynomials

59 results, 31 proved and 28 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html).

## The $r$-Fibonacci polynomials

Let $R$ be a commutative semiring, let $r$ be a natural
number and let $x, y \in R$. The $r$-Fibonacci polynomials $U^{(r)}_n(x, y) \in R$, $n \ge 0$, are
defined by $U^{(r)}_0 = 0$, $U^{(r)}_k = x^{k-1}$ for $1 \le k \le r$, and
$U^{(r)}_{n+1} = x \, U^{(r)}_n + y \, U^{(r)}_{n-r}$ for $n \ge r$.

These are the initial values and recurrence displayed for $\xi_n = m^{n-1} U_n$ in the paper,
at $m = 1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 4.

Formalized by `MetaMathlibExt.rFibonacciPolynomial`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-fibonacci-polynomial).

## The zeroth $r$-Fibonacci polynomial vanishes

For every natural number $r$ and all
$x, y$ in a commutative semiring $R$, the $r$-Fibonacci polynomial $U^{(r)}_0(x, y)$ is $0$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 4.

Formalized by `MetaMathlibExt.rFibonacciPolynomial_zero`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-fibonacci-polynomial-zero).

## Initial values of the $r$-Fibonacci polynomials

Let $R$ be a commutative semiring, let
$x, y \in R$, and let $n < r$ be natural numbers. Then the $r$-Fibonacci polynomial
$U^{(r)}_{n+1}(x, y)$ equals $x^n$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 4.

Formalized by `MetaMathlibExt.rFibonacciPolynomial_succ_of_lt`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-fibonacci-polynomial-succ-of-lt).

## Recurrence for the $r$-Fibonacci polynomials

Let $R$ be a commutative semiring, let
$x, y \in R$, and let $r \le n$ be natural numbers. Then the $r$-Fibonacci polynomials
$U_m = U^{(r)}_m(x, y)$ satisfy $U_{n+1} = x \, U_n + y \, U_{n-r}$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 4.

Formalized by `MetaMathlibExt.rFibonacciPolynomial_succ_of_le`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-fibonacci-polynomial-succ-of-le).

## The $1$-Fibonacci polynomials at $x = y = 1$ are the Fibonacci numbers

For every
natural number $n$, the $r$-Fibonacci polynomial with $r = 1$, evaluated at $x = y = 1$ in the
natural numbers, is the $n$-th Fibonacci number: $U^{(1)}_n(1, 1) = F_n$, where $F_0 = 0$,
$F_1 = 1$ and $F_{n+2} = F_{n+1} + F_n$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 1.

Formalized by `MetaMathlibExt.rFibonacciPolynomial_one_one_one`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-fibonacci-polynomial-one-one-one).

## Geometrically weighted sum of $r$-Fibonacci polynomials

Let $K$ be a field, let $r \ge 1$
be a natural number, let $x, y, m \in K$ with $1 - m x - m^{r+1} y \ne 0$, and write $U_j$ for
the $r$-Fibonacci polynomial $U^{(r)}_j(x, y)$. Then for every natural number $n$,

$$
\sum_{j=1}^{n} m^{j-1} U_j =
\frac{1 - m^n U_{n+1} - m^{r+1} y \sum_{j=1}^{r} m^{n-r+j-1} U_{n-r+j}}{1 - m x - m^{r+1} y},
$$

where the terms of the inner sum with $n - r + j \le 0$ are zero.

The paper takes $m$ a positive integer; here $m$ is any element of $K$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 4.

Stated but not proved: `MetaMathlibExt.sum_pow_mul_rFibonacciPolynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#sum-pow-mul-r-fibonacci-polynomial).

## Sum of the first $n$ $r$-Fibonacci polynomials

Let $K$ be a field, let $r \ge 1$ be a
natural number, let $x, y \in K$ with $1 - x - y \ne 0$, and write $U_j$ for the $r$-Fibonacci
polynomial $U^{(r)}_j(x, y)$. Then for every natural number $n$,

$$
\sum_{j=1}^{n} U_j = \frac{1 - U_{n+1} - y \sum_{j=1}^{r} U_{n-r+j}}{1 - x - y},
$$

where the terms of the inner sum with $n - r + j \le 0$ are zero.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Corollary 2.

Stated but not proved: `MetaMathlibExt.sum_rFibonacciPolynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#sum-r-fibonacci-polynomial).

## Alternating sum of $r$-Fibonacci polynomials

Let $K$ be a field, let $r \ge 1$ be a
natural number, let $x, y \in K$ with $1 + x + (-1)^r y \ne 0$, and write $U_j$ for the
$r$-Fibonacci polynomial $U^{(r)}_j(x, y)$. Then for every natural number $n$,

$$
\sum_{j=1}^{n} (-1)^{j-1} U_j =
\frac{1 - (-1)^n U_{n+1} + (-1)^r y \sum_{j=1}^{r} (-1)^{n-r+j-1} U_{n-r+j}}{1 + x + (-1)^r y},
$$

where the terms of the inner sum with $n - r + j \le 0$ are zero.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Corollary 3.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_mul_rFibonacciPolynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#sum-neg-one-pow-mul-r-fibonacci-polynomi).

## The $r$-Lucas polynomials of type $s$

Let $R$ be a commutative semiring, let $r$ and $s$
be natural numbers and let $x, y \in R$. The $r$-Lucas polynomials of type $s$ are the sequence
$V_n = V^{(r,s)}_n(x, y)$, $n \ge 0$, of elements of $R$ given by $V_0 = s + 1$, $V_k = x^k$ for
$1 \le k \le r$, and $V_{n+1} = x V_n + y V_{n-r}$ for $n \ge r$.

The paper takes $1 \le s \le r$; the definition makes sense for every natural number $s$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 1.

Formalized by `MetaMathlibExt.rLucasPolynomial`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-lucas-polynomial).

## Initial value of the $r$-Lucas polynomials

For every commutative semiring $R$, all natural
numbers $r$ and $s$ and all $x, y \in R$, the $r$-Lucas polynomial of type $s$ satisfies
$V^{(r,s)}_0(x, y) = s + 1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 1.

Formalized by `MetaMathlibExt.rLucasPolynomial_zero`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-lucas-polynomial-zero).

## Initial values of the $r$-Lucas polynomials

Let $R$ be a commutative semiring, let $s$ be
a natural number, let $x, y \in R$, and let $n < r$ be natural numbers. Then the $r$-Lucas
polynomial of type $s$ satisfies $V^{(r,s)}_{n+1}(x, y) = x^{n+1}$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 1.

Formalized by `MetaMathlibExt.rLucasPolynomial_succ_of_lt`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 162](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L162). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-lucas-polynomial-succ-of-lt).

## Recurrence for the $r$-Lucas polynomials

Let $R$ be a commutative semiring, let $s$ be a
natural number, let $x, y \in R$, and let $r \le n$ be natural numbers. Then the $r$-Lucas
polynomials of type $s$, $V_m = V^{(r,s)}_m(x, y)$, satisfy $V_{n+1} = x \, V_n + y \, V_{n-r}$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 1.

Formalized by `MetaMathlibExt.rLucasPolynomial_succ_of_le`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-lucas-polynomial-succ-of-le).

## Binet formula for the $r$-Fibonacci polynomials (distinct zeros)

Let $K$ be a field, let
$r \ge 1$ be a natural number and let $x, y \in K$. Suppose that
$t^{r+1} - x t^r - y = \prod_{k=0}^{r} (t - \alpha_k)$ in $K[t]$, where
$\alpha_0, \dots, \alpha_r \in K$ are pairwise distinct. Then for every $n \ge 0$ the
$r$-Fibonacci polynomials $U^{(r)}_n(x, y)$ satisfy

$$U^{(r)}_{n+1}(x, y) = \sum_{k=0}^{r} \frac{\alpha_k^{n+1}}{(r+1) \alpha_k - r x}.$$

The paper's hypothesis $y \ne -\frac{1}{r} \left( \frac{rx}{r+1} \right)^{r+1}$ is replaced by the
distinctness of the zeros it is meant to guarantee (it does not exclude the multiple zero $0$
when $y = 0$, $r \ge 2$).

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 1.

Stated but not proved: `MetaMathlibExt.rFibonacciPolynomial_eq_sum_roots` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-fibonacci-polynomial-eq-sum-roots).

## Binet formula for the $r$-Lucas polynomials (distinct zeros)

Let $K$ be a field, let
$r \ge 1$ and $s$ be natural numbers, and let $x, y \in K$. Suppose that
$t^{r+1} - x t^r - y = \prod_{k=0}^{r} (t - \alpha_k)$ in $K[t]$, where
$\alpha_0, \dots, \alpha_r \in K$ are pairwise distinct. Then for every $n \ge 0$ the
$r$-Lucas polynomials of type $s$ satisfy

$$V^{(r,s)}_n(x, y) = \sum_{k=0}^{r} \frac{\alpha_k^n ((s+1)\alpha_k - s x)}{(r+1)\alpha_k - r x}.$$

The paper takes $1 \le s \le r$; the identity holds for every $s$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 1.

Stated but not proved: `MetaMathlibExt.rLucasPolynomial_eq_sum_roots` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-lucas-polynomial-eq-sum-roots).

## Binet formula for the r-Fibonacci polynomials with one double zero

Let $K$ be a field
of characteristic zero, let $r \ge 1$ be a natural number, and let $x, y, \alpha \in K$. Let
$\beta_1, \dots, \beta_{r-1} \in K$ be pairwise distinct and all different from $\alpha$, put
$\tilde P(t) = \prod_{k=1}^{r-1} (t - \beta_k)$, and suppose that
$t^{r+1} - x t^r - y = (t - \alpha)^2 \tilde P(t)$ as polynomials over $K$. Then for every
natural number $n$ the $r$-Fibonacci polynomial $U^{(r)}$ satisfies

$$
U^{(r)}_{n+1}(x, y) = \frac{\alpha^{n+r-1}}{\tilde P(\alpha)}
\Bigl((n + r) - \frac{\alpha \tilde P'(\alpha)}{\tilde P(\alpha)}\Bigr) +
\sum_{k=1}^{r-1} \frac{\beta_k^{n+1}}{(r+1)\beta_k - r x}.
$$

The paper's hypothesis $y = -\frac{1}{r}\bigl(\frac{rx}{r+1}\bigr)^{r+1}$ (which makes
$\alpha = rx/(r+1)$ the double zero) is replaced by the factorization it yields.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 1.

Stated but not proved: `MetaMathlibExt.rFibonacciPolynomial_eq_of_double_root` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-fibonacci-polynomial-eq-of-double-root).

## Binet formula for the $r$-Lucas polynomials (one double zero)

Let $K$ be a field of
characteristic zero, let $r \ge 1$ and $s$ be natural numbers, and let $x, y, \alpha \in K$ with
$\alpha \ne 0$. Suppose that $t^{r+1} - x t^r - y = (t - \alpha)^2 \tilde P(t)$ in $K[t]$, where
$\tilde P(t) = \prod_{k=1}^{r-1} (t - \beta_k)$ for pairwise distinct
$\beta_1, \dots, \beta_{r-1} \in K$, all different from $\alpha$. Then for every $n \ge 0$ the
$r$-Lucas polynomials of type $s$ satisfy

$$V^{(r,s)}_n(x, y) = \frac{\alpha^{n+r-1}}{\tilde P(\alpha)} \left( n \, \frac{r-s}{r} + r +
\frac{s}{r} - \alpha \, \frac{r-s}{r} \, \frac{\tilde P'(\alpha)}{\tilde P(\alpha)} \right) +
\sum_{k=1}^{r-1} \frac{\beta_k^n ((s+1) \beta_k - s x)}{(r+1) \beta_k - r x}.$$

The paper's hypothesis $y = -\frac{1}{r} \left( \frac{rx}{r+1} \right)^{r+1}$ (which makes
$\alpha = rx/(r+1)$ the double zero) is replaced by the factorization it yields. The paper takes
$1 \le s \le r$; the identity holds for every $s$. The hypothesis $\alpha \ne 0$ is added: for
$r = 2$, $y = 0$ the factorization $t^2 (t - x)$ has $\alpha = 0$ and the formula fails at $n = 0$
(for $x = s = 1$: $V_0 = 2$, right side $1$). In the paper's setting $\alpha = rx/(r+1)$ with
$x \ne 0$, so $\alpha \ne 0$; the only other $\alpha = 0$ case, $r = 1$, $x = y = 0$, is dropped.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 1.

Stated but not proved: `MetaMathlibExt.rLucasPolynomial_eq_of_double_root` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#r-lucas-polynomial-eq-of-double-root).

## $(p,q)$-binomial coefficient

Let $R$ be a commutative semiring and $p, q \in R$. For
natural numbers $n$ and $k$, the $(p,q)$-binomial coefficient $\binom{n}{k}_{p,q} \in R$ is
defined recursively by $\binom{n}{0}_{p,q} = 1$, $\binom{0}{k+1}_{p,q} = 0$ and
$\binom{n+1}{k+1}_{p,q} = p^{n-k} \binom{n}{k}_{p,q} + q^{k+1} \binom{n}{k+1}_{p,q}$, where $n - k$
is truncated subtraction ($0$ when $k > n$).

For $k \le n$, where the $(p,q)$-factorials are invertible, $\binom{n}{k}_{p,q}$ equals
$[n]_{p,q}! / ([k]_{p,q}! \, [n-k]_{p,q}!)$, where $[j]_{p,q} = p^{j-1} + p^{j-2} q + \dots +
q^{j-1}$; this is the definition used in the source. At $p = 1$ it is the Gaussian binomial
coefficient $\binom{n}{k}_q$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 3, Equation (3).

Formalized by `MetaMathlibExt.pqBinomial`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-binomial).

## $(p,q)$-binomial coefficients with lower index zero

For all elements $p, q$ of a
commutative semiring and every natural number $n$, the $(p,q)$-binomial coefficient
$\binom{n}{0}_{p,q}$ equals $1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 3.

Formalized by `MetaMathlibExt.pqBinomial_zero_right`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 277](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L277). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-binomial-zero-right).

## $(p,q)$-binomial coefficients with upper index zero and positive lower index

For all
elements $p, q$ of a commutative semiring and every natural number $k$, the $(p,q)$-binomial
coefficient $\binom{0}{k+1}_{p,q}$ equals $0$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 3.

Formalized by `MetaMathlibExt.pqBinomial_zero_succ`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-binomial-zero-succ).

## Pascal recursion for $(p,q)$-binomial coefficients

For all elements $p, q$ of a
commutative semiring and all natural numbers $n$ and $k$, the $(p,q)$-binomial coefficients satisfy
$\binom{n+1}{k+1}_{p,q} = p^{n-k} \binom{n}{k}_{p,q} + q^{k+1} \binom{n}{k+1}_{p,q}$, where $n - k$
is truncated subtraction ($0$ when $k > n$).

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 3, Equation (3).

Formalized by `MetaMathlibExt.pqBinomial_succ_succ`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 294](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L294). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-binomial-succ-succ).

## The $(p, q)$-binomial coefficients at $p = 1$

Let $R$ be a commutative semiring and
$q \in R$. For all natural numbers $n$ and $k$, the $(p, q)$-binomial coefficient
$[n, k]_{p,q}$ at $p = 1$ equals the Gaussian binomial coefficient $\binom{n}{k}_q$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Section 3 (Remark 1: `p = 1` gives the `q`-analogue).

Formalized by `MetaMathlibExt.pqBinomial_one_left`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-binomial-one-left).

## $(p,q)$-analogue of the $r$-Fibonacci polynomial

Let $R$ be a commutative semiring, let
$r$ and $m$ be natural numbers and let $x, y, p, q \in R$. The $(p,q)$-analogue
$U^{(r)}_n(x, y, p, q, m) \in R$ of the $r$-Fibonacci polynomial is defined by
$U^{(r)}_0(x, y, p, q, m) = 0$ and, for every natural number $n$,

$$
U^{(r)}_{n+1}(x, y, p, q, m) = \sum_{k=0}^{\lfloor n/(r+1) \rfloor} p^{\binom{n+1-(r+1)k}{2}}
q^{\binom{k+1}{2} + m \binom{k}{2}} \binom{n-rk}{k}_{p,q} x^{n-(r+1)k} y^k,
$$

where $\binom{a}{b}_{p,q}$ is the $(p,q)$-binomial coefficient.

The source also states $U^{(r)}_j = p^{\binom{j+1}{2}} x^{j-1}$ for $1 \le j \le r$, which
contradicts this sum: the sum gives $p^{\binom{j}{2}} x^{j-1}$ (for example $U^{(2)}_2 = p x$,
not $p^3 x$). The sum, which Theorem 2 of the source requires, is used.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 1.

Formalized by `MetaMathlibExt.pqRFibonacci`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rfibonacci).

## Zeroth value of the $(p,q)$-analogue of the $r$-Fibonacci polynomial

For all natural
numbers $r$ and $m$ and all elements $x, y, p, q$ of a commutative semiring, the
$(p,q)$-analogue of the $r$-Fibonacci polynomial satisfies $U^{(r)}_0(x, y, p, q, m) = 0$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 1.

Formalized by `MetaMathlibExt.pqRFibonacci_zero`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rfibonacci-zero).

## First value of the $(p,q)$-analogue of the $r$-Fibonacci polynomial

For all natural
numbers $r$ and $m$ and all elements $x, y, p, q$ of a commutative semiring, the
$(p,q)$-analogue of the $r$-Fibonacci polynomial satisfies $U^{(r)}_1(x, y, p, q, m) = 1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 1.

Formalized by `MetaMathlibExt.pqRFibonacci_one`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 342](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L342). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rfibonacci-one).

## First recurrence for the $(p,q)$-analogue of the $r$-Fibonacci polynomial

Let $R$ be a
commutative semiring, let $r \ge 1$, $n \ge r$ and $m$ be natural numbers and let
$x, y, p, q \in R$. Write $U_j(x, y)$ for $U^{(r)}_j(x, y, p, q, m)$, the $(p,q)$-analogue of the
$r$-Fibonacci polynomial with $r$, $p$, $q$ and $m$ fixed. Then

$$U_{n+1}(x, y) = p x \, U_n(p x, q y) + q y \, U_{n-r}(p x, q^{m+1} y).$$

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 2, Equation (4).

Stated but not proved: `MetaMathlibExt.pqRFibonacci_succ_eq_left` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rfibonacci-succ-eq-left).

## Second recurrence for the $(p,q)$-analogue of the $r$-Fibonacci polynomial

Let $R$ be a
commutative semiring, let $r \ge 1$, $n \ge r$ and $m$ be natural numbers and let
$x, y, p, q \in R$. Write $U_j(x, y)$ for $U^{(r)}_j(x, y, p, q, m)$, the $(p,q)$-analogue of the
$r$-Fibonacci polynomial with $r$, $p$, $q$ and $m$ fixed. Then

$$U_{n+1}(x, y) = p x \, U_n(p x, p y) + q y \, U_{n-r}(q x, q^{m+1} y).$$

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 2, Equation (5).

Stated but not proved: `MetaMathlibExt.pqRFibonacci_succ_eq_right` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rfibonacci-succ-eq-right).

## First-kind (p, q)-Lucas polynomials

Let $R$ be a commutative semiring, let $r$, $s$ and
$m$ be natural numbers, let $x, y, p, q \in R$, and write $[a, b]_{p,q}$ for the
$(p, q)$-binomial coefficients. The first-kind $(p, q)$-analogue $V^{(r,s)}_n(x, y, p, q, m)$ of
the $r$-Lucas polynomial of type $s$, written $V_n$, is defined by $V_0 = s + 1$ and, for
$n \ge 1$,

$$
V_n = \sum_{k=0}^{\lfloor n/(r+1) \rfloor} p^{\binom{n-(r+1)k}{2}} q^{(m+1)\binom{k}{2}}\,
c_{n,k}\,x^{n-(r+1)k} y^k,
$$

where $c_{n,0} = [n, 0]_{p,q}$ and, for $k \ge 1$,
$c_{n,k} = [n - rk, k]_{p,q} + s\,p^{n-(r+1)k} [n - rk - 1, k - 1]_{p,q}$.

The paper writes $c_{n,k}$ as
$[n - rk, k]_{p,q} (1 + s\,p^{n-(r+1)k} [k]_{p,q} / [n - rk]_{p,q})$, with $[a]_{p,q}$ the
$(p, q)$-numbers; the division-free form is the first step of the paper's proof of Theorem 3
and agrees with it whenever $[n - rk]_{p,q} \ne 0$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 2.

Formalized by `MetaMathlibExt.pqRLucas`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 383](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L383). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas).

## Initial value of the first-kind (p, q)-Lucas polynomials

Let $R$ be a commutative
semiring, let $r$, $s$ and $m$ be natural numbers, and let $x, y, p, q \in R$. The first-kind
$(p, q)$-analogue $V^{(r,s)}_n(x, y, p, q, m)$ of the $r$-Lucas polynomial of type $s$ satisfies
$V^{(r,s)}_0(x, y, p, q, m) = s + 1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 2.

Formalized by `MetaMathlibExt.pqRLucas_zero`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-zero).

## Second-kind (p, q)-Lucas polynomials

Let $K$ be a field, let $r$, $s$ and $m$ be natural
numbers, let $x, y, p, q \in K$, and write $[a, b]_{p,q}$ for the $(p, q)$-binomial
coefficients. The second-kind $(p, q)$-analogue $\mathbb{V}^{(r,s)}_n(x, y, p, q, m)$ of the
$r$-Lucas polynomial of type $s$, written $\mathbb{V}_n$, is defined by $\mathbb{V}_0 = s + 1$
and, for $n \ge 1$,

$$
\mathbb{V}_n = \sum_{k=0}^{\lfloor n/(r+1) \rfloor}
\frac{p^{\binom{n-(r+1)k}{2}} q^{\binom{k+1}{2} + m\binom{k}{2}}}{p^k}\,
d_{n,k}\,x^{n-(r+1)k} y^k,
$$

where $d_{n,0} = [n, 0]_{p,q}$ and, for $k \ge 1$,
$d_{n,k} = [n - rk, k]_{p,q} + s\,q^{n-(r+1)k} [n - rk - 1, k - 1]_{p,q}$. Division by $0$ is
read as $0$, so for $p = 0$ every term with $k \ge 1$ vanishes.

The paper writes $d_{n,k}$ as
$[n - rk, k]_{p,q} (1 + s\,q^{n-(r+1)k} [k]_{p,q} / [n - rk]_{p,q})$, with $[a]_{p,q}$ the
$(p, q)$-numbers; the two agree whenever $[n - rk]_{p,q} \ne 0$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 2.

Formalized by `MetaMathlibExt.pqRLucasSecond`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 408](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L408). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-second).

## Initial value of the second-kind (p, q)-Lucas polynomials

Let $K$ be a field, let $r$,
$s$ and $m$ be natural numbers, and let $x, y, p, q \in K$. The second-kind $(p, q)$-analogue
$\mathbb{V}^{(r,s)}_n(x, y, p, q, m)$ of the $r$-Lucas polynomial of type $s$ satisfies
$\mathbb{V}^{(r,s)}_0(x, y, p, q, m) = s + 1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 2.

Formalized by `MetaMathlibExt.pqRLucasSecond_zero`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 421](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L421). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-second-zero).

## Splitting formula for first-kind (p, q)-Lucas polynomials

Let $K$ be a field, let
$r \ge 1$, $s$ and $m$ be natural numbers, and let $x, y, p, q \in K$ with $p \ne 0$ and
$q \ne 0$. Write $U_n(x, y)$ for the $(p, q)$-analogue of the $r$-Fibonacci polynomial with
parameters $p, q, m$, and $V_n(x, y)$ for the first-kind $(p, q)$-analogue of the $r$-Lucas
polynomial of type $s$ with the same parameters. Then for every natural number $n \ge r$,

$$
V_n(x, y) = U_{n+1}(x/p, y/q) + s\,y\,U_{n-r}(x, y q^m).
$$

The paper takes positive $s$; the identity holds for every natural number $s$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 3, part 1.

Stated but not proved: `MetaMathlibExt.pqRLucas_eq_pqRFibonacci_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 431](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L431). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-eq-pq-rfibonacci-add).

## Splitting formula for second-kind (p, q)-Lucas polynomials

Let $K$ be a field, let
$r \ge 1$, $s$ and $m$ be natural numbers, and let $x, y, p, q \in K$ with $p \ne 0$ and
$q \ne 0$. Write $U_n(x, y)$ for the $(p, q)$-analogue of the $r$-Fibonacci polynomial with
parameters $p, q, m$, and $\mathbb{V}_n(x, y)$ for the second-kind $(p, q)$-analogue of the
$r$-Lucas polynomial of type $s$ with the same parameters. Then for every natural number
$n \ge r$,

$$
\mathbb{V}_n(x, y) = U_{n+1}(x/p, y/p) + s\,y\,(q/p)^{n-r}\,U_{n-r}(x, y p^r q^m / q^r).
$$

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 3, part 1.

Stated but not proved: `MetaMathlibExt.pqRLucasSecond_eq_pqRFibonacci_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 443](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L443). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-second-eq-pq-rfibonacci-add).

## First-kind (p, q)-Lucas polynomials as a difference of (p, q)-Fibonacci polynomials

Let
$K$ be a field, let $r \ge 1$, $s$ and $m$ be natural numbers, and let $x, y, p, q \in K$ with
$p \ne 0$ and $q \ne 0$. Write $U_n(x, y)$ for the $(p, q)$-analogue of the $r$-Fibonacci
polynomial with parameters $p, q, m$, and $V_n(x, y)$ for the first-kind $(p, q)$-analogue of
the $r$-Lucas polynomial of type $s$ with the same parameters. Then for every natural number $n$,

$$
V_n(x, y) = (s + 1)\,U_{n+1}(x/p, y/q) - s\,x\,U_n(x, y).
$$

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 3, part 2.

Stated but not proved: `MetaMathlibExt.pqRLucas_eq_succ_mul_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-eq-succ-mul-sub).

## Second-kind (p, q)-Lucas polynomials as a difference of (p, q)-Fibonacci polynomials

Let
$K$ be a field, let $r \ge 1$, $s$ and $m$ be natural numbers, and let $x, y, p, q \in K$ with
$p \ne 0$. Write $U_n(x, y)$ for the $(p, q)$-analogue of the $r$-Fibonacci polynomial with
parameters $p, q, m$, and $\mathbb{V}_n(x, y)$ for the second-kind $(p, q)$-analogue of the
$r$-Lucas polynomial of type $s$ with the same parameters. Then for every natural number $n$,

$$
\mathbb{V}_n(x, y) = (s + 1)\,U_{n+1}(x/p, y/p) - s\,x\,U_n(x, y).
$$

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 3, part 2.

Stated but not proved: `MetaMathlibExt.pqRLucasSecond_eq_succ_mul_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-second-eq-succ-mul-sub).

## First-kind $(p,q)$-analogue of the $r$-Lucas polynomial via two $r$-Fibonacci terms

Let
$R$ be a commutative semiring, let $r \ge 1$, $n \ge r$, $s$ and $m$ be natural numbers and let
$x, y, p, q \in R$. Write $U_j(x, y)$ for the $(p,q)$-analogue $U^{(r)}_j(x, y, p, q, m)$ of the
$r$-Fibonacci polynomial and $V_n(x, y)$ for the first-kind $(p,q)$-analogue
$V^{(r,s)}_n(x, y, p, q, m)$ of the $r$-Lucas polynomial of type $s$, with $r$, $s$, $p$, $q$
and $m$ fixed. Then

$$V_n(x, y) = x \, U_n(x, y) + (1 + s) \, y \, U_{n-r}(x, y q^m).$$

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 3, part 3.

Stated but not proved: `MetaMathlibExt.pqRLucas_eq_mul_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 479](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L479). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-eq-mul-add).

## Recurrence-type formula for second-kind (p, q)-Lucas polynomials

Let $K$ be a field, let
$r \ge 1$, $s$ and $m$ be natural numbers, and let $x, y, p, q \in K$ with $p \ne 0$ and
$q \ne 0$. Write $U_n(x, y)$ for the $(p, q)$-analogue of the $r$-Fibonacci polynomial with
parameters $p, q, m$, and $\mathbb{V}_n(x, y)$ for the second-kind $(p, q)$-analogue of the
$r$-Lucas polynomial of type $s$ with the same parameters. Then for every natural number
$n \ge r$,

$$
\mathbb{V}_n(x, y) = x\,U_n(x, y) + (1 + s)\,(q/p)^{n-r}\,y\,U_{n-r}(x, y p^r q^m / q^r).
$$

The paper writes the second argument as $y p^r q^{m-r}$ and drops $p, q$ from the argument list
$(x, y p^r q^{m-r}, m)$; they are unchanged.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 3, part 3.

Stated but not proved: `MetaMathlibExt.pqRLucasSecond_eq_mul_add` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#pq-rlucas-second-eq-mul-add).

## Geometrically weighted sum of $r$-Lucas polynomials

Let $K$ be a field, let $r \ge 1$ and
$s$ be natural numbers, let $x, y, m \in K$ with $1 - m x - m^{r+1} y \ne 0$, and write $V_j$ for
the $r$-Lucas polynomial of type $s$, $V_j = V^{(r,s)}_j(x, y)$. Then for every natural number
$n \ge r - 1$,

$$
\sum_{j=1}^{n} m^j V_j =
\frac{1 + s m^{r+1} y - m^{n+1} V_{n+1} - m^{r+1} y \sum_{j=1}^{r} m^{n-r+j} V_{n-r+j}}
{1 - m x - m^{r+1} y} - 1.
$$

The paper takes $m$ a positive integer (here any element of $K$) and states no range for $n$; for
$n < r - 1$ the right side involves $V$ at negative indices.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 5.

Stated but not proved: `MetaMathlibExt.sum_pow_mul_rLucasPolynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 508](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L508). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#sum-pow-mul-r-lucas-polynomial).

## Sum of the first $n$ $r$-Lucas polynomials

Let $K$ be a field, let $r \ge 1$ and $s$ be
natural numbers, let $x, y \in K$ with $1 - x - y \ne 0$, and write $V_j$ for the $r$-Lucas
polynomial of type $s$, $V_j = V^{(r,s)}_j(x, y)$. Then for every natural number $n$ with
$n \ge 1$ and $n \ge r - 1$,

$$
\sum_{j=1}^{n} V_j = \frac{1 + s y - V_{n+1} - y \sum_{j=1}^{r} V_{n-r+j}}{1 - x - y} - 1.
$$

The paper states $n \ge 1$; for $n < r - 1$ the right side involves $V$ at negative indices.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Corollary 4.

Stated but not proved: `MetaMathlibExt.sum_rLucasPolynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 524](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L524). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#sum-r-lucas-polynomial).

## Alternating sum of $r$-Lucas polynomials

Let $K$ be a field, let $r \ge 1$ and $s$ be
natural numbers, let $x, y \in K$ with $1 + x + (-1)^r y \ne 0$, and write $V_j$ for the
$r$-Lucas polynomial of type $s$, $V_j = V^{(r,s)}_j(x, y)$. Then for every natural number
$n \ge r - 1$,

$$
\sum_{j=1}^{n} (-1)^j V_j =
\frac{1 - (-1)^r s y + (-1)^n V_{n+1} + (-1)^r y \sum_{j=1}^{r} (-1)^{n-r+j} V_{n-r+j}}
{1 + x + (-1)^r y} - 1.
$$

For $n < r - 1$ the right side involves $V$ at negative indices.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Corollary 5.

Stated but not proved: `MetaMathlibExt.sum_neg_one_pow_mul_rLucasPolynomial` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#sum-neg-one-pow-mul-r-lucas-polynomial).

## The (-r)-Fibonacci polynomials

Let $A$ be a commutative ring, $r$ a natural number,
$x \in A$ and $y$ a unit of $A$. The values $U_n = U^{(-r)}_n(x, y) \in A$ of the
$(-r)$-Fibonacci polynomials are defined for $n \ge 0$ by $U_0 = 0$, $U_1 = 1$, $U_n = 0$ for
$2 \le n \le r$, and, when $r \ge 1$, $U_{n+1} = y^{-1} U_{n-r+1} - y^{-1} x U_{n-r}$ for
$n \ge r$. When $r = 0$, $U_n = 0$ for every $n \ge 2$.

The paper takes $r \ge 2$; the case $r = 0$ only makes the definition total.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 3.

Formalized by `MetaMathlibExt.negRFibonacci`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci).

## The zeroth (-r)-Fibonacci polynomial

For every commutative ring $A$, natural number
$r$, $x \in A$ and unit $y$ of $A$, the $(-r)$-Fibonacci polynomial satisfies
$U^{(-r)}_0(x, y) = 0$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 3.

Formalized by `MetaMathlibExt.negRFibonacci_zero`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 569](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L569). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-zero).

## The first (-r)-Fibonacci polynomial

For every commutative ring $A$, natural number
$r$, $x \in A$ and unit $y$ of $A$, the $(-r)$-Fibonacci polynomial satisfies
$U^{(-r)}_1(x, y) = 1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 3.

Formalized by `MetaMathlibExt.negRFibonacci_one`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-one).

## The (-r)-Fibonacci polynomials vanish at indices 2 to r

Let $A$ be a commutative ring,
$x \in A$ and $y$ a unit of $A$. For natural numbers $r$ and $n$ with $1 \le n < r$, the
$(-r)$-Fibonacci polynomial satisfies $U^{(-r)}_{n+1}(x, y) = 0$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 3.

Formalized by `MetaMathlibExt.negRFibonacci_succ_of_lt`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 588](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L588). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-succ-of-lt).

## Recurrence for the (-r)-Fibonacci polynomials

Let $A$ be a commutative ring, $x \in A$
and $y$ a unit of $A$, let $r$ and $n$ be natural numbers with $1 \le r \le n$, and write
$U_m = U^{(-r)}_m(x, y)$. Then $U_{n+1} = y^{-1} U_{n-r+1} - y^{-1} x U_{n-r}$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 3, Equation (7).

Formalized by `MetaMathlibExt.negRFibonacci_succ_of_le`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 598](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L598). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-succ-of-le).

## Companion sequence of the $(-r)$-Fibonacci polynomials

Let $A$ be a commutative ring,
$r$ a natural number, $x \in A$ and $y$ a unit of $A$. The companion sequence
$V^{(-r)}_n(x, y) \in A$, $n \ge 0$, is defined by $V^{(-r)}_0 = r + 1$ and, if $r \ge 1$, by
$V^{(-r)}_n = 0$ for $1 \le n < r$, $V^{(-r)}_r = r y^{-1}$ and
$V^{(-r)}_{n+1} = y^{-1} V^{(-r)}_{n-r+1} - y^{-1} x V^{(-r)}_{n-r}$ for $n \ge r$. If $r = 0$,
then $V^{(-r)}_n = 0$ for all $n \ge 1$.

The paper takes $r \ge 2$; the case $r = 0$ only makes the definition total.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 4.

Formalized by `MetaMathlibExt.negRLucas`, a definition declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 613](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L613). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas).

## Zeroth term of the companion sequence $V^{(-r)}$

Let $A$ be a commutative ring, $r$ a
natural number, $x \in A$ and $y$ a unit of $A$. The companion sequence of the
$(-r)$-Fibonacci polynomials satisfies $V^{(-r)}_0(x, y) = r + 1$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 4.

Formalized by `MetaMathlibExt.negRLucas_zero`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 627](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L627). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-zero).

## Vanishing initial terms of the companion sequence $V^{(-r)}$

Let $A$ be a commutative
ring, $x \in A$ and $y$ a unit of $A$. For natural numbers $r$ and $n$ with $n + 1 < r$, the
companion sequence of the $(-r)$-Fibonacci polynomials satisfies $V^{(-r)}_{n+1}(x, y) = 0$;
that is, $V^{(-r)}_m(x, y) = 0$ for $1 \le m < r$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 4.

Formalized by `MetaMathlibExt.negRLucas_succ_of_lt`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 636](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L636). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-succ-of-lt).

## The $r$-th term of the companion sequence $V^{(-r)}$

Let $A$ be a commutative ring,
$r \ge 1$ a natural number, $x \in A$ and $y$ a unit of $A$. The companion sequence of the
$(-r)$-Fibonacci polynomials satisfies $V^{(-r)}_r(x, y) = r y^{-1}$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 4.

Formalized by `MetaMathlibExt.negRLucas_self`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 646](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L646). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-self).

## Recurrence for the companion sequence $V^{(-r)}$

Let $A$ be a commutative ring, $x \in A$
and $y$ a unit of $A$. For natural numbers $r$ and $n$ with $1 \le r \le n$, the companion
sequence of the $(-r)$-Fibonacci polynomials satisfies
$V^{(-r)}_{n+1}(x, y) = y^{-1} V^{(-r)}_{n-r+1}(x, y) - y^{-1} x V^{(-r)}_{n-r}(x, y)$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Definition 4.

Formalized by `MetaMathlibExt.negRLucas_succ_of_le`, a theorem declared in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 657](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L657). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-succ-of-le).

## Explicit sum for the (-r)-Fibonacci polynomials

Let $A$ be a commutative ring,
$r \ge 2$, $x \in A$ and $y$ a unit of $A$, and write $U_n = U^{(-r)}_n(x, y)$. For every
$n \ge 0$,

$$U_{n+1} = \sum_{k=0}^{\lfloor n/r \rfloor} \binom{k}{n - rk} y^{-k} (-x)^{n-rk},$$

where $\binom{a}{b} = 0$ for $b > a$, so the terms with $(r+1) k < n$ vanish.

The paper states $n \ge 1$ and $x$ a unit; the identity holds for $n = 0$ and every $x$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 6.

Stated but not proved: `MetaMathlibExt.negRFibonacci_succ_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 672](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L672). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-succ-eq-sum).

## Explicit sum for the (-r)-Fibonacci polynomials, second form

Let $A$ be a commutative
ring, $r \ge 2$, $x \in A$ and $y$ a unit of $A$, and write $U_n = U^{(-r)}_n(x, y)$. For every
$n \ge 0$, $U_{n+1}$ is the sum of $\binom{(n-k)/r}{k} y^{-(n-k)/r} (-x)^k$ over the integers
$k$ with $0 \le k \le \lfloor n/r \rfloor$ and $r \mid n - k$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 6.

Stated but not proved: `MetaMathlibExt.negRFibonacci_succ_eq_sum'` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 685](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L685). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-succ-eq-sum-2).

## The companion sequence in terms of the $(-r)$-Fibonacci polynomials

Let $A$ be a
commutative ring, $r \ge 2$ a natural number, $x \in A$ and $y$ a unit of $A$, and let
$U^{(-r)}_n(x, y)$ be the $(-r)$-Fibonacci polynomials and $V^{(-r)}_n(x, y)$ their companion
sequence. For every natural number $n \ge r$,
$V^{(-r)}_n(x, y) = r \, U^{(-r)}_{n+1}(x, y) - x y^{-1} U^{(-r)}_{n-r}(x, y)$.

The paper takes $x$ a unit; the identity holds for every $x$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Proposition 1, Equation (8).

Stated but not proved: `MetaMathlibExt.negRLucas_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 698](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L698). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-eq).

## Explicit sum for the companion sequence $V^{(-r)}$

Let $K$ be a field of
characteristic zero, $r \ge 2$ and $n \ge 1$ natural numbers, $x \in K$ and $y$ a unit of
$K$, and let $V^{(-r)}_n(x, y)$ be the companion sequence of the $(-r)$-Fibonacci
polynomials. Then

$$V^{(-r)}_n(x, y) = \sum_{k} \frac{n}{n - rk} \binom{k - 1}{n - 1 - rk} y^{-k} \,
(-x)^{n - rk} + \varepsilon,$$

where the sum runs over the natural numbers $k \ge 1$ with $rk < n$, $\binom{a}{b}$ is the
binomial coefficient of natural numbers (zero when $b > a$), and $\varepsilon = r y^{-n/r}$ if
$r$ divides $n$ and $\varepsilon = 0$ otherwise.

The paper's range $\lfloor n/(r+1) \rfloor \le k \le \lfloor n/r \rfloor$ also admits $k = n/r$
(division by zero; that term is the $\varepsilon$ term) and, for $n \le r$, $k = 0$, whose term
$\binom{-1}{n-1}$ must be read as $0$ (with $\binom{-1}{j} = (-1)^j$, $r = 2$, $n = 1$ gives
$-x$ instead of $V^{(-r)}_1 = 0$); both are excluded.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 7.

Stated but not proved: `MetaMathlibExt.negRLucas_eq_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 713](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L713). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-eq-sum).

## Explicit sum for the (-r)-Lucas polynomials, second form

Let $K$ be a field of
characteristic zero, $r \ge 2$, $x \in K$ and $y \in K$ nonzero, and write
$V_n = V^{(-r)}_n(x, y)$ for the companion $(-r)$-Lucas sequence. For every $n \ge 1$, $V_n$ is
the sum of

$$\frac{n}{k+1} \binom{(n-1-r-k)/r}{k} y^{-(n-1-k)/r} (-x)^{k+1}$$

over the integers $k$ with $0 \le k \le \lfloor n/(r+1) \rfloor - 1$ and $r \mid n - k - 1$,
plus $r y^{-n/r}$ when $r \mid n$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 7.

Stated but not proved: `MetaMathlibExt.negRLucas_eq_sum'` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 728](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L728). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-eq-sum-2).

## Generating function of the (-r)-Fibonacci polynomials

Let $A$ be a commutative ring,
$r \ge 2$, $x \in A$ and $y$ a unit of $A$, and write $U_n = U^{(-r)}_n(x, y)$. In the ring
$A[[z]]$ of formal power series,

$$\left(1 - y^{-1} z^r + x y^{-1} z^{r+1}\right) \sum_{n \ge 0} U_{n+1} z^n = 1.$$

The paper states the identity for complex $z$; convergence is not part of this statement.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 8.

Stated but not proved: `MetaMathlibExt.negRFibonacci_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 743](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L743). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-generating-function).

## Generating function of the companion sequence $V^{(-r)}$

Let $A$ be a commutative
ring, $r \ge 2$ a natural number, $x \in A$ and $y$ a unit of $A$, and let $V^{(-r)}_n(x, y)$
be the companion sequence of the $(-r)$-Fibonacci polynomials. In the ring $A[[z]]$ of formal
power series,

$$(1 - y^{-1} z^r + x y^{-1} z^{r+1}) \sum_{n \ge 0} V^{(-r)}_n(x, y) z^n = r + 1 - y^{-1} z^r.$$

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 8.

Stated but not proved: `MetaMathlibExt.negRLucas_generatingFunction` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 755](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L755). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-generating-function).

## Separability of $t^{r+1} - y^{-1} t + x y^{-1}$

Let $K$ be a field of characteristic zero,
let $r \ge 1$, let $x \in K$ and let $y \in K$ be nonzero with $(r+1)^{r+1} x^r y \ne r^r$. Then
the polynomial $t^{r+1} - y^{-1} t + x y^{-1} \in K[t]$ is separable, that is, coprime to its
derivative; equivalently, it has no multiple zeros in an algebraic closure of $K$.

This corrects Lemma 1 of the paper. The printed hypothesis $x \ne \frac{r}{r+1} ((r+1) y)^{-1/r}$
names only one $r$-th root and is insufficient: $r = 2$, $y = 1/3$, $x = -2/3$ satisfies it, since
$\frac{2}{3} \cdot 1^{-1/2} = \frac{2}{3}$, yet $t^3 - 3t - 2 = (t + 1)^2 (t - 2)$. The paper's
proof shows that a multiple zero $\beta$ forces $x = r\beta/(r+1)$ with $\beta^r = 1/((r+1) y)$,
that is, $(r+1)^{r+1} x^r y = r^r$, which is the branch-free condition used here.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Lemma 1.

Stated but not proved: `MetaMathlibExt.separable_negRFibonacci_charPoly` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 773](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L773). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#separable-neg-rfibonacci-char-poly).

## Binet formula for the (-r)-Fibonacci polynomials

Let $K$ be a field, $r \ge 2$,
$x \in K$ and $y \in K$ nonzero, and write $U_n = U^{(-r)}_n(x, y)$. Suppose that
$\beta_0, \dots, \beta_r \in K$ are pairwise distinct and that
$t^{r+1} - y^{-1} t + x y^{-1} = \prod_{k=0}^{r} (t - \beta_k)$ as polynomials over $K$. Then for
every $n \ge 0$,

$$U_{n+1} = \sum_{k=0}^{r} \frac{\beta_k^{n+r+1}}{r \beta_k^{r+1} - x y^{-1}},$$

where a term whose denominator vanishes is read as $0$.

The paper's hypothesis $x \ne \frac{r}{r+1} ((r+1) y)^{-1/r}$ is replaced by the distinctness of
the zeros (compare Lemma 1).

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 9.

Stated but not proved: `MetaMathlibExt.negRFibonacci_eq_sum_roots` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rfibonacci-eq-sum-roots).

## Binet formula for the companion sequence $V^{(-r)}$

Let $K$ be a field, $r \ge 2$ a
natural number, $x \in K$ and $y$ a unit of $K$, and let $V^{(-r)}_n(x, y)$ be the companion
sequence of the $(-r)$-Fibonacci polynomials. Suppose $\beta_0, \dots, \beta_r \in K$ are
pairwise distinct and $t^{r+1} - y^{-1} t + x y^{-1} = \prod_{k=0}^{r} (t - \beta_k)$ in the
polynomial ring $K[t]$. Then $V^{(-r)}_n(x, y) = \sum_{k=0}^{r} \beta_k^n$ for every natural
number $n$.

## Sources

- Abbad and Belbachir, *The r-Fibonacci Polynomial and Its Companion Sequences Linked with Some Classical Sequences*, INTEGERS 25 (2025), Article A38, Theorem 9.

Stated but not proved: `MetaMathlibExt.negRLucas_eq_sum_roots` is written with `theorem_wanted` in [WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean, line 801](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RFibonacciPolynomialWanted.lean#L801). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html#neg-rlucas-eq-sum-roots).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: r-Fibonacci and r-Lucas polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/r-fibonacci-and-r-lucas-polynomials)
