---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.QuadraticForms.BinaryQuadraticArithmeticProgressionsWanted.exists_int_representations_of_rat_arithmetic_progression, MathlibExt.NumberTheory.QuadraticForms.BinaryQuadraticArithmeticProgressionsWanted.exists_representation_nine_term_diagonal_quadratic, MathlibExt.NumberTheory.QuadraticForms.BinaryQuadraticArithmeticProgressionsWanted.exists_nine_term_arithmetic_progression_binary_quadratic
statement: formalized
---

# Arithmetic progressions represented by binary forms

3 results, 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/arithmetic-progressions-represented-by-binary-fo/index.html).

## Rational representations of an arithmetic progression scale to integral ones

Let
$a, b, c$ be integers, $n$ a natural number and $u_0, d$ rational numbers. If for every natural
number $i < n$ there are rational numbers $x, y$ with $ax^2 + bxy + cy^2 = u_0 + id$, then there
is a nonzero integer $k$ such that for every natural number $i < n$ there are integers $x, y$
with $ax^2 + bxy + cy^2 = k^2(u_0 + id)$.

The nonzero condition on $k$ is the paper's common-denominator choice; it also excludes the
trivial zero scaling.

## Sources

- Ajai Choudhry, "Arithmetic Progressions Represented by Binary Quadratic Forms", Lemma 1.

Stated but not proved: `MathlibExt.NumberTheory.QuadraticForms.BinaryQuadraticArithmeticProgressionsWanted.exists_int_representations_of_rat_arithmetic_progression` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/BinaryQuadraticArithmeticProgressionsWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticForms/BinaryQuadraticArithmeticProgressionsWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/arithmetic-progressions-represented-by-binary-fo/index.html#exists-int-representations-of-rat-arithm).

## Nine-term arithmetic progressions represented by $px^2 + qy^2$

Let $p, q, g, h$ be
integers such that $-4pq$ is not a perfect square, and put

$$
u_1 = 4p^5g^{10} - 47p^4qg^8h^2 - 156p^3q^2g^6h^4 + 2052p^2q^3g^4h^6 +
4833pq^4g^2h^8 + 324q^5h^{10}
$$

and

$$
d = 12pqg^2h^2(pg^2 - 3qh^2)(pg^2 + 6qh^2)(2pg^2 + 3qh^2).
$$

Then for every natural number $i < 9$ there are integers $x, y$ with $u_1 + id = px^2 + qy^2$.

## Sources

- Ajai Choudhry, "Arithmetic Progressions Represented by Binary Quadratic Forms", Theorem 1, relations (3.1).

Stated but not proved: `MathlibExt.NumberTheory.QuadraticForms.BinaryQuadraticArithmeticProgressionsWanted.exists_representation_nine_term_diagonal_quadratic` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/BinaryQuadraticArithmeticProgressionsWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticForms/BinaryQuadraticArithmeticProgressionsWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/arithmetic-progressions-represented-by-binary-fo/index.html#exists-representation-nine-term-diagonal).

## Binary quadratic forms with non-square discriminant represent nine-term progressions

Let $a, b, c$ be integers such that the discriminant $b^2 - 4ac$ is not a perfect square. Then
there are integers $u_0$ and $d \ne 0$ such that for every natural number $i < 9$ there are
integers $x, y$ with $u_0 + id = ax^2 + bxy + cy^2$.

The condition $d \ne 0$ excludes constant progressions.

## Sources

- Ajai Choudhry, "Arithmetic Progressions Represented by Binary Quadratic Forms", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.QuadraticForms.BinaryQuadraticArithmeticProgressionsWanted.exists_nine_term_arithmetic_progression_binary_quadratic` is written with `theorem_wanted` in [WantedExt/NumberTheory/QuadraticForms/BinaryQuadraticArithmeticProgressionsWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/QuadraticForms/BinaryQuadraticArithmeticProgressionsWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/arithmetic-progressions-represented-by-binary-fo/index.html#exists-nine-term-arithmetic-progression).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Arithmetic progressions represented by binary forms](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/arithmetic-progressions-represented-by-binary-fo/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/binary-quaternary-forms/arithmetic-progressions-represented-by-binary-fo)
