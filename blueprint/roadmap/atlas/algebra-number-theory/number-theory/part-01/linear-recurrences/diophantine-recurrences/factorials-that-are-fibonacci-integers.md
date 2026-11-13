---
declaration: section
origin: cited
lean: MetaMathlibExt.factorial_mem_fibonacciIntegers_iff, MetaMathlibExt.primitive_prime_dvd_fib_modEq_one_or_neg_one, MetaMathlibExt.fibEntryPoint, MetaMathlibExt.fibEntryPoint_two, MetaMathlibExt.fibEntryPoint_five, MetaMathlibExt.fibCyclotomicValue, MetaMathlibExt.fibCyclotomicValue_two, MetaMathlibExt.fibPrimitivePart
statement: formalized
---

# Factorials that are Fibonacci integers

11 results, 7 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html).

## The largest factorial that is a Fibonacci integer is $36!$

For every natural number $n$,
the factorial $n!$ lies in the subgroup of the multiplicative group $\mathbb{Q}^\times$ generated
by the Fibonacci numbers $F_m$ with $m \ge 1$ if and only if $n \le 36$.

Calling a positive integer in this subgroup a Fibonacci integer, the statement records both the
paper's claim that $36!$ is a Fibonacci integer and that no $n!$ with $n \ge 37$ is.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Theorem 1.

Stated but not proved: `MetaMathlibExt.factorial_mem_fibonacciIntegers_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#factorial-mem-fibonacci-integers-iff).

## Carmichael's congruence for primitive prime divisors of Fibonacci numbers

Let $F_n$
denote the $n$-th Fibonacci number. For every natural number $m > 12$, every primitive prime
divisor $p$ of $F_m$ (a prime $p$ that divides $F_m$ but divides no $F_n$ with $0 < n < m$)
satisfies $p \equiv \pm 1 \pmod{m}$, that is, $p \equiv 1 \pmod{m}$ or $p + 1 \equiv 0 \pmod{m}$.

This is the congruence half of Carmichael's theorem; the existence of a primitive prime divisor
of $F_m$ for $m > 12$ is a separate statement.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Theorem 2 (Primitive Divisor Theorem, quoting R. D. Carmichael).

Stated but not proved: `MetaMathlibExt.primitive_prime_dvd_fib_modEq_one_or_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#primitive-prime-dvd-fib-mod-eq-one-or-ne).

## Entry point in the Fibonacci sequence

The entry point (rank of apparition) $z(k)$ of a
natural number $k$ is the least $m > 0$ such that $k$ divides the Fibonacci number $F_m$, and
$z(k) = 0$ if there is no such $m$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Section 2.

Formalized by `MetaMathlibExt.fibEntryPoint`, a definition declared in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#fib-entry-point).

## Fibonacci entry point of $2$

The least $m > 0$ such that $2$ divides the Fibonacci number
$F_m$ is $3$, that is, the Fibonacci entry point of $2$ is $z(2) = 3$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Section 2 (`6 = 2 z(2)`).

Formalized by `MetaMathlibExt.fibEntryPoint_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#fib-entry-point-two).

## Fibonacci entry point of $5$

The least $m > 0$ such that $5$ divides the Fibonacci number
$F_m$ is $5$, that is, the Fibonacci entry point of $5$ is $z(5) = 5$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Section 2 (the exceptional index `m = 5`).

Formalized by `MetaMathlibExt.fibEntryPoint_five`, a theorem declared in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#fib-entry-point-five).

## Fibonacci cyclotomic values

For a natural number $m$, $\Phi_m$ is the rational number
$\prod_{d \mid m} F_{m/d}^{\mu(d)}$, where $d$ runs over the positive divisors of $m$, $F_k$ is the
$k$-th Fibonacci number and $\mu$ is the Möbius function. For $m > 1$ this is the value
$\Phi_m(\alpha, \beta)$ of the homogenized $m$-th cyclotomic polynomial at the roots
$\alpha, \beta$ of $x^2 - x - 1$.

At $m = 1$ the formula gives $1$, not $\Phi_1(\alpha, \beta) = \alpha - \beta = \sqrt{5}$, and
$m = 0$ is treated as having no divisors, so $\Phi_0 = 1$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Section 2.

Formalized by `MetaMathlibExt.fibCyclotomicValue`, a definition declared in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#fib-cyclotomic-value).

## Fibonacci cyclotomic value at $2$

The Fibonacci cyclotomic value
$\Phi_2 = \prod_{d \mid 2} F_{2/d}^{\mu(d)} = F_2 / F_1$, where $F_k$ is the $k$-th Fibonacci number
and $\mu$ is the Möbius function, equals $1$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Section 2, Equation (1).

Formalized by `MetaMathlibExt.fibCyclotomicValue_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#fib-cyclotomic-value-two).

## Primitive part of a Fibonacci number

For a natural number $m$, the primitive part of the
Fibonacci number $F_m$ is $\Psi_m = \prod_p p^{a_p}$, where the product runs over the primes $p$
dividing $F_m$ whose Fibonacci entry point is $z(p) = m$, and $a_p$ is the exponent of $p$ in
$F_m$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Section 2.

Formalized by `MetaMathlibExt.fibPrimitivePart`, a definition declared in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#fib-primitive-part).

## Primitive part of $F_6$

The primitive part of the Fibonacci number $F_6$ is $\Psi_6 = 1$:
$F_6 = 8 = 2^3$ and the Fibonacci entry point of $2$ is $z(2) = 3 \ne 6$, so $F_6$ has no prime
factor $p$ with $z(p) = 6$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Section 2.

Formalized by `MetaMathlibExt.fibPrimitivePart_six`, a theorem declared in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#fib-primitive-part-six).

## Prime factors of the primitive parts of the denominator indices

Let $I$ and $J$ be finite
multisets of natural numbers, every element of which is at least $3$ and different from $6$ and
$12$, such that no element of $I$ equals an element of $J$ and
$\prod_{a \in I} \Phi_a / \prod_{b \in J} \Phi_b$ is a natural number, where $\Phi_m$ is the
$m$-th Fibonacci cyclotomic value. Let $\Psi_m$ be the primitive part of the Fibonacci number
$F_m$ and $z(p)$ the Fibonacci entry point of $p$. Then there is a finite multiset $e$ of pairs
$(p, k)$ of natural numbers such that the multiset of first coordinates of $e$ is the multiset of
prime factors of $\prod_{b \in J} \Psi_b$, counted with multiplicity, and the multiset of the
numbers $p^k z(p)$ for $(p, k) \in e$ is a sub-multiset of $I$.

In other words, there is an injection from the prime factors $p_1, \dots, p_r$ of
$\prod_{b \in J} \Psi_b$, counted with multiplicity, into $I$ that sends each $p_l$ to an element
of the form $p_l^{k_l} z(p_l)$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Lemma 1.

Stated but not proved: `MetaMathlibExt.exists_injection_primeFactors_fibPrimitivePart` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#exists-injection-prime-factors-fib-primi).

## Bound on denominator indices of $p$-adic valuation one

Let $n \ge 37$ and let $I$ and $J$
be finite multisets of natural numbers, every element of which is at least $3$ and different from
$6$ and $12$, such that no element of $I$ equals an element of $J$ and
$n! = \prod_{a \in I} \Phi_a / \prod_{b \in J} \Phi_b$, where $\Phi_m$ is the $m$-th Fibonacci
cyclotomic value. Let $p$ be a prime whose Fibonacci entry point $z(p)$ exceeds $12$, and let
$N_p$ be the number of elements $m$ of $J$, counted with multiplicity, such that the $p$-adic
valuation of $\Phi_m / \Psi_m$ is $1$, where $\Psi_m$ is the primitive part of the Fibonacci
number $F_m$. Then $N_p < \frac{2n}{z(p)\, p\, (p - 2)}$.

## Sources

- Florian Luca, *`F_4 F_5^6 F_7 F_8^4 F_9 F_{10}^2 F_{12}^5 F_{14} F_{15}^{-1} F_{18} F_{24} F_{30} = 36!`*, INTEGERS 24 (2024), Article A72, Lemma 2.

Stated but not proved: `MetaMathlibExt.card_padicValRat_fibDelta_eq_one_lt` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/FibonacciIntegerFactorialWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html#card-padic-val-rat-fib-delta-eq-one-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Factorials that are Fibonacci integers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/diophantine-recurrences/factorials-that-are-fibonacci-integers)
