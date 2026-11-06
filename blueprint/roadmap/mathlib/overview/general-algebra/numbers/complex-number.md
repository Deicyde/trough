# Complex number

A **complex number** is an expression $a + bi$ in which $a$ and $b$ are
[real numbers](real-number.md) and $i$ is a number whose square is $-1$. The complex
numbers form a [field](../field-theory/field.md), written $\mathbb{C}$, that contains the real
numbers and in which every nonconstant polynomial equation has a solution. This makes
$\mathbb{C}$ the natural setting for algebra, for the theory of analytic functions,
and for much of number theory, geometry and physics.

## Definition

A [complex number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex) is an ordered pair $z = (a, b)$ of real numbers,
called its real part $a = \operatorname{Re} z$ and its imaginary part
$b = \operatorname{Im} z$. Two complex numbers
[are equal when their real parts agree and their imaginary parts agree](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.ext).
Addition is componentwise, and multiplication is defined by

$$(a, b)(c, d) = (ac - bd,\ ad + bc).$$

The real part of a product is [$ac - bd$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.mul_re) and its imaginary part is
[$ad + bc$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.mul_im). A real number $r$ is identified with the pair $(r, 0)$;
this identification
[is injective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.ofReal_injective) and respects addition and
multiplication, so $\mathbb{R}$ sits inside $\mathbb{C}$. The
[imaginary unit](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.I) is $i = (0, 1)$, and the multiplication rule gives
[$i^2 = -1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.I_sq). Every complex number can then be written
[as $z = a + bi$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.re_add_im) with $a = \operatorname{Re} z$ and
$b = \operatorname{Im} z$, and products are computed by expanding and replacing
$i^2$ by $-1$.

With these operations $\mathbb{C}$ is
[a field](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.instField) (see [the field of complex numbers](../../../undergraduate/ring-theory/field-theory/field-c-of-complex-numbers.md)).
The inverse of a nonzero $z = a + bi$ is

$$z^{-1} = \frac{a - bi}{a^2 + b^2}.$$

## Conjugate and absolute value

The **complex conjugate** of $z = a + bi$ is $\bar z = a - bi$: it
[has the same real part](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.conj_re) and
[the negated imaginary part](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.conj_im). Conjugation preserves sums and
products, and [$\bar z = z$ exactly when $z$ is real](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.conj_eq_iff_real).
The product of a number and its conjugate is
the real number [$z \bar z = a^2 + b^2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.mul_conj), which is positive unless $z = 0$.

The **absolute value** (or modulus) $|z|$ is the nonnegative square root of
$a^2 + b^2$, so that [$|z|^2 = a^2 + b^2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Norm.html#Complex.sq_norm). It is the distance
from $0$ to the point $(a, b)$ in the plane. It is multiplicative,
[$|zw| = |z|\,|w|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Norm.html#Complex.norm_mul), and satisfies the
[triangle inequality $|z + w| \le |z| + |w|$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Norm.html#Complex.norm_add_le').
The distance $|z - w|$ makes $\mathbb{C}$ a complete
[metric space](../../topology/metric-spaces/metric-space.md), isometric to the Euclidean plane.

## Examples

- $(1 + 2i)(3 - i) = 3 - i + 6i - 2i^2 = 5 + 5i$.
- $\dfrac{1}{1 + i} = \dfrac{1 - i}{2}$, since $(1 + i)(1 - i) = 2$.
- The equation $z^2 = -1$ has the two solutions $i$ and $-i$, and $|i| = 1$.
- $|3 + 4i| = 5$, so multiplying by $3 + 4i$ scales lengths in the plane by $5$.

## Properties

- **Dimension over the reals.** As a vector space over $\mathbb{R}$, $\mathbb{C}$
  has basis $1, i$, so
  [its dimension is $2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Complex/FiniteDimensional.html#Complex.finrank_real_complex).
- **Algebraic closure.** By the
  [fundamental theorem of algebra](../../analysis/complex-analysis/fundamental-theorem-of-algebra.md),
  [every polynomial of positive degree with complex coefficients has a complex root](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/Basic.html#Complex.exists_root);
  equivalently, [$\mathbb{C}$ is algebraically closed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/Basic.html#Complex.isAlgClosed)
  (see [algebraically closed field](../field-theory/algebraically-closed-field.md)). Every nonconstant complex
  [polynomial](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) therefore factors as a constant times a product of
  linear factors.
- **Characteristic zero.** $\mathbb{C}$
  [has characteristic zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.instCharZero) (see
  [characteristic zero](../field-theory/characteristic-zero.md)), since it contains $\mathbb{R}$.
- **No field ordering.** In any ordered field squares are nonnegative, so
  $1 = 1^2 > 0$ and $-1 = i^2 \ge 0$ would contradict each other. Hence $\mathbb{C}$
  admits no ordering compatible with its field operations.
- **Automorphisms.** The only ring homomorphisms from $\mathbb{C}$ to itself that fix
  every real number, that is, the
  [$\mathbb{R}$-algebra homomorphisms, are the identity and conjugation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Complex/Module.html#Complex.real_algHom_eq_id_or_conj).
  The same two maps are
  [the only continuous ring homomorphisms from $\mathbb{C}$ to itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Basic.html#Complex.ringHom_eq_id_or_conj_of_continuous).

## Polar form and the exponential

The [complex exponential](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/complex-exponential.md) satisfies
[$e^{z + w} = e^z e^w$ for all complex $z$ and $w$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Exponential.html#Complex.exp_add) and Euler's formula
[$e^{ix} = \cos x + i \sin x$ for every complex $x$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Trigonometric.html#Complex.exp_mul_I). For real $x$
the number $e^{ix}$ [has absolute value $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Trigonometric.html#Complex.norm_exp_ofReal_mul_I), and
taking $x = \pi$ gives [$e^{i\pi} = -1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Basic.html#Complex.exp_pi_mul_I).

Every complex number has a polar form
[$z = |z|\,e^{i \arg z}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/Arg.html#Complex.norm_mul_exp_arg_mul_I), where the
[argument](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/Arg.html#Complex.arg) $\arg z$ of a nonzero $z$ is the angle, taken in
$(-\pi, \pi]$, from the positive real axis to the point $z$. For $z = 0$ there is no
such angle; the argument is [taken to be $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Complex/Arg.html#Complex.arg_zero), and the polar form
holds trivially. In polar form multiplication multiplies absolute values and adds
arguments up to a multiple of $2\pi$, so for real $x$ raising $\cos x + i \sin x$ to
the $n$-th power multiplies its argument by $n$. Combining Euler's formula with the
addition law for the exponential, $(\cos x + i \sin x)^n = (e^{ix})^n = e^{inx}$, gives
[De Moivre's formula](../../../hundred-theorems/part-01/de-moivres-formula.md)
[$(\cos x + i \sin x)^n = \cos nx + i \sin nx$ for every complex $x$ and natural number $n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Trigonometric.html#Complex.cos_add_sin_mul_I_pow).
For $n \ge 1$ the $n$-th [roots of unity](../../../undergraduate/group-theory/abelian-group/complex-roots-of-unity.md) are
[the numbers $e^{2\pi i k/n}$ with $0 \le k < n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.mem_rootsOfUnity), and
[there are exactly $n$ of them](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/RootsOfUnity/Complex.html#Complex.card_rootsOfUnity).

## Related concepts

The complex numbers are the degree-$2$ extension of $\mathbb{R}$ obtained by adjoining a
root of $x^2 + 1$. Applying the same pair construction to complex numbers, with a
suitably twisted multiplication, gives the quaternions, a
noncommutative division ring of dimension $4$ over $\mathbb{R}$. Complex
[inner product spaces](../../analysis/hilbert-spaces/inner-product-space-over-r-or-c.md) and the complex
[sine](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/sin.md) and [cosine](../../../undergraduate/single-variable-complex-analysis/complex-valued-series/extension-of-trigonometric-functions-to-the-comp/cos.md) functions are built on
$\mathbb{C}$, and analysis of functions of a complex variable is the subject of complex
analysis.

## In Mathlib

Mathlib defines a complex number as a structure with two real fields, its real and
imaginary parts, and builds the field operations on top of this pair. The real numbers
enter through a coercion that sends $r$ to $(r, 0)$. Division follows Mathlib's general
convention that the inverse of $0$ is $0$, so
[the formula $z^{-1} = \bar z / (a^2 + b^2)$ holds for every $z$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.inv_def),
zero included. The absolute value is the norm of $\mathbb{C}$, and the squared modulus
$a^2 + b^2$ is also available as a separate function,
[defined as $(\operatorname{Re} z)^2 + (\operatorname{Im} z)^2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex.normSq_apply),
that is multiplicative and avoids square roots. Conjugation is the star operation of
$\mathbb{C}$ as a star ring. Mathlib also provides
[a partial order on $\mathbb{C}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Order.html#Complex.partialOrder), in which $z \le w$ means
that $w - z$ is a nonnegative real number; it is available only on request and is not
a field ordering, since numbers with different imaginary parts are incomparable.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Real number](real-number.md)
- [Field](../field-theory/field.md)

## Sources

- [Mathlib documentation: `Complex`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Basic/Complex/Basic.html#Complex)
- [Source of `Complex` in Mathlib/Basic/Complex/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Basic/Complex/Basic.lean#L33)
- [Mathlib overview: General algebra › Numbers](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L27)
