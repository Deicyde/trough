---
declaration: section
origin: cited
lean: GroupRing.inversion, GroupRing.inversion_single, GroupRing.inversion_involution, GroupRing.InversionTwist, GroupRing.InversionTwist.equiv, GroupRing.InversionTwist.val_smul, GroupRing.InversionTwist.twistTwistEquiv
statement: formalized
proof: formalized
---

# Inversion on commutative group rings

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html).

## Group Ring

## Inversion on a group ring

Let $R$ be a commutative ring and $G$ a commutative group.
The inversion of the group ring $R[G]$ is the ring automorphism of $R[G]$ induced by the group
automorphism $g \mapsto g^{-1}$ of $G$: it sends $\sum_g r_g\, g$ to $\sum_g r_g\, g^{-1}$.

Formalized by `GroupRing.inversion`, a definition declared in [MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html#inversion).

## Inversion on basis elements

Let $R$ be a commutative ring and $G$ a commutative group.
For every $g \in G$ and $r \in R$, the inversion of the group ring $R[G]$ sends $r\, g$ to
$r\, g^{-1}$.

Formalized by `GroupRing.inversion_single`, a theorem declared in [MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html#inversion-single).

## Group-ring inversion is an involution

Let $R$ be a commutative ring, $G$ a commutative
group and $\iota$ the inversion of the group ring $R[G]$. For every $x \in R[G]$,
$\iota(\iota(x)) = x$.

Formalized by `GroupRing.inversion_involution`, a theorem declared in [MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html#inversion-involution).

## Inversion twist of a group-ring module

Let $R$ be a commutative ring, $G$ a commutative
group and $A$ a module over the group ring $R[G]$. The inversion twist of $A$ is a copy of $A$
with the same addition, on which $r \in R[G]$ acts by $a \mapsto \iota(r) \cdot a$, where $\iota$
is the inversion of $R[G]$ and $\cdot$ is the original action on $A$.

As a bare type, the inversion twist of any type $A$ is a copy of $A$; the addition and the
action above are defined when $A$ is an $R[G]$-module.

Formalized by `GroupRing.InversionTwist`, a structure declared in [MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html#inversion-twist).

## Underlying bijection of the inversion twist

For every type $A$, the map sending an
element of the inversion twist of $A$ to its underlying element of $A$ is a bijection, whose
inverse sends $a \in A$ to its copy in the twist.

Formalized by `GroupRing.InversionTwist.equiv`, a definition declared in [MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html#equiv).

## Scalar action on the inversion twist

Let $R$ be a commutative ring, $G$ a commutative
group and $A$ a module over the group ring $R[G]$. For every $r \in R[G]$ and every element $a$
of the inversion twist of $A$, with underlying element $\bar a \in A$, the underlying element of
$r \cdot a$ is $\iota(r) \cdot \bar a$, where $\iota$ is the inversion of $R[G]$ and $\cdot$ on
the right is the original action on $A$.

Formalized by `GroupRing.InversionTwist.val_smul`, a theorem declared in [MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html#val-smul).

## Twisting twice by inversion recovers the module

Let $R$ be a commutative ring, $G$ a
commutative group and $A$ a module over the group ring $R[G]$. The map sending an element of the
inversion twist of the inversion twist of $A$ to its underlying element of $A$ is an
$R[G]$-linear isomorphism.

Formalized by `GroupRing.InversionTwist.twistTwistEquiv`, a definition declared in [MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Algebra/MonoidAlgebra/InversionTwist.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html#twist-twist-equiv).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Inversion on commutative group rings](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/group-rings/inversion-on-commutative-group-rings)
