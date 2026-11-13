---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.SpacesEtale.extensionByZeroConstant_preservesBinaryCoproduct, AlgebraicGeometry.Space.SpacesEtale.extensionByZeroConstantTensorIso, AlgebraicGeometry.Space.SpacesEtale.extensionByZeroConstantTensorIso_hom_generator, AlgebraicGeometry.Space.SpacesEtale.koszulAugmentation, AlgebraicGeometry.Space.SpacesEtale.koszulAugmentation_quasiIso, AlgebraicGeometry.Space.SpacesEtale.alternatingCechComplex, AlgebraicGeometry.Space.SpacesEtale.alternatingCechToDerivedGlobalSections, AlgebraicGeometry.Space.SpacesEtale.exists_alternatingCechExtSpectralSequence
statement: formalized
proof: formalized
---

# 69.6 The alternating Čech complex

Section 69.6 of the Stacks Project, [Tag 0721](https://stacks.math.columbia.edu/tag/0721). 7 tags here are carried by 28 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0722, a lemma

[Tag 0722](https://stacks.math.columbia.edu/tag/0722) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.extensionByZeroConstant_preservesBinaryCoproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleCoproduct.lean, line 584](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleCoproduct.lean#L584). The attribute's comment: “coproduct\_sum”.

> The two canonical maps induced by the inclusions into a binary coproduct of the
> spaces-étale site give a direct-sum decomposition of extensions by zero.

```lean
theorem extensionByZeroConstant_preservesBinaryCoproduct
    (U₁ U₂ U : SpacesEtale B S hS X)
    (i₁ : U₁ ⟶ U) (i₂ : U₂ ⟶ U)
    (hU : IsColimit (BinaryCofan.mk i₁ i₂)) :
    Nonempty (IsColimit (BinaryCofan.mk
      (extensionByZeroConstantMap B S hS X i₁)
      (extensionByZeroConstantMap B S hS X i₂)))
```

**`AlgebraicGeometry.Space.SpacesEtale.extensionByZeroConstantTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleTensor.lean, line 841](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleTensor.lean#L841). The attribute's comment: “product\_tensor”.

> The tensor product of the extensions by zero of the constant sheaf `ℤ` from two objects of
> the spaces-étale site of `X` is the extension by zero from their product.

```lean
def extensionByZeroConstantTensorIso (U₁ U₂ U₁₂ : SpacesEtale B S hS X) (p₁ : U₁₂ ⟶ U₁)
    (p₂ : U₁₂ ⟶ U₂) (h : IsLimit (BinaryFan.mk p₁ p₂)) :
    abelianSheafTensor B S hS X (extensionByZeroConstant B S hS X U₁)
        (extensionByZeroConstant B S hS X U₂) ≅
      extensionByZeroConstant B S hS X U₁₂
```

**`AlgebraicGeometry.Space.SpacesEtale.extensionByZeroConstantTensorIso_hom_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleTensor.lean, line 913](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleTensor.lean#L913). The attribute's comment: “product\_tensor on generators”.

> The tensor-product isomorphism sends the pure tensor of the generators indexed by `φ₁` and
> `φ₂` to the generator indexed by their pairing into the product.

```lean
theorem extensionByZeroConstantTensorIso_hom_generator (U₁ U₂ U₁₂ : SpacesEtale B S hS X)
    (p₁ : U₁₂ ⟶ U₁) (p₂ : U₁₂ ⟶ U₂) (h : IsLimit (BinaryFan.mk p₁ p₂))
    (V : SpacesEtale B S hS X) (φ₁ : V ⟶ U₁) (φ₂ : V ⟶ U₂) :
    ((extensionByZeroConstantTensorIso B S hS X U₁ U₂ U₁₂ p₁ p₂ h).hom.hom.app
        (Opposite.op V))
      (((toSheafify (topology B S hS X)
        (presheafTensor (extensionByZeroConstant B S hS X U₁).obj
          (extensionByZeroConstant B S hS X U₂).obj)).app (Opposite.op V))
        (TensorProduct.tmul ℤ (extensionByZeroConstantGenerator B S hS X U₁ V φ₁)
          (extensionByZeroConstantGenerator B S hS X U₂ V φ₂))) =
      extensionByZeroConstantGenerator B S hS X U₁₂ V (h.lift (BinaryFan.mk φ₁ φ₂))
```

## Tag 0723, an equation

[Tag 0723](https://stacks.math.columbia.edu/tag/0723) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.koszulAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/KoszulComplex.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/KoszulComplex.lean#L176). The attribute's comment: “the augmentation K^• ⟶ ℤ[0]”.

> **Stacks 0723.** The augmentation `K^• ⟶ ℤ[0]` of the complex `K^•` attached to an object
> of the spaces-étale site of `X`: the trace in degree `0` and zero in higher degrees.

```lean
def koszulAugmentation (U : SpacesEtale B S hS X) :
    koszulComplex B S hS X U ⟶
      (ChainComplex.single₀ (Sheaf (topology B S hS X) AddCommGrpCat.{u + 1})).obj
        (constantIntSheaf B S hS X)
```

**`AlgebraicGeometry.Space.SpacesEtale.koszulAugmentation_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/KoszulResolution.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/KoszulResolution.lean#L401). The attribute's comment: “the augmentation is a quasi-isomorphism for a surjective cover”.

> **Stacks 0723.** For an algebraic space `U` étale and surjective over `X`, the augmentation
> `K^• ⟶ ℤ[0]` of the Koszul complex of the trace `j_{U!} ℤ ⟶ ℤ` is a quasi-isomorphism: `K^•`
> is a resolution of the constant sheaf `ℤ` on the spaces-étale site of `X`.

```lean
theorem koszulAugmentation_quasiIso (U : SpacesEtale B S hS X)
    (hsurj : IsSurjective B S hS U.obj.hom.hom) :
    QuasiIso (koszulAugmentation B S hS X U)
```

## Tag 0724, a definition

[Tag 0724](https://stacks.math.columbia.edu/tag/0724) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.alternatingCechComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/Complex.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/Complex.lean#L66).

> **Stacks 0724.** The alternating Čech complex `Č^•_alt(f, F)` associated to an abelian
> sheaf `F` on the spaces-étale site of `X` and an object `U` of that site: the complex
> `Hom(K^0, F) → Hom(K^1, F) → Hom(K^2, F) → …` with Hom groups computed in `Ab(X_étale)` and
> `K^p = ∧^{p+1} j_{U!} ℤ`.

```lean
def alternatingCechComplex (U : SpacesEtale B S hS X)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    CochainComplex AddCommGrpCat.{u + 1} ℕ
```

## Tag 0725, a lemma

[Tag 0725](https://stacks.math.columbia.edu/tag/0725) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.alternatingCechToDerivedGlobalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DerivedGlobalSections.lean, line 557](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DerivedGlobalSections.lean#L557). The attribute's comment: “the canonical map Č^•\_alt(f, ℱ) ⟶ RΓ(X, ℱ) in D(Ab)”.

> Let `S` be a scheme, let `f : U ⟶ X` be a surjective étale morphism of algebraic spaces over
> `S` and let `ℱ` be an abelian sheaf on the spaces-étale site of `X`. There is a canonical map
>
> `Č^•_alt(f, ℱ) ⟶ RΓ(X, ℱ)`
>
> in `D(Ab)`, where `Č^•_alt(f, ℱ)` is the alternating Čech complex of [Stacks 0724] and
> `RΓ(X, ℱ)` is represented by the global sections of an injective resolution of `ℱ`, so that
> `H^n(RΓ(X, ℱ)) = H^n(X, ℱ)` by `derivedGlobalSectionsHomologyAddEquivSheafH`.
>
> It is the composite of the map into the total complex of the Hom bicomplex `Hom(K^p, I^q)` with
> the inverse of the quasi-isomorphism `Γ(X, I^•) ⟶ Tot(Hom(K^•, I^•))` of [Stacks 0133].
>
> The other assertion of [Stacks 0725], the spectral sequence with `E₁^{p,q} = Ext^q(K^p, ℱ)`
> converging to `H^{p+q}(X, ℱ)`, is
> `AlgebraicGeometry.Space.SpacesEtale.exists_alternatingCechCohomologySpectralSequence`.

```lean
def alternatingCechToDerivedGlobalSections (U : SpacesEtale B S hS X)
    (hsurj : IsSurjective B S hS U.obj.hom.hom)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    DerivedCategory.Q.obj (alternatingCechComplexExtend B S hS X U F) ⟶
      derivedGlobalSections B S hS X F
```

**`AlgebraicGeometry.Space.SpacesEtale.exists_alternatingCechExtSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/ExtSpectralSequence.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/ExtSpectralSequence.lean#L167). The attribute's comment: “the spectral sequence with E₁^\{p,q} = Ext^q(K^p, ℱ), abutting to Ext^\{p+q}(K^•, ℱ)”.

> **Stacks 0725, the first page of the spectral sequence.** Let `X` be an algebraic space over
> a scheme `S`, let `U` be an algebraic space étale over `X` and let `ℱ` be an abelian sheaf on the
> spaces-étale site of `X`. There is a cohomological spectral sequence, starting on page one, with
> `E₁^{p,q} = Ext^q_{Ab(X_étale)}(K^p, ℱ)` for `K^p = ∧^{p+1} j_{U!} ℤ` the terms of the Koszul
> complex, abutting to the hyper-`Ext` groups `Ext^{p+q}(K^•, ℱ)` of the Koszul complex.
>
> It is the spectral sequence of the total complex of the Hom bicomplex `Hom(K^p, I^q)` filtered
> by the Koszul degree, for `I^•` an injective resolution of `ℱ`.

```lean
theorem exists_alternatingCechExtSpectralSequence (U : SpacesEtale B S hS X)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 2} 1,
      (∀ (p : ℕ) (q : ℤ), Nonempty ((E.page 1).X ((p : ℤ), q) ≅
        AddCommGrpCat.of (Abelian.zExt ((koszulComplex B S hS X U).X p) F q))) ∧
      SpectralSequence.AbutsTo E (fun n ↦ AddCommGrpCat.of
        (DerivedCategory.Ext (DerivedCategory.Q.obj (koszulCochainComplex B S hS X U))
          ((DerivedCategory.singleFunctor
            (Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) 0).obj F) n))
```

**`AlgebraicGeometry.Space.SpacesEtale.exists_alternatingCechCohomologySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/ExtSpectralSequence.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/ExtSpectralSequence.lean#L256). The attribute's comment: “the abutment is the cohomology of X, for a surjective cover”.

> **Stacks 0725.** Let `X` be an algebraic space over a scheme `S`, let `U` be an algebraic
> space étale and *surjective* over `X` and let `ℱ` be an abelian sheaf on the spaces-étale site
> of `X`. There is a first-quadrant cohomological spectral sequence, starting on page one, with
> `E₁^{p,q} = Ext^q_{Ab(X_étale)}(K^p, ℱ)` for `K^p = ∧^{p+1} j_{U!} ℤ` the terms of the Koszul
> complex, abutting to the sheaf cohomology `H^{p+q}(X, ℱ)`.
>
> The abutment is written as the `Ext` group out of the constant sheaf `ℤ`, which is Mathlib's
> definition of sheaf cohomology; the last conjunct records that identification.

```lean
theorem exists_alternatingCechCohomologySpectralSequence (U : SpacesEtale B S hS X)
    (hsurj : IsSurjective B S hS U.obj.hom.hom)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 2} 1,
      (∀ (p : ℕ) (q : ℤ), Nonempty ((E.page 1).X ((p : ℤ), q) ≅
        AddCommGrpCat.of (Abelian.zExt ((koszulComplex B S hS X U).X p) F q))) ∧
      (∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((E.page 1).X (p, q))) ∧
      SpectralSequence.AbutsTo E
        (fun n ↦ AddCommGrpCat.of (Abelian.zExt (constantIntSheaf B S hS X) F n)) ∧
      ∀ n : ℕ, Nonempty (AddCommGrpCat.of (Sheaf.H F n) ≅
        AddCommGrpCat.of (Abelian.zExt (constantIntSheaf B S hS X) F (n : ℤ)))
```

## Tag 0726, a lemma

[Tag 0726](https://stacks.math.columbia.edu/tag/0726) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.isIso_signTwistToKoszul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean, line 847](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean#L847). The attribute's comment: “the canonical map ℤ(sign) ⟶ K^p is an isomorphism”.

> **Stacks 0726.** The canonical map `ℤ(sign) ⟶ K^p` from the sign twist of `W_p` to the
> `(p+1)`-st exterior power of the extension by zero of `ℤ` from `U` is an isomorphism: it is the
> sheafification of a map of presheaves which is both locally injective and locally
> surjective.

```lean
theorem isIso_signTwistToKoszul (U : SpacesEtale B S hS X) (p : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom) :
    IsIso (signTwistToKoszul B S hS X U p hsep)
```

**`AlgebraicGeometry.Space.SpacesEtale.bijective_koszulHomToSignSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean, line 865](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean#L865). The attribute's comment: “bijectivity of the map Hom(K^p, F) ⟶ anti-invariant sections”.

> **Stacks 0726.** The canonical map from `Hom(K^p, ℱ)` to the `S_{p+1}`-anti-invariant
> sections of `ℱ` over `W_p` is bijective: it is precomposition with the isomorphism
> `ℤ(sign) ⟶ K^p` followed by the identification of maps out of `ℤ(sign)` with anti-invariant
> sections.

```lean
theorem bijective_koszulHomToSignSections (U : SpacesEtale B S hS X) (p : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    Function.Bijective (koszulHomToSignSections B S hS X U p hsep F).hom
```

**`AlgebraicGeometry.Space.SpacesEtale.koszulHomSignSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean, line 883](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean#L883). The attribute's comment: “the map Hom(K^p, F) ⟶ anti-invariant sections is an isomorphism of groups”.

> **Stacks 0726.** The identification of `Hom(K^p, ℱ)` with the group of
> `S_{p+1}`-anti-invariant sections of `ℱ` over `W_p`, as an isomorphism of abelian groups.

```lean
def koszulHomSignSectionsEquiv (U : SpacesEtale B S hS X) (p : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    ((koszulComplex B S hS X U).X p ⟶ F) ≃+
      characterSections (diagonalComplement B S hS X U (p + 1) hsep)
        (diagonalComplementAut B S hS X U (p + 1) hsep) Equiv.Perm.sign F.obj
```

**`AlgebraicGeometry.Space.SpacesEtale.freeAction_and_bijective_koszulHomToSignSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean, line 902](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/AntiInvariantSections.lean#L902).

> **Stacks 0726.** For `U` étale and separated over `X` the space
> `W_p = U ×_X ⋯ ×_X U ∖ (all diagonals)` with `p + 1` factors carries a free action of the
> symmetric group on `p + 1` letters over `X`, and for every abelian sheaf `ℱ` on the
> spaces-étale site of `X` the canonical map from `Hom(K^p, ℱ)` to the `S_{p+1}`-anti-invariant
> sections of `ℱ` over `W_p` is bijective, functorially in `ℱ`.
>
> Freeness is stated in the shape a site asks for: a morphism `φ : V ⟶ W_p` fixed by `σ` forces
> `σ = 1` unless the empty sieve covers `V`.  Surjectivity of `U ⟶ X`, which Stacks 0726 also
> assumes, is not used: it is what makes the Koszul complex a resolution.

```lean
theorem freeAction_and_bijective_koszulHomToSignSections (U : SpacesEtale B S hS X) (p : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom) :
    (∀ (V : SpacesEtale B S hS X) (φ : V ⟶ diagonalComplement B S hS X U (p + 1) hsep)
        (σ : Equiv.Perm (Fin (p + 1))),
        φ ≫ (diagonalComplementAut B S hS X U (p + 1) hsep σ).asIso.hom = φ →
          (⊥ : Sieve V) ∈ topology B S hS X V ∨ σ = 1) ∧
      (∀ F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1},
        Function.Bijective (koszulHomToSignSections B S hS X U p hsep F).hom) ∧
      (∀ (F F' : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) (k : F ⟶ F')
        (g : (koszulComplex B S hS X U).X p ⟶ F),
        (((koszulHomToSignSections B S hS X U p hsep F').hom (g ≫ k)).1 :
            F'.obj.obj (op (diagonalComplement B S hS X U (p + 1) hsep))) =
          k.hom.app (op (diagonalComplement B S hS X U (p + 1) hsep))
            (((koszulHomToSignSections B S hS X U p hsep F).hom g).1))
```

**`AlgebraicGeometry.Space.SpacesEtale.diagonalComplement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean#L488). The attribute's comment: “the space W\_p”.

> **Stacks 0726.** The space `W = U ×_X ⋯ ×_X U ∖ (all diagonals)` with `n` factors, as an
> object of the spaces-étale site of `X`: the complement of the diagonals is an open subspace of
> `U^n`, and an open subspace of an object of the site is again one.

```lean
def diagonalComplement (U : SpacesEtale B S hS X) (n : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom) : SpacesEtale B S hS X
```

**`AlgebraicGeometry.Space.SpacesEtale.diagonalComplementAut`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean, line 638](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean#L638). The attribute's comment: “the action of S\_\{p+1} on W\_p over X”.

> **Stacks 0726.** The action of the symmetric group on `n` letters on `W` by permuting the
> factors of `U^n`.  It is an action over `X` because `W` and the permutations of the factors
> live in the spaces-étale site of `X`.

```lean
def diagonalComplementAut (U : SpacesEtale B S hS X) (n : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom) :
    Equiv.Perm (Fin n) →* Aut (diagonalComplement B S hS X U n hsep)
```

**`AlgebraicGeometry.Space.SpacesEtale.isEmpty_points_of_comp_diagonalComplementAut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean, line 696](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean#L696). The attribute's comment: “freeness of the action of S\_\{p+1} on W\_p: a fixed morphism has empty source”.

> **Stacks 0726.** The action of the symmetric group on `W` is free: an object of the site
> carrying a morphism to `W` fixed by a permutation `σ ≠ 1` has no points.
>
> Pick `i` with `σ⁻¹ i ≠ i`.  A point of `V` would give a point of `U^n` at which the factors of
> index `i` and `σ⁻¹ i` agree, whereas the points of `W` avoid all the diagonals.

```lean
theorem isEmpty_points_of_comp_diagonalComplementAut (U : SpacesEtale B S hS X) (n : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom) {V : SpacesEtale B S hS X}
    (φ : V ⟶ diagonalComplement B S hS X U n hsep) (σ : Equiv.Perm (Fin n)) (hσ : σ ≠ 1)
    (hφ : φ ≫ (diagonalComplementAut B S hS X U n hsep σ).asIso.hom = φ) :
    IsEmpty (points B S hS (underlying B S hS X V).1)
```

**`AlgebraicGeometry.Space.SpacesEtale.eq_one_of_comp_diagonalComplementAut`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean, line 725](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean#L725). The attribute's comment: “freeness of the action of S\_\{p+1} on W\_p”.

> **Stacks 0726.** The action of the symmetric group on `W` is free, in the shape the
> site-theoretic notion of a torsor asks for: a morphism `φ : V ⟶ W` fixed by `σ` forces `σ = 1`
> unless the empty sieve covers `V`.

```lean
theorem eq_one_of_comp_diagonalComplementAut (U : SpacesEtale B S hS X) (n : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom) {V : SpacesEtale B S hS X}
    (φ : V ⟶ diagonalComplement B S hS X U n hsep) (σ : Equiv.Perm (Fin n))
    (hφ : φ ≫ (diagonalComplementAut B S hS X U n hsep σ).asIso.hom = φ) :
    (⊥ : Sieve V) ∈ topology B S hS X V ∨ σ = 1
```

**`AlgebraicGeometry.Space.SpacesEtale.signTwistToKoszul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean, line 868](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean#L868). The attribute's comment: “the canonical map ℤ(sign) ⟶ K^p”.

> **Stacks 0726.** The canonical map `ℤ(sign) ⟶ K^p` from the sign twist of `W_p` to the
> `(p+1)`-st exterior power of the extension by zero of `ℤ` from `U`: the sheafification of the
> map sending the class of a morphism `V ⟶ W_p` to the wedge of its `p + 1` components.

```lean
def signTwistToKoszul (U : SpacesEtale B S hS X) (p : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom) :
    signTwist B S hS X U (p + 1) hsep ⟶ (koszulComplex B S hS X U).X p
```

**`AlgebraicGeometry.Space.SpacesEtale.koszulHomToSignSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean, line 880](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean#L880). The attribute's comment: “the map Hom(K^p, F) ⟶ S\_\{p+1}-anti-invariant sections of F over W\_p”.

> **Stacks 0726.** The canonical map from `Hom(K^p, ℱ)` to the `S_{p+1}`-anti-invariant
> sections of `ℱ` over `W_p`: precompose with `ℤ(sign) ⟶ K^p` and use that a map out of
> `ℤ(sign)` is the same thing as an anti-invariant section over `W_p`.
>
> Stacks 0726 asserts in addition that this map is bijective, which is not proved here.

```lean
def koszulHomToSignSections (U : SpacesEtale B S hS X) (p : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    AddCommGrpCat.of ((koszulComplex B S hS X U).X p ⟶ F) ⟶
      AddCommGrpCat.of (characterSections (diagonalComplement B S hS X U (p + 1) hsep)
        (diagonalComplementAut B S hS X U (p + 1) hsep) Equiv.Perm.sign F.obj)
```

**`AlgebraicGeometry.Space.SpacesEtale.koszulHomToSignSections_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean, line 899](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/DiagonalComplement.lean#L899). The attribute's comment: “functoriality in F of the map Hom(K^p, F) ⟶ anti-invariant sections”.

> **Stacks 0726.** The map from `Hom(K^p, ℱ)` to the `S_{p+1}`-anti-invariant sections of `ℱ`
> over `W_p` is functorial in `ℱ`: composing a map `K^p ⟶ ℱ` with `ℱ ⟶ ℱ'` takes the
> corresponding section to its image over `W_p`.

```lean
theorem koszulHomToSignSections_naturality (U : SpacesEtale B S hS X) (p : ℕ)
    (hsep : IsSeparated B S hS U.1.hom.hom)
    {F F' : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}} (k : F ⟶ F')
    (g : (koszulComplex B S hS X U).X p ⟶ F) :
    (((koszulHomToSignSections B S hS X U p hsep F').hom (g ≫ k)).1 :
        F'.obj.obj (op (diagonalComplement B S hS X U (p + 1) hsep))) =
      k.hom.app (op (diagonalComplement B S hS X U (p + 1) hsep))
        (((koszulHomToSignSections B S hS X U p hsep F).hom g).1)
```

## Tag 0727, a lemma

[Tag 0727](https://stacks.math.columbia.edu/tag/0727) in the Stacks Project.

**`AlgebraicGeometry.Space.freeActionChartSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionQuotientSignTwist.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionQuotientSignTwist.lean#L83). The attribute's comment: “the identification of the chi-semi-invariant sections over the chart with the global sections of the twist, for the quotient of an object of a big fppf site by a free action of a u-small group. The source's group is finite; finiteness is not used here. The locally free rank one half is freeActionChartTwistOverIso”.

> **[Stacks, Tag 0727], the sections half, for the quotient of an object of a big fppf site by
> a free action.**  The `χ`-semi-invariant sections of an abelian sheaf `ℱ` on the spaces-étale
> site of the quotient `U = V/G` over the chart `h_V` are the global sections over `U` of the
> twist `ℱ ⊗_ℤ ℤ(χ)`.
>
> The chart is a `G`-torsor over the final object of that site, which is what
> `CategoryTheory.IsTorsorObject.twistTensorSectionsEquiv` asks for; the final object is terminal
> by `AlgebraicGeometry.Space.SpacesEtale.final_isTerminal`.

```lean
def freeActionChartSectionsEquiv
    (F : Sheaf (SpacesEtale.topology B S hS (actionQuotientSpace G B S hS V a ha))
      AddCommGrpCat.{u + 1}) :
    characterSections (freeActionQuotientChart G B S hS V a ha)
        (freeActionChartAut G B S hS V a ha) χ F.obj ≃+
      (characterTwistTensor F.obj (freeActionChartAut G B S hS V a ha) χ
        (SpacesEtale.topology B S hS (actionQuotientSpace G B S hS V a ha))).obj.obj
        (op (SpacesEtale.final B S hS (actionQuotientSpace G B S hS V a ha)))
```

**`AlgebraicGeometry.Space.freeActionChartTwistOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionQuotientSignTwist.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionQuotientSignTwist.lean#L101). The attribute's comment: “the twist is locally free of rank one, for the quotient of an object of a big fppf site by a free action of a u-small group: it restricts to the constant sheaf Z on the site localized at the chart. The sections half is freeActionChartSectionsEquiv”.

> **[Stacks, Tag 0727], the local freeness half, for the quotient of an object of a big fppf
> site by a free action.**  The twist `ℤ(χ)` on the spaces-étale site of the quotient `U = V/G`
> restricts to the constant sheaf `ℤ` on the site localized at the chart `h_V`, which is the
> sheaf-theoretic form of being locally free of rank one.

```lean
def freeActionChartTwistOverIso :
    (constantSheaf ((SpacesEtale.topology B S hS (actionQuotientSpace G B S hS V a ha)).over
        (freeActionQuotientChart G B S hS V a ha)) AddCommGrpCat.{u + 1}).obj
        (AddCommGrpCat.of (ULift.{u + 1} ℤ)) ≅
      ((SpacesEtale.topology B S hS (actionQuotientSpace G B S hS V a ha)).overPullback
          AddCommGrpCat.{u + 1} (freeActionQuotientChart G B S hS V a ha)).obj
        (characterTwist (freeActionQuotientChart G B S hS V a ha)
          (freeActionChartAut G B S hS V a ha) χ
          (SpacesEtale.topology B S hS (actionQuotientSpace G B S hS V a ha)))
```

**`AlgebraicGeometry.Space.characterTwistOfOrbitQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionSpacesEtaleCharacterTwist.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/FreeActionSpacesEtaleCharacterTwist.lean#L90).

> **Stacks 0727.** Let `W` be an algebraic space over a scheme `S` carrying a free action of
> a group `G`, let `U = W/G` be the quotient of [Stacks 071S] and let `χ : G → ℤˣ` be a
> character. Then there is a sheaf of `ℤ`-modules `ℤ(χ)` on the spaces-étale site of `U` which is
> locally free of rank one — trivial over the covering of `U` by `W` — and satisfies
>
> ```
> H⁰(W, F|_W)^χ = H⁰(U, F ⊗_ℤ ℤ(χ))
> ```
>
> for every abelian sheaf `F` on that site.
>
> This is `CategoryTheory.characterTwistOfQuotient` at the spaces-étale site of `U`: the action
> of `G` on `W` is free there and the quotient morphism exhibits the final object as `W/G`.

```lean
def characterTwistOfOrbitQuotient (χ : G →* ℤˣ) :
    CharacterTwistOfQuotient (orbitQuotientEtaleSource hnat hW hfree)
      (orbitQuotientAut hnat hW hfree) χ
      (SpacesEtale.topology B S hS (orbitQuotientSpace hnat hW hfree))
      (SpacesEtale.final B S hS (orbitQuotientSpace hnat hW hfree))
```

**`CategoryTheory.IsTorsorObject.twistTensorSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleCharacterTwistTorsor.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleCharacterTwistTorsor.lean#L552). The attribute's comment: “the sections transforming according to the character”.

> For a torsor `W` under a group `G` over the final object of a site and a character
> `χ : G → ℤˣ`, the sections of an abelian sheaf `F` over `W` that transform according to `χ` are
> the global sections of `F ⊗_ℤ ℤ(χ)`, where `ℤ(χ)` is the twisted free abelian sheaf on `W`.

```lean
def twistTensorSectionsEquiv (F : Sheaf J AddCommGrpCat.{u + 1}) :
    characterSections W act χ F.obj ≃+ (characterTwistTensor F.obj act χ J).obj.obj (op T)
```

**`CategoryTheory.characterTwistOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CharacterTwistLocalFreeness.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CharacterTwistLocalFreeness.lean#L146). The attribute's comment: “the twist is locally free of rank one”.

> **The twist `ℤ(χ)` becomes constant on the localized site `Over W`**: its pullback along
> `Over.forget W` is the constant sheaf with value `ℤ`. This is the sheaf-theoretic form of the
> freeness of rank one of `ℤ(χ)` over a torsor.

```lean
noncomputable def characterTwistOverIso (h : IsTorsorObject act J) (χ : G →* ℤˣ) :
    (constantSheaf (J.over W) AddCommGrpCat.{v}).obj (AddCommGrpCat.of (ULift.{v} ℤ)) ≅
      (J.overPullback AddCommGrpCat.{v} W).obj (characterTwist W act χ J)
```

**`CategoryTheory.characterTwistOfQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/FreeQuotientCharacterTwist.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/FreeQuotientCharacterTwist.lean#L120).

> **Stacks 0727.** Let `C` be a site with final object `T`, let a group `G` act freely by
> automorphisms on an object `W` of `C`, let `q : W ⟶ T` exhibit `T` as the quotient `W/G` and
> let `χ : G → ℤˣ` be a character. Then there is a sheaf of `ℤ`-modules `ℤ(χ)` on the base which
> is locally free of rank one — trivial over the covering of the base by `W` — and satisfies
> `H⁰(W, F|_W)^χ = H⁰(T, F ⊗_ℤ ℤ(χ))` for every abelian sheaf `F` on the base.
>
> That `W` is a `G`-torsor over the base is *not* assumed: it is the first sentence of the
> source's proof, and is proved from freeness and the quotient identification in
> `CategoryTheory.IsOrbitQuotient.isTorsorObject`.

```lean
noncomputable def characterTwistOfQuotient {T : C} {q : W ⟶ T} (hfree : ActsFreelyOnObject act J)
    (hq : IsOrbitQuotient act J q) (hT : IsTerminal T) (χ : G →* ℤˣ) :
    CharacterTwistOfQuotient W act χ J T
```

## Tag 0728, a lemma

[Tag 0728](https://stacks.math.columbia.edu/tag/0728) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.exists_alternatingCechSignTwistedSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/ExtSpectralSequence.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/ExtSpectralSequence.lean#L330). The attribute's comment: “the row q = 0 of the E₁-page, as the S\_\{p+1}-anti-invariant sections of ℱ over W\_p, and the convergence to H^\{p+q}(X, ℱ)”.

> **Stacks 0728.** Let `S` be a scheme, let `f : U ⟶ X` be a surjective, étale and separated
> morphism of algebraic spaces over `S` and let `ℱ` be an abelian sheaf on the spaces-étale site
> of `X`.  The spectral sequence of [Stacks 0725] is concentrated in the first quadrant, the row
> `q = 0` of its first page is the group of `S_{p+1}`-anti-invariant sections of `ℱ` over
> `W_p = U ×_X ⋯ ×_X U ∖ (all diagonals)`, and it converges to the sheaf cohomology
> `H^{p+q}(X, ℱ)`.
>
> The group of anti-invariant sections is what [Stacks 0727] identifies with
> `H^0(U_p, ℱ|_{U_p} ⊗_ℤ ℤ(χ_p))` for `U_p = W_p/S_{p+1}`; the higher rows of the first page are
> stated here as the `Ext` groups out of `K^p` of [Stacks 0725], the quotient `U_p` of an
> algebraic space by a free action of a finite group not being available.

```lean
theorem exists_alternatingCechSignTwistedSpectralSequence (U : SpacesEtale B S hS X)
    (hsurj : IsSurjective B S hS U.obj.hom.hom)
    (hsep : IsSeparated B S hS U.obj.hom.hom)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 2} 1,
      (∀ (p : ℕ) (q : ℤ), Nonempty ((E.page 1).X ((p : ℤ), q) ≅
        AddCommGrpCat.of (Abelian.zExt ((koszulComplex B S hS X U).X p) F q))) ∧
      (∀ p : ℕ, Nonempty ((E.page 1).X ((p : ℤ), 0) ≃+
        characterSections (diagonalComplement B S hS X U (p + 1) hsep)
          (diagonalComplementAut B S hS X U (p + 1) hsep) Equiv.Perm.sign F.obj)) ∧
      (∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((E.page 1).X (p, q))) ∧
      SpectralSequence.AbutsTo E
        (fun n ↦ AddCommGrpCat.of (Abelian.zExt (constantIntSheaf B S hS X) F n)) ∧
      ∀ n : ℕ, Nonempty (AddCommGrpCat.of (Sheaf.H F n) ≅
        AddCommGrpCat.of (Abelian.zExt (constantIntSheaf B S hS X) F (n : ℤ)))
```

**`AlgebraicGeometry.Space.SpacesEtale.exists_alternatingCechQuotientSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuotientSpectralSequence.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlternatingCech/QuotientSpectralSequence.lean#L103). The attribute's comment: “the E₁-page is H^q(U\_p, F|\_\{U\_p} ⊗ Z(χ\_p)) in every degree q, and the convergence to H^\{p+q}(X, F)”.

> **Stacks 0728.** Let `S` be a scheme, let `f : U ⟶ X` be a surjective, étale and separated
> morphism of algebraic spaces over `S` and let `ℱ` be an abelian sheaf on the spaces-étale site
> of `X`. Write `W_p = U ×_X ⋯ ×_X U ∖ (all diagonals)` with `p + 1` factors, let
> `U_p = W_p/S_{p+1}` and let `ℤ(χ_p)` be the rank one twist of [Stacks 0727] attached to the
> sign character of `S_{p+1}`. The spectral sequence of [Stacks 0725] is concentrated in the
> first quadrant, its first page is
>
> `E₁^{p,q} = H^q(U_p, ℱ|_{U_p} ⊗_ℤ ℤ(χ_p))`
>
> in every degree `q`, and it converges to the sheaf cohomology `H^{p+q}(X, ℱ)`.
>
> Cohomology is written as the `Ext` group out of the constant sheaf `ℤ` read in the derived
> category; two conjuncts identify those groups with Mathlib's sheaf cohomology, on `X` for the
> abutment and on `U_p` for the first page, and the last one identifies the coefficient sheaf on
> `U_p` with the tensor product of `ℱ|_{U_p}` against the twist of [Stacks 0727]. The first
> conjunct records the first page in the `Ext` form of [Stacks 0725] out of the terms
> `K^p = ∧^{p+1} j_{U!} ℤ` of the Koszul complex.

```lean
theorem exists_alternatingCechQuotientSpectralSequence
    (hsurj : IsSurjective B S hS U.1.hom.hom)
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{u + 1}) :
    ∃ E : CohomologicalSpectralSequence AddCommGrpCat.{u + 2} 1,
      (∀ (p : ℕ) (q : ℤ), Nonempty ((E.page 1).X ((p : ℤ), q) ≅
        AddCommGrpCat.of (zExt ((koszulComplex B S hS X U).X p) F q))) ∧
      (∀ p q : ℕ, Nonempty ((E.page 1).X ((p : ℤ), (q : ℤ)) ≃+
        zExt (constantIntSheaf B S hS (diagonalComplementQuotient B S hS X U (p + 1) hsep))
          (diagonalComplementTwistedRestriction B S hS X U hsep p F) (q : ℤ))) ∧
      (∀ p q : ℤ, p < 0 ∨ q < 0 → IsZero ((E.page 1).X (p, q))) ∧
      SpectralSequence.AbutsTo E
        (fun n ↦ AddCommGrpCat.of (zExt (constantIntSheaf B S hS X) F n)) ∧
      (∀ n : ℕ, Nonempty (AddCommGrpCat.of (Sheaf.H F n) ≅
        AddCommGrpCat.of (zExt (constantIntSheaf B S hS X) F (n : ℤ)))) ∧
      (∀ p q : ℕ, Nonempty (AddCommGrpCat.of
          (Sheaf.H (diagonalComplementTwistedRestriction B S hS X U hsep p F) q) ≅
        AddCommGrpCat.of
          (zExt (constantIntSheaf B S hS (diagonalComplementQuotient B S hS X U (p + 1) hsep))
            (diagonalComplementTwistedRestriction B S hS X U hsep p F) (q : ℤ)))) ∧
      ∀ p : ℕ, Nonempty (diagonalComplementTwistedRestriction B S hS X U hsep p F ≅
        (presheafToSheaf (topology B S hS (diagonalComplementQuotient B S hS X U (p + 1) hsep))
            AddCommGrpCat.{u + 1}).obj
          (AddCommGrpCat.presheafTensor
            ((diagonalComplementQuotientRestriction B S hS X U (p + 1) hsep).obj F).obj
            (characterTwistOfDiagonalComplement B S hS X U (p + 1) hsep
              (diagonalComplementSignCharacter (p + 1))).twist.obj))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.6, Tag 0721](https://stacks.math.columbia.edu/tag/0721)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
