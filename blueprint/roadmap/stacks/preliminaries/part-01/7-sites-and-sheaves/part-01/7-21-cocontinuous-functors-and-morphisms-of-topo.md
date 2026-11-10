---
declaration: section
origin: cited
lean: main_adjunction00XO, main_left_exact, CategoryTheory.Functor.morphismOfTopoiOfCocontinuous, sheafPushforwardCocontinuousCompIso, CategoryTheory.isCocontinuous_comp, StacksOpenMapSite.isCocontinuous_isOpenMapFunctor, StacksOpenMapSite.sheafPullbackCocontinuousIsoTopPullback, StacksOpenMapSite.sheafPushforwardCocontinuousIsoTopPushforward
statement: formalized
proof: formalized
---

# 7.21 Cocontinuous functors and morphisms of topoi

Section 7.21 of the Stacks Project, [Tag 00XN](https://stacks.math.columbia.edu/tag/00XN). 8 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00XO, a lemma

[Tag 00XO](https://stacks.math.columbia.edu/tag/00XO) in the Stacks Project.

**`main_adjunction00XO`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousAdjunction.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousAdjunction.lean#L55). References: SGA 4 III (2.3), “3), special case”; SGA 4 III (2.6), “partial”; SGA 4 III (2.7), “partial”; SGA 4 III (4.4), “3), special case”; SGA 4 III (5.3), “partial”; SGA 4 IV (4.7), “partial”; SGA 4 IV (4.9.1), “For cocontinuous u”.

> **Stacks 00XO.** For a cocontinuous functor `u`, the functor `g^{-1}` is left adjoint
> to `g_*`.

```lean
theorem main_adjunction00XO :
    Nonempty (gInv C D J K u ⊣ gStar C D J K u)
```

**`main_left_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousAdjunction.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousAdjunction.lean#L69). References: SGA 4 III (2.3), “1)”.

> **Stacks 00XO.** The functor `g^{-1}` is left exact; together with the adjunction this makes
> `(g_*, g^{-1})` a morphism of topoi `Sh(C) ⟶ Sh(D)`.

```lean
theorem main_left_exact :
    PreservesFiniteLimits (gInv C D J K u)
```

**`CategoryTheory.Functor.morphismOfTopoiOfCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAMorphism.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAMorphism.lean#L90). The attribute's comment: “for a functor that is also continuous, with inverse image the restriction along F.op”. References: SGA 4 III (2.3), “special case”; SGA 4 III (2.4), “partial”; SGA 4 IV (4.6.1), “more general”; SGA 4 IV (4.7), “special case”; SGA 4 IV (4.9.1).

> The morphism of topoi attached to a functor of sites that is both continuous and
> cocontinuous (Stacks 00XO): its inverse image is restriction along `F.op` and its direct image is
> the right Kan extension along `F.op`.
>
> Each field is a single application, so that projecting out of it stays cheap: an inline proof of
> left exactness here makes every later unification that has to see through this definition
> expensive. Left exactness is the instance
> `CategoryTheory.Functor.preservesFiniteLimits_sheafPushforwardContinuous` (Stacks 04J4).

```lean
noncomputable def morphismOfTopoiOfCocontinuous {A : Type ua}
    [Category.{va} A] {B : Type ub} [Category.{vb} B]
    (F : A ⥤ B) (JA : GrothendieckTopology A) (JB : GrothendieckTopology B)
    [F.IsContinuous JA JB] [F.IsCocontinuous JA JB]
    [∀ (G : Aᵒᵖ ⥤ Type ww), F.op.HasPointwiseRightKanExtension G] :
    MorphismOfTopoi (Sheaf JA (Type ww)) (Sheaf JB (Type ww))
```

## Tag 03L5, a lemma

[Tag 03L5](https://stacks.math.columbia.edu/tag/03L5) in the Stacks Project.

**`sheafPushforwardCocontinuousCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousComp.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousComp.lean#L47). The attribute's comment: “(2)”. References: SGA 4 IV (4.7), “partial”.

> **Stacks 03L5**, second half. The canonical natural isomorphism between the direct image
> functor of the morphism of topoi attached to `u ⋙ v` and the composition of the direct image
> functors attached to `u` and to `v`.

```lean
noncomputable def sheafPushforwardCocontinuousCompIso (u : C ⥤ D) (v : D ⥤ E)
    [u.IsCocontinuous J K] [v.IsCocontinuous K L] :
    haveI : (u ⋙ v).IsCocontinuous J L := CategoryTheory.isCocontinuous_comp u v J K
    (u ⋙ v).sheafPushforwardCocontinuous (Type u) J L ≅
      u.sheafPushforwardCocontinuous (Type u) J K ⋙
        v.sheafPushforwardCocontinuous (Type u) K L
```

Declarations registered for the tag:

- [`CategoryTheory.isCocontinuous_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.isCocontinuous_comp#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousComp.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/CocontinuousComp.lean#L32) (StacksFrontier): “(1), the composition of two cocontinuous site functors is cocontinuous. Mathlib states it for arbitrary, independent object and hom universes; the statement this replaced fixed all three categories to a single universe `u` with `SmallCategory`, and its proof was a call to this declaration.”. References: SGA 4 III (4.4), “Cocontinuity of u∘i”.

## Tag 00XQ, an example

[Tag 00XQ](https://stacks.math.columbia.edu/tag/00XQ) in the Stacks Project.

**`StacksOpenMapSite.isCocontinuous_isOpenMapFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/OpenMapFunctor.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/OpenMapFunctor.lean#L50). References: SGA 4 III (2.5), “(ii), special case”; SGA 4 III (2.7), “cocontinuity of Φ”.

> **Stacks 00XQ.** For an open continuous map `f : X ⟶ Y` the functor
> `v : X_Zar ⥤ Y_Zar`, `U ↦ f(U)`, is cocontinuous: if `f(U) = ⋃ V j` is an open covering then
> `U = ⋃ (f⁻¹(V j) ∩ U)` is an open covering refining it.
>
> Formally, `v` is a left adjoint of the continuous functor `u = Opens.map f`
> (`IsOpenMap.adjunction`), and a left adjoint is cocontinuous exactly when its right adjoint
> preserves covering sieves (`Adjunction.isCocontinuous_iff_coverPreserving`).

```lean
theorem isCocontinuous_isOpenMapFunctor :
    (IsOpenMap.functor hf).IsCocontinuous (Opens.grothendieckTopology X)
      (Opens.grothendieckTopology Y)
```

**`StacksOpenMapSite.sheafPullbackCocontinuousIsoTopPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/OpenMapFunctor.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/OpenMapFunctor.lean#L63).

> **Stacks 00XQ.** The pullback `(v^p)^#` of the morphism of topoi attached to the cocontinuous
> functor `v = IsOpenMap.functor` is the usual topological pullback `f⁻¹` on sheaves of sets.
>
> By Stacks 00XX (2) the presheaf restriction along `v` is the left Kan extension along
> `u = Opens.map f`, so sheafifying identifies `(v^p)^#` with the construction of `f⁻¹` as
> `(u_p)^#`.

```lean
noncomputable def sheafPullbackCocontinuousIsoTopPullback :
    (IsOpenMap.functor hf).sheafPullbackCocontinuous (Type u) (Opens.grothendieckTopology X)
        (Opens.grothendieckTopology Y) ≅
      TopCat.Sheaf.pullback (Type u) f
```

**`StacksOpenMapSite.sheafPushforwardCocontinuousIsoTopPushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/OpenMapFunctor.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/OpenMapFunctor.lean#L80). References: SGA 4 III (2.7), “Φ_* ≅ (i^{-1})_s”.

> **Stacks 00XQ.** The pushforward `{}_sv` of the morphism of topoi attached to the cocontinuous
> functor `v = IsOpenMap.functor` is the usual topological pushforward `f_*` on sheaves of sets.
>
> Both are right adjoint to `f⁻¹`: for `{}_sv` this is Stacks 00XL
> (`CategoryTheory.Functor.sheafAdjunctionPullbackCocontinuous`) transported along
> `sheafPullbackCocontinuousIsoTopPullback`, and for `f_*` it is
> `TopCat.Sheaf.pullbackPushforwardAdjunction`.

```lean
noncomputable def sheafPushforwardCocontinuousIsoTopPushforward :
    haveI := isCocontinuous_isOpenMapFunctor hf
    (IsOpenMap.functor hf).sheafPushforwardCocontinuous (Type u) (Opens.grothendieckTopology X)
        (Opens.grothendieckTopology Y) ≅
      TopCat.Sheaf.pushforward (Type u) f
```

## Tag 00XR, a lemma

[Tag 00XR](https://stacks.math.columbia.edu/tag/00XR) in the Stacks Project.

**`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139). The attribute's comment: “(1)”. References: SGA 4 III (2.7), “more general”.

> **Stacks 00XR (1).** If `u` is both cocontinuous and continuous then the
> sheafification in `g^{-1} = (u^p\ )^#` is unnecessary: the sheaf pullback is naturally
> isomorphic to plain restriction along `u.op`, so `g^{-1}(G)(U) = G(u(U))`.
>
> Both functors are left adjoint to `u.sheafPushforwardCocontinuous` — the first by
> `sheafAdjunctionPullbackCocontinuous` (Stacks 00XL), the second by Mathlib's
> `sheafAdjunctionCocontinuous` — so they agree by uniqueness of left adjoints.
>
> See `sheafPullbackCocontinuousObjObjIso` for the displayed formula itself. Mathlib's
> `CoverLifting.lean` records this comparison as a `TODO`.

```lean
noncomputable def sheafPullbackCocontinuousIsoSheafPushforwardContinuous :
    u.sheafPullbackCocontinuous A J K ≅ u.sheafPushforwardContinuous A J K
```

**`CategoryTheory.Functor.sheafPullbackCocontinuousObjObjIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L151). The attribute's comment: “(1)”.

> **Stacks 00XR (1)**, the displayed formula `g^{-1}(G)(U) = G(u(U))`.
>
> Composing `sheafPullbackCocontinuousIsoSheafPushforwardContinuous` — which removes the
> sheafification — with the fact that `u.sheafPushforwardContinuous` is restriction along
> `u.op`, so that its sections over `U` are literally `G(u(U))`.

```lean
noncomputable def sheafPullbackCocontinuousObjObjIso (G : Sheaf K A) (U : C) :
    ((u.sheafPullbackCocontinuous A J K).obj G).obj.obj (Opposite.op U) ≅
      G.obj.obj (Opposite.op (u.obj U))
```

**`CategoryTheory.Functor.preservesColimits_sheafPushforwardContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L164). The attribute's comment: “(3)”. References: SGA 4 III (2.6), “u* commutes w/ colimits”; SGA 4 III (2.3), “continuous u; colimits”; SGA 4 IV (4.6.1), “f^* commutes with colim”.

> **Stacks 00XR (3)**, colimits. `g^{-1}` commutes with arbitrary colimits: by
> Mathlib's `sheafAdjunctionCocontinuous` it is a left adjoint, its right adjoint being
> `{}_s u = u.sheafPushforwardCocontinuous`.

```lean
instance preservesColimits_sheafPushforwardContinuous :
    PreservesColimits (u.sheafPushforwardContinuous A J K)
```

**`CategoryTheory.Functor.sheafAdjunctionLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L186). The attribute's comment: “(2)”. References: SGA 4 III (1.3), “1)”; SGA 4 IV (4.9.1), “left adjoint f^s ⊣ f_s”; SGA 4 IV (4.7.4), “sufficiency: F_! exists”; SGA 4 IV (4.6.1), “left adjoint f_!”; SGA 4 IV (4.7), “f̃_! ⊣ f̃^*”; SGA 4 III (5.3), “more general”.

> **Stacks 00XR (2).** `g^{-1}` has a left adjoint `g_! = (u_p\ )^#`.
>
> The left adjoint is Mathlib's `sheafPullbackConstruction.sheafPullback`, which is
> literally `(u_p\ )^#`: the left Kan extension `u.op.lan = u_p` followed by
> sheafification.

```lean
noncomputable def sheafAdjunctionLowerShriek :
    sheafPullbackConstruction.sheafPullback u A J K ⊣ u.sheafPushforwardContinuous A J K
```

**`CategoryTheory.Functor.preservesLimits_sheafPushforwardContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L197). The attribute's comment: “(3)”. References: SGA 4 III (2.6), “u* commutes w/ limits”; SGA 4 IV (4.6.1), “f^* commutes with lim”; SGA 4 IV (4.7), “f also continuous”; SGA 4 IV (3.1.2), “special case”.

> **Stacks 00XR (3)**, limits. `g^{-1}` commutes with arbitrary limits: it is a right
> adjoint, its left adjoint being `g_! = (u_p\ )^#`.

```lean
instance preservesLimits_sheafPushforwardContinuous :
    PreservesLimits (u.sheafPushforwardContinuous A J K)
```

**`CategoryTheory.Functor.preservesFiniteLimits_sheafPushforwardContinuous_of_essentiallySmall`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/MorphismOfSites/CocontinuousSmallModel.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/MorphismOfSites/CocontinuousSmallModel.lean#L104). The attribute's comment: “(3) at the universe of a small model”. References: SGA 4 III (1.8), “special case”; SGA 4½ Arcata (2.3.3), “left exactness of f_*”.

> **Stacks 00XR (3) at the universe of a small model.**  Restriction of sheaves of sets in
> `Type u` along a continuous functor between sites essentially small at `u` is left exact: it is
> the right adjoint of the lower shriek functor.

```lean
public instance preservesFiniteLimits_sheafPushforwardContinuous_of_essentiallySmall (v : C ⥤ D)
    (J : GrothendieckTopology C) (K : GrothendieckTopology D) [v.IsContinuous J K] :
    PreservesFiniteLimits (v.sheafPushforwardContinuous (Type u) J K)
```

## Tag 00XS, a lemma

[Tag 00XS](https://stacks.math.columbia.edu/tag/00XS) in the Stacks Project.

**`CategoryTheory.Functor.preservesLimitsOfShape_sheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Continuous.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Continuous.lean#L149). The attribute's comment: “If `u` is continuous and `C` has fibre products and equalizers which `u` preserves, then `g_!` commutes with fibre products and equalizers, and more generally with finite connected limits.”. References: SGA 4 III (1.3), “5), connected limits”; SGA 4 III (1.9.2), “more general”.

> Let `u : C ⥤ D` be a continuous functor of sites such that `C` has fibre products and
> equalizers and `u` preserves them. Then `g_! = u.sheafPullback` preserves limits of every finite
> connected shape, in particular fibre products and equalizers.

```lean
public theorem preservesLimitsOfShape_sheafPullback
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D]
    (u : C ⥤ D) (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsContinuous J K] [HasPullbacks C] [HasEqualizers C]
    [PreservesLimitsOfShape WalkingCospan u] [PreservesLimitsOfShape WalkingParallelPair u]
    [HasSheafify K (Type w)] [∀ Y : Dᵒᵖ, Small.{w} (CostructuredArrow u.op Y)]
    (I : Type t) [SmallCategory I] [FinCategory I] [IsConnected I] :
    PreservesLimitsOfShape I (u.sheafPullback (Type w) J K)
```

## Tag 00XT, a lemma

[Tag 00XT](https://stacks.math.columbia.edu/tag/00XT) in the Stacks Project.

**`CategoryTheory.Functor.isIso_sheafAdjunctionCocontinuous_counit`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Continuous.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Continuous.lean#L204). The attribute's comment: “If `u` is cocontinuous, continuous and fully faithful, the canonical map `g^{-1}g_*F → F` is an isomorphism for every sheaf `F` on `C`. Existence of `g_!` is not needed for this half.”. References: SGA 4 III (2.6), “u ff ⇒ u_* ff”; SGA 4 IV (4.10.5), “more general”.

> If `u : C ⥤ D` is cocontinuous, continuous and fully faithful, the counit
> `g^{-1}g_*F ⟶ F` of `g^{-1} ⊣ g_*` is an isomorphism; equivalently `g_*` is fully faithful.

```lean
public instance isIso_sheafAdjunctionCocontinuous_counit
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D] (u : C ⥤ D)
    (A : Type w) [Category.{w'} A]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsCocontinuous J K] [u.IsContinuous J K] [u.Full] [u.Faithful]
    [∀ F : Cᵒᵖ ⥤ A, u.op.HasPointwiseRightKanExtension F] :
    IsIso (u.sheafAdjunctionCocontinuous A J K).counit
```

**`CategoryTheory.Functor.isIso_unit_of_sheafPushforwardContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Continuous.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Continuous.lean#L220). The attribute's comment: “If `u` is cocontinuous, continuous and fully faithful, the canonical map `F → g^{-1}g_!F` is an isomorphism, for every left adjoint `g_!` of `g^{-1}`.”. References: SGA 4 III (2.6), “u ff ⇒ u_! ff”; SGA 4 I (5.6), “i⇒iii”; SGA 4 IV (4.10.5), “more general”.

> If `u : C ⥤ D` is cocontinuous, continuous and fully faithful, then for every left adjoint `L`
> of `g^{-1} = u^s` the unit `F ⟶ g^{-1}LF` of `L ⊣ g^{-1}` is an isomorphism.

```lean
public theorem isIso_unit_of_sheafPushforwardContinuous
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D] (u : C ⥤ D)
    (A : Type w) [Category.{w'} A]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsCocontinuous J K] [u.IsContinuous J K] [u.Full] [u.Faithful]
    [∀ F : Cᵒᵖ ⥤ A, u.op.HasPointwiseRightKanExtension F]
    {L : Sheaf J A ⥤ Sheaf K A} (adj : L ⊣ u.sheafPushforwardContinuous A J K) :
    IsIso adj.unit
```

**`CategoryTheory.Functor.isIso_sheafAdjunctionContinuous_unit`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Continuous.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Continuous.lean#L238). The attribute's comment: “If `u` is cocontinuous, continuous and fully faithful, the canonical map `F → g^{-1}g_!F` is an isomorphism for every sheaf `F` on `C`.”. References: SGA 4 III (2.6), “u ff ⇒ u_! ff”; SGA 4 VII (4.1), “more general”.

> If `u : C ⥤ D` is cocontinuous, continuous and fully faithful and `g^{-1}` has a left adjoint
> `g_!`, the unit `F ⟶ g^{-1}g_!F` of `g_! ⊣ g^{-1}` is an isomorphism; equivalently `g_!` is fully
> faithful.

```lean
public instance isIso_sheafAdjunctionContinuous_unit
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D] (u : C ⥤ D)
    (A : Type w) [Category.{w'} A]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsCocontinuous J K] [u.IsContinuous J K] [u.Full] [u.Faithful]
    [∀ F : Cᵒᵖ ⥤ A, u.op.HasPointwiseRightKanExtension F]
    [(u.sheafPushforwardContinuous A J K).IsRightAdjoint] :
    IsIso (u.sheafAdjunctionContinuous A J K).unit
```

## Tag 00XU, a lemma

[Tag 00XU](https://stacks.math.columbia.edu/tag/00XU) in the Stacks Project.

**`CategoryTheory.Functor.full_and_faithful_sheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/MorphismsOfTopoi.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/MorphismsOfTopoi.lean#L129). The attribute's comment: “The clause that `f^{-1} = g_!` is fully faithful, which needs only that `u` is cocontinuous, continuous and fully faithful. That `u` defines a morphism of sites `f : D → C` is `isMorphismOfSites_of_isTerminal`, and that `f ∘ g` is isomorphic to the identity morphism of `Sh(C)` is `isIso_sheafAdjunctionCocontinuous_counit`.”. References: SGA 4 III (2.6), “u ff ⇒ u_! ff”; SGA 4 I (5.14), “special case”.

> **Stacks 00XU**, the clause that `f^{-1}` is fully faithful. Let `(C, J)` and `(D, K)` be sites
> and let `u : C ⥤ D` be cocontinuous, continuous and fully faithful, and suppose that the inverse
> image `g^{-1}` of the associated morphism of topoi `g : Sh(C) → Sh(D)` admits a left adjoint `g_!`.
> Then `g_!` is fully faithful.
>
> When `u` also satisfies the hypotheses of Stacks 00X6, so that it defines a morphism of sites
> `f : D → C` with `f^{-1} = g_!`, this is the assertion that `f^{-1}` is fully faithful.

```lean
public theorem full_and_faithful_sheafPullback
    {C : Type u₁} [Category.{v₁} C] {D : Type u₂} [Category.{v₂} D] (u : C ⥤ D)
    (A : Type w) [Category.{w'} A]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsCocontinuous J K] [u.IsContinuous J K] [u.Full] [u.Faithful]
    [∀ F : Cᵒᵖ ⥤ A, u.op.HasPointwiseRightKanExtension F]
    [(u.sheafPushforwardContinuous A J K).IsRightAdjoint] :
    (u.sheafPullback A J K).Full ∧ (u.sheafPullback A J K).Faithful
```

## Tag 00XV, an example

[Tag 00XV](https://stacks.math.columbia.edu/tag/00XV) in the Stacks Project.

**`real_punctured_uOpens_not_cocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/ZariskiCounterexample.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/ZariskiCounterexample.lean#L158).

> Stacks Tag 00XV (Example 7.21.9): for `X = ℝ` and `Z = ℝ \ {0}` (with the subspace
> topology), the functor `u : X_Zar → Z_Zar`, `U ↦ Z ∩ U`, is NOT cocontinuous.

```lean
theorem real_punctured_uOpens_not_cocontinuous :
    ¬ CocontinuousZar (X := ℝ) {x : ℝ | x ≠ 0}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.21, Tag 00XN](https://stacks.math.columbia.edu/tag/00XN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
