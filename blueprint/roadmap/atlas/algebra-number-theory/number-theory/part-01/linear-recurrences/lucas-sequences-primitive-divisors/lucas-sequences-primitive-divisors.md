---
declaration: section
origin: cited
lean: MetaMathlibExt.fib_prime_dvd_fib_of_legendre_sub, MetaMathlibExt.lengyel_fibonacci_five_adic
statement: formalized
proof: formalized
---

# Lucas sequences and primitive divisors: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/index.html).

General Lucas sequences U_n, V_n, Lucas pairs, divisibility, Bang–Zsigmondy and primitive-divisor theorems, Fibonacci prime divisibility.

## Fibonacci prime divisibility

Let $p$ be a prime with $p > 2$ and $p \ne 5$, and let
$\left(\frac{5}{p}\right)$ be the Legendre symbol of $5$ modulo $p$. Then $p$ divides the
Fibonacci number $F_{p-1}$ if $\left(\frac{5}{p}\right) = 1$, and $p$ divides the Fibonacci
number $F_{p+1}$ otherwise. Since $\left(\frac{5}{p}\right) = \pm 1$, this says that $p$ divides
$F_{p - \left(\frac{5}{p}\right)}$.

## Sources

- Phakhinkon Phunphayap and Prapanpong Pongsriiam, "Explicit Formulas for the p-adic Valuations of Fibonomial Coefficients," Journal of Integer Sequences 21 (2018), Article 18.3.1, Lemma, item (i), lines 166–169, https://cs.uwaterloo.ca/journals/JIS/VOL21/Pongsriiam/pong12.tex

Formalized by `MetaMathlibExt.fib_prime_dvd_fib_of_legendre_sub`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/FibonacciPrimeDivisibility.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/FibonacciPrimeDivisibility.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/index.html#fib-prime-dvd-fib-of-legendre-sub).

## The $5$-adic valuation of Fibonacci numbers

Writing $F_n$ for the $n$-th Fibonacci number
and $v_5$ for the $5$-adic valuation, $v_5(F_n) = v_5(n)$ for every integer $n \ge 1$.

## Sources

- Fatehizadeh–Yaqubi, Lemma `Leg1`, citing Lengyel (1995). The source prints `n ≥ 0`, but its p-adic valuation is defined for positive integers, so this formalizes the audited `1 ≤ n` restriction. Only the 5-adic clause is formalized; the source's separate 2-adic and 3-adic clauses are out of scope.

Formalized by `MetaMathlibExt.lengyel_fibonacci_five_adic`, a theorem declared in [MathlibExt/NumberTheory/Padics/FibonacciFiveAdicValuation.lean, line 268](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/FibonacciFiveAdicValuation.lean#L268). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/index.html#lengyel-fibonacci-five-adic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lucas sequences and primitive divisors](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/lucas-sequences-primitive-divisors)
