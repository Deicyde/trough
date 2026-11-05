---
article_id: af_1d2c3e9fdbc5a193ec465fd0
concept: Polynomial.irreducible_of_eisenstein_criterion
---

**Eisenstein's criterion** is a sufficient condition for a [polynomial](trough:Polynomial) to be
[irreducible](trough:Irreducible), read off from its coefficients alone. In its best-known form it
says that an integer polynomial whose leading coefficient is not divisible by a prime $p$, whose
other coefficients are all divisible by $p$, and whose constant term is not divisible by $p^2$,
cannot be factored into polynomials of lower degree with rational coefficients. Irreducibility is
hard to decide in general, and the criterion produces irreducible polynomials of every degree with
almost no work; it is the standard tool for showing that cyclotomic polynomials of prime index and
polynomials such as $x^n - 2$ are irreducible.

## Statement

Let $R$ be an integral domain, let $P$ be a [prime ideal](trough:Ideal.IsPrime) of $R$, and let

$$f = a_n x^n + a_{n-1} x^{n-1} + \cdots + a_1 x + a_0 \in R[x]$$

have degree $n \ge 1$. Suppose that $f$ is
[primitive](lean:Polynomial.IsPrimitive), meaning that the only constant polynomials dividing $f$
are units of $R$. If

- the leading coefficient $a_n$ does not lie in $P$,
- the coefficients $a_0, a_1, \dots, a_{n-1}$ all lie in $P$, and
- the constant term $a_0$ does not lie in $P^2$,

then [$f$ is irreducible in $R[x]$](lean:Polynomial.irreducible_of_eisenstein_criterion). A
polynomial satisfying the three coefficient conditions is said to be
[Eisenstein at $P$](lean:Polynomial.IsEisensteinAt).

For $R = \mathbb{Z}$ and $P = (p)$ with $p$ a prime number, the conditions read $p \nmid a_n$,
$p \mid a_i$ for $i < n$, and $p^2 \nmid a_0$. Primitivity is automatic for a
[monic polynomial](lean:Polynomial.Monic.isPrimitive), and in general it is needed only for
irreducibility in $R[x]$ itself: when $R$ is a GCD domain such as $\mathbb{Z}$, it can be dropped
for irreducibility over the field of fractions (see below). Over an arbitrary integral domain the
coefficient conditions do not guarantee irreducibility over the field of fractions: in
$k[t^2, t^3][x]$, with $k$ a field, the monic polynomial $x^2 - t^2$ is Eisenstein at the prime
ideal $(t^2, t^3)$, because $t^2$ does not lie in $(t^2, t^3)^2 = (t^4, t^5, t^6)$, yet over $k(t)$
it equals $(x - t)(x + t)$.

## Examples

- **Pure powers.** For a prime $p$ and $n \ge 1$, the polynomial $x^n - p$ is monic and Eisenstein
  at $p$, so it is irreducible over $\mathbb{Z}$, and hence over $\mathbb{Q}$. In particular
  $\mathbb{Q}[x]$ has irreducible polynomials of every degree.
- **Cyclotomic polynomials of prime index.** For a prime $p$, the [cyclotomic
  polynomial](trough:Polynomial.cyclotomic) $\Phi_p(x) = x^{p-1} + \cdots + x + 1$ is not itself
  Eisenstein, but after the substitution $x \mapsto x + 1$,
  $$\Phi_p(x+1) = \frac{(x+1)^p - 1}{x} = \sum_{k=1}^{p} \binom{p}{k} x^{k-1}.$$
  Its leading coefficient is $1$, the binomial coefficients $\binom{p}{k}$ with $1 \le k \le p-1$
  are divisible by $p$, and the constant term is $p$, so
  [$\Phi_p(x+1)$ is Eisenstein at $p$](lean:cyclotomic_comp_X_add_one_isEisensteinAt).
  Substitution of $x + 1$ for $x$ is a ring automorphism of $\mathbb{Z}[x]$, so $\Phi_p$ is
  irreducible.
- **Shifting.** The same device handles $x^2 + 1$, which is Eisenstein at no prime: replacing $x$
  by $x + 1$ gives $x^2 + 2x + 2$, which is Eisenstein at $2$.
- **Polynomials over other rings.** If $k$ is a field, the ideal $(t)$ of $k[t]$ is prime, and
  $x^n - t$ is Eisenstein at $(t)$; so $x^n - t$ is irreducible in $k[t][x]$ for every $n \ge 1$.

The hypotheses cannot be dropped. The polynomial $x^2 - 4 = (x-2)(x+2)$ satisfies every condition
at $p = 2$ except that its constant term lies in $(2)^2 = (4)$. The polynomial
$2x + 6 = 2(x + 3)$ is Eisenstein at $3$ but not primitive, and it is reducible in
$\mathbb{Z}[x]$ because $2$ is not a unit there, although it is irreducible in $\mathbb{Q}[x]$.
The criterion is only sufficient: $x^2 + x + 1$ has no rational root, so it is irreducible over
$\mathbb{Q}$, but it is Eisenstein at no prime, since no prime divides its middle coefficient $1$.

## Proof

Since $R$ is an integral domain, the units of $R[x]$ are constants, so $f$, of positive degree, is
not a unit. Suppose $f = gh$ in $R[x]$. If $g$ is a constant $c$, then $c$ divides $f$, so $c$ is a unit by
primitivity; likewise for $h$. It remains to rule out a factorization in which $g$ and $h$ both
have positive degree. Since $a_n$ is the product of the leading coefficients of $g$ and $h$ and
$a_n \notin P$, neither leading coefficient lies in $P$.

Reduce coefficients modulo $P$. The [quotient ring](trough:Ideal.Quotient.ring) $R/P$ is an
integral domain; let $F$ be its [field of fractions](trough:IsFractionRing). In $F[x]$ the
reduction of $f$ is $\bar a_n x^n$ with $\bar a_n \neq 0$, so $\bar g \bar h = \bar a_n x^n$.
[Polynomials over a field](trough:Polynomial.instEuclideanDomain) form a Euclidean domain and so
factor uniquely, and $x$ is irreducible, so $\bar g = u x^k$ and
$\bar h = v x^m$ for nonzero constants $u, v \in F$. The leading coefficients of $g$ and $h$
survive reduction, so $k = \deg g \ge 1$ and $m = \deg h \ge 1$. Hence the constant terms
$g(0)$ and $h(0)$ both reduce to $0$, that is, both lie in $P$, and
$a_0 = g(0)\,h(0) \in P^2$, a contradiction.

## Consequences

Over a GCD domain $R$ (an integral domain in which any two elements have a
[greatest common divisor](trough:GCDMonoid.gcd); every [unique factorisation
domain](trough:UniqueFactorizationMonoid), such as $\mathbb{Z}$, is one) with field of fractions
$K$, [a primitive polynomial is irreducible in $R[x]$ exactly when it is irreducible in
$K[x]$](lean:Polynomial.IsPrimitive.irreducible_iff_irreducible_map_fraction_map) (Gauss's lemma).
So a primitive polynomial of positive degree that is Eisenstein at a prime ideal of $R$ is irreducible in $K[x]$.
Primitivity is not needed for this conclusion: writing $f = c f_1$ with $c \in R$ and $f_1$
primitive, the element $c$ is not in $P$ because $a_n \notin P$, so $f_1$ is again Eisenstein at
$P$, hence irreducible in $K[x]$, and $f$ differs from it by a nonzero constant. For
$R = \mathbb{Z}$ this is the classical form: an integer polynomial of positive degree that is
Eisenstein at some prime $p$ is irreducible over $\mathbb{Q}$.

## Related concepts

Eisenstein's criterion is one of several coefficient tests for irreducibility; the
[rational root theorem](trough:num_dvd_of_is_root) reduces the search for a linear factor over
$\mathbb{Q}$ to finitely many candidates, which settles irreducibility over $\mathbb{Q}$ in degrees
$2$ and $3$. The shift used for $\Phi_p$ also works for prime powers: for a prime $p$ and $k \ge 1$,
[$\Phi_{p^k}(x+1)$ is Eisenstein at $p$](lean:cyclotomic_prime_pow_comp_X_add_one_isEisensteinAt).
Irreducibility of every cyclotomic polynomial needs a different argument:
[$\Phi_n$ is irreducible over $\mathbb{Z}$ for every $n \ge 1$](lean:Polynomial.cyclotomic.irreducible).

## In Mathlib

Mathlib states the criterion for an arbitrary integral domain and an arbitrary prime
ideal, and its conclusion is irreducibility in $R[x]$ itself, which is why primitivity appears as
a hypothesis; passing to the field of fractions is left to Gauss's lemma. The three coefficient
conditions are also packaged as a predicate, being Eisenstein at an ideal, which does not include
positive degree; [a primitive polynomial of positive degree that is Eisenstein at a prime ideal is
irreducible](lean:Polynomial.IsEisensteinAt.irreducible). The classical criterion is derived as a
special case of a [more general one](lean:Polynomial.generalizedEisenstein): for an $R$-algebra
$K$ that is a field and a monic $q \in R[x]$ whose image in $K[x]$ is irreducible, a primitive
$f$ of positive degree is irreducible when its leading coefficient is nonzero in $K$, its image in
$K[x]$ is that leading coefficient times a power of the image of $q$, and the remainder of $f$ on
division by $q$ is nonzero modulo $P^2$, where $P$ is the kernel of the map from $R$ to $K$.
Taking $K$ to be the field of fractions of $R/P$ and $q = x$ gives Eisenstein's criterion.

## Depends on

- [Polynomial in one indeterminate](trough:Polynomial)
- [Prime ideal](trough:Ideal.IsPrime)
- [Irreducible element](trough:Irreducible)

## Proof depends on

- [Quotient ring](trough:Ideal.Quotient.ring)
- [Field of fractions of an integral domain](trough:IsFractionRing)
- [Polynomials over a field form a Euclidean domain](trough:Polynomial.instEuclideanDomain)
- [Unique factorisation domain](trough:UniqueFactorizationMonoid)
