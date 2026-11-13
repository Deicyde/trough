---
declaration: section
origin: cited
lean: Stacks.Cohomology.ExtProjectionFormula.extCohomologyIso, Stacks.Cohomology.ExtProjectionFormulaBoundary.extCohomologyIso_qcoh_boundary, Stacks.Cohomology.ExtPerfectProjection.extIso_qcoh_boundary, Stacks.Cohomology.RelativeExt.exists_perfect_relativeExt_comparison, Stacks.Cohomology.RelativeExt.exists_pseudoCoherent_relativeExt_representative, Stacks.Cohomology.RelativeExtCanonical.exists_baseChange_relativeExt_iso, Stacks.Cohomology.RelativeExtCanonical.exists_iso_pseudoCoherentRepresentative
statement: formalized
proof: formalized
---

# 36.28 A projection formula for Ext

Section 36.28 of the Stacks Project, [Tag 08IC](https://stacks.math.columbia.edu/tag/08IC). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A1F, a lemma

[Tag 0A1F](https://stacks.math.columbia.edu/tag/0A1F) in the Stacks Project.

**`Stacks.Cohomology.ExtProjectionFormula.extCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ExtProjectionFormula.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ExtProjectionFormula.lean#L292). The attribute's comment: “the functorial isomorphisms for every i, as a natural isomorphism in ℱ ranging over all 𝒪\_S-modules rather than only the quasi-coherent ones, and Γ(S, 𝒪\_S)-linear; two steps of the source's proof are carried as explicit named hypotheses, the fields projectionFormula and mixedFlatTensor of ExtProjectionInput — invertibility of the projection-formula map of Tag 0B53 at ℱ, which is Tag 08EU and which this library proves only at ℱ = 𝒪\_S, and the identification of 𝒢 ⊗ᴸ Lf^*ℱ with 𝒢 ⊗ f^*ℱ, which is Tag 08DE together with flatness of the terms of 𝒢 over S; the remaining two steps, associativity of the derived tensor product and Leray, are proved, the latter in the unbounded form of Tag 0D5W; the compatibility with boundary maps is NOT carried”.

> In the situation of [Stacks, Tag 0DJQ] there are isomorphisms
>
> `H^i(S, K ⊗^L_{𝒪_S} ℱ) ≅ H^i(X, E ⊗^L_{𝒪_X} (𝒢 ⊗_{𝒪_X} f^*ℱ))`,
>
> functorial in the `𝒪_S`-module `ℱ` — the statement is a natural isomorphism of functors on
> `𝒪_S`-modules, so functoriality is part of its type — and `Γ(S, 𝒪_S)`-linear.  Quasi-coherence
> of `ℱ` is not assumed.
>
> Two steps of the source's proof are carried, as the `projectionFormula` and `mixedFlatTensor`
> fields of `h`: [Stacks, Tag 08EU] at `ℱ`, which this library proves only at `ℱ = 𝒪_S`, and the
> identification `𝒢 ⊗^L_{𝒪_X} Lf^*ℱ ≅ 𝒢 ⊗_{𝒪_X} f^*ℱ`, which is [Stacks, Tag 08DE] together
> with flatness of the `𝒢^n` over `S`.  The other two steps are proved: associativity of the
> derived tensor product, and Leray in the unbounded form [Stacks, Tag 0D5W], which holds with no
> hypothesis on `f` and which the bounded-below [Stacks, Tag 01EZ] that the source cites does not
> cover here.
>
> The compatibility with boundary maps is **not** part of this statement; see the module
> docstring for what it asks and why naturality does not give it.

```lean
def extCohomologyIso (h : ExtProjectionInput f E G) (i : ℤ) :
    baseTensorFunctor f E G ⋙ cohomologyOnBase S i ≅
      pullbackTensorFunctor f E G ⋙ cohomologyOnSource f i
```

**`Stacks.Cohomology.ExtProjectionFormulaBoundary.extCohomologyIso_qcoh_boundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ExtProjectionFormulaBoundary.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ExtProjectionFormulaBoundary.lean#L183). The attribute's comment: “the functorial isomorphisms on quasi-coherent F for every i, and their compatibility with the boundary maps of every short exact sequence of quasi-coherent modules; H^i(S, -) = H^i of unbounded RΓ(S, -), H^i(X, -) as a Γ(S, O\_S)-module along f^♯, boundary maps the connecting morphisms of H^0 at the image under RΓ(S, -) of K ⊗^L (triangle of the sequence) and at the image under RΓ(X, E ⊗^L -) of the triangle of 0 → G ⊗ f^*F₁ → G ⊗ f^*F₂ → G ⊗ f^*F₃ → 0; no hypothesis beyond those of Tag 0DJQ”.

> **[Stacks, Tag 0A1F].**  Let `S` be a Noetherian scheme, `f : X ⟶ S` a morphism locally of
> finite type, `E ∈ D(𝒪_X)` perfect and `𝒢` a bounded complex of coherent `𝒪_X`-modules, flat over
> `S`, whose support is contained in a closed subset proper over `S` (the assumptions of
> [Stacks, Tag 0DJQ]), and let `K = Rf_*(E ⊗^𝐋_{𝒪_X} 𝒢)`.  Then there are isomorphisms
>
> `H^i(S, K ⊗^𝐋_{𝒪_S} ℱ) ≅ H^i(X, E ⊗^𝐋_{𝒪_X} (𝒢 ⊗_{𝒪_X} f^*ℱ))`,
>
> functorial in the quasi-coherent `𝒪_S`-module `ℱ` (a natural isomorphism of functors on the full
> subcategory of quasi-coherent modules, for every `i`), and compatible with boundary maps: for a
> short exact sequence `0 → ℱ₁ → ℱ₂ → ℱ₃ → 0` of quasi-coherent `𝒪_S`-modules the square formed
> with the connecting morphisms commutes, where on the left the connecting morphism is that of
> `H^*(S, -)` at the distinguished triangle `K ⊗^𝐋 ℱ₁ → K ⊗^𝐋 ℱ₂ → K ⊗^𝐋 ℱ₃ → (K ⊗^𝐋 ℱ₁)[1]`,
> and on the right that of `H^*(X, E ⊗^𝐋 -)` at the distinguished triangle of the short exact
> sequence of complexes `0 → 𝒢 ⊗ f^*ℱ₁ → 𝒢 ⊗ f^*ℱ₂ → 𝒢 ⊗ f^*ℱ₃ → 0`.
>
> Here `H^i(S, -)` is the `i`-th cohomology of unbounded derived global sections, valued in
> `Γ(S, 𝒪_S)`-modules, `H^i(X, -)` is read as a `Γ(S, 𝒪_S)`-module by restriction along `f^♯`, the
> connecting morphisms are `CategoryTheory.Functor.homologySequenceδ` of the homological functor
> `H^0` at the image triangles, and `𝒢 ⊗ f^*ℱ` is the complex with terms `𝒢^p ⊗ f^*ℱ`
> (`Stacks.Cohomology.ExtProjectionFormula.tensorModuleComplex`); its short exactness is
> `shortExact_Ψ`, proved from flatness of the `𝒢^p` over `S`.
>
> Every step of the source's proof is proved: the projection formula ([Stacks, Tag 08EU]) through a
> quasi-compact open neighbourhood of the support (`f` need not be quasi-compact), associativity,
> Leray ([Stacks, Tag 0D5W]) and the flat identification `𝒢 ⊗^𝐋 Lf^*ℱ ≅ 𝒢 ⊗ f^*ℱ`
> ([Stacks, Tag 08DE] with flatness over `S`); the isomorphisms in degree `i` are obtained from a
> degree-zero comparison evaluated at `ℱ[i]`, which is what makes them compatible with the
> connecting morphisms.

```lean
theorem extCohomologyIso_qcoh_boundary [IsNoetherian S] [LocallyOfFiniteType f]
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E)
    (hG : PerfectPushforward.FlatProperSupportComplex f G) :
    ∃ Φ : ∀ i : ℤ, (qcModules S).ι ⋙ DerivedCategory.singleFunctor (ModS S) 0 ⋙
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor S.toRingedSpace.sheaf).obj
            (Kobj f E G) ⋙
          Stacks.Cohomology.DerivedSectionsLeray.derivedSectionsOverOpen S.toRingedSpace ⊤ ⋙
          DerivedCategory.homologyFunctor _ i ≅
        (qcModules S).ι ⋙ Ψ f G ⋙ DerivedCategory.Q ⋙
          (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor X.toRingedSpace.sheaf).obj
            E ⋙
          Stacks.Cohomology.DerivedSectionsLeray.derivedPreimageSections f.toLRSHom.toShHom ⊤ ⋙
          DerivedCategory.homologyFunctor _ i,
      ∀ (T : ShortComplex (ModS S)) (hT : T.ShortExact) (h₁ : qcModules S T.X₁)
        (h₃ : qcModules S T.X₃) (i : ℤ),
        (Φ i).hom.app ⟨T.X₃, h₃⟩ ≫
          (H0 (S := S)).homologySequenceδ
            ((sourceSections f E).mapTriangle.obj
              (DerivedCategory.triangleOfSES (shortExact_Ψ f G hG T hT))) i (i + 1) rfl =
        (H0 (S := S)).homologySequenceδ
            ((sectionsS (S := S)).mapTriangle.obj
              ((tensorK f E G).mapTriangle.obj hT.singleTriangle)) i (i + 1) rfl ≫
          (Φ (i + 1)).hom.app ⟨T.X₁, h₁⟩
```

## Tag 08ID, a lemma

[Tag 08ID](https://stacks.math.columbia.edu/tag/08ID) in the Stacks Project.

**`Stacks.Cohomology.ExtPerfectProjection.extIso_qcoh_boundary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ExtPerfectProjectionBoundary.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ExtPerfectProjectionBoundary.lean#L206). The attribute's comment: “the functorial isomorphisms for every i, Ext^i read as Hom\_\{D(O\_X)}(E, -[i]), and their compatibility with the boundary maps of every short exact sequence of quasi-coherent modules (with ℱ₂ an arbitrary O\_S-module): the class of a boundary is the Yoneda composite with the connecting morphism of the triangle of 0 → G ⊗ f^*F₁ → G ⊗ f^*F₂ → G ⊗ f^*F₃ → 0; H^i(S, -) is H^i of unbounded RΓ(S, -) with its Γ(S, O\_S)-module structure forgotten”.

> **[Stacks, Tag 08ID].**  Let `S` be a Noetherian scheme, `f : X ⟶ S` locally of finite type,
> `E` a perfect object of `D(𝒪_X)` and `𝒢` a bounded complex of coherent `𝒪_X`-modules, flat over
> `S`, with support proper over `S`, and let `K = Rf_* RSheafHom(E, 𝒢)` as in [Stacks, Tag 0DJR].
> Then there are isomorphisms
>
> `Φᵢ : H^i(S, K ⊗^L_{𝒪_S} ℱ) ⟶ Ext^i_{𝒪_X}(E, 𝒢 ⊗_{𝒪_X} f^*ℱ) = Hom_{D(𝒪_X)}(E, (𝒢 ⊗ f^*ℱ)[i])`,
>
> functorial in the quasi-coherent `𝒪_S`-module `ℱ` (a natural isomorphism of functors on
> quasi-coherent modules for every `i`), compatible with boundary maps: for a short exact sequence
> `0 → ℱ₁ → ℱ₂ → ℱ₃ → 0` of `𝒪_S`-modules with `ℱ₁`, `ℱ₃` quasi-coherent and every class `y` in
> `H^i(S, K ⊗^L ℱ₃)`,
>
> `Φᵢ₊₁(∂ y) = Φᵢ(y) ∘ δ`,
>
> where `∂ : H^i(S, K ⊗^L ℱ₃) ⟶ H^{i+1}(S, K ⊗^L ℱ₁)` is the connecting morphism of the
> distinguished triangle `K ⊗^L ℱ₁ → K ⊗^L ℱ₂ → K ⊗^L ℱ₃ → (K ⊗^L ℱ₁)[1]` (the image under
> `K ⊗^L -` of the triangle of the sequence) and `δ : 𝒢 ⊗ f^*ℱ₃ ⟶ (𝒢 ⊗ f^*ℱ₁)[1]` is the
> connecting morphism of the distinguished triangle of the short exact sequence of complexes
> `0 → 𝒢 ⊗ f^*ℱ₁ → 𝒢 ⊗ f^*ℱ₂ → 𝒢 ⊗ f^*ℱ₃ → 0`, composed as an element of `Ext¹`.
>
> `H^i(S, -)` is the `i`-th cohomology of the unbounded derived global sections; it is a group of
> `Γ(S, 𝒪_S)`-modules, read as an abelian group and lifted to the universe of the morphism groups of
> `D(𝒪_X)`.  `f^*` is the pullback of modules and `𝒢 ⊗ f^*ℱ` the complex with terms
> `𝒢^p ⊗ f^*ℱ`.

```lean
theorem extIso_qcoh_boundary [IsNoetherian S] [LocallyOfFiniteType f]
    (hE : RingedSpace.IsPerfect (X := X.toRingedSpace) E)
    (hG : PerfectPushforward.FlatProperSupportComplex f G) :
    ∃ Φ : ∀ i : ℤ, (qcModules S).ι ⋙ DerivedCategory.singleFunctor (ModS S) 0 ⋙
          tensorSheafHomK f E G ⋙ sectionsS (S := S) ⋙ DerivedCategory.homologyFunctor _ i ⋙
          forgetLift (Y := S.toRingedSpace) ≅
        (qcModules S).ι ⋙ Ψ f G ⋙ DerivedCategory.Q ⋙ shiftFunctor _ i ⋙
          preadditiveCoyoneda.obj (op E),
      ∀ (T : ShortComplex (ModS S)) (hT : T.ShortExact) (h₁ : qcModules S T.X₁)
        (h₃ : qcModules S T.X₃) (i : ℤ)
        (y : ((qcModules S).ι ⋙ DerivedCategory.singleFunctor (ModS S) 0 ⋙
          tensorSheafHomK f E G ⋙ sectionsS (S := S) ⋙ DerivedCategory.homologyFunctor _ i ⋙
          forgetLift (Y := S.toRingedSpace)).obj ⟨T.X₃, h₃⟩),
        (Φ (i + 1)).hom.app ⟨T.X₁, h₁⟩
            ((forgetLift (Y := S.toRingedSpace)).map ((H0 (S := S)).homologySequenceδ
              ((sectionsS (S := S)).mapTriangle.obj
                ((tensorSheafHomK f E G).mapTriangle.obj hT.singleTriangle)) i (i + 1) rfl) y) =
          ((Φ i).hom.app ⟨T.X₃, h₃⟩ y : E ⟶ _) ≫
            (DerivedCategory.triangleOfSESδ
              (Stacks.Cohomology.ExtProjectionFormulaBoundary.shortExact_Ψ f G hG T hT))⟦i⟧' ≫
            (shiftFunctorAdd' _ 1 i (i + 1) (by omega)).inv.app _
```

## Tag 08IF, a lemma

[Tag 08IF](https://stacks.math.columbia.edu/tag/08IF) in the Stacks Project.

**`Stacks.Cohomology.RelativeExt.exists_perfect_relativeExt_comparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeExt/PartA.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeExt/PartA.lean#L51). The attribute's comment: “(A)”.

> Let `S` be a Noetherian scheme, `f : X ⟶ S` a morphism locally of finite type,
> `E ∈ D^-_{Coh}(𝒪_X)` and `𝒢` a bounded complex of coherent `𝒪_X`-modules, flat over `S`, with
> support proper over `S`. For every `m` there are a perfect object `K` of `D(𝒪_S)` and maps
>
> `α^i_ℱ : Ext^i_{𝒪_X}(E, 𝒢 ⊗_{𝒪_X} f^*ℱ) ⟶ H^i(S, K ⊗^L_{𝒪_S} ℱ)`
>
> for quasi-coherent `ℱ` (with `H^i(S, -) = Ext^i_{𝒪_S}(𝒪_S, -)`), which are additive, functorial in
> `ℱ`, compatible with the boundary maps of short exact sequences `0 ⟶ ℱ₁ ⟶ ℱ₂ ⟶ ℱ₃ ⟶ 0` of
> quasi-coherent modules (on the left, the connecting morphism of
> `0 ⟶ 𝒢 ⊗ f^*ℱ₁ ⟶ 𝒢 ⊗ f^*ℱ₂ ⟶ 𝒢 ⊗ f^*ℱ₃ ⟶ 0`, exact because `𝒢` is flat over `S`; on the right,
> that of the distinguished triangle `K ⊗^L ℱ₁ ⟶ K ⊗^L ℱ₂ ⟶ K ⊗^L ℱ₃ ⟶`), and bijective for
> `i ≤ m`.

```lean
theorem exists_perfect_relativeExt_comparison (E : DStd X) (hE : IsBoundedAboveCoherent E)
    (G : CochainComplex (TModules X.toRingedSpace) ℤ)
    (hG : Stacks.Cohomology.PerfectPushforward.FlatProperSupportComplex f G) (m : ℤ) :
    ∃ K : DStd S, IsPerfectObject K ∧
      ∃ α : ∀ (i : ℤ) (F : SheafOfModules.{u} (structureSheafRing S.toRingedSpace)),
          F.IsQuasicoherent → (relativeExtGroup f G E F i →+ baseTensorGroup K F i),
        (∀ (i : ℤ) (F F' : SheafOfModules.{u} (structureSheafRing S.toRingedSpace))
            (hF : F.IsQuasicoherent) (hF' : F'.IsQuasicoherent) (v : F ⟶ F')
            (y : relativeExtGroup f G E F i),
          α i F' hF' (relativeExtMap f G E i v y) = baseTensorMap i K v (α i F hF y)) ∧
        (∀ (A : ShortComplex (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)))
            (hA : A.ShortExact) (h₁ : A.X₁.IsQuasicoherent) (h₃ : A.X₃.IsQuasicoherent)
            (n m' : ℤ) (h : 1 + n = m') (y : relativeExtGroup f G E A.X₃ n),
          α m' A.X₁ h₁ (relativeExtBoundaryMap E
              (isBoundedFlatOver_of_flatProperSupportComplex hG) hA n m' h y) =
            baseTensorBoundaryMap K hA n m' h (α n A.X₃ h₃ y)) ∧
        (∀ (i : ℤ), i ≤ m → ∀ (F : SheafOfModules.{u} (structureSheafRing S.toRingedSpace))
            (hF : F.IsQuasicoherent), Function.Bijective (α i F hF))
```

**`Stacks.Cohomology.RelativeExt.exists_pseudoCoherent_relativeExt_representative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeExt/PartB.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeExt/PartB.lean#L369). The attribute's comment: “(B)”.

> **[Stacks, Tag 08IF] (B).** Let `S` be a Noetherian scheme, `f : X ⟶ S` a morphism locally of
> finite type, `E ∈ D^-_{Coh}(𝒪_X)` and `𝒢` a bounded complex of coherent `𝒪_X`-modules, flat over
> `S`, with support proper over `S`. There is a pseudo-coherent object `L` of `D(𝒪_S)` and
> isomorphisms
>
> `Ext^i_{𝒪_S}(L, ℱ) ≅ Ext^i_{𝒪_X}(E, 𝒢 ⊗_{𝒪_X} f^*ℱ)`
>
> for all `i` and all quasi-coherent `ℱ`, functorial in `ℱ` and compatible with the boundary maps of
> short exact sequences `0 ⟶ ℱ₁ ⟶ ℱ₂ ⟶ ℱ₃ ⟶ 0` of quasi-coherent modules (on the left, composition
> with the connecting morphism `ℱ₃ ⟶ ℱ₁[1]`; on the right, with that of
> `0 ⟶ 𝒢 ⊗ f^*ℱ₁ ⟶ 𝒢 ⊗ f^*ℱ₂ ⟶ 𝒢 ⊗ f^*ℱ₃ ⟶ 0`, exact because `𝒢` is flat over `S`).

```lean
theorem exists_pseudoCoherent_relativeExt_representative (E : DStd X)
    (hE : IsBoundedAboveCoherent E) (G : CochainComplex (TModules X.toRingedSpace) ℤ)
    (hG : Stacks.Cohomology.PerfectPushforward.FlatProperSupportComplex f G) :
    ∃ L : DStd S, IsPseudoCoherentObject L ∧
      ∃ β : ∀ (i : ℤ) (F : SheafOfModules.{u} (structureSheafRing S.toRingedSpace)),
          F.IsQuasicoherent → (baseExtGroup L F i ≃+ relativeExtGroup f G E F i),
        (∀ (i : ℤ) (F F' : SheafOfModules.{u} (structureSheafRing S.toRingedSpace))
            (hF : F.IsQuasicoherent) (hF' : F'.IsQuasicoherent) (v : F ⟶ F')
            (z : baseExtGroup L F i),
          β i F' hF' (baseExtMap L i v z) = relativeExtMap f G E i v (β i F hF z)) ∧
        (∀ (A : ShortComplex (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)))
            (hA : A.ShortExact) (h₁ : A.X₁.IsQuasicoherent) (h₃ : A.X₃.IsQuasicoherent)
            (n m : ℤ) (h : 1 + n = m) (z : baseExtGroup L A.X₃ n),
          β m A.X₁ h₁ (baseExtBoundaryMap L hA n m h z) =
            relativeExtBoundaryMap E (isBoundedFlatOver_of_flatProperSupportComplex hG) hA n m
              h (β n A.X₃ h₃ z))
```

## Tag 0DJS, a remark

[Tag 0DJS](https://stacks.math.columbia.edu/tag/0DJS) in the Stacks Project.

**`Stacks.Cohomology.RelativeExtCanonical.exists_baseChange_relativeExt_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCanonical/BaseChangeExt.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCanonical/BaseChangeExt.lean#L102). The attribute's comment: “base change”.

> **[Stacks, Tag 0DJS]: formation of the complex `L` of [Stacks, Tag 08IF] (B) is compatible
> with base change.** Let `S` be Noetherian, `f : X ⟶ S` locally of finite type,
> `E ∈ D^-_{Coh}(𝒪_X)` and `𝒢` a bounded complex of coherent `𝒪_X`-modules, flat over `S`, with
> support proper over `S`, and let `L` be the pseudo-coherent complex of (B). For every cartesian
> square of schemes with `g' : X' ⟶ X`, `f' : X' ⟶ S'`, `g : S' ⟶ S` there are isomorphisms
>
> `Ext^i_{𝒪_{S'}}(Lg^*L, ℱ') ≅ Ext^i_{𝒪_{X'}}(L(g')^*E, (g')^*𝒢 ⊗_{𝒪_{X'}} (f')^*ℱ')`
>
> for quasi-coherent `ℱ'` on `S'`, with `(g')^*𝒢` the ordinary termwise pullback of `𝒢`, which are
> functorial in `ℱ'` and compatible with the boundary maps of short exact sequences. They are
> canonical: they are the ones induced by an identification
> `Hom(Lg^*L, N) ≃ Hom(L(g')^*E, L(f')^*N ⊗^L (g')^*𝒢)` natural in `N ∈ D^+_{QCoh}(𝒪_{S'})`.

```lean
theorem exists_baseChange_relativeExt_iso :
    ∃ β : ∀ (i : ℤ) (F' : SheafOfModules.{u} (structureSheafRing S'.toRingedSpace)),
        F'.IsQuasicoherent →
        (baseExtGroup (baseChangedRepresentative f E hE G hG g) F' i ≃+
          relativeExtGroup f'
            ((Stacks.Cohomology.DerivedPullbackTensor.pullbackComplex g'.toLRSHom.toShHom).obj G)
            (baseChangedSource E g') F' i),
      (∀ (i : ℤ) (F F' : SheafOfModules.{u} (structureSheafRing S'.toRingedSpace))
          (hF : F.IsQuasicoherent) (hF' : F'.IsQuasicoherent) (v : F ⟶ F')
          (z : baseExtGroup (baseChangedRepresentative f E hE G hG g) F i),
        β i F' hF' (baseExtMap _ i v z) =
          relativeExtMap f'
            ((Stacks.Cohomology.DerivedPullbackTensor.pullbackComplex g'.toLRSHom.toShHom).obj G)
            (baseChangedSource E g') i v (β i F hF z)) ∧
      (∀ (A : ShortComplex (SheafOfModules.{u} (structureSheafRing S'.toRingedSpace)))
          (hA : A.ShortExact) (h₁ : A.X₁.IsQuasicoherent) (h₃ : A.X₃.IsQuasicoherent)
          (n m : ℤ) (h : 1 + n = m)
          (z : baseExtGroup (baseChangedRepresentative f E hE G hG g) A.X₃ n),
        β m A.X₁ h₁ (baseExtBoundaryMap _ hA n m h z) =
          relativeExtBoundaryMap (baseChangedSource E g')
            (isBoundedFlatOver_total_pullback hsq hG) hA n m h (β n A.X₃ h₃ z)) ∧
      ∃ θ : ShiftedHom.NaturalHomEquiv (𝟭 (DStd S'))
          (pullbackTensorDerivedFunctor (isBoundedFlatOver_total_pullback hsq hG))
          (baseChangedRepresentative f E hE G hG g)
          (baseChangedSource E g') (plusQCohDerived S'),
        ∀ (i : ℤ) (F' : SheafOfModules.{u} (structureSheafRing S'.toRingedSpace))
          (hF' : F'.IsQuasicoherent),
          β i F' hF' = extIsoOfIdentification (isBoundedFlatOver_total_pullback hsq hG)
            (θ.toIdentification (plusQCohDerived_biprod S')) i F' hF'
```

**`Stacks.Cohomology.RelativeExtCanonical.exists_iso_pseudoCoherentRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCanonical/Canonicity.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/RelativeExtCanonical/Canonicity.lean#L63). The attribute's comment: “canonical”.

> **The pseudo-coherent complex `L` representing relative `Ext` is canonical.**
> Let `S` be Noetherian, `f : X ⟶ S` locally of finite type, `E ∈ D^-_{Coh}(𝒪_X)` and `𝒢` a bounded
> complex of coherent `𝒪_X`-modules, flat over `S`, with support proper over `S`; let `L` be the
> pseudo-coherent complex `pseudoCoherentRepresentative f E hE G hG`, with its identification
> `θ_N : Hom(L, N) ≃ Hom(E, Lf^*N ⊗^L 𝒢)`, natural in `N ∈ D^+_{QCoh}(𝒪_S)`, and the
> isomorphisms `Ext^i_{𝒪_S}(L, ℱ) ≅ Ext^i_{𝒪_X}(E, 𝒢 ⊗ f^*ℱ)` it induces. Then these are
> functorial in quasi-coherent `ℱ` and compatible with boundary maps, and for every `L'` with
> quasi-coherent cohomology and every identification
> `θ'_N : Hom(L', N) ≃ Hom(E, Lf^*N ⊗^L 𝒢)` natural in `N ∈ D^+_{QCoh}(𝒪_S)` there is an
> isomorphism `φ : L' ≅ L` with `θ'(φ ∘ x) = θ(x)` for all such `N` and `x : L ⟶ N`; in particular
> `φ` carries the `Ext`-isomorphisms induced by `θ'` to those of `L`.

```lean
theorem exists_iso_pseudoCoherentRepresentative (E : DStd X) (hE : IsBoundedAboveCoherent E)
    (G : CochainComplex (TModules X.toRingedSpace) ℤ)
    (hG : Stacks.Cohomology.PerfectPushforward.FlatProperSupportComplex f G) :
    IsPseudoCoherentObject (pseudoCoherentRepresentative f E hE G hG) ∧
    (∀ (i : ℤ) (F F' : SheafOfModules.{u} (structureSheafRing S.toRingedSpace))
        (hF : F.IsQuasicoherent) (hF' : F'.IsQuasicoherent) (v : F ⟶ F')
        (z : baseExtGroup (pseudoCoherentRepresentative f E hE G hG) F i),
      extIsoOfIdentification (isBoundedFlatOver_of_flatProperSupportComplex hG)
          ((pseudoCoherentRepresentativeHomEquiv f E hE G hG).toIdentification
            (plusQCohDerived_biprod S)) i F' hF'
          (baseExtMap (pseudoCoherentRepresentative f E hE G hG) i v z) =
        relativeExtMap f G E i v
          (extIsoOfIdentification (isBoundedFlatOver_of_flatProperSupportComplex hG)
            ((pseudoCoherentRepresentativeHomEquiv f E hE G hG).toIdentification
              (plusQCohDerived_biprod S)) i F hF z)) ∧
    (∀ (A : ShortComplex (SheafOfModules.{u} (structureSheafRing S.toRingedSpace)))
        (hA : A.ShortExact) (h₁ : A.X₁.IsQuasicoherent) (h₃ : A.X₃.IsQuasicoherent)
        (n m : ℤ) (h : 1 + n = m)
        (z : baseExtGroup (pseudoCoherentRepresentative f E hE G hG) A.X₃ n),
      extIsoOfIdentification (isBoundedFlatOver_of_flatProperSupportComplex hG)
          ((pseudoCoherentRepresentativeHomEquiv f E hE G hG).toIdentification
            (plusQCohDerived_biprod S)) m A.X₁ h₁
          (baseExtBoundaryMap (pseudoCoherentRepresentative f E hE G hG) hA n m h z) =
        relativeExtBoundaryMap E (isBoundedFlatOver_of_flatProperSupportComplex hG) hA n m h
          (extIsoOfIdentification (isBoundedFlatOver_of_flatProperSupportComplex hG)
            ((pseudoCoherentRepresentativeHomEquiv f E hE G hG).toIdentification
              (plusQCohDerived_biprod S)) n A.X₃ h₃ z)) ∧
    ∀ (L' : DStd S) (_ : qcohDerived S L')
      (θ' : ShiftedHom.NaturalHomEquiv (𝟭 (DStd S))
        (pullbackTensorDerivedFunctor (isBoundedFlatOver_of_flatProperSupportComplex hG)) L' E
        (plusQCohDerived S)),
      ∃ φ : L' ≅ pseudoCoherentRepresentative f E hE G hG,
        (∀ (N : DStd S) (hN : plusQCohDerived S N)
            (x : pseudoCoherentRepresentative f E hE G hG ⟶ N),
          θ'.equiv N hN (φ.hom ≫ x) =
            (pseudoCoherentRepresentativeHomEquiv f E hE G hG).equiv N hN x) ∧
        ∀ (i : ℤ) (F : SheafOfModules.{u} (structureSheafRing S.toRingedSpace))
          (hF : F.IsQuasicoherent)
          (z : baseExtGroup (pseudoCoherentRepresentative f E hE G hG) F i),
          extIsoOfIdentification (isBoundedFlatOver_of_flatProperSupportComplex hG)
              (θ'.toIdentification (plusQCohDerived_biprod S)) i F hF (φ.hom ≫ z) =
            extIsoOfIdentification (isBoundedFlatOver_of_flatProperSupportComplex hG)
              ((pseudoCoherentRepresentativeHomEquiv f E hE G hG).toIdentification
                (plusQCohDerived_biprod S)) i F hF z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.28, Tag 08IC](https://stacks.math.columbia.edu/tag/08IC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
