---
declaration: section
origin: cited
lean: MetaMathlibExt.ncard_regular_eq_sum_totient_unitaryDivisors, MetaMathlibExt.morgado_card_regular_modulo, isRegularMod_iff_gcd_sq_eq_gcd
statement: formalized
---

# Regular integers modulo n

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/regular-integers-modulo-n/index.html).

## Morgado's formula as a sum over unitary divisors

For every positive integer $n$, the
number of residue classes $m \in \mathbb{Z}/n\mathbb{Z}$ for which the equation $m^2 x = m$ has a
solution $x \in \mathbb{Z}/n\mathbb{Z}$ equals the sum of $\varphi(d)$ over the unitary divisors
$d$ of $n$ (the positive divisors $d$ of $n$ with $\gcd(d, n/d) = 1$), where $\varphi$ is Euler's
totient function.

Formalized by `MetaMathlibExt.ncard_regular_eq_sum_totient_unitaryDivisors`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/MorgadoRegularResidues.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/MorgadoRegularResidues.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/regular-integers-modulo-n/index.html#ncard-regular-eq-sum-totient-unitary-div).

## Morgado's formula for the number of regular residues

Let $n$ be a positive integer. Call
a residue class $m \in \mathbb{Z}/n\mathbb{Z}$ regular if the equation $m^2 x = m$ has a solution
$x \in \mathbb{Z}/n\mathbb{Z}$, and let $\varrho(n)$ be the number of regular residue classes. Let
$U(n)$ be the set of positive divisors $d$ of $n$ with $\gcd(d, n/d) = 1$. Then

$$\varrho(n) = \sum_{d \in U(n)} \varphi(d),$$

where $\varphi$ is Euler's totient function.

The sequence $\varrho(1), \varrho(2), \ldots$ is OEIS A055653.

## Sources

- Klaus Dohmen and Mandy Lange-Geisler, "On the Number of Regular Integers Modulo n and Its Significance for Cryptography", Journal of Integer Sequences 29 (2026), Article 26.2.4, Definition [Morgado 1972] lines 108-112 and Theorem [Morgado 1972] (equation `eq:2`) lines 127-132: https://cs.uwaterloo.ca/journals/JIS/VOL29/Dohmen/dohmen4.tex The formula is attributed to J. Morgado (1972). It follows from `ncard_regular_eq_sum_totient_unitaryDivisors`; the filter spells out `n.unitaryDivisors` and keeps the source's shape.

Formalized by `MetaMathlibExt.morgado_card_regular_modulo`, a theorem declared in [MathlibExt/NumberTheory/ArithmeticFunction/MorgadoRegularResidues.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ArithmeticFunction/MorgadoRegularResidues.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/regular-integers-modulo-n/index.html#morgado-card-regular-modulo).

## Morgado's characterization of regular integers

Let $n$ be a positive integer and $m$
an integer, and write $\gcd$ for the nonnegative greatest common divisor. The congruence
$m^2 x \equiv m \pmod{n}$ has a solution $x \in \mathbb{Z}$ if and only if
$\gcd(m^2, n) = \gcd(m, n)$, and $\gcd(m^2, n) = \gcd(m, n)$ holds if and only if $\gcd(m, n)$
and $n / \gcd(m, n)$ are coprime, that is, $\gcd(m, n)$ is a unitary divisor of $n$.

## Sources

- Klaus Dohmen and Mandy Lange-Geisler, "On the Number of Regular Integers Modulo `n` and Its Significance for Cryptography", Journal of Integer Sequences 29 (2026), Article 26.2.4, Proposition [Morgado 1972]: <https://cs.uwaterloo.ca/journals/JIS/VOL29/Dohmen/dohmen4.tex>.

Stated but not proved: `isRegularMod_iff_gcd_sq_eq_gcd` is written with `theorem_wanted` in [WantedExt/NumberTheory/RegularResiduesWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/RegularResiduesWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/regular-integers-modulo-n/index.html#is-regular-mod-iff-gcd-sq-eq-gcd).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Regular integers modulo n](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/regular-integers-modulo-n/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-functions/divisor-totient-functions/part-01/regular-integers-modulo-n)
