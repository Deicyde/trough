---
declaration: section
origin: cited
lean: MetaMathlibExt.bAryBinomialCoefficient, MetaMathlibExt.bAryBinomialCoefficient_eq_prod_getD, MetaMathlibExt.bAryBinomialCoefficient_generating_function, MetaMathlibExt.base_digits_binomial_generating_function, MetaMathlibExt.bAryBinomialCoefficient_eq_prod_div_pow, MetaMathlibExt.bAryBinomialCoefficient_symm, MetaMathlibExt.bAryBinomialCoefficient_pascal, MetaMathlibExt.baryBinomial_symmetry_and_pascal
statement: formalized
proof: formalized
---

# Base-b digitwise binomial and multinomial coefficients

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html).

## The $b$-ary binomial coefficient

Let $b \ge 2$ and let $n$ and $k$ be natural numbers
with base-$b$ digits $n_l$ and $k_l$, taken to be $0$ beyond the last digit (with $0$ having no
digits). The $b$-ary binomial coefficient of $n$ and $k$ is $\prod_{l=0}^{m-1} \binom{n_l}{k_l}$,
where $m$ is the larger of the numbers of base-$b$ digits of $n$ and of $k$.

Formalized by `MetaMathlibExt.bAryBinomialCoefficient`, a definition declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialCoefficient.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialCoefficient.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-binomial-coefficient).

## Digitwise product formula for the $b$-ary binomial coefficient

Let $b \ge 2$, let $n$
and $k$ be natural numbers with base-$b$ digits $n_i$ and $k_i$ (taken to be $0$ beyond the last
digit, and with $0$ having no digits), and let $L$ be at least the number of base-$b$ digits of
$n$ and at least the number of base-$b$ digits of $k$. Then the $b$-ary binomial coefficient of
$n$ and $k$ equals $\prod_{i=0}^{L-1} \binom{n_i}{k_i}$.

Formalized by `MetaMathlibExt.bAryBinomialCoefficient_eq_prod_getD`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialCoefficient.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialCoefficient.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-binomial-coefficient-eq-prod-get-d).

## Generating function of the $b$-ary binomial coefficients

Let $R$ be a commutative semiring,
let $x \in R$, let $b \ge 2$, and write $\binom{n}{k}_b$ for the $b$-ary binomial coefficient of
natural numbers $n$ and $k$. Let $n$ have base-$b$ digits $n_0, \dots, n_{m-1}$, where $m$ is
the number of base-$b$ digits of $n$ ($m = 0$ for $n = 0$). Then

$$
\sum_{k=0}^{n} \binom{n}{k}_b x^k = \prod_{l=0}^{m-1} \left(1 + x^{b^l}\right)^{n_l}.
$$

## Sources

- Lin Jiu and Christophe Vignat, "On Binomial Identities in Arbitrary Bases," Journal of Integer Sequences 19 (2016), Article 16.5.5, Theorem (equation eq:barybinomialgeneratingfunction), lines 322–329, https://cs.uwaterloo.ca/journals/JIS/VOL19/Jiu/jiu4.tex

Formalized by `MetaMathlibExt.bAryBinomialCoefficient_generating_function`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialGeneratingFunction.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialGeneratingFunction.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-binomial-coefficient-generating-fu).

## Generating function of digitwise binomial products

Let $R$ be a commutative ring, let
$x \in R$, let $b \ge 2$, and let $n$ have base-$b$ digits $n_0, \dots, n_{m-1}$, where $m$ is
the number of base-$b$ digits of $n$ ($m = 0$ for $n = 0$). For each natural number $k$ let
$k_l$ be its $l$-th base-$b$ digit, taken to be $0$ beyond the last digit. Then

$$
\sum_{k=0}^{n} \Bigl(\prod_{l=0}^{m-1} \binom{n_l}{k_l}\Bigr) x^k
= \prod_{l=0}^{m-1} \left(1 + x^{b^l}\right)^{n_l}.
$$

The product $\prod_{l=0}^{m-1} \binom{n_l}{k_l}$ is the $b$-ary binomial coefficient of $n$
and $k$ whenever $k \le n$.

## Sources

- Lin Jiu and Christophe Vignat, "On Binomial Identities in Arbitrary Bases," Journal of Integer Sequences 19 (2016), Article 16.5.5, Theorem (equation eq:barybinomialgeneratingfunction), lines 322–329, https://cs.uwaterloo.ca/journals/JIS/VOL19/Jiu/jiu4.tex

Formalized by `MetaMathlibExt.base_digits_binomial_generating_function`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialGeneratingFunction.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialGeneratingFunction.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#base-digits-binomial-generating-function).

## Digit-product formula for $b$-ary binomial coefficients

Let $b \ge 2$ and let $n$, $k$
and $L$ be natural numbers with $n < b^L$ and $k < b^L$. Then the $b$-ary binomial coefficient
$\binom{n}{k}_b$ equals

$$\prod_{i=0}^{L-1} \binom{\lfloor n / b^i \rfloor \bmod b}{\lfloor k / b^i \rfloor \bmod b},$$

the product over the positions $i < L$ of the binomial coefficients of the $i$-th base-$b$ digits
of $n$ and $k$.

Formalized by `MetaMathlibExt.bAryBinomialCoefficient_eq_prod_div_pow`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-binomial-coefficient-eq-prod-div-p).

## Symmetry of $b$-ary binomial coefficients

Let $b \ge 2$ and write $\binom{n}{k}_b$ for
the $b$-ary binomial coefficient. For all natural numbers $k \le n$,
$\binom{n}{k}_b = \binom{n}{n-k}_b$.

Formalized by `MetaMathlibExt.bAryBinomialCoefficient_symm`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-binomial-coefficient-symm).

## Pascal's recurrence for $b$-ary binomial coefficients

Let $b \ge 2$ and write
$\binom{n}{k}_b$ for the $b$-ary binomial coefficient. For all natural numbers $n$ and $k$ with
$0 < k \le n$ and $\binom{n}{k}_b \ne 0$,
$\binom{n}{k}_b = \binom{n-1}{k-1}_b + \binom{n-1}{k}_b$.

Formalized by `MetaMathlibExt.bAryBinomialCoefficient_pascal`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean, line 292](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean#L292). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-binomial-coefficient-pascal).

## Symmetry and Pascal's recurrence for $b$-ary binomial coefficients

Let $b \ge 2$. For a
natural number $m$ write $m_i = \lfloor m / b^i \rfloor \bmod b$ for its $i$-th base-$b$ digit.
For integers $m$ and $j$, let $C_b(m, j) = \prod_{i=0}^{m+j} \binom{m_i}{j_i}$ if $m \ge 0$ and
$j \ge 0$, and $C_b(m, j) = 0$ otherwise. Then for all integers $n$ and $k$ with $0 < n$ and
$0 \le k \le n$, we have $C_b(n, k) = C_b(n, n - k)$, and if $C_b(n, k) \ne 0$ then
$C_b(n, k) = C_b(n - 1, k - 1) + C_b(n - 1, k)$.

## Sources

- Lin Jiu and Christophe Vignat, "On Binomial Identities in Arbitrary Bases," Journal of Integer Sequences 19 (2016), Article 16.5.5, Theorem (Symmetry and recurrence), equation, lines 432–445, https://cs.uwaterloo.ca/journals/JIS/VOL19/Jiu/jiu4.tex

Formalized by `MetaMathlibExt.baryBinomial_symmetry_and_pascal`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean, line 315](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryBinomialSymmetryPascal.lean#L315). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#bary-binomial-symmetry-and-pascal).

## Chu–Vandermonde identity for $b$-ary binomial coefficients

Let $b \ge 2$ and write
$\binom{n}{k}_b$ for the $b$-ary binomial coefficient. Let $m$ and $n$ be natural numbers that
add without carries in base $b$, that is,
$\lfloor m / b^l \rfloor \bmod b + \lfloor n / b^l \rfloor \bmod b < b$ for every natural number
$l$. Then for every natural number $r$,

$$\binom{m+n}{r}_b = \sum_{k=0}^{r} \binom{m}{k}_b \binom{n}{r-k}_b.$$

Formalized by `MetaMathlibExt.bAryBinomialCoefficient_chu_vandermonde`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryChuVandermonde.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryChuVandermonde.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-binomial-coefficient-chu-vandermon).

## $b$-ary Chu–Vandermonde identity

Let $b \ge 2$. For a natural number $x$ write
$x_l = \lfloor x / b^l \rfloor \bmod b$ for its $l$-th base-$b$ digit, and for natural numbers
$x$ and $y$ let $C(x, y) = \prod_{l=0}^{x+y} \binom{x_l}{y_l}$. Let $m$, $n$ and $r$ be natural
numbers such that the addition of $m$ and $n$ in base $b$ has no carries, that is,
$m_l + n_l < b$ for every $l \le m + n$. Then

$$C(m + n, r) = \sum_{k=0}^{r} C(m, k)\, C(n, r - k).$$

The product $C(x, y)$ is the $b$-ary binomial coefficient $\binom{x}{y}_b$.

## Sources

- Lin Jiu and Christophe Vignat, "On Binomial Identities in Arbitrary Bases," Journal of Integer Sequences 19 (2016), Article 16.5.5, Theorem (equation bChuVandermonde), lines 371–377, https://cs.uwaterloo.ca/journals/JIS/VOL19/Jiu/jiu4.tex

Formalized by `MetaMathlibExt.bary_chu_vandermonde`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BAryChuVandermonde.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/BAryChuVandermonde.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#bary-chu-vandermonde).

## Base-$b$ digit of a natural number

For natural numbers $b$, $n$ and $l$, the rank-$l$
base-$b$ digit $n_l$ of $n$ is the entry at position $l$ (counting from $0$) of the list of
base-$b$ digits of $n$, least significant digit first, and $0$ when $l$ is at least the length of
that list (with $0$ having no digits). For $b \ge 2$ this is the coefficient of $b^l$ in the
base-$b$ expansion of $n$.

For $b \le 1$ the digit list follows Mathlib's convention: for $b = 0$ a positive $n$ has the
single digit $n$, and for $b = 1$ the digits of $n$ are $n$ ones.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL19/Jiu/jiu3.tex, lines 349-359.

Formalized by `MetaMathlibExt.bAryDigit`, a definition declared in [MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-digit).

## Rank-$l$ base-$b$ digits of a list

For natural numbers $b$ and $l$ and a list
$(k_1, \dots, k_m)$ of natural numbers, this is the list $((k_1)_l, \dots, (k_m)_l)$, where
$(k_i)_l$ is the rank-$l$ base-$b$ digit of $k_i$.

Formalized by `MetaMathlibExt.bAryLowerDigits`, a definition declared in [MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-lower-digits).

## Multinomial coefficient with a prescribed top

For a natural number $t$ and a list
$(a_1, \dots, a_m)$ of natural numbers, the multinomial factor of $t$ over $(a_1, \dots, a_m)$ is
$\frac{t!}{a_1! \cdots a_m!}$ if $a_1 + \dots + a_m = t$, and $0$ otherwise.

Formalized by `MetaMathlibExt.ordinaryMultinomialFactor`, a definition declared in [MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#ordinary-multinomial-factor).

## Digitwise $b$-ary multinomial factor

For natural numbers $b$, $n$ and $l$ and a list
$(k_1, \dots, k_m)$ of natural numbers, let $n_l$ and $(k_i)_l$ be the rank-$l$ base-$b$ digits
of $n$ and $k_i$. The factor at rank $l$ is $\frac{n_l!}{(k_1)_l! \cdots (k_m)_l!}$ if
$(k_1)_l + \dots + (k_m)_l = n_l$, and $0$ otherwise.

Formalized by `MetaMathlibExt.bAryMultinomialFactor`, a definition declared in [MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-multinomial-factor).

## Digit-length bound for the $b$-ary multinomial coefficient

For natural numbers $b$ and
$n$ and a list $(k_1, \dots, k_m)$ of natural numbers, the bound is the largest of the numbers of
base-$b$ digits of $n, k_1, \dots, k_m$ (with $0$ having no digits).

Every nonzero base-$b$ digit of $n$ and of each $k_i$ has rank below the bound, so at every higher
rank the digitwise $b$-ary multinomial factor equals $1$; this plays the role of the source's
sufficiently large $N$.

Formalized by `MetaMathlibExt.bAryMultinomialBound`, a definition declared in [MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-multinomial-bound).

## The $b$-ary multinomial coefficient

Let $b \ge 2$, let $n$ be a natural number and let
$(k_1, \dots, k_m)$ be a list of natural numbers, and write $n_l$ and $(k_i)_l$ for the rank-$l$
base-$b$ digits of $n$ and $k_i$ (taken to be $0$ beyond the last digit, with $0$ having no
digits). Let $N$ be the largest of the numbers of base-$b$ digits of $n, k_1, \dots, k_m$. The
$b$-ary multinomial coefficient of $n$ over $(k_1, \dots, k_m)$ is $\prod_{l=0}^{N-1} c_l$, where
$c_l = \frac{n_l!}{(k_1)_l! \cdots (k_m)_l!}$ if $(k_1)_l + \dots + (k_m)_l = n_l$ and $c_l = 0$
otherwise.

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL19/Jiu/jiu3.tex, lines 349-359.

Formalized by `MetaMathlibExt.bAryMultinomial`, a definition declared in [MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/BAryMultinomialCoefficient.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html#b-ary-multinomial).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Base-b digitwise binomial and multinomial coefficients](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/generalized-binomial-coefficients/base-b-digitwise-binomial-and-multinomial-coeffi)
