---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.completionModificationFunctor, AlgebraicGeometry.FormalSpace.completionOfFiniteTypeModification, AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctor, AlgebraicGeometry.FormalSpace.completionModificationFunctorBaseChangeIso, AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctorBaseChangeIso, AlgebraicGeometry.Space.completionOverFunctor_map_bijective, AlgebraicGeometry.FormalSpace.finiteTypeModificationCompletionFullyFaithful, AlgebraicGeometry.FormalSpace.isEquivalence_completionModificationFunctor_affineOver
statement: formalized
proof: formalized
---

# 88.27 Algebraization of rig-étale morphisms

Section 88.27 of the Stacks Project, [Tag 0AR1](https://stacks.math.columbia.edu/tag/0AR1). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AR5, an equation

[Tag 0AR5](https://stacks.math.columbia.edu/tag/0AR5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.completionModificationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationFunctor.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationFunctor.lean#L102). The attribute's comment: “the completion functor with the source's hypotheses only: X a locally Noetherian algebraic space and T closed; the three conditions placing f\_\{/T} in the right-hand category are proved by 0AIZ, 0AQ1 (2) and 0AR2”.

> **Stacks 0AR5.** Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be
> closed and let `U ⊂ X` be the open subspace with `|U| = |X| ∖ T`. Completion along `T` is a
> functor from the morphisms `f : X' ⟶ X` of algebraic spaces which are locally of finite type and
> an isomorphism over `U` to the morphisms `g : W ⟶ X_{/T}` of formal algebraic spaces with `W`
> locally Noetherian and `g` rig-étale.
>
> The arrow map is `AlgebraicGeometry.Space.completionOverFunctor`. The three conditions on the
> value are proved: `X'_{/T'}` is a formal algebraic space by Stacks 0AIZ, it is locally Noetherian
> by Stacks 0AQ1 (2) since `X'` is locally of finite type over the locally Noetherian `X`, and
> `f_{/T}` is rig-étale by Stacks 0AR2 since `U' ⟶ U` is an isomorphism.
>
> This is a new object and not a copy of
> `AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctor`: that functor is only
> defined when three hypotheses (`h0AIZ`, `hnoeth`, `hred`) are given, and this one needs none of
> them. When they are given, the two functors are equal
> (`completionFiniteTypeModificationFunctor_eq_completionModificationFunctor`).

```lean
def completionModificationFunctor {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (T : Set (Space.points B S hS X)) (hT : IsClosed T) (hXsp : IsAlgebraicSpace B S hS X)
    (hX : Space.IsLocallyNoetherian B S hS X) :
    Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ) ⥤
      RigEtaleOverCompletion B S hS X T
```

**`AlgebraicGeometry.FormalSpace.completionOfFiniteTypeModification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtale.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtale.lean#L431). The attribute's comment: “the arrow of the displayed equation, that is the assignment sending a morphism locally of finite type which is an isomorphism over `U` to its completion along `T`, together with the three conditions placing the result in the right-hand collection. The rig-étaleness, which is what the source says makes the arrow well defined, is Stacks 0AR2 (`AlgebraicGeometry.FormalSpace.isRigEtale_completionSheafMap`) applied through the proof here that `U'` is the fibre product of `U` with `f`, so that the modification condition makes `U' ⟶ U` an isomorphism and therefore étale. The two conditions on the source `X'_{/T'}` are hypotheses: Stacks 0AIZ, that a completion along a closed set is a formal algebraic space, as `h0AIZ`, and its locally Noetherian refinement as `hnoeth`; neither is carried by this library, which proves only the affine case Stacks 0AIY of the first. The reduction of Stacks 0AR2 to the affine case is forwarded as `hred`”.

> **Stacks 0AR5.** The arrow of the displayed equation: a morphism `f : X' ⟶ X` of algebraic
> spaces over `S` which is locally of finite type and an isomorphism over `U` is sent to
> `f_{/T} : X'_{/T'} ⟶ X_{/T}`, a rig-étale morphism with locally Noetherian source.
>
> That `f_{/T}` is rig-étale is Stacks 0AR2 applied to `U' ⟶ U`, which is an isomorphism — and
> hence étale — because `U'` is the fibre product of `U` with `f`.

```lean
def completionOfFiniteTypeModification {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (hX : Space.IsLocallyNoetherian B S hS X)
    (M : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ))
    (h0AIZ : IsFormalAlgebraicSpaceCompletionSheaf B S hS X T)
    (hnoeth : IsLocallyNoetherianCompletionSheaf B S hS X T)
    (hred : ChartSquareReducesToIsEtaleOutside B S hS M.obj.hom T) :
    RigEtaleOverCompletion B S hS X T
```

**`AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleFunctor.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleFunctor.lean#L120). The attribute's comment: “the displayed assignment as a FUNCTOR, not only on objects: the object map is `AlgebraicGeometry.FormalSpace.completionOfFiniteTypeModification`, which is what this library already carried for Stacks 0AR5, and the arrow map is the completion along `T` of a morphism over `X`, which is `AlgebraicGeometry.Space.completionOverFunctor` and carries no hypotheses. The three conditions placing the value in the right-hand collection are the hypotheses of the object map, unchanged except that the reduction of Stacks 0AR2 to the affine case is asked of every object of the source category rather than of one, which is the only form in which a functor can carry it: Stacks 0AIZ for the algebraic spaces over `X` as `h0AIZ`, its locally Noetherian refinement from Stacks 0AQ1 as `hnoeth`, and the reduction of Stacks 0AR2 as `hred`”.

> **Stacks 0AR5, as a functor.** Sending a finite-type modification `f : X' ⟶ X` of `X`
> outside `U` to `f_{/T} : X'_{/T'} ⟶ X_{/T}` is a functor to the rig-étale morphisms with
> locally Noetherian source over `X_{/T}`.

```lean
def completionFiniteTypeModificationFunctor {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (hX : Space.IsLocallyNoetherian B S hS X)
    (h0AIZ : IsFormalAlgebraicSpaceCompletionSheaf B S hS X T)
    (hnoeth : IsLocallyNoetherianCompletionSheaf B S hS X T)
    (hred : ChartSquareReducesToIsEtaleOutsideModifications T) :
    Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ) ⥤
      RigEtaleOverCompletion B S hS X T
```

## Tag 0GDQ, a lemma

[Tag 0GDQ](https://stacks.math.columbia.edu/tag/0GDQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.completionModificationFunctorBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleBaseChange.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleBaseChange.lean#L111).

> **Stacks 0GDQ.** Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be
> closed with open complement `U`, and let `g : X₁ ⟶ X` be a morphism of algebraic spaces with `X₁`
> locally Noetherian; write `T₁ = |g|⁻¹T` and `U₁ = g⁻¹U`. Then the square
> ```
>   C_{X,T}   ⟶  C_{X_{/T}}
>      ↓              ↓
>   C_{X₁,T₁} ⟶  C_{X_{1,/T_1}}
> ```
> commutes, where the horizontal arrows are the functors of Stacks 0AR5, the left vertical arrow is
> base change along `g` and the right vertical arrow is base change along `X_{1, /T_1} ⟶ X_{/T}`.
> Base change being defined by a universal property, commutativity is a natural isomorphism of the
> two composite functors.
>
> The proof is the source's: the completion functor `(h : Y ⟶ X) ↦ Y_{/T}` commutes with fibre
> products.

```lean
def completionModificationFunctorBaseChangeIso {X₁ X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (g : X₁ ⟶ X) (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (hX₁sp : IsAlgebraicSpace B S hS X₁) (hXsp : IsAlgebraicSpace B S hS X)
    (hX₁ : Space.IsLocallyNoetherian B S hS X₁) (hX : Space.IsLocallyNoetherian B S hS X) :
    Space.finiteTypeBaseChangePointsFunctor hX₁sp hXsp g T ⋙
        completionModificationFunctor (Space.pointsMap B S hS X₁ g ⁻¹' T)
          (hT.preimage (Space.continuous_pointsMap B S hS g)) hX₁sp hX₁ ≅
      completionModificationFunctor T hT hXsp hX ⋙
        rigEtaleOverCompletionPullback g T hT hX₁sp hXsp hX₁ hX
```

**`AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctorBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleFunctor.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleFunctor.lean#L184). The attribute's comment: “the commutativity of the square, as an isomorphism of the two composite functors rather than an equality, the two completion functors being defined by a sheafification; and conditional on the right vertical arrow, which is the hypothesis `D` together with `hD` saying that `D` restricts base change along `X_{1, /T_1} ⟶ X_{/T}`: the categories of Stacks 0AS2 are realized here as full subcategories of an over-category, and base change on them is not available in this repository without the fibre products of formal algebraic spaces that Stacks 0AS2 provides”.

> **The square of Stacks 0GDQ**, for the categories of Stacks 0AS2 and 0AR5 and conditional
> on its right vertical arrow. Base change along `g : X₁ ⟶ X` on finite-type modifications
> followed by the functor of Stacks 0AR5 for `X₁` and `T₁ = |g|⁻¹T` agrees with the functor of
> Stacks 0AR5 for `X` and `T` followed by any functor restricting base change along
> `X_{1, /T_1} ⟶ X_{/T}`.
>
> The commutativity is the one the source's proof gives: the completion functor
> `(h : Y ⟶ X) ↦ Y_{/T}` commutes with fibre products, which is
> `AlgebraicGeometry.Space.completionBaseChangeIso` and, after restriction to the two
> subcategories, `AlgebraicGeometry.Space.restrictedCompletionBaseChangeSquareIso`.

```lean
def completionFiniteTypeModificationFunctorBaseChangeIso
    {X₁ X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X₁ ⟶ X)
    (hX₁sp : IsAlgebraicSpace B S hS X₁) (hXsp : IsAlgebraicSpace B S hS X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (hX : Space.IsLocallyNoetherian B S hS X)
    (h0AIZ : IsFormalAlgebraicSpaceCompletionSheaf B S hS X T)
    (hnoeth : IsLocallyNoetherianCompletionSheaf B S hS X T)
    (hred : ChartSquareReducesToIsEtaleOutsideModifications T)
    (hX₁ : Space.IsLocallyNoetherian B S hS X₁)
    (h0AIZ₁ : IsFormalAlgebraicSpaceCompletionSheaf B S hS X₁
      (Space.pointsMap B S hS X₁ g ⁻¹' T))
    (hnoeth₁ : IsLocallyNoetherianCompletionSheaf B S hS X₁
      (Space.pointsMap B S hS X₁ g ⁻¹' T))
    (hred₁ : ChartSquareReducesToIsEtaleOutsideModifications
      (Space.pointsMap B S hS X₁ g ⁻¹' T))
    {D : RigEtaleOverCompletion B S hS X T ⥤
      RigEtaleOverCompletion B S hS X₁ (Space.pointsMap B S hS X₁ g ⁻¹' T)}
    (hD : D ⋙ ObjectProperty.ι (fun W : Over (Space.completionSheaf B S hS X₁
            (Space.pointsMap B S hS X₁ g ⁻¹' T)) =>
          IsFormalAlgebraicSpace B S hS W.left ∧ IsLocallyNoetherian B S hS W.left ∧
            IsRigEtale B S hS W.hom) ≅
      ObjectProperty.ι (fun W : Over (Space.completionSheaf B S hS X T) =>
          IsFormalAlgebraicSpace B S hS W.left ∧ IsLocallyNoetherian B S hS W.left ∧
            IsRigEtale B S hS W.hom) ⋙
        Over.pullback (Space.completionSheafMap B S hS g T)) :
    Space.finiteTypeBaseChangePointsFunctor hX₁sp hXsp g T ⋙
        completionFiniteTypeModificationFunctor (Space.pointsMap B S hS X₁ g ⁻¹' T)
          (hT.preimage (Space.continuous_pointsMap B S hS g)) hX₁ h0AIZ₁ hnoeth₁ hred₁ ≅
      completionFiniteTypeModificationFunctor T hT hX h0AIZ hnoeth hred ⋙ D
```

## Tag 0GDR, a lemma

[Tag 0GDR](https://stacks.math.columbia.edu/tag/0GDR) in the Stacks Project.

**`AlgebraicGeometry.Space.completionOverFunctor_map_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean, line 824](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean#L824).

> **Stacks 0GDR.** Let `X` be a locally Noetherian algebraic space over `S`, `T ⊆ |X|`
> closed and `U ⊂ X` the open subspace with `|U| = |X| ∖ T`. Let `f : X' ⟶ X` be a morphism of
> algebraic spaces which is locally of finite type and an isomorphism over `U`, and let
> `g : Y ⟶ X` be a morphism with `Y` a locally Noetherian algebraic space. Then completion along
> `T` (`AlgebraicGeometry.Space.completionOverFunctor`, the completion of Section 0GDB used in
> Stacks 0AR5) is a bijection from the morphisms `Y ⟶ X'` over `X` to the morphisms
> `Y_{/T} ⟶ X'_{/T}` over `X_{/T}`.
>
> Injectivity is `AlgebraicGeometry.Space.completionOverFunctor_map_injective`; surjectivity is
> `AlgebraicGeometry.Space.exists_completionOverFunctor_map_eq_of_affineCompletionLiftProperty`
> applied to its affine case `AlgebraicGeometry.Space.affineCompletionLiftProperty`. The
> consequence that the functor of Stacks 0AR5 is fully faithful is
> `AlgebraicGeometry.FormalSpace.finiteTypeModificationCompletionFullyFaithful`.

```lean
theorem completionOverFunctor_map_bijective {X X' Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X)
    (hXnoeth : HasEtaleLocalProperty B S hS X
      (fun V : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian V))
    {T : Set (points B S hS X)} (hT : IsClosed T) {f : X' ⟶ X}
    (hX' : IsAlgebraicSpace B S hS X') (hf : IsLocallyOfFiniteType B S hS f)
    (hfU : IsIso (pullback.snd f (openSubspaceOfPoints B S hS X Tᶜ).ι)) (g : Y ⟶ X)
    (hY : IsAlgebraicSpace B S hS Y)
    (hYnoeth : HasEtaleLocalProperty B S hS Y
      (fun V : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian V)) :
    Function.Bijective
      (fun a : Over.mk g ⟶ Over.mk f => (completionOverFunctor B S hS T).map a)
```

**`AlgebraicGeometry.FormalSpace.finiteTypeModificationCompletionFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean, line 863](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean#L863). The attribute's comment: “in particular: the functor of Stacks 0AR5 is fully faithful”.

> **Stacks 0GDR, the consequence: the functor of Stacks 0AR5 is fully faithful.** For a
> locally Noetherian algebraic space `X` and a closed `T ⊆ |X|`, completion along `T` is fully
> faithful on the morphisms `X' ⟶ X` locally of finite type which are an isomorphism over the
> open subspace with points `|X| ∖ T`. The functor of Stacks 0AR5,
> `AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctor`, is this functor with
> its values regarded in the full subcategory of rig-étale morphisms with locally Noetherian
> formal source (`AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctor_comp_ι`).
> Fullness and faithfulness are the two halves of the bijection
> `AlgebraicGeometry.Space.completionOverFunctor_map_bijective`, applied to a finite-type
> modification `M` as the locally Noetherian source: `M` is locally Noetherian because it is
> locally of finite type over `X`.

```lean
noncomputable def finiteTypeModificationCompletionFullyFaithful
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXnoeth : Space.HasEtaleLocalProperty B S hS X
      (fun V : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian V))
    (T : Set (Space.points B S hS X)) (hT : IsClosed T) :
    (finiteTypeModificationCompletion (B := B) (S := S) (hS := hS) T).FullyFaithful
```

## Tag 0ARA, a lemma

[Tag 0ARA](https://stacks.math.columbia.edu/tag/0ARA) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEquivalence_completionModificationFunctor_affineOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionEssentialSurjectivity.lean, line 931](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionEssentialSurjectivity.lean#L931).

> **Stacks 0ARA.** Let `S` be a scheme, let `X` be a locally Noetherian algebraic space over
> `S` which is affine, so `X = Spec R` with `R` Noetherian, let `T ⊆ |X|` be closed and let
> `U ⊂ X` be the open subspace with `|U| = |X| ∖ T`. Then the completion functor of Stacks 0AR5,
> `AlgebraicGeometry.FormalSpace.completionModificationFunctor`, from the morphisms `f : X' ⟶ X`
> of algebraic spaces which are locally of finite type and an isomorphism over `U` to the
> morphisms `g : W ⟶ X_{/T}` of formal algebraic spaces with `W` locally Noetherian and `g`
> rig-étale, is an equivalence.
>
> Full faithfulness is Stacks 0GDR
> (`AlgebraicGeometry.FormalSpace.completionModificationFunctorFullyFaithful`). Essential
> surjectivity is `exists_finiteTypeModification_completion_iso_of_isRigEtale`, assembled as in the
> source from Step 1 (Stacks 0AR4 and 0AR9), Step 2 (a separated `W`: Stacks 0AR8 and 04S6 applied
> to the algebraizations of an affine étale covering) and Step 3 (a general `W`, whose
> `Wᵢ ×_W Wⱼ` are separated).

```lean
theorem isEquivalence_completionModificationFunctor_affineOver
    {R : Type u} [CommRing R] [IsNoetherianRing R] (hR : B.Contains (Spec (.of R)))
    (s : Spec (.of R) ⟶ S)
    (T : Set (Space.points B S hS (yoneda.obj (affineOver B S hS hR s)))) (hT : IsClosed T) :
    (completionModificationFunctor T hT (isAlgebraicSpace_yoneda B S hS (affineOver B S hS hR s))
      (Space.isLocallyNoetherian_yoneda_affineOver hR s)).IsEquivalence
```

## Tag 0ARB, a theorem

[Tag 0ARB](https://stacks.math.columbia.edu/tag/0ARB) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEquivalence_completionModificationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean#L75).

> **Stacks 0ARB.** Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be
> closed and let `U ⊂ X` be the open subspace with `|U| = |X| ∖ T`. The completion functor of
> Stacks 0AR5 sends `f : X' ⟶ X` to `f_{/T} : X'_{/T'} ⟶ X_{/T}`. Its source is the morphisms of
> algebraic spaces which are locally of finite type and an isomorphism over `U`. Its target is the
> morphisms `g : W ⟶ X_{/T}` of formal algebraic spaces with `W` locally Noetherian and `g`
> rig-étale. This functor is an equivalence.
>
> Full faithfulness is Stacks 0GDR (`completionModificationFunctorFullyFaithful`). For essential
> surjectivity, the base change of `W` to each affine étale chart `Spec R ⟶ X`, `R` Noetherian, is
> an object of the right-hand category for `Spec R` (`rigEtaleOverCompletionBaseChange`, through
> Stacks 0GD1). By Stacks 0ARA
> (`exists_finiteTypeModification_completion_iso_of_isRigEtale`) it is the completion of a
> finite-type modification of `Spec R`. These glue
> (`mem_essImage_completionModificationFunctor_of_affine_charts`).

```lean
theorem isEquivalence_completionModificationFunctor {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (T : Set (Space.points B S hS X)) (hT : IsClosed T) (hXsp : IsAlgebraicSpace B S hS X)
    (hX : Space.IsLocallyNoetherian B S hS X) :
    (completionModificationFunctor T hT hXsp hX).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.27, Tag 0AR1](https://stacks.math.columbia.edu/tag/0AR1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
