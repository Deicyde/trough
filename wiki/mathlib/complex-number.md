A **complex number** is an expression $a + bi$ in which $a$ and $b$ are
[real numbers](trough:Real) and $i$ is a number whose square is $-1$. The complex
numbers form a [field](trough:Field), written $\mathbb{C}$, that contains the real
numbers and in which every nonconstant polynomial equation has a solution. This makes
$\mathbb{C}$ the natural setting for algebra, for the theory of analytic functions,
and for much of number theory, geometry and physics.

## Definition

A complex number is an ordered pair $z = (a, b)$ of real numbers,
called its real part $a = \operatorname{Re} z$ and its imaginary part
$b = \operatorname{Im} z$. Two complex numbers
are equal when their real parts agree and their imaginary parts agree.
Addition is componentwise, and multiplication is defined by

$$(a, b)(c, d) = (ac - bd,\ ad + bc).$$

The real part of a product is $ac - bd$ and its imaginary part is
$ad + bc$. A real number $r$ is identified with the pair $(r, 0)$;
this identification
is injective and respects addition and
multiplication, so $\mathbb{R}$ sits inside $\mathbb{C}$. The
imaginary unit is $i = (0, 1)$, and the multiplication rule gives
$i^2 = -1$. Every complex number can then be written
as $z = a + bi$ with $a = \operatorname{Re} z$ and
$b = \operatorname{Im} z$, and products are computed by expanding and replacing
$i^2$ by $-1$.

With these operations $\mathbb{C}$ is
a field (see [the field of complex numbers](trough:Complex.instField)).
The inverse of a nonzero $z = a + bi$ is

$$z^{-1} = \frac{a - bi}{a^2 + b^2}.$$

## Conjugate and absolute value

The **complex conjugate** of $z = a + bi$ is $\bar z = a - bi$: it
has the same real part and
the negated imaginary part. Conjugation preserves sums and
products, and $\bar z = z$ exactly when $z$ is real.
The product of a number and its conjugate is
the real number $z \bar z = a^2 + b^2$, which is positive unless $z = 0$.

The **absolute value** (or modulus) $|z|$ is the nonnegative square root of
$a^2 + b^2$, so that $|z|^2 = a^2 + b^2$. It is the distance
from $0$ to the point $(a, b)$ in the plane. It is multiplicative,
$|zw| = |z|\,|w|$, and satisfies the
triangle inequality $|z + w| \le |z| + |w|$.
The distance $|z - w|$ makes $\mathbb{C}$ a complete
[metric space](trough:MetricSpace), isometric to the Euclidean plane.

## Examples

- $(1 + 2i)(3 - i) = 3 - i + 6i - 2i^2 = 5 + 5i$.
- $\dfrac{1}{1 + i} = \dfrac{1 - i}{2}$, since $(1 + i)(1 - i) = 2$.
- The equation $z^2 = -1$ has the two solutions $i$ and $-i$, and $|i| = 1$.
- $|3 + 4i| = 5$, so multiplying by $3 + 4i$ scales lengths in the plane by $5$.

## Properties

- **Dimension over the reals.** As a vector space over $\mathbb{R}$, $\mathbb{C}$
  has basis $1, i$, so
  its dimension is $2$.
- **Algebraic closure.** By the
  [fundamental theorem of algebra](trough:Complex.isAlgClosed),
  every polynomial of positive degree with complex coefficients has a complex root;
  equivalently, $\mathbb{C}$ is algebraically closed
  (see [algebraically closed field](trough:IsAlgClosed)). Every nonconstant complex
  [polynomial](trough:Polynomial) therefore factors as a constant times a product of
  linear factors.
- **Characteristic zero.** $\mathbb{C}$
  has characteristic zero (see
  [characteristic zero](trough:CharZero)), since it contains $\mathbb{R}$.
- **No field ordering.** In any ordered field squares are nonnegative, so
  $1 = 1^2 > 0$ and $-1 = i^2 \ge 0$ would contradict each other. Hence $\mathbb{C}$
  admits no ordering compatible with its field operations.
- **Automorphisms.** The only ring homomorphisms from $\mathbb{C}$ to itself that fix
  every real number, that is, the
  $\mathbb{R}$-algebra homomorphisms, are the identity and conjugation.
  The same two maps are
  the only continuous ring homomorphisms from $\mathbb{C}$ to itself.

## Polar form and the exponential

The [complex exponential](trough:Complex.exp) satisfies
$e^{z + w} = e^z e^w$ for all complex $z$ and $w$ and Euler's formula
$e^{ix} = \cos x + i \sin x$ for every complex $x$. For real $x$
the number $e^{ix}$ has absolute value $1$, and
taking $x = \pi$ gives $e^{i\pi} = -1$.

Every complex number has a polar form
$z = |z|\,e^{i \arg z}$, where the
argument $\arg z$ of a nonzero $z$ is the angle, taken in
$(-\pi, \pi]$, from the positive real axis to the point $z$. For $z = 0$ there is no
such angle; the argument is taken to be $0$, and the polar form
holds trivially. In polar form multiplication multiplies absolute values and adds
arguments up to a multiple of $2\pi$, so for real $x$ raising $\cos x + i \sin x$ to
the $n$-th power multiplies its argument by $n$. Combining Euler's formula with the
addition law for the exponential, $(\cos x + i \sin x)^n = (e^{ix})^n = e^{inx}$, gives
[De Moivre's formula](trough:Complex.cos_add_sin_mul_I_pow)
$(\cos x + i \sin x)^n = \cos nx + i \sin nx$ for every complex $x$ and natural number $n$.
For $n \ge 1$ the $n$-th [roots of unity](trough:Complex.mem_rootsOfUnity) are
the numbers $e^{2\pi i k/n}$ with $0 \le k < n$, and
there are exactly $n$ of them.

## Related concepts

The complex numbers are the degree-$2$ extension of $\mathbb{R}$ obtained by adjoining a
root of $x^2 + 1$. Applying the same pair construction to complex numbers, with a
suitably twisted multiplication, gives the quaternions, a
noncommutative division ring of dimension $4$ over $\mathbb{R}$. Complex
[inner product spaces](trough:InnerProductSpace) and the complex
[sine](trough:Complex.sin) and [cosine](trough:Complex.cos) functions are built on
$\mathbb{C}$, and analysis of functions of a complex variable is the subject of complex
analysis.

## In Mathlib

Mathlib defines a complex number as a structure with two real fields, its real and
imaginary parts, and builds the field operations on top of this pair. The real numbers
enter through a coercion that sends $r$ to $(r, 0)$. Division follows Mathlib's general
convention that the inverse of $0$ is $0$, so
the formula $z^{-1} = \bar z / (a^2 + b^2)$ holds for every $z$,
zero included. The absolute value is the norm of $\mathbb{C}$, and the squared modulus
$a^2 + b^2$ is also available as a separate function,
defined as $(\operatorname{Re} z)^2 + (\operatorname{Im} z)^2$,
that is multiplicative and avoids square roots. Conjugation is the star operation of
$\mathbb{C}$ as a star ring. Mathlib also provides
a partial order on $\mathbb{C}$, in which $z \le w$ means
that $w - z$ is a nonnegative real number; it is available only on request and is not
a field ordering, since numbers with different imaginary parts are incomparable.

## Depends on

- [Real number](trough:Real)
- [Field](trough:Field)
