---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.HasSquareElementarySymmetricFunctions, MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.HasSquareElementarySymmetricFunctionsℚ, MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.IsSumTwoSquaresℚ, MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.IsSumTwoSquaresℤ, MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.IsSumTwoNonzeroSquaresℤ, MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.sum_two_squares_div_sum_two_squaresℚ, MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_pairwise_products, MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.isSumTwoSquaresℚ_of_hasSquareElementarySymmetricFunctionsℚ_and_scaling
statement: formalized
---

# Integer triples with square symmetric functions

17 results, 5 proved and 12 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html).

## Integer triples with square elementary symmetric functions

Integers $a$, $b$ and $c$
have square elementary symmetric functions when $a + b + c$, $ab + bc + ca$ and $abc$ are each
the square of an integer.

Formalized by `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.HasSquareElementarySymmetricFunctions`, a definition declared in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function).

## Rationals with square elementary symmetric functions

Rational numbers $a$, $b$, $c$
have square elementary symmetric functions when each of $a + b + c$, $ab + bc + ca$ and $abc$
is the square of a rational number.

Formalized by `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.HasSquareElementarySymmetricFunctionsℚ`, a definition declared in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-2).

## Sums of two rational squares

A rational number $q$ is a sum of two squares when
$q = x^2 + y^2$ for some rational numbers $x$ and $y$.

Formalized by `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.IsSumTwoSquaresℚ`, a definition declared in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#is-sum-two-squares).

## Sums of two integer squares

An integer $z$ is a sum of two squares when $z = x^2 + y^2$
for some integers $x$ and $y$.

Formalized by `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.IsSumTwoSquaresℤ`, a definition declared in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#is-sum-two-squares-2).

## Sums of two nonzero integer squares

An integer $z$ is a sum of two nonzero squares
when $z = x^2 + y^2$ for some nonzero integers $x$ and $y$.

Formalized by `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.IsSumTwoNonzeroSquaresℤ`, a definition declared in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#is-sum-two-nonzero-squares).

## Quotients of sums of two rational squares

If $\alpha$ and $\beta$ are nonzero rational
numbers that are each a sum of two squares of rational numbers, then $\alpha / \beta$ is also a
sum of two squares of rational numbers.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.sum_two_squares_div_sum_two_squaresℚ` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#sum-two-squares-div-sum-two-squares).

## Pairwise products preserve square symmetric functions

If $a$, $b$, $c$ are integers
such that each of $a + b + c$, $ab + bc + ca$ and $abc$ is the square of an integer, then the
same holds for the triple $ab$, $bc$, $ca$.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Lemma 2.

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_pairwise_products` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-3).

## Rational solutions are sums of two squares and rescale to integer solutions

Let $a$, $b$,
$c$ be rational numbers such that $a + b + c$, $ab + bc + ca$ and $abc$ are squares of rational
numbers. Then each of $a$, $b$ and $c$ is a sum of two squares of rational numbers. Moreover,
there is a nonzero rational number $k$ such that $A = ka$, $B = kb$ and $C = kc$ are integers,
$A + B + C$, $AB + BC + CA$ and $ABC$ are squares of integers, and each of $A$, $B$ and $C$ is a
sum of two squares of integers.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Lemma 3.

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.isSumTwoSquaresℚ_of_hasSquareElementarySymmetricFunctionsℚ_and_scaling` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#is-sum-two-squares-of-has-square-element).

## Choudhry's family (3.3) of integer triples with square symmetric functions

For all
integers $s$ and $t$, put $a = t^2 (s^2 - t^2)^2 (s^2 + t^2)$, $b = s^2 (s^2 - t^2)^2 (s^2 + t^2)$
and $c = 4 s^4 t^4$. Then each of $a + b + c$, $ab + bc + ca$ and $abc$ is the square of an
integer.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 1, family (3.3).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family33` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-4).

## Choudhry's family (3.4) of integer triples with square symmetric functions

For all
integers $s$ and $t$, put $a = 4 s^4 t^2 (s^2 + t^2)$, $b = 4 s^2 t^4 (s^2 + t^2)$ and
$c = (s^4 - t^4)^2$. Then each of $a + b + c$, $ab + bc + ca$ and $abc$ is the square of an
integer.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 1, family (3.4).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family34` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-5).

## Choudhry's family (3.5) of integer triples with square symmetric functions

For all
integers $s$ and $t$, let $f = s^6 - s^4 t^2 - 5 s^2 t^4 + t^6$ and
$g = 3 s^6 + s^4 t^2 + s^2 t^4 - t^6$, and put $a = 4 s^4 t^2 (s^2 + t^2) f^2$,
$b = (s^4 - t^4)^2 f^2$ and $c = 4 s^2 t^4 (s^2 + t^2) g^2$. Then each of $a + b + c$,
$ab + bc + ca$ and $abc$ is the square of an integer.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 1, family (3.5).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family35` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-6).

## Choudhry's family (3.6) of integer triples with square symmetric functions

For all
integers $s$ and $t$, let $f = s^6 - s^4 t^2 - 5 s^2 t^4 + t^6$ and
$g = 3 s^6 + s^4 t^2 + s^2 t^4 - t^6$, and put $a = t^2 (s^2 - t^2)^2 (s^2 + t^2) g^2$,
$b = 4 s^4 t^4 g^2$ and $c = s^2 (s^2 - t^2)^2 (s^2 + t^2) f^2$. Then each of $a + b + c$,
$ab + bc + ca$ and $abc$ is the square of an integer.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 1, family (3.6).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family36` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-7).

## Choudhry's family (3.30) of square triples with square symmetric functions

For all
integers $m$ and $n$, let $Q = m^4 - 6 m^2 n^2 + n^4$ and put $a = (m^4 - n^4)^2 Q^2$,
$b = 4 m^2 n^2 (m^2 + n^2)^2 Q^2$ and $c = 64 m^4 n^4 (m^2 - n^2)^4$. Then each of $a$, $b$,
$c$, $a + b + c$, $ab + bc + ca$ and $abc$ is the square of an integer.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 2, family (3.30).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family330_and_entries_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-8).

## Choudhry's family (3.31) of square triples with square symmetric functions

For all
integers $m$ and $n$, let $a = 64 m^4 n^4 (m^2 - n^2)^2$, $b = 16 m^2 n^2 (m^2 - n^2)^4$ and
$c = (m^2 + n^2)^2 (m^4 - 6 m^2 n^2 + n^4)^2$. Then $a + b + c$, $ab + bc + ca$ and $abc$ are
squares of integers, and $a$, $b$ and $c$ are themselves squares of integers.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 2, family (3.31).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family331_and_entries_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 196](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L196). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-9).

## Choudhry's family (3.32) of square triples with square symmetric functions

For all
integers $m$ and $n$, let $Q = m^4 - 6 m^2 n^2 + n^4$,
$P = m^{12} - 26 m^{10} n^2 + 79 m^8 n^4 - 44 m^6 n^6 + 79 m^4 n^8 - 26 m^2 n^{10} + n^{12}$ and
$R = m^{12} - 10 m^{10} n^2 + 15 m^8 n^4 - 204 m^6 n^6 + 15 m^4 n^8 - 10 m^2 n^{10} + n^{12}$,
and put $a = 64 m^4 n^4 (m^2 - n^2)^2 P^2$, $b = (m^2 + n^2)^2 Q^2 P^2$ and
$c = 16 m^2 n^2 (m^2 - n^2)^4 R^2$. Then each of $a$, $b$, $c$, $a + b + c$, $ab + bc + ca$ and
$abc$ is the square of an integer.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 2, family (3.32).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family332_and_entries_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 207](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L207). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-10).

## Choudhry's family (3.33) of square triples with square symmetric functions

For all
integers $m$ and $n$, let $Q = m^4 - 6 m^2 n^2 + n^4$,
$P = m^{12} - 26 m^{10} n^2 + 79 m^8 n^4 - 44 m^6 n^6 + 79 m^4 n^8 - 26 m^2 n^{10} + n^{12}$ and
$R = m^{12} - 10 m^{10} n^2 + 15 m^8 n^4 - 204 m^6 n^6 + 15 m^4 n^8 - 10 m^2 n^{10} + n^{12}$,
and put $a = (m^4 - n^4)^2 Q^2 R^2$, $b = 64 m^4 n^4 (m^2 - n^2)^4 R^2$ and
$c = 4 m^2 n^2 (m^2 + n^2)^2 Q^2 P^2$. Then each of $a$, $b$, $c$, $a + b + c$, $ab + bc + ca$
and $abc$ is the square of an integer.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 2, family (3.33).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family333_and_entries_square` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-11).

## Choudhry's family (3.34) of sums of two nonzero squares

For all nonzero integers $r$
and $s$, let $E = r^8 + 2 r^6 s^2 - 12 r^4 s^4 - 6 r^2 s^6 - s^8$,
$T = r^{12} + 6 r^{10} s^2 + 87 r^8 s^4 + 108 r^6 s^6 + 55 r^4 s^8 + 14 r^2 s^{10} + s^{12}$ and
$S = 5 r^6 + 3 r^4 s^2 + 3 r^2 s^4 + s^6$, and put $a = r^2 (r^2 + s^2) E^2 T$,
$b = s^2 (r^2 + s^2) S^2 E^2$ and $c = 4 r^4 s^4 S^2 T$. Then each of $a + b + c$, $ab + bc + ca$
and $abc$ is the square of an integer, and each of $a$, $b$, $c$ is a sum $x^2 + y^2$ of the
squares of two nonzero integers $x$ and $y$.

The hypothesis that $r$ and $s$ are nonzero is the nondegenerate range used in the proof.

## Sources

- Ajai Choudhry, "Three Integers Whose Sum, Product, and the Sum of the Products of the Integers, Taken Two at a Time, Are Perfect Squares", Theorem 3, family (3.34).

Stated but not proved: `MathlibExt.NumberTheory.ThreeIntegersSymmetricSquaresWanted.hasSquareElementarySymmetricFunctions_family334_and_entries_sum_two_nonzero_squares` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeIntegersSymmetricSquaresWanted.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html#has-square-elementary-symmetric-function-12).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integer triples with square symmetric functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/integer-triples-with-square-symmetric-functions)
