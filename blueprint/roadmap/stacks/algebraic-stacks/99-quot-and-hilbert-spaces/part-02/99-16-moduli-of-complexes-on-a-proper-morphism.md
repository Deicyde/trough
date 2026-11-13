---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_negativeExtLocus_and_vanishing_and_representable, AlgebraicGeometry.Space.ComplexesSituation.conditions_negativeSelfExt_selfHom_overBaseChange, AlgebraicGeometry.Space.ComplexesSituation, AlgebraicGeometry.Space.ComplexesObject, AlgebraicGeometry.Space.ComplexesHom, AlgebraicGeometry.Space.ComplexesSituation.complexesCategory, AlgebraicGeometry.Space.ComplexesSituation.complexesProjection, AlgebraicGeometry.Space.ComplexesSituation.complexesFunctor
statement: formalized
proof: formalized
---

# 99.16 Moduli of complexes on a proper morphism

Section 99.16 of the Stacks Project, [Tag 0DLB](https://stacks.math.columbia.edu/tag/0DLB). 12 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DLC, a lemma

[Tag 0DLC](https://stacks.math.columbia.edu/tag/0DLC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_negativeExtLocus_and_vanishing_and_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean#L222).

> **Stacks 0DLC.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is proper,
> flat and of finite presentation, and let `K`, `E ∈ D(𝒪_X)` with `K` pseudo-coherent and `E`
> `Y`-perfect (Stacks 0DKN). For a point `y : Spec(k) ⟶ Y` with values in a field write `K_y`, `E_y`
> for the pullbacks to the fibre `X_y`.
> 1. There is an open `W ⊆ Y` characterized by: `y ∈ |W|` if and only if
>    `Ext^i_{𝒪_{X_y}}(K_y, E_y) = 0` for `i < 0`
>    (`AlgebraicGeometry.Space.IsNegativeExtLocus`).
> 2. For such a `W` and every algebraic space `V` over `Y` whose morphism to `Y` factors through `W`,
>    `Ext^i_{𝒪_{X_V}}(K_V, E_V) = 0` for `i < 0`, where `X_V` is the base change of `X` and `K_V`,
>    `E_V` are the derived pullbacks of `K` and `E` to `X_V`.
> 3. For such a `W`, the functor `V ↦ Hom_{𝒪_{X_V}}(K_V, E_V)` on the schemes over `W` is
>    representable by an algebraic space affine and of finite presentation over `W` (in particular
>    it is a sheaf).

```lean
theorem exists_negativeExtLocus_and_vanishing_and_representable
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hproper : IsProper B S hS f.hom)
    (hflat : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (K E : derivedModules B S hS X) (hK : (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent K)
    (hE : IsPerfectRelativeToCanonical B S hS f hflat hfp.1 E) :
    (∃ W : OpenSubspaces B S hS Y.1, IsNegativeExtLocus f K E W) ∧
      (∀ W : OpenSubspaces B S hS Y.1, IsNegativeExtLocus f K E W →
        ∀ V : Over Y, (∃ g : V.left ⟶ openSubspaceAsSpace B S hS W,
            g ≫ openSubspaceImmersion B S hS W = V.hom) →
        ∀ i : ℤ, i < 0 →
          Subsingleton (((smallEtaleDerivedPullbackData B S hS).pull (overProjection f V)).obj K ⟶
            (((smallEtaleDerivedPullbackData B S hS).pull (overProjection f V)).obj E)⟦i⟧)) ∧
      (∀ W : OpenSubspaces B S hS Y.1, IsNegativeExtLocus f K E W →
        IsAffineFinitePresentationAlgebraicSpaceOver (openSubspaceAsSpace B S hS W)
          (relativeDerivedHomOverOpen f K E W))
```

## Tag 0DLD, a lemma

[Tag 0DLD](https://stacks.math.columbia.edu/tag/0DLD) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.conditions_negativeSelfExt_selfHom_overBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/RelativeDerivedHomDualProved.lean#L257).

> **Stacks 0DLD.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is proper,
> flat and of finite presentation, and let `E ∈ D(𝒪_X)`. Assume that `E` is `Y`-perfect
> (Stacks 0DKN) and that `Ext^i_{𝒪_{X_y}}(E_y, E_y) = 0` for `i < 0` at every point
> `y : Spec(k) ⟶ Y` with values in a field, `E_y` the derived pullback to the fibre `X_y`. Then
> * (a) both conditions hold for `X_V ⟶ V` and `E_V` after every base change `V ⟶ Y`;
> * (b) `Ext^i_{𝒪_{X_V}}(E_V, E_V) = 0` for `i < 0` and every algebraic space `V` over `Y`;
> * (c) `V ↦ Hom_{𝒪_{X_V}}(E_V, E_V)` is representable by an algebraic space affine and of finite
>   presentation over `Y`.
> Here `X_V` is the base change of `X` and `E_V` the derived pullback of `E` to `X_V`.

```lean
theorem conditions_negativeSelfExt_selfHom_overBaseChange (E : derivedModules B S hS D.X)
    (h1 : IsPerfectRelativeToCanonical B S hS D.f D.flat D.finitePresentation.1 E)
    (h2 : HasNoNegativeFieldFibreExt D.f E) :
    (∀ V : Over D.Y,
      IsPerfectRelativeToCanonical B S hS (overInclusion D.f V) (D.overInclusion_isFlat V)
          (D.overInclusion_isLocallyOfFinitePresentation V)
          (((smallEtaleDerivedPullbackData B S hS).pull (overProjection D.f V)).obj E) ∧
        HasNoNegativeFieldFibreExt (overInclusion D.f V)
          (((smallEtaleDerivedPullbackData B S hS).pull (overProjection D.f V)).obj E)) ∧
      (∀ (V : Over D.Y) (i : ℤ), i < 0 →
        Subsingleton
          (((smallEtaleDerivedPullbackData B S hS).pull (overProjection D.f V)).obj E ⟶
            (((smallEtaleDerivedPullbackData B S hS).pull (overProjection D.f V)).obj E)⟦i⟧)) ∧
      IsAffineFinitePresentationAlgebraicSpaceOver D.Y (relativeDerivedHom D.f E E)
```

## Tag 0DLE, a situation

[Tag 0DLE](https://stacks.math.columbia.edu/tag/0DLE) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L318). The attribute's comment: “the standing situation: a proper, flat, finitely presented morphism of algebraic spaces”.

> **Stacks 0DLE, the standing data.**  A morphism `f : X ⟶ Y` of algebraic spaces over `S`
> which is proper, flat and of finite presentation: the relative algebraic space whose relatively
> perfect complexes the category `Complexes_{X/Y}` classifies.
>
> It is the standing datum `AlgebraicGeometry.Space.CoherentSituation` of Stacks 08KB, which
> assumes only finite presentation, together with the two further hypotheses of Stacks 0DLE.

```lean
structure ComplexesSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    extends CoherentSituation B S hS
```

**`AlgebraicGeometry.Space.ComplexesObject`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L522). The attribute's comment: “objects”.

> **Stacks 0DLE, the objects.**  An object of `Complexes_{X/Y}`: a scheme `T` of the site over
> `Y` together with an object of `D(𝒪_{X_T})` satisfying conditions (1) and (2) of Stacks
> 0DLD.

```lean
structure ComplexesObject (D : ComplexesSituation B S hS)
```

**`AlgebraicGeometry.Space.ComplexesHom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 536](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L536). The attribute's comment: “morphisms”.

> **Stacks 0DLE, the morphisms.**  A morphism of `Complexes_{X/Y}`: a morphism `h : T ⟶ T'` of
> test schemes over `Y` together with an isomorphism `L(X_h)^*E' ⟶ E` of `D(𝒪_{X_T})`.

```lean
structure ComplexesHom {D : ComplexesSituation B S hS} (A A' : ComplexesObject D)
```

**`AlgebraicGeometry.Space.ComplexesSituation.complexesCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 684](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L684). The attribute's comment: “the category structure on the objects: the hom-sets are the pairs (h, φ), with the identity and the composition the tag designates”.

> **The category `Complexes_{X/Y}` of Stacks 0DLE.**  The category structure on the objects
> whose hom-sets are `AlgebraicGeometry.Space.ComplexesHom`, whose identity is
> `AlgebraicGeometry.Space.ComplexesHom.id` and whose composition is
> `AlgebraicGeometry.Space.ComplexesHom.comp`.

```lean
def complexesCategory : Category.{u + 1} (ComplexesObject D)
```

**`AlgebraicGeometry.Space.ComplexesSituation.complexesProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 695](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L695). The attribute's comment: “the functor (T, g, E) ↦ (T, g) to the test schemes over the base”.

> **The projection of `Complexes_{X/Y}` to the test schemes over `Y` of Stacks 0DLE**,
> `(T, g, E) ↦ (T, g)`: it forgets the complex and keeps the base map of a morphism.

```lean
def complexesProjection :
    letI : Category.{u + 1} (ComplexesObject D) := complexesCategory D
    ComplexesObject D ⥤ SchemesOver D.Y
```

**`AlgebraicGeometry.Space.ComplexesSituation.complexesFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 734](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L734). The attribute's comment: “the functor p : Complexes\_\{X/B} ⥤ (Sch/S)\_fppf, (T, g, E) ↦ T”.

> **The functor `p : Complexes_{X/Y} ⥤ (Sch/S)_fppf` of Stacks 0DLE**, `(T, g, E) ↦ T`: the
> projection to the test schemes over `Y` followed by forgetting the morphism to `Y`.

```lean
def complexesFunctor :
    letI : Category.{u + 1} (ComplexesObject D) := complexesCategory D
    ComplexesObject D ⥤ BigFppfOver B S hS
```

**`AlgebraicGeometry.Space.ComplexesSituation.isGroupoid_fiber_complexesFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 802](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L802). The attribute's comment: “the fibre categories of p over the schemes T are groupoids”.

> **The fibre categories of `p : Complexes_{X/Y} ⥤ (Sch/S)_fppf` are groupoids**, as Stacks
> 0DLE asserts.

```lean
theorem isGroupoid_fiber_complexesFunctor (T : BigFppfOver B S hS) :
    IsGroupoid ((complexesFunctor D).Fiber T)
```

**`AlgebraicGeometry.Space.ComplexesSituation.complexesCategory_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean, line 838](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStack.lean#L838). The attribute's comment: “the whole statement: the category Complexes\_\{X/B} of the triples (T, g, E) and the pairs (h, φ), with the designated identity and composition, the functor p : (T, g, E) ↦ T to (Sch/S)\_fppf, and its fibre categories being groupoids”.

> **Stacks 0DLE in full.**  `Complexes_{X/Y}` is a category whose objects are the triples
> `(T, g, E)` of `AlgebraicGeometry.Space.ComplexesObject` — a scheme `T` over `S`, a morphism
> `g : T ⟶ Y` and an object `E` of `D(𝒪_{X_T})` satisfying conditions (1) and (2) of Stacks
> 0DLD — and whose morphisms are the pairs `(h, φ)` of `AlgebraicGeometry.Space.ComplexesHom`,
> with the identity and the composition the tag designates; the rule `(T, g, E) ↦ T` is a functor
> `p` to `(Sch/S)_fppf`, and its fibre categories are groupoids.
>
> The conjuncts are: the hom-sets, the identity, the composition, the two clauses saying that `p`
> is the designated rule, and that the fibre categories of `p` are groupoids.  That the objects
> and the morphisms are the designated data is the definition of
> `AlgebraicGeometry.Space.ComplexesObject` and `AlgebraicGeometry.Space.ComplexesHom`, and that
> the category laws hold is `AlgebraicGeometry.Space.ComplexesSituation.complexesCategory`, whose
> existence is asserted by the statement being about it.

```lean
theorem complexesCategory_spec :
    letI : Category.{u + 1} (ComplexesObject D) := complexesCategory D
    (∀ A A' : ComplexesObject D, (A ⟶ A') = ComplexesHom A A') ∧
      (∀ A : ComplexesObject D, (𝟙 A : ComplexesHom A A) = ComplexesHom.id A) ∧
      (∀ {A A' A'' : ComplexesObject D} (m : ComplexesHom A A') (n : ComplexesHom A' A''),
        ((m ≫ n : A ⟶ A'') : ComplexesHom A A'') = ComplexesHom.comp m n) ∧
      (∀ A : ComplexesObject D, (complexesFunctor D).obj A = A.T.left) ∧
      (∀ {A A' : ComplexesObject D} (m : ComplexesHom A A'),
        (complexesFunctor D).map (m : A ⟶ A') = m.base.left) ∧
      ∀ T : BigFppfOver B S hS, IsGroupoid ((complexesFunctor D).Fiber T)
```

## Tag 0DLF, a lemma

[Tag 0DLF](https://stacks.math.columbia.edu/tag/0DLF) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.complexesFunctor_isFiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackBaseChange.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackBaseChange.lean#L264). The attribute's comment: “the functor p : Complexes\_\{X/B} ⥤ (Sch/S)\_fppf, (T, g, E) ↦ T, is fibred in groupoids”.

> **Stacks 0DLF.**  In Situation 0DLE the functor `p : Complexes_{X/B} ⥤ (Sch/S)_fppf`,
> `(T, g, E) ↦ T`, is fibred in groupoids: every morphism `h : T ⟶ T'` of schemes over `S` lifts
> at every object `(T', g', E')`, to `(T, g' ∘ h, L(h')^*E') ⟶ (T', g', E')` with the identity as
> comparison of complexes, and fill-ins exist and are unique.
>
> The lift is an object because both conditions of Stacks 0DLD survive pullback
> (`AlgebraicGeometry.Space.ComplexesSituation.relativelyPerfectBaseChange` and
> `AlgebraicGeometry.Space.ComplexesSituation.hasNoNegativeFibreExt_pull`); the fill-in is
> `AlgebraicGeometry.Space.ComplexesSituation.fillIn`.

```lean
theorem complexesFunctor_isFiberedInGroupoids :
    letI : Category.{u + 1} (ComplexesObject D) := complexesCategory D
    (complexesFunctor D).IsFiberedInGroupoids
```

## Tag 0DLG, a lemma

[Tag 0DLG](https://stacks.math.columbia.edu/tag/0DLG) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.complexes_hasRepresentableDiagonal_proved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackProved.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackProved.lean#L64).

> **Stacks 0DLG.** In Situation 0DLE (`f : X ⟶ Y` proper, flat and of finite presentation),
> the diagonal `Δ : 𝒳 ⟶ 𝒳 × 𝒳` of `𝒳 = Complexes_{X/Y}` is representable by algebraic spaces:
> `AlgebraicGeometry.Space.ComplexesSituation.complexes_hasRepresentableDiagonal` with Stacks 0DLC,
> parts (1) and (3), discharged.

```lean
theorem complexes_hasRepresentableDiagonal_proved :
    Stack.HasRepresentableDiagonal B S hS
      (CatFiberedInGroupoids.mk (complexesBasedCategory D)
        (complexesFunctor_isFiberedInGroupoids D))
```

## Tag 0DLH, a lemma

[Tag 0DLH](https://stacks.math.columbia.edu/tag/0DLH) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.complexesFunctor_isStackInGroupoids_proved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackCechDescentProved.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackCechDescentProved.lean#L74).

> In a `Complexes` situation `D` over `S`, the category `Complexes_{X/Y}` fibred in groupoids
> over `(Sch/S)_fppf` is a stack in groupoids.

```lean
theorem complexesFunctor_isStackInGroupoids_proved {S : Scheme.{u}} {hS : B.Contains S}
    (D : ComplexesSituation B S hS) :
    (complexesFunctor D).IsStackInGroupoids.{u + 1} (BigFppfOver.topology B S hS)
```

## Tag 0DLI, a remark

[Tag 0DLI](https://stacks.math.columbia.edu/tag/0DLI) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.complexesToBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackBaseChangeSquare.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackBaseChangeSquare.lean#L176). The attribute's comment: “the 1-morphism Complexes\_\{X/B} → 𝒮\_B, (T, g, E) ↦ (T, g)”.

> **The projection to the base.**  The rule `(T, g, E) ↦ (T, g)` which forgets the complex is
> a 1-morphism `Complexes_{X/B} ⟶ 𝒮_B` of categories over the big fppf site of `S`.

```lean
def complexesToBase (D : ComplexesSituation B S hS) :
    complexesBasedCategory D ⥤ᵇ baseBasedCategory D.Y
```

**`AlgebraicGeometry.Space.ComplexesSituation.baseChangeSquare_isTwoFibreProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackBaseChangeSquare.lean, line 630](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackBaseChangeSquare.lean#L630). The attribute's comment: “the square Complexes\_\{X'/B'} → Complexes\_\{X/B} over 𝒮\_\{B'} → 𝒮\_B is a 2-fibre product”.

> **The square
>
> `Complexes_{X'/B'} ⟶ Complexes_{X/B}`, `𝒮_{B'} ⟶ 𝒮_B`
>
> is a 2-fibre product.**  That is, `Complexes_{X'/B'}`, with the base-change functor and the
> projection which forgets the complex, is a 2-fibre product of the projection
> `Complexes_{X/B} ⟶ 𝒮_B` with the morphism `𝒮_{B'} ⟶ 𝒮_B` induced by `g : B' ⟶ B`.

```lean
def baseChangeSquare_isTwoFibreProduct (g : Y' ⟶ D.Y) :
    Bicategory.IsTwoFibreProduct (D.baseChangeSquare g)
```

## Tag 0DLJ, a lemma

[Tag 0DLJ](https://stacks.math.columbia.edu/tag/0DLJ) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.isLimitPreserving_complexes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackProved.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackProved.lean#L88).

> **Stacks 0DLJ.** In Situation 0DLE assume that `Y ⟶ S` is locally of finite presentation.
> Then `p : Complexes_{X/Y} ⥤ (Sch/S)_fppf` is limit preserving (Stacks 07XL):
> `AlgebraicGeometry.Space.ComplexesSituation.isLimitPreserving_of_existsNegativeExtLocus` with
> Stacks 0DKW and Stacks 0DLC (1) discharged.

```lean
theorem isLimitPreserving_complexes
    (hY : IsLocallyOfFinitePresentation B S hS (terminal.from D.Y.1)) :
    Deformation.Artin.IsLimitPreserving.{u, u, u, u + 1, u + 1} B S hS
      (CatFiberedInGroupoids.mk (complexesBasedCategory D)
        (complexesFunctor_isFiberedInGroupoids D))
```

## Tag 0DLK, a lemma

[Tag 0DLK](https://stacks.math.columbia.edu/tag/0DLK) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.ComplexesSituation.isEquivalence_complexesFiberSquareComparison_proved`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackPushoutsProved.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackPushoutEquivalence.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackPushoutEquivalence.lean#L23) (StacksFrontier).

## Tag 0DLL, a lemma

[Tag 0DLL](https://stacks.math.columbia.edu/tag/0DLL) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.finiteDimensional_tangentSpace_infinitesimalAutomorphisms_complexes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackTangentFiniteDimensional.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackTangentFiniteDimensional.lean#L88).

> In Situation 0DLE (`f : X ⟶ Y` proper, flat and of finite presentation, the `B` of the source
> being `Y`), assume that `S` is locally Noetherian and `Y ⟶ S` is locally of finite presentation.
> Let `k` be a field of finite type over `S`, presented as in Stacks Section 07T2 through an affine
> open `Spec Λ ⊆ S` with `Λ → k` finite, and let `x₀` be an object of `𝒳 = Complexes_{X/Y}` over
> `Spec k`. Then `𝒳` satisfies (RS), so that the predeformation category `𝓕_{𝒳,k,x₀}` is a
> deformation category and the spaces of Stacks Section 07WY are defined, and the tangent space
> `T𝓕_{𝒳,k,x₀}` (`Deformation.Artin.tangentSpaceModuleOfSatisfiesRS`) and the infinitesimal
> automorphisms `Inf(𝓕_{𝒳,k,x₀})` (`Deformation.Artin.infinitesimalAutomorphismModuleOfSatisfiesRS`,
> at every object over `k` and every choice of pushforwards) are finite dimensional over `k`.

```lean
theorem finiteDimensional_tangentSpace_infinitesimalAutomorphisms_complexes
    (D : ComplexesSituation B S hS) [_root_.AlgebraicGeometry.IsLocallyNoetherian S]
    (hY : IsLocallyOfFinitePresentation B S hS (terminal.from D.Y.obj))
    {Λ k : Type u} [CommRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    (iΛ : Spec (.of Λ) ⟶ S) (hiΛ : _root_.AlgebraicGeometry.IsOpenImmersion iΛ)
    (x₀ : ComplexesObject D)
    (hx₀ : (complexesFunctor D ⋙ Over.post B.inclusion).obj x₀ =
      Over.mk (Spec.map (CommRingCat.ofHom (algebraMap Λ k)) ≫ iΛ)) :
    SatisfiesRS B S hS (complexesFunctor D) (complexesFunctor_isFiberedInGroupoids D) ∧
      ∀ hRS : SatisfiesRS B S hS (complexesFunctor D) (complexesFunctor_isFiberedInGroupoids D),
        FiniteDimensional k (tangentSpaceModuleOfSatisfiesRS B S hS (complexesFunctor D)
            (complexesFunctor_isFiberedInGroupoids D) hRS iΛ x₀ hx₀
            (locallyOfFiniteType_specMap_comp_of_isOpenImmersion iΛ hiΛ)
            (quasiCompact_of_spec_field _)) ∧
          ∀ x P, FiniteDimensional k (infinitesimalAutomorphismModuleOfSatisfiesRS B S hS
            (complexesFunctor D) (complexesFunctor_isFiberedInGroupoids D) hRS iΛ x₀ hx₀
            (locallyOfFiniteType_specMap_comp_of_isOpenImmersion iΛ hiΛ)
            (quasiCompact_of_spec_field _) x P)
```

## Tag 0DLM, a lemma

[Tag 0DLM](https://stacks.math.columbia.edu/tag/0DLM) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.isStronglyFormallyEffective_complexes_proved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackFormalEffectivenessProved.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackFormalEffectivenessProved.lean#L51).

> `Complexes_{X/S}` is strongly formally effective: in a `ComplexesSituation` whose target `Y`
> of `f : X ⟶ Y` is terminal over `S`, with `S` locally Noetherian, the functor
> `p : Complexes_{X/S} ⟶ (Sch/S)_fppf` is strongly formally effective.

```lean
theorem isStronglyFormallyEffective_complexes_proved {S : Scheme.{u}} {hS : B.Contains S}
    (D : ComplexesSituation B S hS) [_root_.AlgebraicGeometry.IsLocallyNoetherian S]
    (hY : IsTerminal D.Y) :
    IsStronglyFormallyEffective B S hS (complexesFunctor D)
      (complexesFunctor_isFiberedInGroupoids D)
```

## Tag 0DLN, a theorem

[Tag 0DLN](https://stacks.math.columbia.edu/tag/0DLN) in the Stacks Project.

**`AlgebraicGeometry.Space.ComplexesSituation.isAlgebraicStack_complexes_proved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackAlgebraicStackProved.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/ComplexesStackAlgebraicStackProved.lean#L112).

> **Stacks 0DLN: `Complexes_{X/Y}` is an algebraic stack.** In Situation 0DLE over `S`
> (`f : X ⟶ Y` proper, flat and of finite presentation), `Complexes_{X/Y}` is an algebraic stack
> over `S`.
>
> This is
> `ComplexesSituation.isAlgebraicStack_complexes_of_cechDescent_of_derivedExistence`
> with Stacks 0DLA, Čech case, given by
> `AlgebraicGeometry.Space.ComplexesSituation.cechDescent_proved` and Stacks 0DIQ given by
> `AlgebraicGeometry.Space.ComplexesSituation.SpecLimitTower.exists_restriction_proved`.

```lean
theorem isAlgebraicStack_complexes_proved {S : Scheme.{u}} (hS : B.Contains S)
    (D : ComplexesSituation B S hS) :
    Stack.IsAlgebraicStack.{u, z, u + 1, u + 1} B S hS (complexesBasedCategory D)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 99.16, Tag 0DLB](https://stacks.math.columbia.edu/tag/0DLB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
