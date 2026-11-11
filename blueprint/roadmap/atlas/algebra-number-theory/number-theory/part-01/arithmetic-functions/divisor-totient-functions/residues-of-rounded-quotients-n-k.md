---
declaration: section
origin: cited
lean: MetaMathlibExt.floorQuotientOddCount, MetaMathlibExt.floorQuotientOddCount_ten, MetaMathlibExt.ceilQuotientOddCount, MetaMathlibExt.ceilQuotientOddCount_nine, MetaMathlibExt.roundQuotientOddCount, MetaMathlibExt.roundQuotientOddCount_ten, MetaMathlibExt.shiftedFloorResidueCount, MetaMathlibExt.shiftedFloorResidueCount_modulus_one
statement: formalized
---

# Residues of rounded quotients n/k

40 results, 8 proved and 32 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html).

## Floor sequence parity count

For a natural number $n$, the floor sequence parity count
$\mathcal{F}_n$ is the number of integers $k$ with $1 \le k \le n$ for which
$\lfloor n/k \rfloor$ is odd (OEIS A059851).

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Section 1 (definition of `𝓕_n`).

Formalized by `MetaMathlibExt.floorQuotientOddCount`, a definition declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#floor-quotient-odd-count).

## The floor sequence parity count at $10$

The number $\mathcal{F}_{10}$ of integers $k$
with $1 \le k \le 10$ for which $\lfloor 10/k \rfloor$ is odd equals $7$: the quotients
$\lfloor 10/k \rfloor$ for $k = 1, \dots, 10$ are $10, 5, 3, 2, 2, 1, 1, 1, 1, 1$, and seven of
them are odd.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Section 1 and Figure 1.

Formalized by `MetaMathlibExt.floorQuotientOddCount_ten`, a theorem declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#floor-quotient-odd-count-ten).

## Ceiling parity count

For a natural number $n$, the ceiling parity count $\mathcal{C}_n$
is the number of integers $k$ with $1 \le k \le n$ for which $\lceil n/k \rceil$ is odd
(OEIS A330926).

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Section 1 (definition of `𝓒_n`).

Formalized by `MetaMathlibExt.ceilQuotientOddCount`, a definition declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#ceil-quotient-odd-count).

## The ceiling parity count at $9$

The ceiling parity count $\mathcal{C}_9$, the number of
integers $k$ with $1 \le k \le 9$ for which $\lceil 9/k \rceil$ is odd, equals $5$.

The ceilings $\lceil 9/k \rceil$ for $k = 1, \dots, 9$ are $9, 5, 3, 3, 2, 2, 2, 2, 1$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Figure 1.

Formalized by `MetaMathlibExt.ceilQuotientOddCount_nine`, a theorem declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#ceil-quotient-odd-count-nine).

## Rounding sequence parity count

For a natural number $n$, the rounding sequence parity
count $\mathcal R_n$ is the number of integers $k$ with $1 \le k \le n$ for which the nearest
integer to $n/k$ is odd, where half-integers are rounded up: the nearest integer to a rational
number $x$ is taken to be $\lfloor x + 1/2 \rfloor$.

Rounding half-integers up is the paper's convention for $\mathrm{nint}$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Section 1 (definition of `𝓡_n` and the footnote on `nint`).

Formalized by `MetaMathlibExt.roundQuotientOddCount`, a definition declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#round-quotient-odd-count).

## The rounding sequence parity count at $10$

The number $\mathcal{R}_{10}$ of integers $k$
with $1 \le k \le 10$ for which the nearest integer to $10/k$ (half-integers rounded up) is odd
equals $7$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Figure 1.

Formalized by `MetaMathlibExt.roundQuotientOddCount_ten`, a theorem declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#round-quotient-odd-count-ten).

## Residue counts of the shifted floor sequence

For a natural number $n$, real numbers
$\alpha$ and $\nu$, an integer $r$ and a natural number $m$, the count
$\mathcal N_{n,\alpha,\nu,r,m}$ is the number of integers $k$ with $1 \le k \le n$ such that
$\lfloor (n - \nu)/k + \alpha \rfloor \equiv r \pmod m$. In other words, it counts the terms of
the $\alpha$-shifted, $\nu$-offset floor sequence
$\lfloor (n - \nu)/1 + \alpha \rfloor, \dots, \lfloor (n - \nu)/n + \alpha \rfloor$ that are
congruent to $r$ modulo $m$, where congruence modulo $0$ means equality.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Section 4 (definition of `𝓝_{n,α,ν,r,m}`).

Formalized by `MetaMathlibExt.shiftedFloorResidueCount`, a definition declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-residue-count).

## Every term is counted modulo one

For a natural number $n$, real numbers $\alpha$ and
$\nu$, an integer $r$ and a natural number $m$, let $\mathcal N_{n,\alpha,\nu,r,m}$ be the number
of integers $k$ with $1 \le k \le n$ such that
$\lfloor (n - \nu)/k + \alpha \rfloor \equiv r \pmod m$. Then $\mathcal N_{n,\alpha,\nu,r,1} = n$
for every natural number $n$, all real numbers $\alpha$ and $\nu$ and every integer $r$.

This is the remark after equation (4.2) of the paper.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Section 4.

Formalized by `MetaMathlibExt.shiftedFloorResidueCount_modulus_one`, a theorem declared in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-residue-count-modulus-one).

## Counting large terms of the floor sequence

For every natural number $n$ and every
integer $k \ge 1$, exactly $\lfloor n/k \rfloor$ of the integers $d$ with $1 \le d \le n$
satisfy $\lfloor n/d \rfloor \ge k$; that is, exactly $\lfloor n/k \rfloor$ terms of the floor
sequence $\lfloor n/1 \rfloor, \dots, \lfloor n/n \rfloor$ are at least $k$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Lemma 1 (`jis-2024-24.2.5-lem-1`).

Stated but not proved: `MetaMathlibExt.floor_div_sequence_card_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#floor-div-sequence-card-ge).

## The floor parity count as an alternating sum

Let $\mathcal{F}_n$ be the number of
integers $k$ with $1 \le k \le n$ for which $\lfloor n/k \rfloor$ is odd. For every natural
number $n$, $\mathcal{F}_n = \sum_{d=1}^{n} \lfloor n/d \rfloor (-1)^{d+1}$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 2 (`jis-2024-24.2.5-prop-2`).

Stated but not proved: `MetaMathlibExt.floorQuotientOddCount_eq_alternating_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#floor-quotient-odd-count-eq-alternating).

## The floor parity count through the divisor summatory function

Let $\tau(m)$ be the
number of positive divisors of $m$, let $D(x) = \sum_{1 \le m \le x} \tau(m)$, and let
$\mathcal{F}_n$ be the number of integers $k$ with $1 \le k \le n$ for which
$\lfloor n/k \rfloor$ is odd. For every natural number $n$, $\mathcal{F}_n = D(n) - 2D(n/2)$,
where $D(n/2) = D(\lfloor n/2 \rfloor)$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 3 (`jis-2024-24.2.5-cor-3`).

Stated but not proved: `MetaMathlibExt.floorQuotientOddCount_eq_divisor_summatory_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#floor-quotient-odd-count-eq-divisor-summ).

## Odd floor quotients as a hyperbolic lattice-point difference

For every natural number
$n$, the floor sequence parity count $\mathcal{F}_n$ equals the number of integer pairs $(x, y)$
with $x, y \ge 1$ and $n/2 < xy \le n$ minus the number of integer pairs $(x, y)$ with
$x, y \ge 1$ and $xy \le n/2$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 4 (`jis-2024-24.2.5-prop-4`).

Stated but not proved: `MetaMathlibExt.floorQuotientOddCount_eq_hyperbolic_lattice_difference` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 139](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L139). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#floor-quotient-odd-count-eq-hyperbolic-l).

## Dirichlet's asymptotic for the divisor summatory function

Let $\tau(m)$ be the number of
positive divisors of $m$, let $D(x) = \sum_{1 \le m \le x} \tau(m)$ for real $x$, and let
$\gamma$ be the Euler–Mascheroni constant. There is a real constant $C$ such that
$|D(x) - (x \log x + (2\gamma - 1)\, x)| \le C \sqrt{x}$ for every real $x \ge 1$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Theorem 6 (`jis-2024-24.2.5-thm-6`).

Stated but not proved: `MetaMathlibExt.divisor_summatory_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#divisor-summatory-asymptotic).

## Asymptotics of the floor parity count

Let $\mathcal{F}_n$ be the number of integers $k$
with $1 \le k \le n$ for which $\lfloor n/k \rfloor$ is odd. There is a real constant $C$ such
that $|\mathcal{F}_n - n \log 2| \le C \sqrt{n}$ for every integer $n \ge 1$, and
$\mathcal{F}_n / n \to \log 2$ as $n \to \infty$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 7 (`jis-2024-24.2.5-prop-7`).

Stated but not proved: `MetaMathlibExt.floorQuotientOddCount_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#floor-quotient-odd-count-asymptotic).

## Ceiling parity count from the floor parity count

For a natural number $m$, let
$\mathcal{C}_m$ and $\mathcal{F}_m$ be the numbers of integers $k$ with $1 \le k \le m$ for which
$\lceil m/k \rceil$, respectively $\lfloor m/k \rfloor$, is odd. Then for every natural number
$n$, $\mathcal{C}_{n+1} = (n + 1) - \mathcal{F}_n$.

The source prints a second equality $\mathcal{C}_n = \sum_{d=2}^{n} \lfloor n/d \rfloor (-1)^d$,
which is not part of this statement: it fails at $n = 3$, where $\mathcal{C}_3 = 2$ but the sum
is $1 - 1 = 0$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 9 (`jis-2024-24.2.5-prop-9`).

Stated but not proved: `MetaMathlibExt.ceilQuotientOddCount_succ_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#ceil-quotient-odd-count-succ-eq).

## Asymptotics of the ceiling parity count

Let $\mathcal{C}_n$ be the number of integers
$k$ with $1 \le k \le n$ for which $\lceil n/k \rceil$ is odd. There is a real constant $C$ such
that $|\mathcal{C}_n - (1 - \log 2)\, n| \le C \sqrt{n}$ for every integer $n \ge 1$, and
$\mathcal{C}_n / n \to 1 - \log 2$ as $n \to \infty$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 10 (`jis-2024-24.2.5-cor-10`).

Stated but not proved: `MetaMathlibExt.ceilQuotientOddCount_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#ceil-quotient-odd-count-asymptotic).

## Square-root bound for the number of divisors

For every natural number $n$, the number
of positive divisors of $n$ is at most $2\sqrt{n}$. For $n = 0$ the set of divisors is taken to
be empty, so the bound holds trivially.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Lemma 12 (`jis-2024-24.2.5-lem-12`).

Stated but not proved: `MetaMathlibExt.card_divisors_le_two_mul_sqrt` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-divisors-le-two-mul-sqrt).

## Counting large terms of the rounded quotient sequence

Let $n$ be a natural number.
Every $d$ with $1 \le d \le n$ satisfies $\lfloor n/d + 1/2 \rfloor \ge 1$, and for every
integer $k \ge 2$ the number of $d$ with $1 \le d \le n$ and $\lfloor n/d + 1/2 \rfloor \ge k$
is $\lfloor 2n/(2k-1) \rfloor$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Lemma 13 (`jis-2024-24.2.5-lem-13`).

Stated but not proved: `MetaMathlibExt.round_div_sequence_card_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#round-div-sequence-card-ge).

## Alternating-sum formula for the rounding sequence parity count

For every natural
number $n$, the rounding sequence parity count $\mathcal{R}_n$ satisfies
$\mathcal{R}_n = -n + \sum_{d=1}^{n} (-1)^{d+1} \lfloor 2n/(2d-1) \rfloor$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 14 (`jis-2024-24.2.5-prop-14`).

Stated but not proved: `MetaMathlibExt.roundQuotientOddCount_eq_alternating_sum` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#round-quotient-odd-count-eq-alternating).

## Divisor-sum formula for the rounding sequence parity count

For a positive integer $k$
and $r \in \{1, 3\}$, let $d_{r,4}(k)$ be the number of positive divisors of $k$ congruent to
$r$ modulo $4$. Then for every natural number $n$, the rounding sequence parity count
$\mathcal{R}_n$ satisfies $\mathcal{R}_n = -n + \sum_{k=1}^{2n} (d_{1,4}(k) - d_{3,4}(k))$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Lemma 15 (`jis-2024-24.2.5-lem-15`).

Stated but not proved: `MetaMathlibExt.roundQuotientOddCount_eq_sum_divisor_difference` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#round-quotient-odd-count-eq-sum-divisor).

## Jacobi's formula for the number of representations as a sum of two squares

For every
integer $n \ge 1$, the number $r_2(n)$ of pairs $(a, b) \in \mathbb{Z}^2$ with $a^2 + b^2 = n$
equals $4\,(d_{1,4}(n) - d_{3,4}(n))$, where $d_{r,4}(n)$ is the number of positive divisors of
$n$ congruent to $r$ modulo $4$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Theorem 16 (`jis-2024-24.2.5-thm-16`).

Stated but not proved: `MetaMathlibExt.card_sq_add_sq_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 242](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L242). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-sq-add-sq-eq).

## Lattice points in the disc of radius $\sqrt{2n}$

For every natural number $n$, the
number of pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + y^2 \le 2n$ equals
$4\,\mathcal{R}_n + 4n + 1$, where $\mathcal{R}_n$ is the number of $k \in \{1, \dots, n\}$ for
which the nearest integer to $n/k$, with half-integers rounded up, is odd. At $n = 0$ both sides
are $1$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 17 (`jis-2024-24.2.5-prop-17`).

Stated but not proved: `MetaMathlibExt.card_lattice_disc_two_mul` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-lattice-disc-two-mul).

## The rounding sequence parity count drops by at most one

For every natural number $n$,
the rounding sequence parity count $\mathcal{R}$ satisfies
$\mathcal{R}_{n+1} \ge \mathcal{R}_n - 1$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 19 (`jis-2024-24.2.5-cor-19`).

Stated but not proved: `MetaMathlibExt.roundQuotientOddCount_sub_one_le_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#round-quotient-odd-count-sub-one-le-succ).

## Gauss's bound for lattice points in a disc

There is a constant $C$ such that for every
real $x \ge 1$, the number $N(x)$ of integer pairs $(a, b)$ with $a^2 + b^2 \le x$ satisfies
$|N(x) - \pi x| \le C \sqrt{x}$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Theorem 20 (`jis-2024-24.2.5-thm-20`).

Stated but not proved: `MetaMathlibExt.gauss_circle_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#gauss-circle-asymptotic).

## Asymptotic density of odd rounded quotients

There is a constant $C$ such that the
rounding sequence parity count $\mathcal{R}_n$ satisfies $|\mathcal{R}_n - (\pi/2 - 1)n| \le
C\sqrt{n}$ for every natural number $n \ge 1$; moreover $\mathcal{R}_n / n \to \pi/2 - 1$ as
$n \to \infty$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 21 (`jis-2024-24.2.5-prop-21`).

Stated but not proved: `MetaMathlibExt.roundQuotientOddCount_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#round-quotient-odd-count-asymptotic).

## Tail counts of the shifted floor sequence

Let $n$ be a natural number and let $\alpha$
and $\nu$ be real numbers with $0 \le \alpha < 1$, $0 \le \nu < 1$ and $\nu \le n\alpha$. Then
$\lfloor (n - \nu)/d + \alpha \rfloor \ge 1$ for all $n$ integers $d$ with $1 \le d \le n$, and
for every natural number $k \ge 2$ the number of integers $d$ with $1 \le d \le n$ and
$\lfloor (n - \nu)/d + \alpha \rfloor \ge k$ is $\lfloor (n - \nu)/(k - \alpha) \rfloor$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Lemma 24 (`jis-2024-24.2.5-lem-24`).

Stated but not proved: `MetaMathlibExt.shifted_floor_sequence_card_ge` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-sequence-card-ge).

## Floor-sum formulas for the shifted floor residue counts

Let $n$ and $m$ be natural
numbers with $m \ge 2$, and let $\alpha$ and $\nu$ be real numbers with $0 \le \alpha < 1$,
$0 \le \nu < 1$ and $\nu \le n\alpha$. For an integer $r$ let $\mathcal N_{n,\alpha,\nu,r,m}$ be
the number of integers $k$ with $1 \le k \le n$ such that
$\lfloor (n - \nu)/k + \alpha \rfloor \equiv r \pmod m$. Then

$$\mathcal N_{n,\alpha,\nu,1,m} = n - \Bigl\lfloor \frac{n - \nu}{1 - \alpha} \Bigr\rfloor +
\sum_{i=0}^{n} \Bigl( \Bigl\lfloor \frac{n - \nu}{1 + im - \alpha} \Bigr\rfloor -
\Bigl\lfloor \frac{n - \nu}{2 + im - \alpha} \Bigr\rfloor \Bigr),$$

and for every natural number $r$ with $2 \le r \le m$,

$$\mathcal N_{n,\alpha,\nu,r,m} = \sum_{i=0}^{n} \Bigl( \Bigl\lfloor \frac{n - \nu}{r + im - \alpha}
\Bigr\rfloor - \Bigl\lfloor \frac{n - \nu}{r + 1 + im - \alpha} \Bigr\rfloor \Bigr).$$

The paper sums over all $i \ge 0$; the terms with $i > n$ vanish, because for them every
denominator exceeds $n - \nu \ge 0$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 25 (`jis-2024-24.2.5-prop-25`).

Stated but not proved: `MetaMathlibExt.shiftedFloorResidueCount_eq_sum_floor_sub` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-residue-count-eq-sum-floor).

## Alternating sums of floor quotients along an increasing sequence

Let $0 \le \nu < 1$
and let $b_0, b_1, b_2, \dots$ be a strictly increasing sequence of real numbers with $b_k \ge 1$
and $b_k \ge k$ for every $k \ge 0$. Then there is a real constant $C$ such that for every integer
$n \ge 1$, with both sums taken over the integers $k$ satisfying $0 \le k \le n - \nu$,

$$\Bigl| \sum_k (-1)^k \lfloor (n - \nu)/b_k \rfloor - n \sum_k (-1)^k/b_k \Bigr| \le C\sqrt{n}.$$

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 32 (`jis-2024-24.2.5-prop-32`).

Stated but not proved: `MetaMathlibExt.alternating_sum_floor_div_eq_add_bigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#alternating-sum-floor-div-eq-add-big-o).

## Series asymptotics for the shifted floor residue counts with $2 \le r \le m$

Let $r$ and
$m$ be natural numbers with $2 \le r \le m$, and let $\alpha$ and $\nu$ be real numbers with
$0 \le \alpha < 1$ and $0 \le \nu < 1$. For a natural number $n$ let
$\mathcal N_{n,\alpha,\nu,r,m}$ be the number of integers $k$ with $1 \le k \le n$ such that
$\lfloor (n - \nu)/k + \alpha \rfloor \equiv r \pmod m$, and put

$$S = \sum_{i \ge 0} \Bigl( \frac{1}{r + im - \alpha} - \frac{1}{r + 1 + im - \alpha} \Bigr).$$

Then there is a constant $C$ such that
$\bigl| \mathcal N_{n,\alpha,\nu,r,m} - nS \bigr| \le C \sqrt n$ for every natural number
$n \ge 1$ with $\nu \le n\alpha$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 34 (`jis-2024-24.2.5-cor-34`).

Stated but not proved: `MetaMathlibExt.shiftedFloorResidueCount_asymptotic_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-residue-count-asymptotic-s).

## Series asymptotics for the shifted floor residue count with $r = 1$

Let $m \ge 2$ be a
natural number and let $\alpha$ and $\nu$ be real numbers with $0 \le \alpha < 1$ and
$0 \le \nu < 1$. For a natural number $n$ let $\mathcal N_{n,\alpha,\nu,1,m}$ be the number of
integers $k$ with $1 \le k \le n$ such that
$\lfloor (n - \nu)/k + \alpha \rfloor \equiv 1 \pmod m$, and put

$$S = \sum_{i \ge 0} \Bigl( \frac{1}{1 + im - \alpha} - \frac{1}{2 + im - \alpha} \Bigr).$$

Then there is a constant $C$ such that

$$\Bigl| \mathcal N_{n,\alpha,\nu,1,m} - \Bigl( -\frac{\alpha n}{1 - \alpha} + nS \Bigr) \Bigr| \le
C \sqrt n$$

for every natural number $n \ge 1$ with $\nu \le n\alpha$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 35 (`jis-2024-24.2.5-cor-35`).

Stated but not proved: `MetaMathlibExt.shiftedFloorResidueCount_one_asymptotic_series` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-residue-count-one-asymptot).

## Integral formula for an alternating series of reciprocals

Let $r$ and $m$ be natural
numbers with $2 \le r \le m$ and let $\alpha$ be a real number with $0 \le \alpha < 1$. Then

$$\sum_{i \ge 0} \Bigl( \frac{1}{r + im - \alpha} - \frac{1}{r + 1 + im - \alpha} \Bigr) =
\int_0^1 \frac{(1 - x)\, x^{r - 1 - \alpha}}{1 - x^m} \, dx.$$

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 36 (`jis-2024-24.2.5-prop-36`).

Stated but not proved: `MetaMathlibExt.tsum_alternating_inv_eq_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#tsum-alternating-inv-eq-integral).

## Integral asymptotics for the shifted floor residue counts

Let $m \ge 1$ be a natural
number and let $\alpha$ and $\nu$ be real numbers with $0 \le \alpha < 1$ and $0 \le \nu < 1$.
For natural numbers $n$ and $r$ let $\mathcal N_{n,\alpha,\nu,r,m}$ be the number of integers $k$
with $1 \le k \le n$ such that $\lfloor (n - \nu)/k + \alpha \rfloor \equiv r \pmod m$, and put

$$I_r = \int_0^1 \frac{(1 - x)\, x^{r - 1 - \alpha}}{1 - x^m} \, dx.$$

Then there is a constant $C$ such that

$$\Bigl| \mathcal N_{n,\alpha,\nu,1,m} - \Bigl( -\frac{\alpha n}{1 - \alpha} + n I_1 \Bigr) \Bigr|
\le C \sqrt n$$

for every natural number $n \ge 1$ with $\nu \le n\alpha$, and for every natural number $r$ with
$2 \le r \le m$ there is a constant $C_r$ such that
$\bigl| \mathcal N_{n,\alpha,\nu,r,m} - n I_r \bigr| \le C_r \sqrt n$ for every natural number
$n \ge 1$ with $\nu \le n\alpha$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Theorem 37 (`jis-2024-24.2.5-thm-37`).

Stated but not proved: `MetaMathlibExt.shiftedFloorResidueCount_asymptotic_integral` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 397](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L397). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-residue-count-asymptotic-i).

## Limiting densities of the shifted floor residue counts

Let $r$ and $m$ be natural
numbers with $1 \le r \le m$, and let $\alpha$ and $\nu$ be real numbers with $0 \le \alpha < 1$
and $0 \le \nu < 1$. For a natural number $n$ let $\mathcal N_{n,\alpha,\nu,r,m}$ be the number
of integers $k$ with $1 \le k \le n$ such that
$\lfloor (n - \nu)/k + \alpha \rfloor \equiv r \pmod m$, and for a natural number $s$ put

$$I_s = \int_0^1 \frac{(1 - x)\, x^{s - 1 - \alpha}}{1 - x^m} \, dx.$$

Then, as $n \to \infty$, $\mathcal N_{n,\alpha,\nu,r,m}/n$ tends to $-\alpha/(1 - \alpha) + I_1$
if $r = 1$ and to $I_r$ if $r \ge 2$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 38 (`jis-2024-24.2.5-cor-38`).

Stated but not proved: `MetaMathlibExt.shiftedFloorResidueCount_div_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#shifted-floor-residue-count-div-tendsto).

## Lattice points in the disc of radius $\sqrt{n}$ via shifted floor sequences

For every
natural number $n$, the number of pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + y^2 \le n$ equals
$4\,\mathcal{N}_{\lceil n/2 \rceil, 1/2, \{n/2\}, 1, 2} + 4\lfloor n/2 \rfloor + 1$, where
$\{n/2\}$ is the fractional part of $n/2$ and $\mathcal{N}_{N,\alpha,\nu,r,m}$ is the number of
$k \in \{1, \dots, N\}$ with $\lfloor (N - \nu)/k + \alpha \rfloor \equiv r \pmod m$. At $n = 0$
both sides are $1$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 39 (`jis-2024-24.2.5-prop-39`).

Stated but not proved: `MetaMathlibExt.card_lattice_disc_eq_shiftedFloorResidueCount` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-lattice-disc-eq-shifted-floor-resid).

## Number of representations by $x^2 + xy + y^2$

For every integer $n \ge 1$, the number
of pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + xy + y^2 = n$ equals
$6\,(d_{1,3}(n) - d_{2,3}(n))$, where $d_{r,3}(n)$ is the number of positive divisors of $n$
congruent to $r$ modulo $3$.

The paper cites this as Dickson, Exercise XXII.2.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 42 (`jis-2024-24.2.5-prop-42`).

Stated but not proved: `MetaMathlibExt.card_eisenstein_form_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 445](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L445). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-eisenstein-form-eq).

## Lattice points in the ellipse $x^2 + xy + y^2 \le n$

For every natural number $n$, the
number of pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + xy + y^2 \le n$ equals
$6\,\mathcal{N}_{n,0,0,1,3} + 1$, where $\mathcal{N}_{n,0,0,1,3}$ is the number of
$k \in \{1, \dots, n\}$ with $\lfloor n/k \rfloor \equiv 1 \pmod 3$. At $n = 0$ both sides
are $1$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 43 (`jis-2024-24.2.5-cor-43`).

Stated but not proved: `MetaMathlibExt.card_eisenstein_ellipse_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 457](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L457). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-eisenstein-ellipse-eq).

## Lattice points in the ellipse $x^2 + xy + y^2 \le n$, asymptotically

There is a real
constant $C$ such that for every integer $n \ge 1$, the number $E(n)$ of pairs
$(x, y) \in \mathbb{Z}^2$ with $x^2 + xy + y^2 \le n$ satisfies
$\bigl| E(n) - \tfrac{2}{3}\sqrt{3}\,\pi n \bigr| \le C\sqrt{n}$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 45 (`jis-2024-24.2.5-cor-45`).

Stated but not proved: `MetaMathlibExt.card_eisenstein_ellipse_asymptotic` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 467](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L467). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-eisenstein-ellipse-asymptotic).

## Lattice points in a disc of the hexagonal lattice

Let $\omega = e^{2\pi i/3}$, so that
$\mathbb{Z} + \mathbb{Z}\omega$ is the hexagonal (triangular) lattice whose neighboring points are
one unit apart. For every natural number $n$, the number of pairs $(x, y) \in \mathbb{Z}^2$ with
$|x + y\omega| \le \sqrt{n}$ equals $1 + 6\,\mathcal{N}_{n,0,0,1,3}$, where
$\mathcal{N}_{n,\alpha,\nu,r,m}$ is the number of $k \in \{1, \dots, n\}$ with
$\lfloor (n - \nu)/k + \alpha \rfloor \equiv r \pmod m$. Moreover, $\mathcal{N}_{n,0,0,1,3}$ is
the number of terms of $\lfloor n/1 \rfloor, \dots, \lfloor n/n \rfloor$ that are congruent to
$1$ modulo $3$.

Every hexagonal lattice with unit spacing is congruent to this one, so this counts the lattice
points in any closed disc of radius $\sqrt{n}$ centered at a lattice point.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 47 (`jis-2024-24.2.5-cor-47`).

Stated but not proved: `MetaMathlibExt.card_hexagonal_lattice_disc_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 483](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L483). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-hexagonal-lattice-disc-eq).

## Dickson's divisor formula for $x^2 + 2y^2$

For every integer $n \ge 1$, the number of
pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + 2y^2 = n$ equals
$2\,(d_1(n) + d_3(n) - d_5(n) - d_7(n))$, where $d_r(n)$ denotes the number of positive divisors
$d$ of $n$ with $d \equiv r \pmod 8$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Proposition 48 (`jis-2024-24.2.5-prop-48`).

Stated but not proved: `MetaMathlibExt.card_sq_add_two_mul_sq_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-sq-add-two-mul-sq-eq).

## Lattice points in the ellipse $x^2 + 2y^2 \le n$

For a natural number $n$, let $F(n)$ be
the number of pairs $(x, y) \in \mathbb{Z}^2$ with $x^2 + 2y^2 \le n$, and let
$\mathcal{N}_{N,\alpha,\nu,r,m}$ be the number of $k \in \{1, \dots, N\}$ with
$\lfloor (N - \nu)/k + \alpha \rfloor \equiv r \pmod m$. Then $F(0) = 1$, $F(1) = 3$,
$F(2) = 5$ and $F(5) = 11$. For every natural number $n \notin \{1, 2, 5\}$, writing
$N = \lceil n/4 \rceil$ and $\theta = \{-n/4\}$ for the fractional part of $-n/4$,
$F(n) = 1 + 2\,\mathcal{N}_{N,3/4,\theta,1,2} + 2\,\mathcal{N}_{N,1/4,\theta,1,2} +
2n + 2\lfloor n/3 \rfloor - 4N$. This formula includes $n = 0$, where both sides are $1$.

## Sources

- Nicholas Dent and Caleb M. Shor, *On Residues of Rounded Shifted Fractions with a Common Numerator*, Journal of Integer Sequences 27 (2024), Article 24.2.5, Corollary 49 (`jis-2024-24.2.5-cor-49`).

Stated but not proved: `MetaMathlibExt.card_sq_add_two_mul_sq_ellipse_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean, line 515](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/RoundedShiftedFractionResiduesWanted.lean#L515). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html#card-sq-add-two-mul-sq-ellipse-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Residues of rounded quotients n/k](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/residues-of-rounded-quotients-n-k)
