A **separable polynomial** over a [field](trough:Field) is a nonzero [polynomial](trough:Polynomial) without
repeated roots: in any field over which it factors into linear factors, its roots are pairwise
distinct. Separability can be decided inside the base field, without finding a single root, by
checking that the polynomial and its [formal derivative](trough:Polynomial.derivative) have no common
factor of positive degree. The notion is basic to field theory: separable extensions, built from roots of separable
polynomials, are the setting of the [primitive element theorem](trough:Field.exists_primitive_element)
and of Galois theory. In [characteristic zero](trough:CharZero) every irreducible polynomial is
separable, so the subtleties live in [characteristic $p$](trough:CharP).

## Definition

Let $R$ be a commutative ring, $f \in R[X]$, and $f'$ its formal derivative. The polynomial $f$ is
separable when $f$ and $f'$ are [coprime](trough:IsCoprime) in the sense
of Bézout: $f$ is separable exactly when there are polynomials $a, b \in R[X]$ with $af + bf' = 1$.

Over a field $F$ the ring $F[X]$ is a Euclidean domain, so the condition says that $f$ and $f'$ have
no common factor of positive degree, which the Euclidean algorithm decides. The connection with
[roots](trough:Polynomial.roots) is the following:
if a nonzero polynomial $f$ over $F$ splits into linear factors over an extension field $K$, then $f$ is separable if and only if its roots in $K$ are pairwise distinct,
that is, each root has [multiplicity](trough:Polynomial.rootMultiplicity) one. Taking $K$ to be a
[splitting field](trough:Polynomial.SplittingField) of $f$ gives the definition by roots. The reason
is the product rule: if $(X - \alpha)^2$ divides $f$, then $X - \alpha$ divides $f'$; conversely, if
$f = (X - \alpha)g$ and $f'(\alpha) = 0$, then $g(\alpha) = 0$, so $\alpha$ is a repeated root. Since $f$ splits over $K$, any common factor of
positive degree of $f$ and $f'$ has a root in $K$, which is then a common root of $f$ and $f'$.

For an [irreducible](trough:Irreducible) polynomial the test is simpler, since the only candidate for a
common factor of $f$ and $f'$ is $f$ itself, up to a nonzero constant factor, which can divide $f'$ only if $f' = 0$, because
$f'$ has smaller degree than $f$:
an irreducible polynomial $f$ over a field is separable if and only if $f' \neq 0$.

## Examples

- **Linear and constant polynomials.** Over a commutative ring,
  $X - c$ is separable for every $c$, its derivative being $1$.
  A constant polynomial $c$ is separable if and only if $c$ is a unit,
  so over any ring other than the zero ring
  the zero polynomial is not separable.
- **A repeated factor.** The polynomial $(X - 1)^2 = X^2 - 2X + 1$ has derivative $2(X - 1)$, and the
  two share the factor $X - 1$. In general
  a separable polynomial is squarefree: if $g^2$ divides it,
  then $g$ is a unit.
- **Binomials.** Over a field $F$,
  $X^n - a$ is separable whenever $a \neq 0$ and the natural number $n$ is nonzero in $F$,
  and $X^n - 1$ is separable if and only if $n$ is nonzero in $F$.
  Over the complex numbers, for $n \ge 1$, $X^n - 1$ has $n$ distinct roots, the $n$th roots of unity; over a field of characteristic
  $p$, the polynomial $X^p - 1$ equals $(X - 1)^p$.
- **Finite fields.** Over a commutative ring of characteristic $p$,
  $X^q - X$ is separable whenever $p$ divides $q$, since its derivative
  is $qX^{q-1} - 1 = -1$. When $p$ is prime and $q = p^n$ with $n \ge 1$, the roots of this polynomial in
  a splitting field over $\mathbb{F}_p$ form the field with $q$ elements (see [finite fields](trough:Mathlib.FieldTheory.Finite.Basic)).
- **An inseparable irreducible polynomial.** Let $F = \mathbb{F}_p(t)$ be the field of rational
  functions over the field with $p$ elements, and $f = X^p - t$. It is irreducible in
  $\mathbb{F}_p[t][X]$ by [Eisenstein's criterion](trough:Polynomial.irreducible_of_eisenstein_criterion)
  at the prime $t$, hence over $\mathbb{F}_p(t)$ by Gauss's lemma, since $f$ is monic; but $f' = pX^{p-1} = 0$, so $f$ is not separable. If $s^p = t$ in a splitting field, then
  $X^p - t = (X - s)^p$, so $f$ has one root, of multiplicity $p$.
- **Dependence on the coefficient ring.** Over $\mathbb{Q}$, $X^2 + 1$ is separable, because
  $(X^2 + 1) - \tfrac{X}{2}\cdot 2X = 1$. Over $\mathbb{Z}$ it is not:
  separability is preserved by every ring homomorphism, and modulo
  $2$ the polynomial becomes $(X + 1)^2$, which is not separable over $\mathbb{F}_2$.

## Properties

- **Base change over a field.** For a polynomial $f$ over a field $F$ and a
  [ring homomorphism](trough:RingHom) $F \to S$ into a nonzero commutative ring,
  the image of $f$ is separable if and only if $f$ is. In
  particular, enlarging the field does not change whether $f$ is separable.
- **Roots.** Over an integral domain,
  a separable polynomial has no repeated roots in that domain. If a separable
  polynomial over $F$ splits over an extension field $K$, then
  its number of distinct roots in $K$ equals its degree.
- **Factors.** A divisor of a separable polynomial is separable,
  and if $fg$ is separable then $f$ and $g$ are coprime.
  Conversely, over a commutative ring,
  the product of two coprime separable polynomials is separable.
- **Characteristic zero.** A nonconstant polynomial has nonzero derivative in characteristic zero,
  so every irreducible polynomial over a field of characteristic zero is separable.
- **Characteristic $p$.** Here $f' = 0$ exactly when $f$ is a polynomial in $X^p$. Over a field of
  characteristic $p > 0$,
  every irreducible $f$ can be written as $f(X) = g(X^{p^n})$ with $n \ge 0$ and $g$ separable,
  and $n$ and $g$ are uniquely determined by $f$.

## Related concepts

- **Separable elements and extensions.** For an algebra over $F$,
  an element is separable when its minimal polynomial over $F$ is separable
  (see [minimal polynomial](trough:minpoly)), and
  the algebra is separable over $F$ when all of its elements are. By the
  primitive element theorem,
  every finite separable field extension is generated by a single element.
  Galois extensions are the separable normal ones, the setting of the
  [Galois correspondence](trough:IsGalois.intermediateFieldEquivSubgroup).
- **Perfect fields.** A field is perfect when every irreducible polynomial over it is separable;
  in characteristic $p$ this amounts to surjectivity of the [Frobenius](trough:frobenius) map.
  Every field of characteristic zero is perfect, as is
  every finite field, while $\mathbb{F}_p(t)$ is not, by the example
  above. Over a perfect field a polynomial is separable if and only if it is squarefree,
  and every algebraic extension of a perfect field is separable.
  See also [perfect closure](trough:PerfectClosure).

## In Mathlib

Mathlib defines separability for polynomials over any commutative semiring, directly as Bézout
coprimality of the polynomial and its formal derivative; roots play no part in the definition, and
the description by distinct roots over a field is a theorem. The definition fixes the edge cases:
the zero polynomial is not separable over a nonzero ring, nonzero constants over a field are
separable because they are units, and over the zero ring every polynomial is separable. It is the
strict notion, under which a polynomial with a repeated irreducible factor, such as $(X - 1)^2$, is
not separable; some texts instead call a polynomial separable when each of its irreducible factors
has distinct roots, and under that convention $(X - 1)^2$ would count as separable. Separable
elements are defined for algebras over a commutative ring through the minimal polynomial. Since
Mathlib gives a non-integral element the minimal polynomial $0$,
a separable element is automatically integral, and separable
extensions are algebraic.

## Depends on

- [Polynomial in one indeterminate](trough:Polynomial)
- [Polynomial derivative](trough:Polynomial.derivative)
- [Coprime element](trough:IsCoprime)
- [Roots of a polynomial](trough:Polynomial.roots)
