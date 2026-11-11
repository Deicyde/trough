---
declaration: section
origin: cited
lean: MetaMathlibExt.degenerateHarmonicTerm, MetaMathlibExt.degenerateHarmonicTerm_zero, MetaMathlibExt.degenerateHarmonicTerm_one, MetaMathlibExt.generalizedDegenerateHarmonic, MetaMathlibExt.generalizedDegenerateHarmonic_zero, MetaMathlibExt.generalizedDegenerateHarmonic_succ, MetaMathlibExt.generalizedDegenerateHyperharmonic, MetaMathlibExt.generalizedDegenerateHyperharmonic_succ_zero
statement: formalized
---

# Degenerate harmonic numbers and Riordan arrays

33 results, 24 proved and 9 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html).

## Degenerate harmonic terms

For real numbers $\lambda$ and $\alpha$ and a natural number
$n$, the degenerate harmonic term is $0$ when $n = 0$ and
$(-1)^{n-1} \binom{\lambda}{n} / (\lambda \alpha^n)$ when $n \ge 1$, where
$\binom{\lambda}{n} = \lambda(\lambda - 1)\cdots(\lambda - n + 1)/n!$.

These are the coefficients of $t^n$ in $-\log_\lambda(1 - t/\alpha)$, where
$\log_\lambda(1 + t) = \sum_{n \ge 1} \binom{\lambda}{n} t^n / \lambda$; the series has no constant
term. For $n \ge 1$ the term is the paper's $H^0_{n,\lambda}(\alpha)$; at $n = 0$ the value $0$
follows the paper's convention $H^r_{0,\lambda}(\alpha) = 0$ and the generating function.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1 (`H⁰_{n,λ}(α)` and Equation (2)).

Formalized by `MetaMathlibExt.degenerateHarmonicTerm`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-term).

## Degenerate harmonic term of index zero

For all real $\lambda$ and $\alpha$, the
degenerate harmonic term of index $0$, $H^0_{0,\lambda}(\alpha)$, is $0$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.degenerateHarmonicTerm_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-term-zero).

## Degenerate harmonic term of index one

For every real $\lambda \ne 0$ and every real
$\alpha$, the degenerate harmonic term of index $1$,
$H^0_{1,\lambda}(\alpha) = \binom{\lambda}{1} / (\lambda \alpha)$, equals $1/\alpha$.

At $\alpha = 0$ both sides are $0$, under the convention that a quotient by $0$ is $0$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.degenerateHarmonicTerm_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-term-one).

## Generalized degenerate harmonic numbers

For real numbers $\lambda$ and $\alpha$ and a
natural number $n$, Dağlı's generalized degenerate harmonic number is

$$
H_{n,\lambda}(\alpha) = \sum_{k=1}^{n} \frac{(-1)^{k-1} \binom{\lambda}{k}}{\lambda\, \alpha^k},
$$

where $\binom{\lambda}{k} = \lambda(\lambda - 1)\cdots(\lambda - k + 1)/k!$; in particular
$H_{0,\lambda}(\alpha) = 0$. At $\alpha = 1$ these are the degenerate harmonic numbers
$H_{n,\lambda}$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.generalizedDegenerateHarmonic`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#generalized-degenerate-harmonic).

## The zeroth generalized degenerate harmonic number

For all real numbers $\lambda$ and
$\alpha$, the generalized degenerate harmonic number $H_{0,\lambda}(\alpha)$ is $0$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.generalizedDegenerateHarmonic_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#generalized-degenerate-harmonic-zero).

## Recurrence for generalized degenerate harmonic numbers

For all real numbers $\lambda$ and
$\alpha$ and every natural number $n$, the generalized degenerate harmonic numbers satisfy

$$
H_{n+1,\lambda}(\alpha) = H_{n,\lambda}(\alpha) +
\frac{(-1)^n \binom{\lambda}{n+1}}{\lambda\, \alpha^{n+1}},
$$

where $\binom{\lambda}{n+1} = \lambda(\lambda - 1)\cdots(\lambda - n)/(n+1)!$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.generalizedDegenerateHarmonic_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#generalized-degenerate-harmonic-succ).

## Generalized degenerate hyperharmonic numbers

For real numbers $\lambda$ and $\alpha$,
the generalized degenerate hyperharmonic numbers $H^r_{n,\lambda}(\alpha)$, indexed by natural
numbers $r$ (the order) and $n$, are defined by recursion on $r$. At order $0$ they are the
degenerate harmonic terms: $H^0_{0,\lambda}(\alpha) = 0$ and
$H^0_{n,\lambda}(\alpha) = (-1)^{n-1} \binom{\lambda}{n} / (\lambda \alpha^n)$ for $n \ge 1$,
where $\binom{\lambda}{n}$ is the generalized binomial coefficient. For every order $r$,
$H^{r+1}_{n,\lambda}(\alpha) = \sum_{k=1}^{n} H^r_{k,\lambda}(\alpha)$.

In particular $H^r_{0,\lambda}(\alpha) = 0$ for $r \ge 1$, and $H^1_{n,\lambda}(\alpha)$ is the
generalized degenerate harmonic number
$H_{n,\lambda}(\alpha) = \sum_{k=1}^{n} (-1)^{k-1} \binom{\lambda}{k} / (\lambda \alpha^k)$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.generalizedDegenerateHyperharmonic`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#generalized-degenerate-hyperharmonic).

## Generalized degenerate hyperharmonic numbers of positive order vanish at zero

For all
real numbers $\lambda$ and $\alpha$ and every natural number $r$, the generalized degenerate
hyperharmonic number of order $r + 1$ at index $0$ is zero: $H^{r+1}_{0,\lambda}(\alpha) = 0$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.generalizedDegenerateHyperharmonic_succ_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#generalized-degenerate-hyperharmonic-suc).

## Generalized degenerate hyperharmonic numbers of order one

For all real numbers
$\lambda$ and $\alpha$ and every natural number $n$, the generalized degenerate hyperharmonic
number of order $1$ equals the generalized degenerate harmonic number:
$H^1_{n,\lambda}(\alpha) = H_{n,\lambda}(\alpha)$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.generalizedDegenerateHyperharmonic_one`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#generalized-degenerate-hyperharmonic-one).

## Generalized degenerate harmonic numbers of a given rank

For real $\lambda$ and $\alpha$,
let $\ell_0 = 0$ and $\ell_m = (-1)^{m-1} \binom{\lambda}{m} / (\lambda \alpha^m)$ for $m \ge 1$,
where $\binom{\lambda}{m}$ is the generalized binomial coefficient and a quotient by $0$ is read
as $0$, and let $L(t) = \sum_{m \ge 0} \ell_m t^m$ as a formal power series. For
$\lambda, \alpha > 0$ this is the expansion of $-\log_\lambda(1 - t/\alpha)$, where
$\log_\lambda(1 + t) = ((1 + t)^\lambda - 1)/\lambda$ is the degenerate logarithm. For natural
numbers $n$ and $r$, the generalized degenerate harmonic number of rank $r$, written
$H_\lambda(n, r, \alpha)$, is the sum of the coefficients of $t^0, t^1, \dots, t^n$ in
$L(t)^{r+1}$. Equivalently, $\sum_{n \ge 0} H_\lambda(n, r, \alpha) t^n = L(t)^{r+1} / (1 - t)$.

Expanding the power, $H_\lambda(n, r, \alpha)$ is the sum of $\ell_{k_0} \cdots \ell_{k_r}$ over
all $k_0, \dots, k_r \ge 1$ with $k_0 + \cdots + k_r \le n$, which is the explicit definition in
the source.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1, Equation (5).

Formalized by `MetaMathlibExt.degenerateHarmonicRank`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank).

## Degenerate harmonic numbers of rank vanish at index zero

For all real $\lambda$ and
$\alpha$ and every natural number $r$, the generalized degenerate harmonic number of rank $r$
satisfies $H_\lambda(0, r, \alpha) = 0$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.degenerateHarmonicRank_zero_left`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-zero-left).

## Degenerate harmonic numbers of rank zero

For all real $\lambda$ and $\alpha$ and every
natural number $n$, the generalized degenerate harmonic number of rank $0$ equals the generalized
degenerate harmonic number: $H_\lambda(n, 0, \alpha) = H_{n,\lambda}(\alpha)$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Section 1.

Formalized by `MetaMathlibExt.degenerateHarmonicRank_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-zero-right).

## Degenerate exponential series

For a real number $\lambda$, the degenerate exponential
series is the formal power series $e_\lambda(t) = \sum_{n \ge 0} (1)_{n,\lambda} \, t^n / n!$
over $\mathbb{R}$, where $(1)_{0,\lambda} = 1$ and, for $n \ge 1$,
$(1)_{n,\lambda} = 1 \cdot (1 - \lambda) \cdots (1 - (n - 1)\lambda)$ is the generalized falling
factorial of $1$ with increment $\lambda$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (1) at `x = 1`.

Formalized by `MetaMathlibExt.degenerateExpSeries`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-exp-series).

## Constant term of the degenerate exponential series

For every real number $\lambda$, the
constant term of the degenerate exponential series $e_\lambda(t)$ is $1$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (1).

Formalized by `MetaMathlibExt.constantCoeff_degenerateExpSeries`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#constant-coeff-degenerate-exp-series).

## Degenerate Bernoulli numbers

For a real number $\lambda$, let $(1)_{0,\lambda} = 1$ and
$(1)_{m,\lambda} = 1 \cdot (1 - \lambda) \cdots (1 - (m - 1)\lambda)$ for $m \ge 1$ (the
generalized falling factorial of $1$ with increment $\lambda$). For $n \in \mathbb{N}$, the
degenerate Bernoulli number $\beta_{n,\lambda}$ is $n!$ times the coefficient of $t^n$ in the
inverse of the formal power series $\sum_{m \ge 0} (1)_{m+1,\lambda} \, t^m / (m + 1)!$ over
$\mathbb{R}$, whose constant term is $1$.

Since this power series is $(e_\lambda(t) - 1) / t$ for the degenerate exponential series
$e_\lambda(t)$, the numbers $\beta_{n,\lambda}$ satisfy
$t / (e_\lambda(t) - 1) = \sum_{n \ge 0} \beta_{n,\lambda} \, t^n / n!$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (6).

Formalized by `MetaMathlibExt.degenerateBernoulli`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-bernoulli).

## The zeroth degenerate Bernoulli number

For every real number $\lambda$, the degenerate
Bernoulli number $\beta_{0,\lambda}$ equals $1$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (6).

Formalized by `MetaMathlibExt.degenerateBernoulli_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-bernoulli-zero).

## Degenerate Euler numbers

For a real number $\lambda$ and $n \in \mathbb{N}$, the
degenerate Euler number $\varepsilon_{n,\lambda}$ is $n!$ times the coefficient of $t^n$ in the
formal power series $2 / (e_\lambda(t) + 1)$ over $\mathbb{R}$, where $e_\lambda(t)$ is the
degenerate exponential series; that is,
$2 / (e_\lambda(t) + 1) = \sum_{n \ge 0} \varepsilon_{n,\lambda} \, t^n / n!$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (7).

Formalized by `MetaMathlibExt.degenerateEuler`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-euler).

## The zeroth degenerate Euler number

For every real number $\lambda$, the degenerate Euler
number $\varepsilon_{0,\lambda}$ equals $1$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (7).

Formalized by `MetaMathlibExt.degenerateEuler_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 195](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L195). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-euler-zero).

## Degenerate Stirling numbers of the first kind

For a real number $\lambda$, let
$\log_\lambda(1 + t)$ be the formal power series $\sum_{m \ge 1} \binom{\lambda}{m} t^m / \lambda$,
where $\binom{\lambda}{m} = \lambda(\lambda - 1)\cdots(\lambda - m + 1)/m!$. For natural numbers
$n$ and $k$, the degenerate Stirling number of the first kind $S_{1,\lambda}(n, k)$ is $n!/k!$
times the coefficient of $t^n$ in $(\log_\lambda(1 + t))^k$. Equivalently,
$(\log_\lambda(1 + t))^k / k! = \sum_{n \ge k} S_{1,\lambda}(n, k) t^n / n!$, and
$S_{1,\lambda}(n, k) = 0$ for $n < k$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equations (2) and (8).

Formalized by `MetaMathlibExt.degenerateStirlingFirst`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-stirling-first).

## Degenerate Stirling numbers of the first kind in column zero

For every real number
$\lambda$ and every natural number $n$, the degenerate Stirling number of the first kind
$S_{1,\lambda}(n, 0)$ equals $1$ if $n = 0$ and $0$ otherwise.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (8).

Formalized by `MetaMathlibExt.degenerateStirlingFirst_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-stirling-first-zero-right).

## Degenerate Stirling numbers of the second kind

For a real number $\lambda$, let
$e_\lambda(t) = \sum_{n \ge 0} (1)_{n,\lambda} t^n / n!$ be the degenerate exponential series,
where $(1)_{0,\lambda} = 1$ and $(1)_{n,\lambda} = 1 (1 - \lambda) \cdots (1 - (n - 1)\lambda)$.
For natural numbers $n$ and $k$, the degenerate Stirling number of the second kind
$S_{2,\lambda}(n, k)$ is $n!/k!$ times the coefficient of $t^n$ in $(e_\lambda(t) - 1)^k$.
Equivalently, $(e_\lambda(t) - 1)^k / k! = \sum_{n \ge k} S_{2,\lambda}(n, k) t^n / n!$, and
$S_{2,\lambda}(n, k) = 0$ for $n < k$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (8).

Formalized by `MetaMathlibExt.degenerateStirlingSecond`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-stirling-second).

## Degenerate Stirling numbers of the second kind in column zero

For every real number
$\lambda$ and every natural number $n$, the degenerate Stirling number of the second kind
$S_{2,\lambda}(n, 0)$ equals $1$ if $n = 0$ and $0$ otherwise.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (8).

Formalized by `MetaMathlibExt.degenerateStirlingSecond_zero_right`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-stirling-second-zero-right).

## Degenerate Daehee numbers

For a real number $\lambda$ and $n \in \mathbb{N}$, the
degenerate Daehee number is $D_{n,\lambda} = n! \binom{\lambda}{n+1} / \lambda$, where
$\binom{\lambda}{k} = \lambda (\lambda - 1) \cdots (\lambda - k + 1) / k!$ is the generalized
binomial coefficient (for $\lambda = 0$ the value is $0$, by the convention $x / 0 = 0$).

For $\lambda \ne 0$ the degenerate logarithm $\log_\lambda(1 + t) = ((1 + t)^\lambda - 1) / \lambda$
satisfies $\log_\lambda(1 + t) / t = \sum_{n \ge 0} \binom{\lambda}{n+1} t^n / \lambda$, so the
numbers $D_{n,\lambda}$ are given by
$\log_\lambda(1 + t) / t = \sum_{n \ge 0} D_{n,\lambda} \, t^n / n!$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equations (2) and (9).

Formalized by `MetaMathlibExt.degenerateDaehee`, a definition declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-daehee).

## The zeroth degenerate Daehee number

For every real number $\lambda \ne 0$, the degenerate
Daehee number $D_{0,\lambda}$ equals $1$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Equation (9).

Formalized by `MetaMathlibExt.degenerateDaehee_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 247](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L247). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-daehee-zero).

## Alternating and binomial sums of degenerate hyperharmonic numbers

Let $\lambda > 0$ and
$\alpha > 0$ be real numbers and let $n$ be a natural number. Write $H_{m,\lambda}(\alpha)$ for the
generalized degenerate harmonic numbers, $H^s_{m,\lambda}(\alpha)$ for the generalized degenerate
hyperharmonic numbers of order $s$, and $D_{n,\lambda}$ for the degenerate Daehee numbers. Then

$$
\sum_{k=0}^{n} (-1)^k H^{k+1}_{n-k+1,\lambda}(\alpha) =
\frac{(-1)^n D_{n,\lambda}}{\alpha^{n+1}\, n!},
$$

and for every natural number $r$,

$$
\sum_{k=0}^{n} \binom{k+r}{r} H_{n-k+1,\lambda}(\alpha) = H^{r+2}_{n+1,\lambda}(\alpha).
$$

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 1.

Stated but not proved: `MetaMathlibExt.degenerateHyperharmonic_alternating_and_binomial_sums` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-hyperharmonic-alternating-and).

## Alternating binomial sum of degenerate harmonic numbers

Let $\lambda > 0$ be real and let
$H_{k,\lambda} = H_{k,\lambda}(1)$ be the degenerate harmonic numbers, that is, the generalized
degenerate harmonic numbers at $\alpha = 1$. Then for every integer $n \ge 1$,
$\sum_{k=0}^{n} (-1)^{k+1} \binom{n}{k} H_{k,\lambda} = \binom{n + \lambda - 1}{n} / \lambda$,
where $\binom{n + \lambda - 1}{n}$ is the generalized binomial coefficient.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 2.

Stated but not proved: `MetaMathlibExt.degenerateHarmonic_alternating_binomial_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-alternating-binomial).

## Alternating degenerate exponential sum of degenerate harmonic numbers of rank

Let
$\lambda > 0$ and $\alpha > 0$ be real and let $n$ be a natural number. Write
$(1)_{k,\lambda} = 1 \cdot (1 - \lambda) \cdots (1 - (k-1)\lambda)$ for the generalized falling
factorial (so $(1)_{0,\lambda} = 1$), $H_\lambda(m, r, \alpha)$ for the generalized degenerate
harmonic numbers of rank $r$, and $H_{m,\lambda}(\alpha)$ for the generalized degenerate harmonic
numbers. Then

$$\sum_{k=0}^{n} (-1)^k \frac{(1)_{k,\lambda}}{k!} H_\lambda(n+1, k, \alpha) =
H_{n+1,\lambda}(\alpha) - \frac{H_{n,\lambda}(\alpha)}{\alpha}.$$

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 3.

Stated but not proved: `MetaMathlibExt.degenerateHarmonicRank_exp_weighted_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-exp-weighted-su).

## Partial sums of degenerate harmonic numbers of rank as a convolution

Let $\lambda > 0$
and $\alpha > 0$ be real and let $n$ and $r$ be natural numbers. Write $H_\lambda(k, r, \alpha)$
for the generalized degenerate harmonic numbers of rank $r$ and $H_{m,\lambda}(\alpha)$ for the
generalized degenerate harmonic numbers. Then

$$\sum_{k=0}^{n} H_\lambda(k, r+1, \alpha) =
\sum_{k=0}^{n} H_{n-k,\lambda}(\alpha) \, H_\lambda(k, r, \alpha).$$

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 4.

Stated but not proved: `MetaMathlibExt.degenerateHarmonicRank_succ_partial_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-succ-partial-su).

## Shifted alternating degenerate exponential sum of degenerate harmonic numbers of rank

Let $\lambda > 0$ and $\alpha > 0$ be real and let $n$ be a natural number. Write
$(1)_{k,\lambda} = 1 \cdot (1 - \lambda) \cdots (1 - (k-1)\lambda)$ for the generalized falling
factorial and $H_\lambda(m, r, \alpha)$ for the generalized degenerate harmonic numbers of rank $r$.
Then

$$\sum_{k=0}^{n} (-1)^k \frac{(1)_{k+1,\lambda}}{(k+1)!} H_\lambda(n+1, k, \alpha) =
\frac{1}{\alpha}.$$

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 5.

Stated but not proved: `MetaMathlibExt.degenerateHarmonicRank_shifted_exp_weighted_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-shifted-exp-wei).

## A binomial sum equal to a degenerate hyperharmonic number

Let $\lambda > 0$ and
$\alpha > 0$ be real numbers and let $r \le n$ be natural numbers. Write
$\binom{\lambda}{j} = \lambda(\lambda - 1)\cdots(\lambda - j + 1)/j!$ and $H^s_{m,\lambda}(\alpha)$
for the generalized degenerate hyperharmonic numbers of order $s$. Then

$$
\sum_{k=r}^{n} (-1)^{n-k} \frac{\binom{\lambda}{n-k+1}}{\lambda\, \alpha^{n-k+1}} \binom{k}{r} =
H^{r+1}_{n-r+1,\lambda}(\alpha).
$$

The hypothesis $r \le n$ makes the summation range $r \le k \le n$ nonempty, as in the paper.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 6.

Stated but not proved: `MetaMathlibExt.degenerateHyperharmonic_eq_binomial_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 324](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L324). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-hyperharmonic-eq-binomial-sum).

## Degenerate harmonic numbers of rank and degenerate Stirling numbers of the first kind

Let
$\lambda > 0$ and $\alpha > 0$ be real and let $n \ge 1$ be a natural number. Write
$(1)_{k,\lambda} = 1 \cdot (1 - \lambda) \cdots (1 - (k-1)\lambda)$ for the generalized falling
factorial, $H_\lambda(m, r, \alpha)$ for the generalized degenerate harmonic numbers of rank $r$,
and $S_{1,\lambda}(k, i)$ for the degenerate Stirling numbers of the first kind. Then

$$\sum_{k=1}^{n} \frac{(1)_{k,\lambda}}{k!} H_\lambda(n, k-1, \alpha) =
\sum_{k=1}^{n} \sum_{i=1}^{k} \frac{(-1)^{k+i} (1)_{i,\lambda} S_{1,\lambda}(k, i)}{\alpha^k k!}.$$

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 7.

Stated but not proved: `MetaMathlibExt.degenerateHarmonicRank_exp_sum_eq_stirlingFirst` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-exp-sum-eq-stir).

## Degenerate Bernoulli and Euler sums of higher-rank degenerate harmonic numbers

Let
$\lambda > 0$ and $\alpha > 0$ be real and let $n \ge 1$ be an integer. Write $\beta_{k,\lambda}$
and $\varepsilon_{k,\lambda}$ for the degenerate Bernoulli and Euler numbers,
$H_{m,\lambda}(\alpha)$ for the generalized degenerate harmonic numbers, and
$H_\lambda(m, r, \alpha)$ for the generalized degenerate harmonic numbers of rank $r$. Then
$\sum_{k=1}^{n} (-1)^k \beta_{k,\lambda} H_\lambda(n, k - 1, \alpha) / k! =
\alpha H_{n+1,\lambda}(\alpha) - 1$, and if moreover $\alpha \ne 1/2$, then
$\sum_{k=1}^{n} (-1)^{k+1} \varepsilon_{k,\lambda} H_\lambda(n, k - 1, \alpha) / k! =
((2\alpha)^{-n} - 1) / (2\alpha - 1)$.

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 8.

Stated but not proved: `MetaMathlibExt.degenerateHarmonicRank_bernoulli_euler_sums` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-bernoulli-euler).

## Degenerate harmonic numbers of rank and degenerate Stirling numbers of the second kind

Let $\lambda > 0$ and $\alpha > 0$ be real and let $m$ and $n$ be natural numbers with
$1 \le m \le n$. Write $S_{2,\lambda}(k, m)$ for the degenerate Stirling numbers of the second kind
and $H_\lambda(n, r, \alpha)$ for the generalized degenerate harmonic numbers of rank $r$. Then

$$\sum_{k=m}^{n} \frac{(-1)^k S_{2,\lambda}(k, m) H_\lambda(n, k-1, \alpha)}{k!} =
\frac{(-1)^m}{m! \, \alpha^m}.$$

## Sources

- Ömer Duran, Neşe Ömür and Sibel Koparal, *Generalized Degenerate Harmonic Numbers and Their Applications with Riordan Arrays*, INTEGERS 24 (2024), Article A41, Theorem 9.

Stated but not proved: `MetaMathlibExt.degenerateHarmonicRank_stirlingSecond_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean, line 371](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/DegenerateHarmonicRiordanWanted.lean#L371). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html#degenerate-harmonic-rank-stirling-second).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Degenerate harmonic numbers and Riordan arrays](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/riordan-arrays-transforms/riordan-arrays/degenerate-harmonic-numbers-and-riordan-arrays)
