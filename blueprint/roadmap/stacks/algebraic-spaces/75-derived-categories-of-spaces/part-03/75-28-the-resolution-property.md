---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HasResolutionProperty, AlgebraicGeometry.Space.exists_affine_etale_cover_hasResolutionProperty_of_isRelativelyAmple, AlgebraicGeometry.Space.hasResolutionProperty_source_of_isRelativelyAmple, AlgebraicGeometry.Space.exists_finiteLocallyFree_modulePullback_hom_of_hasResolutionProperty, AlgebraicGeometry.Space.isQuasiAffineHom_of_isAffineHom, AlgebraicGeometry.Space.exists_affine_etale_cover_hasResolutionProperty_of_isQuasiAffineHom, AlgebraicGeometry.Space.hasResolutionProperty_source_of_isQuasiAffineHom, AlgebraicGeometry.Space.hasResolutionProperty_source_of_isAffineHom
statement: formalized
proof: formalized
---

# 75.28 The resolution property

Section 75.28 of the Stacks Project, [Tag 0GUR](https://stacks.math.columbia.edu/tag/0GUR). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GUS, a definition

[Tag 0GUS](https://stacks.math.columbia.edu/tag/0GUS) in the Stacks Project.

**`AlgebraicGeometry.Space.HasResolutionProperty`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionProperty.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionProperty.lean#L55).

> **Stacks 0GUS.** An algebraic space has the *resolution property* when every
> quasi-coherent module of finite type on it is a quotient of a finite locally free module.

```lean
class HasResolutionProperty (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) : Prop
```

## Tag 0GUT, a lemma

[Tag 0GUT](https://stacks.math.columbia.edu/tag/0GUT) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_affine_etale_cover_hasResolutionProperty_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyRelativeAmple.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyRelativeAmple.lean#L87). The attribute's comment: “the first step of the proof: an affine surjective étale chart of the target over which the scheme fibre product carries an ample module and has the resolution property”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme with `Y` quasi-compact, and
> let `L` be an `f`-ample module on `X`.  Then there is an affine scheme `V` over the base with a
> surjective étale morphism `g` to `Y`, and a cartesian square presenting the fibre product
> `V ×_Y X` as a scheme `U`, such that the base change of `L` to `U` is ample and `U` has the
> resolution property.

```lean
theorem exists_affine_etale_cover_hasResolutionProperty_of_isRelativelyAmple
    {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y} {L : Modules.{u, u} B S hS X.1 X.2}
    (hL : IsRelativelyAmple B S hS f L) (hY : IsQuasiCompactSpace B S hS Y.1) :
    ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y.1),
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
        (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        IsEtale B S hS g ∧
        ∃ (U : BigFppfOver B S hS) (q : U ⟶ V) (p : yoneda.obj U ⟶ X.1),
          IsPullback p (yoneda.map q) f.hom g ∧
            (∃ hinv : Stacks.Ample.IsInvertibleModule ((BigFppfOver.toScheme B S hS).obj U)
                (baseChangeModule B S hS L U p),
              @Stacks.Ample.IsAmple ((BigFppfOver.toScheme B S hS).obj U)
                (baseChangeModule B S hS L U p) hinv) ∧
            _root_.AlgebraicGeometry.HasResolutionProperty
              ((BigFppfOver.toScheme B S hS).obj U)
```

**`AlgebraicGeometry.Space.hasResolutionProperty_source_of_isRelativelyAmple`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyRelativeAmpleMain.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyRelativeAmpleMain.lean#L163).

> **Stacks 0GUT.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over a scheme `S` such
> that `Y` is quasi-compact, quasi-separated and has the resolution property, and such that there
> is an `f`-ample invertible `𝒪_X`-module `L`.  Then `X` has the resolution property.
>
> This is `AlgebraicGeometry.Space.exists_finiteLocallyFree_epi_of_isRelativelyAmple` packaged as
> the class `AlgebraicGeometry.Space.HasResolutionProperty` of Stacks 0GUS.
>
> The hypotheses are exactly the tag's.  `hLinv` is part of hypothesis (2): Stacks 0D31 defines an
> `f`-ample module to be invertible, and in this tree `IsRelativelyAmple` records invertibility only
> of the base changes of `L` to the scheme charts, so it is carried separately.  `hZ` is needed only
> to state `IsAbsolutelyQuasiSeparated`, this tree's spelling of quasi-separatedness of `Y`.
> Quasi-compactness and quasi-separatedness of `f` are *derived* from `hL` by Stacks 0D34 and 03KK,
> not assumed.

```lean
theorem hasResolutionProperty_source_of_isRelativelyAmple (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (L : Modules.{u, u} B S hS X.1 X.2)
    (hLinv : IsInvertibleModule X L) (hL : IsRelativelyAmple B S hS f L)
    (hYqc : IsQuasiCompactSpace B S hS Y.1) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    (hYres : HasResolutionProperty.{u, u} B S hS Y.1 Y.2) :
    HasResolutionProperty.{u, u} B S hS X.1 X.2
```

## Tag 0GUU, a lemma

[Tag 0GUU](https://stacks.math.columbia.edu/tag/0GUU) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_finiteLocallyFree_modulePullback_hom_of_hasResolutionProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyPushforwardSections.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyPushforwardSections.lean#L151). The attribute's comment: “the step of the proof producing the finite locally free module on the target and its transpose on the source, for a quasi-compact quasi-separated morphism: the sections of the direct image over an affine chart of the target lie in the image submodule”.

> **The step of the proof of Stacks 0GUU which produces the finite locally free module on the
> source.**  In the situation of
> `AlgebraicGeometry.Space.exists_finiteLocallyFree_epi_submodule_modulePushforward` the pullback
> `f^*ℰ` is again finite locally free, and the map `ℰ ⟶ f_*ℱ` — the epimorphism onto the submodule
> `𝒢` followed by its inclusion — transposes along `f^* ⊣ f_*` to a map `ψ : f^*ℰ ⟶ ℱ`.
>
> This is the source's sentence *"Then the corresponding maps `f^*ℰ_i ⊗ ℒ^{⊗ n_i} → ℱ` are going to
> be jointly surjective"* at `ℒ = 𝒪_X`, up to that surjectivity: the module and the map exist, and
> `ψ` is characterized by its transpose being `φ ≫ 𝒢.ι`.  Finite local freeness of `f^*ℰ` is
> Stacks 03DL under pullback.

```lean
theorem exists_finiteLocallyFree_modulePullback_hom_of_hasResolutionProperty
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hYqc : IsQuasiCompactSpace B S hS Y.1)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    (hYres : HasResolutionProperty.{u, u} B S hS Y.1 Y.2)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    {α : Type*} (s : Finset α) (V : SmallEtale B S hS Y.1) (hV : IsAffine (chartScheme V))
    (σ : α → ((modulePushforward B S hS f).obj F).val.obj (op V)) :
    ∃ (G : ((modulePushforward B S hS f).obj F).Submodule)
      (E : Modules.{u, u} B S hS Y.1 Y.2)
      (_ : SheafOfModules.IsFiniteLocallyFreeOnSite E)
      (φ : E ⟶ G.toSheafOfModules), Epi φ ∧ (∀ x ∈ s, σ x ∈ G.obj (op V)) ∧
        SheafOfModules.IsFiniteLocallyFreeOnSite ((modulePullback B S hS f).obj E) ∧
        ∃ ψ : (modulePullback B S hS f).obj E ⟶ F,
          (modulePullbackAdjunction B S hS f).homEquiv E F ψ = φ ≫ G.ι
```

**`AlgebraicGeometry.Space.isQuasiAffineHom_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffine.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffine.lean#L125). The attribute's comment: “the reduction of the hypothesis: the affine case of the statement is its quasi-affine case, an affine morphism of algebraic spaces being quasi-affine”.

> **The reduction of the affine case of Stacks 0GUU to its quasi-affine case.**  An affine
> morphism of algebraic spaces is quasi-affine: its base change to an affine test object is
> represented by an affine, hence quasi-affine, scheme.
>
> This is why Stacks 0GUU may assume `f` quasi-affine throughout: its two hypotheses, affine and
> quasi-affine, are one hypothesis.

```lean
theorem isQuasiAffineHom_of_isAffineHom {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : IsAffineHom B S hS f) : IsQuasiAffineHom B S hS f
```

**`AlgebraicGeometry.Space.exists_affine_etale_cover_hasResolutionProperty_of_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffine.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffine.lean#L168). The attribute's comment: “the chart step of the proof: an affine surjective étale chart of the target over which the scheme fibre product has the resolution property”.

> **The chart step of the proof of Stacks 0GUU.** For `f : X ⟶ Y` a
> quasi-affine morphism of algebraic spaces with `Y` quasi-compact there are an affine scheme `V`
> over the base with a surjective étale morphism to `Y` and a cartesian square presenting the
> fibre product `V ×_Y X` as a scheme `U` with the resolution property.
>
> This is the source's sentence *"Choose an affine scheme `V` and a surjective étale morphism
> `V → Y`.  Set `U = V ×_Y X`"*, with the properties of `U` that the rest of the proof reads off
> it: `𝒪_U` is ample on `U` because `f` is quasi-affine and `V` is affine (Stacks 0GUQ and
> Stacks 01VK), so `U` has the resolution property by Stacks 0F87.

```lean
theorem exists_affine_etale_cover_hasResolutionProperty_of_isQuasiAffineHom
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsQuasiAffineHom B S hS f.hom)
    (hY : IsQuasiCompactSpace B S hS Y.1) :
    ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y.1),
      IsAffine ((BigFppfOver.toScheme B S hS).obj V) ∧
        (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        IsEtale B S hS g ∧
        ∃ (U : BigFppfOver B S hS) (q : U ⟶ V) (p : yoneda.obj U ⟶ X.1),
          IsPullback p (yoneda.map q) f.hom g ∧
            _root_.AlgebraicGeometry.HasResolutionProperty
              ((BigFppfOver.toScheme B S hS).obj U)
```

**`AlgebraicGeometry.Space.hasResolutionProperty_source_of_isQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffineMain.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffineMain.lean#L86). The attribute's comment: “the quasi-affine case; the affine case is `AlgebraicGeometry.Space.hasResolutionProperty_source_of_isAffineHom`, and the two together are the tag's "affine or quasi-affine"”.

> **Stacks 0GUU, the quasi-affine case.**  For `f : X ⟶ Y` a quasi-affine morphism of algebraic
> spaces over `S` with `Y` quasi-compact, quasi-separated and carrying the resolution property, `X`
> has the resolution property.
>
> This is the source's reduction: by Stacks 0GUQ the structure sheaf of `X` is `f`-ample
> (`AlgebraicGeometry.Space.isRelativelyAmple_unit_of_isQuasiAffineHom`) and invertible
> (`AlgebraicGeometry.Space.isInvertibleModule_unit`), so this is Stacks 0GUT,
> `AlgebraicGeometry.Space.hasResolutionProperty_source_of_isRelativelyAmple`, at `L = 𝒪_X`.

```lean
theorem hasResolutionProperty_source_of_isQuasiAffineHom (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsQuasiAffineHom B S hS f.hom)
    (hYqc : IsQuasiCompactSpace B S hS Y.1) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    (hYres : HasResolutionProperty.{u, u} B S hS Y.1 Y.2) :
    HasResolutionProperty.{u, u} B S hS X.1 X.2
```

**`AlgebraicGeometry.Space.hasResolutionProperty_source_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffineMain.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyQuasiAffineMain.lean#L103). The attribute's comment: “the affine case; the quasi-affine case is `AlgebraicGeometry.Space.hasResolutionProperty_source_of_isQuasiAffineHom`, and the two together are the tag's "affine or quasi-affine"”.

> **Stacks 0GUU, the affine case.**  For `f : X ⟶ Y` an affine morphism of algebraic spaces over
> `S` with `Y` quasi-compact, quasi-separated and carrying the resolution property, `X` has the
> resolution property.
>
> An affine morphism of algebraic spaces is quasi-affine
> (`AlgebraicGeometry.Space.isQuasiAffineHom_of_isAffineHom`), so this is the quasi-affine case.

```lean
theorem hasResolutionProperty_source_of_isAffineHom (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hf : IsAffineHom B S hS f.hom)
    (hYqc : IsQuasiCompactSpace B S hS Y.1) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y.1)
    (hYres : HasResolutionProperty.{u, u} B S hS Y.1 Y.2) :
    HasResolutionProperty.{u, u} B S hS X.1 X.2
```

## Tag 0GUV, a lemma

[Tag 0GUV](https://stacks.math.columbia.edu/tag/0GUV) in the Stacks Project.

**`AlgebraicGeometry.Space.hasResolutionProperty_of_isSurjective_isFiniteLocallyFree_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyFiniteLocallyFreeTrace.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ResolutionPropertyFiniteLocallyFreeTrace.lean#L186).

> **Stacks 0GUV, with no further input.**  For `f : X ⟶ Y` a surjective finite locally free
> morphism of algebraic spaces over a scheme `S`, if `X` has the resolution property then so does
> `Y`.
>
> This is
> `AlgebraicGeometry.Space.hasResolutionProperty_of_isSurjective_isFiniteLocallyFree_of_dualTwist`
> with its hypothesis `hdual` discharged by `AlgebraicGeometry.Space.directImageDualDescent`, which
> is proved outright for every morphism of algebraic spaces.  Its hypotheses are therefore exactly
> the tag's: `f` surjective, `f` finite locally free, and `X` having the resolution property.

```lean
theorem hasResolutionProperty_of_isSurjective_isFiniteLocallyFree_unconditional (f : X ⟶ Y)
    (hsurj : IsSurjective B S hS f.hom) (hflf : IsFiniteLocallyFree B S hS f)
    (hX : HasResolutionProperty.{u, u} B S hS X.1 X.2) :
    HasResolutionProperty.{u, u} B S hS Y.1 Y.2
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.28, Tag 0GUR](https://stacks.math.columbia.edu/tag/0GUR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
