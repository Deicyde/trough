---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.t0Space_points_of_isZariskiLocallyQuasiSeparatedOver, AlgebraicGeometry.Space.quasiSober_points_of_isZariskiLocallyQuasiSeparatedOver, AlgebraicGeometry.Space.stacksSober_points_of_isZariskiLocallyQuasiSeparatedOver, AlgebraicGeometry.Space.spectralSpace_points_of_isQuasiCompactSpace_isAbsolutelyQuasiSeparated, AlgebraicGeometry.Space.exists_iso_yoneda_spec_of_surjective_etale_fieldSpec, AlgebraicGeometry.Space.exists_field_spectrum_of_surjective_etale, AlgebraicGeometry.Space.exists_iso_yoneda_spec_of_isDecentSpace_of_etale_fieldSpec, AlgebraicGeometry.Space.isDecentSpace_of_isAbsolutelyLocallySeparated
statement: formalized
proof: formalized
---

# 66.15 Points on quasi-separated spaces

Section 66.15 of the Stacks Project, [Tag 06NI](https://stacks.math.columbia.edu/tag/06NI). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06NJ, a lemma

[Tag 06NJ](https://stacks.math.columbia.edu/tag/06NJ) in the Stacks Project.

**`AlgebraicGeometry.Space.t0Space_points_of_isZariskiLocallyQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean#L98). The attribute's comment: “Kolmogorov property”.

> Two points of the space of points of a Zariski locally quasi-separated algebraic space over
> `S` which are topologically indistinguishable are equal.

```lean
theorem t0Space_points_of_isZariskiLocallyQuasiSeparatedOver
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsZariskiLocallyQuasiSeparatedOver B S hS F) :
    T0Space (points B S hS F)
```

**`AlgebraicGeometry.Space.quasiSober_points_of_isZariskiLocallyQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean#L108). The attribute's comment: “generic points of irreducible closed subsets”.

> Every irreducible closed subset of the space of points of a Zariski locally quasi-separated
> algebraic space over `S` is the closure of one of its points.

```lean
theorem quasiSober_points_of_isZariskiLocallyQuasiSeparatedOver
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsZariskiLocallyQuasiSeparatedOver B S hS F) :
    QuasiSober (points B S hS F)
```

**`AlgebraicGeometry.Space.stacksSober_points_of_isZariskiLocallyQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean#L118).

> The space of points of a Zariski locally quasi-separated algebraic space over `S` is sober:
> every irreducible closed subset of it has a unique generic point.

```lean
theorem stacksSober_points_of_isZariskiLocallyQuasiSeparatedOver
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsZariskiLocallyQuasiSeparatedOver B S hS F) :
    StacksSober (points B S hS F)
```

## Tag 0A4G, a lemma

[Tag 0A4G](https://stacks.math.columbia.edu/tag/0A4G) in the Stacks Project.

**`AlgebraicGeometry.Space.spectralSpace_points_of_isQuasiCompactSpace_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpectralPoints.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpectralPoints.lean#L213).

> **Stacks 0A4G.** The point space of a quasi-compact quasi-separated algebraic space over
> `S` is a spectral space.

```lean
theorem spectralSpace_points_of_isQuasiCompactSpace_isAbsolutelyQuasiSeparated
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X) :
    SpectralSpace (points B S hS X)
```

## Tag 03DZ, a lemma

[Tag 03DZ](https://stacks.math.columbia.edu/tag/03DZ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_iso_yoneda_spec_of_surjective_etale_fieldSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleFieldAtlas.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleFieldAtlas.lean#L273).

> A quasi-separated algebraic space over `S` admitting a surjective étale morphism from the
> spectrum of a field `k` is the spectrum of a field `k'`, and `k` is a finite separable extension
> of `k'`.

```lean
theorem exists_iso_yoneda_spec_of_surjective_etale_fieldSpec
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal F)
    (k : Type u) [Field k] {U : BigFppfOver B S hS}
    (eU : (BigFppfOver.toScheme B S hS).obj U ≅ Spec (.of k)) (f : yoneda.obj U ⟶ F)
    (hsurj : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) f)
    (hetale : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u}) (BigFppfOver.toScheme B S hS))) f) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k' k) (_ : Module.Finite k' k)
      (_ : Algebra.IsSeparable k' k) (U' : BigFppfOver B S hS)
      (eU' : (BigFppfOver.toScheme B S hS).obj U' ≅ Spec (.of k'))
      (m : U ⟶ U') (e : F ≅ yoneda.obj U'),
      f ≫ e.hom = yoneda.map m ∧
        eU.inv ≫ (BigFppfOver.toScheme B S hS).map m ≫ eU'.hom =
          Spec.map (CommRingCat.ofHom (algebraMap k' k))
```

**`AlgebraicGeometry.Space.exists_field_spectrum_of_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointLikeSpace.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointLikeSpace.lean#L643).

> **Stacks 03DZ.** Let `S` be a scheme, `k` a field and `X` an algebraic space over `S`
> admitting a surjective étale morphism `Spec(k) ⟶ X`. If `X` is quasi-separated — Stacks 03BS
> part (3), that is, quasi-separated over `Spec(ℤ)` — then `X` is isomorphic to `Spec(k')` for a
> field `k'` with `k/k'` finite separable, the isomorphism carrying the given atlas to the
> morphism induced by the field extension.
>
> This is
> `AlgebraicGeometry.Space.exists_field_spectrum_of_surjective_etale_of_isQuasiSeparatedOver`,
> which asks only for quasi-separatedness over `S` and is therefore stronger, together with
> `AlgebraicGeometry.Space.isQuasiSeparatedOver_of_isAbsolutelyQuasiSeparated`.
> Surjectivity is taken in the sense of Stacks 03ME, that the induced map on points is
> surjective, which is the source's reading; the engine asks instead that every represented base
> change be a surjective morphism of schemes, and the two agree for a morphism into an algebraic
> space by `AlgebraicGeometry.Space.presheafSurjective_of_isSurjective`, whose representability
> hypothesis is supplied by the representable diagonal of `X`.

```lean
theorem exists_field_spectrum_of_surjective_etale
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ F)
    (k : Type u) [Field k] (hk : B.Contains (Spec (CommRingCat.of k)))
    (b : Spec (CommRingCat.of k) ⟶ S)
    (f : yoneda.obj (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS)) ⟶ F)
    (hsurj : IsSurjective B S hS f)
    (hetale : (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) f) :
    ∃ (k' : Type u) (_ : Field k') (_ : Algebra k' k)
      (_ : Module.Finite k' k) (_ : Algebra.IsSeparable k' k)
      (hk' : B.Contains (Spec (CommRingCat.of k')))
      (b' : Spec (CommRingCat.of k') ⟶ S),
      ∃ (hbase : Spec.map (CommRingCat.ofHom (algebraMap k' k)) ≫ b' = b)
        (e : F ≅ yoneda.obj (Over.mk (⟨b'⟩ : B.obj hk' ⟶ B.obj hS))),
        f ≫ e.hom = yoneda.map (Over.homMk
          (ObjectProperty.homMk (Spec.map (CommRingCat.ofHom (algebraMap k' k))) :
            B.obj hk ⟶ B.obj hk') (by
              apply ObjectProperty.hom_ext
              exact hbase))
```

## Tag 03E0, a remark

[Tag 03E0](https://stacks.math.columbia.edu/tag/03E0) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.exists_iso_yoneda_spec_of_isDecentSpace_of_etale_fieldSpec`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldAtlas.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldAtlas.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldAtlas.lean#L156) (StacksFrontier): “Stacks 03DZ holds for decent algebraic spaces”.
- [`AlgebraicGeometry.Space.isDecentSpace_of_isAbsolutelyLocallySeparated`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallySeparated.lean#L1018), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallySeparated.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallySeparated.lean#L1033) (StacksFrontier): “a locally separated algebraic space is decent”.
- [`AlgebraicGeometry.Space.isRepresentable_of_subsingleton_points`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/SinglePointSpace.lean#L253), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/SinglePointSpace.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/SinglePointSpace.lean#L370) (StacksFrontier): “a decent algebraic space with one point is a scheme”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.15, Tag 06NI](https://stacks.math.columbia.edu/tag/06NI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
