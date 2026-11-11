---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticSquareSum, MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticPowerSum, MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticSquareSum_holds, MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticPowerSum_holds
statement: formalized
---

# Monochromatic sums equal to perfect powers

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums-equal-to-perfect-powers/index.html).

## Erdős Problem 439 for squares

The statement that for every colouring of the positive
integers with finitely many colours there are distinct positive integers $x$ and $y$ of the same
colour such that $x + y$ is a perfect square.

Formalized by `MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticSquareSum`, a definition declared in [WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums-equal-to-perfect-powers/index.html#monochromatic-square-sum).

## Erdős Problem 439 for $k$-th powers

The statement that for every integer $k \ge 2$ and
every colouring of the positive integers with finitely many colours there are distinct positive
integers $x$ and $y$ of the same colour such that $x + y = z^k$ for some natural number $z$.

Formalized by `MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticPowerSum`, a definition declared in [WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums-equal-to-perfect-powers/index.html#monochromatic-power-sum).

## Erdős Problem 439 for squares is true

For every colouring of the positive integers with
finitely many colours there are distinct positive integers $x$ and $y$ of the same colour such
that $x + y$ is a perfect square.

This is the case $f(z) = z^2$ of a theorem of Khalfalah and Szemerédi on monochromatic
solutions of $x + y = f(z)$; Erdős, Sárközy and Sós had proved the cases of $2$ and $3$ colours.

## Sources

- T. F. Bloom, Erdős Problems, Problem #439, https://www.erdosproblems.com/439 (status PROVED); resolution: A. Khalfalah and E. Szemerédi, On the number of monochromatic solutions of x + y = z², Combin. Probab. Comput. (2006), 213-227, main theorem (a conjecture of Erdős, Roth, Sárközy and Sós): for every nonconstant f ∈ ℤ[z] with 2 ∣ f(z) for some z ∈ ℤ, every finite colouring of the integers has x ≠ y of the same colour with x + y = f(z) (abstract; erdosproblems.com/439), https://doi.org/10.1017/S0963548305007169.

Stated but not proved: `MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticSquareSum_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums-equal-to-perfect-powers/index.html#monochromatic-square-sum-holds).

## Erdős Problem 439 for $k$-th powers is true

For every integer $k \ge 2$ and every colouring
of the positive integers with finitely many colours there are distinct positive integers $x$ and
$y$ of the same colour such that $x + y = z^k$ for some natural number $z$.

Khalfalah and Szemerédi proved the corresponding statement for $x + y = f(z)$ for every
nonconstant polynomial $f$ with integer coefficients such that $f(z)$ is even for some integer
$z$; the polynomial $f(z) = z^k$ qualifies, since $f(2) = 2^k$.

## Sources

- T. F. Bloom, Erdős Problems, Problem #439, https://www.erdosproblems.com/439 (status PROVED); resolution: A. Khalfalah and E. Szemerédi, On the number of monochromatic solutions of x + y = z², Combin. Probab. Comput. (2006), 213-227, main theorem (a conjecture of Erdős, Roth, Sárközy and Sós): for every nonconstant f ∈ ℤ[z] with 2 ∣ f(z) for some z ∈ ℤ, every finite colouring of the integers has x ≠ y of the same colour with x + y = f(z) (abstract; erdosproblems.com/439), https://doi.org/10.1017/S0963548305007169.

Stated but not proved: `MathlibExt.Combinatorics.MonochromaticSquareSumErdosProblem439Wanted.monochromaticPowerSum_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/MonochromaticSquareSumErdosProblem439Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums-equal-to-perfect-powers/index.html#monochromatic-power-sum-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monochromatic sums equal to perfect powers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums-equal-to-perfect-powers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/ramsey-theory/schur-rado-theorems/monochromatic-sums-equal-to-perfect-powers)
