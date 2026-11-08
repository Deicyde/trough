# Projective space

> Projective spectra of graded rings, polynomial standard charts and covers, homogeneous ideals, coordinate points, graded transport, geometric-cover global-sections morphisms, positive-degree-scaled Proj maps on their natural open domains with full ordinary point-prime contraction and arbitrary-element membership, whole-arrow unit-scaling invariance, positive-Veronese chart equivalences and whole-scheme Proj invariance, coherent-tail whole-scheme isomorphisms with degree-zero coefficient naturality, Noetherian projective spectra and geometric properties.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/formalization.yaml) of [FormalFrontier/projective-space](https://github.com/FormalFrontier/projective-space) at commit [9dbd208f](https://github.com/FormalFrontier/projective-space/tree/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of the 7 headline results in its README names a declaration that the linked file declares at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/projective-space](https://github.com/FormalFrontier/projective-space), read at commit [9dbd208f](https://github.com/FormalFrontier/projective-space/tree/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “Independently reviewed mathematical development”
- Review notes: “Independent mathematical review and maintainer acceptance do not establish correspondence with or coverage of any selected source.”
- Automation: agent; framework “Codex CLI and Hive Tasks”; tool setup “AI-assisted source and Lean development with maintainer coordination and independent bounded reviews.”
- Automation notes: “AI agents prepared original and adapted code, documentation and source assembly; this metadata describes involvement, not automated proof certification.”

## Scope

Reusable 30-leaf mathematical library with aggregate public import, eleven test clients, two diagnostic modules and three reader examples (47 Lean files). Results include positive-degree projective basics and radical, homogeneous coordinates, charts, quotient and symmetric-algebra Proj, geometric-cover global sections, whole-arrow unit scaling, degree-scaled maps on their natural open domain with full ordinary-prime contraction, positive-Veronese whole-scheme isomorphism and coherent-tail whole-scheme isomorphisms with both degree-zero coefficient triangles, and Noetherian Proj of arbitrary N-graded Noetherian commutative rings, including finite-coordinate polynomial Proj over any Noetherian coefficient ring. Finite-dimensional polynomial projective space is geometrically integral over every commutative ring, with finite nonempty coordinates. The Noetherian results need no field, domain, degree-one generation or nontriviality assumption. Official pinned Graded Rings supplies the selected-component and coherent-tail algebra. See README.md and docs/MODULES.md for exact assumptions and direct imports.

*Quoted from the status in [formalization.yaml](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/formalization.yaml) of [FormalFrontier/projective-space](https://github.com/FormalFrontier/projective-space) at commit [9dbd208f](https://github.com/FormalFrontier/projective-space/tree/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91), Apache-2.0.*

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Original projective-space formal development*, Formal Frontier Agents (original-proof; independently-proves).
- [The Lean mathematical library (mathlib4)](https://github.com/leanprover-community/mathlib4), The mathlib community (software; background).
- *Graded Rings* (software; background).
- *Scheme Properties* (software; background).
- *The Rising Sea: Foundations of Algebraic Geometry*, Ravi Vakil, October 21, 2025 draft, projective-space corollary following Exercise 5.1.C, printed p. 157; §7.4.4, Exercises 7.4.D and 7.4.F, printed p. 215; coefficient conventions pp. 151–152 (book; background).

## Builds on

- [Graded rings](../../commutative-algebra/graded-rings/README.md) (a Lake dependency, pinned at db2a1d55)
- [Scheme properties](../scheme-properties/README.md) (a Lake dependency, pinned at 6b204a3e)


## Headline results

**Inverse degree-preserving graded ring maps give whole-scheme `Proj` isomorphisms through `ProjectiveSpace.projIsoOfInverseGradedRingHom` and ….** Inverse degree-preserving graded ring maps give whole-scheme `Proj`
isomorphisms through `ProjectiveSpace.projIsoOfInverseGradedRingHom` and
homeomorphisms and closed-point equivalences through
`ProjectiveSpace.projectiveSpectrumHomeomorphOfInverseGradedRingHom` and
`ProjectiveSpace.projClosedPointsEquivOfInverseGradedRingHom`.
Scheme transport uses one universe for underlying rings; point transport
permits independent ring universes. See the
[module](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/GradedProjIso.lean) and
[point client](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpaceTest/PointClient.lean).

**Compatible graded tails with equivalent degree-zero rings and high-degree pieces induce an isomorphism of **entire projective schemes** ….** Compatible graded tails with equivalent degree-zero rings and high-degree
pieces induce an isomorphism of **entire projective schemes**
`E.projIso n hNn hn` for `N ≤ n` and `0 < n`, with both forward and inverse
equalities over the actual degree-zero base. No graded map on the omitted
low-degree original components, finite generation, domain, reducedness or
`Nontrivial` is needed. The algebraic `TailEquiv` is provided by the official
Graded Rings dependency; this library proves the geometric transfer. See
[the coherent-tail guide](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/docs/CoherentTailProj.md),
[module](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/CoherentTailProj.lean) and
[client](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpaceTest/CoherentTailProjClient.lean).

**Every positive selected-component Veronese has a whole-scheme isomorphism `AlgebraicGeometry.Proj.Veronese.schemeIso`, compatible with the ….** Every positive selected-component Veronese has a whole-scheme isomorphism
`AlgebraicGeometry.Proj.Veronese.schemeIso`, compatible with the degree-zero
coefficient map; its charts accommodate zero divisors and nilpotents.
Selected-component ring algebra comes from Graded Rings. See
[the Veronese guide](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/docs/Veronese.md),
[module](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Veronese.lean) and
[client](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpaceTest/VeroneseClient.lean).

**A positive degree-scaled ring hom constructs a projective scheme arrow on the **actual open complement** of its image-irrelevant zero locus ….** A positive degree-scaled ring hom constructs a projective scheme arrow on
the **actual open complement** of its image-irrelevant zero locus, with
coefficient naturality and arbitrary-element ordinary point-prime
contraction. The generic arrow is not asserted to extend to all of `Proj`.
See the [degree-scaled guide](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/docs/DegreeScaledMap.md),
[point-prime guide](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/docs/DegreeScaledMapPoint.md) and
[direct client](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpaceTest/DegreeScaledMapPointClient.lean).

**Positive-degree homogeneous basic opens form a basis on arbitrary graded `Proj`, including the zero ring.** Positive-degree homogeneous basic opens form a basis on arbitrary graded
`Proj`, including the zero ring; the positive-degree projective radical
criterion identifies vanishing with membership in an **ordinary** radical.
The latter needs a positive-degree homogeneous element, not a field or
Noetherianity. See the [basis module](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/BasicOpenBasis.lean),
[radical module](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/ProjectiveNullstellensatz.lean) and
[geometry client](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpaceTest/GeometryClient.lean).

**The `Proj` of a naturally graded **Noetherian commutative ring** is a Noetherian scheme.** The `Proj` of a naturally graded **Noetherian commutative ring** is a
Noetherian scheme. In particular, total-degree polynomial `Proj` over any
Noetherian commutative ring with **finite coordinates** is Noetherian,
including empty coordinate types and the zero ring. Mathlib then gives
Noetherianity of its underlying topological space; every subset is compact.
See the [module](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Noetherian.lean) and
[client](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpaceTest/NoetherianClient.lean).

**Finite-dimensional projective space is **geometrically integral over every commutative ring**.** Finite-dimensional projective space is **geometrically integral over every
commutative ring**: `polynomialProjToSpec_fin_geometricallyIntegral` applies
to `Fin (n + 1)`, and `polynomialProjToSpec_geometricallyIntegral_of_finite`
to any finite nonempty coordinate type. No domain, Noetherian or
nontrivial-base hypothesis is needed. The finite restriction belongs to the
polynomial-chart API; empty coordinates are excluded because projective
space over a field would be empty. See the
[module](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/GeometricallyIntegral.lean) and the
[projective-line client](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpaceTest/GeometricallyIntegralClient.lean).

## Main results

The 26 main results its formalization.yaml lists (`status.main_results`). They are listed here, not made articles: in several Formal Frontier libraries this list is close to the whole API.

| Declaration | Kind | Where | Note |
| --- | --- | --- | --- |
| `ProjectiveSpace.polynomialProjToSpec_geometricallyIntegral_of_finite` | theorem | [ProjectiveSpace/GeometricallyIntegral.lean, line 341](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/GeometricallyIntegral.lean#L341) |  |
| `ProjectiveSpace.polynomialProjToSpec_fin_geometricallyIntegral` | theorem | [ProjectiveSpace/GeometricallyIntegral.lean, line 355](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/GeometricallyIntegral.lean#L355) |  |
| `AlgebraicGeometry.Proj.isNoetherian` | instance | [ProjectiveSpace/Noetherian.lean, line 51](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Noetherian.lean#L51) |  |
| `ProjectiveSpace.isNoetherian_polynomialProj` | theorem | [ProjectiveSpace/Noetherian.lean, line 79](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Noetherian.lean#L79) |  |
| `AlgebraicGeometry.Proj.imageIrrelevant` | def | [ProjectiveSpace/DegreeScaledMap.lean, line 44](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L44) |  |
| `AlgebraicGeometry.Proj.degreeScaledDomain` | def | [ProjectiveSpace/DegreeScaledMap.lean, line 52](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L52) |  |
| `AlgebraicGeometry.Proj.degreeScaledDomain_eq_zeroLocus_compl` | theorem | [ProjectiveSpace/DegreeScaledMap.lean, line 55](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L55) |  |
| `AlgebraicGeometry.Proj.degreeScaledChartMap` | def | [ProjectiveSpace/DegreeScaledMap.lean, line 82](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L82) |  |
| `AlgebraicGeometry.Proj.degreeScaledChartMap_compatible` | theorem | [ProjectiveSpace/DegreeScaledMap.lean, line 263](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L263) |  |
| `AlgebraicGeometry.Proj.degreeScaledMap` | def | [ProjectiveSpace/DegreeScaledMap.lean, line 288](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L288) |  |
| `AlgebraicGeometry.Proj.chartCover_map` | theorem | [ProjectiveSpace/DegreeScaledMap.lean, line 296](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L296) |  |
| `AlgebraicGeometry.Proj.degreeScaledMap_chartSpec` | theorem | [ProjectiveSpace/DegreeScaledMap.lean, line 305](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L305) |  |
| `AlgebraicGeometry.Proj.degreeScaledMap_unique` | theorem | [ProjectiveSpace/DegreeScaledMap.lean, line 323](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L323) |  |
| `AlgebraicGeometry.Proj.degreeZeroRingHom` | def | [ProjectiveSpace/DegreeScaledMap.lean, line 332](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L332) |  |
| `AlgebraicGeometry.Proj.degreeScaledMap_toSpecZero` | theorem | [ProjectiveSpace/DegreeScaledMap.lean, line 374](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L374) |  |
| `AlgebraicGeometry.Proj.degreeScaledMap_preimage_basicOpen` | theorem | [ProjectiveSpace/DegreeScaledMap.lean, line 472](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMap.lean#L472) |  |
| `AlgebraicGeometry.Proj.degreeScaledMap_pointIdeal` | theorem | [ProjectiveSpace/DegreeScaledMapPoint.lean, line 139](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMapPoint.lean#L139) |  |
| `AlgebraicGeometry.Proj.degreeScaledMap_mem_pointIdeal` | theorem | [ProjectiveSpace/DegreeScaledMapPoint.lean, line 167](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/DegreeScaledMapPoint.lean#L167) |  |
| `AlgebraicGeometry.Proj.Veronese.schemeIso` | def | [ProjectiveSpace/Veronese.lean, line 291](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Veronese.lean#L291) |  |
| `AlgebraicGeometry.Proj.Veronese.chartEquiv` | def | [ProjectiveSpace/Veronese.lean, line 84](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Veronese.lean#L84) |  |
| `AlgebraicGeometry.Proj.Veronese.forward_pointIdeal` | theorem | [ProjectiveSpace/Veronese.lean, line 162](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Veronese.lean#L162) |  |
| `AlgebraicGeometry.Proj.Veronese.forward_toSpecZero` | theorem | [ProjectiveSpace/Veronese.lean, line 203](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/Veronese.lean#L203) |  |
| `AlgebraicGeometry.Proj.map_toSpecZero` | theorem | [ProjectiveSpace/GradedProjIso.lean, line 210](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/GradedProjIso.lean#L210) |  |
| `GradedRing.Veronese.CoherentTail.TailEquiv.selectedProjIso` | def | [ProjectiveSpace/CoherentTailProj.lean, line 41](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/CoherentTailProj.lean#L41) |  |
| `GradedRing.Veronese.CoherentTail.TailEquiv.projIso` | def | [ProjectiveSpace/CoherentTailProj.lean, line 48](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/CoherentTailProj.lean#L48) |  |
| `GradedRing.Veronese.CoherentTail.TailEquiv.projIso_toSpecZero` | theorem | [ProjectiveSpace/CoherentTailProj.lean, line 91](https://github.com/FormalFrontier/projective-space/blob/9dbd208f42754d4b3e0fd8e778faa9125b9c6d91/ProjectiveSpace/CoherentTailProj.lean#L91) |  |
