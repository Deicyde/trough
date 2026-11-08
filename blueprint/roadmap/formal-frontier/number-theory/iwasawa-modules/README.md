# Iwasawa modules

> Generic pseudo-null and directional pseudo-isomorphism calculus and the RingCat finite-quotient completed group algebra, topology, Hausdorffness, compactness and compact-route canonical-uniformity completeness.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/formalization.yaml) of [FormalFrontier/iwasawa-modules](https://github.com/FormalFrontier/iwasawa-modules) at commit [e71db96b](https://github.com/FormalFrontier/iwasawa-modules/tree/e71db96b779b35bb05bd64eec63393e57b8da691), Apache-2.0.*

1 article: 1 for headline results in its README whose declaration link names a declaration the scan finds in the linked file. Its other headline results are quoted where they stand.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/iwasawa-modules](https://github.com/FormalFrontier/iwasawa-modules), read at commit [e71db96b](https://github.com/FormalFrontier/iwasawa-modules/tree/e71db96b779b35bb05bd64eec63393e57b8da691) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [e37d88a2](https://github.com/leanprover-community/mathlib4/tree/e37d88a26f3791ed5a93daa1f949af1021b8d103).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “independently reviewed published foundation; successor candidates require exact review”.
- Review notes: “Prism, Atlas, Lattice and Anchor reviewed earlier original mathematical contributions. Separate independent reviews addressed the original development and subsequent published snapshots. Each successor requires its own exact-candidate review and applicable build and complete transitive standard-axiom evidence, including private and generated declarations. Schema validity or public API documentation alone is not acceptance.”
- Reviewers: “Prism, Atlas, Lattice and Anchor (historical individual mathematical contributions)”, “Independent Formal Frontier reviewers (development and published-release candidates)”.
- Automation: agent; framework “AI-assisted Lean authoring with pinned Lake and mathlib”; tool setup “Beacon's original bridges, native-module and lint contributions; independently contributed public clients and metadata. The default build checks production and test roots with pinned Lean/mathlib. Separately retained native doc-gen4 SQLite/raw-record runs supplied the eleven-module API catalogue, not a private-proof census.”; prompting notes “AI agents assisted with original construction, proof search, module migration, testing and documentation. Human/operator authorization for verified original project contributions does not assign copyright ownership or clear third-party reuse.”
- Automation notes: “Mathematical and module/test contributions received independent review. The adapted native-documentation generator draws on the finite-group Tate cohomology, polynomial-root-stability and Anchor ideal-completion adapters; expression credit and the bounds of public API documentation are explained in docs/README.md. Exact release decisions are recorded separately.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Original Formal Frontier bridge definitions and proofs for Iwasawa modules*, Beacon, IwasawaModules/PseudoIsomorphism and IwasawaModules/CompletedGroupAlgebra (original-proof; independently-proves).
- [mathlib4](https://github.com/leanprover-community/mathlib4/tree/e37d88a26f3791ed5a93daa1f949af1021b8d103), Lean community contributors (software library; background).
- *Cohomology of Number Fields*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Chapter V, sections 1, 3 and 5 (book; background).

## Builds on

No other Formal Frontier library.

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/README.md#headline-results) of [FormalFrontier/iwasawa-modules](https://github.com/FormalFrontier/iwasawa-modules) at commit [e71db96b](https://github.com/FormalFrontier/iwasawa-modules/tree/e71db96b779b35bb05bd64eec63393e57b8da691), Apache-2.0.*

- [Pseudo-nullity and short exact sequences](pseudo-nullity-and-short-exact-sequences.md)

**Directional map calculus.** A *specified* linear map has pseudo-null kernel
and cokernel exactly when it is [bijective after localization](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/PseudoIsomorphism/LinearMap.lean#L67)
at every prime of height at most one. Identity and bijective maps qualify;
[composition](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/PseudoIsomorphism/LinearMap.lean#L106) preserves
the predicate, with independent scalar and module universes. This gives no
unrestricted reverse arrow or symmetric relation.

**Completed group algebra.** For a commutative coefficient ring `R` and a
profinite group `G`, [`CompletedGroupAlgebra R G`](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Basic.lean#L60)
is the finite-quotient group-algebra limit in `RingCat`, so `G` need not be
commutative. Its [coordinate projections](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Basic.lean#L65)
are compatible and detect equality; the [canonical ring map](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Basic.lean#L98)
from `R[G]` has a [coordinate formula](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Basic.lean#L103).
No injectivity or density of this map is asserted.

**Coefficientwise topology and separation.** For any finite index type,
even an empty one, [coefficient extraction is a homeomorphism](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Topology.lean#L59)
with a finite product; this part needs no group structure. The completed
topology is induced by finite-quotient projections: a map into the completion
is [continuous iff each coordinate is](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Topology.lean#L224).
Hausdorff coefficients give [finite-level](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Separation.lean#L33)
and [completed](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Separation.lean#L40)
Hausdorff spaces. Multiplicative/topological-ring results retain their group
and ring-continuity hypotheses.

**Compact-route completeness.** [Finite-index coefficient spaces](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Compactness.lean#L72)
are compact over compact coefficients *without* a Hausdorff or topological-ring
assumption. [Finite-level completeness](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Completeness.lean#L64)
for canonical additive-group uniformity additionally needs a topological ring.
[Completed compactness](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Compactness.lean#L176)
and [completed completeness](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/IwasawaModules/CompletedGroupAlgebra/Completeness.lean#L100)
by this route need compact **and Hausdorff** topological-ring coefficients;
merely complete coefficients are not covered.

These noncomputable constructions also include the zero coefficient ring.
Compact-module structure, `Z_p[[Gamma]]` comparisons, Iwasawa structure and
invariants, growth, adjoints and full source coverage remain outside this library.
The [native API reference](https://github.com/FormalFrontier/iwasawa-modules/blob/e71db96b779b35bb05bd64eec63393e57b8da691/docs/API.md) gives signatures and further declarations.

## Main results

Its formalization.yaml lists 4 main results, and the scan finds 4 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
