---
declaration: section
origin: cited
lean: MathlibExt.Topology.Algebra.PeterWeylWanted.peter_weyl_point_separation, MathlibExt.GroupTheory.CompactGroupSemisimpleWanted.RepresentationTheory.CompactGroupSemisimple.compact_group_semisimple
statement: formalized
---

# Representations of compact groups

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/representations-of-compact-groups/index.html).

## Peter–Weyl theorem: unitary representations separate points

Let $G$ be a compact Hausdorff
topological group and let $x \ne y$ be elements of $G$. Then there are an integer $n > 0$ and a
continuous map $\rho$ from $G$ to the complex $n \times n$ matrices such that $\rho(1) = 1$,
$\rho(gh) = \rho(g)\rho(h)$ for all $g, h \in G$, the matrix $\rho(g)$ is unitary for every
$g \in G$, and $\rho(x) \ne \rho(y)$.

## Sources

- F. Peter and H. Weyl, Math. Ann. 97 (1927), 737–755; Folland, A Course in Abstract Harmonic Analysis 2nd ed.; Knapp, Lie Groups Beyond an Introduction 2nd ed.

Formalized by `MathlibExt.Topology.Algebra.PeterWeylWanted.peter_weyl_point_separation`, a theorem declared in [MathlibExt/Topology/Algebra/PeterWeyl.lean, line 805](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/PeterWeyl.lean#L805). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/representations-of-compact-groups/index.html#peter-weyl-point-separation).

## Representations of compact groups are semisimple

Let $G$ be a compact topological group
and let $\rho$ be a representation of $G$ on a finite-dimensional real normed space $V$ such that
the action map $G \times V \to V$, $(g, v) \mapsto \rho(g)(v)$, is continuous. Then $\rho$ is
semisimple: every subrepresentation of $\rho$ has a complementary subrepresentation.

## Sources

- H. Weyl, *Theorie der Darstellung kontinuierlicher halb-einfacher Gruppen durch lineare Transformationen* (1925–26); Peter–Weyl (1927). Knill, *Some fundamental theorems in mathematics*, §21. Problem `compact_group_semisimple` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.CompactGroupSemisimpleWanted.RepresentationTheory.CompactGroupSemisimple.compact_group_semisimple` is written with `theorem_wanted` in [WantedExt/GroupTheory/CompactGroupSemisimpleWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/CompactGroupSemisimpleWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/representations-of-compact-groups/index.html#compact-group-semisimple).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representations of compact groups](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/lie-and-topological-representations/representations-of-compact-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RepresentationTheory/lie-and-topological-representations/representations-of-compact-groups)
