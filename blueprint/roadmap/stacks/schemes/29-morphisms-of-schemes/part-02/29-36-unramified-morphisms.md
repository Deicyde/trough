---
declaration: section
origin: cited
lean: AlgebraicGeometry.UnramifiedAt, AlgebraicGeometry.GUnramifiedAt, AlgebraicGeometry.Unramified, AlgebraicGeometry.GUnramified, AlgebraicGeometry.unramified_iff_locallyOfFiniteType_and_isZero_relativeDifferentials, AlgebraicGeometry.gUnramified_iff_locallyOfFinitePresentation_and_isZero_relativeDifferentials, AlgebraicGeometry.unramified_tfae, AlgebraicGeometry.gUnramified_tfae
statement: formalized
proof: formalized
---

# 29.36 Unramified morphisms

Section 29.36 of the Stacks Project, [Tag 02G3](https://stacks.math.columbia.edu/tag/02G3). 17 tags here are carried by 46 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02G4, a definition

[Tag 02G4](https://stacks.math.columbia.edu/tag/02G4) in the Stacks Project.

**`AlgebraicGeometry.UnramifiedAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean#L55). The attribute's comment: “part (1)”. References: SGA 3 XI (1.3); SGA 3 XI (1.5).

> A morphism of schemes `f : X ⟶ S` is unramified at `x : X` if there are affine open
> neighbourhoods `U` of `x` and `V` of its image, with `U ≤ f ⁻¹ᵁ V`, such that the induced map on
> rings of sections is unramified.

```lean
public def UnramifiedAt {X S : Scheme.{u}} (f : X ⟶ S) (x : X) : Prop
```

**`AlgebraicGeometry.GUnramifiedAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean#L65). The attribute's comment: “part (2)”. References: EGA IV (17.3.7), “unramified case”.

> A morphism of schemes `f : X ⟶ S` is G-unramified at `x : X` if there are affine open
> neighbourhoods `U` of `x` and `V` of its image, with `U ≤ f ⁻¹ᵁ V`, such that the induced map on
> rings of sections is G-unramified.

```lean
public def GUnramifiedAt {X S : Scheme.{u}} (f : X ⟶ S) (x : X) : Prop
```

**`AlgebraicGeometry.Unramified`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean#L73). The attribute's comment: “part (3)”.

> A morphism of schemes is unramified if it is unramified at every point of its source.

```lean
public class Unramified {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

**`AlgebraicGeometry.GUnramified`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Defs.lean#L79). The attribute's comment: “part (4)”.

> A morphism of schemes is G-unramified if it is G-unramified at every point of its source.

```lean
public class GUnramified {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 02G5, a lemma

[Tag 02G5](https://stacks.math.columbia.edu/tag/02G5) in the Stacks Project.

**`AlgebraicGeometry.unramified_iff_locallyOfFiniteType_and_isZero_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean#L96). The attribute's comment: “part (1)”. References: EGA IV (17.4.1.2), “Omega = 0 criterion”; SGA 1 II (4.1), “S=Y, unramified clause”.

> A morphism of schemes is unramified if and only if it is locally of finite type and its
> sheaf of relative differentials is zero.

```lean
theorem unramified_iff_locallyOfFiniteType_and_isZero_relativeDifferentials (f : X ⟶ S) :
    Unramified f ↔
      (LocallyOfFiniteType f ∧ IsZero (Scheme.Hom.relativeDifferentials f))
```

**`AlgebraicGeometry.gUnramified_iff_locallyOfFinitePresentation_and_isZero_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean#L106). The attribute's comment: “part (2)”.

> A morphism of schemes is G-unramified if and only if it is locally of finite presentation
> and its sheaf of relative differentials is zero.

```lean
theorem gUnramified_iff_locallyOfFinitePresentation_and_isZero_relativeDifferentials
    (f : X ⟶ S) :
    GUnramified f ↔
      (LocallyOfFinitePresentation f ∧ IsZero (Scheme.Hom.relativeDifferentials f))
```

## Tag 02G6, a lemma

[Tag 02G6](https://stacks.math.columbia.edu/tag/02G6) in the Stacks Project.

**`AlgebraicGeometry.unramified_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean#L149). The attribute's comment: “unramified characterization”.

> The four characterizations of an unramified morphism: the global condition, the condition on
> every compatible pair of affine opens, an open-covering criterion, and an affine-open-covering
> criterion on rings of sections.

```lean
public theorem unramified_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE [
      Unramified f,
      ∀ (U : X.Opens) (_ : IsAffineOpen U) (V : S.Opens) (_ : IsAffineOpen V)
        (hUV : U ≤ f ⁻¹ᵁ V),
        letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U hUV).hom.toAlgebra
        Algebra.Unramified Γ(S, V) Γ(X, U),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            ∀ i, Unramified
              (f.resLE (V j) (U i) ((le_iSup U i).trans hU.le)),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i,
                let hUV : U i ≤ f ⁻¹ᵁ V j := (le_iSup U i).trans hU.le
                letI : Algebra Γ(S, V j) Γ(X, U i) := (f.appLE (V j) (U i) hUV).hom.toAlgebra
                Algebra.Unramified Γ(S, V j) Γ(X, U i)]
```

**`AlgebraicGeometry.gUnramified_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean#L299). The attribute's comment: “G-unramified characterization”.

> The four characterizations of a G-unramified morphism: the global condition, the condition on
> every compatible pair of affine opens, an open-covering criterion, and an affine-open-covering
> criterion on rings of sections.

```lean
public theorem gUnramified_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE [
      GUnramified f,
      ∀ (U : X.Opens) (_ : IsAffineOpen U) (V : S.Opens) (_ : IsAffineOpen V)
        (hUV : U ≤ f ⁻¹ᵁ V),
        letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U hUV).hom.toAlgebra
        Algebra.GUnramified Γ(S, V) Γ(X, U),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            ∀ i, GUnramified
              (f.resLE (V j) (U i) ((le_iSup U i).trans hU.le)),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i,
                let hUV : U i ≤ f ⁻¹ᵁ V j := (le_iSup U i).trans hU.le
                letI : Algebra Γ(S, V j) Γ(X, U i) := (f.appLE (V j) (U i) hUV).hom.toAlgebra
                Algebra.GUnramified Γ(S, V j) Γ(X, U i)]
```

**`AlgebraicGeometry.unramified_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean#L375). The attribute's comment: “restriction of an unramified morphism”.

> Restricting an unramified morphism to compatible open subschemes of its source and target
> is unramified.

```lean
public theorem unramified_resLE {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : Unramified f) (U : X.Opens) (V : S.Opens) (hUV : U ≤ f ⁻¹ᵁ V) :
    Unramified (f.resLE V U hUV)
```

**`AlgebraicGeometry.gUnramified_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Local.lean#L388). The attribute's comment: “restriction of a G-unramified morphism”.

> Restricting a G-unramified morphism to compatible open subschemes of its source and target
> is G-unramified.

```lean
public theorem gUnramified_resLE {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : GUnramified f) (U : X.Opens) (V : S.Opens) (hUV : U ≤ f ⁻¹ᵁ V) :
    GUnramified (f.resLE V U hUV)
```

## Tag 02G9, a lemma

[Tag 02G9](https://stacks.math.columbia.edu/tag/02G9) in the Stacks Project.

**`AlgebraicGeometry.unramified_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L235). The attribute's comment: “unramified”. References: EGA IV (17.3.3), “(ii), special case”; SGA 1 I (3.5), “more general”.

> Unramified morphisms of schemes are stable under composition.

```lean
public instance unramified_isStableUnderComposition :
    MorphismProperty.IsStableUnderComposition (@Unramified.{u})
```

**`AlgebraicGeometry.gUnramified_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L243). The attribute's comment: “G-unramified”. References: EGA IV (17.3.3), “(ii)”; SGA 1 I (3.5), “more general”.

> G-unramified morphisms of schemes are stable under composition.

```lean
public instance gUnramified_isStableUnderComposition :
    MorphismProperty.IsStableUnderComposition (@GUnramified.{u})
```

## Tag 02GA, a lemma

[Tag 02GA](https://stacks.math.columbia.edu/tag/02GA) in the Stacks Project.

**`AlgebraicGeometry.unramified_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L251). The attribute's comment: “unramified”. References: SGA 1 I (3.5), “(iii)”.

> Unramified morphisms of schemes are stable under arbitrary base change.

```lean
public instance unramified_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun {X S : Scheme.{u}} (f : X ⟶ S) ↦ Unramified f)
```

**`AlgebraicGeometry.gUnramified_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L260). The attribute's comment: “G-unramified”. References: SGA 1 I (3.5), “(iii)”.

> G-unramified morphisms of schemes are stable under arbitrary base change.

```lean
public instance gUnramified_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun {X S : Scheme.{u}} (f : X ⟶ S) ↦ GUnramified f)
```

## Tag 04EV, a lemma

[Tag 04EV](https://stacks.math.columbia.edu/tag/04EV) in the Stacks Project.

**`AlgebraicGeometry.unramified_iff_gUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Noetherian.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Noetherian.lean#L39).

> Over a locally Noetherian target, a morphism of schemes is unramified if and only if it is
> G-unramified.

```lean
theorem unramified_iff_gUnramified {X S : Scheme.{u}} (f : X ⟶ S) [IsLocallyNoetherian S] :
    Unramified f ↔ GUnramified f
```

## Tag 02GB, a lemma

[Tag 02GB](https://stacks.math.columbia.edu/tag/02GB) in the Stacks Project.

**`AlgebraicGeometry.gUnramified_of_isOpenImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UnramifiedOpenImmersion.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UnramifiedOpenImmersion.lean#L32).

> An open immersion of schemes is G-unramified.

```lean
public instance gUnramified_of_isOpenImmersion {X S : Scheme.{u}} (f : X ⟶ S)
    [IsOpenImmersion f] : GUnramified f
```

## Tag 02GC, a lemma

[Tag 02GC](https://stacks.math.columbia.edu/tag/02GC) in the Stacks Project.

**`AlgebraicGeometry.unramified_of_isClosedImmersion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/ClosedImmersion.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/ClosedImmersion.lean#L48). The attribute's comment: “unramified”. References: EGA IV (17.3.3), “(i), special case”.

> A closed immersion of schemes is unramified.

```lean
instance unramified_of_isClosedImmersion {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] : Unramified i
```

**`AlgebraicGeometry.gUnramified_iff_isFiniteType_idealSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/ClosedImmersion.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/ClosedImmersion.lean#L55). The attribute's comment: “G-unramified iff finite-type ideal sheaf”.

> A closed immersion of schemes is G-unramified exactly when its ideal sheaf is of finite
> type.

```lean
theorem gUnramified_iff_isFiniteType_idealSheaf {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] :
    GUnramified i ↔ (Stacks.ClosedImmersion.idealSheaf i.toLRSHom.toShHom).IsFiniteType
```

## Tag 02GD, a lemma

[Tag 02GD](https://stacks.math.columbia.edu/tag/02GD) in the Stacks Project.

**`AlgebraicGeometry.unramified_iff_locallyOfFiniteType_and_isZero_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean#L96). The attribute's comment: “first sentence: an unramified morphism is locally of finite type”. References: EGA IV (17.4.1.2), “Omega = 0 criterion”; SGA 1 II (4.1), “S=Y, unramified clause”.

> A morphism of schemes is unramified if and only if it is locally of finite type and its
> sheaf of relative differentials is zero.

```lean
theorem unramified_iff_locallyOfFiniteType_and_isZero_relativeDifferentials (f : X ⟶ S) :
    Unramified f ↔
      (LocallyOfFiniteType f ∧ IsZero (Scheme.Hom.relativeDifferentials f))
```

**`AlgebraicGeometry.gUnramified_iff_locallyOfFinitePresentation_and_isZero_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean#L106). The attribute's comment: “first sentence: an unramified morphism is locally of finite type”.

> A morphism of schemes is G-unramified if and only if it is locally of finite presentation
> and its sheaf of relative differentials is zero.

```lean
theorem gUnramified_iff_locallyOfFinitePresentation_and_isZero_relativeDifferentials
    (f : X ⟶ S) :
    GUnramified f ↔
      (LocallyOfFinitePresentation f ∧ IsZero (Scheme.Hom.relativeDifferentials f))
```

## Tag 02V5, a lemma

[Tag 02V5](https://stacks.math.columbia.edu/tag/02V5) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFiniteType_of_unramified`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L99). The attribute's comment: “local finite-type part of the global consequence”.

> An unramified morphism of schemes is locally of finite type.

```lean
public instance locallyOfFiniteType_of_unramified (f : X ⟶ S) [Unramified f] :
    LocallyOfFiniteType f
```

**`AlgebraicGeometry.quasiFiniteAt_of_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L126). The attribute's comment: “the pointwise claim: unramified at `x` implies quasi-finite at `x`”.

> **Stacks Project, Tag 02V5, the pointwise claim.** A morphism of schemes unramified at `x` is
> quasi-finite at `x`. No hypothesis beyond unramifiedness at the point: the affine chart witnessing
> it carries an unramified, hence finite-type, map of sections, which is finite type at the point
> and makes the stalk map both essentially of finite type and formally unramified, and such an
> algebra is quasi-finite.

```lean
public theorem quasiFiniteAt_of_unramifiedAt (f : X ⟶ S) {x : X} (h : UnramifiedAt f x) :
    quasiFiniteAt f x
```

**`AlgebraicGeometry.locallyQuasiFinite_of_unramified`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L159). The attribute's comment: “fiber-isolation part of the global consequence”. References: EGA IV (17.4.3).

> The fibers of an unramified morphism are locally discrete.

```lean
public instance locallyQuasiFinite_of_unramified (f : X ⟶ S) [Unramified f] :
    LocallyQuasiFinite f
```

## Tag 02G7, a lemma

[Tag 02G7](https://stacks.math.columbia.edu/tag/02G7) in the Stacks Project.

**`AlgebraicGeometry.unramified_iff_iso_coproduct_spectra_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Fibers.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Fibers.lean#L195). The attribute's comment: “part (1)”. References: EGA IV (17.15.11), “b) <=> c)”; SGA 3 XI (1.3), “(a)<=>(e) over field”.

> **Stacks Project, Tag 02G7, part (1).** A morphism to the spectrum of a field is unramified
> if and only if its source is, over that spectrum, a coproduct of spectra of finite separable
> field extensions.

```lean
public theorem unramified_iff_iso_coproduct_spectra_finite_separable
    (k : Type u) [Field k] {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) :
    Unramified f ↔
      ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
        (_ : ∀ i, Algebra k (K i)) (_ : ∀ i, Module.Finite k (K i))
        (_ : ∀ i, Algebra.IsSeparable k (K i))
        (e : X ≅ ∐ fun i ↦ Spec (.of (K i))),
        e.hom ≫ Sigma.desc (fun i ↦ Spec.map (CommRingCat.ofHom (algebraMap k (K i)))) = f
```

**`AlgebraicGeometry.Unramified.exists_iso_fiber_coproduct_spectra_finite_separable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Fibers.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Fibers.lean#L270). The attribute's comment: “part (2)”. References: SGA 3 XI (1.3), “(a) => (e)”.

> **Stacks Project, Tag 02G7, part (2).** Every fibre of an unramified morphism is, over the
> residue field of the base point, a coproduct of spectra of finite separable field extensions.

```lean
public theorem Unramified.exists_iso_fiber_coproduct_spectra_finite_separable
    {X S : Scheme.{u}} (f : X ⟶ S) [Unramified f] (s : S) :
    ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
      (_ : ∀ i, Algebra (S.residueField s) (K i))
      (_ : ∀ i, Module.Finite (S.residueField s) (K i))
      (_ : ∀ i, Algebra.IsSeparable (S.residueField s) (K i))
      (e : f.fiber s ≅ ∐ fun i ↦ Spec (.of (K i))),
      e.hom ≫ Sigma.desc (fun i ↦
        Spec.map (CommRingCat.ofHom (algebraMap (S.residueField s) (K i)))) =
        f.fiberToSpecResidueField s
```

## Tag 02G8, a lemma

[Tag 02G8](https://stacks.math.columbia.edu/tag/02G8) in the Stacks Project.

**`AlgebraicGeometry.unramified_of_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/FiberCriterion.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/FiberCriterion.lean#L100). The attribute's comment: “part (2): a morphism locally of finite type all of whose fibres are disjoint unions of spectra of finite separable extensions of the residue field of the base point is unramified”. References: EGA IV (17.4.2), “Implication d′ ⇒ a”; SGA 3 XI (1.3), “(i)(e)⇒(a)”.

> A morphism locally of finite type whose fibres are disjoint unions of spectra of finite
> separable extensions of the corresponding residue fields is unramified.

```lean
public theorem unramified_of_fibres {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (h : ∀ s : S,
      ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
        (_ : ∀ i, Algebra (S.residueField s) (K i))
        (_ : ∀ i, Module.Finite (S.residueField s) (K i))
        (_ : ∀ i, Algebra.IsSeparable (S.residueField s) (K i))
        (e : f.fiber s ≅ ∐ fun i ↦ Spec (.of (K i))),
        e.hom ≫ Sigma.desc (fun i ↦
          Spec.map (CommRingCat.ofHom (algebraMap (S.residueField s) (K i)))) =
            f.fiberToSpecResidueField s) :
    Unramified f
```

**`AlgebraicGeometry.gUnramified_of_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/FiberCriterion.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/FiberCriterion.lean#L119). The attribute's comment: “part (3): a morphism locally of finite presentation all of whose fibres are disjoint unions of spectra of finite separable extensions of the residue field of the base point is G-unramified”. References: EGA IV (17.4.2), “Implication d′ ⇒ a”; SGA 3 XI (1.3), “(i)(e)⇒(a)”.

> A morphism locally of finite presentation whose fibres are disjoint unions of spectra of
> finite separable extensions of the corresponding residue fields is G-unramified.

```lean
public theorem gUnramified_of_fibres {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f]
    (h : ∀ s : S,
      ∃ (I : Type u) (K : I → Type u) (_ : ∀ i, Field (K i))
        (_ : ∀ i, Algebra (S.residueField s) (K i))
        (_ : ∀ i, Module.Finite (S.residueField s) (K i))
        (_ : ∀ i, Algebra.IsSeparable (S.residueField s) (K i))
        (e : f.fiber s ≅ ∐ fun i ↦ Spec (.of (K i))),
        e.hom ≫ Sigma.desc (fun i ↦
          Spec.map (CommRingCat.ofHom (algebraMap (S.residueField s) (K i)))) =
            f.fiberToSpecResidueField s) :
    GUnramified f
```

**`AlgebraicGeometry.finite_residueField_of_unramified`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L294). The attribute's comment: “finite_separable_residue”. References: EGA IV (17.4.1), “a) => d'' finiteness”; SGA 3 XI (1.3), “(ii) k(B)/k(A) finite”; SGA 1 I (3.1), “(ii)=>(i) finiteness”.

> The residue field extension at a point of an unramified morphism is finite.

```lean
public instance finite_residueField_of_unramified (f : X ⟶ S) [Unramified f] (x : X) :
    letI := (f.residueFieldMap x).hom.toAlgebra
    Module.Finite (S.residueField (f x)) (X.residueField x)
```

**`AlgebraicGeometry.isSeparable_residueField_of_unramified`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L320). The attribute's comment: “finite_separable_residue”. References: EGA IV (17.4.1), “a) => d'' separability”; SGA 3 XI (1.3), “(ii) k(B)/k(A) separable”; SGA 1 I (3.1), “(ii)=>(i) separability”.

> The residue field extension at a point of an unramified morphism is separable.

```lean
public instance isSeparable_residueField_of_unramified (f : X ⟶ S) [Unramified f] (x : X) :
    letI := (f.residueFieldMap x).hom.toAlgebra
    Algebra.IsSeparable (S.residueField (f x)) (X.residueField x)
```

## Tag 02GE, a lemma

[Tag 02GE](https://stacks.math.columbia.edu/tag/02GE) in the Stacks Project.

**`AlgebraicGeometry.Unramified.isOpenImmersion_diagonal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean#L43). The attribute's comment: “part (1)”. References: EGA IV (17.4.2), “a) ⇒ b)”; EGA IV (17.4.1), “a) => b)”; SGA 3 XI (1.3), “(a) => (b)”; SGA 1 I (3.4), “diagonal case (g = id)”; SGA 1 I (3.1), “(ii) => (iii)”.

> The diagonal of an unramified morphism is an open immersion.

```lean
public instance isOpenImmersion_diagonal {X S : Scheme.{u}} (f : X ⟶ S) [Unramified f] :
    IsOpenImmersion (pullback.diagonal f)
```

**`AlgebraicGeometry.Unramified.of_isOpenImmersion_diagonal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean#L55). The attribute's comment: “part (2)”. References: EGA IV (17.4.2), “b) ⇒ a)”; EGA IV (17.4.1.2), “diagonal => unramified”; EGA IV (17.4.1), “b) => a)”; SGA 3 XI (1.3), “(b) => (a)”; SGA 1 I (3.1), “(iii) => (ii)”.

> A morphism locally of finite type whose diagonal is an open immersion is unramified.

```lean
public instance of_isOpenImmersion_diagonal {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] [IsOpenImmersion (pullback.diagonal f)] :
    Unramified f
```

**`AlgebraicGeometry.GUnramified.of_isOpenImmersion_diagonal`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Diagonal.lean#L71). The attribute's comment: “part (3)”. References: EGA IV (17.4.2), “b) ⇒ a)”; EGA IV (17.4.1), “b) => a)”; SGA 3 XI (1.3), “(b) => (a)”; SGA 1 I (3.1), “(iii)=>(ii), fin pres”.

> A morphism locally of finite presentation whose diagonal is an open immersion is
> G-unramified.

```lean
public instance of_isOpenImmersion_diagonal {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f] [IsOpenImmersion (pullback.diagonal f)] :
    GUnramified f
```

## Tag 02GF, a lemma

[Tag 02GF](https://stacks.math.columbia.edu/tag/02GF) in the Stacks Project.

**`AlgebraicGeometry.unramifiedAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/AtPointCriteria.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/AtPointCriteria.lean#L220).

> **Stacks Project, Tag 02GF.** For a morphism of schemes `f : X ⟶ S` locally of finite type
> and a point `x` of `X` with image `s = f x`, the following are equivalent: `f` is unramified at
> `x`; the fibre `X_s` is unramified over `κ(s)` at `x`; the `𝒪_{X,x}`-module `Ω_{X/S,x}` is zero;
> the `𝒪_{X_s,x}`-module `Ω_{X_s/s,x}` is zero; the `κ(x)`-vector space
> `Ω_{X_s/s,x} ⊗ κ(x) = Ω_{X/S,x} ⊗ κ(x)` is zero, in either of its two canonically identified
> spellings; and `𝔪_s 𝒪_{X,x} = 𝔪_x` with `κ(x)/κ(s)` finite separable.

```lean
public theorem unramifiedAt_tfae (f : X ⟶ S) [LocallyOfFiniteType f] (x : X) :
    List.TFAE [
      UnramifiedAt f x,
      UnramifiedAt (f.fiberToSpecResidueField (f x)) (f.asFiber x),
      Subsingleton (relativeDifferentialStalk f x),
      Subsingleton (relativeDifferentialStalk (f.fiberToSpecResidueField (f x))
        (f.asFiber x)),
      Subsingleton (fiberRelativeCotangentSpace f x),
      Subsingleton (relativeCotangentSpace f x),
      Ideal.map (f.stalkMap x).hom
            (IsLocalRing.maximalIdeal (S.presheaf.stalk (f x))) =
          IsLocalRing.maximalIdeal (X.presheaf.stalk x) ∧
        (letI := (f.residueFieldMap x).hom.toAlgebra
         Module.Finite (S.residueField (f x)) (X.residueField x) ∧
           Algebra.IsSeparable (S.residueField (f x)) (X.residueField x))]
```

**`AlgebraicGeometry.gUnramifiedAt_iff_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean#L96). The attribute's comment: “the G-unramified reading of condition (1): for `f` locally of finite presentation, G-unramified at `x` is equivalent to unramified at `x`”.

> **Stacks Project, Tag 02GF, the G-unramified clause.** A morphism of schemes locally of
> finite presentation is G-unramified at a point exactly when it is unramified there: the affine
> chart witnessing either notion witnesses the other, local finite presentation of the morphism
> supplying finite presentation of the map of sections.

```lean
public theorem gUnramifiedAt_iff_unramifiedAt (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (x : X) : GUnramifiedAt f x ↔ UnramifiedAt f x
```

**`AlgebraicGeometry.gUnramifiedAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean#L116). The attribute's comment: “the `resp. G-unramified` reading, under local finite presentation; the unramified reading is `AlgebraicGeometry.unramifiedAt_tfae`”.

> **Stacks Project, Tag 02GF, the G-unramified reading.** For a morphism of schemes `f : X ⟶ S`
> locally of finite presentation and a point `x` of `X` with image `s = f x`, the following are
> equivalent: `f` is G-unramified at `x`; `f` is unramified at `x`; the fibre `X_s` is unramified
> over `κ(s)` at `x`; the `𝒪_{X,x}`-module `Ω_{X/S,x}` is zero; the `𝒪_{X_s,x}`-module
> `Ω_{X_s/s,x}` is zero; the `κ(x)`-vector space `Ω_{X_s/s,x} ⊗ κ(x) = Ω_{X/S,x} ⊗ κ(x)` is zero,
> in either of its two canonically identified spellings; and `𝔪_s 𝒪_{X,x} = 𝔪_x` with
> `κ(x)/κ(s)` finite separable.

```lean
public theorem gUnramifiedAt_tfae (f : X ⟶ S) [LocallyOfFinitePresentation f] (x : X) :
    List.TFAE [
      GUnramifiedAt f x,
      UnramifiedAt f x,
      UnramifiedAt (f.fiberToSpecResidueField (f x)) (f.asFiber x),
      Subsingleton (relativeDifferentialStalk f x),
      Subsingleton (relativeDifferentialStalk (f.fiberToSpecResidueField (f x))
        (f.asFiber x)),
      Subsingleton (fiberRelativeCotangentSpace f x),
      Subsingleton (relativeCotangentSpace f x),
      Ideal.map (f.stalkMap x).hom
            (IsLocalRing.maximalIdeal (S.presheaf.stalk (f x))) =
          IsLocalRing.maximalIdeal (X.presheaf.stalk x) ∧
        (letI := (f.residueFieldMap x).hom.toAlgebra
         Module.Finite (S.residueField (f x)) (X.residueField x) ∧
           Algebra.IsSeparable (S.residueField (f x)) (X.residueField x))]
```

## Tag 0475, a lemma

[Tag 0475](https://stacks.math.columbia.edu/tag/0475) in the Stacks Project.

**`AlgebraicGeometry.unramifiedAt_iff_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/BaseChangeLocus.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/BaseChangeLocus.lean#L115). The attribute's comment: “base change of the unramified locus”. References: SGA 1 I (3.5), “more general”.

> **Stacks Project, Tag 0475, the base-change half, pointwise.** Let
> ```
> X' → X
> ↓    ↓
> Y' → Y
> ```
> be a cartesian diagram of schemes with `f : X ⟶ Y` locally of finite type, and let
> `f' : X' ⟶ Y'` be the base change of `f` along `g : Y' ⟶ Y`. A point `x'` of `X'` is a point of
> unramifiedness of `f'` if and only if its image `g' x'` in `X` is a point of unramifiedness
> of `f`.

```lean
theorem unramifiedAt_iff_of_isPullback {X' X Y' Y : Scheme.{u}}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (sq : IsPullback g' f' f g) [LocallyOfFiniteType f] (x' : X') :
    UnramifiedAt f (g'.base x') ↔ UnramifiedAt f' x'
```

**`AlgebraicGeometry.setOf_unramifiedAt_fiber_eq_setOf_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean#L157). The attribute's comment: “the two descriptions of `T` agree, locally-of-finite-type reading”. References: EGA IV (17.4.1), “more general”; EGA IV (17.8.1), “case Y = S”; SGA 1 I (5.8), “Net clause, special case”; SGA 3 VIB (2.7), “(iii) ⇔ (iv)”.

> **Stacks Project, Tag 0475, the equality of the two descriptions of `T`.** For a morphism of
> schemes locally of finite type, the set of points at which the scheme-theoretic fibre is
> unramified over the residue field of its image is the set of points at which the morphism itself
> is unramified.

```lean
public theorem setOf_unramifiedAt_fiber_eq_setOf_unramifiedAt (f : X ⟶ S)
    [LocallyOfFiniteType f] :
    {x : X | UnramifiedAt (f.fiberToSpecResidueField (f x)) (f.asFiber x)} =
      {x : X | UnramifiedAt f x}
```

**`AlgebraicGeometry.setOf_unramifiedAt_fiber_eq_setOf_gUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean#L174). The attribute's comment: “the two descriptions of `T` agree in the locally-of-finite-presentation reading, identifying `T` with the G-unramified locus”. References: EGA IV (17.4.1); EGA IV (17.8.1), “case Y = S”; SGA 1 I (5.8), “Net clause, special case”; SGA 3 VIB (2.7), “(iii) ⇔ (iv)”.

> **Stacks Project, Tag 0475, the equality of the two descriptions of `T`, G-unramified
> reading.** For a morphism of schemes locally of finite presentation, the set of points at which
> the scheme-theoretic fibre is unramified over the residue field of its image is the set of points
> at which the morphism itself is G-unramified. Hence that set is the open G-unramified locus, which
> is what makes the second half of the tag follow from the first.

```lean
public theorem setOf_unramifiedAt_fiber_eq_setOf_gUnramifiedAt (f : X ⟶ S)
    [LocallyOfFinitePresentation f] :
    {x : X | UnramifiedAt (f.fiberToSpecResidueField (f x)) (f.asFiber x)} =
      {x : X | GUnramifiedAt f x}
```

**`AlgebraicGeometry.setOf_unramifiedAt_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean#L195). The attribute's comment: “`T' = (g')⁻¹ T` in set form, for the unramified locus”. References: EGA IV (17.7.2), “more general”.

> **Stacks Project, Tag 0475, the base-change half in set form.** Let
> ```
> X' → X
> ↓    ↓
> S' → S
> ```
> be a cartesian diagram of schemes with `f : X ⟶ S` locally of finite type and `f' : X' ⟶ S'` the
> base change of `f` along `g : S' ⟶ S`. Then the unramified locus `T'` of `f'` is the inverse
> image under `g' : X' ⟶ X` of the unramified locus `T` of `f`.

```lean
public theorem setOf_unramifiedAt_eq_preimage_of_isPullback {X' X S' S : Scheme.{u}}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S}
    (sq : IsPullback g' f' f g) [LocallyOfFiniteType f] :
    {x' : X' | UnramifiedAt f' x'} = g'.base ⁻¹' {x : X | UnramifiedAt f x}
```

**`AlgebraicGeometry.gUnramifiedAt_iff_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean#L214). The attribute's comment: “base change of the G-unramified locus, pointwise”. References: SGA 1 I (3.5), “more general”; SGA 3 XI (1.3), “more general”.

> **Stacks Project, Tag 0475, the base-change half for the G-unramified locus, pointwise.** Let
> ```
> X' → X
> ↓    ↓
> S' → S
> ```
> be a cartesian diagram of schemes with `f : X ⟶ S` locally of finite presentation and
> `f' : X' ⟶ S'` the base change of `f` along `g : S' ⟶ S`. A point `x'` of `X'` is a point of
> G-unramifiedness of `f'` if and only if its image `g' x'` in `X` is a point of G-unramifiedness
> of `f`.

```lean
public theorem gUnramifiedAt_iff_of_isPullback {X' X S' S : Scheme.{u}}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S}
    (sq : IsPullback g' f' f g) [LocallyOfFinitePresentation f] (x' : X') :
    GUnramifiedAt f (g'.base x') ↔ GUnramifiedAt f' x'
```

**`AlgebraicGeometry.setOf_gUnramifiedAt_eq_preimage_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/GUnramifiedLocusBaseChange.lean#L228). The attribute's comment: “`T' = (g')⁻¹ T` in set form, for the G-unramified locus, under local finite presentation”.

> **Stacks Project, Tag 0475, the second half in set form.** For a cartesian diagram of schemes
> with `f : X ⟶ S` locally of finite presentation, the G-unramified locus of the base change
> `f' : X' ⟶ S'` is the inverse image under `g' : X' ⟶ X` of the G-unramified locus of `f`.

```lean
public theorem setOf_gUnramifiedAt_eq_preimage_of_isPullback {X' X S' S : Scheme.{u}}
    {g' : X' ⟶ X} {f' : X' ⟶ S'} {f : X ⟶ S} {g : S' ⟶ S}
    (sq : IsPullback g' f' f g) [LocallyOfFinitePresentation f] :
    {x' : X' | GUnramifiedAt f' x'} = g'.base ⁻¹' {x : X | GUnramifiedAt f x}
```

**`AlgebraicGeometry.isOpen_setOf_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/OpenLocus.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/OpenLocus.lean#L66). The attribute's comment: “openness of the unramified locus”. References: SGA 1 I (3.3).

> **Stacks Project, Tag 0475.** The locus where a morphism of schemes is unramified is open.

```lean
theorem isOpen_setOf_unramifiedAt (f : X ⟶ Y) : IsOpen {x : X | UnramifiedAt f x}
```

**`AlgebraicGeometry.isOpen_setOf_gUnramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/OpenLocus.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/OpenLocus.lean#L74). The attribute's comment: “openness of the G-unramified locus”. References: SGA 1 I (3.3), “loc. finite presentation”.

> **Stacks Project, Tag 0475.** The locus where a morphism of schemes is G-unramified is
> open.

```lean
theorem isOpen_setOf_gUnramifiedAt (f : X ⟶ Y) : IsOpen {x : X | GUnramifiedAt f x}
```

## Tag 02GG, a lemma

[Tag 02GG](https://stacks.math.columbia.edu/tag/02GG) in the Stacks Project.

**`AlgebraicGeometry.unramified_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L269). The attribute's comment: “part (1)”. References: SGA 1 I (3.6), “(v)”.

> If the composite `X ⟶ Y ⟶ S` is unramified, then `X ⟶ Y` is unramified.

```lean
public theorem unramified_of_comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [Unramified (f ≫ g)] : Unramified f
```

**`AlgebraicGeometry.gUnramified_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Properties.lean#L281). The attribute's comment: “part (2): carries the hypothesis that `g` is locally of finite type”.

> If the composite `X ⟶ Y ⟶ S` is G-unramified and `Y ⟶ S` is locally of finite type, then
> `X ⟶ Y` is G-unramified.

```lean
public theorem gUnramified_of_comp {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [GUnramified (f ≫ g)] [LocallyOfFiniteType g] : GUnramified f
```

## Tag 04HB, a lemma

[Tag 04HB](https://stacks.math.columbia.edu/tag/04HB) in the Stacks Project.

**`AlgebraicGeometry.exists_open_eq_of_residueFieldMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UnramifiedLocalEquality.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UnramifiedLocalEquality.lean#L62). References: EGA IV (17.4.7), “open nbhd U, f|U=g|U”.

> Two morphisms over `S` to a scheme unramified over `S` which have the same value and
> induce the same residue-field map at `x` agree on an open neighbourhood of `x`.

```lean
public theorem exists_open_eq_of_residueFieldMap_eq {S : Scheme.{u}} {X Y : Over S}
    (f g : X ⟶ Y) (x : X.left) [Unramified Y.hom]
    (hfg : f.left x = g.left x)
    (hκ : f.left.residueFieldMap x =
      (Y.left.residueFieldCongr hfg).hom ≫ g.left.residueFieldMap x) :
    ∃ U : X.left.Opens, x ∈ U ∧ U.ι ≫ f.left = U.ι ≫ g.left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.36, Tag 02G3](https://stacks.math.columbia.edu/tag/02G3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
