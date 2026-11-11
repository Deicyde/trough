---
declaration: section
origin: cited
lean: MetaMathlibExt.frobeniusRepCount, MetaMathlibExt.frobeniusRepCount_eq_zero_of_neg, MetaMathlibExt.frobeniusRepCount_ne_top, MetaMathlibExt.IsGenFrobeniusNumber, MetaMathlibExt.IsGenFrobeniusNumber.unique
statement: formalized
proof: formalized
---

# Generalized Frobenius numbers

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers/index.html).

## Number of representations by a vector of generators

For natural numbers
$a_1, \dots, a_k$ and an integer $m$, the representation count $d(m; a_1, \dots, a_k)$ is the
number of tuples $(x_1, \dots, x_k)$ of natural numbers with $x_1 a_1 + \dots + x_k a_k = m$,
counted as an extended natural number, so that it is $\infty$ when there are infinitely many such
tuples.

It is $0$ for $m < 0$, and finite when every $a_i$ is positive.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Introduction (definition of `d(n; a₁, …, a_k)`).

Formalized by `MetaMathlibExt.frobeniusRepCount`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers/index.html#frobenius-rep-count).

## Negative integers have no representations

For all natural numbers $a_1, \dots, a_k$ and
every integer $m < 0$, the representation count $d(m; a_1, \dots, a_k)$ is $0$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Introduction (definition of `d(n; a₁, …, a_k)`).

Formalized by `MetaMathlibExt.frobeniusRepCount_eq_zero_of_neg`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers/index.html#frobenius-rep-count-eq-zero-of-neg).

## Finitely many representations for positive generators

If $a_1, \dots, a_k$ are positive
natural numbers, then for every integer $m$ the representation count $d(m; a_1, \dots, a_k)$ is
finite.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Introduction (definition of `d(n; a₁, …, a_k)`).

Formalized by `MetaMathlibExt.frobeniusRepCount_ne_top`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers/index.html#frobenius-rep-count-ne-top).

## Generalized Frobenius number

For natural numbers $a_1, \dots, a_k$ and $s$, write
$d(m; a)$ for the number of representations of an integer $m$ by $a = (a_1, \dots, a_k)$. An
integer $g$ is the generalized Frobenius number $g(a; s) = \max \{m \in \mathbb{Z} \mid
d(m; a) \le s\}$ when $d(g; a) \le s$ and $d(m; a) > s$ for every integer $m > g$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Introduction (definition of `g(A; s)`).

Formalized by `MetaMathlibExt.IsGenFrobeniusNumber`, a definition declared in [MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers/index.html#is-gen-frobenius-number).

## Uniqueness of the generalized Frobenius number

For natural numbers $a_1, \dots, a_k$ and
$s$, if the integers $g$ and $g'$ are both the generalized Frobenius number $g(a_1, \dots, a_k; s)$,
then $g = g'$.

## Sources

- Kittipong Subwattanachai, *Formulas for the Generalized Frobenius Number of Triangular Numbers*, INTEGERS 26 (2026), Article A63, Introduction (definition of `g(A; s)` as a maximum).

Formalized by `MetaMathlibExt.IsGenFrobeniusNumber.unique`, a theorem declared in [MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/GeneralizedFrobeniusNumber.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers/index.html#unique).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Generalized Frobenius numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/numerical-semigroups/generalized-frobenius-numbers)
