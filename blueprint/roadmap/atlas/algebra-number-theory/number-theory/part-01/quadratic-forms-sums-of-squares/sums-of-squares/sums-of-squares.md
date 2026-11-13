---
declaration: section
origin: cited
lean: MetaMathlibExt.landau_ramanujan_asymptotic, MetaMathlibExt.nat_eq_sq_sub_sq_iff_not_eq_four_mul_add_two, MetaMathlibExt.SumTwoCoprimeSquares.sum_two_coprime_squares_characterization
statement: formalized
proof: formalized
---

# Sums of squares and representation numbers: its own results

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/index.html).

Two-, three- and four-square theorems, Jacobi-type counts, Gaussian and Hurwitz integer methods, x²+2y² and similar representations.

## Landau–Ramanujan theorem

For real $x$, let $B(x)$ be the number of natural numbers
$m \le x$, including $m = 0$, that can be written as $m = a^2 + b^2$ with natural numbers $a$
and $b$. Then there is a constant $c_0 > 0$ such that $B(x)$ is asymptotically equivalent to
$c_0 x / \sqrt{\log x}$ as $x \to \infty$.

This only asserts the existence of some positive constant $c_0$; it does not identify $c_0$
with the Landau–Ramanujan constant (the Euler product over the primes $p \equiv 3 \pmod 4$ in
the cited result). That identification is an intentional omission relative to the source.

## Sources

- Labib Haddad and Charles Helou, "Representation of Integers by Near Quadratic Sequences," Journal of Integer Sequences 15 (2012), <https://cs.uwaterloo.ca/journals/JIS/VOL15/Helou/helou3.tex>, lines 483–486. Proof-method source (distinct from the statement source above): the proof adapts Wirsing's mean-value method as presented in Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Chapter III.4.

Formalized by `MetaMathlibExt.landau_ramanujan_asymptotic`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/LandauRamanujan.lean, line 3376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/LandauRamanujan.lean#L3376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/index.html#landau-ramanujan-asymptotic).

## Positive integers that are differences of two squares

A positive natural number $n$ can be
written as $n = a^2 - b^2$ with natural numbers $a$ and $b$ if and only if there is no natural
number $k$ with $n = 4k + 2$.

## Sources

- Arias, Borja, and Rubio cite D. M. Burton, "Elementary Number Theory," 7th edition, Theorem 13.4; truncated subtraction is exact on the witnesses.
- Fabián Arias, Jerson Borja, and Luis Rubio, "Counting Integers Representable as Images of Polynomials Modulo n," Journal of Integer Sequences 22 (2019), Article 19.6.7, Theorem, lines 821–823, https://cs.uwaterloo.ca/journals/JIS/VOL22/Borja/borja3.tex

Formalized by `MetaMathlibExt.nat_eq_sq_sub_sq_iff_not_eq_four_mul_add_two`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/DifferenceOfTwoSquares.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/DifferenceOfTwoSquares.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/index.html#nat-eq-sq-sub-sq-iff-not-eq-four-mul-add).

## Sums of two coprime squares

Let $d > 2$ be a natural number. Then $d = a^2 + b^2$ for
some coprime positive natural numbers $a$ and $b$ if and only if there is a natural number $q$,
all of whose prime factors are congruent to $1$ modulo $4$, such that $d = q$ or $d = 2q$.

## Sources

- Nguyen Viet Dung and Luu Ba Thang, "The Number a²+b²−dc² Revisited", Journal of Integer Sequences 24 (2021), Article 21.9.3, theorem lines 105–107, https://cs.uwaterloo.ca/journals/JIS/VOL24/Thang/thang41.tex.

Formalized by `MetaMathlibExt.SumTwoCoprimeSquares.sum_two_coprime_squares_characterization`, a theorem declared in [MathlibExt/NumberTheory/QuadraticForms/SumTwoCoprimeSquares.lean, line 391](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/QuadraticForms/SumTwoCoprimeSquares.lean#L391). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/index.html#sum-two-coprime-squares-characterization).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sums of squares and representation numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/quadratic-forms-sums-of-squares/sums-of-squares)
