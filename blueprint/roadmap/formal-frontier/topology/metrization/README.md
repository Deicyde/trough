# Metrization

> The Nagata–Smirnov sigma-locally-finite open-basis criterion and its metric converse, and metrizability from a locally finite closed metrizable neighbourhood cover, preserving the given topologies.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/metrization/blob/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235/formalization.yaml) of [FormalFrontier/metrization](https://github.com/FormalFrontier/metrization) at commit [9c7cf0d8](https://github.com/FormalFrontier/metrization/tree/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235), Apache-2.0.*

3 articles, for headline results in its README whose declaration link names a declaration the linked file declares.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/metrization](https://github.com/FormalFrontier/metrization), read at commit [9c7cf0d8](https://github.com/FormalFrontier/metrization/tree/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “agent-reviewed”
- Automation: agent; tool setup “Lean 4 and Mathlib”
- Automation notes: “AI agents contributed to the formalization and documentation.”

## Scope

Metrizability from a T3 sigma-locally-finite open basis, the metrizable-space converse, and the locally finite closed metrizable neighbourhood-cover criterion without ambient separation assumptions. Supporting regular-basis and finite-support continuity results, with three coproduct clients.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/metrization/blob/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235/formalization.yaml) of [FormalFrontier/metrization](https://github.com/FormalFrontier/metrization) at commit [9c7cf0d8](https://github.com/FormalFrontier/metrization/tree/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *On a necessary and sufficient condition of metrizability*, J. Nagata, The sigma-locally-finite basis criterion for metrizability. (article; adapts).
- *A necessary and sufficient condition for metrizability of a topological space*, Yu. M. Smirnov, The sigma-locally-finite basis criterion for metrizability. (article; adapts).
- [Mathlib](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5), The Mathlib Community, Topological bases, locally finite families, separation and Urysohn's lemma, metric paracompactness, countable products, finite-support Lp metrics and coproduct homeomorphisms. (software; adapts).

## Builds on

No other Formal Frontier library.

## Used by

- [Vector bundles](../vector-bundles/README.md)

## Headline results

- [Sigma-locally-finite basis criterion](sigma-locally-finite-basis-criterion.md)
- [Metric converse](metric-converse.md)
- [Closed metrizable neighbourhood-cover criterion](closed-metrizable-neighbourhood-cover-criterion.md)

## Main results

The 3 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `TopologicalSpace.metrizableSpace_of_sigmaLocallyFinite_isTopologicalBasis` | theorem | [Metrization/LocallyFinite.lean, line 48](https://github.com/FormalFrontier/metrization/blob/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235/Metrization/LocallyFinite.lean#L48) |  |
| `TopologicalSpace.exists_sigmaLocallyFinite_isTopologicalBasis` | theorem | [Metrization/LocallyFinite.lean, line 149](https://github.com/FormalFrontier/metrization/blob/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235/Metrization/LocallyFinite.lean#L149) |  |
| `TopologicalSpace.metrizableSpace_of_locallyFinite_isClosed_interior_cover` | theorem | [Metrization/LocallyFinite.lean, line 189](https://github.com/FormalFrontier/metrization/blob/9c7cf0d82ab3c69a759c43e2ab6a246d537b7235/Metrization/LocallyFinite.lean#L189) |  |
