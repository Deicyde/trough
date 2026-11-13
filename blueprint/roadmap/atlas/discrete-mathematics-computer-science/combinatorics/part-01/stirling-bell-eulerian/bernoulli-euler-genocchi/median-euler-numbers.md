---
declaration: section
origin: cited
lean: MetaMathlibExt.medianEulerCoefficients, MetaMathlibExt.medianEulerCoeff, MetaMathlibExt.medianEulerInitialRow, MetaMathlibExt.medianEulerNumber, MetaMathlibExt.medianEulerCoeff_zero, MetaMathlibExt.medianEulerCoeff_succ, MetaMathlibExt.medianEulerCoeff_egf, MetaMathlibExt.medianEulerNumber_div_three_and_modFive
statement: formalized
proof: formalized
---

# Median Euler numbers

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html).

## The list of the first Euler coefficients

Let $\varepsilon_N$ be $1$ if $N$ is odd and $0$
if $N$ is even. For each natural number $n$, this is the list $[c_0, c_1, \dots, c_n]$ of integers
with $c_0 = 1$ and, for $1 \le N \le n$, $c_N = \varepsilon_N - \sum_j \binom{N}{j} c_{N-j}$, where
the sum runs over the even $j$ with $2 \le j \le N$. The Euler coefficient $E_n$ is its last entry
$c_n$. The list is built one entry at a time, so each step reuses the earlier values.

The recurrence comes from $\cosh x \cdot (\operatorname{sech} x + \tanh x) = 1 + \sinh x$.

Formalized by `MetaMathlibExt.medianEulerCoefficients`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-coefficients).

## Euler coefficients

Let $\varepsilon_n$ be $1$ if $n$ is odd and $0$ if $n$ is even. The
Euler coefficients $E_n$ are the integers defined by $E_0 = 1$ and, for $n \ge 1$,
$E_n = \varepsilon_n - \sum_j \binom{n}{j} E_{n-j}$, where the sum runs over the even $j$ with
$2 \le j \le n$.

They are the coefficients in $\operatorname{sech} x + \tanh x = \sum_{n \ge 0} E_n x^n / n!$: the
recurrence compares coefficients in $\cosh x \cdot (\operatorname{sech} x + \tanh x) = 1 + \sinh x$.
The first values are $1, 1, -1, -2, 5, 16, -61$.

Formalized by `MetaMathlibExt.medianEulerCoeff`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-coeff).

## Initial row for the median Euler numbers

Let $E_m$ denote the Euler coefficients. This is
the integer sequence $(a_m)_{m \ge 0}$ with $a_0 = 0$ and $a_m = E_m$ for $m \ge 1$. It is the
initial row of the Euler–Seidel matrix from which the median Euler numbers are read off.

Formalized by `MetaMathlibExt.medianEulerInitialRow`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-initial-row).

## Median Euler numbers

Let $E_m$ denote the Euler coefficients, and let $(a_n^k)$ be the
Euler–Seidel matrix of the initial row $a_0 = 0$, $a_m = E_m$ for $m \ge 1$, so that $a_n^0 = a_n$
and $a_n^{k+1} = a_n^k + a_{n+1}^k$. The median Euler number $R_n$ is the natural number
$|a_{n+1}^n|$. Equivalently, $R_n = \left|\sum_{i=0}^{n} \binom{n}{i} E_{n+1+i}\right|$.

The first values are $R_0 = 1$, $R_1 = 3$, $R_2 = 24$ and $R_3 = 402$.

Formalized by `MetaMathlibExt.medianEulerNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-number).

## The zeroth Euler coefficient

The Euler coefficient $E_0$ equals $1$.

Formalized by `MetaMathlibExt.medianEulerCoeff_zero`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-coeff-zero).

## Recurrence for the Euler coefficients

Let $E_m$ denote the Euler coefficients, and let
$\varepsilon_m$ be $1$ if $m$ is odd and $0$ if $m$ is even. For every natural number $n$,
$E_{n+1} = \varepsilon_{n+1} - \sum_j \binom{n+1}{j} E_{n+1-j}$, where the sum runs over the even
$j$ with $2 \le j \le n+1$.

It comes from comparing coefficients in
$\cosh x \cdot (\operatorname{sech} x + \tanh x) = 1 + \sinh x$.

Formalized by `MetaMathlibExt.medianEulerCoeff_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 121](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L121). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-coeff-succ).

## Exponential generating function of the Euler coefficients

Let $E_n$ denote the Euler
coefficients, let $e^x$ be the exponential series, and let $e^{-x}$ be the series obtained from
it by replacing $x$ with $-x$. In the ring $\mathbb{Q}[[x]]$ of formal power series with rational
coefficients, $(e^x + e^{-x}) \sum_{n \ge 0} E_n x^n / n! = 2 + e^x - e^{-x}$.

Since $e^x + e^{-x} = 2 \cosh x$ and $2 + e^x - e^{-x} = 2 (1 + \sinh x)$, and $\cosh x$ is
invertible, this says that the exponential generating function of the $E_n$ is
$\operatorname{sech} x + \tanh x$.

Formalized by `MetaMathlibExt.medianEulerCoeff_egf`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 261](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L261). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-coeff-egf).

## Median Euler numbers modulo three and five

For every natural number $n \ge 1$, the median
Euler number $R_n$ is divisible by $3$, and $R_n / 3 \equiv 3^{n-1} \pmod 5$.

Formalized by `MetaMathlibExt.medianEulerNumber_div_three_and_modFive`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean, line 1219](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/MedianEulerNumber.lean#L1219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html#median-euler-number-div-three-and-mod-fi).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Median Euler numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bernoulli-euler-genocchi/median-euler-numbers)
