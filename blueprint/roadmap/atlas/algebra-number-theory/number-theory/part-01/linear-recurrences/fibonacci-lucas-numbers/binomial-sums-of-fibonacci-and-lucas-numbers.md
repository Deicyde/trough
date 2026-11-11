---
declaration: section
origin: cited
lean: MetaMathlibExt.choose_succ_int, MetaMathlibExt.fib_conv_step, MetaMathlibExt.binomial_fibonacci_convolution, MetaMathlibExt.sqrt5_ne, MetaMathlibExt.cb_lucas_binet, MetaMathlibExt.cb_keyR, MetaMathlibExt.church_bicknell_fibonacci_convolution
statement: formalized
proof: formalized
---

# Binomial sums of Fibonacci and Lucas numbers

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html).

## Pascal's rule for binomial coefficients

For all natural numbers $n$ and $i$,
$\binom{n+1}{i+1} = \binom{n}{i} + \binom{n}{i+1}$, as an identity of integers.

Formalized by `MetaMathlibExt.choose_succ_int`, a theorem declared in [MathlibExt/NumberTheory/BinomialFibonacciConvolution.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinomialFibonacciConvolution.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html#choose-succ-int).

## Fibonacci step in the alternating binomial sum

Let $F_m$ denote the $m$-th Fibonacci
number, with $F_0 = 0$ and $F_1 = 1$. For natural numbers $n$, $k$ and $i$ with $i \le n$,
$F_{2n+2-i+k} - F_{2n+1-i+k} = F_{2n-i+k}$, as an identity of integers.

Formalized by `MetaMathlibExt.fib_conv_step`, a theorem declared in [MathlibExt/NumberTheory/BinomialFibonacciConvolution.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinomialFibonacciConvolution.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html#fib-conv-step).

## Alternating binomial sum of Fibonacci numbers

Let $F_m$ denote the $m$-th Fibonacci
number, with $F_0 = 0$ and $F_1 = 1$. For all natural numbers $n$ and $k$,

$$\sum_{i=0}^{n} (-1)^i \binom{n}{i} F_{2n-i+k} = F_k.$$

## Sources

- Brian Hopkins and Aram Tangboonduangjit, "Scaled Fibonacci- and Lucas-Producing Rational Polynomials," Journal of Integer Sequences 25 (2022), Article 22.3.5 (Corollary generalizing Corollary cor51(a), lines 989–1000), <https://cs.uwaterloo.ca/journals/JIS/VOL25/Hopkins/tang25.tex>. The sum is the `n`-th forward difference, which telescopes by Pascal's rule and `fib (m + 2) = fib m + fib (m + 1)`.

Formalized by `MetaMathlibExt.binomial_fibonacci_convolution`, a theorem declared in [MathlibExt/NumberTheory/BinomialFibonacciConvolution.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/BinomialFibonacciConvolution.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html#binomial-fibonacci-convolution).

## The square root of 5 is nonzero

The real square root $\sqrt{5}$ is not equal to $0$.

This is used to clear the denominators in Binet's formula.

Formalized by `MetaMathlibExt.sqrt5_ne`, a theorem declared in [MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html#sqrt5-ne).

## Binet's formula for the Lucas numbers

For every natural number $n$,
$\varphi^n + \psi^n = L_n$ as real numbers, where $\varphi = (1 + \sqrt{5})/2$ is the golden ratio,
$\psi = (1 - \sqrt{5})/2$ is its conjugate, and $L_n$ is the $n$-th Lucas number.

Formalized by `MetaMathlibExt.cb_lucas_binet`, a theorem declared in [MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html#cb-lucas-binet).

## Church–Bicknell convolution over the reals

For every natural number $n$,

$$\sum_{k=0}^{n} \binom{n}{k} F_k F_{n-k} = \frac{2^n L_n - 2}{5}$$

holds as an identity of real numbers, where $F_k$ is the $k$-th Fibonacci number and $L_n$ is
the $n$-th Lucas number.

Formalized by `MetaMathlibExt.cb_keyR`, a theorem declared in [MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html#cb-key-r).

## Church–Bicknell Fibonacci binomial convolution

For every natural number $n$,

$$\sum_{k=0}^{n} \binom{n}{k} F_k F_{n-k} = \frac{2^n L_n - 2}{5}$$

holds as an identity of rational numbers, where $F_k$ is the $k$-th Fibonacci number and $L_n$
is the $n$-th Lucas number.

## Sources

- Ira M. Gessel and Ishan Kar, "Binomial Convolutions for Rational Power Series," Journal of Integer Sequences 27 (2024), Article 24.1.3, equation `e-cb1` (attributed there to C. A. Church and Marjorie Bicknell, "Exponential generating functions for Fibonacci identities," Fibonacci Quarterly 11 (1973), 275–281). The proof follows the Binet-form computation in the JIS article: with `φ`, `ψ` the golden ratio and its conjugate, expand `(φ^k - ψ^k)(φ^(n-k) - ψ^(n-k))` and evaluate the four resulting binomial sums by the binomial theorem.

Formalized by `MetaMathlibExt.church_bicknell_fibonacci_convolution`, a theorem declared in [MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/ChurchBicknellFibonacciConvolution.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html#church-bicknell-fibonacci-convolution).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binomial sums of Fibonacci and Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/fibonacci-lucas-numbers/binomial-sums-of-fibonacci-and-lucas-numbers)
