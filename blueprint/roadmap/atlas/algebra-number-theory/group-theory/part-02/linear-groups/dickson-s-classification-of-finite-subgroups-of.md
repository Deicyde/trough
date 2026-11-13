---
declaration: section
origin: cited
lean: MetaMathlibExt.Dickson.K, MetaMathlibExt.Dickson.PGL, MetaMathlibExt.Dickson.PSL, MetaMathlibExt.Dickson.classification_tame, MetaMathlibExt.Dickson.projGenLinGroup_map_injective, MetaMathlibExt.Dickson.card_projGenLinGroup_fin_two, MetaMathlibExt.Dickson.card_projectiveSpecialLinearGroup_fin_two, MetaMathlibExt.Dickson.orderOf_eq_char_of_char_dvd
statement: formalized
proof: formalized
---

# Dickson's classification of finite subgroups of PGL₂

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html).

## Algebraic closure of the field with p elements

For a prime $p$, $K_p$ denotes a fixed
algebraic closure of the finite field $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$.

Formalized by `MetaMathlibExt.Dickson.K`, an abbreviation declared in [MathlibExt/GroupTheory/DicksonPGL2Tame.lean, line 782](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Tame.lean#L782). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#k).

## Projective general linear group of degree two

For a prime $p$, $\mathrm{PGL}_2(K_p)$ is
the quotient of the group $\mathrm{GL}_2(K_p)$ of invertible $2 \times 2$ matrices over the
algebraic closure $K_p$ of $\mathbb{F}_p$ by its center.

Formalized by `MetaMathlibExt.Dickson.PGL`, an abbreviation declared in [MathlibExt/GroupTheory/DicksonPGL2Tame.lean, line 785](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Tame.lean#L785). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#pgl).

## Projective special linear group of degree two

For a prime $p$, $\mathrm{PSL}_2(K_p)$ is
the quotient of the group $\mathrm{SL}_2(K_p)$ of $2 \times 2$ matrices of determinant $1$ over
the algebraic closure $K_p$ of $\mathbb{F}_p$ by its center.

Formalized by `MetaMathlibExt.Dickson.PSL`, an abbreviation declared in [MathlibExt/GroupTheory/DicksonPGL2Tame.lean, line 788](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Tame.lean#L788). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#psl).

## Dickson's classification, tame case

Let $p$ be an odd prime and let $K$ be an algebraic
closure of $\mathbb{F}_p$. Every finite nontrivial subgroup $G$ of $\mathrm{PGL}_2(K)$ whose order
is not divisible by $p$ is cyclic, or isomorphic to the dihedral group of order $2n$ for some
$n \ge 2$, or isomorphic to one of the groups $A_4$, $S_4$, $A_5$.

Proof: Klein's orbit count on the projective line, followed by identification
of the resulting orbit signatures.

## Sources

- L. E. Dickson, *Linear Groups with an Exposition of the Galois Field Theory*, Teubner (1901).

Formalized by `MetaMathlibExt.Dickson.classification_tame`, a theorem declared in [MathlibExt/GroupTheory/DicksonPGL2Tame.lean, line 1996](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Tame.lean#L1996). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#classification-tame).

## Injective ring maps induce injective maps of $\mathrm{PGL}_n$

Let $f : R \to S$ be an
injective homomorphism of commutative rings and let $n$ be a finite index set. Then the
homomorphism $\mathrm{PGL}_n(R) \to \mathrm{PGL}_n(S)$ induced by applying $f$ to matrix entries
is injective, where $\mathrm{PGL}_n(R)$ denotes $\mathrm{GL}_n(R)$ modulo its center.

Formalized by `MetaMathlibExt.Dickson.projGenLinGroup_map_injective`, a theorem declared in [MathlibExt/GroupTheory/DicksonPGL2Wild.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Wild.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#proj-gen-lin-group-map-injective).

## Order of $\mathrm{PGL}_2$ over a finite field

If $F$ is a finite field with $q$ elements,
then the projective general linear group $\mathrm{PGL}_2(F)$ has order $q(q^2 - 1)$.

Formalized by `MetaMathlibExt.Dickson.card_projGenLinGroup_fin_two`, a theorem declared in [MathlibExt/GroupTheory/DicksonPGL2Wild.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Wild.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#card-proj-gen-lin-group-fin-two).

## Order of $\mathrm{PSL}_2$ over a finite field of odd characteristic

Let $F$ be a finite
field with $q$ elements whose characteristic $p$ is not $2$. Then the projective special linear
group $\mathrm{PSL}_2(F)$ has order $q(q^2 - 1)/2$.

Formalized by `MetaMathlibExt.Dickson.card_projectiveSpecialLinearGroup_fin_two`, a theorem declared in [MathlibExt/GroupTheory/DicksonPGL2Wild.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Wild.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#card-projective-special-linear-group-fin).

## Elements of $\mathrm{PGL}_2$ of order divisible by the characteristic

Let $p$ be an odd
prime and let $F$ be a field of characteristic $p$. If an element $g$ of $\mathrm{PGL}_2(F)$ has
finite order and $p$ divides the order of $g$, then the order of $g$ is $p$.

Formalized by `MetaMathlibExt.Dickson.orderOf_eq_char_of_char_dvd`, a theorem declared in [MathlibExt/GroupTheory/DicksonPGL2Wild.lean, line 959](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Wild.lean#L959). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#order-of-eq-char-of-char-dvd).

## Dickson's classification, wild case

Let $p$ be an odd prime, let $K$ be an algebraic
closure of $\mathbb{F}_p$, and let $G$ be a finite subgroup of $\mathrm{PGL}_2(K)$ whose order
is divisible by $p$. Then at least one of the following holds. (a) There are natural numbers
$m \ge 1$ and $t$ with $t$ coprime to $p$ and $t \mid p^m - 1$, and an injective homomorphism
$\varphi$ from the cyclic group $\mathbb{Z}/t\mathbb{Z}$ to the automorphism group of the
additive group $\mathbb{F}_p^m$ such that $\varphi(c)$ fixes no nonzero vector of
$\mathbb{F}_p^m$ for every $c \ne 0$, and $G$ is isomorphic to the semidirect product
$\mathbb{F}_p^m \rtimes_\varphi \mathbb{Z}/t\mathbb{Z}$. (b) $G$ is isomorphic to
$\mathrm{PSL}_2(\mathbb{F}_{p^m})$ for some $m \ge 1$, where $\mathbb{F}_{p^m}$ is the field
with $p^m$ elements. (c) $G$ is isomorphic to $\mathrm{PGL}_2(\mathbb{F}_{p^m})$ for some
$m \ge 1$. (d) $p = 3$ and $G$ is isomorphic to the alternating group $A_5$.

In the source, the first case is a group of maps $z \mapsto az + b$ with $a$ a root of unity;
only the resulting abstract group structure is recorded here.

Proof: We follow X. Faber, *Finite p-irregular subgroups of $\mathrm{PGL}_2(k)$*,
arXiv:1112.1999, §6, using the Sylow normal form, exceptional-orbit count, and projective-line
actions to identify the $\mathrm{PSL}_2$, $\mathrm{PGL}_2$, and $A_5$ cases.

## Sources

- L. E. Dickson, *Linear Groups with an Exposition of the Galois Field Theory*, Teubner (1901).

Formalized by `MetaMathlibExt.Dickson.classification_wild`, a theorem declared in [MathlibExt/GroupTheory/DicksonPGL2Wild.lean, line 6566](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/DicksonPGL2Wild.lean#L6566). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html#classification-wild).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dickson's classification of finite subgroups of PGL₂](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/linear-groups/dickson-s-classification-of-finite-subgroups-of)
