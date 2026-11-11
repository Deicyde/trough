---
declaration: section
origin: cited
lean: NumberField.primeUnitFractionalIdeal, FractionalIdeal.factorizationMulEquiv_primeUnitFractionalIdeal, NumberField.Modulus.mem_coprimeFractionalIdeals_primeUnit, NumberField.Modulus.primeCoprimeUnit, NumberField.Modulus.CoprimePrimes, NumberField.Modulus.coprimePrimeUnits, NumberField.Modulus.mem_coprimePrimeUnits, NumberField.Modulus.coprimePrimeUnits_eq_range
statement: formalized
proof: formalized
---

# Artin map

27 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html).

## A prime as an invertible fractional ideal

For a number field $K$ with ring of integers
$\mathcal O_K$ and a height-one prime $\mathfrak p$ of $\mathcal O_K$, this is $\mathfrak p$
regarded as a fractional ideal of $K$; it is nonzero, hence a unit in the group of nonzero
fractional ideals of $K$.

Formalized by `NumberField.primeUnitFractionalIdeal`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#prime-unit-fractional-ideal).

## Factorization of a prime of a number field

Let $K$ be a number field with ring of
integers $\mathcal O_K$ and let $\mathfrak p$ be a height-one prime of $\mathcal O_K$. The
factorization isomorphism sends $\mathfrak p$, regarded as an invertible fractional ideal of $K$,
to the function on height-one primes of $\mathcal O_K$ that is $1$ at $\mathfrak p$ and $0$
elsewhere.

Formalized by `FractionalIdeal.factorizationMulEquiv_primeUnitFractionalIdeal`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#factorization-mul-equiv-prime-unit-fract).

## Primes not dividing the modulus are coprime to it

Let $\mathfrak m$ be a modulus of a
number field $K$ and let $\mathfrak p$ be a height-one prime of the ring of integers
$\mathcal O_K$ that does not contain the finite part of $\mathfrak m$. Then $\mathfrak p$, viewed
as an invertible fractional ideal of $K$, lies in the group of fractional ideals coprime to
$\mathfrak m$: its exponent at every height-one prime containing the finite part of
$\mathfrak m$ is zero.

Formalized by `NumberField.Modulus.mem_coprimeFractionalIdeals_primeUnit`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#mem-coprime-fractional-ideals-prime-unit).

## The prime as a coprime fractional ideal

Let $\mathfrak m$ be a modulus of a number
field $K$ and let $\mathfrak p$ be a height-one prime of the ring of integers $\mathcal O_K$ that
does not contain the finite part of $\mathfrak m$. This is $\mathfrak p$, viewed as an invertible
fractional ideal of $K$, regarded as an element of the group of fractional ideals coprime to
$\mathfrak m$.

Formalized by `NumberField.Modulus.primeCoprimeUnit`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGenerators.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#prime-coprime-unit).

## Primes coprime to a modulus

Let $\mathfrak m$ be a modulus of a number field $K$. The
primes coprime to $\mathfrak m$ are the nonzero prime ideals $\mathfrak p$ of the ring of
integers $\mathcal O_K$ that do not contain the finite part of $\mathfrak m$, that is, that do
not divide it. They index the generators of a free group that maps to the group of
fractional ideals coprime to the finite part of $\mathfrak m$.

Formalized by `NumberField.Modulus.CoprimePrimes`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#coprime-primes).

## Prime coprime units

Let $\mathfrak m$ be a modulus of a number field $K$, and let
$I_K^{\mathfrak m}$ be the group of invertible fractional ideals of $K$ coprime to the finite
part of $\mathfrak m$. The prime coprime units of $\mathfrak m$ are the elements of
$I_K^{\mathfrak m}$ of the form $\mathfrak p$, where $\mathfrak p$ is a nonzero prime ideal of
the ring of integers $\mathcal O_K$ that does not divide the finite part of $\mathfrak m$.

Formalized by `NumberField.Modulus.coprimePrimeUnits`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#coprime-prime-units).

## Membership in the prime coprime units

Let $\mathfrak m$ be a modulus of a number field
$K$, and let $I_K^{\mathfrak m}$ be the group of invertible fractional ideals of $K$ coprime to
the finite part of $\mathfrak m$. An element $I$ of $I_K^{\mathfrak m}$ is a prime coprime unit
of $\mathfrak m$ if and only if $I = \mathfrak p$ for some nonzero prime ideal $\mathfrak p$ of
the ring of integers $\mathcal O_K$ that does not divide the finite part of $\mathfrak m$.

Formalized by `NumberField.Modulus.mem_coprimePrimeUnits`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#mem-coprime-prime-units).

## The prime coprime units are the image of the coprime primes

Let $\mathfrak m$ be a
modulus of a number field $K$, let $I_K^{\mathfrak m}$ be the group of invertible fractional
ideals of $K$ coprime to the finite part of $\mathfrak m$, and let $P$ be the set of nonzero
prime ideals of the ring of integers $\mathcal O_K$ that do not divide the finite part of
$\mathfrak m$. Then the set of prime coprime units of $\mathfrak m$ equals the range of the map
$P \to I_K^{\mathfrak m}$ sending each $\mathfrak p \in P$ to $\mathfrak p$ viewed as an element
of $I_K^{\mathfrak m}$.

## Sources

- direct native counterpart of ATLAS `primesCoprime_eq_range`.

Formalized by `NumberField.Modulus.coprimePrimeUnits_eq_range`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#coprime-prime-units-eq-range).

## The coprime primes generate the coprime ideals

Let $\mathfrak m$ be a modulus of a
number field $K$, and let $I_K^{\mathfrak m}$ be the group of invertible fractional ideals
of $K$ coprime to the finite part of $\mathfrak m$. Then $I_K^{\mathfrak m}$ is generated,
as a group, by the nonzero prime ideals $\mathfrak p$ of the ring of integers
$\mathcal O_K$ that do not divide the finite part of $\mathfrak m$.

Formalized by `NumberField.Modulus.closure_coprimePrimeUnits_eq_top`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#closure-coprime-prime-units-eq-top).

## The free group on the coprime primes maps to the coprime ideals

Let $\mathfrak m$ be
a modulus of a number field $K$, let $P$ be the set of nonzero prime ideals of the ring of
integers $\mathcal O_K$ that do not divide the finite part of $\mathfrak m$, and let
$I_K^{\mathfrak m}$ be the group of invertible fractional ideals of $K$ coprime to the finite
part of $\mathfrak m$. This is the group homomorphism $F(P) \to I_K^{\mathfrak m}$ from the free
group on $P$ that sends each generator $\mathfrak p$ to $\mathfrak p$, viewed as an element of
$I_K^{\mathfrak m}$.

Formalized by `NumberField.Modulus.freeGroupToCoprime`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-coprime).

## The free-group map on generators

Let $\mathfrak m$ be a modulus of a number field $K$,
let $P$ be the set of nonzero prime ideals of the ring of integers $\mathcal O_K$ that do not
divide the finite part of $\mathfrak m$, and let $I_K^{\mathfrak m}$ be the group of invertible
fractional ideals of $K$ coprime to the finite part of $\mathfrak m$. For every
$\mathfrak p \in P$, the homomorphism $F(P) \to I_K^{\mathfrak m}$ from the free group on $P$
sends the generator attached to $\mathfrak p$ to $\mathfrak p$, viewed as an element of
$I_K^{\mathfrak m}$.

Formalized by `NumberField.Modulus.freeGroupToCoprime_of`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-coprime-of).

## The free group on the coprime primes surjects onto the coprime ideals

Let
$\mathfrak m$ be a modulus of a number field $K$, let $P$ be the set of nonzero prime ideals
of the ring of integers $\mathcal O_K$ that do not divide the finite part of $\mathfrak m$, and
let $I_K^{\mathfrak m}$ be the group of invertible fractional ideals of $K$ coprime to the
finite part of $\mathfrak m$. The homomorphism $F(P) \to I_K^{\mathfrak m}$ from the free group
on $P$ sending each generator $\mathfrak p$ to $\mathfrak p$ is surjective.

Formalized by `NumberField.Modulus.freeGroupToCoprime_surjective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-coprime-surjective).

## The kernel of the free-group map lies in the commutator subgroup

Let $\mathfrak m$ be
a modulus of a number field $K$, let $P$ be the set of nonzero prime ideals of the ring of
integers $\mathcal O_K$ that do not divide the finite part of $\mathfrak m$, and let
$I_K^{\mathfrak m}$ be the group of invertible fractional ideals of $K$ coprime to the finite
part of $\mathfrak m$. The kernel of the homomorphism $F(P) \to I_K^{\mathfrak m}$ from the free
group on $P$ sending each generator $\mathfrak p$ to $\mathfrak p$ is contained in the
commutator subgroup $[F(P), F(P)]$.

## Sources

- direct native counterpart of ATLAS `freeGroupToCoprime_ker_le_commutator` (source lines 429--487). The prime basis-vector computation at source lines 416--427 is replaced by `FractionalIdeal.factorizationMulEquiv_primeUnitFractionalIdeal`. The proof builds the ATLAS retraction to the abelianization through `FractionalIdeal.factorizationMulEquiv`, `Finsupp.comapDomain.addMonoidHom`, `Finsupp.toFreeAbelianGroup`, and `Abelianization.of`; the retraction itself stays private to this proof.

Formalized by `NumberField.Modulus.freeGroupToCoprime_ker_le_commutator`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-coprime-ker-le-commutator).

## The kernel of the free-group map is the commutator subgroup

Let $\mathfrak m$ be a
modulus of a number field $K$, let $P$ be the set of nonzero prime ideals of the ring of
integers $\mathcal O_K$ that do not divide the finite part of $\mathfrak m$, and let
$I_K^{\mathfrak m}$ be the group of invertible fractional ideals of $K$ coprime to the finite
part of $\mathfrak m$. The kernel of the homomorphism $F(P) \to I_K^{\mathfrak m}$ from the free
group on $P$ sending each generator $\mathfrak p$ to $\mathfrak p$ equals the commutator
subgroup $[F(P), F(P)]$.

The commutator subgroup lies in the kernel because $I_K^{\mathfrak m}$ is abelian.

Formalized by `NumberField.Modulus.freeGroupToCoprime_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/PrimeGeneration.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-coprime-ker).

## Extensions unramified outside a modulus

Let $m$ be a modulus of a number field $K$.
An extension of number fields $L / K$ is unramified outside $m$ when every finite prime
$\mathfrak p$ of $K$ not dividing the finite part of $m$ is unramified in $\mathcal O_L$,
that is, every prime of $\mathcal O_L$ lying over $\mathfrak p$ is unramified over
$\mathcal O_K$.

Formalized by `NumberField.Modulus.IsUnramifiedOutside`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#is-unramified-outside).

## Unramified outside a modulus implies unramified at coprime primes

Let $m$ be a
modulus of a number field $K$ and let $L / K$ be an extension of number fields that is
unramified outside $m$. Then every finite prime $\mathfrak p$ of $K$ not dividing the finite
part of $m$ is unramified in $\mathcal O_L$.

Formalized by `NumberField.Modulus.IsUnramifiedOutside.at_coprimePrime`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#at-coprime-prime).

## Chosen Frobenius element at a coprime prime

Let $m$ be a modulus of a number field
$K$, let $L / K$ be a Galois extension of number fields that is unramified outside $m$, and
let $\mathfrak p$ be a finite prime of $K$ not dividing the finite part of $m$. Fix a prime
$\mathfrak P$ of $\mathcal O_L$ lying over $\mathfrak p$. The chosen Frobenius element at
$\mathfrak p$ is a fixed element $\sigma \in \mathrm{Gal}(L/K)$ that is an arithmetic
Frobenius at $\mathfrak P$, that is, $\sigma(x) \equiv x^q \pmod{\mathfrak P}$ for all
$x \in \mathcal O_L$, where $q$ is the number of elements of $\mathcal O_K / \mathfrak p$.

The value may depend on the choice of $\mathfrak P$.

Formalized by `NumberField.Modulus.frobeniusAtCoprimePrime`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#frobenius-at-coprime-prime).

## The chosen Frobenius is an arithmetic Frobenius at an unramified prime

Let $m$ be
a modulus of a number field $K$, let $L / K$ be a Galois extension of number fields that is
unramified outside $m$, and let $\mathfrak p$ be a finite prime of $K$ not dividing the
finite part of $m$, with chosen Frobenius element $\sigma \in \mathrm{Gal}(L/K)$. Then there
is a prime $\mathfrak P$ of $\mathcal O_L$ lying over $\mathfrak p$ such that
$\mathcal O_L / \mathfrak P$ is finite, $\mathfrak P$ is unramified over $\mathcal O_K$, and
$\sigma(x) \equiv x^q \pmod{\mathfrak P}$ for all $x \in \mathcal O_L$, where $q$ is the
number of elements of $\mathcal O_K / \mathfrak p$.

Formalized by `NumberField.Modulus.frobeniusAtCoprimePrime_spec`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#frobenius-at-coprime-prime-spec).

## Frobenius homomorphism on the free group of coprime primes

Let $m$ be a modulus
of a number field $K$ and let $L / K$ be a Galois extension of number fields that is
unramified outside $m$. The Frobenius homomorphism is the group homomorphism from the free
group on the finite primes of $K$ not dividing the finite part of $m$ to $\mathrm{Gal}(L/K)$
that sends each such prime $\mathfrak p$ to the chosen Frobenius element at $\mathfrak p$.

Formalized by `NumberField.Modulus.freeGroupToGal`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-gal).

## The Frobenius homomorphism on generators

Let $m$ be a modulus of a number field
$K$ and let $L / K$ be a Galois extension of number fields that is unramified outside $m$.
For every finite prime $\mathfrak p$ of $K$ not dividing the finite part of $m$, the
Frobenius homomorphism from the free group on these primes to $\mathrm{Gal}(L/K)$ sends the
generator $\mathfrak p$ to the chosen Frobenius element at $\mathfrak p$.

Formalized by `NumberField.Modulus.freeGroupToGal_of`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusGenerators.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-gal-of).

## Kernel containment for the free-group Frobenius map

Let $L/K$ be an abelian Galois
extension of number fields and $\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$,
such that every prime of $\mathcal O_K$ not dividing $\mathfrak m_0$ is unramified in $L$. Let
$F$ be the free group on the primes $\mathfrak p$ of $\mathcal O_K$ not dividing $\mathfrak m_0$.
Then the kernel of the homomorphism from $F$ to the group of fractional ideals of $K$ coprime to
$\mathfrak m_0$ sending each generator $\mathfrak p$ to the ideal $\mathfrak p$ is contained in
the kernel of the homomorphism $F \to \mathrm{Gal}(L/K)$ sending each generator $\mathfrak p$ to
the arithmetic Frobenius at a chosen prime of $\mathcal O_L$ above $\mathfrak p$.

The first kernel lies in the commutator subgroup of $F$, which the second map kills because
$\mathrm{Gal}(L/K)$ is abelian.

Formalized by `NumberField.Modulus.freeGroupToCoprime_ker_le_freeGroupToGal_ker`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#free-group-to-coprime-ker-le-free-group).

## Artin map

Let $L/K$ be an abelian Galois extension of number fields and $\mathfrak m$
a modulus of $K$ with finite part $\mathfrak m_0$, such that every prime of $\mathcal O_K$ not
dividing $\mathfrak m_0$ is unramified in $L$. Let $I^{\mathfrak m}$ be the group of fractional
ideals of $K$ coprime to $\mathfrak m_0$ and $F$ the free group on the primes $\mathfrak p$ of
$\mathcal O_K$ not dividing $\mathfrak m_0$. The homomorphism $F \to I^{\mathfrak m}$ sending
each generator $\mathfrak p$ to the ideal $\mathfrak p$ is surjective, and its kernel lies in the
kernel of the homomorphism $F \to \mathrm{Gal}(L/K)$ sending each generator $\mathfrak p$ to the
arithmetic Frobenius at a chosen prime of $\mathcal O_L$ above $\mathfrak p$. The Artin map is
the homomorphism $I^{\mathfrak m} \to \mathrm{Gal}(L/K)$ induced by the second map through the
first.

Formalized by `NumberField.Modulus.artinMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#artin-map).

## The Artin map factors the free-group Frobenius map

Let $L/K$ be an abelian Galois
extension of number fields and $\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$,
such that every prime of $\mathcal O_K$ not dividing $\mathfrak m_0$ is unramified in $L$. Let
$F$ be the free group on the primes $\mathfrak p$ of $\mathcal O_K$ not dividing $\mathfrak m_0$,
and let $I^{\mathfrak m}$ be the group of fractional ideals of $K$ coprime to $\mathfrak m_0$.
Then the Artin map $I^{\mathfrak m} \to \mathrm{Gal}(L/K)$ composed with the homomorphism
$F \to I^{\mathfrak m}$ sending each generator $\mathfrak p$ to the ideal $\mathfrak p$ equals the
homomorphism $F \to \mathrm{Gal}(L/K)$ sending each generator $\mathfrak p$ to the arithmetic
Frobenius at a chosen prime of $\mathcal O_L$ above $\mathfrak p$.

Formalized by `NumberField.Modulus.artinMap_comp_freeGroupToCoprime`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#artin-map-comp-free-group-to-coprime).

## The Artin map at a prime

Let $L/K$ be an abelian Galois extension of number fields and
$\mathfrak m$ a modulus of $K$ with finite part $\mathfrak m_0$, such that every prime of
$\mathcal O_K$ not dividing $\mathfrak m_0$ is unramified in $L$. For every prime $\mathfrak p$
of $\mathcal O_K$ not dividing $\mathfrak m_0$, the Artin map sends $\mathfrak p$, viewed as a
fractional ideal coprime to $\mathfrak m_0$, to the arithmetic Frobenius in $\mathrm{Gal}(L/K)$
at a chosen prime of $\mathcal O_L$ above $\mathfrak p$.

Formalized by `NumberField.Modulus.artinMap_primeCoprimeUnit`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/ArtinMap.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#artin-map-prime-coprime-unit).

## Restriction of Frobenius elements in a tower

Let $K \subseteq L \subseteq M$ be a tower
of number fields with $L/K$ abelian Galois and $M/K$ Galois, and let $\mathfrak m$ be a modulus
of $K$ such that $L$ and $M$ are both unramified outside $\mathfrak m$. For every finite prime
$\mathfrak p$ of $K$ not dividing the finite part of $\mathfrak m$, the restriction to $L$ of the
chosen Frobenius element of $\mathfrak p$ in $\mathrm{Gal}(M/K)$ equals the chosen Frobenius
element of $\mathfrak p$ in $\mathrm{Gal}(L/K)$.

The abelianity of $L/K$ is used only to make conjugation of the Frobenius element in
$\mathrm{Gal}(L/K)$ trivial.

Formalized by `NumberField.Modulus.restrictNormalHom_frobeniusAtCoprimePrime`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusRestriction.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/FrobeniusRestriction.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#restrict-normal-hom-frobenius-at-coprime).

## Restriction of the Artin map at a prime

Let $K \subseteq L \subseteq M$ be a tower of
number fields with $L/K$ and $M/K$ abelian Galois, and let $\mathfrak m$ be a modulus of $K$ with
finite part $\mathfrak m_0$ such that every prime of $\mathcal O_K$ not dividing $\mathfrak m_0$
is unramified in $L$ and in $M$. For every prime $\mathfrak p$ of $\mathcal O_K$ not dividing
$\mathfrak m_0$, restricting to $L$ the image of $\mathfrak p$ under the Artin map of $M/K$ gives
the image of $\mathfrak p$ under the Artin map of $L/K$.

Formalized by `NumberField.Modulus.restrictNormalHom_artinMap_primeCoprimeUnit`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ArtinMapRestriction.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/ArtinMapRestriction.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#restrict-normal-hom-artin-map-prime-copr).

## The Artin map commutes with restriction

Let $K \subseteq L \subseteq M$ be a tower of
number fields with $L/K$ and $M/K$ abelian Galois, and let $\mathfrak m$ be a modulus of $K$
with finite part $\mathfrak m_0$ such that every prime of $\mathcal O_K$ not dividing
$\mathfrak m_0$ is unramified in $L$ and in $M$. Then the Artin map of $M/K$ followed by
restriction $\mathrm{Gal}(M/K) \to \mathrm{Gal}(L/K)$ equals the Artin map of $L/K$, as
homomorphisms from the group of fractional ideals of $K$ coprime to $\mathfrak m_0$ to
$\mathrm{Gal}(L/K)$.

Formalized by `NumberField.Modulus.restrictNormalHom_comp_artinMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ArtinMapRestriction.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/RayClass/ArtinMapRestriction.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html#restrict-normal-hom-comp-artin-map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Artin map](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/artin-map)
