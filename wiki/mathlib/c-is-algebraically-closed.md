The statement that **$\mathbb{C}$ is algebraically closed**, usually called the
fundamental theorem of algebra, says that every nonconstant
[polynomial](trough:Polynomial) with [complex](trough:Complex) coefficients has a
complex root. It means that the complex numbers need no further enlargement to solve
polynomial equations: adjoining a square root of $-1$ to the real numbers already
produces a field in which every polynomial equation of positive degree has a
solution. The result underlies the factorization of real and complex polynomials,
the existence of eigenvalues in linear algebra, and much of algebraic geometry over
$\mathbb{C}$.

## Statement

Let $f(z) = a_n z^n + a_{n-1} z^{n-1} + \cdots + a_1 z + a_0$ be a polynomial with
complex coefficients and $a_n \neq 0$, where $n \ge 1$. Then
there is a complex number $z_0$ with $f(z_0) = 0$.

Applying this repeatedly, together with the fact that $z_0$ is a root of $f$ exactly
when $z - z_0$ divides $f$, splits off one linear factor at a time. Hence every
complex polynomial factors completely,

$$f(z) = a_n (z - z_1)(z - z_2) \cdots (z - z_n), \qquad z_1, \dots, z_n \in \mathbb{C},$$

which is to say that the field $\mathbb{C}$ is algebraically closed
in the sense of the article [algebraically closed field](trough:IsAlgClosed). That
formulation, as a property of the field, is treated in the article
[fundamental theorem of algebra](trough:Complex.isAlgClosed); this article concerns the
existence of a root for a single polynomial.

## Examples

- The polynomial $z^2 + 1$ has no real root but has the complex roots $i$ and $-i$.
- For every complex number $a$ and every integer $n \ge 1$, the polynomial $z^n - a$
  has a root, so every complex number has an $n$-th root;
  Mathlib proves this for any algebraically closed field. Writing
  $a = r e^{i\theta}$ with $r \ge 0$, one such root is $r^{1/n} e^{i\theta/n}$.
- A polynomial of degree $5$ with integer coefficients may have roots that cannot
  be written using radicals, but it still has five complex roots counted with
  multiplicity. The theorem asserts existence, not a formula.

## Proof

The proof in Mathlib uses complex analysis. Suppose that $f$ has positive degree and
no root. Then $g = 1/f$ is defined on all of $\mathbb{C}$, and it is complex
differentiable everywhere, because
polynomial functions are differentiable and $f$
never vanishes. Since $f$ has positive degree,
$|f(z)| \to \infty$ as $|z| \to \infty$, so
$g(z) \to 0$ as $|z| \to \infty$. A continuous function on $\mathbb{C}$ that tends
to $0$ at infinity is bounded. By [Liouville's theorem](trough:Differentiable.apply_eq_apply_of_bounded),
a bounded function that is complex differentiable on the whole plane is constant,
and a constant that tends to $0$ is $0$. But $g = 1/f$ never takes the value $0$, a
contradiction.

A second classical argument avoids Liouville's theorem. Since $|f(z)|$ grows without
bound, $|f|$ attains a minimum value at some point $z_0$ of $\mathbb{C}$.
If $f(z_0) \neq 0$, expand $f$ around $z_0$ as
$f(z_0 + w) = f(z_0) + c\,w^k + (\text{terms of degree} > k \text{ in } w)$ with
$c \neq 0$ and $k \ge 1$. Choosing $w$ small, with $c\,w^k$ pointing in the direction
opposite to $f(z_0)$, makes $|f(z_0 + w)| < |f(z_0)|$, contradicting minimality. So
$f(z_0) = 0$.

To pass from roots to algebraic closedness, it suffices that
every monic irreducible polynomial has a root,
and an irreducible polynomial has positive degree
(see [irreducible element](trough:Irreducible)), so the root statement applies to it.

## Consequences

- **Counting roots.** A nonzero complex polynomial of degree $n$
  has exactly $n$ roots, counted with multiplicity
  (see [roots of a polynomial](trough:Polynomial.roots) and
  [multiplicity](trough:Polynomial.rootMultiplicity)).
- **Real polynomials.** If $p$ has real coefficients, then
  $p(\bar z) = \overline{p(z)}$ for every complex $z$,
  so the non-real roots of $p$ come in conjugate pairs. For such a root $z$,
  the real quadratic $x^2 - 2\operatorname{Re}(z)\,x + |z|^2$ divides $p$.
  Consequently every irreducible real polynomial has degree at most $2$,
  and every nonconstant real polynomial is a product of real linear and quadratic factors.
- **Extensions of the reals.** The complex numbers form a
  vector space of dimension $2$ over $\mathbb{R}$, and
  every algebraic extension field of $\mathbb{R}$ is isomorphic, as an algebra over $\mathbb{R}$, to $\mathbb{R}$ or to $\mathbb{C}$
  (see [algebraic extension](trough:Algebra.IsAlgebraic)). Since
  an extension field is an algebraic closure of the base field exactly when it is algebraically closed and algebraic over it,
  and an extension of finite degree is algebraic, $\mathbb{C}$ is an algebraic closure of
  the [real numbers](trough:Real) (see also
  [existence of algebraic closure of a field](trough:AlgebraicClosure)).
- **Eigenvalues.** The characteristic polynomial of a linear map has a root, so
  every linear map from a nonzero finite-dimensional complex vector space to itself has an eigenvalue
  (see [eigenvalue](trough:Module.End.HasEigenvalue));
  Mathlib proves this over any algebraically closed field. This is the starting point
  for triangular and Jordan normal forms of complex matrices.

## In Mathlib

Mathlib states the theorem for a single polynomial: if its degree is positive, it has
a complex root. The degree of the zero polynomial is taken to be minus infinity
rather than a natural number, so the hypothesis of positive degree excludes exactly
the zero polynomial and the nonzero constants, and the root is expressed as a point
where the polynomial evaluates to zero. The statement that $\mathbb{C}$ is an
algebraically closed field is recorded separately, derived from the root statement
through the criterion on monic irreducible polynomials. Through it, every general
theorem about algebraically closed fields, such as root counting and the existence of
eigenvalues, applies to the complex numbers. The proof applies a corollary of Liouville's
theorem, for differentiable functions that tend to a limit at infinity, directly to
$1/f$, so the boundedness step of the sketch above stays implicit. Mathlib proves
Liouville's theorem for complex differentiable maps between complex normed
spaces, not only for functions from $\mathbb{C}$ to $\mathbb{C}$, and it proves the
growth of polynomials at infinity over any normed ring whose norm is multiplicative.

## Depends on

- [Complex number](trough:Complex)
- [Polynomial in one indeterminate](trough:Polynomial)
- [Polynomial functions](trough:Polynomial.eval)
- [Algebraically closed field](trough:IsAlgClosed)

## Proof depends on

- [Differentiable functions](trough:Differentiable)
- [Liouville theorem](trough:Differentiable.apply_eq_apply_of_bounded)
- [Irreducible element](trough:Irreducible)
