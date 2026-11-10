---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_externalTensorProduct_epi, AlgebraicGeometry.exists_externalTensorProduct_epi_of_isFiniteType, AlgebraicGeometry.exists_externalTensorProduct_epi_of_isFiniteType_of_quasiSeparatedSpace, AlgebraicGeometry.exists_diagonalResolution, AlgebraicGeometry.subsingleton_zExt_of_isRegular, AlgebraicGeometry.subsingleton_hom_of_homology_separated_of_isRegular, Stacks.RegularExtVanishing.subsingleton_zExt_of_isRegular, Stacks.RegularExtVanishing.subsingleton_hom_of_homology_separated_of_isRegular
statement: formalized
proof: formalized
---

# 57.9 Resolutions and bounds

Section 57.9 of the Stacks Project, [Tag 0FYZ](https://stacks.math.columbia.edu/tag/0FYZ). 10 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FZ0, a lemma

[Tag 0FZ0](https://stacks.math.columbia.edu/tag/0FZ0) in the Stacks Project.

**`AlgebraicGeometry.exists_externalTensorProduct_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExternalTensorResolution.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExternalTensorResolution.lean#L204).

> Let `R` be a Noetherian ring and let `X`, `Y` be schemes of finite type over `R` having the
> resolution property. Every coherent `𝒪_{X ×_R Y}`-module is a quotient of `𝓔 ⊠ 𝓖` with `𝓔` a
> finite locally free `𝒪_X`-module and `𝓖` a finite locally free `𝒪_Y`-module.

```lean
theorem exists_externalTensorProduct_epi (R : Type u) [CommRing R] [IsNoetherianRing R]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of R)) (g : Y ⟶ Spec (.of R))
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyOfFiniteType g] [QuasiCompact g]
    [HasResolutionProperty X] [HasResolutionProperty Y]
    (F : (pullback f g).Modules) [F.IsCoherent] :
    ∃ (E : X.Modules) (G : Y.Modules)
      (_ : SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) E)
      (_ : SheafOfModules.IsFiniteLocallyFree (R := Y.ringCatSheaf) G)
      (q : externalTensorProduct f g E G ⟶ F), Epi q
```

## Tag 0FZ1, a lemma

[Tag 0FZ1](https://stacks.math.columbia.edu/tag/0FZ1) in the Stacks Project.

**`AlgebraicGeometry.exists_externalTensorProduct_epi_of_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExternalTensorFiniteType.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExternalTensorFiniteType.lean#L75). The attribute's comment: “the case where the product is Noetherian and the two factors are locally Noetherian; the limit argument removing those hypotheses is not covered”.

> **[Stacks, Tag 0FZ1] when `X ×_R Y` is Noetherian.** Let `R` be a ring and let `X`, `Y` be
> quasi-compact, quasi-separated, locally Noetherian `R`-schemes with the resolution property,
> with `X ×_R Y` Noetherian.  Every finite type quasi-coherent `𝒪_{X ×_R Y}`-module `F` admits a
> surjection `𝓔 ⊠ 𝓖 ⟶ F` with `𝓔` a finite locally free `𝒪_X`-module and `𝓖` a finite locally
> free `𝒪_Y`-module.
>
> Under the Noetherian hypothesis `F` is coherent ([Stacks, Tag 01XZ]) and the statement is
> [Stacks, Tag 0FZ0]; the limit argument that removes the hypothesis is not proved, see the
> implementation notes of this file.

```lean
theorem exists_externalTensorProduct_epi_of_isFiniteType (R : Type u) [CommRing R]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of R)) (g : Y ⟶ Spec (.of R))
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    [IsLocallyNoetherian X] [IsLocallyNoetherian Y]
    [HasResolutionProperty X] [HasResolutionProperty Y] [IsNoetherian (pullback f g)]
    (F : (pullback f g).Modules) [F.IsQuasicoherent] [F.IsFiniteType] :
    ∃ (E : X.Modules) (G : Y.Modules)
      (_ : SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) E)
      (_ : SheafOfModules.IsFiniteLocallyFree (R := Y.ringCatSheaf) G)
      (q : externalTensorProduct f g E G ⟶ F), Epi q
```

**`AlgebraicGeometry.exists_externalTensorProduct_epi_of_isFiniteType_of_quasiSeparatedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExternalTensorFiniteTypeQcqs.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExternalTensorFiniteTypeQcqs.lean#L370).

> Let `R` be a ring and let `X`, `Y` be quasi-compact and quasi-separated schemes over `R`
> having the resolution property.  For every finite type quasi-coherent `𝒪_{X ×_R Y}`-module `F`
> there is a surjection `𝓔 ⊠ 𝓖 ⟶ F` with `𝓔` a finite locally free `𝒪_X`-module and `𝓖` a finite
> locally free `𝒪_Y`-module.

```lean
theorem exists_externalTensorProduct_epi_of_isFiniteType_of_quasiSeparatedSpace
    (R : Type u) [CommRing R] {X Y : Scheme.{u}} (f : X ⟶ Spec (.of R)) (g : Y ⟶ Spec (.of R))
    [CompactSpace X] [QuasiSeparatedSpace X] [CompactSpace Y] [QuasiSeparatedSpace Y]
    [HasResolutionProperty X] [HasResolutionProperty Y]
    (F : (pullback f g).Modules) [F.IsQuasicoherent] [F.IsFiniteType] :
    ∃ (E : X.Modules) (G : Y.Modules)
      (_ : SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) E)
      (_ : SheafOfModules.IsFiniteLocallyFree (R := Y.ringCatSheaf) G)
      (q : externalTensorProduct f g E G ⟶ F), Epi q
```

## Tag 0FZ2, a lemma

[Tag 0FZ2](https://stacks.math.columbia.edu/tag/0FZ2) in the Stacks Project.

**`AlgebraicGeometry.exists_diagonalResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/DiagonalResolution.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/DiagonalResolution.lean#L67).

> **Stacks Project, Tag 0FZ2.** Let `R` be a Noetherian ring and let `X` be a separated scheme
> of finite type over `R` having the resolution property. The structure sheaf `𝒪_Δ = Δ_*𝒪_X` of the
> diagonal `Δ : X ⟶ X ×_R X` admits a resolution
>
> `… → ℰ₁ ⊠ 𝒢₁ → ℰ₀ ⊠ 𝒢₀ → 𝒪_Δ → 0`
>
> by external tensor products of finite locally free `𝒪_X`-modules.

```lean
theorem exists_diagonalResolution [IsSeparated f] :
    ∃ (C : ChainComplex (pullback f f).Modules ℕ) (E G : ℕ → X.Modules)
      (_ : ∀ i, SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) (E i))
      (_ : ∀ i, SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) (G i))
      (_ : C.X 0 ≅
        (Scheme.Modules.pushforward (pullback.diagonal f)).obj (SheafOfModules.unit _))
      (_ : ∀ i, C.X (i + 1) ≅ externalTensorProduct f f (E i) (G i)),
      C.Acyclic
```

## Tag 0FZ3, a lemma

[Tag 0FZ3](https://stacks.math.columbia.edu/tag/0FZ3) in the Stacks Project.

**`AlgebraicGeometry.subsingleton_zExt_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExtVanishingRegular.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExtVanishingRegular.lean#L222). The attribute's comment: “part (1)”.

> **[Stacks, Tag 0FZ3] part (1).** Let `X` be a regular Noetherian scheme of dimension
> `d < ∞`, let `F` be a coherent `𝒪_X`-module and `G` an arbitrary `𝒪_X`-module. Then
> `Ext^n_X(F, G) = 0` for every `n > d`.

```lean
theorem subsingleton_zExt_of_isRegular (X : Scheme.{u}) [IsNoetherian X] (hX : IsRegular X)
    (d : ℕ) (hd : topologicalKrullDim X = (d : WithBot ℕ∞)) (F G : X.Modules)
    (hF : F.IsCoherent) (n : ℤ) (hn : (d : ℤ) < n) : Subsingleton (Abelian.zExt F G n)
```

**`AlgebraicGeometry.subsingleton_hom_of_homology_separated_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExtVanishingRegular.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/ExtVanishingRegular.lean#L236). The attribute's comment: “part (2)”.

> **[Stacks, Tag 0FZ3] part (2).** Let `X` be a regular Noetherian scheme of dimension
> `d < ∞`. Let `K` and `L` be objects of `D^b_{Coh}(𝒪_X)` and let `a` be an integer. If
> `H^i(K) = 0` for `i < a + d` and `H^i(L) = 0` for `i ≥ a`, then `Hom_X(K, L) = 0`.

```lean
theorem subsingleton_hom_of_homology_separated_of_isRegular (X : Scheme.{u}) [IsNoetherian X]
    (hX : IsRegular X) (d : ℕ) (hd : topologicalKrullDim X = (d : WithBot ℕ∞))
    (K L : DerivedCategory X.Modules) (a : ℤ)
    (hKb : DerivedCategory.TStructure.t.bounded K)
    (hLb : DerivedCategory.TStructure.t.bounded L)
    (hKcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsCoherent)
    (hLcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj L).IsCoherent)
    (hK : ∀ i : ℤ, i < a + d → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K))
    (hL : ∀ i : ℤ, a ≤ i → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj L)) :
    Subsingleton (K ⟶ L)
```

**`Stacks.RegularExtVanishing.subsingleton_zExt_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/RegularExtVanishing/Basic.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/RegularExtVanishing/Basic.lean#L320). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0FZ3, part (1).** Let `X` be a regular Noetherian scheme of dimension
> `d < ∞`. For coherent `𝒪_X`-modules `F` and `G`, `Ext^n_X(F, G) = 0` for every `n > d`.
>
> The statement holds for every model of the derived category of `𝒪_X`-modules, since in
> non-negative degrees all of them compute the same `Ext` groups (`Abelian.Ext.homEquiv`).

```lean
theorem subsingleton_zExt_of_isRegular [HasDerivedCategory.{u + 1} X.Modules]
    (hX : IsRegular X) (d : ℕ) (hd : topologicalKrullDim X = (d : WithBot ℕ∞))
    (F G : X.Modules) (hF : _root_.SheafOfModules.IsCoherent F)
    (hG : _root_.SheafOfModules.IsCoherent G) (n : ℤ) (hn : (d : ℤ) < n) :
    Subsingleton (Abelian.zExt F G n)
```

**`Stacks.RegularExtVanishing.subsingleton_hom_of_homology_separated_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/RegularExtVanishing/Basic.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/RegularExtVanishing/Basic.lean#L340). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0FZ3, part (2).** Let `X` be a regular Noetherian scheme of dimension
> `d < ∞`, let `K` and `L` be objects of `D^b_{Coh}(𝒪_X)` and let `a` be an integer. If
> `H^i(K) = 0` for `i < a + d` and `H^i(L) = 0` for `i ≥ a`, then `Hom_X(K, L) = 0`.
>
> This is the formal consequence of part (1), `subsingleton_zExt_of_isRegular`, that the source
> draws by induction along the truncation triangles, which is
> `Stacks.SeparatedCohomology.subsingleton_hom_of_isGE_of_isLE`.

```lean
theorem subsingleton_hom_of_homology_separated_of_isRegular
    [HasDerivedCategory.{u + 1} X.Modules] (hX : IsRegular X) (d : ℕ)
    (hd : topologicalKrullDim X = (d : WithBot ℕ∞))
    (K L : DerivedCategory X.Modules) (a : ℤ)
    (hKb : DerivedCategory.TStructure.t.bounded K)
    (hLb : DerivedCategory.TStructure.t.bounded L)
    (hKcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsCoherent)
    (hLcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj L).IsCoherent)
    (hK : ∀ i : ℤ, i < a + d → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K))
    (hL : ∀ i : ℤ, a ≤ i → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj L)) :
    Subsingleton (K ⟶ L)
```

**`AlgebraicGeometry.subsingleton_hom_of_homology_separated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/SeparatedCohomologyHomVanishing.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/SeparatedCohomologyHomVanishing.lean#L210). The attribute's comment: “part (2), with part (1) as a hypothesis”.

> **Stacks Project, Tag 0FZ3, part (2).** Let `X` be a regular Noetherian scheme of dimension
> `d < ∞`. Let `K` and `L` be objects of `D^b_{Coh}(𝒪_X)` and let `a` be an integer. If
> `H^i(K) = 0` for `i < a + d` and `H^i(L) = 0` for `i ≥ a`, then `Hom_X(K, L) = 0`.
>
> The vanishing of `Ext^n_X(F, G)` for coherent `F`, `G` and `n > d`, which is part (1) of the same
> tag, is the hypothesis `hExt`; see the implementation notes of this file.

```lean
public theorem subsingleton_hom_of_homology_separated (X : Scheme.{u'}) [IsNoetherian X]
    (_hX : IsRegular X) (d : ℕ) (_hd : topologicalKrullDim X = (d : WithBot ℕ∞))
    (hExt : ∀ F G : X.Modules, F.IsCoherent → G.IsCoherent →
      ∀ n : ℤ, (d : ℤ) < n → Subsingleton (Abelian.zExt F G n))
    (K L : DerivedCategory X.Modules) (a : ℤ)
    (hKb : DerivedCategory.TStructure.t.bounded K)
    (hLb : DerivedCategory.TStructure.t.bounded L)
    (hKcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsCoherent)
    (hLcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj L).IsCoherent)
    (hK : ∀ i : ℤ, i < a + d → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K))
    (hL : ∀ i : ℤ, a ≤ i → IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj L)) :
    Subsingleton (K ⟶ L)
```

## Tag 0FZ4, a lemma

[Tag 0FZ4](https://stacks.math.columbia.edu/tag/0FZ4) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_biprod_truncations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/CohomologyGapSplitting.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/CohomologyGapSplitting.lean#L212). The attribute's comment: “a bounded coherent complex splits across a cohomology gap of length the dimension”.

> **[Stacks, Tag 0FZ4].** Let `X` be a regular Noetherian scheme of finite dimension `d`, with
> `0 < d`. Let `K` be a bounded complex of `𝒪_X`-modules with coherent cohomology and let `a` be
> an integer such that `H^i(K) = 0` for `a < i < a + d`. Then `K = τ^{≤ a} K ⊕ τ^{≥ a + d} K`.
>
> This is `exists_iso_biprod_truncLE_truncGE` together with the identification
> `τ^{≤ a + d - 1} K = τ^{≤ a} K`, which holds because the gap hypothesis makes
> `τ^{≤ a + d - 1} K` concentrated in degrees `≤ a`. The `Hom`-vanishing of
> [Stacks, Tag 0FZ3] part (2) that the splitting consumes is supplied by
> `AlgebraicGeometry.forall_separatedCohomologyHomVanishing`, so no hypothesis beyond the
> source's — and `0 < d`, without which the source's statement is false — is assumed.

```lean
public theorem exists_iso_biprod_truncations (X : Scheme.{u}) [IsNoetherian X]
    (hX : IsRegular X) (d : ℕ) (hd : topologicalKrullDim X = (d : WithBot ℕ∞)) (hd0 : 0 < d)
    (K : DerivedCategory X.Modules)
    (hKbdd : DerivedCategory.TStructure.t.bounded K)
    (hKcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsCoherent)
    (a : ℤ)
    (hgap : ∀ i : ℤ, a < i → i < a + (d : ℤ) →
      IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K)) :
    Nonempty (K ≅ (DerivedCategory.TStructure.t.truncLE a).obj K ⊞
      (DerivedCategory.TStructure.t.truncGE (a + (d : ℤ))).obj K)
```

**`AlgebraicGeometry.exists_iso_biprod_truncations_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/CohomologyGapSplittingRegular.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/CohomologyGapSplittingRegular.lean#L185). The attribute's comment: “corrected statement, under exactly the source's hypotheses: the source's form `K = τ^{≤ a} K ⊕ τ^{≥ a + d} K` is false at `d = 0` (`not_forall_nonempty_iso_biprod_truncLE_truncGE_of_dim_zero`), so it is concluded for `0 < d`, together with the form `K = τ^{≤ a + d - 1} K ⊕ τ^{≥ a + d} K`, which holds for every `d` and agrees with the source's for `0 < d`”.

> Let `X` be a regular Noetherian scheme of dimension `d < ∞`, let `K ∈ D^b_{Coh}(𝒪_X)` and
> `a ∈ ℤ` with `H^i(K) = 0` for `a < i < a + d`. Then `K ≅ τ^{≤ a + d - 1} K ⊕ τ^{≥ a + d} K`, and
> when `d ≥ 1` (where `τ^{≤ a + d - 1} K = τ^{≤ a} K`) `K ≅ τ^{≤ a} K ⊕ τ^{≥ a + d} K`, the
> source's form. At `d = 0` the source's form is false
> (`not_forall_nonempty_iso_biprod_truncLE_truncGE_of_dim_zero`), so the first conjunct is the
> statement for every `d` and the second is the source's conclusion wherever it holds. The
> connecting morphism of the truncation triangle vanishes by [Stacks, Tag 0FZ3] part (2).

```lean
theorem exists_iso_biprod_truncations_of_isRegular (X : Scheme.{u}) [IsNoetherian X]
    (hX : IsRegular X) (d : ℕ) (hd : topologicalKrullDim X = (d : WithBot ℕ∞))
    (K : DerivedCategory X.Modules)
    (hKbdd : DerivedCategory.TStructure.t.bounded K)
    (hKcoh : ∀ i : ℤ, ((DerivedCategory.homologyFunctor X.Modules i).obj K).IsCoherent)
    (a : ℤ)
    (hgap : ∀ i : ℤ, a < i → i < a + (d : ℤ) →
      IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj K)) :
    Nonempty (K ≅ (DerivedCategory.TStructure.t.truncLE (a + (d : ℤ) - 1)).obj K ⊞
        (DerivedCategory.TStructure.t.truncGE (a + (d : ℤ))).obj K) ∧
      (0 < d → Nonempty (K ≅ (DerivedCategory.TStructure.t.truncLE a).obj K ⊞
        (DerivedCategory.TStructure.t.truncGE (a + (d : ℤ))).obj K))
```

## Tag 0FZ5, a lemma

[Tag 0FZ5](https://stacks.math.columbia.edu/tag/0FZ5) in the Stacks Project.

**`AlgebraicGeometry.exists_externalTensor_triangEnvelope_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/DiagonalBoxGenerator.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/DiagonalBoxGenerator.lean#L183). The attribute's comment: “with Stacks 0FZ3(2), finite-dimensionality, brutal truncation and the box-sum retraction carried; see the module docstring”.

> **[Stacks, Tag 0FZ5].** Let `k` be a field and let `X` be a quasi-compact separated smooth
> scheme over `k`. There are finite locally free `𝒪_X`-modules `ℰ` and `𝒢` such that
> `𝒪_Δ ∈ ⟨ℰ ⊠ 𝒢⟩` in `D(𝒪_{X × X})`, where `⟨−⟩` is the smallest strictly full saturated
> triangulated subcategory containing the object, the notation of Derived Categories,
> Section 09SI.

```lean
public theorem exists_externalTensor_triangEnvelope_diagonal
    (hvan : HomVanishingAcrossCohomologyGap.{u})
    (hdim : FiniteDimensionalOfSmoothOverField.{u})
    (htrunc : BrutalTruncationOfAcyclicResolution.{u})
    (hsum : ExternalTensorSumRetract.{u})
    (hideal : ExistsSectionImageIdeal.{u})
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [CompactSpace X] [IsSeparated f] [Smooth f] :
    ∃ E G : X.Modules,
      SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) E ∧
      SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) G ∧
      (ObjectProperty.singleton ((DerivedCategory.singleFunctor (pullback f f).Modules 0).obj
          (externalTensorProduct f f E G))).triangEnvelope
        ((DerivedCategory.singleFunctor (pullback f f).Modules 0).obj
          ((Scheme.Modules.pushforward (pullback.diagonal f)).obj
            (SheafOfModules.unit X.ringCatSheaf)))
```

**`AlgebraicGeometry.exists_finiteLocallyFree_triangEnvelope_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/DiagonalBoxGeneratorUnconditional.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/DiagonalBoxGeneratorUnconditional.lean#L268).

> **[Stacks, Tag 0FZ5].** Let `k` be a field and let `X` be a quasi-compact separated smooth
> scheme over `k`. There are finite locally free `𝒪_X`-modules `ℰ` and `𝒢` such that
> `𝒪_Δ ∈ ⟨ℰ ⊠ 𝒢⟩` in `D(𝒪_{X × X})`, where `⟨−⟩` is the smallest strictly full saturated
> triangulated subcategory containing the object, the notation of Derived Categories,
> Section 09SI.

```lean
theorem exists_finiteLocallyFree_triangEnvelope_diagonal
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    [CompactSpace X] [IsSeparated f] [Smooth f] :
    ∃ E G : X.Modules,
      SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) E ∧
      SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) G ∧
      (ObjectProperty.singleton ((DerivedCategory.singleFunctor (pullback f f).Modules 0).obj
          (externalTensorProduct f f E G))).triangEnvelope
        ((DerivedCategory.singleFunctor (pullback f f).Modules 0).obj
          ((Scheme.Modules.pushforward (pullback.diagonal f)).obj
            (SheafOfModules.unit X.ringCatSheaf)))
```

## Tag 0FZ6, a lemma

[Tag 0FZ6](https://stacks.math.columbia.edu/tag/0FZ6) in the Stacks Project.

**`AlgebraicGeometry.isStrongTriangulatedGenerator_of_diagonalEnvelope`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/PerfectProperSmooth.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/PerfectProperSmooth.lean#L233). The attribute's comment: “the source's proof with its two external inputs carried, and its uniformity argument proved. Carried: (1) `hdiag`, the conclusion of Stacks 0FZ5 — proved as `AlgebraicGeometry.exists_externalTensor_triangEnvelope_diagonal`, itself carrying six hypotheses — with `box` for `ℰ ⊠ 𝒢` and `diag` for `𝒪_Δ`; (2) `Φ`, `hdiagΦ`, `hboxΦ`: the Fourier–Mukai family `R pr_{2,*}(L pr_1^* K ⊗^𝐋 −)` with `Φ_K(𝒪_Δ) ≅ K` and `Φ_K(ℰ ⊠ 𝒢) ∈ ⟨𝒢⟩₀`, neither of which the library has — Stacks 0FYV as formalized (base-only) explicitly does NOT cover `Φ_{𝒪_Δ} = id`, which needs Stacks 0B55 for a projection, proved only for closed embeddings, and Stacks 08EU as formalized (StacksFrontier/Topology/Sheaves/Cohomology/DerivedPushforward/ProjectionFormulaInvertibility.lean:249, base-only) covers only the base case `K = 𝒪_Y[0]`. Claimed: that `𝒢` is a STRONG generator, Stacks 09SJ(2), with the level uniform in `K` because it is read off the single object `𝒪_Δ`; and the functoriality of the stages `⟨−⟩ₙ` along an exact functor, the content of Stacks 0FX5, proved here as `Stacks.TriangulatedGenerators.triangEnvelopeIter_inverseImage_of_le`. Disclaimed: the construction of `ℰ`, `𝒢`, `Φ` and the two identities; accordingly this proof consumes neither properness nor smoothness directly — both enter only through the carried hypotheses”.

> **[Stacks, Tag 0FZ6].** Let `k` be a field and let `X` be a scheme proper and smooth over
> `k`. Then `D_perf(𝒪_X)` has a strong generator.
>
> The two external inputs of the source's proof are carried. `hdiag` is the conclusion of
> [Stacks, Tag 0FZ5]: the structure sheaf `𝒪_Δ` of the diagonal lies in the triangulated
> subcategory generated by a single external tensor product `ℰ ⊠ 𝒢` of finite locally free modules,
> here abstracted to objects `diag` and `box` of `D(𝒪_{X × X})`. The family `Φ` with `hdiagΦ` and
> `hboxΦ` is the Fourier–Mukai functor `Φ_K = R pr_{2,*}(L pr_1^* K ⊗^𝐋 −)` together with the two
> computations the source makes with it: `Φ_K(𝒪_Δ) = K` and `Φ_K(ℰ ⊠ 𝒢) = RΓ(X, K ⊗^𝐋 ℰ) ⊗_k 𝒢`,
> the latter already recorded as membership in `⟨𝒢⟩₀`, which is where properness of `X` enters
> through the finite dimensionality of the cohomology.
>
> What is proved here is the rest: that these inputs make `𝒢` a *strong* generator, with a level
> `n` independent of the perfect complex `K` because it is read off the single object `𝒪_Δ`.

```lean
theorem isStrongTriangulatedGenerator_of_diagonalEnvelope {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (CommRingCat.of k)) [IsProper f] [Smooth f] (G : perfectDerived X)
    (box diag : DerivedCategory (pullback f f).Modules)
    (hdiag : (ObjectProperty.singleton box).triangEnvelope diag)
    (Φ : perfectDerived X → DerivedCategory (pullback f f).Modules ⥤ perfectDerived X)
    [∀ K, (Φ K).CommShift ℤ] [∀ K, (Φ K).IsTriangulated]
    (hdiagΦ : ∀ K, (Φ K).obj diag ≅ K)
    (hboxΦ : ∀ K, ((ObjectProperty.singleton G).triangEnvelopeIter 0) ((Φ K).obj box)) :
    (ObjectProperty.singleton G).IsStrongTriangulatedGenerator
```

**`AlgebraicGeometry.exists_isStrongTriangulatedGenerator_perfectDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/PerfectProperSmoothUnconditional.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/PerfectProperSmoothUnconditional.lean#L131).

> **[Stacks, Tag 0FZ6].** Let `k` be a field and let `X` be a scheme proper and smooth over
> `k`. Then `D_perf(𝒪_X)` has a strong generator: there are an object `𝒢` and an integer `n` with
> `⟨𝒢⟩ₙ = D_perf(𝒪_X)`.
>
> The generator is the module `𝒢` of [Stacks, Tag 0FZ5] placed in degree zero, as in the source:
> [Stacks, Tag 0FZ5] applies because a proper scheme over `k` is quasi-compact and separated, and
> `isStrongTriangulatedGenerator_perfectDerivedCategory_of_diagonal` is the rest of the proof, a
> smooth morphism being flat.

```lean
theorem exists_isStrongTriangulatedGenerator_perfectDerivedCategory {k : Type u} [Field k]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] [Smooth f] :
    ∃ G : PerfectDerivedCategory X, (ObjectProperty.singleton G).IsStrongTriangulatedGenerator
```

## Tag 0FZ7, a lemma

[Tag 0FZ7](https://stacks.math.columbia.edu/tag/0FZ7) in the Stacks Project.

**`AlgebraicGeometry.exists_uniform_generator_isCoherent_of_diagonalEnvelope`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentUniformGenerator.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentUniformGenerator.lean#L131). The attribute's comment: “the source's statement, read at the locally small derived-category model `AlgebraicGeometry.Scheme.Modules.hasDerivedCategory` and proved there by transporting `AlgebraicGeometry.exists_uniform_generator_isCoherent` — the same tag at the standard model, in StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentUniformGeneratorUnconditional.lean — along the exact equivalence `AlgebraicGeometry.Scheme.Modules.derivedModelEquiv`, with Stacks 0FX5 (`Stacks.TriangulatedGenerators.``retractClosure_extensionProductIter_biSup_shift_inverseImage_of_le`) moving the four closure operations with the window and the level fixed and `StacksDraft.Perfect.GeomReducedFibre.modelEquivSingleIso` identifying the two readings of a module in cohomological degree zero. The name records the route by which the statement was first proved here”.

> **[Stacks, Tag 0FZ7].** Let `k` be a field and let `X` be a scheme proper and smooth over
> `k`. Then there are `m, n ≥ 1` and a finite locally free `𝒪_X`-module `𝒢` such that every
> coherent `𝒪_X`-module is a direct summand of an `n`-fold extension of finite direct sums of the
> shifts of `𝒢` by the degrees in `[-m, m]`.
>
> This is the tag read in the locally small derived category
> `AlgebraicGeometry.Scheme.Modules.hasDerivedCategory`. It comes from
> `AlgebraicGeometry.exists_uniform_generator_isCoherent`, the same tag at the standard model, by
> transport along the exact equivalence `AlgebraicGeometry.Scheme.Modules.derivedModelEquiv`:
> [Stacks, Tag 0FX5] carries `smd(add(𝒢[-m, m])^{⋆ n})` across an exact functor with the window and
> the level unchanged, and `StacksDraft.Perfect.GeomReducedFibre.modelEquivSingleIso` identifies the
> two readings of a module placed in cohomological degree zero.
>
> The name records the route by which the statement was first proved here, from the diagonal
> presentation of [Stacks, Tag 0FZ5].

```lean
theorem exists_uniform_generator_isCoherent_of_diagonalEnvelope
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (CommRingCat.of k))
    [IsProper f] [Smooth f] :
    ∃ (m n : ℕ) (𝒢 : X.Modules), 1 ≤ m ∧ 1 ≤ n ∧
      SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) 𝒢 ∧
      ∀ F : X.Modules, F.IsCoherent →
        ((⨆ i ∈ Set.Icc (-(m : ℤ)) (m : ℤ), (ObjectProperty.singleton
            ((DerivedCategory.singleFunctor X.Modules 0).obj 𝒢)).isoClosure.shift i
          ).binaryProductsClosure.extensionProductIter n).retractClosure
            ((DerivedCategory.singleFunctor X.Modules 0).obj F)
```

**`AlgebraicGeometry.exists_uniform_generator_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentUniformGeneratorUnconditional.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentUniformGeneratorUnconditional.lean#L60).

> **[Stacks, Tag 0FZ7].** Let `k` be a field and let `X` be a scheme proper and smooth over
> `k`. There are integers `m, n ≥ 1` and a finite locally free `𝒪_X`-module `𝒢` such that every
> coherent `𝒪_X`-module, placed in degree zero, is a direct summand of an object obtained by `n`
> extensions from finite direct sums of the shifts of `𝒢` by the degrees in `[-m, m]`; that is,
> it lies in `smd(add(𝒢[-m, m])^{⋆ n})`.

```lean
theorem exists_uniform_generator_isCoherent {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f] [Smooth f] :
    ∃ (m n : ℕ) (𝒢 : X.Modules), 1 ≤ m ∧ 1 ≤ n ∧
      SheafOfModules.IsFiniteLocallyFree (R := X.ringCatSheaf) 𝒢 ∧
      ∀ F : X.Modules, F.IsCoherent →
        ((⨆ i ∈ Set.Icc (-(m : ℤ)) (m : ℤ), (ObjectProperty.singleton
            ((DerivedCategory.singleFunctor X.Modules 0).obj 𝒢)).isoClosure.shift i
          ).binaryProductsClosure.extensionProductIter n).retractClosure
            ((DerivedCategory.singleFunctor X.Modules 0).obj F)
```

## Tag 0FZ8, a lemma

[Tag 0FZ8](https://stacks.math.columbia.edu/tag/0FZ8) in the Stacks Project.

**`AlgebraicGeometry.exists_uniform_bound_isZero_of_isHomological`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorBounds.lean, line 468](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorBounds.lean#L468). The attribute's comment: “the homological case, from Stacks 0FZ7 as it stands. The cohomological case of the final sentence is `AlgebraicGeometry.exists_uniform_bound_isZero_of_isCohomological`”.

> **[Stacks, Tag 0FZ8], the homological case.** Let `k` be a field, let `X` be a scheme proper
> and smooth over `k`, let `𝒜` be an abelian category and let `H : D_perf(𝒪_X) ⥤ 𝒜` be a
> homological functor whose cohomology `H^i(K) = H(K[i])` is nonzero for only finitely many `i`,
> for every perfect `K`. Then there is an `m ≥ 1`, independent of the module, with `H^i(ℱ) = 0` for
> every coherent `𝒪_X`-module `ℱ` and every `i ∉ [-m, m]`.
>
> [Stacks, Tag 0FZ7] is used as it stands, with no input of its own left open. The window of `H` on
> the single generator it supplies exists because the cohomology of `H` is finitely supported, and
> [Stacks, Tag 0FX8] widens it to the whole tower by the fixed amount `[-m₀, m₀]`, which is what
> makes the bound uniform.

```lean
theorem exists_uniform_bound_isZero_of_isHomological {𝒜 : Type*} [Category 𝒜] [Abelian 𝒜]
    (H : ObjectProperty.FullSubcategory
      (fun K : DerivedCategory X.Modules => IsPerfect (X := X.toRingedSpace) K) ⥤ 𝒜)
    [H.IsHomological]
    (hfin : ∀ Z, {i : ℤ | ¬ IsZero (H.obj (Z⟦i⟧))}.Finite) :
    ∃ m : ℕ, 1 ≤ m ∧ ∀ (F : X.Modules) [F.IsCoherent] (i : ℤ),
      i ∉ Set.Icc (-(m : ℤ)) (m : ℤ) → IsZero (H.obj ((coherentPerfect f F)⟦i⟧))
```

**`AlgebraicGeometry.exists_uniform_bound_isZero_of_isCohomological`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorBounds.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorBounds.lean#L500). The attribute's comment: “the cohomological case of the final sentence, with a cohomological functor read as a homological functor on the opposite category, and from Stacks 0FZ7 as it stands, as in the homological case”.

> **[Stacks, Tag 0FZ8], the cohomological case.** Let `k` be a field, let `X` be a scheme
> proper and smooth over `k`, let `𝒜` be an abelian category and let `H : D_perf(𝒪_X)ᵒᵖ ⥤ 𝒜` be a
> cohomological functor whose cohomology `H^i(K) = H(K[i])` is nonzero for only finitely many `i`,
> for every perfect `K`. Then there is an `m ≥ 1`, independent of the module, with `H^i(ℱ) = 0` for
> every coherent `𝒪_X`-module `ℱ` and every `i ∉ [-m, m]`.
>
> This is the final sentence of the tag. A cohomological functor is a homological functor on the
> opposite category, and the window argument is
> `Stacks.TriangulatedGenerators.isZero_obj_op_shift_of_retractClosure_extensionProductIter`, the
> contravariant form of [Stacks, Tag 0FX8]; [Stacks, Tag 0FZ7] is used as it stands, as in the
> homological case.

```lean
theorem exists_uniform_bound_isZero_of_isCohomological {𝒜 : Type*} [Category 𝒜] [Abelian 𝒜]
    (H : (ObjectProperty.FullSubcategory
      (fun K : DerivedCategory X.Modules => IsPerfect (X := X.toRingedSpace) K))ᵒᵖ ⥤ 𝒜)
    [H.IsHomological]
    (hfin : ∀ Z, {i : ℤ | ¬ IsZero (H.obj (op (Z⟦i⟧)))}.Finite) :
    ∃ m : ℕ, 1 ≤ m ∧ ∀ (F : X.Modules) [F.IsCoherent] (i : ℤ),
      i ∉ Set.Icc (-(m : ℤ)) (m : ℤ) → IsZero (H.obj (op ((coherentPerfect f F)⟦i⟧)))
```

**`AlgebraicGeometry.exists_uniform_bound_isZero_of_isHomological_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorUniformBounds.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorUniformBounds.lean#L273). The attribute's comment: “the homological case; the cohomological case of the final sentence is `AlgebraicGeometry.exists_uniform_bound_isZero_of_isCohomological_of_isProper`”.

> **Uniform bounds for a homological functor on the coherent modules.** Let `k` be a field, let
> `X` be a scheme proper and smooth over `k`, let `𝒜` be an abelian category and let
> `H : D_perf(𝒪_X) ⥤ 𝒜` be a homological functor whose cohomology `H^i(K) = H(K[i])` is nonzero for
> only finitely many `i`, for every perfect `K`. Then there is an `m ≥ 1` with `H^i(ℱ) = 0` for
> every coherent `𝒪_X`-module `ℱ` and every `i ∉ [-m, m]`.

```lean
theorem exists_uniform_bound_isZero_of_isHomological_of_isProper [IsProper f]
    {𝒜 : Type*} [Category 𝒜] [Abelian 𝒜]
    (H : ObjectProperty.FullSubcategory
      (fun K : DerivedCategory X.Modules => IsPerfect (X := X.toRingedSpace) K) ⥤ 𝒜)
    [H.IsHomological]
    (hfin : ∀ Z, {i : ℤ | ¬ IsZero (H.obj (Z⟦i⟧))}.Finite) :
    ∃ m : ℕ, 1 ≤ m ∧ ∀ (F : X.Modules) [F.IsCoherent] (i : ℤ),
      i ∉ Set.Icc (-(m : ℤ)) (m : ℤ) → IsZero (H.obj ((coherentPerfect f F)⟦i⟧))
```

**`AlgebraicGeometry.exists_uniform_bound_isZero_of_isCohomological_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorUniformBounds.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrongGenerator/CoherentFunctorUniformBounds.lean#L289). The attribute's comment: “the cohomological case of the final sentence, a cohomological functor being a homological functor on the opposite category”.

> **Uniform bounds for a cohomological functor on the coherent modules.** As
> `AlgebraicGeometry.exists_uniform_bound_isZero_of_isHomological_of_isProper`, for a
> cohomological functor, read as a homological functor `D_perf(𝒪_X)ᵒᵖ ⥤ 𝒜`.

```lean
theorem exists_uniform_bound_isZero_of_isCohomological_of_isProper [IsProper f]
    {𝒜 : Type*} [Category 𝒜] [Abelian 𝒜]
    (H : (ObjectProperty.FullSubcategory
      (fun K : DerivedCategory X.Modules => IsPerfect (X := X.toRingedSpace) K))ᵒᵖ ⥤ 𝒜)
    [H.IsHomological]
    (hfin : ∀ Z, {i : ℤ | ¬ IsZero (H.obj (op (Z⟦i⟧)))}.Finite) :
    ∃ m : ℕ, 1 ≤ m ∧ ∀ (F : X.Modules) [F.IsCoherent] (i : ℤ),
      i ∉ Set.Icc (-(m : ℤ)) (m : ℤ) → IsZero (H.obj (op ((coherentPerfect f F)⟦i⟧)))
```

## Tag 0FZ9, a lemma

[Tag 0FZ9](https://stacks.math.columbia.edu/tag/0FZ9) in the Stacks Project.

**`AlgebraicGeometry.isZero_homology_of_notInBands_of_finiteTypeOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandsOverField.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandsOverField.lean#L80). The attribute's comment: “part (1)”.

> Let `X` and `Y` be locally of finite type over a field `k` and let `K₀, K₁, …` be perfect
> objects of `D(𝒪_{X ×_k Y})` with cohomology vanishing above `m`. If for every coherent
> `𝒪_X`-module `𝓕` with zero-dimensional support the cohomology of `R pr_{2,*}(pr_1^*𝓕 ⊗^𝐋 Kₙ)` is
> concentrated in `[-m, m] ∪ [-m-n, m-n]`, then so is the cohomology of `Kₙ`.

```lean
public theorem isZero_homology_of_notInBands_of_finiteTypeOverField
    [LocallyOfFiniteType f] [LocallyOfFiniteType g]
    (K : ℕ → DerivedCategory (Limits.pullback f g).Modules) (m : ℕ)
    (hperf : ∀ n, RingedSpace.IsPerfect.{u, u + 1}
      (X := (Limits.pullback f g).toRingedSpace) (K n))
    (hupper : ∀ (n : ℕ) (j : ℤ), (m : ℤ) < j →
      IsZero ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules j).obj (K n)))
    (hfibreBand : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), ¬ InBands m n j →
      IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj (fibreTransform f g (K n) F)))
    (n : ℕ) (i : ℤ) (hi : ¬ InBands m n i) :
    IsZero ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules i).obj (K n))
```

**`AlgebraicGeometry.isIso_homologyMap_of_fibreStable_of_finiteTypeOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandsOverField.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandsOverField.lean#L102). The attribute's comment: “part (2)”.

> In the situation of `isZero_homology_of_notInBands_of_finiteTypeOverField`, if moreover
> the transition maps `tₙ : Kₙ ⟶ Kₙ₊₁` are isomorphisms on the cohomology of the integral
> transforms of the coherent modules with zero-dimensional support throughout `[-m, m]` once
> `n > 2m`, then for `n > 2m` the map `tₙ` is an isomorphism on the cohomology sheaves of the
> kernels throughout `[-m, m]`.

```lean
public theorem isIso_homologyMap_of_fibreStable_of_finiteTypeOverField
    [LocallyOfFiniteType f] [LocallyOfFiniteType g]
    (K : ℕ → DerivedCategory (Limits.pullback f g).Modules) (t : ∀ n, K n ⟶ K (n + 1)) (m : ℕ)
    (hperf : ∀ n, RingedSpace.IsPerfect.{u, u + 1}
      (X := (Limits.pullback f g).toRingedSpace) (K n))
    (hupper : ∀ (n : ℕ) (j : ℤ), (m : ℤ) < j →
      IsZero ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules j).obj (K n)))
    (hfibreBand : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), ¬ InBands m n j →
      IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj (fibreTransform f g (K n) F)))
    (hfibreStable : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), 2 * m < n →
      -(m : ℤ) ≤ j → j ≤ (m : ℤ) →
      IsIso ((DerivedCategory.homologyFunctor Y.Modules j).map
        ((fibreTransformFunctor f g F).map (t n))))
    (n : ℕ) (i : ℤ) (hn : 2 * m < n) (hi₁ : -(m : ℤ) ≤ i) (hi₂ : i ≤ (m : ℤ)) :
    IsIso ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules i).map (t n))
```

**`AlgebraicGeometry.exists_stable_biprod_of_smooth_of_finiteTypeOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandsOverField.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandsOverField.lean#L194). The attribute's comment: “part (3)”.

> Let `X` and `Y` be smooth and of finite type over a field `k`, and let `K₀ ⟶ K₁ ⟶ ⋯` be a
> system of perfect objects of `D(𝒪_{X ×_k Y})` with cohomology vanishing above `m` such that, for
> every coherent `𝒪_X`-module `𝓕` with zero-dimensional support, the cohomology of
> `R pr_{2,*}(pr_1^*𝓕 ⊗^𝐋 Kₙ)` is concentrated in `[-m, m] ∪ [-m-n, m-n]` and the transition maps
> are isomorphisms on it throughout `[-m, m]` once `n > 2m`. Then for all large `n` the kernel `Kₙ`
> is the direct sum of a perfect object `A` concentrated in `[-m, m]` and independent of `n` and a
> perfect object `Cₙ` concentrated in `[-m-n, m-n]`, and each transition map is the direct sum of an
> automorphism of `A` and a map `Cₙ ⟶ Cₙ₊₁`.
>
> This is `AlgebraicGeometry.exists_stable_biprod_of_smooth_of_homVanishing` with
> [Stacks, Tag 0FZ3] part (2) supplied by `AlgebraicGeometry.separatedCohomologyHomVanishing`.

```lean
public theorem exists_stable_biprod_of_smooth_of_finiteTypeOverField
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyOfFiniteType g] [QuasiCompact g]
    [Smooth f] [Smooth g]
    (K : ℕ → DerivedCategory (pullback f g).Modules) (t : ∀ n, K n ⟶ K (n + 1)) (m : ℕ)
    (hperf : ∀ n, RingedSpace.IsPerfect.{u, u + 1}
      (X := (pullback f g).toRingedSpace) (K n))
    (hupper : ∀ (n : ℕ) (j : ℤ), (m : ℤ) < j →
      Limits.IsZero
        ((DerivedCategory.homologyFunctor (pullback f g).Modules j).obj (K n)))
    (hfibreBand : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), ¬ InBands m n j →
      Limits.IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj
        (fibreTransform f g (K n) F)))
    (hfibreStable : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), 2 * m < n →
      -(m : ℤ) ≤ j → j ≤ (m : ℤ) →
      IsIso ((DerivedCategory.homologyFunctor Y.Modules j).map
        ((fibreTransformFunctor f g F).map (t n)))) :
    ∃ (N : ℕ) (A : DerivedCategory (pullback f g).Modules)
      (C : ℕ → DerivedCategory (pullback f g).Modules),
      RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) A ∧
      (∀ n, N ≤ n →
        RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) (C n)) ∧
      (∀ i : ℤ, (i < -(m : ℤ) ∨ (m : ℤ) < i) →
        Limits.IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj A)) ∧
      (∀ n, N ≤ n → ∀ i : ℤ, (i < -(m : ℤ) - (n : ℤ) ∨ (m : ℤ) - (n : ℤ) < i) →
        Limits.IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj (C n))) ∧
      ∃ e : (∀ n : ℕ, N ≤ n → (K n ≅ A ⊞ C n)),
        ∀ (n : ℕ) (hn : N ≤ n),
          ∃ (a : A ≅ A) (c : C n ⟶ C (n + 1)),
            t n ≫ (e (n + 1) (by omega)).hom = (e n hn).hom ≫ biprod.map a.hom c
```

**`AlgebraicGeometry.exists_stable_biprod_of_smooth_of_fibreBands`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandSplitting.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreBandSplitting.lean#L155). The attribute's comment: “part (3), on the source's hypotheses: parts (1) and (2), the derived-tensor comparisons, Stacks 0FZ3(2) and the non-emptiness of the product are all discharged”.

> **Stacks Project, Tag 0FZ9, part (3), on the source's hypotheses.** Let `X` and `Y` be
> quasi-compact schemes, smooth and locally of finite type over a field `k`, and let
> `K₀ ⟶ K₁ ⟶ ⋯` be a system of perfect objects of `D(𝒪_{X ×_k Y})` with cohomology vanishing above
> `m`. Assume that for every coherent `𝒪_X`-module with zero-dimensional support the cohomology of
> the integral transform by `Kₙ` is concentrated in `[-m, m] ∪ [-m-n, m-n]` and that, for `n > 2m`,
> the transition maps are isomorphisms on the cohomology of those transforms throughout `[-m, m]`.
> Then for all large `n` the object `Kₙ` is the direct sum of a perfect object `A` concentrated in
> `[-m, m]` and independent of `n` and a perfect object `Cₙ` concentrated in `[-m-n, m-n]`,
> compatibly with the transition maps.
>
> This is `AlgebraicGeometry.exists_stable_biprod_of_smooth_of_fibreTransforms` with its three extra
> hypotheses discharged: the comparisons by `AlgebraicGeometry.fibreTensorComparisonsOfPullback`,
> [Stacks, Tag 0FZ3] part (2) by `AlgebraicGeometry.forall_separatedCohomologyHomVanishing`, and the
> non-emptiness of `X ×_k Y` by treating the empty product apart, where every object is zero, so that
> `A = K₀` and `Cₙ = Kₙ` do.

```lean
theorem exists_stable_biprod_of_smooth_of_fibreBands (k : Type u) [Field k]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyOfFiniteType g] [QuasiCompact g]
    [Smooth f] [Smooth g]
    (K : ℕ → DerivedCategory (pullback f g).Modules) (t : ∀ n, K n ⟶ K (n + 1)) (m : ℕ)
    (hperf : ∀ n, RingedSpace.IsPerfect.{u, u + 1}
      (X := (pullback f g).toRingedSpace) (K n))
    (hupper : ∀ (n : ℕ) (j : ℤ), (m : ℤ) < j →
      IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules j).obj (K n)))
    (hfibreBand : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), ¬ InBands m n j →
      IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj (fibreTransform f g (K n) F)))
    (hfibreStable : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), 2 * m < n →
      -(m : ℤ) ≤ j → j ≤ (m : ℤ) →
      IsIso ((DerivedCategory.homologyFunctor Y.Modules j).map
        ((fibreTransformFunctor f g F).map (t n)))) :
    ∃ (N : ℕ) (A : DerivedCategory (pullback f g).Modules)
      (C : ℕ → DerivedCategory (pullback f g).Modules),
      RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) A ∧
      (∀ n, N ≤ n →
        RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) (C n)) ∧
      (∀ i : ℤ, (i < -(m : ℤ) ∨ (m : ℤ) < i) →
        IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj A)) ∧
      (∀ n, N ≤ n → ∀ i : ℤ, (i < -(m : ℤ) - (n : ℤ) ∨ (m : ℤ) - (n : ℤ) < i) →
        IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj (C n))) ∧
      ∃ e : (∀ n : ℕ, N ≤ n → (K n ≅ A ⊞ C n)),
        ∀ (n : ℕ) (hn : N ≤ n),
          ∃ (a : A ≅ A) (c : C n ⟶ C (n + 1)),
            t n ≫ (e (n + 1) (by omega)).hom = (e n hn).hom ≫ biprod.map a.hom c
```

**`AlgebraicGeometry.isIso_homologyMap_of_fibreStable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreStableTransitions.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/FibreStableTransitions.lean#L204). The attribute's comment: “part (2), the transition map is invertible on the cohomology of the kernels in [-m, m] once n > 2m, with the general derived-tensor comparisons carried as FibreTensorComparisons”.

> Let `τ : K ⟶ K'` be a morphism of perfect objects of `D(𝒪_{X ×_S Y})` with cohomology
> vanishing above `m`, let the cohomology of the integral transforms of the coherent modules with
> zero-dimensional support be concentrated in `[-m, m] ∪ [-m-n, m-n]` for `K` and in
> `[-m, m] ∪ [-m-n-1, m-n-1]` for `K'`, and let `τ` be an isomorphism on the cohomology of those
> transforms throughout `[-m, m]`. If `n > 2m` then `τ` is an isomorphism on the cohomology sheaves
> of the kernels throughout `[-m, m]`.

```lean
public theorem isIso_homologyMap_of_fibreStable (cmp : FibreTensorComparisons f g)
    (K K' : DerivedCategory (Limits.pullback f g).Modules) (τ : K ⟶ K')
    (hK : RingedSpace.IsPerfect (X := (Limits.pullback f g).toRingedSpace) K)
    (hK' : RingedSpace.IsPerfect (X := (Limits.pullback f g).toRingedSpace) K') (m n : ℕ)
    (hupper : ∀ j : ℤ, (m : ℤ) < j →
      IsZero ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules j).obj K))
    (hupper' : ∀ j : ℤ, (m : ℤ) < j →
      IsZero ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules j).obj K'))
    (hband : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ j : ℤ, ¬ InBands m n j →
      IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj (fibreTransform f g K F)))
    (hband' : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ j : ℤ, ¬ InBands m (n + 1) j →
      IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj (fibreTransform f g K' F)))
    (hstable : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ j : ℤ, -(m : ℤ) ≤ j → j ≤ (m : ℤ) →
      IsIso ((DerivedCategory.homologyFunctor Y.Modules j).map
        ((fibreTransformFunctor f g F).map τ)))
    (hn : 2 * m < n) (i : ℤ) (hi₁ : -(m : ℤ) ≤ i) (hi₂ : i ≤ (m : ℤ)) :
    IsIso ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules i).map τ)
```

**`AlgebraicGeometry.isZero_homology_of_notInBands`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/PerfectFibreBands.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/PerfectFibreBands.lean#L475). The attribute's comment: “part (1), the two bands for the kernels, with the general derived-tensor comparisons carried as FibreTensorComparisons”.

> **Stacks Project, Tag 0FZ9, part (1).** Let `S` be affine and Jacobson, let `X` and `Y` be
> locally of finite type over `S` with `X` and `X ×_S Y` locally Noetherian, and let `K` be a
> perfect object of `D(𝒪_{X ×_S Y})` whose cohomology vanishes above `m`. If for every coherent
> `𝒪_X`-module `𝓕` with zero-dimensional support the cohomology of the integral transform
> `R pr_{2,*}(pr_1^*𝓕 ⊗^𝐋 K)` is concentrated in `[-m, m] ∪ [-m-n, m-n]`, then so is the
> cohomology of `K` itself.

```lean
public theorem isZero_homology_of_notInBands (cmp : FibreTensorComparisons f g)
    (K : DerivedCategory (Limits.pullback f g).Modules)
    (hK : RingedSpace.IsPerfect (X := (Limits.pullback f g).toRingedSpace) K) (m n : ℕ)
    (hupper : ∀ j : ℤ, (m : ℤ) < j →
      IsZero ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules j).obj K))
    (hband : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ j : ℤ, ¬ InBands m n j →
      IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj (fibreTransform f g K F)))
    (i : ℤ) (hi : ¬ InBands m n i) :
    IsZero ((DerivedCategory.homologyFunctor (Limits.pullback f g).Modules i).obj K)
```

**`AlgebraicGeometry.exists_stable_biprod_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/SmoothBandSplitting.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/SmoothBandSplitting.lean#L499). The attribute's comment: “part (3) in kernel-level form, taking parts (1) and (2) as hband/hstable; those ARE proved, in PerfectFibreBands and FibreStableTransitions, and are discharged in exists_stable_biprod_of_smooth_of_fibreTransforms. Carries 0FZ3(2) as hvan and non-emptiness of the product as hne, neither of which the source has”.

> **The splitting of a sequence of perfect complexes on a product of smooth schemes.** Let `X`
> and `Y` be quasi-compact schemes, smooth and locally of finite type over a field `k`, with
> `X ×_k Y` nonempty, and let `K₀ ⟶ K₁ ⟶ ⋯` be a sequence of perfect objects of
> `D(𝒪_{X ×_k Y})` whose cohomology lives in the stable band `[-m, m]` together with the receding
> band `[-m-n, m-n]`, and whose transition maps are isomorphisms on cohomology throughout the
> stable band once `n > 2m`. Then for all large `n` the object `Kₙ` is the direct sum of a perfect
> object `A` concentrated in `[-m, m]` and independent of `n`, and a perfect object `Cₙ`
> concentrated in `[-m-n, m-n]`, compatibly with the transition maps.
>
> The product of two schemes smooth over `k` is smooth over `k`, hence regular by
> [Stacks, Tag 056S]; it is quasi-compact over the base, hence Noetherian, and of finite dimension
> because it is nonempty, quasi-compact and locally of finite type over `k`.
>
> The band hypotheses `hband` and `hstable` are the conclusions of parts (1) and (2) of
> [Stacks, Tag 0FZ9], which are *not* proved in this development; see the coverage note in the
> module docstring.

```lean
public theorem exists_stable_biprod_of_smooth (k : Type u) [Field k] {X Y : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyOfFiniteType g] [QuasiCompact g]
    [Smooth f] [Smooth g] [IsNoetherian (pullback f g)] (hne : Nonempty ↥(pullback f g))
    (hvan : ∀ d : ℕ, SeparatedCohomologyHomVanishing (pullback f g) d)
    (K : ℕ → DerivedCategory (pullback f g).Modules) (t : ∀ n, K n ⟶ K (n + 1)) (m : ℕ)
    (hperf : ∀ n, RingedSpace.IsPerfect.{u, u + 1}
      (X := (pullback f g).toRingedSpace) (K n))
    (hband : ∀ (n : ℕ) (i : ℤ), ¬ InBands m n i →
      Limits.IsZero
        ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj (K n)))
    (hstable : ∀ (n : ℕ) (i : ℤ), 2 * m < n → -(m : ℤ) ≤ i → i ≤ (m : ℤ) →
      IsIso ((DerivedCategory.homologyFunctor (pullback f g).Modules i).map (t n))) :
    ∃ (N : ℕ) (A : DerivedCategory (pullback f g).Modules)
      (C : ℕ → DerivedCategory (pullback f g).Modules),
      RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) A ∧
      (∀ n, N ≤ n →
        RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) (C n)) ∧
      (∀ i : ℤ, (i < -(m : ℤ) ∨ (m : ℤ) < i) →
        Limits.IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj A)) ∧
      (∀ n, N ≤ n → ∀ i : ℤ, (i < -(m : ℤ) - (n : ℤ) ∨ (m : ℤ) - (n : ℤ) < i) →
        Limits.IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj (C n))) ∧
      ∃ e : (∀ n : ℕ, N ≤ n → (K n ≅ A ⊞ C n)),
        ∀ (n : ℕ) (hn : N ≤ n),
          ∃ (a : A ≅ A) (c : C n ⟶ C (n + 1)),
            t n ≫ (e (n + 1) (by omega)).hom = (e n hn).hom ≫ biprod.map a.hom c
```

**`AlgebraicGeometry.exists_stable_biprod_of_smooth_of_fibreTransforms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/SmoothBandSplittingUnconditional.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ResolutionsAndBounds/SmoothBandSplittingUnconditional.lean#L140). The attribute's comment: “part (3) with parts (1) and (2) DISCHARGED from the tag's fibrewise hypotheses, carrying only the general derived-tensor comparisons as FibreTensorComparisons together with the two hypotheses the source does not have, 0FZ3(2) as hvan (which the library's 0FZ4 itself carries) and non-emptiness of the product as hne”.

> Let `X` and `Y` be quasi-compact schemes, smooth and locally of finite type over a field `k`,
> with `X ×_k Y` nonempty, and let `K₀ ⟶ K₁ ⟶ ⋯` be a system of perfect objects of
> `D(𝒪_{X ×_k Y})` with cohomology vanishing above `m`. Assume that for every coherent `𝒪_X`-module
> with zero-dimensional support the cohomology of the integral transform by `Kₙ` is concentrated in
> `[-m, m] ∪ [-m-n, m-n]` and that, for `n > 2m`, the transition maps are isomorphisms on the
> cohomology of those transforms throughout `[-m, m]`. Then for all large `n` the object `Kₙ` is the
> direct sum of a perfect object `A` concentrated in `[-m, m]` and independent of `n` and a perfect
> object `Cₙ` concentrated in `[-m-n, m-n]`, compatibly with the transition maps.

```lean
public theorem exists_stable_biprod_of_smooth_of_fibreTransforms (k : Type u) [Field k]
    {X Y : Scheme.{u}} (f : X ⟶ Spec (.of k)) (g : Y ⟶ Spec (.of k))
    [LocallyOfFiniteType f] [QuasiCompact f] [LocallyOfFiniteType g] [QuasiCompact g]
    [Smooth f] [Smooth g] [IsNoetherian (pullback f g)] (hne : Nonempty ↥(pullback f g))
    (hvan : ∀ d : ℕ, SeparatedCohomologyHomVanishing (pullback f g) d)
    (cmp : FibreTensorComparisons f g)
    (K : ℕ → DerivedCategory (pullback f g).Modules) (t : ∀ n, K n ⟶ K (n + 1)) (m : ℕ)
    (hperf : ∀ n, RingedSpace.IsPerfect.{u, u + 1}
      (X := (pullback f g).toRingedSpace) (K n))
    (hupper : ∀ (n : ℕ) (j : ℤ), (m : ℤ) < j →
      Limits.IsZero
        ((DerivedCategory.homologyFunctor (pullback f g).Modules j).obj (K n)))
    (hfibreBand : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), ¬ InBands m n j →
      Limits.IsZero ((DerivedCategory.homologyFunctor Y.Modules j).obj
        (fibreTransform f g (K n) F)))
    (hfibreStable : ∀ F : X.Modules, F.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp F) = 0 → ∀ (n : ℕ) (j : ℤ), 2 * m < n →
      -(m : ℤ) ≤ j → j ≤ (m : ℤ) →
      IsIso ((DerivedCategory.homologyFunctor Y.Modules j).map
        ((fibreTransformFunctor f g F).map (t n)))) :
    ∃ (N : ℕ) (A : DerivedCategory (pullback f g).Modules)
      (C : ℕ → DerivedCategory (pullback f g).Modules),
      RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) A ∧
      (∀ n, N ≤ n →
        RingedSpace.IsPerfect.{u, u + 1} (X := (pullback f g).toRingedSpace) (C n)) ∧
      (∀ i : ℤ, (i < -(m : ℤ) ∨ (m : ℤ) < i) →
        Limits.IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj A)) ∧
      (∀ n, N ≤ n → ∀ i : ℤ, (i < -(m : ℤ) - (n : ℤ) ∨ (m : ℤ) - (n : ℤ) < i) →
        Limits.IsZero ((DerivedCategory.homologyFunctor (pullback f g).Modules i).obj (C n))) ∧
      ∃ e : (∀ n : ℕ, N ≤ n → (K n ≅ A ⊞ C n)),
        ∀ (n : ℕ) (hn : N ≤ n),
          ∃ (a : A ≅ A) (c : C n ⟶ C (n + 1)),
            t n ≫ (e (n + 1) (by omega)).hom = (e n hn).hom ≫ biprod.map a.hom c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.9, Tag 0FYZ](https://stacks.math.columbia.edu/tag/0FYZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
