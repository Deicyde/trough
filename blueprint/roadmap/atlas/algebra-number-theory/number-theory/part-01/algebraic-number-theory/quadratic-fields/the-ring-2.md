---
declaration: section
origin: cited
lean: Zsqrtd.NegTwo.norm_nonneg', Zsqrtd.NegTwo.norm_eq_zero', Zsqrtd.NegTwo.norm_pos', Zsqrtd.NegTwo.abs_natCast_norm', Zsqrtd.NegTwo.div_def', Zsqrtd.NegTwo.mod_def', Zsqrtd.NegTwo.round_error, Zsqrtd.NegTwo.norm_key
statement: formalized
proof: formalized
---

# The ring ℤ\[√−2\]

24 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html).

## The norm on $\mathbb{Z}(\sqrt{-2})$ is nonnegative

For every $x = a + b\sqrt{-2}$ in
$\mathbb{Z}[\sqrt{-2}]$, the norm $N(x) = a^2 + 2b^2$ satisfies $N(x) \ge 0$.

Formalized by `Zsqrtd.NegTwo.norm_nonneg'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#norm-nonneg).

## The norm on $\mathbb{Z}(\sqrt{-2})$ vanishes only at zero

For $x = a + b\sqrt{-2}$ in
$\mathbb{Z}[\sqrt{-2}]$ with norm $N(x) = a^2 + 2b^2$, we have $N(x) = 0$ if and only if
$x = 0$.

Formalized by `Zsqrtd.NegTwo.norm_eq_zero'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#norm-eq-zero).

## Nonzero elements of $\mathbb{Z}(\sqrt{-2})$ have positive norm

For $x = a + b\sqrt{-2}$
in $\mathbb{Z}[\sqrt{-2}]$ with norm $N(x) = a^2 + 2b^2$, we have $N(x) > 0$ if and only if
$x \ne 0$.

Formalized by `Zsqrtd.NegTwo.norm_pos'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#norm-pos).

## The norm on $\mathbb{Z}(\sqrt{-2})$ equals its absolute value

For every
$x = a + b\sqrt{-2}$ in $\mathbb{Z}[\sqrt{-2}]$, the norm $N(x) = a^2 + 2b^2$ satisfies
$|N(x)| = N(x)$, where $|N(x)|$ is taken as a natural number and read back as an integer.

Formalized by `Zsqrtd.NegTwo.abs_natCast_norm'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#abs-nat-cast-norm).

## Rounding division on $\mathbb{Z}(\sqrt{-2})$

Let $x, y \in \mathbb{Z}[\sqrt{-2}]$ with
$y = c + d\sqrt{-2}$, let $\bar{y} = c - d\sqrt{-2}$ be its conjugate and $N(y) = c^2 + 2d^2$ its
norm, and write $x\bar{y} = u + v\sqrt{-2}$ with $u, v \in \mathbb{Z}$. The quotient is $x / y = \operatorname{round}(u / N(y)) +
\operatorname{round}(v / N(y))\sqrt{-2}$, where $u / N(y)$ and $v / N(y)$ are computed in
$\mathbb{Q}$ (division by $0$ gives $0$) and $\operatorname{round}$ sends a rational number to
the nearest integer, rounding halves up.

Formalized by `Zsqrtd.NegTwo.div_def'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#div-def).

## Remainder of the rounding division on $\mathbb{Z}(\sqrt{-2})$

For all $x, y$ in
$\mathbb{Z}[\sqrt{-2}]$, the remainder is $x \bmod y = x - y\,(x / y)$,
where $x / y$ is the rounding division of $\mathbb{Z}[\sqrt{-2}]$.

Formalized by `Zsqrtd.NegTwo.mod_def'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#mod-def).

## Error of rounded integer division

Let $a$ and $N$ be integers with $N > 0$, and let
$q$ be the integer nearest to the rational number $a/N$ (halves rounded up). Then
$|2(a - qN)| \le N$, that is, $a$ differs from $qN$ by at most $N/2$.

Formalized by `Zsqrtd.NegTwo.round_error`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#round-error).

## Norm identity for the remainder

Let $x, y, q \in \mathbb{Z}[\sqrt{-2}]$, write
$N(a + b\sqrt{-2}) = a^2 + 2b^2$ for the norm and $\bar{y}$ for the conjugate of $y$, and write
$x\bar{y} = u + v\sqrt{-2}$ and $q = e + f\sqrt{-2}$ with $u, v, e, f \in \mathbb{Z}$. Then
$N(y)\,N(x - yq) = (u - N(y)\,e)^2 + 2\,(v - N(y)\,f)^2$.

Formalized by `Zsqrtd.NegTwo.norm_key`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#norm-key).

## The remainder is smaller than the divisor in $\mathbb{Z}(\sqrt{-2})$

Let $x, y$ be
elements of $\mathbb{Z}[\sqrt{-2}]$ with $y \ne 0$, and let $N(a + b\sqrt{-2}) = a^2 + 2b^2$ be
the norm. The remainder $x \bmod y = x - y\,(x / y)$ of the rounding division of
$\mathbb{Z}[\sqrt{-2}]$ satisfies $N(x \bmod y) < N(y)$.

Formalized by `Zsqrtd.NegTwo.norm_mod_lt'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#norm-mod-lt).

## The remainder is smaller than the divisor, in absolute norm

Let $x, y$ be elements of
$\mathbb{Z}[\sqrt{-2}]$ with $y \ne 0$, and let $N(a + b\sqrt{-2}) = a^2 + 2b^2$ be the norm.
The remainder $x \bmod y = x - y\,(x / y)$ of the rounding division of $\mathbb{Z}[\sqrt{-2}]$
satisfies $|N(x \bmod y)| < |N(y)|$ as natural numbers.

Formalized by `Zsqrtd.NegTwo.natAbs_norm_mod_lt'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#nat-abs-norm-mod-lt).

## Multiplying by a nonzero element does not decrease the norm in $\mathbb{Z}(\sqrt{-2})$

Let $N(a + b\sqrt{-2}) = a^2 + 2b^2$ be the norm on $\mathbb{Z}[\sqrt{-2}]$. For
$x, y \in \mathbb{Z}[\sqrt{-2}]$ with $y \ne 0$, we have $|N(x)| \le |N(xy)|$ as natural
numbers.

Formalized by `Zsqrtd.NegTwo.norm_le_norm_mul_left'`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoEuclidean.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#norm-le-norm-mul-left).

## Units of ℤ(√−2)

An element $x$ of $\mathbb{Z}[\sqrt{-2}]$ is a unit if and only if $x = 1$
or $x = -1$.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_isUnit_iff`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-is-unit-iff).

## Elements of ℤ(√−2) of prime norm are prime

For $\pi = a + b\sqrt{-2}$ in
$\mathbb{Z}[\sqrt{-2}]$ let $N(\pi) = a^2 + 2b^2$ be its norm. If $|N(\pi)|$ is a prime number, then
$\pi$ is a prime element of $\mathbb{Z}[\sqrt{-2}]$.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_prime_of_natAbs_norm_prime`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-prime-of-nat-abs-norm-pri).

## √−2 is prime in ℤ(√−2)

The element $\sqrt{-2}$ is a prime element of
$\mathbb{Z}[\sqrt{-2}]$.

Its norm is $2$, a prime number.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_prime_sqrtd`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-prime-sqrtd).

## $2$ is minus the square of $\sqrt{-2}$

In $\mathbb{Z}[\sqrt{-2}]$ one has
$2 = -(\sqrt{-2})^2$.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_two_eq`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-two-eq).

## x² + 2y² is never 5 or 7 modulo 8

For all $x, y \in \mathbb{Z}/8\mathbb{Z}$,
$x^2 + 2y^2 \ne 5$ and $x^2 + 2y^2 \ne 7$.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_mod8_obstruction`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-mod8-obstruction).

## Primes congruent to 5 or 7 mod 8 are inert in ℤ(√−2)

If $p$ is a prime number with
$p \equiv 5 \pmod 8$ or $p \equiv 7 \pmod 8$, then $p$ is a prime element of
$\mathbb{Z}[\sqrt{-2}]$.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_inert`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-inert).

## Primes $p \equiv 1, 3 \pmod 8$ are norms of primes of $\mathbb{Z}(\sqrt{-2})$

Let $p$ be a prime number with $p \equiv 1 \pmod 8$ or $p \equiv 3 \pmod 8$. Then there is a
prime element $\pi = a + b\sqrt{-2}$ of $\mathbb{Z}[\sqrt{-2}]$ whose norm $a^2 + 2b^2$ equals
$p$.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_split`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 167](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L167). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-split).

## Conjugate factorization of an odd prime in $\mathbb{Z}(\sqrt{-2})$

Let $p$ be an odd
prime number and let $\pi = a + b\sqrt{-2}$ be an element of $\mathbb{Z}[\sqrt{-2}]$ whose norm
$a^2 + 2b^2$ equals $p$. Write $\bar\pi = a - b\sqrt{-2}$ for the conjugate of $\pi$. Then
$p = \pi\bar\pi$, $\bar\pi$ is prime in $\mathbb{Z}[\sqrt{-2}]$, and $\bar\pi$ is not associated
to $\pi$.

Formalized by `Zsqrtd.NegTwo.zsqrtd_neg_two_split_conj`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#zsqrtd-neg-two-split-conj).

## Enumeration of the units of ℤ(√−2)

The map $\{0, 1\} \to \mathbb{Z}[\sqrt{-2}]$ sending
$0$ to $1$ and $1$ to $-1$, which lists the two units of $\mathbb{Z}[\sqrt{-2}]$.

Formalized by `Zsqrtd.NegTwo.unitVal`, a definition declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 334](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L334). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#unit-val).

## The enumeration of the units of ℤ(√−2) is injective

Let $\varepsilon_0 = 1$ and
$\varepsilon_1 = -1$ in $\mathbb{Z}[\sqrt{-2}]$. For $i, j \in \{0, 1\}$, if
$\varepsilon_i = \varepsilon_j$ then $i = j$.

Formalized by `Zsqrtd.NegTwo.unitVal_inj`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#unit-val-inj).

## Every unit of ℤ(√−2) is enumerated

Let $\varepsilon_0 = 1$ and $\varepsilon_1 = -1$ be the
enumeration of the units of $\mathbb{Z}[\sqrt{-2}]$. Every unit $u$ of $\mathbb{Z}[\sqrt{-2}]$
equals $\varepsilon_i$ for some $i \in \{0, 1\}$.

Formalized by `Zsqrtd.NegTwo.unitVal_complete`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#unit-val-complete).

## Inverses of the enumerated units of ℤ(√−2)

The map $\{0, 1\} \to \mathbb{Z}[\sqrt{-2}]$
sending $0$ to $1$ and $1$ to $-1$. Since $1$ and $-1$ are their own inverses, its value at $i$ is
the inverse of the $i$-th enumerated unit.

Formalized by `Zsqrtd.NegTwo.unitValInv`, a definition declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 350](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L350). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#unit-val-inv).

## Each enumerated unit of ℤ(√−2) times its listed inverse is one

Let $\varepsilon_0 = 1$,
$\varepsilon_1 = -1$ be the enumerated units of $\mathbb{Z}[\sqrt{-2}]$ and $\eta_0 = 1$,
$\eta_1 = -1$ their listed inverses. Then $\varepsilon_i \eta_i = 1$ for each $i \in \{0, 1\}$.

Formalized by `Zsqrtd.NegTwo.unitVal_mul_unitValInv`, a theorem declared in [MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean, line 354](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/ZsqrtdNegTwoPrimes.lean#L354). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html#unit-val-mul-unit-val-inv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The ring ℤ\[√−2\]](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/quadratic-fields/the-ring-2)
