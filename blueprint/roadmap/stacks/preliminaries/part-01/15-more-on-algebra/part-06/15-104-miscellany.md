---
declaration: section
origin: cited
lean: Stacks.AdicSystem.ExtEssentiallyConstant.ext_quotient_ideal_pow_essentially_constant, Stacks.TorIdealPowerVanishing.torMap_idealPowerInclusion_eq_zero, Stacks.PseudoCoherent.DerivedInverseLimit.derivedLimit_tensor_iso, Stacks.ProjectiveDimension.Additivity.projectiveDimension_restrictScalars_quotient_eq_add, Stacks.SubcomplexEnlargement.exists_enlargements_killing_kernel_and_covering_image, Stacks.DerivedCategory.MultiplicationCone.homology_isZero_of_localization_and_cone_isZero, Stacks.Flatness.LocalizationReduction.isomorphic_to_flat_module_of_localization_and_quotient
statement: formalized
proof: formalized
---

# 15.104 Miscellany

Section 15.104 of the Stacks Project, [Tag 0926](https://stacks.math.columbia.edu/tag/0926). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DYJ, a lemma

[Tag 0DYJ](https://stacks.math.columbia.edu/tag/0DYJ) in the Stacks Project.

**`Stacks.AdicSystem.ExtEssentiallyConstant.ext_quotient_ideal_pow_essentially_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean, line 1323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/AdicSystem/ExtRestriction.lean#L1323).

> **Stacks 0DYJ.** If high-degree Ext from a pseudo-coherent complex into every finite module is
> `I`-power torsion, then the inverse system `Ext^p(K, M / I ^ n M)` is essentially constant with
> value `Ext^p(K, M)`, which is also its limit.

```lean
public theorem ext_quotient_ideal_pow_essentially_constant
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (K : DerivedCategory (ModuleCat.{v} A))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (a : ℤ)
    (h : ∀ (N : ModuleCat.{v} A) [Module.Finite A N] (j : ℤ), a ≤ j →
      IsIPowerTorsion A
        (DerivedCategory.Ext K
          ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj N) j) I)
    (p : ℤ) (hp : a ≤ p) (M : ModuleCat.{v} A) [Module.Finite A M] :
    let D : ℕᵒᵖ ⥤ DerivedCategory (ModuleCat.{v} A) :=
      Functor.ofOpSequence
        (X := fun n ↦ (DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj
          (ModuleCat.of A (M ⧸ (I ^ n • ⊤ : Submodule A M)))) (fun n ↦
        (DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).map
          (ModuleCat.ofHom (Submodule.factorPowSucc I M n)))
    let E : ℕᵒᵖ ⥤ ModuleCat.{max u (v + 1)} A :=
      D ⋙ shiftFunctor (DerivedCategory (ModuleCat.{v} A)) p ⋙
        (linearCoyoneda A (DerivedCategory (ModuleCat.{v} A))).obj (op K)
    let X := ModuleCat.of A
      (DerivedCategory.Ext K
        ((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).obj M) p)
    ∃ π : (Functor.const ℕᵒᵖ).obj X ⟶ E,
      (∀ n : ℕ, π.app (op n) = ModuleCat.ofHom (Linear.rightComp A K
        (((DerivedCategory.singleFunctor (ModuleCat.{v} A) 0).map
          (ModuleCat.ofHom
            ((I ^ n • ⊤ : Submodule A M).mkQ)))⟦p⟧'))) ∧
      (∃ (n : ℕᵒᵖ) (s : E.obj n ⟶ X),
        EssentiallyConstantPro.IsEssentiallyConstantWith E (Cone.mk X π) n s) ∧
      Nonempty (IsLimit (Cone.mk X π))
```

## Tag 0FXN, a lemma

[Tag 0FXN](https://stacks.math.columbia.edu/tag/0FXN) in the Stacks Project.

**`Stacks.TorIdealPowerVanishing.torMap_idealPowerInclusion_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/IdealPower.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/IdealPower.lean#L142).

> **Stacks Project, Tag 0FXN.** If `M` is a finite module over a Noetherian ring and `N`
> is annihilated by an ideal `I`, then for some positive power of `I` the inclusion
> `IⁿM ⟶ M` induces zero on `Tor_p(-, N)` for every `p ≥ 0`. The index `n` denotes the
> positive exponent `n + 1`.

```lean
public theorem torMap_idealPowerInclusion_eq_zero
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (M N : ModuleCat.{u} A) [Module.Finite A M]
    (hN : I ≤ Module.annihilator A N) :
    let K := (CochainComplex.singleFunctor (ModuleCat.{u} A) 0).obj M
    let N₀ := (DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj N
    ∃ n : ℕ, ∀ p : ℕ,
      (DerivedCategory.homologyFunctor (ModuleCat.{u} A) (-(p : ℤ))).map
          (((DerivedTensorData.canonicalDerivedTensorProduct A).tensor.flip.obj N₀).map
            (DerivedCategory.Q.map
              (image.ι (Stacks.AdicSystem.IdealPowerTensorComparison.idealPowerMultiplication K I
                n)))) = 0
```

## Tag 0D2L, a lemma

[Tag 0D2L](https://stacks.math.columbia.edu/tag/0D2L) in the Stacks Project.

**`Stacks.PseudoCoherent.DerivedInverseLimit.derivedLimit_tensor_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/PseudoCoherent/InverseLimit.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/PseudoCoherent/InverseLimit.lean#L179).

> **Stacks Project, Tag 0D2L.** Let `K` be pseudo-coherent and `(Mₙ)` an inverse
> system of modules. If `L` and `L'` are derived inverse limits of `(Mₙ)` and
> `(K ⊗ᴸ Mₙ)`, respectively, then the canonical comparison
> `L' ⟶ K ⊗ᴸ L` is an isomorphism. Its displayed equation characterizes it as the
> comparison induced by the two Milnor triangles.

```lean
theorem derivedLimit_tensor_iso
    (T : DerivedTensorProduct.{u, v, w} R)
    (P : DerivedProducts.{u, v, w} R)
    (K : D.{u, v, w} R) (hK : IsPseudoCoherent K)
    (M : ℕ → ModuleCat.{max v w} (SmallRing.{u, v, w} R))
    (t : ∀ n, M (n + 1) ⟶ M n) :
    letI := hasProductsOfShapeNat R P
    let S := DerivedCategory.singleFunctor (ModuleCat.{max v w} (SmallRing.{u, v, w} R)) 0
    ∀ (L : D.{u, v, w} R) (ι : L ⟶ ∏ᶜ fun n => S.obj (M n))
      (δ : (∏ᶜ fun n => S.obj (M n)) ⟶ L⟦(1 : ℤ)⟧)
      (_ : IsMilnorTriangle (A := SmallRing.{u, v, w} R) (fun n => S.obj (M n))
        (fun n => S.map (t n)) L ι δ)
      (L' : D.{u, v, w} R)
      (ι' : L' ⟶ ∏ᶜ fun n => (T.tensor.obj K).obj (S.obj (M n)))
      (δ' : (∏ᶜ fun n => (T.tensor.obj K).obj (S.obj (M n))) ⟶ L'⟦(1 : ℤ)⟧)
      (_ : IsMilnorTriangle (A := SmallRing.{u, v, w} R)
        (fun n => (T.tensor.obj K).obj (S.obj (M n)))
        (fun n => (T.tensor.obj K).map (S.map (t n))) L' ι' δ'),
      ∃ e : L' ≅ (T.tensor.obj K).obj L,
        e.hom ≫ (T.tensor.obj K).map ι ≫
          derivedTensorProductComparison R T K (fun n => S.obj (M n)) = ι'
```

## Tag 0929, a lemma

[Tag 0929](https://stacks.math.columbia.edu/tag/0929) in the Stacks Project.

**`Stacks.ProjectiveDimension.Additivity.projectiveDimension_restrictScalars_quotient_eq_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/ProjectiveDimension/Quotient.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/ProjectiveDimension/Quotient.lean#L338).

> **Stacks 0929.** Let `R` be a Noetherian local ring, `I` an ideal of `R`, and `E` a
> nonzero finite `R ⧸ I`-module. If `R ⧸ I` has finite projective dimension over `R` and `E` has
> finite projective dimension over `R ⧸ I`, then the restriction of `E` to `R` has finite
> projective dimension, equal to the sum of the two given projective dimensions.

```lean
theorem projectiveDimension_restrictScalars_quotient_eq_add
    {R : Type u} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] [Small.{v} R]
    (I : Ideal R) (E : Type v) [AddCommGroup E] [Module (R ⧸ I) E]
    [Nontrivial E] [Module.Finite (R ⧸ I) E]
    (hRI : Module.projectiveDimension R (R ⧸ I) ≠ ⊤)
    (hE : Module.projectiveDimension (R ⧸ I) E ≠ ⊤) :
    let E_R := (ModuleCat.restrictScalars.{v} (Ideal.Quotient.mk I)).obj
      (ModuleCat.of (R ⧸ I) E)
    Module.projectiveDimension R E_R ≠ ⊤ ∧
      Module.projectiveDimension R E_R =
        Module.projectiveDimension R (R ⧸ I) + Module.projectiveDimension (R ⧸ I) E
```

## Tag 0GYI, a lemma

[Tag 0GYI](https://stacks.math.columbia.edu/tag/0GYI) in the Stacks Project.

**`Stacks.SubcomplexEnlargement.exists_enlargements_killing_kernel_and_covering_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/SubcomplexEnlargement/CompatibleEnlargements.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/SubcomplexEnlargement/CompatibleEnlargements.lean#L370).

> Compatible subcomplexes of quasi-isomorphic complexes after derived base change can be
> enlarged, with a bound depending only on the ring map, so that the kernel defect vanishes and the
> image defect is covered in every degree.

```lean
public theorem exists_enlargements_killing_kernel_and_covering_image
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] (f : A →+* B) :
    ∃ κ : Cardinal.{max u v},
      letI : (ModuleCat.extendScalars.{u, v, max v (max u w)} f).IsLeftAdjoint :=
        ModuleCat.instIsLeftAdjointExtendScalars.{u, v, max u w} f
      let E : CochainComplex (ModuleCat.{max u v w} A) ℤ ⥤
          CochainComplex (ModuleCat.{max u v w} B) ℤ :=
        (ModuleCat.extendScalars.{u, v, max v (max u w)} f).mapHomologicalComplex
          (ComplexShape.up ℤ)
      let G : CochainComplex (ModuleCat.{max u v w} A) ℤ ⥤
          DerivedCategory (ModuleCat.{max u v w} B) :=
        E ⋙ DerivedCategory.Q (C := ModuleCat.{max u v w} B)
      ∀ (T : DerivedCategory (ModuleCat.{max u v w} A) ⥤
          DerivedCategory (ModuleCat.{max u v w} B))
        (α : DerivedCategory.Q (C := ModuleCat.{max u v w} A) ⋙ T ⟶ G)
        [T.IsLeftDerivedFunctor α
          (HomologicalComplex.quasiIso (ModuleCat.{max u v w} A) (ComplexShape.up ℤ))]
        (M : CochainComplex (ModuleCat.{max u v w} A) ℤ)
        (N : CochainComplex (ModuleCat.{max u v w} B) ℤ),
      ∀ (b : E.obj M ⟶ N),
      IsIso (α.app M ≫
        (DerivedCategory.Q (C := ModuleCat.{max u v w} B)).map b) →
      ∀ (M₁ : CochainComplex (ModuleCat.{max u v w} A) ℤ)
        (N₁ : CochainComplex (ModuleCat.{max u v w} B) ℤ)
        (m₁ : M₁ ⟶ M) (n₁ : N₁ ⟶ N) [Mono m₁] [Mono n₁]
        (b₁ : E.obj M₁ ⟶ N₁),
      E.map m₁ ≫ b = b₁ ≫ n₁ →
      ∃ (M₂ : CochainComplex (ModuleCat.{max u v w} A) ℤ)
        (N₂ : CochainComplex (ModuleCat.{max u v w} B) ℤ)
        (m₂ : M₂ ⟶ M) (n₂ : N₂ ⟶ N) (_ : Mono m₂) (_ : Mono n₂)
        (m₁₂ : M₁ ⟶ M₂) (n₁₂ : N₁ ⟶ N₂) (_ : Mono m₁₂) (_ : Mono n₁₂)
        (b₂ : E.obj M₂ ⟶ N₂),
      m₁₂ ≫ m₂ = m₁ ∧ n₁₂ ≫ n₂ = n₁ ∧ E.map m₂ ≫ b = b₂ ≫ n₂ ∧
      (∀ i : ℤ,
        let H := DerivedCategory.homologyFunctor (ModuleCat.{max u v w} B) i
        kernel.ι (H.map (α.app M₁ ≫
          (DerivedCategory.Q (C := ModuleCat.{max u v w} B)).map b₁)) ≫
          H.map (T.map
            ((DerivedCategory.Q (C := ModuleCat.{max u v w} A)).map m₁₂)) = 0) ∧
      (∀ i : ℤ,
        let H := DerivedCategory.homologyFunctor (ModuleCat.{max u v w} B) i
        imageSubobject (H.map
          ((DerivedCategory.Q (C := ModuleCat.{max u v w} B)).map n₁₂)) ≤
          imageSubobject (H.map (α.app M₂ ≫
            (DerivedCategory.Q (C := ModuleCat.{max u v w} B)).map b₂))) ∧
      Cardinal.mk ((Σ i : ℤ, M₂.X i) ⊕ (Σ i : ℤ, N₂.X i)) ≤
        max (Cardinal.lift.{w} κ)
          (Cardinal.mk ((Σ i : ℤ, M₁.X i) ⊕ (Σ i : ℤ, N₁.X i)))
```

## Tag 0H84, a lemma

[Tag 0H84](https://stacks.math.columbia.edu/tag/0H84) in the Stacks Project.

**`Stacks.DerivedCategory.MultiplicationCone.homology_isZero_of_localization_and_cone_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/ConeBoundedness.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/ConeBoundedness.lean#L94).

> Let `C` be a cone of multiplication by `f` on `M`. If every negative cohomology module of
> `M` vanishes after localizing away from `f`, and the cohomology of `C` vanishes in degrees below
> `-1`, then every negative cohomology module of `M` vanishes.

```lean
theorem homology_isZero_of_localization_and_cone_isZero
    {R : Type u} [CommRing R]
    (f : R) (M C : DerivedCategory (ModuleCat.{v} R))
    (g : M ⟶ C) (h : C ⟶ M⟦1⟧)
    (hC : Triangle.mk (f • 𝟙 M) g h ∈
      distTriang (DerivedCategory (ModuleCat.{v} R)))
    (hM : ∀ i : ℤ, i < 0 →
      IsZero (ModuleCat.of R (LocalizedModule.Away f
        ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj M))))
    (hcone : ∀ i : ℤ, i < -1 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj C)) :
    ∀ i : ℤ, i < 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj M)
```

## Tag 0H85, a lemma

[Tag 0H85](https://stacks.math.columbia.edu/tag/0H85) in the Stacks Project.

**`Stacks.Flatness.LocalizationReduction.isomorphic_to_flat_module_of_localization_and_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalizationReduction.lean, line 502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/LocalizationReduction.lean#L502).

> Let `M ∈ D(R)` have no positive cohomology. If its derived base changes to the
> localization `R_f` and the quotient `R / fR` are each isomorphic to a flat module placed in
> degree zero, then `M` is isomorphic to a flat `R`-module placed in degree zero.

```lean
public theorem isomorphic_to_flat_module_of_localization_and_quotient
    {R : Type u} [CommRing R] (f : R)
    (M : DerivedCategory (ModuleCat.{max v u} R))
    (hM : ∀ i : ℤ, 0 < i →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max v u} R) i).obj M))
    (hAway : ∃ F : ModuleCat.{max v u} (Localization.Away f),
      Module.Flat (Localization.Away f) F ∧
        Nonempty ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars
          (algebraMap R (Localization.Away f))).functor.obj M ≅
            (DerivedCategory.singleFunctor
              (ModuleCat.{max v u} (Localization.Away f)) 0).obj F))
    (hQuot : ∃ F : ModuleCat.{max v u} (R ⧸ Ideal.span {f}),
      Module.Flat (R ⧸ Ideal.span {f}) F ∧
        Nonempty ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars
          (Ideal.Quotient.mk (Ideal.span {f}))).functor.obj M ≅
            (DerivedCategory.singleFunctor
              (ModuleCat.{max v u} (R ⧸ Ideal.span {f})) 0).obj F)) :
    ∃ F : ModuleCat.{max v u} R, Module.Flat R F ∧
      Nonempty (M ≅
        (DerivedCategory.singleFunctor (ModuleCat.{max v u} R) 0).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.104, Tag 0926](https://stacks.math.columbia.edu/tag/0926)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
