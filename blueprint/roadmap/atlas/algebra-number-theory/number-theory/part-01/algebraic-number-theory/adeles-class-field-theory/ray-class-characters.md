---
declaration: section
origin: cited
lean: NumberField.Modulus.RayClassCharacter, NumberField.Modulus.trivialCharacter, NumberField.Modulus.pullback, NumberField.Modulus.pullback_eq_one_of_mem_rayGroup, NumberField.Modulus.evalComplex, NumberField.Modulus.evalComplex_rayGroup, NumberField.Modulus.extendByZero, NumberField.Modulus.finiteExponent_le_of_dvd
statement: formalized
proof: formalized
---

# Ray class characters

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html).

## Ray class character

A ray class character of a modulus $m$ of a number field $K$ is a
group homomorphism from the ray class group of $m$ to the unit circle
$\{z \in \mathbb C : |z| = 1\}$.

Formalized by `NumberField.Modulus.RayClassCharacter`, an abbreviation declared in [MathlibExt/NumberTheory/NumberField/RayClass/Character.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Character.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#ray-class-character).

## Trivial character

The trivial ray class character of a modulus $m$ of a number field $K$
is the ray class character sending every ray class of $m$ to $1$.

Formalized by `NumberField.Modulus.trivialCharacter`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/Character.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Character.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#trivial-character).

## Pullback of a ray class character to ideals

For a ray class character $\chi$ of a
modulus $m$ of a number field $K$, its pullback is the group homomorphism from the group of
nonzero fractional ideals of $K$ coprime to the finite part of $m$ to the unit circle sending
$\mathfrak a$ to $\chi([\mathfrak a])$, where $[\mathfrak a]$ is the ray class of $\mathfrak a$.

Formalized by `NumberField.Modulus.pullback`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/Character.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Character.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#pullback).

## Pulled-back ray class characters are trivial on the ray group

Let $\chi$ be a ray class
character of a modulus $m$ of a number field $K$. If a nonzero fractional ideal $\mathfrak a$ of
$K$ coprime to the finite part of $m$ lies in the ray group of $m$, then the pullback of $\chi$ to
the fractional ideals coprime to the finite part of $m$ takes the value $1$ at $\mathfrak a$.

Formalized by `NumberField.Modulus.pullback_eq_one_of_mem_rayGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/Character.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Character.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#pullback-eq-one-of-mem-ray-group).

## Complex value of a ray class character

For a ray class character $\chi$ of a modulus $m$
and a ray class $x$ of $m$, the complex value of $\chi$ at $x$ is $\chi(x)$, a point of the unit
circle, regarded as a complex number.

Formalized by `NumberField.Modulus.evalComplex`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/Character.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Character.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#eval-complex).

## Ray class characters take the complex value $1$ on the ray group

Let $m$ be a modulus
of a number field $K$ and $\chi$ a ray class character of $m$. If a nonzero fractional ideal
$\mathfrak a$ of $K$ coprime to the finite part of $m$ lies in the ray group of $m$, then the value
of $\chi$ at the ray class of $\mathfrak a$, regarded as a complex number, is $1$.

Formalized by `NumberField.Modulus.evalComplex_rayGroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/Character.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Character.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#eval-complex-ray-group).

## Extension by zero of a ray class character

Let $\chi$ be a ray class character of a
modulus $m$ of a number field $K$. Its extension by zero assigns to a nonzero fractional ideal
$\mathfrak a$ of $K$ the complex number $\chi([\mathfrak a])$ if $\mathfrak a$ is coprime to the
finite part of $m$, where $[\mathfrak a]$ is the ray class of $\mathfrak a$, and the value $0$
otherwise.

Formalized by `NumberField.Modulus.extendByZero`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/Character.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/Character.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#extend-by-zero).

## Exponents of a modulus grow under divisibility

Let $m_1$ and $m_2$ be moduli of a number
field $K$ with $m_1 \mid m_2$, that is, the finite part of $m_2$ is contained in the finite part
of $m_1$ and every real place of $m_1$ is a real place of $m_2$. Then for every finite prime $v$
of $K$ (a height-one prime of the ring of integers $\mathcal{O}_K$), the exponent of $v$ in the
finite part of $m_1$ is at most the exponent of $v$ in the finite part of $m_2$.

Formalized by `NumberField.Modulus.finiteExponent_le_of_dvd`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#finite-exponent-le-of-dvd).

## Inclusion of coprime ideal groups under divisibility of moduli

Let $m_1$ and $m_2$ be
moduli of a number field $K$ with $m_1 \mid m_2$, that is, the finite part of $m_2$ is contained
in the finite part of $m_1$ and every real place of $m_1$ is a real place of $m_2$. Then every
fractional ideal of $K$ coprime to $m_2$ is coprime to $m_1$, and this map is the inclusion
homomorphism from the group of fractional ideals coprime to $m_2$ into the group of fractional
ideals coprime to $m_1$.

Formalized by `NumberField.Modulus.coprimeInclusion`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#coprime-inclusion).

## Ray congruence to $1$ passes to divisors of the modulus

Let $m_1$ and $m_2$ be moduli
of a number field $K$ with $m_1 \mid m_2$, that is, the finite part of $m_2$ is contained in the
finite part of $m_1$ and every real place of $m_1$ is a real place of $m_2$. If a nonzero element
$x$ of $K$ is congruent to $1$ modulo $m_2$ in the ray sense (its principal ideal is coprime to
$m_2$, for each prime $v$ dividing the finite part of $m_2$ either $x = 1$ or the exponent of
$v$ in $x - 1$ is at least its exponent in that finite part, and $x$ is positive at every real
place of $m_2$), then $x$ is congruent to $1$ modulo $m_1$ in the same sense.

Formalized by `NumberField.Modulus.IsRayElementOne.of_dvd`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#of-dvd).

## Level-change map on ray class groups

Let $m_1$ and $m_2$ be moduli of a number field $K$
with $m_1 \mid m_2$, that is, the finite part of $m_2$ is contained in the finite part of $m_1$
and every real place of $m_1$ is a real place of $m_2$. The inclusion of the group of fractional
ideals coprime to $m_2$ into the group of fractional ideals coprime to $m_1$ maps the ray group
modulo $m_2$ into the ray group modulo $m_1$, so it induces a group homomorphism from the ray
class group modulo $m_2$ to the ray class group modulo $m_1$, sending the class of an ideal
modulo $m_2$ to its class modulo $m_1$.

Formalized by `NumberField.Modulus.RayClassGroup.mapOfDvd`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#map-of-dvd).

## The level-change map on ray classes

Let $m_1$ and $m_2$ be moduli of a number field $K$
with $m_1 \mid m_2$, that is, the finite part of $m_2$ is contained in the finite part of $m_1$
and every real place of $m_1$ is a real place of $m_2$. For every fractional ideal
$\mathfrak{a}$ of $K$ coprime to $m_2$, the level-change homomorphism from the ray class group
modulo $m_2$ to the ray class group modulo $m_1$ sends the ray class of $\mathfrak{a}$ modulo
$m_2$ to the ray class of $\mathfrak{a}$ modulo $m_1$ (an ideal coprime to $m_2$ is also coprime
to $m_1$).

Formalized by `NumberField.Modulus.RayClassGroup.mapOfDvd_rayClassMap`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#map-of-dvd-ray-class-map).

## Induced ray class character

Let $m_1$ and $m_2$ be moduli of a number field $K$ with
$m_1 \mid m_2$, that is, the finite part of $m_2$ is contained in the finite part of $m_1$ and
every real place of $m_1$ is a real place of $m_2$. A ray class character $\chi_2$ modulo $m_2$
is induced by a ray class character $\chi_1$ modulo $m_1$ when $\chi_2 = \chi_1 \circ \pi$, where
$\pi$ is the level-change homomorphism from the ray class group modulo $m_2$ to the ray class
group modulo $m_1$ that sends the class of an ideal coprime to $m_2$ to its class modulo
$m_1$.

Formalized by `NumberField.Modulus.RayClassCharacter.IsInducedBy`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#is-induced-by).

## Induced characters agree on coprime ideals

Let $m_1$ and $m_2$ be moduli of a number
field $K$ with $m_1 \mid m_2$, that is, the finite part of $m_2$ is contained in the finite part
of $m_1$ and every real place of $m_1$ is a real place of $m_2$. Let $\chi_1$ be a ray class
character modulo $m_1$ and $\chi_2$ a ray class character modulo $m_2$. Then $\chi_2$ is induced
by $\chi_1$ if and only if, for every fractional ideal $\mathfrak{a}$ of $K$ coprime to $m_2$,
the value of $\chi_2$ on the ray class of $\mathfrak{a}$ modulo $m_2$ equals the value of
$\chi_1$ on the ray class of $\mathfrak{a}$ modulo $m_1$ (an ideal coprime to $m_2$ is also
coprime to $m_1$).

Formalized by `NumberField.Modulus.RayClassCharacter.isInducedBy_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#is-induced-by-iff).

## Primitive ray class character

Let $m$ be a modulus of a number field $K$. A ray class
character $\chi$ modulo $m$ is primitive when, for every modulus $m_0$ of $K$ with $m_0 \mid m$
(the finite part of $m$ is contained in the finite part of $m_0$ and every real place of $m_0$
is a real place of $m$) and every ray class character $\chi_0$ modulo $m_0$ by which $\chi$ is
induced, $m_0 = m$.

Formalized by `NumberField.Modulus.RayClassCharacter.IsPrimitive`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#is-primitive).

## Primitivity in terms of the level-change map

Let $m$ be a modulus of a number field $K$.
A ray class character $\chi$ modulo $m$ is primitive if and only if, for every modulus $m_0$ of
$K$ with $m_0 \mid m$ (the finite part of $m$ is contained in the finite part of $m_0$ and every
real place of $m_0$ is a real place of $m$) and every ray class character $\chi_0$ modulo $m_0$
with $\chi = \chi_0 \circ \pi$, where $\pi$ is the level-change homomorphism from the ray class
group modulo $m$ to the ray class group modulo $m_0$, we have $m_0 = m$.

Formalized by `NumberField.Modulus.RayClassCharacter.isPrimitive_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/InducedCharacter.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html#is-primitive-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ray class characters](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/ray-class-characters)
