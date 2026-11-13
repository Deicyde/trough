---
declaration: section
origin: cited
lean: IsSetoidCategory, CategoryTheory.Functor.IsFiberedInSetoids, CategoryTheory.Functor.isFiberedInSetoids_iff, CategoryTheory.CatFiberedInSetoids, CategoryTheory.TwoFibreProd.proj_isFiberedInSetoids, CategoryTheory.BasedCategory.Equivalence.isFiberedInSetoids_of_isFiberedInSets, CategoryTheory.BasedCategory.Equivalence.fiberMap_identifiesIsoClasses, CategoryTheory.Functor.isFiberedInSets_isoClassElementsProj
statement: formalized
proof: formalized
---

# 4.39 Categories fibred in setoids

Section 4.39 of the Stacks Project, [Tag 04S9](https://stacks.math.columbia.edu/tag/04S9). 8 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02XZ, a definition

[Tag 02XZ](https://stacks.math.columbia.edu/tag/02XZ) in the Stacks Project.

**`IsSetoidCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/Setoid.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/Setoid.lean#L54). References: SGA 4 I (6.5.1), “discrete category def”.

> **Stacks 02XZ.** A category `C` is a *setoid* when every morphism of `C` is an
> isomorphism and every endomorphism `f : X ⟶ X` is `𝟙 X`; equivalently `C` is a thin groupoid,
> so a setoid is a set together with an equivalence relation on it.

```lean
def IsSetoidCategory (C : Type*) [Category C] : Prop
```

## Tag 04SA, a definition

[Tag 04SA](https://stacks.math.columbia.edu/tag/04SA) in the Stacks Project.

**`CategoryTheory.Functor.IsFiberedInSetoids`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/Defs.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/Defs.lean#L49).

> **Stacks 04SA.** A functor `p : 𝒳 ⥤ 𝒮` is a *category fibred in setoids* if it is
> fibred in groupoids and each fibre category `p.Fiber S` is a setoid, i.e. thin (its fibres
> are groupoids automatically, by Stacks `003V`).

```lean
class IsFiberedInSetoids (p : 𝒳 ⥤ 𝒮) : Prop
```

**`CategoryTheory.Functor.isFiberedInSetoids_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/SetoidFibers.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/SetoidFibers.lean#L38). The attribute's comment: “Stacks' definition verbatim: fibred in groupoids, and every fibre category is a setoid (`IsSetoidCategory`, Stacks 02XZ).”.

> **Stacks 04SA.** A functor `p : 𝒳 ⥤ 𝒮` is fibred in setoids if and only if it is fibred in
> groupoids (Stacks `003T`) and every fibre category `p.Fiber S` is a setoid in the sense of Stacks
> `02XZ`: a groupoid in which every object has exactly one automorphism, the identity.

```lean
theorem isFiberedInSetoids_iff (p : 𝒳 ⥤ 𝒮) :
    p.IsFiberedInSetoids ↔
      p.IsFiberedInGroupoids ∧ ∀ S : 𝒮, IsSetoidCategory (p.Fiber S)
```

## Tag 02Y1, a definition

[Tag 02Y1](https://stacks.math.columbia.edu/tag/02Y1) in the Stacks Project.

**`CategoryTheory.CatFiberedInSetoids`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/TwoCategory.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/TwoCategory.lean#L41).

> The 2-category of categories fibred in setoids over `𝒞`: the full sub-2-category of the
> 2-category `BasedCategory 𝒞` of categories over `𝒞` spanned by the categories fibred in setoids.
> Explicitly:
>
> 1. its objects are the categories `p : 𝒮 ⥤ 𝒞` over `𝒞` that are fibred in setoids;
> 2. its 1-morphisms `(𝒮, p) ⟶ (𝒮', p')` are the functors `G : 𝒮 ⥤ 𝒮'` with `p' ∘ G = p`;
> 3. its 2-morphisms `t : G ⟶ H` are the morphisms of functors with `p'(t_x) = 𝟙 (p x)` for every
>    object `x` of `𝒮`.

```lean
abbrev CatFiberedInSetoids (𝒞 : Type u₁) [Category.{v₁} 𝒞]
```

## Tag 04SB, a lemma

[Tag 04SB](https://stacks.math.columbia.edu/tag/04SB) in the Stacks Project.

**`CategoryTheory.TwoFibreProd.proj_isFiberedInSetoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/TwoFibreProduct.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/TwoFibreProduct.lean#L334).

> **The 2-fibre product of categories fibred in setoids.** If `𝒳`, `𝒴`, `𝒮` are fibred in
> setoids over `𝒞` and
> `F : 𝒳 ⥤ 𝒮`, `G : 𝒴 ⥤ 𝒮` are 1-morphisms over `𝒞`, then the 2-fibre product `𝒳 ×_𝒮 𝒴`
> over `𝒞`, with its structure functor, is again fibred in setoids over `𝒞`.

```lean
theorem TwoFibreProd.proj_isFiberedInSetoids
    (hX : pX.IsFiberedInSetoids) (hY : pY.IsFiberedInSetoids) (hS : pS.IsFiberedInSetoids)
    (hF : F ⋙ pS = pX) (hG : G ⋙ pS = pY) :
    (TwoFibreProd.proj pX pY pS F G).IsFiberedInSetoids
```

## Tag 0045, a lemma

[Tag 0045](https://stacks.math.columbia.edu/tag/0045) in the Stacks Project.

**`CategoryTheory.BasedCategory.Equivalence.isFiberedInSetoids_of_isFiberedInSets`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean#L115). The attribute's comment: “(1)(a)”. References: SGA 4 I (6.5.1), “more general”.

> **Stacks 0045 (1)(a).** Let `𝒞` be a category and let `𝒳` be a category over `𝒞`. If `𝒳` is
> equivalent over `𝒞` to a category `𝒴` fibred in sets over `𝒞`, then `𝒳` is fibred in setoids
> over `𝒞`.
>
> Both fibre conditions are transported backwards along the equivalence: a category fibred in sets
> is fibred in groupoids with discrete, hence thin, fibres (Stacks 0043), and being fibred in
> groupoids and having thin fibres each transport.

```lean
theorem isFiberedInSetoids_of_isFiberedInSets (e : BasedCategory.Equivalence 𝒳 𝒴)
    (h : 𝒴.p.IsFiberedInSets) : 𝒳.p.IsFiberedInSetoids
```

**`CategoryTheory.BasedCategory.Equivalence.fiberMap_identifiesIsoClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean#L132). The attribute's comment: “(1)(b)”.

> **Stacks 0045 (1)(b).** Let `𝒞` be a category, let `𝒳` be a category over `𝒞` and let `e` be
> an equivalence over `𝒞` from `𝒳` to a category `𝒴` fibred in sets over `𝒞`. For every object `U`
> of `𝒞` the induced map `Ob(𝒳_U) → Ob(𝒴_U)` on the objects of the fibres identifies its target
> with the set of isomorphism classes of its source: it is surjective, and two objects of `𝒳_U`
> have the same image exactly when they are isomorphic in `𝒳_U`.
>
> The same content packaged as a bijection `Ob(𝒳_U)/≅ ≃ Ob(𝒴_U)` is
> `CategoryTheory.BasedCategory.Equivalence.fiberQuotientEquiv`; as there, the two categories over
> `𝒞` are taken in one pair of universes.

```lean
theorem fiberMap_identifiesIsoClasses {𝒳 𝒴 : BasedCategory.{v₂, u₂} 𝒞}
    (e : BasedCategory.Equivalence 𝒳 𝒴)
    (h : 𝒴.p.IsFiberedInSets) (U : 𝒞) :
    Function.Surjective (e.fiberMap (U := U)) ∧
      ∀ x y : 𝒳.p.Fiber U, e.fiberMap x = e.fiberMap y ↔ IsIsomorphic x y
```

**`CategoryTheory.Functor.isFiberedInSets_isoClassElementsProj`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean#L264). The attribute's comment: “(2), the category fibred in sets”.

> **Stacks 0045 (2)**, the category produced is fibred in sets. The lift of `f : V ⟶ U` at
> `(U, ξ)` is `(V, f^*ξ)`, with the restriction map of the presheaf of isomorphism classes as the
> morphism, and it is the only one: a lift of `f` with target `(U, ξ)` has its underlying morphism
> of `𝒞` forced to be `f`, and then the class at its source is forced to be `f^*ξ`.

```lean
instance isFiberedInSets_isoClassElementsProj (p : 𝒮 ⥤ 𝒞) [p.IsFibered] :
    (isoClassElementsProj p).IsFiberedInSets
```

**`CategoryTheory.Functor.basedEquivalenceIsoClassElements`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean, line 428](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/EquivalentFiberedInSets.lean#L428). The attribute's comment: “(2), the equivalence over the base”.

> **Stacks 0045 (2)**, the equivalence. Let `𝒞` be a category and let `p : 𝒮 ⥤ 𝒞` be a category
> fibred in setoids. Then `can : 𝒮 ⥤ 𝒮'` is an equivalence over `𝒞` onto the category of elements
> of the presheaf of isomorphism classes, which is fibred in sets by
> `CategoryTheory.Functor.isFiberedInSets_isoClassElementsProj`.

```lean
noncomputable def basedEquivalenceIsoClassElements (p : 𝒮 ⥤ 𝒞) [p.IsFiberedInSetoids] :
    BasedCategory.Equivalence (BasedCategory.ofFunctor p)
      (BasedCategory.ofFunctor (isoClassElementsProj p))
```

## Tag 04SC, a lemma

[Tag 04SC](https://stacks.math.columbia.edu/tag/04SC) in the Stacks Project.

**`CategoryTheory.Functor.existsUnique_twoIso_of_isoClassMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean#L360). The attribute's comment: “(1): a unique 2-isomorphism between two 1-morphisms with the same image under F.”.

> **Stacks 04SC (1).** For two 1-morphisms `f, g : 𝒮₁ ⟶ 𝒮₂` of categories fibred in setoids
> over `𝒞` with `F(f) = F(g)`, that is inducing the same map on the presheaves of isomorphism
> classes of objects, there is a unique 2-isomorphism `f ⟶ g`.

```lean
theorem existsUnique_twoIso_of_isoClassMap_eq {G H : 𝒮 ⥤ 𝒯} (hG : G ⋙ q = p) (hH : H ⋙ q = p)
    (h : isoClassMapOfCompEq hG = isoClassMapOfCompEq hH) :
    ∃! e : G ≅ H, ∀ x : 𝒮, q.IsHomLift (𝟙 (p.obj x)) (e.hom.app x)
```

**`CategoryTheory.Functor.exists_oneMorphism_isoClassMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean#L476). The attribute's comment: “(2): every map of the associated presheaves comes from a 1-morphism.”.

> **Stacks 04SC (2).** Every morphism `h : F(𝒮₁) ⟶ F(𝒮₂)` of presheaves of isomorphism classes
> is `F(f)` for a 1-morphism `f : 𝒮₁ ⟶ 𝒮₂` of categories fibred in setoids over `𝒞`.

```lean
theorem exists_oneMorphism_isoClassMap_eq :
    ∃ (G : 𝒮 ⥤ 𝒯) (hG : G ⋙ q = p), isoClassMapOfCompEq hG = φ
```

**`CategoryTheory.Functor.isoClassMapEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean, line 526](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean#L526). The attribute's comment: “The bijection `Mor(𝒮₁, 𝒮₂)/2-isomorphism = Mor_{PSh}(F₁, F₂)`.”.

> **Stacks 04SC**, final form: for categories `𝒮₁`, `𝒮₂` fibred in setoids over `𝒞`,
> `Mor_{Cat/𝒞}(𝒮₁, 𝒮₂)` modulo 2-isomorphism is `Mor_{PSh(𝒞)}(F₁, F₂)`, where `F_i(U)` is the set of
> isomorphism classes of objects of the fibre of `𝒮_i` over `U`. The forward map sends a 1-morphism
> to the induced map of presheaves; it is surjective by Stacks 04SC (2) and injective by
> Stacks 04SC (1).

```lean
noncomputable def isoClassMapEquiv :
    _root_.Quotient (twoIsoSetoid p q) ≃ (p.isoClassPresheaf ⟶ q.isoClassPresheaf)
```

**`CategoryTheory.Functor.fiberPresheafIsoIsoClassPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean#L584). The attribute's comment: “(3): for a category fibred in sets the presheaf of isomorphism classes of the fibres is the presheaf of objects of the fibres, i.e. `𝒮 = F(𝒮)`.”.

> **Stacks 04SC (3).** A category fibred in sets `𝒮` is equal to `F(𝒮)`: the presheaf of
> isomorphism classes of the fibres of `𝒮` is the presheaf `U ↦ Ob(𝒮_U)` of objects of the fibres,
> which is the presheaf that Stacks 02Y2 attaches to `𝒮`. The isomorphism is the quotient map at
> each `U`, a bijection because the fibres are discrete, and it is natural because on both sides the
> restriction along `f : V ⟶ U` is `x ↦ f^* x`.

```lean
noncomputable def fiberPresheafIsoIsoClassPresheaf (hd : ∀ U : 𝒞, IsDiscrete (p.Fiber U)) :
    p.fiberPresheaf hd ≅ p.isoClassPresheaf
```

## Tag 042J, a lemma

[Tag 042J](https://stacks.math.columbia.edu/tag/042J) in the Stacks Project.

**`isFiberedInSetoids_iff_π_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInSetoids/Inertia.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedInSetoids/Inertia.lean#L31).

> **Stacks 042J.** A category fibred in groupoids `p : 𝒮 ⥤ 𝒞` is fibred in setoids if and
> only if the forgetful 1-morphism `π : I_𝒮 ⥤ 𝒮` of the absolute inertia is an equivalence.
> Since `π` is always faithful and essentially surjective, the content is that `π` is full
> exactly when the fibres of `p` are thin.

```lean
theorem isFiberedInSetoids_iff_π_isEquivalence (p : 𝒮 ⥤ 𝒞) (hp : p.IsFiberedInGroupoids) :
    p.IsFiberedInSetoids ↔ (RelativeInertia.π p : AbsoluteInertia p ⥤ 𝒮).IsEquivalence
```

## Tag 04SD, a lemma

[Tag 04SD](https://stacks.math.columbia.edu/tag/04SD) in the Stacks Project.

**`CategoryTheory.Functor.twoFibreProductIsoClassEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean, line 837](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean#L837).

> **Stacks 04SD.** The presheaf attached by Stacks 04SC to a 2-fibre product `𝒳 ×_𝒵 𝒴` over `𝒞`
> is the fibre product of the presheaves attached to `𝒳`, `𝒴` and `𝒵`: at every object `U` of `𝒞`,
> `Ob((𝒳 ×_𝒵 𝒴)_U)/≅ = Ob(𝒳_U)/≅ ×_{Ob(𝒵_U)/≅} Ob(𝒴_U)/≅`, by the bijection sending the class of
> an object to the pair of the classes of its components. This is the display to which the source's
> proof reduces the lemma.

```lean
noncomputable def twoFibreProductIsoClassEquiv (U : 𝒞) :
    _root_.Quotient
        (isIsomorphicSetoid
          ((TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒵 F G).Fiber U)) ≃
      {ab : _root_.Quotient (isIsomorphicSetoid (p𝒳.Fiber U)) ×
            _root_.Quotient (isIsomorphicSetoid (p𝒴.Fiber U)) //
          (isoClassMap hF).app (op U) ab.1 = (isoClassMap hG).app (op U) ab.2}
```

**`CategoryTheory.Functor.twoFibreProductIsoClassMap_naturality`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean, line 852](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/FiberedInSetoids.lean#L852). The attribute's comment: “Naturality: the bijection is an isomorphism of presheaves.”.

> **Stacks 04SD**, naturality: the bijection of
> `CategoryTheory.Functor.twoFibreProductIsoClassEquiv` commutes with restriction along a morphism
> of `𝒞`, so it is an isomorphism of presheaves and not merely a family of bijections.

```lean
lemma twoFibreProductIsoClassMap_naturality
    [(TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒵 F G).IsFibered] {V U : 𝒞} (f : V ⟶ U)
    (c : (TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒵 F G).isoClassPresheaf.obj (op U)) :
    (twoFibreProductIsoClassMap hF hG V
        ((TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒵 F G).isoClassPresheaf.map f.op c)).val =
      (p𝒳.isoClassPresheaf.map f.op (twoFibreProductIsoClassMap hF hG U c).val.fst,
        p𝒴.isoClassPresheaf.map f.op (twoFibreProductIsoClassMap hF hG U c).val.snd)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.39, Tag 04S9](https://stacks.math.columbia.edu/tag/04S9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
