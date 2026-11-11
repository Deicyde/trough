---
declaration: section
origin: cited
lean: Nat.exists_three_squares_of_not_four_pow_mul_eight_mul_add_seven, Nat.not_exists_four_pow_mul_eight_mul_add_seven_of_exists_three_squares, MetaMathlibExt.every_nat_eq_sum_three_sq_div_eight, Nat.threeSquareRepresentationCount, Nat.threeSquareRepresentationCount_eq_zero_of_mod_eight_eq_seven, Nat.threeSquareRepresentationCount_eq_threeSquareRepresentationCount_div_four, MetaMathlibExt.r3_legendre_recursion, Nat.hurwitzClassNumber
statement: formalized
---

# Sums of three squares

10 results, 7 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html).

## Legendre's three-square theorem

Every natural number $n$ that is not of the form
$4^a (8b + 7)$ with natural numbers $a, b$ is a sum of three squares: there are natural numbers
$x, y, z$ with $x^2 + y^2 + z^2 = n$.

## Sources

- Soufiane Mezroui, Abdelmalek Azizi, and M'hammed Ziane, "On a Conjecture of Farhi", Journal of Integer Sequences 17 (2014), source TeX lines 122-127, https://cs.uwaterloo.ca/journals/JIS/VOL17/Mezroui/soufiane4.tex.

Formalized by `Nat.exists_three_squares_of_not_four_pow_mul_eight_mul_add_seven`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/LegendreThreeSquare.lean, line 1159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/LegendreThreeSquare.lean#L1159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#exists-three-squares-of-not-four-pow-mul).

## Converse of Legendre's three-square theorem

If a natural number $n$ is a sum of three
squares of natural numbers, then $n$ is not of the form $4^a (8b + 7)$ with natural numbers $a, b$.

## Sources

- Fabián Arias, Jerson Borja, and Luis Rubio, "Counting Integers Representable as Images of Polynomials Modulo n", Journal of Integer Sequences 22 (2019), Article 19.6.7, theorem, lines 134–136, https://cs.uwaterloo.ca/journals/JIS/VOL22/Borja/borja3.tex.

Formalized by `Nat.not_exists_four_pow_mul_eight_mul_add_seven_of_exists_three_squares`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/LegendreThreeSquareConverse.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/LegendreThreeSquareConverse.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#not-exists-four-pow-mul-eight-mul-add-se).

## Sums of three terms of the sequence ⌊n²/8⌋

For every natural number $m$ there are natural
numbers $a$, $b$, $c$ with
$m = \lfloor a^2/8 \rfloor + \lfloor b^2/8 \rfloor + \lfloor c^2/8 \rfloor$.

## Sources

- Bakir Farhi, "On the Representation of the Natural Numbers as the Sum of Three Terms of the Sequence floor(n^2/a)", Journal of Integer Sequences 16 (2013), Article 13.6.4, Theorem 1, lines 104-106, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Farhi/farhi7.tex>.

Formalized by `MetaMathlibExt.every_nat_eq_sum_three_sq_div_eight`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/ThreeFloorSquareSums.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/ThreeFloorSquareSums.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#every-nat-eq-sum-three-sq-div-eight).

## Number of representations as a sum of three squares

For a natural number $n$, $r_3(n)$
is the number of ordered triples $(x, y, z)$ of integers in the interval $[-n, n]$ with
$x^2 + y^2 + z^2 = n$. Every integer solution of $x^2 + y^2 + z^2 = n$ lies in this interval
(also for $n = 0$), so $r_3(n)$ is the number of all ordered integer solutions.

## Sources

- Primary source: E. T. Mortenson, arXiv:1702.01627v2, `Mortenson-AC-Gauss-arxiv-v2.tex` lines 127-131 defining `rₛ` by `Rₛ(q) = ∑ₙ rₛ(n) (-q) ^ n = (∑_{m ∈ ℤ} (-1) ^ m q ^ (m ^ 2)) ^ s` (ordered signed integer tuples). Ranked source arXiv:2307.05244 `main.tex` lines 78-82 identifies the equation `x ^ 2 + y ^ 2 + z ^ 2 = n`.

Formalized by `Nat.threeSquareRepresentationCount`, a definition declared in [MathlibExt/NumberTheory/QuadraticForms/ThreeSquares.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/ThreeSquares.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#three-square-representation-count).

## Numbers congruent to 7 modulo 8 are not sums of three squares

For a natural number $m$,
let $r_3(m)$ denote the number of ordered triples of integers $(x, y, z)$ with
$x^2 + y^2 + z^2 = m$. For every positive natural number $n$ with $n \equiv 7 \pmod 8$,
$r_3(n) = 0$. This is the case $n \equiv 7 \pmod 8$ of Gauss's formula for $r_3$.

## Sources

- arXiv:2307.05244 `main.tex` lines 191-199.

Formalized by `Nat.threeSquareRepresentationCount_eq_zero_of_mod_eight_eq_seven`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/ThreeSquares.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/ThreeSquares.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#three-square-representation-count-eq-zer).

## Removing a factor of 4 preserves the three-square count

For a natural number $m$, let
$r_3(m)$ denote the number of ordered triples of integers $(x, y, z)$ with $x^2 + y^2 + z^2 = m$.
For every positive natural number $n$ divisible by $4$, $r_3(n) = r_3(n/4)$. This is the case
$4 \mid n$ of Gauss's formula for $r_3$.

## Sources

- arXiv:2307.05244 `main.tex` lines 191-199.

Formalized by `Nat.threeSquareRepresentationCount_eq_threeSquareRepresentationCount_div_four`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/ThreeSquares.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/ThreeSquares.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#three-square-representation-count-eq-thr).

## Legendre-symbol recursion for three-square counts

For a natural number $m$, let $r_3(m)$
denote the number of ordered triples of integers $(x, y, z)$ with $x^2 + y^2 + z^2 = m$. Let
$p \ge 3$ be a prime and let $n \ge 1$ and $\alpha \ge 0$ be natural numbers. Then

$$
r_3(p^{2\alpha} n) = \left(\frac{p^{\alpha+1} - 1}{p - 1} - \left(\frac{-n}{p}\right)
\frac{p^{\alpha} - 1}{p - 1}\right) r_3(n) - p \, \frac{p^{\alpha} - 1}{p - 1} \, r_3(n/p^2),
$$

where $\left(\frac{-n}{p}\right)$ is the Legendre symbol, both quotients by $p - 1$ are exact
integer divisions, and the term $r_3(n/p^2)$ is read as $0$ when $p^2$ does not divide $n$.

Proof: The route is an elementary p-neighbour double count using quaternionic descent and
finite-field conic counts, followed by a two-step induction on the exponent.

## Sources

- Liuquan Wang, "Another Proof of a Conjecture by Hirschhorn and Sellers on Overpartitions", Journal of Integer Sequences 17 (2014), Article 14.9.8, Lemma `r3relation`, lines 228-232, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Wang2/wang15.tex>.

Formalized by `MetaMathlibExt.r3_legendre_recursion`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/ThreeSquaresLegendreRecursion.lean, line 2391](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/QuadraticForms/ThreeSquaresLegendreRecursion.lean#L2391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#r3-legendre-recursion).

## Hurwitz class number

The Hurwitz class number is the function $H$ from the natural
numbers to the rationals given by $H(0) = -1/12$; $H(N) = 0$ if $N \equiv 1$ or $2 \pmod 4$; and,
for $N > 0$ with $N \equiv 0$ or $3 \pmod 4$, $H(N)$ is the number of equivalence classes of
positive-definite integral binary quadratic forms of discriminant $-N$, primitive or not, where
the class of a form equivalent to $a (x^2 + y^2)$ for some positive integer $a$ counts with weight
$1/2$, the class of a form equivalent to $a (x^2 + x y + y^2)$ for some positive integer $a$
counts with weight $1/3$, and every other class counts with weight $1$.

## Sources

- arXiv:2307.05244 `main.tex` lines 359-365: `H(N) = 0` if `N ≡ 1` or `2 mod 4`; `H(0) = -1 / 12`; otherwise `N > 0` and `N ≡ 0` or `3 mod 4`, `H(N)` is the class number of not necessarily primitive positive-definite quadratic forms of discriminant `-N`, with weight `1 / 2` for forms equivalent to `a * (x ^ 2 + y ^ 2)` and weight `1 / 3` for forms equivalent to `a * (x ^ 2 + x * y + y ^ 2)`.

Stated but not proved: `Nat.hurwitzClassNumber` is written with `def_wanted` in [WantedExt/NumberTheory/QuadraticForms/ThreeSquares.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/ThreeSquares.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#hurwitz-class-number).

## Gauss's three-square formula, residues 1, 2, 5, 6 modulo 8

For every positive natural
number $n$ with $n \equiv 1$, $2$, $5$ or $6 \pmod 8$, the number $r_3(n)$ of ordered triples
$(x, y, z)$ of integers with $x^2 + y^2 + z^2 = n$ equals $12 H(4n)$, where $H$ is the Hurwitz
class number.

## Sources

- arXiv:2307.05244 `main.tex` lines 191-199.

Stated but not proved: `Nat.threeSquareRepresentationCount_eq_twelve_mul_hurwitzClassNumber_four_n` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/ThreeSquares.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/ThreeSquares.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#three-square-representation-count-eq-twe).

## Gauss's three-square formula, residue 3 modulo 8

For every positive natural number $n$
with $n \equiv 3 \pmod 8$, the number $r_3(n)$ of ordered triples $(x, y, z)$ of integers with
$x^2 + y^2 + z^2 = n$ equals $24 H(n)$, where $H$ is the Hurwitz class number.

## Sources

- arXiv:2307.05244 `main.tex` lines 191-199.

Stated but not proved: `Nat.threeSquareRepresentationCount_eq_twenty_four_mul_hurwitzClassNumber` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/ThreeSquares.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/QuadraticForms/ThreeSquares.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html#three-square-representation-count-eq-twe-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of three squares](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-three-squares)
