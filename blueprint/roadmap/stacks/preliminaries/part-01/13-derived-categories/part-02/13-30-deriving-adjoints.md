---
declaration: section
origin: cited
lean: CategoryTheory.Adjunction.existsUnique_homEquiv_of_isRightDerivedValueAt, CategoryTheory.Adjunction.derivedHomEquiv_naturality, CategoryTheory.Adjunction.derivedHomEquiv_comp_eq_comp, CategoryTheory.Adjunction.derivedHomEquiv_comp_eq_comp_left, CategoryTheory.Adjunction.existsUnique_homEquiv_derivedCategory_of_isRightDerivedValueAt, CategoryTheory.Adjunction.derivedCategoryHomEquiv, CategoryTheory.Adjunction.derivedCategoryHomEquiv_comp_rightDerivedMap, CategoryTheory.Adjunction.derivedCategoryHomEquiv_map_comp
statement: formalized
proof: formalized
---

# 13.30 Deriving adjoints

Section 13.30 of the Stacks Project, [Tag 0FNC](https://stacks.math.columbia.edu/tag/0FNC). 3 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FND, a lemma

[Tag 0FND](https://stacks.math.columbia.edu/tag/0FND) in the Stacks Project.

**`CategoryTheory.Adjunction.existsUnique_homEquiv_of_isRightDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean, line 610](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean#L610). The attribute's comment: “the canonical bijection and its characterisation by fractions; its functoriality in both variables is `derivedHomEquiv_naturality`, `derivedHomEquiv_comp_eq_comp` and `derivedHomEquiv_comp_eq_comp_left`”. References: SGA 4 XVII (2.3.7), “outer Hom bijection”.

> **Stacks 0FND**: deriving adjoints. Let `F : 𝒟 ⥤ 𝒟'` be right adjoint to `G : 𝒟' ⥤ 𝒟`, let
> `S`, `S'` be classes of morphisms of `𝒟`, `𝒟'` admitting left, resp. right fractions, and let
> `Q : 𝒟 ⥤ S⁻¹𝒟` and `Q' : 𝒟' ⥤ (S')⁻¹𝒟'` be localization functors. Let `K` be an object of `𝒟`
> at which the right derived functor `RF` of `Q' ∘ F` is defined, with value `RF(K) = c.pt`, and
> let `M` be an object of `𝒟'` at which the left derived functor `LG` of `Q ∘ G` is defined, with
> value `LG(M) = d.pt.unop` (the left derived value is the right derived value of the opposite
> functors, as in Stacks 05S9). Then there is a unique bijection
> `Hom_{(S')⁻¹𝒟'}(M, RF(K)) ≃ Hom_{S⁻¹𝒟}(LG(M), K)` compatible with the fractions computing the
> two sides: for every index `s : K ⟶ I` of the ind-object defining `RF(K)`, every index
> `t : P ⟶ M` of the pro-object defining `LG(M)` and every `f : P ⟶ F(I)`, a morphism
> `ψ : M ⟶ RF(K)` satisfies `Q'(t) ≫ ψ = Q'(f) ≫ (coprojection at s)` if and only if its image
> satisfies `φ(ψ) ≫ Q(s) = (projection at t) ≫ Q(f^♯)`, where `f^♯ : G(P) ⟶ I` is adjoint
> to `f`.
>
> The source's further assertion that this bijection is functorial in both variables is proved in
> `StacksFrontier.CategoryTheory.Localization.DerivingAdjointsNaturality`, where the bijection is named
> `CategoryTheory.Adjunction.derivedHomEquiv`: `derivedHomEquiv_naturality` for morphisms of `𝒟`
> and `𝒟'`, and `derivedHomEquiv_comp_eq_comp`, `derivedHomEquiv_comp_eq_comp_left` for morphisms
> of `S⁻¹𝒟` and `(S')⁻¹𝒟'`.

```lean
theorem existsUnique_homEquiv_of_isRightDerivedValueAt
    {D : Type u₁} [Category.{v₁} D] {D' : Type u₂} [Category.{v₂} D']
    {SD : Type u₃} [Category.{v₃} SD] {SD' : Type u₄} [Category.{v₄} SD']
    {F : D ⥤ D'} {G : D' ⥤ D} (adj : G ⊣ F)
    (S : MorphismProperty D) (S' : MorphismProperty D')
    [S.HasLeftCalculusOfFractions] [S'.HasRightCalculusOfFractions]
    (Q : D ⥤ SD) [Q.IsLocalization S] (Q' : D' ⥤ SD') [Q'.IsLocalization S']
    (K : D) (M : D')
    (c : Cocone (MorphismProperty.Under.forget S ⊤ K ⋙ Under.forget K ⋙ F ⋙ Q'))
    (hc : (F ⋙ Q').IsRightDerivedValueAt S K c)
    (d : Cocone (MorphismProperty.Under.forget S'.op ⊤ (Opposite.op M) ⋙
      Under.forget (Opposite.op M) ⋙ (G ⋙ Q).op))
    (hd : (G ⋙ Q).op.IsRightDerivedValueAt S'.op (Opposite.op M) d) :
    ∃! φ : (Q'.obj M ⟶ c.pt) ≃ (d.pt.unop ⟶ Q.obj K),
      ∀ (s : S.Under ⊤ K) (t : S'.op.Under ⊤ (Opposite.op M))
        (f : t.right.unop ⟶ F.obj s.right) (ψ : Q'.obj M ⟶ c.pt),
        Q'.map t.hom.unop ≫ ψ = Q'.map f ≫ c.ι.app s ↔
          φ ψ ≫ Q.map s.hom = (d.ι.app t).unop ≫ Q.map ((adj.homEquiv _ _).symm f)
```

**`CategoryTheory.Adjunction.derivedHomEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean#L244). The attribute's comment: “functoriality of the bijection in both variables, for morphisms of `𝒟` and `𝒟'`”.

> **Stacks 0FND**, functoriality of the canonical bijection in both variables, with respect to
> morphisms of `𝒟` and `𝒟'`. Let `κ : K ⟶ K'` be a morphism of `𝒟` with `RF` defined at `K` and
> `K'`, and `γ : M' ⟶ M` a morphism of `𝒟'` with `LG` defined at `M'` and `M`, with induced
> morphisms `RF(κ) : RF(K) ⟶ RF(K')` and `LG(γ) : LG(M') ⟶ LG(M)` between the values
> (Stacks 05SA). Then for every `ψ : M ⟶ RF(K)`,
> `φ_{K',M'}(Q'(γ) ≫ ψ ≫ RF(κ)) = LG(γ) ≫ φ_{K,M}(ψ) ≫ Q(κ)`. Morphisms of the localized categories
> are `derivedHomEquiv_comp_eq_comp` and `derivedHomEquiv_comp_eq_comp_left`.

```lean
theorem derivedHomEquiv_naturality
    (hc : (F ⋙ Q').IsRightDerivedValueAt S K c) (hc' : (F ⋙ Q').IsRightDerivedValueAt S K' c')
    (hd : (G ⋙ Q).op.IsRightDerivedValueAt S'.op (op M) d)
    (hd' : (G ⋙ Q).op.IsRightDerivedValueAt S'.op (op M') d')
    (κ : K ⟶ K') (γ : M' ⟶ M) (ψ : Q'.obj M ⟶ c.pt) :
    adj.derivedHomEquiv hc' hd' (Q'.map γ ≫ ψ ≫ rightDerivedMap S (F ⋙ Q') hc hc' κ) =
      (rightDerivedMap S'.op (G ⋙ Q).op hd hd' γ.op).unop ≫
        adj.derivedHomEquiv hc hd ψ ≫ Q.map κ
```

**`CategoryTheory.Adjunction.derivedHomEquiv_comp_eq_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean#L275). The attribute's comment: “functoriality of the bijection in `K`, for morphisms of `S⁻¹𝒟`”.

> **Stacks 0FND**, functoriality of the canonical bijection in `K` with respect to a morphism
> `g : Q(K) ⟶ Q(K')` of `S⁻¹𝒟`. Such a morphism is a left fraction `g = Q(κ) ≫ Q(σ)⁻¹` with
> `κ : K ⟶ L` and `σ : K' ⟶ L` in `S`, that is `g ≫ Q(σ) = Q(κ)`; then `RF` is defined at `L`
> (Stacks 05SB) and `RF(g) = RF(κ) ≫ RF(σ)⁻¹` is the morphism `ρ : RF(K) ⟶ RF(K')` with
> `ρ ≫ RF(σ) = RF(κ)`. For every `ψ : M ⟶ RF(K)`, `φ_{K',M}(ψ ≫ ρ) = φ_{K,M}(ψ) ≫ g`.

```lean
theorem derivedHomEquiv_comp_eq_comp
    (hc : (F ⋙ Q').IsRightDerivedValueAt S K c) (hc' : (F ⋙ Q').IsRightDerivedValueAt S K' c')
    (hL : (F ⋙ Q').IsRightDerivedValueAt S L cL)
    (hd : (G ⋙ Q).op.IsRightDerivedValueAt S'.op (op M) d)
    (κ : K ⟶ L) (σ : K' ⟶ L) (hσ : S σ) (g : Q.obj K ⟶ Q.obj K')
    (hg : g ≫ Q.map σ = Q.map κ) (ρ : c.pt ⟶ c'.pt)
    (hρ : ρ ≫ rightDerivedMap S (F ⋙ Q') hc' hL σ = rightDerivedMap S (F ⋙ Q') hc hL κ)
    (ψ : Q'.obj M ⟶ c.pt) :
    adj.derivedHomEquiv hc' hd (ψ ≫ ρ) = adj.derivedHomEquiv hc hd ψ ≫ g
```

**`CategoryTheory.Adjunction.derivedHomEquiv_comp_eq_comp_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean#L296). The attribute's comment: “functoriality of the bijection in `M`, for morphisms of `(S')⁻¹𝒟'`”.

> **Stacks 0FND**, functoriality of the canonical bijection in `M` with respect to a morphism
> `γ : Q'(M') ⟶ Q'(M)` of `(S')⁻¹𝒟'`. Such a morphism is a right fraction
> `γ = Q'(τ)⁻¹ ≫ Q'(ν)` with `τ : N ⟶ M'` in `S'` and `ν : N ⟶ M`, that is `Q'(τ) ≫ γ = Q'(ν)`;
> then `LG` is defined at `N` (Stacks 05SB) and `LG(γ) = LG(τ)⁻¹ ≫ LG(ν)` is the morphism
> `μ : LG(M') ⟶ LG(M)` with `LG(τ) ≫ μ = LG(ν)`. For every `ψ : M ⟶ RF(K)`,
> `φ_{K,M'}(γ ≫ ψ) = μ ≫ φ_{K,M}(ψ)`.

```lean
theorem derivedHomEquiv_comp_eq_comp_left
    (hc : (F ⋙ Q').IsRightDerivedValueAt S K c)
    (hd : (G ⋙ Q).op.IsRightDerivedValueAt S'.op (op M) d)
    (hd' : (G ⋙ Q).op.IsRightDerivedValueAt S'.op (op M') d')
    (hN : (G ⋙ Q).op.IsRightDerivedValueAt S'.op (op N) dN)
    (ν : N ⟶ M) (τ : N ⟶ M') (hτ : S' τ) (γ : Q'.obj M' ⟶ Q'.obj M)
    (hγ : Q'.map τ ≫ γ = Q'.map ν) (μ : d'.pt.unop ⟶ d.pt.unop)
    (hμ : (rightDerivedMap S'.op (G ⋙ Q).op hd' hN τ.op).unop ≫ μ =
      (rightDerivedMap S'.op (G ⋙ Q).op hd hN ν.op).unop)
    (ψ : Q'.obj M ⟶ c.pt) :
    adj.derivedHomEquiv hc hd' (γ ≫ ψ) = μ ≫ adj.derivedHomEquiv hc hd ψ
```

## Tag 0DVC, a lemma

[Tag 0DVC](https://stacks.math.columbia.edu/tag/0DVC) in the Stacks Project.

**`CategoryTheory.Adjunction.existsUnique_homEquiv_derivedCategory_of_isRightDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean, line 854](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean#L854). The attribute's comment: “the canonical isomorphism and its characterisation by fractions; functoriality is `derivedCategoryHomEquiv_comp_rightDerivedMap` and `derivedCategoryHomEquiv_map_comp`”.

> **Stacks 0DVC**: deriving adjoints between derived categories. Let `F : 𝒜 ⥤ ℬ` be right
> adjoint to `G : ℬ ⥤ 𝒜`, functors of abelian categories, let `K` be a complex of `𝒜` and `M` a
> complex of `ℬ`, and let `RF`, resp. `LG`, be the right, resp. left, derived functor of
> `K(𝒜) ⥤ K(ℬ) ⥤ D(ℬ)`, resp. `K(ℬ) ⥤ K(𝒜) ⥤ D(𝒜)`, with respect to the quasi-isomorphisms.
> Assume `RF` is defined at `K`, with value `RF(K) = c.pt`, and `LG` is defined at `M`, with value
> `LG(M) = d.pt` (Stacks 05S9). Then there is a unique bijection
> `Hom_{D(ℬ)}(M, RF(K)) ≃ Hom_{D(𝒜)}(LG(M), K)` compatible with the fractions computing the two
> sides: for every index `s : K ⟶ I` of the ind-object defining `RF(K)`, every index `t : P ⟶ M`
> of the pro-object defining `LG(M)` and every pair of chain maps `f : P ⟶ F(I)`, `g : G(P) ⟶ I`
> that are adjoint to one another in each degree, a morphism `ψ : M ⟶ RF(K)` satisfies
> `Qh(t) ≫ ψ = Qh(f) ≫ (coprojection at s)` if and only if its image satisfies
> `φ(ψ) ≫ Qh(s) = (projection at t) ≫ Qh(g)`.
>
> The source's further assertion that this isomorphism is functorial in both variables is not part
> of this statement: the bijection is named `CategoryTheory.Adjunction.derivedCategoryHomEquiv`, and
> its naturality in `K` and in `M` is `derivedCategoryHomEquiv_comp_rightDerivedMap` and
> `derivedCategoryHomEquiv_map_comp`, in the module
> `StacksFrontier.CategoryTheory.Localization.DerivingAdjointsNaturality`.

```lean
theorem existsUnique_homEquiv_derivedCategory_of_isRightDerivedValueAt
    {A : Type u₁} [Category.{v₁} A] [Abelian A] [HasDerivedCategory.{w₁} A]
    {B : Type u₂} [Category.{v₂} B] [Abelian B] [HasDerivedCategory.{w₂} B]
    {F : A ⥤ B} {G : B ⥤ A} [F.Additive] [G.Additive] (adj : G ⊣ F)
    (K : HomotopyCategory A (ComplexShape.up ℤ)) (M : HomotopyCategory B (ComplexShape.up ℤ))
    (c : Cocone (MorphismProperty.Under.forget
        (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) ⊤ K ⋙
      Under.forget K ⋙ F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh))
    (hc : (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsRightDerivedValueAt
      (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) K c)
    (d : Cone (MorphismProperty.Over.forget
        (HomotopyCategory.quasiIso B (ComplexShape.up ℤ)) ⊤ M ⋙
      Over.forget M ⋙ G.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh))
    (hd : (G.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsLeftDerivedValueAt
      (HomotopyCategory.quasiIso B (ComplexShape.up ℤ)) M d) :
    ∃! φ : (DerivedCategory.Qh.obj M ⟶ c.pt) ≃ (d.pt ⟶ DerivedCategory.Qh.obj K),
      ∀ (s : (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).Under ⊤ K)
        (t : (HomotopyCategory.quasiIso B (ComplexShape.up ℤ)).Over ⊤ M)
        (f : t.left.as ⟶ (F.mapHomologicalComplex (ComplexShape.up ℤ)).obj s.right.as)
        (g : (G.mapHomologicalComplex (ComplexShape.up ℤ)).obj t.left.as ⟶ s.right.as),
        (∀ n, f.f n = adj.homEquiv _ _ (g.f n)) →
        ∀ ψ : DerivedCategory.Qh.obj M ⟶ c.pt,
          DerivedCategory.Qh.map t.hom ≫ ψ =
              DerivedCategory.Qh.map
                ((HomotopyCategory.quotient B (ComplexShape.up ℤ)).map f) ≫ c.ι.app s ↔
            φ ψ ≫ DerivedCategory.Qh.map s.hom =
              d.π.app t ≫ DerivedCategory.Qh.map
                ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).map g)
```

**`CategoryTheory.Adjunction.derivedCategoryHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean#L340). The attribute's comment: “the canonical isomorphism; its functoriality in both variables is `derivedCategoryHomEquiv_comp_rightDerivedMap` and `derivedCategoryHomEquiv_map_comp`”.

> **Stacks 0DVC**: the canonical bijection `Hom_{D(ℬ)}(M, RF(K)) ≃ Hom_{D(𝒜)}(LG(M), K)` for
> `F : 𝒜 ⥤ ℬ` right adjoint to `G : ℬ ⥤ 𝒜`, a complex `K` of `𝒜` at which `RF` is defined, with
> value `RF(K) = c.pt`, and a complex `M` of `ℬ` at which `LG` is defined, with value
> `LG(M) = d.pt`. It is the unique bijection compatible with the fractions computing the two sides
> (`derivedCategoryHomEquiv_spec`, `derivedCategoryHomEquiv_unique`), and it is natural in `K`
> (`derivedCategoryHomEquiv_comp_rightDerivedMap`) and in `M`
> (`derivedCategoryHomEquiv_map_comp`).

```lean
noncomputable def derivedCategoryHomEquiv
    (hc : (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsRightDerivedValueAt
      (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) K c)
    (hd : (G.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsLeftDerivedValueAt
      (HomotopyCategory.quasiIso B (ComplexShape.up ℤ)) M d) :
    (DerivedCategory.Qh.obj M ⟶ c.pt) ≃ (d.pt ⟶ DerivedCategory.Qh.obj K)
```

**`CategoryTheory.Adjunction.derivedCategoryHomEquiv_comp_rightDerivedMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean, line 434](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean#L434). The attribute's comment: “functoriality in `K`, with respect to morphisms of `K(𝒜)`”.

> **Stacks 0DVC**, functoriality in `K`. Let `κ : K ⟶ K'` be a morphism of complexes of `𝒜`
> (in the homotopy category) such that `RF` is defined at `K` and at `K'`, and let
> `RF(κ) : RF(K) ⟶ RF(K')` be the induced morphism between the values (Stacks 05SA). Then for every
> `ψ : M ⟶ RF(K)` in `D(ℬ)`, `φ_{K',M}(ψ ≫ RF(κ)) = φ_{K,M}(ψ) ≫ κ` in `D(𝒜)`.

```lean
theorem derivedCategoryHomEquiv_comp_rightDerivedMap
    (hc : (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsRightDerivedValueAt
      (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) K c)
    (hc' : (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsRightDerivedValueAt
      (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) K' c')
    (hd : (G.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsLeftDerivedValueAt
      (HomotopyCategory.quasiIso B (ComplexShape.up ℤ)) M d)
    (κ : K ⟶ K') (ψ : DerivedCategory.Qh.obj M ⟶ c.pt) :
    adj.derivedCategoryHomEquiv hc' hd
        (ψ ≫ rightDerivedMap (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))
          (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh) hc hc' κ) =
      adj.derivedCategoryHomEquiv hc hd ψ ≫ DerivedCategory.Qh.map κ
```

**`CategoryTheory.Adjunction.derivedCategoryHomEquiv_map_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean, line 508](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjointsNaturality.lean#L508). The attribute's comment: “functoriality in `M`, with respect to morphisms of `K(ℬ)`”.

> **Stacks 0DVC**, functoriality in `M`. Let `γ : M' ⟶ M` be a morphism of complexes of `ℬ`
> (in the homotopy category) such that `LG` is defined at `M'` and at `M`, and let
> `LG(γ) : LG(M') ⟶ LG(M)` be the induced morphism between the values (Stacks 05SA). Then for every
> `ψ : M ⟶ RF(K)` in `D(ℬ)`, `φ_{K,M'}(γ ≫ ψ) = LG(γ) ≫ φ_{K,M}(ψ)` in `D(𝒜)`.

```lean
theorem derivedCategoryHomEquiv_map_comp
    (hc : (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsRightDerivedValueAt
      (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) K c)
    (hd : (G.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsLeftDerivedValueAt
      (HomotopyCategory.quasiIso B (ComplexShape.up ℤ)) M d)
    (hd' : (G.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsLeftDerivedValueAt
      (HomotopyCategory.quasiIso B (ComplexShape.up ℤ)) M' d')
    (γ : M' ⟶ M) (ψ : DerivedCategory.Qh.obj M ⟶ c.pt) :
    adj.derivedCategoryHomEquiv hc hd' (DerivedCategory.Qh.map γ ≫ ψ) =
      leftDerivedMap (HomotopyCategory.quasiIso B (ComplexShape.up ℤ))
          (G.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh) hd' hd γ ≫
        adj.derivedCategoryHomEquiv hc hd ψ
```

## Tag 09T5, a lemma

[Tag 09T5](https://stacks.math.columbia.edu/tag/09T5) in the Stacks Project.

**`CategoryTheory.Adjunction.exists_derived_of_isRightDerivedValueAt_of_isLeftDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean, line 1270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean#L1270).

> **Stacks 09T5**: the derived functors of an adjoint pair are adjoint. Let `F : 𝒟 ⥤ 𝒟'` be
> right adjoint to `G : 𝒟' ⥤ 𝒟`, let `S`, `S'` be classes of morphisms of `𝒟`, `𝒟'` admitting
> left, resp. right fractions, and let `Q : 𝒟 ⥤ S⁻¹𝒟`, `Q' : 𝒟' ⥤ (S')⁻¹𝒟'` be localization
> functors. Let `RF : S⁻¹𝒟 ⥤ (S')⁻¹𝒟'` with `β : F ⋙ Q' ⟶ Q ⋙ RF` be the right derived functor
> of `Q' ∘ F`, in the sense that for every object `K` of `𝒟` the ind-object
> `(s : K ⟶ I) ↦ Q'(F(I))` is essentially constant with value `RF(Q(K))` and coprojections
> induced by `β` (Stacks 05S9), and let `LG : (S')⁻¹𝒟' ⥤ S⁻¹𝒟` with `α : Q' ⋙ LG ⟶ G ⋙ Q` be
> the left derived functor of `Q ∘ G`, in the dual sense. Then `LG` is left adjoint to `RF`, by an
> adjunction whose unit and counit are compatible with `α`, `β` and the adjunction between `F`
> and `G`.

```lean
theorem exists_derived_of_isRightDerivedValueAt_of_isLeftDerivedValueAt
    {D : Type u₁} [Category.{v₁} D] {D' : Type u₂} [Category.{v₂} D']
    {SD : Type u₃} [Category.{v₃} SD] {SD' : Type u₄} [Category.{v₄} SD']
    {F : D ⥤ D'} {G : D' ⥤ D} (adj : G ⊣ F)
    (S : MorphismProperty D) (S' : MorphismProperty D')
    [S.HasLeftCalculusOfFractions] [S'.HasRightCalculusOfFractions]
    (Q : D ⥤ SD) [Q.IsLocalization S] (Q' : D' ⥤ SD') [Q'.IsLocalization S']
    (RF : SD ⥤ SD') (β : F ⋙ Q' ⟶ Q ⋙ RF)
    (LG : SD' ⥤ SD) (α : Q' ⋙ LG ⟶ G ⋙ Q)
    (hRF : ∀ K : D, ∃ (c : Cocone (MorphismProperty.Under.forget S ⊤ K ⋙
          Under.forget K ⋙ F ⋙ Q'))
        (_ : (F ⋙ Q').IsRightDerivedValueAt S K c) (e : c.pt ≅ RF.obj (Q.obj K)),
        ∀ s : S.Under ⊤ K, c.ι.app s ≫ e.hom ≫ RF.map (Q.map s.hom) = β.app s.right)
    (hLG : ∀ M : D', ∃ (d : Cone (MorphismProperty.Over.forget S' ⊤ M ⋙
          Over.forget M ⋙ G ⋙ Q))
        (_ : (G ⋙ Q).IsLeftDerivedValueAt S' M d) (e : LG.obj (Q'.obj M) ≅ d.pt),
        ∀ t : S'.Over ⊤ M, LG.map (Q'.map t.hom) ≫ e.hom ≫ d.π.app t = α.app t.left) :
    ∃ adj' : LG ⊣ RF,
      (∀ M : D', adj'.unit.app (Q'.obj M) ≫ RF.map (α.app M) =
          Q'.map (adj.unit.app M) ≫ β.app (G.obj M)) ∧
        (∀ K : D, LG.map (β.app K) ≫ adj'.counit.app (Q.obj K) =
          α.app (F.obj K) ≫ Q.map (adj.counit.app K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.30, Tag 0FNC](https://stacks.math.columbia.edu/tag/0FNC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
