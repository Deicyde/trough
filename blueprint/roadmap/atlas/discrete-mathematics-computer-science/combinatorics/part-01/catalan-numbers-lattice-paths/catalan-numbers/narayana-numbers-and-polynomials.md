---
declaration: section
origin: cited
lean: MetaMathlibExt.narayana, MetaMathlibExt.narayana_eq, MetaMathlibExt.narayana_eq_second, MetaMathlibExt.narayanaPolynomialCoeff, MetaMathlibExt.narayanaPolynomialCoeff_succ_succ, MetaMathlibExt.narayanaPolynomial
statement: formalized
proof: formalized
---

# Narayana numbers and polynomials

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html).

## Narayana number

For positive integers $n$ and $k$, the Narayana number $N(n, k)$ is the
natural number $\lfloor \binom{n}{k}\binom{n}{k-1} / n \rfloor$.

Formalized by `MetaMathlibExt.narayana`, a definition declared in [MathlibExt/Combinatorics/Enumerative/NarayanaNumber.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/NarayanaNumber.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html#narayana).

## Defining formula for the Narayana number

For positive integers $n$ and $k$, the Narayana
number $N(n, k)$ satisfies $N(n, k) = \lfloor \binom{n}{k}\binom{n}{k-1} / n \rfloor$.

Formalized by `MetaMathlibExt.narayana_eq`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/NarayanaNumber.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/NarayanaNumber.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html#narayana-eq).

## Second formula for the Narayana number

For positive integers $n$ and $k$, the Narayana
number $N(n, k)$ satisfies $N(n, k) = \lfloor \binom{n-1}{k-1}\binom{n}{k-1} / k \rfloor$.

Formalized by `MetaMathlibExt.narayana_eq_second`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/NarayanaNumber.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/NarayanaNumber.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html#narayana-eq-second).

## Narayana polynomial coefficients

The Narayana polynomial coefficients are the natural
numbers $a(n, k)$, for natural numbers $n$ and $k$, given by $a(0, 0) = 1$, $a(0, k) = 0$ for
$k \ge 1$, $a(n, 0) = 0$ for $n \ge 1$, and $a(n, k) = N(n, k)$ for $n, k \ge 1$, where $N(n, k)$
is the Narayana number. So row zero is $1$ and every positive row has zero constant term.

Formalized by `MetaMathlibExt.narayanaPolynomialCoeff`, a definition declared in [MathlibExt/Combinatorics/Enumerative/NarayanaPolynomial.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/NarayanaPolynomial.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html#narayana-polynomial-coeff).

## Narayana polynomial coefficients at positive indices

For all natural numbers $n$ and
$k$, the Narayana polynomial coefficient in row $n + 1$ and degree $k + 1$ equals the Narayana
number $N(n + 1, k + 1)$.

This holds by definition.

Formalized by `MetaMathlibExt.narayanaPolynomialCoeff_succ_succ`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/NarayanaPolynomial.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/NarayanaPolynomial.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html#narayana-polynomial-coeff-succ-succ).

## Narayana polynomials

For a semiring $R$ and a natural number $n$, the $n$-th Narayana
polynomial is

$$N_n(X) = \sum_{k=0}^{n} a(n, k)\, X^k \in R[X],$$

where $a(n, k)$ is the Narayana polynomial coefficient, taken in $R$. Since $a(0, 0) = 1$ and,
for $n \ge 1$, $a(n, 0) = 0$ and $a(n, k)$ is the Narayana number $N(n, k)$ for $k \ge 1$, the
first polynomials are $N_0 = 1$, $N_1 = X$, $N_2 = X^2 + X$ and $N_3 = X^3 + 3X^2 + X$.

Formalized by `MetaMathlibExt.narayanaPolynomial`, a definition declared in [MathlibExt/Combinatorics/Enumerative/NarayanaPolynomial.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/NarayanaPolynomial.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html#narayana-polynomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Narayana numbers and polynomials](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/narayana-numbers-and-polynomials)
