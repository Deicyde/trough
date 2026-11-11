---
declaration: section
origin: cited
lean: CategoryTheory.CostructuredArrow.objEquiv, CategoryTheory.CostructuredArrow.homEquiv, CategoryTheory.Functor.lanRanAdjunctionTriple, CategoryTheory.Functor.ranObjIsoLimitCostructuredArrow, CategoryTheory.Functor.ranObjIsoLimitCostructuredArrow_hom_π, CategoryTheory.Functor.ranObjEquivCompatibleFamilies, CategoryTheory.Functor.ranObjEquivCompatibleFamilies_apply, CategoryTheory.Functor.ranObjEquivCompatibleFamilies_map
statement: formalized
proof: formalized
---

# 7.19 More functoriality of presheaves

Section 7.19 of the Stacks Project, [Tag 00XF](https://stacks.math.columbia.edu/tag/00XF). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00XF, the section

[Tag 00XF](https://stacks.math.columbia.edu/tag/00XF) in the Stacks Project.

**`CategoryTheory.CostructuredArrow.objEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L80). The attribute's comment: “the objects of the category `{}_V I` are the pairs `(U, ψ : u U ⟶ V)`”.

> The objects of the category `{}_T I = CostructuredArrow S T` are the pairs `(U, ψ)` of an
> object `U` of `C` and a morphism `ψ : S U ⟶ T`.

```lean
def objEquiv : CostructuredArrow S T ≃ Σ U : C, (S.obj U ⟶ T)
```

**`CategoryTheory.CostructuredArrow.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L102). The attribute's comment: “a morphism `(U, ψ) ⟶ (U', ψ')` of `{}_V I` is a morphism `α : U ⟶ U'` with `ψ = ψ' ∘ u(α)`”.

> The morphisms `(U, ψ) ⟶ (U', ψ')` of `{}_T I = CostructuredArrow S T` are the morphisms
> `α : U ⟶ U'` of `C` with `ψ = ψ' ∘ S α`.

```lean
def homEquiv (X Y : CostructuredArrow S T) :
    (X ⟶ Y) ≃ { α : X.left ⟶ Y.left // S.map α ≫ Y.hom = X.hom }
```

**`CategoryTheory.Functor.lanRanAdjunctionTriple`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L144). The attribute's comment: “`u^p` has the left adjoint `u_p` and also a right adjoint `{}_pu`; in the sequence `u_p, u^p, {}_pu` each consecutive pair is an adjoint pair”. References: SGA 4 I (5.1), “special case”; SGA 4 I (5.3), “more general”; SGA 4 I (5.5.2), “partial”; SGA 4 I (5.8.3), “more general”; SGA 4 III (2.2); SGA 4 IV (4.5.2), “partial”; SGA 4 V (7.1.0), “more general”.

> The restriction functor `u^p : PSh(D) ⥤ PSh(C)` has a left adjoint `u_p`, the left Kan
> extension along `u.op`, and a right adjoint `{}_pu`, the right Kan extension along `u.op`: the
> functors `u_p, u^p, {}_pu` form an adjoint triple.

```lean
noncomputable def lanRanAdjunctionTriple [HasLimitsOfSize.{v₁, max u₁ v₂} A]
    [HasColimitsOfSize.{v₁, max u₁ v₂} A] :
    Adjunction.Triple u.op.lan ((whiskeringLeft Cᵒᵖ Dᵒᵖ A).obj u.op) u.op.ran
```

**`CategoryTheory.Functor.ranObjIsoLimitCostructuredArrow`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L154). The attribute's comment: “`{}_pu F (V)` is the limit over `{}_V Iᵒᵖ` of `{}_V F : (U, ψ) ↦ F(U)`”.

> The value `{}_pu F (V)` of the right Kan extension of a presheaf `F` along `u.op` is the limit
> over `{}_V Iᵒᵖ = (CostructuredArrow u V)ᵒᵖ` of the functor `{}_V F : (U, ψ) ↦ F(U)`.

```lean
noncomputable def ranObjIsoLimitCostructuredArrow (F : Cᵒᵖ ⥤ A) (V : D) :
    (u.op.ran.obj F).obj (op V) ≅ limit ((CostructuredArrow.proj u V).op ⋙ F)
```

**`CategoryTheory.Functor.ranObjIsoLimitCostructuredArrow_hom_π`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L166). The attribute's comment: “the projection maps `c(ψ) : {}_pu F (V) ⟶ F(U)` of the limit”.

> The projection map `c(ψ) : {}_pu F (V) ⟶ F(U)` of the limit at an object `(U, ψ)` of `{}_V I`
> is the restriction along `ψ` followed by the canonical map `{}_pu F (u U) ⟶ F(U)` of Stacks 00XG,
> the counit of `u^p ⊣ {}_pu`.

```lean
lemma ranObjIsoLimitCostructuredArrow_hom_π (F : Cᵒᵖ ⥤ A) (V : D)
    (X : CostructuredArrow u V) :
    (u.ranObjIsoLimitCostructuredArrow F V).hom ≫ limit.π _ (op X) =
      (u.op.ran.obj F).map X.hom.op ≫ (u.op.ranCounit.app F).app (op X.left)
```

**`CategoryTheory.Functor.ranObjEquivCompatibleFamilies`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L186). The attribute's comment: “`{}_pu F (V)` is the set of collections `s_{(U, ψ)} ∈ F(U)` with `β^* s_{(U₂, ψ₂)} = s_{(U₁, ψ₁)}` for all `β : (U₁, ψ₁) ⟶ (U₂, ψ₂)` in `{}_V I`”.

> For a presheaf of sets `F` on `C`, the set `{}_pu F (V)` is the set of collections
> `s_{(U, ψ)} ∈ F(U)`, indexed by the objects `(U, ψ)` of `{}_V I`, such that
> `β^* s_{(U₂, ψ₂)} = s_{(U₁, ψ₁)}` for every morphism `β : (U₁, ψ₁) ⟶ (U₂, ψ₂)` of `{}_V I`.

```lean
noncomputable def ranObjEquivCompatibleFamilies :
    (u.op.ran.obj F).obj (op V) ≃
      { s : ∀ X : CostructuredArrow u V, F.obj (op X.left) //
        ∀ ⦃X Y : CostructuredArrow u V⦄ (β : X ⟶ Y), F.map β.left.op (s Y) = s X }
```

**`CategoryTheory.Functor.ranObjEquivCompatibleFamilies_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L200). The attribute's comment: “the correspondence is given by `s ↦ s_{(U, ψ)} = c(ψ)(s)`”.

> The correspondence `ranObjEquivCompatibleFamilies` is `s ↦ s_{(U, ψ)} = c(ψ)(s)`, where
> `c(ψ)` is the projection map of the limit.

```lean
lemma ranObjEquivCompatibleFamilies_apply (s : (u.op.ran.obj F).obj (op V))
    (X : CostructuredArrow u V) :
    (u.ranObjEquivCompatibleFamilies F V s).1 X =
      limit.π ((CostructuredArrow.proj u V).op ⋙ F) (op X)
        ((u.ranObjIsoLimitCostructuredArrow F V).hom s)
```

**`CategoryTheory.Functor.ranObjEquivCompatibleFamilies_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L220). The attribute's comment: “the restriction mappings `{}_pu F (V) ⟶ {}_pu F (V')` along `V' ⟶ V`”.

> The restriction mapping `{}_pu F (V) ⟶ {}_pu F (V')` along `g : V' ⟶ V` sends a collection
> `s` to the collection `(U, ψ') ↦ s_{(U, g ∘ ψ')}`.

```lean
lemma ranObjEquivCompatibleFamilies_map {V' : D} (g : V' ⟶ V) (s : (u.op.ran.obj F).obj (op V))
    (X : CostructuredArrow u V') :
    (u.ranObjEquivCompatibleFamilies F V' ((u.op.ran.obj F).map g.op s)).1 X =
      (u.ranObjEquivCompatibleFamilies F V s).1 ((CostructuredArrow.map g).obj X)
```

**`CategoryTheory.Functor.ranObjEquivCompatibleFamilies_ran_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L230). The attribute's comment: “a map of presheaves `F ⟶ F'` gives the map `{}_pu F ⟶ {}_pu F'` componentwise”.

> A map of presheaves `φ : F ⟶ F'` induces the map `{}_pu F ⟶ {}_pu F'` acting componentwise:
> `s_{(U, ψ)} ↦ φ_U(s_{(U, ψ)})`.

```lean
lemma ranObjEquivCompatibleFamilies_ran_map {F' : Cᵒᵖ ⥤ Type w} (φ : F ⟶ F')
    (s : (u.op.ran.obj F).obj (op V)) (X : CostructuredArrow u V) :
    (u.ranObjEquivCompatibleFamilies F' V ((u.op.ran.map φ).app (op V) s)).1 X =
      φ.app (op X.left) ((u.ranObjEquivCompatibleFamilies F V s).1 X)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.whiskeringLeft_obj_obj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.whiskeringLeft_obj_obj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/RestrictionRightAdjoint.lean#L68) (StacksFrontier): “`u^p : PSh(D) ⥤ PSh(C)` sends `G` to `G ∘ u`”.

## Tag 00XG, a lemma

[Tag 00XG](https://stacks.math.columbia.edu/tag/00XG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.ranCounit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.ranCounit#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/PullbackPushforwardUnit.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/PullbackPushforwardUnit.lean#L25) (StacksFrontier): “the canonical map `{}_p u F (u U) ⟶ F(U)` is the counit of `u^p ⊣ {}_p u`”.
- [`CategoryTheory.NatTrans.naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.NatTrans.naturality#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/PullbackPushforwardUnit.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/PullbackPushforwardUnit.lean#L27) (StacksFrontier): “compatibility with the restriction maps is naturality of that counit”. References: EGA 0 (8.2.1), “more general”.

## Tag 00XH, a lemma

[Tag 00XH](https://stacks.math.columbia.edu/tag/00XH) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.whiskeringLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.whiskeringLeft#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Presheaf/Functoriality/PrecompositionIso.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Presheaf/Functoriality/PrecompositionIso.lean#L25) (StacksCore): “the restriction functor `u^p : PSh(D) ⥤ PSh(C)` is precomposition with `u.op`”. References: EGA III (7.1.3), “partial”.
- [`CategoryTheory.Functor.ran`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.ran#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Presheaf/Functoriality/PrecompositionIso.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Presheaf/Functoriality/PrecompositionIso.lean#L27) (StacksCore): “the functor `{}_pu : PSh(C) ⥤ PSh(D)` is right Kan extension along `u.op`”.
- [`CategoryTheory.Functor.ranAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.ranAdjunction#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Presheaf/Functoriality/PrecompositionIso.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Sites/Presheaf/Functoriality/PrecompositionIso.lean#L29) (StacksCore): “`{}_pu` is right adjoint to `u^p`”.

## Tag 09VQ, a lemma

[Tag 09VQ](https://stacks.math.columbia.edu/tag/09VQ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Adjunction.compYonedaIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.compYonedaIso#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean#L30) (StacksFrontier): “(1) `u^p h_V = h_{v V}`, naturally in `V`”.
- [`CategoryTheory.mkInitialOfLeftAdjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.mkInitialOfLeftAdjoint#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean#L32) (StacksFrontier): “(2) `I^v_U` has the initial object `(u U, η_U)`”.
- [`CategoryTheory.mkTerminalOfRightAdjoint`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.mkTerminalOfRightAdjoint#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean#L34) (StacksFrontier): “(3) `{}^u_V I` has the final object `(v V, ε_V)`”.
- [`CategoryTheory.Functor.ranIsoRestrictionOfAdjunction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L215), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean#L36) (StacksFrontier): “(4) `{}_p u = v^p`”.
- [`CategoryTheory.Functor.restrictionIsoLanOfAdjunction`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L239), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/Functoriality/AdjointPairPresheafFunctors.lean#L38) (StacksFrontier): “(5) `u^p = v_p`”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.19, Tag 00XF](https://stacks.math.columbia.edu/tag/00XF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
