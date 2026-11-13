---
declaration: section
origin: cited
lean: NumberField.Modulus.CongruenceSubgroup, NumberField.Modulus.CongruenceSubgroup.image, NumberField.Modulus.CongruenceSubgroup.mem_image_iff, NumberField.Modulus.CongruenceSubgroup.toAmbientSubgroup, NumberField.Modulus.CongruenceSubgroup.smallest, NumberField.Modulus.CongruenceSubgroup.largest, NumberField.Modulus.CongruenceSubgroupPair, NumberField.Modulus.CongruenceSubgroupPair.IsEquivalent
statement: formalized
proof: formalized
---

# Congruence subgroups for a modulus

20 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html).

## Congruence subgroup

Let $K$ be a number field and $\mathfrak m$ a modulus of $K$. A
congruence subgroup for $\mathfrak m$ is a subgroup $H$ of the group of invertible fractional
ideals of $K$ coprime to the finite part of $\mathfrak m$ such that $H$ contains the ray group
of $\mathfrak m$.

Formalized by `NumberField.Modulus.CongruenceSubgroup`, a structure declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#congruence-subgroup).

## Image of a congruence subgroup in the ray class group

Let $H$ be a congruence subgroup
for a modulus $\mathfrak m$ of a number field $K$, and let $\pi$ be the canonical projection from
the group of invertible fractional ideals of $K$ coprime to the finite part of $\mathfrak m$ onto
the ray class group of $\mathfrak m$. The image of $H$ is the subgroup $\pi(H)$ of the ray class
group.

Formalized by `NumberField.Modulus.CongruenceSubgroup.image`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#image).

## Membership in the image of a congruence subgroup

Let $H$ be a congruence subgroup for a
modulus $\mathfrak m$ of a number field $K$, and let $\pi$ be the canonical projection from the
group of invertible fractional ideals of $K$ coprime to the finite part of $\mathfrak m$ onto the
ray class group of $\mathfrak m$. An element $x$ of the ray class group lies in the image $\pi(H)$
if and only if $\pi(y) = x$ for some $y \in H$.

Formalized by `NumberField.Modulus.CongruenceSubgroup.mem_image_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#mem-image-iff).

## Congruence subgroup as a subgroup of all invertible fractional ideals

For a congruence
subgroup $H$ for a modulus $\mathfrak m$ of a number field $K$, this is the image of $H$ under the
inclusion of the group of invertible fractional ideals of $K$ coprime to the finite part of
$\mathfrak m$ into the group of all invertible fractional ideals of $K$.

Formalized by `NumberField.Modulus.CongruenceSubgroup.toAmbientSubgroup`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#to-ambient-subgroup).

## Smallest congruence subgroup

For a modulus $\mathfrak m$ of a number field $K$, the
smallest congruence subgroup for $\mathfrak m$ is the ray group of $\mathfrak m$ itself, a
subgroup of the group of invertible fractional ideals of $K$ coprime to the finite part of
$\mathfrak m$.

Formalized by `NumberField.Modulus.CongruenceSubgroup.smallest`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#smallest).

## Largest congruence subgroup

For a modulus $\mathfrak m$ of a number field $K$, the largest
congruence subgroup for $\mathfrak m$ is the whole group of invertible fractional ideals of $K$
coprime to the finite part of $\mathfrak m$, which contains the ray group of $\mathfrak m$.

Formalized by `NumberField.Modulus.CongruenceSubgroup.largest`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceSubgroup.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#largest).

## Congruence subgroup pair

Let $K$ be a number field. A congruence subgroup pair for $K$
consists of a modulus $\mathfrak m$ of $K$ together with a congruence subgroup for
$\mathfrak m$, that is, a subgroup of the group of invertible fractional ideals of $K$ coprime to
the finite part of $\mathfrak m$ that contains the ray group of $\mathfrak m$.

Formalized by `NumberField.Modulus.CongruenceSubgroupPair`, a structure declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#congruence-subgroup-pair).

## Equivalence of congruence subgroup pairs

Let $K$ be a number field. For a modulus
$\mathfrak m$ of $K$, write $I^{\mathfrak m}$ for the group of nonzero fractional ideals of $K$
coprime to the finite part of $\mathfrak m$. Two pairs $(\mathfrak m, H)$ and $(\mathfrak n, H')$,
each consisting of a modulus of $K$ and a congruence subgroup for it, are equivalent when
$I^{\mathfrak m} \cap H' = I^{\mathfrak n} \cap H$, where both congruence subgroups are viewed as
subgroups of the group of all nonzero fractional ideals of $K$.

Formalized by `NumberField.Modulus.CongruenceSubgroupPair.IsEquivalent`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#is-equivalent).

## Criterion for equivalence of congruence subgroup pairs

Let $K$ be a number field, and for
a modulus $\mathfrak m$ of $K$ write $I^{\mathfrak m}$ for the group of nonzero fractional ideals
of $K$ coprime to the finite part of $\mathfrak m$. Two pairs $(\mathfrak m, H)$ and
$(\mathfrak n, H')$, each consisting of a modulus of $K$ and a congruence subgroup for it, are
equivalent if and only if $I^{\mathfrak m} \cap H' = I^{\mathfrak n} \cap H$ in the group of all
nonzero fractional ideals of $K$.

Formalized by `NumberField.Modulus.CongruenceSubgroupPair.isEquivalent_iff`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#is-equivalent-iff).

## Equivalence of congruence subgroup pairs is reflexive

Let $K$ be a number field. Every
pair consisting of a modulus of $K$ and a congruence subgroup for it is equivalent to itself.

Formalized by `NumberField.Modulus.CongruenceSubgroupPair.IsEquivalent.refl`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#refl).

## Equivalence of congruence subgroup pairs is symmetric

Let $K$ be a number field. If a
pair $P$, consisting of a modulus of $K$ and a congruence subgroup for it, is equivalent to such
a pair $Q$, then $Q$ is equivalent to $P$.

Formalized by `NumberField.Modulus.CongruenceSubgroupPair.IsEquivalent.symm`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/CongruenceEquivalence.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#symm).

## Ray group among all fractional ideals

For a modulus $\mathfrak m$ of a number field
$K$, the ambient ray group of $\mathfrak m$ is the image of the ray group of $\mathfrak m$ under
the inclusion of the group of nonzero fractional ideals of $K$ coprime to the finite part of
$\mathfrak m$ into the group of all nonzero fractional ideals of $K$.

Formalized by `NumberField.Modulus.rayGroupAmbient`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#ray-group-ambient).

## The ray group consists of coprime ideals

For every modulus $\mathfrak m$ of a number
field $K$, the ray group of $\mathfrak m$, viewed as a subgroup of the group of nonzero
fractional ideals of $K$, is contained in the group of nonzero fractional ideals coprime to the
finite part of $\mathfrak m$.

Formalized by `NumberField.Modulus.rayGroupAmbient_le_coprime`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#ray-group-ambient-le-coprime).

## A congruence subgroup contains the ray group

Let $C$ be a congruence subgroup for a
modulus $\mathfrak m$ of a number field $K$. Viewed as subgroups of the group of nonzero
fractional ideals of $K$, the ray group of $\mathfrak m$ is contained in $C$.

Formalized by `NumberField.Modulus.CongruenceSubgroup.rayGroupAmbient_le_toAmbientSubgroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#ray-group-ambient-le-to-ambient-subgroup).

## Coprimality passes to divisors of a modulus

Let $\mathfrak m_1$ and $\mathfrak m_2$ be
moduli of a number field $K$ with $\mathfrak m_2 \mid \mathfrak m_1$. Then every nonzero
fractional ideal of $K$ coprime to the finite part of $\mathfrak m_1$ is coprime to the finite
part of $\mathfrak m_2$.

Formalized by `NumberField.Modulus.coprimeFractionalIdeals_le_of_dvd`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#coprime-fractional-ideals-le-of-dvd).

## Change of modulus of a congruence subgroup

Let $C_1$ be a congruence subgroup for a
modulus $\mathfrak m_1$ of a number field $K$, viewed as a subgroup of the group of nonzero
fractional ideals of $K$, and let $\mathfrak m_2$ be any modulus of $K$. Write
$I^{\mathfrak m_2}$ for the group of nonzero fractional ideals of $K$ coprime to the finite part
of $\mathfrak m_2$ and $P_{\mathfrak m_2} \subseteq I^{\mathfrak m_2}$ for the ray group of
$\mathfrak m_2$. The change of modulus of $C_1$ to $\mathfrak m_2$ is the congruence subgroup for
$\mathfrak m_2$ generated, inside $I^{\mathfrak m_2}$, by $C_1 \cap I^{\mathfrak m_2}$ and
$P_{\mathfrak m_2}$.

Formalized by `NumberField.Modulus.changeModulus`, a definition declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#change-modulus).

## Ambient subgroup of a change of modulus

Let $\mathfrak m_1$ and $\mathfrak m_2$ be
moduli of a number field $K$ and let $C_1$ be a congruence subgroup for $\mathfrak m_1$. Write
$I^{\mathfrak m_2}$ for the group of nonzero fractional ideals of $K$ coprime to the finite part
of $\mathfrak m_2$ and $P_{\mathfrak m_2}$ for the ray group of $\mathfrak m_2$. Viewing all of
these as subgroups of the group of nonzero fractional ideals of $K$, the change of modulus of
$C_1$ to $\mathfrak m_2$ is the subgroup generated by $C_1 \cap I^{\mathfrak m_2}$ and
$P_{\mathfrak m_2}$.

Formalized by `NumberField.Modulus.changeModulus_toAmbientSubgroup`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#change-modulus-to-ambient-subgroup).

## Ambient subgroup of a change of modulus to a divisor

Let $\mathfrak m_1$ and
$\mathfrak m_2$ be moduli of a number field $K$ with $\mathfrak m_2 \mid \mathfrak m_1$, and let
$C_1$ be a congruence subgroup for $\mathfrak m_1$. Viewed as subgroups of the group of nonzero
fractional ideals of $K$, the change of modulus of $C_1$ to $\mathfrak m_2$ equals the subgroup
generated by $C_1$ and the ray group $P_{\mathfrak m_2}$ of $\mathfrak m_2$.

Formalized by `NumberField.Modulus.changeModulus_toAmbientSubgroup_of_dvd`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#change-modulus-to-ambient-subgroup-of-dv).

## The change of modulus is equivalent to the original pair

Let $\mathfrak m_1$ and
$\mathfrak m_2$ be moduli of a number field $K$ with $\mathfrak m_2 \mid \mathfrak m_1$, and let
$C_1$ be a congruence subgroup for $\mathfrak m_1$. Write $I^{\mathfrak m_1}$ for the group of
nonzero fractional ideals of $K$ coprime to the finite part of $\mathfrak m_1$ and
$P_{\mathfrak m_2}$ for the ray group of $\mathfrak m_2$, and view all of these as subgroups of
the group of nonzero fractional ideals of $K$. If
$I^{\mathfrak m_1} \cap P_{\mathfrak m_2} \subseteq C_1$, then the pair $(\mathfrak m_1, C_1)$ is
equivalent to the pair $(\mathfrak m_2, C_2)$, where $C_2$ is the change of modulus of $C_1$ to
$\mathfrak m_2$.

Formalized by `NumberField.Modulus.changeModulus_isEquivalent`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#change-modulus-is-equivalent).

## Criterion for an equivalent congruence subgroup at a divisor of the modulus

Let
$\mathfrak m_1$ and $\mathfrak m_2$ be moduli of a number field $K$ with
$\mathfrak m_2 \mid \mathfrak m_1$, and let $C_1$ be a congruence subgroup for $\mathfrak m_1$.
Write $I^{\mathfrak m_1}$ for the group of nonzero fractional ideals of $K$ coprime to the finite
part of $\mathfrak m_1$ and $P_{\mathfrak m_2}$ for the ray group of $\mathfrak m_2$, and view all
of these as subgroups of the group of nonzero fractional ideals of $K$. Then there is a
congruence subgroup $C_2$ for $\mathfrak m_2$ such that the pair $(\mathfrak m_1, C_1)$ is
equivalent to the pair $(\mathfrak m_2, C_2)$ if and only if
$I^{\mathfrak m_1} \cap P_{\mathfrak m_2} \subseteq C_1$.

## Sources

- ATLAS NumberTheoryI item N422, Lemma 22.5.

Formalized by `NumberField.Modulus.exists_equivalent_iff_changeModulus`, a theorem declared in [MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/RayClass/ChangeModulus.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html#exists-equivalent-iff-change-modulus).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Congruence subgroups for a modulus](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/adeles-class-field-theory/congruence-subgroups-for-a-modulus)
