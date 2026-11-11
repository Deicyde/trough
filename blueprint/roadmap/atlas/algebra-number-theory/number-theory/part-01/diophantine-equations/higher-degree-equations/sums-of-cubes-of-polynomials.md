---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PolynomialCubesWanted.int_sum_four_polynomial_cubes_of_cube_form, MathlibExt.NumberTheory.PolynomialCubesWanted.int_eq_sum_five_polynomial_cubes
statement: formalized
---

# Sums of cubes of polynomials

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/sums-of-cubes-of-polynomials/index.html).

## Integers of the form $p^3 + q^3$ or $2(p^6 - q^6)$ as sums of four polynomial cubes

Let $p$ and $q$ be integers and let $N = p^3 + q^3$ or $N = 2(p^6 - q^6)$. Then there are
polynomials $f, g, h, k \in \mathbb{Z}[x]$, each of degree at least $1$, such that
$f^3 + g^3 + h^3 + k^3 = N$ as an identity in $\mathbb{Z}[x]$.

## Sources

- Ajai Choudhry, "Expressing an Integer as a Sum of Cubes of Polynomials", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.PolynomialCubesWanted.int_sum_four_polynomial_cubes_of_cube_form` is written with `theorem_wanted` in [WantedExt/NumberTheory/PolynomialCubesWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PolynomialCubesWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/sums-of-cubes-of-polynomials/index.html#int-sum-four-polynomial-cubes-of-cube-fo).

## Every integer is a sum of five cubes of polynomials

For every integer $N$ there are
polynomials $f, g, h, k, l \in \mathbb{Z}[x]$, each of degree at least $1$, such that
$f^3 + g^3 + h^3 + k^3 + l^3 = N$ as an identity in $\mathbb{Z}[x]$.

## Sources

- Ajai Choudhry, "Expressing an Integer as a Sum of Cubes of Polynomials", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.PolynomialCubesWanted.int_eq_sum_five_polynomial_cubes` is written with `theorem_wanted` in [WantedExt/NumberTheory/PolynomialCubesWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/PolynomialCubesWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/sums-of-cubes-of-polynomials/index.html#int-eq-sum-five-polynomial-cubes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of cubes of polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/sums-of-cubes-of-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/sums-of-cubes-of-polynomials)
