---
declaration: section
origin: cited
lean: ClosedImmersionSheaves.isTerminalStalkPushforwardOfNotMemRange, ClosedImmersionSheaves.sheaf_pullback_pushforward_counit_isIso, TopCat.Presheaf.stalkPushforward.stalkPushforward_iso_of_isInducing, pushforward_faithful, pushforward_full, pushforward_stalkIsSingleton_of_notMem, closedInclusion_pushforward_faithful, closedInclusion_pushforward_full
statement: formalized
proof: formalized
---

# 6.32 Closed immersions and (pre)sheaves

Section 6.32 of the Stacks Project, [Tag 00AD](https://stacks.math.columbia.edu/tag/00AD). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00AE, a lemma

[Tag 00AE](https://stacks.math.columbia.edu/tag/00AE) in the Stacks Project.

**`ClosedImmersionSheaves.isTerminalStalkPushforwardOfNotMemRange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Pushforward.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Pushforward.lean#L116). References: EGA 0 (4.2.5), “zero stalks outside X”.

> **Stacks 00AE, the stalks of `i_* F` away from `Z`.** For `i : Z ⟶ X` a closed embedding,
> `F` a sheaf on `Z` and `x ∈ X` not in the image of `i`, the stalk `(i_* F)_x` is a terminal
> object of the target category: a singleton for sheaves of sets, `0` for abelian sheaves, a
> final object for sheaves of algebraic structures.
>
> The complement of the (closed) image is an open neighbourhood `W` of `x` with `i⁻¹(W) = ∅`,
> so `pushforwardStalkIsoOfEmptyPreimage` identifies the stalk with the terminal object
> `(i_* F)(W) = F(∅)`.

```lean
noncomputable def isTerminalStalkPushforwardOfNotMemRange
    (hi : IsClosedEmbedding (ConcreteCategory.hom i)) (x : X)
    (hx : x ∉ Set.range (ConcreteCategory.hom i)) :
    IsTerminal (stalk (i _* F) x)
```

**`ClosedImmersionSheaves.sheaf_pullback_pushforward_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Pushforward.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Pushforward.lean#L202).

> **Stacks 00AE, `i⁻¹ i_* = id`.** For an inducing `i : Z ⟶ X` — in particular for the
> inclusion of a closed subset — the counit `i⁻¹ i_* ⟶ 𝟭` of the adjunction
> `i⁻¹ ⊣ i_*` between categories of sheaves is a natural isomorphism, because its right
> adjoint `i_*` is fully faithful.

```lean
theorem sheaf_pullback_pushforward_counit_isIso
    (hi : IsInducing (ConcreteCategory.hom i)) :
    IsIso (Sheaf.pullbackPushforwardAdjunction A i).counit
```

Declarations registered for the tag:

- [`TopCat.Presheaf.stalkPushforward.stalkPushforward_iso_of_isInducing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.stalkPushforward.stalkPushforward_iso_of_isInducing#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Pushforward.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Pushforward.lean#L217) (StacksFrontier): “The stalk of `i_* F` at a point `i z` of the closed subset `Z` is `F_z`, via the canonical comparison map `stalkPushforward`. Mathlib proves this for any inducing map, and a closed embedding is inducing.”. References: EGA 0 (3.4.5), “more general”.

## Tag 00AF, a lemma

[Tag 00AF](https://stacks.math.columbia.edu/tag/00AF) in the Stacks Project.

**`pushforward_faithful`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Sets.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Sets.lean#L81).

> The pushforward of sheaves of sets along the inclusion of a subset is faithful.

```lean
lemma pushforward_faithful (X : TopCat.{u}) (Z : Set X) : (pushforward00AF X Z).Faithful
```

**`pushforward_full`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Sets.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Sets.lean#L87).

> The pushforward of sheaves of sets along the inclusion of a subset is full: every morphism
> `i_* F ⟶ i_* G` is `i_*` of a morphism `F ⟶ G`.

```lean
lemma pushforward_full (X : TopCat.{u}) (Z : Set X) : (pushforward00AF X Z).Full
```

**`pushforward_stalkIsSingleton_of_notMem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Sets.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Sets.lean#L94). References: EGA IV (21.9.1), “special case”.

> For `Z` closed and `x ∉ Z`, the stalk `(i_* F)_x` is a singleton.

```lean
theorem pushforward_stalkIsSingleton_of_notMem
    (X : TopCat.{u}) {Z : Set X} (hZ : IsClosed Z)
    (F : TopCat.Sheaf (Type u) (TopCat.of Z))
    (x : X) (hx : x ∉ Z) :
    StalkIsSingleton X ((pushforward00AF X Z).obj F) x
```

## Tag 00AG, a lemma

[Tag 00AG](https://stacks.math.columbia.edu/tag/00AG) in the Stacks Project.

**`closedInclusion_pushforward_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean#L63).

> **Stacks 00AG, faithfulness.** The pushforward of sheaves of abelian groups along a closed
> embedding is a faithful functor.

```lean
theorem closedInclusion_pushforward_faithful
    (Z X : TopCat.{u}) (i : Z ⟶ X) (hi : Topology.IsClosedEmbedding i.hom) :
    (closedInclusionPushforward Z X i).Faithful
```

**`closedInclusion_pushforward_full`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean#L71).

> **Stacks 00AG, fullness.** The pushforward of sheaves of abelian groups along a closed
> embedding is a full functor: every morphism `i_* 𝒜 ⟶ i_* ℬ` is `i_*` of a morphism `𝒜 ⟶ ℬ`.

```lean
theorem closedInclusion_pushforward_full
    (Z X : TopCat.{u}) (i : Z ⟶ X) (hi : Topology.IsClosedEmbedding i.hom) :
    (closedInclusionPushforward Z X i).Full
```

**`closedInclusion_pushforward_essImage_stalk_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/Abelian.lean#L112). References: EGA 0 (3.4.6), “(F)”; EGA 0 (4.2.5), “Ψ\_*M is zero outside X”; EGA IV (21.9.1), “special case”; SGA 6 IX (1.1), “Support clause”.

> **Stacks 00AG, essential image, forward direction.** If a sheaf `G` of abelian groups on
> `X` lies in the essential image of the pushforward along a closed embedding `i`, then the stalk
> of `G` vanishes at every point outside the range of `i`.

```lean
theorem closedInclusion_pushforward_essImage_stalk_isZero
    (Z X : TopCat.{u}) (i : Z ⟶ X) (hi : Topology.IsClosedEmbedding i.hom)
    (G : TopCat.Sheaf AddCommGrpCat.{u} X)
    (hG : (closedInclusionPushforward Z X i).essImage G) :
    ∀ x : X, x ∉ Set.range i.hom → IsZero (Presheaf.stalk G.obj x)
```

## Tag 00AH, a lemma

[Tag 00AH](https://stacks.math.columbia.edu/tag/00AH) in the Stacks Project.

**`Stacks.full_and_faithful_pushforward_subsetInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/PushforwardAlgStruct.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/PushforwardAlgStruct.lean#L149).

> **Stacks 00AH, Part 1.** The pushforward functor `i_* : Sh(Z, C) ⥤ Sh(X, C)`
> along the inclusion `i : Z ↪ X` is full and faithful, for any type of algebraic
> structure `(C, F)`. The proof only uses that `Opens.map i` is surjective on
> opens, so `Z` may be an arbitrary subset; closedness is needed only for
> `essImage_pushforward_subsetInclusion_iff`.

```lean
theorem full_and_faithful_pushforward_subsetInclusion (X : TopCat.{u}) (Z : Set X)
    (S : AlgebraicStructureType.{u, u}) [HasColimits S.C] :
    (TopCat.Sheaf.pushforward S.C (subsetInclusion X Z)).Full ∧
      (TopCat.Sheaf.pushforward S.C (subsetInclusion X Z)).Faithful
```

**`Stacks.essImage_pushforward_subsetInclusion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/PushforwardAlgStruct.lean, line 507](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/PushforwardAlgStruct.lean#L507).

> **Stacks 00AH, Part 2.** A sheaf `G ∈ Sh(X, C)` lies in the essential image
> of `i_* : Sh(Z, C) ⥤ Sh(X, C)`, for `i` the inclusion of a closed subset `Z`,
> exactly when its stalk at every point `x ∉ Z` is isomorphic in `C` to the final
> object `0`.

```lean
theorem essImage_pushforward_subsetInclusion_iff (X : TopCat.{u}) (Z : Set X) (hZ : IsClosed Z)
    (S : AlgebraicStructureType.{u, u}) [HasColimits S.C] (Sfinal : S.WithFinal)
    (G : TopCat.Sheaf S.C X) :
    (TopCat.Sheaf.pushforward S.C (subsetInclusion X Z)).essImage G ↔
      ∀ x : X, x ∉ Z → Nonempty (TopCat.Presheaf.stalk G.obj x ≅ Sfinal.zero)
```

## Tag 00AI, a remark

[Tag 00AI](https://stacks.math.columbia.edu/tag/00AI) in the Stacks Project.

**`ClosedImmersionSheaves.not_preservesColimitsOfShape_sheafPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/NotRightExact.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/NotRightExact.lean#L78). The attribute's comment: “i\_* is not right exact as a functor between categories of sheaves of sets”. References: SGA 4 IV (3.1.2), “u\_* not right exact”.

> **Stacks 00AI, first half.** For `i : Z ⟶ X` a closed embedding and `x ∈ X` outside the image
> of `i`, the pushforward `i_* : Sh(Z, Type) ⥤ Sh(X, Type)` does not preserve binary coproducts, i.e.
> it is not right exact.
>
> Take `F` to be the final sheaf `*` on `Z`. Stacks 00AE makes the stalk at `x` of `i_*G` terminal
> for *every* sheaf `G` on `Z`, in particular for `G = F` and for `G = F ⨿ F`. Taking stalks of
> sheaves is a left adjoint, so it preserves the coproduct; if `i_*` preserved it too, the terminal
> set `(i_*(F ⨿ F))_x` would be the coproduct of the terminal set `(i_*F)_x` with itself, which
> `isEmpty_isTerminal_coprod_self` forbids.

```lean
theorem not_preservesColimitsOfShape_sheafPushforward
    (hi : IsClosedEmbedding (ConcreteCategory.hom i)) (x : X)
    (hx : x ∉ Set.range (ConcreteCategory.hom i)) :
    ¬ PreservesColimitsOfShape (Discrete WalkingPair) (Sheaf.pushforward (Type u) i)
```

**`ClosedImmersionSheaves.not_isLeftAdjoint_sheafPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/ClosedImmersion/NotRightExact.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/ClosedImmersion/NotRightExact.lean#L111). The attribute's comment: “in particular i\_* cannot have a right adjoint”.

> **Stacks 00AI, second half.** For `i : Z ⟶ X` a closed embedding and `x ∈ X` outside the image
> of `i`, the pushforward `i_* : Sh(Z, Type) ⥤ Sh(X, Type)` has no right adjoint: a functor with a
> right adjoint preserves all colimits, and `i_*` does not preserve binary coproducts.

```lean
theorem not_isLeftAdjoint_sheafPushforward
    (hi : IsClosedEmbedding (ConcreteCategory.hom i)) (x : X)
    (hx : x ∉ Set.range (ConcreteCategory.hom i)) :
    ¬ (Sheaf.pushforward (Type u) i).IsLeftAdjoint
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.32, Tag 00AD](https://stacks.math.columbia.edu/tag/00AD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
