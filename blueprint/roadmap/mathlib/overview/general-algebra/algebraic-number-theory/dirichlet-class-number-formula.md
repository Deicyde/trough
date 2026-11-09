# Dirichlet class number formula

The **Dirichlet class number formula**, also called the analytic class number
formula, expresses the behaviour of the Dedekind zeta function of a number field
near $s = 1$ in terms of the field's basic arithmetic invariants: its class
number, regulator, number of roots of unity, discriminant and numbers of real and
complex places. It ties an analytic quantity to algebraic ones, and is the main
route by which the class number, which is defined algebraically, can be computed
or estimated with analysis. Through it, the positivity of these invariants yields
the nonvanishing of Dirichlet $L$-functions at $s = 1$, the key input to
[Dirichlet's theorem](../../../hundred-theorems/part-02/dirichlets-theorem.md) on primes in
arithmetic progressions.

## Statement

Let $K$ be a number field of degree $n$ over $\mathbb{Q}$ with ring of integers
$\mathcal{O}_K$. The norm of a nonzero [ideal](../ideals-and-quotients/ideal-of-a-commutative-ring.md) $I$ of $\mathcal{O}_K$ is the
size of the finite quotient ring $\mathcal{O}_K / I$. The
[Dedekind zeta function of $K$ is the Dirichlet series $\zeta_K(s) = \sum_{m \ge 1} a_m m^{-s}$, where $a_m$ is the number of ideals of $\mathcal{O}_K$ of norm $m$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.dedekindZeta).
It converges for complex $s$ with real part greater than $1$; for $K = \mathbb{Q}$ it
agrees there with the Riemann zeta function.

The formula involves the following invariants of $K$.

- $r_1$ is the number of real places and $r_2$ the number of complex places of
  $K$. Each field embedding $\sigma : K \to \mathbb{C}$ defines an absolute value
  $|x|_v = |\sigma(x)|$ on $K$, and an infinite place $v$ is an absolute value
  arising in this way. An embedding and its complex conjugate give the same place;
  the place is real when $\sigma$ maps $K$ into $\mathbb{R}$ and complex otherwise, so
  complex places correspond to pairs of conjugate non-real embeddings and
  [$r_1 + 2r_2 = n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/InfinitePlace/Basic.html#NumberField.InfinitePlace.card_add_two_mul_card_eq_rank).
- $h_K$ is the [class number](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/ClassNumber.html#NumberField.classNumber), the order of the ideal
  class group, which is [finite](finiteness-of-the-class-number.md);
  [$h_K = 1$ exactly when $\mathcal{O}_K$ is a principal ideal domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/ClassNumber.html#NumberField.classNumber_eq_one_iff).
- $R_K$ is the regulator. By the
  [Dirichlet unit theorem](dirichlet-unit-theorem.md), there
  are units $\varepsilon_1, \dots, \varepsilon_r$ of $\mathcal{O}_K$, where
  $r = r_1 + r_2 - 1$, such that every unit is uniquely a root of unity times a
  product $\varepsilon_1^{k_1} \cdots \varepsilon_r^{k_r}$ with integer exponents; these
  form a system of fundamental units. Fix one infinite place $v_0$. Then $R_K$ is
  the absolute value of the determinant of the $r \times r$ matrix with entries
  $n_v \log |\varepsilon_i|_v$, where $v$ runs over the infinite places other than
  $v_0$, and $n_v$ is $1$ for a real place and $2$ for a complex place. The value
  depends neither on the system of fundamental units nor on the choice of $v_0$.
- $w_K$ is [the number of roots of unity in $K$, that is, the order of the torsion subgroup of the unit group of $\mathcal{O}_K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Basic.html#NumberField.Units.torsionOrder).
- $d_K$ is the [discriminant of $K$, the discriminant of an integral basis of $\mathcal{O}_K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Discriminant/Defs.html#NumberField.discr).

With these, [$(s - 1)\zeta_K(s)$ tends to the following constant as the real number $s$ decreases to $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT):

$$\lim_{s \to 1^+} (s - 1)\,\zeta_K(s) = \frac{2^{r_1} (2\pi)^{r_2}\, h_K\, R_K}{w_K \sqrt{|d_K|}}.$$

[The constant on the right-hand side](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.dedekindZeta_residue) is
[strictly positive](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.dedekindZeta_residue_pos), so $\zeta_K(s)$
tends to infinity as $s \to 1^+$.

## Examples

- **The rational numbers.** Here $r_1 = 1$, $r_2 = 0$, $h_K = 1$, $R_K = 1$,
  $w_K = 2$ and $d_K = 1$, so the right-hand side is $1$. This matches the fact that
  the Riemann zeta function satisfies
  [$(s - 1)\zeta(s) \to 1$ as $s \to 1$ in the complex plane](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/RiemannZeta.html#riemannZeta_residue_one).
- **Quadratic fields.** If $K$ is quadratic with discriminant $d = d_K$, then
  $\zeta_K(s) = \zeta(s)\,L(s, \chi_d)$. Here, for a Dirichlet character $\chi$, the
  Dirichlet $L$-function is $L(s, \chi) = \sum_{m \ge 1} \chi(m) m^{-s}$, and
  $\chi_d(m)$ is the Kronecker symbol $(d/m)$, a character modulo $|d|$. Comparing
  limits at $s = 1$ gives, for $d < 0$ (where $r_2 = 1$ and $R_K = 1$),
  $$h_K = \frac{w_K \sqrt{|d|}}{2\pi}\, L(1, \chi_d),$$
  and, for $d > 0$ (where $r_1 = 2$ and $R_K = \log \varepsilon$ for the fundamental unit $\varepsilon > 1$),
  $$h_K = \frac{\sqrt{d}}{2 \log \varepsilon}\, L(1, \chi_d).$$
- **Gaussian rationals.** For $K = \mathbb{Q}(i)$ one has $d_K = -4$, $w_K = 4$ and
  $h_K = 1$, so $L(1, \chi_{-4}) = 1 - \tfrac13 + \tfrac15 - \tfrac17 + \cdots = \pi/4$,
  the Leibniz series.
- **The field $\mathbb{Q}(\sqrt2)$.** Here $d_K = 8$, $h_K = 1$ and
  $\varepsilon = 1 + \sqrt2$, which gives
  $1 - \tfrac13 - \tfrac15 + \tfrac17 + \tfrac19 - \cdots = \log(1 + \sqrt2)/\sqrt2$.

## Proof

The argument has a counting part and an analytic part.

**Counting ideals.** The ideal class group is the group of nonzero
[fractional ideals](../ideals-and-quotients/fractional-ideal.md) of $\mathcal{O}_K$ modulo the principal
ones, so each class contains integral ideals. Fix an ideal class $C$ and an
integral ideal $J$ in the inverse class. Multiplication by $J$ matches the
integral ideals $I$ in $C$ with the principal ideals $(\alpha)$ divisible by $J$,
and $|N(\alpha)| = N(I)\,N(J)$. Principal ideals correspond to nonzero elements of
$J$ up to multiplication by units. Embedding $K$ into
$\mathbb{R}^{r_1} \times \mathbb{C}^{r_2}$ turns $J$ into a lattice, and the unit
theorem provides a cone that is a fundamental domain for the action of the units
modulo roots of unity, so that each principal ideal has exactly $w_K$ generators
in the cone. Counting lattice points in the part of this cone where the norm is
at most $t$, a region that scales with $t$, and comparing with its volume shows
that
[the number of nonzero ideals in $C$ of norm at most $t$, divided by $t$, tends to $2^{r_1}(2\pi)^{r_2} R_K / (w_K \sqrt{|d_K|})$ as $t \to \infty$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Ideal/Asymptotics.html#NumberField.Ideal.tendsto_norm_le_and_mk_eq_div_atTop).
The limit does not depend on $C$, so ideals are equidistributed among the classes.
Summing over the $h_K$ classes,
[the number of nonzero ideals of norm at most $t$, divided by $t$, tends to the right-hand side of the formula](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Ideal/Asymptotics.html#NumberField.Ideal.tendsto_norm_le_div_atTop%E2%82%80).

**From counting to the zeta function.** Partial summation writes a Dirichlet
series with partial sums $A(t) = \sum_{m \le t} a_m$ as
$\sum a_m m^{-s} = s \int_1^\infty A(t)\, t^{-s-1}\, dt$ for real $s > 1$. If $A(t)$
is close to $\ell t$, the integral is close to $\ell s / (s - 1)$. This gives the
general fact that
[if the coefficients are nonnegative real numbers and $(a_1 + \cdots + a_m)/m \to \ell$ as $m \to \infty$, then $(s - 1)\sum a_m m^{-s} \to \ell$ as the real number $s$ decreases to $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/SumCoeff.html#LSeries_tendsto_sub_mul_nhds_one_of_tendsto_sum_div_and_nonneg).
Applied to the ideal counts, it yields the formula.

## Consequences and generalizations

- **Nonvanishing of $L(1, \chi)$.** The Dedekind zeta function of the cyclotomic
  field $\mathbb{Q}(\zeta_m)$ is, up to finitely many Euler factors, the product of the
  Dirichlet $L$-functions of the characters modulo $m$. The factor of the trivial
  character has a simple pole at $s = 1$, and the left-hand side has a finite
  positive limit after multiplying by $s - 1$. Since the other factors are
  analytic at $s = 1$, none of them can vanish there.
  This is the analytic heart of Dirichlet's theorem.
- **Class number computations.** The quadratic formulas above, combined with
  evaluations of $L(1, \chi_d)$ as finite sums, give a finite formula for the
  class number of an imaginary quadratic field, and for the product
  $h_K \log \varepsilon$ for a real quadratic field.
- **The point $s = 0$.** Through the functional equation of $\zeta_K$, the formula is
  equivalent to the statement that $\zeta_K$ has a zero of order $r_1 + r_2 - 1$ at
  $s = 0$ with leading coefficient $-h_K R_K / w_K$.

## In Mathlib

Mathlib states the formula for an arbitrary number field. It defines the Dedekind
zeta function only by its Dirichlet series, as a function of a complex variable,
following the library's convention that an $L$-series takes the value $0$ where
it does not converge absolutely; it does not construct the analytic continuation.
For this reason the formula is phrased as a one-sided limit of $(s - 1)\zeta_K(s)$
as the real number $s$ decreases to $1$, rather than as the residue of a
meromorphic function. The limiting value is a separate definition written out in
the six invariants above. The regulator is defined as
[the covolume of the lattice of logarithms of units](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Regulator.html#NumberField.Units.regulator).
Mathlib fixes one system of fundamental units, and
[for that system and any choice of the omitted place $v_0$, the regulator is the absolute value of the determinant described above](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/Units/Regulator.html#NumberField.Units.regulator_eq_det).
The class number is the cardinality of the class group, and $r_1$ and $r_2$ are
defined as numbers of infinite places.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Ideal of a commutative ring](../ideals-and-quotients/ideal-of-a-commutative-ring.md)
- [Finiteness of the class number](finiteness-of-the-class-number.md)
- [Dirichlet unit theorem](dirichlet-unit-theorem.md)
- [Determinant](../../linear-algebra/matrices/determinant.md)
- [Logarithm](../../analysis/special-functions/logarithm.md)
- [Limit of a map with respect to filters](../../topology/general-topology/part-01/limit-of-a-map-with-respect-to-filters.md)

## Proof depends on

- [Fractional ideal](../ideals-and-quotients/fractional-ideal.md)
- [Lebesgue measure (Measures and integral calculus)](../../analysis/measures-and-integral-calculus/part-01/lebesgue-measure.md)

## Sources

- [Mathlib documentation: `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/NumberField/DedekindZeta.html#NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT)
- [Source of `NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT` in Mathlib/NumberTheory/NumberField/DedekindZeta.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/NumberTheory/NumberField/DedekindZeta.lean#L75)
- [Mathlib overview: General algebra › Algebraic Number Theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L159)
