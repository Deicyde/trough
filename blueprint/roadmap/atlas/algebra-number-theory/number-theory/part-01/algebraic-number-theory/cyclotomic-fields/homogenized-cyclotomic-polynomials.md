---
declaration: section
origin: cited
lean: MetaMathlibExt.homogenizedCyclotomic, MetaMathlibExt.homogenizedCyclotomic_one, MetaMathlibExt.homogenizedCyclotomic_two, MetaMathlibExt.homogenizedCyclotomic_one_right, MetaMathlibExt.homogenizedCyclotomic_cast
statement: formalized
proof: formalized
---

# Homogenized cyclotomic polynomials

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials/index.html).

## Homogenized cyclotomic value

For a natural number $n$ and integers $a, b$, let
$c_0, \dots, c_{\varphi(n)}$ be the integer coefficients of the $n$-th cyclotomic polynomial,
whose degree is $\varphi(n)$, where $\varphi$ is Euler's totient function. The homogenized
cyclotomic value is the integer

$$\Phi_n(a, b) = \sum_{i=0}^{\varphi(n)} c_i \, a^i \, b^{\varphi(n) - i}.$$

When $b \neq 0$ it equals $b^{\varphi(n)} \Phi_n(a/b)$, where $\Phi_n$ is the $n$-th cyclotomic
polynomial.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Section 2 (notation `Φ_n(a, b)`, Lemma 3 and the explicit values in the proof of Theorem 1).

Formalized by `MetaMathlibExt.homogenizedCyclotomic`, a definition declared in [MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials/index.html#homogenized-cyclotomic).

## Homogenized cyclotomic value of index one

For all integers $a$ and $b$, the
homogenized cyclotomic value $\Phi_1(a, b)$ equals $a - b$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 3 (v) (the case `n = 1`).

Formalized by `MetaMathlibExt.homogenizedCyclotomic_one`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials/index.html#homogenized-cyclotomic-one).

## Homogenized cyclotomic value of index two

For all integers $a$ and $b$, the
homogenized cyclotomic value $\Phi_2(a, b)$ equals $a + b$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Lemma 3 (v) (the case `n = 2`).

Formalized by `MetaMathlibExt.homogenizedCyclotomic_two`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials/index.html#homogenized-cyclotomic-two).

## Homogenized cyclotomic value with second argument one

For every natural number $n$
and every integer $a$, the homogenized cyclotomic value $\Phi_n(a, 1)$ equals $\Phi_n(a)$, the
value at $a$ of the $n$-th cyclotomic polynomial with integer coefficients.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Section 2 (notation `Φ_n(a, b)`).

Formalized by `MetaMathlibExt.homogenizedCyclotomic_one_right`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials/index.html#homogenized-cyclotomic-one-right).

## Homogenized cyclotomic value in a field

Let $K$ be a field, $n$ a natural number and
$a, b$ integers such that the image of $b$ in $K$ is nonzero. Then the image in $K$ of the
homogenized cyclotomic value $\Phi_n(a, b)$ equals $b^{\varphi(n)} \Phi_n(a/b)$, where $\Phi_n$
is the $n$-th cyclotomic polynomial over $K$, $\varphi$ is Euler's totient function, and $b$
and $a/b$ are computed in $K$.

## Sources

- Ömer Avcı, *Large Zsigmondy Primes*, INTEGERS 24 (2024), Article A62, Section 2 (notation `Φ_n(a, b)`).

Formalized by `MetaMathlibExt.homogenizedCyclotomic_cast`, a theorem declared in [MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Cyclotomic/HomogenizedCyclotomic.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials/index.html#homogenized-cyclotomic-cast).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Homogenized cyclotomic polynomials](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/homogenized-cyclotomic-polynomials)
