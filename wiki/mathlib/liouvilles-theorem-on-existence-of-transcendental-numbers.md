**Liouville's theorem on existence of transcendental numbers** says that explicit
real numbers such as
$$\sum_{k=1}^{\infty} 10^{-k!} = 0.110001000000000000000001000\ldots$$
are [transcendental](trough:Transcendental): they are not roots of any nonzero
[polynomial](trough:Polynomial) with integer coefficients. The theorem names
specific transcendental numbers instead of only proving that some exist. The
method behind it is a lower bound on how well an algebraic number can be
approximated by fractions: a number that has rational approximations too good for
any algebraic number must be transcendental.

## Statement

Fix an integer $m \ge 2$ and put
$$L_m = \sum_{k=0}^{\infty} \frac{1}{m^{k!}}.$$
The series converges because its terms are dominated by those of a
[geometric series](trough:tsum_geometric_of_norm_lt_one). The theorem states that
$L_m$ is transcendental for every integer $m \ge 2$,
meaning that no nonzero polynomial with integer coefficients vanishes at $L_m$.
Since $0! = 1! = 1$, the term $1/m$ occurs twice in this sum. Removing one copy
gives the more common form $\sum_{k \ge 1} m^{-k!}$, which differs from $L_m$ by the
rational number $1/m$ and is therefore transcendental as well; for $m = 10$ it is the
decimal number displayed above.

The theorem is a special case of a general criterion. A real number $x$ is a
**Liouville number** if for every natural number $n$ there are integers $a$ and $b$
with $b > 1$ and
$$0 < \left| x - \frac{a}{b} \right| < \frac{1}{b^n}$$
(the definition). [Liouville's
criterion](trough:Liouville.transcendental) states that
every Liouville number is transcendental. The
number $L_m$ meets the definition, so
$L_m$ is a Liouville number, and the theorem
follows.

## Proof

**$L_m$ is a Liouville number.** Fix $n$ and split $L_m$ after the term with index
$n$. Every $k!$ with $k \le n$ divides $n!$, so
the partial sum is a fraction $a/b$ with denominator $b = m^{n!}$,
and $b > 1$. The tail is positive, and comparing it with a geometric series shows
that it is less than $2/m^{(n+1)!}$. Since $(n+1)! = n!\,(n+1)$, this bound equals
$2/b^{n+1}$, which is at most $1/b^n$ because $b \ge 2$. So
the tail is less than $1/b^n$, and
$0 < |L_m - a/b| < 1/b^n$.

**Liouville numbers are transcendental.** Let $x$ be a Liouville number. First,
$x$ is irrational: if $x = p/q$ with $q \ge 1$, then
every fraction $a/b \neq x$ with $b \ge 2$ satisfies $|x - a/b| \ge 1/(qb)$, and for
$n$ with $2^{n-1} \ge q$ this is at least $1/b^n$, against the definition. Now suppose $x$ is a root of a nonzero integer
polynomial $f$ of degree $d$. The key estimate is that
there is a constant $A > 0$ with $|x - a/q| \ge 1/(A\,q^d)$ for all integers $a$ and $q \ge 1$.
For $a/q$ near $x$ this comes from two facts. The number $q^d f(a/q)$ is an integer;
since $f$ has only finitely many roots, it is nonzero for $a/q$ close enough to $x$
but different from $x$, so $|f(a/q)| \ge q^{-d}$. On the other hand, the
[mean value theorem](trough:exists_deriv_eq_slope), in its inequality form, gives
$|f(a/q)| = |f(x) - f(a/q)| \le M\,|x - a/q|$, where $M$ bounds $|f'|$ near $x$.
Fractions far from $x$ are covered by enlarging $A$. Finally choose $n \ge d$ with
$2^{\,n-d} > A$. The Liouville property provides $a/b$ with $b \ge 2$ and
$|x - a/b| < b^{-n} \le b^{-d}/2^{\,n-d} < 1/(A\,b^d)$, contradicting the estimate.

## Related results

- **Abundance of transcendental numbers.**
  The real numbers algebraic over the integers form a countable set;
  Mathlib proves this for any countable integral domain of coefficients and any
  integral domain that is a torsion-free algebra over it. Since
  the real numbers are uncountable
  (see [uncountability of the continuum](trough:Cardinal.not_countable_real)), all
  but countably many real numbers are transcendental. This argument shows that
  transcendental numbers exist but names none; the construction of $L_m$ names them.
- **Size of the set of Liouville numbers.** In the sense of Baire category the Liouville
  numbers are plentiful: they form a dense subset of the real line,
  and the set of Liouville numbers is residual,
  so its complement is meagre. In the sense of measure they are scarce:
  the set of Liouville numbers has Lebesgue measure zero.
  As the algebraic numbers are countable, almost every real number is transcendental
  but not a Liouville number, so Liouville's criterion detects only a small part of
  the transcendental numbers.
- **Approximation exponents.** A real number $x$ is Liouville with exponent $p$ if
  there is a constant $C$ such that $0 < |x - a/b| < C/b^p$ for infinitely many
  denominators $b$. The estimate in the proof shows that an irrational algebraic
  number of degree $d$ is not Liouville with any exponent above $d$, and
  a real number is Liouville with every exponent exactly when it is a Liouville number.
  Roth's theorem, which Mathlib does not contain, sharpens the bound $d$ to $2$ for
  every irrational algebraic number.

## In Mathlib

Mathlib defines the number for every real argument $m$ as the sum of the terms
$1/m^{k!}$ over all natural numbers $k$, starting at $k = 0$; when the series
diverges, Mathlib's convention for infinite sums assigns it the value $0$. The
transcendence theorem is stated only for natural numbers $m \ge 2$, viewed as real
numbers. Transcendence is taken over the integers, which for a real number is the
same as transcendence over the rationals, since clearing denominators turns a
rational polynomial into an integer one. The definition of a Liouville number
requires $x \neq a/b$ in place of the strict lower bound $0 < |x - a/b|$, an
equivalent condition.

## Depends on

- [Transcendental elements](trough:Transcendental)
- [Polynomial in one indeterminate](trough:Polynomial)
- [Real number](trough:Real)
- [Infinite sum](trough:HasSum)

## Proof depends on

- [Liouville’s Theorem and the Construction of Transcendental Numbers](trough:Liouville.transcendental)
- [The Mean Value Theorem](trough:exists_deriv_eq_slope)
- [Geometric series](trough:tsum_geometric_of_norm_lt_one)
