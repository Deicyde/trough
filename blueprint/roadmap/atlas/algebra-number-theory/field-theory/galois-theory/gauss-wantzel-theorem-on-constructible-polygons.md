---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.GaussWantzelWanted.NumberTheory.GaussWantzel.IsConstructible, MathlibExt.NumberTheory.GaussWantzelWanted.NumberTheory.GaussWantzel.GaussWantzelNumber, MathlibExt.NumberTheory.GaussWantzelWanted.NumberTheory.GaussWantzel.gauss_wantzel_constructible_polygon
statement: formalized
---

# Gauss–Wantzel theorem on constructible polygons

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/gauss-wantzel-theorem-on-constructible-polygons/index.html).

## Constructible real numbers

The constructible real numbers form the smallest set of real
numbers that contains every rational number and is closed under addition, negation,
multiplication, inverses of nonzero elements and square roots of nonnegative elements;
equivalently, the smallest subfield of $\mathbb{R}$ closed under square roots.

These are the real values constructible from rational data by straightedge and compass.

Formalized by `MathlibExt.NumberTheory.GaussWantzelWanted.NumberTheory.GaussWantzel.IsConstructible`, an inductive type declared in [WantedExt/NumberTheory/GaussWantzelWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussWantzelWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/gauss-wantzel-theorem-on-constructible-polygons/index.html#is-constructible).

## Gauss–Wantzel number

A natural number $n$ is a Gauss–Wantzel number if $n > 0$, every
prime factor of $n$ is either $2$ or a Fermat prime, and $p^2$ does not divide $n$ for every odd
prime factor $p$ of $n$.

Equivalently, $n$ is a power of $2$ times a product of distinct Fermat primes.

Formalized by `MathlibExt.NumberTheory.GaussWantzelWanted.NumberTheory.GaussWantzel.GaussWantzelNumber`, a definition declared in [WantedExt/NumberTheory/GaussWantzelWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussWantzelWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/gauss-wantzel-theorem-on-constructible-polygons/index.html#gauss-wantzel-number).

## Gauss–Wantzel theorem

For every natural number $n \ge 3$, the real number
$\cos(2\pi/n)$ is constructible (it lies in the smallest subfield of $\mathbb{R}$ closed under
square roots) if and only if $n$ is a Gauss–Wantzel number, that is, every prime factor of $n$ is
$2$ or a Fermat prime and every odd prime factor of $n$ divides $n$ only once.

## Sources

- C. F. Gauss, Disquisitiones Arithmeticae (1801), §365-366; P. L. Wantzel, Recherches sur les moyens de reconnaître si un problème de géométrie peut se résoudre avec la règle et le compas, J. Math. Pures Appl. 1 (1837). Listed as §174 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Knill, §174. Problem `gauss_wantzel_constructible_polygon` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.GaussWantzelWanted.NumberTheory.GaussWantzel.gauss_wantzel_constructible_polygon` is written with `theorem_wanted` in [WantedExt/NumberTheory/GaussWantzelWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GaussWantzelWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/gauss-wantzel-theorem-on-constructible-polygons/index.html#gauss-wantzel-constructible-polygon).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Gauss–Wantzel theorem on constructible polygons](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/galois-theory/gauss-wantzel-theorem-on-constructible-polygons/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/FieldTheory/galois-theory/gauss-wantzel-theorem-on-constructible-polygons)
