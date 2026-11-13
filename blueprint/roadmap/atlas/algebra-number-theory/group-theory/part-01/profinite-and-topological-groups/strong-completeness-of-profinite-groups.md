---
declaration: section
origin: cited
lean: IsStronglyComplete, ProfiniteGrp.ProfiniteCompletion.isClosed_toSubgroup_of_surjective_etaFn, ProfiniteGrp.ProfiniteCompletion.isOpen_toSubgroup_of_surjective_etaFn, ProfiniteGrp.ProfiniteCompletion.isStronglyComplete_iff_bijective_etaFn, MathlibExt.GroupTheory.NikolovSegalWanted.GroupTheory.IsTopologicallyFinitelyGenerated, MathlibExt.GroupTheory.NikolovSegalWanted.GroupTheory.nikolov_segal
statement: formalized
---

# Strong completeness of profinite groups

6 results, 5 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html).

## Strongly complete group

A group $G$ equipped with a topology is *strongly complete* when
every subgroup of finite index in $G$ is open.

Formalized by `IsStronglyComplete`, a definition declared in [MathlibExt/Topology/Algebra/StrongCompleteness.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/StrongCompleteness.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html#is-strongly-complete).

## Finite-index normal subgroups are closed when the completion map is onto

Let $P$ be a
profinite group and let $\hat P$ be the profinite completion of $P$ as an abstract group, that is,
the inverse limit of the finite quotients $P/N$ over all normal subgroups $N$ of finite index in
$P$. If the canonical map $P \to \hat P$ is surjective, then every normal subgroup of finite
index in $P$ is closed in $P$.

Formalized by `ProfiniteGrp.ProfiniteCompletion.isClosed_toSubgroup_of_surjective_etaFn`, a theorem declared in [MathlibExt/Topology/Algebra/StrongCompleteness.lean, line 75](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/StrongCompleteness.lean#L75). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html#is-closed-to-subgroup-of-surjective-eta).

## Finite-index normal subgroups are open when the completion map is onto

Let $P$ be a
profinite group and let $\hat P$ be the profinite completion of $P$ as an abstract group, that is,
the inverse limit of the finite quotients $P/N$ over all normal subgroups $N$ of finite index in
$P$. If the canonical map $P \to \hat P$ is surjective, then every normal subgroup of finite
index in $P$ is open in $P$.

Formalized by `ProfiniteGrp.ProfiniteCompletion.isOpen_toSubgroup_of_surjective_etaFn`, a theorem declared in [MathlibExt/Topology/Algebra/StrongCompleteness.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/StrongCompleteness.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html#is-open-to-subgroup-of-surjective-eta-fn).

## Strongly complete profinite groups via the profinite completion

Let $P$ be a profinite
group and let $\hat P$ be the profinite completion of $P$ as an abstract group, that is, the
inverse limit of the finite quotients $P/N$ over all normal subgroups $N$ of finite index in $P$.
Then $P$ is strongly complete if and only if the canonical map $P \to \hat P$ is bijective.

Formalized by `ProfiniteGrp.ProfiniteCompletion.isStronglyComplete_iff_bijective_etaFn`, a theorem declared in [MathlibExt/Topology/Algebra/StrongCompleteness.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Topology/Algebra/StrongCompleteness.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html#is-strongly-complete-iff-bijective-eta-f).

## Topologically finitely generated group

A topological group is topologically finitely
generated if some finite set generates a dense abstract subgroup.

Formalized by `MathlibExt.GroupTheory.NikolovSegalWanted.GroupTheory.IsTopologicallyFinitelyGenerated`, a definition declared in [WantedExt/GroupTheory/NikolovSegalWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NikolovSegalWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html#is-topologically-finitely-generated).

## Nikolov–Segal strong completeness theorem

Every finite-index subgroup of a
topologically finitely generated profinite group is open.

## Sources

- Nikolay Nikolov and Dan Segal, *On finitely generated profinite groups, I: strong completeness and uniform bounds*, Annals of Mathematics 165 (2007), no. 1, 171–238, Theorem 1.1, https://doi.org/10.4007/annals.2007.165.171; *On finitely generated profinite groups, II: products in quasisimple groups*, Annals of Mathematics 165 (2007), no. 1, 239–273, https://doi.org/10.4007/annals.2007.165.239. Problem `nikolov_segal` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.GroupTheory.NikolovSegalWanted.GroupTheory.nikolov_segal` is written with `theorem_wanted` in [WantedExt/GroupTheory/NikolovSegalWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/NikolovSegalWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html#nikolov-segal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Strong completeness of profinite groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/profinite-and-topological-groups/strong-completeness-of-profinite-groups)
