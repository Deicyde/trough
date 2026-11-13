---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.primitive_pythagorean_sides_sum_two_squares_infinite, MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.primitive_pythagorean_sides_square_middle_infinite, MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.primitive_pythagorean_sides_sum_two_cubes_infinite, MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.rational_right_triangles_reciprocal_sums_infinite, MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.rational_right_triangles_reciprocal_differences_infinite, MetaMathlibExt.amatoCathetusParams, MetaMathlibExt.one_mem_amatoCathetusParams_three, MetaMathlibExt.two_mem_amatoCathetusParams_four
statement: formalized
---

# Pythagorean triples

20 results, 10 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html).

## Infinitely many primitive Pythagorean triples with sides sums of two squares

There are
infinitely many triples $(X, Y, Z)$ of natural numbers with $X^2 + Y^2 = Z^2$ and
$\gcd(X, Y) = 1$ such that each of $X$, $Y$ and $Z$ is a sum of two squares of positive
integers.

## Sources

- Yangcheng Li and Yong Zhang, "Primitive Pythagorean Triangles with Sides of Certain Forms", Theorem 1.

Stated but not proved: `MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.primitive_pythagorean_sides_sum_two_squares_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#primitive-pythagorean-sides-sum-two-squa).

## Infinitely many primitive Pythagorean triples with a square leg

There are infinitely
many triples $(X, Y, Z)$ of natural numbers with $X^2 + Y^2 = Z^2$ and $\gcd(X, Y) = 1$ such that
$X$ and $Z$ are each a sum of two squares of positive integers and $Y$ is the square of a
positive integer.

## Sources

- Yangcheng Li and Yong Zhang, "Primitive Pythagorean Triangles with Sides of Certain Forms", Corollary 1.

Stated but not proved: `MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.primitive_pythagorean_sides_square_middle_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#primitive-pythagorean-sides-square-middl).

## Infinitely many primitive Pythagorean triples with sides sums of two cubes

There are
infinitely many triples $(X, Y, Z)$ of natural numbers with $X^2 + Y^2 = Z^2$ and
$\gcd(X, Y) = 1$ such that each of $X$, $Y$ and $Z$ is a sum of two cubes of positive
integers.

## Sources

- Yangcheng Li and Yong Zhang, "Primitive Pythagorean Triangles with Sides of Certain Forms", Theorem 2.

Stated but not proved: `MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.primitive_pythagorean_sides_sum_two_cubes_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#primitive-pythagorean-sides-sum-two-cube).

## Infinitely many rational right triangles with sides sums of unit fractions

There are
infinitely many triples $(X, Y, Z)$ of positive rational numbers with $X^2 + Y^2 = Z^2$ such
that each of $X$, $Y$ and $Z$ has the form $1/u + 1/v$ for some positive integers $u$ and $v$.

## Sources

- Yangcheng Li and Yong Zhang, "Primitive Pythagorean Triangles with Sides of Certain Forms", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.rational_right_triangles_reciprocal_sums_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#rational-right-triangles-reciprocal-sums).

## Infinitely many rational right triangles with sides differences of unit fractions

There
are infinitely many triples $(X, Y, Z)$ of positive rational numbers with $X^2 + Y^2 = Z^2$ such
that each of $X$, $Y$ and $Z$ has the form $1/u - 1/v$ for some positive integers $u$ and $v$.

## Sources

- Yangcheng Li and Yong Zhang, "Primitive Pythagorean Triangles with Sides of Certain Forms", Theorem 3.

Stated but not proved: `MathlibExt.NumberTheory.PrimitivePythagoreanFormsWanted.rational_right_triangles_reciprocal_differences_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PrimitivePythagoreanFormsWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#rational-right-triangles-reciprocal-diff).

## Amato's cathetus parameter set

For a natural number $x$, let $n$ be the exponent of $2$
in $x$ (taken to be $0$ for $x = 0$). The set $C(x)$ consists of the natural numbers $d$ with
$d \le x$ and $d \mid x^2$ such that, if $x$ is even, $d = 2^s l$ for some natural numbers $s$ and
$l$ with $1 \le s \le n - 1$ and $l \mid x^2$.

This is the definition as printed in the source: for odd $x$ it is
$D(x) = \{d \in \mathbb{N} : d \le x,\ d \mid x^2\}$, and for even $x = 2^n k$ with $k$ odd it is
$D(x) \cap P(x)$ with $P(x) = \{2^s l : l \mid x^2,\ s \in \{1, \dots, n - 1\}\}$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 1 (quoting [1]).

Formalized by `MetaMathlibExt.amatoCathetusParams`, a definition declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#amato-cathetus-params).

## Amato's parameter set for the cathetus $3$ contains $1$

We have $1 \in C(3)$, where
$C(x)$ is Amato's cathetus parameter set.

The parameter $d = 1$ generates the triple $(3, 4, 5)$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 1 (quoting [1]).

Formalized by `MetaMathlibExt.one_mem_amatoCathetusParams_three`, a theorem declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#one-mem-amato-cathetus-params-three).

## $2$ is an Amato parameter for the cathetus $4$

The number $2$ belongs to Amato's parameter
set $C(4)$ for the cathetus $4$.

With $x = 4$ and $d = 2$, the formulas $x^2 / (2d) \mp d / 2$ give $3$ and $5$, so $2$ generates
the triple $(4, 3, 5)$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 1 (quoting [1]).

Formalized by `MetaMathlibExt.two_mem_amatoCathetusParams_four`, a theorem declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#two-mem-amato-cathetus-params-four).

## Products of Pythagorean triples through a cathetus

Let $a$ and $b$ be positive natural
numbers, and let $d_1 \in C(a)$ and $d_2 \in C(b)$, where $C(x)$ is Amato's cathetus parameter
set. Define the rational numbers $a_1 = a^2/(2 d_1) - d_1/2$, $a_2 = a^2/(2 d_1) + d_1/2$,
$b_1 = b^2/(2 d_2) - d_2/2$, $b_2 = b^2/(2 d_2) + d_2/2$,
$y = (ab)^2/(2 d_1 d_2) - d_1 d_2/2$ and $z = (ab)^2/(2 d_1 d_2) + d_1 d_2/2$, so that
$(a, a_1, a_2)$, $(b, b_1, b_2)$ and $(ab, y, z)$ are the triples generated by $d_1$, $d_2$ and
$d_1 d_2$ through $x^2/(2d) \mp d/2$. Then $y = a_1 b_2 + a_2 b_1$,
$z = a_1 b_2 + a_2 b_1 + d_1 d_2$, $y = a_1 b_1 + a_2 b_2 - d_1 d_2$, $z = a_1 b_1 + a_2 b_2$,
and $d_1 d_2 \in C(ab)$.

The source takes any triple $(ab, y, z)$ with $z - y = d_3 \in C(ab)$ and concludes
$d_3 = d_1 d_2$, which is false as printed: for $(3, 4, 5)$ taken twice ($d_1 = d_2 = 1$) and
$(9, 12, 15)$ ($d_3 = 3 \in C(9)$), $d_3 \ne d_1 d_2$ and $a_1 b_2 + a_2 b_1 = 40 \ne 12$.
Following the closing clause "with $d_3 = d_1 \cdot d_2$", the triple for $ab$ is the one
generated by $d_3 = d_1 d_2$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 2 (quoting [1], [3]).

Stated but not proved: `MetaMathlibExt.pythagorean_cathetus_product` is written with `theorem_wanted` in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#pythagorean-cathetus-product).

## Amato's product of triples

For a commutative ring $R$, the product of two triples
$(x, y, z)$ and $(x', y', z')$ in $R^3$ is

$$(x, y, z) \star (x', y', z') = (x x',\ y z' + z y',\ y z' + z y' + (z - y)(z' - y')).$$

This is the source's product (4); its operation (12) on integral triples is the same formula.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Lemma 1, (4).

Formalized by `MetaMathlibExt.pythagoreanTripleMul`, a definition declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#pythagorean-triple-mul).

## Amato's product of $(3, 4, 5)$ with itself

For integer triples,
$(3, 4, 5) \star (3, 4, 5) = (9, 40, 41)$, where $\star$ is Amato's product of triples.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Lemma 1, (4).

Formalized by `MetaMathlibExt.pythagoreanTripleMul_three_four_five`, a theorem declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#pythagorean-triple-mul-three-four-five).

## Right identity for Amato's product

For every commutative ring $R$ and every triple
$u \in R^3$, we have $u \star (1, 0, 1) = u$, where $\star$ is Amato's product of triples.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 3, (7)-(8).

Formalized by `MetaMathlibExt.pythagoreanTripleMul_one`, a theorem declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#pythagorean-triple-mul-one).

## Rational Pythagorean triples

The set $E$ consists of the triples $(x, y, z)$ of rational
numbers with $x \ne 0$ and $x^2 + y^2 = z^2$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Section 2, definition of `E`.

Formalized by `MetaMathlibExt.ratPythagoreanTriples`, a definition declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#rat-pythagorean-triples).

## $(3, 4, 5)$ is a rational Pythagorean triple

The triple $(3, 4, 5)$ belongs to the set $E$
of rational triples $(x, y, z)$ with $x \neq 0$ and $x^2 + y^2 = z^2$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Section 2, definition of `E`.

Formalized by `MetaMathlibExt.three_four_five_mem_ratPythagoreanTriples`, a theorem declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#three-four-five-mem-rat-pythagorean-trip).

## Amato's product preserves rational Pythagorean triples

Let $E$ be the set of rational
triples $(x, y, z)$ with $x \ne 0$ and $x^2 + y^2 = z^2$, and let $\star$ be Amato's product of
triples. If $u \in E$ and $v \in E$, then $u \star v \in E$; that is, $\star$ is a binary
operation on $E$.

The source's fraction representation $(a/b, c/d, e/f)$ with $a, b, d, f \ne 0$ describes the
same set $E$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Lemma 1.

Stated but not proved: `MetaMathlibExt.pythagoreanTripleMul_mem_ratPythagoreanTriples` is written with `theorem_wanted` in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#pythagorean-triple-mul-mem-rat-pythagore).

## Group laws for Amato's product on rational Pythagorean triples

Let $E$ be the set of
rational triples $(x, y, z)$ with $x \ne 0$ and $x^2 + y^2 = z^2$, and let $\star$ be Amato's
product of triples. Then $(1, 0, 1) \in E$; $(u \star v) \star w = u \star (v \star w)$ for all
$u, v, w \in E$; $u \star v = v \star u$ for all $u, v \in E$; $u \star (1, 0, 1) = u$ for every
$u \in E$; every $u \in E$ has some $v \in E$ with $u \star v = (1, 0, 1)$; and $E$ is infinite.

Together with the closure of $E$ under $\star$ (stated separately), this makes $E$ an infinite
commutative group under $\star$ with identity $(1, 0, 1)$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 3.

Stated but not proved: `MetaMathlibExt.ratPythagoreanTriples_commGroup` is written with `theorem_wanted` in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#rat-pythagorean-triples-comm-group).

## Integral Pythagorean triples form a commutative monoid

Let $M$ be the set of integer
triples $(a, b, c)$ with $a^2 + b^2 = c^2$, let $N$ be the set of triples in $M$ whose three
entries are nonnegative, and let $\star$ be Amato's product of triples. Then the product of two
triples in $M$ lies in $M$, $\star$ is associative and commutative on $M$, and
$u \star (1, 0, 1) = u$ for every $u \in M$. Moreover $(1, 0, 1) \in N$, the product of two
triples in $N$ lies in $N$, and $N$ is infinite. So $M$ is an infinite commutative monoid with
identity $(1, 0, 1)$, and $N$ is an infinite submonoid.

The source prints its operation (12) as $(a, b, c) \star (e, f, g) = (ae, bf + ce, \dots)$ with
$d_2 = f - e$; it is read as
$(a, b, c) \star (d, e, f) = (ad,\ bf + ce,\ bf + ce + (c - b)(f - e))$, the integral case of (4),
as the source states.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Corollary 1.

Stated but not proved: `MetaMathlibExt.intPythagoreanTriples_commMonoid` is written with `theorem_wanted` in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#int-pythagorean-triples-comm-monoid).

## Amato's product on rational points of the unit circle

For rational pairs $(x, y)$ and
$(x', y')$, the product is
$(x, y) \odot (x', y') = (x x' / (1 + y y'), (y + y') / (1 + y y'))$, where division by $0$
gives $0$; so the product is $(0, 0)$ when $1 + y y' = 0$.

For points $(a/c, b/c)$ and $(d/f, e/f)$ with $c, f \neq 0$ this reads
$(ad / (cf + eb), (bf + ec) / (cf + eb))$, the form (14)(I) of the source.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 4, (14)(I).

Formalized by `MetaMathlibExt.unitCircleRatMul`, a definition declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#unit-circle-rat-mul).

## Squaring $(3/5, 4/5)$ under Amato's product

For Amato's product
$(x, y) \odot (x', y') = (x x' / (1 + y y'), (y + y') / (1 + y y'))$ on $\mathbb{Q}^2$, we have
$(3/5, 4/5) \odot (3/5, 4/5) = (9/41, 40/41)$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 4, (14)(I).

Formalized by `MetaMathlibExt.unitCircleRatMul_three_four_five`, a theorem declared in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#unit-circle-rat-mul-three-four-five).

## Amato's group law on rational points of the unit circle

Let
$P = \{(x, y) \in \mathbb{Q}^2 : x \neq 0,\ x^2 + y^2 = 1\}$ and let $\odot$ be Amato's product
$(x, y) \odot (x', y') = (x x' / (1 + y y'), (y + y') / (1 + y y'))$. Then $(1, 0) \in P$; for all
$p, q \in P$ we have $p \odot q \in P$; $\odot$ is associative and commutative on $P$; for every
$(x, y) \in P$ we have $(x, y) \odot (1, 0) = (x, y)$ and $(x, y) \odot (x, -y) = (1, 0)$; and $P$
is infinite.

$P$ is the set of points $(a/c, b/c)$ coming from primitive Pythagorean triples $(a, b, c)$ with
$a \neq 0$: writing a rational point of the unit circle over its reduced common denominator gives
a primitive triple. Rules (II) and (III) of (14) in the source concern fraction representatives
and hold automatically in $\mathbb{Q}$.

## Sources

- Roberto Amato, *Groups and Monoid in the Set of Pythagorean Triples*, INTEGERS 24 (2024), Article A5, Theorem 4.

Stated but not proved: `MetaMathlibExt.unitCircleRat_commGroup` is written with `theorem_wanted` in [WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/PythagoreanTripleGroupsWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html#unit-circle-rat-comm-group).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pythagorean triples](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/pythagorean-triples)
