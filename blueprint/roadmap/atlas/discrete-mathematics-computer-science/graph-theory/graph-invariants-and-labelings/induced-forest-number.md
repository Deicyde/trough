---
declaration: section
origin: cited
lean: SimpleGraph.inducedForestNumber, SimpleGraph.card_le_inducedForestNumber, SimpleGraph.inducedForestNumber_le_card, SimpleGraph.exists_isAcyclic_card_eq_inducedForestNumber
statement: formalized
proof: formalized
---

# Induced forest number

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/induced-forest-number/index.html).

## Induced forest number

For a simple graph $G$ on a finite vertex set $V$, the induced
forest number $a(G)$ is the maximum number of vertices of an induced forest in $G$, that is, the
maximum cardinality of a set $S \subseteq V$ such that the subgraph of $G$ induced on $S$ is
acyclic.

## Sources

- H. Jung, A 15/31 Counterexample Family to the Albertson--Berman Conjecture, arXiv:2608.17350v1, the definition of $a(G)$.

Formalized by `SimpleGraph.inducedForestNumber`, a definition declared in [MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/induced-forest-number/index.html#induced-forest-number).

## Induced forests are no larger than the induced forest number

Let $G$ be a simple graph
on a finite vertex set $V$. For every set $S \subseteq V$ such that the subgraph of $G$ induced
on $S$ is acyclic, $|S|$ is at most the induced forest number of $G$.

Formalized by `SimpleGraph.card_le_inducedForestNumber`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/induced-forest-number/index.html#card-le-induced-forest-number).

## The induced forest number is at most the number of vertices

For every simple graph $G$
on a finite vertex set $V$, the induced forest number of $G$ is at most $|V|$.

Formalized by `SimpleGraph.inducedForestNumber_le_card`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/induced-forest-number/index.html#induced-forest-number-le-card).

## The induced forest number is attained

For every simple graph $G$ on a finite vertex set
$V$, there is a set $S \subseteq V$ such that the subgraph of $G$ induced on $S$ is acyclic and
$|S|$ equals the induced forest number of $G$.

Formalized by `SimpleGraph.exists_isAcyclic_card_eq_inducedForestNumber`, a theorem declared in [MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/SimpleGraph/InducedForestNumber.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/induced-forest-number/index.html#exists-is-acyclic-card-eq-induced-forest).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Induced forest number](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/graph-invariants-and-labelings/induced-forest-number/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/graph-invariants-and-labelings/induced-forest-number)
