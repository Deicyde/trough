---
declaration: section
origin: cited
lean: SumSquares.divChiSum, SumSquares.divChiSum_mul_of_coprime, SumSquares.divChiSum_one, SumSquares.divChiSum_prime_pow_two, SumSquares.divChiSum_prime_pow_split, SumSquares.divChiSum_prime_pow_inert, SumSquares.pairEquivGaussianNormFiber, SumSquares.representationNumber_two_eq
statement: formalized
proof: formalized
---

# Jacobi's two-square theorem

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html).

## Divisor sum of the character modulo 4

For a natural number $n$, this is the integer
$\sum_{d \mid n} \chi_4(d)$, the sum over the positive divisors $d$ of $n$ of the nonprincipal
Dirichlet character $\chi_4$ modulo 4, which takes the value $0$ at even $d$, $1$ at
$d \equiv 1 \pmod 4$ and $-1$ at $d \equiv 3 \pmod 4$. For $n = 0$ there are no divisors and the
sum is $0$.

Formalized by `SumSquares.divChiSum`, a definition declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#div-chi-sum).

## The divisor sum of $\chi_4$ is multiplicative

Let $\chi_4$ be the nonprincipal Dirichlet
character modulo 4 and, for a natural number $n$, write $S(n) = \sum_{d \mid n} \chi_4(d)$ for
the sum over the positive divisors $d$ of $n$ (so $S(0) = 0$). If $m$ and $n$ are coprime natural
numbers, then $S(mn) = S(m)\,S(n)$.

Formalized by `SumSquares.divChiSum_mul_of_coprime`, a theorem declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#div-chi-sum-mul-of-coprime).

## The divisor sum of $\chi_4$ at one

For the nonprincipal Dirichlet character $\chi_4$
modulo 4, the sum $\sum_{d \mid 1} \chi_4(d)$ over the divisors of $1$ equals $1$.

Formalized by `SumSquares.divChiSum_one`, a theorem declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#div-chi-sum-one).

## The divisor sum of $\chi_4$ at powers of two

Let $\chi_4$ be the nonprincipal Dirichlet
character modulo 4. For every natural number $e$, $\sum_{d \mid 2^e} \chi_4(d) = 1$: only the
divisor $1$ contributes.

Formalized by `SumSquares.divChiSum_prime_pow_two`, a theorem declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#div-chi-sum-prime-pow-two).

## The divisor sum of $\chi_4$ at powers of a prime $p \equiv 1 \pmod 4$

Let $\chi_4$ be
the nonprincipal Dirichlet character modulo 4. If $p$ is a prime with $p \equiv 1 \pmod 4$ and
$e$ is a natural number, then $\sum_{d \mid p^e} \chi_4(d) = e + 1$.

Formalized by `SumSquares.divChiSum_prime_pow_split`, a theorem declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#div-chi-sum-prime-pow-split).

## The divisor sum of $\chi_4$ at powers of a prime $q \equiv 3 \pmod 4$

Let $\chi_4$ be
the nonprincipal Dirichlet character modulo 4. If $q$ is a prime with $q \equiv 3 \pmod 4$ and
$f$ is a natural number, then $\sum_{d \mid q^f} \chi_4(d)$ equals $1$ when $f$ is even and $0$
when $f$ is odd.

Formalized by `SumSquares.divChiSum_prime_pow_inert`, a theorem declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#div-chi-sum-prime-pow-inert).

## Sums of two squares as Gaussian norms

For a natural number $j$, the map
$(a, b) \mapsto a + bi$ is a bijection from the set of integer pairs $(a, b)$ with
$a^2 + b^2 = j$ to the set of Gaussian integers $z$ with norm $N(z) = j$; its inverse sends $z$
to the pair of its real and imaginary parts.

Formalized by `SumSquares.pairEquivGaussianNormFiber`, a definition declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#pair-equiv-gaussian-norm-fiber).

## Two-square representation numbers count integer pairs

For every natural number $j$,
the representation number $r_2(j)$ equals the number of pairs $(a, b)$ of integers with
$a^2 + b^2 = j$.

Formalized by `SumSquares.representationNumber_two_eq`, a theorem declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#representation-number-two-eq).

## Jacobi's two-square theorem

Let $\chi_4$ be the nonprincipal Dirichlet character modulo
$4$, so $\chi_4(d)$ is $0$ for even $d$, $1$ for $d \equiv 1 \pmod 4$ and $-1$ for
$d \equiv 3 \pmod 4$. For every natural number $j \ge 1$, the representation number $r_2(j)$,
the number of integer pairs $(x_1, x_2)$ with $x_1^2 + x_2^2 = j$ counted with order and signs,
satisfies $r_2(j) = 4 \sum_{d \mid j} \chi_4(d)$, where $d$ runs over the positive divisors
of $j$.

Formalized by `SumSquares.representationNumber_two_jacobi_count`, a theorem declared in [MathlibExt/NumberTheory/JacobiTwoSquareCount.lean, line 275](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/JacobiTwoSquareCount.lean#L275). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html#representation-number-two-jacobi-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobi's two-square theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/jacobi-s-two-square-theorem)
