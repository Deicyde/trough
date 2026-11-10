---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsQuasiAffineHom, AlgebraicGeometry.isSeparated_of_isQuasiAffineHom, AlgebraicGeometry.quasiCompact_of_isQuasiAffineHom, AlgebraicGeometry.isQuasiAffineHom_iff_toSpecΓ, AlgebraicGeometry.isQuasiAffineHom_iff_exists_isOpenCover, AlgebraicGeometry.isQuasiAffineHom_iff_canonicalMorphism, AlgebraicGeometry.isOpenImmersion_canonicalMorphism, AlgebraicGeometry.quasiCompact_canonicalMorphism
statement: formalized
proof: formalized
---

# 29.13 Quasi-affine morphisms

Section 29.13 of the Stacks Project, [Tag 01SJ](https://stacks.math.columbia.edu/tag/01SJ). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01SK, a definition

[Tag 01SK](https://stacks.math.columbia.edu/tag/01SK) in the Stacks Project.

**`AlgebraicGeometry.IsQuasiAffineHom`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean#L47).

> A morphism of schemes is quasi-affine if the inverse image of every affine open subscheme of
> the target is a quasi-affine scheme.

```lean
class IsQuasiAffineHom {X S : Scheme} (f : X ⟶ S) : Prop
```

## Tag 01SL, a lemma

[Tag 01SL](https://stacks.math.columbia.edu/tag/01SL) in the Stacks Project.

**`AlgebraicGeometry.isSeparated_of_isQuasiAffineHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean#L52). The attribute's comment: “separated”. References: EGA II (1.2.4), “more general”; EGA II (5.1.6), “partial”.

> A quasi-affine morphism of schemes is separated.

```lean
instance isSeparated_of_isQuasiAffineHom {X S : Scheme.{u}} (f : X ⟶ S)
    [IsQuasiAffineHom f] : IsSeparated f
```

**`AlgebraicGeometry.quasiCompact_of_isQuasiAffineHom`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean#L66). The attribute's comment: “quasi-compact”.

> A quasi-affine morphism of schemes is quasi-compact.

```lean
instance quasiCompact_of_isQuasiAffineHom {X S : Scheme.{u}} (f : X ⟶ S)
    [IsQuasiAffineHom f] : QuasiCompact f
```

## Tag 01SM, a lemma

[Tag 01SM](https://stacks.math.columbia.edu/tag/01SM) in the Stacks Project.

**`AlgebraicGeometry.isQuasiAffineHom_iff_toSpecΓ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatBaseChange.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiAffineFlatBaseChange.lean#L140). The attribute's comment: “(4) over an affine base”. References: EGA II (5.1.6), “(a)<=>(b), affine base”; EGA II (5.1.8).

> **Stacks Project, Tag 01SM, part (4), over an affine base.** A morphism to an affine scheme
> is quasi-affine if and only if the canonical morphism from its source to the spectrum of its
> global sections — the relative spectrum of the pushforward of the structure sheaf — is a
> quasi-compact open immersion.

```lean
theorem isQuasiAffineHom_iff_toSpecΓ [IsAffine S] (f : X ⟶ S) :
    IsQuasiAffineHom f ↔ IsOpenImmersion X.toSpecΓ ∧ QuasiCompact X.toSpecΓ
```

**`AlgebraicGeometry.isQuasiAffineHom_iff_exists_isOpenCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineLocal.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineLocal.lean#L154). The attribute's comment: “(1) ↔ (2)”. References: EGA II (5.1.1).

> A morphism of schemes is quasi-affine if and only if there exists an affine open covering of
> the target all of whose members have quasi-affine inverse image.

```lean
theorem isQuasiAffineHom_iff_exists_isOpenCover {X S : Scheme.{u}} (f : X ⟶ S) :
    IsQuasiAffineHom f ↔ ∃ (ι : Type u) (U : ι → S.affineOpens),
      IsOpenCover (fun i ↦ (U i : S.Opens)) ∧
        ∀ i, Scheme.IsQuasiAffine (f ⁻¹ᵁ (U i : S.Opens)).toScheme
```

**`AlgebraicGeometry.isQuasiAffineHom_iff_canonicalMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean#L140). The attribute's comment: “(1) ↔ (4) over a general base, carrying the quasi-compact and quasi-separated hypotheses that make `f_* 𝒪_X` quasi-coherent”. References: EGA II (5.1.2), “more general”; EGA II (5.1.6).

> A morphism of schemes which is quasi-compact and quasi-separated — so that `f_* 𝒪_X` is a
> quasi-coherent sheaf of `𝒪_S`-algebras and the canonical morphism `X ⟶ Spec_S(f_* 𝒪_X)` exists —
> is quasi-affine if and only if that canonical morphism is a quasi-compact open immersion.

```lean
theorem isQuasiAffineHom_iff_canonicalMorphism :
    IsQuasiAffineHom f ↔
      IsOpenImmersion (canonicalMorphism f) ∧ QuasiCompact (canonicalMorphism f)
```

**`AlgebraicGeometry.isOpenImmersion_canonicalMorphism`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean#L161). The attribute's comment: “(1) ⇒ (4), the open-immersion half”.

> The canonical morphism from the source of a quasi-affine morphism to the relative spectrum of
> the pushed-forward structure sheaf is an open immersion.

```lean
instance isOpenImmersion_canonicalMorphism (f : X ⟶ S) [IsQuasiAffineHom f] :
    IsOpenImmersion (canonicalMorphism f)
```

**`AlgebraicGeometry.quasiCompact_canonicalMorphism`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean#L168). The attribute's comment: “(1) ⇒ (4), the quasi-compactness half”.

> The canonical morphism from the source of a quasi-affine morphism to the relative spectrum of
> the pushed-forward structure sheaf is quasi-compact.

```lean
instance quasiCompact_canonicalMorphism (f : X ⟶ S) [IsQuasiAffineHom f] :
    QuasiCompact (canonicalMorphism f)
```

**`AlgebraicGeometry.isQuasiAffineHom_iff_exists_relativeSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineRelativeSpec.lean#L175). The attribute's comment: “(1) ↔ (3) over a general base, no hypotheses”.

> A morphism of schemes `f : X ⟶ S` is quasi-affine if and only if there is a quasi-coherent
> sheaf `A` of `𝒪_S`-algebras and a quasi-compact open immersion `X ⟶ Spec_S(A)` over `S`.

```lean
theorem isQuasiAffineHom_iff_exists_relativeSpec (f : X ⟶ S) :
    IsQuasiAffineHom f ↔
      ∃ (A : AlgebraSheaf S) (hA : AlgebraSheaf.IsQuasicoherent A)
        (g : X ⟶ @relativeSpec S A hA),
        IsOpenImmersion g ∧ QuasiCompact g ∧ g ≫ @relativeSpecToBase S A hA = f
```

**`AlgebraicGeometry.isQuasiAffineHom_iff_of_iSup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean#L162). The attribute's comment: “(1) iff (2)”.

> **Stacks Project, Tag 01SM, (1) is equivalent to (2).** A morphism of schemes is
> quasi-affine if and only if the preimages of the members of one affine open covering of the
> target are quasi-affine schemes.

```lean
theorem isQuasiAffineHom_iff_of_iSup_eq_top {X S : Scheme.{u}} (f : X ⟶ S) {ι : Type*}
    (U : ι → S.Opens) (hU : ∀ i, IsAffineOpen (U i)) (hU' : ⨆ i, U i = ⊤) :
    IsQuasiAffineHom f ↔ ∀ i, (f ⁻¹ᵁ U i).toScheme.IsQuasiAffine
```

## Tag 01SN, a lemma

[Tag 01SN](https://stacks.math.columbia.edu/tag/01SN) in the Stacks Project.

**`AlgebraicGeometry.isQuasiAffineHom_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean#L185). References: EGA II (5.1.10).

> **Stacks Project, Tag 01SN.** A composition of quasi-affine morphisms of schemes is
> quasi-affine.

```lean
instance isQuasiAffineHom_isStableUnderComposition :
    MorphismProperty.IsStableUnderComposition
      (@IsQuasiAffineHom : MorphismProperty Scheme.{u})
```

## Tag 01SO, a lemma

[Tag 01SO](https://stacks.math.columbia.edu/tag/01SO) in the Stacks Project.

**`AlgebraicGeometry.isQuasiAffineHom_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineStability.lean#L201). References: EGA IV (2.7.1), “(xiv)”.

> **Stacks Project, Tag 01SO.** Quasi-affine morphisms of schemes are stable under arbitrary
> base change.

```lean
instance isQuasiAffineHom_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@IsQuasiAffineHom : MorphismProperty Scheme.{u})
```

## Tag 02JR, a lemma

[Tag 02JR](https://stacks.math.columbia.edu/tag/02JR) in the Stacks Project.

**`AlgebraicGeometry.isQuasiAffineHom_of_isImmersion_of_quasiCompact`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/QuasiAffineImmersion.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/QuasiAffineImmersion.lean#L40).

> **Stacks Project, Tag 02JR.** Every quasi-compact immersion of schemes is
> quasi-affine.

```lean
instance isQuasiAffineHom_of_isImmersion_of_quasiCompact
    {X S : Scheme.{u}} (f : X ⟶ S) [IsImmersion f] [QuasiCompact f] :
    IsQuasiAffineHom f
```

## Tag 01SP, a lemma

[Tag 01SP](https://stacks.math.columbia.edu/tag/01SP) in the Stacks Project.

**`AlgebraicGeometry.isQuasiAffineHom_iff_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean#L74). The attribute's comment: “characterization”.

> A morphism from an affine scheme is quasi-affine if and only if it is quasi-compact.

```lean
theorem isQuasiAffineHom_iff_quasiCompact {X S : Scheme.{u}} [IsAffine X]
    (f : X ⟶ S) : IsQuasiAffineHom f ↔ QuasiCompact f
```

**`AlgebraicGeometry.isQuasiAffineHom_of_isQuasiAffine_of_quasiSeparatedSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean#L85). The attribute's comment: “quasi-separated target”. References: EGA II (5.1.8), “X q-affine ⇒ f q-affine”.

> Every morphism from a quasi-affine scheme to a quasi-separated scheme is quasi-affine.

```lean
instance isQuasiAffineHom_of_isQuasiAffine_of_quasiSeparatedSpace
    {X S : Scheme.{u}} [Scheme.IsQuasiAffine X] [QuasiSeparatedSpace S]
    (f : X ⟶ S) : IsQuasiAffineHom f
```

## Tag 054G, a lemma

[Tag 054G](https://stacks.math.columbia.edu/tag/054G) in the Stacks Project.

**`AlgebraicGeometry.isQuasiAffineHom_of_isQuasiAffine_of_quasiSeparatedSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffine.lean#L85). The attribute's comment: “absolute corollary”. References: EGA II (5.1.8), “X q-affine ⇒ f q-affine”.

> Every morphism from a quasi-affine scheme to a quasi-separated scheme is quasi-affine.

```lean
instance isQuasiAffineHom_of_isQuasiAffine_of_quasiSeparatedSpace
    {X S : Scheme.{u}} [Scheme.IsQuasiAffine X] [QuasiSeparatedSpace S]
    (f : X ⟶ S) : IsQuasiAffineHom f
```

**`AlgebraicGeometry.IsQuasiAffineHom.of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiSeparated.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiSeparated.lean#L36). The attribute's comment: “relative statement”.

> A morphism `g : X ⟶ Y` to a scheme quasi-separated over a base `S` via `h : Y ⟶ S` is
> quasi-affine as soon as the structure morphism `g ≫ h` of `X` over `S` is quasi-affine.

```lean
theorem IsQuasiAffineHom.of_comp {X Y S : Scheme.{u}} (g : X ⟶ Y) (h : Y ⟶ S)
    [IsQuasiAffineHom (g ≫ h)] [QuasiSeparated h] : IsQuasiAffineHom g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.13, Tag 01SJ](https://stacks.math.columbia.edu/tag/01SJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
