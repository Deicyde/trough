# Morphism properties

> Relative preservation of maps between pullbacks, canonical transport between structured over-categories, pullback pairing over a fixed base, and density under slicing, using Mathlib's morphism-property and dense-functor classes. See README.md for hypotheses and limitations.

*Quoted from the project description in [formalization.yaml](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/formalization.yaml) of [FormalFrontier/morphism-properties](https://github.com/FormalFrontier/morphism-properties) at commit [1666ed81](https://github.com/FormalFrontier/morphism-properties/tree/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f), Apache-2.0.*

No articles: its formalization.yaml lists no highlights, and none of its 13 headline results links a declaration that the scan finds in the linked file at this commit, so they are quoted below.

## Facts

From the repository and its formalization.yaml; the review and automation statements are quoted as written.

- Repository: [FormalFrontier/morphism-properties](https://github.com/FormalFrontier/morphism-properties), read at commit [1666ed81](https://github.com/FormalFrontier/morphism-properties/tree/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f) (2026-11-04).
- Lean toolchain v4.34.0-rc2, Mathlib at [83abb3e7](https://github.com/leanprover-community/mathlib4/tree/83abb3e776bdefcbc447a1e44d0debe4010039e5).
- License: Apache-2.0.
- Authors: Formal Frontier Agents.
- Review status: “Under development”.
- Review notes: “The library covers relative preservation, fixed-base-arrow structured-over transport and fixed-base pairing, not the full B1/B2 package, converse, adjunction or creation of structured pullbacks.”
- Automation: agent; tool setup “Formal Frontier AI agents assisted with Lean formalization, examples, package configuration and documentation using Mathlib.”

## Literature

The sources its formalization.yaml names, with their relationship to it.

- *Foundations of Rigid Geometry I*, Kazuhiro Fujiwara, Fumiharu Kato, arXiv:1308.4734v5, Chapter 0, section 1.4(a), Proposition 1.4.1 (book; background).
- *Mathlib*, The mathlib community, https://github.com/leanprover-community/mathlib4 (software; adapts).

## Builds on

No other Formal Frontier library.

## Headline results

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/README.md#headline-results) of [FormalFrontier/morphism-properties](https://github.com/FormalFrontier/morphism-properties) at commit [1666ed81](https://github.com/FormalFrontier/morphism-properties/tree/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f), Apache-2.0.*

The pullback declarations below lie in `CategoryTheory.MorphismProperty`.
In the one-factor results, `f : S' ⟶ S` is a fixed base-change arrow.
For structure maps `v₁₂ : X ⟶ S`, `v₂₂ : Y ⟶ S`, and `g : X ⟶ Y` with
`v₁₂ = g ≫ v₂₂`, the induced map is `X ×[S] S' ⟶ Y ×[S] S'`.
In the two-factor result, instead, `f : X ⟶ S` and `g : Y ⟶ S` are structure
arrows into the common base, as are `f' : X' ⟶ S` and `g' : Y' ⟶ S`.
Maps `i₁ : X ⟶ X'` and `i₂ : Y ⟶ Y'` satisfying `f = i₁ ≫ f'` and
`g = i₂ ≫ g'` induce Mathlib's `pullback.map : X ×[S] Y ⟶ X' ×[S] Y'`.

**Preservation along a target projection**
([`pullbackLift_fst_snd_of_isStableUnderBaseChangeAlong`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
If `P g` and `P` is stable under base change along `Y ×[S] S' ⟶ Y`,
the induced map has property `P`. Only the two endpoint pullbacks are required.

**Relative preservation along an `E` arrow**
([`pullbackLift_fst_snd_of_isStableUnderBaseChangeAgainst`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
Assume `P.IsStableUnderBaseChangeAgainst E`, `E.IsStableUnderBaseChange`,
`E f`, and `P g`, with the two endpoint pullbacks. Then the induced map has `P`.

**Relative slice-functor preservation**
([`overPullbackMap_of_isStableUnderBaseChangeAgainst`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
Under the same stability and base-arrow hypotheses and
`Limits.HasPullbacksAlong f`, Mathlib's existing `CategoryTheory.Over.pullback f`
preserves `P` on underlying horizontal arrows.

**Object-structured preservation**
([`pullbackLift_fst_snd_of_intersection_of_postcomp`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
Assume `(P ⊓ E).IsStableUnderBaseChange`, `E.HasOfPostcompProperty E`,
`E v₁₂`, `E v₂₂`, and `P g`. With the two endpoint pullbacks, the induced
map belongs to `P ⊓ E` along arbitrary `f`, without `E f` or absolute
stability of `P` or `E`.

**One-factor preservation alternatives**
([`pullbackLift_fst_snd_of_relative_alternatives`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
Assume stability of `P` against `E`, absolute stability of `P ⊓ E` and of
`E`, cancellation of `E` under postcomposition by `E`, and `P g`. With the
endpoint pullbacks, the induced map has `P` if either both structure maps
belong to `E` or `f` belongs to `E`.

**Two-factor relative preservation**
([`pullbackMap_of_relative_alternatives`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
Assume composition closure of `P`, stability of `P` against `E`, absolute
stability of `P ⊓ E` and `E`, and cancellation of `E` under postcomposition
by `E`. If `P i₁` and `P i₂`, the canonical map has `P` provided either
`E f ∧ E f'` or `E f ∧ E g'`. Besides the endpoint pullbacks of `(f, g)`
and `(f', g')`, only the mixed pullback selected by the alternative is
required: `(f', g)` in the first case, `(f, g')` in the second.
No identity closure of `P` is assumed.

**Absolute two-factor specialization**
([`pullbackMap_of_relative_alternatives_top`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
With `E = ⊤`, absolute base-change stability and composition closure of `P`,
`P i₁`, `P i₂`, and the same commuting equations suffice under Mathlib's
`pullbackMap` hypotheses `Limits.HasPullbacksAlong f` and
`Limits.HasPullbacksAlong g'`. The conclusion is membership for the same
canonical map. No pullbacks along `g` or identity closure are added.

**Either-leg criterion for existing squares**
([`isStableUnderBaseChange_either_iff`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/RelativeBaseChange.lean)).
For base-change-stable `E`, preservation of `P` on an existing square
`IsPullback p q a b` whenever `P a` and `E a ∨ E b` is equivalent to
`P.IsStableUnderBaseChangeAgainst E` and `(P ⊓ E).IsStableUnderBaseChange`.
The preserved arrow is `q`; no pullback-existence assumption is made.

**Canonical structured-over transport**
([`Over.pullbackOfIntersectionOfPostcomp`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/OverPullback.lean)).
A functor `E.Over P S ⥤ E.Over P S'` assuming `P.IsMultiplicative`,
`E.HasPullbacksAlong f`, `E.IsStableUnderBaseChangeAlong f`,
`(P ⊓ E).IsStableUnderBaseChange`, and `E.HasOfPostcompProperty E`.
Here existence is required only for structure arrows satisfying `E`,
not for every object over `S`.

**Fixed-base pullback pairing**
([`Over.pullbackPairing` and `Over.pullbackPairing_map_mem_of_relative`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/PullbackPairing.lean)).
A functor `(E.Over P S × Q.Over P S) ⥤ CategoryTheory.Over S` assuming only
`P.IsMultiplicative` and `HasPullback A.hom B.hom` for every selected
`A : E.Over P S`, `B : Q.Over P S`. No closure of `E` or `Q` is required.
Objects are the chosen ambient pullbacks and maps are the canonical
`pullback.map`. Preservation of `P` separately assumes stability of `P`
against `E`, base-change stability of `P ⊓ E` and `E`, and cancellation of
`E` under postcomposition by `E`. The left endpoints supply `E`; the selected
family supplies the mixed pullback `(target-left, source-right)`.

**Product of the forgetful input functors**
([`Over.pullbackPairingFan_isLimit`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/PullbackPairing.lean)).
Under the same multiplicativity and selected-pair existence hypotheses,
the pullback pairing with its two projection transformations is a binary
product of `Prod.fst ⋙ Over.forget E P S` and `Prod.snd ⋙ Over.forget Q P S`
in `(E.Over P S × Q.Over P S) ⥤ CategoryTheory.Over S`. Joint lifts and
projections are ordinary-over morphisms; no membership in `P` is imposed.

**Symmetry of fixed-base pairing**
([`Over.pullbackPairingSymmetry`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/PullbackPairing.lean)).
With the same multiplicativity and selected-pair existence hypotheses,
interchanging `E` and `Q` gives a natural isomorphism to the reversed pairing.
Reverse pullbacks are derived from the forward family. Components are the
ambient pullback symmetry maps, with characteristic equations for both
projections, the inverse, and swapping twice. No stability or iso invariance
of the morphism properties is required.

**Density under slicing**
([`CategoryTheory.CostructuredArrow.isDenseAt_toOver` and `isDense_toOver`](https://github.com/FormalFrontier/morphism-properties/blob/1666ed81a5c4bcebb188ff67ab3b46df00aa6e4f/MorphismProperties/Density.lean)).
For arbitrary categories `A`, `C`, a functor `F : A ⥤ C`, `X : C`, and
`Y : CategoryTheory.Over X`, `F.isDenseAt Y.left` implies
`(CategoryTheory.CostructuredArrow.toOver F X).isDenseAt Y`.
Consequently, if `F.IsDense`, then `CostructuredArrow.toOver F X` is dense.
No fullness, faithfulness, limit-existence or nonemptiness hypothesis is required;
a converse to the pointwise implication is not asserted.

The transport API characterizes objects, structure maps, underlying maps and
both projections, supplies membership in `P` and `P ⊓ E`, and gives the ambient
pullback universal property and uniqueness of the structured map and functor lift.
Identity and composition equations come from the assembled functor laws.
Under absolute stability of `P`, the functor agrees with Mathlib's structured
pullback. Under `Limits.HasPullbacksAlong f`, its forgetful factorization has
Mathlib's ordinary over-category pullback comparison isomorphism.

## Main results

Its formalization.yaml lists 6 main results, and the scan finds 6 of them declared in the file the yaml gives; they are on their own page, not made articles.

- [Main results](main-results/README.md)
