---
declaration: section
origin: cited
lean: Deformation.SchlessingerConditionS1, Deformation.SchlessingerConditionS2, Deformation.squareComparisonFunctor, Deformation.schlessingerConditionS1_of_smallExtensions, Deformation.schlessingerConditionS1_elements_iff, Deformation.schlessingerConditionS2_elements_iff, Deformation.schlessingerConditionS2_completion_squareZero, Deformation.schlessingerConditionS2_comparison_squareZero
statement: formalized
proof: formalized
---

# 90.10 Schlessinger's conditions

Section 90.10 of the Stacks Project, [Tag 06HV](https://stacks.math.columbia.edu/tag/06HV). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06HW, a definition

[Tag 06HW](https://stacks.math.columbia.edu/tag/06HW) in the Stacks Project.

**`Deformation.SchlessingerConditionS1`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Basic.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Basic.lean#L148). The attribute's comment: “condition (S1)”. References: SGA 7 VI (1.16), “(I)”.

> Schlessinger's condition (S1): every cospan whose second base map is
> surjective has a completion over a pullback square in `C_Λ`.

```lean
public structure SchlessingerConditionS1
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] {F : Type u₁} [Category.{v₁} F]
      (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) : Prop
```

**`Deformation.SchlessingerConditionS2`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Basic.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Basic.lean#L161). The attribute's comment: “condition (S2)”.

> Schlessinger's condition (S2): completions exist when the second map is
> the dual-number projection, and any two completions over the same base square
> admit the required fibrewise comparison morphism.

```lean
public structure SchlessingerConditionS2
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k] {F : Type u₁} [Category.{v₁} F]
      (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) : Prop
```

## Tag 06SP, an equation

[Tag 06SP](https://stacks.math.columbia.edu/tag/06SP) in the Stacks Project.

**`Deformation.squareComparisonFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Comparison.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Comparison.lean#L92).

> **Stacks Project, Tag 06SP.** For a pullback square of Artinian local
> `Λ`-algebras with `f₂` surjective, choices of pushforwards in a category
> cofibered in groupoids determine the canonical comparison functor
> `F(P) ⟶ F(A₁) ×_{F(A)} F(A₂)`.

```lean
public noncomputable def squareComparisonFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (_hp : IsCofiberedInGroupoids p)
    {P A₁ A₂ A : ArtinianLocalAlgCat.{u, v, w} Λ k}
    (p₁ : P ⟶ A₁) (p₂ : P ⟶ A₂) (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A)
    (hP : IsPullback p₁ p₂ f₁ f₂) (_hf₂ : Function.Surjective f₂.hom)
    (P₁ : PushforwardChoice p p₁) (P₂ : PushforwardChoice p p₂)
    (F₁ : PushforwardChoice p f₁) (F₂ : PushforwardChoice p f₂)
    (Qp₁ : PushforwardFunctor P₁) (Qp₂ : PushforwardFunctor P₂)
    (Qf₁ : PushforwardFunctor F₁) (Qf₂ : PushforwardFunctor F₂) :
    SquareComparisonFunctor p p₁ p₂ f₁ f₂ P₁ P₂ F₁ F₂ Qp₁ Qp₂ Qf₁ Qf₂
```

## Tag 06HX, a lemma

[Tag 06HX](https://stacks.math.columbia.edu/tag/06HX) in the Stacks Project.

**`Deformation.schlessingerConditionS1_of_smallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SmallExtensions.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SmallExtensions.lean#L288).

> The small-extension cases of the completion property suffice for
> Schlessinger's condition (S1).

```lean
theorem schlessingerConditionS1_of_smallExtensions
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : IsCofiberedInGroupoids p)
    (h : ∀ {x₁ x₂ x : F} (f₁ : x₁ ⟶ x) (f₂ : x₂ ⟶ x),
      IsSmallExtension (CommRingCat.ofHom (p.map f₂).hom.toRingHom) →
        ∀ {A₁₂ : ArtinianLocalAlgCat.{u, v, w} Λ k}
          (g₁ : A₁₂ ⟶ p.obj x₁) (g₂ : A₁₂ ⟶ p.obj x₂),
          IsPullback g₂ g₁ (p.map f₂) (p.map f₁) →
            Nonempty (PullbackCompletion p f₁ f₂ g₁ g₂)) :
    SchlessingerConditionS1 p
```

## Tag 06HY, a remark

[Tag 06HY](https://stacks.math.columbia.edu/tag/06HY) in the Stacks Project.

**`Deformation.schlessingerConditionS1_elements_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SetValuedFunctor.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SetValuedFunctor.lean#L119). The attribute's comment: “condition (S1)”.

> For the category of elements of `F : 𝒞_Λ ⥤ Type t`, Schlessinger's condition (S1) says
> that the map `F(A₁ ×_A A₂) → F(A₁) ×_{F(A)} F(A₂)` is surjective whenever `A₂ → A` is
> surjective.

```lean
theorem schlessingerConditionS1_elements_iff
    (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type t) :
    SchlessingerConditionS1 (Functor.Elements.π F) ↔
      ∀ ⦃A₁ A₂ A A₁₂ : ArtinianLocalAlgCat.{u, v, w} Λ k⦄ (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A),
        Function.Surjective f₂.hom →
          ∀ (g₁ : A₁₂ ⟶ A₁) (g₂ : A₁₂ ⟶ A₂) (hPB : IsPullback g₂ g₁ f₂ f₁),
            Function.Surjective (fibreProductComparison F g₁ g₂ f₁ f₂ hPB.w)
```

**`Deformation.schlessingerConditionS2_elements_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SetValuedFunctor.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SetValuedFunctor.lean#L140). The attribute's comment: “condition (S2)”.

> For the category of elements of `F : 𝒞_Λ ⥤ Type t`, Schlessinger's condition (S2) says
> that the map `F(A ×_k k[ε]) → F(A) ×_{F(k)} F(k[ε])` is bijective.

```lean
theorem schlessingerConditionS2_elements_iff
    (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type t) :
    SchlessingerConditionS2 (Functor.Elements.π F) ↔
      ∀ ⦃A A₀ Aε B : ArtinianLocalAlgCat.{u, v, w} Λ k⦄ (d : A ⟶ A₀) (e : Aε ⟶ A₀),
        IsDualNumberProjection e →
          ∀ (g : B ⟶ A) (gε : B ⟶ Aε) (hPB : IsPullback gε g e d),
            Function.Bijective (fibreProductComparison F g gε d e hPB.w)
```

## Tag 06HZ, a lemma

[Tag 06HZ](https://stacks.math.columbia.edu/tag/06HZ) in the Stacks Project.

**`Deformation.schlessingerConditionS2_completion_squareZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SquareZeroExtension.lean, line 1201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SquareZeroExtension.lean#L1201). The attribute's comment: “existence of completions”.

> The existence clause of (S2) extends from dual numbers to `k[V]` for
> finite-dimensional `V`.

```lean
theorem schlessingerConditionS2_completion_squareZero
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {V : Type z} [AddCommGroup V] [Module k V] [FiniteDimensional k V]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p) (hS2 : SchlessingerConditionS2 p)
    {x xV x₀ : F} (d : x ⟶ x₀) (e : xV ⟶ x₀)
    (he : IsSquareZeroProjection (V := V) (p.map e))
    {AV : ArtinianLocalAlgCat.{u, v, w} Λ k}
    (g : AV ⟶ p.obj x) (gV : AV ⟶ p.obj xV)
    (hpb : IsPullback gV g (p.map e) (p.map d)) :
    Nonempty (PullbackCompletion p d e g gV)
```

**`Deformation.schlessingerConditionS2_comparison_squareZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SquareZeroExtension.lean, line 1218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SquareZeroExtension.lean#L1218). The attribute's comment: “comparison of completions”.

> The comparison clause of (S2) extends from dual numbers to `k[V]` for
> finite-dimensional `V`.

```lean
theorem schlessingerConditionS2_comparison_squareZero
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {V : Type z} [AddCommGroup V] [Module k V] [FiniteDimensional k V]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p) (hS2 : SchlessingerConditionS2 p)
    {x xV x₀ : F} (d : x ⟶ x₀) (e : xV ⟶ x₀)
    (he : IsSquareZeroProjection (V := V) (p.map e))
    {AV : ArtinianLocalAlgCat.{u, v, w} Λ k}
    (g : AV ⟶ p.obj x) (gV : AV ⟶ p.obj xV)
    (hpb : IsPullback gV g (p.map e) (p.map d))
    (P Q : PullbackCompletion p d e g gV) :
    ∃ b : P.apex ⟶ Q.apex,
      (P.toFirst = b ≫ Q.toFirst) ∧
        (p.map b = eqToHom P.apex_eq ≫ eqToHom Q.apex_eq.symm)
```

## Tag 06I0, a lemma

[Tag 06I0](https://stacks.math.columbia.edu/tag/06I0) in the Stacks Project.

**`Deformation.schlessingerConditionS2_of_isIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/AssociatedFunctor.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/AssociatedFunctor.lean#L450). The attribute's comment: “s2_associated_functor”.

> The associated functor of isomorphism classes of a category cofibered in
> groupoids inherits (S2) if the special fibre is a setoid or automorphisms
> over the residue field lift along dual-number projections. In particular this
> holds for a predeformation category.

```lean
public theorem schlessingerConditionS2_of_isIsomorphismClasses
    (𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, max v w, w} Λ k))
    (h𝓕 : IsCofiberedInGroupoids 𝓕.p)
    (hS2 : SchlessingerConditionS2 𝓕.p)
    (hSpecial :
      (IsPredeformationCategory 𝓕.p) ∨
      (IsSetoidCategory (𝓕.p.Fiber (residueFieldObject Λ k))) ∨
      (∀ {xε x₀ : 𝓕.obj} (e : xε ⟶ x₀),
        IsDualNumberProjection (𝓕.p.map e) →
        ∀ a : x₀ ≅ x₀, 𝓕.p.map a.hom = 𝟙 (𝓕.p.obj x₀) →
          ∃ b : xε ≅ xε,
            (𝓕.p.map b.hom = 𝟙 (𝓕.p.obj xε)) ∧
              (b.hom ≫ e = e ≫ a.hom))) :
    SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓕 h𝓕))
```

**`Deformation.schlessingerConditionS1_of_isIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Basic.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Basic.lean#L354). The attribute's comment: “s1_associated_functor”. References: SGA 7 VI (1.13), “partial”.

> The associated functor of isomorphism classes of a category cofibered in
> groupoids inherits Schlessinger's condition (S1).

```lean
public theorem schlessingerConditionS1_of_isIsomorphismClasses
    {𝓕 : BasedCategory.{v₁, u₁} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    {𝓖 : BasedCategory.{v₂, u₂} (ArtinianLocalAlgCat.{u, v, w} Λ k)}
    (φ : BasedFunctor 𝓕 𝓖)
    (hφ : IsIsomorphismClasses φ)
    (hS1 : SchlessingerConditionS1 𝓕.p) :
    SchlessingerConditionS1 𝓖.p
```

## Tag 06SQ, a lemma

[Tag 06SQ](https://stacks.math.columbia.edu/tag/06SQ) in the Stacks Project.

**`Deformation.schlessingerConditionS1_objectsOverFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Basic.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Basic.lean#L288). The attribute's comment: “condition (S1)”.

> Condition (S1) passes to the category of objects over a fixed object.

```lean
public theorem schlessingerConditionS1_objectsOverFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (x : F)
    (hS1 : SchlessingerConditionS1 p) :
    SchlessingerConditionS1
      (objectsOverFunctor p x)
```

**`Deformation.schlessingerConditionS2_objectsOverFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Basic.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Basic.lean#L304). The attribute's comment: “condition (S2)”.

> Condition (S2) passes to the category of objects over a fixed object.

```lean
public theorem schlessingerConditionS2_objectsOverFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (x : F)
    (hS2 : SchlessingerConditionS2 p) :
    SchlessingerConditionS2
      (objectsOverFunctor p x)
```

**`Deformation.schlessingerConditionS2_isomorphismClasses_objectsOverFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/TangentSpace/PredeformationLinear.lean#L69). The attribute's comment: “condition (S2) for the associated functor of a slice”.

> **Stacks Project, Tag 06SQ.** Schlessinger's condition (S2) passes from a category
> cofibered in groupoids to the associated functor of isomorphism classes of its slice
> predeformation category at a point over the residue field.

```lean
theorem schlessingerConditionS2_isomorphismClasses_objectsOverFunctor
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (hS2 : SchlessingerConditionS2 p)
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses
        (BasedCategory.ofFunctor (objectsOverFunctor p x.1))
        (isPredeformationCategory_objectsOverFunctor p hp x).cofibered))
```

## Tag 06IS, a lemma

[Tag 06IS](https://stacks.math.columbia.edu/tag/06IS) in the Stacks Project.

**`Deformation.exists_section_iff_exists_dualNumberLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Schlessinger/Basic.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Schlessinger/Basic.lean#L190).

> **Stacks Project, Tag 06IS.** In a square over the pullback of an
> Artinian local algebra and the dual numbers over the residue field, a section
> of the first projection exists precisely when the bottom arrow lifts across
> the dual-number projection.

```lean
public theorem exists_section_iff_exists_dualNumberLift
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k)
    (hp : IsCofiberedInGroupoids p)
    (hS2 : SchlessingerConditionS2 p)
    {y xε x x₀ : F} (b : y ⟶ xε) (a : y ⟶ x)
    (e : xε ⟶ x₀) (d : x ⟶ x₀)
    (hcomm : b ≫ e = a ≫ d)
    (hdual : IsDualNumberProjection (p.map e))
    (hPB : IsPullback (p.map b) (p.map a) (p.map e) (p.map d)) :
    (∃ s : x ⟶ y, s ≫ a = 𝟙 x) ↔
      (∃ sε : x ⟶ xε, sε ≫ e = d)
```

## Tag 06IT, a lemma

[Tag 06IT](https://stacks.math.columbia.edu/tag/06IT) in the Stacks Project.

**`Deformation.exists_lift_of_pushforward_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/SchlessingerConditions/SmallExtensionLift.lean, line 1035](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/SchlessingerConditions/SmallExtensionLift.lean#L1035). References: SGA 7 VI (1.5), “(2)”.

> A map from `x₁` to the pushforward of `y` along the canonical
> infinitesimal-coordinate map produces a lift `x₁ → x₂`.

```lean
theorem exists_lift_of_pushforward_map
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : IsPredeformationCategory p)
    (hS2 : SchlessingerConditionS2 p)
    {y x₁ x₂ x z : F}
    (a : y ⟶ x₁) (c : y ⟶ x₂) (a₁ : x₁ ⟶ x) (a₂ : x₂ ⟶ x)
    (hcomm : c ≫ a₂ = a ≫ a₁)
    (hPB : IsPullback (p.map c) (p.map a) (p.map a₂) (p.map a₁))
    (hsmall : InfinitesimalLifting.IsSmallExtension
      (CommRingCat.ofHom (p.map a₂).hom.toRingHom))
    (h : p.obj x₁ ⟶ p.obj x₂)
    (hh : h ≫ p.map a₂ = p.map a₁)
    (target_eq : p.obj z =
      (infinitesimalMap (p.map a₁) (p.map a₂) hsmall h hh
        (p.map a) (p.map c) hPB).target)
    (q : y ⟶ z)
    (hqmap : p.map q =
      (infinitesimalMap (p.map a₁) (p.map a₂) hsmall h hh
        (p.map a) (p.map c) hPB).g ≫ eqToHom target_eq.symm)
    (_hq : p.IsCocartesian (p.map q) q)
    (lift : x₁ ⟶ z) :
    ∃ b : x₁ ⟶ x₂, b ≫ a₂ = a₁
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.10, Tag 06HV](https://stacks.math.columbia.edu/tag/06HV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
