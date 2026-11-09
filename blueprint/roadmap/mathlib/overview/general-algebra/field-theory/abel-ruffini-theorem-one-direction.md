# Abel-Ruffini theorem (one direction)

The **Abel–Ruffini theorem**, in the direction treated here, says that if an
element of a [field](field.md) extension can be built from the base field by
the field operations and the extraction of $n$-th roots, then the Galois group of
its [minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md) is a solvable group. It is the half of
Galois's criterion for solvability by radicals that serves as an obstruction: to show that a
polynomial has a root that no formula in radicals can express, it suffices to show
that its Galois group is not solvable. This is how one proves that there is no
[general formula in radicals for equations of degree five or more](../../../hundred-theorems/part-01/insolvability-of-general-higher-degree-equations.md).

## Statement

Let $E$ be a field containing a field $F$. The elements of $E$ that are
**solvable by radicals** over $F$ form the
[smallest intermediate field of $E/F$ closed under taking roots](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#solvableByRad):
the smallest field $K$ with $F \subseteq K \subseteq E$ such that whenever
$x \in E$ and $x^n \in K$ for some $n \ge 1$,
[$x$ itself lies in $K$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#solvableByRad.rad_mem). Equivalently, $x$ is solvable
by radicals when it is reached from elements of $F$ by finitely many additions,
subtractions, multiplications, divisions and extractions of $n$-th roots inside $E$.
Every such element [is a root of a monic polynomial with coefficients in $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#isIntegral_of_mem_solvableByRad),
so it has a minimal polynomial over $F$.

The Galois group $\mathrm{Gal}(p)$ of a polynomial $p$ over $F$ is the
[group of automorphisms of its splitting field that fix $F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/PolynomialGaloisGroup.html#Polynomial.Gal)
(see [splitting field](splitting-field.md)). A group $G$ is
[solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.IsSolvable) if its derived series
$G \supseteq [G,G] \supseteq [[G,G],[G,G]] \supseteq \cdots$
reaches the trivial group after finitely many steps; equivalently, $G$ has a finite
chain of subgroups from $\{e\}$ to $G$, each [normal](../group-theory/part-01/normal-subgroup.md) in the
next with an abelian [quotient](../group-theory/part-01/quotient-group.md).

**Theorem.** If $x \in E$ is solvable by radicals over $F$, then
[the Galois group of the minimal polynomial of $x$ over $F$ is solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#isSolvable_gal_minpoly).

Since an [irreducible](../divisibility-in-integral-domains/irreducible-element.md) polynomial is a constant multiple of the
minimal polynomial of each of its roots, an equivalent form reads:
[if an irreducible polynomial $q$ over $F$ has a root in $E$ that is solvable by radicals, then $\mathrm{Gal}(q)$ is solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#isSolvable_gal_of_irreducible).

## Examples

- **Pure radicals.** For $n \ge 1$, every root of $X^n - a$ in $E$ with $a \in F$ is
  solvable by radicals by definition, and indeed
  [the Galois group of $X^n - a$ is solvable for every $n$ and every $a \in F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#gal_X_pow_sub_C_isSolvable).
- **A quintic with no solution in radicals.** Let $p = X^5 - 4X + 2$ over the
  rationals. It is irreducible by [Eisenstein's criterion](../polynomials-and-power-series/eisensteins-criterion.md)
  at the prime $2$. Its sign changes on $[-2,0]$, $[0,1]$ and $[1,2]$ give three real
  roots, and since $p' = 5X^4 - 4$ has only two real zeros there are no more, so $p$
  has exactly two non-real complex roots. For an irreducible polynomial over the
  rationals of prime degree with exactly two non-real roots,
  [the Galois group acts on the complex roots as the full group of their permutations, faithfully](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Complex/Polynomial/Basic.html#Polynomial.Gal.galActionHom_bijective_of_prime_degree).
  Thus $\mathrm{Gal}(p)$ is isomorphic to the [symmetric group](../group-theory/part-02/permutation-group-of-a-type.md)
  $S_5$, and [the permutation group of a set with at least five elements is not solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Equiv.Perm.not_isSolvable).
  By the theorem, no complex root of $p$ is solvable by radicals over the rationals.

## Proof

The argument uses the closure properties of solvable groups: subgroups and
[images under surjective homomorphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.isSolvable_of_surjective) of
solvable groups are solvable, and
[an extension of a solvable group by a solvable group is solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.isSolvable_of_ker_le_range).
Abelian groups, those
[in which all elements commute, are solvable](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Group.isSolvable_of_comm).

Mathlib argues by induction on the way $x$ is built. If $x \in F$, its minimal
polynomial is $X - x$ and the group is trivial. For the other steps two facts about
Galois groups of polynomials are used. First, the splitting field of $pq$ is generated
by the roots of $p$ and of $q$, so $\mathrm{Gal}(pq)$ embeds in
$\mathrm{Gal}(p) \times \mathrm{Gal}(q)$ and
[is solvable when both factors are](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#gal_mul_isSolvable). Second, if $p$ splits
in the splitting field of $q$, restriction maps $\mathrm{Gal}(q)$ onto
$\mathrm{Gal}(p)$, [so $\mathrm{Gal}(p)$ is solvable whenever $\mathrm{Gal}(q)$ is](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#gal_isSolvable_of_splits).

If $x$ and $y$ have minimal polynomials $p$ and $q$ with solvable Galois groups, let
$z$ be any element of $F(x,y)$, for instance $x \pm y$, $xy$ or $x/y$. An
$F$-embedding of $F(x,y)$ into the splitting field of $pq$ sends $z$ to an element
with the same minimal polynomial; that splitting field is normal over $F$, so the
minimal polynomial of $z$ splits there and the second fact applies. Negatives and
inverses therefore need no separate step, and indeed
[a property that holds for the elements of $F$ and is preserved by sums, products and $n$-th roots holds for every element solvable by radicals](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#solvableByRad.induction). If $x^n$ has minimal polynomial $p$ with solvable Galois group, the minimal
polynomial of $x$ divides $p(X^n)$, and it remains to see that $\mathrm{Gal}(p(X^n))$
is solvable. Over the splitting field $K$ of $p$, the polynomial $p(X^n)$ is, up to a
constant factor, a product of factors $X^n - c$, whose Galois groups are solvable. The
Galois group of $X^n - 1$ is abelian, because each automorphism raises every $n$-th
root of unity to one fixed power; over the splitting field of $X^n - 1$, for $c \ne 0$,
each automorphism multiplies a root of $X^n - c$ by an $n$-th root of unity lying in
the base, which again gives an abelian group. For $c \ne 0$,
[$X^n - 1$ splits in every field in which $X^n - c$ splits](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#splits_X_pow_sub_one_of_X_pow_sub_C),
since dividing the roots of $X^n - c$ by one of them gives the roots of $X^n - 1$;
so the splitting field of $X^n - 1$ lies inside that of $X^n - c$, and the tower
property below combines the two abelian groups. Finally, if $K$ is
normal over $F$ and
[the automorphism groups of $K/F$ and $L/K$ are solvable, so is that of $L/F$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Normal/Basic.html#isSolvable_of_isScalarTower),
which assembles the pieces.

## Related concepts

Over a field $F$ of characteristic zero the converse also holds, provided the roots are
taken in a large enough field, such as an algebraic closure of $F$ in the role of $E$:
if the Galois group of an irreducible polynomial over $F$ is solvable, its roots in an
algebraic closure of $F$ are solvable by radicals there. The choice of $E$ matters. The
polynomial $X^3 - 3X + 1$ over the rationals has a cyclic Galois group of order $3$,
yet its three real roots cannot be expressed by radicals inside the real numbers, so
with $E = \mathbb{R}$ they are not solvable by radicals. Together the two directions
form Galois's criterion. The [Galois correspondence](galois-correspondence.md)
underlies the textbook proof, which translates a tower of radical extensions into a
chain of subgroups with abelian quotients.

## In Mathlib

Mathlib defines the elements solvable by radicals as an intermediate field, the
smallest one closed under $n$-th roots for every $n \ge 1$, rather than through explicit
towers of radical extensions. The Galois group of a polynomial is the full group of
automorphisms of its splitting field over $F$, defined for every polynomial, separable
or not, and always finite. With these conventions the theorem holds over every field, with no
assumption on the characteristic, whereas many textbook treatments assume
characteristic zero. The theorem is stated for an arbitrary extension field $E$ of
$F$, and the minimal polynomial is taken over $F$.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Field](field.md)
- [Group](../group-theory/part-01/group.md)
- [Minimal polynomial](../../linear-algebra/endomorphism-polynomials/minimal-polynomial.md)
- [Splitting field](splitting-field.md)
- [Irreducible element](../divisibility-in-integral-domains/irreducible-element.md)
- [Normal subgroup](../group-theory/part-01/normal-subgroup.md)

## Proof depends on

- [Direct product of groups](../../../undergraduate/group-theory/basic-definitions/direct-product-of-groups.md)

## Sources

- [Mathlib documentation: `isSolvable_gal_minpoly`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/AbelRuffini.html#isSolvable_gal_minpoly)
- [Source of `isSolvable_gal_minpoly` in Mathlib/FieldTheory/AbelRuffini.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/FieldTheory/AbelRuffini.lean#L304)
- [Mathlib overview: General algebra › Field theory](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L135)
