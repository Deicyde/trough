---
declaration: section
origin: cited
lean: groupCohomology.nonempty_linearEquiv_of_iso_res_mulEquiv, groupHomology.biprodIso, groupHomology.biprodIso_hom, groupHomology.biprodIso_inv, groupHomology.biprodIso_hom_fst, groupHomology.biprodIso_hom_snd, groupHomology.biprodIso_inv_inl, groupHomology.biprodIso_inv_inr
statement: formalized
proof: formalized
---

# Group homology and cohomology

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html).

## Invariance of group cohomology under group isomorphism

Group cohomology is invariant under group isomorphism.

Formalized by `groupCohomology.nonempty_linearEquiv_of_iso_res_mulEquiv`, a theorem declared in [MathlibExt/RepresentationTheory/GroupCohomology/Invariance.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/GroupCohomology/Invariance.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#nonempty-linear-equiv-of-iso-res-mul-equ).

## Group homology of a direct sum

Let $k$ be a commutative ring, $G$ a group, $A$ and $B$
representations of $G$ over $k$, and $n \in \mathbb{N}$, and write $H_n(G, M)$ for the $n$th group
homology of a representation $M$. This is the isomorphism
$H_n(G, A \oplus B) \cong H_n(G, A) \oplus H_n(G, B)$ obtained by applying the $n$th group homology
functor, which is additive, to the biproduct $A \oplus B$.

## Sources

- NumberTheoryI, Section 23.4, Corollary 23.22.

Formalized by `groupHomology.biprodIso`, a definition declared in [MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#biprod-iso).

## Forward map of the direct-sum isomorphism in group homology

Let $k$ be a commutative
ring, $G$ a group, $A$ and $B$ representations of $G$ over $k$, and $n \in \mathbb{N}$, and write
$H_n(G, M)$ for the $n$th group homology of a representation $M$. The forward map of the
isomorphism $H_n(G, A \oplus B) \cong H_n(G, A) \oplus H_n(G, B)$ is the map into the biproduct
whose components are the maps $H_n(G, A \oplus B) \to H_n(G, A)$ and
$H_n(G, A \oplus B) \to H_n(G, B)$ induced by the projections $A \oplus B \to A$ and
$A \oplus B \to B$.

Formalized by `groupHomology.biprodIso_hom`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#biprod-iso-hom).

## Inverse map of the direct-sum isomorphism in group homology

Let $k$ be a commutative
ring, $G$ a group, $A$ and $B$ representations of $G$ over $k$, and $n \in \mathbb{N}$, and write
$H_n(G, M)$ for the $n$th group homology of a representation $M$. The inverse map of the
isomorphism $H_n(G, A \oplus B) \cong H_n(G, A) \oplus H_n(G, B)$ is the map out of the biproduct
whose components are the maps $H_n(G, A) \to H_n(G, A \oplus B)$ and
$H_n(G, B) \to H_n(G, A \oplus B)$ induced by the inclusions $A \to A \oplus B$ and
$B \to A \oplus B$.

Formalized by `groupHomology.biprodIso_inv`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#biprod-iso-inv).

## Direct-sum isomorphism in group homology and the first projection

Let $k$ be a
commutative ring, $G$ a group, $A$ and $B$ representations of $G$ over $k$, and $n \in \mathbb{N}$,
and write $H_n(G, M)$ for the $n$th group homology of a representation $M$. The isomorphism
$H_n(G, A \oplus B) \cong H_n(G, A) \oplus H_n(G, B)$ followed by the projection onto $H_n(G, A)$
equals the map $H_n(G, A \oplus B) \to H_n(G, A)$ induced by the projection $A \oplus B \to A$.

Formalized by `groupHomology.biprodIso_hom_fst`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#biprod-iso-hom-fst).

## Direct-sum isomorphism in group homology and the second projection

Let $k$ be a
commutative ring, $G$ a group, $A$ and $B$ representations of $G$ over $k$, and $n \in \mathbb{N}$,
and write $H_n(G, M)$ for the $n$th group homology of a representation $M$. The isomorphism
$H_n(G, A \oplus B) \cong H_n(G, A) \oplus H_n(G, B)$ followed by the projection onto $H_n(G, B)$
equals the map $H_n(G, A \oplus B) \to H_n(G, B)$ induced by the projection $A \oplus B \to B$.

Formalized by `groupHomology.biprodIso_hom_snd`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#biprod-iso-hom-snd).

## Direct-sum isomorphism in group homology and the first inclusion

Let $k$ be a
commutative ring, $G$ a group, $A$ and $B$ representations of $G$ over $k$, and $n \in \mathbb{N}$,
and write $H_n(G, M)$ for the $n$th group homology of a representation $M$. The inclusion of
$H_n(G, A)$ into $H_n(G, A) \oplus H_n(G, B)$ followed by the inverse of the isomorphism
$H_n(G, A \oplus B) \cong H_n(G, A) \oplus H_n(G, B)$ equals the map
$H_n(G, A) \to H_n(G, A \oplus B)$ induced by the inclusion $A \to A \oplus B$.

Formalized by `groupHomology.biprodIso_inv_inl`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean, line 134](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean#L134). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#biprod-iso-inv-inl).

## Direct-sum isomorphism in group homology and the second inclusion

Let $k$ be a
commutative ring, $G$ a group, $A$ and $B$ representations of $G$ over $k$, and $n \in \mathbb{N}$,
and write $H_n(G, M)$ for the $n$th group homology of a representation $M$. The inclusion of
$H_n(G, B)$ into $H_n(G, A) \oplus H_n(G, B)$ followed by the inverse of the isomorphism
$H_n(G, A \oplus B) \cong H_n(G, A) \oplus H_n(G, B)$ equals the map
$H_n(G, B) \to H_n(G, A \oplus B)$ induced by the inclusion $B \to A \oplus B$.

Formalized by `groupHomology.biprodIso_inv_inr`, a theorem declared in [MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/RepresentationTheory/Homological/GroupHomology/Biproduct.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html#biprod-iso-inv-inr).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Group homology and cohomology](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/RepresentationTheory/group-cohomology/group-homology-and-cohomology)
