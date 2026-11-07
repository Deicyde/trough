A **polynomial in one indeterminate** over a [ring](trough:Ring) $R$ is a formal expression
$a_0 + a_1 X + \dots + a_n X^n$ with coefficients $a_i$ in $R$, added and multiplied by the
familiar rules of high-school algebra. The polynomials over $R$ form a ring $R[X]$, the
polynomial ring. It is the simplest way to enlarge a ring by one new
element, and it underlies much of algebra: the theory of equations, field extensions,
algebraic geometry and the study of linear maps through their characteristic polynomials.

## Definition

Let $R$ be a ring. A polynomial over $R$ is a sequence $(a_0, a_1, a_2, \dots)$ of elements
of $R$ in which only finitely many terms are nonzero, that is, a
[finitely supported function](trough:Finsupp) from the natural numbers to $R$. The term $a_n$
is the coefficient of $X^n$, and
two polynomials are equal exactly when all their coefficients agree.
Addition is coefficientwise, and multiplication is defined so that $X^i X^j = X^{i+j}$: the
product of $f = \sum_i a_i X^i$ and $g = \sum_j b_j X^j$ has
as coefficient of $X^n$ the sum of $a_i b_j$ over all pairs with $i + j = n$,

$$fg = \sum_{n \ge 0} \Bigl( \sum_{i+j=n} a_i b_j \Bigr) X^n.$$

The indeterminate $X$ is the sequence $(0, 1, 0, 0, \dots)$, and an element $a$ of $R$ is
identified with the constant polynomial $(a, 0, 0, \dots)$. With these identifications
every polynomial is the finite sum of its terms $a_i X^i$,
which justifies the usual notation. Even when $R$ is not commutative,
$X$ commutes with every polynomial.

The degree of a nonzero polynomial $f$ is the largest $n$ with $a_n \neq 0$, and $a_n$ is its
leading coefficient; $f$ is monic if its leading coefficient is $1$. The zero polynomial has
no nonzero coefficient, and its degree is set to $-\infty$.

When $R$ is commutative, a polynomial $f = a_0 + a_1 X + \dots + a_n X^n$ can be evaluated at
an element $x$ of $R$: its value is $f(x) = a_0 + a_1 x + \dots + a_n x^n$,
and $x$ is a root of $f$ when $f(x) = 0$.

## Examples

- Over the rational numbers, $X^2 - 2$ is monic of degree $2$; over the real numbers it
  factors as $(X - \sqrt 2)(X + \sqrt 2)$.
- A polynomial is not the same thing as the function it defines. Over the field
  $\mathbb{Z}/p\mathbb{Z}$ with $p$ prime, the polynomial $X^p - X$ is nonzero,
  since its degree $p$ exceeds $1$, yet by [Fermat's little theorem](trough:ZMod.pow_card_sub_one_eq_one)
  $a^p = a$ for every $a$ in $\mathbb{Z}/p\mathbb{Z}$, so it vanishes at every point.
- Over $\mathbb{Z}/4\mathbb{Z}$ the polynomial $1 + 2X$ is invertible, because
  $(1 + 2X)^2 = 1 + 4X + 4X^2 = 1$. Here the coefficient $2$ is nilpotent, since $2^2 = 0$.
  Over a commutative ring,
  a polynomial is a unit exactly when its constant term is a unit and all its other coefficients are nilpotent,
  so nilpotent coefficients, not zero divisors in general, are what allow units of positive
  degree: $\mathbb{Z}/6\mathbb{Z}$ has zero divisors but no nonzero nilpotents, and every unit
  of $(\mathbb{Z}/6\mathbb{Z})[X]$ is constant.

## Properties

- **Degree of a product.** If $R$ has no zero divisors, then
  $\deg(fg) = \deg f + \deg g$, with the convention
  $-\infty + n = -\infty$. Hence $R[X]$ has no zero divisors when $R$ has none, and since $R$
  sits inside $R[X]$ as the constants,
  $R[X]$ has no zero divisors exactly when $R$ has none.
  When $R$ has no zero divisors, the degree formula also shows that
  the units of $R[X]$ are the constant polynomials whose value is a unit of $R$.
- **Division with remainder.** Over a nonzero ring $R$, let $g$ be monic. Every $f$ can be
  written as $f = gq + r$ with a remainder $r$ satisfying
  $\deg r < \deg g$. When the coefficients form a
  [field](trough:Field) $K$, every nonzero $g$ can be made monic, and
  $K[X]$ is a Euclidean domain (see
  [$K[X]$ is Euclidean](trough:Polynomial.instEuclideanDomain)).
- **Roots.** For a commutative ring $R$ and $a$ in $R$,
  $X - a$ divides $f$ if and only if $f(a) = 0$ (the
  [factor theorem](trough:Polynomial.dvd_iff_isRoot)). If moreover $R$ is an integral domain,
  a nonzero polynomial $f$ has at most $\deg f$ roots, counted with multiplicity;
  see [roots of a polynomial](trough:Polynomial.roots). Hence over an infinite integral domain
  two polynomials that take the same value at every point are equal.
- **Universal property.** Let $R$ be commutative and $A$ an [$R$-algebra](trough:Algebra).
  Algebra homomorphisms from $R[X]$ to $A$ correspond one to one to elements of $A$:
  each $x$ in $A$ gives the evaluation map $f \mapsto f(x)$, and each homomorphism is determined
  by the image of $X$. More generally, a [ring morphism](trough:RingHom) $\varphi$ from $R$ to a
  commutative ring $S$ and an element $s$ of $S$
  give a ring morphism from $R[X]$ to $S$ that applies $\varphi$
  to the coefficients and substitutes $s$ for $X$; see [polynomial functions](trough:Polynomial.eval).
- **Finiteness.** By the [Hilbert basis theorem](trough:Polynomial.isNoetherianRing),
  if a commutative ring $R$ is Noetherian, then so is $R[X]$
  (see [Noetherian ring](trough:IsNoetherianRing)).

## Related concepts

Iterating the construction, or allowing any set of indeterminates, gives
[polynomials in several indeterminates](trough:MvPolynomial); dropping the finiteness
condition on the coefficients gives [formal power series](trough:PowerSeries). Within $R[X]$
one studies [irreducible polynomials](trough:Irreducible), with tests such as
[Eisenstein's criterion](trough:Polynomial.irreducible_of_eisenstein_criterion), the
[formal derivative](trough:Polynomial.derivative) and
[separable polynomials](trough:Polynomial.Separable). Quotients of $K[X]$ by an irreducible
polynomial build field extensions, as in the [rupture field](trough:AdjoinRoot) and the
[splitting field](trough:Polynomial.SplittingField).

## In Mathlib

Mathlib defines polynomials over any semiring, commutative or not, so that the natural numbers
and other semirings without subtraction are allowed as coefficients; results that need
negatives, commutativity or the absence of zero divisors carry those as hypotheses. A
polynomial is stored as a finitely supported function from the natural numbers to the
coefficients, wrapped in its own structure so that it is used only through its own interface;
the constant polynomials come from a ring morphism from $R$ into $R[X]$, and $X$ is a separate
element. Mathlib has two notions of degree: one with values in the natural numbers extended by
a bottom element, where the zero polynomial has degree bottom,
playing the role of $-\infty$, and one with natural-number values, where
the zero polynomial has degree $0$. The bound on the number
of roots appears in both forms: with the first for nonzero polynomials, and with the second for
all polynomials, the zero polynomial included, since Mathlib assigns it no roots. Division by
a monic polynomial is defined for every divisor, monic or not, and the identity $f = gq + r$
holds in all cases, with a quotient of zero when the divisor is not monic; only the degree
bound on the remainder needs a monic divisor and a nonzero ring. Over a field, a separate
division operation divides by any nonzero polynomial.

## Depends on

- [Ring](trough:Ring)
- [Finitely supported function](trough:Finsupp)
