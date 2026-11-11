---
declaration: section
origin: cited
lean: ProfiniteGrp.OpenProfiniteCompletion.Index, ProfiniteGrp.OpenProfiniteCompletion.finiteGrpDiagram, ProfiniteGrp.OpenProfiniteCompletion.diagram, ProfiniteGrp.OpenProfiniteCompletion.completion, ProfiniteGrp.OpenProfiniteCompletion.etaFn, ProfiniteGrp.OpenProfiniteCompletion.etaFn_apply, ProfiniteGrp.OpenProfiniteCompletion.etaFn_continuous, ProfiniteGrp.OpenProfiniteCompletion.eta
statement: formalized
proof: formalized
---

# Profinite completion of topological groups

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html).

## Open finite-index normal subgroups

For a group $G$ with a topology, this is the set of
normal subgroups $H$ of $G$ that have finite index and are open in $G$, ordered by inclusion and
viewed as a category: there is a morphism $H \to K$ exactly when $H \subseteq K$.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.Index`, an abbreviation declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#index-2).

## Diagram of finite quotients

For a group $G$ with a topology, this is the functor from
the category of open finite-index normal subgroups of $G$ to finite groups that sends $H$ to the
quotient group $G/H$ and sends an inclusion $H \subseteq K$ to the projection $G/H \to G/K$,
$gH \mapsto gK$.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.finiteGrpDiagram`, a definition declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#finite-grp-diagram).

## Diagram of finite quotients as profinite groups

For a group $G$ with a topology, this is
the functor that sends each open finite-index normal subgroup $H$ of $G$ to the finite quotient
group $G/H$ with the discrete topology, regarded as a profinite group, and each inclusion
$H \subseteq K$ to the projection $G/H \to G/K$, $gH \mapsto gK$. It is the diagram of finite
quotients followed by the inclusion of finite groups into profinite groups.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.diagram`, a definition declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#diagram).

## Open profinite completion of a group

For a group $G$ with a topology, the open profinite
completion of $G$ is the limit, in profinite groups, of the diagram of finite quotients $G/H$,
where $H$ runs over the open finite-index normal subgroups of $G$ and the transition maps are the
projections $G/H \to G/K$ for $H \subseteq K$. Concretely, it is the group of families
$(x_H)_H$ with $x_H \in G/H$ that are compatible under these projections, with the topology of a
subspace of the product of the discrete groups $G/H$.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.completion`, a definition declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#completion).

## Canonical map into the open profinite completion

For a group $G$ with a topology, this is
the map from $G$ to its open profinite completion that sends $x \in G$ to the family of cosets
$(xH)_H$, where $H$ runs over the open finite-index normal subgroups of $G$.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.etaFn`, a definition declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#eta-fn).

## Coordinates of the canonical map

Let $G$ be a group with a topology. For every $x \in G$
and every open finite-index normal subgroup $H$ of $G$, the $H$-coordinate of the image of $x$
under the canonical map into the open profinite completion of $G$ is the coset $xH \in G/H$.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.etaFn_apply`, a theorem declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#eta-fn-apply).

## Continuity of the canonical map

Let $G$ be a group with a topology in which
multiplication is separately continuous: $x \mapsto ax$ and $x \mapsto xa$ are continuous for
every $a \in G$. Then the canonical map from $G$ to its open profinite completion is continuous.

Joint continuity of multiplication is not needed.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.etaFn_continuous`, a theorem declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#eta-fn-continuous).

## Canonical homomorphism into the open profinite completion

Let $G$ be a group with a
topology in which multiplication is separately continuous. This is the canonical map from $G$
to its open profinite completion, $x \mapsto (xH)_H$ with $H$ running over the open
finite-index normal subgroups of $G$, regarded as a continuous group homomorphism.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.eta`, a definition declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#eta).

## The canonical map has dense image

For every group $G$ with a topology, the image of the
canonical map from $G$ to its open profinite completion is dense.

No compatibility between the multiplication and the topology of $G$ is assumed.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.denseRange_etaFn`, a theorem declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#dense-range-eta-fn).

## Density of the canonical homomorphism

Let $G$ be a group with a topology in which
multiplication is separately continuous. Then the canonical continuous homomorphism from $G$ to
its open profinite completion has dense image.

Formalized by `ProfiniteGrp.OpenProfiniteCompletion.denseRange_eta`, a theorem declared in [MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/Group/OpenProfiniteCompletion.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html#dense-range-eta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Profinite completion of topological groups](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/topological-groups/profinite-completion-of-topological-groups)
