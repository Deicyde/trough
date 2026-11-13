---
declaration: section
origin: cited
lean: MetaMathlibExt.AbGeneralizedFibonacciSequence, MetaMathlibExt.AbGeneralizedFibonacciSequence.ext, MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB, MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB_zero, MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB_one, MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB_add_two, MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.lucasAB, MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.lucasAB_zero
statement: formalized
---

# (a, b)-Fibonacci and (a, b)-Lucas numbers

22 results, 10 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html).

## Kalman–Mena generalized Fibonacci sequence

A Kalman–Mena $(a,b)$-generalized
Fibonacci sequence consists of real parameters $a$ and $b$ together with a real sequence
$(F_n)_{n \ge 0}$ such that $F_0 = 0$, $F_1 = 1$, $F_{n+2} = a F_{n+1} + b F_n$ for every
$n \ge 0$, and its ordinary generating series in the formal variable $x$ satisfies the
identity of formal power series $(1 - a x - b x^2) \sum_{n \ge 0} F_n x^n = x$, that is,
$\sum_{n \ge 0} F_n x^n = x / (1 - a x - b x^2)$.

Formalized by `MetaMathlibExt.AbGeneralizedFibonacciSequence`, a structure declared in [MathlibExt/NumberTheory/AbGeneralizedFibonacciSequence.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/AbGeneralizedFibonacciSequence.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#ab-generalized-fibonacci-sequence).

## Extensionality for Kalman–Mena generalized Fibonacci sequences

Two Kalman–Mena
$(a,b)$-generalized Fibonacci sequences are equal when they have the same parameter $a$, the same
parameter $b$ and the same sequence $(F_n)_{n \ge 0}$.

Formalized by `MetaMathlibExt.AbGeneralizedFibonacciSequence.ext`, a theorem declared in [MathlibExt/NumberTheory/AbGeneralizedFibonacciSequence.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/AbGeneralizedFibonacciSequence.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#ext).

## The (a, b)-Fibonacci numbers

For complex numbers $a$ and $b$, the $(a,b)$-Fibonacci
numbers $F^{a,b}_n$, $n \in \mathbb{N}$, are the complex numbers given by $F^{a,b}_0 = 0$,
$F^{a,b}_1 = 1$ and $F^{a,b}_{n+2} = a F^{a,b}_{n+1} + b F^{a,b}_n$ for every $n$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB`, a definition declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#fib-ab).

## Zeroth (a, b)-Fibonacci number

For all complex numbers $a$ and $b$, the $(a,b)$-Fibonacci
number $F^{a,b}_0$ equals $0$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB_zero`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#fib-ab-zero).

## First (a, b)-Fibonacci number

For all complex numbers $a$ and $b$, the $(a,b)$-Fibonacci
number $F^{a,b}_1$ equals $1$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#fib-ab-one).

## Recurrence for the (a, b)-Fibonacci numbers

For all complex numbers $a$ and $b$ and every
natural number $n$, the $(a,b)$-Fibonacci numbers satisfy
$F^{a,b}_{n+2} = a F^{a,b}_{n+1} + b F^{a,b}_n$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.fibAB_add_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#fib-ab-add-two).

## (a, b)-Lucas numbers

For complex numbers $a$ and $b$, the $(a, b)$-Lucas numbers are the
sequence $(L_n)_{n \ge 0}$ of complex numbers defined by $L_0 = 2$, $L_1 = a$ and
$L_{n+2} = a L_{n+1} + b L_n$ for all $n \ge 0$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.lucasAB`, a definition declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#lucas-ab).

## Zeroth (a, b)-Lucas number

For all complex numbers $a$ and $b$, the $(a,b)$-Lucas number
$L^{a,b}_0$ equals $2$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.lucasAB_zero`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#lucas-ab-zero).

## First (a, b)-Lucas number

For all complex numbers $a$ and $b$, the $(a,b)$-Lucas number
$L^{a,b}_1$ equals $a$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.lucasAB_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#lucas-ab-one).

## Recurrence for the (a, b)-Lucas numbers

For all complex numbers $a$ and $b$ and every
natural number $n$, the $(a,b)$-Lucas numbers satisfy
$L^{a,b}_{n+2} = a L^{a,b}_{n+1} + b L^{a,b}_n$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Section 1 (sequence definition).

Formalized by `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.lucasAB_add_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#lucas-ab-add-two).

## Discriminant times an (a, b)-Fibonacci number

Let $a$ and $b$ be complex numbers with
$a^2 + 4b \ne 0$, and write $F_n$ and $L_n$ for the $(a,b)$-Fibonacci and $(a,b)$-Lucas
numbers. Then for every natural number $m$,

$$(a^2 + 4b) F_{m+1} = L_{m+2} + b L_m.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Corollary 4.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.disc_mul_fibAB` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#disc-mul-fib-ab).

## Sum of even-indexed (a, b)-Fibonacci numbers weighted by powers of -b

Let $a, b$ be
complex numbers and let $(F_n)$ be the $(a, b)$-Fibonacci numbers. Then for every integer
$n \ge 0$,

$$\sum_{i=0}^{n} (-b)^{n-i} F_{2i} = F_n F_{n+1}.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Corollary 11.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_b_pow_fibAB_even_prod` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-b-pow-fib-ab-even-prod).

## Sums of (a, b)-Lucas numbers weighted by powers of -b

Let $a, b$ be complex numbers
with $b \ne 0$, and let $(F_n)$ and $(L_n)$ be the $(a, b)$-Fibonacci and $(a, b)$-Lucas
numbers. Then for every integer $n \ge 0$,

$$\sum_{i=0}^{n} (-b)^{n-i} L_{2i+1} = F_{2n+2}
\quad\text{and}\quad \sum_{i=0}^{n} (-b)^{n-i} L_{2i} = F_{2n+1} + (-b)^n.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Theorem 5(a).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_b_pow_lucasAB` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-b-pow-lucas-ab).

## Shifted sums of (a, b)-Lucas numbers weighted by powers of -b

Let $a, b$ be complex
numbers with $b \ne 0$, and let $(F_n)$ and $(L_n)$ be the $(a, b)$-Fibonacci and
$(a, b)$-Lucas numbers. Then for all integers $m, n \ge 0$,

$$\sum_{i=0}^{n} (-b)^{n-i} L_{2(i+m)+1} = F_{2(n+m)+2} + (-1)^n b^{n+1} F_{2m},$$

and this sum also equals $F_{n+m+1} L_{n+m+1} + (-1)^n b^{n+1} F_m L_m$. If moreover $m \ge 1$,
then

$$\sum_{i=0}^{n} (-b)^{n-i} L_{2(i+m)} = F_{2(n+m)+1} + (-1)^n b^{n+1} F_{2m-1},$$

and this sum also equals $F_{n+m+1} L_{n+m} + (-1)^n b^{n+1} F_m L_{m-1}$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Theorem 5(b).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_b_pow_lucasAB_shift` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-b-pow-lucas-ab-shift).

## Sums of (a, b)-Fibonacci numbers weighted by powers of -b, via Lucas numbers

Let $a, b$
be complex numbers with $\Delta = a^2 + 4b \ne 0$, and let $(F_n)$ and $(L_n)$ be the
$(a, b)$-Fibonacci and $(a, b)$-Lucas numbers. Then for every integer $n \ge 0$,

$$\sum_{i=0}^{n} (-b)^{n-i} F_{2i} = \frac{L_{2n+1} + (-1)^{n+1} a b^n}{\Delta}$$

and

$$\sum_{i=0}^{n} (-b)^{n-i} F_{2i+1} = \frac{L_{2n+2} + 2 (-1)^n b^{n+1}}{\Delta}.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Theorem 10(a).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_b_pow_fibAB_disc` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 211](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L211). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-b-pow-fib-ab-disc).

## Alternating sums of Fibonacci and Lucas numbers

Let $(F_n)$ and $(L_n)$ be the
Fibonacci and Lucas numbers, that is, the $(1, 1)$-Fibonacci and $(1, 1)$-Lucas numbers, viewed
as complex numbers. Then for every integer $n \ge 0$,

$$\sum_{i=0}^{n} (-1)^i F_{2i} = \frac{(-1)^n L_{2n+1} - 1}{5}, \qquad
\sum_{i=0}^{n} (-1)^i L_{2i} = (-1)^n F_{2n+1} + 1,$$



$$\sum_{i=0}^{n} (-1)^i F_{2i+1} = \frac{(-1)^n L_{2n+2} + 2}{5}, \qquad
\sum_{i=0}^{n} (-1)^i L_{2i+1} = (-1)^n F_{2n+2}.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Theorem 10(b).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_one_pow_fib` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-one-pow-fib).

## Alternating sums of Pell and Pell–Lucas numbers

Let $(P_n)$ and $(Q_n)$ be the Pell
and Pell–Lucas numbers, that is, the $(2, 1)$-Fibonacci and $(2, 1)$-Lucas numbers, viewed as
complex numbers. Then for every integer $n \ge 0$,

$$\sum_{i=0}^{n} (-1)^i P_{2i} = \frac{(-1)^n Q_{2n+1} - 2}{8}, \qquad
\sum_{i=0}^{n} (-1)^i Q_{2i} = (-1)^n P_{2n+1} + 1,$$



$$\sum_{i=0}^{n} (-1)^i P_{2i+1} = \frac{(-1)^n Q_{2n+2} + 2}{8}, \qquad
\sum_{i=0}^{n} (-1)^i Q_{2i+1} = (-1)^n P_{2n+2}.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Theorem 10(c).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_one_pow_pell` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-one-pow-pell).

## Weighted alternating sums of Jacobsthal and Jacobsthal–Lucas numbers

Let $(J_n)$ and
$(j_n)$ be the Jacobsthal and Jacobsthal–Lucas numbers, that is, the $(1, 2)$-Fibonacci and
$(1, 2)$-Lucas numbers, viewed as complex numbers. Then for every integer $n \ge 0$,

$$\sum_{i=0}^{n} (-1)^i 2^{n-i} J_{2i} = \frac{(-1)^n j_{2n+1} - 2^n}{9}, \qquad
\sum_{i=0}^{n} (-1)^i 2^{n-i} j_{2i} = (-1)^n J_{2n+1} + 2^n,$$



$$\sum_{i=0}^{n} (-1)^i 2^{n-i} J_{2i+1} = \frac{(-1)^n j_{2n+2} + 2^{n+2}}{9}, \qquad
\sum_{i=0}^{n} (-1)^i 2^{n-i} j_{2i+1} = (-1)^n J_{2n+2}.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Theorem 10(d).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_one_pow_jacobsthal` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-one-pow-jacobsthal).

## Alternating sums of even-indexed k-Lucas numbers

Let $k$ be a complex number, and let
$(F_{k,n})$ and $(L_{k,n})$ be the $k$-Fibonacci and $k$-Lucas numbers, that is, the
$(k, 1)$-Fibonacci and $(k, 1)$-Lucas numbers. Then for all integers $m \ge 1$ and $n \ge 0$,

$$\sum_{i=0}^{n} (-1)^i L_{k,2(i+m)} = (-1)^n F_{k,2(n+m)+1} + F_{k,2m-1}.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Corollary 9.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_neg_one_pow_k_lucasAB` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-neg-one-pow-k-lucas-ab).

## Sums of (a, b)-Fibonacci numbers weighted by powers of c

Let $a, b, c$ be complex
numbers with $c \ne 0$ and $c^2 - ac - b \ne 0$, and let $(F_n)$ be the $(a, b)$-Fibonacci
numbers. Then for every integer $n \ge 1$,

$$\sum_{i=1}^{n} c^{n-i} F_i = \frac{c^{n+1} - c F_{n+1} - b F_n}{c^2 - ac - b}.$$

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Theorem 12.

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.sum_c_pow_fibAB` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 311](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L311). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#sum-c-pow-fib-ab).

## A convolution of (a, b)-Lucas and (a, d)-Fibonacci numbers

Let $a, b, d$ be complex
numbers with $b \ne d$, and write $L^{a,b}_n$ for the $(a,b)$-Lucas numbers and $F^{a,b}_n$ for
the $(a,b)$-Fibonacci numbers. Then for every natural number $n$,

$$(b - d) \sum_{i=1}^{n} L^{a,b}_{n-i} F^{a,d}_i = L^{a,b}_{n+1} - L^{a,d}_{n+1}$$

and

$$\sum_{i=1}^{n} L^{a,b}_{n-i} F^{a,d}_i = \sum_{i=1}^{n} L^{a,d}_{n-i} F^{a,b}_i.$$

The source states the first identity in divided form,
$\sum_{i=1}^{n} L^{a,b}_{n-i} F^{a,d}_i = (L^{a,b}_{n+1} - L^{a,d}_{n+1})/(b - d)$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Corollary 14(a).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.convolution_lucasAB_fibAB` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 326](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L326). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#convolution-lucas-ab-fib-ab).

## Fibonacci, Jacobsthal and Pell convolution identities

Write $F_n$ and $L_n$ for the
Fibonacci and Lucas numbers (the $(1,1)$-Fibonacci and $(1,1)$-Lucas numbers), $J_n$ and $j_n$
for the Jacobsthal and Jacobsthal–Lucas numbers (the $(1,2)$-Fibonacci and $(1,2)$-Lucas
numbers), and $P_n$ and $Q_n$ for the Pell and Pell–Lucas numbers (the $(2,1)$-Fibonacci and
$(2,1)$-Lucas numbers), all as complex numbers. Then for every natural number $n$:
(i) $\sum_{i=1}^{n} L_{n-i} J_i = j_{n+1} - L_{n+1}$ and
$\sum_{i=1}^{n} j_{n-i} F_i = j_{n+1} - L_{n+1}$;
(ii) $2 \sum_{i=1}^{n} P_i = (Q_{n+1} - 2)/2$ and $\sum_{i=1}^{n} i \, Q_{n-i} = (Q_{n+1} - 2)/2$;
(iii) $\sum_{i=1}^{n} L_{2(n-i)} (2^i - 1) = L_{2n+2} - 2^{n+1} - 1$ and
$\sum_{i=1}^{n} (2^{n-i} + 1) F_{2i} = L_{2n+2} - 2^{n+1} - 1$.

## Sources

- Emil Daniel Schwab, "Fibonacci Numbers via Dirichlet Convolution and Lucas Numbers via Unitary Convolution", Corollary 14(b).

Stated but not proved: `MathlibExt.NumberTheory.Recurrences.ABFibonacciIdentitiesWanted.convolution_specializations` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean, line 346](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/ABFibonacciIdentitiesWanted.lean#L346). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html#convolution-specializations).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: (a, b)-Fibonacci and (a, b)-Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/a-b-fibonacci-and-a-b-lucas-numbers)
