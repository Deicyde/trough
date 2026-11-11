---
declaration: section
origin: cited
lean: MetaMathlibExt.IsOpenColoring, MetaMathlibExt.IsColoringHomogeneous, MetaMathlibExt.IsColoringFree, MetaMathlibExt.OpenColoringAxiom
statement: formalized
proof: formalized
---

# Open coloring axiom

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/open-coloring-axiom/index.html).

## Open coloring of a topological space

Let $X$ be a topological space. A set
$K \subseteq X \times X$ of ordered pairs is an open coloring of $X$ if $K$ is open in the
product topology, symmetric ($(x, y) \in K$ implies $(y, x) \in K$) and irreflexive
($(x, x) \notin K$ for every $x \in X$).

Formalized by `MetaMathlibExt.IsOpenColoring`, a structure declared in [MathlibExt/SetTheory/Dichotomies/OpenColoring.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Dichotomies/OpenColoring.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/open-coloring-axiom/index.html#is-open-coloring).

## Homogeneous set for a coloring

Let $X$ be a set and $K \subseteq X \times X$. A set
$H \subseteq X$ is $K$-homogeneous if $(x, y) \in K$ for all distinct $x, y \in H$.

Formalized by `MetaMathlibExt.IsColoringHomogeneous`, a definition declared in [MathlibExt/SetTheory/Dichotomies/OpenColoring.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Dichotomies/OpenColoring.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/open-coloring-axiom/index.html#is-coloring-homogeneous).

## Free set for a coloring

Let $X$ be a set and $K \subseteq X \times X$. A set
$H \subseteq X$ is $K$-free if $(x, y) \notin K$ for all $x, y \in H$.

Formalized by `MetaMathlibExt.IsColoringFree`, a definition declared in [MathlibExt/SetTheory/Dichotomies/OpenColoring.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Dichotomies/OpenColoring.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/open-coloring-axiom/index.html#is-coloring-free).

## Open coloring axiom

Todorcevic's Open Coloring Axiom: for every open coloring of a second-countable space,
either there is an uncountable homogeneous set, or the space is a countable union of free sets.

Formalized by `MetaMathlibExt.OpenColoringAxiom`, a definition declared in [MathlibExt/SetTheory/Dichotomies/OpenColoring.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Dichotomies/OpenColoring.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/open-coloring-axiom/index.html#open-coloring-axiom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Open coloring axiom](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/forcing/open-coloring-axiom/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/forcing/open-coloring-axiom)
