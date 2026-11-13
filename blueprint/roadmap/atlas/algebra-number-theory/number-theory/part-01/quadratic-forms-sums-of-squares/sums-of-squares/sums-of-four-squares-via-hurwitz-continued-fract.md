---
declaration: section
origin: cited
lean: MetaMathlibExt.hurwitzRound, MetaMathlibExt.hurwitzIter, MetaMathlibExt.hurwitzDigit, MetaMathlibExt.hurwitzPQ, MetaMathlibExt.hurwitzP, MetaMathlibExt.hurwitzQ, MetaMathlibExt.HurwitzLegal, MetaMathlibExt.abs_re_sub_hurwitzRound_le
statement: formalized
---

# Sums of four squares via Hurwitz continued fractions

13 results, 9 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html).

## Hurwitz rounding to the nearest Gaussian integer

For a complex number $z$, let
$[z] = m + n i$, where $m = \lfloor \operatorname{Re} z + 1/2 \rfloor$ and
$n = \lfloor \operatorname{Im} z + 1/2 \rfloor$; that is, the real and imaginary parts of $z$ are
rounded to the nearest integer, with halves rounded up. Then $[z]$ is a Gaussian integer nearest
to $z$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2 (notation `[z]`).

Formalized by `MetaMathlibExt.hurwitzRound`, a definition declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-round).

## Iterates of the Hurwitz algorithm

For a complex number $z$, the Hurwitz iterates are
$z_0 = z$ and $z_{n+1} = (z_n - [z_n])^{-1}$ for $n \ge 0$, where $[u]$ is the Gaussian integer
nearest to $u$, obtained by rounding the real and imaginary parts of $u$ to the nearest integer
with halves rounded up, and where the inverse of $0$ is taken to be $0$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2.

Formalized by `MetaMathlibExt.hurwitzIter`, a definition declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-iter).

## Partial quotients of the Hurwitz expansion

Let $z$ be a complex number with Hurwitz
iterates $z_0 = z, z_1, z_2, \dots$. For $n \ge 0$, the $n$-th partial quotient is $a_n = [z_n]$,
the Gaussian integer nearest to $z_n$, obtained by rounding the real and imaginary parts of
$z_n$ to the nearest integer with halves rounded up.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2.

Formalized by `MetaMathlibExt.hurwitzDigit`, a definition declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-digit).

## Consecutive pairs of Hurwitz convergents

Let $z$ be a complex number with Hurwitz
partial quotients $a_0, a_1, a_2, \dots$. This is the sequence whose term for $n \ge 0$ is the
pair of pairs of complex numbers $((P_{n-1}, Q_{n-1}), (P_n, Q_n))$, where $P_{-1} = 1$,
$Q_{-1} = 0$, $P_0 = a_0$, $Q_0 = 1$, and $P_{n+1} = a_{n+1} P_n + P_{n-1}$ and
$Q_{n+1} = a_{n+1} Q_n + Q_{n-1}$ for $n \ge 0$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2.

Formalized by `MetaMathlibExt.hurwitzPQ`, a definition declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-pq).

## Convergent numerators of the Hurwitz expansion

Let $z$ be a complex number with Hurwitz
partial quotients $a_0, a_1, a_2, \dots$. Its convergent numerators $P_n$, $n \ge 0$, are given by
$P_{-1} = 1$, $P_0 = a_0$ and $P_{n+1} = a_{n+1} P_n + P_{n-1}$ for $n \ge 0$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2.

Formalized by `MetaMathlibExt.hurwitzP`, a definition declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-p).

## Convergent denominators of the Hurwitz expansion

Let $z$ be a complex number with
Hurwitz partial quotients $a_0, a_1, a_2, \dots$. Its convergent denominators $Q_n$, $n \ge 0$,
are given by $Q_{-1} = 0$, $Q_0 = 1$ and $Q_{n+1} = a_{n+1} Q_n + Q_{n-1}$ for $n \ge 0$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2.

Formalized by `MetaMathlibExt.hurwitzQ`, a definition declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-q).

## Legal indices of the Hurwitz expansion

Let $z$ be a complex number with Hurwitz iterates
$z_j$ and partial quotients $a_j$. A natural number $n$ is a legal index for $z$ when
$z_j \ne a_j$ for every $j < n$, that is, when the Hurwitz expansion of $z$ has not terminated
before step $n$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2 (remark after Proposition 1).

Formalized by `MetaMathlibExt.HurwitzLegal`, a definition declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-legal).

## Rounding error of the nearest Gaussian integer

For every complex number $z$, let $[z]$ be
the Gaussian integer nearest to $z$, obtained by rounding the real and imaginary parts to the
nearest integer with halves rounded up. Then $|\operatorname{Re}(z - [z])| \le 1/2$ and
$|\operatorname{Im}(z - [z])| \le 1/2$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2 (the set `Φ`).

Formalized by `MetaMathlibExt.abs_re_sub_hurwitzRound_le`, a theorem declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#abs-re-sub-hurwitz-round-le).

## Recursion for the Hurwitz convergents

Let $z$ be a complex number with Hurwitz partial
quotients $a_n$, convergent numerators $P_n$ and convergent denominators $Q_n$. Then
$P_0 = a_0$, $Q_0 = 1$, $P_1 = a_1 a_0 + 1$ and $Q_1 = a_1$, and for every $n \ge 0$,
$P_{n+2} = a_{n+2} P_{n+1} + P_n$ and $Q_{n+2} = a_{n+2} Q_{n+1} + Q_n$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Section 2.

Formalized by `MetaMathlibExt.hurwitzPQ_recursion`, a theorem declared in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-pq-recursion).

## Error of the Hurwitz convergents

Let $z$ be a complex number with Hurwitz iterates
$z_0 = z, z_1, z_2, \dots$, convergent numerators $P_n$ and convergent denominators $Q_n$. For
every legal index $n$ for $z$,

$$Q_n z - P_n = (-1)^n (z_1 z_2 \cdots z_{n+1})^{-1},$$

and if moreover $n \ge 1$, then $z_{n+1} = -(Q_{n-1} z - P_{n-1}) / (Q_n z - P_n)$. Here the
inverse of $0$ and any quotient by $0$ are taken to be $0$.

The case $n = 0$ of the second identity, $z_1 = (z - a_0)^{-1}$ with $a_0$ the first partial
quotient (and $Q_{-1} = 0$, $P_{-1} = 1$), is the definition of the iterates.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Proposition 1.

Stated but not proved: `MetaMathlibExt.hurwitzQ_mul_sub_hurwitzP` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-q-mul-sub-hurwitz-p).

## Hurwitz's theorem: the convergent denominators grow in absolute value

Let $z$ be a
complex number and let $Q_0, Q_1, \dots$ be the convergent denominators of its Hurwitz continued
fraction expansion. For every $n \ge 0$ such that $n + 1$ is a legal index for $z$ (the
expansion has not terminated before step $n + 1$), $|Q_n| < |Q_{n+1}|$.

Since $Q_0 = 1$, this gives $1 = |Q_0| < |Q_1| < \cdots < |Q_m|$ for every legal index $m$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Lemma 1.

Stated but not proved: `MetaMathlibExt.norm_hurwitzQ_lt_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#norm-hurwitz-q-lt-succ).

## Lakein's first theorem on Hurwitz convergents

Let $z$ be a complex number and let $P_k$
and $Q_k$ be the convergent numerators and denominators of its Hurwitz continued fraction
expansion. For every legal index $k$ for $z$ (the expansion has not terminated before step $k$),
$|z - P_k / Q_k| \le 1 / |Q_k|^2$.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Lemma 2.

Stated but not proved: `MetaMathlibExt.norm_sub_hurwitz_convergent_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#norm-sub-hurwitz-convergent-le).

## Sums of four squares via Hurwitz continued fractions

Let $w$, $x$, $y$ be natural numbers
such that $w$ is odd and not a perfect square, $2x < w$, $2y < w$ and $w$ divides
$x^2 + y^2 + 1$. Expand $z = (x + yi)/w$ by the Hurwitz algorithm, with convergent numerators
$P_n$ and convergent denominators $Q_n$. Then there is exactly one natural number $n$ such that
$n + 1$ is a legal index for $z$, $|Q_n| \le \sqrt{w} < |Q_{n+1}|$, and, if $|Q_n| \ne \sqrt{w}$,
$w = |(x + yi) Q_n - w P_n|^2 + |Q_n|^2$.

When it holds, the last identity is a representation of $w$ as a sum of four squares.

## Sources

- Zhaonan Wang and Yingpu Deng, *Finding Sums of Four Squares via Complex Continued Fractions*, INTEGERS 24 (2024), Article A25, Theorem 1.

Stated but not proved: `MetaMathlibExt.hurwitz_four_squares` is written with `theorem_wanted` in [WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/HurwitzContinuedFractionFourSquaresWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html#hurwitz-four-squares).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of four squares via Hurwitz continued fractions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/sums-of-four-squares-via-hurwitz-continued-fract)
