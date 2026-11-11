---
declaration: section
origin: cited
lean: MetaMathlibExt.SoCSEq, MetaMathlibExt.IsSoCSSolution, MetaMathlibExt.isSoCSSolution_two_four_five, MetaMathlibExt.soCS_ratio_bounds, MetaMathlibExt.soCS_pell_param_pos_nonsquare, MetaMathlibExt.soCS_infinite_family_plane, MetaMathlibExt.soCS_odd_span, MetaMathlibExt.soCS_even_span_infinite
statement: formalized
---

# Sums of consecutive squares

10 results, 3 proved and 7 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html).

## The sum of consecutive squares equation

Integers $a$, $b$, $c$ satisfy the sum of
consecutive squares (SoCS) equation when $2\,b(b+1)(2b+1) = a(a+1)(2a+1) + c(c+1)(2c+1)$.

With $P_n = n(n+1)(2n+1)/6$ this is $P_a + P_c = 2P_b$ multiplied by $6$. For $a < b < c$ it is
equivalent to $(a+1)^2 + (a+2)^2 + \dots + b^2 = (b+1)^2 + (b+2)^2 + \dots + c^2$, since
$P_n - P_{n-1} = n^2$. No order or sign condition on $a$, $b$, $c$ is imposed.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, equations (1) and (2).

Formalized by `MetaMathlibExt.SoCSEq`, a definition declared in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cseq).

## Solutions of the sum of consecutive squares problem

A triple of integers
$(a, b, c)$ is a SoCS solution when $0 < a + 1 < b < c$ and $(a, b, c)$ satisfies the sum of
consecutive squares equation $2\,b(b+1)(2b+1) = a(a+1)(2a+1) + c(c+1)(2c+1)$, that is,
$(a+1)^2 + \dots + b^2 = (b+1)^2 + \dots + c^2$.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Section 1.

Formalized by `MetaMathlibExt.IsSoCSSolution`, a definition declared in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#is-so-cssolution).

## $(2, 4, 5)$ solves the sum of consecutive squares problem

The triple $(2, 4, 5)$ is a
solution of the sum of consecutive squares problem: $0 < 3 < 4 < 5$ and $3^2 + 4^2 = 5^2$.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Section 1.

Formalized by `MetaMathlibExt.isSoCSSolution_two_four_five`, a theorem declared in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#is-so-cssolution-two-four-five).

## Bounds on the ratio of the two spans

For every solution $(a, b, c)$ of the sum of
consecutive squares problem, $1 < (b - a)/(c - b) < 1 + 2^{1/3} + 2^{2/3}$.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Lemma 1.

Stated but not proved: `MetaMathlibExt.soCS_ratio_bounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cs-ratio-bounds).

## The Pell-type parameter is a positive nonsquare

For every solution $(a, b, c)$ of the
sum of consecutive squares problem, the integer
$A = 3(b - c)^2\bigl(12(b - a)^2(c - b)^2 - (a - 2b + c)^4\bigr)$ is positive and is not a
perfect square.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Corollary 1, verified against arXiv:2411.08398 (the formula is garbled in the statement extraction).

Stated but not proved: `MetaMathlibExt.soCS_pell_param_pos_nonsquare` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cs-pell-param-pos-nonsquare).

## Infinite families of solutions in a plane

Let $(a, b, c)$ be a solution of the sum of
consecutive squares problem. Then there are infinitely many distinct integer triples $(x, y, z)$
satisfying the sum of consecutive squares equation
$2\,y(y+1)(2y+1) = x(x+1)(2x+1) + z(z+1)(2z+1)$, with no order or sign condition, such that
$(b - c)x + (c - a)y + (a - b)z = 0$ and $z - x \equiv c - a \pmod 2$.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Proposition 1.

Stated but not proved: `MetaMathlibExt.soCS_infinite_family_plane` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cs-infinite-family-plane).

## Solutions with odd span $c - a$

For every odd integer $N \ge 3$ there is a solution
$(a, b, c)$ of the sum of consecutive squares problem with $c - a = N$, together with infinitely
many distinct solutions $(x, y, z)$ of that problem with $z - x$ odd, all lying in the plane
$(b - c)x + (c - a)y + (a - b)z = 0$, which passes through $(a, b, c)$ and contains the line
$x = y = z$.

The paper also states that this plane is unique for each $N$; that uniqueness clause is not part
of this statement.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Theorem 2, verified against arXiv:2411.08398.

Stated but not proved: `MetaMathlibExt.soCS_odd_span` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cs-odd-span).

## Infinitely many solutions with $c - a$ even

There are infinitely many solutions
$(a, b, c)$ of the sum of consecutive squares problem with $c - a$ even.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Theorem 3.

Stated but not proved: `MetaMathlibExt.soCS_even_span_infinite` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cs-even-span-infinite).

## At most $2(N - 1)$ solutions with $c - a = N$

For every integer $N > 1$,
there are at most $2(N - 1)$ solutions $(a, b, c)$ of the sum of consecutive squares problem
with $c - a = N$.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Theorem 5.

Stated but not proved: `MetaMathlibExt.soCS_card_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cs-card-le).

## No finitely many planes contain all solutions

Let $S$ be a finite set of affine planes
$ux + vy + wz = t$ in $\mathbb{R}^3$, with $u, v, w, t$ real and $(u, v, w) \ne (0, 0, 0)$. Then
some solution $(a, b, c)$ of the sum of consecutive squares problem lies on none of the planes in
$S$, that is, $ua + vb + wc \ne t$ for every plane in $S$.

## Sources

- Anderson, Woodall and Zaharescu, *Arithmetic Polygons and Sums of Consecutive Squares*, INTEGERS 26 (2026), Article A1, Corollary 2; the proof text appended to the extracted statement is not part of the claim.

Stated but not proved: `MetaMathlibExt.soCS_not_finite_planes` is written with `theorem_wanted` in [WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ConsecutiveSquaresWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html#so-cs-not-finite-planes).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of consecutive squares](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-equations/pell-quadratic-equations/sums-of-consecutive-squares)
