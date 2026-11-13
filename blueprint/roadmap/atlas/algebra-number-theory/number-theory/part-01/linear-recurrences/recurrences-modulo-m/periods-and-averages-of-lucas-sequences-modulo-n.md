---
declaration: section
origin: cited
lean: MetaMathlibExt.lucasUPeriod, MetaMathlibExt.lucasURestrictedPeriod, MetaMathlibExt.lucasPeriodSet, MetaMathlibExt.lucasAverageSet, MetaMathlibExt.lucasAllAveragesIntegral, MetaMathlibExt.lucasUPeriod_one, MetaMathlibExt.lucasUPeriod_fibonacciLucasParams_two, MetaMathlibExt.lucasURestrictedPeriod_one
statement: formalized
---

# Periods and averages of Lucas sequences modulo n

70 results, 21 proved and 49 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html).

## Period of a Lucas sequence modulo $m$

For a Lucas sequence $U = U(P, Q)$ and a natural
number $m$, the least period $\pi_U(m)$ of $U$ modulo $m$ is the minimal period of the pair
$(0, 1)$ under the map $(x, y) \mapsto (y, P y - Q x)$ on pairs of residues modulo $m$, that is,
the least $r > 0$ with $U_r \equiv 0 \pmod m$ and $U_{r+1} \equiv 1 \pmod m$, and $0$ if there
is no such $r$.

For $m > 0$, $\pi_U(m) = 0$ exactly when $U$ is not purely periodic modulo $m$, that is, when
$\gcd(m, Q) > 1$. For $m = 0$ the residues are integers and the congruences are equalities; this
value has no meaning in the paper (for the Fibonacci sequence it is $0$).

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Section 1, equation (1.11).

Formalized by `MetaMathlibExt.lucasUPeriod`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod).

## Restricted period of a Lucas sequence modulo $m$

For a Lucas sequence $U = U(P, Q)$ and
a natural number $m$, the least restricted period $\rho_U(m)$ of $U$ modulo $m$ is the least
$s > 0$ such that $m \mid U_s$ and $U_{s+1}$ is coprime to $m$, and $0$ if there is no such $s$.

In the paper's terms, $U_{s+1} \equiv M \pmod m$ for a multiplier $M$ coprime to $m$; for
$s = \rho_U(m)$ this $U_{s+1}$ is the multiplier $M_U(m)$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Section 1, equations (1.10) and (1.12).

Formalized by `MetaMathlibExt.lucasURestrictedPeriod`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-urestricted-period).

## Moduli divisible by their Lucas period

For the Lucas sequence $U$ with integer
parameters $P$ and $Q \ne 0$ ($U_0 = 0$, $U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$), $S(U)$ is
the set of positive integers $n$ coprime to $Q$ such that the period $\pi_U(n)$ of $U$ modulo
$n$ divides $n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.2.

Formalized by `MetaMathlibExt.lucasPeriodSet`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-set).

## Average set of a Lucas sequence

Let $U$ be the Lucas sequence with parameters $P$ and
$Q \ne 0$, given by $U_0 = 0$, $U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$, and let $S(U)$ be the
set of positive integers $n$ coprime to $Q$ such that the period $\pi_U(n)$ of $U$ modulo $n$
divides $n$. The average set $S'(U)$ is the set of $n \in S(U)$ with $n \mid U_1 + \dots + U_n$,
that is, those $n \in S(U)$ for which the average $(U_1 + \dots + U_n)/n$ is an integer.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.2.

Formalized by `MetaMathlibExt.lucasAverageSet`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-average-set).

## Integral averages of all recurrences

For integers $P$ and $Q \ne 0$ and a natural number
$n$, the property that $n$ has integral averages means that every integer sequence
$(w_k)_{k \ge 0}$ with $w_{k+2} = P w_{k+1} - Q w_k$ for all $k$ satisfies
$n \mid w_1 + \dots + w_n$; for $n > 0$ this says that the average
$A_W(n) = (w_1 + \dots + w_n)/n$ is an integer.

In the paper's notation $a = P$ and $b = -Q$, so the recurrence reads
$w_{k+2} = a w_{k+1} + b w_k$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Section 2 (definition of `B_W(n)` and `A_W(n)`).

Formalized by `MetaMathlibExt.lucasAllAveragesIntegral`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-all-averages-integral).

## Period of a Lucas sequence modulo 1

For every Lucas sequence $U = U(P, Q)$, the least
period $\pi_U(1)$ of $U$ modulo $1$ equals $1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.4 (ix).

Formalized by `MetaMathlibExt.lucasUPeriod_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-one).

## Period of the Fibonacci sequence modulo 2

The Fibonacci sequence, that is, the Lucas
sequence with parameters $(P, Q) = (1, -1)$, has period $3$ modulo $2$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.4 (i) (`π_U(2) = 3` when `2 ∤ bD`).

Formalized by `MetaMathlibExt.lucasUPeriod_fibonacciLucasParams_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-fibonacci-lucas-params-two).

## Restricted period of a Lucas sequence modulo 1

For every Lucas sequence $U = U(P, Q)$,
the least restricted period $\rho_U(1)$ of $U$ modulo $1$ equals $1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.4 (ix).

Formalized by `MetaMathlibExt.lucasURestrictedPeriod_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-urestricted-period-one).

## Restricted period of the Fibonacci sequence modulo 2

The least restricted period
modulo $2$ of the Fibonacci sequence $F = U(1, -1)$ equals $3$ (note $F_3 = 2$).

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, equation (1.12).

Formalized by `MetaMathlibExt.lucasURestrictedPeriod_fibonacciLucasParams_two`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-urestricted-period-fibonacci-lucas).

## The Lucas period set contains $1$

For all integers $P, Q$ with $Q \ne 0$, the number $1$
lies in the Lucas period set $S(U)$ of $U = U(P, Q)$: the set of positive integers $n$ coprime to
$Q$ whose period $\pi_U(n)$ modulo $n$ divides $n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.2.

Formalized by `MetaMathlibExt.one_mem_lucasPeriodSet`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#one-mem-lucas-period-set).

## The Lucas average set contains $1$

For all integers $P, Q$ with $Q \ne 0$, the number $1$
lies in the Lucas average set $S'(U)$ of $U = U(P, Q)$: the set of $n$ in the Lucas period set
$S(U)$ with $n \mid U_1 + \dots + U_n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.2.

Formalized by `MetaMathlibExt.one_mem_lucasAverageSet`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 164](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L164). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#one-mem-lucas-average-set).

## Index-divisible set of a Lucas sequence

Let $U = U(P, Q)$ be the Lucas sequence with
integer parameters $P$ and $Q \ne 0$, given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$ (the paper's $U(a, b)$ with $a = P$ and $b = -Q$). The set $T(U)$
consists of the positive integers $n$ with $\gcd(n, Q) = 1$ and $n \mid U_n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.2.

Formalized by `MetaMathlibExt.lucasIndexDivisibleSet`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-index-divisible-set).

## The index-divisible set of a Lucas sequence contains $1$

For all integers $P, Q$ with
$Q \ne 0$, the number $1$ lies in the set $T(U)$ of positive integers $n$ coprime to $Q$ with
$n \mid U_n$, where $U = U(P, Q)$ is their Lucas sequence.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.2.

Formalized by `MetaMathlibExt.one_mem_lucasIndexDivisibleSet`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#one-mem-lucas-index-divisible-set).

## The average at $n = 1$ is integral

For integers $P$ and $Q \ne 0$, every integer
sequence $(w_k)_{k \ge 0}$ with $w_{k+2} = P w_{k+1} - Q w_k$ for all $k$ satisfies $1 \mid w_1$;
that is, the average $A_W(1) = w_1$ is an integer.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Section 2.

Formalized by `MetaMathlibExt.lucasAllAveragesIntegral_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-all-averages-integral-one).

## Doubling formulas and divisibility for Lucas sequences

Let $U$ and $V$ be the Lucas
sequences with integer parameters $P$ and $Q \neq 0$. Then $U_{2n} = U_n V_n$ and
$U_{2n+1} = -Q U_n^2 + U_{n+1}^2$ for every natural number $n$, and $U_m \mid U_n$ for all
natural numbers $m$ and $n$ with $m \mid n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Lemma 1.1.

Stated but not proved: `MetaMathlibExt.lucasU_two_mul_and_lucasU_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-two-mul-and-lucas-u-dvd).

## Periods of second-order recurrences modulo $m$

Let $U$ be the Lucas sequence with
integer parameters $P$ and $Q \neq 0$, let $m$ be a positive integer with $\gcd(m, Q) = 1$, and
write $\pi(m)$ and $\rho(m)$ for the period and the restricted period of $U$ modulo $m$. Then
$\pi(m) > 0$ and $\rho(m) > 0$, and every integer sequence $w$ with
$w_{k+2} = P w_{k+1} - Q w_k$ for all $k$ satisfies $w_{n + \pi(m)} \equiv w_n \pmod m$ and
$w_{n + \rho(m)} \equiv U_{\rho(m) + 1} w_n \pmod m$ for every natural number $n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.1.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_isPeriod_of_secondOrder` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-is-period-of-second-order).

## Periods of Lucas sequences modulo a least common multiple

Let $U$ be the Lucas sequence
with integer parameters $P$ and $Q \neq 0$, and write $\pi(m)$ and $\rho(m)$ for its period and
restricted period modulo $m$. Let $m$ and $n$ be positive integers with $\gcd(mn, Q) = 1$. Then
$\pi(\operatorname{lcm}(m, n)) = \operatorname{lcm}(\pi(m), \pi(n))$ and
$\rho(\operatorname{lcm}(m, n)) = \operatorname{lcm}(\rho(m), \rho(n))$, and for every $i \ge 1$
the $i$-fold iterates $\pi^i$ and $\rho^i$ of the maps $k \mapsto \pi(k)$ and $k \mapsto \rho(k)$
satisfy $\pi^i(\operatorname{lcm}(m, n)) = \operatorname{lcm}(\pi^i(m), \pi^i(n))$ and
$\rho^i(\operatorname{lcm}(m, n)) = \operatorname{lcm}(\rho^i(m), \rho^i(n))$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.2.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_lcm` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 228](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L228). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-lcm).

## Closed forms of eight degenerate second-order recurrences

For every integer sequence
$(w_j)_{j \ge 0}$ and every $n \in \mathbb{N}$: if $w_{j+2} = w_j$ for all $j$, then
$w_{2n} = w_0$ and $w_{2n+1} = w_1$; if $w_{j+2} = -w_j$ for all $j$, then $w_{4n} = w_0$,
$w_{4n+1} = w_1$, $w_{4n+2} = -w_0$ and $w_{4n+3} = -w_1$; if $w_{j+2} = w_{j+1} - w_j$ for all
$j$, then $w_{6n} = w_0$, $w_{6n+1} = w_1$, $w_{6n+2} = w_1 - w_0$, $w_{6n+3} = -w_0$,
$w_{6n+4} = -w_1$ and $w_{6n+5} = w_0 - w_1$; if $w_{j+2} = -w_{j+1} - w_j$ for all $j$, then
$w_{3n} = w_0$, $w_{3n+1} = w_1$ and $w_{3n+2} = -w_1 - w_0$; if $w_{j+2} = 2 w_{j+1} - w_j$ for
all $j$, then $w_n = n w_1 - (n - 1) w_0$; if $w_{j+2} = -2 w_{j+1} - w_j$ for all $j$, then
$w_n = (-1)^{n+1} (n w_1 + (n - 1) w_0)$; if $w_{j+2} = w_{j+1}$ for all $j$ and $n \ge 1$, then
$w_n = w_1$; and if $w_{j+2} = -w_{j+1}$ for all $j$ and $n \ge 1$, then $w_n = (-1)^{n+1} w_1$.

In the paper's notation $W_{j+2} = a W_{j+1} + b W_j$ these are the pairs $(a, b) = (0, 1)$,
$(0, -1)$, $(1, -1)$, $(-1, -1)$, $(2, -1)$, $(-2, -1)$, $(1, 0)$ and $(-1, 0)$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.3.

Stated but not proved: `MetaMathlibExt.degenerate_secondOrder_closedForms` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#degenerate-second-order-closed-forms).

## Sums of eight degenerate second-order recurrences

For an integer sequence
$(w_j)_{j \ge 0}$ write $B_w(n) = w_1 + \dots + w_n$. Let $u$ be the sequence with $u_0 = 0$,
$u_1 = 1$ and $u_{j+2} = u_j$, and $v$ the sequence with $v_0 = 0$, $v_1 = 1$ and
$v_{j+2} = -2 v_{j+1} - v_j$. For every $n \ge 1$: $B_u(n) = \lfloor (n + 1) / 2 \rfloor$ and
$B_v(n) = (-1)^{n+1} \lfloor (n + 1) / 2 \rfloor$; $n$ divides $B_w(n)$ for every integer
sequence $w$ with $w_{j+2} = w_j$ if and only if $n = 1$; $n$ divides $B_w(n)$ for every integer
sequence $w$ with $w_{j+2} = 2 w_{j+1} - w_j$ if and only if $n$ is odd; and $n$ divides
$B_w(n)$ for every integer sequence $w$ with $w_{j+2} = -2 w_{j+1} - w_j$ if and only if
$n = 1$. For every integer sequence $w$ and every $n \in \mathbb{N}$: if $w_{j+2} = -w_j$ for all
$j$, then $B_w(4n) = 0$; if $w_{j+2} = w_{j+1} - w_j$ for all $j$, then $B_w(6n) = 0$; if
$w_{j+2} = -w_{j+1} - w_j$ for all $j$, then $B_w(3n) = 0$; if $w_{j+2} = w_{j+1}$ for all $j$,
then $B_w(n) = n w_1$; if $w_{j+2} = -w_{j+1}$ for all $j$, then $B_w(2n) = 0$; and if
$w_{j+2} = 2 w_{j+1} - w_j$ for all $j$, then $2 B_w(n) = (w_1 - w_0) n (n + 1) + 2 w_0 n$ and,
when $n \ge 1$, $B_w(2n - 1) = (2n - 1)(n (w_1 - w_0) + w_0)$.

In the paper's notation $W_{j+2} = a W_{j+1} + b W_j$ these are the pairs $(a, b) = (0, 1)$,
$(0, -1)$, $(1, -1)$, $(-1, -1)$, $(2, -1)$, $(-2, -1)$, $(1, 0)$ and $(-1, 0)$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.1.

Stated but not proved: `MetaMathlibExt.degenerate_secondOrder_sums` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#degenerate-second-order-sums).

## Sum formula for second-order recurrences

Let $P, Q$ be integers with $Q \ne 0$ and
$P^2 - 4Q \ne 0$, let $U = U(P, Q)$ be their Lucas sequence, write $a = P$ and $b = -Q$, and let
$w$ be an integer sequence with $w_{k+2} = a w_{k+1} + b w_k$ for all $k \ge 0$. For $n \ge 0$
let $B(n) = w_1 + \dots + w_n$, and for $n > 0$ let $\pi_U(n)$ be the period of $U$ modulo $n$:
the least $r > 0$ with $U_r \equiv 0$ and $U_{r+1} \equiv 1 \pmod n$, or $0$ if there is none.
If $a + b - 1 \ne 0$, then for every $n \ge 0$

$$(a + b - 1) B(n) = w_{n+1} - w_1 + b (w_n - w_0),$$

and for every $n > 0$ coprime to $b$ and every $r \ge 0$ divisible by $\pi_U(n)$, $n$ divides
$w_{r+1} - w_1 + b (w_r - w_0)$. If $a + b - 1 = 0$, then for every $n \ge 0$

$$(-b - 1) B(n) = (w_1 - w_0) U_{n+1} - n (w_1 + b w_0) + w_0 - w_1.$$

The congruence $K(s) \equiv 0 \pmod n$ claimed in part (ii) of the source, for the source's
quantity $K(s)$, is false as printed and is omitted: for $(a, b) = (-6, 7)$, $w = U$ and $n = 3$
one has $\gcd(3, 7) = 1$ and $\pi_U(3) = 2$, but $K(2) = 40$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.2.

Stated but not proved: `MetaMathlibExt.secondOrder_sum_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#second-order-sum-formula).

## Sum of the first $n$ terms of a Lucas sequence

Let $U$ be the Lucas sequence
$U_0 = 0$, $U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$ with integer parameters $P$ and $Q \ne 0$,
and let $B(n) = U_1 + \cdots + U_n$. For every $n \ge 0$: if $P - Q - 1 \ne 0$, then
$(P - Q - 1) B(n) = U_{n+1} - 1 - Q U_n$; if $P - Q - 1 = 0$, then
$(Q - 1) B(n) = U_{n+1} - 1 - n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 2.1.

Stated but not proved: `MetaMathlibExt.lucasU_sum_formula` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-sum-formula).

## Sums of a second-order recurrence over whole periods

Let $P, Q$ be integers with $Q \ne 0$,
let $U = U(P, Q)$ be their Lucas sequence, write $a = P$ and $b = -Q$, and suppose
$a + b - 1 \ne 0$. Let $n > 0$ be coprime to $b(a + b - 1)$, and let $\pi_U(n)$ be the period of
$U$ modulo $n$: the least $r > 0$ with $U_r \equiv 0$ and $U_{r+1} \equiv 1 \pmod n$, or $0$ if
there is none. Then $\pi_U(n) > 0$, and for every $r \ge 0$ divisible by $\pi_U(n)$ and every
integer sequence $w$ with $w_{k+2} = a w_{k+1} + b w_k$ for all $k \ge 0$, $n$ divides
$w_1 + \dots + w_r$.

Part (ii) of the corollary is false as printed and is omitted: for $(a, b) = (-6, 7)$, so that
$a + b - 1 = 0$, the number $n = 3$ is coprime to $7 \cdot (-8)$ and $\pi_U(3) = 2$, but
$U_1 + U_2 = 1 - 6 = -5$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 2.2.

Stated but not proved: `MetaMathlibExt.secondOrder_sum_dvd_of_period_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 344](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L344). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#second-order-sum-dvd-of-period-dvd).

## Multiplying a member of $S(U)$ by one of its prime factors

Let $P, Q$ be integers with
$Q \ne 0$, let $U = U(P, Q)$ be their Lucas sequence, write $a = P$ and $b = -Q$, and let $S(U)$ be
the set of positive integers $n$ coprime to $Q$ whose period $\pi_U(n)$ modulo $n$ divides $n$. If
$n \in S(U)$ and $\ell$ is a prime dividing $n$, then $\ell n \in S(U)$. If moreover
$a + b - 1 \ne 0$ and $\gcd(a + b - 1, n) = 1$, or $a + b - 1 = 0$ and $\gcd(-b - 1, n) = 1$, then
$\ell n$ lies in $S'(U)$, the set of $t \in S(U)$ with $t \mid U_1 + \dots + U_t$, and $\ell n$
divides $w_1 + \dots + w_{\ell n}$ for every integer sequence $w$ with
$w_{k+2} = a w_{k+1} + b w_k$ for all $k \ge 0$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.3.

Stated but not proved: `MetaMathlibExt.prime_mul_mem_lucasPeriodSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#prime-mul-mem-lucas-period-set).

## Multiplying a member of $S(U)$ by a number with no new prime factors

Let $P, Q$ be
integers with $Q \ne 0$, let $U = U(P, Q)$ be their Lucas sequence, write $a = P$ and $b = -Q$, and
let $S(U)$ be the set of positive integers $n$ coprime to $Q$ whose period $\pi_U(n)$ modulo $n$
divides $n$. Let $m > 0$ and $n \in S(U)$ be such that every prime divisor of $m$ divides $n$.
Then $m n \in S(U)$. If moreover $a + b - 1 \ne 0$ and $\gcd(a + b - 1, n) = 1$, or $a + b - 1 = 0$
and $\gcd(-b - 1, n) = 1$, then $m n$ lies in $S'(U)$, the set of $t \in S(U)$ with
$t \mid U_1 + \dots + U_t$, and $m n$ divides $w_1 + \dots + w_{mn}$ for every integer sequence
$w$ with $w_{k+2} = a w_{k+1} + b w_k$ for all $k \ge 0$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 2.3.

Stated but not proved: `MetaMathlibExt.mul_mem_lucasPeriodSet_of_primeFactors` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 373](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L373). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#mul-mem-lucas-period-set-of-prime-factor).

## Closure of the period set under lcm and products

Let $U$ be the Lucas sequence with
parameters $P$ and $Q \ne 0$, given by $U_0 = 0$, $U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$. Let
$S(U)$ be the set of positive integers $n$ coprime to $Q$ such that the period $\pi_U(n)$ of $U$
modulo $n$ divides $n$, and let $S'(U)$ be the set of $n \in S(U)$ with
$n \mid U_1 + \dots + U_n$. Say that a natural number $x$ has integral averages if
$x \mid w_1 + \dots + w_x$ for every integer sequence $(w_k)_{k \ge 0}$ with
$w_{k+2} = P w_{k+1} - Q w_k$ for all $k$, and that $x$ satisfies the coprimality condition if
either $P - Q - 1 \ne 0$ and $\gcd(P - Q - 1, x) = 1$, or $P - Q - 1 = 0$ and
$\gcd(Q - 1, x) = 1$. Then for all $m, n \in S(U)$, both $\operatorname{lcm}(m, n)$ and $mn$ lie
in $S(U)$, and if $mn$ satisfies the coprimality condition, then each of $m$, $n$,
$\operatorname{lcm}(m, n)$ and $mn$ lies in $S'(U)$ and has integral averages. Moreover, for every
positive integer $r$ and every $c$, if $c$ is the least element of $S(U)$ divisible by $r$ and $c$
satisfies the coprimality condition, then $c$ is also the least element of $S'(U)$ divisible by
$r$, and $c$ has integral averages.

In the paper's notation $a = P$ and $b = -Q$, so $P - Q - 1 = a + b - 1$ and $Q - 1 = -b - 1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.4.

Stated but not proved: `MetaMathlibExt.lcm_mem_lucasPeriodSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 390](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L390). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lcm-mem-lucas-period-set).

## The average set is closed under lcm

Let $P$ and $Q \ne 0$ be integers and $U$ the Lucas
sequence given by $U_0 = 0$, $U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$. Let $S'(U)$ be the set
of positive integers $n$ coprime to $Q$ such that the period $\pi_U(n)$ of $U$ modulo $n$ divides
$n$ and $n \mid U_1 + \dots + U_n$, and say that a natural number $x$ has integral averages if
$x \mid w_1 + \dots + w_x$ for every integer sequence $(w_k)_{k \ge 0}$ with
$w_{k+2} = P w_{k+1} - Q w_k$ for all $k$. Let $m, n \in S'(U)$ and let $r$ be a natural number
divisible by $m$. Then $m \mid U_1 + \dots + U_r$, $\operatorname{lcm}(m, n) \in S'(U)$, each of
$m$, $n$ and $\operatorname{lcm}(m, n)$ has integral averages, and $m \mid w_1 + \dots + w_r$ for
every integer sequence $(w_k)_{k \ge 0}$ with $w_{k+2} = P w_{k+1} - Q w_k$ for all $k$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.5.

Stated but not proved: `MetaMathlibExt.lcm_mem_lucasAverageSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 409](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L409). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lcm-mem-lucas-average-set).

## Divisibility of Lucas sums when $P = 1$

Let $U$ be the Lucas sequence $U_0 = 0$,
$U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$ with $P = 1$ and $Q \ne 0$. For every positive integer
$n$ coprime to $Q$, $n \mid U_1 + \cdots + U_n$ if and only if $U_{n+2} \equiv 1 \pmod n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.6.

Stated but not proved: `MetaMathlibExt.lucasU_sum_dvd_iff_of_p_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 424](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L424). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-sum-dvd-iff-of-p-eq-one).

## Integral averages extend to least common multiples

Let $U$ be the Lucas sequence with
parameters $P$ and $Q \ne 0$, given by $U_0 = 0$, $U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$, and
let $S'(U)$ be the set of positive integers $n$ coprime to $Q$ such that the period $\pi_U(n)$ of
$U$ modulo $n$ divides $n$ and $n \mid U_1 + \dots + U_n$. Call an integer sequence
$(w_k)_{k \ge 0}$ a recurrence if $w_{k+2} = P w_{k+1} - Q w_k$ for all $k$, and say that a
natural number $x$ has integral averages if $x \mid w_1 + \dots + w_x$ for every recurrence $w$.
Let $n > 0$ be such that every recurrence $w$ satisfies $w_{k+n} \equiv w_k \pmod n$ for all
$k \ge 1$, and suppose $n$ has integral averages. Then $\operatorname{lcm}(m, n)$ has integral
averages for every $m \in S'(U)$.

In the paper's notation $a = P$ and $b = -Q$, and the recurrences are the sequences $W(a, b)$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.7.

Stated but not proved: `MetaMathlibExt.lucasAllAveragesIntegral_lcm` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 436](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L436). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-all-averages-integral-lcm).

## Integral averages when $n$ divides $Q$

Let $U$ be the Lucas sequence with parameters $P$
and $Q \ne 0$, given by $U_0 = 0$, $U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$, and let $S'(U)$ be
the set of positive integers $n$ coprime to $Q$ such that the period $\pi_U(n)$ of $U$ modulo $n$
divides $n$ and $n \mid U_1 + \dots + U_n$. Say that a natural number $x$ has integral averages
if $x \mid w_1 + \dots + w_x$ for every integer sequence $(w_k)_{k \ge 0}$ with
$w_{k+2} = P w_{k+1} - Q w_k$ for all $k$. Let $n > 1$ divide $Q$, and suppose that either
$P \equiv 1 \pmod n$, or $n$ is even and $P \equiv -1 \pmod n$. Then for every $m \in S'(U)$,
both $n$ and $mn$ have integral averages.

In the paper's notation $a = P$ and $b = -Q$, so $n \mid Q$ is the paper's $n \mid b$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.10.

Stated but not proved: `MetaMathlibExt.lucasAllAveragesIntegral_of_dvd_q` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-all-averages-integral-of-dvd-q).

## Non-integer period average of a Lucas sequence when $\gcd(n, a, b) > 1$

Theorem 2.13: for nondegenerate `U(a, b)` with `d = gcd(a, b) > 1` and
`gcd(n, d) > 1`, `A_U(n)` is not an integer.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.13.

Stated but not proved: `MetaMathlibExt.not_dvd_lucasU_sum_of_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#not-dvd-lucas-u-sum-of-gcd).

## Lucas sums and powers of two for even $P$ and odd $Q$

Let $U$ be the Lucas sequence
$U_0 = 0$, $U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$ with $(P, Q)$ nondegenerate, $P$ even and
$Q$ odd, and let $S$ be the set of positive integers $m$ coprime to $Q$ such that the period of
$U$ modulo $m$ divides $m$. If $n \equiv 2 \pmod 4$, then $U_1 + \cdots + U_n$ is odd and not
divisible by $n$. For every $k \ge 0$, $2^k$ is the least element of $S$ divisible by $2^k$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.14.

Stated but not proved: `MetaMathlibExt.lucasU_sum_odd_of_even_p` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-sum-odd-of-even-p).

## Powers of two when $P \equiv 2$ and $-Q \equiv 1 \pmod 4$

Let $P$ and $Q \ne 0$ be
integers forming a nondegenerate Lucas pair with $P \equiv 2 \pmod 4$ and $-Q \equiv 1 \pmod 4$,
and let $U$ be the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$. Let $S(U)$ be the set of positive integers $n$ coprime to $Q$ such
that the period $\pi_U(n)$ of $U$ modulo $n$ divides $n$, let $S'(U)$ be the set of $n \in S(U)$
with $n \mid U_1 + \dots + U_n$, and say that a natural number $x$ has integral averages if
$x \mid w_1 + \dots + w_x$ for every integer sequence $(w_k)_{k \ge 0}$ with
$w_{k+2} = P w_{k+1} - Q w_k$ for all $k$. Then $2^i \in S(U)$ for every $i \ge 1$; for every
$k \ge 2$ and every natural number $n$ with $2^k \mid n$ and $2^{k+1} \nmid n$, one has
$2^k \mid U_1 + \dots + U_n$; the least even element of $S'(U)$ is $4$, while the least even
element of $S(U)$ is $2$; and for every $k \ge 2$, $2^k$ is the least multiple of $2^k$ in
$S'(U)$ and in $S(U)$, and $2^k$ has integral averages.

In the paper's notation $a = P$ and $b = -Q$, so the hypotheses are $a \equiv 2$ and
$b \equiv 1 \pmod 4$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.15.

Stated but not proved: `MetaMathlibExt.lucasAverageSet_two_pow_of_p_two_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-average-set-two-pow-of-p-two-mod-f).

## Lucas sums not divisible by $2^k$ when $P \equiv 0$ and $-Q \equiv 1 \pmod 4$

Let $P$
and $Q \ne 0$ be integers forming a nondegenerate Lucas pair with $P \equiv 0 \pmod 4$ and
$-Q \equiv 1 \pmod 4$, and let $U$ be the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$. Let $S'(U)$ be the set of positive integers $n$ coprime to $Q$
such that the period $\pi_U(n)$ of $U$ modulo $n$ divides $n$ and $n \mid U_1 + \dots + U_n$.
Then for every $k \ge 1$ and every natural number $n$ with $2^k \mid n$ and $2^{k+1} \nmid n$,
$2^k$ does not divide $U_1 + \dots + U_n$; for every even $n > 0$, no element of $S'(U)$ is
divisible by $n$; and every positive integer $m$ with $m \mid U_1 + \dots + U_m$ is odd.

In the paper's notation $a = P$ and $b = -Q$, so the hypotheses are $a \equiv 0$ and
$b \equiv 1 \pmod 4$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.16.

Stated but not proved: `MetaMathlibExt.lucasU_sum_not_dvd_of_p_zero_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 504](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L504). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-sum-not-dvd-of-p-zero-mod-four).

## Powers of two when $P \equiv 0$ and $-Q \equiv -1 \pmod 4$

Let $P$ and $Q \ne 0$ be
integers forming a nondegenerate Lucas pair with $P \equiv 0 \pmod 4$ and $-Q \equiv -1 \pmod 4$,
and let $U$ be the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$. Let $S(U)$ be the set of positive integers $n$ coprime to $Q$ such
that the period $\pi_U(n)$ of $U$ modulo $n$ divides $n$, let $S'(U)$ be the set of $n \in S(U)$
with $n \mid U_1 + \dots + U_n$, and say that a natural number $x$ has integral averages if
$x \mid w_1 + \dots + w_x$ for every integer sequence $(w_k)_{k \ge 0}$ with
$w_{k+2} = P w_{k+1} - Q w_k$ for all $k$. Then $2^i \in S(U)$ for every $i \ge 1$; for every
$k \ge 2$ and every natural number $n$ with $2^k \mid n$ and $2^{k+1} \nmid n$, one has
$2^k \mid U_1 + \dots + U_n$; the least even element of $S'(U)$ is $4$, while the least even
element of $S(U)$ is $2$; and for every $k \ge 2$, $2^k$ is the least multiple of $2^k$ in
$S'(U)$ and in $S(U)$, and $2^k$ has integral averages.

In the paper's notation $a = P$ and $b = -Q$, so the hypotheses are $a \equiv 0$ and
$b \equiv -1 \pmod 4$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.17.

Stated but not proved: `MetaMathlibExt.lucasAverageSet_two_pow_of_p_zero_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 520](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L520). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-average-set-two-pow-of-p-zero-mod).

## Lucas sums not divisible by $2^k$ when $P \equiv 2$ and $-Q \equiv -1 \pmod 4$

Let $P$
and $Q \ne 0$ be integers forming a nondegenerate Lucas pair with $P \equiv 2 \pmod 4$ and
$-Q \equiv -1 \pmod 4$, and let $U$ be the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$. Let $S'(U)$ be the set of positive integers $n$ coprime to $Q$
such that the period $\pi_U(n)$ of $U$ modulo $n$ divides $n$ and $n \mid U_1 + \dots + U_n$.
Then for every $k \ge 1$ and every natural number $n$ with $2^k \mid n$ and $2^{k+1} \nmid n$,
$2^k$ does not divide $U_1 + \dots + U_n$; for every even $n > 0$, no element of $S'(U)$ is
divisible by $n$; and every positive integer $m$ with $m \mid U_1 + \dots + U_m$ is odd.

In the paper's notation $a = P$ and $b = -Q$, so the hypotheses are $a \equiv 2$ and
$b \equiv -1 \pmod 4$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.18.

Stated but not proved: `MetaMathlibExt.lucasU_sum_not_dvd_of_p_two_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 539](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L539). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-sum-not-dvd-of-p-two-mod-four).

## Wyler's theorem on the period of a Lucas sequence

Let $U$ be the Lucas sequence with
integer parameters $P$ and $Q$, where the pair $(P, Q)$ is nondegenerate, and write $\pi(m)$ and
$\rho(m)$ for the period and the restricted period of $U$ modulo $m$. Let $m \ge 2$ with
$\gcd(m, Q) = 1$, let $h$ be the multiplicative order of $Q$ modulo $m$, and put
$H = \operatorname{lcm}(h, \rho(m))$. Then $\pi(m) = H$ or $\pi(m) = 2H$. If moreover
$m = \ell^i$ for an odd prime $\ell$ and some $i \ge 1$, then $\pi(m) = 2H$ when the $2$-adic
valuations of $h$ and $\rho(m)$ differ, and $\pi(m) = H$ when they are equal and positive.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 3.1.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_eq_lcm_orderOf` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 555](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L555). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-eq-lcm-order-of).

## Period and restricted period of Lucas sequences with $Q = -1$

Let $U$ be the Lucas
sequence with integer parameters $P$ and $Q = -1$, where the pair $(P, Q)$ is nondegenerate, and
write $\pi(m)$ and $\rho(m)$ for the period and the restricted period of $U$ modulo $m$. Let
$m \ge 2$. Then $\pi(m)$ equals $\rho(m)$, $2\rho(m)$ or $4\rho(m)$. If $m = \ell^i$ for an odd
prime $\ell$ and some $i \ge 1$, then $\pi(m) = \rho(m)$ when $\rho(m) \equiv 2 \pmod 4$,
$\pi(m) = 2\rho(m)$ when $\rho(m) \equiv 0 \pmod 4$, and $\pi(m) = 4\rho(m)$ when $\rho(m)$ is
odd. Finally, $\pi(m)$ is even unless $m = 2$ and $P$ is odd.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 3.1.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_of_q_eq_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 581](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L581). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-of-q-eq-neg-one).

## Period and restricted period of Lucas sequences with $Q = 1$

Let $U$ be the Lucas
sequence with integer parameters $P$ and $Q = 1$, where the pair $(P, Q)$ is nondegenerate, and
write $\pi(m)$ and $\rho(m)$ for the period and the restricted period of $U$ modulo $m$. Let
$m \ge 2$. Then $\pi(m) = \rho(m)$ or $\pi(m) = 2\rho(m)$, and if $m = \ell^i$ for an odd prime
$\ell$ and some $i \ge 1$ and $\rho(m)$ is even, then $\pi(m) = 2\rho(m)$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 3.2.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_of_q_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 602](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L602). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-of-q-eq-one).

## Primes dividing the discriminant when $Q = \pm 1$

Let $U = U(P, Q)$ be a Lucas sequence
and let $\ell$ be a prime dividing its discriminant $D = P^2 - 4Q$. Write $\pi_U(m)$ and
$\rho_U(m)$ for the least period and the least restricted period of $U$ modulo $m$. If $Q = -1$,
then $\ell = 2$ or $\ell \equiv 1 \pmod 4$. If $Q = 1$, then $P \equiv 2 \pmod \ell$ or
$P \equiv -2 \pmod \ell$; moreover, if $\ell > 2$ and $P \equiv 2 \pmod \ell$, then
$\pi_U(\ell^i) = \rho_U(\ell^i)$ for every $i \ge 1$, and if $\ell > 2$ and
$P \equiv -2 \pmod \ell$, then $\pi_U(\ell^i) = 2 \rho_U(\ell^i)$ for every $i \ge 1$.

In the paper's notation $W(n + 2) = a W(n + 1) + b W(n)$ one has $a = P$ and $b = -Q$. The
restriction to $\ell > 2$ in the case $P \equiv 2 \pmod \ell$ is needed: for $(P, Q) = (4, 1)$
one has $D = 12$ and $P \equiv 2 \pmod 2$, but $\pi_U(4) = 4$ and $\rho_U(4) = 2$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 3.2.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_prime_dvd_discr` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 619](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L619). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-prime-dvd-discr).

## Lucas sequences with $P = Q + 1$

Let $U$ be the Lucas sequence with integer parameters
$P$ and $Q$, where $P = Q + 1$, $Q \neq \pm 1$ and the pair $(P, Q)$ is nondegenerate, and write
$\pi(n)$ and $\rho(n)$ for the period and the restricted period of $U$ modulo $n$. Then
$P^2 - 4Q = (Q - 1)^2$; for every natural number $n$, $(Q - 1) U_n = Q^n - 1$ and
$U_{n+1} = Q U_n + 1$; $U_i \equiv 1 \pmod Q$ for every $i \ge 1$; and $\pi(n) = \rho(n)$ for
every positive integer $n$ with $\gcd(n, Q) = 1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 3.3.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_eq_restricted_of_p_eq_q_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 638](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L638). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-eq-restricted-of-p-eq-q-ad).

## Lucas sequences with $P = -Q - 1$

Let $U$ be the Lucas sequence with integer parameters
$P$ and $Q$, where $P = -Q - 1$, $Q \neq \pm 1$ and the pair $(P, Q)$ is nondegenerate, and write
$\pi(n)$ and $\rho(n)$ for the period and the restricted period of $U$ modulo $n$. Then
$P^2 - 4Q = (Q - 1)^2$, and for every natural number $n$,
$(1 - Q) U_n = (-Q)^n - (-1)^n$ and $U_{n+1} = -Q U_n + (-1)^n$. Moreover, for every positive
integer $n$ with $\gcd(n, Q) = 1$: if $\rho(n)$ is even, then $\pi(n) = \rho(n)$ and
$U_{\rho(n)+1} \equiv 1 \pmod n$; if $n > 1$ and $\rho(n)$ is odd, then $\pi(n) = 2\rho(n)$ and
$U_{\rho(n)+1} \equiv -1 \pmod n$; and if $n > 1$, then $\pi(n)$ is even.

The hypothesis $n > 1$ in the odd case is needed: for $n = 1$ one has $\rho(1) = \pi(1) = 1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 3.4.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_of_p_eq_neg_q_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 659](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L659). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-of-p-eq-neg-q-sub-one).

## Prime-power divisibility of Lucas sums

Let $U$ be the Lucas sequence $U_0 = 0$,
$U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$ with $(P, Q)$ nondegenerate. Let $\ell$ be an odd prime
and $e \ge 1$ with $\ell^e \mid P$, $\ell^{e+1} \nmid P$ and $Q \equiv -1 \pmod{\ell^{e+1}}$.
Then $\ell^e \mid P - Q - 1$ and $\ell^{e+1} \nmid P - Q - 1$, and
$\ell^i \mid U_1 + U_2 + \cdots + U_{2m\ell^i}$ for all $m \ge 1$ and $i \ge 1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Lemma 2.1.

Stated but not proved: `MetaMathlibExt.lucasU_sum_two_mul_prime_pow_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 682](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L682). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-sum-two-mul-prime-pow-dvd).

## Members of $S(U)$ of the form $2^i 3^j$

Let $P, Q$ be integers with $Q \ne 0$ such that
the Lucas pair $(P, Q)$ is nondegenerate, let $U = U(P, Q)$ be its Lucas sequence, write $a = P$
and $b = -Q$, and suppose $a + b - 1 \ne 0$. Call a positive integer $n$ good if $n$ lies in the
Lucas period set $S(U)$ (the positive integers $n$ coprime to $Q$ whose period $\pi_U(n)$ modulo
$n$ divides $n$) and $n$ divides $w_1 + \dots + w_n$ for every integer sequence $w$ with
$w_{k+2} = a w_{k+1} + b w_k$ for all $k \ge 0$. Then, for all integers $i, j \ge 0$: (i) if
$a \equiv \pm 1$ and $b \equiv 1 \pmod 6$, then $1$ and $2^{i+3} 3^{j+1}$ are good; (ii) if
$a \equiv 1$ and $b \equiv -1 \pmod 6$, then $1$ and $2^{i+1} 3^{j+1}$ are good; (iii) if
$a \equiv 3$ and $b \equiv -1 \pmod 6$, then $1$ and $2^{i+2} 3^{j+1}$ are good; (iv) if $e \ge 1$,
$a \equiv 3 \pmod 6$, $3^e$ divides $a$ but $3^{e+1}$ does not, and
$b \equiv 1 \pmod{2 \cdot 3^{e+1}}$, then $1$ and $2^{i+1} 3^{j+1}$ are good.

The paper's condition $\operatorname{rad}(n) \mid 6$ is implied by these forms of $n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.12.

Stated but not proved: `MetaMathlibExt.mem_lucasPeriodSet_of_two_three_smooth` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 702](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L702). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#mem-lucas-period-set-of-two-three-smooth).

## Odd moduli in the average set when $P \equiv 2$ and $Q \equiv 1$

Let $(P, Q)$ be a
nondegenerate Lucas pair with $P - Q - 1 \ne 0$, Lucas sequence $U$, period set $S(U)$ and average
set $S'(U)$. Let $n \ge 1$ be odd, and suppose that $P \equiv 2$ and $Q \equiv 1 \pmod{\ell}$ for
every prime $\ell$ dividing $n$. Then every prime dividing $n$ divides $P^2 - 4Q$, $n$ is the
least element of $S'(U)$ divisible by $n$ and the least element of $S(U)$ divisible by $n$, and
$n$ divides $w_1 + \dots + w_n$ for every integer sequence $w$ with
$w_{j+2} = P w_{j+1} - Q w_j$ for all $j$.

In the paper's notation $a = P$ and $b = -Q$: the hypotheses read $a + b - 1 \ne 0$, $a \equiv 2$
and $b \equiv -1 \pmod{\operatorname{rad}(n)}$, and $P^2 - 4Q$ is the discriminant $D = a^2 + 4b$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.19.

Stated but not proved: `MetaMathlibExt.isLeast_lucasAverageSet_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 726](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L726). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#is-least-lucas-average-set-of-odd).

## Least multiples of $2^k n_1$ in the period set for even $P$

Let $U$ be the Lucas sequence
$U_0 = 0$, $U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$ with nondegenerate parameters
$P, Q \in \mathbb{Z}$. Let $S$ be the set of positive integers $m$ coprime to $Q$ such that the
period of $U$ modulo $m$ divides $m$, and let $S'$ be the set of $m \in S$ with
$m \mid U_1 + \cdots + U_m$. Call $m$ *integral for all recurrences* if every integer sequence
$w$ with $w_{j+2} = P w_{j+1} - Q w_j$ for all $j \ge 0$ satisfies $m \mid w_1 + \cdots + w_m$.

Suppose $P - Q - 1 \ne 0$, $P$ is even and $Q \equiv 1 \pmod 4$. Let $n = 2^k n_1$ with
$k \ge 1$ and $n_1 > 1$ odd, and suppose $P \equiv -2$ and $Q \equiv 1$ modulo every prime
dividing $n_1$. Then every prime dividing $n_1$ divides $P^2 - 4Q$, and $n$ is the least element
of $S$ divisible by $n$. If $P \equiv 2 \pmod 4$, no element of $S'$ is divisible by $n$. If
$P \equiv 0 \pmod 4$, then for $k = 1$ the least element of $S'$ divisible by $n$ is $2n$, and
$2n$ is integral for all recurrences; for $k \ge 2$ the least element of $S'$ divisible by $n$
is $n$, and $n$ is integral for all recurrences.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.20.

Stated but not proved: `MetaMathlibExt.lucasPeriodSet_isLeast_of_even_p` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 746](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L746). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-set-is-least-of-even-p).

## Multiples of $6$ in the average set when $P \equiv 1$ and $Q \equiv 1$

Let $(P, Q)$ be a
nondegenerate Lucas pair with Lucas sequence $U$, period set $S(U)$ and average set $S'(U)$. Let
$n \ge 1$ be divisible by $6$, and suppose that $P \equiv 1$ and $Q \equiv 1 \pmod{\ell}$ for
every prime $\ell$ dividing $n$. Then $n$ is the least element of $S'(U)$ divisible by $n$ and the
least element of $S(U)$ divisible by $n$, and $n$ divides $w_1 + \dots + w_n$ for every integer
sequence $w$ with $w_{j+2} = P w_{j+1} - Q w_j$ for all $j$.

In the paper's notation $a = P$ and $b = -Q$, and the hypotheses read $a \equiv 1$ and
$b \equiv -1 \pmod{\operatorname{rad}(n)}$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.21.

Stated but not proved: `MetaMathlibExt.isLeast_lucasAverageSet_of_six_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 767](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L767). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#is-least-lucas-average-set-of-six-dvd).

## Multiples of $3$ in the average set when $P \equiv -1$ and $Q \equiv 1$

Let $(P, Q)$ be a
nondegenerate Lucas pair with Lucas sequence $U$, period set $S(U)$ and average set $S'(U)$. Let
$n \ge 1$ be divisible by $3$, and suppose that $P \equiv -1$ and $Q \equiv 1 \pmod{\ell}$ for
every prime $\ell$ dividing $n$. Then $n$ is the least element of $S'(U)$ divisible by $n$ and the
least element of $S(U)$ divisible by $n$, and $n$ divides $w_1 + \dots + w_n$ for every integer
sequence $w$ with $w_{j+2} = P w_{j+1} - Q w_j$ for all $j$.

In the paper's notation $a = P$ and $b = -Q$, and the hypotheses read $a \equiv -1$ and
$b \equiv -1 \pmod{\operatorname{rad}(n)}$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.22.

Stated but not proved: `MetaMathlibExt.isLeast_lucasAverageSet_of_three_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 779](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L779). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#is-least-lucas-average-set-of-three-dvd).

## Multiples of $4$ in the average set when $P \equiv 0$ and $Q \equiv 1$

Let $(P, Q)$ be a
nondegenerate Lucas pair with Lucas sequence $U$, period set $S(U)$ and average set $S'(U)$. Let
$k \ge 2$, let $n_1$ be odd and put $n = 2^k n_1$. Suppose that $P \equiv 0$ and
$Q \equiv 1 \pmod 4$, and that $P \equiv 0$ and $Q \equiv 1 \pmod{\ell}$ for every prime $\ell$
dividing $n_1$. Then $n$ is the least element of $S'(U)$ divisible by $n$ and the least element
of $S(U)$ divisible by $n$, and $n$ divides $w_1 + \dots + w_n$ for every integer sequence $w$
with $w_{j+2} = P w_{j+1} - Q w_j$ for all $j$.

In the paper's notation $a = P$ and $b = -Q$, and the hypotheses read $a \equiv 0$ and
$b \equiv -1 \pmod{4 \operatorname{rad}(n_1)}$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.23.

Stated but not proved: `MetaMathlibExt.isLeast_lucasAverageSet_of_four_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#is-least-lucas-average-set-of-four-dvd).

## Period set equals index-divisible set for nondegenerate $U(P, Q)$ with $P = Q + 1$

Let
$U = U(P, Q)$ be a nondegenerate Lucas sequence with integer parameters $P$ and $Q \ne 0$ and
$P = Q + 1$ (in the paper's notation $U(a, b)$ with $a = P$ and $b = -Q$, this is $a = -b + 1$).
Then $S(U) = T(U)$, where $S(U)$ is the set of positive integers $n$ with $\gcd(n, Q) = 1$ and
$\pi_U(n) \mid n$, $\pi_U(n)$ being the period of $U$ modulo $n$, and $T(U)$ is the set of
positive integers $n$ with $\gcd(n, Q) = 1$ and $n \mid U_n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 4.2.

Stated but not proved: `MetaMathlibExt.lucasPeriodSet_eq_lucasIndexDivisibleSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 805](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L805). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-set-eq-lucas-index-divisibl).

## Closing of the period orbit

Let $U = U(P, Q)$ be the Lucas sequence with integer
parameters $P$ and $Q \ne 0$ (the paper's $U(a, b)$ with $a = P$ and $b = -Q$). For $m \ge 0$ let
$\pi_U(m)$ be the least $r > 0$ with $U_r \equiv 0$ and $U_{r+1} \equiv 1 \pmod m$ (congruence
modulo $0$ being equality), or $0$ if there is none, and let $\pi_U^i$ be its $i$-th iterate, with
$\pi_U^0(n) = n$. For natural numbers $n$ and $k$, the period orbit of $n$ closes at step $k$ when
$\pi_U^i(n)$ is coprime to $Q$ for every $0 \le i \le k$ and $\pi_U^{k+1}(n) = \pi_U^j(n)$ for
some $j \le k$.

The least such $k$ is the paper's $\omega(n)$, and "$\omega(n)$ exists" means that the period
orbit of $n$ closes at some step.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.4.

Formalized by `MetaMathlibExt.LucasPeriodOrbitCloses`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 815](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L815). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-closes).

## The orbit index $\omega(n)$

For a Lucas sequence $U = U(P, Q)$ and a natural number $n$,
$\omega(n)$ is the least natural number $k$ such that the period orbit of $n$ closes at step $k$,
and $\omega(n) = 0$ when there is no such $k$. Here $\pi_U(m)$ is the period of $U$ modulo $m$,
$\pi_U^i$ is its $i$-th iterate with $\pi_U^0(n) = n$, and the orbit of $n$ closes at step $k$
when $\pi_U^i(n)$ is coprime to $Q$ for all $i \le k$ and $\pi_U^{k+1}(n) = \pi_U^j(n)$ for some
$j \le k$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.4.

Formalized by `MetaMathlibExt.lucasPeriodOrbitIndex`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 824](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L824). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-index).

## The orbit lcm $L(n)$

For a Lucas sequence $U = U(P, Q)$ and a natural number $n$, let
$\pi_U(m)$ be the period of $U$ modulo $m$, with iterates $\pi_U^i$ and $\pi_U^0(n) = n$, and let
$\omega(n)$ be the orbit index of $n$ (the least step at which the period orbit of $n$ closes, or
$0$ if there is none). Then $L(n)$ is defined by

$$L(n) = \operatorname{lcm}\bigl(\pi_U^0(n), \pi_U^1(n), \ldots, \pi_U^{\omega(n)}(n)\bigr).$$

It is meaningful when $\omega(n)$ exists.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.8, equation (2.14).

Formalized by `MetaMathlibExt.lucasPeriodOrbitLcm`, a definition declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 833](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L833). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-lcm).

## The period orbit of $1$ closes at step $0$

For every Lucas sequence $U = U(P, Q)$, let
$\pi_U(m)$ be the period of $U$ modulo $m$ and $\pi_U^i$ its $i$-th iterate, with
$\pi_U^0(n) = n$. Then the period orbit of $1$ closes at step $0$: $1$ is coprime to $Q$ and
$\pi_U^1(1) = \pi_U^0(1)$, that is, $\pi_U(1) = 1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.4 and Theorem 1.4 (ix).

Formalized by `MetaMathlibExt.lucasPeriodOrbitCloses_one_zero`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 841](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L841). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-closes-one-zero).

## The orbit index of $1$ is zero

For every Lucas sequence $U = U(P, Q)$, the orbit index
of $1$ is $\omega(1) = 0$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.4.

Formalized by `MetaMathlibExt.lucasPeriodOrbitIndex_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 851](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L851). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-index-one).

## The orbit lcm of $1$ is $1$

For every Lucas sequence $U = U(P, Q)$ with integer
parameters $P$ and $Q \ne 0$, $L(1) = 1$, where
$L(n) = \operatorname{lcm}(\pi_U^0(n), \dots, \pi_U^{\omega(n)}(n))$ is the lcm of the iterates
$\pi_U^i(n)$ of the period map $\pi_U$ of $U$, with $\pi_U^0(n) = n$, up to the orbit index
$\omega(n)$ of $n$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, equation (2.14).

Formalized by `MetaMathlibExt.lucasPeriodOrbitLcm_one`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 859](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L859). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-lcm-one).

## $n$ divides $L(n)$

Let $P, Q$ be integers with $Q \ne 0$ and $U$ the Lucas sequence with
$U_0 = 0$, $U_1 = 1$ and $U_{j+2} = P U_{j+1} - Q U_j$. For $m \in \mathbb{N}$ let $\pi_U(m)$ be
the least $r \ge 1$ with $U_r \equiv 0$ and $U_{r+1} \equiv 1 \pmod m$, or $0$ if there is none,
and let $\pi_U^i$ be its $i$-th iterate, so that $\pi_U^0(m) = m$. Let $\omega(n)$ be the least
$k$ such that $\pi_U^i(n)$ is coprime to $Q$ for all $i \le k$ and $\pi_U^{k+1}(n) = \pi_U^j(n)$
for some $j \le k$, or $0$ if there is no such $k$. Then every $n \in \mathbb{N}$ divides
$L(n) = \operatorname{lcm}(\pi_U^0(n), \pi_U^1(n), \dots, \pi_U^{\omega(n)}(n))$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Remark 2.6.

Formalized by `MetaMathlibExt.dvd_lucasPeriodOrbitLcm`, a theorem declared in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 867](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L867). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#dvd-lucas-period-orbit-lcm).

## Periods of a Lucas sequence modulo a prime

Let $U = U(P, Q)$ be a nondegenerate Lucas
sequence with discriminant $D = P^2 - 4Q$, and let $p$ be a prime. Write $\pi_U(m)$ and
$\rho_U(m)$ for the least period and the least restricted period of $U$ modulo $m$, and
$\left(\frac{x}{p}\right)$ for the Jacobi symbol.
(i) If $p \nmid 2QD$, then $\rho_U(p) > 1$, $\rho_U(p) \mid p - \left(\frac{D}{p}\right)$,
$\rho_U(p) \mid \pi_U(p)$ and $\pi_U(p) / \rho_U(p) \mid p - 1$; if $p = 2$ and $2 \nmid QD$,
then $\pi_U(2) = 3$.
(ii) If $p \nmid 2QD$, then $\rho_U(p) \mid \left(p - \left(\frac{D}{p}\right)\right) / 2$ if and
only if $\left(\frac{Q}{p}\right) = 1$.
(iii) If $p \nmid Q$ and $p \mid D$, then $\rho_U(p) = p$ and $\pi_U(p) \mid p (p - 1)$.
(iv) If $p \nmid 2Q$ and $\left(\frac{D}{p}\right) = 1$, then $\pi_U(p) \mid p - 1$.
(v) If $p \nmid 2Q$ and $\left(\frac{D}{p}\right) = -1$, then $\pi_U(p) \mid p^2 - 1$ and every
prime factor $\ell$ of $\pi_U(p)$ satisfies $2 \ell \le p + 1$.
(vi) If $p \nmid Q$ and $p \mid D$, then $p \mid \pi_U(p)$ and every prime factor of $\pi_U(p)$
is at most $p$.
(vii) If $p \nmid Q$, there is a largest $c \ge 1$ with $\rho_U(p^c) = \rho_U(p)$. If
$p^c \ne 2$, then $\rho_U(p^i) = p^{\max(i - c, 0)} \rho_U(p)$ for every $i \ge 1$. If
$p^c = 2$, there is a largest $d \ge 2$ with $\rho_U(2^d) = \rho_U(4)$, and
$\rho_U(2^i) = 2^{\max(i + 1 - d, 1)} \rho_U(2)$ for every $i \ge 2$.
(viii) If $p \nmid Q$, there is a largest $e \ge 1$ with $\pi_U(p^e) = \pi_U(p)$. If
$p^e \ne 2$, then $\pi_U(p^i) = p^{\max(i - e, 0)} \pi_U(p)$ for every $i \ge 1$. If
$p^e = 2$, there is a largest $g \ge 2$ with $\pi_U(2^g) = \pi_U(4)$, and
$\pi_U(2^i) = 2^{\max(i + 1 - g, 1)} \pi_U(2)$ for every $i \ge 2$.
(ix) $\rho_U(1) = \pi_U(1) = 1$.

In the paper's notation $W(n + 2) = a W(n + 1) + b W(n)$ one has $a = P$ and $b = -Q$. The claim
$\pi_U(p) / \rho_U(p) \mid p - 1$, printed under "if $p \ge 2$", is stated here under the
hypothesis $p \nmid 2QD$ of (i).

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.4.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_prime_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 889](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L889). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-prime-properties).

## Uniform distribution of Lucas sequences modulo primes dividing the discriminant

Let $U$
be the Lucas sequence with integer parameters $P$ and $Q$, where the pair $(P, Q)$ is
nondegenerate, and write $\pi(m)$ and $\rho(m)$ for the period and the restricted period of $U$
modulo $m$; for a positive integer $N$ and a residue $r$ modulo $N$, let $c_N(r)$ be the number of
$k < \pi(N)$ with $U_k \equiv r \pmod N$. Let $p$ be a prime with $p \nmid Q$ and
$p \mid P^2 - 4Q$, and put $E = \lfloor \pi(p) / \rho(p) \rfloor$. Then: (i) $\rho(p) = p$,
$\rho(p) \mid \pi(p)$, and $c_p(r) = E$ for every residue $r$ modulo $p$; (ii) if $p \ge 5$, then
for every $i \ge 1$, $\rho(p^i) = p^i$, $\pi(p^i) = p^i E$, and $c_{p^i}(r) = E$ for every residue
$r$ modulo $p^i$; (iii) if $p = 2$, then $P$ is even, and if moreover $P \equiv 2 \pmod 4$, then
for every $i \ge 1$, $\rho(2^i) = 2^i$, and if in addition $Q \equiv 1 \pmod 4$, then
$c_{2^i}(r) = 1$ for every residue $r$ modulo $2^i$; (iv) if $p = 3$, then $3 \mid P^2 - Q$, and
if $9 \nmid P^2 - Q$, then for every $i \ge 1$, $\rho(3^i) = 3^i$ and $c_{3^i}(r) = E$ for every
residue $r$ modulo $3^i$; (v) if $p = 2$ and the $2$-adic valuation of $P$ is $e \ge 2$, then
$\rho(2^i) = 2^{\max(i + 1 - e, 1)}$ for every $i \ge 1$; (vi) if $p = 3$ and the $3$-adic
valuation of $P^2 - Q$ is $d \ge 2$, then $\rho(3^i) = 3^{\max(i + 1 - d, 1)}$ for every $i \ge 1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 1.5.

Stated but not proved: `MetaMathlibExt.lucasU_uniform_of_prime_dvd_discr` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 946](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L946). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-u-uniform-of-prime-dvd-discr).

## Least multiples in $S(U)$ and the orbit lcm $L(n)$

Let $P$ and $Q \ne 0$ be integers and
$U$ the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$. Let
$\pi_U(m)$ be the period of $U$ modulo $m$ and $\pi_U^i$ its $i$-th iterate, with
$\pi_U^0(m) = m$. Let $S(U)$ be the set of positive integers $m$ coprime to $Q$ with
$\pi_U(m) \mid m$, let $S'(U)$ be the set of $m \in S(U)$ with $m \mid U_1 + \dots + U_m$, and
say that a natural number $x$ has integral averages if $x \mid w_1 + \dots + w_x$ for every
integer sequence $(w_k)_{k \ge 0}$ with $w_{k+2} = P w_{k+1} - Q w_k$ for all $k$. Let $n > 0$.
If the period orbit of $n$ closes at some step $k$, meaning that $\pi_U^i(n)$ is coprime to $Q$
for all $i \le k$ and $\pi_U^{k+1}(n) = \pi_U^j(n)$ for some $j \le k$, then the least element of
$S(U)$ divisible by $n$ is $L(n) = \operatorname{lcm}(\pi_U^0(n), \dots, \pi_U^{\omega(n)}(n))$,
where $\omega(n)$ is the least such $k$. Moreover, if $c$ is the least element of $S(U)$
divisible by $n$, and either $P - Q - 1 \ne 0$ and $\gcd(c, P - Q - 1) = 1$, or $P - Q - 1 = 0$
and $\gcd(c, Q - 1) = 1$, then $c$ is also the least element of $S'(U)$ divisible by $n$, and $c$
has integral averages.

In the paper's notation $a = P$ and $b = -Q$, so $P - Q - 1 = a + b - 1$ and $Q - 1 = -b - 1$;
the paper's hypothesis $\gcd(n, b) = 1$ is the case $i = 0$ of the closing condition.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.8.

Stated but not proved: `MetaMathlibExt.isLeast_lucasPeriodSet_eq_lucasPeriodOrbitLcm` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 988](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L988). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#is-least-lucas-period-set-eq-lucas-perio).

## Divisibility and multiplicativity of the orbit lcm

Let $P$ and $Q \ne 0$ be integers and
$U$ the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$. Let
$\pi_U(m)$ be the period of $U$ modulo $m$ and $\pi_U^i$ its $i$-th iterate, with
$\pi_U^0(m) = m$. Say that $\omega(m)$ exists if the period orbit of $m$ closes at some step $k$,
meaning that $\pi_U^i(m)$ is coprime to $Q$ for all $i \le k$ and $\pi_U^{k+1}(m) = \pi_U^j(m)$
for some $j \le k$; then $\omega(m)$ is the least such $k$ and
$L(m) = \operatorname{lcm}(\pi_U^0(m), \dots, \pi_U^{\omega(m)}(m))$. Then:
(i) if $n > 0$, $\omega(n)$ exists and $m \mid n$, then $\omega(m)$ exists and $L(m) \mid L(n)$;
(ii) if $n > 0$, $g > 0$, $\omega(n)$ exists and $g \mid \pi_U^i(n)$ for some $i$, then
$\omega(g)$ exists and $L(g) \mid L(n)$;
(iii) if $r, s > 0$ are coprime and $\omega(r)$ and $\omega(s)$ exist, then $\omega(rs)$ exists
and $L(rs) = \operatorname{lcm}(L(r), L(s))$;
(iv) if $p$ is prime, $i \ge 1$ and $\omega(p)$ exists, then $\omega(p^i)$ exists and
$L(p^i) = \operatorname{lcm}(p^i, L(p))$.

In the paper's notation $b = -Q$. The coprimality to $b$ of $n$, $r$, $s$ and $p$ is part of the
existence of $\omega$; the existence of $\omega(g)$ in (ii) and of $\omega(rs)$ in (iii) is
implicit in the paper's statements about $L(g)$ and $L(rs)$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 2.4.

Stated but not proved: `MetaMathlibExt.lucasPeriodOrbitLcm_dvd_of_dvd` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1008](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1008). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-lcm-dvd-of-dvd).

## The orbit lcms $L(2)$ and $L(3)$

Let $P$ and $Q \ne 0$ be integers, write $a = P$ and
$b = -Q$, and let $U$ be the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$. Let $\pi_U(m)$ be the period of $U$ modulo $m$ and $\pi_U^i$ its
$i$-th iterate, with $\pi_U^0(m) = m$. Say that $L(m)$ exists if the period orbit of $m$ closes at
some step $k$, meaning that $\pi_U^i(m)$ is coprime to $Q$ for all $i \le k$ and
$\pi_U^{k+1}(m) = \pi_U^j(m)$ for some $j \le k$; then, with $\omega(m)$ the least such $k$,
$L(m) = \operatorname{lcm}(\pi_U^0(m), \dots, \pi_U^{\omega(m)}(m))$. Then:
(i) if $a$ and $b$ are odd, then $L(2)$ exists if and only if $\gcd(b, 3) = 1$;
(ii) if $a$ is even, then $L(2)$ exists if and only if $b$ is odd;
(iii) if $L(3)$ exists, then $L(3) = 3$ or $6 \mid L(3)$;
(iv) $L(3)$ exists and equals $3$ if and only if $a \equiv b \equiv -1 \pmod 3$;
(v) $L(3)$ exists and is divisible by $6$ if and only if $\gcd(b, 6) = 1$ and not both
$a \equiv -1 \pmod 3$ and $b \equiv -1 \pmod 6$;
(vi) if $a$ is even and $b$ is odd, then $L(2)$ exists and $L(2) = 2$.
In each of the following cases, with all congruences modulo $6$, every $L(m)$ named exists and
has the given value:
(vii) if $a \equiv \pm 1$ and $b \equiv 1$, then $L(2) = L(3) = 24$;
(viii) if $a \equiv 1$ and $b \equiv -1$, or $a \equiv 3$ and $b \equiv 1$, then
$L(2) = L(3) = 6$;
(ix) if $a \equiv -1$ and $b \equiv -1$, then $L(2) = 6$ and $L(3) = 3$;
(x) if $a \equiv 0$, then $L(3) = 6$ when $b \equiv 1$, and $L(3) = 12$ when $b \equiv -1$;
(xi) if $a \equiv 3$ and $b \equiv -1$, then $L(2) = L(3) = 12$;
(xii) if $a \equiv \pm 2$ and $b \equiv 1$, then $L(3) = 24$, and if $a \equiv -2$ and
$b \equiv -1$, then $L(3) = 6$.
Finally, (xiii) if $n > 0$, every prime factor of $n$ divides $6$ and $L(n)$ exists, then every
prime factor of $L(n)$ divides $6$.

The second half of (xii) is false as printed in the paper for $a \equiv 2 \pmod 6$ and is
restricted here to $a \equiv -2 \pmod 6$: for $(a, b) = (2, 5)$, a nondegenerate pair, one has
$\pi_U(3) = 3$, so $L(3) = 3$, in line with (iv).

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.9.

Stated but not proved: `MetaMathlibExt.lucasPeriodOrbitLcm_two_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1041](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1041). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-orbit-lcm-two-three).

## Least multiples in $S(U)$ for nondegenerate $U(P, Q)$

Let $P$ and $Q \ne 0$ be integers
forming a nondegenerate Lucas pair, and let $U$ be the Lucas sequence given by $U_0 = 0$,
$U_1 = 1$ and $U_{k+2} = P U_{k+1} - Q U_k$. Let $S(U)$ be the set of positive integers $n$
coprime to $Q$ such that the period $\pi_U(n)$ of $U$ modulo $n$ divides $n$, and say that a
natural number $x$ has integral averages if $x \mid w_1 + \dots + w_x$ for every integer sequence
$(w_k)_{k \ge 0}$ with $w_{k+2} = P w_{k+1} - Q w_k$ for all $k$. Then $1$ is the least element
of $S(U)$ divisible by $1$, that is, the least element of $S(U)$. If $Q \ne \pm 1$ and every prime
factor of $Q$ is at least $5$, then: every $n \ge 2$ whose prime factors are all smaller than
every prime factor of $Q$ divides some element of $S(U)$; for every $n > 0$ whose prime factors
are all smaller than every prime factor of $Q$, if $c$ is the least element of $S(U)$ divisible
by $n$ and $\gcd(c, P - Q - 1) = 1$, then $c$ has integral averages; and if moreover
$P - Q - 1 \notin \{-1, 0, 1\}$ and every prime factor of $P - Q - 1$ is at least $5$, then for
every $n > 0$ whose prime factors are all smaller than every prime factor of $Q (P - Q - 1)$, the
least element of $S(U)$ divisible by $n$, if it exists, has integral averages. If $Q = \pm 1$,
then every $n > 0$ divides some element of $S(U)$. If $(P, Q)$ is $(1, -1)$, $(-1, -1)$ or
$(3, 1)$, then for every $n > 0$ the least element of $S(U)$ divisible by $n$, if it exists, has
integral averages.

In the paper's notation $a = P$ and $b = -Q$, so $P - Q - 1 = a + b - 1$. The claims for
$b = \pm 1$ are stated without the hypothesis that the least prime factor of $b$ is at least $5$,
which they would contradict under the paper's convention that the least prime factor of $\pm 1$
is $1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.11.

Stated but not proved: `MetaMathlibExt.exists_lucasPeriodSet_multiple` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1090](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1090). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#exists-lucas-period-set-multiple).

## Integral averages for $U(P, -1)$

Let $U = U(P, Q)$ be a Lucas sequence with $Q = -1$,
so that its discriminant is $D = P^2 + 4$, and let $\pi_U(n)$ be the least period of $U$ modulo
$n$. Call a natural number $n$ good if $n$ lies in the set $S'(U)$ of positive integers $n$
coprime to $Q$ with $\pi_U(n) \mid n$ and $n \mid U_1 + \dots + U_n$, and every integer sequence
$w$ with $w_{k+2} = P w_{k+1} + w_k$ for all $k$ satisfies $n \mid w_1 + \dots + w_n$. Let
$t \ne 1$ be a natural number all of whose prime factors are at least $5$ and divide $D$, and let
$i, j \ge 0$.
(i) If $P \equiv \pm 1 \pmod 6$, then $2^{i+3} 3^{j+1} t$ is good.
(ii) If $P \equiv 3 \pmod 6$, then $2^{i+1} 3^{j+1}$ and $2^{i+2} 3^{j+1} t$ are good.
(iii) If $P \equiv \pm 2 \pmod{12}$, then $2^{i+2} t$ and $2^{i+3} 3^{j+1} t$ are good.
(iv) If $P \equiv 6 \pmod{12}$, then $2^{i+2} 3^j t$ is good.

In the paper's notation $W(n + 2) = a W(n + 1) + b W(n)$ one has $a = P$ and $b = -Q = 1$, and
the paper's $q$ is $t$. The paper's conditions $n > 1$ and $\operatorname{rad}(n) \mid 6 D$
follow from the displayed forms.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 2.5.

Stated but not proved: `MetaMathlibExt.mem_lucasAverageSet_of_q_eq_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#mem-lucas-average-set-of-q-eq-neg-one).

## Integral averages for $U(P, 1)$

Let $U = U(P, Q)$ be a nondegenerate Lucas sequence with
$Q = 1$, so that its discriminant is $D = P^2 - 4$, and let $\pi_U(n)$ be the least period of $U$
modulo $n$. Call a natural number $n$ good if $n$ lies in the set $S'(U)$ of positive integers
$n$ coprime to $Q$ with $\pi_U(n) \mid n$ and $n \mid U_1 + \dots + U_n$, and every integer
sequence $w$ with $w_{k+2} = P w_{k+1} - w_k$ for all $k$ satisfies $n \mid w_1 + \dots + w_n$.
(i) Every odd $t > 1$ all of whose prime factors divide $P - 2$ is good.
(ii) Let $t \ne 1$ be odd with all prime factors at least $5$ and dividing $D$, and let
$i, j \ge 0$. If $P \equiv \pm 1 \pmod 6$, then $2^{i+1} 3^{j+1} t$ is good; if
$P \equiv 3 \pmod 6$ or $P \equiv 0 \pmod{12}$, then $2^{i+2} 3^{j+1} t$ is good.
(iii) If $P \equiv 0 \pmod 4$, $t$ is odd with all prime factors dividing $D$, and $i \ge 0$,
then $2^{i+2} t$ is good.

In the paper's notation $W(n + 2) = a W(n + 1) + b W(n)$ one has $a = P$ and $b = -Q = -1$. The
paper's "for all recurrences $W(a, 1)$" is read as $W(a, -1)$, the recurrences of $U(a, -1)$
(Theorem 2.5); as printed it is false: for $a = 5$, $n = 3$ and $W = U(5, 1)$ in the paper's
notation, $W_1 + W_2 + W_3 = 1 + 5 + 26 = 32$, which $3$ does not divide. The paper's condition
$a \ne 0, \pm 1, \pm 2$ in (i) is nondegeneracy.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Corollary 2.6.

Stated but not proved: `MetaMathlibExt.mem_lucasAverageSet_of_q_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#mem-lucas-average-set-of-q-eq-one).

## Least period and average multiples for $Q = -1$

Let $U$ be the Lucas sequence
$U_0 = 0$, $U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$ with $Q = -1$ and $(P, Q)$ nondegenerate.
Write $\pi(m)$ for the period of $U$ modulo $m$ and $\pi^i$ for the $i$-th iterate of $\pi$
($\pi^0(m) = m$). Let $S$ be the set of positive integers $m$ coprime to $Q$ with
$\pi(m) \mid m$, and $S'$ the set of $m \in S$ with $m \mid U_1 + \cdots + U_m$. Say the orbit
of $n$ closes at $k$ if $\pi^i(n)$ is coprime to $Q$ for all $i \le k$ and
$\pi^{k+1}(n) = \pi^j(n)$ for some $j \le k$; let $\omega(n)$ be the least such $k$ ($0$ if
there is none) and $L(n) = \operatorname{lcm}(\pi^0(n), \pi^1(n), \dots, \pi^{\omega(n)}(n))$.
Call $m$ *integral for all recurrences* if every integer sequence $w$ with
$w_{j+2} = P w_{j+1} - Q w_j$ for all $j \ge 0$ satisfies $m \mid w_1 + \cdots + w_m$. Then:

(i) for every $n \ge 1$ the orbit of $n$ closes at some $k$, and $L(n)$ is the least element of
$S$ divisible by $n$; for every $n > 1$, $L(n)$ is even and $L(2) \mid L(n)$; $\pi(n)$ is even
for every $n \ge 3$; and $\pi(2)$ is even if $P$ is even;

(ii) if $P$ is odd, then for every $n \ge 1$ the least element of $S'$ divisible by $n$ is
$L(n)$, and $L(n)$ is integral for all recurrences; moreover $L(2) = 24$ if
$P \equiv \pm 1 \pmod 6$, and $L(2) = 6$ if $P \equiv 3 \pmod 6$;

(iii) if $P \equiv 2 \pmod 4$, then $L(2) = 2$, and for every $n \ge 1$: if
$L(n) \not\equiv 2 \pmod 4$, the least element of $S'$ divisible by $n$ is $L(n)$ and $L(n)$ is
integral for all recurrences; if $L(n) \equiv 2 \pmod 4$, the least element of $S'$ divisible
by $n$ is $2L(n)$ and $2L(n)$ is integral for all recurrences;

(iv) if $P \equiv 0 \pmod 4$, then for every $n \ge 2$, $n \notin S'$ and no element of $S'$ is
divisible by $n$; $n \nmid U_1 + \cdots + U_n$ for every even $n \ge 1$; and every $n \ge 1$
with $n \mid U_1 + \cdots + U_n$ is odd.

The case split in (iii) is on $L(n)$ modulo $4$, not on $n$ modulo $4$: for $P = 6$ and $n = 3$
the least element of $S$ divisible by $3$ is $6$, while the least element of $S'$ divisible by
$3$ is $12$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.24.

Stated but not proved: `MetaMathlibExt.lucasPeriodSet_of_q_eq_neg_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-set-of-q-eq-neg-one).

## Least period and average multiples for $Q = 1$

Let $U$ be the Lucas sequence
$U_0 = 0$, $U_1 = 1$, $U_{j+2} = P U_{j+1} - Q U_j$ with $Q = 1$ and $(P, Q)$ nondegenerate. Let
$S$ be the set of positive integers $m$ coprime to $Q$ such that the period of $U$ modulo $m$
divides $m$, and $S'$ the set of $m \in S$ with $m \mid U_1 + \cdots + U_m$. For $n \ge 1$ let
$C(n)$ and $C'(n)$ be the least elements of $S$ and of $S'$ divisible by $n$, when they exist.
Call $m$ *integral for all recurrences* if every integer sequence $w$ with
$w_{j+2} = P w_{j+1} - Q w_j$ for all $j \ge 0$ satisfies $m \mid w_1 + \cdots + w_m$. Then:

(i) $C(n)$ exists for every $n \ge 1$, and for $n > 1$ one has $C(n) > 1$ and some prime divides
both $C(n)$ and $6(P^2 - 4)$;

(ii) if $n_1$ is odd and every prime dividing $n_1$ divides $P - 2$, then
$C(n_1) = C'(n_1) = n_1$ and $n_1$ is integral for all recurrences; and if $n \ge 1$ and $C(n)$
is odd, then $n$ is odd, $C'(n) = C(n)$, and $C(n)$ is integral for all recurrences;

(iii) if $P$ is odd, then for every $n \ge 1$, $C'(n) = C(n)$ and $C(n)$ is integral for all
recurrences;

(iv) if $P \equiv 0 \pmod 4$ and $n \ge 1$, then $C'(n) = 2C(n)$ and $2C(n)$ is integral for
all recurrences when $C(n) \equiv 2 \pmod 4$, and $C'(n) = C(n)$ and $C(n)$ is integral for all
recurrences when $4 \mid C(n)$;

(v) if $P \equiv 2 \pmod 4$ and $n \ge 1$, then $C'(n)$ does not exist when $C(n)$ is even, and
it does not exist when $n$ is even or $\gcd(n, P + 2) > 1$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.25.

Stated but not proved: `MetaMathlibExt.lucasPeriodSet_of_q_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-period-set-of-q-eq-one).

## Period and average sets when $P = Q + 1$

Let $P$ and $Q \ne 0$ be integers forming a
nondegenerate Lucas pair with $P = Q + 1$, so that the roots of $x^2 - Px + Q$ are $Q$ and $1$,
and let $U$ be the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$. Write $\pi_U(n)$ for the period of $U$ modulo $n$, $\rho_U(n)$ for
the least $s > 0$ with $n \mid U_s$ and $U_{s+1}$ coprime to $n$, $S(U)$ for the set of positive
integers $n$ coprime to $Q$ with $\pi_U(n) \mid n$, $S'(U)$ for the set of $n \in S(U)$ with
$n \mid U_1 + \dots + U_n$, and $T(U)$ for the set of positive integers $n$ coprime to $Q$ with
$n \mid U_n$. Say that a natural number $x$ has integral averages if $x \mid w_1 + \dots + w_x$
for every integer sequence $(w_k)_{k \ge 0}$ with $w_{k+2} = P w_{k+1} - Q w_k$ for all $k$.
Then $\pi_U(n) = \rho_U(n)$ for every $n > 0$ coprime to $Q$; $mn$ has integral averages for all
$n > 0$ dividing $Q$ and all $m \in S'(U)$; and $S(U) = T(U)$. If $P$ is odd, then
$S'(U) = S(U)$, every $n \in S(U)$ and every $n > 0$ dividing $Q$ has integral averages, and if
moreover $P = 3$, then $P^2 - 4Q = 1$ and $S(U) = \{1\}$. If $P$ is even, then $S'(U)$ consists
of the odd elements of $S(U)$, every odd $n \in S(U)$ has integral averages, and if
$P = 2 + 2^k$ for some $k \ge 1$, then no $n > 1$ lies in $S'(U)$.

In the paper's notation $a = P$ and $b = -Q$, so the hypothesis is $b = -a + 1$, and the paper's
$E_U(n) = 1$ is $\pi_U(n) = \rho_U(n)$; the paper's conditions $a \ne 0, 1, 2$ follow from
nondegeneracy. The paper's condition on even $a$ is read as $a = 2 + 2^k$ (the exponent is set as
a superscript); the linear reading $a = 2 + 2k$ is false: for $a = 8$ ($b = -7$) one has
$\pi_U(3) = 3$ and $3 \mid U_1 + U_2 + U_3 = 1 + 8 + 57 = 66$, so $3 \in S'(U)$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.26.

Stated but not proved: `MetaMathlibExt.lucasAverageSet_of_p_eq_q_add_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1275](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-average-set-of-p-eq-q-add-one).

## Period and average sets when $P = -Q - 1$

Let $P$ and $Q \ne 0$ be integers forming a
nondegenerate Lucas pair with $P = -Q - 1$, so that the roots of $x^2 - Px + Q$ are $-Q$ and $-1$,
and let $U$ be the Lucas sequence given by $U_0 = 0$, $U_1 = 1$ and
$U_{k+2} = P U_{k+1} - Q U_k$. Write $\pi_U(n)$ for the period of $U$ modulo $n$, $S(U)$ for the
set of positive integers $n$ coprime to $Q$ with $\pi_U(n) \mid n$, $S'(U)$ for the set of
$n \in S(U)$ with $n \mid U_1 + \dots + U_n$, and $T(U)$ for the set of positive integers $n$
coprime to $Q$ with $n \mid U_n$. Say that a natural number $x$ has integral averages if
$x \mid w_1 + \dots + w_x$ for every integer sequence $(w_k)_{k \ge 0}$ with
$w_{k+2} = P w_{k+1} - Q w_k$ for all $k$. Then $\pi_U(n)$ is even for every $n > 1$ coprime to
$Q$; if $Q$ is even, every even natural number $n$ dividing $Q$ has integral averages; if $P$ is
even, then $n \nmid U_1 + \dots + U_n$ for every $n > 1$ in $S(U)$, and $S'(U) = \{1\}$; and if
$P$ is odd, then $S(U) = \{1\}$, $Q$ is even, and for every even $m$ dividing $Q$ and every
$t \in T(U)$, $t$ is odd and $mt$ has integral averages.

In the paper's notation $a = P$ and $b = -Q$, so the hypothesis is $a = b - 1$; the paper's
conditions $a \ne 0, -1, -2$ follow from nondegeneracy.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 2.27.

Stated but not proved: `MetaMathlibExt.lucasAverageSet_of_p_eq_neg_q_sub_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-average-set-of-p-eq-neg-q-sub-one).

## Smyth's description of the indices $n$ with $n \mid U_n$

Let $P, Q$ be coprime integers
with $Q \ne 0$ such that the Lucas pair $(P, Q)$ is nondegenerate, let $U = U(P, Q)$ be its Lucas
sequence, write $a = P$, $b = -Q$ (so that $U_{k+2} = a U_{k+1} + b U_k$) and $D = P^2 - 4Q$, and
let $T(U)$ be the set of positive integers $n$ coprime to $Q$ with $n \mid U_n$. Call $q_0$
admissible if $q_0 = 1$, or $q_0 = 6$ with $a \equiv 3$ and $b \equiv \pm 1 \pmod 6$, or
$q_0 = 12$ with $a \equiv \pm 1$ and $b \equiv 1 \pmod 6$. Call a finite list of primes
$q_1, \dots, q_r$ ($r \ge 0$, repetitions allowed) a chain from $q_0$ if
$q_i \mid D \, U_{q_0 q_1 \cdots q_{i-1}}$ for each $i$. Then every admissible $q_0$ lies in
$T(U)$; a natural number $n$ lies in $T(U)$ if and only if $n = q_0 q_1 \cdots q_r$ for some
admissible $q_0$ and some chain $q_1, \dots, q_r$ from $q_0$; for every admissible $q_0$ and every
chain $q_1, \dots, q_r$ from $q_0$, each product $q_0 q_1 \cdots q_i$ with $0 \le i \le r$ lies in
$T(U)$; and if $D = 1$, then $T(U) = \{1\}$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 4.1.

Stated but not proved: `MetaMathlibExt.mem_lucasIndexDivisibleSet_iff_chain` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#mem-lucas-index-divisible-set-iff-chain).

## Period quotients and seeds of $S(U)$

Let $U = U(P, Q)$ be a nondegenerate Lucas
sequence with $Q = -1$, or $Q = 1$, or $Q$ odd and $P = -Q - 1$. Write $\pi_U(m)$ and
$\rho_U(m)$ for the least period and the least restricted period of $U$ modulo $m$, and $S(U)$
for the set of positive integers $n$ coprime to $Q$ with $\pi_U(n) \mid n$. For every prime
$p \nmid Q$, $\rho_U(p)$ divides $\pi_U(p)$, and the quotient $\pi_U(p) / \rho_U(p)$ divides $4$
if $Q = -1$ and divides $2$ if $Q \ne -1$. Moreover, each of the following numbers $s_0$ lies in
$S(U)$: $s_0 = 1$; $s_0 = 6$ if $P \equiv 3 \pmod 6$ and $Q = -1$, or if $P \equiv \pm 1 \pmod 6$
and $Q = 1$; $s_0 = 24$ if $P \equiv \pm 1 \pmod 6$ and $Q = -1$; $s_0 = 12$ if
$P \equiv 3 \pmod 6$ and $Q = 1$; $s_0 = 2$ if $Q$ is odd and $P = -Q - 1$.

In the paper's notation $W(n + 2) = a W(n + 1) + b W(n)$ one has $a = P$ and $b = -Q$. The
paper also characterizes $S(U)$ by chains $n_0 = s_0$, $n_i = n_{i-1} s_i 2^{\varepsilon(s_i)}$
with primes $s_i \mid D U_{n_{i-1}}$, where $D = P^2 - 4Q$ and
$\varepsilon(s_i) = \max(\nu_2(\pi_U(s_i)) - \nu_2(n_{i-1}), 0)$; that characterization is
false as printed in both directions and is omitted. For $(P, Q) = (-10, 1)$ only $s_0 = 1$ is
admissible and $\pi_U(2) = 2$, so $2 \in S(U)$, but the only chain that could end at $2$ has
$s_1 = 2$, and then $\varepsilon(2) = \nu_2(\pi_U(2)) = 1$ gives $n_1 = 4$. For
$(P, Q) = (-11, 1)$, where $D = 117$, the chain $s_0 = 1$, $s_1 = 13$,
$s_2 = 53 \mid U_{13} = 2862615066961$ gives $\varepsilon(53) = \nu_2(26) = 1$ and
$n_2 = 1378$, while $\pi_U(1378) = 78 \nmid 1378$.

## Sources

- Michal Křížek and Lawrence Somer, *Period Lengths Modulo n and Average of Terms of Second Order Linear Recurrences*, INTEGERS 24 (2024), Article A36, Theorem 4.3.

Stated but not proved: `MetaMathlibExt.lucasUPeriod_quotient_dvd_and_seed_mem_lucasPeriodSet` is written with `theorem_wanted` in [WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean, line 1356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/Recurrences/LucasPeriodAverageWanted.lean#L1356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html#lucas-uperiod-quotient-dvd-and-seed-mem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Periods and averages of Lucas sequences modulo n](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/recurrences-modulo-m/periods-and-averages-of-lucas-sequences-modulo-n)
