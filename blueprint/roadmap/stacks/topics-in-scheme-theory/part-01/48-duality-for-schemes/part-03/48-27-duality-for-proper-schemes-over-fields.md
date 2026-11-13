---
declaration: section
origin: cited
lean: Stacks.Duality.dualityEquiv, Stacks.Duality.dualityEquiv_comp, Stacks.Duality.dualityEquiv_shiftedHomComp, Stacks.Duality.dualityLinearMap_shift, Stacks.Duality.dualityLinearMap_triangle, Stacks.Duality.isDualizingComplex_relativeDualizingComplex_of_isProper, Stacks.Duality.le_zero_and_le_dim_of_not_isZero_homology_of_isProper, Stacks.Duality.relativeDualizingModule_of_isProper
statement: formalized
proof: formalized
---

# 48.27 Duality for proper schemes over fields

Section 48.27 of the Stacks Project, [Tag 0FVU](https://stacks.math.columbia.edu/tag/0FVU). 7 tags here are carried by 36 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FVV, a lemma

[Tag 0FVV](https://stacks.math.columbia.edu/tag/0FVV) in the Stacks Project.

**`Stacks.Duality.dualityEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean#L367). The attribute's comment: “part (5): the isomorphisms Ext^i\_X(K, ω\_X) = Hom\_k(H^\{-i}(X, K), k)”.

> **The duality isomorphisms.** Let `X` be a proper scheme over a field `k` and
> `ω_X^• = a(𝒪_{Spec k})` its relative dualizing complex. For `K` in `D_QCoh(𝒪_X)` and every `i`
> there is a `k`-linear isomorphism `Ext^i_X(K, ω_X^•) ≅ Hom_k(H^{-i}(X, K), k)`, sending `α` to
> `t ∘ H^{-i}(X, α)` with `t : H⁰(X, ω_X^•) ⟶ k` the trace (`Stacks.Duality.traceOverField`); it is
> natural in `K` (`Stacks.Duality.dualityEquiv_comp`) and compatible with shifts and distinguished
> triangles (`Stacks.Duality.dualityEquiv_shiftedHomComp`,
> `Stacks.Duality.dualityEquiv_triangle`).

```lean
def dualityEquiv (K : quasiCoherentDerivedCategory X) (i : ℤ) :
    letI := Scheme.linearOver f
    DerivedCategory.Ext K.obj (ωX).obj i ≃ₗ[k]
      ((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
        ((derivedGlobalSectionsOver f).obj K.obj) →ₗ[k] k)
```

**`Stacks.Duality.dualityEquiv_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean#L389). The attribute's comment: “part (5): the isomorphisms are functorial in K”.

> **Part (5) of [Stacks, Tag 0FVV], functoriality.** The duality isomorphisms are natural in
> `K`: for `g : K ⟶ L` in `D(𝒪_X)` and `α ∈ Ext^i_X(L, ω_X^•)`, the linear form attached to
> `g ≫ α` is the one attached to `α` precomposed with `H^{-i}(X, g)`.

```lean
theorem dualityEquiv_comp (K L : quasiCoherentDerivedCategory X) (i : ℤ) (g : K.obj ⟶ L.obj)
    (α : DerivedCategory.Ext L.obj (ωX).obj i)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
      ((derivedGlobalSectionsOver f).obj K.obj)) :
    letI := Scheme.linearOver f
    dualityEquiv f K i (g ≫ α) x =
      dualityEquiv f L i α
        ((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).map
          ((derivedGlobalSectionsOver f).map g) x)
```

**`Stacks.Duality.dualityEquiv_shiftedHomComp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean#L409). The attribute's comment: “part (5): compatibility with shifts and distinguished triangles”.

> **Part (5) of [Stacks, Tag 0FVV], compatibility with shifted morphisms.** For
> `β ∈ Ext^j_X(L, K)` and `α ∈ Ext^i_X(K, ω_X^•)`, the linear form on `H^{-(i+j)}(X, L)` attached to
> the product `β.comp α ∈ Ext^{i+j}_X(L, ω_X^•)` is the one attached to `α` precomposed with the map
> `H^{-(i+j)}(X, L) ⟶ H^{-i}(X, K)` induced by `β`. Taking for `β` the identity of `K⟦n⟧` gives
> compatibility with shifts (`Stacks.Duality.dualityLinearMap_shift`), and taking for `β` the third
> morphism of a distinguished triangle gives compatibility with its connecting maps
> (`Stacks.Duality.dualityLinearMap_triangle`).

```lean
theorem dualityEquiv_shiftedHomComp (K L : quasiCoherentDerivedCategory X) {i j c : ℤ}
    (β : DerivedCategory.Ext L.obj K.obj j) (α : DerivedCategory.Ext K.obj (ωX).obj i)
    (h : i + j = c)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-c)).obj
      ((derivedGlobalSectionsOver f).obj L.obj)) :
    letI := Scheme.linearOver f
    dualityEquiv f L c (β.comp α h) x =
      dualityEquiv f K i α ((HX).shiftMap β (-c) (-i) (by omega) x)
```

**`Stacks.Duality.dualityLinearMap_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean#L426). The attribute's comment: “part (5): compatibility with shifts”.

> **Compatibility of the duality map with shifts.** Under `Ext^\{i+n}\_X(K⟦n⟧, ω\_X^•) =
> Ext^i\_X(K, ω\_X^•)` (composition with the identity of `K⟦n⟧`, an element of `Ext^n\_X(K⟦n⟧, K)`) and
> the canonical isomorphism `H^{-(i+n)}(X, K⟦n⟧) ≅ H^{-i}(X, K)`, the duality maps of `K⟦n⟧` and
> of `K` agree.

```lean
theorem dualityLinearMap_shift (K : DerivedCategory X.Modules) (i n : ℤ)
    (α : DerivedCategory.Ext K (ωX).obj i)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-(i + n))).obj
      ((derivedGlobalSectionsOver f).obj (K⟦n⟧))) :
    letI := Scheme.linearOver f
    dualityLinearMap f (K⟦n⟧) (i + n)
        (ShiftedHom.comp (𝟙 (K⟦n⟧)) α rfl) x =
      dualityLinearMap f K i α
        (((HX).shiftIso n (-(i + n)) (-i) (by omega)).hom.app K x)
```

**`Stacks.Duality.dualityLinearMap_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/Duality.lean#L444). The attribute's comment: “part (5): compatibility with distinguished triangles”.

> **Compatibility of the duality map with distinguished triangles.** For a triangle
> `K ⟶ L ⟶ M ⟶ K⟦1⟧` of `D(𝒪_X)`, the duality maps intertwine composition with its third morphism,
> `Ext^i_X(K, ω_X^•) ⟶ Ext^{i+1}_X(M, ω_X^•)`, and the connecting morphism
> `H^{-(i+1)}(X, M) ⟶ H^{-i}(X, K)` of the long exact cohomology sequence.

```lean
theorem dualityLinearMap_triangle (T : Pretriangulated.Triangle (DerivedCategory X.Modules))
    (i : ℤ) (α : DerivedCategory.Ext T.obj₁ (ωX).obj i)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-(i + 1))).obj
      ((derivedGlobalSectionsOver f).obj T.obj₃)) :
    letI := Scheme.linearOver f
    dualityLinearMap f T.obj₃ (i + 1)
        (ShiftedHom.comp (T.mor₃ : DerivedCategory.Ext T.obj₃ T.obj₁ 1) α rfl) x =
      dualityLinearMap f T.obj₁ i α
        ((HX).homologySequenceδ T (-(i + 1)) (-i) (by omega) x)
```

**`Stacks.Duality.isDualizingComplex_relativeDualizingComplex_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean#L75). The attribute's comment: “existence: ω\_X^• = a(O\_\{Spec k}) is a dualizing complex”.

> **[Stacks, Tag 0FVV], existence.** For `X` proper over a field `k`, the complex
> `ω_X^• = a(𝒪_{Spec k})` is a dualizing complex on `X`.

```lean
theorem isDualizingComplex_relativeDualizingComplex_of_isProper :
    letI := LocallyOfFiniteType.isLocallyNoetherian f
    IsDualizingComplex (relativeDualizingComplex f
      (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
      (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj
```

**`Stacks.Duality.le_zero_and_le_dim_of_not_isZero_homology_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean#L85). The attribute's comment: “part (1): H^i(ω\_X^•) is nonzero only for i ∈ [-dim X, 0]”.

> **[Stacks, Tag 0FVV], part (1).** `H^i(ω_X^•)` is nonzero only for `i ∈ [-dim X, 0]`.

```lean
theorem le_zero_and_le_dim_of_not_isZero_homology_of_isProper (i : ℤ)
    (hi : ¬ Limits.IsZero ((DerivedCategory.homologyFunctor X.Modules i).obj
      (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj)) :
    i ≤ 0 ∧ (((-i).toNat : ℕ) : WithBot ℕ∞) ≤ topologicalKrullDim X
```

**`Stacks.Duality.relativeDualizingModule_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean#L97). The attribute's comment: “part (2): ω\_X is a coherent (S₂)-module supported on the components of dimension dim X”.

> **[Stacks, Tag 0FVV], part (2).** `ω_X = H^{-dim X}(ω_X^•)` is a coherent module with property
> `(S₂)` whose support is the union of the irreducible components of dimension `dim X`.

```lean
theorem relativeDualizingModule_of_isProper :
    (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).IsCoherent ∧
    SheafHasPropertySk X (relativeDualizingModule f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))) 2 ∧
    _root_.SheafOfModules.supp (relativeDualizingModule f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))) =
      ⋃₀ {C ∈ irreducibleComponents X | topologicalKrullDim C = topologicalKrullDim X}
```

**`Stacks.Duality.topologicalKrullDim_supp_homology_le_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean#L113). The attribute's comment: “part (3): dim Supp H^i(ω\_X^•) ≤ -i”.

> **[Stacks, Tag 0FVV], part (3).** The support of `H^i(ω_X^•)` has dimension at most `-i`
> (and is empty for `i > 0`).

```lean
theorem topologicalKrullDim_supp_homology_le_of_isProper (i : ℤ) :
    topologicalKrullDim (_root_.SheafOfModules.supp
        ((DerivedCategory.homologyFunctor X.Modules i).obj
          (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj)) ≤
      if i ≤ 0 then (((-i).toNat : ℕ) : WithBot ℕ∞) else ⊥
```

**`Stacks.Duality.exists_nontrivial_stalk_homology_iff_depth_le_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean#L126). The attribute's comment: “part (4): H^i(ω\_\{X,x}^•) ⊕ … ⊕ H^0(ω\_\{X,x}^•) ≠ 0 iff depth(O\_\{X,x}) ≤ -i, at closed points”.

> **[Stacks, Tag 0FVV], part (4).** For `x ∈ X` closed, one of `H^i(ω_{X,x}^•)`, …,
> `H^0(ω_{X,x}^•)` is nonzero if and only if `depth(𝒪_{X,x}) ≤ -i`.

```lean
theorem exists_nontrivial_stalk_homology_iff_depth_le_of_isProper {x : X}
    (hx : IsClosed ({x} : Set X)) (i : ℤ) :
    (∃ j : ℤ, i ≤ j ∧ j ≤ 0 ∧ Nontrivial (moduleStalkAtPoint
        ((DerivedCategory.homologyFunctor X.Modules j).obj
          (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj) x)) ↔
      i ≤ 0 ∧ Module.depth (X.presheaf.stalk x) (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
        (X.presheaf.stalk x) ≤ ((-i).toNat : ℕ∞)
```

**`Stacks.Duality.dualizingModuleHomEquivOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean#L150). The attribute's comment: “part (6): Hom(F, ω\_X) = Hom\_k(H^\{dim X}(X, F), k) for F quasi-coherent”.

> **[Stacks, Tag 0FVV], part (6).** For `F` quasi-coherent on `X` there is a `k`-linear
> isomorphism `Hom_X(F, ω_X) ≅ Hom_k(H^{dim X}(X, F), k)`, natural in `F`
> (`Stacks.Duality.dualizingModuleHomEquivOfIsProper_comp`).

```lean
def dualizingModuleHomEquivOfIsProper (F : X.Modules) [F.IsQuasicoherent] :
    letI := Scheme.linearOver f
    (F ⟶ relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (CommRingCat.of k)))) ≃ₗ[k]
      (cohomologyOverField k f F (ENat.toNat ((topologicalKrullDim X).getD 0)) →ₗ[k] k)
```

**`Stacks.Duality.dualizingModuleHomEquivOfIsProper_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplex.lean#L160). The attribute's comment: “part (6): the isomorphisms are functorial in F”.

> **[Stacks, Tag 0FVV], part (6), functoriality.** The isomorphisms of part (6) are natural in
> the quasi-coherent module `F`.

```lean
theorem dualizingModuleHomEquivOfIsProper_comp {F G : X.Modules} [F.IsQuasicoherent]
    [G.IsQuasicoherent] (φ : F ⟶ G)
    (v : G ⟶ relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (CommRingCat.of k))))
    (x : cohomologyOverField k f F (ENat.toNat ((topologicalKrullDim X).getD 0))) :
    letI := Scheme.linearOver f
    dualizingModuleHomEquivOfIsProper f F (φ ≫ v) x =
      dualizingModuleHomEquivOfIsProper f G v
        ((cohomologyOverFieldFunctor k f (ENat.toNat ((topologicalKrullDim X).getD 0))).map
          φ x)
```

**`Stacks.Duality.boundedCoherent_relativeDualizingComplex_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplexCharacterization.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplexCharacterization.lean#L57). The attribute's comment: “footnote to part (5): ω\_X^• is in D^b\_Coh(O\_X)”.

> **[Stacks, Tag 0FVV], footnote to part (5): `ω_X^•` lies in `D^b_Coh(𝒪_X)`.** Its cohomology
> sheaves are coherent ([Stacks, Tag 0A89]) and vanish outside `[-dim X, 0]` (part (1)).

```lean
theorem boundedCoherent_relativeDualizingComplex_of_isProper :
    DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X)
      (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj
```

**`Stacks.Duality.existsUnique_iso_relativeDualizingComplex_of_quasiCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplexCharacterization.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplexCharacterization.lean#L127). The attribute's comment: “footnote to part (5): the isomorphisms characterize ω\_X^• in D\_QCoh(O\_X) up to unique isomorphism”.

> **[Stacks, Tag 0FVV], footnote to part (5): the duality isomorphisms characterize `ω_X^•` in
> `D_QCoh(𝒪_X)` up to unique isomorphism.** If `ω ∈ D_QCoh(𝒪_X)` has bijections
> `Hom(K, ω) ≃ Hom_k(H⁰(X, K), k)` natural in `K ∈ D_QCoh(𝒪_X)`, then exactly one isomorphism
> `ω ≅ ω_X^•` carries them to the duality isomorphisms of `ω_X^•` (degree zero of part (5)).

```lean
theorem existsUnique_iso_relativeDualizingComplex_of_quasiCoherent
    (ω : quasiCoherentDerivedCategory X)
    (φ : ∀ K : quasiCoherentDerivedCategory X, (K.obj ⟶ ω.obj) ≃
      ((DerivedCategory.homologyFunctor (ModuleCat k) 0).obj
        ((derivedGlobalSectionsOver f).obj K.obj) ⟶ ModuleCat.of k k))
    (hφ : ∀ {K L : quasiCoherentDerivedCategory X} (g : K.obj ⟶ L.obj) (α : L.obj ⟶ ω.obj),
      φ K (g ≫ α) =
        (DerivedCategory.homologyFunctor (ModuleCat k) 0).map
          ((derivedGlobalSectionsOver f).map g) ≫ φ L α) :
    ∃! e : ω.obj ≅ (relativeDualizingComplex f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj,
      ∀ (K : quasiCoherentDerivedCategory X) (α : K.obj ⟶ ω.obj),
        (DerivedCategory.homologyFunctor (ModuleCat k) 0).map
          ((derivedGlobalSectionsOver f).map (α ≫ e.hom)) ≫ traceOverField f = φ K α
```

**`Stacks.Duality.existsUnique_iso_relativeDualizingComplex_of_boundedCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplexCharacterization.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/DualizingComplexCharacterization.lean#L156). The attribute's comment: “footnote to part (5): ω\_X^• is characterized by the isomorphisms for K in D^b\_Coh(O\_X)”.

> **[Stacks, Tag 0FVV], footnote to part (5): it suffices to consider `K ∈ D^b_Coh(𝒪_X)`.** If
> `ω ∈ D^b_Coh(𝒪_X)` has bijections `Hom(K, ω) ≃ Hom_k(H⁰(X, K), k)` natural in
> `K ∈ D^b_Coh(𝒪_X)`, then exactly one isomorphism `ω ≅ ω_X^•` carries them to the duality
> isomorphisms of `ω_X^•`; this uses that `ω_X^•` lies in `D^b_Coh(𝒪_X)`
> (`Stacks.Duality.boundedCoherent_relativeDualizingComplex_of_isProper`).

```lean
theorem existsUnique_iso_relativeDualizingComplex_of_boundedCoherent
    (ω : DerivedCategory X.Modules)
    (hω : DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X) ω)
    (φ : ∀ K : DerivedCategory X.Modules,
      DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X) K →
      ((K ⟶ ω) ≃ ((DerivedCategory.homologyFunctor (ModuleCat k) 0).obj
        ((derivedGlobalSectionsOver f).obj K) ⟶ ModuleCat.of k k)))
    (hφ : ∀ {K L : DerivedCategory X.Modules}
      (hK : DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X) K)
      (hL : DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X) L)
      (g : K ⟶ L) (α : L ⟶ ω),
      φ K hK (g ≫ α) =
        (DerivedCategory.homologyFunctor (ModuleCat k) 0).map
          ((derivedGlobalSectionsOver f).map g) ≫ φ L hL α) :
    ∃! e : ω ≅ (relativeDualizingComplex f
        (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj,
      ∀ (K : DerivedCategory X.Modules)
        (hK : DerivedCategoryB.derivedCategoryBBounded (A := X.Modules) (isCoherentSheaf X) K)
        (α : K ⟶ ω),
        (DerivedCategory.homologyFunctor (ModuleCat k) 0).map
          ((derivedGlobalSectionsOver f).map (α ≫ e.hom)) ≫ traceOverField f = φ K hK α
```

**`Stacks.Duality.nonempty_relativeDualizingComplex_iso_and_relativeDualizingModule_iso_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/SmoothDualizingModule.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/SmoothDualizingModule.lean#L81). The attribute's comment: “part (7): for X smooth of relative dimension d over k, ω\_X^• ≅ ∧^d Ω\_\{X/k}[d] and ω\_X ≅ ∧^d Ω\_\{X/k}”.

> **[Stacks, Tag 0FVV], part (7).** Let `X` be proper over a field `k`, with
> `ω_X^• = a(𝒪_{Spec k})`. If `X ⟶ Spec k` is smooth of relative dimension `d`, then
> `ω_X^• ≅ ∧^d Ω_{X/k}[d]` and `ω_X ≅ ∧^d Ω_{X/k}`.

```lean
theorem nonempty_relativeDualizingComplex_iso_and_relativeDualizingModule_iso_of_smooth
    {k : Type u} [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] (d : ℕ)
    [SmoothOfRelativeDimension d f] :
    haveI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    haveI : QuasiSeparatedSpace X := quasiSeparatedSpace_of_quasiSeparated f
    Nonempty ((relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))).obj ≅
      (DerivedCategory.singleFunctor X.Modules (-d)).obj
        (Scheme.Modules.exteriorPower (Scheme.Hom.relativeDifferentials f) d)) ∧
    Nonempty (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k))) ≅
      Scheme.Modules.exteriorPower (Scheme.Hom.relativeDifferentials f) d)
```

## Tag 0FVW, a remark

[Tag 0FVW](https://stacks.math.columbia.edu/tag/0FVW) in the Stacks Project.

**`Stacks.Duality.dualityEquiv_id_eq_traceOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean#L190). The attribute's comment: “the identity of ω\_X^• corresponds via 0FVV (5) to the trace t : H^0(X, ω\_X^•) → k”.

> **The identity of `ω_X^•` corresponds to the trace.** Under the isomorphism of part (5) of
> [Stacks, Tag 0FVV] in degree zero, `Hom(ω_X^•, ω_X^•) ≅ Hom_k(H⁰(X, ω_X^•), k)`, the identity
> of `ω_X^•` is sent to the trace `t : H⁰(X, ω_X^•) ⟶ k`.

```lean
theorem dualityEquiv_id_eq_traceOverField :
    letI := Scheme.linearOver f
    dualityEquiv f ωX 0 (ShiftedHom.mk₀ (0 : ℤ) rfl (𝟙 (ωX).obj)) = (traceOverField f).hom
```

**`Stacks.Duality.dualityEquiv_mk₀_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean#L202). The attribute's comment: “the degree-zero pairing Hom\_X(K, ω\_X^•) × H^0(X, K) → k, (α, β) ↦ t(α(β))”.

> **The degree-zero pairing.** For `K` in `D_QCoh(𝒪_X)`, the identification
> `Hom(K, ω_X^•) ≅ H⁰(X, K)^∨` of part (5) of [Stacks, Tag 0FVV] is the pairing
> `(α, β) ↦ t(α(β))`, where `α(β)` is the image of `β ∈ H⁰(X, K)` under the map
> `H⁰(X, K) ⟶ H⁰(X, ω_X^•)` induced by `α`.

```lean
theorem dualityEquiv_mk₀_apply (K : quasiCoherentDerivedCategory X) (α : K.obj ⟶ (ωX).obj)
    (β : (H⁰).obj ((derivedGlobalSectionsOver f).obj K.obj)) :
    letI := Scheme.linearOver f
    dualityEquiv f K 0 (ShiftedHom.mk₀ (0 : ℤ) rfl α) β =
      (traceOverField f).hom (((H⁰).map ((derivedGlobalSectionsOver f).map α)).hom β)
```

**`Stacks.Duality.dualityEquiv_apply_eq_traceOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean#L217). The attribute's comment: “the pairing Ext^i\_X(K, ω\_X^•) × H^\{-i}(X, K) → k, (α, β) ↦ t(α(β)), with α a morphism K[-i] → ω\_X^• and β in H^0(X, K[-i])”.

> **The pairing in degree `i`.** For `K` in `D_QCoh(𝒪_X)` and `i ∈ ℤ`, the identification
> `Ext^i_X(K, ω_X^•) ≅ H^{-i}(X, K)^∨` of part (5) of [Stacks, Tag 0FVV] is the pairing
> `(α, β) ↦ t(α(β))`: here `α` is regarded as a morphism `K⟦-i⟧ ⟶ ω_X^•` (`extShiftHom`), `β` as an
> element of `H⁰(X, K⟦-i⟧) ≅ H^{-i}(X, K)`, and `α(β) ∈ H⁰(X, ω_X^•)` is the image of `β` under
> the map that `α` induces on `H⁰(X, -)`.

```lean
theorem dualityEquiv_apply_eq_traceOverField (K : quasiCoherentDerivedCategory X) (i : ℤ)
    (α : DerivedCategory.Ext K.obj (ωX).obj i)
    (β : (DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
      ((derivedGlobalSectionsOver f).obj K.obj)) :
    letI := Scheme.linearOver f
    dualityEquiv f K i α β =
      (traceOverField f).hom (((H⁰).map ((derivedGlobalSectionsOver f).map (extShiftHom α))).hom
        ((((HX).shiftIso (-i) 0 (-i) (add_zero _)).inv.app K.obj).hom β))
```

**`Stacks.Duality.bijective_dualityLinearMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean#L247). The attribute's comment: “the pairing identifies Ext^i\_X(K, ω\_X^•) with the k-linear dual of H^\{-i}(X, K)”.

> **The pairing is nondegenerate on one side.** For `K` in `D_QCoh(𝒪_X)` and every `i`, the
> pairing `(α, β) ↦ t(α(β))` of `Ext^i_X(K, ω_X^•)` with `H^{-i}(X, K)` identifies
> `Ext^i_X(K, ω_X^•)` with the `k`-linear dual of `H^{-i}(X, K)`.

```lean
theorem bijective_dualityLinearMap (K : quasiCoherentDerivedCategory X) (i : ℤ) :
    letI := Scheme.linearOver f
    Function.Bijective (dualityLinearMap f K.obj i)
```

**`Stacks.Duality.exists_not_bijective_dualityLinearMap_flip`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean#L282). The attribute's comment: “the 'not vice versa' clause: on X = Spec k some K in D\_QCoh has H^0(X, K) → Hom\_X(K, ω\_X^•)^∨ not bijective”.

> **The pairing is in general not nondegenerate on the other side** (the clause "but in general
> not vice versa" of [Stacks, Tag 0FVW]). For every field `k`, on the proper scheme `X = Spec k`
> there is an object `K` of `D_QCoh(𝒪_X)` for which the other-side map
> `H⁰(X, K) ⟶ Hom_X(K, ω_X^•)^∨`, `β ↦ (α ↦ t(α(β)))`, is not bijective: take for `K` the object
> with `RΓ(X, K) = k^{(ℕ)}[0]` ([Stacks, Tag 06Z0]), whose `H⁰(X, K) = k^{(ℕ)}` is infinite
> dimensional, so that the evaluation map into its double dual is not surjective.

```lean
theorem exists_not_bijective_dualityLinearMap_flip (k : Type u) [Field k] :
    ∃ K : quasiCoherentDerivedCategory (Spec (.of k)),
      letI := Scheme.linearOver (𝟙 (Spec (.of k)))
      ¬ Function.Bijective (dualityLinearMap (𝟙 (Spec (.of k))) K.obj 0).flip
```

**`Stacks.Duality.finiteDimensional_and_isPerfPair_of_coherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/TracePairing.lean#L315). The attribute's comment: “K in D^b\_Coh: Hom\_X(K, ω\_X^•), Ext^i\_X(K, ω\_X^•), H^i(X, K) are finite dimensional and the pairings are perfect”.

> **The coherent case.** For `K` in `D^b_Coh(𝒪_X)`, the `k`-vector spaces
> `Hom_X(K, ω_X^•)`, `Ext^i_X(K, ω_X^•)` and `H^n(X, K)` are finite dimensional, and for every `i`
> the pairing `Ext^i_X(K, ω_X^•) × H^{-i}(X, K) ⟶ k`, `(α, β) ↦ t(α(β))`, is perfect.

```lean
theorem finiteDimensional_and_isPerfPair_of_coherent (K : DerivedCategory X.Modules)
    (hK : DerivedCategoryB.derivedCategoryBBounded (fun M : X.Modules => M.IsCoherent) K) :
    letI := Scheme.linearOver f
    FiniteDimensional k (K ⟶ (ωX).obj) ∧
      (∀ i : ℤ, FiniteDimensional k (DerivedCategory.Ext K (ωX).obj i)) ∧
      (∀ n : ℤ, FiniteDimensional k ((DerivedCategory.homologyFunctor (ModuleCat k) n).obj
        ((derivedGlobalSectionsOver f).obj K))) ∧
      ∀ i : ℤ, (dualityLinearMap f K i).IsPerfPair
```

## Tag 0FVX, a remark

[Tag 0FVX](https://stacks.math.columbia.edu/tag/0FVX) in the Stacks Project.

**`Stacks.Duality.coherentTracePairing_isPerfPair_and_dualMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CoherentTracePairing.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CoherentTracePairing.lean#L114).

> **[Stacks, Tag 0FVX].** Let `X` be a proper scheme over a field `k`, `ω_X^•` and
> `t : H⁰(X, ω_X^•) ⟶ k` as in [Stacks, Tag 0FVW], and `i ∈ ℤ`.
> 1. For a coherent `𝒪_X`-module `ℱ`, `Ext^i_X(ℱ, ω_X^•)` and `H^{-i}(X, ℱ)` are finite dimensional
>    and the pairing `⟨α, β⟩ = t(α(β))` between them (`α` regarded as a morphism
>    `ℱ[-i] ⟶ ω_X^•`, `β` as an element of `H⁰(X, ℱ[-i])`) is perfect.
> 2. For a homomorphism `φ : ℱ ⟶ 𝒢` of coherent `𝒪_X`-modules, `⟨α ∘ φ, β⟩ = ⟨α, φ(β)⟩` for
>    `α ∈ Ext^i_X(𝒢, ω_X^•)` and `β ∈ H^{-i}(X, ℱ)`.
> 3. For a homomorphism `φ : ℱ ⟶ 𝒢` of quasi-coherent `𝒪_X`-modules, the map
>    `Ext^i_X(𝒢, ω_X^•) ⟶ Ext^i_X(ℱ, ω_X^•)` induced by `φ` is, via the identifications of
>    `Ext^i_X(-, ω_X^•)` with `H^{-i}(X, -)^∨` given by the pairings, the `k`-linear dual of the map
>    `H^{-i}(X, ℱ) ⟶ H^{-i}(X, 𝒢)` induced by `φ`.

```lean
theorem coherentTracePairing_isPerfPair_and_dualMap (i : ℤ) :
    letI := Scheme.linearOver f
    (∀ F : X.Modules, F.IsCoherent →
      FiniteDimensional k (DerivedCategory.Ext ((single₀).obj F) (ωX).obj i) ∧
      FiniteDimensional k ((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
        ((derivedGlobalSectionsOver f).obj ((single₀).obj F))) ∧
      (dualityLinearMap f ((single₀).obj F) i).IsPerfPair ∧
      ∀ (α : DerivedCategory.Ext ((single₀).obj F) (ωX).obj i)
        (β : (DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
          ((derivedGlobalSectionsOver f).obj ((single₀).obj F))),
        dualityLinearMap f ((single₀).obj F) i α β =
          (traceOverField f).hom
            (((H⁰).map ((derivedGlobalSectionsOver f).map (extShiftHom α))).hom
              ((((HX).shiftIso (-i) 0 (-i) (add_zero _)).inv.app ((single₀).obj F)).hom β))) ∧
    (∀ (F G : X.Modules) (φ : F ⟶ G), F.IsCoherent → G.IsCoherent →
      ∀ (α : DerivedCategory.Ext ((single₀).obj G) (ωX).obj i)
        (β : (DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
          ((derivedGlobalSectionsOver f).obj ((single₀).obj F))),
        dualityLinearMap f ((single₀).obj F) i ((single₀).map φ ≫ α) β =
          dualityLinearMap f ((single₀).obj G) i α
            (((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).map
              ((derivedGlobalSectionsOver f).map ((single₀).map φ))).hom β)) ∧
    ∀ (F G : X.Modules) (φ : F ⟶ G) (hF : F.IsQuasicoherent) (hG : G.IsQuasicoherent),
      (dualityEquiv f (singleQuasiCoherent F hF 0) i).toLinearMap ∘ₗ
          extPrecompLinearMap f ((single₀).map φ) i =
        ((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).map
            ((derivedGlobalSectionsOver f).map ((single₀).map φ))).hom.dualMap ∘ₗ
          (dualityEquiv f (singleQuasiCoherent G hG 0) i).toLinearMap
```

## Tag 0FVY, a lemma

[Tag 0FVY](https://stacks.math.columbia.edu/tag/0FVY) in the Stacks Project.

**`Stacks.Duality.isPerfPair_dualityCupPairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/PerfectPairing.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/PerfectPairing.lean#L324). References: SGA 4½ Fonctions L (3.7), “special case”.

> **[Stacks, Tag 0FVY].** Let `X` be a proper scheme over a field `k`, with structure morphism
> `f : X ⟶ Spec k`, let `ω_X^•` be its dualizing complex of [Stacks, Tag 0FVV] and
> `t : H⁰(X, ω_X^•) ⟶ k` the trace of [Stacks, Tag 0FVW]. Let `E ∈ D(𝒪_X)` be perfect. Then for
> every `i` the pairing
>
> `Hⁱ(X, ω_X^• ⊗^𝐋 E^∨) × H⁻ⁱ(X, E) ⟶ k`, `(ξ, η) ↦ t((1 ⊗ ε)(ξ ∪ η))`
>
> is perfect: both spaces are finite-dimensional `k`-vector spaces and the pairing is a perfect
> pairing (`LinearMap.IsPerfPair`: each side is identified with the `k`-linear dual of the other).
> Here `∪` is the cup product of Cohomology, Section 0FKU (`cupPairing` at the canonical global cup
> product), `E^∨ = R𝓗om(E, 𝒪_X)` and `ε : E^∨ ⊗^𝐋 E ⟶ 𝒪_X` is the evaluation of Cohomology,
> Example 0FPC, and `1 ⊗ ε : (ω_X^• ⊗^𝐋 E^∨) ⊗^𝐋 E ⟶ ω_X^•` is followed by the unit constraint
> (`dualityCupPairing`). The cohomology groups are the `Γ(X, 𝒪_X)`-modules of hypercohomology with
> the scalars restricted along `k ⟶ Γ(X, 𝒪_X)`, and `t` is `Stacks.Duality.traceOverField` read on
> them (`traceStd`).

```lean
theorem isPerfPair_dualityCupPairing
    (hE : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) E) (i : ℤ) :
    FiniteDimensional k ((ModuleCat.restrictScalars.{u} (globalRingHom f)).obj
        (cohomologyModule (tensorDual X.toRingedSpace (dualizingComplexStd f) E) i)) ∧
      FiniteDimensional k
        ((ModuleCat.restrictScalars.{u} (globalRingHom f)).obj (cohomologyModule E (-i))) ∧
      (dualityCupPairing f E i).IsPerfPair
```

## Tag 0FVZ, a lemma

[Tag 0FVZ](https://stacks.math.columbia.edu/tag/0FVZ) in the Stacks Project.

**`Stacks.Duality.isDualizingModuleOf_relativeDualizingModule_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L184). The attribute's comment: “part (1): ω\_X is a dualizing module on X (Section 0AWH)”.

> **[Stacks, Tag 0FVZ], part (1).** Let `X` be a proper scheme over a field `k` which is
> Cohen--Macaulay and equidimensional of dimension `d`. The module `ω_X` of [Stacks, Tag 0FVV] is a
> dualizing module on `X` in the sense of [Stacks, Section 0AWH]: `ω_X^•` is a dualizing complex,
> `-d` is the least degree in which it has nonzero cohomology, and `ω_X = H^{-d}(ω_X^•)`.

```lean
theorem isDualizingModuleOf_relativeDualizingModule_of_isProper
    (hCM : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X)
    (d : ℕ) (hd : topologicalKrullDim X = d) :
    letI := LocallyOfFiniteType.isLocallyNoetherian f
    IsDualizingModuleOf ωM (ωX).obj (-(d : ℤ))
```

**`Stacks.Duality.relativeDualizingModule_isCoherent_cohenMacaulay_supp_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L218). The attribute's comment: “part (2): ω\_X is a coherent Cohen-Macaulay module whose support is X”.

> **[Stacks, Tag 0FVZ], part (2).** Let `X` be a proper scheme over a field `k` which is
> Cohen--Macaulay and equidimensional of dimension `d`. The module `ω_X` of [Stacks, Tag 0FVV] is a
> coherent Cohen--Macaulay `𝒪_X`-module whose support is `X`.

```lean
theorem relativeDualizingModule_isCoherent_cohenMacaulay_supp_of_isProper
    (hCM : AlgebraicGeometry.IsCohenMacaulay X) (hequi : TopologicalSpace.Equidimensional X) :
    (ωM).IsCoherent ∧ AlgebraicGeometry.SheafIsCohenMacaulay X ωM ∧
      _root_.SheafOfModules.supp ωM = Set.univ
```

**`Stacks.Duality.dualityEquivShiftOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L245). The attribute's comment: “part (3): the isomorphisms Ext^i\_X(K, ω\_X[d]) = Hom\_k(H^\{-i}(X, K), k)”.

> **[Stacks, Tag 0FVZ], part (3), the isomorphisms.** Let `X` be a proper scheme over a field `k`
> which is Cohen--Macaulay and equidimensional of dimension `d`. For `K` in `D_QCoh(𝒪_X)` and every
> `i` there is a `k`-linear isomorphism `Ext^i_X(K, ω_X[d]) ≅ Hom_k(H^{-i}(X, K), k)`. It is part (5)
> of [Stacks, Tag 0FVV] (`Stacks.Duality.dualityEquiv`) read through `ω_X^• ≅ ω_X[d]`
> (`Stacks.Duality.relativeDualizingComplexIsoShiftOfIsProper`); it is natural in `K`
> (`Stacks.Duality.dualityEquivShiftOfIsProper_comp`) and compatible with shifts and distinguished
> triangles (`Stacks.Duality.dualityEquivShiftOfIsProper_shiftedHomComp`,
> `Stacks.Duality.dualityEquivShiftOfIsProper_shift`,
> `Stacks.Duality.dualityEquivShiftOfIsProper_triangle`).

```lean
def dualityEquivShiftOfIsProper (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    (K : quasiCoherentDerivedCategory X) (i : ℤ) :
    letI := Scheme.linearOver f
    DerivedCategory.Ext K.obj (((DerivedCategory.singleFunctor X.Modules 0).obj ωM)⟦(d : ℤ)⟧) i
      ≃ₗ[k] ((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
        ((derivedGlobalSectionsOver f).obj K.obj) →ₗ[k] k)
```

**`Stacks.Duality.dualityEquivShiftOfIsProper_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L276). The attribute's comment: “part (3): the isomorphisms are functorial in K”.

> **[Stacks, Tag 0FVZ], part (3), functoriality.** The isomorphisms of part (3) are natural in
> `K`: for `g : K ⟶ L` and `α ∈ Ext^i_X(L, ω_X[d])`, the linear form attached to `g ≫ α` is the one
> attached to `α` precomposed with `H^{-i}(X, g)`.

```lean
theorem dualityEquivShiftOfIsProper_comp (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    (K L : quasiCoherentDerivedCategory X) (i : ℤ) (g : K.obj ⟶ L.obj)
    (α : DerivedCategory.Ext L.obj
      (((DerivedCategory.singleFunctor X.Modules 0).obj ωM)⟦(d : ℤ)⟧) i)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-i)).obj
      ((derivedGlobalSectionsOver f).obj K.obj)) :
    letI := Scheme.linearOver f
    dualityEquivShiftOfIsProper f hCM hequi d hd K i (g ≫ α) x =
      dualityEquivShiftOfIsProper f hCM hequi d hd L i α
        ((DerivedCategory.homologyFunctor (ModuleCat k) (-i)).map
          ((derivedGlobalSectionsOver f).map g) x)
```

**`Stacks.Duality.dualityEquivShiftOfIsProper_shiftedHomComp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L307). The attribute's comment: “part (3): compatibility with shifts and distinguished triangles”.

> **[Stacks, Tag 0FVZ], part (3), compatibility with shifted morphisms.** For
> `β ∈ Ext^j_X(L, K)` and `α ∈ Ext^i_X(K, ω_X[d])`, the linear form on `H^{-(i+j)}(X, L)` attached to
> `β.comp α ∈ Ext^{i+j}_X(L, ω_X[d])` is the one attached to `α` precomposed with the map
> `H^{-(i+j)}(X, L) ⟶ H^{-i}(X, K)` induced by `β`. This contains the compatibility with shifts
> (`Stacks.Duality.dualityEquivShiftOfIsProper_shift`) and with distinguished triangles
> (`Stacks.Duality.dualityEquivShiftOfIsProper_triangle`).

```lean
theorem dualityEquivShiftOfIsProper_shiftedHomComp (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    (K L : quasiCoherentDerivedCategory X) {i j c : ℤ}
    (β : DerivedCategory.Ext L.obj K.obj j)
    (α : DerivedCategory.Ext K.obj
      (((DerivedCategory.singleFunctor X.Modules 0).obj ωM)⟦(d : ℤ)⟧) i)
    (h : i + j = c)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-c)).obj
      ((derivedGlobalSectionsOver f).obj L.obj)) :
    letI := Scheme.linearOver f
    dualityEquivShiftOfIsProper f hCM hequi d hd L c (β.comp α h) x =
      dualityEquivShiftOfIsProper f hCM hequi d hd K i α
        ((HX).shiftMap β (-c) (-i) (by omega) x)
```

**`Stacks.Duality.dualityEquivShiftOfIsProper_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L327). The attribute's comment: “part (3): compatibility with shifts”.

> **[Stacks, Tag 0FVZ], part (3), compatibility with shifts.** Under
> `Ext^{i+n}_X(K⟦n⟧, ω_X[d]) = Ext^i_X(K, ω_X[d])` (composition with the identity of `K⟦n⟧`) and
> `H^{-(i+n)}(X, K⟦n⟧) ≅ H^{-i}(X, K)`, the isomorphisms of `K⟦n⟧` and of `K` agree.

```lean
theorem dualityEquivShiftOfIsProper_shift (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    (K : quasiCoherentDerivedCategory X) (i n : ℤ)
    (α : DerivedCategory.Ext K.obj
      (((DerivedCategory.singleFunctor X.Modules 0).obj ωM)⟦(d : ℤ)⟧) i)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-(i + n))).obj
      ((derivedGlobalSectionsOver f).obj (K.obj⟦n⟧))) :
    letI := Scheme.linearOver f
    dualityEquivShiftOfIsProper f hCM hequi d hd
        ⟨K.obj⟦n⟧, ObjectProperty.le_shift _ n K.obj K.property⟩ (i + n)
        (ShiftedHom.comp (𝟙 (K.obj⟦n⟧)) α rfl) x =
      dualityEquivShiftOfIsProper f hCM hequi d hd K i α
        (((HX).shiftIso n (-(i + n)) (-i) (by omega)).hom.app K.obj x)
```

**`Stacks.Duality.dualityEquivShiftOfIsProper_triangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L348). The attribute's comment: “part (3): compatibility with distinguished triangles”.

> **[Stacks, Tag 0FVZ], part (3), compatibility with distinguished triangles.** For a triangle
> `K ⟶ L ⟶ M ⟶ K⟦1⟧` in `D_QCoh(𝒪_X)`, the isomorphisms intertwine composition with its third
> morphism, `Ext^i_X(K, ω_X[d]) ⟶ Ext^{i+1}_X(M, ω_X[d])`, and the connecting morphism
> `H^{-(i+1)}(X, M) ⟶ H^{-i}(X, K)` of the long exact cohomology sequence.

```lean
theorem dualityEquivShiftOfIsProper_triangle (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    (T : Pretriangulated.Triangle (DerivedCategory X.Modules))
    (h₁ : DerivedCategoryB.derivedCategoryB (A := X.Modules)
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) T.obj₁)
    (h₃ : DerivedCategoryB.derivedCategoryB (A := X.Modules)
      (SheafOfModules.isQuasicoherent X.ringCatSheaf) T.obj₃)
    (i : ℤ)
    (α : DerivedCategory.Ext T.obj₁
      (((DerivedCategory.singleFunctor X.Modules 0).obj ωM)⟦(d : ℤ)⟧) i)
    (x : (DerivedCategory.homologyFunctor (ModuleCat k) (-(i + 1))).obj
      ((derivedGlobalSectionsOver f).obj T.obj₃)) :
    letI := Scheme.linearOver f
    dualityEquivShiftOfIsProper f hCM hequi d hd ⟨T.obj₃, h₃⟩ (i + 1)
        (ShiftedHom.comp (T.mor₃ : DerivedCategory.Ext T.obj₃ T.obj₁ 1) α rfl) x =
      dualityEquivShiftOfIsProper f hCM hequi d hd ⟨T.obj₁, h₁⟩ i α
        ((HX).homologySequenceδ T (-(i + 1)) (-i) (by omega) x)
```

**`Stacks.Duality.dualizingModuleExtEquivOfIsProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L378). The attribute's comment: “part (4): Ext^\{d-i}(F, ω\_X) = Hom\_k(H^i(X, F), k) for F quasi-coherent”.

> **[Stacks, Tag 0FVZ], part (4).** Let `X` be a proper scheme over a field `k` which is
> Cohen--Macaulay and equidimensional of dimension `d`. For `F` a quasi-coherent `𝒪_X`-module there
> are `k`-linear isomorphisms `Ext^{d-i}_X(F, ω_X) ≅ Hom_k(H^i(X, F), k)`, natural in `F`
> (`Stacks.Duality.dualizingModuleExtEquivOfIsProper_comp`). It is part (3) for `K = F[0]` in degree
> `-i`, through `Ext^{d-i}(F[0], ω_X[0]) = Ext^{-i}(F[0], ω_X[d])` and
> `H^{-(-i)}(X, F[0]) = H^i(X, F)`.

```lean
def dualizingModuleExtEquivOfIsProper (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    (F : X.Modules) [F.IsQuasicoherent] (i : ℕ) :
    letI := Scheme.linearOver f
    Abelian.zExt F ωM ((d : ℤ) - i) ≃ₗ[k] (cohomologyOverField k f F i →ₗ[k] k)
```

**`Stacks.Duality.dualizingModuleExtEquivOfIsProper_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/CohenMacaulay.lean#L395). The attribute's comment: “part (4): the isomorphisms are functorial in F”.

> **[Stacks, Tag 0FVZ], part (4), functoriality.** The isomorphisms of part (4) are natural in
> the quasi-coherent module `F`: for `φ : F ⟶ G` and `α ∈ Ext^{d-i}_X(G, ω_X)`, the linear form
> attached to `φ ≫ α` is the one attached to `α` precomposed with `H^i(X, φ)`.

```lean
theorem dualizingModuleExtEquivOfIsProper_comp (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    {F G : X.Modules} [F.IsQuasicoherent] [G.IsQuasicoherent] (φ : F ⟶ G) (i : ℕ)
    (α : Abelian.zExt G ωM ((d : ℤ) - i)) (x : cohomologyOverField k f F i) :
    letI := Scheme.linearOver f
    dualizingModuleExtEquivOfIsProper f hCM hequi d hd F i
        ((DerivedCategory.singleFunctor X.Modules 0).map φ ≫ α) x =
      dualizingModuleExtEquivOfIsProper f hCM hequi d hd G i α
        ((cohomologyOverFieldFunctor k f i).map φ x)
```

## Tag 0FW0, a remark

[Tag 0FW0](https://stacks.math.columbia.edu/tag/0FW0) in the Stacks Project.

**`Stacks.Duality.serrePairing_isPerfPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/SerreDualityLocallyFree.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/SerreDualityLocallyFree.lean#L599).

> **[Stacks, Tag 0FW0].** Let `X` be a proper Cohen--Macaulay scheme over a field `k` which is
> equidimensional of dimension `d`, let `ω_X^•` and `ω_X` be as in [Stacks, Tag 0FVV], so that
> `ω_X^• = ω_X[d]` by [Stacks, Tag 0FVZ], and let `t : Hᵈ(X, ω_X) ⟶ k` be the trace of
> [Stacks, Tag 0FVW] (`Stacks.Duality.topTrace`). Let `ℰ` be a finite locally free `𝒪_X`-module with
> dual `ℰ^∨`. Then for all `i + j = d` the pairing
>
> `Hⁱ(X, ω_X ⊗_{𝒪_X} ℰ^∨) × Hʲ(X, ℰ) ⟶ k,  (ξ, η) ↦ t((1 ⊗ ε)(ξ ∪ η))`
>
> (`Stacks.Duality.serrePairing`) is perfect, where `∪` is the cup product of Cohomology,
> Section 0FKU and `ε : ℰ^∨ ⊗_{𝒪_X} ℰ ⟶ 𝒪_X` is the evaluation map.

```lean
theorem serrePairing_isPerfPair (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hequi : TopologicalSpace.Equidimensional X) (d : ℕ) (hd : topologicalKrullDim X = d)
    (E : X.Modules) (hE : AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E)
    (i j : ℤ) (hij : i + j = d) :
    (serrePairing f hCM hequi d hd E i j hij).IsPerfPair
```

## Tag 0FW1, a lemma

[Tag 0FW1](https://stacks.math.columbia.edu/tag/0FW1) in the Stacks Project.

**`Stacks.Duality.nonempty_iso_relativeDualizing_of_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/ChangeOfField.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/ChangeOfField.lean#L293). The attribute's comment: “(1): ω\_X^• and ω\_X are as in 0FVV for a factorization X → Spec k' → Spec k”.

> Let `X` be proper over a field `k` with structure morphism `f`, and suppose `f` factors as
> `f' ≫ g` with `f' : X ⟶ Spec k'` for a field `k'`. Then `ω_X^•` and `ω_X` of [Stacks, Tag 0FVV]
> for `f` are isomorphic to those constructed for `f'`.

```lean
theorem nonempty_iso_relativeDualizing_of_factorization {k' : Type u} [Field k']
    (f' : X ⟶ Spec (.of k')) (g : Spec (.of k') ⟶ Spec (.of k)) (h : f' ≫ g = f) :
    haveI : IsProper f' := haveI : IsProper (f' ≫ g) := h ▸ ‹IsProper f›; IsProper.of_comp f' g
    Nonempty (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k))) ≅
      relativeDualizingComplex f' (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k')))) ∧
    Nonempty (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k))) ≅
      relativeDualizingModule f' (isQuasicoherent_homology_derivedPushforward_of_qcqs f')
        (DerivedPushforward.derivedStructureSheaf (Spec (.of k'))))
```

**`Stacks.Duality.nonempty_iso_relativeDualizing_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/ChangeOfField.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/ProperOverField/ChangeOfField.lean#L312). The attribute's comment: “(2): the pullbacks of ω\_X^• and ω\_X to X\_K are as in 0FVV for X\_K → Spec K”.

> Let `X` be proper over a field `k` with structure morphism `f`, let `K/k` be a field extension
> and `X_K = X ×_{Spec k} Spec K`, with projections `g' : X_K ⟶ X` and `f_K : X_K ⟶ Spec K`. Then
> the pullbacks `L(g')^* ω_X^•` and `(g')^* ω_X` are isomorphic to the dualizing complex and module
> of [Stacks, Tag 0FVV] constructed for `f_K`.

```lean
theorem nonempty_iso_relativeDualizing_baseChange (K : Type u) [Field K] [Algebra k K] :
    Nonempty ((quasiCoherentDerivedPullback'
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))))).obj
          (relativeDualizingComplex f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))) ≅
      relativeDualizingComplex (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
        (isQuasicoherent_homology_derivedPushforward_of_qcqs _)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of K)))) ∧
    Nonempty ((Scheme.Modules.pullback
        (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))))).obj
          (relativeDualizingModule f (isQuasicoherent_homology_derivedPushforward_of_qcqs f)
            (DerivedPushforward.derivedStructureSheaf (Spec (.of k)))) ≅
      relativeDualizingModule (pullback.snd f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
        (isQuasicoherent_homology_derivedPushforward_of_qcqs _)
        (DerivedPushforward.derivedStructureSheaf (Spec (.of K))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.27, Tag 0FVU](https://stacks.math.columbia.edu/tag/0FVU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
