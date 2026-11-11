---
declaration: section
origin: cited
lean: MetaMathlibExt.digitCount, MetaMathlibExt.integerLength, MetaMathlibExt.irwinSum, MetaMathlibExt.stringValue, MetaMathlibExt.normalizedStringValue, MetaMathlibExt.stringWeight, MetaMathlibExt.stringAtom, MetaMathlibExt.irwinMeasure
statement: formalized
---

# Irwin series

38 results, 22 proved and 16 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html).

## Digit count

For natural numbers $b$, $d$ and $n$, the digit count of $d$ in $n$ is the
number of occurrences of the digit $d$ in the minimal base-$b$ representation of $n$ (its base-$b$
digits without leading zeros). The representation of $0$ is empty, so $0$ has digit count $0$.

For the degenerate bases, the representation of $n \ne 0$ is the single digit $n$ when $b = 0$
and a string of $n$ ones when $b = 1$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Notation and Terminology.

Formalized by `MetaMathlibExt.digitCount`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#digit-count).

## Integer length

For natural numbers $b$ and $n$, the integer length of $n$ in base $b$ is
the number of digits in the minimal base-$b$ representation of $n$ (its base-$b$ digits without
leading zeros); in particular $0$ has length $0$.

For the degenerate bases, the representation of $n \ne 0$ is the single digit $n$ when $b = 0$
and a string of $n$ ones when $b = 1$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Notation and Terminology.

Formalized by `MetaMathlibExt.integerLength`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#integer-length).

## Irwin sum

For natural numbers $b$, $d$ and $k$, the Irwin sum $H^{(k)}_{b,d}$ is the sum
of $1/n$ over the positive integers $n$ whose base-$b$ expansion contains exactly $k$ occurrences
of the digit $d$. It is taken as an unconditional sum of real numbers, with the value $0$ if this
family is not summable; positivity and convergence are results, not part of the definition.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Notation and Terminology.

Formalized by `MetaMathlibExt.irwinSum`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-sum).

## Value of a digit string

For a natural number $b$ and a base-$b$ digit string
$X = x_1 x_2 \cdots x_\ell$ with digits $x_i \in \{0, \dots, b-1\}$, written with the most
significant digit first, the integer value of $X$ is

$$
n(X) = \sum_{i=1}^{\ell} x_i\, b^{\ell - i},
$$

so the last digit $x_\ell$ has weight $b^0 = 1$.

These exponents correct a typo in the corresponding displayed formula of the source.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Notation and Terminology.

Formalized by `MetaMathlibExt.stringValue`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#string-value).

## Normalized value of a digit string

For a base $b$ and a string $X$ of base-$b$ digits,
written most significant digit first, with integer value $n(X)$ and length $|X|$, the normalized
value of $X$ is the real number $n(X) / b^{|X|}$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, definition of `μ_k`.

Formalized by `MetaMathlibExt.normalizedStringValue`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#normalized-string-value).

## Weight of a digit string

For a natural number $b$ and a base-$b$ digit string $X$ of
length $|X|$, the weight of $X$ is $b^{-|X|}$, regarded as an element of $[0, \infty]$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, definition of `μ_k`.

Formalized by `MetaMathlibExt.stringWeight`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#string-weight).

## Atom of a digit string

For a natural number $b$ and a base-$b$ digit string $X$ of
length $|X|$ and integer value $n(X)$, the atom of $X$ is the measure
$b^{-|X|}\,\delta_{n(X)/b^{|X|}}$ on $\mathbb{R}$: the Dirac measure at the point $n(X)/b^{|X|}$,
scaled by the weight $b^{-|X|}$.

The Irwin measures are sums of these atoms.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, definition of `μ_k`.

Formalized by `MetaMathlibExt.stringAtom`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#string-atom).

## Irwin measure

Let $b$, $d$ and $k$ be natural numbers with $d < b$. For a finite string
$X$ of base-$b$ digits (of any length, including the empty string, with leading zeros allowed),
read most significant digit first, let $|X|$ be its length and $n(X)$ the integer it represents.
The Irwin measure $\mu_k$ of base $b$ and digit $d$ with index $k$ is the measure on $\mathbb{R}$
obtained by summing, over all strings $X$ containing exactly $k$ occurrences of the digit $d$,
the point mass of weight $b^{-|X|}$ at $n(X)/b^{|X|}$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, definition of `μ_k`.

Formalized by `MetaMathlibExt.irwinMeasure`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-measure).

## Leading digits

For natural numbers $b$, $l$ and $m$, let $L$ be the number of digits of
$m$ in base $b$. The leading-digits integer of $m$ is the natural-number quotient of $m$ by
$b^{\max(L - l,\, 0)}$, rounded down (with quotient $0$ when the divisor is $0$). For $b \ge 2$
and $L \ge l$ this is the integer formed by the first $l$ base-$b$ digits of $m$; when $L < l$
it is $m$ itself, and statements using this notion separately require $L \ge l$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, notation before Proposition 4.

Formalized by `MetaMathlibExt.leadingDigits`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#leading-digits).

## Prefix-restricted reciprocal terms

For natural numbers $b$, $d$, $k$, $n$ and $m$, write
$L(x)$ for the number of base-$b$ digits of $x$. The term is $1/m$ when $m$ is positive,
$L(n) \le L(m)$, the leading-digits integer of $m$ keeping its first $L(n)$ digits equals $n$,
and $m$ has exactly $k$ occurrences of $d$ in base $b$; otherwise the term is $0$. For $b \ge 2$
the leading-digits condition says that the base-$b$ expansion of $m$ begins with that of $n$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, notation before Proposition 4.

Formalized by `MetaMathlibExt.leadingReciprocalTerm`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#leading-reciprocal-term).

## Prefix-restricted Irwin sum

For natural numbers $b$, $d$, $k$ and $n$, this is the sum of
the prefix-restricted reciprocal terms over all natural numbers $m$: the sum of $1/m$ over the
positive integers $m$ with at least as many base-$b$ digits as $n$, whose leading-digits integer
keeping as many digits as $n$ has equals $n$, and with exactly $k$ occurrences of $d$ in base
$b$. For $b \ge 2$ the middle condition says that the base-$b$ expansion of $m$ begins with that
of $n$. It is taken as an unconditional sum of real numbers, with the value $0$ if this family is
not summable; the results that take a limit of this sum also assert summability.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 3.

Formalized by `MetaMathlibExt.leadingIrwinSum`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#leading-irwin-sum).

## Ordinary moments of the Irwin measures

For natural numbers $b$, $d$, $k$, $m$ with
$d < b$, the ordinary moment $u_{k;m}$ is the integral of $x^m$ over $[0,1)$ with respect to the
Irwin measure $\mu_k$ of base $b$ and digit $d$:

$$
u_{k;m} = \int_{[0,1)} x^m \, d\mu_k(x).
$$

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, definition before Corollary 1.

Formalized by `MetaMathlibExt.ordinaryMoment`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#ordinary-moment).

## Complementary moment

For natural numbers $b$, $d$, $k$ and $m$ with $d < b$, let $\mu_k$
be the Irwin measure for base $b$, digit $d$ and digit count $k$. The complementary moment is

$$
v_{k;m} = \int_{[0,1)} (1 - x)^m \, d\mu_k(x).
$$

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, definition before Corollary 2.

Formalized by `MetaMathlibExt.complementaryMoment`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#complementary-moment).

## Digit power sum

For natural numbers $b$, $d$ and $j$, the digit power sum $\gamma_j$ is
the real number $\sum_{0 \le a < b,\ a \ne d} a^j$, the sum of the $j$-th powers of the base-$b$
digits other than $d$, with the convention $0^0 = 1$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 1.

Formalized by `MetaMathlibExt.digitPowerSum`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#digit-power-sum).

## Complementary digit power sum

For natural numbers $b$, $d$ and $j$, let $d' = b - 1 - d$,
computed by natural-number subtraction (so $d' = 0$ when $d \ge b - 1$). The complementary digit
power sum $\gamma'_j$ is the real number $\sum_{0 \le a < b,\ a \ne d'} a^j$, the sum of the
$j$-th powers of the base-$b$ digits other than $d'$, with the convention $0^0 = 1$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 2.

Formalized by `MetaMathlibExt.complementaryDigitPowerSum`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#complementary-digit-power-sum).

## Ordinary moment recurrence

Let $b$ and $d$ be natural numbers, and for $i \ge 1$ let
$\gamma_i$ be the sum of the $i$-th powers of the base-$b$ digits $a \in \{0, \dots, b-1\}$ with
$a \ne d$. A family of real numbers $(u_{j;m})_{j, m \in \mathbb{N}}$ satisfies the ordinary
moment recurrence for $b$ and $d$ when $u_{0;0} = b$, when for every $m \ge 1$

$$
(b^{m+1} - b + 1)\, u_{0;m} = \sum_{i=1}^{m} \binom{m}{i} \gamma_i\, u_{0;m-i},
$$

and when for every $j \ge 1$ and every $m \ge 0$

$$
(b^{m+1} - b + 1)\, u_{j;m} = \sum_{i=1}^{m} \binom{m}{i} \gamma_i\, u_{j;m-i} +
\sum_{i=0}^{m} \binom{m}{i} d^i\, u_{j-1;m-i}.
$$

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 1.

Formalized by `MetaMathlibExt.OrdinaryMomentRecurrence`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 137](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L137). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#ordinary-moment-recurrence).

## Complementary moment recurrence

Let $b$ and $d$ be natural numbers, let $d' = b - 1 - d$
(natural-number subtraction), and let $\gamma'_i$ be the complementary digit power sum for $b$ and
$d$. A family $(v_{j,m})_{j, m \ge 0}$ of real numbers satisfies the complementary moment
recurrence when, for every $m \ge 0$,

$$
(b^{m+1} - b + 1)\, v_{0,m} = b^{m+1} + \sum_{i=1}^{m} \binom{m}{i} \gamma'_i \, v_{0,m-i},
$$

and, for every $j \ge 1$ and every $m \ge 0$,

$$
(b^{m+1} - b + 1)\, v_{j,m} = \sum_{i=1}^{m} \binom{m}{i} \gamma'_i \, v_{j,m-i} +
\sum_{i=0}^{m} \binom{m}{i} (d')^i \, v_{j-1,m-i},
$$

with the convention $0^0 = 1$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 2.

Formalized by `MetaMathlibExt.ComplementaryMomentRecurrence`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#complementary-moment-recurrence).

## Base depth of a real number

For a natural number $b$, a real number $x$ and a natural
number $l$, the number $x$ has base-$b$ depth $l$ when $x = z / b^l$ for some integer $z$, and for
no $q < l$ is there an integer $z$ with $x = z / b^q$. Thus $l$ is the least exponent for which
$x$ can be written as an integer divided by $b^l$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Notation and Terminology.

Formalized by `MetaMathlibExt.HasBaseDepth`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#has-base-depth).

## Scaled translate of a set

For natural numbers $b$ and $l$, a real number $x$ and a set
$U \subseteq \mathbb{R}$, the affine scale set $b^l U - b^l x$ is the image of $U$ under the map
$y \mapsto b^l y - b^l x$, that is, $\{\, b^l y - b^l x : y \in U \,\}$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Lemma 2.

Formalized by `MetaMathlibExt.affineScaleSet`, a definition declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#affine-scale-set).

## Zero has no digits

For all natural numbers $b$ and $d$, the digit $d$ occurs $0$ times in
the minimal base-$b$ representation of $0$, which is empty.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Notation and Terminology.

Formalized by `MetaMathlibExt.digitCount_zero`, a theorem declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#digit-count-zero).

## The empty digit string has value zero

For every natural number $b$, the integer value
of the empty base-$b$ digit string is $0$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Notation and Terminology.

Formalized by `MetaMathlibExt.stringValue_nil`, a theorem declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#string-value-nil).

## The atom of the empty string is the unit Dirac mass at the origin

For every natural
number $b$, the atom $b^{-|X|}\,\delta_{n(X)/b^{|X|}}$ of a base-$b$ digit string $X$ is the
Dirac measure $\delta_0$ when $X$ is the empty string.

This concerns the summand of the empty string alone, not the total mass that an Irwin measure
places at $0$ once all strings with the same value are combined.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, definition of `μ_k` and Remark `rem:zero`.

Formalized by `MetaMathlibExt.stringAtom_nil`, a theorem declared in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 200](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L200). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#string-atom-nil).

## Alternating series for the Irwin sum

Let $b > 1$ and $d < b$ be natural numbers, let
$(u_{j;m})_{j, m \in \mathbb{N}}$ be a family of real numbers satisfying the ordinary moment
recurrence for $b$ and $d$, and let $k$ and $l \ge 1$ be natural numbers. For a natural number
$n$ write $c(n)$ for the number of occurrences of the digit $d$ in the base-$b$ expansion of $n$,
and let $H^{(k)}_{b,d}$ be the Irwin sum, the sum of $1/n$ over the positive integers $n$ with
$c(n) = k$. Then the family of real numbers indexed by $m \ge 1$

$$
(-1)^m \sum_{\substack{b^{l-1} \le n < b^l \\ c(n) \le k}} \frac{u_{k - c(n);m}}{n^{m+1}}
$$

is summable, with sum

$$
H^{(k)}_{b,d} - \sum_{\substack{1 \le n < b^{l-1} \\ c(n) = k}} \frac{1}{n} -
b \sum_{\substack{b^{l-1} \le n < b^l \\ c(n) \le k}} \frac{1}{n}.
$$

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 1.

Stated but not proved: `MetaMathlibExt.irwinSum_hasSum_alternating` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-sum-has-sum-alternating).

## Properties of solutions of the ordinary moment recurrence

Let $b > 1$ and $d < b$ be
natural numbers, and let $(u_{j;m})_{j, m \in \mathbb{N}}$ be a family of real numbers that
satisfies the ordinary moment recurrence for $b$ and $d$. Then $u_{j;0} = b$ for every $j$, and for
all $j$ and all $m \ge 1$: $u_{j;m} \ge 0$, with $u_{j;m} = 0$ if and only if $j = 0$, $b = 2$ and
$d = 1$; $u_{j;m+1} \le u_{j;m}$, with strict inequality when $u_{j;m} \ne 0$;
$u_{j;m} < u_{j+1;m}$; and $u_{j;m} \to b/(m+1)$ as $j \to \infty$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 1.

Stated but not proved: `MetaMathlibExt.ordinaryMomentRecurrence_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#ordinary-moment-recurrence-properties).

## Complementary-moment series for the Irwin sums

Let $b > 1$ and $d < b$ be natural
numbers, let $k$ and $l \ge 1$ be natural numbers, and let $(v_{j,m})_{j, m \ge 0}$ be a family
of real numbers satisfying the complementary moment recurrence for $b$ and $d$. For a natural
number $n$ let $k(n)$ be the number of occurrences of $d$ in the base-$b$ representation of $n$,
and let $H^{(k)}$ be the Irwin sum, the sum of $1/n$ over the positive integers $n$ with
$k(n) = k$. Then the family indexed by $m \ge 1$ of

$$\sum_{b^{l-1} \le n < b^l,\ k(n) \le k} \frac{v_{k - k(n), m}}{(n + 1)^{m + 1}}$$

is summable, with sum

$$H^{(k)} - \sum_{1 \le n < b^{l-1},\ k(n) = k} \frac{1}{n} -
b \sum_{b^{l-1} \le n < b^l,\ k(n) \le k} \frac{1}{n + 1}.$$

The hypothesis $b > 1$ is the paper's standing assumption, in place of an isolated $b > 0$ in the
statement of Theorem 2.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 2.

Stated but not proved: `MetaMathlibExt.irwinSum_hasSum_positive` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-sum-has-sum-positive).

## Properties of the complementary moment recurrence

Let $b > 1$ and $d < b$ be natural
numbers, and let $(v_{j,m})_{j, m \ge 0}$ be any family of real numbers satisfying the
complementary moment recurrence for $b$ and $d$. Then $v_{j,0} = b$ for every $j$. For every $j$
and every $m \ge 1$: $0 < v_{j,m} \le b$; if $(b, d, j) = (2, 1, 0)$ then $v_{j,m} = 2$, and
otherwise $v_{j,m+1} < v_{j,m}$; and $v_{j+1,m} < v_{j,m}$. Finally, for every $m \ge 1$,
$v_{j,m} \to b/(m+1)$ as $j \to \infty$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 2.

Stated but not proved: `MetaMathlibExt.complementaryMomentRecurrence_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 273](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L273). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#complementary-moment-recurrence-properti).

## Monotonicity and limit of the Irwin sums

Let $b > 1$ be a base and $d < b$ a digit, and
for $k \ge 0$ let $H^{(k)}$ be the Irwin sum, the sum of $1/n$ over the positive integers $n$ whose
base-$b$ expansion contains exactly $k$ occurrences of $d$. If $d \ne 0$, then $k \mapsto H^{(k)}$
is strictly decreasing on $k \ge 1$; if $d = 0$, it is strictly decreasing on all $k \ge 0$. In
both cases $H^{(k)} \to b \log b$ as $k \to \infty$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Proposition 1.

Stated but not proved: `MetaMathlibExt.irwinSum_strictAnti_and_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-sum-strict-anti-and-tendsto).

## Lower bounds for the Irwin sum without the digit

Let $b > 2$ be a base and let $d$ be a
nonzero digit, $0 < d < b$. Let $H^{(0)}$ be the Irwin sum of $1/n$ over the positive integers $n$
whose base-$b$ expansion does not contain $d$. Then
$b \log b - b \log(1 + 1/d) < H^{(0)}$ and $b \log(b/2) < H^{(0)}$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Proposition 2.

Stated but not proved: `MetaMathlibExt.irwinSum_zero_lowerBounds` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-sum-zero-lower-bounds).

## Prefix reciprocal sums as integrals against the Irwin measure

Let $b > 1$ and $d < b$
be natural numbers, let $n > 0$ and $k$ be natural numbers, let $k(n)$ be the number of
occurrences of the digit $d$ in the base-$b$ representation of $n$, and let $\mu_k$ be the Irwin
measure of base $b$ and digit $d$ with index $k$. Then the family that assigns $1/m$ to each
positive integer $m$ whose base-$b$ representation begins with that of $n$ and contains exactly
$k(n) + k$ occurrences of $d$, and $0$ to every other natural number $m$, is summable with sum
$\int_{[0,1)} \frac{1}{n + x}\, d\mu_k(x)$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Proposition 4.

Stated but not proved: `MetaMathlibExt.integral_eq_leadingReciprocal_hasSum` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 310](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L310). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#integral-eq-leading-reciprocal-has-sum).

## Prefix sums as alternating ordinary-moment series

Let $b > 1$, let $d < b$ be a digit, let
$n$ be a positive integer, let $k(n)$ be the number of occurrences of $d$ in the base-$b$
expansion of $n$, and let $k \ge k(n)$. Write $u_{j;m} = \int_{[0,1)} x^m \, d\mu_j(x)$ for the
ordinary moments of the Irwin measure $\mu_j$. Then there is a real number $S$ such that the
reciprocals $1/N$ of the positive integers $N$ whose base-$b$ expansion begins with that of $n$
and contains exactly $k$ occurrences of $d$ have sum $S$, and the series
$\sum_{m \ge 0} (-1)^m u_{k - k(n);m} / n^{m+1}$ also has sum $S$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Corollary 1.

Stated but not proved: `MetaMathlibExt.leadingReciprocal_hasSum_ordinaryMoments` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 321](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L321). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#leading-reciprocal-has-sum-ordinary-mome).

## Prefix sums as complementary-moment series

Let $b > 1$, let $d < b$ be a digit, let $n$
be a positive integer, let $k(n)$ be the number of occurrences of $d$ in the base-$b$ expansion
of $n$, and let $k \ge k(n)$. Write $v_{j;m} = \int_{[0,1)} (1 - x)^m \, d\mu_j(x)$ for the
complementary moments of the Irwin measure $\mu_j$. Then there is a real number $S$ such that
the reciprocals $1/N$ of the positive integers $N$ whose base-$b$ expansion begins with that of
$n$ and contains exactly $k$ occurrences of $d$ have sum $S$, and the series
$\sum_{m \ge 0} v_{k - k(n);m} / (n+1)^{m+1}$ also has sum $S$. Moreover every term
$v_{k - k(n);m} / (n+1)^{m+1}$ of this series is positive, and the series is summable.

Positivity plus summability renders the paper's phrase "positive series with geometric
convergence"; no explicit ratio is asserted.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Corollary 2.

Stated but not proved: `MetaMathlibExt.leadingReciprocal_hasSum_complementaryMoments` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#leading-reciprocal-has-sum-complementary).

## Digit decomposition of the Irwin measures, positive index

Let $b > 1$ and $d < b$ be
natural numbers, and for each natural number $j$ let $\mu_j$ be the Irwin measure of base $b$ and
digit $d$ with index $j$. Let $f : \mathbb{R} \to \mathbb{R}$ be measurable and bounded on
$[0, b)$, and let $k \ge 1$. Then

$$\int_{[0,1)} f(bx)\, d\mu_k(x) =
\frac{1}{b} \sum_{a \ne d} \int_{[0,1)} f(a + x)\, d\mu_k(x) +
\frac{1}{b} \int_{[0,1)} f(d + x)\, d\mu_{k-1}(x),$$

where $a$ ranges over the digits $0, 1, \dots, b - 1$ other than $d$.

Measurability of $f$ is a hypothesis added to the paper's boundedness assumption.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Lemma 1.

Stated but not proved: `MetaMathlibExt.integral_irwinMeasure_succ` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 359](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L359). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#integral-irwin-measure-succ).

## Digit decomposition of the Irwin measure, zero index

Let $b > 1$ and $d < b$ be natural
numbers, and let $\mu_0$ be the Irwin measure of base $b$ and digit $d$ with index $0$. For every
measurable function $f : \mathbb{R} \to \mathbb{R}$ that is bounded on $[0, b)$,

$$\int_{[0,1)} f(bx)\, d\mu_0(x) = f(0) +
\frac{1}{b} \sum_{a \ne d} \int_{[0,1)} f(a + x)\, d\mu_0(x),$$

where $a$ ranges over the digits $0, 1, \dots, b - 1$ other than $d$.

Measurability of $f$ is a hypothesis added to the paper's boundedness assumption.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Lemma 1.

Stated but not proved: `MetaMathlibExt.integral_irwinMeasure_zero` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#integral-irwin-measure-zero).

## Local structure of the Irwin measures on open intervals

Let $b > 1$ and $d < b$ be
natural numbers, and for each natural number $k$ let $\mu_k$ be the Irwin measure of base $b$ and
digit $d$ with index $k$. Let $x \in [0, 1)$ have base-$b$ depth $l$, that is, $l$ is the least
natural number such that $b^l x$ is an integer; let $X$ be a string of $l$ base-$b$ digits, read
most significant digit first, whose value $n(X)$ satisfies $n(X)/b^l = x$; and let $j$ be the
number of occurrences of $d$ in $X$. Let $l' \ge l$ be a natural number, put $j' = j$ if $d > 0$
and $j' = j + l' - l$ if $d = 0$, and let $U \subseteq (x, x + b^{-l'})$. Then for every natural
number $k$: if $k < j'$ then $\mu_k(U) = 0$, and if $k \ge j'$ then, as real numbers,
$\mu_k(U) = b^{-l'} \mu_{k-j'}(b^{l'} U - b^{l'} x)$, where $b^{l'} U - b^{l'} x$ is the image
of $U$ under $y \mapsto b^{l'} y - b^{l'} x$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Lemma 2.

Stated but not proved: `MetaMathlibExt.irwinMeasure_open_local_mass` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 394](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L394). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-measure-open-local-mass).

## Local structure of the Irwin measures on half-open intervals

Let $b > 1$ and $d < b$ be
natural numbers, and for each natural number $k$ let $\mu_k$ be the Irwin measure of base $b$ and
digit $d$ with index $k$. Let $x \in [0, 1)$ have base-$b$ depth $l$, that is, $l$ is the least
natural number such that $b^l x$ is an integer; let $X$ be a string of $l$ base-$b$ digits, read
most significant digit first, whose value $n(X)$ satisfies $n(X)/b^l = x$; and let $j$ be the
number of occurrences of $d$ in $X$. Let $l' \ge l$ be a natural number, put $j' = j$ if $d > 0$
and $j' = j + l' - l$ if $d = 0$, and let $k \ge j'$ be a natural number. Then for every set
$U \subseteq [x, x + b^{-l'})$, as real numbers,
$\mu_k(U) = b^{-l'} \mu_{k-j'}(b^{l'} U - b^{l'} x)$, where $b^{l'} U - b^{l'} x$ is the image
of $U$ under $y \mapsto b^{l'} y - b^{l'} x$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Lemma 3.

Stated but not proved: `MetaMathlibExt.irwinMeasure_halfOpen_deeper_local_mass` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-measure-half-open-deeper-local-mas).

## Local structure of the Irwin measures on cylinders

Let $b > 1$ and $d < b$ be natural
numbers, and for each natural number $k$ let $\mu_k$ be the Irwin measure of base $b$ and digit
$d$ with index $k$. Let $x \in [0, 1)$ have base-$b$ depth $l$, that is, $l$ is the least natural
number such that $b^l x$ is an integer; let $X$ be a string of $l$ base-$b$ digits, read most
significant digit first, whose value $n(X)$ satisfies $n(X)/b^l = x$; and let $j$ be the number
of occurrences of $d$ in $X$. Then for every $k < j$ the restriction of $\mu_k$ to
$[x, x + b^{-l})$ is the zero measure, and for every $k \ge j$ and every subset
$U \subseteq [x, x + b^{-l})$, as real numbers $\mu_k(U) = b^{-l} \mu_{k-j}(b^l U - b^l x)$,
where $b^l U - b^l x$ is the image of $U$ under $y \mapsto b^l y - b^l x$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Proposition 8.

Stated but not proved: `MetaMathlibExt.irwinMeasure_halfOpen_local_mass` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 434](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L434). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-measure-half-open-local-mass).

## Masses of intervals under the Irwin measures

Let $b > 1$ and $d < b$ be natural numbers,
and for each natural number $k$ let $\mu_k$ be the Irwin measure of base $b$ and digit $d$ with
index $k$; masses below are taken as real numbers. First, for all reals $0 \le t < u \le 1$ and
every natural number $l'$ such that $b^{l'} t$ and $b^{l'} u$ are integers,
$\mu_k([t, u)) = bu - bt$ for every $k \ge l'$. Second, for every nonempty interval
$I \subseteq [0, 1)$, $\mu_k(I)$ tends to $b(\sup I - \inf I)$ as $k \to \infty$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Proposition 9.

Stated but not proved: `MetaMathlibExt.irwinMeasure_interval_convergence` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#irwin-measure-interval-convergence).

## Limit of the prefix-restricted Irwin sums

Let $b > 1$, let $d < b$ be a digit and let $n$
be a positive integer. For every $k \ge 0$, the family of reciprocals $1/m$ of the positive
integers $m$ whose base-$b$ expansion begins with the base-$b$ expansion of $n$ and contains
exactly $k$ occurrences of $d$ is summable, and its sum tends to $b \log(1 + 1/n)$ as
$k \to \infty$.

## Sources

- Jean-François Burnol, *Measures for the Summation of Irwin Series*, INTEGERS 26 (2026), Article A11, Theorem 3.

Stated but not proved: `MetaMathlibExt.leadingIrwinSum_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean, line 472](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/IrwinSeriesMeasuresWanted.lean#L472). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html#leading-irwin-sum-tendsto).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Irwin series](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/irwin-series)
