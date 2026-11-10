---
declaration: section
origin: cited
lean: AlgebraicGeometry.fullyFaithful_of_bijective_on_spanning_set, AlgebraicGeometry.exists_ringKrullDim_eq_and_homAddEquiv_homologyDerivedTensor, Dualizing.exists_addEquiv_hom_homology_derivedTensor_matlisDual, AlgebraicGeometry.exists_mem_isZero_stalkHomology_of_derivedTensor_residueField, AlgebraicGeometry.exists_mem_forall_isZero_stalkHomology_of_derivedTensor_residueField, AlgebraicGeometry.exists_mem_isZero_stalkHomology_of_isZero_homology_globalSections_derivedTensor, AlgebraicGeometry.exists_mem_forall_isZero_stalkHomology_of_isZero_homology_globalSections_derivedTensor, AlgebraicGeometry.exists_mem_isZero_stalkHomology_of_subsingleton_hom_from_residueFieldSkyscraper
statement: formalized
proof: formalized
---

# 57.11 Deducing fully faithfulness

Section 57.11 of the Stacks Project, [Tag 0G23](https://stacks.math.columbia.edu/tag/0G23). 6 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G24, a lemma

[Tag 0G24](https://stacks.math.columbia.edu/tag/0G24) in the Stacks Project.

**`AlgebraicGeometry.fullyFaithful_of_bijective_on_spanning_set`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/SpanningSet.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/SpanningSet.lean#L304).

> **Stacks Project, Tag 0G24.** Let `F : C ⥤ D` be an exact functor of
> pre-triangulated categories which has both adjoints. If a set `S` detects zero objects by maps
> from and to all shifts of its members, and `F` induces bijections on all shifted Hom sets between
> members of `S`, then `F` is fully faithful.

```lean
public theorem fullyFaithful_of_bijective_on_spanning_set
    {C : Type u} {D : Type u'} [Category.{v} C] [Category.{v'} D]
    [HasZeroObject C] [HasShift C ℤ] [Preadditive C]
    [∀ n : ℤ, (shiftFunctor C n).Additive] [Pretriangulated C]
    [HasZeroObject D] [HasShift D ℤ] [Preadditive D]
    [∀ n : ℤ, (shiftFunctor D n).Additive] [Pretriangulated D]
    (F : C ⥤ D) [F.CommShift ℤ] [F.IsTriangulated]
    [F.IsLeftAdjoint] [F.IsRightAdjoint] (S : Set C)
    (h_from : ∀ K : C,
      (∀ E : C, E ∈ S → ∀ i : ℤ, Subsingleton (E ⟶ K⟦i⟧)) → IsZero K)
    (h_to : ∀ K : C,
      (∀ E : C, E ∈ S → ∀ i : ℤ, Subsingleton (K ⟶ E⟦i⟧)) → IsZero K)
    (h_bijective : ∀ E : C, E ∈ S → ∀ E' : C, E' ∈ S → ∀ i : ℤ,
      Function.Bijective (fun f : E ⟶ E'⟦i⟧ ↦
        F.map f ≫ (F.commShiftIso i).hom.app E')) :
    Nonempty F.FullyFaithful
```

## Tag 0G02, a lemma

[Tag 0G02](https://stacks.math.columbia.edu/tag/0G02) in the Stacks Project.

**`AlgebraicGeometry.exists_ringKrullDim_eq_and_homAddEquiv_homologyDerivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedPointMatlisDuality.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedPointMatlisDuality.lean#L324). The attribute's comment: “the scheme-level statement: k a field, X a scheme of finite type over k which is regular, x a closed point of X, F a coherent 𝒪\_X-module supported at x and F' a coherent 𝒪\_X-module supported at x whose stalk at x is a Matlis dual of F\_x; then Hom\_X(F, M) is identified additively with H⁰(X, M ⊗^L\_\{𝒪\_X} F'[-d\_x]), d\_x = dim 𝒪\_\{X,x}, functorially in M. The identification is produced for every M in D(𝒪\_X), which generalizes the source's clause for M in D\_perf(𝒪\_X). The local ring is read as the RingCat-valued stalk of the sheaf of rings, which is the local ring 𝒪\_\{X,x} by AlgebraicGeometry.ringCatStalkRingEquiv and is where the Matlis-duality hypothesis is stated; the dimension clause d\_x = dim 𝒪\_\{X,x} is stated at the CommRingCat-valued stalk X.presheaf.stalk x. The duality at the point to which the source's proof reduces this -- for A a regular local ring of dimension d, Hom\_\{D(A)}(N, K) is H⁰(K ⊗^L\_A N'[-d]) functorially in K -- is registered separately, on Dualizing.exists\_addEquiv\_hom\_homology\_derivedTensor\_matlisDual”.

> **Stacks 0G02.** Let `k` be a field, `X` a scheme of finite type over `k` which is regular,
> `x ∈ X` a closed point, `F` a coherent `𝒪_X`-module supported at `x`, and `F'` a coherent
> `𝒪_X`-module supported at `x` whose stalk at `x` is a Matlis dual of `F_x`. Then with
> `d_x = dim 𝒪_{X,x}`,
>
> `Hom_X(F, M) = H⁰(X, M ⊗^𝐋_{𝒪_X} F'[-d_x])`
>
> functorially in `M`.

```lean
theorem exists_ringKrullDim_eq_and_homAddEquiv_homologyDerivedTensor
    (k : Type u) [Field k] (X : Scheme.{u}) (sX : X ⟶ Spec (CommRingCat.of k))
    [LocallyOfFiniteType sX] [QuasiCompact sX] (hX : IsRegular X)
    (x : X) (hx : IsClosed ({x} : Set X))
    (F F' : X.Modules) [F.IsCoherent] [F'.IsCoherent]
    (hFsupp : SheafOfModules.supp (R := X.ringCatSheaf) F ⊆ {x})
    (hF'supp : SheafOfModules.supp (R := X.ringCatSheaf) F' ⊆ {x})
    (hdual : Dualizing.IsMatlisDualPair (stalkRing X.toRingedSpace x)
      (SheafOfModules.stalkObjStalkRing x F) (SheafOfModules.stalkObjStalkRing x F')) :
    ∃ d : ℕ, ringKrullDim (X.presheaf.stalk x) = (d : ℕ∞) ∧
      ∃ e : ∀ M : DerivedCategory X.Modules,
          ((DerivedCategory.singleFunctor X.Modules 0).obj F ⟶ M) ≃+
            ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).obj
              ((Stacks.Cohomology.ModuleSections.derivedModuleGlobalSections
                  (ringedSite X.sheaf)).obj
                (((Stacks.SheafOfModules.derivedTensorProductFunctor
                    (ringedSite X.sheaf)).obj M).obj
                  (((DerivedCategory.singleFunctor X.Modules 0).obj F')⟦-(d : ℤ)⟧))) : Type u),
        ∀ (M N : DerivedCategory X.Modules) (g : M ⟶ N)
            (a : (DerivedCategory.singleFunctor X.Modules 0).obj F ⟶ M),
          e N (a ≫ g) =
            (DerivedCategory.homologyFunctor AddCommGrpCat.{u} 0).map
              ((Stacks.Cohomology.ModuleSections.derivedModuleGlobalSections
                  (ringedSite X.sheaf)).map
                (((Stacks.SheafOfModules.derivedTensorProductFunctor
                    (ringedSite X.sheaf)).map g).app
                  (((DerivedCategory.singleFunctor X.Modules 0).obj F')⟦-(d : ℤ)⟧)))
              (e M a)
```

**`Dualizing.exists_addEquiv_hom_homology_derivedTensor_matlisDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/RegularLocalFiniteLengthDuality.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/RegularLocalFiniteLengthDuality.lean#L403). The attribute's comment: “duality at the point”.

> **Stacks 0G02**, the duality at the point to which the source reduces its statement. Let `A`
> be a regular local ring of dimension `d`, let `N` be an `A`-module of finite length and let `N'`
> be a Matlis dual of `N` with respect to an injective hull `E` of the residue field. Then
> `Hom_{D(A)}(N, K) ≃+ H⁰(K ⊗^L_A N'[-d])`, functorially in `K`.

```lean
public theorem exists_addEquiv_hom_homology_derivedTensor_matlisDual
    (A : Type u) [CommRing A] [IsRegularLocalRing A]
    (E : ModuleCat.{u} A)
    (i : (ModuleCat.uliftFunctor.{0} A).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)) ⟶ E)
    [Mono i] (hi : Module.IsInjectiveHull i)
    (N N' : ModuleCat.{u} A) (hN : IsFiniteLength A N)
    (hdual : Nonempty (N' ≅ ModuleCat.of A (N ⟶ E))) :
    ∃ d : ℕ, ringKrullDim A = (d : ℕ∞) ∧
      ∃ e : ∀ L : DerivedCategory (ModuleCat.{u} A),
          (((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
              ((derivedHomAdjunctionOverRing.{u, 0, u + 1} A).tensor.obj
                (L, ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N')⟦-(d : ℤ)⟧)))
            : Type u) ≃+
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N ⟶ L),
        ∀ (L L' : DerivedCategory (ModuleCat.{u} A)) (f : L ⟶ L')
          (a : (DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).obj
            ((derivedHomAdjunctionOverRing.{u, 0, u + 1} A).tensor.obj
              (L, ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N')⟦-(d : ℤ)⟧))),
          e L' ((DerivedCategory.homologyFunctor (ModuleCat.{u} A) 0).map
              ((derivedHomAdjunctionOverRing.{u, 0, u + 1} A).tensor.map
                (f, 𝟙 (((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N')⟦-(d : ℤ)⟧)))
              a) = e L a ≫ f
```

## Tag 0G03, a lemma

[Tag 0G03](https://stacks.math.columbia.edu/tag/0G03) in the Stacks Project.

**`AlgebraicGeometry.exists_mem_isZero_stalkHomology_of_derivedTensor_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/DerivedTensorResidueFieldSkyscraper.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/DerivedTensorResidueFieldSkyscraper.lean#L168). The attribute's comment: “part (5), the derived-tensor form, for `X` a Noetherian scheme and `K` perfect: the source's `H^i(X, K ⊗^𝐋_{𝒪_X} 𝒪_x)` is read as the degree-`i` cohomology of the derived stalk at `x` of `K ⊗^𝐋_{𝒪_X} 𝒪_x`, and `H^i(K)|_U = 0` as the vanishing of the degree-`i` cohomology stalk at every point of `U`”.

> **[Stacks, Tag 0G03] part (5).** Let `X` be a Noetherian scheme, `x` a point of `X`, `𝒪_x` the
> skyscraper at `x` with value the residue field `κ(x)`, and `K` a perfect object of `D(𝒪_X)`. If the
> degree-`i` cohomology of `K ⊗^𝐋_{𝒪_X} 𝒪_x` at `x` vanishes, then the degree-`i` cohomology sheaf
> of `K` has vanishing stalk at every point of an open neighbourhood of `x`.

```lean
public theorem exists_mem_isZero_stalkHomology_of_derivedTensor_residueField
    (X : Scheme.{u}) [IsNoetherian X] (x : X)
    (K : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K) (i : ℤ)
    (h : IsZero ((DerivedCategory.homologyFunctor
      (ModuleCat.{u} (ToType (StacksDraft.StalkRingComparison.stalkRing X x))) i).obj
        ((SheafOfModules.stalkFunctor X.ringCatSheaf x).mapDerivedCategory.obj
          (derivedTensorResidueFieldSkyscraper X x K)))) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U →
      IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} X.ringCatSheaf) i).obj K))
```

**`AlgebraicGeometry.exists_mem_forall_isZero_stalkHomology_of_derivedTensor_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/DerivedTensorResidueFieldSkyscraper.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/DerivedTensorResidueFieldSkyscraper.lean#L202). The attribute's comment: “part (6), the derived-tensor form, for `X` a Noetherian scheme and `K` perfect: the source's `H^i(X, K ⊗^𝐋_{𝒪_X} 𝒪_x)` is read as the degree-`i` cohomology of the derived stalk at `x` of `K ⊗^𝐋_{𝒪_X} 𝒪_x`, and `K` being zero near `x` as the vanishing of every cohomology stalk at every point of the neighbourhood”.

> **[Stacks, Tag 0G03] part (6).** In the situation of part (5), if `K ⊗^𝐋_{𝒪_X} 𝒪_x` has no
> cohomology at `x` in any degree, then `K` is zero on an open neighbourhood of `x`: every
> cohomology sheaf of `K` has vanishing stalk at every point of that neighbourhood.

```lean
public theorem exists_mem_forall_isZero_stalkHomology_of_derivedTensor_residueField
    (X : Scheme.{u}) [IsNoetherian X] (x : X)
    (K : DerivedCategory (SheafOfModules.{u} X.ringCatSheaf))
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (h : ∀ i : ℤ, IsZero ((DerivedCategory.homologyFunctor
      (ModuleCat.{u} (ToType (StacksDraft.StalkRingComparison.stalkRing X x))) i).obj
        ((SheafOfModules.stalkFunctor X.ringCatSheaf x).mapDerivedCategory.obj
          (derivedTensorResidueFieldSkyscraper X x K)))) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U → ∀ i : ℤ,
      IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} X.ringCatSheaf) i).obj K))
```

**`AlgebraicGeometry.exists_mem_isZero_stalkHomology_of_isZero_homology_globalSections_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean#L246). The attribute's comment: “part (5), for X a Noetherian scheme (which every scheme of finite type over a field is), x a closed point and K perfect: H^i(X, -) is the cohomology of the derived global sections of the ringed site of opens, and H^i(K)|\_U = 0 is read as the vanishing of the stalk of H^i(K) at every point of U”.

> **[Stacks, Tag 0G03] part (5), global form.** Let `X` be a Noetherian scheme, `x` a closed
> point of `X`, `𝒪_x` the skyscraper at `x` with value `κ(x)` and `K` a perfect object of
> `D(𝒪_X)`. If `H^i(X, K ⊗^𝐋_{𝒪_X} 𝒪_x) = 0`, then `H^i(K)` vanishes on an open neighbourhood
> of `x`.

```lean
theorem exists_mem_isZero_stalkHomology_of_isZero_homology_globalSections_derivedTensor
    (X : Scheme.{u}) [IsNoetherian X] (x : X) (hx : IsClosed ({x} : Set X))
    (K : DerivedCategory X.Modules) (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K) (i : ℤ)
    (h : IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
      ((Stacks.Cohomology.ModuleSections.derivedModuleGlobalSections
        (Stacks.SheafOfModules.ringedSite X.sheaf)).obj (derivedTensorSkyscraper X x K)))) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U →
      IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
        ((DerivedCategory.homologyFunctor X.Modules i).obj K))
```

**`AlgebraicGeometry.exists_mem_forall_isZero_stalkHomology_of_isZero_homology_globalSections_derivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean#L263). The attribute's comment: “part (6), for X a Noetherian scheme (which every scheme of finite type over a field is), x a closed point and K perfect: if H^i(X, K ⊗^L 𝒪\_x) = 0 for all i then every cohomology sheaf of K has vanishing stalk at every point of an open neighbourhood of x”.

> **[Stacks, Tag 0G03] part (6), global form.** In the situation of part (5), if
> `H^i(X, K ⊗^𝐋_{𝒪_X} 𝒪_x) = 0` for all `i`, then `K` is zero on an open neighbourhood of `x`.

```lean
theorem exists_mem_forall_isZero_stalkHomology_of_isZero_homology_globalSections_derivedTensor
    (X : Scheme.{u}) [IsNoetherian X] (x : X) (hx : IsClosed ({x} : Set X))
    (K : DerivedCategory X.Modules) (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (h : ∀ i : ℤ, IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u} i).obj
      ((Stacks.Cohomology.ModuleSections.derivedModuleGlobalSections
        (Stacks.SheafOfModules.ringedSite X.sheaf)).obj (derivedTensorSkyscraper X x K)))) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U → ∀ i : ℤ,
      IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
        ((DerivedCategory.homologyFunctor X.Modules i).obj K))
```

**`AlgebraicGeometry.exists_mem_isZero_stalkHomology_of_subsingleton_hom_from_residueFieldSkyscraper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean#L313). The attribute's comment: “part (1), at the source's hypotheses: k a field, X a regular scheme of finite type over k, x a closed point, 𝒪\_x the skyscraper at x with value κ(x), K perfect. Ext^i\_X(𝒪\_x, K) is Hom\_\{D(𝒪\_X)}(𝒪\_x, K[i]); d\_x = dim 𝒪\_\{X,x} is the natural number d with ringKrullDim 𝒪\_\{X,x} = d, produced by the conclusion; H^\{i-d\_x}(K)|\_U = 0 is read as the vanishing of the stalk of H^\{i-d\_x}(K) at every point of U”.

> **[Stacks, Tag 0G03] part (1).** Let `k` be a field, `X` a regular scheme of finite type
> over `k`, `x ∈ X` a closed point, `𝒪_x` the skyscraper at `x` with value `κ(x)`, `d` the
> dimension of `𝒪_{X,x}`, and `K` a perfect object of `D(𝒪_X)`. If `Ext^i_X(𝒪_x, K) = 0`, then
> `H^{i - d}(K)` vanishes on an open neighbourhood of `x`.

```lean
theorem exists_mem_isZero_stalkHomology_of_subsingleton_hom_from_residueFieldSkyscraper
    (k : Type u) [Field k] (X : Scheme.{u}) (sX : X ⟶ Spec (CommRingCat.of k))
    [LocallyOfFiniteType sX] [QuasiCompact sX] (hX : IsRegular X)
    (x : X) (hx : IsClosed ({x} : Set X))
    (K : DerivedCategory X.Modules) (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (i : ℤ)
    (h : Subsingleton ((DerivedCategory.singleFunctor X.Modules 0).obj
      (residueFieldSkyscraperSheaf X x) ⟶ K⟦i⟧)) :
    ∃ d : ℕ, ringKrullDim (X.presheaf.stalk x) = d ∧
      ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U →
        IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
          ((DerivedCategory.homologyFunctor X.Modules (i - d)).obj K))
```

**`AlgebraicGeometry.exists_mem_forall_isZero_stalkHomology_of_subsingleton_hom_from_residueFieldSkyscraper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean#L373). The attribute's comment: “part (2), at the source's hypotheses: k a field, X a regular scheme of finite type over k, x a closed point, K perfect; if Hom\_\{D(𝒪\_X)}(𝒪\_x, K[i]) = 0 for all i then every cohomology sheaf of K has vanishing stalk at every point of an open neighbourhood of x”.

> **[Stacks, Tag 0G03] part (2).** Let `k` be a field, `X` a regular scheme of finite type
> over `k`, `x ∈ X` a closed point, `𝒪_x` the skyscraper at `x` with value `κ(x)` and `K` a perfect
> object of `D(𝒪_X)`. If `Hom_X(𝒪_x, K[i]) = 0` for all `i ∈ ℤ`, then `K` is zero on an open
> neighbourhood of `x`.

```lean
theorem exists_mem_forall_isZero_stalkHomology_of_subsingleton_hom_from_residueFieldSkyscraper
    (k : Type u) [Field k] (X : Scheme.{u}) (sX : X ⟶ Spec (CommRingCat.of k))
    [LocallyOfFiniteType sX] [QuasiCompact sX] (hX : IsRegular X)
    (x : X) (hx : IsClosed ({x} : Set X))
    (K : DerivedCategory X.Modules) (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (h : ∀ i : ℤ, Subsingleton ((DerivedCategory.singleFunctor X.Modules 0).obj
      (residueFieldSkyscraperSheaf X x) ⟶ K⟦i⟧)) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U → ∀ i : ℤ,
      IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
        ((DerivedCategory.homologyFunctor X.Modules i).obj K))
```

**`AlgebraicGeometry.exists_mem_isZero_stalkHomology_derivedDual_of_subsingleton_hom_to_residueFieldSkyscraper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean#L438). The attribute's comment: “part (3), for X a Noetherian scheme (which every scheme of finite type over a field is), x a closed point and K perfect: Ext^i\_X(K, 𝒪\_x) is Hom\_\{D(𝒪\_X)}(K, 𝒪\_x[i]), K^∨ is R𝓗om(K, 𝒪\_X), and H^i(K^∨)|\_U = 0 is read as the vanishing of the stalk of H^i(K^∨) at every point of U”.

> **[Stacks, Tag 0G03] part (3).** Let `X` be a Noetherian scheme, `x ∈ X` a closed point,
> `𝒪_x` the skyscraper at `x` with value `κ(x)` and `K` a perfect object of `D(𝒪_X)`, with dual
> `K^∨ = R𝓗om(K, 𝒪_X)`. If `Ext^i_X(K, 𝒪_x) = 0`, then `H^i(K^∨)` vanishes on an open
> neighbourhood of `x`.

```lean
theorem exists_mem_isZero_stalkHomology_derivedDual_of_subsingleton_hom_to_residueFieldSkyscraper
    (X : Scheme.{u}) [IsNoetherian X] (x : X) (hx : IsClosed ({x} : Set X))
    (K : DerivedCategory X.Modules) (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K) (i : ℤ)
    (h : Subsingleton (K ⟶ ((DerivedCategory.singleFunctor X.Modules 0).obj
      (residueFieldSkyscraperSheaf X x))⟦i⟧)) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U →
      IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
        ((DerivedCategory.homologyFunctor X.Modules i).obj
          (Stacks.SheafOfModules.derivedDual X.sheaf K)))
```

**`AlgebraicGeometry.exists_mem_forall_isZero_stalkHomology_of_subsingleton_hom_to_residueFieldSkyscraper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/LocalVanishingCriteria.lean#L471). The attribute's comment: “part (4), for X a Noetherian scheme (which every scheme of finite type over a field is), x any point and K perfect: if Hom\_\{D(𝒪\_X)}(K, 𝒪\_x[i]) = 0 for all i then every cohomology sheaf of K has vanishing stalk at every point of an open neighbourhood of x”.

> **[Stacks, Tag 0G03] part (4).** Let `X` be a Noetherian scheme, `x ∈ X` a point, `𝒪_x`
> the skyscraper at `x` with value `κ(x)` and `K` a perfect object of `D(𝒪_X)`. If
> `Hom_X(K, 𝒪_x[i]) = 0` for all `i ∈ ℤ`, then `K` is zero on an open neighbourhood of `x`.

```lean
theorem exists_mem_forall_isZero_stalkHomology_of_subsingleton_hom_to_residueFieldSkyscraper
    (X : Scheme.{u}) [IsNoetherian X] (x : X)
    (K : DerivedCategory X.Modules) (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (h : ∀ i : ℤ, Subsingleton (K ⟶ ((DerivedCategory.singleFunctor X.Modules 0).obj
      (residueFieldSkyscraper X x))⟦i⟧)) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U → ∀ i : ℤ,
      IsZero (OXModule.stalk ((DerivedCategory.homologyFunctor X.Modules i).obj K) y)
```

**`AlgebraicGeometry.exists_mem_forall_stalkHomology_isZero_of_hom_residueFieldSkyscraper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraper.lean, line 1102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraper.lean#L1102). The attribute's comment: “part (4), with the source's hypotheses `X` regular of finite type over a field and `K` in `D_perf(𝒪_X)` replaced by `X` Noetherian and `K` bounded with coherent cohomology, that is `K` in `D^b_Coh(𝒪_X)`. The source's class of pairs sits inside this one, but the containment — a perfect object of `D(𝒪_X)` in the sense of `Stacks.Cohomology.PerfectComplexes.IsPerfect` is bounded with coherent cohomology, Tags 0BCJ and 08E8 — is not bridged in the library, so that is what is granted here. `K` being zero near `x` is read as the vanishing of every cohomology stalk at every point of the neighbourhood”.

> A complex with no nonzero map to any shift of the residue-field skyscraper at `x` is zero on
> an open neighbourhood of `x`: every cohomology sheaf has vanishing stalk at every point of that
> neighbourhood.

```lean
public theorem exists_mem_forall_stalkHomology_isZero_of_hom_residueFieldSkyscraper
    (X : Scheme.{u}) [IsNoetherian X] (x : X)
    [HasDerivedCategory (SheafOfModules.{u} X.ringCatSheaf)]
    (K : DerivedCategory.Bounded (SheafOfModules.{u} X.ringCatSheaf))
    (hK : ∀ i : ℤ,
      ((DerivedCategory.homologyFunctor
        (SheafOfModules.{u} X.ringCatSheaf) i).obj K.obj).IsCoherent)
    (h : ∀ i : ℤ,
      Subsingleton (K.obj ⟶
        (DerivedCategory.singleFunctor (SheafOfModules.{u} X.ringCatSheaf) i).obj
          (residueFieldSkyscraper X x))) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U → ∀ i : ℤ,
      IsZero (OXModule.stalk
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} X.ringCatSheaf) i).obj K.obj) y)
```

**`AlgebraicGeometry.residueFieldSkyscraperIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraperComparison.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraperComparison.lean#L256). The attribute's comment: “the two spellings of the residue-field skyscraper 𝒪\_x agree, identifying part (4)'s with the one used by parts (1), (2), (3), (5), (6)”.

> **The two residue-field skyscrapers at `x` agree.**  The sheafification of the skyscraper
> presheaf of modules at `x` with value `κ(x)` is the skyscraper sheaf of modules at `x` with value
> the residue field of the `RingCat`-valued stalk.

```lean
def residueFieldSkyscraperIso :
    residueFieldSkyscraper X x ≅ residueFieldSkyscraperSheaf X x
```

**`AlgebraicGeometry.exists_mem_forall_isZero_stalkHomology_of_subsingleton_hom_to_residueFieldSkyscraperSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraperComparison.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraperComparison.lean#L271). The attribute's comment: “part (4), for X a Noetherian scheme (which every scheme of finite type over a field is), x any point and K perfect, with 𝒪\_x read as residueFieldSkyscraperSheaf, the spelling parts (1), (2), (3), (5) and (6) use: if Hom\_\{D(𝒪\_X)}(K, 𝒪\_x[i]) = 0 for all i then every cohomology sheaf of K has vanishing stalk at every point of an open neighbourhood of x”.

> Let `X` be a Noetherian scheme, `x ∈ X` a point, `𝒪_x` the skyscraper sheaf
> `residueFieldSkyscraperSheaf X x` at `x` with value `κ(x)` and `K` a perfect object of `D(𝒪_X)`.
> If `Hom_X(K, 𝒪_x[i]) = 0` for all `i ∈ ℤ`, then there is an open neighbourhood of `x` at every
> point of which every cohomology sheaf of `K` has zero stalk.

```lean
theorem exists_mem_forall_isZero_stalkHomology_of_subsingleton_hom_to_residueFieldSkyscraperSheaf
    [IsNoetherian X] (K : DerivedCategory X.Modules)
    (hK : RingedSpace.IsPerfect (X := X.toRingedSpace) K)
    (h : ∀ i : ℤ, Subsingleton (K ⟶ ((DerivedCategory.singleFunctor X.Modules 0).obj
      (residueFieldSkyscraperSheaf X x))⟦i⟧)) :
    ∃ U : Opens X.carrier, x ∈ U ∧ ∀ y : X, y ∈ U → ∀ i : ℤ,
      IsZero (OXModule.stalk ((DerivedCategory.homologyFunctor X.Modules i).obj K) y)
```

**`Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.exists_mem_forall_stalkHomology_isZero_of_pointSheaf_hom_shift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/MapsFromPointSheaf.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/MapsFromPointSheaf.lean#L360). The attribute's comment: “part (2), for `X` a regular Noetherian scheme (a regular scheme of finite type over a field, the source's hypothesis, is one) and `K` perfect: `K` being zero in an open neighbourhood of `x` is read as the vanishing of every cohomology stalk at every point of the neighbourhood”.

> **[Stacks, Tag 0G03] part (2).** Let `X` be a regular Noetherian scheme, `x` a closed point
> of `X`, `𝒪_x` the skyscraper sheaf at `x` with value `κ(x)` and `K` a perfect object of
> `D(𝒪_X)`. If `Hom(𝒪_x, K[i]) = 0` for every `i ∈ ℤ`, then `K` is zero on an open neighbourhood of
> `x`: every cohomology sheaf of `K` has vanishing stalk at every point of that neighbourhood.

```lean
theorem exists_mem_forall_stalkHomology_isZero_of_pointSheaf_hom_shift (hX : IsRegular X)
    [IsNoetherian X] (hx : IsClosed ({x} : Set X)) (K : DerivedCategory X.Modules)
    (hK : IsPerfect (X := X.toRingedSpace) K)
    (h : ∀ i : ℤ, Subsingleton (pointSheaf X x ⟶ K⟦i⟧)) :
    ∃ U : TopologicalSpace.Opens X, x ∈ U ∧ ∀ y : X, y ∈ U → ∀ i : ℤ,
      IsZero (SheafOfModules.stalkObj X.ringCatSheaf y
        ((DerivedCategory.homologyFunctor X.Modules i).obj K))
```

## Tag 0GWZ, a lemma

[Tag 0GWZ](https://stacks.math.columbia.edu/tag/0GWZ) in the Stacks Project.

**`AlgebraicGeometry.stalkHomology_isZero_iff_hom_residueFieldSkyscraper_subsingleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraper.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/DeducingFullyFaithfulness/ResidueFieldSkyscraper.lean#L1012).

> For a bounded complex with coherent cohomology, stalk cohomology above `b`
> vanishes exactly when all maps to the residue-field skyscraper in those degrees vanish.

```lean
public theorem stalkHomology_isZero_iff_hom_residueFieldSkyscraper_subsingleton
    (X : Scheme.{u}) [IsNoetherian X] (x : X)
    [HasDerivedCategory (SheafOfModules.{u} X.ringCatSheaf)]
    (K : DerivedCategory.Bounded (SheafOfModules.{u} X.ringCatSheaf))
    (hK : ∀ i : ℤ,
      ((DerivedCategory.homologyFunctor
        (SheafOfModules.{u} X.ringCatSheaf) i).obj K.obj).IsCoherent)
    (b : ℤ) :
    (∀ i : ℤ, b < i →
      IsZero (OXModule.stalk
        ((DerivedCategory.homologyFunctor (SheafOfModules.{u} X.ringCatSheaf) i).obj K.obj) x)) ↔
    (∀ i : ℤ, b < i →
      Subsingleton (K.obj ⟶
        (DerivedCategory.singleFunctor (SheafOfModules.{u} X.ringCatSheaf) i).obj
          (residueFieldSkyscraper X x)))
```

## Tag 0G25, a lemma

[Tag 0G25](https://stacks.math.columbia.edu/tag/0G25) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.fullyFaithful_iff_bijective_ext_perfectPointSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/FixingZeroDimensional.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/FixingZeroDimensional.lean#L551).

> **[Stacks, Tag 0G25].** Let `k` be a field and let `X`, `Y` be proper schemes over `k` with
> `X` regular. A `k`-linear exact functor `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_Y)` is fully faithful if and
> only if for all closed points `x, x' ∈ X` the maps
> `F : Ext^i_X(𝒪_x, 𝒪_{x'}) ⟶ Ext^i_Y(F(𝒪_x), F(𝒪_{x'}))` are isomorphisms for all `i ∈ ℤ`. Here
> `𝒪_x` is the skyscraper sheaf at `x` with value `κ(x)` (`perfectPointSheaf`), and
> `Ext^i(A, B) = Hom(A, B[i])`, the map being `f ↦ F(f)` followed by the commutation of `F` with the
> shift.
>
> The proof is the source's: `F` has both adjoints ([Stacks, Tag 0FYN]), so the criterion of
> [Stacks, Tag 0G24] applies to the closed-point skyscrapers, its hypotheses (2) and (3) being
> [Stacks, Tag 0G03] parts (2) and (4).

```lean
theorem fullyFaithful_iff_bijective_ext_perfectPointSheaf (hX : IsRegular X.left)
    (F : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory Y.left)
    [F.CommShift ℤ] [F.IsTriangulated] [F.Linear k] :
    Nonempty F.FullyFaithful ↔
      ∀ (x x' : X.left) (hx : IsClosed ({x} : Set X.left))
        (hx' : IsClosed ({x'} : Set X.left)) (i : ℤ),
        haveI : IsNoetherian X.left := isNoetherian_of_locallyOfFiniteType X.hom
        Function.Bijective (fun f : perfectPointSheaf X.left hX x hx ⟶
            (perfectPointSheaf X.left hX x' hx')⟦i⟧ =>
          F.map f ≫ (F.commShiftIso i).hom.app (perfectPointSheaf X.left hX x' hx'))
```

## Tag 0G26, a lemma

[Tag 0G26](https://stacks.math.columbia.edu/tag/0G26) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DerivedVarieties.Orlov.fullyFaithful_of_fixes_zeroDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/FixingZeroDimensional.lean, line 799](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Orlov/FixingZeroDimensional.lean#L799).

> **[Stacks, Tag 0G26].** Let `k` be a field, let `X` be a proper scheme over `k` which is
> regular, and let `F : D_perf(𝒪_X) ⥤ D_perf(𝒪_X)` be a `k`-linear exact functor. Assume that for
> every coherent `𝒪_X`-module `𝓕` with `dim Supp(𝓕) = 0` there is an isomorphism `𝓕 ≅ F(𝓕)`. Then
> `F` is fully faithful.
>
> Here `𝓕` is read in `D_perf(𝒪_X)` placed in degree zero (it is perfect, `X` being regular, and the
> hypothesis is asked for every proof of that); the isomorphism is taken in `D(𝒪_X)`, which is the
> same as one in the full subcategory `D_perf(𝒪_X)`. "Exact" is a triangulated functor, and
> `k`-linearity is for the structure induced by the structure morphism
> (`AlgebraicGeometry.modulesLinear`). By [Stacks, Tag 0G25] it suffices that `F` is bijective on
> `Ext` between closed-point skyscrapers, which is
> `bijective_map_shift_perfectPointSheaf_of_fixes_zeroDimensional`.

```lean
theorem fullyFaithful_of_fixes_zeroDimensional (hX : IsRegular X.left)
    (F : PerfectDerivedCategory X.left ⥤ PerfectDerivedCategory X.left) [F.CommShift ℤ]
    [F.IsTriangulated]
    (hlin : letI : Linear k X.left.Modules := modulesLinear k X; F.Linear k)
    (hfix : ∀ (𝓕 : X.left.Modules), 𝓕.IsCoherent →
      topologicalKrullDim (SheafOfModules.supp 𝓕) = 0 →
      ∀ h𝓕 : IsPerfect (X := X.left.toRingedSpace)
          ((DerivedCategory.singleFunctor X.left.Modules 0).obj 𝓕),
        Nonempty ((F.obj ⟨_, h𝓕⟩).obj ≅ (DerivedCategory.singleFunctor X.left.Modules 0).obj 𝓕)) :
    Nonempty F.FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.11, Tag 0G23](https://stacks.math.columbia.edu/tag/0G23)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
