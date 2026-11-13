---
declaration: section
origin: cited
lean: MetaMathlibExt.fibonacciFactorial, MetaMathlibExt.fibonacciFactorial_zero, MetaMathlibExt.fibonacciFactorial_pos, MetaMathlibExt.fibonacciFactorial_ne, MetaMathlibExt.fibonacciFactorial_one, MetaMathlibExt.fibonacciFactorial_two, MetaMathlibExt.fibonacciFactorial_three, MetaMathlibExt.fibonacciJordanQuotient
statement: formalized
---

# FiboCatalan numbers

31 results, 21 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html).

## Fibonacci factorial

For a natural number $n$, the Fibonacci factorial $F_n!$ is the
rational number $F_n! = F_1 F_2 \cdots F_n$, the product of the first $n$ Fibonacci numbers
(where $F_1 = F_2 = 1$ and $F_{k+2} = F_{k+1} + F_k$); in particular $F_0! = 1$, the empty
product.

Values are taken in $\mathbb{Q}$ so that quotients of Fibonacci factorials are exact rather
than truncated by natural-number division.

Formalized by `MetaMathlibExt.fibonacciFactorial`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-factorial).

## Fibonacci factorial at zero

The Fibonacci factorial $F_0!$ equals $1$, by the
empty-product convention.

Formalized by `MetaMathlibExt.fibonacciFactorial_zero`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-factorial-zero).

## Fibonacci factorials are positive

For every natural number $n$, the Fibonacci factorial
$F_n!$ is a strictly positive rational number.

Formalized by `MetaMathlibExt.fibonacciFactorial_pos`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-factorial-pos).

## Fibonacci factorials are nonzero

For every natural number $n$, the Fibonacci factorial
$F_n!$ is a nonzero rational number.

Formalized by `MetaMathlibExt.fibonacciFactorial_ne`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-factorial-ne).

## Fibonacci factorial at one

The Fibonacci factorial $F_1!$ equals $1$, since the first
Fibonacci number is $F_1 = 1$.

Formalized by `MetaMathlibExt.fibonacciFactorial_one`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-factorial-one).

## Fibonacci factorial at two

The Fibonacci factorial $F_2! = F_1 F_2$ of the Fibonacci
numbers $F_1, F_2$ equals $1$, since $F_1 = F_2 = 1$.

Formalized by `MetaMathlibExt.fibonacciFactorial_two`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-factorial-two).

## Fibonacci factorial at three

The Fibonacci factorial $F_3! = F_1 F_2 F_3$ of the
Fibonacci numbers $F_1, F_2, F_3$ equals $2$, since $F_1 = F_2 = 1$ and $F_3 = 2$.

Formalized by `MetaMathlibExt.fibonacciFactorial_three`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-factorial-three).

## Fibonacci Jordan quotient

For a natural number $r$, the Jordan-type quotient is the
rational number $J_{r,F} = F_{2r+1}! / F_r!$, where $F_m! = F_1 F_2 \cdots F_m$ is the Fibonacci
factorial of the Fibonacci numbers $F_1 = F_2 = 1$, $F_{k+2} = F_{k+1} + F_k$ (so $F_0! = 1$).

Formalized by `MetaMathlibExt.fibonacciJordanQuotient`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-jordan-quotient).

## Fibonacci Jordan quotient is positive

For every natural number $r$, the Jordan-type
quotient $J_{r,F} = F_{2r+1}! / F_r!$ of Fibonacci factorials is a strictly positive rational
number.

Formalized by `MetaMathlibExt.fibonacciJordanQuotient_pos`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-jordan-quotient-pos).

## Fibonacci Jordan quotient at zero

The Jordan-type quotient $J_{r,F} = F_{2r+1}! / F_r!$
of Fibonacci factorials takes the value $J_{0,F} = F_1! / F_0! = 1$.

Formalized by `MetaMathlibExt.fibonacciJordanQuotient_r0`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-jordan-quotient-r0).

## Fibonacci Jordan quotient at one

The Jordan-type quotient $J_{r,F} = F_{2r+1}! / F_r!$
of Fibonacci factorials takes the value $J_{1,F} = F_3! / F_1! = 2$.

Formalized by `MetaMathlibExt.fibonacciJordanQuotient_r1`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonacci-jordan-quotient-r1).

## Generalized FiboCatalan numbers

Let $F_m! = F_1 F_2 \cdots F_m$ denote the Fibonacci
factorial of the Fibonacci numbers $F_1 = F_2 = 1$, $F_{k+2} = F_{k+1} + F_k$ (so $F_0! = 1$),
and let $J_{r,F} = F_{2r+1}! / F_r!$ be the Fibonacci Jordan quotient. For natural numbers $r$
and $n$, the generalized FiboCatalan number with parameters $r$ and $n$ is the rational number
$J_{r,F} \, F_{2n}! / (F_n! \, F_{n+r+1}!)$.

Formalized by `MetaMathlibExt.generalizedFibonacciCatalan`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#generalized-fibonacci-catalan).

## Positivity of generalized FiboCatalan numbers

For all natural numbers $r$ and $n$, the
generalized FiboCatalan number with parameters $r$ and $n$ is a strictly positive rational
number.

Formalized by `MetaMathlibExt.generalizedFibonacciCatalan_pos`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#generalized-fibonacci-catalan-pos).

## Generalized FiboCatalan numbers are positive integers

For all natural numbers $r$ and
$n$, the generalized FiboCatalan number with parameters $r$ and $n$ is a positive integer: it
equals $k$ for some natural number $k \ge 1$.

Formalized by `MetaMathlibExt.generalizedFibonacciCatalan_isPosInt`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#generalized-fibonacci-catalan-is-pos-int).

## Generalized FiboCatalan numbers at r = 0

For every natural number $n$, the generalized
FiboCatalan number with parameters $r = 0$ and $n$ equals the FiboCatalan number
$F_{2n}! / (F_n! \, F_{n+1}!)$, where $F_i$ is the $i$-th Fibonacci number ($F_1 = F_2 = 1$) and
$F_m! = F_1 F_2 \cdots F_m$ is the Fibonacci factorial (with $F_0! = 1$).

Formalized by `MetaMathlibExt.generalizedFibonacciCatalan_r0`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 501](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L501). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#generalized-fibonacci-catalan-r0).

## Generalized FiboCatalan numbers at r = 1

For every natural number $n$, the generalized
FiboCatalan number with parameters $r = 1$ and $n$ equals $2 F_{2n}! / (F_{n+2}! \, F_n!)$, where
$F_i$ is the $i$-th Fibonacci number ($F_1 = F_2 = 1$) and $F_m! = F_1 F_2 \cdots F_m$ is the
Fibonacci factorial (with $F_0! = 1$).

Formalized by `MetaMathlibExt.generalizedFibonacciCatalan_r1`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/GeneralizedFibocatalanNumber.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#generalized-fibonacci-catalan-r1).

## FiboCatalan numbers

For a natural number $n$, the FiboCatalan number is the rational
number $C_{n,F} = F_{2n}!/(F_n! \, F_{n+1}!)$, where $F_j$ is the $j$-th Fibonacci number and
$F_k! = F_1 F_2 \cdots F_k$ is the Fibonacci factorial.

Formalized by `MathlibExt.NumberTheory.SuperFibocatalanWanted.fiboCatalan`, a definition declared in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibo-catalan).

## Fibonomial coefficients

For natural numbers $n$ and $k$, the fibonomial coefficient
$\binom{n}{k}_F$ is the rational number $F_n!/(F_k! \, F_{n-k}!)$ when $k \le n$, where $F_i$ is
the $i$-th Fibonacci number and $F_j! = F_1 F_2 \cdots F_j$ is the Fibonacci factorial, and $0$
when $k > n$.

Formalized by `MathlibExt.NumberTheory.SuperFibocatalanWanted.fibonomial`, a definition declared in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibonomial).

## Super FiboCatalan numbers are positive integers

For all natural numbers $m$ and $n$, the
super FiboCatalan number

$$S(m, n)_F = \frac{F_{2m}!\, F_{2n}!}{F_m!\, F_n!\, F_{m+n}!},$$

where $F_j!$ denotes the Fibonacci factorial, is a positive integer: it equals $k$ for some
natural number $k \ge 1$.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Corollary 5.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.superFibonacciCatalan_isPosInt` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#super-fibonacci-catalan-is-pos-int).

## Fibonacci identity $F_{2n} F_{n+2} - F_{2n+2} F_n = (-1)^n F_n$

For every natural
number $n$, the Fibonacci numbers ($F_0 = 0$, $F_1 = 1$, $F_{k+2} = F_{k+1} + F_k$) satisfy
$F_{2n} F_{n+2} - F_{2n+2} F_n = (-1)^n F_n$.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Lemma 6.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.fib_mul_sub_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 91](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L91). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fib-mul-sub-mul).

## An identity between consecutive FiboCatalan numbers

Let $F_k$ be the Fibonacci
numbers, $F_k! = F_1 F_2 \cdots F_k$ the Fibonacci factorial and
$C_{k,F} = F_{2k}!/(F_k! \, F_{k+1}!)$ the FiboCatalan number. For every natural number $n$,
in $\mathbb{Q}$,

$$F_{2n+1} F_{2n} C_{n,F} - F_{n+1} F_n C_{n+1,F}
= (-1)^n F_n F_{2n+1} \frac{F_{2n}!}{F_{n+2}! \, F_n!}.$$

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Theorem 7.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.fiboCatalan_identity` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fibo-catalan-identity).

## Integrality of $F_{2n+1} F_{2n}!/(F_{n+2}! \, F_n!)$

Let $F_k$ be the Fibonacci
numbers, $F_k! = F_1 F_2 \cdots F_k$ the Fibonacci factorial and, for $k \le m$,
$\binom{m}{k}_F = F_m!/(F_k! \, F_{m-k}!)$ the fibonomial coefficient. For every natural
number $n \ge 1$,

$$F_{2n+1} \frac{F_{2n}!}{F_{n+2}! \, F_n!} = \frac{1}{F_{n+2}} \binom{2n+1}{n}_F,$$

and this rational number is an integer.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Corollary 8.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.fib_mul_factorialQuotient_eq_and_isInt` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#fib-mul-factorial-quotient-eq-and-is-int).

## Lucas polynomials in $s$ and $t$

The Lucas polynomials $\{n\}$, for natural numbers
$n$, are the polynomials in two variables $s$ and $t$ with integer coefficients defined by
$\{0\} = 0$, $\{1\} = 1$ and $\{n + 2\} = s\{n + 1\} + t\{n\}$ for every $n \ge 0$.

Formalized by `MathlibExt.NumberTheory.SuperFibocatalanWanted.lucasPoly`, a definition declared in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#lucas-poly).

## Lucas factorial

For a natural number $n$, the Lucas factorial $\{n\}!$ is the product
$\{n\}! = \{1\}\{2\} \cdots \{n\}$ of the Lucas polynomials $\{i\}$ in $s$ and $t$ for
$1 \le i \le n$, a polynomial with integer coefficients; in particular $\{0\}! = 1$, the empty
product.

Formalized by `MathlibExt.NumberTheory.SuperFibocatalanWanted.lucasFactorial`, a definition declared in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#lucas-factorial).

## $k$-divisible Lucas factorial

For natural numbers $k$ and $n$, the $k$-divisible Lucas
factorial $\{n : k\}!$ is the product $\{n : k\}! = \{k\}\{2k\} \cdots \{nk\}$ of the Lucas
polynomials $\{ki\}$ in $s$ and $t$ for $1 \le i \le n$; in particular $\{0 : k\}! = 1$,
the empty product.

Formalized by `MathlibExt.NumberTheory.SuperFibocatalanWanted.lucasKDivFactorial`, a definition declared in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#lucas-kdiv-factorial).

## Lucas super FiboCatalan numbers have non-negative coefficients

Let $\{k\}$ be the
Lucas polynomials in $s$ and $t$ ($\{0\} = 0$, $\{1\} = 1$, $\{k+2\} = s\{k+1\} + t\{k\}$) and
let $\{k\}! = \{1\}\{2\} \cdots \{k\}$ be the Lucas factorial. For all natural numbers $m$
and $n$ there is a polynomial $p \in \mathbb{Z}[s, t]$ with non-negative coefficients such
that $p \, \{m\}! \, \{n\}! \, \{m+n\}! = \{2m\}! \, \{2n\}!$; that is, the Lucas analogue
$S\{m, n\} = \{2m\}! \, \{2n\}!/(\{m\}! \, \{n\}! \, \{m+n\}!)$ of the super FiboCatalan number
is a polynomial in $s$ and $t$ with non-negative integer coefficients.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.exists_nonneg_poly_superLucasCatalan` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#exists-nonneg-poly-super-lucas-catalan).

## Lucas generalized FiboCatalan numbers have non-negative coefficients

Let $\{k\}$ be
the Lucas polynomials in $s$ and $t$ ($\{0\} = 0$, $\{1\} = 1$, $\{k+2\} = s\{k+1\} + t\{k\}$)
and let $\{k\}! = \{1\}\{2\} \cdots \{k\}$ be the Lucas factorial. For all natural numbers
$r$ and $n$ there is a polynomial $p \in \mathbb{Z}[s, t]$ with non-negative coefficients such
that $p \, \{r\}! \, \{n\}! \, \{n+r+1\}! = \{2r+1\}! \, \{2n\}!$; that is, with
$J_{\{r\}} = \{2r+1\}!/\{r\}!$, the Lucas analogue $J_{\{r\}} \, \{2n\}!/(\{n\}! \, \{n+r+1\}!)$
of the generalized FiboCatalan number is a polynomial in $s$ and $t$ with non-negative integer
coefficients.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Theorem 4.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.exists_nonneg_poly_generalizedLucasCatalan` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#exists-nonneg-poly-generalized-lucas-cat).

## Cross-product identity for Lucas polynomials

For every natural number $n$, the Lucas
polynomials $\{k\}$ in $s$ and $t$ satisfy
$\{2n\}\{n + 2\} - \{2n + 2\}\{n\} = (-1)^n \{2\} t^n \{n\}$.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Lemma 10.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.lucasPoly_mul_sub_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#lucas-poly-mul-sub-mul).

## Lucas analogue of the FiboCatalan identity, cleared of denominators

Let $\{k\}$ be
the Lucas polynomials in $s$ and $t$ ($\{0\} = 0$, $\{1\} = 1$, $\{k+2\} = s\{k+1\} + t\{k\}$)
and let $\{k\}! = \{1\}\{2\} \cdots \{k\}$ be the Lucas factorial. For every natural number
$n$, in $\mathbb{Z}[s, t]$,

$$(\{2n+1\} \{2n\} \{n+2\} - \{2n+2\} \{2n+1\} \{n\}) \, \{2n\}!
= (-1)^n t^n \{2\} \{n\} \{2n+1\} \, \{2n\}!.$$

With the Lucas Catalan numbers $C_{\{k\}} = \{2k\}!/(\{k\}! \, \{k+1\}!)$, this is the identity

$$\{2n+1\} \{2n\} C_{\{n\}} - \{n+1\} \{n\} C_{\{n+1\}}
= (-1)^n t^n \{2\} \{n\} \{2n+1\} \frac{\{2n\}!}{\{n+2\}! \, \{n\}!}$$

multiplied through by $\{n+2\}! \, \{n\}!$.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Theorem 11.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.lucasCatalan_identity_mul_factorial` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#lucas-catalan-identity-mul-factorial).

## The Lucas quotient $\{2n+1\} \{2\} \{2n\}!/(\{n+2\}! \, \{n\}!)$ has non-negative coefficients

**The Lucas quotient $\{2n+1\} \{2\} \{2n\}!/(\{n+2\}! \, \{n\}!)$ has non-negative
coefficients.** Let $\{k\}$ be the Lucas polynomials in $s$ and $t$ ($\{0\} = 0$, $\{1\} = 1$,
$\{k+2\} = s\{k+1\} + t\{k\}$) and let $\{k\}! = \{1\}\{2\} \cdots \{k\}$ be the Lucas
factorial. For every natural number $n \ge 1$,

$$\{n+2\} \, \{2n+1\} \, \{2n\}! \, \{n\}! \, \{n+1\}! = \{n+2\}! \, \{n\}! \, \{2n+1\}!,$$

and there is a polynomial $p \in \mathbb{Z}[s, t]$ with non-negative coefficients such that
$p \, \{n+2\}! \, \{n\}! = \{2n+1\} \, \{2\} \, \{2n\}!$. That is, the quotient
$\{2n+1\} \{2\} \{2n\}!/(\{n+2\}! \, \{n\}!)$, which by the first identity equals
$\{2\} \, \frac{1}{\{n+2\}} \, \{2n+1\}!/(\{n\}! \, \{n+1\}!)$, is a polynomial in $s$ and $t$
with non-negative integer coefficients.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Corollary 12.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.exists_nonneg_poly_lucasQuotient` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#exists-nonneg-poly-lucas-quotient).

## $k$-divisible Lucas super Catalan numbers have non-negative coefficients

Let $\{j\}$ be
the Lucas polynomials in $s$ and $t$ ($\{0\} = 0$, $\{1\} = 1$, $\{j+2\} = s\{j+1\} + t\{j\}$)
and let $\{n : k\}! = \{k\}\{2k\} \cdots \{nk\}$ be the $k$-divisible Lucas factorial. For all
natural numbers $k$, $m$ and $n$ with $k \ge 1$ there is a polynomial $p \in \mathbb{Z}[s, t]$
with non-negative coefficients such that

$$p \, \{m : k\}! \, \{n : k\}! \, \{m+n : k\}! = \{2m : k\}! \, \{2n : k\}!;$$

that is, the $k$-divisible lucanomial analogue
$S\{m, n : k\} = \{2m : k\}! \, \{2n : k\}!/(\{m : k\}! \, \{n : k\}! \, \{m+n : k\}!)$ of the
super Catalan numbers is a polynomial in $s$ and $t$ with non-negative integer coefficients.

## Sources

- Kendra Killpatrick, "Super FiboCatalan Numbers and Their Lucas Analogues", Theorem 13.

Stated but not proved: `MathlibExt.NumberTheory.SuperFibocatalanWanted.exists_nonneg_poly_kDivLucasCatalan` is written with `theorem_wanted` in [WantedExt/NumberTheory/SuperFibocatalanWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SuperFibocatalanWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html#exists-nonneg-poly-k-div-lucas-catalan).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: FiboCatalan numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/special-numbers/catalan-numbers/fibocatalan-numbers)
