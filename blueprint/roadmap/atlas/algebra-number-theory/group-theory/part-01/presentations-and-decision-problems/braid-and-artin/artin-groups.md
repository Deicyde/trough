---
declaration: section
origin: cited
lean: CoxeterMatrix.alternatingWord, CoxeterMatrix.map_alternatingWord, CoxeterMatrix.artinRelation, CoxeterMatrix.artinRelationsSet, CoxeterMatrix.ArtinGroup, CoxeterMatrix.ArtinGroup.of, CoxeterMatrix.ArtinGroup.closure_range_of, CoxeterMatrix.ArtinGroup.braid_relation
statement: formalized
proof: formalized
---

# Artin groups

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html).

## Coxeter Matrix

## Alternating word

For elements $a$ and $b$ of a monoid and $n \in \mathbb{N}$, the
alternating word of length $n$ starting with $a$ is the product $a b a b \cdots$ of $n$ factors
that alternate between $a$ and $b$, beginning with $a$; for $n = 0$ it is the identity.

Formalized by `CoxeterMatrix.alternatingWord`, a definition declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#alternating-word).

## Monoid homomorphisms preserve alternating words

Let $f : G \to H$ be a homomorphism of
monoids. For all $a, b \in G$ and $n \in \mathbb{N}$, $f$ maps the alternating word $a b a \cdots$
of length $n$ starting with $a$ to the alternating word $f(a) f(b) f(a) \cdots$ of length $n$
starting with $f(a)$.

Formalized by `CoxeterMatrix.map_alternatingWord`, a theorem declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#map-alternating-word).

## Artin relator

Let $M = (m_{ij})$ be a Coxeter matrix over an index type $B$, and write
$s_i$ for the free generators of the free group on $B$. For $i, j \in B$, let $u$ and $v$ be the
alternating words $s_i s_j s_i \cdots$ and $s_j s_i s_j \cdots$ of length $m_{ij}$. The Artin
relator of the ordered pair $(i, j)$ is the element $u v^{-1}$ of the free group; setting it equal
to $1$ imposes the braid relation $u = v$.

Formalized by `CoxeterMatrix.artinRelation`, a definition declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#artin-relation).

## Artin relators of a Coxeter matrix

Let $M = (m_{ij})$ be a Coxeter matrix over an index
type $B$, where $m_{ij} = 0$ encodes $m_{ij} = \infty$, and write $s_i$ for the free generators of
the free group on $B$. The set of Artin relators of $M$ consists of the elements $u v^{-1}$ of the
free group, one for each ordered pair of distinct $i, j \in B$ with $m_{ij} \neq 0$, where $u$ and
$v$ are the alternating words $s_i s_j s_i \cdots$ and $s_j s_i s_j \cdots$ of length $m_{ij}$.
Pairs with $m_{ij} = \infty$ contribute no relator.

Formalized by `CoxeterMatrix.artinRelationsSet`, a definition declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#artin-relations-set).

## Artin group

Let $M = (m_{ij})_{i, j \in B}$ be a Coxeter matrix over an index type $B$,
where $m_{ij} = 0$ encodes $m_{ij} = \infty$. The Artin group (Artin–Tits group) of $M$ is the
group presented by generators $s_i$, one for each $i \in B$, subject only to the braid relations:
for every ordered pair of distinct $i, j \in B$ with $m_{ij} \neq 0$, the alternating words
$s_i s_j s_i \cdots$ and $s_j s_i s_j \cdots$ of length $m_{ij}$ are equal. Unlike for the
Coxeter group of $M$, no relations $s_i^2 = 1$ are imposed.

Formalized by `CoxeterMatrix.ArtinGroup`, a definition declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#artin-group).

## Generators of the Artin group

For a Coxeter matrix $M$ over an index type $B$ and
$i \in B$, the generator $s_i$ of the Artin group of $M$ is the image of the free generator $i$
under the quotient map from the free group on $B$ onto the Artin group.

Formalized by `CoxeterMatrix.ArtinGroup.of`, a definition declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 109](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L109). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#of).

## The generators generate the Artin group

For a Coxeter matrix $M$ over an index type $B$,
the subgroup of the Artin group of $M$ generated by its generators $s_i$, $i \in B$, is the whole
group.

Formalized by `CoxeterMatrix.ArtinGroup.closure_range_of`, a theorem declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#closure-range-of).

## Braid relations in the Artin group

Let $M = (m_{ij})$ be a Coxeter matrix over an index
type $B$, where $m_{ij} = 0$ encodes $m_{ij} = \infty$, and let $s_i$ ($i \in B$) be the
generators of the Artin group of $M$. For distinct $i, j \in B$ with $m_{ij} \neq 0$, the
alternating words $s_i s_j s_i \cdots$ and $s_j s_i s_j \cdots$ of length $m_{ij}$ are equal in
the Artin group.

Formalized by `CoxeterMatrix.ArtinGroup.braid_relation`, a theorem declared in [MathlibExt/GroupTheory/ArtinGroup.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/GroupTheory/ArtinGroup.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html#braid-relation).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Artin groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/presentations-and-decision-problems/braid-and-artin/artin-groups)
