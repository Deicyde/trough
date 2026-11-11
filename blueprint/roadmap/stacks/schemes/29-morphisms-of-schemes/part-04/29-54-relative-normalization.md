---
declaration: section
origin: cited
lean: Stacks.RelativeNormalization.integralClosureSpectrum_isRelativeNormalization, AlgebraicGeometry.Scheme.QuasicoherentAlgebra.mem_range_integralClosureAlgebraι_app_iff, AlgebraicGeometry.Scheme.QuasicoherentAlgebra.isQuasicoherent_integralClosureAlgebra, AlgebraicGeometry.Scheme.QuasicoherentAlgebra.range_stalkFunctor_map_integralClosureAlgebraι, AlgebraicGeometry.Scheme.QuasicoherentAlgebra.range_integralClosureAlgebraι_app_of_isAffineOpen, AlgebraicGeometry.Scheme.QuasicoherentAlgebra.integralClosureAlgebra, AlgebraicGeometry.Scheme.Hom.normalization_universalProperty_iff_existsUnique_iso, AlgebraicGeometry.Scheme.Hom.normalizationDesc_universalProperty
statement: formalized
proof: formalized
---

# 29.54 Relative normalization

Section 29.54 of the Stacks Project, [Tag 0BAK](https://stacks.math.columbia.edu/tag/0BAK). 14 tags here are carried by 26 declarations of the repository (all in StacksFrontier) and 15 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BAK, the section

[Tag 0BAK](https://stacks.math.columbia.edu/tag/0BAK) in the Stacks Project.

**`Stacks.RelativeNormalization.integralClosureSpectrum_isRelativeNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureSpectrum.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureSpectrum.lean#L352). References: EGA IV (18.10.10), “more general”; EGA IV (18.12.14), “partial”; EGA IV (8.12.3).

> **Relative normalization.** Let `f : Y ⟶ X` be a
> quasi-compact and quasi-separated morphism of schemes, let `𝒪' ⊆ f_* 𝒪_Y` be the integral
> closure of `𝒪_X` in `f_* 𝒪_Y`, and let `ν : X' = Spec_X(𝒪') ⟶ X` be its relative spectrum, the
> normalization of `X` in `Y`. Then:
>
> * `f` factors as `f = ν ∘ f'`, where `f' : Y ⟶ X'` is the canonical morphism
>   `Y ⟶ Spec_X(f_* 𝒪_Y)` followed by the morphism of relative spectra induced by the inclusion
>   `𝒪' ⊆ f_* 𝒪_Y`;
> * `ν` is integral and `f'` is dominant;
> * for every factorization `f = π ∘ g` with `π : Z ⟶ X` integral there is a unique
>   `h : X' ⟶ Z` with `h ∘ f' = g` and `π ∘ h = ν`;
> * consequently `X'` is uniquely isomorphic, under `Y` and over `X`, to the relative
>   normalization `f.normalization`.

```lean
theorem integralClosureSpectrum_isRelativeNormalization :
    toIntegralClosureSpectrum f ≫ (integralClosureSpectrum f).toBase = f ∧
    toRelativeSpec f ≫ relativeSpectrumMapOfAlgebraHom (integralClosureSituation f)
        (pushforwardAlgebra f) (AlgebraSheaf.isQuasicoherent_pushforwardAlgebra f)
        (integralClosureAlgebraι (pushforwardAlgebra f)) = toIntegralClosureSpectrum f ∧
    IsIntegralHom (integralClosureSpectrum f).toBase ∧
    IsDominant (toIntegralClosureSpectrum f) ∧
    (∀ (Z : Scheme.{u}) (g : Y ⟶ Z) (π : Z ⟶ X), IsIntegralHom π → g ≫ π = f →
      ∃! h : (integralClosureSpectrum f).scheme ⟶ Z,
        toIntegralClosureSpectrum f ≫ h = g ∧ h ≫ π = (integralClosureSpectrum f).toBase) ∧
    ∃! e : (integralClosureSpectrum f).scheme ≅ f.normalization,
      toIntegralClosureSpectrum f ≫ e.hom = f.toNormalization ∧
        e.hom ≫ f.fromNormalization = (integralClosureSpectrum f).toBase
```

## Tag 035F, a lemma

[Tag 035F](https://stacks.math.columbia.edu/tag/035F) in the Stacks Project.

**`AlgebraicGeometry.Scheme.QuasicoherentAlgebra.mem_range_integralClosureAlgebraι_app_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean, line 897](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean#L897). The attribute's comment: “the defining rule”.

> A section of `A` over `U` lies in the integral closure of the structure sheaf exactly when
> its germ at every point of `U` is integral over the local ring of `X` at that point.

```lean
theorem mem_range_integralClosureAlgebraι_app_iff {X : Scheme.{u}}
    (A : X.QuasicoherentAlgebra) (U : Opens X) (s : A.right.presheaf.obj (.op U)) :
    s ∈ Set.range ((integralClosureAlgebraι A).right.hom.app (.op U)) ↔
      ∀ (x : X) (hx : x ∈ U),
        ((TopCat.Presheaf.stalkFunctor CommRingCat x).map A.hom.hom).hom.IsIntegralElem
          (A.right.presheaf.germ U x hx s)
```

**`AlgebraicGeometry.Scheme.QuasicoherentAlgebra.isQuasicoherent_integralClosureAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean, line 912](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean#L912). The attribute's comment: “quasi-coherence”. References: EGA II (6.3.4), “quasi-coherence”.

> The integral closure of the structure sheaf in a quasi-coherent sheaf of `𝒪_X`-algebras is
> itself a quasi-coherent sheaf of `𝒪_X`-algebras.

```lean
theorem isQuasicoherent_integralClosureAlgebra {X : Scheme.{u}} (A : X.QuasicoherentAlgebra)
    [(underlyingModule A).IsQuasicoherent] :
    (underlyingModule (integralClosureAlgebra A)).IsQuasicoherent
```

**`AlgebraicGeometry.Scheme.QuasicoherentAlgebra.range_stalkFunctor_map_integralClosureAlgebraι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean, line 920](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean#L920). The attribute's comment: “stalks”. References: EGA II (6.3.2), “special case”.

> The stalk at `x` of the integral closure of the structure sheaf in `A` is the integral
> closure of the local ring `𝒪_{X,x}` in the stalk `A_x`.

```lean
theorem range_stalkFunctor_map_integralClosureAlgebraι {X : Scheme.{u}}
    (A : X.QuasicoherentAlgebra) (x : X) :
    letI : Algebra ((TopCat.Presheaf.stalkFunctor CommRingCat x).obj X.presheaf)
        ((TopCat.Presheaf.stalkFunctor CommRingCat x).obj A.right.presheaf) :=
      ((TopCat.Presheaf.stalkFunctor CommRingCat x).map A.hom.hom).hom.toAlgebra
    Set.range (((TopCat.Presheaf.stalkFunctor CommRingCat x).map
        (integralClosureAlgebraι A).right.hom).hom) =
      (integralClosure ((TopCat.Presheaf.stalkFunctor CommRingCat x).obj X.presheaf)
        ((TopCat.Presheaf.stalkFunctor CommRingCat x).obj A.right.presheaf) : Set _)
```

**`AlgebraicGeometry.Scheme.QuasicoherentAlgebra.range_integralClosureAlgebraι_app_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean, line 955](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean#L955). The attribute's comment: “affine sections”. References: EGA II (6.3.4), “affine sections”.

> Over an affine open `U`, the sections of the integral closure of the structure sheaf in a
> quasi-coherent `A` form the integral closure of `𝒪_X(U)` in `A(U)`.

```lean
theorem range_integralClosureAlgebraι_app_of_isAffineOpen {X : Scheme.{u}}
    (A : X.QuasicoherentAlgebra) [(underlyingModule A).IsQuasicoherent]
    (U : Opens X) (hU : IsAffineOpen U) :
    letI : Algebra (X.presheaf.obj (.op U)) (A.right.presheaf.obj (.op U)) :=
      (A.hom.hom.app (.op U)).hom.toAlgebra
    Set.range ((integralClosureAlgebraι A).right.hom.app (.op U)) =
      (integralClosure (X.presheaf.obj (.op U)) (A.right.presheaf.obj (.op U)) : Set _)
```

## Tag 035G, a definition

[Tag 035G](https://stacks.math.columbia.edu/tag/035G) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.QuasicoherentAlgebra.integralClosureAlgebra`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean#L858), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean, line 971](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/IntegralClosureAlgebra.lean#L971) (StacksFrontier).

## Tag 035I, a lemma

[Tag 035I](https://stacks.math.columbia.edu/tag/035I) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.normalization_universalProperty_iff_existsUnique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L95). The attribute's comment: “universal\_property”.

> An integral factorization of a quasi-compact, quasi-separated morphism has the
> universal property of relative normalization if and only if it is uniquely isomorphic
> to the relative normalization, compatibly with both maps of the factorization.

```lean
theorem normalization_universalProperty_iff_existsUnique_iso
    {X Y Z : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f]
    (i : Y ⟶ Z) (p : Z ⟶ X) [IsIntegralHom p] (hip : i ≫ p = f) :
    (∀ (T : Scheme.{u}) (j : Y ⟶ T) (q : T ⟶ X),
      IsIntegralHom q → j ≫ q = f →
        ∃! k : Z ⟶ T, i ≫ k = j ∧ k ≫ q = p) ↔
      ∃! e : Z ≅ f.normalization,
        i ≫ e.hom = f.toNormalization ∧ e.hom ≫ f.fromNormalization = p
```

**`AlgebraicGeometry.Scheme.Hom.normalizationDesc_universalProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L133). The attribute's comment: “normalization\_over\_intermediate”.

> Relative normalization is unchanged after replacing the target by an
> intermediate scheme integral over it.

```lean
theorem normalizationDesc_universalProperty
    {X Y Z : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f]
    (g : Y ⟶ Z) (p : Z ⟶ X) [IsIntegralHom p] (H : f = g ≫ p) :
    ∀ (T : Scheme.{u}) (j : Y ⟶ T) (q : T ⟶ Z),
      IsIntegralHom q → j ≫ q = g →
        ∃! k : f.normalization ⟶ T,
          f.toNormalization ≫ k = j ∧
            k ≫ q = f.normalizationDesc g p H
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.instIsIntegralHomFromNormalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.instIsIntegralHomFromNormalization#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L66) (StacksFrontier): “integral”.
- [`AlgebraicGeometry.Scheme.Hom.instIsDominantToNormalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.instIsDominantToNormalization#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L68) (StacksFrontier): “dominant”.
- [`AlgebraicGeometry.Scheme.Hom.normalizationDesc`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.normalizationDesc#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L72) (StacksFrontier): “universal\_property”.
- [`AlgebraicGeometry.Scheme.Hom.toNormalization_normalizationDesc`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.toNormalization_normalizationDesc#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L75) (StacksFrontier): “universal\_property”.
- [`AlgebraicGeometry.Scheme.Hom.normalizationDesc_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.normalizationDesc_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L78) (StacksFrontier): “universal\_property”.
- [`AlgebraicGeometry.Scheme.Hom.normalization.hom_ext`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.normalization.hom_ext#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L81) (StacksFrontier): “universal\_property”.

## Tag 035J, a lemma

[Tag 035J](https://stacks.math.columbia.edu/tag/035J) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.normalizationMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean#L55). The attribute's comment: “canonical morphism”.

> The canonical morphism between relative normalizations induced by a commutative square.

```lean
noncomputable def normalizationMap : f₂.normalization ⟶ f₁.normalization
```

**`AlgebraicGeometry.Scheme.Hom.toNormalization_normalizationMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean#L65). The attribute's comment: “upper square”.

> The canonical morphism between normalizations commutes with the maps from the source
> schemes.

```lean
lemma toNormalization_normalizationMap :
    f₂.toNormalization ≫ normalizationMap f₁ f₂ gY gX sq =
      gY ≫ f₁.toNormalization
```

**`AlgebraicGeometry.Scheme.Hom.normalizationMap_fromNormalization`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean#L74). The attribute's comment: “lower square”.

> The canonical morphism between normalizations commutes with the maps to the target
> schemes.

```lean
lemma normalizationMap_fromNormalization :
    normalizationMap f₁ f₂ gY gX sq ≫ f₁.fromNormalization =
      f₂.fromNormalization ≫ gX
```

**`AlgebraicGeometry.Scheme.Hom.normalizationMap_unique`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Functorial.lean#L84). The attribute's comment: “uniqueness”.

> A morphism between the relative normalizations that makes both squares commute is the
> canonical morphism.

```lean
lemma normalizationMap_unique (h : f₂.normalization ⟶ f₁.normalization)
    (h_source : f₂.toNormalization ≫ h = gY ≫ f₁.toNormalization)
    (h_target : h ≫ f₁.fromNormalization = f₂.fromNormalization ≫ gX) :
    h = normalizationMap f₁ f₂ gY gX sq
```

## Tag 035K, a lemma

[Tag 035K](https://stacks.math.columbia.edu/tag/035K) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.normalizationPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.normalizationPullback#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L350) (StacksFrontier): “the comparison morphism from the normalization of the base change to the base change of the normalization, for `f` quasi-compact and quasi-separated”.
- [`AlgebraicGeometry.Scheme.Hom.instIsIsoNormalizationPullbackOfSmooth`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.instIsIsoNormalizationPullbackOfSmooth#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L353) (StacksFrontier): “it is an isomorphism for a smooth base change, in particular for the inclusion of an open `U`”. References: SGA 3 X (8.9), “partial”.
- [`AlgebraicGeometry.instSmoothOfIsOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instSmoothOfIsOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L355) (StacksFrontier): “open immersions are smooth”. References: SGA 1 II (1.3), “more general”.

## Tag 0BXA, a lemma

[Tag 0BXA](https://stacks.math.columbia.edu/tag/0BXA) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.normalization_fromNormalization_isIso`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L156).

> The normalization of `f.normalization` in `X` is canonically isomorphic to
> `f.normalization`.

```lean
instance normalization_fromNormalization_isIso :
    IsIso (f.toNormalization.fromNormalization)
```

## Tag 0AXP, a lemma

[Tag 0AXP](https://stacks.math.columbia.edu/tag/0AXP) in the Stacks Project.

**`AlgebraicGeometry.exists_genericPoint_irreducibleComponent_mapping_to`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/RelativeGenericPoints.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/RelativeGenericPoints.lean#L42).

> Every generic point of an irreducible component of the relative normalization of the target
> in the source is the image of a generic point of an irreducible component of the source.

```lean
public theorem exists_genericPoint_irreducibleComponent_mapping_to
    {X Y : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f]
    {x : f.normalization} {Z : Set f.normalization}
    (hZ : Z ∈ irreducibleComponents f.normalization) (hx : IsGenericPoint x Z) :
    ∃ (y : Y) (T : Set Y),
      T ∈ irreducibleComponents Y ∧ IsGenericPoint y T ∧ f.toNormalization y = x
```

## Tag 03GO, a lemma

[Tag 03GO](https://stacks.math.columbia.edu/tag/03GO) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.normalizationCoprodIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.normalizationCoprodIso#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L117) (StacksFrontier): “the isomorphism of schemes”. References: EGA IV (18.10.8), “partial”; EGA IV (18.10.10), “partial”.
- [`AlgebraicGeometry.Scheme.Hom.normalizationCoprodIso_inv_coprodDesc_fromNormalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.normalizationCoprodIso_inv_coprodDesc_fromNormalization#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L120) (StacksFrontier): “compatibility with the morphisms to the base”. References: EGA II (6.3.6), “more general”.
- [`AlgebraicGeometry.Scheme.Hom.toNormalization_inl_normalizationCoprodIso_hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.toNormalization_inl_normalizationCoprodIso_hom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L123) (StacksFrontier): “compatibility with the dominant morphism from the first summand”.
- [`AlgebraicGeometry.Scheme.Hom.toNormalization_inr_normalizationCoprodIso_hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.toNormalization_inr_normalizationCoprodIso_hom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L126) (StacksFrontier): “compatibility with the dominant morphism from the second summand”.

## Tag 03GQ, a lemma

[Tag 03GQ](https://stacks.math.columbia.edu/tag/03GQ) in the Stacks Project.

**`AlgebraicGeometry.isIntegral_app_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/UniversallyClosed.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/UniversallyClosed.lean#L64). The attribute's comment: “integrality of the pushed-forward structure sheaf”.

> **Stacks Project, Tag 03GQ.** For a universally closed morphism of schemes `f : X ⟶ S` and
> an affine open `U` of `S`, the ring map `Γ(S, U) ⟶ Γ(X, f⁻¹(U))` on sections is integral. This
> is the assertion that `f_* 𝒪_X` is integral over `𝒪_S`.
>
> Only universal closedness is needed; the quasi-compactness and quasi-separatedness of Tag 03GQ
> are what make `f_* 𝒪_X` a quasi-coherent algebra, not what make it integral.

```lean
theorem isIntegral_app_of_universallyClosed (f : X ⟶ S) [UniversallyClosed f] {U : S.Opens}
    (hU : IsAffineOpen U) : RingHom.IsIntegral (f.app U).hom
```

**`AlgebraicGeometry.isIntegralHom_toBase_pushforwardSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean#L113). The attribute's comment: “integral”.

> For a quasi-separated, universally closed morphism `f : X ⟶ S` the sheaf of algebras
> `f_* 𝒪_X` is integral over `𝒪_S`: the structure morphism `Spec_S(f_* 𝒪_X) ⟶ S` of its relative
> spectrum is an integral morphism.
>
> An affine morphism is integral as soon as it is universally closed, and universal closedness is
> checked on the affine opens of `S`, where the structure morphism is the spectrum of the integral
> ring map `Γ(S, U) ⟶ Γ(X, f⁻¹U)`.

```lean
theorem isIntegralHom_toBase_pushforwardSpectrum :
    IsIntegralHom (pushforwardSpectrum f).toBase
```

**`AlgebraicGeometry.normalizationIsoPushforwardSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean#L209). The attribute's comment: “normalization”.

> For a quasi-separated, universally closed morphism `f : X ⟶ S` the normalization of `S` in
> `X` is isomorphic to the relative spectrum `Spec_S(f_* 𝒪_X)`.

```lean
noncomputable def normalizationIsoPushforwardSpectrum :
    f.normalization ≅ (pushforwardSpectrum f).scheme
```

**`AlgebraicGeometry.toNormalization_normalizationIsoPushforwardSpectrum_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean#L216). The attribute's comment: “normalization: first factor”.

> Under the identification of the normalization of `S` in `X` with `Spec_S(f_* 𝒪_X)`, the
> canonical morphism `X ⟶ f.normalization` becomes the canonical morphism `X ⟶ Spec_S(f_* 𝒪_X)`.

```lean
theorem toNormalization_normalizationIsoPushforwardSpectrum_hom :
    f.toNormalization ≫ (normalizationIsoPushforwardSpectrum f).hom = canonicalMorphism f
```

**`AlgebraicGeometry.normalizationIsoPushforwardSpectrum_hom_comp_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/UniversallyClosed/IntegralPushforward.lean#L223). The attribute's comment: “normalization: second factor”.

> Under the identification of the normalization of `S` in `X` with `Spec_S(f_* 𝒪_X)`, the
> structure morphism `f.normalization ⟶ S` becomes the structure morphism `Spec_S(f_* 𝒪_X) ⟶ S`.

```lean
theorem normalizationIsoPushforwardSpectrum_hom_comp_toBase :
    (normalizationIsoPushforwardSpectrum f).hom ≫ (pushforwardSpectrum f).toBase =
      f.fromNormalization
```

**`Stacks.RelativeSpec.normalizationIsoRelativeSpec`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Normalization.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/Normalization.lean#L191). The attribute's comment: “comparison with relative normalization”.

> **Stacks Project, Tag 03GQ.** For a quasi-separated and universally closed morphism
> `f : X ⟶ S`, the relative normalization of `S` in `X` is the relative spectrum of `f_* 𝒪_X`.

```lean
noncomputable def normalizationIsoRelativeSpec :
    f.normalization ≅ (gluedSpectrum (pushforwardSituation f)).scheme
```

**`Stacks.RelativeSpec.normalizationIsoRelativeSpec_hom_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Normalization.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/Normalization.lean#L198). The attribute's comment: “comparison over the base”.

> **Stacks Project, Tag 03GQ.** The comparison of the relative normalization with the relative
> spectrum of `f_* 𝒪_X` is an isomorphism over the base.

```lean
theorem normalizationIsoRelativeSpec_hom_toBase :
    (normalizationIsoRelativeSpec f).hom ≫
        (gluedSpectrum (pushforwardSituation f)).toBase = f.fromNormalization
```

**`Stacks.RelativeSpec.toNormalization_normalizationIsoRelativeSpec_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeSpec/Normalization.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeSpec/Normalization.lean#L209). The attribute's comment: “comparison of canonical source maps”.

> **Stacks Project, Tag 03GQ.** The comparison of the relative normalization with the relative
> spectrum of `f_* 𝒪_X` carries the canonical morphism to the relative normalization to the
> canonical morphism of [Stacks, Tag 01LY]. Together with
> `Stacks.RelativeSpec.normalizationIsoRelativeSpec_hom_toBase` this says that the relative
> normalization of `S` in `X` *is* the factorization `X ⟶ Spec_S(f_* 𝒪_X) ⟶ S`.

```lean
theorem toNormalization_normalizationIsoRelativeSpec_hom :
    f.toNormalization ≫ (normalizationIsoRelativeSpec f).hom = toRelativeSpec f
```

## Tag 035L, a lemma

[Tag 035L](https://stacks.math.columbia.edu/tag/035L) in the Stacks Project.

**`AlgebraicGeometry.exists_iso_sigma_normalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/RelativeNormal.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/RelativeNormal.lean#L517). The attribute's comment: “disjoint union of integral normal schemes”.

> **Stacks Project, Tag 035L.** The normalization of `Y` in a normal scheme `X` whose
> quasi-compact opens have finitely many irreducible components is a disjoint union of integral
> normal schemes.

```lean
theorem exists_iso_sigma_normalization [IsNormal X]
    (hX : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) :
    ∃ (ι : Type u) (Z : ι → Scheme.{u}) (_ : ∀ i, IsNormal (Z i))
        (_ : ∀ i, AlgebraicGeometry.IsIntegral (Z i)), Nonempty (f.normalization ≅ ∐ Z)
```

**`AlgebraicGeometry.bijOn_irreducibleComponents_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/RelativeNormal.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/RelativeNormal.lean#L529). The attribute's comment: “bijection on irreducible components”.

> **Stacks Project, Tag 035L.** The dominant morphism from `X` to the normalization of `Y` in
> `X` carries irreducible components to irreducible components bijectively.

```lean
theorem bijOn_irreducibleComponents_toNormalization [IsNormal X]
    (hX : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite) :
    Set.BijOn (fun C ↦ closure (f.toNormalization.base '' C))
      (irreducibleComponents X) (irreducibleComponents f.normalization)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.instIsDominantToNormalization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.instIsDominantToNormalization#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/Relative.lean#L70) (StacksFrontier): “dominance”.

## Tag 0AVK, a lemma

[Tag 0AVK](https://stacks.math.columbia.edu/tag/0AVK) in the Stacks Project.

**`AlgebraicGeometry.isFinite_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean#L164).

> **Stacks Project, Tag 0AVK.** Let `f : X ⟶ S` be quasi-compact and quasi-separated with `X`
> reduced. If the quasi-compact opens of `X` have finitely many irreducible components, the residue
> field extension at every generic point of an irreducible component of `X` is finitely generated,
> and `S` is Nagata, then the normalization of `S` in `X` is finite over `S`.

```lean
theorem isFinite_fromNormalization
    {X S : Scheme.{u}} (f : X ⟶ S) (hS : IsNagataScheme S)
    [QuasiCompact f] [QuasiSeparated f] [IsReduced X]
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite)
    (hκ : ∀ x : genericPoints X,
      letI := (f.residueFieldMap x.1).hom.toAlgebra
      (⊤ : IntermediateField (S.residueField (f x.1)) (X.residueField x.1)).FG) :
    IsFinite f.fromNormalization
```

## Tag 03GR, a lemma

[Tag 03GR](https://stacks.math.columbia.edu/tag/03GR) in the Stacks Project.

**`AlgebraicGeometry.isFinite_fromNormalization_of_locallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/NagataNormalization/Basic.lean#L208).

> **Stacks Project, Tag 03GR.** Let `f : X ⟶ S` be of finite type with `X` reduced and `S`
> Nagata. Then the normalization of `S` in `X` is finite over `S`.

```lean
theorem isFinite_fromNormalization_of_locallyOfFiniteType {X S : Scheme.{u}} (f : X ⟶ S)
    (hS : IsNagataScheme S) [LocallyOfFiniteType f] [QuasiCompact f] [IsReduced X] :
    haveI : IsLocallyNoetherian S :=
      ((isNagataScheme_iff_isLocallyNoetherian_and_isUniversallyJapaneseScheme S).mp hS).1
    IsFinite f.fromNormalization
```

## Tag 0BXB, a lemma

[Tag 0BXB](https://stacks.math.columbia.edu/tag/0BXB) in the Stacks Project.

**`AlgebraicGeometry.isDiscreteValuationRing_stalk_normalization_of_isEmpty_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/CodimensionOne.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Normalization/CodimensionOne.lean#L234).

> **Stacks Project, Tag 0BXB.** Let `f : Y ⟶ X` be of finite type with `Y` reduced and `X`
> Nagata, and let `X'` be the normalization of `X` in `Y`. If the local ring of `X'` at a point `x'`
> has Krull dimension one and the fibre of `Y ⟶ X'` over `x'` is empty, then that local ring is a
> discrete valuation ring.

```lean
theorem isDiscreteValuationRing_stalk_normalization_of_isEmpty_fiber {X Y : Scheme.{u}}
    (f : Y ⟶ X) [LocallyOfFiniteType f] [QuasiCompact f] [IsReduced Y] (hX : IsNagataScheme X) :
    haveI : IsLocallyNoetherian X :=
      ((isNagataScheme_iff_isLocallyNoetherian_and_isUniversallyJapaneseScheme X).mp hX).1
    ∀ x' : f.normalization,
      ringKrullDim (f.normalization.presheaf.stalk x') = 1 →
      IsEmpty (f.toNormalization.fiber x') →
      ∃ _ : IsDomain (f.normalization.presheaf.stalk x'),
        IsDiscreteValuationRing (f.normalization.presheaf.stalk x')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.54, Tag 0BAK](https://stacks.math.columbia.edu/tag/0BAK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
