---
declaration: section
origin: cited
lean: CategoryTheory.Adjunction.existsUnique_homEquiv_of_isRightDerivedValueAt, CategoryTheory.Adjunction.existsUnique_homEquiv_derivedCategory_of_isRightDerivedValueAt, CategoryTheory.Adjunction.exists_derived_of_isRightDerivedValueAt_of_isLeftDerivedValueAt
statement: formalized
proof: formalized
---

# 13.30 Deriving adjoints

Section 13.30 of the Stacks Project, [Tag 0FNC](https://stacks.math.columbia.edu/tag/0FNC). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FND, a lemma

[Tag 0FND](https://stacks.math.columbia.edu/tag/0FND) in the Stacks Project.

**`CategoryTheory.Adjunction.existsUnique_homEquiv_of_isRightDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean, line 593](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean#L593). References: SGA 4 XVII (2.3.7), “outer Hom bijection”.

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

## Tag 0DVC, a lemma

[Tag 0DVC](https://stacks.math.columbia.edu/tag/0DVC) in the Stacks Project.

**`CategoryTheory.Adjunction.existsUnique_homEquiv_derivedCategory_of_isRightDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean, line 830](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean#L830).

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

## Tag 09T5, a lemma

[Tag 09T5](https://stacks.math.columbia.edu/tag/09T5) in the Stacks Project.

**`CategoryTheory.Adjunction.exists_derived_of_isRightDerivedValueAt_of_isLeftDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean, line 1246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Localization/DerivingAdjoints.lean#L1246).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
