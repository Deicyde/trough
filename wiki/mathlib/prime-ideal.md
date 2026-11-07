A **prime ideal** of a commutative [ring](trough:Ring) is a proper
[ideal](trough:Ideal) with the property that whenever a product of two elements
lies in it, one of the two factors already does. The definition transfers a
characteristic property of a prime number (Euclid's lemma: it divides a product
only if it divides one of the factors) from elements to ideals. Prime ideals are
exactly the ideals whose [quotient ring](trough:Ideal.Quotient.ring) is an
integral domain, a nonzero commutative ring in which a product of nonzero
elements is nonzero, and they
are the points of the [prime spectrum](trough:PrimeSpectrum), the space on which
algebraic geometry is built.

## Definition

Let $R$ be a commutative ring. An ideal $P$ of $R$ is
prime if

- $P \neq R$, and
- for all $a, b \in R$, if $ab \in P$ then $a \in P$ or $b \in P$.

Since an ideal equals $R$ exactly when it contains $1$, the first condition says
that $1 \notin P$. Read contrapositively, the second condition says that
the product of two elements outside $P$ is again outside $P$.
Together with $1 \notin P$, this means that the
complement $R \setminus P$ is a multiplicatively closed set.

The leading characterization is through quotients: for an ideal $P$ of $R$,
the quotient $R/P$ is an integral domain exactly when $P$ is prime.
The condition $P \neq R$ corresponds to the requirement that an integral domain
have $0 \neq 1$, and the product condition to the absence of zero divisors in
$R/P$.

## Examples

- **The integers.** For a nonzero element $p$ of a commutative ring,
  the principal ideal $(p)$ is prime exactly when $p$ is a prime element
  (see [prime element](trough:Prime)). In the [integers](trough:Int) an integer
  $k$ is a prime element
  exactly when its absolute value is a prime number,
  so the nonzero prime ideals of $\mathbb{Z}$ are the ideals $p\mathbb{Z}$ with
  $p$ a prime number. Since every ideal of $\mathbb{Z}$ is principal, the only
  other prime ideal is $\{0\}$.
- **The zero ideal.** For a commutative ring $R$,
  if $R$ is an integral domain then $\{0\}$ is a prime ideal,
  and conversely, if $\{0\}$ is prime then $R$ is an integral domain.
- **Fields.** In a [field](trough:Field),
  every prime ideal is $\{0\}$, and $\{0\}$ is
  prime because a field is an integral domain, so $\{0\}$ is the only prime
  ideal.
- **Polynomials.** In the [polynomial](trough:Polynomial) ring $\mathbb{Z}[x]$, the
  ideal $(x)$ is prime, because $\mathbb{Z}[x]/(x)$ is isomorphic to $\mathbb{Z}$,
  an integral domain. The ideal $(4, x)$ is not prime: $2 \cdot 2 \in (4, x)$, but
  $2 \notin (4, x)$.

## Properties

**Maximal ideals are prime.** In a commutative ring,
every maximal ideal is prime, as one also sees
from the quotients: the quotient by a [maximal ideal](trough:Ideal.IsMaximal) is a
field, and every field is an integral domain. The converse fails: $\{0\}$ is a
prime ideal of $\mathbb{Z}$ that is not maximal, and so is $(x)$ in
$\mathbb{Z}[x]$, which lies strictly inside the proper ideal $(2, x)$. Since
every proper ideal is contained in a maximal ideal,
every proper ideal is contained in a prime ideal, and in particular every
nonzero commutative ring has at least one prime ideal.

**Products and powers.** By induction on the number of factors,
a finite product of elements lies in a prime ideal $P$ exactly when one of the factors does.
In particular if $r^n \in P$ for some $n$, then $r \in P$.
The radical of an ideal $I$ is the set of elements $r$ with $r^n \in I$ for some
$n \geq 1$, and $I$ is a radical ideal when it equals its radical; so a prime
ideal is a radical ideal:
it equals its own radical. The same property holds
one level up, for ideals: for ideals $I$ and $J$,
the product $IJ$ is contained in $P$ exactly when $I \subseteq P$ or $J \subseteq P$,
and likewise $I \cap J \subseteq P$ exactly when $I \subseteq P$ or $J \subseteq P$.

**Radicals.** Prime ideals determine radicals: for every ideal $I$ of $R$,
the radical of $I$ is the intersection of all prime ideals containing $I$.

**Ring morphisms.** If $f \colon R \to S$ is a [ring morphism](trough:RingHom)
of commutative rings and $Q$ is a prime ideal of $S$, then
the preimage $f^{-1}(Q)$ is a prime ideal of $R$.
In particular, taking $Q = \{0\}$ in an integral domain,
the kernel of a ring morphism into an integral domain is a prime ideal.
Images of prime ideals, by contrast, need not be prime.

**Existence by maximality.** Let $S$ be a multiplicatively closed subset of $R$
and $I$ an ideal disjoint from $S$ such that every ideal strictly containing $I$
meets $S$. Then $I$ is prime.
Combined with Zorn's lemma, this shows that
every ideal disjoint from $S$ is contained in a prime ideal disjoint from $S$;
such an ideal exists only when $0 \notin S$. Similarly,
the intersection of a nonempty chain of prime ideals is prime,
so, by Zorn's lemma applied to reverse inclusion, every prime ideal contains a
minimal prime ideal, one that contains no strictly smaller prime ideal.

## Related concepts

- **Localization.** Because $R \setminus P$ is multiplicatively closed, one can
  [localize](trough:Localization) $R$ at it, inverting every element outside $P$.
  The resulting ring $R_P$ is a local ring
  (see [local ring](trough:IsLocalRing)), whose unique maximal ideal comes from $P$.
- **Prime spectrum.** The set of all prime ideals of $R$, equipped with the
  [Zariski topology](trough:PrimeSpectrum.zariskiTopology), is the
  [prime spectrum](trough:PrimeSpectrum) of $R$.
- **Prime elements.** A nonzero element $p$ is prime exactly when the principal
  ideal $(p)$ is prime, so prime ideals generalize prime elements; in rings
  without unique factorization, such as many rings of integers of number fields
  (for instance $\mathbb{Z}[\sqrt{-5}]$),
  factorization of ideals into prime ideals takes the place of factorization of
  elements.

## In Mathlib

Mathlib states primality as a property of an ideal that may be supplied
automatically, so that facts such as the primality of maximal ideals, of the zero
ideal of an integral domain and of preimages are found without being invoked by
name. The definition is made for an arbitrary semiring rather than only for
commutative rings. For a noncommutative ring an ideal in Mathlib means a left
ideal, and the elementwise product condition is then stronger than the usual
noncommutative notion of a prime ideal, which is phrased with products of
ideals; most results about prime ideals, such as the description of the radical,
assume commutativity. Prime ideals of a lattice in the sense of order theory are
a separate notion with their own definition.

## Depends on

- [Ring](trough:Ring)
- [Ideal of a commutative ring](trough:Ideal)
- [Quotient ring](trough:Ideal.Quotient.ring)
