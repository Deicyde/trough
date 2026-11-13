---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.isIso_properBaseChangeMap_app, AlgebraicGeometry.SmallEtale.properBaseChangeMap_rectangle_eq_comp, AlgebraicGeometry.SmallEtale.properBaseChangeMap_horizontal_paste, AlgebraicGeometry.SmallEtale.properBaseChangeMap_interchange, AlgebraicGeometry.SmallEtale.properBaseChangeMap_rectangle_interchange, AlgebraicGeometry.SmallEtale.properBaseChangeMap_baseChange, AlgebraicGeometry.SmallEtale.isIso_lowerShriekProperDirectImageMap_app
statement: formalized
proof: formalized
---

# 63.8 Preliminaries to derived lower shriek via compactifications

Section 63.8 of the Stacks Project, [Tag 0F7A](https://stacks.math.columbia.edu/tag/0F7A). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F7B, a lemma

[Tag 0F7B](https://stacks.math.columbia.edu/tag/0F7B) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isIso_properBaseChangeMap_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeIsIso.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeIsIso.lean#L453).

> **[Stacks, Tag 0F7B].** Consider a commutative diagram of schemes of a big étale site
> ```
> X' --k--> X
> |         |
> f'        f
> v         v
> Y' --l--> Y
> ```
> with `f` and `f'` proper and `k` and `l` separated and locally quasi-finite (here, as in the
> source, locally quasi-finite includes locally of finite type). Let `Λ` be a ring, in the
> universe `u` of the site. Functorially in `K ∈ D(X'_étale, Λ)` there is a canonical map
> `l_! Rf'_* K ⟶ Rf_*(k_! K)` in `D(Y_étale, Λ)`, namely
> `AlgebraicGeometry.SmallEtale.properBaseChangeMap` (for any right derived functors `Rf'_*`, `Rf_*`
> of the direct images, with their units). This map is an isomorphism if
>
> * (a) `K` is bounded below and has torsion cohomology sheaves, or
> * (b) `Λ` is a torsion ring.
>
> Case (a) is `isIso_properBaseChangeMap_app_of_isGE`, case (b)
> `isIso_properBaseChangeMap_of_natCast_eq_zero`.

```lean
theorem isIso_properBaseChangeMap_app (K : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ))
    (hK : (∃ n : ℤ, K.IsGE n ∧ moduleTorsionCohomologyProperty.{u, u, w, u} B X' Λ K) ∨
      ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) :
    IsIso ((properBaseChangeMap B Λ k f' f l w RF' αF' RF αF).app K)
```

## Tag 0F7C, a lemma

[Tag 0F7C](https://stacks.math.columbia.edu/tag/0F7C) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properBaseChangeMap_rectangle_eq_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChange.lean, line 816](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChange.lean#L816).

> **[Stacks, Tag 0F7C]**, in the form the source states it. Consider a commutative diagram of
> a big étale site
> ```
> X' --k--> X
> |         |
> f'        f
> v         v
> Y' --l--> Y
> |         |
> g'        g
> v         v
> Z' --m--> Z
> ```
> with `f`, `f'`, `g` and `g'` proper and `k`, `l` and `m` separated and locally quasi-finite, and
> let `Λ` be a ring. Write `R(g ∘ f)_* = Rg_* ∘ Rf_*` and `R(g' ∘ f')_* = Rg'_* ∘ Rf'_*` through
> the canonical comparisons, which are isomorphisms
> (`AlgebraicGeometry.SmallEtale.isIso_compComparison_etalePushforwardMod`). Then the map
> `m_! ∘ Rg'_* ∘ Rf'_* ⟶ Rg_* ∘ Rf_* ∘ k_!` of [Stacks, Tag 0F7B] for the outer rectangle is the
> composite
> ```
> m_! ∘ Rg'_* ∘ Rf'_* ⟶ Rg_* ∘ l_! ∘ Rf'_* ⟶ Rg_* ∘ Rf_* ∘ k_!
> ```
> of the maps of the two squares. This holds for every choice of the six right derived functors.
>
> The source calls the maps of [Stacks, Tag 0F7B] isomorphisms; that is [Stacks, Tag 0F7B]
> itself (whose proof rests on proper base change, [Stacks, Tag 0DDF], under its torsion
> hypotheses), and is not needed here: the content of this tag is the identity between the maps,
> which holds without any hypothesis on `Λ` or on the complexes. The identity before identifying
> `R(g ∘ f)_*` with `Rg_* ∘ Rf_*`, which needs no invertibility of the comparisons, is
> `AlgebraicGeometry.SmallEtale.properBaseChangeMap_vertical_paste`.

```lean
theorem properBaseChangeMap_rectangle_eq_comp (k : X' ⟶ X) (f' : X' ⟶ Y') (f : X ⟶ Y)
    (l : Y' ⟶ Y) (g' : Y' ⟶ Z') (g : Y ⟶ Z) (m : Z' ⟶ Z)
    (w₁ : k ≫ f = f' ≫ l) (w₂ : l ≫ g = g' ≫ m)
    [IsProper (B.inclusion.map f')] [IsProper (B.inclusion.map f)]
    [IsProper (B.inclusion.map g')] [IsProper (B.inclusion.map g)]
    [IsSeparated (B.inclusion.map k)] [LocallyQuasiFinite (B.inclusion.map k)]
    [LocallyOfFiniteType (B.inclusion.map k)]
    [IsSeparated (B.inclusion.map l)] [LocallyQuasiFinite (B.inclusion.map l)]
    [LocallyOfFiniteType (B.inclusion.map l)]
    [IsSeparated (B.inclusion.map m)] [LocallyQuasiFinite (B.inclusion.map m)]
    [LocallyOfFiniteType (B.inclusion.map m)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z Λ)]
    (RF' : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ))
    (αF' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF')
    (RF : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ))
    (αF : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    (RG' : DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z' Λ))
    (αG' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG')
    (RG : DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z Λ))
    (αG : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG)
    (RP' : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z' Λ))
    (αP' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B (f' ≫ g'))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP')
    (RP : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z Λ))
    (αP : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B (f ≫ g))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    [RF'.IsRightDerivedFunctor αF'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))]
    [RF.IsRightDerivedFunctor αF
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X Λ) (ComplexShape.up ℤ))]
    [RG'.IsRightDerivedFunctor αG'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Y' Λ) (ComplexShape.up ℤ))]
    [RG.IsRightDerivedFunctor αG
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Y Λ) (ComplexShape.up ℤ))]
    [RP'.IsRightDerivedFunctor αP'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))]
    [RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X Λ) (ComplexShape.up ℤ))] :
    haveI := isIso_compComparison_etalePushforwardMod B Λ f' g' αF' αG' αP'
    Functor.whiskerRight (inv (compComparison
        (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))
        αF' αG' αP' (Functor.mapHomotopyCategoryCompIso (etalePushforwardModCompIso B Λ f' g')
          (ComplexShape.up ℤ))))
        (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m)).mapDerivedCategory ≫
      properBaseChangeMap B Λ k (f' ≫ g') (f ≫ g) m (rectangle_comm B w₁ w₂) RP' αP' RP αP ≫
      Functor.whiskerLeft (etaleModuleLift B Λ (fShriekFunctor.{u, u} B k)).mapDerivedCategory
        (compComparison
          (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X Λ) (ComplexShape.up ℤ))
          αF αG αP (Functor.mapHomotopyCategoryCompIso (etalePushforwardModCompIso B Λ f g)
            (ComplexShape.up ℤ))) =
      (Functor.associator RF' RG'
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m)).mapDerivedCategory).hom ≫
        Functor.whiskerLeft RF' (properBaseChangeMap B Λ l g' g m w₂ RG' αG' RG αG) ≫
        (Functor.associator RF'
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B l)).mapDerivedCategory RG).inv ≫
        Functor.whiskerRight (properBaseChangeMap B Λ k f' f l w₁ RF' αF' RF αF) RG ≫
        (Functor.associator
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B k)).mapDerivedCategory RF RG).hom
```

## Tag 0F7D, a lemma

[Tag 0F7D](https://stacks.math.columbia.edu/tag/0F7D) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properBaseChangeMap_horizontal_paste`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeHorizontal.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeHorizontal.lean#L317).

> **[Stacks, Tag 0F7D].** Consider a commutative diagram of a big étale site
> ```
> X'' --g'--> X' --g--> X
> |           |         |
> f''         f'        f
> v           v         v
> Y'' --h'--> Y' --h--> Y
> ```
> with `f`, `f'` and `f''` proper and `g`, `g'`, `h` and `h'` separated and locally quasi-finite,
> and let `Λ` be a ring. Then the maps of [Stacks, Tag 0F7B] for the two squares compose to the map
> for the outer rectangle. Precisely, as the source states it in its proof: write
> `(h' ≫ h)_! = h'_! ⋙ h_!` and `(g' ≫ g)_! = g'_! ⋙ g_!` on derived categories, through the
> identifications of Stacks 0F50 (`AlgebraicGeometry.SmallEtale.etaleModuleLiftFShriekCompIso`)
> induced on unbounded derived categories by
> `CategoryTheory.Functor.mapDerivedCategoryCompIsoOfCompIso`;
> then the map `(h' ≫ h)_! ∘ Rf''_* ⟶ Rf_* ∘ (g' ≫ g)_!` of the outer rectangle is the composite
> ```
> h_! ∘ h'_! ∘ Rf''_* ⟶ h_! ∘ Rf'_* ∘ g'_! ⟶ Rf_* ∘ g_! ∘ g'_!
> ```
> of the maps of the two squares. The statement holds for every choice of the three right derived
> functors `Rf''_*`, `Rf'_*`, `Rf_*` of the direct images on the unbounded homotopy categories.
>
> The source calls the maps of [Stacks, Tag 0F7B] isomorphisms; that they are is
> [Stacks, Tag 0F7B] itself, whose proof rests on proper base change, [Stacks, Tag 0DDF], and it is
> not used here: the content of this tag is the identity between the maps, from which the identity
> between the isomorphisms follows whenever they are isomorphisms.

```lean
theorem properBaseChangeMap_horizontal_paste (g' : X'' ⟶ X') (g : X' ⟶ X)
    (f'' : X'' ⟶ Y'') (f' : X' ⟶ Y') (f : X ⟶ Y) (h' : Y'' ⟶ Y') (h : Y' ⟶ Y)
    (w₁ : g' ≫ f' = f'' ≫ h') (w₂ : g ≫ f = f' ≫ h)
    [IsProper (B.inclusion.map f'')] [IsProper (B.inclusion.map f')]
    [IsProper (B.inclusion.map f)]
    [IsSeparated (B.inclusion.map g')] [LocallyQuasiFinite (B.inclusion.map g')]
    [LocallyOfFiniteType (B.inclusion.map g')]
    [IsSeparated (B.inclusion.map g)] [LocallyQuasiFinite (B.inclusion.map g)]
    [LocallyOfFiniteType (B.inclusion.map g)]
    [IsSeparated (B.inclusion.map h')] [LocallyQuasiFinite (B.inclusion.map h')]
    [LocallyOfFiniteType (B.inclusion.map h')]
    [IsSeparated (B.inclusion.map h)] [LocallyQuasiFinite (B.inclusion.map h)]
    [LocallyOfFiniteType (B.inclusion.map h)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y Λ)]
    (RF'' : DerivedCategory (ModuleSheaf.{u, u, u} B X'' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y'' Λ))
    (αF'' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f'')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF'')
    (RF' : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ))
    (αF' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF')
    (RF : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ))
    (αF : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    [RF''.IsRightDerivedFunctor αF''
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X'' Λ) (ComplexShape.up ℤ))]
    [RF'.IsRightDerivedFunctor αF'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))] :
    properBaseChangeMap B Λ (g' ≫ g) f'' f (h' ≫ h) (rectangle_comm_horizontal B w₁ w₂)
        RF'' αF'' RF αF =
      Functor.whiskerLeft RF''
          (Functor.mapDerivedCategoryCompIsoOfCompIso
            (etaleModuleLiftFShriekCompIso B Λ h' h (h' ≫ h) rfl)).inv ≫
        (Functor.associator RF''
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B h')).mapDerivedCategory
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B h)).mapDerivedCategory).inv ≫
        Functor.whiskerRight (properBaseChangeMap B Λ g' f'' f' h' w₁ RF'' αF'' RF' αF')
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B h)).mapDerivedCategory ≫
        (Functor.associator
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B g')).mapDerivedCategory RF'
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B h)).mapDerivedCategory).hom ≫
        Functor.whiskerLeft
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B g')).mapDerivedCategory
          (properBaseChangeMap B Λ g f' f h w₂ RF' αF' RF αF) ≫
        (Functor.associator
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B g')).mapDerivedCategory
          (etaleModuleLift B Λ (fShriekFunctor.{u, u} B g)).mapDerivedCategory RF).inv ≫
        Functor.whiskerRight
          (Functor.mapDerivedCategoryCompIsoOfCompIso
            (etaleModuleLiftFShriekCompIso B Λ g' g (g' ≫ g) rfl)).hom RF
```

## Tag 0F7E, a remark

[Tag 0F7E](https://stacks.math.columbia.edu/tag/0F7E) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properBaseChangeMap_interchange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeInterchange.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeInterchange.lean#L92). The attribute's comment: “the two composites of the maps of the four squares”.

> **[Stacks, Tag 0F7E], for the maps of the four squares.** Consider a commutative diagram of a
> big étale site
> ```
> X'' --k'--> X' --k--> X
>  |          |         |
>  f''        f'        f
>  v          v         v
> Y'' --l'--> Y' --l--> Y
>  |          |         |
>  g''        g'        g
>  v          v         v
> Z'' --m'--> Z' --m--> Z
> ```
> whose vertical arrows are proper and whose horizontal arrows are separated and locally
> quasi-finite, label its squares `A B / C D`, and let `Λ` be a ring. With `γ_A, γ_B, γ_C, γ_D`
> the maps of [Stacks, Tag 0F7B] for the squares
> (`γ_A : l'_! ∘ Rf''_* ⟶ Rf'_* ∘ k'_!`, `γ_B : l_! ∘ Rf'_* ⟶ Rf_* ∘ k_!`,
> `γ_C : m'_! ∘ Rg''_* ⟶ Rg'_* ∘ l'_!`, `γ_D : m_! ∘ Rg'_* ⟶ Rg_* ∘ l_!`), the two transformations
> `m_! ∘ m'_! ∘ Rg''_* ∘ Rf''_* ⟶ Rg_* ∘ Rf_* ∘ k_! ∘ k'_!`
> ```
> γ_B ∘ γ_D ∘ γ_A ∘ γ_C   and   γ_B ∘ γ_A ∘ γ_D ∘ γ_C
> ```
> (composites of whiskerings, as in Categories, Section 003D) agree, here at every object `K` of
> `D(X''_étale, Λ)`. The squares `A` and `D` meet in a single point, and the identity is the
> naturality of `γ_D` with respect to `γ_A` (Categories, Lemma 003F). It holds for every choice of
> the six right derived functors of the direct images.

```lean
theorem properBaseChangeMap_interchange
    (k' : X'' ⟶ X') (k : X' ⟶ X) (l' : Y'' ⟶ Y') (l : Y' ⟶ Y) (m' : Z'' ⟶ Z') (m : Z' ⟶ Z)
    (f'' : X'' ⟶ Y'') (f' : X' ⟶ Y') (f : X ⟶ Y)
    (g'' : Y'' ⟶ Z'') (g' : Y' ⟶ Z') (g : Y ⟶ Z)
    (wA : k' ≫ f' = f'' ≫ l') (wB : k ≫ f = f' ≫ l)
    (wC : l' ≫ g' = g'' ≫ m') (wD : l ≫ g = g' ≫ m)
    [IsProper (B.inclusion.map f'')] [IsProper (B.inclusion.map f')]
    [IsProper (B.inclusion.map f)]
    [IsProper (B.inclusion.map g'')] [IsProper (B.inclusion.map g')]
    [IsProper (B.inclusion.map g)]
    [IsSeparated (B.inclusion.map k')] [LocallyQuasiFinite (B.inclusion.map k')]
    [LocallyOfFiniteType (B.inclusion.map k')]
    [IsSeparated (B.inclusion.map k)] [LocallyQuasiFinite (B.inclusion.map k)]
    [LocallyOfFiniteType (B.inclusion.map k)]
    [IsSeparated (B.inclusion.map l')] [LocallyQuasiFinite (B.inclusion.map l')]
    [LocallyOfFiniteType (B.inclusion.map l')]
    [IsSeparated (B.inclusion.map l)] [LocallyQuasiFinite (B.inclusion.map l)]
    [LocallyOfFiniteType (B.inclusion.map l)]
    [IsSeparated (B.inclusion.map m')] [LocallyQuasiFinite (B.inclusion.map m')]
    [LocallyOfFiniteType (B.inclusion.map m')]
    [IsSeparated (B.inclusion.map m)] [LocallyQuasiFinite (B.inclusion.map m)]
    [LocallyOfFiniteType (B.inclusion.map m)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z Λ)]
    (RF'' : DerivedCategory (ModuleSheaf.{u, u, u} B X'' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y'' Λ))
    (αF'' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f'')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF'')
    (RF' : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ))
    (αF' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF')
    (RF : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ))
    (αF : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    (RG'' : DerivedCategory (ModuleSheaf.{u, u, u} B Y'' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z'' Λ))
    (αG'' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g'')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG'')
    (RG' : DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z' Λ))
    (αG' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG')
    (RG : DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z Λ))
    (αG : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG)
    [RF''.IsRightDerivedFunctor αF''
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X'' Λ) (ComplexShape.up ℤ))]
    [RF'.IsRightDerivedFunctor αF'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))]
    [RG''.IsRightDerivedFunctor αG''
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Y'' Λ) (ComplexShape.up ℤ))]
    [RG'.IsRightDerivedFunctor αG'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Y' Λ) (ComplexShape.up ℤ))]
    (K : DerivedCategory (ModuleSheaf.{u, u, u} B X'' Λ)) :
    (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m)).mapDerivedCategory.map
        ((properBaseChangeMap B Λ l' g'' g' m' wC RG'' αG'' RG' αG').app (RF''.obj K)) ≫
      (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m)).mapDerivedCategory.map
        (RG'.map ((properBaseChangeMap B Λ k' f'' f' l' wA RF'' αF'' RF' αF').app K)) ≫
      (properBaseChangeMap B Λ l g' g m wD RG' αG' RG αG).app
        (RF'.obj ((etaleModuleLift B Λ (fShriekFunctor.{u, u} B k')).mapDerivedCategory.obj K)) ≫
      RG.map ((properBaseChangeMap B Λ k f' f l wB RF' αF' RF αF).app
        ((etaleModuleLift B Λ (fShriekFunctor.{u, u} B k')).mapDerivedCategory.obj K)) =
    (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m)).mapDerivedCategory.map
        ((properBaseChangeMap B Λ l' g'' g' m' wC RG'' αG'' RG' αG').app (RF''.obj K)) ≫
      (properBaseChangeMap B Λ l g' g m wD RG' αG' RG αG).app
        ((etaleModuleLift B Λ (fShriekFunctor.{u, u} B l')).mapDerivedCategory.obj
          (RF''.obj K)) ≫
      RG.map ((etaleModuleLift B Λ (fShriekFunctor.{u, u} B l)).mapDerivedCategory.map
        ((properBaseChangeMap B Λ k' f'' f' l' wA RF'' αF'' RF' αF').app K)) ≫
      RG.map ((properBaseChangeMap B Λ k f' f l wB RF' αF' RF αF).app
        ((etaleModuleLift B Λ (fShriekFunctor.{u, u} B k')).mapDerivedCategory.obj K))
```

**`AlgebraicGeometry.SmallEtale.properBaseChangeMap_rectangle_interchange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeInterchange.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangeInterchange.lean#L205). The attribute's comment: “the two composites of the maps of the rectangles”.

> **[Stacks, Tag 0F7E], for the maps of the rectangles.** In the situation of
> `AlgebraicGeometry.SmallEtale.properBaseChangeMap_interchange`, consider moreover right derived
> functors `R(g'' ∘ f'')_*`, `R(g' ∘ f')_*`, `R(g ∘ f)_*` of the direct images along the vertical
> composites, and the maps of [Stacks, Tag 0F7B] for the four rectangles
> ```
> γ_{A+B} : (l ∘ l')_! ∘ Rf''_* ⟶ Rf_* ∘ (k ∘ k')_!
> γ_{C+D} : (m ∘ m')_! ∘ Rg''_* ⟶ Rg_* ∘ (l ∘ l')_!
> γ_{A+C} : m'_! ∘ R(g'' ∘ f'')_* ⟶ R(g' ∘ f')_* ∘ k'_!
> γ_{B+D} : m_! ∘ R(g' ∘ f')_* ⟶ R(g ∘ f)_* ∘ k_!
> ```
> written, as the source does, through `R(g ∘ f)_* = Rg_* ∘ Rf_*` (the canonical comparisons of
> [Stacks, Tag 05T2], isomorphisms by
> `AlgebraicGeometry.SmallEtale.isIso_compComparison_etalePushforwardMod`) and
> `(l ∘ l')_! = l_! ∘ l'_!` (Stacks 0F50,
> `AlgebraicGeometry.SmallEtale.etaleModuleLiftFShriekCompIso`, on derived categories by
> `CategoryTheory.Functor.mapDerivedCategoryCompIsoOfCompIso`). Then the two transformations
> `m_! ∘ m'_! ∘ Rg''_* ∘ Rf''_* ⟶ Rg_* ∘ Rf_* ∘ k_! ∘ k'_!`
> ```
> γ_{B+D} ∘ γ_{A+C}   and   γ_{A+B} ∘ γ_{C+D}
> ```
> agree, here at every object `K` of `D(X''_étale, Λ)`. By [Stacks, Tag 0F7C]
> (`AlgebraicGeometry.SmallEtale.properBaseChangeMap_rectangle_eq_comp`) and [Stacks, Tag 0F7D]
> (`AlgebraicGeometry.SmallEtale.properBaseChangeMap_horizontal_paste`) these are
> `γ_B ∘ γ_D ∘ γ_A ∘ γ_C` and `γ_B ∘ γ_A ∘ γ_D ∘ γ_C`, which agree by
> `AlgebraicGeometry.SmallEtale.properBaseChangeMap_interchange`. It holds for every choice of the
> nine right derived functors.

```lean
theorem properBaseChangeMap_rectangle_interchange
    (k' : X'' ⟶ X') (k : X' ⟶ X) (l' : Y'' ⟶ Y') (l : Y' ⟶ Y) (m' : Z'' ⟶ Z') (m : Z' ⟶ Z)
    (f'' : X'' ⟶ Y'') (f' : X' ⟶ Y') (f : X ⟶ Y)
    (g'' : Y'' ⟶ Z'') (g' : Y' ⟶ Z') (g : Y ⟶ Z)
    (wA : k' ≫ f' = f'' ≫ l') (wB : k ≫ f = f' ≫ l)
    (wC : l' ≫ g' = g'' ≫ m') (wD : l ≫ g = g' ≫ m)
    [IsProper (B.inclusion.map f'')] [IsProper (B.inclusion.map f')]
    [IsProper (B.inclusion.map f)]
    [IsProper (B.inclusion.map g'')] [IsProper (B.inclusion.map g')]
    [IsProper (B.inclusion.map g)]
    [IsSeparated (B.inclusion.map k')] [LocallyQuasiFinite (B.inclusion.map k')]
    [LocallyOfFiniteType (B.inclusion.map k')]
    [IsSeparated (B.inclusion.map k)] [LocallyQuasiFinite (B.inclusion.map k)]
    [LocallyOfFiniteType (B.inclusion.map k)]
    [IsSeparated (B.inclusion.map l')] [LocallyQuasiFinite (B.inclusion.map l')]
    [LocallyOfFiniteType (B.inclusion.map l')]
    [IsSeparated (B.inclusion.map l)] [LocallyQuasiFinite (B.inclusion.map l)]
    [LocallyOfFiniteType (B.inclusion.map l)]
    [IsSeparated (B.inclusion.map m')] [LocallyQuasiFinite (B.inclusion.map m')]
    [LocallyOfFiniteType (B.inclusion.map m')]
    [IsSeparated (B.inclusion.map m)] [LocallyQuasiFinite (B.inclusion.map m)]
    [LocallyOfFiniteType (B.inclusion.map m)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z'' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Z Λ)]
    (RF'' : DerivedCategory (ModuleSheaf.{u, u, u} B X'' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y'' Λ))
    (αF'' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f'')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF'')
    (RF' : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ))
    (αF' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF')
    (RF : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ))
    (αF : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    (RG'' : DerivedCategory (ModuleSheaf.{u, u, u} B Y'' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z'' Λ))
    (αG'' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g'')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG'')
    (RG' : DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z' Λ))
    (αG' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG')
    (RG : DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z Λ))
    (αG : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B g)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RG)
    (RP'' : DerivedCategory (ModuleSheaf.{u, u, u} B X'' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z'' Λ))
    (αP'' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B (f'' ≫ g''))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP'')
    (RP' : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z' Λ))
    (αP' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B (f' ≫ g'))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP')
    (RP : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Z Λ))
    (αP : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B (f ≫ g))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RP)
    [RF''.IsRightDerivedFunctor αF''
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X'' Λ) (ComplexShape.up ℤ))]
    [RF'.IsRightDerivedFunctor αF'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))]
    [RG''.IsRightDerivedFunctor αG''
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Y'' Λ) (ComplexShape.up ℤ))]
    [RG'.IsRightDerivedFunctor αG'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Y' Λ) (ComplexShape.up ℤ))]
    [RF.IsRightDerivedFunctor αF
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X Λ) (ComplexShape.up ℤ))]
    [RG.IsRightDerivedFunctor αG
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B Y Λ) (ComplexShape.up ℤ))]
    [RP''.IsRightDerivedFunctor αP''
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X'' Λ) (ComplexShape.up ℤ))]
    [RP'.IsRightDerivedFunctor αP'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))]
    [RP.IsRightDerivedFunctor αP
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X Λ) (ComplexShape.up ℤ))]
    (K : DerivedCategory (ModuleSheaf.{u, u, u} B X'' Λ)) :
    haveI := isIso_compComparison_etalePushforwardMod B Λ f'' g'' αF'' αG'' αP''
    haveI := isIso_compComparison_etalePushforwardMod B Λ f' g' αF' αG' αP'
    (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m)).mapDerivedCategory.map
        ((Functor.whiskerRight (inv (compComparison
            (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X'' Λ) (ComplexShape.up ℤ))
            αF'' αG'' αP'' (Functor.mapHomotopyCategoryCompIso
              (etalePushforwardModCompIso B Λ f'' g'') (ComplexShape.up ℤ))))
            (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m')).mapDerivedCategory ≫
          properBaseChangeMap B Λ k' (f'' ≫ g'') (f' ≫ g') m' (rectangle_comm B wA wC)
            RP'' αP'' RP' αP' ≫
          Functor.whiskerLeft (etaleModuleLift B Λ (fShriekFunctor.{u, u} B k')).mapDerivedCategory
            (compComparison
              (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))
              αF' αG' αP' (Functor.mapHomotopyCategoryCompIso
                (etalePushforwardModCompIso B Λ f' g') (ComplexShape.up ℤ)))).app K) ≫
      (Functor.whiskerRight (inv (compComparison
            (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))
            αF' αG' αP' (Functor.mapHomotopyCategoryCompIso
              (etalePushforwardModCompIso B Λ f' g') (ComplexShape.up ℤ))))
            (etaleModuleLift B Λ (fShriekFunctor.{u, u} B m)).mapDerivedCategory ≫
          properBaseChangeMap B Λ k (f' ≫ g') (f ≫ g) m (rectangle_comm B wB wD)
            RP' αP' RP αP ≫
          Functor.whiskerLeft (etaleModuleLift B Λ (fShriekFunctor.{u, u} B k)).mapDerivedCategory
            (compComparison
              (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X Λ) (ComplexShape.up ℤ))
              αF αG αP (Functor.mapHomotopyCategoryCompIso
                (etalePushforwardModCompIso B Λ f g) (ComplexShape.up ℤ)))).app
        ((etaleModuleLift B Λ (fShriekFunctor.{u, u} B k')).mapDerivedCategory.obj K) =
    (Functor.whiskerLeft RG'' (Functor.mapDerivedCategoryCompIsoOfCompIso
            (etaleModuleLiftFShriekCompIso B Λ m' m (m' ≫ m) rfl)).hom ≫
          properBaseChangeMap B Λ (l' ≫ l) g'' g (m' ≫ m) (rectangle_comm_horizontal B wC wD)
            RG'' αG'' RG αG ≫
          Functor.whiskerRight (Functor.mapDerivedCategoryCompIsoOfCompIso
            (etaleModuleLiftFShriekCompIso B Λ l' l (l' ≫ l) rfl)).inv RG).app (RF''.obj K) ≫
      RG.map ((Functor.whiskerLeft RF'' (Functor.mapDerivedCategoryCompIsoOfCompIso
            (etaleModuleLiftFShriekCompIso B Λ l' l (l' ≫ l) rfl)).hom ≫
          properBaseChangeMap B Λ (k' ≫ k) f'' f (l' ≫ l) (rectangle_comm_horizontal B wA wB)
            RF'' αF'' RF αF ≫
          Functor.whiskerRight (Functor.mapDerivedCategoryCompIsoOfCompIso
            (etaleModuleLiftFShriekCompIso B Λ k' k (k' ≫ k) rfl)).inv RF).app K)
```

## Tag 0F7F, a lemma

[Tag 0F7F](https://stacks.math.columbia.edu/tag/0F7F) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.properBaseChangeMap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangePullback.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ProperLowerShriekBaseChangePullback.lean#L699).

> **[Stacks, Tag 0F7F]: the base change maps of Tag 0F7B are compatible with change of base.**
> Let `b : Y₁ ⟶ Y` be a morphism of a big étale site and `k ≫ f = f' ≫ l` a commutative square
> ```
> X' --k--> X
> |         |
> f'        f
> v         v
> Y' --l--> Y
> ```
> with `f`, `f'` proper and `k`, `l` separated and locally quasi-finite. Let its base change by `b`
> be given by cartesian squares `X₁ = X ×_Y Y₁` (projections `a : X₁ ⟶ X`, `f₁ : X₁ ⟶ Y₁`),
> `Y'₁ = Y' ×_Y Y₁` (projections `b' : Y'₁ ⟶ Y'`, `l₁ : Y'₁ ⟶ Y₁`), `X'₁ = X' ×_{Y'} Y'₁`
> (projections `a' : X'₁ ⟶ X'`, `f'₁ : X'₁ ⟶ Y'₁`), and `k₁ : X'₁ ⟶ X₁` the induced morphism
> (`k₁ ≫ a = a' ≫ k`, `k₁ ≫ f₁ = f'₁ ≫ l₁`); the base-changed square inherits the hypotheses.
> For a ring `Λ`, right derived functors `Rf'_*`, `Rf_*`, `Rf'₁_*`, `Rf₁_*` of the direct images
> (with their units), and `K` in `D(X'_étale, Λ)`, the diagram
> ```
> b⁻¹ l_! Rf'_* K ⟶ l₁_! b'⁻¹ Rf'_* K ⟶ l₁_! Rf'₁_* a'⁻¹ K
>       |                                        |
> b⁻¹ Rf_* k_! K ⟶ Rf₁_* a⁻¹ k_! K  ⟶ Rf₁_* k₁_! a'⁻¹ K
> ```
> in `D(Y₁_étale, Λ)` commutes, where the vertical maps are those of [Stacks, Tag 0F7B]
> (`AlgebraicGeometry.SmallEtale.properBaseChangeMap`), and the horizontal maps are the base change
> maps of Étale Cohomology, Section 0EZQ (`AlgebraicGeometry.SmallEtale.etaleDerivedBaseChangeMap`)
> and the isomorphisms of [Stacks, Tag 0F55]
> (`AlgebraicGeometry.SmallEtale.derivedFShriekBaseChangeIso`). The original square is not required
> to be cartesian, and `Rf₁_*` may be any functor with a transformation from `f₁_*`.

```lean
theorem properBaseChangeMap_baseChange {X' X Y' Y X'₁ X₁ Y'₁ Y₁ : B.Scheme}
    (k : X' ⟶ X) (f' : X' ⟶ Y') (f : X ⟶ Y) (l : Y' ⟶ Y) (w : k ≫ f = f' ≫ l)
    (b : Y₁ ⟶ Y) (a : X₁ ⟶ X) (f₁ : X₁ ⟶ Y₁) (sqX : IsPullback a f₁ f b)
    (b' : Y'₁ ⟶ Y') (l₁ : Y'₁ ⟶ Y₁) (sqY : IsPullback b' l₁ l b)
    (a' : X'₁ ⟶ X') (f'₁ : X'₁ ⟶ Y'₁) (sqX' : IsPullback a' f'₁ f' b')
    (k₁ : X'₁ ⟶ X₁) (hk₁ : k₁ ≫ a = a' ≫ k) (w₁ : k₁ ≫ f₁ = f'₁ ≫ l₁)
    [IsProper (B.inclusion.map f')] [IsProper (B.inclusion.map f)]
    [IsSeparated (B.inclusion.map k)] [LocallyQuasiFinite (B.inclusion.map k)]
    [LocallyOfFiniteType (B.inclusion.map k)]
    [IsSeparated (B.inclusion.map l)] [LocallyQuasiFinite (B.inclusion.map l)]
    [LocallyOfFiniteType (B.inclusion.map l)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y' Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X'₁ Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B X₁ Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y'₁ Λ)]
    [HasDerivedCategory.{w} (ModuleSheaf.{u, u, u} B Y₁ Λ)]
    (RF' : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y' Λ))
    (αF' : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f')).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF')
    (RF : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y Λ))
    (αF : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF)
    (RF'₁ : DerivedCategory (ModuleSheaf.{u, u, u} B X'₁ Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y'₁ Λ))
    (αF'₁ : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f'₁)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF'₁)
    (RF₁ : DerivedCategory (ModuleSheaf.{u, u, u} B X₁ Λ) ⥤
      DerivedCategory (ModuleSheaf.{u, u, u} B Y₁ Λ))
    (αF₁ : (etaleModuleLift B Λ (etalePushforward.{u, u + 1} B f₁)).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶ DerivedCategory.Qh ⋙ RF₁)
    [RF'.IsRightDerivedFunctor αF'
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X' Λ) (ComplexShape.up ℤ))]
    [RF.IsRightDerivedFunctor αF
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X Λ) (ComplexShape.up ℤ))]
    [RF'₁.IsRightDerivedFunctor αF'₁
      (HomotopyCategory.quasiIso (ModuleSheaf.{u, u, u} B X'₁ Λ) (ComplexShape.up ℤ))]
    (K : DerivedCategory (ModuleSheaf.{u, u, u} B X' Λ)) :
    haveI := isProper_of_isPullback B a f₁ f b sqX
    haveI := isProper_of_isPullback B a' f'₁ f' b' sqX'
    haveI := isSeparated_of_isPullback B b' l₁ l b sqY
    haveI := locallyQuasiFinite_of_isPullback B b' l₁ l b sqY
    haveI := locallyOfFiniteType_of_isPullback B b' l₁ l b sqY
    haveI := isSeparated_of_isPullback B a' k₁ k a
      (isPullback_baseChange_left B w sqX sqY sqX' hk₁ w₁)
    haveI := locallyQuasiFinite_of_isPullback B a' k₁ k a
      (isPullback_baseChange_left B w sqX sqY sqX' hk₁ w₁)
    haveI := locallyOfFiniteType_of_isPullback B a' k₁ k a
      (isPullback_baseChange_left B w sqX sqY sqX' hk₁ w₁)
    (etaleModuleLift B Λ (abPullback.{u, u} B b)).mapDerivedCategory.map
        ((properBaseChangeMap B Λ k f' f l w RF' αF' RF αF).app K) ≫
      (etaleDerivedBaseChangeMap B Λ a f₁ f b sqX RF αF RF₁ αF₁).app
        ((etaleModuleLift B Λ (fShriekFunctor.{u, u} B k)).mapDerivedCategory.obj K) ≫
      RF₁.map ((derivedFShriekBaseChangeIso B Λ a' k₁ k a
        (isPullback_baseChange_left B w sqX sqY sqX' hk₁ w₁)).hom.app K) =
    (derivedFShriekBaseChangeIso B Λ b' l₁ l b sqY).hom.app (RF'.obj K) ≫
      (etaleModuleLift B Λ (fShriekFunctor.{u, u} B l₁)).mapDerivedCategory.map
        ((etaleDerivedBaseChangeMap B Λ a' f'₁ f' b' sqX' RF' αF' RF'₁ αF'₁).app K) ≫
      (properBaseChangeMap B Λ k₁ f'₁ f₁ l₁ w₁ RF'₁ αF'₁ RF₁ αF₁).app
        ((etaleModuleLift B Λ (abPullback.{u, u} B a')).mapDerivedCategory.obj K)
```

## Tag 0F7G, a lemma

[Tag 0F7G](https://stacks.math.columbia.edu/tag/0F7G) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.isIso_lowerShriekProperDirectImageMap_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/LowerShriekProperDirectImageComparison.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/LowerShriekProperDirectImageComparison.lean#L224).

> **[Stacks, Tag 0F7G].** Consider a commutative diagram of schemes `f ≫ h = g` (that is,
> `g = h ∘ f`, with `f : X ⟶ Y`, `h : Y ⟶ Z` and `g : X ⟶ Z`) with `f` and `g` locally
> quasi-finite and `h` proper. Let `Λ` be a ring. Functorially in `K ∈ D(X_étale, Λ)` there is a
> canonical map `g_! K ⟶ Rh_*(f_! K)` in `D(Z_étale, Λ)`, namely
> `AlgebraicGeometry.SmallEtale.lowerShriekProperDirectImageMap` (a natural transformation, for
> any right derived functor `Rh_*` of the direct image). This map is an isomorphism if
>
> * (a) `K` is bounded below and has torsion cohomology sheaves, or
> * (b) `Λ` is a torsion ring.
>
> Case (a) is `isIso_lowerShriekProperDirectImageMap_app_of_isGE`, case (b)
> `isIso_lowerShriekProperDirectImageMap_of_natCast_eq_zero`.

```lean
theorem isIso_lowerShriekProperDirectImageMap_app
    (K : DerivedCategory (ModuleSheaf.{u, u, u} B X Λ))
    (hK : (∃ n : ℤ, K.IsGE n ∧ moduleTorsionCohomologyProperty.{u, u, w, u} B X Λ K) ∨
      ∃ m : ℕ, 0 < m ∧ (m : Λ) = 0) :
    IsIso ((lowerShriekProperDirectImageMap B Λ f h g w RH αH).app K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 63.8, Tag 0F7A](https://stacks.math.columbia.edu/tag/0F7A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
