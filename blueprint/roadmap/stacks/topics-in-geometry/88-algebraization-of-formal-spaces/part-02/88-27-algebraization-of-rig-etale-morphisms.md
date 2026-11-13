---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.completionModificationFunctor, AlgebraicGeometry.FormalSpace.completionModificationFunctorBaseChangeIso, AlgebraicGeometry.Space.completionOverFunctor_map_bijective, AlgebraicGeometry.FormalSpace.finiteTypeModificationCompletionFullyFaithful, AlgebraicGeometry.FormalSpace.isEquivalence_completionModificationFunctor_affineOver, AlgebraicGeometry.FormalSpace.isEquivalence_completionModificationFunctor
statement: formalized
proof: formalized
---

# 88.27 Algebraization of rig-étale morphisms

Section 88.27 of the Stacks Project, [Tag 0AR1](https://stacks.math.columbia.edu/tag/0AR1). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AR5, an equation

[Tag 0AR5](https://stacks.math.columbia.edu/tag/0AR5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.completionModificationFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationFunctor.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationFunctor.lean#L102). The attribute's comment: “the completion functor under the source's hypotheses, X a locally Noetherian algebraic space and T closed; the three conditions placing f\_\{/T} in the right-hand category are proved by 0AIZ, 0AQ1 (2) and 0AR2”.

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
> `AlgebraicGeometry.FormalSpace.completionFiniteTypeModificationFunctor`: that functor takes
> three hypotheses (`h0AIZ`, `hnoeth`, `hred`), and this one needs none of them. When they are
> given, the two functors are equal
> (`completionFiniteTypeModificationFunctor_eq_completionModificationFunctor`).

```lean
def completionModificationFunctor {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (T : Set (Space.points B S hS X)) (hT : IsClosed T) (hXsp : IsAlgebraicSpace B S hS X)
    (hX : Space.IsLocallyNoetherian B S hS X) :
    Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ) ⥤
      RigEtaleOverCompletion B S hS X T
```

## Tag 0GDQ, a lemma

[Tag 0GDQ](https://stacks.math.columbia.edu/tag/0GDQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.completionModificationFunctorBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleBaseChange.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleBaseChange.lean#L115). The attribute's comment: “the commutativity of the square as a natural isomorphism of the two composite functors, base change being defined by a universal property; the horizontal arrows are the functors of Stacks 0AR5 with the source's hypotheses, the left vertical arrow is base change along g on the finite-type modifications of Stacks 0AS2 and the right vertical arrow is base change along the completion of g”.

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

## Tag 0GDR, a lemma

[Tag 0GDR](https://stacks.math.columbia.edu/tag/0GDR) in the Stacks Project.

**`AlgebraicGeometry.Space.completionOverFunctor_map_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean, line 824](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean#L824).

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

**`AlgebraicGeometry.FormalSpace.finiteTypeModificationCompletionFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionLift.lean#L863). The attribute's comment: “in particular: the functor of Stacks 0AR5 is fully faithful”.

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

**`AlgebraicGeometry.FormalSpace.isEquivalence_completionModificationFunctor_affineOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionEssentialSurjectivity.lean, line 931](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineCompletionEssentialSurjectivity.lean#L931).

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

**`AlgebraicGeometry.FormalSpace.isEquivalence_completionModificationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean#L75).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
