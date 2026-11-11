---
declaration: section
origin: cited
lean: FDRep.isIrreducible_of_simple, FDRep.finrank_eq_one_of_isMulCommutative, FDRep.rho_eq_character_smul_of_simple, FDRep.character_mul_of_simple, FDRep.characterMonoidHom, FDRep.coe_characterMonoidHom, FDRep.ofMonoidHom, FDRep.ofMonoidHom_ρ
statement: formalized
proof: formalized
---

# Representations of finite abelian groups

14 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html).

## Simple finite-dimensional representations of a monoid are irreducible

Let $k$ be a
field and let $G$ be a monoid. If a finite-dimensional representation $V$ of $G$ over $k$ is
simple as an object of the category of finite-dimensional representations of $G$ over $k$, then
$V$ is irreducible as a representation: $V \ne 0$, and the only subrepresentations of $V$ are $0$
and $V$.

Formalized by `FDRep.isIrreducible_of_simple`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#is-irreducible-of-simple).

## Simple finite-dimensional representations of commutative monoids are one-dimensional

Let $k$ be an algebraically closed field and let $G$ be a commutative monoid. Every
finite-dimensional representation $V$ of $G$ over $k$ that is simple as an object of the category
of finite-dimensional representations of $G$ over $k$ has dimension $1$ over $k$.

Formalized by `FDRep.finrank_eq_one_of_isMulCommutative`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#finrank-eq-one-of-is-mul-commutative).

## Simple representations of commutative monoids act by scalars

Let $k$ be an
algebraically closed field, $G$ a monoid with commutative multiplication, and $V$ a simple
finite-dimensional representation of $G$ over $k$ (a simple object of the category of
finite-dimensional representations), with action $\rho$ and character
$\chi_V(g) = \operatorname{tr} \rho(g)$. Then for every $g \in G$ the map $\rho(g)$ is scalar
multiplication by $\chi_V(g)$, that is, $\rho(g) = \chi_V(g) \cdot \mathrm{id}_V$.

Formalized by `FDRep.rho_eq_character_smul_of_simple`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#rho-eq-character-smul-of-simple).

## Characters of simple representations of commutative monoids are multiplicative

Let $k$
be an algebraically closed field, let $G$ be a commutative monoid, and let $V$ be a
finite-dimensional representation of $G$ over $k$ that is simple as an object of the category of
finite-dimensional representations of $G$ over $k$. Let $\chi_V : G \to k$ be the character of
$V$, where $\chi_V(g)$ is the trace of the action of $g$ on $V$. Then
$\chi_V(gh) = \chi_V(g)\,\chi_V(h)$ for all $g, h \in G$.

Formalized by `FDRep.character_mul_of_simple`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#character-mul-of-simple).

## The character of a simple representation as a monoid homomorphism

Let $k$ be an
algebraically closed field, let $G$ be a commutative monoid, and let $V$ be a finite-dimensional
representation of $G$ over $k$ that is simple as an object of the category of finite-dimensional
representations of $G$ over $k$. The character $\chi_V : G \to k$ of $V$, where $\chi_V(g)$ is the
trace of the action of $g$ on $V$, satisfies $\chi_V(1) = 1$ and $\chi_V(gh) = \chi_V(g)\,\chi_V(h)$
for all $g, h \in G$; this is $\chi_V$ regarded as a monoid homomorphism from $G$ to $k$.

Formalized by `FDRep.characterMonoidHom`, a definition declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#character-monoid-hom).

## The character homomorphism has the character as its underlying function

Let $k$ be an
algebraically closed field, let $G$ be a commutative monoid, and let $V$ be a finite-dimensional
representation of $G$ over $k$ that is simple as an object of the category of finite-dimensional
representations of $G$ over $k$. The character of $V$, regarded as a monoid homomorphism from $G$
to $k$, has the character $\chi_V : G \to k$ of $V$ as its underlying function, where $\chi_V(g)$
is the trace of the action of $g$ on $V$.

Formalized by `FDRep.coe_characterMonoidHom`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#coe-character-monoid-hom).

## The one-dimensional representation of a homomorphism

Let $k$ be a field, let $G$ be a
monoid, and let $\varphi : G \to k$ be a monoid homomorphism. This is the finite-dimensional
representation $k_\varphi$ of $G$ on the one-dimensional space $k$ in which each $g \in G$ acts by
multiplication by $\varphi(g)$, that is, by the linear map $x \mapsto \varphi(g)\,x$.

Formalized by `FDRep.ofMonoidHom`, a definition declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#of-monoid-hom).

## The action in the one-dimensional representation of a homomorphism

Let $k$ be a field,
let $G$ be a monoid, let $\varphi : G \to k$ be a monoid homomorphism, and let $k_\varphi$ be the
one-dimensional representation of $G$ on $k$ defined by $\varphi$. For every $g \in G$, the action
of $g$ on $k_\varphi$ is $\varphi(g)$ times the identity map of $k$.

Formalized by `FDRep.ofMonoidHom_ρ`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#of-monoid-hom-2).

## The representation of a homomorphism is one-dimensional

Let $k$ be a field, let $G$ be
a monoid, let $\varphi : G \to k$ be a monoid homomorphism, and let $k_\varphi$ be the
representation of $G$ on $k$ in which each $g \in G$ acts by multiplication by $\varphi(g)$. Then
$k_\varphi$ has dimension $1$ over $k$.

Formalized by `FDRep.ofMonoidHom_finrank`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 178](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L178). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#of-monoid-hom-finrank).

## The character of the representation of a homomorphism is the homomorphism

Let $k$ be a
field, let $G$ be a monoid, let $\varphi : G \to k$ be a monoid homomorphism, and let $k_\varphi$
be the one-dimensional representation of $G$ on $k$ in which each $g \in G$ acts by multiplication
by $\varphi(g)$. The character of $k_\varphi$ is $\varphi$: the trace of the action of each
$g \in G$ on $k_\varphi$ is $\varphi(g)$.

Formalized by `FDRep.ofMonoidHom_character`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#of-monoid-hom-character).

## The representation of a homomorphism is simple

Let $k$ be a field, let $G$ be a monoid,
let $\varphi : G \to k$ be a monoid homomorphism, and let $k_\varphi$ be the one-dimensional
representation of $G$ on $k$ in which each $g \in G$ acts by multiplication by $\varphi(g)$. Then
$k_\varphi$ is a simple object of the category of finite-dimensional representations of $G$ over
$k$.

Formalized by `FDRep.ofMonoidHom_simple`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#of-monoid-hom-simple).

## Characters of simple representations of a finite abelian group are homomorphisms

Let $G$
be a finite abelian group and let $V$ be a simple finite-dimensional complex representation of
$G$. Then there is a monoid homomorphism $\varphi : G \to \mathbb{C}$ such that the character of
$V$ equals $\varphi$.

Proof: Simplicity of $V$ makes it irreducible, and complex irreducible representations of an
abelian group are one-dimensional (the corollary in Wikipedia, “Schur's lemma”), so $V$ is
one-dimensional. Endomorphisms of a one-dimensional space are scalars, and their traces give the
multiplicative character.

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2.8 (degree-one characters of abelian groups).

Formalized by `MathlibExt.GroupTheory.AbelianRepresentationWanted.abelian_simple_char_is_hom`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 231](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L231). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#abelian-simple-char-is-hom).

## Every homomorphism of a finite abelian group to the complex numbers is a simple character

Let $G$ be a finite abelian group and let $\varphi : G \to \mathbb{C}$ be a monoid homomorphism.
Then there is a simple finite-dimensional complex representation $V$ of $G$ whose character
equals $\varphi$.

Proof: Let each $g \in G$ act on the one-dimensional space $\mathbb{C}$ by the scalar
$\varphi(g)$; its trace is $\varphi(g)$. One-dimensional modules are simple. Wikipedia,
“Representation theory of finite groups”, notes that the irreducible characters of an abelian
group are its homomorphisms to $\mathbb{C}^\times$.

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, Ch. I (one-dimensional representations from characters).

Formalized by `MathlibExt.GroupTheory.AbelianRepresentationWanted.abelian_hom_is_simple_char`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 251](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L251). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#abelian-hom-is-simple-char).

## Characters determine simple representations of a finite abelian group

Let $G$ be a finite
abelian group and let $V$ and $W$ be simple finite-dimensional complex representations of $G$,
with characters $\chi_V$ and $\chi_W$. If $\chi_V = \chi_W$, then $V$ and $W$ are isomorphic.

Proof: For functions $\chi, \psi : G \to \mathbb{C}$ write
$\langle \chi, \psi \rangle = \frac{1}{|G|} \sum_{g \in G} \chi(g)\,\psi(g^{-1})$, where $|G|$ is
the order of $G$. The orthonormality of irreducible characters gives
$\langle \chi_V, \chi_V \rangle = 1$. Replacing the second character by the equal character
$\chi_W$ gives $\langle \chi_V, \chi_W \rangle = 1$, which forces $V \cong W$. This is the
orthonormality of irreducible characters in Wikipedia, “Character theory”.

## Sources

- J.-P. Serre, Linear Representations of Finite Groups, GTM 42, §2.8 (characters determine representations of abelian groups).

Formalized by `MathlibExt.GroupTheory.AbelianRepresentationWanted.abelian_simple_iso_of_char_eq`, a theorem declared in [MathlibExt/GroupTheory/AbelianRepresentation.lean, line 289](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/AbelianRepresentation.lean#L289). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html#abelian-simple-iso-of-char-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representations of finite abelian groups](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RepresentationTheory/finite-group-representations/representations-of-finite-abelian-groups)
