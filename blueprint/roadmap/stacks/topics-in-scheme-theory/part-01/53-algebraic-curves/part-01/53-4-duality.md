---
declaration: section
origin: cited
lean: Stacks.Duality.isDualizingComplex_dualizingComplexOverField, Stacks.Duality.isZero_homology_dualizingComplexOverField_of_ne, Stacks.Duality.dualizingSheafOverField_clauseTwo, Stacks.Duality.nontrivial_stalk_homology_zero_dualizingComplexOverField_iff, Stacks.Duality.dualizingComplexOverField_properties, Stacks.Duality.clauseFiveAddEquiv, Stacks.Duality.clauseFiveAddEquiv_naturality, Stacks.Duality.homDualizingSheafAddEquiv
statement: formalized
proof: formalized
---

# 53.4 Duality

Section 53.4 of the Stacks Project, [Tag 0E31](https://stacks.math.columbia.edu/tag/0E31). 6 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BS2, a lemma

[Tag 0BS2](https://stacks.math.columbia.edu/tag/0BS2) in the Stacks Project.

**`Stacks.Duality.isDualizingComplex_dualizingComplexOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean#L106). The attribute's comment: “the existence assertion: ω_X^• = f^× O_{Spec k} is a dualizing complex”.

> **`ω_X^• = f^×(𝒪_{Spec k})` is a dualizing complex** on a proper scheme over a field
> ([Stacks, Tag 0FVV]).

```lean
theorem isDualizingComplex_dualizingComplexOverField :
    letI := LocallyOfFiniteType.isLocallyNoetherian f
    IsDualizingComplex (dualizingComplexOverField f).obj
```

**`Stacks.Duality.isZero_homology_dualizingComplexOverField_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean#L122). The attribute's comment: “clause (1), at the constructed ω_X^• = f^× O_{Spec k}”.

> **[Stacks, Tag 0BS2], clause (1).** On a proper scheme of dimension at most one over a field,
> `H^i(ω_X^•)` is nonzero only for `i = -1, 0`.

```lean
theorem isZero_homology_dualizingComplexOverField_of_ne (hdim : topologicalKrullDim X ≤ 1)
    {i : ℤ} (hi : i ≠ -1) (hi0 : i ≠ 0) :
    IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj
      (dualizingComplexOverField f).obj)
```

**`Stacks.Duality.dualizingSheafOverField_clauseTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean#L205). The attribute's comment: “clause (2), at the constructed ω_X = H^{-1}(f^× O_{Spec k})”.

> **[Stacks, Tag 0BS2], clause (2).** On a proper scheme of dimension at most one over a field,
> `ω_X = H^{-1}(ω_X^•)` is a coherent Cohen--Macaulay module whose support is the union of the
> irreducible components of dimension `1`.

```lean
theorem dualizingSheafOverField_clauseTwo (hdim : topologicalKrullDim X ≤ 1) :
    _root_.SheafOfModules.IsCoherent (dualizingSheafOverField f) ∧
      SheafIsCohenMacaulay X (dualizingSheafOverField f) ∧
      _root_.SheafOfModules.supp (dualizingSheafOverField f) =
        ⋃₀ {C ∈ irreducibleComponents X | topologicalKrullDim C = 1}
```

**`Stacks.Duality.nontrivial_stalk_homology_zero_dualizingComplexOverField_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldClauses.lean#L217). The attribute's comment: “clause (3), at the constructed ω_X^• = f^× O_{Spec k}”.

> **[Stacks, Tag 0BS2], clause (3).** On a proper scheme of dimension at most one over a
> field, for `x ∈ X` closed the module `H^0(ω_{X,x}^•)` is nonzero if and only if either
> `dim 𝒪_{X,x} = 0`, or `dim 𝒪_{X,x} = 1` and `𝒪_{X,x}` is not Cohen--Macaulay.

```lean
theorem nontrivial_stalk_homology_zero_dualizingComplexOverField_iff
    (hdim : topologicalKrullDim X ≤ 1) {x : X} (hx : IsClosed ({x} : Set X)) :
    letI := LocallyOfFiniteType.isLocallyNoetherian f
    Nontrivial (moduleStalkAtPoint ((DerivedCategory.homologyFunctor X.Modules 0).obj
        (dualizingComplexOverField f).obj) x) ↔
      ringKrullDim (X.presheaf.stalk x) = 0 ∨
        ringKrullDim (X.presheaf.stalk x) = 1 ∧
          ¬ IsCohenMacaulayLocalRing (X.presheaf.stalk x)
```

**`Stacks.Duality.dualizingComplexOverField_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldExistence.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexOverFieldExistence.lean#L93).

> **[Stacks, Tag 0BS2].** Let `X` be a proper scheme of dimension at most one over a field `k`.
> The complex `ω_X^• = f^×(𝒪_{Spec k})` is a dualizing complex on `X`, and, writing
> `ω_X = H^{-1}(ω_X^•)`:
> 1. `H^i(ω_X^•)` is nonzero only for `i = -1, 0`;
> 2. `ω_X` is a coherent Cohen--Macaulay module whose support is the union of the irreducible
>    components of dimension `1`;
> 3. for `x ∈ X` closed, `H^0(ω_{X,x}^•)` is nonzero if and only if `dim 𝒪_{X,x} = 0`, or
>    `dim 𝒪_{X,x} = 1` and `𝒪_{X,x}` is not Cohen--Macaulay;
> 4. for `K` in `D_QCoh(𝒪_X)` the maps `Ext^i_X(K, ω_X^•) ⟶ Hom_k(H^{-i}(X, K), k)` are
>    isomorphisms, functorial in `K` and compatible with shifts and distinguished triangles;
> 5. there are functorial isomorphisms of `k`-vector spaces `Hom(ℱ, ω_X) = Hom_k(H^1(X, ℱ), k)`
>    for `ℱ` quasi-coherent;
> 6. if `X ⟶ Spec k` is smooth of relative dimension `1`, then `ω_X ≅ Ω_{X/k}`.

```lean
theorem dualizingComplexOverField_properties (hdim : topologicalKrullDim X ≤ 1) :
    letI := LocallyOfFiniteType.isLocallyNoetherian f
    letI := Scheme.linearOver f
    -- `ω_X^•` is a dualizing complex
    IsDualizingComplex (dualizingComplexOverField f).obj ∧
    -- (1)
    (∀ i : ℤ, ¬ IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj
      (dualizingComplexOverField f).obj) → i = -1 ∨ i = 0) ∧
    -- (2)
    (_root_.SheafOfModules.IsCoherent (dualizingSheafOverField f) ∧
      SheafIsCohenMacaulay X (dualizingSheafOverField f) ∧
      _root_.SheafOfModules.supp (dualizingSheafOverField f) =
        ⋃₀ {C ∈ irreducibleComponents X | topologicalKrullDim C = 1}) ∧
    -- (3)
    (∀ x : X, IsClosed ({x} : Set X) →
      (Nontrivial (moduleStalkAtPoint ((DerivedCategory.homologyFunctor X.Modules 0).obj
          (dualizingComplexOverField f).obj) x) ↔
        ringKrullDim (X.presheaf.stalk x) = 0 ∨
          ringKrullDim (X.presheaf.stalk x) = 1 ∧
            ¬ IsCohenMacaulayLocalRing (X.presheaf.stalk x))) ∧
    -- (4): isomorphisms on `D_QCoh(𝒪_X)`
    (∀ (K : quasiCoherentDerivedCategory X) (i : ℤ),
      Function.Bijective (dualityLinearMap f K.obj i)) ∧
    -- (4): functoriality
    (∀ (K L : DerivedCategory X.Modules) (i : ℤ) (g : K ⟶ L)
      (α : DerivedCategory.Ext L (dualizingComplexOverField f).obj i)
      (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
        ((derivedGlobalSectionsOver f).obj K)),
      dualityLinearMap f K i (g ≫ α) x =
        dualityLinearMap f L i α
          ((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).map
            ((derivedGlobalSectionsOver f).map g) x)) ∧
    -- (4): compatibility with shifts
    (∀ (K : DerivedCategory X.Modules) (i n : ℤ)
      (α : DerivedCategory.Ext K (dualizingComplexOverField f).obj i)
      (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-(i + n))).obj
        ((derivedGlobalSectionsOver f).obj (K⟦n⟧))),
      dualityLinearMap f (K⟦n⟧) (i + n) (ShiftedHom.comp (𝟙 (K⟦n⟧)) α rfl) x =
        dualityLinearMap f K i α
          ((((derivedGlobalSectionsOver f ⋙
            DerivedCategory.homologyFunctor (ModuleCat k) 0).shiftIso n (-(i + n)) (-i)
              (by omega)).hom.app K) x)) ∧
    -- (4): compatibility with distinguished triangles
    (∀ (T : Pretriangulated.Triangle (DerivedCategory X.Modules)) (i : ℤ)
      (α : DerivedCategory.Ext T.obj₁ (dualizingComplexOverField f).obj i)
      (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-(i + 1))).obj
        ((derivedGlobalSectionsOver f).obj T.obj₃)),
      dualityLinearMap f T.obj₃ (i + 1)
          (ShiftedHom.comp (T.mor₃ : DerivedCategory.Ext T.obj₃ T.obj₁ 1) α rfl) x =
        dualityLinearMap f T.obj₁ i α
          ((derivedGlobalSectionsOver f ⋙
            DerivedCategory.homologyFunctor (ModuleCat k) 0).homologySequenceδ T (-(i + 1)) (-i)
              (by omega) x)) ∧
    -- (5)
    (∃ e : ∀ F : X.Modules, F.IsQuasicoherent →
        ((F ⟶ dualizingSheafOverField f) ≃ₗ[k] (cohomologyOverField k f F 1 →ₗ[k] k)),
      ∀ (F G : X.Modules) (hF : F.IsQuasicoherent) (hG : G.IsQuasicoherent) (u : F ⟶ G)
        (φ : G ⟶ dualizingSheafOverField f),
        e F hF (u ≫ φ) = (e G hG φ).comp (cohomologyOverFieldMap k f u 1).hom) ∧
    -- (6)
    (SmoothOfRelativeDimension 1 f →
      Nonempty (dualizingSheafOverField f ≅ Scheme.Hom.relativeDifferentials f))
```

**`Stacks.Duality.clauseFiveAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafClauseFive.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafClauseFive.lean#L369). The attribute's comment: “clause (5)”.

> **Clause (5) of [Stacks, Tag 0BS2] at the dualizing sheaf of a proper curve**: for a
> quasi-coherent `ℱ` on a proper `X` of dimension at most one over `k`,
>
>   `Hom_{𝒪_X}(ℱ, ω_X) = Hom_k(H¹(X, ℱ), k)`.
>
> This is `Stacks.Duality.dualityAddEquiv` at `m = 1`, followed by the comparison
> `H¹(X, ℱ) = H¹(X, ℱ[0])` of `Stacks.Duality.cohomologyOverFieldIsoDerivedCohomologyOverField`.

```lean
def clauseFiveAddEquiv (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞)) (F : X.Modules)
    (hF : F.IsQuasicoherent) :
    (F ⟶ dualizingSheafOverField f) ≃+ (cohomologyOverField k f F 1 →ₗ[k] k)
```

**`Stacks.Duality.clauseFiveAddEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafClauseFive.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafClauseFive.lean#L441). The attribute's comment: “clause (5): naturality”.

> **Clause (5) of [Stacks, Tag 0BS2] is natural in the module**: precomposing a map to `ω_X`
> with `u` corresponds to precomposing the functional with `H¹(X, u)`.

```lean
theorem clauseFiveAddEquiv_naturality (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞))
    (F G : X.Modules) (hF : F.IsQuasicoherent) (hG : G.IsQuasicoherent) (u : F ⟶ G)
    (φ : G ⟶ dualizingSheafOverField f) :
    clauseFiveAddEquiv f hdim F hF (u ≫ φ) =
      (clauseFiveAddEquiv f hdim G hG φ).comp (cohomologyOverFieldMap k f u 1).hom
```

**`Stacks.Duality.homDualizingSheafAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafHom.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafHom.lean#L133). The attribute's comment: “clause (5)”.

> **[Stacks, Tag 0BS2], clause (5).** For a proper `f : X ⟶ Spec k` with `X` of dimension at
> most one and a quasi-coherent `𝒪_X`-module `ℱ` there is an isomorphism
>
>   `Hom_{𝒪_X}(ℱ, ω_X) = Hom_k(H^1(X, ℱ), k)`,
>
> where `ω_X = H^{-1}(ω_X^•)` is the dualizing sheaf. It is natural in `ℱ` by
> `Stacks.Duality.homDualizingSheafAddEquiv_naturality`.

```lean
def homDualizingSheafAddEquiv (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞)) (F : X.Modules)
    (hF : F.IsQuasicoherent) :
    (F ⟶ dualizingSheafOverField f) ≃+ (cohomologyOverField k f F 1 ⟶ ModuleCat.of k k)
```

**`Stacks.Duality.homDualizingSheafAddEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafHom.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafHom.lean#L172). The attribute's comment: “clause (5): naturality”.

> **[Stacks, Tag 0BS2], clause (5), is natural in `ℱ`**: the isomorphism
> `Hom_{𝒪_X}(ℱ, ω_X) = Hom_k(H^1(X, ℱ), k)` turns precomposition with `g : 𝒢 ⟶ ℱ` into
> precomposition with `H^1(X, g)`.

```lean
theorem homDualizingSheafAddEquiv_naturality (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞))
    {G F : X.Modules} (hG : G.IsQuasicoherent) (hF : F.IsQuasicoherent) (g : G ⟶ F)
    (α : F ⟶ dualizingSheafOverField f) :
    homDualizingSheafAddEquiv f hdim G hG (g ≫ α) =
      cohomologyOverFieldMap k f g 1 ≫ homDualizingSheafAddEquiv f hdim F hF α
```

**`Stacks.Duality.exists_natural_linearEquiv_hom_dualizingSheafOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafSmoothCurve.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafSmoothCurve.lean#L161). The attribute's comment: “clause (5): functorial isomorphisms of k-vector spaces Hom(F, ω_X) = Hom_k(H^1(X, F), k) for F quasi-coherent, at the constructed ω_X = H^{-1}(f^× O_{Spec k})”.

> **Clause (5) of [Stacks, Tag 0BS2]** for the constructed dualizing sheaf
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))`: for `X` proper of dimension at most one over `k` there are
> isomorphisms of `k`-vector spaces `Hom(ℱ, ω_X) = Hom_k(H¹(X, ℱ), k)` for `ℱ` quasi-coherent,
> functorial in `ℱ`. The `k`-structure on `Hom(ℱ, ω_X)` is the one `X.Modules` carries over `k`,
> `AlgebraicGeometry.Scheme.linearOver f`. The isomorphisms are
> `Stacks.Duality.clauseFiveLinearEquiv`, and their functoriality is
> `Stacks.Duality.clauseFiveAddEquiv_naturality`.

```lean
theorem exists_natural_linearEquiv_hom_dualizingSheafOverField [IsProper f]
    (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞)) :
    letI := Scheme.linearOver f
    ∃ e : ∀ F : X.Modules, F.IsQuasicoherent →
        ((F ⟶ dualizingSheafOverField f) ≃ₗ[k] (cohomologyOverField k f F 1 →ₗ[k] k)),
      ∀ (F G : X.Modules) (hF : F.IsQuasicoherent) (hG : G.IsQuasicoherent) (u : F ⟶ G)
        (φ : G ⟶ dualizingSheafOverField f),
        e F hF (u ≫ φ) = (e G hG φ).comp (cohomologyOverFieldMap k f u 1).hom
```

**`Stacks.Duality.nonempty_dualizingSheafOverField_iso_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafSmoothCurve.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingSheafSmoothCurve.lean#L209). The attribute's comment: “clause (6): ω_X ≅ Ω_{X/k} when X → Spec k is smooth of relative dimension 1, at the constructed ω_X = H^{-1}(f^× O_{Spec k})”.

> **Clause (6) of [Stacks, Tag 0BS2]**: if `f : X ⟶ Spec k` is proper and smooth of relative
> dimension one, the dualizing sheaf `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` is isomorphic to the sheaf of
> relative differentials `Ω_{X/k}`.
>
> The proof is that of [Stacks, Tag 0BRT] at `d = 1`; see the module documentation.

```lean
theorem nonempty_dualizingSheafOverField_iso_relativeDifferentials [IsProper f]
    [SmoothOfRelativeDimension 1 f] :
    Nonempty (dualizingSheafOverField f ≅ Scheme.Hom.relativeDifferentials f)
```

**`Stacks.Duality.extDualityAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean, line 583](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean#L583). The attribute's comment: “clause (4)”.

> **[Stacks, Tag 0BS2], clause (4).** For a quasi-compact quasi-separated morphism
> `f : X ⟶ Spec k` to the spectrum of a field and for every object `K` of `D_QCoh(𝒪_X)` there is an
> identification
>
>   `Ext^i_X(K, ω_X^•) = Hom_k(H^{-i}(X, K), k)`,
>
> where `ω_X^• = f^×(𝒪_{Spec k})` is the dualizing complex. It is an isomorphism of abelian groups,
> and it is natural in `K` by `Stacks.Duality.extDualityAddEquiv_naturality`.
>
> The source states this for `X` proper over `k` of dimension at most one; neither hypothesis is
> used, the identification being, as the source says, a matter of the construction of `ω_X^•`.
> `Stacks.Duality.extDualityAddEquivOfIsProper` is the statement at the source's own hypotheses.

```lean
def extDualityAddEquiv (K : quasiCoherentDerivedCategory X) (i : ℤ) :
    DerivedCategory.Ext K.obj (dualizingComplexOverField f).obj i ≃+
      (derivedCohomologyOverField f K.obj (-i) ⟶ ModuleCat.of k k)
```

**`Stacks.Duality.extDualityAddEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean#L602). The attribute's comment: “clause (4): naturality”.

> **Clause (4) of [Stacks, Tag 0BS2] is natural in `K`.** The identification
> `Ext^i_X(K, ω_X^•) = Hom_k(H^{-i}(X, K), k)` turns precomposition with `g : K ⟶ L` into
> postcomposition with `H^{-i}(X, g)`.

```lean
theorem extDualityAddEquiv_naturality (K L : quasiCoherentDerivedCategory X) (i : ℤ)
    (g : K.obj ⟶ L.obj)
    (α : DerivedCategory.Ext L.obj (dualizingComplexOverField f).obj i) :
    extDualityAddEquiv f K i (g ≫ α) =
      (DerivedCategory.homologyFunctor (ModuleCat.{u} k) (-i)).map
          ((derivedGlobalSectionsOver f).map g) ≫ extDualityAddEquiv f L i α
```

**`Stacks.Duality.extDualityAddEquiv_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean#L653). The attribute's comment: “clause (4): compatibility with the shift”.

> **Clause (4) of [Stacks, Tag 0BS2]: the identifications are compatible with the shift.**
> The degree-`i` identification at `K` is the degree-zero identification at `K⟦-i⟧`, transported
> along the canonical isomorphisms on the two sides: the shift adjunction
> `Ext^i_X(K, ω_X^•) = Hom_{D(𝒪_X)}(K⟦-i⟧, ω_X^•)` on the left, and the shift comparison
> `H^{-i}(X, K) = H^0(X, K⟦-i⟧)` of `Stacks.Duality.derivedCohomologyShiftNatIso` on the right.

```lean
theorem extDualityAddEquiv_shift (K : quasiCoherentDerivedCategory X) (i : ℤ)
    (α : DerivedCategory.Ext K.obj (dualizingComplexOverField f).obj i) :
    extDualityAddEquiv f K i α =
      (derivedCohomologyShiftIso f K.obj (-i)).inv ≫
        dualityAddEquivZero f (shiftQuasiCoherent K (-i)) (dualityStepShift f K i α)
```

**`Stacks.Duality.extDualityAddEquivOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean, line 667](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDuality.lean#L667). The attribute's comment: “clause (4) for a proper morphism”.

> **[Stacks, Tag 0BS2], clause (4), for a proper morphism** — the situation of the source.
> A proper morphism is quasi-compact and quasi-separated, so this is
> `Stacks.Duality.extDualityAddEquiv`; the source's bound on the dimension of `X` plays no part in
> this clause.

```lean
def extDualityAddEquivOfIsProper {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (CommRingCat.of k)) [IsProper f] (K : quasiCoherentDerivedCategory X)
    (i : ℤ) :
    DerivedCategory.Ext K.obj (dualizingComplexOverField f).obj i ≃+
      (derivedCohomologyOverField f K.obj (-i) ⟶ ModuleCat.of k k)
```

**`Stacks.Duality.extDualityLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDualityLinear.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ProperOverFieldDualityLinear.lean#L223). The attribute's comment: “clause (4) as an isomorphism of k-vector spaces for the k-linear structure over the base, which is what makes it count dimensions over k”.

> **[Stacks, Tag 0BS2], clause (4), as an isomorphism of `k`-vector spaces.** For a
> quasi-compact quasi-separated morphism `f : X ⟶ Spec k` and every object `K` of `D_QCoh(𝒪_X)`,
>
>   `Ext^i_X(K, ω_X^•) ≃ₗ[k] Hom_k(H^{-i}(X, K), k)`,
>
> where `ω_X^• = f^×(𝒪_{Spec k})` is the dualizing complex. This is
> `Stacks.Duality.extDualityAddEquiv` together with
> `Stacks.Duality.extDualityAddEquiv_smul`; the `k`-structure on the left is the one `X.Modules`
> carries over the base, and the `k`-linearity is what makes the identification count dimensions
> over `k`.

```lean
def extDualityLinearEquiv (K : quasiCoherentDerivedCategory X) (i : ℤ) :
    DerivedCategory.Ext K.obj (dualizingComplexOverField f).obj i ≃ₗ[k]
      (derivedCohomologyOverField f K.obj (-i) ⟶ ModuleCat.of k k)
```

## Tag 0BS3, a lemma

[Tag 0BS3](https://stacks.math.columbia.edu/tag/0BS3) in the Stacks Project.

**`Stacks.Duality.isDualizingModuleOf_dualizingSheafOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean#L81). The attribute's comment: “(1)”.

> **[Stacks, Tag 0BS3], clause (1).** Let `X` be a proper scheme over a field `k` which is
> Cohen–Macaulay and equidimensional of dimension one. Then `ω_X = H^{-1}(ω_X^•)` is a dualizing
> module on `X` in the sense of [Stacks, Section 0AWH]: `ω_X^• = f^×(𝒪_{Spec k})` is a dualizing
> complex, `-1` is the least degree in which it has nonzero cohomology, and `ω_X` is that
> cohomology sheaf.

```lean
theorem isDualizingModuleOf_dualizingSheafOverField
    (hcm : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    IsDualizingModuleOf (dualizingSheafOverField f) (dualizingComplexOverField f).obj (-1)
```

**`Stacks.Duality.dualizingSheafOverField_isCoherent_isCohenMacaulay_supp_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean#L105). The attribute's comment: “(2)”.

> **[Stacks, Tag 0BS3], clause (2).** Let `X` be a proper scheme over a field `k` which is
> Cohen–Macaulay and equidimensional of dimension one. Then `ω_X = H^{-1}(ω_X^•)` is a coherent
> Cohen–Macaulay `𝒪_X`-module ([Stacks, Tag 0343]) whose support is `X`.

```lean
theorem dualizingSheafOverField_isCoherent_isCohenMacaulay_supp_eq_univ
    (hcm : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) :
    _root_.SheafOfModules.IsCoherent (dualizingSheafOverField f) ∧
      AlgebraicGeometry.SheafIsCohenMacaulay X (dualizingSheafOverField f) ∧
      _root_.SheafOfModules.supp (dualizingSheafOverField f) = Set.univ
```

**`Stacks.Duality.exists_extDualityShiftOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean#L217). The attribute's comment: “(3)”.

> **[Stacks, Tag 0BS3], clause (3).** Let `X` be a proper scheme over a field `k` which is
> Cohen–Macaulay and equidimensional of dimension one, and `ω_X = H^{-1}(ω_X^•)`. There are
> isomorphisms
>
>   `Ext^i_X(K, ω_X[1]) = Hom_k(H^{-i}(X, K), k)`
>
> for `K ∈ D_QCoh(𝒪_X)` and `i ∈ ℤ`, functorial in `K` and compatible with shifts: they come from
> isomorphisms `Hom(K, ω_X[1]) = Hom_k(H^0(X, K), k)`, functorial in `K`, by reading
> `Ext^i_X(K, ω_X[1])` as `Hom(K⟦-i⟧, ω_X[1])` (the shift adjunction) and `H^{-i}(X, K)` as
> `H^0(X, K⟦-i⟧)`.

```lean
theorem exists_extDualityShiftOne
    (hcm : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) :
    ∃ (e : ∀ (K : quasiCoherentDerivedCategory X) (i : ℤ),
        DerivedCategory.Ext K.obj (dualizingSheafShiftOne f) i ≃+
          (derivedCohomologyOverField f K.obj (-i) ⟶ ModuleCat.of k k))
      (e₀ : ∀ K : quasiCoherentDerivedCategory X,
        (K.obj ⟶ dualizingSheafShiftOne f) ≃+
          (derivedCohomologyOverField f K.obj 0 ⟶ ModuleCat.of k k)),
      (∀ (K L : quasiCoherentDerivedCategory X) (i : ℤ) (g : K.obj ⟶ L.obj)
          (α : DerivedCategory.Ext L.obj (dualizingSheafShiftOne f) i),
        e K i (g ≫ α) =
          (DerivedCategory.homologyFunctor (ModuleCat.{u} k) (-i)).map
            ((derivedGlobalSectionsOver f).map g) ≫ e L i α) ∧
      (∀ (K L : quasiCoherentDerivedCategory X) (g : K.obj ⟶ L.obj)
          (β : L.obj ⟶ dualizingSheafShiftOne f),
        e₀ K (g ≫ β) =
          (DerivedCategory.homologyFunctor (ModuleCat.{u} k) 0).map
            ((derivedGlobalSectionsOver f).map g) ≫ e₀ L β) ∧
      (∀ (K : quasiCoherentDerivedCategory X) (i : ℤ)
          (α : DerivedCategory.Ext K.obj (dualizingSheafShiftOne f) i),
        e K i α = (derivedCohomologyShiftIso f K.obj (-i)).inv ≫
          e₀ (shiftQuasiCoherent K (-i))
            (((shiftEquiv' (DerivedCategory X.Modules) (-i) i (by omega)).toAdjunction.homEquiv
              K.obj (dualizingSheafShiftOne f)).symm α))
```

**`Stacks.Duality.exists_extSuccDuality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/CohenMacaulayCurveDuality.lean#L297). The attribute's comment: “(4)”.

> **[Stacks, Tag 0BS3], clause (4).** Let `X` be a proper scheme over a field `k` which is
> Cohen–Macaulay and equidimensional of dimension one, and `ω_X = H^{-1}(ω_X^•)`. There are
> isomorphisms
>
>   `Ext^{1 + i}_X(ℱ, ω_X) = Hom_k(H^{-i}(X, ℱ), k)`
>
> for quasi-coherent `ℱ` on `X` and `i ∈ ℤ`, functorial in `ℱ`.

```lean
theorem exists_extSuccDuality
    (hcm : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) :
    ∃ e : ∀ (F : X.Modules) (_ : F.IsQuasicoherent) (i : ℤ),
        DerivedCategory.Ext ((DerivedCategory.singleFunctor X.Modules 0).obj F)
            ((DerivedCategory.singleFunctor X.Modules 0).obj (dualizingSheafOverField f))
            (1 + i) ≃+
          (derivedCohomologyOverField f ((DerivedCategory.singleFunctor X.Modules 0).obj F) (-i) ⟶
            ModuleCat.of k k),
      ∀ (F G : X.Modules) (hF : F.IsQuasicoherent) (hG : G.IsQuasicoherent) (i : ℤ) (u : F ⟶ G)
        (α : DerivedCategory.Ext ((DerivedCategory.singleFunctor X.Modules 0).obj G)
          ((DerivedCategory.singleFunctor X.Modules 0).obj (dualizingSheafOverField f)) (1 + i)),
        e F hF i ((DerivedCategory.singleFunctor X.Modules 0).map u ≫ α) =
          (DerivedCategory.homologyFunctor (ModuleCat.{u} k) (-i)).map
              ((derivedGlobalSectionsOver f).map
                ((DerivedCategory.singleFunctor X.Modules 0).map u)) ≫
            e G hG i α
```

## Tag 0BS4, a remark

[Tag 0BS4](https://stacks.math.columbia.edu/tag/0BS4) in the Stacks Project.

**`AlgebraicGeometry.finrank_cohomologyOverField_one_eq_zero_tensorPowerModuleNegOneTensorDualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DualizingInvertibleDimensionDuality.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/DualizingInvertibleDimensionDuality.lean#L98). The attribute's comment: “the fourth display, dim_k H^1(X, L) = dim_k H^0(X, L^(tensor -1) tensor omega_X), at an invertible L and the dualizing sheaf of Tag 0BS2, for every proper X of dimension at most one over k; the Remark's Cohen-Macaulay and equidimensionality conditions are not needed”.

> **`dim_k H¹(X, ℒ) = dim_k H⁰(X, ℒ^{⊗ -1} ⊗ ω_X)`** for an invertible `𝒪_X`-module `ℒ` on a
> proper scheme `X` of dimension at most one over a field `k`, with
> `ω_X = H^{-1}(f^×(𝒪_{Spec k}))` the dualizing sheaf of [Stacks, Tag 0BS2].
>
> This is the last of the four formulas displayed in [Stacks, Tag 0BS4]. The proof is the duality
> of dimensions at a vector bundle,
> `AlgebraicGeometry.finrank_cohomologyOverField_zero_dualTensorDualizingSheafOverField_eq_one`,
> at `ℒ` itself — an invertible module being finite locally free of rank one — with the dual `ℒ^∨`
> rewritten as the inverse `ℒ^{⊗ -1}` by the last clause of [Stacks, Tag 0B8K]. Neither the
> Cohen--Macaulay nor the equidimensionality condition under which the Remark states it is
> used.

```lean
public theorem finrank_cohomologyOverField_one_eq_zero_tensorPowerModuleNegOneTensorDualizing
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞)) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] :
    Module.finrank k (cohomologyOverField k f L 1) =
      Module.finrank k (cohomologyOverField k f
        ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf,
            CategoryTheory.Presheaf.isSheaf_of_isSheaf_comp _ X.presheaf
              (CategoryTheory.forget₂ CommRingCat RingCat) X.ringCatSheaf.property⟩).obj
            (tensorPowerModule L (-1))).obj (Stacks.Duality.dualizingSheafOverField f))) 0)
```

**`AlgebraicGeometry.finrank_cohomologyOverField_zero_eq_one_tensorPowerModuleNegOneTensorDualizing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/DualizingInvertibleDimensionDuality.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/DualizingInvertibleDimensionDuality.lean#L128). The attribute's comment: “the third display, dim_k H^0(X, L) = dim_k H^1(X, L^(tensor -1) tensor omega_X), for X proper over k, Cohen-Macaulay and equidimensional of dimension one, at the dualizing sheaf of Tag 0BS2”.

> **`dim_k H⁰(X, ℒ) = dim_k H¹(X, ℒ^{⊗ -1} ⊗ ω_X)`** for an invertible `𝒪_X`-module `ℒ` on a
> proper scheme `X` over a field `k` which is Cohen--Macaulay and equidimensional of dimension one,
> with `ω_X` the dualizing sheaf of [Stacks, Tag 0BS2].
>
> This is the third display of [Stacks, Tag 0BS4], and the source's proof: the second display at
> `ℰ = ℒ` and `i = 0`, `Hom_k(H⁰(X, ℒ), k) ≃ₗ[k] H¹(X, ℒ^∨ ⊗ ω_X)`, which is
> `Stacks.Duality.LocallyFreeTwist.dualityTensorDualizingSheafLinearEquiv`, together with the
> equality of the dimensions of a vector space and of its dual, and the identification of the dual
> `ℒ^∨` with the inverse `ℒ^{⊗ -1}` ([Stacks, Tag 0B8K]).

```lean
public theorem finrank_cohomologyOverField_zero_eq_one_tensorPowerModuleNegOneTensorDualizing
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f]
    (hcm : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) (L : X.Modules)
    [SheafOfModules.IsInvertible X.presheaf X.ringCatSheaf.2 L] :
    Module.finrank k (cohomologyOverField k f L 0) =
      Module.finrank k (cohomologyOverField k f
        ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf,
            CategoryTheory.Presheaf.isSheaf_of_isSheaf_comp _ X.presheaf
              (CategoryTheory.forget₂ CommRingCat RingCat) X.ringCatSheaf.property⟩).obj
            (tensorPowerModule L (-1))).obj (Stacks.Duality.dualizingSheafOverField f))) 1)
```

**`Stacks.Duality.LocallyFreeTwist.dualityDerivedTensorLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LocallyFreeDualizingDuality.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LocallyFreeDualizingDuality.lean#L246). The attribute's comment: “the first display, Hom_k(H^{-i}(X, E), k) = H^i(X, E^dual tensor^L omega^bullet), as an isomorphism of k-vector spaces, for E finite locally free; for every quasi-compact quasi-separated X over k, of which a proper X of dimension at most one is a case”.

> **[Stacks, Tag 0BS4], first display**: for a finite locally free `E` with dual `E^∨`,
>
>   `Hom_k(H^{-i}(X, E), k) ≃ₗ[k] H^i(X, E^∨ ⊗^L ω_X^•)`,
>
> with `ω_X^•` the dualizing complex of [Stacks, Tag 0BS2] and `⊗^L` the derived tensor product of
> [Stacks, Tag 06YU]. The source assumes `X` proper of dimension at most one over `k`; only the
> quasi-compactness and quasi-separatedness of `f`, under which clause (4) of Tag 0BS2 holds, are
> used.

```lean
def dualityDerivedTensorLinearEquiv (i : ℤ) :
    Module.Dual k (derivedCohomologyOverField f ((DerivedCategory.singleFunctor X.Modules 0).obj E)
        (-i)) ≃ₗ[k]
      derivedCohomologyOverField f (((Stacks.Duality.derivedTensor X).obj
        ((DerivedCategory.singleFunctor X.Modules 0).obj (dual E))).obj
          (dualizingComplexOverField f).obj) i
```

**`Stacks.Duality.LocallyFreeTwist.dualityTensorDualizingSheafLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LocallyFreeDualizingDuality.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LocallyFreeDualizingDuality.lean#L316). The attribute's comment: “the second display, Hom_k(H^{-i}(X, E), k) = H^{1+i}(X, E^dual tensor omega_X), as an isomorphism of k-vector spaces, for X proper over k, Cohen-Macaulay and equidimensional of dimension one, and E finite locally free”.

> **[Stacks, Tag 0BS4], second display**: if `X` is proper over `k`, Cohen--Macaulay and
> equidimensional of dimension one, then for a finite locally free `E` with dual `E^∨`,
>
>   `Hom_k(H^{-i}(X, E), k) ≃ₗ[k] H^{1+i}(X, E^∨ ⊗_{𝒪_X} ω_X)`,
>
> with `ω_X` the dualizing sheaf of [Stacks, Tag 0BS2]. This is the first display with
> `ω_X^• = ω_X[1]` of [Stacks, Tag 0BS3] substituted.

```lean
def dualityTensorDualizingSheafLinearEquiv [IsProper f]
    (hcm : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) (i : ℤ) :
    Module.Dual k (derivedCohomologyOverField f ((DerivedCategory.singleFunctor X.Modules 0).obj E)
        (-i)) ≃ₗ[k]
      derivedCohomologyOverField f ((DerivedCategory.singleFunctor X.Modules 0).obj
        (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} (R X)).obj (dual E)).obj
          (dualizingSheafOverField f))) (1 + i)
```

**`Stacks.Duality.LocallyFreeTwist.dualityTensorDualizingSheafLinearEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/LocallyFreeDualizingDuality.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/LocallyFreeDualizingDuality.lean#L548). The attribute's comment: “the second display: the canonical isomorphism is natural in the finite locally free E, for the dual map E_2^dual -> E_1^dual of E_1 -> E_2”.

> **The second display of [Stacks, Tag 0BS4] is natural in `E`**: for `g : E₁ ⟶ E₂` between
> finite locally free modules, precomposition with `H^{-i}(X, g)` corresponds to
> `H^{1+i}(X, g^∨ ⊗ ω_X)`, `g^∨` being the dual of `g`.

```lean
theorem dualityTensorDualizingSheafLinearEquiv_naturality [IsProper f]
    (hcm : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (hdim : topologicalKrullDim X = 1) (i : ℤ)
    (φ : Module.Dual k (derivedCohomologyOverField f
      ((DerivedCategory.singleFunctor X.Modules 0).obj E₂) (-i))) :
    dualityTensorDualizingSheafLinearEquiv E₁ f hcm hequi hdim i
        (φ ∘ₗ ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) (-i)).map
          ((derivedGlobalSectionsOver f).map
            ((DerivedCategory.singleFunctor X.Modules 0).map g))).hom) =
      ((DerivedCategory.homologyFunctor (ModuleCat.{u} k) (1 + i)).map
        ((derivedGlobalSectionsOver f).map ((DerivedCategory.singleFunctor X.Modules 0).map
          (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} (R X)).map
            (dualMap g)).app (dualizingSheafOverField f))))).hom
        (dualityTensorDualizingSheafLinearEquiv E₂ f hcm hequi hdim i φ)
```

## Tag 0E32, a lemma

[Tag 0E32](https://stacks.math.columbia.edu/tag/0E32) in the Stacks Project.

**`Stacks.Duality.nonempty_dualizingComplexOverField_baseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexBaseChange.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexBaseChange.lean#L103). The attribute's comment: “part (2)”.

> Let `X` be a proper scheme over a field `k`, let `K/k` be a field extension and `X' = X_K`
> the base change, with projection `g'`. Then the pullbacks of `ω_X^•` and `ω_X` to `X'` are the
> dualizing complex and the dualizing sheaf of [Stacks, Tag 0BS2] for `X' ⟶ Spec K`:
> `L(g')^*ω_X^• ≅ ω_{X'}^•` and `(g')^*ω_X ≅ ω_{X'}`. No hypothesis on `dim X` is needed.

```lean
theorem nonempty_dualizingComplexOverField_baseChange_iso :
    haveI := isProper_of_isPullback_specMapAlgebraMap k K g' f' f h
    Nonempty ((quasiCoherentDerivedPullback' g').obj (dualizingComplexOverField f) ≅
        dualizingComplexOverField f') ∧
      Nonempty ((Scheme.Modules.pullback g').obj (dualizingSheafOverField f) ≅
        dualizingSheafOverField f')
```

**`Stacks.Duality.dualizingComplexOverFieldFactorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexFactorization.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexFactorization.lean#L509). The attribute's comment: “part (1), in the form the proof states it: omega_X^bullet over k is omega_X^bullet over k', along which the properties of Tag 0BS2 over k' transfer; omega_X is dualizingSheafOverFieldFactorIso and clause (4) over k' is extDualityAddEquivOfFactor”.

> **[Stacks, Tag 0E32], part (1).** Let `X` be proper over a field `k` and suppose
> `X ⟶ Spec k` factors as `X ⟶ Spec k' ⟶ Spec k` for a field `k'`. Then the dualizing complex
> `ω_X^•` of `X` over `k` is the dualizing complex of `X` over `k'`; hence `ω_X^•` and `ω_X`
> satisfy the properties of [Stacks, Tag 0BS2] with `k` replaced by `k'`.
>
> As in the source, `k'/k` is finite because `k' ⊆ H⁰(X, 𝒪_X)`
> (`Stacks.Duality.finite_of_isProper_comp`), and the two dualizing complexes both represent
> `K ↦ Hom(H⁰(X, K), -)`, the `k`-dual and the `k'`-dual corresponding through a nonzero
> `k`-linear form on `k'` (`Stacks.Duality.dualizingComplexOverFieldChangeIsoOfForm`).

```lean
noncomputable def dualizingComplexOverFieldFactorIso (hf : f' ≫ Spec.map φ = f) :
    haveI := isProper_of_comp_eq f φ f' hf
    dualizingComplexOverField f ≅ dualizingComplexOverField f'
```

## Tag 0E33, a lemma

[Tag 0E33](https://stacks.math.columbia.edu/tag/0E33) in the Stacks Project.

**`Stacks.Duality.dualizingComplexOverField_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexClosedSubscheme.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/DualizingComplexClosedSubscheme.lean#L277).

> **Stacks Project, Tag 0E33.** Let `X` be a proper scheme of dimension at most one over a
> field `k` and let `i : Y ⟶ X` be a closed immersion, with dualizing complexes and dualizing
> sheaves `ω_X^•, ω_X, ω_Y^•, ω_Y` as in [Stacks, Tag 0BS2]. Then
> 1. `ω_Y^• = R𝓗om(𝒪_Y, ω_X^•)`;
> 2. `ω_Y = 𝓗om(𝒪_Y, ω_X)` and `i_*ω_Y = 𝓗om_{𝒪_X}(i_*𝒪_Y, ω_X)`.

```lean
theorem dualizingComplexOverField_closedImmersion
    (hdim : topologicalKrullDim X ≤ (1 : WithBot ℕ∞)) :
    Nonempty ((dualizingComplexOverField (i ≫ f)).obj ≅
        (LocallySmall.derivedSheafHomExactSupport i).obj (dualizingComplexOverField f).obj) ∧
      Nonempty (dualizingSheafOverField (i ≫ f) ≅
        (closedQuotient i).sheafHomExactSupport.obj (dualizingSheafOverField f)) ∧
      Nonempty ((Scheme.Modules.pushforward i).obj (dualizingSheafOverField (i ≫ f)) ≅
        (closedQuotient i).homSheafFromPushforwardStructureSheaf.obj
          (dualizingSheafOverField f))
```

## Tag 0E34, a lemma

[Tag 0E34](https://stacks.math.columbia.edu/tag/0E34) in the Stacks Project.

**`Stacks.Curves.dualizingSheafOverField_closedSubcurve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/ComplementaryCurve/DualizingSheaf.lean, line 963](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Curves/ComplementaryCurve/DualizingSheaf.lean#L963). The attribute's comment: “in (2) and (4) the source swaps the roles of i and j: the forms stated are I = j_* I', J = i_* J', omega_Z = I'(j^* omega_X) and j_* omega_Z = I omega_X”.

> **Stacks Project, Tag 0E34.** Let `X` be a proper scheme over a field which is Gorenstein,
> reduced, and equidimensional of dimension one. Let `C` cut out a reduced closed subscheme
> `i : Y ⟶ X` equidimensional of dimension one, let `j : Z ⟶ X` be the scheme-theoretic closure of
> `X \ Y`, cut out by `𝓙 = complementaryCurveIdeal C`, and let `Y ∩ Z` be cut out by `𝓘 ⊔ 𝓙`. With
> `𝓘'` and `𝓙'` the ideals of `Y ∩ Z` in `Z` and in `Y`:
> 1. `Y` and `Z` are Cohen–Macaulay;
> 2. `𝓘 = j_*𝓘'` and `𝓙 = i_*𝓙'`, read on affine opens;
> 3. `ω_Y ≅ 𝓙'(i^*ω_X)` and `i_*ω_Y ≅ 𝓙ω_X`;
> 4. `ω_Z ≅ 𝓘'(j^*ω_X)` and `j_*ω_Z ≅ 𝓘ω_X`;
> 5. the six short exact sequences of
>    `Stacks.Curves.dualizingSheafOverField_closedSubcurve_of_isInvertible`.
>
> Since `X` is Gorenstein and its closed points have one-dimensional local rings, `ω_X` is
> invertible (`AlgebraicGeometry.isInvertible_dualizingSheafOverField`), and the statement is
> `Stacks.Curves.dualizingSheafOverField_closedSubcurve_of_isInvertible`.

```lean
theorem dualizingSheafOverField_closedSubcurve [IsReduced X] [IsGorenstein X]
    (hXeq : TopologicalSpace.Equidimensional X) (hXdim : topologicalKrullDim X = 1)
    (C : X.IdealSheafData) [IsReduced C.subscheme]
    (hYeq : TopologicalSpace.Equidimensional C.subscheme)
    (hYdim : topologicalKrullDim C.subscheme = 1) :
    -- (1)
    (IsCohenMacaulay C.subscheme ∧ IsCohenMacaulay (complementaryCurve C)) ∧
    -- (2)
    (∀ U : X.affineOpens,
      Set.BijOn ((complementaryCurveIdeal C).subschemeι.app U.1) (C.ideal U)
        ((Scheme.IdealSheafData.inclusion
            (le_sup_right : complementaryCurveIdeal C ≤
              intersectionWithComplementaryCurveIdeal C)).ker.ideal
          ⟨(complementaryCurveIdeal C).subschemeι ⁻¹ᵁ U.1, U.2.preimage _⟩) ∧
      Set.BijOn (C.subschemeι.app U.1) ((complementaryCurveIdeal C).ideal U)
        ((Scheme.IdealSheafData.inclusion
            (le_sup_left : C ≤ intersectionWithComplementaryCurveIdeal C)).ker.ideal
          ⟨C.subschemeι ⁻¹ᵁ U.1, U.2.preimage _⟩)) ∧
    -- (3)
    (Nonempty (Stacks.Duality.dualizingSheafOverField (C.subschemeι ≫ f) ≅
        (Stacks.Algebraization.idealPowerMultiple
          (Scheme.IdealSheafData.inclusion
            (le_sup_left : C ≤ intersectionWithComplementaryCurveIdeal C)).ker 1
          ((Scheme.Modules.pullback C.subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField f))).toSheafOfModules) ∧
      Nonempty ((Scheme.Modules.pushforward C.subschemeι).obj
          (Stacks.Duality.dualizingSheafOverField (C.subschemeι ≫ f)) ≅
        (Stacks.Algebraization.idealPowerMultiple (complementaryCurveIdeal C) 1
          (Stacks.Duality.dualizingSheafOverField f)).toSheafOfModules)) ∧
    -- (4)
    (Nonempty (Stacks.Duality.dualizingSheafOverField
          ((complementaryCurveIdeal C).subschemeι ≫ f) ≅
        (Stacks.Algebraization.idealPowerMultiple
          (Scheme.IdealSheafData.inclusion
            (le_sup_right : complementaryCurveIdeal C ≤
              intersectionWithComplementaryCurveIdeal C)).ker 1
          ((Scheme.Modules.pullback (complementaryCurveIdeal C).subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField f))).toSheafOfModules) ∧
      Nonempty ((Scheme.Modules.pushforward (complementaryCurveIdeal C).subschemeι).obj
          (Stacks.Duality.dualizingSheafOverField ((complementaryCurveIdeal C).subschemeι ≫ f)) ≅
        (Stacks.Algebraization.idealPowerMultiple C 1
          (Stacks.Duality.dualizingSheafOverField f)).toSheafOfModules)) ∧
    -- (5)
    ((∃ (a : Stacks.Duality.dualizingSheafOverField f ⟶
          (Scheme.Modules.pushforward C.subschemeι).obj
            ((Scheme.Modules.pullback C.subschemeι).obj
              (Stacks.Duality.dualizingSheafOverField f)) ⊞
          (Scheme.Modules.pushforward (complementaryCurveIdeal C).subschemeι).obj
            ((Scheme.Modules.pullback (complementaryCurveIdeal C).subschemeι).obj
              (Stacks.Duality.dualizingSheafOverField f)))
        (b : (Scheme.Modules.pushforward C.subschemeι).obj
            ((Scheme.Modules.pullback C.subschemeι).obj
              (Stacks.Duality.dualizingSheafOverField f)) ⊞
          (Scheme.Modules.pushforward (complementaryCurveIdeal C).subschemeι).obj
            ((Scheme.Modules.pullback (complementaryCurveIdeal C).subschemeι).obj
              (Stacks.Duality.dualizingSheafOverField f)) ⟶
          (Scheme.Modules.pushforward (intersectionWithComplementaryCurveIdeal C).subschemeι).obj
            (SheafOfModules.unit (intersectionWithComplementaryCurve C).ringCatSheaf))
        (w : a ≫ b = 0), (ShortComplex.mk a b w).ShortExact) ∧
      (∃ (a : (Scheme.Modules.pushforward C.subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField (C.subschemeι ≫ f)) ⟶
            Stacks.Duality.dualizingSheafOverField f)
        (b : Stacks.Duality.dualizingSheafOverField f ⟶
          (Scheme.Modules.pushforward (complementaryCurveIdeal C).subschemeι).obj
            ((Scheme.Modules.pullback (complementaryCurveIdeal C).subschemeι).obj
              (Stacks.Duality.dualizingSheafOverField f)))
        (w : a ≫ b = 0), (ShortComplex.mk a b w).ShortExact) ∧
      (∃ (a : (Scheme.Modules.pushforward (complementaryCurveIdeal C).subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField ((complementaryCurveIdeal C).subschemeι ≫ f)) ⟶
            Stacks.Duality.dualizingSheafOverField f)
        (b : Stacks.Duality.dualizingSheafOverField f ⟶
          (Scheme.Modules.pushforward C.subschemeι).obj
            ((Scheme.Modules.pullback C.subschemeι).obj (Stacks.Duality.dualizingSheafOverField f)))
        (w : a ≫ b = 0), (ShortComplex.mk a b w).ShortExact) ∧
      (∃ (a : (Scheme.Modules.pushforward C.subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField (C.subschemeι ≫ f)) ⊞
          (Scheme.Modules.pushforward (complementaryCurveIdeal C).subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField ((complementaryCurveIdeal C).subschemeι ≫ f)) ⟶
            Stacks.Duality.dualizingSheafOverField f)
        (b : Stacks.Duality.dualizingSheafOverField f ⟶
          (Scheme.Modules.pushforward (intersectionWithComplementaryCurveIdeal C).subschemeι).obj
            (SheafOfModules.unit (intersectionWithComplementaryCurve C).ringCatSheaf))
        (w : a ≫ b = 0), (ShortComplex.mk a b w).ShortExact) ∧
      (∃ (a : Stacks.Duality.dualizingSheafOverField (C.subschemeι ≫ f) ⟶
          (Scheme.Modules.pullback C.subschemeι).obj (Stacks.Duality.dualizingSheafOverField f))
        (b : (Scheme.Modules.pullback C.subschemeι).obj (Stacks.Duality.dualizingSheafOverField f) ⟶
          (Scheme.Modules.pushforward (Scheme.IdealSheafData.inclusion
            (le_sup_left : C ≤ intersectionWithComplementaryCurveIdeal C))).obj
            (SheafOfModules.unit (intersectionWithComplementaryCurve C).ringCatSheaf))
        (w : a ≫ b = 0), (ShortComplex.mk a b w).ShortExact) ∧
      (∃ (a : Stacks.Duality.dualizingSheafOverField
            ((complementaryCurveIdeal C).subschemeι ≫ f) ⟶
          (Scheme.Modules.pullback (complementaryCurveIdeal C).subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField f))
        (b : (Scheme.Modules.pullback (complementaryCurveIdeal C).subschemeι).obj
            (Stacks.Duality.dualizingSheafOverField f) ⟶
          (Scheme.Modules.pushforward (Scheme.IdealSheafData.inclusion
            (le_sup_right : complementaryCurveIdeal C ≤
              intersectionWithComplementaryCurveIdeal C))).obj
            (SheafOfModules.unit (intersectionWithComplementaryCurve C).ringCatSheaf))
        (w : a ≫ b = 0), (ShortComplex.mk a b w).ShortExact))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.4, Tag 0E31](https://stacks.math.columbia.edu/tag/0E31)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
