---
declaration: section
origin: cited
lean: SumSquares.chiNeg2_one, SumSquares.divChiNeg2Sum, SumSquares.divChiNeg2Sum_mul_of_coprime, SumSquares.divChiNeg2Sum_one, SumSquares.divChiNeg2Sum_prime_pow_two, SumSquares.divChiNeg2Sum_prime_pow_split, SumSquares.divChiNeg2Sum_prime_pow_inert, SumSquares.repX2Y2Count
statement: formalized
proof: formalized
---

# Representations by x² + 2y²

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html).

## The character $\chi_{-2}$ takes the value $1$ at $1$

Let $\chi_{-2}$ be the quadratic
character modulo $8$ with values in $\mathbb{Z}$ (the character of $\mathbb{Q}(\sqrt{-2})$):
$\chi_{-2}(n) = 1$ for $n \equiv 1, 3 \pmod 8$, $\chi_{-2}(n) = -1$ for $n \equiv 5, 7 \pmod 8$,
and $\chi_{-2}(n) = 0$ for even $n$. Then $\chi_{-2}(1) = 1$.

Formalized by `SumSquares.chiNeg2_one`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#chi-neg2-one).

## Divisor sum of the character $\chi_{-2}$

Let $\chi_{-2}$ be the quadratic character
modulo $8$ with values in $\mathbb{Z}$ (the character of $\mathbb{Q}(\sqrt{-2})$):
$\chi_{-2}(n) = 1$ for $n \equiv 1, 3 \pmod 8$, $\chi_{-2}(n) = -1$ for $n \equiv 5, 7 \pmod 8$,
and $\chi_{-2}(n) = 0$ for even $n$. For a natural number $t$, the divisor sum of $\chi_{-2}$ at
$t$ is the integer $\sum_{d \mid t} \chi_{-2}(d)$, the sum over the positive divisors $d$ of $t$.
By convention $0$ has no divisors here, so the divisor sum at $t = 0$ is $0$.

Formalized by `SumSquares.divChiNeg2Sum`, a definition declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#div-chi-neg2-sum).

## Multiplicativity of the divisor sum of $\chi_{-2}$

Let $\chi_{-2}$ be the quadratic
character modulo $8$ with $\chi_{-2}(n) = 1$ for $n \equiv 1, 3 \pmod 8$, $\chi_{-2}(n) = -1$ for
$n \equiv 5, 7 \pmod 8$ and $\chi_{-2}(n) = 0$ for even $n$. For a natural number $t$, let
$S(t) = \sum_{d \mid t} \chi_{-2}(d)$, the sum over the positive divisors $d$ of $t$, with
$S(0) = 0$ (the empty sum). For coprime natural numbers $m$ and $n$, $S(mn) = S(m)\,S(n)$.

The proof uses that $\chi_{-2}$ is completely multiplicative.

Formalized by `SumSquares.divChiNeg2Sum_mul_of_coprime`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#div-chi-neg2-sum-mul-of-coprime).

## The divisor sum of $\chi_{-2}$ at $1$

Let $\chi_{-2}$ be the quadratic character modulo
$8$ with $\chi_{-2}(n) = 1$ for $n \equiv 1, 3 \pmod 8$, $\chi_{-2}(n) = -1$ for
$n \equiv 5, 7 \pmod 8$ and $\chi_{-2}(n) = 0$ for even $n$. For a positive integer $t$, let
$S(t) = \sum_{d \mid t} \chi_{-2}(d)$, the sum over the positive divisors $d$ of $t$.
Then $S(1) = 1$.

Formalized by `SumSquares.divChiNeg2Sum_one`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#div-chi-neg2-sum-one).

## The divisor sum of $\chi_{-2}$ at powers of $2$

Let $\chi_{-2}$ be the quadratic
character modulo $8$ with $\chi_{-2}(n) = 1$ for $n \equiv 1, 3 \pmod 8$, $\chi_{-2}(n) = -1$ for
$n \equiv 5, 7 \pmod 8$ and $\chi_{-2}(n) = 0$ for even $n$. For a positive integer $t$, let
$S(t) = \sum_{d \mid t} \chi_{-2}(d)$, the sum over the positive divisors $d$ of $t$. For every
natural number $e$, $S(2^e) = 1$: only the divisor $1$ contributes.

Formalized by `SumSquares.divChiNeg2Sum_prime_pow_two`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#div-chi-neg2-sum-prime-pow-two).

## The divisor sum of $\chi_{-2}$ at powers of a prime $p \equiv 1, 3 \pmod 8$

Let
$\chi_{-2}$ be the quadratic character modulo $8$ with $\chi_{-2}(n) = 1$ for
$n \equiv 1, 3 \pmod 8$, $\chi_{-2}(n) = -1$ for $n \equiv 5, 7 \pmod 8$ and $\chi_{-2}(n) = 0$
for even $n$. For a positive integer $t$, let $S(t) = \sum_{d \mid t} \chi_{-2}(d)$, the sum over
the positive divisors $d$ of $t$. If $p$ is a prime with $p \equiv 1 \pmod 8$ or
$p \equiv 3 \pmod 8$, then $S(p^e) = e + 1$ for every natural number $e$: every divisor of
$p^e$ contributes $1$.

Formalized by `SumSquares.divChiNeg2Sum_prime_pow_split`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#div-chi-neg2-sum-prime-pow-split).

## The divisor sum of $\chi_{-2}$ at powers of a prime $q \equiv 5, 7 \pmod 8$

Let
$\chi_{-2}$ be the quadratic character modulo $8$ with $\chi_{-2}(n) = 1$ for
$n \equiv 1, 3 \pmod 8$, $\chi_{-2}(n) = -1$ for $n \equiv 5, 7 \pmod 8$ and $\chi_{-2}(n) = 0$
for even $n$. For a positive integer $t$, let $S(t) = \sum_{d \mid t} \chi_{-2}(d)$, the sum over
the positive divisors $d$ of $t$. If $q$ is a prime with $q \equiv 5 \pmod 8$ or
$q \equiv 7 \pmod 8$, then for every natural number $f$, $S(q^f) = 1$ if $f$ is even and
$S(q^f) = 0$ if $f$ is odd.

Formalized by `SumSquares.divChiNeg2Sum_prime_pow_inert`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#div-chi-neg2-sum-prime-pow-inert).

## Number of elements of $\mathbb{Z}(\sqrt{-2})$ of a given norm

For a natural number $t$,
the representation count of $t$ is the number of elements $z = a + b\sqrt{-2}$ of
$\mathbb{Z}[\sqrt{-2}]$, with $a, b$ integers, whose norm $N(z) = a^2 + 2b^2$ has absolute
value $t$. Since the norm is never negative, this is the number of elements of norm $t$.

Formalized by `SumSquares.repX2Y2Count`, a definition declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#rep-x2-y2-count).

## Elements of norm one in $\mathbb{Z}(\sqrt{-2})$

Exactly two elements $a + b\sqrt{-2}$ of
$\mathbb{Z}[\sqrt{-2}]$, with $a, b$ integers, have norm $a^2 + 2b^2 = 1$.

These are the units $\pm 1$.

Formalized by `SumSquares.repX2Y2Count_one`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#rep-x2-y2-count-one).

## Elements of $\mathbb{Z}(\sqrt{-2})$ whose norm is a power of $2$

For every natural
number $e$, exactly two elements $a + b\sqrt{-2}$ of $\mathbb{Z}[\sqrt{-2}]$, with $a, b$ integers,
have norm $a^2 + 2b^2 = 2^e$.

The prime $2$ is ramified in $\mathbb{Z}[\sqrt{-2}]$.

Formalized by `SumSquares.repX2Y2Count_two_pow`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 246](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L246). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#rep-x2-y2-count-two-pow).

## Elements of $\mathbb{Z}(\sqrt{-2})$ whose norm is a power of an inert prime

Let $q$ be a
prime with $q \equiv 5$ or $q \equiv 7 \pmod 8$, and let $f$ be a natural number. The number of
elements $a + b\sqrt{-2}$ of $\mathbb{Z}[\sqrt{-2}]$, with $a, b$ integers, of norm
$a^2 + 2b^2 = q^f$ is $2$ if $f$ is even and $0$ if $f$ is odd.

Formalized by `SumSquares.repX2Y2Count_inert_pow`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#rep-x2-y2-count-inert-pow).

## Elements of $\mathbb{Z}(\sqrt{-2})$ whose norm is a power of a split prime

Write
$N(a + b\sqrt{-2}) = a^2 + 2b^2$ for the norm of an element of $\mathbb{Z}[\sqrt{-2}]$, where
$a, b$ are integers. Let $p$ be a prime with $p \equiv 1$ or $p \equiv 3 \pmod 8$, and suppose
$\pi$ is a prime element of $\mathbb{Z}[\sqrt{-2}]$ with $N(\pi) = p$. Then for every natural
number $e$, the number of elements of $\mathbb{Z}[\sqrt{-2}]$ of norm $p^e$ is $2(e + 1)$.

Formalized by `SumSquares.repX2Y2Count_split_pow`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#rep-x2-y2-count-split-pow).

## Elements of $\mathbb{Z}(\sqrt{-2})$ of norm $t$ counted by a divisor sum

For every
positive integer $t$, the number of elements $a + b\sqrt{-2}$ of $\mathbb{Z}[\sqrt{-2}]$, with
$a, b$ integers, of norm $a^2 + 2b^2 = t$ equals $2 \sum_{d \mid t} \chi(d)$, where $d$ runs over
the positive divisors of $t$ and $\chi$ is the character modulo $8$ given by $\chi(d) = 1$ if
$d \equiv 1, 3 \pmod 8$, $\chi(d) = -1$ if $d \equiv 5, 7 \pmod 8$, and $\chi(d) = 0$ if $d$ is
even.

Equivalently, this counts the integer pairs $(x, y)$ with $x^2 + 2y^2 = t$.

Formalized by `SumSquares.x2y2_count`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 297](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L297). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#x2y2-count).

## Coordinates of an element of norm $N$ in $\mathbb{Z}(\sqrt{-2})$

Let $N$ be a natural
number and let $z = a + b\sqrt{-2}$, with $a, b \in \mathbb{Z}$, be an element of
$\mathbb{Z}[\sqrt{-2}]$ whose norm has absolute value $N$. Then $a^2 + 2b^2 = N$.

Formalized by `SumSquares.re_mul_re_add_two_mul_im_mul_im`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#re-mul-re-add-two-mul-im-mul-im).

## Counting representations by $x^2 + 2y^2$ through positive solutions

Let $N$ be a natural
number such that every element $a + b\sqrt{-2}$ of $\mathbb{Z}[\sqrt{-2}]$ of norm $a^2 + 2b^2 = N$
has $a \neq 0$ and $b \neq 0$. Then the number of elements of $\mathbb{Z}[\sqrt{-2}]$ of norm $N$ is
four times the number of pairs $(x, y)$ of positive integers with $x^2 + 2y^2 = N$.

Formalized by `SumSquares.repX2Y2Count_eq_four_mul_pos`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 384](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L384). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#rep-x2-y2-count-eq-four-mul-pos).

## Doubling an odd argument leaves the divisor sum of $\chi_{-2}$ unchanged

Let $\chi_{-2}$
be the quadratic character modulo $8$ with $\chi_{-2}(n) = 1$ for $n \equiv 1, 3 \pmod 8$,
$\chi_{-2}(n) = -1$ for $n \equiv 5, 7 \pmod 8$ and $\chi_{-2}(n) = 0$ for even $n$. For a
positive integer $t$, let $S(t) = \sum_{d \mid t} \chi_{-2}(d)$, the sum over the positive
divisors $d$ of $t$. For every odd natural number $m$, $S(2m) = S(m)$.

Formalized by `SumSquares.divChiNeg2Sum_two_mul_of_odd`, a theorem declared in [MathlibExt/NumberTheory/X2Y2Count.lean, line 507](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/X2Y2Count.lean#L507). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#div-chi-neg2-sum-two-mul-of-odd).

## Representations by $x^2 + 2y^2$ as elements of $\mathbb{Z}(\sqrt{-2})$

For every natural
number $j$, the map $(x, y) \mapsto x + y\sqrt{-2}$ is a bijection from the set of integer pairs
$(x, y)$ with $x^2 + 2y^2 = j$ to the set of elements $z \in \mathbb{Z}[\sqrt{-2}]$ whose norm
$N(z)$ has absolute value $j$.

Formalized by `SumSquares.pairEquivSqrtNegTwoNormFiber`, a definition declared in [MathlibExt/NumberTheory/QuadraticForms/SqrtNeg2Count.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/SqrtNeg2Count.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#pair-equiv-sqrt-neg-two-norm-fiber).

## Number of representations by $x^2 + 2y^2$

For every integer $j \ge 1$, the number of
pairs of integers $(x, y)$ with $x^2 + 2y^2 = j$ equals $2 \sum_{d \mid j} \chi(d)$, where $d$
runs over the positive divisors of $j$ and $\chi$ is the Dirichlet character modulo $8$ attached
to $\mathbb{Q}(\sqrt{-2})$: $\chi(d) = 1$ if $d \equiv 1, 3 \pmod 8$, $\chi(d) = -1$ if
$d \equiv 5, 7 \pmod 8$, and $\chi(d) = 0$ if $d$ is even.

Formalized by `SumSquares.x2_add_two_sq_count`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/SqrtNeg2Count.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/SqrtNeg2Count.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html#x2-add-two-sq-count).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representations by x² + 2y²](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/representations-by-x-2y)
