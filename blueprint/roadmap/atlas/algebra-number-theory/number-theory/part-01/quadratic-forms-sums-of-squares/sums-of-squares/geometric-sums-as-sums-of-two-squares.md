---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.phi4pX1, MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.phi4pY1, MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.cyclotomicFourMul_eq_sq_add_sq, MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.cyclotomicFourMulPow_eq_sq_add_sq, MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.exists_sq_add_sq_eq_cyclotomic, MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.geomSum_pythagorean, MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.geomSumPow_eq_sq_add_sq, MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.altGeomSum_pythagorean
statement: formalized
---

# Geometric sums as sums of two squares

12 results, 2 proved and 10 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html).

## The alternating polynomial $X_1$

For a natural number $p$, $X_1$ is the polynomial with
integer coefficients

$$
X_1(x) = \sum_{i=0}^{\lfloor (p+1)/2 \rfloor - 1} (-1)^i x^{p-1-2i}.
$$

For odd $p \ge 5$ this is the even polynomial
$x^{p-1} - x^{p-3} + \dots - (-1)^{(p-1)/2} x^2 + (-1)^{(p-1)/2}$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Proposition 2.

Formalized by `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.phi4pX1`, a definition declared in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#phi4p-x1).

## The alternating polynomial $Y_1$

For a natural number $p$, $Y_1$ is the polynomial with
integer coefficients

$$
Y_1(x) = \sum_{i=0}^{\lfloor (p-1)/2 \rfloor - 1} (-1)^i x^{p-2-2i}.
$$

For odd $p \ge 5$ this is the odd polynomial
$x^{p-2} - x^{p-4} + \dots + (-1)^{(p-1)/2} x^3 - (-1)^{(p-1)/2} x$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Proposition 2.

Formalized by `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.phi4pY1`, a definition declared in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#phi4p-y1).

## The cyclotomic polynomial $\Phi_{4p}$ as a sum of two explicit squares

Let $p$ be an
odd prime, let $X_1 = \sum_{i=0}^{(p-1)/2} (-1)^i x^{p-1-2i}$ and
$Y_1 = \sum_{i=0}^{(p-3)/2} (-1)^i x^{p-2-2i}$ in $\mathbb{Z}[x]$, and let $\Phi_{4p}$ be the
$4p$-th cyclotomic polynomial over $\mathbb{Z}$. Then $\Phi_{4p} = X_1^2 + Y_1^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Proposition 2.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.cyclotomicFourMul_eq_sq_add_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#cyclotomic-four-mul-eq-sq-add-sq).

## The cyclotomic polynomial $\Phi_{4p^k}$ as a sum of two explicit squares

Let $p$ be an
odd prime, let $k \ge 1$, let $X_1 = \sum_{i=0}^{(p-1)/2} (-1)^i x^{p-1-2i}$ and
$Y_1 = \sum_{i=0}^{(p-3)/2} (-1)^i x^{p-2-2i}$ in $\mathbb{Z}[x]$, and let $\Phi_{4p^k}$ be the
$4p^k$-th cyclotomic polynomial over $\mathbb{Z}$. Then
$\Phi_{4p^k}(x) = X_1\bigl(x^{p^{k-1}}\bigr)^2 + Y_1\bigl(x^{p^{k-1}}\bigr)^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Corollary 3.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.cyclotomicFourMulPow_eq_sq_add_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#cyclotomic-four-mul-pow-eq-sq-add-sq).

## Every cyclotomic polynomial $\Phi_{4q}$ is a sum of two squares

For every integer
$q \ge 1$ there are polynomials $A, B \in \mathbb{Z}[x]$ such that the $4q$-th cyclotomic
polynomial $\Phi_{4q}$ over $\mathbb{Z}$ satisfies $\Phi_{4q} = A^2 + B^2$.

The paper gives the two squares explicitly, from a product over the primitive $4q$-th roots of
unity in the class $1 \pmod 4$; only their existence is stated here.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Proposition 4.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.exists_sq_add_sq_eq_cyclotomic` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#exists-sq-add-sq-eq-cyclotomic).

## Geometric sums for primes $p \equiv 3 \pmod 4$ and odd $n$ are sums of two squares

Let $p$ be a prime with $p \equiv 3 \pmod 4$, let $n$ be a positive odd integer, and let
$S = \sum_{j=0}^{p-1} p^{nj} = 1 + p^n + p^{2n} + \cdots + p^{(p-1)n}$. Then every prime divisor
of $S$ is $2$ or congruent to $1$ modulo $4$, and there are natural numbers $a, b$ with
$S = a^2 + b^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Theorem 10.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.geomSum_pythagorean` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#geom-sum-pythagorean).

## Geometric sums with $p^k$ terms, $p \equiv 3 \pmod 4$ and $n$ odd, are sums of two squares

Let $p$ be a prime with $p \equiv 3 \pmod 4$, let $n$ be a positive odd integer, let $k$ be a
positive integer, and put $q = p^k$. Then there are integers $a, b$ with
$\sum_{j=0}^{q-1} p^{nj} = 1 + p^n + p^{2n} + \cdots + p^{(q-1)n} = a^2 + b^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Corollary 11.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.geomSumPow_eq_sq_add_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#geom-sum-pow-eq-sq-add-sq).

## Alternating geometric sums for odd primes $p$ and even $n$ are sums of two coprime squares

Let $p$ be an odd prime, let $n$ be a positive even integer, and let
$S = \sum_{j=0}^{p-1} (-1)^j p^{nj} = 1 - p^n + p^{2n} - \cdots + p^{(p-1)n}$. Then every prime
divisor of $S$ is $2$ or congruent to $1$ modulo $4$, and there are coprime natural numbers
$a, b$ with $S = a^2 + b^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Theorem 5.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.altGeomSum_pythagorean` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#alt-geom-sum-pythagorean).

## Alternating geometric sums for primes $p \equiv 1 \pmod 4$ are sums of two squares

Let $p$ be a prime with $p \equiv 1 \pmod 4$, let $n \ge 0$ be an integer, and let
$S = \sum_{j=0}^{p-1} (-1)^j p^{nj} = 1 - p^n + p^{2n} - \cdots + p^{(p-1)n}$. Then every prime
divisor of $S$ is $2$ or congruent to $1$ modulo $4$, and there are natural numbers $a, b$ with
$S = a^2 + b^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Theorem 7.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.altGeomSum_pythagorean_one_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#alt-geom-sum-pythagorean-one-mod-four).

## Alternating geometric sums with $p^k$ terms, $p \equiv 1 \pmod 4$, as sums of two squares

Let $p$ be a prime with $p \equiv 1 \pmod 4$, let $n$ be a positive odd integer, let $k$ be a
positive integer, and put $q = p^k$. Then there are integers $a, b$ with
$\sum_{j=0}^{q-1} (-1)^j p^{nj} = 1 - p^n + p^{2n} - \cdots + p^{(q-1)n} = a^2 + b^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Corollary 8.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.altGeomSumPow_eq_sq_add_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#alt-geom-sum-pow-eq-sq-add-sq).

## Alternating geometric sums for primes $p \equiv 3 \pmod 4$ and odd $n$ are differences of two squares

**Alternating geometric sums for primes $p \equiv 3 \pmod 4$ and odd $n$ are differences of
two squares.** Let $p$ be a prime with $p \equiv 3 \pmod 4$ and let $n$ be a positive odd integer.
Then there are integers $a, b$ with
$\sum_{j=0}^{p-1} (-1)^j p^{nj} = 1 - p^n + p^{2n} - \cdots + p^{(p-1)n} = a^2 - b^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Proposition 9.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.altGeomSum_eq_sq_sub_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#alt-geom-sum-eq-sq-sub-sq).

## An alternating sum in coprime integers $x, y$ is a sum of two coprime squares

Let $x$ and $y$ be coprime integers, let $n$ be a positive integer, and let
$S = \sum_{j=0}^{2n} (-1)^j x^{4n-2j} y^{2j}$, that is,
$S = x^{4n} - x^{4n-2} y^2 + \cdots - x^2 y^{4n-2} + y^{4n}$. Then every prime divisor of $S$ is
$2$ or congruent to $1$ modulo $4$, and there are coprime natural numbers $a, b$ with
$S = a^2 + b^2$.

## Sources

- Lorenz Halbeisen, Norbert Hungerbühler, and Franz Lemmermeyer, "Geometric Sums as Sums of Two Squares", Theorem 6.

Stated but not proved: `MathlibExt.NumberTheory.GeometricSumsTwoSquaresWanted.altBigeom_pythagorean` is written with `theorem_wanted` in [WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/GeometricSumsTwoSquaresWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html#alt-bigeom-pythagorean).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Geometric sums as sums of two squares](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/geometric-sums-as-sums-of-two-squares)
