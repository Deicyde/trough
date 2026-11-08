# Sheaf cohomology

> Compact-open filtered section colimits, quasi-flasque acyclicity, sheaf cohomology and right-derived pushforward, native sheafed-space limits and pullback cocones, coefficient-forgetting comparisons, and global and compact-open cylinder sections of spectral inverse limits. Generic open-variable restrictions and principal-tail changes compare the actual section diagrams for arbitrary original cones; invertibility of the specialized comparisons has additional hypotheses.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/formalization.yaml) of [FormalFrontier/sheaf-cohomology](https://github.com/FormalFrontier/sheaf-cohomology) at commit [85cf087f](https://github.com/FormalFrontier/sheaf-cohomology/tree/85cf087ff3e2311834bc8c16cb347f1a513d18e4), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 6 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/sheaf-cohomology](https://github.com/FormalFrontier/sheaf-cohomology), read at commit [85cf087f](https://github.com/FormalFrontier/sheaf-cohomology/tree/85cf087ff3e2311834bc8c16cb347f1a513d18e4) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “other: historical mathematical review is distinct from revision-specific acceptance”
- Review notes: “The mathematical library had distinct-execution agent review before its prior private release. Build, complete standard-axiom and independent mathematical/API/rights decisions apply only to the exact revisions they assessed; this metadata is not itself an acceptance certificate for any successor. No human or source-author endorsement is asserted.”
- Automation: agent; tool setup “Formal Frontier AI agents using Lean, Lake and Git for formalization, examples, documentation and distinct-execution independent review.”
- Automation notes: “Contributor and adaptation credits are in docs/CREDITS.md and repository history. No human peer review, source-author approval, model-cost estimate or current-tree performance measurement is inferred.”

## Scope

A 103-module Lean library with compact-open filtered comparisons, quasi-flasque and derived-cohomological results, conditional constructed native limits and their forgetful comparisons, and spectral inverse-limit global and cylinder sections. Generic open-variable naturality and transition-pullback principal-tail comparisons are arrow-level results for actual diagrams and original cones; neither proves an all-open isomorphism, unconditional global limits nor source-level coverage. Examples include both public named examples and private clients. The historical generated docs/API.md covers 26 original modules only; consult the focused guides for later modules and exact hypotheses.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/formalization.yaml) of [FormalFrontier/sheaf-cohomology](https://github.com/FormalFrontier/sheaf-cohomology) at commit [85cf087f](https://github.com/FormalFrontier/sheaf-cohomology/tree/85cf087ff3e2311834bc8c16cb347f1a513d18e4), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Sheaf cohomology, compact-open colimits, pullback and open base change* (folklore; independently-proves).
- [Foundations of Rigid Geometry I](https://arxiv.org/abs/1308.4734v5), Kazuhiro Fujiwara, Fumiharu Kato (book; background).

## Builds on

- [Spectral Stone duality](../../topology/spectral-stone-duality/README.md) (a Lake dependency, pinned at 452b7b7b)


## Headline results

**Compact-open sections and acyclicity.** On a prespectral,
quasi-separated space, evaluation of suitable concrete-category sheaves on
a compact open preserves small filtered colimits, subject to the explicit
sheafification, concrete-category and universe assumptions. For abelian
sheaves on a *compact* such space, quasi-flasqueness implies vanishing of
positive-degree sheaf cohomology, using an injective-envelope dimension
shift. See
[`preservesColimit_sections`](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/CompactOpenSections.lean#L784),
[`subsingleton_H_succ`](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/QuasiFlasqueAcyclicity.lean#L259),
and the [mathematical guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/Guide.md).

**Higher direct images.** For a spectral map from a prespectral,
quasi-separated source to a prespectral target, right-derived pushforward
of abelian sheaves preserves filtered colimits in every natural degree. The
theorem identifies the *canonical* `colimit.post` comparison for a small,
nonempty directed-preorder diagram, not an arbitrary isomorphism; this API
has universe-zero spaces, coefficients and Ext groups and requires its
stated sheafification/Ext instances. See
[`rightDerivedPushforward_colimitPost_isIso`](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/HigherDirectImageFilteredColimit.lean#L332)
and the [mathematical guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/Guide.md).

**Native sheafed-space limits.** For an actual cone, a limiting underlying
space cone and a colimiting cocone of its projection-pullback sheaves imply
that the native cone is limiting; over that same limiting base, the converse
recovers the sheaf colimit. A separate construction builds such a native
limit when the required coefficient colimits and local weak sheafification
exist. These are conditional results under the concrete-coefficient
hypotheses, not a global limits instance. See the
[limit criterion](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/ConePullbackLimit.lean#L222),
[fixed-base converse](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/ConePullbackLimitConverse.lean#L170),
[construction](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/LimitConstruction.lean#L62), and
[limit guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/ConePullbackLimit.md).

**Forgetting coefficients.** The native additive-to-Type and
commutative-ring-to-Type functors preserve same-universe cofiltered limits
of sheafed spaces, using canonical pullback mates and filtered sheaf-colimit
comparisons. The ring pullback `canonicalComparison` is a *different* map
from the filtered-diagram `colimit.post` comparison; neither preservation
theorem covers arbitrary diagram shapes. See the
[additive theorem](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/AbelianForget/LimitPreservation.lean#L103),
[ring theorem](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/CommRingForget/LimitPreservation.lean#L112),
and [ring guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/CommRingForget.md).

**Global sections of spectral inverse limits.** Filtered colimits of
native stage sections recover the global sections of the constructed
Type-valued native limit, and of the *original actual limiting cone* for
additive or commutative-ring coefficients. All three isomorphisms require
small filtered indexing, spectral original stages and spectral original
transition maps. In the ring case each limit section comes from
*some* stage, not from every fixed stage. See the
[Type comparison](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeLimitGlobalSections.lean#L181),
[additive comparison](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeAdditiveGlobalSections.lean#L99),
[ring comparison and stage theorem](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCommRingGlobalSections.lean#L105),
and [ring sections guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/NativeCommRingGlobalSections.md).

**Compact-open cylinders.** For a directed preorder and a selected index,
restricting an actual native limit to the inverse image of a compact stage
open gives filtered-colimit descriptions of sections over that open for
Type-valued, additive and commutative-ring sheafed spaces. For an arbitrary
original cone, the actual restricted-stage section diagrams also vary
contravariantly with the stage open: their colimits form a presheaf under
the stated family of `HasColimit` assumptions, and the comparison to the
original cone commutes with open restriction. Ring and additive restriction
squares identify their existing arrows with this generic comparison; none
of these arrow laws asserts an all-open isomorphism. The
change-of-principal-tail result uses the actual transition-pullback open:
the later native and section diagrams are isomorphic to the earlier diagrams
restricted along the final tail inclusion. Colimit existence transfers both
ways; one local `HasColimit` at the earlier tail yields the canonical iso,
coprojection law and an arbitrary-original-cone comparison square with a
forward target equality cast. This makes no all-open `IsIso` or identity/
composition claim for tail changes. Separately, the conditional ring result
compares the literal restricted tail-stage rings with sections
on the *original* cone's inverse-image open: its original-stage law uses the
actual projection and both equality transports in `CommRingCat`. For an actual
limiting cone, spectral original stages and transition maps, and a compact
possibly-empty stage open, this comparison is an isomorphism, and each
section comes from *some* tail stage, not every fixed stage. No nonempty-open,
nontrivial-ring or transition-surjectivity premise is needed. See the
[Type theorem](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeSpectralCylinderSections.lean#L45),
[additive theorem](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeAdditiveCylinderSections.lean#L101),
[ring IsIso and some-stage declarations](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCommRingCylinderSections.lean),
[additive cylinder guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/NativeAdditiveCylinderSections.md),
[generic open-naturality guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/NativeCylinderOpenNaturality.md),
[generic tail-change guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/NativeCylinderTailChange.md),
[`betweenTailInclusion_final`](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCylinderTailChange.lean),
[`cylinderSectionsTailColimitIso`](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCylinderTailChange.lean),
[`cylinderSectionsComparison_betweenTail`](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCylinderTailChange.lean), and
[ring-cylinder guide](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/docs/NativeCommRingCylinderSections.md).

## Main results

The 10 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `SheafCohomology.CompactOpenSections.preservesColimit_sections` | theorem | [SheafCohomology/CompactOpenSections.lean, line 783](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/CompactOpenSections.lean#L783) |  |
| `TopCat.Sheaf.IsQuasiFlasque.subsingleton_H_succ` | theorem | [SheafCohomology/QuasiFlasqueAcyclicity.lean, line 260](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/QuasiFlasqueAcyclicity.lean#L260) |  |
| `SheafCohomology.HigherDirectImageFilteredColimit.rightDerivedPushforward_colimitPost_isIso` | theorem | [SheafCohomology/HigherDirectImageFilteredColimit.lean, line 332](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/HigherDirectImageFilteredColimit.lean#L332) |  |
| `AlgebraicGeometry.SheafedSpace.AbelianForget.preservesCofilteredLimit` | theorem | [SheafCohomology/AbelianForget/LimitPreservation.lean, line 103](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/AbelianForget/LimitPreservation.lean#L103) |  |
| `AlgebraicGeometry.SheafedSpace.CommRingForget.preservesCofilteredLimit` | theorem | [SheafCohomology/CommRingForget/LimitPreservation.lean, line 112](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/CommRingForget/LimitPreservation.lean#L112) |  |
| `AlgebraicGeometry.SheafedSpace.isIso_nativeCommRingGlobalSectionsComparison` | theorem | [SheafCohomology/NativeCommRingGlobalSections.lean, line 104](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCommRingGlobalSections.lean#L104) |  |
| `AlgebraicGeometry.SheafedSpace.NativeCylinderLimit.isIso_nativeCommRingCylinderSectionsComparison` | theorem | [SheafCohomology/NativeCommRingCylinderSections.lean, line 106](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCommRingCylinderSections.lean#L106) |  |
| `AlgebraicGeometry.SheafedSpace.NativeCylinderLimit.cylinderSectionsNaturality` | def | [SheafCohomology/NativeCylinderOpenNaturality.lean, line 331](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCylinderOpenNaturality.lean#L331) |  |
| `AlgebraicGeometry.SheafedSpace.NativeCylinderLimit.cylinderSectionsComparison_betweenTail` | theorem | [SheafCohomology/NativeCylinderTailChange.lean, line 253](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/NativeCylinderTailChange.lean#L253) |  |

The scan does not find 1 of them declared in the file the yaml gives: `AlgebraicGeometry.SheafedSpace.isLimit_of_isLimit_forget_of_isColimit_conePullbackCocone` ([SheafCohomology/ConePullbackLimit.lean](https://github.com/FormalFrontier/sheaf-cohomology/blob/85cf087ff3e2311834bc8c16cb347f1a513d18e4/SheafCohomology/ConePullbackLimit.lean)).
