A **polynomial in several indeterminates** over a commutative [ring](trough:Ring) $R$ is a
finite sum of terms $c\,X_1^{a_1}X_2^{a_2}\cdots X_n^{a_n}$ with coefficients $c$ in $R$,
such as $x^2 + y^2 - 1$ or $xyz - 2$. These polynomials form a commutative ring,
written $R[X_1, \dots, X_n]$ or $R[X_i : i \in I]$, which generalizes the
[polynomials in one indeterminate](trough:Polynomial). It is a basic object of
commutative algebra and algebraic geometry: every finitely generated commutative
$R$-algebra is a quotient of such a ring, and the solution sets of systems of polynomial
equations are studied through its [ideals](trough:Ideal).

## Definition

Let $R$ be a commutative ring and $I$ a set indexing the indeterminates; $I$ may be
infinite. An exponent vector is a function $\alpha \colon I \to \mathbb{N}$ that is
zero outside a finite set (a [finitely supported function](trough:Finsupp)), and to each
exponent vector corresponds a monomial

$$X^\alpha = \prod_{i \in I} X_i^{\alpha(i)},$$

a finite product since almost all exponents vanish. A polynomial is a formal finite sum
$p = \sum_\alpha p_\alpha X^\alpha$, that is, a function $\alpha \mapsto p_\alpha$ from
exponent vectors to $R$ with only finitely many nonzero values. Polynomials are added
coefficientwise, and multiplied by extending the rule
$X^\alpha \cdot X^\beta = X^{\alpha + \beta}$
bilinearly, so that

$$(pq)_\gamma = \sum_{\alpha + \beta = \gamma} p_\alpha\, q_\beta.$$

The result is the polynomial ring in the indeterminates $X_i$ with coefficients in $R$.
By construction, two polynomials with the same coefficient at every monomial are equal,
and every polynomial is the sum of its finitely many nonzero terms.
Each term is a constant times a product of powers of indeterminates:
$c\,X^\alpha$ is the constant $c$ times $\prod_i X_i^{\alpha(i)}$.
The map sending $c$ to the constant polynomial $c$ is
injective, so $R$ sits inside the polynomial ring.

The total degree of a nonzero polynomial is the largest value of
$\sum_i \alpha(i)$ over the exponent vectors $\alpha$ with $p_\alpha \neq 0$; for
example $x^3 y + y^2$ has total degree $4$.

## Examples

- With no indeterminates, the polynomial ring is
  $R$ itself; with exactly one, it is
  the ring $R[X]$ of polynomials in one indeterminate.
- Polynomials in $n + 1$ indeterminates are the same as
  polynomials in one indeterminate whose coefficients are polynomials in the other $n$;
  more generally, splitting the indeterminates into two sets $I$ and $J$ identifies
  $R[X_i, Y_j]$ with $(R[Y_j])[X_i]$. This identification
  lets many properties pass from one indeterminate to finitely many by induction.
- In three indeterminates, $X_1X_2 + X_1X_3 + X_2X_3$ is unchanged by any permutation
  of the indeterminates; it is one of the elementary
  [symmetric polynomials](trough:MvPolynomial.IsSymmetric).
- The determinant of an $n \times n$ matrix is a polynomial with integer coefficients
  in its $n^2$ entries, regarded as indeterminates.

## Properties

**Universal property.** For every commutative $R$-algebra $A$ (see
[associative algebra](trough:Algebra)) and every family $(a_i)_{i \in I}$ of elements of
$A$, there is an $R$-algebra homomorphism from $R[X_i : i \in I]$ to $A$
sending each $X_i$ to $a_i$, and
it is the only $R$-algebra homomorphism that agrees with it on every $X_i$.
This homomorphism is evaluation, or substitution, at the point $(a_i)$. In this sense
the polynomial ring is the free commutative $R$-algebra on the set $I$; dropping
commutativity gives the [free algebra](trough:FreeAlgebra). Polynomials also admit
induction: a statement that holds for constants, is preserved by sums, and is
preserved by multiplication by an indeterminate holds for every polynomial.

**Ring-theoretic properties.**

- If $R$ is an integral domain, so is $R[X_i : i \in I]$. The ring is nonzero because $R$
  sits inside it. To see that it has no zero divisors, fix a monomial order, such as the
  lexicographic order: a total order on monomials, compatible with multiplication, in
  which $1$ is the smallest monomial. The leading coefficient of a nonzero polynomial is
  its coefficient at its largest monomial, so it is nonzero. If $R$ has no zero divisors,
  the leading coefficient of $pq$ is the product of the leading coefficients of $p$ and $q$,
  so for nonzero $p$ and $q$ it is nonzero, and hence $pq \neq 0$. Comparing leading
  monomials under an order that ranks monomials first by degree shows, in the same way,
  that for nonzero $p$ and $q$ the total degree of $pq$ is the sum of the total degrees of $p$ and $q$.
- If $R$ is a [unique factorisation domain](trough:UniqueFactorizationMonoid), so is the
  polynomial ring in any set of indeterminates
  (see [unique factorisation in polynomial rings](trough:MvPolynomial.uniqueFactorizationMonoid)).
- By the [Hilbert basis theorem](trough:Polynomial.isNoetherianRing) and induction on the
  number of indeterminates, if $R$ is a [Noetherian ring](trough:IsNoetherianRing) then
  so is the polynomial ring in finitely many indeterminates over $R$.
  With infinitely many indeterminates over a nonzero ring this fails: the ideal generated
  by all the $X_i$ is not finitely generated.

**Polynomials and functions.** Each polynomial $p$ over $R$ defines a function
$R^I \to R$ by evaluation. If $R$ is an infinite integral domain,
two polynomials that agree at every point of $R^I$ are equal,
so polynomials may be identified with the functions they define. Over a finite field
this fails: over a field with $q$ elements, $X_1^q - X_1$ is a nonzero polynomial that
vanishes at every point.

## Related concepts

Every polynomial is uniquely a sum of homogeneous polynomials, one in each total degree
(see [decomposition into homogeneous components](trough:MvPolynomial.sum_homogeneousComponent)).
The [Nullstellensatz](trough:MvPolynomial.vanishingIdeal_zeroLocus_eq_radical) describes,
over an algebraically closed field, which polynomials in finitely many indeterminates
vanish on the common zeros of an ideal, and the
[Schwartz–Zippel theorem](trough:MvPolynomial.schwartz_zippel_sup_sum) bounds how many
points of a finite grid a nonzero polynomial over an integral domain can vanish at.
Allowing infinite sums of monomials in one indeterminate gives
[power series](trough:PowerSeries).

## In Mathlib

Mathlib allows the coefficients to lie in any commutative semiring, so polynomials with
natural-number coefficients are covered, and indexes the indeterminates by an arbitrary
type, which may be infinite. A polynomial is literally a finitely supported function
from exponent vectors to coefficients, and exponent vectors are themselves finitely
supported functions from the index type to the natural numbers; multiplication is the
convolution of the monoid algebra of the exponent vectors. Polynomials in one
indeterminate form a separate type, related to the several-indeterminate version with a
one-element index type by an isomorphism of algebras. The total degree is a natural
number, and the zero polynomial is given total degree $0$, so the additivity of total
degree under multiplication requires both factors to be nonzero. The integral domain
property holds over any semiring that is a domain and has cancellative addition, which
for a ring is automatic.

## Depends on

- [Ring](trough:Ring)
- [Finitely supported function](trough:Finsupp)
