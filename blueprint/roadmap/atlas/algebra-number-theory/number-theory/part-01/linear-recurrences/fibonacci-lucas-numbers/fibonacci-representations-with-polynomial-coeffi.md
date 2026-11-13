---
declaration: section
origin: cited
lean: MetaMathlibExt.fib_linear_coeff_isInt_iff, MetaMathlibExt.fib_quadratic_coeff_isInt_iff, MetaMathlibExt.fib_quadratic_linear_coeff_isInt_iff, MetaMathlibExt.fib_linear_coeff_add_alternating_isInt_iff
statement: formalized
---

# Fibonacci representations with polynomial coefficients

4 results, 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-representations-with-polynomial-coeffi/index.html).

## Integer sequences with linear Fibonacci coefficients

Let $F_n$ be the $n$-th Fibonacci
number and put $F_{-1} = 1$, so that $F_{n-1} = F_{n+1} - F_n$ for every $n \ge 0$. For rational
numbers $a, b, c, d$, the number $w_n = (an + b)F_n + (cn + d)F_{n-1}$ is an integer for every
natural number $n$ if and only if $d$ is an integer and there are integers $z_1, z_2, z_3$ with
$a = (-z_1 - 3z_2 + 2z_3)/5$, $b = (6z_1 + 3z_2 - 2z_3)/5$ and $c = (-2z_1 + 4z_2 - z_3)/5$.

The integers $z_i$ are then determined by the sequence: $z_1 = w_1$, $z_2 = w_2 - d$ and
$z_3 = w_3 - d$.

## Sources

- Kálmán Liptai, László Németh, Tamás Szakács and László Szalay, *On Certain Fibonacci Representations*, Fibonacci Quarterly 62 (2024), no. 4, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.fib_linear_coeff_isInt_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-representations-with-polynomial-coeffi/index.html#fib-linear-coeff-is-int-iff).

## Integer sequences with quadratic Fibonacci coefficients

Let $F_n$ be the $n$-th Fibonacci
number and put $F_{-1} = 1$, so that $F_{n-1} = F_{n+1} - F_n$ for every $n \ge 0$. For rational
numbers $a, b, c, d, e, f$, the number
$w_n = (an^2 + bn + c)F_n + (dn^2 + en + f)F_{n-1}$ is an integer for every natural number $n$
if and only if $f$ is an integer and there are integers $z_1, \dots, z_5$ with
$a = (-z_1 + 3z_2 + z_3 - 3z_4 + z_5)/10$,
$b = (-5z_1 - 75z_2 + 15z_3 + 45z_4 - 17z_5)/50$,
$c = (30z_1 + 30z_2 - 10z_3 - 15z_4 + 6z_5)/25$,
$d = (3z_1 - 4z_2 - 3z_3 + 4z_4 - z_5)/10$ and
$e = (-45z_1 + 80z_2 + 15z_3 - 40z_4 + 11z_5)/50$.

The integers $z_i$ are then determined by the sequence: $z_1 = w_1$, $z_2 = w_2 - f$,
$z_3 = w_3 - f$, $z_4 = w_4 - 2f$ and $z_5 = w_5 - 3f$.

## Sources

- Kálmán Liptai, László Németh, Tamás Szakács and László Szalay, *On Certain Fibonacci Representations*, Fibonacci Quarterly 62 (2024), no. 4, Theorem 2.2.

Stated but not proved: `MetaMathlibExt.fib_quadratic_coeff_isInt_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-representations-with-polynomial-coeffi/index.html#fib-quadratic-coeff-is-int-iff).

## Integer sequences with quadratic and linear Fibonacci coefficients

Let $F_n$ be the
$n$-th Fibonacci number and put $F_{-1} = 1$, so that $F_{n-1} = F_{n+1} - F_n$ for every
$n \ge 0$. For rational numbers $a, b, c, d, e$, the number
$w_n = (an^2 + bn + c)F_n + (dn + e)F_{n-1}$ is an integer for every natural number $n$ if and
only if $e$ is an integer and there are integers $z_1, z_2, z_3, z_4$ with
$a = (2z_1 - z_2 - 2z_3 + z_4)/10$, $b = (-56z_1 - 7z_2 + 66z_3 - 23z_4)/50$,
$c = (48z_1 + 6z_2 - 28z_3 + 9z_4)/25$ and $d = (-6z_1 + 18z_2 - 9z_3 + 2z_4)/25$.

The integers $z_i$ are then determined by the sequence: $z_1 = w_1$, $z_2 = w_2 - e$,
$z_3 = w_3 - e$ and $z_4 = w_4 - 2e$.

## Sources

- Kálmán Liptai, László Németh, Tamás Szakács and László Szalay, *On Certain Fibonacci Representations*, Fibonacci Quarterly 62 (2024), no. 4, Theorem 2.3.

Stated but not proved: `MetaMathlibExt.fib_quadratic_linear_coeff_isInt_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-representations-with-polynomial-coeffi/index.html#fib-quadratic-linear-coeff-is-int-iff).

## Integer sequences with linear Fibonacci coefficients and an alternating term

Let $F_n$
be the $n$-th Fibonacci number and put $F_{-1} = 1$, so that $F_{n-1} = F_{n+1} - F_n$ for every
$n \ge 0$. For rational numbers $a, b, c, d, e, f$, the number
$w_n = (an + b)F_n + (cn + d)F_{n-1} + e + f(-1)^n$ is an integer for every natural number $n$
if and only if there are integers $v_0, \dots, v_5$ with
$a = (3v_0 + 2v_1 - 7v_2 - v_3 + 4v_4 - v_5)/5$,
$b = (-3v_0 - 2v_1 - 3v_2 + 6v_3 + 6v_4 - 4v_5)/5$,
$c = (-4v_0 - v_1 + 11v_2 - 2v_3 - 7v_4 + 3v_5)/5$,
$d = -2v_1 + v_2 + 2v_3 - v_4$,
$e = (v_0 + 3v_1 + v_2 - 3v_3 - v_4 + v_5)/2$ and
$f = (v_0 + v_1 - 3v_2 - v_3 + 3v_4 - v_5)/2$.

These integers are then the initial values of the sequence: $v_i = w_i$ for $0 \le i \le 5$.

## Sources

- Kálmán Liptai, László Németh, Tamás Szakács and László Szalay, *On Certain Fibonacci Representations*, Fibonacci Quarterly 62 (2024), no. 4, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.fib_linear_coeff_add_alternating_isInt_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean, line 119](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialCoefficientsWanted.lean#L119). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-representations-with-polynomial-coeffi/index.html#fib-linear-coeff-add-alternating-is-int).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fibonacci representations with polynomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-representations-with-polynomial-coeffi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/fibonacci-representations-with-polynomial-coeffi)
