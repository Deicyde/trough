---
declaration: section
origin: cited
lean: MetaMathlibExt.fibonacciPolyGenFun_mem_intPoly_iff, MetaMathlibExt.lucasPolyGenFun_mem_intPoly_iff, MetaMathlibExt.fibonacciGenFun_eval_isInt_iff, MetaMathlibExt.lucasGenFun_eval_isInt_iff, MetaMathlibExt.fibonacciGenFun_eval_isInt_iff_of_abs_lt_radius, MetaMathlibExt.lucasGenFun_eval_isInt_iff_of_abs_lt_radius, MetaMathlibExt.lucasNumberGenFun_eval_isInt_iff_of_abs_lt_radius, MetaMathlibExt.fibLucasPoly_of_pell_eq
statement: formalized
---

# Integer values of Fibonacci polynomial generating functions

10 results, 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html).

## Integer-polynomial values of the Fibonacci polynomial generating function

Let $a$ and $b$
be positive integers with $b \mid a$, let $F_i(x) \in \mathbb{Z}[x]$ be the polynomials with
$F_0 = 0$, $F_1 = 1$ and $F_{i+2} = ax\,F_{i+1} + b\,F_i$ for all $i \ge 0$, and let
$f(x, t) = t / (1 - axt - bt^2)$. For a rational function $q(x) \in \mathbb{Q}(x)$, the rational
function $f(x, q(x))$ is a polynomial with integer coefficients if and only if
$q(x) = F_i(x) / F_{i+1}(x)$ for some $i \in \mathbb{N}$ or
$q(x) = -F_{i+1}(x) / (b F_i(x))$ for some $i \ge 1$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Theorem 1.2.

Stated but not proved: `MetaMathlibExt.fibonacciPolyGenFun_mem_intPoly_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#fibonacci-poly-gen-fun-mem-int-poly-iff).

## Integer-polynomial values of the Lucas polynomial generating function

Let $a$ and $b$ be
positive integers with $b \mid a$, let $F_i(x), L_i(x) \in \mathbb{Z}[x]$ be the polynomials with
$F_0 = 0$, $F_1 = 1$, $L_0 = 2$, $L_1 = ax$ and $G_{i+2} = ax\,G_{i+1} + b\,G_i$ for $G = F, L$
and all $i \ge 0$, and let $l(x, t) = (2 - axt) / (1 - axt - bt^2)$. For a rational function
$q(x) \in \mathbb{Q}(x)$, the rational function $l(x, q(x))$ is a polynomial with integer
coefficients if and only if $q(x)$ is one of $F_i(x) / F_{i+1}(x)$, $L_i(x) / L_{i+1}(x)$ and
$-L_{i+1}(x) / (b L_i(x))$ for some $i \in \mathbb{N}$, or $q(x) = -F_{i+1}(x) / (b F_i(x))$ for
some $i \ge 1$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Theorem 1.3.

Stated but not proved: `MetaMathlibExt.lucasPolyGenFun_mem_intPoly_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#lucas-poly-gen-fun-mem-int-poly-iff).

## Integer values of the generalized Fibonacci generating function at rationals

Let $a$ and
$b$ be positive integers with $b \mid a$, and let $F_i(x) \in \mathbb{Z}[x]$ be the polynomials
with $F_0 = 0$, $F_1 = 1$ and $F_{i+2} = ax\,F_{i+1} + b\,F_i$ for all $i \ge 0$. For a rational
number $q$, the number $q / (1 - aq - bq^2)$ is an integer if and only if
$q = F_i(1) / F_{i+1}(1)$ for some $i \in \mathbb{N}$ or $q = -F_{i+1}(1) / (b F_i(1))$ for some
$i \ge 1$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Theorem 1.4.

Stated but not proved: `MetaMathlibExt.fibonacciGenFun_eval_isInt_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#fibonacci-gen-fun-eval-is-int-iff).

## Integer values of the generalized Lucas generating function at rationals

Let $a$ and $b$
be positive integers with $b \mid a$, and let $F_i(x), L_i(x) \in \mathbb{Z}[x]$ be the
polynomials with $F_0 = 0$, $F_1 = 1$, $L_0 = 2$, $L_1 = ax$ and
$G_{i+2} = ax\,G_{i+1} + b\,G_i$ for $G = F, L$ and all $i \ge 0$. For a rational number $q$, the
number $(2 - aq) / (1 - aq - bq^2)$ is an integer if and only if $q$ is one of
$F_i(1) / F_{i+1}(1)$, $L_i(1) / L_{i+1}(1)$ and $-L_{i+1}(1) / (b L_i(1))$ for some
$i \in \mathbb{N}$, or $q = -F_{i+1}(1) / (b F_i(1))$ for some $i \ge 1$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Theorem 1.5.

Stated but not proved: `MetaMathlibExt.lucasGenFun_eval_isInt_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#lucas-gen-fun-eval-is-int-iff).

## Integer values of the generalized Fibonacci generating function in its interval of convergence

**Integer values of the generalized Fibonacci generating function in its interval of
convergence.** Let $a$ and $b$ be positive integers with $b \mid a$, and let
$F_i(x) \in \mathbb{Z}[x]$ be the polynomials with $F_0 = 0$, $F_1 = 1$ and
$F_{i+2} = ax\,F_{i+1} + b\,F_i$ for all $i \ge 0$. For a rational number $q$ with
$|q| < 2 / (a + \sqrt{a^2 + 4b})$, the radius of convergence of the power series of
$t / (1 - at - bt^2)$, the number $q / (1 - aq - bq^2)$ is an integer if and only if
$q = F_{2i}(1) / F_{2i+1}(1)$ for some $i \in \mathbb{N}$.

The source attributes this result (its Theorem 1.1) to Bulawa and Lee.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Corollary 1.6 and Theorem 1.1.

Stated but not proved: `MetaMathlibExt.fibonacciGenFun_eval_isInt_iff_of_abs_lt_radius` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#fibonacci-gen-fun-eval-is-int-iff-of-abs).

## Integer values of the generalized Lucas generating function in its interval of convergence

**Integer values of the generalized Lucas generating function in its interval of
convergence.** Let $a$ and $b$ be positive integers with $a \ne 1$ and $b \mid a$, and let
$F_i(x), L_i(x) \in \mathbb{Z}[x]$ be the polynomials with $F_0 = 0$, $F_1 = 1$, $L_0 = 2$,
$L_1 = ax$ and $G_{i+2} = ax\,G_{i+1} + b\,G_i$ for $G = F, L$ and all $i \ge 0$. For a rational
number $q$ with $|q| < 2 / (a + \sqrt{a^2 + 4b})$, the radius of convergence of the power series
of $(2 - at) / (1 - at - bt^2)$, the number $(2 - aq) / (1 - aq - bq^2)$ is an integer if and
only if $q = F_{2i}(1) / F_{2i+1}(1)$ or $q = L_{2i+1}(1) / L_{2i+2}(1)$ for some
$i \in \mathbb{N}$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Corollary 1.7.

Stated but not proved: `MetaMathlibExt.lucasGenFun_eval_isInt_iff_of_abs_lt_radius` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#lucas-gen-fun-eval-is-int-iff-of-abs-lt).

## Integer values of the Lucas number generating function in its interval of convergence

Let $F_n$ be the Fibonacci numbers and $L_n$ the Lucas numbers, given by $L_0 = 2$, $L_1 = 1$
and $L_{n+2} = L_{n+1} + L_n$. For a rational number $q$ with $|q| < 2 / (1 + \sqrt 5)$, the
number $(2 - q) / (1 - q - q^2)$ is an integer if and only if $q = -1/2$, or
$q = F_{2i} / F_{2i+1}$ or $q = L_{2i+1} / L_{2i+2}$ for some $i \in \mathbb{N}$.

This is the case $a = b = 1$ of the generating function $(2 - at) / (1 - at - bt^2)$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Corollary 1.8.

Stated but not proved: `MetaMathlibExt.lucasNumberGenFun_eval_isInt_iff_of_abs_lt_radius` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#lucas-number-gen-fun-eval-is-int-iff-of).

## Polynomial Pell-type solutions as rescaled Fibonacci–Lucas polynomials

Let $a$ and $b$ be
positive integers, and let $F_n(x), L_n(x) \in \mathbb{Z}[x]$ be the polynomials with $F_0 = 0$,
$F_1 = 1$, $L_0 = 2$, $L_1 = ax$ and $G_{n+2} = ax\,G_{n+1} + b\,G_n$ for $G = F, L$ and all
$n \ge 0$. Let $r_0 \in \{0, 1\}$ and let $P(x), Q(x) \in \mathbb{Q}[x]$ have nonnegative leading
coefficients (the zero polynomial has leading coefficient $0$) and satisfy
$P(x)^2 - (a^2x^2 + 4b) Q(x)^2 = 4(-b)^{r_0}$. Then there is $n \in \mathbb{N}$ with
$n \equiv r_0 \pmod 2$, $b^{\lfloor n/2 \rfloor} P(x) = L_n(x)$ and
$b^{\lfloor n/2 \rfloor} Q(x) = F_n(x)$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Proposition 2.1.

Stated but not proved: `MetaMathlibExt.fibLucasPoly_of_pell_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#fib-lucas-poly-of-pell-eq).

## Pell-type solutions as rescaled odd Fibonacci–Lucas values, squarefree case

Let $a$ and
$b$ be positive integers with $b \mid a$ and $b$ squarefree, and let
$F_i(x), L_i(x) \in \mathbb{Z}[x]$ be the polynomials with $F_0 = 0$, $F_1 = 1$, $L_0 = 2$,
$L_1 = ax$ and $G_{i+2} = ax\,G_{i+1} + b\,G_i$ for $G = F, L$ and all $i \ge 0$. If natural
numbers $P$ and $Q$ satisfy $P^2 - (a^2 + 4b) Q^2 = -4b$, then there is $n \in \mathbb{N}$ with
$b^n P = L_{2n+1}(1)$ and $b^n Q = F_{2n+1}(1)$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Proposition 2.2.

Stated but not proved: `MetaMathlibExt.fibLucas_odd_of_pell_eq_of_squarefree` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 168](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L168). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#fib-lucas-odd-of-pell-eq-of-squarefree).

## Pell-type solutions as rescaled odd Fibonacci–Lucas values

Let $a$ and $b$ be positive
integers with $b \mid a$, and let $F_i(x), L_i(x) \in \mathbb{Z}[x]$ be the polynomials with
$F_0 = 0$, $F_1 = 1$, $L_0 = 2$, $L_1 = ax$ and $G_{i+2} = ax\,G_{i+1} + b\,G_i$ for $G = F, L$
and all $i \ge 0$. If natural numbers $P$ and $Q$ satisfy $P^2 - (a^2 + 4b) Q^2 = -4b$, then
there is $n \in \mathbb{N}$ with $b^n P = L_{2n+1}(1)$ and $b^n Q = F_{2n+1}(1)$.

## Sources

- Yuji Tsuno, *Polynomial Values with Integer Coefficients for the Generating Functions of Fibonacci Polynomials*, The Fibonacci Quarterly 62 (2024), Article tsuno05142024, Proposition 2.3.

Stated but not proved: `MetaMathlibExt.fibLucas_odd_of_pell_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean, line 181](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciPolynomialGeneratingFunctionValuesWanted.lean#L181). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html#fib-lucas-odd-of-pell-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer values of Fibonacci polynomial generating functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-polynomials/integer-values-of-fibonacci-polynomial-generatin)
