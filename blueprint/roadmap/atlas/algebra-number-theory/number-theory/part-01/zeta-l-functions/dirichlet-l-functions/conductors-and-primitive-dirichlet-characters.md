---
declaration: section
origin: cited
lean: MonoidHom.IsDirichletCharacterModulus, MonoidHom.isDirichletCharacterModulus_iff, MonoidHom.isDirichletCharacterModulus_self, DirichletCharacter.PrimitiveInducer, DirichletCharacter.PrimitiveInducer.ext, DirichletCharacter.equivPrimitiveInducer, DirichletCharacter.equivPrimitiveInducer_level, DirichletCharacter.equivPrimitiveInducer_char
statement: formalized
proof: formalized
---

# Conductors and primitive Dirichlet characters

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html).

## Dirichlet character of a given modulus

Let $R$ be a monoid with zero, let
$\chi \colon \mathbb{Z} \to R$ be a multiplicative map with $\chi(1) = 1$, and let $q$ be a
natural number. Then $\chi$ is a Dirichlet character of modulus $q$ if $\chi(n + q) = \chi(n)$
for every integer $n$, and, for every integer $n$, $\chi(n) \neq 0$ if and only if $q$ and $n$
are coprime.

Formalized by `MonoidHom.IsDirichletCharacterModulus`, a definition declared in [MathlibExt/NumberTheory/DirichletCharacter/Period.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/Period.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#is-dirichlet-character-modulus).

## Moduli of a character with a given least period

Let $R$ be a nontrivial monoid with zero
in which nonzero elements can be cancelled on both sides, and let $\chi \colon \mathbb{Z} \to R$
be a multiplicative map with $\chi(1) = 1$. Suppose $m \ge 1$ is the least positive period of
$\chi$: $\chi(n + m) = \chi(n)$ for every integer $n$, and every positive integer $d$ with
$\chi(n + d) = \chi(n)$ for all $n$ satisfies $m \le d$. Then for every integer $m' \ge 1$,
$\chi$ is a Dirichlet character of modulus $m'$ if and only if $m \mid m'$ and $m' \mid m^k$
for some natural number $k$.

The hypothesis that $R$ is nontrivial cannot be dropped: in the zero monoid every value of
$\chi$ is $0$, so $\chi$ is a Dirichlet character of no modulus.

## Sources

- ATLAS `NumberTheoryI` Lemma 18.8. Forward: minimality gives the divisibility, and a prime divisor of `m'` divides `m` (else `χ p` is simultaneously zero and nonzero). Backward: periodicity lifts along `m ∣ m'`, and the nonvanishing locus transfers via the two lemmas above.

Formalized by `MonoidHom.isDirichletCharacterModulus_iff`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/Period.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/Period.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#is-dirichlet-character-modulus-iff).

## A character is a Dirichlet character modulo its least period

Let $R$ be a nontrivial
monoid with zero in which nonzero elements can be cancelled on both sides, and let
$\chi \colon \mathbb{Z} \to R$ be a multiplicative map with $\chi(1) = 1$. If $m \ge 1$ is the
least positive period of $\chi$ (that is, $\chi(n + m) = \chi(n)$ for every integer $n$, and every
positive integer $d$ with $\chi(n + d) = \chi(n)$ for all $n$ satisfies $m \le d$), then $\chi$
is a Dirichlet character of modulus $m$.

Formalized by `MonoidHom.isDirichletCharacterModulus_self`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/Period.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/Period.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#is-dirichlet-character-modulus-self).

## Primitive characters at divisor levels

Let $R$ be a commutative monoid with zero and $m$
a natural number. A primitive inducer of modulus $m$ with values in $R$ consists of a natural
number $d$, its level, with $d \mid m$, together with a Dirichlet character $\psi$ of level $d$
with values in $R$ that is primitive, that is, whose conductor is $d$. These are the elements of
the set $X(m)$ of Corollary 18.16; changing the level of $\psi$ from $d$ to $m$ gives the induced
Dirichlet character of level $m$.

Formalized by `DirichletCharacter.PrimitiveInducer`, a structure declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#primitive-inducer).

## Equality of primitive characters at divisor levels

Let $R$ be a commutative monoid with
zero and $m$ a natural number, and let $p$ and $q$ be primitive inducers of modulus $m$ with
values in $R$. If $p$ and $q$ have the same level, and the character of $p$, transported along
this equality of levels, equals the character of $q$, then $p = q$.

Formalized by `DirichletCharacter.PrimitiveInducer.ext`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#ext).

## Dirichlet characters correspond to primitive characters at divisor levels

Let $R$ be a
commutative monoid with zero and $m \ge 1$ a natural number. This is the bijection from Dirichlet
characters of level $m$ with values in $R$ to primitive inducers of modulus $m$ (primitive
Dirichlet characters with values in $R$ whose level divides $m$) that sends $\chi$ to the
primitive character associated to $\chi$, whose level is the conductor of $\chi$. Its inverse
sends a primitive character $\psi$ of level $d \mid m$ to the Dirichlet character of level $m$
obtained from $\psi$ by changing the level from $d$ to $m$.

## Sources

- ATLAS NumberTheoryI, Section 18.2.1, Corollary 18.16 (first bijection).

Formalized by `DirichletCharacter.equivPrimitiveInducer`, a definition declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#equiv-primitive-inducer).

## Level of the primitive inducer attached to a character

Let $R$ be a commutative monoid
with zero, let $m \ge 1$, and let $\chi$ be a Dirichlet character of level $m$ with values in $R$.
The level of the primitive inducer that the bijection between Dirichlet characters of level $m$
and primitive inducers of modulus $m$ assigns to $\chi$ is the conductor of $\chi$.

Formalized by `DirichletCharacter.equivPrimitiveInducer_level`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#equiv-primitive-inducer-level).

## Character of the primitive inducer attached to a character

Let $R$ be a commutative
monoid with zero, let $m \ge 1$, and let $\chi$ be a Dirichlet character of level $m$ with values
in $R$. The character of the primitive inducer that the bijection between Dirichlet characters of
level $m$ and primitive inducers of modulus $m$ assigns to $\chi$, a Dirichlet character whose
level is the conductor of $\chi$, is the primitive character associated to $\chi$.

Formalized by `DirichletCharacter.equivPrimitiveInducer_char`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#equiv-primitive-inducer-char).

## Primitive characters at divisor levels correspond to unit-group characters

Let $R$ be a
commutative monoid with zero and $m \ge 1$ a natural number. This is the bijection from primitive
inducers of modulus $m$ with values in $R$ to monoid homomorphisms
$(\mathbb{Z}/m\mathbb{Z})^\times \to R^\times$ that sends a primitive character $\psi$ of level
$d \mid m$ to the homomorphism $u \mapsto \chi(u)$, where $\chi$ is the Dirichlet character of
level $m$ obtained from $\psi$ by changing the level from $d$ to $m$.

## Sources

- ATLAS NumberTheoryI, Section 18.2.1, Corollary 18.16 (second bijection).

Formalized by `DirichletCharacter.PrimitiveInducer.equivUnitHom`, a definition declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#equiv-unit-hom).

## Values of the unit-group character of a primitive inducer

Let $R$ be a commutative monoid
with zero, let $m \ge 1$, and let $p$ be a primitive inducer of modulus $m$ with values in $R$,
with level $d$ and character $\psi$. For every unit $u$ of $\mathbb{Z}/m\mathbb{Z}$, the value at
$u$ of the homomorphism $(\mathbb{Z}/m\mathbb{Z})^\times \to R^\times$ corresponding to $p$,
viewed as an element of $R$, equals the value at $u$ of the Dirichlet character of level $m$
obtained from $\psi$ by changing the level from $d$ to $m$.

Formalized by `DirichletCharacter.PrimitiveInducer.equivUnitHom_apply`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean, line 133](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveEquiv.lean#L133). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#equiv-unit-hom-apply).

## The level of a primitive inducer is the conductor

Let $R$ be a commutative monoid with
zero, let $n \ge 1$ and $d$ be natural numbers with $d \mid n$, and let $\chi$ be a Dirichlet
character of level $n$ with values in $R$. If $\chi'$ is a primitive Dirichlet character of
level $d$ whose change of level to $n$ is $\chi$, then $d$ equals the conductor of $\chi$.

Formalized by `DirichletCharacter.conductor_eq_of_isPrimitive_changeLevel`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveUniqueness.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveUniqueness.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#conductor-eq-of-is-primitive-change-leve).

## An inducer at the conductor level is the primitive character

Let $R$ be a commutative
monoid with zero, let $n \ge 1$ and $d$ be natural numbers with $d \mid n$, and let $\chi$ be a
Dirichlet character of level $n$ with values in $R$ whose conductor is $d$. If $\chi'$ is a
Dirichlet character of level $d$ whose change of level to $n$ is $\chi$, then $\chi'$ is the
primitive character associated to $\chi$.

Formalized by `DirichletCharacter.eq_primitiveCharacter_of_changeLevel_eq`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveUniqueness.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveUniqueness.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#eq-primitive-character-of-change-level-e).

## Existence and uniqueness of the primitive character inducing a Dirichlet character

Let
$R$ be a commutative monoid with zero, let $n \ge 1$, and let $\chi$ be a Dirichlet character of
level $n$ with values in $R$. The primitive character associated to $\chi$, whose level is the
conductor of $\chi$, is primitive, and its change of level to $n$ is $\chi$. Moreover, if
$\chi'$ is a primitive Dirichlet character of some level $d$ with $d \mid n$ whose change of level
to $n$ is $\chi$, then $d$ is the conductor of $\chi$ and $\chi'$ is the primitive character
associated to $\chi$.

Formalized by `DirichletCharacter.primitiveCharacter_isPrimitive_and_unique`, a theorem declared in [MathlibExt/NumberTheory/DirichletCharacter/PrimitiveUniqueness.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/DirichletCharacter/PrimitiveUniqueness.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html#primitive-character-is-primitive-and-uni).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conductors and primitive Dirichlet characters](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/conductors-and-primitive-dirichlet-characters)
