---
declaration: section
origin: cited
lean: NumberField.primitiveIntMinpoly, MathlibExt.NumberTheory.Height.AbsoluteWanted.absLogHeight₁_eq_log_leadingCoeff_add_sum_log_roots_of_isIntegral, MathlibExt.NumberTheory.Height.AbsoluteWanted.absLogHeight₁_eq_log_leadingCoeff_add_sum_log_roots_of_isAlgebraic, MathlibExt.NumberTheory.Height.AbsoluteWanted.absLogHeight₁_eq_log_leadingCoeff_add_sum_log_roots, MathlibExt.NumberTheory.Height.AbsoluteWanted.absMulHeight₁_eq_mapMahlerMeasure_of_isIntegral, MathlibExt.NumberTheory.Height.AbsoluteWanted.absMulHeight₁_eq_mapMahlerMeasure, NumberField.positivePrimitiveIntMinpoly, NumberField.positivePrimitiveIntMinpoly_isPrimitive
statement: formalized
proof: formalized
---

# Absolute height and Mahler measure

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html).

## Primitive integral minimal polynomial

Let $K$ be a field that is an algebra over
$\mathbb{Q}$, let $x \in K$, and let $m_x \in \mathbb{Q}[X]$ be the minimal polynomial of $x$
over $\mathbb{Q}$, with $m_x = 0$ when $x$ is not algebraic over $\mathbb{Q}$. Choose a nonzero
integer $b$ such that $b\,m_x$ has integer coefficients. The primitive integral minimal polynomial
$P_x \in \mathbb{Z}[X]$ of $x$ is the primitive part of $b\,m_x$: when $b\,m_x \neq 0$ it is
$b\,m_x$ divided by the nonnegative greatest common divisor of its coefficients, and when
$b\,m_x = 0$ it is $1$.

Thus for algebraic $x$, $P_x$ is a primitive polynomial with integer coefficients that is a
nonzero rational multiple of $m_x$, determined up to sign, and for nonalgebraic $x$, $P_x = 1$.
The sign is immaterial for applications to Mahler measure.

Formalized by `NumberField.primitiveIntMinpoly`, a definition declared in [MathlibExt/NumberTheory/Height/Absolute.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/Absolute.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#primitive-int-minpoly).

## Logarithmic height from the roots of the minimal polynomial, for an integral element

Let
$K$ be a field of characteristic zero and let $x \in K$ be integral over $\mathbb{Q}$. Let $d$ be
the degree of the minimal polynomial of $x$ over $\mathbb{Q}$, and let $P_x \in \mathbb{Z}[X]$ be
the primitive integral minimal polynomial of $x$, with leading coefficient $a$. Then the absolute
logarithmic height of $x$ is

$$h(x) = \frac{1}{d}\Big(\log |a| + \sum_{z} \log^+ |z|\Big),$$

where the sum runs over the complex roots $z$ of $P_x$, counted with multiplicity, and
$\log^+ t = \max(0, \log t)$.

Formalized by `MathlibExt.NumberTheory.Height.AbsoluteWanted.absLogHeight₁_eq_log_leadingCoeff_add_sum_log_roots_of_isIntegral`, a theorem declared in [MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean, line 714](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean#L714). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#abs-log-height-eq-log-leading-coeff-add).

## Logarithmic height from the roots of the minimal polynomial, for an algebraic element

Let
$K$ be a field of characteristic zero and let $x \in K$ be algebraic over $\mathbb{Q}$. Let $d$ be
the degree of the minimal polynomial of $x$ over $\mathbb{Q}$, and let $P_x \in \mathbb{Z}[X]$ be
the primitive integral minimal polynomial of $x$, with leading coefficient $a$. Then the absolute
logarithmic height of $x$ is

$$h(x) = \frac{1}{d}\Big(\log |a| + \sum_{z} \log^+ |z|\Big),$$

where the sum runs over the complex roots $z$ of $P_x$, counted with multiplicity, and
$\log^+ t = \max(0, \log t)$.

Formalized by `MathlibExt.NumberTheory.Height.AbsoluteWanted.absLogHeight₁_eq_log_leadingCoeff_add_sum_log_roots_of_isAlgebraic`, a theorem declared in [MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean, line 737](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean#L737). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#abs-log-height-eq-log-leading-coeff-add-2).

## Logarithmic height from the roots of the minimal polynomial

Let $K$ be a field of
characteristic zero that is algebraic over $\mathbb{Q}$, and let $x \in K$. Let $d$ be the degree
of the minimal polynomial of $x$ over $\mathbb{Q}$, and let $P_x \in \mathbb{Z}[X]$ be the
primitive integral minimal polynomial of $x$, with leading coefficient $a$. Then the absolute
logarithmic height of $x$ is

$$h(x) = \frac{1}{d}\Big(\log |a| + \sum_{z} \log^+ |z|\Big),$$

where the sum runs over the complex roots $z$ of $P_x$, counted with multiplicity, and
$\log^+ t = \max(0, \log t)$.

## Sources

- arXiv:2608.15903; equivalent formulas occur in arXiv:2304.11607, 2309.11173, 2311.13047, 2311.14001, 2607.25168, 2608.04445, and 2608.20995.

Formalized by `MathlibExt.NumberTheory.Height.AbsoluteWanted.absLogHeight₁_eq_log_leadingCoeff_add_sum_log_roots`, a theorem declared in [MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean, line 756](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean#L756). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#abs-log-height-eq-log-leading-coeff-add-3).

## Multiplicative height as a Mahler measure, for an integral element

Let $K$ be a field of
characteristic zero and let $x \in K$ be integral over $\mathbb{Q}$. Let $d$ be the degree of the
minimal polynomial of $x$ over $\mathbb{Q}$, and let $P_x \in \mathbb{Z}[X]$ be the primitive
integral minimal polynomial of $x$. Then the absolute multiplicative height of $x$ is
$H(x) = M(P_x)^{1/d}$, where $M(P_x)$ is the Mahler measure of $P_x$ regarded as a polynomial
with complex coefficients.

Formalized by `MathlibExt.NumberTheory.Height.AbsoluteWanted.absMulHeight₁_eq_mapMahlerMeasure_of_isIntegral`, a theorem declared in [MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean, line 768](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean#L768). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#abs-mul-height-eq-map-mahler-measure-of).

## Absolute multiplicative height as a Mahler measure

Let $K$ be a field of characteristic
zero that is algebraic over $\mathbb{Q}$, and let $x \in K$. Let $d$ be the degree of the minimal
polynomial of $x$ over $\mathbb{Q}$, and let $P_x \in \mathbb{Z}[X]$ be the primitive integral
minimal polynomial of $x$. Then the absolute multiplicative height of $x$ is $H(x) = M(P_x)^{1/d}$,
where $M(P_x)$ is the Mahler measure of $P_x$ regarded as a polynomial with complex coefficients.

## Sources

- arXiv:2608.15891, lines 205–217; equivalent formulations also occur in arXiv:2306.11331, 2307.11849, 2307.14915, 2312.04354, 2607.28857, 2607.29208, and 2608.11904.

Formalized by `MathlibExt.NumberTheory.Height.AbsoluteWanted.absMulHeight₁_eq_mapMahlerMeasure`, a theorem declared in [MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean, line 792](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/AbsoluteLogHeightRoots.lean#L792). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#abs-mul-height-eq-map-mahler-measure).

## Positive primitive integral minimal polynomial

Let $K$ be a field that is a
$\mathbb{Q}$-algebra, let $x \in K$, and let $p$ be the canonical primitive integral minimal
polynomial of $x$. The positive primitive integral minimal polynomial of $x$ is $-p$ if the
leading coefficient of $p$ is negative, and $p$ otherwise.

Since $p$ is nonzero, the result has positive leading coefficient. When $x$ is not algebraic
over $\mathbb{Q}$, $p$ is the constant polynomial $1$, and so is the result.

Formalized by `NumberField.positivePrimitiveIntMinpoly`, a definition declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#positive-primitive-int-minpoly).

## The positive primitive integral minimal polynomial is primitive

For every element $x$ of
a field $K$ that is an algebra over $\mathbb{Q}$, the positive primitive integral minimal
polynomial of $x$ is primitive: the greatest common divisor of its integer coefficients is $1$.

Formalized by `NumberField.positivePrimitiveIntMinpoly_isPrimitive`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#positive-primitive-int-minpoly-is-primit).

## The positive primitive integral minimal polynomial is nonzero

Let $K$ be a field
that is a $\mathbb{Q}$-algebra. For every $x \in K$, the positive primitive integral minimal
polynomial of $x$ is not the zero polynomial.

Formalized by `NumberField.positivePrimitiveIntMinpoly_ne_zero`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#positive-primitive-int-minpoly-ne-zero).

## The positive primitive integral minimal polynomial has positive leading coefficient

For
every element $x$ of a field $K$ that is an algebra over $\mathbb{Q}$, the leading coefficient of
the positive primitive integral minimal polynomial of $x$ is a strictly positive integer.

Formalized by `NumberField.positivePrimitiveIntMinpoly_leadingCoeff_pos`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#positive-primitive-int-minpoly-leading-c).

## Sign normalization preserves the degree

For every element $x$ of a field $K$ that is an
algebra over $\mathbb{Q}$, the positive primitive integral minimal polynomial of $x$ has the same
degree as the primitive integral minimal polynomial of $x$.

Formalized by `NumberField.positivePrimitiveIntMinpoly_natDegree`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#positive-primitive-int-minpoly-nat-degre).

## The positive primitive integral minimal polynomial has the degree of the minimal polynomial

**The positive primitive integral minimal polynomial has the degree of the minimal
polynomial.** For every element $x$ of a field $K$ that is an algebra over $\mathbb{Q}$, the
positive primitive integral minimal polynomial of $x$ has the same degree as the minimal
polynomial of $x$ over $\mathbb{Q}$.

Degrees are natural numbers, the zero polynomial having degree $0$; if $x$ is not algebraic over
$\mathbb{Q}$, both degrees are $0$.

Formalized by `NumberField.positivePrimitiveIntMinpoly_natDegree_eq`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#positive-primitive-int-minpoly-nat-degre-2).

## An algebraic element is a root of its positive primitive integral minimal polynomial

Let
$K$ be a field of characteristic zero that is an algebra over $\mathbb{Q}$, and let $x \in K$ be
algebraic over $\mathbb{Q}$. Then the positive primitive integral minimal polynomial of $x$, with
its integer coefficients mapped into $K$, vanishes at $x$.

Formalized by `NumberField.positivePrimitiveIntMinpoly_eval₂_at`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#positive-primitive-int-minpoly-eval-at).

## Algebraic Mahler measure

For an element $x$ of a field $K$ that is an algebra over
$\mathbb{Q}$, the algebraic Mahler measure $M(x)$ is the Mahler measure of the positive primitive
integral minimal polynomial of $x$, regarded as a polynomial with complex coefficients. If $x$ is
not algebraic over $\mathbb{Q}$, this polynomial is the constant $1$, so $M(x) = 1$.

Formalized by `NumberField.algebraicMahlerMeasure`, a definition declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#algebraic-mahler-measure).

## The sign normalization does not change the Mahler measure

For every element $x$ of a
field $K$ that is an algebra over $\mathbb{Q}$, the algebraic Mahler measure of $x$, that is the
Mahler measure of the positive primitive integral minimal polynomial of $x$, equals the Mahler
measure of the primitive integral minimal polynomial of $x$, both polynomials being regarded as
polynomials with complex coefficients.

Formalized by `NumberField.algebraicMahlerMeasure_eq`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#algebraic-mahler-measure-eq).

## The algebraic Mahler measure is at least one

For every element $x$ of a field $K$ that
is an algebra over $\mathbb{Q}$, the algebraic Mahler measure $M(x)$ of $x$ satisfies
$1 \le M(x)$.

This holds because the positive primitive integral minimal polynomial of $x$ has a positive
integer leading coefficient.

Formalized by `NumberField.one_le_algebraicMahlerMeasure`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#one-le-algebraic-mahler-measure).

## Absolute logarithmic height from the algebraic Mahler measure

Let $K$ be a field of
characteristic zero that is an algebra over $\mathbb{Q}$, and let $x \in K$ be algebraic over
$\mathbb{Q}$. Let $d$ be the degree of the minimal polynomial of $x$ over $\mathbb{Q}$, and let
$M(x)$ be the algebraic Mahler measure of $x$, the Mahler measure of the positive primitive
integral minimal polynomial of $x$ regarded as a complex polynomial. Then the absolute
logarithmic height of $x$ equals $\log M(x) / d$.

Formalized by `NumberField.absLogHeight₁_eq_log_algebraicMahlerMeasure`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#abs-log-height-eq-log-algebraic-mahler-m).

## One plus the logarithm of a Mahler measure above one is below it

Let $x$ be an element
of a field $K$ that is an algebra over $\mathbb{Q}$, and let $M(x)$ be its algebraic Mahler
measure. If $M(x) > 1$, then $1 + \log M(x) < M(x)$.

Voutier uses this elementary inequality to pass from lower bounds for $\log M(x)$ to lower bounds
for $M(x)$.

Formalized by `NumberField.log_algebraicMahlerMeasure_add_one_lt`, a theorem declared in [MathlibExt/NumberTheory/Height/PrimitiveMahler.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Height/PrimitiveMahler.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html#log-algebraic-mahler-measure-add-one-lt).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Absolute height and Mahler measure](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/heights-mahler-measure/absolute-height-and-mahler-measure)
