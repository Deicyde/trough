---
declaration: section
origin: cited
lean: Stacks.Pushout.isPushout_spec_map_of_isPullback_of_surjective, AlgebraicGeometry.isColimit_of_fpqc, Stacks.Pushout.exists_isPushout_isPullback_isThickening_of_isFiniteOrderThickening, Stacks.Pushout.hasPushout_of_isFiniteOrderThickening_of_isAffineHom, Stacks.Pushout.isPullback_pushout_of_isFiniteOrderThickening_of_isAffineHom, Stacks.Pushout.pushout_inr_isThickening_of_isFiniteOrderThickening, Stacks.Pushout.pushout_structureSheaf_isPullback_of_isFiniteOrderThickening, Stacks.Pushout.exists_isPushout_isPullback_isThickening_of_isThickening
statement: formalized
proof: formalized
---

# 37.14 Pushouts in the category of schemes, I

Section 37.14 of the Stacks Project, [Tag 07RS](https://stacks.math.columbia.edu/tag/07RS). 6 tags here are carried by 30 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ET0, a lemma

[Tag 0ET0](https://stacks.math.columbia.edu/tag/0ET0) in the Stacks Project.

**`Stacks.Pushout.isPushout_spec_map_of_isPullback_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Pushout/SchemePushout.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Pushout/SchemePushout.lean#L88).

> **Stacks Project, Tag 0ET0.**  A fibre product of rings over a surjective map is sent by
> `Spec` to a pushout of schemes: if `p : A' ⟶ A` is surjective and the square with sides `p'`,
> `q'`, `q`, `p` is cartesian in `CommRingCat`, then its image under `Spec` is a pushout square
> of schemes.

```lean
theorem isPushout_spec_map_of_isPullback_of_surjective
    {A A' B B' : CommRingCat.{u}} (p : A' ⟶ A) (q : B ⟶ A)
    (p' : B' ⟶ B) (q' : B' ⟶ A') (h : IsPullback p' q' q p)
    (hp : Function.Surjective p) :
    IsPushout (Spec.map p) (Spec.map q) (Spec.map q') (Spec.map p')
```

## Tag 0BMP, a lemma

[Tag 0BMP](https://stacks.math.columbia.edu/tag/0BMP) in the Stacks Project.

**`AlgebraicGeometry.isColimit_of_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FpqcLocalColimit.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/CohenMacaulay/FpqcLocalColimit.lean#L195).

> **Stacks Project, Tag 0BMP.** The colimit property for a cocone of schemes can be checked
> on an fpqc covering of its vertex and on all pairwise overlaps.

```lean
public theorem isColimit_of_fpqc {J : Type v} [Category.{w} J]
    {F : J ⥤ Scheme.{u}} (c : Cocone F) {I : Type*}
    (W' : I → Scheme.{u}) (f : ∀ i, W' i ⟶ c.pt)
    (hfpqc : Presieve.ofArrows W' f ∈ Scheme.fpqcPrecoverage c.pt)
    (hlocal : ∀ i, Nonempty (IsColimit (baseChangeCocone c (f i))))
    (hoverlap : ∀ i j, Nonempty (IsColimit
      (baseChangeCocone c (pullback.fst (f i) (f j) ≫ f i)))) :
    Nonempty (IsColimit c)
```

## Tag 07RT, a lemma

[Tag 07RT](https://stacks.math.columbia.edu/tag/07RT) in the Stacks Project.

**`Stacks.Pushout.exists_isPushout_isPullback_isThickening_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean#L154). The attribute's comment: “the existence of the pushout, that Y ⊂ Y' is a thickening and that the square is cartesian; for a thickening of finite order”.

> **Stacks Project, Tag 07RT for a finite-order thickening, on an explicitly constructed
> apex.**  For a finite-order thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` there is
> a scheme `Q` with maps `A : X' ⟶ Q` and `B : Y ⟶ Q` whose square is cocartesian, is
> simultaneously cartesian, and has `B` a thickening.

```lean
theorem exists_isPushout_isPullback_isThickening_of_isFiniteOrderThickening (i : X ⟶ X')
    (f : X ⟶ Y) (hi : IsFiniteOrderThickening i) [IsAffineHom f] :
    ∃ (Q : Scheme.{u}) (A : X' ⟶ Q) (B : Y ⟶ Q),
      IsPushout i f A B ∧ IsPullback i f A B ∧ IsThickening B
```

**`Stacks.Pushout.hasPushout_of_isFiniteOrderThickening_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean#L168). The attribute's comment: “the existence of the pushout, for a thickening of finite order”.

> **Stacks Project, Tag 07RT, first assertion, for a finite-order thickening.**  A finite-order
> thickening and an affine morphism have a pushout in the category of schemes.

```lean
theorem hasPushout_of_isFiniteOrderThickening_of_isAffineHom (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsFiniteOrderThickening i) [IsAffineHom f] : HasPushout i f
```

**`Stacks.Pushout.isPullback_pushout_of_isFiniteOrderThickening_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean#L178). The attribute's comment: “that the square is cartesian, X = Y ×\_\{Y'} X'; for a thickening of finite order”.

> **Stacks Project, Tag 07RT, third assertion, for a finite-order thickening.**  The pushout
> square of a finite-order thickening and an affine morphism is also cartesian, that is,
> `X = Y ×_{Y'} X'`; stated for Mathlib's canonical pushout.

```lean
theorem isPullback_pushout_of_isFiniteOrderThickening_of_isAffineHom (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsFiniteOrderThickening i) [IsAffineHom f] [HasPushout i f] :
    IsPullback i f (pushout.inl i f) (pushout.inr i f)
```

**`Stacks.Pushout.pushout_inr_isThickening_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean#L191). The attribute's comment: “that Y ⊂ Y' is a thickening, for a thickening of finite order”.

> **Stacks Project, Tag 07RT, second assertion, for a finite-order thickening.**  The map from
> `Y` into the pushout of a finite-order thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y`
> is again a thickening; stated for Mathlib's canonical pushout.

```lean
theorem pushout_inr_isThickening_of_isFiniteOrderThickening (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsFiniteOrderThickening i) [IsAffineHom f] [HasPushout i f] :
    IsThickening (pushout.inr i f)
```

**`Stacks.Pushout.pushout_structureSheaf_isPullback_of_isFiniteOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutFiniteOrder.lean#L207). The attribute's comment: “the description of 𝒪\_\{Y'} as 𝒪\_Y ×\_\{f\_*𝒪\_X} f'\_*𝒪\_\{X'}; for a thickening of finite order”.

> **Stacks Project, Tag 07RT, fourth assertion, for a finite-order thickening.**  On every open
> `U` of the pushout of a finite-order thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y`
> the ring of sections is the fibre product of the rings of sections over the two preimages of `U`
> in `Y` and `X'` above the ring of sections over their common preimage in `X`; this is
> `𝒪_{Y'} = 𝒪_Y ×_{f_*𝒪_X} f'_*𝒪_{X'}`.

```lean
theorem pushout_structureSheaf_isPullback_of_isFiniteOrderThickening (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsFiniteOrderThickening i) [IsAffineHom f] [HasPushout i f] (U : (pushout i f).Opens) :
    IsPullback ((pushout.inr i f).app U) ((pushout.inl i f).app U)
      (f.app (pushout.inr i f ⁻¹ᵁ U))
      (i.app (pushout.inl i f ⁻¹ᵁ U) ≫ eqToHom (congrArg (fun V : X.Opens ↦ Γ(X, V))
        (congrArg (fun g : X ⟶ pushout i f ↦ g ⁻¹ᵁ U)
          (pushout.condition (f := i) (g := f)))))
```

**`Stacks.Pushout.exists_isPushout_isPullback_isThickening_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean#L77). The attribute's comment: “the existence of the pushout, that Y ⊂ Y' is a thickening and that the square is cartesian, X = Y ×\_\{Y'} X'”.

> **Stacks Project, Tag 07RT for an arbitrary thickening, on an explicitly constructed apex.**
> For a thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` there is a scheme `Q` with maps
> `A : X' ⟶ Q` and `B : Y ⟶ Q` whose square is cocartesian, is simultaneously cartesian, and has
> `B` a thickening.

```lean
theorem exists_isPushout_isPullback_isThickening_of_isThickening (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] :
    ∃ (Q : Scheme.{u}) (A : X' ⟶ Q) (B : Y ⟶ Q),
      IsPushout i f A B ∧ IsPullback i f A B ∧ IsThickening B
```

**`Stacks.Pushout.hasPushout_of_isThickening_of_isAffineHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean#L91). The attribute's comment: “the existence of the pushout”.

> **Stacks Project, Tag 07RT, first assertion.**  A thickening and an affine morphism have a
> pushout in the category of schemes.

```lean
theorem hasPushout_of_isThickening_of_isAffineHom' (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] : HasPushout i f
```

**`Stacks.Pushout.pushout_inr_isThickening'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean#L99). The attribute's comment: “that Y ⊂ Y' is a thickening”.

> **Stacks Project, Tag 07RT, second assertion.**  The map from `Y` into the pushout of a
> thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` is again a thickening; stated for
> Mathlib's canonical pushout.

```lean
theorem pushout_inr_isThickening' (i : X ⟶ X') (f : X ⟶ Y) (hi : IsThickening i) [IsAffineHom f]
    [HasPushout i f] : IsThickening (pushout.inr i f)
```

**`Stacks.Pushout.isPullback_pushout_of_isThickening_of_isAffineHom'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean#L107). The attribute's comment: “that the square is cartesian, X = Y ×\_\{Y'} X'”.

> **Stacks Project, Tag 07RT, third assertion.**  The pushout square of a thickening and an
> affine morphism is also cartesian, that is, `X = Y ×_{Y'} X'`; stated for Mathlib's canonical
> pushout.

```lean
theorem isPullback_pushout_of_isThickening_of_isAffineHom' (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] [HasPushout i f] :
    IsPullback i f (pushout.inl i f) (pushout.inr i f)
```

**`Stacks.Pushout.pushout_structureSheaf_isPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutUnconditional.lean#L117). The attribute's comment: “the description of 𝒪\_\{Y'} as 𝒪\_Y ×\_\{f\_*𝒪\_X} f'\_*𝒪\_\{X'}”.

> **Stacks Project, Tag 07RT, fourth assertion.**  On every open `U` of the pushout of a
> thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` the ring of sections is the fibre
> product of the rings of sections over the two preimages of `U` in `Y` and `X'` above the ring of
> sections over their common preimage in `X`; this is `𝒪_{Y'} = 𝒪_Y ×_{f_*𝒪_X} f'_*𝒪_{X'}`.

```lean
theorem pushout_structureSheaf_isPullback' (i : X ⟶ X') (f : X ⟶ Y) (hi : IsThickening i)
    [IsAffineHom f] [HasPushout i f] (U : (pushout i f).Opens) :
    IsPullback ((pushout.inr i f).app U) ((pushout.inl i f).app U)
      (f.app (pushout.inr i f ⁻¹ᵁ U))
      (i.app (pushout.inl i f ⁻¹ᵁ U) ≫ eqToHom (congrArg (fun V : X.Opens ↦ Γ(X, V))
        (congrArg (fun g : X ⟶ pushout i f ↦ g ⁻¹ᵁ U)
          (pushout.condition (f := i) (g := f)))))
```

## Tag 07RV, a lemma

[Tag 07RV](https://stacks.math.columbia.edu/tag/07RV) in the Stacks Project.

**`Stacks.Pushout.baseChangeFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean#L165). The attribute's comment: “the base-change functor F”.

> Base change from schemes over the pushout to compatible schemes over
> its two constituent pieces.

```lean
noncomputable def baseChangeFunctor {X X' Y : Scheme.{u}}
    (i : X ⟶ X') (f : X ⟶ Y) (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening i f hi
    Over (pushout i f) ⥤ gluingData i f
```

**`Stacks.Pushout.gluingFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean#L486). The attribute's comment: “the left adjoint G”.

> Gluing compatible schemes over `Y` and `X'` to a scheme over their
> pushout. Its objectwise pushout property is stated below.

```lean
noncomputable def gluingFunctor {X X' Y : Scheme.{u}}
    (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening i f hi
    gluingData i f ⥤ Over (pushout i f)
```

**`Stacks.Pushout.gluingFunctor_obj_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean#L562). The attribute's comment: “the left adjoint sends a triple to the pushout V ⨿\_\{V ×\_Y X} U'”.

> The glued scheme is the pushout of its two components along their
> identified restrictions to `X`, with the induced map to the ambient pushout.

```lean
theorem gluingFunctor_obj_isPushout {X X' Y : Scheme.{u}}
    (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f]
    (T : gluingData i f) :
    letI := hasPushout_of_isThickening i f hi
    ∃ (v : T.obj.left.left ⟶ ((gluingFunctor i f hi).obj T).left)
      (u' : T.obj.right.left ⟶ ((gluingFunctor i f hi).obj T).left),
      IsPushout (gluingSourceMap i f T) (pullback.fst T.obj.right.hom i) v u' ∧
      v ≫ ((gluingFunctor i f hi).obj T).hom =
        T.obj.left.hom ≫ pushout.inr i f ∧
      u' ≫ ((gluingFunctor i f hi).obj T).hom =
        T.obj.right.hom ≫ pushout.inl i f
```

**`Stacks.Pushout.gluingAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean#L1018). The attribute's comment: “the adjunction G ⊣ F”.

> **Stacks Project, Tag 07RV, the adjunction.**  Gluing is left adjoint to
> base change: a morphism from the glued scheme `V ⨿_U U'` to a scheme `Z` over `Y'` is the same
> thing as a morphism of compatible pairs from `(V, U', φ)` to the base change of `Z`.
>
> The bijection is the universal property of the pushout on one side and of the two fibre products
> on the other.

```lean
noncomputable def gluingAdjunction {X X' Y : Scheme.{u}}
    (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening i f hi
    gluingFunctor i f hi ⊣ baseChangeFunctor i f hi
```

**`Stacks.Pushout.gluingCompBaseChangeIsoId`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean, line 1528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluing.lean#L1528). The attribute's comment: “the composition F ∘ G is isomorphic to the identity functor”.

> **Stacks Project, Tag 07RV, the last assertion.**  The composition of
> gluing with base change is isomorphic to the identity functor: a compatible pair `(V, U', φ)` is
> recovered from the glued scheme `V ⨿_{V ×_Y X} U'` by base change along `Y ⟶ Y'` and
> `X' ⟶ Y'`.
>
> The isomorphism is the unit of `Stacks.Pushout.gluingAdjunction`, which is exactly the
> comparison map of the source.

```lean
noncomputable def gluingCompBaseChangeIsoId {X X' Y : Scheme.{u}}
    (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening i f hi
    gluingFunctor i f hi ⋙ baseChangeFunctor i f hi ≅ 𝟭 (gluingData i f)
```

## Tag 08KU, a lemma

[Tag 08KU](https://stacks.math.columbia.edu/tag/08KU) in the Stacks Project.

**`Stacks.Pushout.isEquivalence_flatBaseChangeTripleFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushout08KU.lean, line 916](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushout08KU.lean#L916). The attribute's comment: “the equivalence of the first clause”.

> **Stacks Project, Tag 08KU, the equivalence of the first clause.**  For a thickening
> `i : X ⟶ X'`, an affine morphism `f : X ⟶ Y`, the pushout `Y' = Y ⨿_X X'` and any
> `g : V' ⟶ Y'`, the comparison functor of the tag — a quasi-coherent `𝒪_{V'}`-module flat over
> `Y'` goes to its restrictions to `V = Y ×_{Y'} V'` and to `U' = X' ×_{Y'} V'` together with the
> canonical isomorphism of their restrictions to `U = X ×_{Y'} V'` — is an **equivalence of
> categories** onto the triples `(𝒢, ℱ', φ)` with `𝒢` quasi-coherent on `V` and flat over `Y`,
> `ℱ'` quasi-coherent on `U'` and flat over `X'`, and `φ` an isomorphism of their restrictions
> to `U`.
>
> The pushout `Y' = Y ⨿_X X'` is not assumed to exist: for a thickening `i` and an affine `f` it
> does, by the first assertion of [Stacks Project, Tag 07RT],
> `Stacks.Pushout.hasPushout_of_isThickening_of_isAffineHom`, whose [Stacks Project, Tag 06AD]
> hypothesis is discharged by `Stacks.Thickenings.forall_isAffine_of_isThickening`; that is the
> instance the statement binds for itself.

```lean
theorem isEquivalence_flatBaseChangeTripleFunctor (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening_of_isAffineHom forall_isAffine_of_isThickening i f hi
    ∀ g : V' ⟶ pushout i f, (flatBaseChangeTripleFunctor i f g hi).IsEquivalence
```

**`Stacks.Pushout.baseChangeTripleFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean#L182). The attribute's comment: “the comparison functor of the tag, on all modules on V'”.

> The comparison functor, sending a module on `V'` to its two restrictions to `V` and to `U'`
> together with the canonical isomorphism `Stacks.Pushout.overlapComparison` between their
> restrictions to `U`.

```lean
noncomputable def baseChangeTripleFunctor (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening_of_isAffineHom forall_isAffine_of_isThickening i f hi
    ∀ g : V' ⟶ pushout i f, V'.Modules ⥤ GluingTriple i f g
```

**`Stacks.Pushout.isFiniteType_baseChangeTripleFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean#L203). The attribute's comment: “the finite type clause, for an arbitrary module on V'”.

> If a module on `V'` is of finite type, then both components of its comparison triple, its
> restrictions to `V` and to `U'`, are of finite type.

```lean
theorem isFiniteType_baseChangeTripleFunctor_obj (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening_of_isAffineHom forall_isAffine_of_isThickening i f hi
    ∀ (g : V' ⟶ pushout i f) (M : V'.Modules) [M.IsFiniteType],
      ((baseChangeTripleFunctor i f hi g).obj M).target.IsFiniteType ∧
        ((baseChangeTripleFunctor i f hi g).obj M).ambient.IsFiniteType
```

**`Stacks.Pushout.isFinitePresentation_baseChangeTripleFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean#L220). The attribute's comment: “the finite presentation clause, for an arbitrary module on V'”.

> If a module on `V'` is of finite presentation, then both components of its comparison
> triple, its restrictions to `V` and to `U'`, are of finite presentation.

```lean
theorem isFinitePresentation_baseChangeTripleFunctor_obj (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening_of_isAffineHom forall_isAffine_of_isThickening i f hi
    ∀ (g : V' ⟶ pushout i f) (M : V'.Modules) [M.IsFinitePresentation],
      ((baseChangeTripleFunctor i f hi g).obj M).target.IsFinitePresentation ∧
        ((baseChangeTripleFunctor i f hi g).obj M).ambient.IsFinitePresentation
```

**`Stacks.Pushout.isFiniteType_iff_baseChangeTripleFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean#L583). The attribute's comment: “the finite type clause”.

> A quasi-coherent module on `V'` flat over `Y'` is of finite type if and only if both
> components of its comparison triple, its restrictions to `V` and to `U'`, are of finite type.

```lean
theorem isFiniteType_iff_baseChangeTripleFunctor_obj (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening_of_isAffineHom forall_isAffine_of_isThickening i f hi
    ∀ (g : V' ⟶ pushout i f) (M : FlatQuasicoherentModule g),
      M.obj.IsFiniteType ↔
        ((baseChangeTripleFunctor i f hi g).obj M.obj).target.IsFiniteType ∧
          ((baseChangeTripleFunctor i f hi g).obj M.obj).ambient.IsFiniteType
```

**`Stacks.Pushout.isFinitePresentation_iff_baseChangeTripleFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean, line 1158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutModules.lean#L1158). The attribute's comment: “the finite presentation clause”.

> If `V' ⟶ Y'` is locally of finite presentation, a quasi-coherent module on `V'` flat over `Y'`
> is of finite presentation if and only if both components of its comparison triple, its
> restrictions to `V` and to `U'`, are of finite presentation.

```lean
theorem isFinitePresentation_iff_baseChangeTripleFunctor_obj (hi : IsThickening i)
    [IsAffineHom f] :
    letI := hasPushout_of_isThickening_of_isAffineHom forall_isAffine_of_isThickening i f hi
    ∀ (g : V' ⟶ pushout i f), LocallyOfFinitePresentation g →
      ∀ M : FlatQuasicoherentModule g,
        M.obj.IsFinitePresentation ↔
          ((baseChangeTripleFunctor i f hi g).obj M.obj).target.IsFinitePresentation ∧
            ((baseChangeTripleFunctor i f hi g).obj M.obj).ambient.IsFinitePresentation
```

## Tag 07RX, a lemma

[Tag 07RX](https://stacks.math.columbia.edu/tag/07RX) in the Stacks Project.

**`Stacks.Pushout.gluingAdjunction_counit_app_isIso_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushout07RXFlat.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushout07RXFlat.lean#L383). The attribute's comment: “the closing paragraph: the counit G(F(W')) ⟶ W' is an isomorphism for W' flat over Y', for the adjunction of Tag 07RV over Mathlib's canonical pushout”.

> **[Stacks, Tag 07RX], the closing paragraph, first assertion.**  If `W'` is flat over the
> pushout `Y' = Y ⨿_X X'` of a thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y`, then
> the adjunction mapping `G(F(W')) ⟶ W'` is an isomorphism: `W'` is glued from its two base
> changes to `Y` and to `X'`.

```lean
theorem gluingAdjunction_counit_app_isIso_of_flat (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] :
    letI := hasPushout_of_isThickening i f hi
    ∀ W' : Over (pushout i f), Flat W'.hom →
      IsIso ((gluingAdjunction i f hi).counit.app W')
```

**`Stacks.Pushout.flatGluingEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushout07RXFlat.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushout07RXFlat.lean#L494). The attribute's comment: “the closing paragraph: F and G are mutually quasi-inverse between the schemes flat over Y' and the triples with both components flat, for Tag 07RV over Mathlib's canonical pushout”.

> **[Stacks, Tag 07RX], the closing paragraph, second assertion.**  For the pushout
> `Y' = Y ⨿_X X'` of a thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y`, the functors `F`
> and `G` of [Stacks Project, Tag 07RV] are mutually quasi-inverse between the category of schemes
> flat over `Y'` and the category of triples `(V, U', φ)` with `V ⟶ Y` and `U' ⟶ X'` flat.
>
> Both functors restrict to those subcategories, so the adjunction of Tag 07RV does; its unit is
> invertible by the last assertion of that tag and its counit by
> `Stacks.Pushout.gluingAdjunction_counit_app_isIso_of_flat`.

```lean
noncomputable def flatGluingEquivalence (i : X ⟶ X') (f : X ⟶ Y) (hi : IsThickening i)
    [IsAffineHom f] :
    letI := hasPushout_of_isThickening i f hi
    FlatGluingEquivalenceData i f hi
```

**`Stacks.Pushout.etale_gluingFunctor_obj_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutEtale.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutEtale.lean#L160). The attribute's comment: “clause (5): étale, for the gluing functor of Tag 07RV over Mathlib's canonical pushout”.

> **Stacks 07RX, clause (5).** The glued scheme of Tag 07RV over Mathlib's canonical pushout is
> étale over the pushout exactly when both of its pieces are étale over their bases.

```lean
theorem etale_gluingFunctor_obj_iff {X X' Y : Scheme.{u}} (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] (T : gluingData i f) :
    letI := hasPushout_of_isThickening i f hi
    Etale ((gluingFunctor i f hi).obj T).hom ↔
      (Etale T.obj.left.hom ∧ Etale T.obj.right.hom)
```

**`Stacks.Pushout.locallyOfFiniteType_gluingFunctor_obj_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean#L78). The attribute's comment: “clause (1): locally of finite type, for the gluing functor of Tag 07RV over Mathlib's canonical pushout”.

> **[Stacks, Tag 07RX], clause (1).**  The scheme glued from a triple `(V, U', φ)` across the
> pushout `Y' = Y ⨿_X X'` of a thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` is
> locally of finite type over `Y'` if and only if both `V ⟶ Y` and `U' ⟶ X'` are.

```lean
theorem locallyOfFiniteType_gluingFunctor_obj_iff (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] (T : gluingData i f) :
    letI := hasPushout_of_isThickening i f hi
    LocallyOfFiniteType ((gluingFunctor i f hi).obj T).hom ↔
      (LocallyOfFiniteType T.obj.left.hom ∧ LocallyOfFiniteType T.obj.right.hom)
```

**`Stacks.Pushout.flat_gluingFunctor_obj_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean#L92). The attribute's comment: “clause (2): flat, for the gluing functor of Tag 07RV over Mathlib's canonical pushout”.

> **[Stacks, Tag 07RX], clause (2).**  The scheme glued from a triple `(V, U', φ)` across the
> pushout `Y' = Y ⨿_X X'` of a thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` is flat
> over `Y'` if and only if both `V ⟶ Y` and `U' ⟶ X'` are flat.

```lean
theorem flat_gluingFunctor_obj_iff (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] (T : gluingData i f) :
    letI := hasPushout_of_isThickening i f hi
    Flat ((gluingFunctor i f hi).obj T).hom ↔
      (Flat T.obj.left.hom ∧ Flat T.obj.right.hom)
```

**`Stacks.Pushout.flat_and_locallyOfFinitePresentation_gluingFunctor_obj_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean#L106). The attribute's comment: “clause (3): flat and locally of finite presentation, for the gluing functor of Tag 07RV over Mathlib's canonical pushout”.

> **[Stacks, Tag 07RX], clause (3).**  The scheme glued from a triple `(V, U', φ)` across the
> pushout `Y' = Y ⨿_X X'` of a thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` is flat
> and locally of finite presentation over `Y'` if and only if both `V ⟶ Y` and `U' ⟶ X'` are.

```lean
theorem flat_and_locallyOfFinitePresentation_gluingFunctor_obj_iff (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] (T : gluingData i f) :
    letI := hasPushout_of_isThickening i f hi
    (Flat ((gluingFunctor i f hi).obj T).hom ∧
        LocallyOfFinitePresentation ((gluingFunctor i f hi).obj T).hom) ↔
      ((Flat T.obj.left.hom ∧ LocallyOfFinitePresentation T.obj.left.hom) ∧
        (Flat T.obj.right.hom ∧ LocallyOfFinitePresentation T.obj.right.hom))
```

**`Stacks.Pushout.smooth_gluingFunctor_obj_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ThickeningPushoutGluingUnconditional.lean#L123). The attribute's comment: “clause (4): smooth, for the gluing functor of Tag 07RV over Mathlib's canonical pushout”.

> **[Stacks, Tag 07RX], clause (4).**  The scheme glued from a triple `(V, U', φ)` across the
> pushout `Y' = Y ⨿_X X'` of a thickening `i : X ⟶ X'` and an affine morphism `f : X ⟶ Y` is
> smooth over `Y'` if and only if both `V ⟶ Y` and `U' ⟶ X'` are smooth.

```lean
theorem smooth_gluingFunctor_obj_iff (i : X ⟶ X') (f : X ⟶ Y)
    (hi : IsThickening i) [IsAffineHom f] (T : gluingData i f) :
    letI := hasPushout_of_isThickening i f hi
    Smooth ((gluingFunctor i f hi).obj T).hom ↔
      (Smooth T.obj.left.hom ∧ Smooth T.obj.right.hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.14, Tag 07RS](https://stacks.math.columbia.edu/tag/07RS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
