---
declaration: section
origin: cited
lean: MetaMathlibExt.fuss_catalan_dvd_choose, MetaMathlibExt.fussCatalanNumber, MetaMathlibExt.generalizedCatalan_prime_dvd_iff_not_geometric_sum, MetaMathlibExt.generalizedFussCatalanNumber, MetaMathlibExt.generalizedFussCatalanNumber_eq, MetaMathlibExt.generalizedFussCatalanNumber_one
statement: formalized
proof: formalized
---

# Fuss–Catalan numbers

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html).

## Integrality of the Fuss–Catalan numbers

For natural numbers $a \ge 2$ and $n \ge 1$, the
integer $(a-1)n + 1$ divides the binomial coefficient $\binom{an}{n}$. Hence the Fuss–Catalan
number $\frac{1}{(a-1)n+1}\binom{an}{n}$ is an integer.

## Sources

- Christian Ballot, "Lucasnomial Fuss-Catalan Numbers and Related Divisibility Questions," Journal of Integer Sequences 21 (2018), Article 18.6.5, equation, lines 115–117 (classical definition), line 127 (classical integrality recorded as known), Theorem, lines 516–521 (Lucasnomial generalization), https://cs.uwaterloo.ca/journals/JIS/VOL21/Ballot/ballot30.tex

Formalized by `MetaMathlibExt.fuss_catalan_dvd_choose`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FussCatalanDivisibility.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/FussCatalanDivisibility.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html#fuss-catalan-dvd-choose).

## Fuss–Catalan numbers

For natural numbers $k \ge 1$ (the chord arity) and $m$, the
Fuss–Catalan number is the natural-number quotient of $\binom{km}{m}$ by $(k-1)m+1$, that is
$\lfloor \binom{km}{m} / ((k-1)m+1) \rfloor$.

## Sources

- JIS VOL23/Young, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Young/young5.tex>.

Formalized by `MetaMathlibExt.fussCatalanNumber`, a definition declared in [MathlibExt/NumberTheory/FussCatalanNumber.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/FussCatalanNumber.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html#fuss-catalan-number).

## Prime divisibility of generalized Catalan numbers

Let $p$ be a prime and $n$ a natural
number. Then $p$ divides the generalized Catalan number $\frac{1}{(p-1)n+1}\binom{pn}{n}$ (an
integer) if and only if $n$ is not of the form $\frac{p^k-1}{p-1}$ for any natural number $k$.

The source theorem's "in particular" Mersenne-index clause is already recorded
as `catalan_odd_iff`; this declaration keeps only the new general-`p` result.

## Sources

- B. Sury, "Generalized Catalan Numbers: Linear Recursion and Divisibility," Journal of Integer Sequences 12 (2009), Article 09.7.5, Theorem, lines 154–158, https://cs.uwaterloo.ca/journals/JIS/VOL12/Sury/sury31.tex

Formalized by `MetaMathlibExt.generalizedCatalan_prime_dvd_iff_not_geometric_sum`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedCatalanPrimeDivisibility.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedCatalanPrimeDivisibility.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html#generalized-catalan-prime-dvd-iff-not-ge).

## Generalized Fuss–Catalan number

For natural numbers $m$, $n$ and $k$, the generalized
Fuss–Catalan number $F_m(n, k)$ is the quotient of $k \binom{mn + k}{n}$ by $mn + k$ in
natural-number division, rounded down, with division by $0$ giving $0$.

The source considers $m \ge 2$ and $n, k \ge 1$. The definition is totalized over natural numbers.

Formalized by `MetaMathlibExt.generalizedFussCatalanNumber`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFussCatalanNumbersFMNK.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFussCatalanNumbersFMNK.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html#generalized-fuss-catalan-number).

## Formula for the generalized Fuss–Catalan number

For all natural numbers $m$, $n$ and $k$,
the generalized Fuss–Catalan number $F_m(n, k)$ equals the quotient of $k \binom{mn + k}{n}$ by
$mn + k$ in natural-number division, rounded down, with division by $0$ giving $0$.

Formalized by `MetaMathlibExt.generalizedFussCatalanNumber_eq`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFussCatalanNumbersFMNK.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFussCatalanNumbersFMNK.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html#generalized-fuss-catalan-number-eq).

## Generalized Fuss–Catalan numbers at $n = 1$

For all natural numbers $m$ and $k$, the
generalized Fuss–Catalan number $F_m(1, k)$ equals $k$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL21/He/he61.tex>, case (c) of the source theorem.

Formalized by `MetaMathlibExt.generalizedFussCatalanNumber_one`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFussCatalanNumbersFMNK.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFussCatalanNumbersFMNK.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html#generalized-fuss-catalan-number-one).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fuss–Catalan numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/special-numbers/catalan-numbers/fuss-catalan-numbers)
