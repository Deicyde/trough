---
declaration: section
origin: cited
lean: SimpleGraph.IsDominating, SimpleGraph.IsIndepDominating, SimpleGraph.dominationNumber, SimpleGraph.indepDominationNumber, SimpleGraph.exists_isIndepDominating, SimpleGraph.exists_indepDominationNumber_eq_card, SimpleGraph.indepDominationNumber_le_card, SimpleGraph.exists_dominationNumber_eq_card
statement: formalized
proof: formalized
---

# Dominating sets

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html).

## Dominating set

A set $S$ of vertices of a simple graph $G$ dominates $G$ when every vertex
of $G$ lies in $S$ or is adjacent to some vertex of $S$.

Formalized by `SimpleGraph.IsDominating`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 21](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L21). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#is-dominating).

## Independent dominating set

A set $S$ of vertices of a simple graph $G$ is an independent
dominating set of $G$ when no two vertices of $S$ are adjacent and $S$ dominates $G$.

Formalized by `SimpleGraph.IsIndepDominating`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#is-indep-dominating).

## Domination number

For a simple graph $G$ on a finite vertex set, the domination number of
$G$ is the least number of elements of a dominating set of $G$.

Formalized by `SimpleGraph.dominationNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#domination-number).

## Independent domination number

For a simple graph $G$ on a finite vertex set, the
independent domination number of $G$ is the least number of elements of an independent dominating
set of $G$.

Formalized by `SimpleGraph.indepDominationNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#indep-domination-number).

## Existence of independent dominating sets

Every finite graph has an independent dominating
set.

Formalized by `SimpleGraph.exists_isIndepDominating`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#exists-is-indep-dominating).

## A minimum independent dominating set exists

Every simple graph $G$ on a finite vertex set
has an independent dominating set whose number of elements equals the independent domination
number of $G$.

Formalized by `SimpleGraph.exists_indepDominationNumber_eq_card`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#exists-indep-domination-number-eq-card).

## Independent dominating sets are at least as large as the independent domination number

Let $G$ be a simple graph on a finite vertex set. If $S$ is an independent dominating set of $G$,
then the independent domination number of $G$ is at most the number of elements of $S$.

Formalized by `SimpleGraph.indepDominationNumber_le_card`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#indep-domination-number-le-card).

## A minimum dominating set exists

Every simple graph $G$ on a finite vertex set has a
dominating set whose number of elements equals the domination number of $G$.

Formalized by `SimpleGraph.exists_dominationNumber_eq_card`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#exists-domination-number-eq-card).

## Dominating sets are at least as large as the domination number

Let $G$ be a simple graph
on a finite vertex set. If $S$ is a dominating set of $G$, then the domination number of $G$ is at
most the number of elements of $S$.

Formalized by `SimpleGraph.dominationNumber_le_card`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/Domination.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/Domination.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html#domination-number-le-card).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dominating sets](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/independence-and-domination/dominating-sets/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/independence-and-domination/dominating-sets)
