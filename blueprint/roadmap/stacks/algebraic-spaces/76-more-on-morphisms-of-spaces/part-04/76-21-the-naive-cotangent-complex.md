---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.naiveCotangentComplex, AlgebraicGeometry.Space.naiveCotangentEtaleLocalisationIso, AlgebraicGeometry.Space.naiveCotangentEtaleLocalisationIso_hom, AlgebraicGeometry.Space.naiveCotangentEtaleRestrictionIso, AlgebraicGeometry.Space.naiveCotangentEtaleRestrictionDerivedIso, AlgebraicGeometry.Space.representedNaiveCotangentComparison, AlgebraicGeometry.Space.representedPulledBackNaiveCotangentComparison, AlgebraicGeometry.Space.quasiIso_representableEpsilonNaiveCotangentIdentification
statement: formalized
proof: formalized
---

# 76.21 The naive cotangent complex

Section 76.21 of the Stacks Project, [Tag 0D0U](https://stacks.math.columbia.edu/tag/0D0U). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D0V, a definition

[Tag 0D0V](https://stacks.math.columbia.edu/tag/0D0V) in the Stacks Project.

**`AlgebraicGeometry.Space.naiveCotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentComplex.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentComplex.lean#L58).

> **Stacks 0D0V.** The naive cotangent complex `NL_{X/Y} = NL_f` of a morphism `f : X ⟶ Y` of
> algebraic spaces: the naive cotangent complex of the inverse-image form `f⁻¹𝒪_Y ⟶ 𝒪_X` of the
> structure map of the morphism of small étale ringed topoi of `f`.

```lean
noncomputable def naiveCotangentComplex (f : X ⟶ Y) :
    CochainComplex (_root_.SheafOfModules.{u + 1, u, u + 1, u}
      (Stacks.SheafOfModules.Tensor.ringSheaf.{u + 1, u, u}
        (smallEtaleRingedTopos B S hS X).O)) ℤ
```

## Tag 0D0W, a lemma

[Tag 0D0W](https://stacks.math.columbia.edu/tag/0D0W) in the Stacks Project.

**`AlgebraicGeometry.Space.naiveCotangentEtaleLocalisationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleLocalisation.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleLocalisation.lean#L183). The attribute's comment: “the canonical identification NL\_\{X/Y}|\_\{U\_étale} = NL\_\{U/V} for a commutative square of algebraic spaces with p and q étale, REDUCED TO THE SECOND HALF OF THE SOURCE'S PROOF. What is proved is `NL_{p⁻¹O_X / p⁻¹f⁻¹O_Y} ≅ NL_{U/V}`: the two identifications of Tag 03LV, `p⁻¹O_X = O_U` and `q⁻¹O_Y = O_V`, together with the composition law of Tag 03G8 for the square, make the data defining the two complexes correspond, and the canonical chain map of Tag 08TX between them is then an isomorphism. The FIRST half, `p⁻¹NL_{X/Y} = NL_{p⁻¹O_X / p⁻¹f⁻¹O_Y}` (Modules on Sites, Lemma 08TZ), is not instantiated here, so the source of this isomorphism is not yet known to be the restriction `NL_{X/Y}|_{U_étale}`. Tag 08TZ itself IS carried for sites, as `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`, for an arbitrary morphism of topoi; what is missing is only its universe shape, which ties the ambient section universe of each topos to a universe containing its site's object universe, whereas the small étale site has objects in `Type (u + 1)` and structure sheaves in `CommRingCat.{u}`. Carried beyond the source's statement: the étale hypotheses are hypotheses `IsEtale p.hom` and `IsEtale q.hom` in the big-fppf-site presentation of algebraic spaces; the identification is an isomorphism of cochain complexes of sheaves of `p⁻¹O_X`-modules, the target being `NL_{U/V}` read there by restriction of scalars along `p⁻¹O_X ≅ O_U`, and NOTHING is asserted in the derived category `D(O_U)`”.

> **Stacks 0D0W, the identification of the two naive cotangent complexes.**  For a commuting
> square `p ≫ f = g ≫ q` of algebraic spaces over `S` with `p` and `q` étale,
>
> `NL_{p⁻¹𝒪_X / p⁻¹f⁻¹𝒪_Y} ≅ NL_{U/V}`,
>
> the target read in complexes of sheaves of `p⁻¹𝒪_X`-modules through the identification
> `p⁻¹𝒪_X ≅ 𝒪_U` of Stacks 03LV.
>
> Both horizontal morphisms of the square of sheaves of rings
> ```
> p⁻¹𝒪_X ──────▸ 𝒪_U
>    ▲             ▲
>    │             │
> p⁻¹f⁻¹𝒪_Y ────▸ g⁻¹𝒪_V
> ```
> are isomorphisms — the top one by Stacks 03LV at the étale morphism `p`, the bottom one by
> `AlgebraicGeometry.Space.etaleSquareBaseRingIso` — so the canonical chain map of Stacks 08TX
> attached to it is an isomorphism.

```lean
noncomputable def naiveCotangentEtaleLocalisationIso {p : U ⟶ X} {f : X ⟶ Y} {g : U ⟶ V}
    {q : V ⟶ Y} (h : p ≫ f = g ≫ q) (hp : IsEtale B S hS p.hom) (hq : IsEtale B S hS q.hom) :
    inverseImageNaiveCotangentComplex B S hS p f ≅
      ((_root_.SheafOfModules.restrictScalars.{u + 1}
          (underlyingRingHomOfSite.{u, u + 1, u}
            (etaleInverseImageStructureSheafIso B S hS p hp).hom)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj (naiveCotangentComplex B S hS g)
```

**`AlgebraicGeometry.Space.naiveCotangentEtaleLocalisationIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleLocalisation.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleLocalisation.lean#L200). The attribute's comment: “the identification is the canonical chain map of Tag 08TX, not an arbitrary isomorphism; same scope as `naiveCotangentEtaleLocalisationIso`”.

> The forward map of `AlgebraicGeometry.Space.naiveCotangentEtaleLocalisationIso` is the
> canonical chain map of Stacks 08TX attached to the square of sheaves of rings, so the
> identification is canonical.

```lean
theorem naiveCotangentEtaleLocalisationIso_hom {p : U ⟶ X} {f : X ⟶ Y} {g : U ⟶ V}
    {q : V ⟶ Y} (h : p ≫ f = g ≫ q) (hp : IsEtale B S hS p.hom)
    (hq : IsEtale B S hS q.hom) :
    (naiveCotangentEtaleLocalisationIso B S hS h hp hq).hom =
      Stacks.SheafOfModules.naiveCotangentComplexMapOfSquare.{u, u + 1, u, u}
        (smallEtaleRingedTopos B S hS U).J _ _ _ _ _ _
        (etaleSquareBaseRingIso B S hS h hq).hom
        (etaleInverseImageStructureSheafIso B S hS p hp).hom
        (etaleSquareBaseRingIso_fSharpInverseImage B S hS h hq)
```

**`AlgebraicGeometry.Space.naiveCotangentEtaleRestrictionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleRestriction.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleRestriction.lean#L184). The attribute's comment: “the canonical identification NL\_\{X/Y}|\_\{U\_étale} = NL\_\{U/V}, as an isomorphism of complexes of sheaves of O\_U-modules, of which the identification in D(O\_U) is the image. The restriction is along the postcomposition functor U\_étale ⥤ X\_étale, i.e. p\_small⁻¹ (Tag 03LQ), with O\_X|\_\{U\_étale} = O\_U (Tag 03LV); formation of the naive cotangent complex commutes with it (Tag 08TZ for that functor), and the square of structure maps is identified through Tags 03LV and 03G8”.

> **Stacks 0D0W, as an isomorphism of complexes.** For a commutative square `p ≫ f = g ≫ q` of
> algebraic spaces over `S` with `p` and `q` étale, the restriction to the small étale site of
> `U` of the naive cotangent complex of `f` is the naive cotangent complex of `g`:
>
> `NL_{X/Y}|_{U_étale} ≅ NL_{U/V}`,
>
> as complexes of sheaves of `𝒪_U`-modules. It is the restriction of scalars along
> `𝒪_U ≅ 𝒪_X|_{U_étale}` of `Stacks.SheafOfModules.restrictionNaiveCotangentComplexIso`, which
> identifies `NL_{X/Y}|_{U_étale}` with the naive cotangent complex of
> `(f⁻¹𝒪_Y)|_{U_étale} ⟶ 𝒪_X|_{U_étale}`, followed by the inverse of the canonical chain map of
> Stacks 08TX attached to the square of sheaves of rings of
> `AlgebraicGeometry.Space.etaleRestrictionNaiveBaseRingIso_fSharp`.

```lean
noncomputable def naiveCotangentEtaleRestrictionIso {p : U ⟶ X} {f : X ⟶ Y} {g : U ⟶ V}
    {q : V ⟶ Y} (h : p ≫ f = g ≫ q) (hp : IsEtale B S hS p.hom) (hq : IsEtale B S hS q.hom) :
    ((etaleModuleRestriction B S hS p hp).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (naiveCotangentComplex B S hS f) ≅
      naiveCotangentComplex B S hS g
```

**`AlgebraicGeometry.Space.naiveCotangentEtaleRestrictionDerivedIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleRestriction.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleRestriction.lean#L228). The attribute's comment: “the canonical identification NL\_\{X/Y}|\_\{U\_étale} = NL\_\{U/V} in D(O\_U) for a commutative square of algebraic spaces over S with p and q étale”.

> **Stacks 0D0W.** For a commutative square `p ≫ f = g ≫ q` of algebraic spaces over `S` with
> `p` and `q` étale, there is a canonical identification
>
> `NL_{X/Y}|_{U_étale} = NL_{U/V}` in `D(𝒪_U)`:
>
> the image in the derived category of sheaves of `𝒪_U`-modules of the isomorphism of complexes
> `AlgebraicGeometry.Space.naiveCotangentEtaleRestrictionIso`.

```lean
noncomputable def naiveCotangentEtaleRestrictionDerivedIso {p : U ⟶ X} {f : X ⟶ Y} {g : U ⟶ V}
    {q : V ⟶ Y} (h : p ≫ f = g ≫ q) (hp : IsEtale B S hS p.hom) (hq : IsEtale B S hS q.hom)
    [HasDerivedCategory.{t} (_root_.SheafOfModules.{u + 1}
      (Stacks.SheafOfModules.Tensor.ringSheaf.{u + 1, u, u} (smallEtaleRingedTopos B S hS U).O))] :
    DerivedCategory.Q.obj
        (((etaleModuleRestriction B S hS p hp).mapHomologicalComplex (ComplexShape.up ℤ)).obj
          (naiveCotangentComplex B S hS f)) ≅
      DerivedCategory.Q.obj (naiveCotangentComplex B S hS g)
```

## Tag 0D0X, a lemma

[Tag 0D0X](https://stacks.math.columbia.edu/tag/0D0X) in the Stacks Project.

**`AlgebraicGeometry.Space.representedNaiveCotangentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentRepresentableComparison.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentRepresentableComparison.lean#L245). The attribute's comment: “the canonical map `ε^*NL_{X₀/Y₀} ⟶ NL_{X/Y}` of the source's proof, in its `ε⁻¹`-adjoint form, for the morphism of algebraic spaces represented by a morphism `T₁ ⟶ T₂` of the big fppf site over `S` (so `X`, `Y` are represented by the schemes `X₀`, `Y₀` underlying `T₁`, `T₂`); `ε` is the comparison of Section 071P (`representedToZariskiRingedToposHom`). WHAT IS PROVED IS THE SECOND STEP OF THE SOURCE'S PROOF: the canonical chain map of Tag 08TX attached to the square of Remark 08GH, `representedBaseMap_square`, from the naive cotangent complex of the inverse image along `ε` of the structure map of `f₀`. Its source is identified with `ε⁻¹NL_{X₀/Y₀}`, which is the source's FIRST step (Modules on Sites, Lemma 08TZ), separately by `representedInverseImageNaiveCotangentComplexIso`; the composite of the two is `representedPulledBackNaiveCotangentComparison`. THE SOURCE'S THIRD STEP IS NOT PROVED: the map is NOT shown to be an ISOMORPHISM; nothing is asserted in the derived category `D(O_X)`. The source checks that on stalks at geometric points, where the stalk maps of `ε` and of `representedBaseMap` are strict henselizations (Tags 04K5, 04KF, 05V1) and the conclusion is More on Algebra, Lemma 0D08; `NL` has no fundamental triangle, so the two-vanishing-vertices factorisation that `quasiIso_representedCotangentComparison` uses for Tag 08VF is unavailable. Carried beyond the source's statement: sections are lifted to `CommRingCat.{u + 1}` throughout, which is the only universe at which `ε` exists, so both ends are the naive cotangent complexes of the lifted structure maps and NOT `Space.naiveCotangentComplex` of Tag 0D0V, whose sections are in `CommRingCat.{u}`; an `NL` analogue of `Scheme.Hom.cotangentComplexULiftIso` is the one remaining input needed to read this at Tag 0D0V. The target is read in complexes of `ε⁻¹O_{X₀}`-modules through restriction of scalars along `ε♯`, the adjoint form of a map out of `ε^*NL_{X₀/Y₀}`”.

> **The canonical chain map `NL_{ε⁻¹𝒪_{X₀}/ε⁻¹f₀⁻¹𝒪_{Y₀}} ⟶ NL_{X/Y}` of the proof of
> Stacks 0D0X.**  It is the map of Stacks 08TX attached to the square of sheaves of commutative
> rings on the small étale site of `X`
> ```
> ε⁻¹𝒪_{X₀} ─────ε♯────▸ 𝒪_X
>     ▲                    ▲
>     │                    │
> ε⁻¹f₀⁻¹𝒪_{Y₀} ─────────▸ f_small⁻¹𝒪_Y
> ```
> whose bottom arrow is `AlgebraicGeometry.Space.representedBaseMap` and whose commutativity is
> the square of Remark 08GH, `AlgebraicGeometry.Space.representedBaseMap_square`.  The target is
> read in complexes of sheaves of `ε⁻¹𝒪_{X₀}`-modules through restriction of scalars along `ε♯`;
> this is the adjoint form of a map out of `ε^*NL_{X₀/Y₀} = ε⁻¹NL_{X₀/Y₀} ⊗_{ε⁻¹𝒪_{X₀}} 𝒪_X`.

```lean
noncomputable def representedNaiveCotangentComparison :
    representedInverseImageNaiveCotangentComplex B S hS h ⟶
      ((_root_.SheafOfModules.restrictScalars.{u + 1}
            (underlyingRingHomOfSite.{u, u + 1, u + 1}
              (representedToZariskiRingedToposHom B S hS T₁).fSharpInverseImage)
          ).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (representedNaiveCotangentComplexULift B S hS h)
```

**`AlgebraicGeometry.Space.representedPulledBackNaiveCotangentComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentRepresentableComparison.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentRepresentableComparison.lean#L316). The attribute's comment: “the canonical map `ε^*NL_{X₀/Y₀} ⟶ NL_{X/Y}` of the source's proof, in its `ε⁻¹`-adjoint form, for the morphism of algebraic spaces represented by a morphism `T₁ ⟶ T₂` of the big fppf site over `S` (so `X`, `Y` are represented by the schemes `X₀`, `Y₀` underlying `T₁`, `T₂`); `ε` is the comparison of Section 071P (`representedToZariskiRingedToposHom`). THE FIRST TWO STEPS OF THE SOURCE'S PROOF ARE WHAT IS PROVED: the identification `ε⁻¹NL_{X₀/Y₀} = NL_{ε⁻¹O_{X₀}/ε⁻¹f₀⁻¹O_{Y₀}}` of Modules on Sites, Lemma 08TZ, instantiated at `ε` (`representedInverseImageNaiveCotangentComplexIso`), and then the canonical chain map of Tag 08TX attached to the square of Remark 08GH, `representedBaseMap_square` (`representedNaiveCotangentComparison`). THE THIRD STEP IS NOT PROVED: this map is NOT shown to be an ISOMORPHISM, and nothing is asserted in the derived category `D(O_X)`. The source checks that on stalks at geometric points, where the stalk maps of `ε` and of `representedBaseMap` are strict henselizations (Tags 04K5, 04KF, 05V1) and the conclusion is More on Algebra, Lemma 0D08; `NL` has no fundamental triangle, so the two-vanishing-vertices factorisation that `quasiIso_representedCotangentComparison` uses for Tag 08VF is unavailable. Carried beyond the source's statement: sections are lifted to `CommRingCat.{u + 1}` throughout, which is the only universe at which `ε` exists, so the two ends are the naive cotangent complexes of the lifted structure maps and NOT `Space.naiveCotangentComplex` of Tag 0D0V, whose sections are in `CommRingCat.{u}`, nor the scheme-level complex of Definition 0D0H at its own section universe; an `NL` analogue of `Scheme.Hom.cotangentComplexULiftIso` is the one remaining input needed to read this at Tag 0D0V. The target is read in complexes of `ε⁻¹O_{X₀}`-modules through restriction of scalars along `ε♯`, the adjoint form of a map out of `ε^*NL_{X₀/Y₀}`”.

> **The canonical map `ε⁻¹NL_{X₀/Y₀} ⟶ NL_{X/Y}` of the proof of Stacks 0D0X.**  The
> identification of Lemma 08TZ at `ε`
> (`AlgebraicGeometry.Space.representedInverseImageNaiveCotangentComplexIso`) followed by the
> canonical chain map of Stacks 08TX over the square of Remark 08GH
> (`AlgebraicGeometry.Space.representedNaiveCotangentComparison`).  Read through restriction of
> scalars along `ε♯`, this is the adjoint form of the map `ε^*NL_{X₀/Y₀} ⟶ NL_{X/Y}` that
> Stacks 0D0X asserts to be an isomorphism.

```lean
noncomputable def representedPulledBackNaiveCotangentComparison :
    ((inverseImageTargetModules.{u + 1, u, u, u, u, u + 1}
          (SmallEtale.topology B S hS (yoneda.obj T₁))
          (Opens.grothendieckTopology ((BigFppfOver.toScheme B S hS).obj T₁))
          (representedToZariskiMorphismOfTopoi B S hS T₁)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj (representedZariskiNaiveCotangentComplex B S hS h) ⟶
      ((_root_.SheafOfModules.restrictScalars.{u + 1}
            (underlyingRingHomOfSite.{u, u + 1, u + 1}
              (representedToZariskiRingedToposHom B S hS T₁).fSharpInverseImage)
          ).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (representedNaiveCotangentComplexULift B S hS h)
```

**`AlgebraicGeometry.Space.quasiIso_representableEpsilonNaiveCotangentIdentification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableNaiveCotangentIdentification.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableNaiveCotangentIdentification.lean#L262). The attribute's comment: “the canonical map `ε^*NL_{X₀/Y₀} ⟶ NL_{X/Y}` is a quasi-isomorphism, i.e. the canonical identification `NL_{X/Y} = ε^*NL_{X₀/Y₀}` in `D(O_X)`, for an arbitrary morphism `f : X ⟶ Y` of algebraic spaces with `X ≅ h_U`, `Y ≅ h_V` representable by schemes, `NL_{X/Y}` read on the small étale site of `X₀` through the identification `(X₀)_étale ≌ X_étale` that the representing isomorphism gives”.

> **Stacks 0D0X.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` with `X` and `Y`
> representable by schemes `X₀` and `Y₀`, through `α : h_U ≅ X` and `β : h_V ≅ Y` for objects `U`,
> `V` of the big fppf site of `S` with underlying schemes `X₀`, `Y₀`, and let `f₀ : X₀ ⟶ Y₀` be the
> morphism of schemes corresponding to `f` (`AlgebraicGeometry.Space.representingMorphism`).  Let
> `ε : ((X₀)_étale, 𝒪) ⟶ ((X₀)_Zar, 𝒪_{X₀})` be the comparison morphism of Stacks 08H7.  Then the
> canonical map
>
> `ε^*NL_{X₀/Y₀} ⟶ NL_{X/Y}`
>
> — the termwise pullback along `ε` of (the universe lift of) `NL_{X₀/Y₀}` of Stacks 0D0H,
> followed by the map of Stacks 08TX of the square of Stacks 08GH into `NL_{h_U/h_V}`, followed by
> the identification of `NL_{h_U/h_V}` with `NL_{X/Y}` of Stacks 0D0V read on `(X₀)_étale` through
> the identification `(X₀)_étale ≌ X_étale` given by `α`
> (`AlgebraicGeometry.Space.representingNaiveCotangentComplexIso`) — is a quasi-isomorphism, so
> it identifies `NL_{X/Y}` with `ε^*NL_{X₀/Y₀}` in `D(𝒪_X)`.

```lean
theorem quasiIso_representableEpsilonNaiveCotangentIdentification (f : X ⟶ Y) :
    QuasiIso ((((representedEpsilonModulePullback B S hS U).mapHomologicalComplex
        (ComplexShape.up ℤ)).map (representedZariskiNaiveCotangentComplexIso B S hS
          (representingMorphism B S hS α β f)).inv ≫
      representedEpsilonNaiveCotangentMap B S hS (representingMorphism B S hS α β f)) ≫
        (representingNaiveCotangentComplexIso B S hS α β
          (comp_eq_representedSpaceMap_representingMorphism B S hS α β f)).hom)
```

## Tag 0D0Y, a lemma

[Tag 0D0Y](https://stacks.math.columbia.edu/tag/0D0Y) in the Stacks Project.

**`AlgebraicGeometry.Space.naiveCotangentComplex_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentHomologyQuasicoherent.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentHomologyQuasicoherent.lean#L113).

> **Stacks 0D0Y.**  Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S`.  The cohomology sheaves of the naive cotangent complex `NL_{X/Y}` are quasi-coherent,
> zero outside degrees `-1` and `0`, and equal to `Ω_{X/Y}` in degree `0`.
>
> `Ω_{X/Y}` is the sheaf of differentials of Stacks 04CT, with its sections lifted to the universe
> of the sections of `NL_{X/Y}`; see the implementation notes.

```lean
theorem naiveCotangentComplex_homology :
    (∀ i : ℤ, ((naiveCotangentComplex B S hS f).homology i).IsQuasicoherentOnSite) ∧
      (∀ i : ℤ, i ≠ -1 → i ≠ 0 → IsZero ((naiveCotangentComplex B S hS f).homology i)) ∧
      Nonempty ((naiveCotangentComplex B S hS f).homology 0 ≅
        SheafOfModules.uliftForPresentation.{u + 1, u, u, u, u + 1}
          (sheafOfDifferentials B S hS f))
```

## Tag 0D0Z, a lemma

[Tag 0D0Z](https://stacks.math.columbia.edu/tag/0D0Z) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_quasiIso_naiveCotangentComplex_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleLocalFinitePresentation.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentEtaleLocalFinitePresentation.lean#L311). The attribute's comment: “the whole statement. `etale locally on X` is read on the small etale site of `X`: every etale chart `U` of `X` has an etale covering `{W_i -> U}` (a covering sieve of `SmallEtale.topology`) such that `NL_{X/Y}` restricted to the slice at each `W_i` receives a quasi-isomorphism from a complex `F` concentrated in degrees -1 and 0 with `F^0` quasi-coherent and of finite presentation and `F^{-1}` quasi-coherent and of finite type -- the two degrees carrying DIFFERENT finiteness conditions, exactly as the tag states. The source's `NL_{X/Y} is quasi-isomorphic to F` is realized by a quasi-isomorphism FROM `F`, which is the same content. The only hypothesis is the source's: `f` locally of finite presentation (`IsLocallyOfFinitePresentation`, Stacks 03XP). Nothing is assumed: the covering is by the affine chart diagrams, on which `F = NL(P) (x)_A O` for a finite presentation `P` of the chart ring `A` over `R`, the comparison with `(NL_{A/R}) (x)_A O` is the Stacks 00S1 homotopy equivalence, and `(NL_{A/R}) (x)_A O -> NL_{X/Y}|_V` is proved to be a quasi-isomorphism on kernels (H^\{-1} = H\_1(L\_\{A/R}) (x)\_A O, using flatness of the etale stalks) and on cokernels (Omega\_\{X/Y}|\_V = Omega\_\{A/R} (x)\_A O, Stacks 0D08 in degree 0 and Stacks 08TP)”.

> **Stacks 0D0Z.**  Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` which is locally of finite presentation.  Then `NL_{X/Y}` is étale locally on `X`
> quasi-isomorphic to a complex `… → 0 → 𝓕⁻¹ → 𝓕⁰ → 0 → …` of quasi-coherent `𝒪_X`-modules with
> `𝓕⁰` of finite presentation and `𝓕⁻¹` of finite type.
>
> "Étale locally on `X`" is read as on the small étale site of `X`: every étale scheme chart `U` of
> `X` has an étale covering `{Wᵢ ⟶ U}` such that the restriction of `NL_{X/Y}` to the small étale
> site of `X` localized at each `Wᵢ` receives a quasi-isomorphism `φ` from a complex `F` of sheaves
> of modules over the restricted structure sheaf which vanishes outside degrees `-1` and `0`, whose
> degree `0` term is quasi-coherent and of finite presentation and whose degree `-1` term is
> quasi-coherent and of finite type.  `NL_{X/Y}` is `AlgebraicGeometry.Space.naiveCotangentComplex`
> (Stacks 0D0V) and the restriction is `SheafOfModules.overFunctor` applied termwise.

```lean
theorem exists_quasiIso_naiveCotangentComplex_of_isLocallyOfFinitePresentation
    (hf : IsLocallyOfFinitePresentation B S hS f.hom) (U : SmallEtale B S hS X.1) :
    ∃ (I : Type (u + 1)) (W : I → SmallEtale B S hS X.1) (g : ∀ i, W i ⟶ U),
      Sieve.ofArrows W g ∈ SmallEtale.topology B S hS X.1 U ∧
      ∀ i, ∃ (F : CochainComplex (_root_.SheafOfModules.{u + 1}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedTopos B S hS X).O).over
            (W i))) ℤ)
        (φ : F ⟶ ((_root_.SheafOfModules.overFunctor.{u + 1}
            (Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedTopos B S hS X).O)
              (W i)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
          (naiveCotangentComplex B S hS f)),
        (∀ j : ℤ, j ≠ -1 → j ≠ 0 → IsZero (F.X j)) ∧ QuasiIso φ ∧
          (F.X 0).IsQuasicoherentOnSite ∧ (F.X 0).IsFinitePresentationOnSite ∧
          (F.X (-1)).IsQuasicoherentOnSite ∧ (F.X (-1)).IsFiniteTypeOnSite
```

## Tag 0D10, a lemma

[Tag 0D10](https://stacks.math.columbia.edu/tag/0D10) in the Stacks Project.

**`AlgebraicGeometry.Space.formallySmooth_iff_isZero_homology_negOne_and_isLocallyProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentFormallySmooth.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentFormallySmooth.lean#L134). The attribute's comment: “the second condition read on the sheaf of differentials Ω\_\{X/Y} of 04CT, which the source identifies with H⁰(NL\_\{X/Y}) (0D0Y)”.

> **Stacks 0D10.** A morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` is formally
> smooth if and only if the cohomology sheaf `H⁻¹(NL_{X/Y})` of its naive cotangent complex
> vanishes and its sheaf of differentials `Ω_{X/Y} = H⁰(NL_{X/Y})` is locally projective.
>
> `Ω_{X/Y}` is the degree-zero cohomology sheaf of `NL_{X/Y}` by Stacks 0D0Y,
> `AlgebraicGeometry.Space.naiveCotangentComplexHomologyZeroIsoSheafOfDifferentials`, and is
> quasi-coherent by Stacks 04CV, which is the standing hypothesis of local projectivity
> (Stacks 060R).

```lean
theorem formallySmooth_iff_isZero_homology_negOne_and_isLocallyProjective
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    FormallySmooth f.hom ↔
      (IsZero ((naiveCotangentComplex B S hS f).homology (-1)) ∧
        IsLocallyProjective B S hS X.2
          ⟨sheafOfDifferentials B S hS f,
            isQuasicoherentOnSite_sheafOfDifferentials B S hS f⟩)
```

## Tag 0D11, a lemma

[Tag 0D11](https://stacks.math.columbia.edu/tag/0D11) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.Smooth.formallyEtale_iff_isZero_homology_naiveCotangentComplex`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentFormallyEtale.lean#L299), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentFormallyEtaleSpacesTag.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentFormallyEtaleSpacesTag.lean#L71) (StacksFrontier): “the tag prints the statement of 0D0M verbatim, for a morphism of schemes; registered on the declaration proving 0D0M rather than restated”.

## Tag 0D12, a lemma

[Tag 0D12](https://stacks.math.columbia.edu/tag/0D12) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_iff_isZero_homology_negOne_and_isFiniteLocallyFreeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentSmoothCriterion.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/NaiveCotangentSmoothCriterion.lean#L81). The attribute's comment: “the third clause read on the sheaf of differentials Ω\_\{X/Y} of 04CT, which the source identifies with H⁰(NL\_\{X/Y})”.

> **Stacks 0D12.** A morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` is smooth if
> and only if it is locally of finite presentation, the cohomology sheaf `H⁻¹(NL_{X/Y})` of its
> naive cotangent complex vanishes, and its sheaf of differentials `Ω_{X/Y} = H⁰(NL_{X/Y})` is
> finite locally free on the small étale site of `X`.

```lean
theorem isSmooth_iff_isZero_homology_negOne_and_isFiniteLocallyFreeOnSite
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) :
    IsSmooth B S hS f.hom ↔
      (IsLocallyOfFinitePresentation B S hS f.hom ∧
        IsZero ((naiveCotangentComplex B S hS f).homology (-1)) ∧
        SheafOfModules.IsFiniteLocallyFreeOnSite (sheafOfDifferentials B S hS f))
```

Declarations registered for the tag:

- [`Stacks.Smooth.smooth_iff_isZero_homology_negOne_and_isFiniteLocallyFree`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentSmoothCriterion.lean#L172), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentSmoothCriterionSpacesTag.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/NaiveCotangentSmoothCriterionSpacesTag.lean#L40) (StacksFrontier): “the tag prints the statement of 0D0N verbatim, for a morphism of schemes; registered on the declaration proving 0D0N rather than restated”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.21, Tag 0D0U](https://stacks.math.columbia.edu/tag/0D0U)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
