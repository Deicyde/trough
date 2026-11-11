---
declaration: section
origin: cited
lean: MetaMathlibExt.generalizedBiPeriodicFibonacci_period_dvd_general, MetaMathlibExt.generalizedBiPeriodicFibonacci_period_dvd, MetaMathlibExt.generalized_biperiodic_fibonacci_zero_indices_general, MetaMathlibExt.generalized_biperiodic_fibonacci_zero_indices
statement: formalized
proof: formalized
---

# Bi-periodic Fibonacci sequences modulo primes

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/bi-periodic-fibonacci-sequences-modulo-primes/index.html).

## Period of a generalized bi-periodic Fibonacci sequence modulo a prime, given the roots

Let
$p$ be an odd prime and let $a, b, c, d \in \mathbb{Z}/p\mathbb{Z}$ with $a \ne 0$, $c \ne 0$,
$d \ne 0$, and $a \ne b$ or $c \ne d$. Let $F : \mathbb{N} \to \mathbb{Z}/p\mathbb{Z}$ satisfy
$F_0 = 0$, $F_1 = 1$ and, for every $n \ge 2$, $F_n = a F_{n-1} + c F_{n-2}$ if $n$ is even and
$F_n = b F_{n-1} + d F_{n-2}$ if $n$ is odd. Put $A = ab + c + d$ and $\Delta = A^2 - 4cd$, and
let $\alpha, \beta \in \mathbb{Z}/p\mathbb{Z}$ satisfy $\alpha + \beta = A$ and
$\alpha \beta = cd$. Let $k$ be the least positive period of $F$: $k > 0$, $F_{n+k} = F_n$ for
all $n$, and $k \le m$ for every $m > 0$ with $F_{n+m} = F_n$ for all $n$. If $\Delta \ne 0$,
then $k$ divides $2(p - 1)$, and if moreover $\alpha$ and $\beta$ are nonzero squares in
$\mathbb{Z}/p\mathbb{Z}$, then $k$ divides $p - 1$.

Since $\Delta = (\alpha - \beta)^2$, no hypothesis that $\Delta$ is a square is needed.

Formalized by `MetaMathlibExt.generalizedBiPeriodicFibonacci_period_dvd_general`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciPeriod.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciPeriod.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/bi-periodic-fibonacci-sequences-modulo-primes/index.html#generalized-bi-periodic-fibonacci-period).

## Period of a generalized bi-periodic Fibonacci sequence modulo a prime

Let $p$ be an odd
prime and let $a, b, c, d \in \mathbb{Z}/p\mathbb{Z}$ with $a \ne 0$, $c \ne 0$, $d \ne 0$, and
$a \ne b$ or $c \ne d$. Let $F : \mathbb{N} \to \mathbb{Z}/p\mathbb{Z}$ satisfy $F_0 = 0$,
$F_1 = 1$ and, for every $n \ge 2$, $F_n = a F_{n-1} + c F_{n-2}$ if $n$ is even and
$F_n = b F_{n-1} + d F_{n-2}$ if $n$ is odd. Put $A = ab + c + d$ and $\Delta = A^2 - 4cd$, and
let $\alpha, \beta \in \mathbb{Z}/p\mathbb{Z}$ satisfy $\alpha + \beta = A$ and
$\alpha \beta = cd$. Let $k$ be the least positive period of $F$: $k > 0$, $F_{n+k} = F_n$ for
all $n$, and $k \le m$ for every $m > 0$ with $F_{n+m} = F_n$ for all $n$. If $\Delta$ is a
nonzero square in $\mathbb{Z}/p\mathbb{Z}$, then $k$ divides $2(p - 1)$, and if moreover
$\alpha$ and $\beta$ are nonzero squares in $\mathbb{Z}/p\mathbb{Z}$, then $k$ divides $p - 1$.

## Sources

- Hacène Belbachir and Celia Salhi, "The Generalized Bi-Periodic Fibonacci Sequence Modulo m," Journal of Integer Sequences 24 (2021), Article 21.9.4, Theorem, lines 225–226, <https://cs.uwaterloo.ca/journals/JIS/VOL24/Salhi/salhi4.tex>. It follows from `generalizedBiPeriodicFibonacci_period_dvd_general`, which drops the unused `IsSquare Δ`.

Formalized by `MetaMathlibExt.generalizedBiPeriodicFibonacci_period_dvd`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciPeriod.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciPeriod.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/bi-periodic-fibonacci-sequences-modulo-primes/index.html#generalized-bi-periodic-fibonacci-period-2).

## Zero indices of a generalized bi-periodic Fibonacci sequence with $c = d$

Let
$a, b, c, d$ be natural numbers with $c = d$, and let $m \ge 2$ be a natural number coprime to $a$
and to $c$. Let $(F_n)_{n \ge 0}$ be a sequence of natural numbers with $F_0 = 0$, $F_1 = 1$,
$F_{2n+2} = a F_{2n+1} + c F_{2n}$ and $F_{2n+3} = b F_{2n+2} + d F_{2n+1}$ for all $n \ge 0$.
Then there is an integer $l > 0$ such that, for every $n \ge 0$, $m$ divides $F_n$ if and only
if $l$ divides $n$, and $l \le r$ for every $r > 0$ such that $m$ divides $F_r$.

Formalized by `MetaMathlibExt.generalized_biperiodic_fibonacci_zero_indices_general`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciZeroIndices.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciZeroIndices.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/bi-periodic-fibonacci-sequences-modulo-primes/index.html#generalized-biperiodic-fibonacci-zero-in).

## Belbachir–Salhi theorem on zero indices of generalized bi-periodic Fibonacci sequences

Let $a, b, c, d$ be positive natural numbers with $c = d$, and let $m \ge 2$ be a natural number
coprime to $a$, to $c$ and to $d$. Let $(F_n)_{n \ge 0}$ be a sequence of natural numbers with
$F_0 = 0$, $F_1 = 1$, $F_{2n+2} = a F_{2n+1} + c F_{2n}$ and
$F_{2n+3} = b F_{2n+2} + d F_{2n+1}$ for all $n \ge 0$. Then there is a natural number $l > 0$
such that, for every $n \ge 0$, $m$ divides $F_n$ if and only if $l$ divides $n$, and
$l \le r$ for every $r > 0$ such that $m$ divides $F_r$.

The recurrence is $F_n = a F_{n-1} + c F_{n-2}$ for even $n \ge 2$ and
$F_n = b F_{n-1} + d F_{n-2}$ for odd $n \ge 3$. The conditions $c = d$ and $\gcd(a, m) = 1$ are
the standing assumptions of the source's section, and coprimality of $c$ and $d$ with $m$ is its
global hypothesis on the modulus; the positivity of $a, b, c, d$ and the coprimality of $d$ with
$m$ are not needed for the conclusion.

## Sources

- Hacène Belbachir and Celia Salhi, "The Generalized Bi-Periodic Fibonacci Sequence Modulo m," Journal of Integer Sequences 24 (2021), Article 21.9.4, Theorem, lines 445–448, https://cs.uwaterloo.ca/journals/JIS/VOL24/Salhi/salhi4.tex

Formalized by `MetaMathlibExt.generalized_biperiodic_fibonacci_zero_indices`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciZeroIndices.lean, line 458](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/GeneralizedBiPeriodicFibonacciZeroIndices.lean#L458). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/bi-periodic-fibonacci-sequences-modulo-primes/index.html#generalized-biperiodic-fibonacci-zero-in-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bi-periodic Fibonacci sequences modulo primes](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/bi-periodic-fibonacci-sequences-modulo-primes/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/bi-periodic-fibonacci-sequences-modulo-primes)
