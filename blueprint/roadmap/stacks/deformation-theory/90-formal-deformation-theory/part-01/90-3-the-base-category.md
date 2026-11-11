---
declaration: section
origin: cited
lean: Deformation.ArtinianLocalAlgCat, Deformation.ArtinianLocalAlgCat.Hom, Deformation.ArtinianLocalAlgCat.instCategory, Deformation.IsClassical, InfinitesimalLifting.IsSmallExtension, Deformation.surjective_factors_into_smallExtensions, Deformation.residueImageField_eq_range, Deformation.finrank_residueImageField_eq_quotient_ker
statement: formalized
proof: formalized
---

# 90.3 The base category

Section 90.3 of the Stacks Project, [Tag 06GB](https://stacks.math.columbia.edu/tag/06GB). 15 tags here are carried by 37 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06GC, a definition

[Tag 06GC](https://stacks.math.columbia.edu/tag/06GC) in the Stacks Project.

**`Deformation.ArtinianLocalAlgCat`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L170). The attribute's comment: “objects”. References: SGA 7 VI (1.15), “objects, K a field”.

> An Artinian local `Λ`-algebra together with a specified `Λ`-algebra isomorphism from
> its residue field to `k`. These are the objects of the category `𝒞_Λ` of Stacks Project,
> Tag 06GC.

```lean
structure ArtinianLocalAlgCat (Λ : Type u) (k : Type w) [CommRing Λ] [Field k]
    [Algebra Λ k]
```

**`Deformation.ArtinianLocalAlgCat.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L196). The attribute's comment: “morphisms”. References: SGA 7 VI (1.15), “morphisms, K a field”.

> A morphism of Artinian local `Λ`-algebras with fixed residue field is a local
> `Λ`-algebra homomorphism whose induced map on residue fields respects the specified
> identifications with `k`.

```lean
structure Hom (A B : ArtinianLocalAlgCat.{u, v, w} Λ k)
```

**`Deformation.ArtinianLocalAlgCat.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L218). The attribute's comment: “category structure”.

> The category structure on Artinian local `Λ`-algebras with the fixed residue field `k`.
> Composition is composition of the underlying local algebra homomorphisms.

```lean
instance instCategory : Category (ArtinianLocalAlgCat.{u, v, w} Λ k)
```

**`Deformation.IsClassical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L275). The attribute's comment: “classical case”.

> The classical case of `𝒞_Λ`: `Λ` is a Noetherian complete local ring and the given
> `Λ`-algebra `k` is its residue field.

```lean
def IsClassical (Λ : Type u) (k : Type w) [CommRing Λ] [Field k] [Algebra Λ k] : Prop
```

## Tag 06GD, a definition

[Tag 06GD](https://stacks.math.columbia.edu/tag/06GD) in the Stacks Project.

Declarations registered for the tag:

- [`InfinitesimalLifting.IsSmallExtension`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Smooth/InfinitesimalLifting.lean#L129), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/Basic.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L286) (StacksFrontier).

## Tag 06GE, a lemma

[Tag 06GE](https://stacks.math.columbia.edu/tag/06GE) in the Stacks Project.

**`Deformation.surjective_factors_into_smallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L535).

> A surjective morphism in `\mathcal{C}_\Lambda` is a finite composite of small
> extensions.

```lean
theorem surjective_factors_into_smallExtensions
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A)
    (hf : Function.Surjective f.hom) :
    ∃ (n : ℕ) (F : ComposableArrows (ArtinianLocalAlgCat.{u, v, w} Λ k) n)
      (hB : F.left = B) (e : F.right ≅ A),
      eqToHom hB.symm ≫ F.hom ≫ e.hom = f ∧
        ∀ (i : ℕ) (hi : i < n),
          InfinitesimalLifting.IsSmallExtension
            (CommRingCat.ofHom (F.map' i (i + 1)).hom.toRingHom)
```

## Tag 06S2, an equation

[Tag 06S2](https://stacks.math.columbia.edu/tag/06S2) in the Stacks Project.

**`Deformation.residueImageField_eq_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 831](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L831). The attribute's comment: “the image is a field”.

> For a finite map to a field, the subfield generated by its image has
> underlying set equal to the image itself.

```lean
theorem residueImageField_eq_range (Λ : Type u) (k : Type v) [CommRing Λ]
    [IsNoetherianRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k] :
    (residueImageField Λ k : Set k) = Set.range (algebraMap Λ k)
```

**`Deformation.finrank_residueImageField_eq_quotient_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 847](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L847). The attribute's comment: “the equality of degrees”.

> The degrees of `k` over the image field and over the quotient of `Λ` by the kernel of its
> structural map agree.

```lean
theorem finrank_residueImageField_eq_quotient_ker
    (Λ : Type u) (k : Type v) [CommRing Λ] [IsNoetherianRing Λ]
    [Field k] [Algebra Λ k] [Module.Finite Λ k] :
    let f : Λ →+* k := algebraMap Λ k
    let e : Λ ⧸ RingHom.ker f ≃+* RingHom.range f :=
      RingHom.quotientKerEquivRange f
    letI : Field f.range := (range_isField Λ k).toField
    letI : Field (Λ ⧸ RingHom.ker f) :=
      ((e.toMulEquiv.isField_congr).mpr (Field.toIsField f.range)).toField
    let q : Λ ⧸ RingHom.ker f →+* k :=
      (Subring.subtype (RingHom.range f)).comp e.toRingHom
    letI : Algebra (Λ ⧸ RingHom.ker f) k := q.toAlgebra
    Module.finrank (residueImageField Λ k) k =
      Module.finrank (Λ ⧸ RingHom.ker f) k
```

**`Deformation.residueImageField_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 887](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L887). The attribute's comment: “finiteness of the degree”.

> **Stacks Project, Tag 06S2.** The extension of `k` over the image field of
> a finite ring map is finite.

```lean
theorem residueImageField_finite
    (Λ : Type u) (k : Type v) [CommRing Λ] [IsNoetherianRing Λ]
    [Field k] [Algebra Λ k] [Module.Finite Λ k] :
    Module.Finite (residueImageField Λ k) k
```

## Tag 06GG, a lemma

[Tag 06GG](https://stacks.math.columbia.edu/tag/06GG) in the Stacks Project.

**`Deformation.finrank_residueImageField_mul_length_eq_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 959](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L959). The attribute's comment: “general case”.

> **Stacks Project, Tag 06GG.** Restricting scalars from a local `Λ`-algebra
> with residue field `k` to `Λ` multiplies module length by the degree of `k` over
> the image field of `Λ`.

```lean
theorem finrank_residueImageField_mul_length_eq_length
    (Λ : Type u) (k : Type w) (A : Type v) (M : Type x)
    [CommRing Λ] [IsNoetherianRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    [CommRing A] [Algebra Λ A] [IsLocalRing A]
    [AddCommGroup M] [Module A M]
    (_ : ResidueField A ≃ₐ[Λ] k) :
    letI : Module Λ M := Module.compHom M (algebraMap Λ A)
    (Module.finrank (residueImageField Λ k) k : ℕ∞) * Module.length A M =
      Module.length Λ M
```

**`Deformation.length_eq_length_of_isClassical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 995](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L995). The attribute's comment: “classical case”.

> **Stacks Project, Tag 06GG.** In the classical case, module length is unchanged
> by restriction of scalars from a local `Λ`-algebra with residue field `k` to `Λ`.

```lean
theorem length_eq_length_of_isClassical
    (Λ : Type u) (k : Type w) (A : Type v) (M : Type x)
    [CommRing Λ] [IsNoetherianRing Λ] [Field k] [Algebra Λ k] [Module.Finite Λ k]
    [CommRing A] [Algebra Λ A] [IsLocalRing A]
    [AddCommGroup M] [Module A M]
    (_ : ResidueField A ≃ₐ[Λ] k) (h : IsClassical Λ k) :
    letI : Module Λ M := Module.compHom M (algebraMap Λ A)
    Module.length A M = Module.length Λ M
```

## Tag 06S3, a lemma

[Tag 06S3](https://stacks.math.columbia.edu/tag/06S3) in the Stacks Project.

**`Deformation.ArtinianLocalAlgCat.surjective_hom_iff_surjective_cotangentMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean#L296). The attribute's comment: “conditions (1) and (2), on the conormal module of a presentation”.

> The criterion of [Stacks, Tag 06S3] for surjectivity, read on the conormal modules of the
> presentations `residueExt B` and `residueExt A`: a morphism of `𝒞_Λ` is surjective exactly when
> the map it induces on `𝔪/𝔪²` is surjective.

```lean
theorem surjective_hom_iff_surjective_cotangentMap (f : B ⟶ A) :
    Function.Surjective f.hom ↔
      Function.Surjective (Algebra.Extension.Cotangent.map (residueExtHom f))
```

**`Deformation.ArtinianLocalAlgCat.surjective_iff_cotangentSpaceMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 1140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L1140). The attribute's comment: “conditions (1) and (2)”.

> A morphism of Artinian local algebras is surjective exactly when its canonical map
> `m_A / m_A² → m_B / m_B²` is surjective.

```lean
public theorem surjective_iff_cotangentSpaceMap_surjective
    {A B : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : A ⟶ B) :
    Function.Surjective f.hom ↔
      Function.Surjective
        (Ideal.mapCotangent (maximalIdeal A) (maximalIdeal B) f.hom
          (by
            let _ : IsLocalHom f.hom.toRingHom := f.isLocal
            intro x hx
            change x ∈ (maximalIdeal B).comap f.hom.toRingHom
            simpa only [maximalIdeal_comap] using hx))
```

**`Deformation.ArtinianLocalAlgCat.cotangentSpaceMap_surjective_iff_relativeCotangentSpaceMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 1187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L1187). The attribute's comment: “conditions (2) and (3)”.

> Surjectivity on `m / m²` is equivalent to surjectivity after also quotienting by the
> extension of the maximal ideal of the base.

```lean
public theorem cotangentSpaceMap_surjective_iff_relativeCotangentSpaceMap_surjective
    {A B : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : A ⟶ B) :
    Function.Surjective
        (Ideal.mapCotangent (maximalIdeal A) (maximalIdeal B) f.hom
          (by
            let _ : IsLocalHom f.hom.toRingHom := f.isLocal
            intro x hx
            change x ∈ (maximalIdeal B).comap f.hom.toRingHom
            simpa only [maximalIdeal_comap] using hx)) ↔
      Function.Surjective (relativeCotangentSpaceMap f)
```

## Tag 06GY, a definition

[Tag 06GY](https://stacks.math.columbia.edu/tag/06GY) in the Stacks Project.

**`Deformation.relativeCotangentSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 776](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L776). References: SGA 1 III (2.2).

> The relative cotangent space of a local homomorphism `f : R → S`, namely
> `m_S / (m_R S + m_S²)`.

```lean
abbrev relativeCotangentSpace
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    [IsLocalRing R] [IsLocalRing S] (f : R →+* S) [IsLocalHom f] : Type v
```

## Tag 06GH, a lemma

[Tag 06GH](https://stacks.math.columbia.edu/tag/06GH) in the Stacks Project.

**`Deformation.ArtinianLocalAlgCat.hasPullback_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/FibreProduct.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/FibreProduct.lean#L431). The attribute's comment: “surjective\_fiber\_product\_in\_clambda”.

> If either morphism is surjective, the ring of compatible pairs is a pullback in `𝒞_Λ`; in
> particular the pullback exists.

```lean
theorem hasPullback_of_surjective (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A)
    (h : Function.Surjective f₁.hom ∨ Function.Surjective f₂.hom) :
    IsConcretePullback f₁ f₂ ∧ HasPullback f₁ f₂
```

**`Deformation.ArtinianLocalAlgCat.isConcretePullback_of_isSeparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/FibreProductSeparable.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/FibreProductSeparable.lean#L173). The attribute's comment: “separable\_fiber\_product\_in\_clambda”.

> The algebraic fibre product has its canonical object structure in `𝒞_Λ`
> when `k` is separable over the image field of `Λ`.

```lean
theorem isConcretePullback_of_isSeparable
    [Algebra.IsSeparable (residueImageField Λ k) k]
    {A₁ A₂ A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A) :
    IsConcretePullback f₁ f₂
```

**`Deformation.ArtinianLocalAlgCat.isSmallExtension_pullback_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/SmallExtensionPullback.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/SmallExtensionPullback.lean#L167). The attribute's comment: “pullback\_small\_extension”.

> The first projection from the pullback of a small extension in `𝒞_Λ` is a small
> extension.

```lean
theorem isSmallExtension_pullback_fst
    {A₁ A₂ A : ArtinianLocalAlgCat.{u, v, w} Λ k}
    (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A) [Limits.HasPullback f₁ f₂]
    (h₂ : IsSmallExtension (CommRingCat.ofHom f₂.hom.toRingHom)) :
    IsSmallExtension
      (CommRingCat.ofHom (Limits.pullback.fst f₁ f₂).hom.toRingHom)
```

## Tag 06GF, a definition

[Tag 06GF](https://stacks.math.columbia.edu/tag/06GF) in the Stacks Project.

**`Deformation.IsEssentialSurjection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L301).

> A surjective morphism in `𝒞_Λ` is essential if, whenever its composite with a
> morphism into its source is surjective, that morphism is already surjective.

```lean
abbrev IsEssentialSurjection
    {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A) : Prop
```

## Tag 06S5, a lemma

[Tag 06S5](https://stacks.math.columbia.edu/tag/06S5) in the Stacks Project.

**`Deformation.ArtinianLocalAlgCat.essentialSurjection_iff_mod_maximalIdeal_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjection.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjection.lean#L265). The attribute's comment: “conditions (1) and (2)”.

> Essential surjectivity is detected modulo the maximal-ideal squares.

```lean
theorem essentialSurjection_iff_mod_maximalIdeal_sq
    {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A) :
    let IB := maximalIdeal B ^ 2
    let IA := maximalIdeal A ^ 2
    let hB : IB ≤ maximalIdeal B := Ideal.pow_le_self (by omega : 2 ≠ 0)
    let hA : IA ≤ maximalIdeal A := Ideal.pow_le_self (by omega : 2 ≠ 0)
    let hmap : IB ≤ IA.comap f.hom := by
      let _ : IsLocalHom f.hom.toRingHom := f.isLocal
      rw [← Ideal.map_le_iff_le_comap, Ideal.map_pow]
      exact Ideal.pow_right_mono (map_maximalIdeal_le f.hom.toRingHom) _
    IsEssentialSurjection f ↔
    IsEssentialSurjection (idealQuotientMap f IB IA hB hA hmap)
```

**`Deformation.ArtinianLocalAlgCat.essentialSurjection_iff_mod_relative_maximalIdeal_sq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjection.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjection.lean#L285). The attribute's comment: “conditions (1) and (3)”.

> Essential surjectivity is detected on the relative cotangent quotient.

```lean
theorem essentialSurjection_iff_mod_relative_maximalIdeal_sq
    {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A) :
    IsEssentialSurjection f ↔
      IsEssentialSurjection
        (idealQuotientMap f
          ((RingHom.ker (algebraMap Λ k)).map (algebraMap Λ B) + maximalIdeal B ^ 2)
          ((RingHom.ker (algebraMap Λ k)).map (algebraMap Λ A) + maximalIdeal A ^ 2)
          (relativeCotangentIdeal_le_maximalIdeal B)
          (relativeCotangentIdeal_le_maximalIdeal A)
          (relativeCotangentIdeal_le_comap f))
```

## Tag 06S6, an equation

[Tag 06S6](https://stacks.math.columbia.edu/tag/06S6) in the Stacks Project.

Declarations registered for the tag:

- [`KaehlerDifferential.kerCotangentToTensor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=KaehlerDifferential.kerCotangentToTensor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch90.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch90.lean#L21) (StacksFrontier): “the map m\_A/m\_A² → k ⊗\_A Ω\_\{A/Λ}”. References: EGA 0 (20.5.11); EGA 0 (20.5.12); EGA 0 (22.2.9); EGA 0 (22.6.4), “partial”; EGA IV (17.15.9); SGA 1 II (5.9).
- [`KaehlerDifferential.mapBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=KaehlerDifferential.mapBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch90.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch90.lean#L22) (StacksFrontier): “the map k ⊗\_A Ω\_\{A/Λ} → Ω\_\{k/Λ}”. References: EGA 0 (20.5.2); EGA 0 (20.5.4), “special case”; EGA 0 (20.5.7); EGA 0 (20.6.5), “differential K₁ → K₀”.
- [`KaehlerDifferential.exact_kerCotangentToTensor_mapBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=KaehlerDifferential.exact_kerCotangentToTensor_mapBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch90.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch90.lean#L23) (StacksFrontier): “exactness at k ⊗\_A Ω\_\{A/Λ}”. References: EGA 0 (20.5.12), “partial”; EGA 0 (20.6.23), “partial”; EGA 0 (22.4.8), “partial”; EGA IV (16.4.21), “special case”; EGA IV (17.2.5), “affine middle exactness”.
- [`KaehlerDifferential.mapBaseChange_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=KaehlerDifferential.mapBaseChange_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch90.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch90.lean#L25) (StacksFrontier): “exactness at Ω\_\{k/Λ} (→ 0)”. References: EGA IV (17.13.1), “special case”.

## Tag 06S7, an equation

[Tag 06S7](https://stacks.math.columbia.edu/tag/06S7) in the Stacks Project.

**`Deformation.exact_cotangentSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/CotangentSequence.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/CotangentSequence.lean#L142). References: EGA 0 (20.6.22), “last three terms”.

> **Stacks 06S7.** Let `Λ` be a ring, `k` a field and `A` a `Λ`-algebra with a `Λ`-algebra
> surjection `A → k` with kernel `𝔪_A`. Then the four-term sequence
>
>     H₁(L_{k/Λ}) ⟶ 𝔪_A/𝔪_A² ⟶ Ω_{A/Λ} ⊗_A k ⟶ Ω_{k/Λ} ⟶ 0
>
> is exact: exact at `𝔪_A/𝔪_A²`, exact at `Ω_{A/Λ} ⊗_A k`, and surjective onto `Ω_{k/Λ}`.

```lean
public theorem exact_cotangentSequence (h : Function.Surjective (algebraMap A k)) :
    Function.Exact (h1CotangentToCotangent Λ h)
        (KaehlerDifferential.kerCotangentToTensor Λ A k) ∧
      Function.Exact (KaehlerDifferential.kerCotangentToTensor Λ A k)
        (KaehlerDifferential.mapBaseChange Λ A k) ∧
      Function.Surjective (KaehlerDifferential.mapBaseChange Λ A k)
```

## Tag 06S8, an equation

[Tag 06S8](https://stacks.math.columbia.edu/tag/06S8) in the Stacks Project.

**`Deformation.cotangentMap_comp_h1CotangentToConormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean#L144). The attribute's comment: “left square, for the canonical map through the universal presentation”.

> **Stacks 06S8**, left square. The two arrows out of `H₁(L_{k/Λ})` agree: pushing a class
> into `𝔪_B/𝔪_B²` and then along `B → A` gives its image in `𝔪_A/𝔪_A²`.
>
> The source leaves this horizontal arrow unlabelled. It is realized here as
> `Deformation.h1CotangentToConormal`, the canonical map through the universal presentation of `k`
> over `Λ`. The square for the other realization of that arrow, the one used in the four-term exact
> sequence of [Stacks, Tag 06S7], is `Deformation.mapCotangent_h1CotangentToCotangent`; the two
> realizations are not compared to each other, which is why the scope label names this one.

```lean
public theorem cotangentMap_comp_h1CotangentToConormal :
    Algebra.Extension.Cotangent.map (residueExtensionHom (Λ := Λ) hB hA) ∘ₗ
        h1CotangentToConormal (residueExtension Λ hB) =
      h1CotangentToConormal (residueExtension Λ hA)
```

**`Deformation.cotangentSpaceMap_comp_cotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean#L163). The attribute's comment: “middle square”.

> **Stacks 06S8**, middle square. The differentials `d_B : 𝔪_B/𝔪_B² → k ⊗_B Ω_{B/Λ}` and
> `d_A : 𝔪_A/𝔪_A² → k ⊗_A Ω_{A/Λ}` are compatible with the maps induced by `B → A`.

```lean
public theorem cotangentSpaceMap_comp_cotangentComplex :
    Algebra.Extension.CotangentSpace.map (residueExtensionHom (Λ := Λ) hB hA) ∘ₗ
        (residueExtension Λ hB).cotangentComplex =
      (residueExtension Λ hA).cotangentComplex ∘ₗ
        Algebra.Extension.Cotangent.map (residueExtensionHom (Λ := Λ) hB hA)
```

**`Deformation.toKaehler_comp_cotangentSpaceMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean#L174). The attribute's comment: “right square”.

> **Stacks 06S8**, right square. The two arrows into `Ω_{k/Λ}` agree: the projection of
> `k ⊗_B Ω_{B/Λ}` onto `Ω_{k/Λ}` factors through `k ⊗_A Ω_{A/Λ}` along `B → A`.

```lean
public theorem toKaehler_comp_cotangentSpaceMap :
    (residueExtension Λ hA).toKaehler ∘ₗ
        Algebra.Extension.CotangentSpace.map (residueExtensionHom (Λ := Λ) hB hA) =
      (residueExtension Λ hB).toKaehler
```

**`Deformation.mapCotangent_h1CotangentToCotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/JacobiZariskiFunctoriality.lean#L239). The attribute's comment: “left square, for the arrow of the four-term sequence of 06S7”.

> **Stacks 06S8**, left square, for the arrow `H₁(L_{k/Λ}) → 𝔪/𝔪²` of the four-term exact
> sequence of [Stacks, Tag 06S7]: pushing a class of `H₁(L_{k/Λ})` into `𝔪_B/𝔪_B²` and then
> along `𝔪_B → 𝔪_A` gives its image in `𝔪_A/𝔪_A²`.

```lean
public theorem mapCotangent_h1CotangentToCotangent (x : Algebra.H1Cotangent Λ k) :
    Ideal.mapCotangent (RingHom.ker (algebraMap B k)) (RingHom.ker (algebraMap A k))
        (Algebra.ofId B A)
        (ker_algebraMap_le_comap_ker (Λ := B) (S := k) (k := k) (A := A))
        (h1CotangentToCotangent Λ hB x) =
      h1CotangentToCotangent Λ hA x
```

## Tag 06S9, a lemma

[Tag 06S9](https://stacks.math.columbia.edu/tag/06S9) in the Stacks Project.

**`Deformation.conormalToH1Cotangent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean#L230). The attribute's comment: “canonical map”.

> **Stacks 06S9.** The canonical map `𝔪_Λ/𝔪_Λ² → H₁(L_{k/Λ})`, for `k'` the subfield of `k`
> generated by the image of `Λ`, presented as a field `S` with `Λ → S` surjective and `S → k` an
> extension: the conormal module of `Λ → S` maps to `H₁(L_{S/Λ})` and then to `H₁(L_{k/Λ})`.

```lean
public noncomputable def conormalToH1Cotangent
    (h : Function.Surjective (algebraMap Λ S)) :
    (RingHom.ker (algebraMap Λ S)).Cotangent →ₗ[Λ] Algebra.H1Cotangent Λ k
```

**`Deformation.conormalToH1Cotangent_baseChange_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean#L325). The attribute's comment: “separable case”.

> **Stacks 06S9.** When `k` is separable over the image field `S = k'`, the canonical map
> induces an isomorphism `𝔪_Λ/𝔪_Λ² ⊗_{k'} k = H₁(L_{k/Λ})`. The base change is written over `Λ`,
> which is the same thing: the conormal module of `Λ → S` is annihilated by its kernel, hence is
> a module over `Λ/𝔪_Λ = k'`.

```lean
public theorem conormalToH1Cotangent_baseChange_bijective
    (h : Function.Surjective (algebraMap Λ S))
    [Algebra.IsSeparable S k] :
    Function.Bijective
      ((conormalToH1Cotangent (Λ := Λ) (S := S) (k := k) h).liftBaseChange k)
```

**`Deformation.conormalToH1Cotangent_bijective_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean#L353). The attribute's comment: “classical case”.

> **Stacks 06S9.** In the classical case `k = k'`, that is `Λ → k` surjective, the canonical
> map `𝔪_Λ/𝔪_Λ² → H₁(L_{k/Λ})` is itself an isomorphism.

```lean
public theorem conormalToH1Cotangent_bijective_of_surjective
    (h : Function.Surjective (algebraMap Λ k)) :
    Function.Bijective
      (conormalToH1Cotangent (Λ := Λ) (S := k) (k := k) h)
```

**`Deformation.conormalToH1Cotangent_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/CotangentHomology.lean#L390). The attribute's comment: “compatibility with the conormal map”.

> **Stacks 06S9.** The composite `𝔪_Λ/𝔪_Λ² → H₁(L_{k/Λ}) → H₁(L_{k/A})` is the map induced
> by the structural map `𝔪_Λ → 𝔪_A`: for `A` with `Λ → A → k` and `A → k` surjective, pushing a
> class of `𝔪_Λ/𝔪_Λ²` forward to `H₁(L_{k/A})` agrees with taking its image in `𝔪_A/𝔪_A²` and
> applying the canonical map of `A → k`. Since the canonical map of `A → k` is an isomorphism by
> `conormalToH1Cotangent_bijective_of_surjective`, this identifies the composite
> `𝔪_Λ/𝔪_Λ² → H₁(L_{k/Λ}) → 𝔪_A/𝔪_A²` of the source.

```lean
public theorem conormalToH1Cotangent_comp
    {A : Type*} [CommRing A] [Algebra Λ A] [Algebra A k]
    [IsScalarTower Λ A k]
    (h : Function.Surjective (algebraMap Λ S))
    (hg : Function.Surjective (algebraMap A k))
    (x : (RingHom.ker (algebraMap Λ S)).Cotangent) :
    Algebra.H1Cotangent.map Λ A k k
        (conormalToH1Cotangent (Λ := Λ) (S := S) (k := k) h x) =
      conormalToH1Cotangent (Λ := A) (S := k) (k := k) hg
        (Ideal.mapCotangent (RingHom.ker (algebraMap Λ S))
          (RingHom.ker (algebraMap A k)) (Algebra.ofId Λ A)
          (ker_algebraMap_le_comap_ker (Λ := Λ) (S := S) (k := k) (A := A)) x)
```

## Tag 06H0, a lemma

[Tag 06H0](https://stacks.math.columbia.edu/tag/06H0) in the Stacks Project.

**`Deformation.ArtinianLocalAlgCat.isEssentialSurjection_iff_bijective_differentialsBaseChangeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityEssentialSurjection.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Artin/Obstruction/NaiveVersalityEssentialSurjection.lean#L187). The attribute's comment: “part (2), conditions (a) and (c), through the base-change map of differentials”.

> **Stacks 06H0, part (2), conditions (a) and (c)**, with the cotangent space written as the
> base-change map of differentials. A morphism `f : B ⟶ A` of `𝒞_Λ` is an essential surjection
> exactly when the canonical map `k ⊗_B Ω_{B/Λ} ⟶ k ⊗_A Ω_{A/Λ}` is bijective.
>
> This is
> `Deformation.ArtinianLocalAlgCat.isEssentialSurjection_iff_cotangentSpaceMap_bijective`
> composed with `Deformation.Artin.differentialsBaseChangeMap_eq_cotangentSpaceMap`. It is the
> form in which the criterion meets Stacks 07YL, which produces its square-zero extension
> together with the bijectivity of exactly this map.

```lean
public theorem isEssentialSurjection_iff_bijective_differentialsBaseChangeMap
    {B A : ArtinianLocalAlgCat.{u, u, u} Λ k} (f : B ⟶ A) :
    letI : Algebra (B : Type u) (A : Type u) := f.hom.toRingHom.toAlgebra
    letI : IsScalarTower Λ (B : Type u) (A : Type u) :=
      .of_algebraMap_eq fun x => (f.hom.commutes x).symm
    letI : IsScalarTower (B : Type u) (A : Type u) k :=
      .of_algebraMap_eq fun b => (f.residue_comm b).symm
    (IsEssentialSurjection f ↔
      Function.Bijective
        (Deformation.Artin.differentialsBaseChangeMap Λ (B : Type u) (A : Type u) k))
```

**`Deformation.ArtinianLocalAlgCat.surjective_iff_imageDMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean#L723). The attribute's comment: “part (1)(a), the image of the differential”.

> **Stacks 06H0**, part (1)(a). A morphism `f : B ⟶ A` of `𝒞_Λ` is surjective — equivalently,
> satisfies the conditions of [Stacks, Tag 06S3] — exactly when `Im(d_B) → Im(d_A)` is
> surjective.

```lean
theorem surjective_iff_imageDMap_surjective (f : B ⟶ A) :
    Function.Surjective f.hom ↔ Function.Surjective (imageDMap f)
```

**`Deformation.ArtinianLocalAlgCat.surjective_iff_cotangentSpaceMap_residueExtHom_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean, line 751](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean#L751). The attribute's comment: “part (1)(b), the cotangent space”.

> **Stacks 06H0**, part (1)(b). A morphism `f : B ⟶ A` of `𝒞_Λ` is surjective — equivalently,
> satisfies the conditions of [Stacks, Tag 06S3] — exactly when
> `Ω_{B/Λ} ⊗_B k → Ω_{A/Λ} ⊗_A k` is surjective.

```lean
theorem surjective_iff_cotangentSpaceMap_residueExtHom_surjective (f : B ⟶ A) :
    Function.Surjective f.hom ↔
      Function.Surjective (Algebra.Extension.CotangentSpace.map (residueExtHom f))
```

**`Deformation.ArtinianLocalAlgCat.imageDMap_bijective_iff_cotangentSpaceMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean, line 761](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean#L761). The attribute's comment: “part (2), conditions (b) and (c)”.

> **Stacks 06H0**, part (2), equivalence of conditions (b) and (c). For a morphism of `𝒞_Λ`
> the map `Im(d_B) → Im(d_A)` is an isomorphism exactly when
> `Ω_{B/Λ} ⊗_B k → Ω_{A/Λ} ⊗_A k` is one.

```lean
theorem imageDMap_bijective_iff_cotangentSpaceMap_bijective (f : B ⟶ A) :
    Function.Bijective (imageDMap f) ↔
      Function.Bijective (Algebra.Extension.CotangentSpace.map (residueExtHom f))
```

**`Deformation.ArtinianLocalAlgCat.isEssentialSurjection_iff_cotangentSpaceMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean, line 832](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean#L832). The attribute's comment: “part (2), conditions (a) and (c)”.

> **Stacks 06H0**, part (2), equivalence of conditions (a) and (c). A morphism of `𝒞_Λ` is an
> essential surjection exactly when `Ω_{B/Λ} ⊗_B k → Ω_{A/Λ} ⊗_A k` is an isomorphism.

```lean
theorem isEssentialSurjection_iff_cotangentSpaceMap_bijective (f : B ⟶ A) :
    IsEssentialSurjection f ↔
      Function.Bijective (Algebra.Extension.CotangentSpace.map (residueExtHom f))
```

**`Deformation.ArtinianLocalAlgCat.isEssentialSurjection_iff_imageDMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean, line 841](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean#L841). The attribute's comment: “part (2), conditions (a) and (b)”.

> **Stacks 06H0**, part (2), equivalence of conditions (a) and (b). A morphism of `𝒞_Λ` is an
> essential surjection exactly when `Im(d_B) → Im(d_A)` is an isomorphism.

```lean
theorem isEssentialSurjection_iff_imageDMap_bijective (f : B ⟶ A) :
    IsEssentialSurjection f ↔ Function.Bijective (imageDMap f)
```

**`Deformation.ArtinianLocalAlgCat.isEssentialSurjection_iff_relativeCotangentSpaceMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/BaseCategory/EssentialSurjectionDifferential.lean#L1012). The attribute's comment: “part (3), separable case”.

> **Stacks 06H0**, part (3). If `k` is separable over the image field `k'` — presented as a
> field `S` with `Λ → S` surjective and `S → k` separable — then a morphism `f : B ⟶ A` of `𝒞_Λ`
> is an essential surjection exactly when
> `𝔪_B/(𝔪_Λ B + 𝔪_B²) → 𝔪_A/(𝔪_Λ A + 𝔪_A²)` is an isomorphism.
>
> In that case `Im(d_A) = 𝔪_A/(𝔪_Λ A + 𝔪_A²)` for every object `A`, by
> `cotangentComplex_mk_eq_zero_of_mem_relative` and
> `mem_relative_of_cotangentComplex_mk_eq_zero`, and the statement follows from part (2). Only
> the forward implication uses separability: the converse is
> `isEssentialSurjection_of_relativeCotangentSpaceMap_bijective`.

```lean
theorem isEssentialSurjection_iff_relativeCotangentSpaceMap_bijective
    {S : Type*} [Field S] [Algebra Λ S] [Algebra S k] [IsScalarTower Λ S k]
    (hS : Function.Surjective (algebraMap Λ S)) [Algebra.IsSeparable S k] (f : B ⟶ A) :
    IsEssentialSurjection f ↔ Function.Bijective (relativeCotangentSpaceMap f)
```

**`Deformation.not_isEssentialSurjection_iff_exists_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Basic.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Basic.lean#L639). The attribute's comment: “small\_extension\_section”.

> A small extension in `𝒞_Λ` is nonessential if and only if it has a section in
> `𝒞_Λ`.

```lean
theorem not_isEssentialSurjection_iff_exists_section
    {B A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : B ⟶ A)
    (hf : InfinitesimalLifting.IsSmallExtension
      (CommRingCat.ofHom f.hom.toRingHom)) :
    ¬ IsEssentialSurjection f ↔ ∃ s : A ⟶ B, s ≫ f = 𝟙 A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.3, Tag 06GB](https://stacks.math.columbia.edu/tag/06GB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
