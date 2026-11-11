---
declaration: section
origin: cited
lean: MetaMathlibExt.berge_general, MetaMathlibExt.Berge
statement: formalized
proof: formalized
---

# Berge's lemma

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/berge-s-lemma/index.html).

## Berge's lemma for matching subgraphs

Let $G$ be a simple graph on a finite vertex set and
let $M$ be a matching subgraph of $G$, so that every vertex of $M$ is incident to exactly one
edge of $M$. Then $M$ has the maximum number of edges among all matching subgraphs of $G$ if and
only if there is no $M$-augmenting path: a path in $G$ of positive length between two distinct
vertices $u$ and $v$, neither of which is a vertex of $M$, whose consecutive edges alternate
between edges of $M$ and edges not in $M$.

Formalized by `MetaMathlibExt.berge_general`, a theorem declared in [MathlibExt/Combinatorics/Matching/BergeLemma.lean, line 1151](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/BergeLemma.lean#L1151). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/berge-s-lemma/index.html#berge-general).

## Berge's lemma

Let $G$ be a simple graph on a finite vertex set and let $M$ be a matching
of $G$, that is, a finite set of edges of $G$ no two distinct members of which share a vertex.
Then $M$ has maximum cardinality among all matchings of $G$ if and only if there is no
$M$-augmenting path: a path in $G$ of positive length between two distinct vertices $u$ and $v$,
neither of which lies on an edge of $M$, whose consecutive edges alternate between edges of $M$
and edges not in $M$.

## Sources

- Wikipedia, Berge's theorem, https://en.wikipedia.org/wiki/Berge%27s_theorem.

Formalized by `MetaMathlibExt.Berge`, a theorem declared in [MathlibExt/Combinatorics/Matching/BergeLemma.lean, line 1208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Matching/BergeLemma.lean#L1208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/berge-s-lemma/index.html#berge).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Berge's lemma](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/matchings-and-flows/berge-s-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/matchings-and-flows/berge-s-lemma)
