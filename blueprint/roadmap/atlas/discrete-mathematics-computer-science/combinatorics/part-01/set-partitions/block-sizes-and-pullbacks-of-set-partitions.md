---
declaration: section
origin: cited
lean: Finpartition.cardProd, Finpartition.card_le_of_mem_parts, Finpartition.one_le_card_of_mem_parts, Finpartition.card_lt_of_ne_top, Finpartition.eq_top_iff_card_parts_eq_one, Finpartition.card_parts_pos_iff, Finpartition.eq_bot_iff_card_parts_eq_card, Finpartition.cardProd_mapMonoidHom
statement: formalized
proof: formalized
---

# Block sizes and pullbacks of set partitions

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html).

## Product over block sizes

For a partition $P$ of a finite set $s$, a commutative monoid
$R$ and a function $f : \mathbb{N} \to R$, the block-size product of $f$ over $P$ is
$\prod_{B \in P} f(|B|)$, the product over the blocks $B$ of $P$ of $f$ applied to the
cardinality of $B$.

Formalized by `Finpartition.cardProd`, a definition declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#card-prod).

## Blocks are no larger than the ground set

If $P$ is a partition of a finite set $s$
and $B$ is a block of $P$, then $|B| \le |s|$.

Formalized by `Finpartition.card_le_of_mem_parts`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#card-le-of-mem-parts).

## Blocks are nonempty

Every block $B$ of a partition of a finite set $s$ satisfies
$|B| \ge 1$.

Formalized by `Finpartition.one_le_card_of_mem_parts`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#one-le-card-of-mem-parts).

## Blocks of a partition other than the coarsest are smaller than the ground set

Let $P$
be a partition of a finite set $s$ that is not the coarsest partition $\top$ of $s$ (the one
whose only block is $s$ when $s$ is nonempty). Then every block $B$ of $P$ satisfies
$|B| < |s|$.

Formalized by `Finpartition.card_lt_of_ne_top`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#card-lt-of-ne-top).

## Recognizing the one-block partition

If $P$ is a partition of a nonempty finite set
$s$, then $P$ is the coarsest partition $\top$ of $s$, whose only block is $s$, if and only if
$P$ has exactly one block.

Formalized by `Finpartition.eq_top_iff_card_parts_eq_one`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#eq-top-iff-card-parts-eq-one).

## A partition has a block exactly when its ground set is nonempty

A partition $P$ of a
finite set $s$ has at least one block, that is, its number of blocks is positive, if and only
if $s$ is nonempty.

Formalized by `Finpartition.card_parts_pos_iff`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#card-parts-pos-iff).

## Recognizing the partition into singletons by its number of blocks

A partition $P$ of a
finite set $s$ is the finest partition $\bot$ of $s$, whose blocks are the singletons $\{a\}$
for $a \in s$, if and only if the number of blocks of $P$ equals $|s|$.

Formalized by `Finpartition.eq_bot_iff_card_parts_eq_card`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#eq-bot-iff-card-parts-eq-card).

## Monoid homomorphisms preserve block-size products

Let $P$ be a partition of a finite
set $s$, let $R$ and $S$ be commutative monoids, let $f : \mathbb{N} \to R$, and let
$g : R \to S$ be a monoid homomorphism. Then
$g\bigl(\prod_{B \in P} f(|B|)\bigr) = \prod_{B \in P} g(f(|B|))$, where both products run
over the blocks $B$ of $P$.

Formalized by `Finpartition.cardProd_mapMonoidHom`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Card.lean, line 239](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Card.lean#L239). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#card-prod-map-monoid-hom).

## Pull-back of a finite partition along a map

The pull-back of a partition `P` of the finite type `β` along a map `f : α → β`:
the blocks are the nonempty preimages `f ⁻¹' B` of the blocks `B` of `P`.

Formalized by `Finpartition.comap`, a definition declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#comap).

## Blocks of a pulled-back partition

The blocks of `P.comap f` are the nonempty preimages of the blocks of `P`.

Formalized by `Finpartition.mem_comap_parts`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#mem-comap-parts).

## Pulling back a partition along the identity

Pulling back along the identity does nothing.

Formalized by `Finpartition.comap_refl`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#comap-refl).

## Pulling back a partition along a composite

Pulling back along a composite is pulling back twice.

Formalized by `Finpartition.comap_comap`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#comap-comap).

## Blocks of a partition pulled back along an equivalence

Along an equivalence `e`, the blocks of `P.comap e` are the images of the blocks of `P`
under `e.symm`.

Formalized by `Finpartition.parts_comap_equiv`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#parts-comap-equiv).

## Pull-back along an equivalence preserves the number of blocks

Pulling back along an equivalence preserves the number of blocks.

Formalized by `Finpartition.card_parts_comap_equiv`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#card-parts-comap-equiv).

## Pull-back along an equivalence preserves block-size products

Pulling back along an equivalence preserves every product over the block sizes.

Formalized by `Finpartition.cardProd_comap_equiv`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#card-prod-comap-equiv).

## Pulling back along an equivalence and its inverse

Pulling back along `e` and then along `e.symm` gives back the partition.

Formalized by `Finpartition.comap_symm_comap`, a theorem declared in [MathlibExt/Combinatorics/Finpartition/Comap.lean, line 120](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Finpartition/Comap.lean#L120). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html#comap-symm-comap).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Block sizes and pullbacks of set partitions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/set-partitions/block-sizes-and-pullbacks-of-set-partitions)
