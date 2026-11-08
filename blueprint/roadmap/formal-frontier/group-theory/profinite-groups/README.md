# Profinite groups

> Reusable Lean APIs for finite-stage limits, finite-target map colimits, maps into limits of finite-space diagrams, profinite-group morphisms, finite-quotient Hom systems, compatible quotient-subgroup and Sylow families, closed subgroups with Sylow finite images, finite-quotient conjugacy, continuous sections, free profinite and pro-p constructions, primewise p-adic models, and procyclic invariants, power images, and closed-subgroup inheritance.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/formalization.yaml) of [FormalFrontier/profinite-groups](https://github.com/FormalFrontier/profinite-groups) at commit [bf258c54](https://github.com/FormalFrontier/profinite-groups/tree/bf258c54ddbe2b2e96f59e1965e55688279b872f), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 8 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/profinite-groups](https://github.com/FormalFrontier/profinite-groups), read at commit [bf258c54](https://github.com/FormalFrontier/profinite-groups/tree/bf258c54ddbe2b2e96f59e1965e55688279b872f) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other”
- Review notes: “Read README.md for headline results and import examples, and docs/Mathematics.md for hypotheses, constructions and limitations.”
- Automation: agent; framework “Codex CLI and Hive Tasks”; tool setup “AI agents developed code and documentation with a pinned Lean/mathlib Lake environment; independent agent executions reviewed mathematics.”
- Automation notes: “Beacon contributed the initial implementation and API and regression-client repairs. Formal Frontier Agents contributed further mathematics, tests, reference documentation and independent reviews. The native reference adapter and catalogue follow the finite-group Tate cohomology, polynomial-root-stability and Anchor ideal-completion adaptation lineage; Folio contributed headline input.”

## Scope

Production modules and checked-use clients have separate import roots. For any small nonempty cofiltered diagram of finite discrete spaces and any limiting cone, stage maps to a finite target form a filtered colimit equivalent to continuous maps from its limit, naturally in the target. Empty stages, limits and targets are allowed, but not an empty index. For an arbitrary diagram of finite-space targets with a specified limiting profinite cone, continuous maps from a specified cofiltered finite-space limit correspond to compatible stage-map classes at the target objects; the target index need not be cofiltered, small or nonempty. This is a comparison of profinite spaces and continuous maps, not groups. For two small nonempty cofiltered diagrams in the finite-set skeleton, morphisms between their canonical dual ind-objects correspond to compatible finite-stage map classes, with representative, composition, identity and fixed-index naturality laws. Specified limiting cones identify these morphisms with continuous maps of profinite spaces; no presentation-independent pro-category equivalence is asserted. Compatible quotient images reconstruct closed subgroups, and arbitrary prescribed quotient-level Sylow coordinates extend to compatible families and closed subgroups with Sylow finite images. Maximality is conditional on every actual finite quotient image of a containing subgroup being a p-group; independently conjugate images of closed subgroups yield an ambient conjugator. Procyclic power images classify open subgroups, not all closed subgroups of an arbitrary procyclic group. The closed-subgroup classification is for the specific primewise p-adic product. Nevertheless, every closed subgroup of a procyclic profinite group inherits procyclicity.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/formalization.yaml) of [FormalFrontier/profinite-groups](https://github.com/FormalFrontier/profinite-groups) at commit [bf258c54](https://github.com/FormalFrontier/profinite-groups/tree/bf258c54ddbe2b2e96f59e1965e55688279b872f), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Cohomology of Number Fields (corrected second edition, electronic version 2.3, May 2020)*, Jürgen Neukirch, Alexander Schmidt, Kay Wingberg, Chapter I, section 1 (including exercises 1 and 3–5); section 6 (finite-quotient pro-p and Sylow arguments); section 7 (before proposition 1.7.7). (book; background).

## Builds on

- [Group theory](../group-theory/README.md) (a Lake dependency, pinned at 77c1f266)

## Used by

- [Continuous group cohomology](../../homological-algebra-and-category-theory/continuous-group-cohomology/README.md)


## Headline results

Explore [finite diagrams](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/README.md#finite-diagrams-and-inverse-limit-characterizations),
[maps and constructions](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/README.md#maps-closed-subgroups-and-universal-constructions),
[product models and classification](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/README.md#primewise-models-product-ideals-and-procyclic-classification),
and [homomorphisms, powers and coefficients](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/README.md#homomorphisms-powers-and-coefficients).

### Finite diagrams and inverse-limit characterizations

**Skeletal finite quotients and equivalence.** Every profinite space in the
same universe is the limit of its included skeletal finite-quotient diagram.
The associated dual ind-object realizes to that space, giving an equivalence
between dual ind-objects of finite sets and profinite spaces whose forward
functor is the [profinite realization](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/IndDualRealization.lean).
The generic inverse's chosen object is compared with the skeletal presentation
by an isomorphism. Empty spaces and
finite stages are allowed; no arbitrary diagram projection is assumed
surjective. See [`IndDualEquivalence`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/IndDualEquivalence.lean)
and its [clients](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroupsTests/IndDualEquivalence.lean).

**Finite-stage inverse-limit characterizations.** A Hausdorff space is an
inverse limit of finite discrete spaces over a small, nonempty cofiltered
category if and only if it is compact with a clopen basis, equivalently
compact and totally disconnected. A topological group is an inverse limit
of finite groups over such a category if and only if it is compact and
totally disconnected (`FiniteGroupPresentation.nonempty_iff`). For a Hausdorff
topological group, this is also equivalent to compactness with an
identity-neighborhood basis of open normal subgroups. The presentations use the
actual inverse-limit topology and include empty spaces and trivial groups;
arbitrary finite-stage projections need not be surjective. See
[`FiniteDiscreteCharacterization`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/FiniteDiscreteCharacterization.lean)
and [`FiniteGroupCharacterization`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/FiniteGroupCharacterization.lean).

### Maps, closed subgroups and universal constructions

**Finite maps and morphisms.** In profinite groups, categorical monomorphisms
are injective and epimorphisms are surjective. For groups in the *same
universe*, continuous Hom is the limit over finite target quotients of the
colimits over finite source quotients. Separately, injective and surjective
maps of profinite **spaces** have finite-map limit presentations, not a
finite-presentation theorem for groups. See [`EpiMono`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/EpiMono.lean),
[`FiniteQuotientHom`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/FiniteQuotientHom.lean),
[`FinitePresentation`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/FinitePresentation.lean).

**Closed-subgroup conjugacy.** Two closed subgroups of a profinite group
are conjugate precisely when their images are conjugate in every finite
open-normal quotient. The quotient conjugators need not form a compatible
family; no countability or openness assumption is used. See
[`FiniteQuotientConjugacy`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/FiniteQuotientConjugacy.lean)
and its [guide](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/docs/finite-quotient-conjugacy.md).

**Continuous sections.** For closed `K ≤ H` in a profinite group, the
projection `G/K → G/H` has a continuous right inverse; a supporting result
supplies sections of surjective local homeomorphisms over compact Hausdorff
totally disconnected spaces. For any closed `H`, a chosen bundled continuous
map `G/H → G` selects a representative of each coset. The choice is neither
asserted to be homomorphic nor normalized at the identity; normality is not
needed. See [`ContinuousSection`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ContinuousSection.lean) and
[`ContinuousCosetRepresentative`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ContinuousCosetRepresentative.lean).

### Primewise models, product ideals and procyclic classification

**Procyclic classification and realization.** Given proofs of procyclicity,
groups in independent universes are continuously equivalent exactly when
their generator-independent primewise exponents agree. Every exponent
family is realized by residue factors `ZMod (p^n)` and p-adic factors: zero
exponent is trivial, infinity retains the full p-adic factor. With a
supplied generator, torsion-freeness means all exponents are zero or
infinity. For a torsion-free procyclic profinite group, its all-primes
quotient model, and hence the group itself, is continuously equivalent to
the product of p-adic integer factors over the infinite-exponent primes,
with zero-exponent coordinates omitted. The support can be empty or infinite
and is generator-independent; the group equivalence uses a chosen
topological generator. The invariant is noncomputable and *not* assigned to
arbitrary nonprocyclic groups; generator independence equates kernel ideals
and exponents, not the associated maps. See
[`ProcyclicInvariant`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ProcyclicInvariant.lean),
[`ProcyclicRealization`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ProcyclicRealization.lean),
[`ProcyclicTorsionFree`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ProcyclicTorsionFree.lean) and
[`ProcyclicTorsionFreeProduct`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ProcyclicTorsionFreeProduct.lean).

### Homomorphisms, powers and coefficients

**Power images and open subgroups.** For a procyclic group, positive `n`th
powers form an open subgroup with cyclic finite quotient and index
*dividing* `n`, not necessarily equal to `n`. Every open subgroup equals
the power image at its actual index. The zero-power image is trivial and
need not be open; no arbitrary-procyclic closed-subgroup classification is
asserted. See [`ProcyclicPower`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ProcyclicPower.lean).

**Closed subgroups of procyclic groups.** Every closed subgroup of an
arbitrary procyclic profinite group is procyclic in its inherited group and
topology, without an openness or finite-index assumption. It has a generator
inside the subgroup whose integral powers are dense there. The result also
accepts an ordinary subgroup with a closedness proof. It does not classify
arbitrary closed subgroups by exponents. See
[`ProcyclicClosedSubgroup`](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/ProfiniteGroups/ProcyclicClosedSubgroup.lean).

[All results and their hypotheses](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/docs/Results.md) ·
[Mathematical details, hypotheses and API limitations](https://github.com/FormalFrontier/profinite-groups/blob/bf258c54ddbe2b2e96f59e1965e55688279b872f/docs/Mathematics.md).
