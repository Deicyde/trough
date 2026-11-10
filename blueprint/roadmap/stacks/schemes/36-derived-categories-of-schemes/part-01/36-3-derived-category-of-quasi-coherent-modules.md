---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparison, Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparisonCommShift, Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparisonIsTriangulated, AlgebraicGeometry.hasCoproducts_quasicoherentDerivedCategory, AlgebraicGeometry.cohomology_isLimit_of_isDerivedLimit_of_epi, AlgebraicGeometry.isDerivedLimit_single_limit_homology, AlgebraicGeometry.isZero_cohomology_limit_homology_of_isAffineOpen, AlgebraicGeometry.isIso_to_isDerivedLimit_truncGETower
statement: formalized
proof: formalized
---

# 36.3 Derived category of quasi-coherent modules

Section 36.3 of the Stacks Project, [Tag 06YZ](https://stacks.math.columbia.edu/tag/06YZ). 10 tags here are carried by 47 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06VT, an equation

[Tag 06VT](https://stacks.math.columbia.edu/tag/06VT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/WeakSerre/DerivedComparison.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/WeakSerre/DerivedComparison.lean#L122). The attribute's comment: “comparison functor”.

> **Stacks 06VT.** The canonical comparison functor `D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` from the
> derived category of quasi-coherent `𝒪_X`-modules to the complexes of `𝒪_X`-modules with
> quasi-coherent cohomology: the derived functor of the exact inclusion, factored through
> `D_QCoh(𝒪_X)`.

```lean
def derivedQuasicoherentComparison :
    DerivedCategory (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (SheafOfModules.isQuasicoherent X.ringCatSheaf)).FullSubcategory
```

**`Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparisonCommShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/WeakSerre/DerivedComparison.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/WeakSerre/DerivedComparison.lean#L132). The attribute's comment: “shift compatibility”.

> **Stacks 06VT.** The comparison functor is compatible with translation of complexes.

```lean
instance derivedQuasicoherentComparisonCommShift :
    (derivedQuasicoherentComparison.{w} X).CommShift ℤ
```

**`Stacks.AlgebraicGeometry.QuasicoherentDerived.derivedQuasicoherentComparisonIsTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/WeakSerre/DerivedComparison.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/WeakSerre/DerivedComparison.lean#L141). The attribute's comment: “exactness”.

> **Stacks 06VT.** The comparison functor preserves distinguished triangles, so it is an exact
> functor of triangulated categories.

```lean
instance derivedQuasicoherentComparisonIsTriangulated :
    (derivedQuasicoherentComparison.{w} X).IsTriangulated
```

## Tag 08DT, a lemma

[Tag 08DT](https://stacks.math.columbia.edu/tag/08DT) in the Stacks Project.

**`AlgebraicGeometry.hasCoproducts_quasicoherentDerivedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/DirectSums.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/DirectSums.lean#L121).

> The derived category of `𝒪_X`-modules with quasi-coherent cohomology has direct sums.

```lean
instance hasCoproducts_quasicoherentDerivedCategory (X : Scheme.{u}) :
    HasCoproducts.{u} (QuasicoherentDerivedCategory X)
```

## Tag 0A0J, a lemma

[Tag 0A0J](https://stacks.math.columbia.edu/tag/0A0J) in the Stacks Project.

**`AlgebraicGeometry.cohomology_isLimit_of_isDerivedLimit_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/DerivedLimitQuasiCoherent.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/DerivedLimitQuasiCoherent.lean#L166). The attribute's comment: “cohomology_limit”.

> **Stacks Project, Tag 0A0J.** The degree-`q` cohomology sheaf of a derived inverse limit of
> a tower with quasi-coherent cohomology and surjective transition maps on cohomology is the
> ordinary inverse limit of the degree-`q` cohomology sheaves.

```lean
public theorem cohomology_isLimit_of_isDerivedLimit_of_epi
    (X : Scheme.{u})
    (K : ℕᵒᵖ ⥤ DerivedCategory.{u + 1} X.Modules)
    (L : DerivedCategory.{u + 1} X.Modules)
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p
        (Pi.lift fun n : ℕ ↦
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
            Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
              K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory X.Modules))
    (hqc : ∀ (n : ℕ) (q : ℤ),
      ((DerivedCategory.homologyFunctor X.Modules q).obj (K.obj ⟨n⟩)).IsQuasicoherent)
    (hsurj : ∀ (n : ℕ) (q : ℤ),
      Epi ((DerivedCategory.homologyFunctor X.Modules q).map
        (K.map (homOfLE (Nat.le_succ n)).op)))
    (q : ℤ) :
    ∃ τ : (Functor.const ℕᵒᵖ).obj
        ((DerivedCategory.homologyFunctor X.Modules q).obj L) ⟶
        K ⋙ DerivedCategory.homologyFunctor X.Modules q,
      (∀ n : ℕ, τ.app ⟨n⟩ =
        (DerivedCategory.homologyFunctor X.Modules q).map
          (p ≫ Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n)) ∧
      Nonempty (IsLimit (Cone.mk _ τ))
```

**`AlgebraicGeometry.isDerivedLimit_single_limit_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/DerivedLimitQuasiCoherent.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/DerivedLimitQuasiCoherent.lean#L271). The attribute's comment: “derived_limit_sheaves”.

> **Stacks Project, Tag 0A0J.** For a tower with quasi-coherent cohomology and surjective
> transition maps on cohomology, the ordinary inverse limit of each tower of cohomology sheaves,
> placed in degree zero, is its derived inverse limit.

```lean
public theorem isDerivedLimit_single_limit_homology
    (X : Scheme.{u})
    (K : ℕᵒᵖ ⥤ DerivedCategory.{u + 1} X.Modules)
    (hqc : ∀ (n : ℕ) (q : ℤ),
      ((DerivedCategory.homologyFunctor X.Modules q).obj (K.obj ⟨n⟩)).IsQuasicoherent)
    (hsurj : ∀ (n : ℕ) (q : ℤ),
      Epi ((DerivedCategory.homologyFunctor X.Modules q).map
        (K.map (homOfLE (Nat.le_succ n)).op)))
    (q : ℤ) :
    let F := K ⋙ DerivedCategory.homologyFunctor X.Modules q
    ∃ h : HasProduct (fun n : ℕ =>
        (F ⋙ DerivedCategory.singleFunctor X.Modules 0).obj ⟨n⟩),
      @IsDerivedLimit (DerivedCategory X.Modules) _ _ _ _ _ _
        (F ⋙ DerivedCategory.singleFunctor X.Modules 0) h
        ((DerivedCategory.singleFunctor X.Modules 0).obj (limit F))
```

**`AlgebraicGeometry.isZero_cohomology_limit_homology_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/DerivedLimitQuasiCoherent.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/DerivedLimitQuasiCoherent.lean#L295). The attribute's comment: “affine_limit_acyclic”.

> **Stacks Project, Tag 0A0J.** The inverse limit of a degreewise-surjective tower of
> quasi-coherent cohomology sheaves has no higher cohomology on an affine open.

```lean
public theorem isZero_cohomology_limit_homology_of_isAffineOpen
    (X : Scheme.{u})
    (K : ℕᵒᵖ ⥤ DerivedCategory.{u + 1} X.Modules)
    (hqc : ∀ (n : ℕ) (q : ℤ),
      ((DerivedCategory.homologyFunctor X.Modules q).obj (K.obj ⟨n⟩)).IsQuasicoherent)
    (hsurj : ∀ (n : ℕ) (q : ℤ),
      Epi ((DerivedCategory.homologyFunctor X.Modules q).map
        (K.map (homOfLE (Nat.le_succ n)).op)))
    (U : X.Opens) (hU : IsAffineOpen U) (q : ℤ) (p : ℕ) (hp : 0 < p) :
    let F : ℕᵒᵖ ⥤ X.Modules := K ⋙ DerivedCategory.homologyFunctor X.Modules q
    let h : HasLimit F := inferInstance
    IsZero (Hgroup X.ringCatSheaf U p (@limit _ _ _ _ F h))
```

## Tag 08D3, a lemma

[Tag 08D3](https://stacks.math.columbia.edu/tag/08D3) in the Stacks Project.

**`AlgebraicGeometry.isIso_to_isDerivedLimit_truncGETower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/SpaltensteinCriterion/QuasicoherentTruncationConvergence.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/SpaltensteinCriterion/QuasicoherentTruncationConvergence.lean#L87).

> **Stacks 08D3.** A complex of `𝒪_X`-modules on a scheme whose cohomology sheaves are all
> quasi-coherent is canonically isomorphic to the derived inverse limit of the tower of its
> canonical lower truncations `n ↦ τ_{≥ -n} E`.
>
> The derived limit is presented by a distinguished triangle whose second map is the canonical
> difference of the projections, and the map `c` is pinned down by the requirement that its
> composites with the projections are the canonical truncation maps; the conclusion is that this
> map is invertible.

```lean
theorem isIso_to_isDerivedLimit_truncGETower
    (E : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} X.ringCatSheaf) i).obj E).IsQuasicoherent)
    [HasProduct fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} X.ringCatSheaf) E).obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf)) (c : E ⟶ L)
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} X.ringCatSheaf) E).obj ⟨n⟩)
    (δ : (∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} X.ringCatSheaf) E).obj ⟨n⟩) ⟶
      L⟦(1 : ℤ)⟧)
    (hL : Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
          (SheafOfModules.{u} X.ringCatSheaf) E).obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
            (SheafOfModules.{u} X.ringCatSheaf) E).obj ⟨n⟩) (n + 1) ≫
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{u} X.ringCatSheaf) E).map
              (homOfLE (Nat.le_succ n)).op) δ ∈
      distTriang (DerivedCategory (SheafOfModules.{u} X.ringCatSheaf)))
    (hc : ∀ n : ℕ, c ≫ p ≫ Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower
        (SheafOfModules.{u} X.ringCatSheaf) E).obj ⟨n⟩) n =
      (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

**`AlgebraicGeometry.isIso_of_isDerivedLimit_truncGETower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TotalDirectImage/TruncationTower.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TotalDirectImage/TruncationTower.lean#L102).

> Let `X` be a scheme and let `E` be an object of `D(𝒪_X)` whose cohomology sheaves are all
> quasi-coherent. Then the canonical map from `E` to a derived limit `L` of the tower
> `n ↦ τ_{≥ -n} E` of canonical truncations from below is an isomorphism.
>
> The derived limit is presented by its structural morphism `p` to the product of the tower and the
> distinguished triangle `hL` characterising it; the map `c` out of `E` is the canonical one because
> its composites with the product projections are required to be the truncation maps.

```lean
theorem isIso_of_isDerivedLimit_truncGETower
    (E : DerivedCategory X.Modules)
    (hE : ∀ q : ℤ, ((DerivedCategory.homologyFunctor X.Modules q).obj E).IsQuasicoherent)
    [HasProduct fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower X.Modules E).obj ⟨n⟩]
    (L : DerivedCategory X.Modules) (c : E ⟶ L)
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower X.Modules E).obj ⟨n⟩)
    (δ : (∏ᶜ fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower X.Modules E).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧)
    (hL : Triangle.mk p (Pi.lift fun n : ℕ ↦
      Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower X.Modules E).obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower X.Modules E).obj ⟨n⟩) (n + 1) ≫
          (Stacks.DerivedLimit.truncGETower X.Modules E).map
            (homOfLE (Nat.le_succ n)).op) δ ∈ distTriang (DerivedCategory X.Modules))
    (hc : ∀ n : ℕ, c ≫ p ≫
      Pi.π (fun n : ℕ ↦ (Stacks.DerivedLimit.truncGETower X.Modules E).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 08D4, a lemma

[Tag 08D4](https://stacks.math.columbia.edu/tag/08D4) in the Stacks Project.

**`Stacks.QuasicoherentAmplitude.isGE_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean, line 481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean#L481). The attribute's comment: “part (3), lower bound”.

> **[Stacks, Tag 08D4] part (3), lower bound.** A total right derived functor preserves a lower
> cohomological bound on a complex with quasi-coherent cohomology.
>
> No product hypothesis on `F` and no vanishing hypothesis are needed: the K-injective complexes
> compute any total right derived functor out of a Grothendieck abelian category, and a bounded
> below object is represented by a K-injective complex in the same range.

```lean
theorem isGE_obj {B : Type*} [Category* B] [Abelian B] [HasDerivedCategory B]
    (X : Scheme.{u})
    (F : X.Modules ⥤ B) [F.Additive]
    (RF : DerivedCategory X.Modules ⥤ DerivedCategory B)
    (alpha : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor alpha
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))]
    (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ,
      ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (a : ℤ) (hE : E.IsGE a) : (RF.obj E).IsGE a
```

**`Stacks.QuasicoherentAmplitude.isLE_obj_of_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean#L504). The attribute's comment: “part (3), upper bound”.

> **[Stacks, Tag 08D4] part (3), upper bound.** If the higher derived functors vanish from degree
> `N` onward on quasi-coherent modules, a total right derived functor shifts an upper cohomological
> bound by at most `N - 1`.

```lean
theorem isLE_obj_of_isZero {B : Type*} [Category* B] [Abelian B]
    [HasDerivedCategory B] [HasProductsOfShape ℕ B] [HasExactLimitsOfShape (Discrete ℕ) B]
    (X : Scheme.{u})
    (F : X.Modules ⥤ B) [F.Additive]
    [PreservesLimitsOfShape (Discrete ℕ) F]
    (RF : DerivedCategory X.Modules ⥤ DerivedCategory B)
    (alpha : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor alpha
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))]
    (N : ℕ)
    (hRF : ∀ (M : X.Modules), M.IsQuasicoherent → ∀ (p : ℤ), (N : ℤ) ≤ p →
      IsZero ((F.rightDerivedPlus p).obj M))
    (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ,
      ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (b : ℤ) (hE : E.IsLE b) : (RF.obj E).IsLE (b + (N : ℤ) - 1)
```

**`Stacks.QuasicoherentAmplitude.isIso_homology_map_truncLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean#L530). The attribute's comment: “part (1)”.

> **[Stacks, Tag 08D4] part (1).** A total right derived functor agrees in degrees at most `a` on
> a complex with quasi-coherent cohomology and its canonical truncation in degrees at most `a`.
>
> The third vertex of the truncation triangle at `a` is `≥ a + 1`, so by part (3) lower bound its
> image under `RF` has no cohomology in degrees `i` and `i - 1` for `i ≤ a`, and the long exact
> sequence makes the comparison both mono and epi.

```lean
theorem isIso_homology_map_truncLE {B : Type*} [Category* B] [Abelian B]
    [HasDerivedCategory B]
    (X : Scheme.{u})
    (F : X.Modules ⥤ B) [F.Additive]
    (RF : DerivedCategory X.Modules ⥤ DerivedCategory B)
    (alpha : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor alpha
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))]
    (E : DerivedCategory X.Modules)
    (hE : ∀ j : ℤ,
      ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (a i : ℤ) (hi : i ≤ a) :
    IsIso ((DerivedCategory.homologyFunctor B i).map
      (RF.map ((DerivedCategory.TStructure.t.truncLEι a).app E)))
```

**`Stacks.QuasicoherentAmplitude.isIso_homology_map_truncGE_of_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/QuasicoherentAmplitude.lean#L572). The attribute's comment: “part (2)”.

> **[Stacks, Tag 08D4] part (2).** If the higher derived functors vanish from degree `N` onward
> on quasi-coherent modules, then in degrees at least `b` a total right derived functor agrees on a
> complex with quasi-coherent cohomology and its canonical truncation in degrees at least
> `b - N + 1`.
>
> The first vertex of the truncation triangle at `a = b - N + 1` is `≤ a - 1`, so by part (3) upper
> bound its image under `RF` is `≤ a - 1 + N - 1 = b - 1`, hence has no cohomology in degrees `i`
> and `i + 1` for `i ≥ b`.

```lean
theorem isIso_homology_map_truncGE_of_isZero {B : Type*} [Category* B] [Abelian B]
    [HasDerivedCategory B] [HasProductsOfShape ℕ B] [HasExactLimitsOfShape (Discrete ℕ) B]
    (X : Scheme.{u})
    (F : X.Modules ⥤ B) [F.Additive]
    [PreservesLimitsOfShape (Discrete ℕ) F]
    (RF : DerivedCategory X.Modules ⥤ DerivedCategory B)
    (alpha : F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh ⟶
      DerivedCategory.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor alpha
      (HomotopyCategory.quasiIso X.Modules (ComplexShape.up ℤ))]
    (N : ℕ)
    (hRF : ∀ (M : X.Modules), M.IsQuasicoherent → ∀ (p : ℤ), (N : ℤ) ≤ p →
      IsZero ((F.rightDerivedPlus p).obj M))
    (E : DerivedCategory X.Modules)
    (hE : ∀ j : ℤ,
      ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (b i : ℤ) (hi : b ≤ i) :
    IsIso ((DerivedCategory.homologyFunctor B i).map
      (RF.map ((DerivedCategory.TStructure.t.truncGEπ (b - (N : ℤ) + 1)).app E)))
```

**`AlgebraicGeometry.isGE_rightDerivedFunctor_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/DerivedBounds.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/DerivedBounds.lean#L102). The attribute's comment: “part (3), lower bound”.

> A total right derived functor of an additive functor out of the `𝒪_X`-modules of a scheme
> preserves the lower end of the range of degrees in which an object with quasi-coherent cohomology
> lives.

```lean
theorem isGE_rightDerivedFunctor_obj
    (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ,
      ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (a : ℤ) (hE : E.IsGE a) : (RF.obj E).IsGE a
```

**`AlgebraicGeometry.isIso_homologyFunctor_map_rightDerivedFunctor_truncLEι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/DerivedBounds.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/DerivedBounds.lean#L116). The attribute's comment: “part (1)”.

> A total right derived functor of an additive functor out of the `𝒪_X`-modules of a scheme
> agrees in degrees at most `a` on an object with quasi-coherent cohomology and on its canonical
> truncation in degrees at most `a`.

```lean
theorem isIso_homologyFunctor_map_rightDerivedFunctor_truncLEι
    (E : DerivedCategory X.Modules)
    (hE : ∀ j : ℤ,
      ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (a i : ℤ) (hi : i ≤ a) :
    IsIso ((DerivedCategory.homologyFunctor B i).map
      (RF.map ((DerivedCategory.TStructure.t.truncLEι a).app E)))
```

**`AlgebraicGeometry.isLE_rightDerivedFunctor_obj_of_isZero_rightDerivedPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/UpperBounds.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/UpperBounds.lean#L531). The attribute's comment: “part (3), upper bound”.

> **Stacks Project, Tag 08D4, part (3), the upper bound.** Let `X` be a scheme, let `F` be an
> additive functor out of the `𝒪_X`-modules which preserves countable products, and let `RF` be a
> total right derived functor of `F` on `D(𝒪_X)`. Suppose the higher right derived functors `R^pF`
> vanish on every quasi-coherent module in every degree `p ≥ N`. If an object `E` of `D(𝒪_X)` has
> quasi-coherent cohomology sheaves and lives in degrees `≤ b`, then `RF(E)` lives in degrees
> `≤ b + N - 1`.
>
> The canonical truncation triangle `τ_{≤ b-1}E ⟶ E ⟶ τ_{≥ b}E` reduces the claim to its third
> vertex, concentrated in degree `b` and so covered by the vanishing hypothesis, and to its first
> vertex, where the bound `b - 1 + N` — one worse, which is why the triangle is used — is supplied
> by the `E = R\lim \tau_{\geq -n}E` argument: `E` is the derived limit of its truncations from
> below ([Stacks, Tag 08D3]), `RF` carries that derived limit to a derived limit
> ([Stacks, Tag 08U1]), each `RF(τ_{≥ -n}E)` lives in degrees `≤ b + N - 1` because `τ_{≥ -n}E` is
> bounded, and a derived limit of such a tower lives in degrees `≤ b + N`.

```lean
theorem isLE_rightDerivedFunctor_obj_of_isZero_rightDerivedPlus (N : ℕ)
    (hRF : ∀ M : SheafOfModules.{u} X.ringCatSheaf, M.IsQuasicoherent →
      ∀ p : ℤ, (N : ℤ) ≤ p → IsZero ((F.rightDerivedPlus p).obj M))
    (E : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} X.ringCatSheaf) i).obj E).IsQuasicoherent)
    (b : ℤ) (hE : E.IsLE b) : (RF.obj E).IsLE (b + (N : ℤ) - 1)
```

**`AlgebraicGeometry.isIso_homologyFunctor_map_rightDerivedFunctor_truncGEπ_of_isZero_rightDerivedPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/UpperBounds.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/AffineVanishing/UpperBounds.lean#L606). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 08D4, part (2).** In the situation of
> `AlgebraicGeometry.isLE_rightDerivedFunctor_obj_of_isZero_rightDerivedPlus`, the canonical
> comparison
> `H^i(RF(E)) ⟶ H^i(RF(τ_{≥ b - N + 1}E))` is an isomorphism for every `i ≥ b`.
>
> Write `a = b - N + 1`. The canonical truncation triangle
> `τ_{≤ a-1}E ⟶ E ⟶ τ_{≥ a}E` goes to a distinguished triangle under `RF`, which is exact; its
> first vertex has `RF`-image in degrees `≤ a - 1 + N - 1 = b - 1` by part (3), so `H^i` and
> `H^{i+1}` vanish there for `i ≥ b`, and the long exact homology sequence makes the second map
> invertible on `H^i`.

```lean
theorem isIso_homologyFunctor_map_rightDerivedFunctor_truncGEπ_of_isZero_rightDerivedPlus
    (N : ℕ)
    (hRF : ∀ M : SheafOfModules.{u} X.ringCatSheaf, M.IsQuasicoherent →
      ∀ p : ℤ, (N : ℤ) ≤ p → IsZero ((F.rightDerivedPlus p).obj M))
    (E : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hE : ∀ i : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} X.ringCatSheaf) i).obj E).IsQuasicoherent)
    (b i : ℤ) (hi : b ≤ i) :
    IsIso ((DerivedCategory.homologyFunctor B i).map
      (RF.map ((DerivedCategory.TStructure.t.truncGEπ (b - (N : ℤ) + 1)).app E)))
```

**`AlgebraicGeometry.isLE_rightDerivedFunctor_obj_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TotalDirectImage/DerivedUpperBound.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TotalDirectImage/DerivedUpperBound.lean#L298). The attribute's comment: “part (3), upper bound”.

> **Stacks 08D4, part (3), the upper bound.** Let `X` be a scheme, let `F` be an additive
> functor out of the `𝒪_X`-modules commuting with countable products, and let `(RF, alpha)` be a
> total right derived functor of `F` on `D(𝒪_X)`. If `R ᵖ F` vanishes on quasi-coherent modules for
> every `p ≥ N`, then `RF` carries an object with quasi-coherent cohomology lying in degrees `≤ b`
> to one lying in degrees `≤ b + N - 1`.
>
> The object is split by the truncation triangle at `b` into a part concentrated in degree `b` and a
> part in degrees `≤ b - 1`. The second is handled by the derived limit of its truncation tower:
> each stage is bounded, so the bounded statement applies with `N - 1`, [Stacks, Tag 08U1] carries
> the derived limit through `RF`, and the derived limit costs the one further degree.

```lean
theorem isLE_rightDerivedFunctor_obj_addCommGrpCat (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (b : ℤ) (hE : E.IsLE b) : (RF.obj E).IsLE (b + (N : ℤ) - 1)
```

**`AlgebraicGeometry.isIso_homologyFunctor_map_rightDerivedFunctor_truncGEπ_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TotalDirectImage/DerivedUpperBound.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TotalDirectImage/DerivedUpperBound.lean#L366). The attribute's comment: “part (2)”.

> **Stacks 08D4, part (2).** With the hypotheses of the upper bound, in degrees at least `b` a
> total right derived functor agrees on an object with quasi-coherent cohomology and on its
> canonical truncation in degrees at least `b - N + 1`.
>
> The truncation triangle at `a = b - N + 1` has first vertex in degrees `≤ a - 1`, so the upper
> bound puts its `RF`-image in degrees `≤ a - 1 + N - 1 = b - 1`; the long exact homology sequence
> then makes the second map invertible on `H^i` for every `i ≥ b`.

```lean
theorem isIso_homologyFunctor_map_rightDerivedFunctor_truncGEπ_addCommGrpCat
    (E : DerivedCategory X.Modules)
    (hcoh : ∀ j : ℤ, ((DerivedCategory.homologyFunctor X.Modules j).obj E).IsQuasicoherent)
    (b i : ℤ) (hi : b ≤ i) :
    IsIso ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).map
      (RF.map ((DerivedCategory.TStructure.t.truncGEπ (b - (N : ℤ) + 1)).app E)))
```

## Tag 06Z0, a lemma

[Tag 06Z0](https://stacks.math.columbia.edu/tag/06Z0) in the Stacks Project.

**`AlgebraicGeometry.isIso_derivedTildeGlobalSectionsAdjunction_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean#L130). The attribute's comment: “canonical unit isomorphism”.

> **The unit of the derived Spec–Γ adjunction is invertible.** For every object `M` of `D(R)`
> the canonical map `M ⟶ RΓ(Spec R, M^~)` is an isomorphism.
>
> This is `AlgebraicGeometry.isIso_derivedTildeGlobalSectionsAdjunction_unit_app_of_quasiIso` fed
> with unbounded affine vanishing for the complexes `M̃^•`, which is
> `AlgebraicGeometry.quasiIso_globalSectionsOver_map_tilde`.

```lean
theorem isIso_derivedTildeGlobalSectionsAdjunction_unit :
    IsIso (derivedTildeGlobalSectionsAdjunction R).val.unit
```

**`AlgebraicGeometry.derivedTilde_isEquivalence`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean#L233). The attribute's comment: “sheafification equivalence”.

> **Derived sheafification is an equivalence** `D(R) ≌ D_QCoh(𝒪_{Spec R})`. This is the
> remaining content of [Stacks, Tag 06Z0] for the two edges `~` and (06VT) of its triangle.
>
> Derived sheafification is exact and fully faithful, and its right adjoint, derived global
> sections, has zero kernel; by [Stacks, Tag 09J1] that is enough.

```lean
instance derivedTilde_isEquivalence : (derivedTilde R).IsEquivalence
```

**`AlgebraicGeometry.derivedGlobalSectionsQuasicoherent_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean#L242). The attribute's comment: “global sections equivalence”.

> **Unbounded derived global sections `D_QCoh(𝒪_{Spec R}) ⥤ D(R)` is an equivalence**, being
> right adjoint to the equivalence `AlgebraicGeometry.derivedTilde`. This is the `RΓ(X, -)` edge of
> the triangle of [Stacks, Tag 06Z0].

```lean
theorem derivedGlobalSectionsQuasicoherent_isEquivalence :
    (derivedGlobalSectionsQuasicoherent R).IsEquivalence
```

**`AlgebraicGeometry.isIso_derivedTildeGlobalSectionsAdjunction_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean#L258). The attribute's comment: “canonical counit isomorphism”.

> **The counit of the derived Spec–Γ adjunction is invertible on `D_QCoh(𝒪_{Spec R})`.** For
> every object `E` of `D(𝒪_{Spec R})` with quasi-coherent cohomology sheaves the canonical map
> `RΓ(Spec R, E)^~ ⟶ E` is an isomorphism.
>
> The left adjoint `derivedTilde R ⋙ ι` is fully faithful, the unit being invertible, so its counit
> is invertible exactly on its essential image; and `E` is in that essential image because derived
> sheafification is essentially surjective onto `D_QCoh(𝒪_{Spec R})`. The restriction to objects
> with quasi-coherent cohomology cannot be dropped: `RΓ(Spec R, E)^~ ⟶ E` fails to be invertible as
> soon as some cohomology sheaf of `E` is not quasi-coherent, which is why the adjunction itself is
> not an equivalence.

```lean
theorem isIso_derivedTildeGlobalSectionsAdjunction_counit_app
    (E : (DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
      (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).FullSubcategory) :
    IsIso ((derivedTildeGlobalSectionsAdjunction R).val.counit.app
      ((DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
        (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).ι.obj E))
```

**`Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedEquivalence.lean#L293). The attribute's comment: “comparison equivalence”.

> **The comparison functor of [Stacks, Tag 06VT] is an equivalence on an affine scheme.** The
> canonical functor `D(QCoh(𝒪_{Spec R})) ⥤ D_QCoh(𝒪_{Spec R})` is an equivalence of triangulated
> categories.
>
> This is the first assertion of [Stacks, Tag 08D9] part (3). It is
> `Stacks.DerivedQCoh.derivedTilde_isEquivalence_iff_comparison` applied to
> `AlgebraicGeometry.derivedTilde_isEquivalence`: the `~` edge of [Stacks, Tag 06Z0] is an
> equivalence of abelian categories, so the comparison functor is an equivalence exactly when
> derived sheafification is.

```lean
theorem derivedQuasicoherentComparison_isEquivalence (R : CommRingCat.{u}) :
    (derivedQuasicoherentComparison.{u} (Spec R)).IsEquivalence
```

**`AlgebraicGeometry.AffineDerivedSections.full_derivedSectionsLeftAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedSectionsLeftAdjoint.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedSectionsLeftAdjoint.lean#L212). The attribute's comment: “the left adjoint of derived global sections is fully faithful on an affine scheme”.

> **The left adjoint of `RΓ(S, -)` is full on an affine scheme**; see
> `derivedSectionsLeftAdjointFullyFaithful`.

```lean
instance full_derivedSectionsLeftAdjoint :
    (derivedBaseExtension S.toRingedSpace).Full
```

**`AlgebraicGeometry.AffineDerivedSections.faithful_derivedSectionsLeftAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedSectionsLeftAdjoint.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedSectionsLeftAdjoint.lean#L219). The attribute's comment: “the left adjoint of derived global sections is fully faithful on an affine scheme”.

> **The left adjoint of `RΓ(S, -)` is faithful on an affine scheme**; see
> `derivedSectionsLeftAdjointFullyFaithful`.

```lean
instance faithful_derivedSectionsLeftAdjoint :
    (derivedBaseExtension S.toRingedSpace).Faithful
```

**`AlgebraicGeometry.AffineDerivedSections.essImage_derivedSectionsLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedSectionsLeftAdjoint.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/AffineDerivedSectionsLeftAdjoint.lean#L235). The attribute's comment: “the essential image of that left adjoint is the quasi-coherent part”.

> **Every complex of `𝒪_S`-modules with quasi-coherent cohomology sheaves is in the essential
> image of the left adjoint of `RΓ(S, -)`,** `S` being affine. This is the predicate
> `AlgebraicGeometry.IsQCohAll` of the Künneth development, written out.
>
> Pulling `U` back along `S ≅ Spec Γ(S, 𝒪_S)` keeps the cohomology sheaves quasi-coherent, by
> [Stacks, Tag 08DW] part (1); over `Spec Γ(S, 𝒪_S)` the result is a derived sheafification by
> [Stacks, Tag 06Z0], `AlgebraicGeometry.StandardModel.exists_iso_mapDerivedCategory`; and pushing
> that back through `derivedSectionsLeftAdjointIso` and the round trip of the derived pullbacks
> along the two directions of the isomorphism exhibits `U` itself.

```lean
theorem essImage_derivedSectionsLeftAdjoint
    (U : DerivedCategory (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)))
    (hU : ∀ j : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)) j).obj U).IsQuasicoherent) :
    (derivedBaseExtension S.toRingedSpace).essImage U
```

**`Stacks.DerivedQCoh.derivedTildeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/Basic.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/Basic.lean#L164). The attribute's comment: “the tilde edge: D(A) ≌ D(QCoh(𝒪_X))”.

> **Stacks Project, Tag 06Z0 (the tilde edge).** For `X = Spec A` the functor `M ↦ M^~` is an
> equivalence of triangulated categories from `D(A)` to `D(QCoh(𝒪_X))`. This is the arrow labelled
> `~` in the triangle of Stacks 06Z0; the other two edges, the functor (06VT) and `RΓ(X, -)`, are
> not treated here.
>
> The underlying functor is `AlgebraicGeometry.tildeEquiv.functor.mapDerivedCategory`, by
> definition.

```lean
def derivedTildeEquiv : DerivedCategory (ModuleCat.{u} R) ≌
    DerivedCategory (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf).FullSubcategory
```

**`Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_isAffine_atModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/ComparisonAffine.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/ComparisonAffine.lean#L306). The attribute's comment: “comparison equivalence, any affine scheme at any model”.

> **[Stacks, Tag 06Z0].** For every affine scheme `X` the comparison functor
> `i_X : D(QCoh(𝒪_X)) ⥤ D_QCoh(𝒪_X)` of [Stacks, Tag 06VT] is an equivalence of triangulated
> categories, at every choice of the two derived categories.
>
> `Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence` is this statement for `Spec R`
> at the locally small model. An affine scheme is isomorphic to `Spec Γ(X, ⊤)` by
> `AlgebraicGeometry.Scheme.isoSpec`, and transporting along that isomorphism simultaneously changes
> the scheme and the model.
>
> `Stacks.DerivedQCoh.derivedQuasicoherentComparison_isEquivalence_of_isAffine` is this statement
> at the locally small model alone, that is the case `w = u`.

```lean
theorem derivedQuasicoherentComparison_isEquivalence_of_isAffine_atModel (X : Scheme.{u})
    [IsAffine X]
    [HasDerivedCategory.{w} (SheafOfModules.{u} X.ringCatSheaf)]
    [HasDerivedCategory.{w} (SheafOfModules.isQuasicoherent X.ringCatSheaf).FullSubcategory] :
    (derivedQuasicoherentComparison.{w} X).IsEquivalence
```

**`AlgebraicGeometry.derivedGlobalSectionsHomologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/DegreeZeroCohomology.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/DegreeZeroCohomology.lean#L486). The attribute's comment: “degree-zero cohomology”.

> **Stacks 06Z0, degree-zero cohomology.** On an affine scheme the degree-zero cohomology of
> derived global sections is the global sections of the degree-zero cohomology sheaf:
> `H⁰(RΓ(Spec R, E)) ≅ Γ(Spec R, H⁰(E))` for `E` in `D_QCoh(𝒪_{Spec R})`, naturally in `E`.
>
> This is `AlgebraicGeometry.derivedGlobalSectionsQuasicoherentCompHomologyIso` in degree zero. Its
> normalization on global cycles, which pins it down uniquely, is
> `AlgebraicGeometry.globalSectionsCyclesToHomology_comp_derivedGlobalSectionsHomologyZeroIso`.

```lean
def derivedGlobalSectionsHomologyZeroIso :
    derivedGlobalSectionsQuasicoherent R ⋙
        DerivedCategory.homologyFunctor (ModuleCat.{u} R) 0 ≅
      (DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
        (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).ι ⋙
        DerivedCategory.homologyFunctor (Spec R).Modules 0 ⋙
          globalSectionsOver (𝟙 (Spec R))
```

**`AlgebraicGeometry.globalSectionsCyclesToHomology_comp_derivedGlobalSectionsHomologyZeroIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedQCoh/DegreeZeroCohomology.lean, line 747](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedQCoh/DegreeZeroCohomology.lean#L747). The attribute's comment: “canonical degree-zero comparison”.

> **Stacks 06Z0, the canonical degree-zero comparison.** The degree-zero identification
> `H⁰(RΓ(Spec R, E)) ≅ Γ(Spec R, H⁰(E))` of
> `AlgebraicGeometry.derivedGlobalSectionsHomologyZeroIso` sends a global cycle of a complex `K`
> with quasi-coherent cohomology to its section of the degree-zero cohomology sheaf: the composite
> `Γ(Spec R, Z⁰(K)) ⟶ H⁰(Γ(Spec R, K)) ⟶ H⁰(RΓ(Spec R, Q K)) ⟶ Γ(Spec R, H⁰(Q K)) ⟶
> Γ(Spec R, H⁰(K))` is `Γ(Spec R, -)` applied to `K.homologyπ 0`.
>
> Together with naturality this characterizes the isomorphism:
> `AlgebraicGeometry.globalSectionsCyclesToHomology` is an epimorphism, being the isomorphism
> `Γ(Z⁰(K)) ≅ Z⁰(Γ(K))` followed by `HomologicalComplex.homologyπ`. The content is
> `AlgebraicGeometry.globalSectionsHomologyComparison_eq`.

```lean
theorem globalSectionsCyclesToHomology_comp_derivedGlobalSectionsHomologyZeroIso
    (K : CochainComplex (Spec R).Modules ℤ)
    (hK : (DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
      (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)) (DerivedCategory.Q.obj K)) :
    globalSectionsCyclesToHomology (𝟙 (Spec R)) K 0 ≫
        (DerivedCategory.homologyFunctorFactors (ModuleCat.{u} R) 0).inv.app
          (((globalSectionsOver (𝟙 (Spec R))).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj K) ≫
        (DerivedCategory.homologyFunctor (ModuleCat.{u} R) 0).map
          (globalSectionsComplexComparison (𝟙 (Spec R)) K) ≫
        (derivedGlobalSectionsHomologyZeroIso R).hom.app ⟨DerivedCategory.Q.obj K, hK⟩ ≫
        (globalSectionsOver (𝟙 (Spec R))).map
          ((DerivedCategory.homologyFunctorFactors (Spec R).Modules 0).hom.app K) =
      (globalSectionsOver (𝟙 (Spec R))).map (K.homologyπ 0)
```

**`AlgebraicGeometry.derivedTildeGlobalSectionsAdjunction_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedTildeCounit.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedTildeCounit.lean#L285). The attribute's comment: “canonical counit isomorphism”.

> **Stacks 06Z0, the counit clause.** On an affine scheme the counit of the canonical derived
> sheafification–sections adjunction is invertible at every object of `D_QCoh(𝒪_{Spec R})`: derived
> sheafification recovers a complex with quasi-coherent cohomology from its derived global
> sections.

```lean
theorem derivedTildeGlobalSectionsAdjunction_counit_isIso (R : CommRingCat.{u})
    [HasDerivedCategory.{w₂} (ModuleCat.{u} R)] :
    let _inst : HasDerivedCategory (Spec R).Modules := HasDerivedCategory.standard _
    ∀ E : (DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
      (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).FullSubcategory,
      IsIso ((derivedTildeGlobalSectionsAdjunction R).val.counit.app
        ((DerivedCategoryB.derivedCategoryB (A := (Spec R).Modules)
          (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)).ι.obj E))
```

## Tag 08DV, a lemma

[Tag 08DV](https://stacks.math.columbia.edu/tag/08DV) in the Stacks Project.

**`AlgebraicGeometry.kFlat_tilde`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/TildeKFlat.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/TildeKFlat.lean#L330).

> **Stacks Project, Tag 08DV.** If `K` is a K-flat complex of `A`-modules, then `K̃` is a
> K-flat complex of `𝒪_{Spec A}`-modules.
>
> By the stalk criterion for K-flatness (Stacks 06YB) it suffices that the stalk complex of `K̃`
> at every point `x` be K-flat over the stalk ring. That stalk complex is the extension of
> scalars of `K` along `A → 𝒪_{Spec A, x}` (`tildeStalkComplexIso`), and extension of scalars
> preserves K-flatness (Stacks 06Y1).

```lean
theorem kFlat_tilde (K : CochainComplex (ModuleCat.{u} A) ℤ)
    (hK : CochainComplex.KFlat.{u, u} K) :
    Stacks.SheafOfModules.IsKFlat (specCommRingSheaf A) (tildeComplexMod K)
```

## Tag 0DJK, a lemma

[Tag 0DJK](https://stacks.math.columbia.edu/tag/0DJK) in the Stacks Project.

**`AlgebraicGeometry.affineDerivedPushforward_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedTildePushforward.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedTildePushforward.lean#L88). The attribute's comment: “pushforward route”.

> **Stacks Project, Tag 0DJK.** Derived direct image under a morphism of affine schemes
> preserves quasi-coherent cohomology.

```lean
public theorem affineDerivedPushforward_isQuasicoherent
    (R S : CommRingCat.{u}) (φ : R ⟶ S)
    (Rf : DerivedCategory (Spec S).Modules ⥤ DerivedCategory (Spec R).Modules)
    (α : (Scheme.Modules.pushforward (Spec.map φ)).mapHomologicalComplex (.up ℤ) ⋙
        DerivedCategory.Q ⟶ DerivedCategory.Q ⋙ Rf)
    [Rf.IsRightDerivedFunctor α
      (HomologicalComplex.quasiIso (Spec S).Modules (.up ℤ))]
    (K : QuasicoherentDerivedCategory (Spec S)) :
    DerivedCategoryB.derivedCategoryB
      (SheafOfModules.isQuasicoherent (Spec R).ringCatSheaf)
      (Rf.obj K.obj)
```

**`AlgebraicGeometry.affineDerivedPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedTildePushforward.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/Coherator/AffineDerivedTildePushforward.lean#L122). The attribute's comment: “commutativity”.

> **Stacks Project, Tag 0DJK.** The affine associated-sheaf/derived-pushforward square
> commutes naturally: derived direct image corresponds to restriction of scalars.

```lean
public noncomputable def affineDerivedPushforwardIso
    (R S : CommRingCat.{u}) (φ : R ⟶ S)
    (Rf : DerivedCategory (Spec S).Modules ⥤ DerivedCategory (Spec R).Modules)
    (α : (Scheme.Modules.pushforward (Spec.map φ)).mapHomologicalComplex (.up ℤ) ⋙
        DerivedCategory.Q ⟶ DerivedCategory.Q ⋙ Rf)
    [Rf.IsRightDerivedFunctor α
      (HomologicalComplex.quasiIso (Spec S).Modules (.up ℤ))] :
    affineTildeQuasicoherent S ⋙ affineDerivedPushforwardQuasicoherent R S φ Rf α ≅
      (ModuleCat.restrictScalars φ.hom).mapDerivedCategory ⋙ affineTildeQuasicoherent R
```

**`AlgebraicGeometry.derivedTildeCompDerivedQuasicoherentPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Coherator/AffineDerivedPushforward.lean#L424).

> **Stacks 0DJK.** Let `φ : R ⟶ S` and let `f = Spec φ : Spec S ⟶ Spec R`. Then the square
> `D(S) ⟶ D_QCoh(𝒪_{Spec S}) ⟶^{Rf_*} D_QCoh(𝒪_{Spec R})`,
> `D(S) ⟶^{restriction of scalars} D(R) ⟶ D_QCoh(𝒪_{Spec R})`
> commutes: derived direct image along a morphism of affine schemes corresponds, under derived
> sheafification, to derived restriction of scalars.
>
> This is `AlgebraicGeometry.derivedTildeCompIso_of_comparisonSquare` with its hypothesis `hsq`
> discharged by `AlgebraicGeometry.derivedQuasicoherentComparisonSquare`, the commuting square of
> [Stacks, Tag 08D7]. It is also the first assertion of [Stacks, Tag 0A9F].

```lean
public def derivedTildeCompDerivedQuasicoherentPushforwardIso :
    derivedTilde S ⋙ derivedQuasicoherentPushforward (Spec.map φ) ≅
      (ModuleCat.restrictScalars φ.hom).mapDerivedCategory ⋙ derivedTilde R
```

## Tag 08DW, a lemma

[Tag 08DW](https://stacks.math.columbia.edu/tag/08DW) in the Stacks Project.

**`AlgebraicGeometry.affineSchemePullbackComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineSchemePullbackComparison.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineSchemePullbackComparison.lean#L92). The attribute's comment: “part (2) for a morphism of arbitrary affine schemes”.

> **[Stacks, Tag 08DW] part (2) for a morphism of arbitrary affine schemes.** Let `g : Y ⟶ X` be
> a morphism of affine schemes, given by the ring map `g.appTop : Γ(X, ⊤) ⟶ Γ(Y, ⊤)`. Then the
> square
>
>   `D(Γ(X, ⊤)) ⟶ D(𝒪_X)`, `D(Γ(Y, ⊤)) ⟶ D(𝒪_Y)`, `- ⊗ᴸ Γ(Y, ⊤)` on the left and `Lg^*` on the
>   right,
>
> commutes: `Lg^*` of the complex of sheaves associated to an object of `D(Γ(X, ⊤))` is the complex
> of sheaves associated to its derived extension of scalars.
>
> This is `AlgebraicGeometry.affinePullbackComparison` conjugated by the two canonical isomorphisms
> `X ≅ Spec Γ(X, ⊤)` and `Y ≅ Spec Γ(Y, ⊤)`, the composition formula
> `Stacks.Duality.derivedPullbackCompIso` crossing the resulting two triangles.

```lean
def affineSchemePullbackComparison {X Y : Scheme.{u}} [IsAffine X] [IsAffine Y] (g : Y ⟶ X) :
    affineSchemeDerivedTilde X ⋙ Stacks.Duality.derivedPullback g ≅
      (CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{u, u, u}
          (CommRingCat.Hom.hom g.appTop)).functor ⋙
        affineSchemeDerivedTilde Y
```

**`Stacks.Duality.isQuasicoherent_homology_derivedPullback'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean#L422). The attribute's comment: “part (1): derived pullback preserves quasi-coherence of cohomology”.

> **[Stacks, Tag 08DW] part (1): `Lf^*` sends `D_QCoh(𝒪_Y)` into `D_QCoh(𝒪_X)`.** For an
> arbitrary morphism of schemes `f : X ⟶ Y` and a complex `K` of `𝒪_Y`-modules all of whose
> cohomology sheaves are quasi-coherent, every cohomology sheaf of `Lf^*K` is quasi-coherent.
>
> This is `Stacks.Duality.isQuasicoherent_homology_derivedPullback`, with `hess` found by instance
> search from `AlgebraicGeometry.derivedTilde_isEquivalence`.

```lean
theorem isQuasicoherent_homology_derivedPullback' {X Y : Scheme.{u}} (f : X ⟶ Y)
    (K : quasiCoherentDerivedCategory Y) (i : ℤ) :
    ((DerivedCategory.homologyFunctor X.Modules i).obj
      ((derivedPullback f).obj K.obj)).IsQuasicoherent
```

**`Stacks.Duality.quasiCoherentDerivedPullback'`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean#L435). The attribute's comment: “part (1): the restriction D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X) of derived pullback”.

> **[Stacks, Tag 08DW] part (1), as a functor.** Derived pullback along a morphism of schemes
> restricts to a functor `D_QCoh(𝒪_Y) ⥤ D_QCoh(𝒪_X)` between the derived categories of complexes
> with quasi-coherent cohomology.
>
> This is `Stacks.Duality.quasiCoherentDerivedPullback` at
> `Stacks.Duality.isQuasicoherent_homology_derivedPullback'`.

```lean
abbrev quasiCoherentDerivedPullback' {X Y : Scheme.{u}} (f : X ⟶ Y) :
    quasiCoherentDerivedCategory Y ⥤ quasiCoherentDerivedCategory X
```

**`Stacks.Duality.isQuasicoherent_homology_derivedPullback_anyModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean, line 479](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean#L479). The attribute's comment: “part (1) at an arbitrary model of the two derived categories”.

> **[Stacks, Tag 08DW] part (1) at an arbitrary model of the two derived categories: `Lf^*`
> sends `D_QCoh(𝒪_Y)` into `D_QCoh(𝒪_X)`.** For an arbitrary morphism of schemes `f : X ⟶ Y` and
> an object `E` of `D(𝒪_Y)` all of whose cohomology sheaves are quasi-coherent, every cohomology
> sheaf of `Lf^*E` is quasi-coherent.
>
> The model of the two derived categories is a free `[HasDerivedCategory.{w}]` binder, so this
> serves the locally small model of `Stacks.Duality.isQuasicoherent_homology_derivedPullback'` and
> `CategoryTheory.HasDerivedCategory.standard` alike. By [Stacks, Tag 06YF] the object `E` is the
> class of a K-flat complex `P`, at that model `Lf^*E` is the class of `f^*P` by
> `Stacks.Cohomology.derivedPullbackIsoPullbackOfKFlat`, and the cohomology sheaves of `f^*P` are
> quasi-coherent by `isQuasicoherent_homology_modulePullback_of_kFlat`.

```lean
theorem isQuasicoherent_homology_derivedPullback_anyModel {X Y : Scheme.{u}} (f : X ⟶ Y)
    [HasDerivedCategory.{w₁} (SheafOfModules.{u} (structureSheafRing X.toRingedSpace))]
    [HasDerivedCategory.{w₂} (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace))]
    (E : DerivedCategory (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)))
    (hE : ∀ j : ℤ, ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (structureSheafRing Y.toRingedSpace)) j).obj E).IsQuasicoherent) (i : ℤ) :
    ((DerivedCategory.homologyFunctor (SheafOfModules.{u} (structureSheafRing X.toRingedSpace))
        i).obj
      ((Stacks.Cohomology.DerivedAdjunctionOnRingedSpaces.derivedPullback
        f.toLRSHom.toShHom).obj E)).IsQuasicoherent
```

Declarations registered for the tag:

- [`AlgebraicGeometry.affinePullbackComparison`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePullbackComparison.lean#L334), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean#L525) (StacksFrontier): “part (2): the affine comparison square Lf^*(M̃^•) ≅ (S ⊗ᴸ_R M^•)~”.
- [`AlgebraicGeometry.affinePullbackComparison_fac`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffinePullbackComparison.lean#L349), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedPullback.lean#L528) (StacksFrontier): “part (2): the canonical normalisation of the affine comparison square”.

## Tag 08DX, a lemma

[Tag 08DX](https://stacks.math.columbia.edu/tag/08DX) in the Stacks Project.

**`AlgebraicGeometry.affineTensorComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedTensor.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedTensor.lean#L250). The attribute's comment: “part (2): the totalised ordinary comparison”.

> **The totalised affine tensor comparison.** For complexes `M^•` and `K^•` of `R`-modules, the
> complex of `𝒪_{Spec R}`-modules associated to the total tensor complex `Tot(M^• ⊗_R K^•)` is
> canonically the total tensor complex `Tot(M̃^• ⊗_{𝒪_{Spec R}} K̃^•)` of the associated complexes.
>
> The isomorphism is returned together with the formula for its value on the summand of total
> degree `n` indexed by `(i, j)`: there it is the degreewise comparison
> `AlgebraicGeometry.tildeTensorIso` of [Stacks, Tag 01I8] at `M^i` and `K^j`. That formula
> determines the isomorphism, since the source of total degree `n` is the direct sum of those
> summands, so it is carried in the type rather than stated separately.

```lean
public def affineTensorComplexIso (R : CommRingCat.{u})
    (M K : CochainComplex (ModuleCat.{u} R) ℤ) :
    { e : tildeComplexMod (A := R) (M ⊗ K) ≅
        ((tensorComplex.{u, u, u} (specCommRingSheaf R)).obj (tildeComplexMod (A := R) M)).obj
          (tildeComplexMod (A := R) K) //
      ∀ (i j n : ℤ) (h : i + j = n),
        (tilde.functor R).map (HomologicalComplex.ιMapBifunctor M K
            (curriedTensor (ModuleCat.{u} R)) (ComplexShape.up ℤ) i j n h) ≫ e.hom.f n =
          (tildeTensorIso R (M.X i) (K.X j)).hom ≫
            HomologicalComplex.ιMapBifunctor (tildeComplexMod (A := R) M)
              (tildeComplexMod (A := R) K)
              (sheafTensor.{u, u, u, u, u} (specCommRingSheaf R)) (ComplexShape.up ℤ) i j n h }
```

**`AlgebraicGeometry.affineDerivedTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedTensor.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDerivedTensor.lean#L343). The attribute's comment: “part (2): the affine comparison”.

> **Stacks Project, Tag 08DX, part (2).** On the spectrum of a commutative ring `R`, the
> derived tensor product of two associated complexes of sheaves of modules is the complex
> associated to their derived tensor product over `R`:
>
> `M̃^• ⊗_{𝒪_{Spec R}}^{L} K̃^•  ≅  (M^• ⊗_R^{L} K^•)~`.
>
> Both arguments are replaced by K-flat representatives, where the two derived tensor products are
> computed by ordinary total tensor complexes and the comparison is the totalised ordinary
> comparison `affineTensorComplexIso` of [Stacks, Tag 01I8]; the representatives are supplied by
> the definite choices of `kFlatRep`.

```lean
public def affineDerivedTensorIso (R : CommRingCat.{u})
    (M K : CochainComplex.DerivedTensor.DObj (R : Type u)) :
    (((Stacks.Cohomology.TorAmplitude.derTensor.{u, u} (Spec R).toRingedSpace).tensor.obj
          ((tildeDS R).obj M)).obj ((tildeDS R).obj K)) ≅
      (tildeDS R).obj
        (((CochainComplex.DerivedTensor.canonicalDerivedTensorProduct
          (R : Type u)).tensor.obj M).obj K)
```

**`AlgebraicGeometry.affineDerivedTensorIsoStandard`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDualizingPair.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/AffineDualizingPair.lean#L119). The attribute's comment: “part (2): the affine comparison, at the standard model”.

> On the spectrum of a commutative ring `R`, the derived tensor product of the complexes of
> sheaves of modules associated to `M` and `K` is the complex associated to their derived tensor
> product over `R`, at the standard model:
>
> `M̃^• ⊗^L_{𝒪_{Spec R}} K̃^•  ≅  (M^• ⊗^L_R K^•)~`.

```lean
def affineDerivedTensorIsoStandard (M K : DerivedCategory (ModuleCat.{u} R)) :
    ((derivedTensorAsSiteDatum (Spec R).sheaf).tensor.obj
          ((Stacks.Duality.derivedTildeStructureSheafModules R).obj M)).obj
        ((Stacks.Duality.derivedTildeStructureSheafModules R).obj K) ≅
      (Stacks.Duality.derivedTildeStructureSheafModules R).obj
        (((canonicalDerivedTensorProduct (R : Type u)).tensor.obj M).obj K)
```

**`Stacks.Duality.isQuasicoherent_homology_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedTensor.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedTensor.lean#L524). The attribute's comment: “part (1): D_QCoh is closed under derived tensor product”.

> **[Stacks, Tag 08DX] part (1): `D_QCoh(𝒪_X)` is closed under the derived tensor product.**
> Let `X` be a scheme and let `K` and `L` be complexes of `𝒪_X`-modules all of whose cohomology
> sheaves are quasi-coherent. Then every cohomology sheaf of `K ⊗ᴸ_{𝒪_X} L` is quasi-coherent.
>
> This is `isQuasicoherent_homology_derivedTensor_of_tensorTilde` with its hypothesis discharged by
> `exists_iso_derivedTilde_derivedTensor`.

```lean
theorem isQuasicoherent_homology_derivedTensor (X : Scheme.{u})
    (K L : quasiCoherentDerivedCategory X) (i : ℤ) :
    ((DerivedCategory.homologyFunctor X.Modules i).obj
      (((derivedTensor X).obj K.obj).obj L.obj)).IsQuasicoherent
```

**`Stacks.Duality.quasiCoherentDerivedTensor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedTensor.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedTensor.lean#L536). The attribute's comment: “part (1): the restriction D_QCoh ⥤ D_QCoh ⥤ D_QCoh of the derived tensor product”.

> **[Stacks, Tag 08DX] part (1), as structure: the derived tensor product restricts to
> `D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_X)`.** This is
> `quasiCoherentDerivedTensor_of_tensorTilde` with its hypothesis discharged by
> `exists_iso_derivedTilde_derivedTensor`.

```lean
abbrev quasiCoherentDerivedTensor (X : Scheme.{u}) :
    quasiCoherentDerivedCategory X ⥤ quasiCoherentDerivedCategory X ⥤
      quasiCoherentDerivedCategory X
```

**`Stacks.Duality.isQuasicoherent_homology_derivedTensor_anyModel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedTensorAnyModel.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/DerivedTilde/QuasiCoherentDerivedTensorAnyModel.lean#L113). The attribute's comment: “part (1) at an arbitrary model of the derived category”.

> **[Stacks, Tag 08DX] part (1) at an arbitrary model of `D(𝒪_X)`: `D_QCoh(𝒪_X)` is closed
> under the derived tensor product.**  For a scheme `X` and objects `E`, `A` of `D(𝒪_X)` all of
> whose cohomology sheaves are quasi-coherent, every cohomology sheaf of `E ⊗^𝐋_{𝒪_X} A` is
> quasi-coherent.
>
> The model of the derived category is a free `[HasDerivedCategory.{w}]` binder, so this serves the
> locally small model of `Stacks.Duality.isQuasicoherent_homology_derivedTensor` and
> `CategoryTheory.HasDerivedCategory.standard` alike.  `A` is the class of a K-flat complex `P` by
> [Stacks, Tag 06YS], `E` is the class of some complex `C`, the K-flat comparison of
> [Stacks, Tag 06YU] identifies `E ⊗^𝐋_{𝒪_X} A` with the class of `Tot(C ⊗_{𝒪_X} P)`, and the
> cohomology of that complex is quasi-coherent by `isQuasicoherent_homology_tensorComplex`.

```lean
theorem isQuasicoherent_homology_derivedTensor_anyModel (X : Scheme.{u})
    [HasDerivedCategory.{w} (Modules X.toRingedSpace.sheaf)]
    (E A : DerivedCategory (Modules X.toRingedSpace.sheaf))
    (hE : ∀ j : ℤ, ((DerivedCategory.homologyFunctor
      (Modules X.toRingedSpace.sheaf) j).obj E).IsQuasicoherent)
    (hA : ∀ j : ℤ, ((DerivedCategory.homologyFunctor
      (Modules X.toRingedSpace.sheaf) j).obj A).IsQuasicoherent) (i : ℤ) :
    ((DerivedCategory.homologyFunctor (Modules X.toRingedSpace.sheaf) i).obj
      (((derivedTensorProductFunctor X.toRingedSpace.sheaf).obj E).obj A)).IsQuasicoherent
```

**`Stacks.Thickenings.isQuasicoherent_homology_specDerivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/ThickeningQuasicoherent.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/ThickeningQuasicoherent.lean#L244). The attribute's comment: “part (1) on an affine scheme, at the standard model of the derived category”.

> **[Stacks, Tag 08DX] part (1) on an affine scheme, at the standard model.** If every
> cohomology sheaf of `A` and of `B` is quasi-coherent, then so is every cohomology sheaf of
> `A ⊗ᴸ_{𝒪_{Spec R}} B`.
>
> This is `Stacks.Duality.isQuasicoherent_homology_derivedTensor_spec`, whose only locally
> small-pinned input was essential surjectivity of derived sheafification, [Stacks, Tag 06Z0];
> that is available at the standard model as
> `AlgebraicGeometry.StandardModel.exists_iso_mapDerivedCategory`, so the argument runs verbatim.
> `A` and `B` are derived sheafifications of complexes of `R`-modules,
> `exists_iso_derivedTilde_derivedTensor_standard` makes their derived tensor product one as well,
> and the cohomology sheaves of a derived sheafification are quasi-coherent by construction.

```lean
public theorem isQuasicoherent_homology_specDerivedTensor (R : CommRingCat.{u})
    (A B : DerivedCategory (Spec R).Modules)
    (hA : ∀ n : ℤ, ((DerivedCategory.homologyFunctor (Spec R).Modules n).obj A).IsQuasicoherent)
    (hB : ∀ n : ℤ, ((DerivedCategory.homologyFunctor (Spec R).Modules n).obj B).IsQuasicoherent)
    (i : ℤ) :
    ((DerivedCategory.homologyFunctor (Spec R).Modules i).obj
      (((specDerivedTensor R).obj A).obj B)).IsQuasicoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.3, Tag 06YZ](https://stacks.math.columbia.edu/tag/06YZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
