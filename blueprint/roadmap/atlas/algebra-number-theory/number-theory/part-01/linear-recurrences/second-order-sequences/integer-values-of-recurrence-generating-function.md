---
declaration: section
origin: cited
lean: MetaMathlibExt.gibonacciGeneratingValue, MetaMathlibExt.gibonacciGeneratingValue_zero, MetaMathlibExt.gibonacciGeneratingValue_one, MetaMathlibExt.IsGibonacciGood, MetaMathlibExt.isGibonacciGood_zero, MetaMathlibExt.isGibonacciGood_one, MetaMathlibExt.gibonacci_powerSeries_mul, MetaMathlibExt.isGibonacciGood_transform
statement: formalized
---

# Integer values of recurrence generating functions

37 results, 19 proved and 18 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html).

## Gibonacci generating function

For integers $a$ and $b$ and a rational number $x$, the
value of the Gibonacci generating function at $x$ is the rational number

$$G^{(a,b)}(x) = \frac{(b - a)x + a}{1 - x - x^2}.$$

It is the generating function of the Gibonacci sequence $(G_n)_{n \ge 0}$ with $G_0 = a$,
$G_1 = b$ and $G_{n+2} = G_{n+1} + G_n$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 5 (`jis-2024-24.3.1-lem-5`).

Formalized by `MetaMathlibExt.gibonacciGeneratingValue`, a definition declared in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#gibonacci-generating-value).

## Value of the Gibonacci generating function at zero

For all integers $a$ and $b$, the
Gibonacci generating function $G^{(a,b)}(x) = \frac{(b - a)x + a}{1 - x - x^2}$ takes the value
$G^{(a,b)}(0) = a$ at $x = 0$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 5 (`jis-2024-24.3.1-lem-5`).

Formalized by `MetaMathlibExt.gibonacciGeneratingValue_zero`, a theorem declared in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#gibonacci-generating-value-zero).

## Value of the Gibonacci generating function at one

For all integers $a$ and $b$, the
Gibonacci generating function $G^{(a,b)}(x) = \frac{(b - a)x + a}{1 - x - x^2}$ takes the value
$G^{(a,b)}(1) = -b$ at $x = 1$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 5 (`jis-2024-24.3.1-lem-5`).

Formalized by `MetaMathlibExt.gibonacciGeneratingValue_one`, a theorem declared in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#gibonacci-generating-value-one).

## Good rationals for a Gibonacci generating function

Let $a$ and $b$ be integers and let
$G^{(a,b)}(x) = \frac{(b - a)x + a}{1 - x - x^2}$ be the generating function of the Gibonacci
sequence with initial terms $a$ and $b$. A rational number $x$ is good for $(a, b)$ when
$1 - x - x^2 \ne 0$ and $G^{(a,b)}(x)$ is an integer.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1 (the paper says `x = p / q` is good for `(a, b)` when `G^{(a,b)}(x)` is an integer; Theorem 1 uses the same integrality without the word good).

Formalized by `MetaMathlibExt.IsGibonacciGood`, a definition declared in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good).

## Zero is good for every pair

For all integers $a$ and $b$, the rational number $0$ is good
for $(a, b)$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 5 (`jis-2024-24.3.1-lem-5`).

Formalized by `MetaMathlibExt.isGibonacciGood_zero`, a theorem declared in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-zero).

## One is good for every pair

For all integers $a$ and $b$, the rational number $1$ is good
for $(a, b)$.

The value of the Gibonacci generating function there is $G^{(a,b)}(1) = -b$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 5 (`jis-2024-24.3.1-lem-5`).

Formalized by `MetaMathlibExt.isGibonacciGood_one`, a theorem declared in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-one).

## Generating series of a Gibonacci sequence

Let $a$ and $b$ be integers and let
$(G_n)_{n \ge 0}$ be the Gibonacci sequence with $G_0 = a$ and $G_1 = b$. In the ring
$\mathbb{Q}[[X]]$ of formal power series with rational coefficients,

$$(1 - X - X^2) \sum_{n \ge 0} G_n X^n = a + (b - a) X.$$

This is the product form of the quotient $\frac{(b - a)x + a}{1 - x - x^2}$ for the generating
function of $(G_n)$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 5 (`jis-2024-24.3.1-lem-5`).

Stated but not proved: `MetaMathlibExt.gibonacci_powerSeries_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#gibonacci-power-series-mul).

## Goodness passes to two transformed fractions

Let $a$, $b$, $p$, $q$ be integers with
$q \ne 0$ and $\gcd(p, q) = 1$, and suppose that $p/q$ is good for $(a, b)$. If $p + q \ne 0$,
then $q/(p + q)$ is good for $(a, b)$; and if $p \ne 0$, then $(q - p)/p$ is good for $(a, b)$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Theorem 1 (`jis-2024-24.3.1-thm-1`).

Stated but not proved: `MetaMathlibExt.isGibonacciGood_transform` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-transform).

## Congruence criterion for good fractions

Let $a, b, p, q$ be integers with
$(a, b) \ne (0, 0)$, $q \ne 0$ and $\gcd(p, q) = 1$, and put $m = |q^2 - pq - p^2|$. Then
$p / q$ is good for $(a, b)$ if and only if there are integers $u$ and $v$ with
$(q - p) u \equiv 1$, $p v \equiv 1$, $a \equiv -b p u$ and $a \equiv -b q v \pmod{m}$.

In the source's notation, with modular inverses, the condition reads
$a \equiv -bp(q - p)^{-1} \equiv -bqp^{-1} \pmod{m}$.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 6 (`jis-2024-24.3.1-lem-6`).

Stated but not proved: `MetaMathlibExt.isGibonacciGood_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-iff).

## Consecutive Fibonacci ratios are good

For all integers $a$ and $b$ and every natural
number $n$, the ratio $F_n / F_{n+1}$ of consecutive Fibonacci numbers is good for $(a, b)$.

The source allows every integer $n \ne -1$, using the Fibonacci numbers at negative indices.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 7 (`jis-2024-24.3.1-lem-7`).

Stated but not proved: `MetaMathlibExt.isGibonacciGood_fib_div` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-fib-div).

## Two standard families of good values

Let $a$ and $b$ be integers and let $(G_n)_{n \ge 0}$
be the Gibonacci sequence with $G_0 = a$ and $G_1 = b$. For every natural number $n$, the ratio
$F_n / F_{n+1}$ of consecutive Fibonacci numbers is good for $(a, b)$, and if $G_n \ne 0$, then
$-G_{n+1} / G_n$ is good for $(a, b)$.

The source indexes both families by all integers ($n \ne -1$ for the first).

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Corollary 2 (`jis-2024-24.3.1-cor-2`).

Stated but not proved: `MetaMathlibExt.isGibonacciGood_standard_values` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-standard-values).

## Consecutive ratios of a shifted Gibonacci sequence are good

Let $a$ and $b$ be integers
and let $(H_n)_{n \ge 0}$ be the Gibonacci sequence with $H_0 = -b$ and $H_1 = a$. For every
natural number $n$ with $H_{n+1} \ne 0$, the ratio $H_n / H_{n+1}$ is good for $(a, b)$.

The source indexes $H$ by all integers.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Lemma 8 (`jis-2024-24.3.1-lem-8`).

Stated but not proved: `MetaMathlibExt.isGibonacciGood_shifted_ratio` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-shifted-ratio).

## Good consecutive ratios of a Gibonacci sequence

Let $p$ and $q$ be coprime integers,
let $(H_n)_{n \ge 0}$ be the Gibonacci sequence with $H_0 = p$ and $H_1 = q$, and put
$m = |q^2 - pq - p^2|$. Call a pair of integers $(a, b)$ admissible when $H_n / H_{n+1}$ is
good for $(a, b)$ for every natural number $n$ with $H_{n+1} \ne 0$. Then there are infinitely
many admissible pairs, and a pair $(a, b)$ is admissible if and only if there are integers $u$
and $v$ with $(q - p) u \equiv 1$, $p v \equiv 1$, $a \equiv -b p u$ and
$a \equiv -b q v \pmod{m}$.

In the source's notation, with modular inverses, the condition reads
$a \equiv -bp(q - p)^{-1} \equiv -bqp^{-1} \pmod{m}$. The source indexes $H$ by all integers.

## Sources

- Knapp, *Fibonacci Generating Functions*, Journal of Integer Sequences 27 (2024), Article 24.3.1, Theorem 3 (`jis-2024-24.3.1-thm-3`).

Stated but not proved: `MetaMathlibExt.isGibonacciGood_ratios_infinite_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/FibonacciGeneratingFunctionsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-gibonacci-good-ratios-infinite-iff).

## Generating function of the recurrence $A_{n+1} = pA_n + A_{n-1}$

For integers $a$, $b$,
$p$ and a rational number $x$, $A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$, with the convention
that a fraction with denominator $0$ is $0$. As a rational function, $A$ is the generating function
$\sum_{n \ge 0} A_n x^n$ of the sequence with $A_0 = a$, $A_1 = b$ and $A_{n+1} = pA_n + A_{n-1}$;
for $p \ne 0$ the denominator $1 - px - x^2$ has no rational root.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Section 2.

Formalized by `MetaMathlibExt.secondOrderGenValue`, a definition declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value).

## Value of the generating function at zero

For all integers $a, b, p$, the function
$A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$ on the rationals satisfies $A(0) = a$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, proof of Theorem 2.

Formalized by `MetaMathlibExt.secondOrderGenValue_zero`, a theorem declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-zero).

## Forward part of a second-order sequence

For integers $p, r, s$, this is the sequence
$(A^{(r,s)}_n)_{n \ge 0}$ of integers with $A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and
$A^{(r,s)}_{n+2} = pA^{(r,s)}_{n+1} + A^{(r,s)}_n$ for every natural number $n$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.secondOrderFwd`, a definition declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-fwd).

## Backward part of the two-sided sequence

For integers $p$, $r$ and $s$, the backward
part is the sequence $(B_k)_{k \ge 0}$ with $B_0 = s$, $B_1 = r$ and $B_{k+2} = B_k - pB_{k+1}$.
Thus $B_k$ is the term of index $1 - k$ of the two-sided sequence with $A_0 = r$, $A_1 = s$ and
$A_{n+1} = pA_n + A_{n-1}$, computed backwards by $A_n = A_{n+2} - pA_{n+1}$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.secondOrderBwd`, a definition declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-bwd).

## Two-sided second-order sequence

For integers $p$, $r$ and $s$, the two-sided sequence
$(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ for $p$ is the integer sequence indexed by $\mathbb{Z}$ with
$A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and $A^{(r,s)}_{n+1} = pA^{(r,s)}_n + A^{(r,s)}_{n-1}$ for
every integer $n$.

The paper's forward rule "if $n > 1$" is read as $n \ge 1$, as the definition of $A_2$ requires.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.secondOrderBiSeq`, a definition declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-bi-seq).

## First values of the two-sided sequence

For all integers $p$, $r$, $s$, the two-sided
sequence $(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ for $p$ with initial values $r$ and $s$ satisfies
$A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$, $A^{(r,s)}_2 = ps + r$ and $A^{(r,s)}_{-1} = s - pr$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.secondOrderBiSeq_small`, a theorem declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-bi-seq-small).

## First initial value of the two-sided sequence

For all integers $p$, $r$, $s$, the
two-sided sequence $(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ for $p$ with initial values $r$ and $s$
satisfies $A^{(r,s)}_0 = r$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.secondOrderBiSeq_zero`, a theorem declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-bi-seq-zero).

## Second initial value of the two-sided sequence

For all integers $p$, $r$, $s$, the
two-sided sequence $(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ for $p$ with initial values $r$ and $s$
satisfies $A^{(r,s)}_1 = s$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.secondOrderBiSeq_one`, a theorem declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-bi-seq-one).

## The two-sided sequence satisfies its recurrence at every index

Let $p$, $r$, $s$ be
integers and $(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ the two-sided sequence for $p$ with initial values
$A^{(r,s)}_0 = r$ and $A^{(r,s)}_1 = s$. Then
$A^{(r,s)}_{n+2} = pA^{(r,s)}_{n+1} + A^{(r,s)}_n$ for every integer $n$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.secondOrderBiSeq_add_two`, a theorem declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-bi-seq-add-two).

## The quantity $M(r, s)$ for the recurrence $A_{n+1} = pA_n + A_{n-1}$

For integers $a$,
$b$, $p$, $r$, $s$, $M(r, s) = \frac{br^2 + bs^2 - apr^2 + 2ars}{s^2 - prs - r^2}$, a rational
number, with the convention that a fraction with denominator $0$ is $0$.

When $s \ne 0$ and $s^2 - prs - r^2 \ne 0$, write $k = A(r/s)$, where
$A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$ is the generating function of the sequence with
$A_0 = a$, $A_1 = b$ and $A_{n+1} = pA_n + A_{n-1}$; then
$M(r, s)^2 = (kp + b - ap)^2 - 4k(a - k)$, that is,
$M(r, s) = \pm\sqrt{(kp + b - ap)^2 - 4k(a - k)}$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Section 2 (before Lemma 8).

Formalized by `MetaMathlibExt.secondOrderMValue`, a definition declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-mvalue).

## Value of $M$ at $(0, 1)$

For all integers $a$, $b$, $p$, the quantity
$M(r, s) = \frac{br^2 + bs^2 - apr^2 + 2ars}{s^2 - prs - r^2}$ satisfies $M(0, 1) = b$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Section 2.

Formalized by `MetaMathlibExt.secondOrderMValue_zero_one`, a theorem declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-mvalue-zero-one).

## Family generated by a rational number

Let $p$ be an integer and $x_0$ a rational number,
written $x_0 = r/s$ in lowest terms with $s > 0$, and let $(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ be
the two-sided sequence with $A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and
$A^{(r,s)}_{n+1} = pA^{(r,s)}_n + A^{(r,s)}_{n-1}$. A rational number $x$ belongs to the family
generated by $x_0$ when there is an integer $n$ with $A^{(r,s)}_{n+1} \ne 0$ and
$x = A^{(r,s)}_n / A^{(r,s)}_{n+1}$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1 and Remark 7(ii).

Formalized by `MetaMathlibExt.IsInSecondOrderFamily`, a definition declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-in-second-order-family).

## Every rational number lies in its own family

For every integer $p$ and every rational
number $x_0$, $x_0$ belongs to the family generated by $x_0$ for $p$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1.

Formalized by `MetaMathlibExt.isInSecondOrderFamily_self`, a theorem declared in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#is-in-second-order-family-self).

## Integer values propagate along a family

Let $a, b, p$ be integers with $p \ne 0$, let
$A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$ for rational $x$, and for integers $r, s$ let
$A^{(r,s)}$ be the two-sided integer sequence with $A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and
$A^{(r,s)}_{n+2} = pA^{(r,s)}_{n+1} + A^{(r,s)}_n$ for all integers $n$. If $r$ and $s$ are
coprime integers with $s \ne 0$ and $A(r/s)$ is an integer, then
$A(A^{(r,s)}_n / A^{(r,s)}_{n+1})$ is an integer for every integer $n$ with
$A^{(r,s)}_{n+1} \ne 0$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 1 (`jis-2025-25.8.3-thm-1`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_family_integer` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-family-integer).

## Two families of integer values

Let $a, b, p$ be integers with $p \ne 0$, let
$A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$ for rational $x$, and for integers $r, s$ let
$A^{(r,s)}$ be the two-sided integer sequence with $A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and
$A^{(r,s)}_{n+2} = pA^{(r,s)}_{n+1} + A^{(r,s)}_n$ for all integers $n$. Then
$A(A^{(0,1)}_n / A^{(0,1)}_{n+1})$ is an integer for every integer $n \ne -1$, and
$A(A^{(-b,a)}_n / A^{(-b,a)}_{n+1})$ is an integer for every integer $n$ with
$A^{(-b,a)}_{n+1} \ne 0$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 2 (`jis-2025-25.8.3-thm-2`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_trivial_families_integer` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 189](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L189). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-trivial-families).

## Integrality criterion at a rational point

Let $a, b, p$ be integers with $p \ne 0$ and let
$A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$ for rational $x$. Let $r, s$ be coprime integers
with $s \ne 0$ and put $D = s^2 - prs - r^2$. Then $A(r/s)$ is an integer if and only if
$b \equiv -art \pmod{D}$ for every integer $t$ with $st \equiv 1 \pmod{D}$.

Since $s$ is invertible modulo $D$, this is the congruence $b \equiv -ars^{-1} \pmod{|D|}$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Lemma 4 (`jis-2025-25.8.3-lem-4`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_integer_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-integer-iff).

## Neighbours of an integer value

Let $a, b, p$ be integers with $p \ne 0$ and let
$A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$ for rational $x$. If $r, s$ are coprime integers
with $r \ne 0$, $s \ne 0$ and $r + ps \ne 0$, and $A(r/s)$ is an integer, then $A(s/(r + ps))$
and $A((s - pr)/r)$ are integers.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Lemma 6 (`jis-2025-25.8.3-lem-6`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_neighbors_integer` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-neighbors-integer).

## Relations between values of $M$ at neighbouring pairs

Let $a$, $b$, $p$ be integers with
$p \ne 0$, and for integers $r$, $s$ let
$M(r, s) = \frac{br^2 + bs^2 - apr^2 + 2ars}{s^2 - prs - r^2}$. Then for all integers $r$, $s$
that are not both zero, $M(s - pr, r) + (p^2 + 2)M(r, s) + M(s, r + ps) = 0$ and
$M(r, s)^2 + (p^2 + 2)M(r, s)M(s, r + ps) + M(s, r + ps)^2 = abp^3 + (a^2 - b^2)p^2$.

The source assumes $r \ne 0$, $s \ne 0$ and $r + ps \ne 0$; here only $(r, s) \ne (0, 0)$ is
assumed. Since $p \ne 0$, the three denominators equal $\pm(s^2 - prs - r^2)$, which is nonzero.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Lemma 8 (`jis-2025-25.8.3-lem-8`).

Stated but not proved: `MetaMathlibExt.secondOrderMValue_relations` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-mvalue-relations).

## A small value of $M$ in the family of $r/s$ when $abp + a^2 - b^2 < 0$

Let $a, b, p$ be
integers with $p \ne 0$ and $abp + a^2 - b^2 < 0$. Let $A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$
for rational $x$, and for integers $u, v$ let
$M(u, v) = \frac{bu^2 + bv^2 - apu^2 + 2auv}{v^2 - puv - u^2}$, where in both a fraction with
denominator $0$ is read as $0$. Let $r, s$ be coprime integers with $s \ne 0$ such that $A(r/s)$
is an integer, and let $(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ be the two-sided sequence with
$A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and $A^{(r,s)}_{n+1} = pA^{(r,s)}_n + A^{(r,s)}_{n-1}$ for
every integer $n$. If $A^{(r,s)}_n \ne 0$ for every integer $n$, then there is an integer $n$
with $|M(A^{(r,s)}_n, A^{(r,s)}_{n+1})| \le \sqrt{b^2 - a^2 - abp}$.

The hypothesis that no term vanishes is the paper's assumption before Lemma 8 ("we can assume
that the conditions $r \ne 0, s \ne 0, r + ps \ne 0$ automatically hold"). Without it the paper's
claim fails: for $(a, b, p) = (-1, 8, -1)$ and $x = 0$, the members $A_n/A_{n+1}$ of the family
$A^{(0,1)}$ with $A_{n+1} \ne 0$ have $\min |M| = 8 > \sqrt{55}$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Lemma 9 (`jis-2025-25.8.3-lem-9`).

Stated but not proved: `MetaMathlibExt.exists_small_secondOrderMValue_of_neg` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#exists-small-second-order-mvalue-of-neg).

## A small value of $M$ in the family of $r/s$ when $abp + a^2 - b^2 \ge 0$

Let $a, b, p$
be integers with $p \ne 0$ and $abp + a^2 - b^2 \ge 0$. Let
$A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$ for rational $x$, and for integers $u, v$ let
$M(u, v) = \frac{bu^2 + bv^2 - apu^2 + 2auv}{v^2 - puv - u^2}$, where in both a fraction with
denominator $0$ is read as $0$. Let $r, s$ be coprime integers with $s \ne 0$ such that $A(r/s)$
is an integer, and let $(A^{(r,s)}_n)_{n \in \mathbb{Z}}$ be the two-sided sequence with
$A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and $A^{(r,s)}_{n+1} = pA^{(r,s)}_n + A^{(r,s)}_{n-1}$ for
every integer $n$. If $A^{(r,s)}_n \ne 0$ for every integer $n$, then there is an integer $n$
with $|M(A^{(r,s)}_n, A^{(r,s)}_{n+1})| \le \sqrt{(abp^3 + (a^2 - b^2)p^2)/(p^2 + 4)}$.

The hypothesis that no term vanishes is the paper's assumption before Lemma 8. Without it the
paper's claim fails: for $(a, b, p) = (-3, -8, 5)$ and $x = 0$, the members $A_n/A_{n+1}$ of the
family $A^{(0,1)}$ with $A_{n+1} \ne 0$ have $\min |M| = 8$, while
$(abp^3 + (a^2 - b^2)p^2)/(p^2 + 4) = 1625/29 < 64$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Lemma 10 (`jis-2025-25.8.3-lem-10`).

Stated but not proved: `MetaMathlibExt.exists_small_secondOrderMValue_of_nonneg` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#exists-small-second-order-mvalue-of-nonn).

## Algorithm for integer values of a second-order generating function

Let $a, b, p$ be
integers with $p \ne 0$ and $(a, b) \ne (0, 0)$, let $A(x) = \frac{a(1 - px) + bx}{1 - px - x^2}$
for rational $x$, and for integers $r, s$ let $A^{(r,s)}$ be the two-sided integer sequence with
$A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and $A^{(r,s)}_{n+2} = pA^{(r,s)}_{n+1} + A^{(r,s)}_n$ for all
integers $n$. Put $E = abp^3 + (a^2 - b^2)p^2$, and let $B = E/(p^2 + 4)$ if $E \ge 0$ and
$B = -abp + b^2 - a^2$ if $E < 0$. (Soundness) If $M$ and $k$ are integers with $k \ne 0$ and
$M^2 = (kp - ap + b)^2 - 4k(a - k)$, then $A(x)$ is an integer for both
$x = (ap - kp - b + M)/(2k)$ and $x = (ap - kp - b - M)/(2k)$. (Completeness) If $x$ is a
rational number for which $A(x)$ is an integer, then at least one of the following holds: there
is an integer $n$ with $A^{(0,1)}_{n+1} \ne 0$ and $x = A^{(0,1)}_n / A^{(0,1)}_{n+1}$; there is
an integer $n$ with $A^{(-b,a)}_{n+1} \ne 0$ and $x = A^{(-b,a)}_n / A^{(-b,a)}_{n+1}$; or there
are integers $M, N, k$ with $M^2 \le B$, $M^2 + (p^2 + 2)MN + N^2 = E$, $k \ne 0$ and
$M^2 = (kp - ap + b)^2 - 4k(a - k)$, and a rational number
$x' \in \{(ap - kp - b + M)/(2k), (ap - kp - b - M)/(2k)\}$ such that $x$ lies in the family of
$x'$: writing $x' = u/v$ in lowest terms with $v > 0$, there is an integer $n$ with
$A^{(u,v)}_{n+1} \ne 0$ and $x = A^{(u,v)}_n / A^{(u,v)}_{n+1}$.

The bound $M^2 \le B$ is the condition $|M| \le \sqrt{B}$ of the source.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Theorem 3 (`jis-2025-25.8.3-thm-3`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_algorithm` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 283](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L283). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-algorithm).

## Rationals where $x/(1 - px - x^2)$ is an integer

Let $p \ne 0$ be an integer, let
$G(x) = \frac{x}{1 - px - x^2}$ for rational $x$, and let $A^{(0,1)}$ be the two-sided integer
sequence with $A^{(0,1)}_0 = 0$, $A^{(0,1)}_1 = 1$ and
$A^{(0,1)}_{n+2} = pA^{(0,1)}_{n+1} + A^{(0,1)}_n$ for all integers $n$. Then the set of rational
numbers $x$ for which $G(x)$ is an integer is
$\{A^{(0,1)}_n / A^{(0,1)}_{n+1} : n \in \mathbb{Z},\ n \ne -1\}$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Corollary 13 (`jis-2025-25.8.3-cor-13`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_zero_one_integer_set` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-zero-one-integer).

## Integer values of $x/(1 - px - x^2)$ come from Lucas ratios

Let $p \ne 0$ be an integer,
let $(U_n)_{n \ge 0}$ be the Lucas sequence $U(p, -1)$, so $U_0 = 0$, $U_1 = 1$ and
$U_{n+2} = pU_{n+1} + U_n$, and let $G(x) = \frac{x}{1 - px - x^2}$ for rational $x$. Then
$G(U_n/U_{n+1})$ is an integer for every natural number $n$; and if $G(x) = k$ for a rational
number $x$ and an integer $k$, then $G(U_n/U_{n+1}) = k$ for some natural number $n$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Corollary 14 (`jis-2025-25.8.3-cor-14`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_lucasU` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-lucas-u).

## Integer values of $(1 - px + x)/(1 - px - x^2)$

Let $p \ne 0$ be an integer, let
$A(x) = \frac{1 - px + x}{1 - px - x^2}$ for rational $x$, and for integers $r, s$ let $A^{(r,s)}$
be the two-sided integer sequence with $A^{(r,s)}_0 = r$, $A^{(r,s)}_1 = s$ and
$A^{(r,s)}_{n+2} = pA^{(r,s)}_{n+1} + A^{(r,s)}_n$ for all integers $n$. If $x$ is a rational
number for which $A(x)$ is an integer, then there is an integer $n$ with $A^{(0,1)}_{n+1} \ne 0$
and $x = A^{(0,1)}_n / A^{(0,1)}_{n+1}$, or there is an integer $n$ with $A^{(-1,1)}_{n+1} \ne 0$
and $x = A^{(-1,1)}_n / A^{(-1,1)}_{n+1}$.

## Sources

- Luu Ba Thang and Nguyen Duy Nguyen, *Integer Values of Generating Functions for a Type of Second-Order Linear Recurrence Sequence*, Journal of Integer Sequences 28 (2025), Article 25.8.3, Corollary 15 (`jis-2025-25.8.3-cor-15`).

Stated but not proved: `MetaMathlibExt.secondOrderGenValue_one_one_families` is written with `theorem_wanted` in [WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/SecondOrderGenFunIntegerValuesWanted.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html#second-order-gen-value-one-one-families).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer values of recurrence generating functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/integer-values-of-recurrence-generating-function)
