---
declaration: section
origin: cited
lean: MetaMathlibExt.LabeledDigraph, MetaMathlibExt.LabeledDigraph.ext, MetaMathlibExt.LabeledDigraph.restrict, MetaMathlibExt.LabeledDigraph.restrict_src, MetaMathlibExt.LabeledDigraph.restrict_tgt, MetaMathlibExt.LabeledDigraph.restrict_label
statement: formalized
proof: formalized
---

# Labeled directed graphs

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html).

## Labeled directed graph

A labeled directed graph with vertex set $V$, edge set $E$ and
label set $L$ consists of a source map $s : E \to V$, a target map $t : E \to V$ and a label
map $\ell : E \to L$; the edge $e$ goes from $s(e)$ to $t(e)$ and carries the label $\ell(e)$.
Loops and parallel edges are allowed.

Formalized by `MetaMathlibExt.LabeledDigraph`, a structure declared in [MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html#labeled-digraph).

## Extensionality for labeled directed graphs

Two labeled directed graphs $G$ and $H$
with the same vertex set, edge set and label set are equal if they have the same source map,
the same target map and the same label map.

Formalized by `MetaMathlibExt.LabeledDigraph.ext`, a theorem declared in [MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html#ext).

## Restriction of a labeled directed graph

Let $G$ be a labeled directed graph with
vertex set $V$ and label set $L$, and let $p$ be a predicate on $V$. The restriction of $G$ to
$p$ is the labeled directed graph with label set $L$ whose vertices are the vertices $v$ of $G$
with $p(v)$, whose edges are the edges of $G$ whose source and target both satisfy $p$, and in
which each edge has the same source, target and label as in $G$.

Formalized by `MetaMathlibExt.LabeledDigraph.restrict`, a definition declared in [MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html#restrict).

## Source of an edge in a restriction

Let $G$ be a labeled directed graph, $p$ a predicate
on its vertices, and $e$ an edge of $G$ whose source and target satisfy $p$, viewed as an edge of
the restriction of $G$ to $p$. The source of $e$ in the restriction, viewed as a vertex of $G$,
is the source of $e$ in $G$.

Formalized by `MetaMathlibExt.LabeledDigraph.restrict_src`, a theorem declared in [MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html#restrict-src).

## Target of an edge in a restriction

Let $G$ be a labeled directed graph, $p$ a predicate
on its vertices, and $e$ an edge of $G$ whose source and target satisfy $p$, viewed as an edge of
the restriction of $G$ to $p$. The target of $e$ in the restriction, viewed as a vertex of $G$,
is the target of $e$ in $G$.

Formalized by `MetaMathlibExt.LabeledDigraph.restrict_tgt`, a theorem declared in [MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html#restrict-tgt).

## Label of an edge in a restriction

Let $G$ be a labeled directed graph, $p$ a predicate
on its vertices, and $e$ an edge of $G$ whose source and target satisfy $p$, viewed as an edge of
the restriction of $G$ to $p$. The label of $e$ in the restriction is its label in $G$.

Formalized by `MetaMathlibExt.LabeledDigraph.restrict_label`, a theorem declared in [MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Digraph/LabeledDigraph.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html#restrict-label).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Labeled directed graphs](https://deicyde.github.io/atlas-lean/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GraphTheory/directed-graphs/labeled-directed-graphs)
