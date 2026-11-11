---
declaration: section
origin: cited
lean: Nat.polygonalNumber, Nat.polygonalNumber_zero, Nat.polygonalNumber_one, Nat.polygonalNumber_at_two, Nat.polygonalNumber_at_three, Nat.polygonalNumber_at_four, Nat.polygonalNumber_three, Nat.polygonalNumber_four
statement: formalized
proof: formalized
---

# Polygonal numbers

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html).

## Polygonal numbers

For natural numbers $s$ and $n$, the $n$-th $s$-gonal number is
$p_s(n) = (s - 2)\binom{n}{2} + n$, where $s - 2$ is truncated subtraction of natural numbers
(so it is $0$ when $s < 2$).

The polygonal interpretation assumes $s \ge 3$; this definition extends the formula to every
natural number $s$.

Formalized by `Nat.polygonalNumber`, a definition declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number).

## Polygonal numbers at zero

For every natural number $s$, $p_s(0) = 0$, where $p_s(n)$ is
the $n$-th $s$-gonal number.

The source considers only $s \ge 3$; the value holds for the extension of the formula to every
natural number $s$.

Formalized by `Nat.polygonalNumber_zero`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-zero).

## Polygonal numbers at one

For every natural number $s$, $p_s(1) = 1$, where $p_s(n)$ is
the $n$-th $s$-gonal number.

The source considers only $s \ge 3$; the value holds for the extension of the formula to every
natural number $s$.

Formalized by `Nat.polygonalNumber_one`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-one).

## Polygonal numbers at two

For every natural number $s \ge 3$, $p_s(2) = s$, where $p_s(n)$
is the $n$-th $s$-gonal number.

Formalized by `Nat.polygonalNumber_at_two`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-at-two).

## Polygonal numbers at three

For every natural number $s \ge 3$, $p_s(3) = 3s - 3$, where
$p_s(n)$ is the $n$-th $s$-gonal number.

Formalized by `Nat.polygonalNumber_at_three`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-at-three).

## Polygonal numbers at four

For every natural number $s \ge 3$, $p_s(4) = 6s - 8$, where
$p_s(n)$ is the $n$-th $s$-gonal number.

Formalized by `Nat.polygonalNumber_at_four`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-at-four).

## Closed form of the triangular numbers

For every natural number $n$, the $n$-th triangular
number is $p_3(n) = \frac{n(n + 1)}{2}$, where $p_s(n)$ is the $n$-th $s$-gonal number.

The quotient is exact, since $n(n + 1)$ is even.

Formalized by `Nat.polygonalNumber_three`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-three).

## Square numbers as polygonal numbers

For every natural number $n$, the $n$-th square
number is $p_4(n) = n^2$, where $p_s(n)$ is the $n$-th $s$-gonal number.

Formalized by `Nat.polygonalNumber_four`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-four).

## Closed form of the pentagonal numbers

For every natural number $n$, the $n$-th pentagonal
number is $p_5(n) = \frac{3n^2 - n}{2}$, where $p_s(n)$ is the $n$-th $s$-gonal number.

The quotient is exact, since $3n^2 - n = n(3n - 1)$ is even.

Formalized by `Nat.polygonalNumber_five`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-five).

## Closed form of the hexagonal numbers

For every natural number $n$, the $n$-th hexagonal
number is $p_6(n) = 2n^2 - n$, where $p_s(n)$ is the $n$-th $s$-gonal number.

Formalized by `Nat.polygonalNumber_six`, a theorem declared in [MathlibExt/NumberTheory/PolygonalNumber.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/PolygonalNumber.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html#polygonal-number-six).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Polygonal numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/waring-figurate/polygonal-numbers)
