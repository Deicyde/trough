---
article_id: af_a069927a04ef2f6fdbc5c5d3
concept: NumberField.RingOfIntegers.instFintypeClassGroup
---

**Finiteness of the class number** is the theorem that the ideal class group of
the ring of integers of a number field is finite. Its order, the class number,
measures how far that ring is from being a [principal ideal
domain](trough:Submodule.IsPrincipal), and in particular whether factorization
of elements into irreducibles in it is unique. Together with the [Dirichlet unit
theorem](trough:NumberField.Units.exist_unique_eq_mul_prod) it is one of the two
basic finiteness results of algebraic number theory.

## Statement

Let $K$ be a number field, that is, a finite extension of the
[rational numbers](trough:Rat), and let $\mathcal{O}_K$ be its ring of integers,
the elements of $K$ that are roots of monic polynomials with integer
coefficients. The ring $\mathcal{O}_K$ is a Dedekind domain: every nonzero
[ideal](trough:Ideal) factors uniquely as a product of [prime
ideals](trough:Ideal.IsPrime). Its nonzero [fractional
ideals](trough:FractionalIdeal) form an abelian group under multiplication, the
principal fractional ideals form a subgroup, and the [quotient
group](trough:QuotientGroup.Quotient.group) is
[the ideal class group](lean:ClassGroup) $\mathrm{Cl}(K)$. Two nonzero ideals
$I$ and $J$ of $\mathcal{O}_K$ lie in the same class exactly when
[there are nonzero $x, y \in \mathcal{O}_K$ with $(x)I = (y)J$](lean:ClassGroup.mk0_eq_mk0_iff),
and [the class of a nonzero ideal is trivial exactly when the ideal is principal](lean:ClassGroup.mk0_eq_one_iff).

The theorem states that
[the class group $\mathrm{Cl}(K)$ is finite](lean:NumberField.RingOfIntegers.instFintypeClassGroup).
Its order is [the class number $h_K$](lean:NumberField.classNumber), which is
therefore [a positive integer](lean:NumberField.classNumber_pos).

A quantitative form gives a bound. Write $n = [K : \mathbb{Q}]$, let $r_2$ be the
number of pairs of complex conjugate embeddings of $K$ into $\mathbb{C}$, let
$d_K$ be the discriminant of $K$, and let the norm $N(I)$ of a nonzero ideal be
the number of elements of $\mathcal{O}_K / I$. Then
[every ideal class contains a nonzero ideal $I$ with $N(I) \le M_K$](lean:NumberField.exists_ideal_in_class_of_norm_le),
where $M_K$ is the Minkowski bound

$$M_K = \left(\frac{4}{\pi}\right)^{r_2} \frac{n!}{n^n} \sqrt{|d_K|}.$$

## Examples

- **The rationals.** Here $\mathcal{O}_K = \mathbb{Z}$ is a principal ideal
  domain, and [the class number of $\mathbb{Q}$ is $1$](lean:Rat.classNumber_eq).
- **The Gaussian integers.** For $K = \mathbb{Q}(i)$ one has
  $\mathcal{O}_K = \mathbb{Z}[i]$, $n = 2$, $r_2 = 1$ and $d_K = -4$, so
  $M_K = 4/\pi < 2$. Every class then contains an ideal of norm $1$, which is
  $\mathcal{O}_K$ itself, and $h_K = 1$.
- **A class number two.** For $K = \mathbb{Q}(\sqrt{-5})$ one has
  $\mathcal{O}_K = \mathbb{Z}[\sqrt{-5}]$ and $d_K = -20$, so
  $M_K = 4\sqrt{5}/\pi \approx 2.85$. The prime $2$ ramifies: $(2) = \mathfrak{p}^2$
  with $\mathfrak{p} = (2, 1 + \sqrt{-5})$, the only ideal of norm $2$. It is not
  principal, since $a^2 + 5b^2 = 2$ has no integer solutions. Hence
  $\mathrm{Cl}(K)$ has order $2$. The two factorizations
  $6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$ into irreducibles reflect this.
- **Cyclotomic fields.** The Minkowski bound shows that
  [the ring of integers of the field generated over $\mathbb{Q}$ by a primitive cube root of unity is a principal ideal domain](lean:IsCyclotomicExtension.Rat.three_pid),
  and that
  [the same holds for a primitive fifth root of unity](lean:IsCyclotomicExtension.Rat.five_pid).

## Consequences

- **Principal ideal domains.**
  [The class number $h_K$ equals $1$ exactly when $\mathcal{O}_K$ is a principal ideal domain](lean:NumberField.classNumber_eq_one_iff).
  A Dedekind domain is a [unique factorization domain](trough:UniqueFactorizationMonoid)
  exactly when it is a principal ideal domain, so $h_K = 1$ also characterizes
  unique factorization of elements in $\mathcal{O}_K$.
- **A discriminant criterion.**
  [If $|d_K| < \left(2 (\pi/4)^{r_2} n^n / n!\right)^2$, then $\mathcal{O}_K$ is a principal ideal domain](lean:RingOfIntegers.isPrincipalIdealRing_of_abs_discr_lt).
  The condition says $M_K < 2$, so every class contains an ideal of norm $1$.
- **Powers of ideals.** By [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card)
  in $\mathrm{Cl}(K)$, the power $I^{h_K}$ of every nonzero ideal $I$ is principal.
  In the other direction, if $m$ is a positive integer coprime to $h_K$ and
  [$I^m$ is principal, then $I$ is principal](lean:Ideal.IsPrincipal.of_isPrincipal_pow_of_coprime).

## Proof

The classical argument uses the geometry of numbers. Embed $K$ in
$\mathbb{R}^{r_1} \times \mathbb{C}^{r_2}$, where $r_1$ counts the real embeddings;
a nonzero ideal becomes a lattice whose covolume is proportional to its norm.
[Minkowski's theorem](trough:MeasureTheory.exists_ne_zero_mem_lattice_of_measure_mul_two_pow_lt_measure)
applied to a suitable convex body shows that
[every nonzero ideal $I$ contains a nonzero $a$ with $|N_{K/\mathbb{Q}}(a)| \le M_K\,N(I)$](lean:NumberField.exists_ne_zero_mem_ideal_of_norm_le_mul_sqrt_discr).

Given a class $C$, pick a nonzero ideal $I$ in the inverse class $C^{-1}$ and such
an element $a \in I$. In a Dedekind domain an ideal containing $(a)$ divides it,
so $(a) = IJ$ for some ideal $J$, which lies in $C$. The norm is multiplicative
and $N((a)) = |N_{K/\mathbb{Q}}(a)|$, so $N(J) \le M_K$.

It remains to see that only finitely many ideals have norm at most $M_K$. An
ideal of norm $m$ contains $m$, so it divides $(m)$, which has only finitely many
ideal divisors. In general,
[a Dedekind domain whose quotients by nonzero ideals are all finite has only finitely many ideals of norm at most a given integer](lean:Ring.HasFiniteQuotients.finite_absNorm_le),
and $\mathcal{O}_K$ is such a ring. Every class contains one of these finitely many
ideals, so there are finitely many classes.

## Related concepts

- The [Dirichlet class number formula](trough:NumberField.tendsto_sub_one_mul_dedekindZeta_nhdsGT)
  expresses the residue at $s = 1$ of the Dedekind zeta function of $K$ in terms of
  $h_K$, the regulator, the number of roots of unity, $r_1$, $r_2$ and $d_K$.
- **Function fields.** The same finiteness holds for the integral closure of
  $\mathbb{F}_q[t]$ in a finite separable extension $F$ of the
  [rational function field](trough:RatFunc) $\mathbb{F}_q(t)$, and Mathlib defines
  [the class number of such a function field](lean:FunctionField.classNumber)
  as the order of that class group. This number depends on the choice of $t$,
  and in general differs from the class number of $F$ defined through divisor
  classes of degree zero.

## In Mathlib

Mathlib defines the class group of any integral domain as the group of
invertible fractional ideals of the domain (inside its field of fractions)
modulo the principal ones. In
a Dedekind domain every nonzero fractional ideal is invertible, so this is the
usual group. Finiteness is recorded as a noncomputable finiteness structure on
the class group, a finite set that contains every class, and the class number
is defined as the cardinality of that set. The proof does not go through the Minkowski bound. It applies a
general theorem: the integral closure of a Euclidean domain in a finite separable
extension of its fraction field has finite class group, provided the domain
is infinite and carries an integer-valued absolute value, compatible with the
Euclidean division, with a suitable approximation property (called admissible). The integers with the usual absolute value give the number field
case, and polynomials over a finite field with an absolute value based on the
degree give the function field case. The Minkowski bound is proved separately,
through the geometry of numbers, and serves as a tool for showing that particular
rings of integers are principal ideal domains.

## Depends on

- [Ideal of a commutative ring](trough:Ideal)
- [Fractional ideal](trough:FractionalIdeal)
- [Quotient group](trough:QuotientGroup.Quotient.group)
- [Prime ideal](trough:Ideal.IsPrime)

## Proof depends on

- [Minkowski’s Fundamental Theorem](trough:MeasureTheory.exists_ne_zero_mem_lattice_of_measure_mul_two_pow_lt_measure)
