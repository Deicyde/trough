---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_and_isFlatOnFibre_iff, AlgebraicGeometry.Space.isFlatOverAtPoint_comp_and_isFlatOnFibreAtFieldValuedPoint_iff, AlgebraicGeometry.Space.isFlat_of_flatFibreCharts, AlgebraicGeometry.Space.isFlat_of_flatFibreCharts_of_isSurjective, AlgebraicGeometry.Space.isOpen_flatLocus_and_preimage_subset_flatLocus, AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_of_flat_quotient_pow, AlgebraicGeometry.Space.preimage_zeroLocus_subset_flatLocus_of_isFlatOver_adicFibre
statement: formalized
proof: formalized
---

# 76.24 Flatness over a Noetherian base

Section 76.24 of the Stacks Project, [Tag 08VN](https://stacks.math.columbia.edu/tag/08VN). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0APR, a theorem

[Tag 0APR](https://stacks.math.columbia.edu/tag/0APR) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_and_isFlatOnFibre_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleNoetherianFibreCriterion.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleNoetherianFibreCriterion.lean#L128). The attribute's comment: “The full equivalence, at a geometric point `x̄` of `X`: condition (1) is flatness of `F` over `Z` at `x̄` (condition (2) of Stacks 05VU for `X ⟶ Z`) together with the fibre condition read on geometric stalks as in part (1) of Stacks 05WY, and condition (2) is flatness of `Y` over `Z` at the image point of `ȳ` together with flatness of `F` over `Y` at `x̄`. Local Noetherianity of `X`, `Y`, `Z` is the étale-local scheme property; coherence of `F` is used only through finiteness of `F_{x̄}` over `𝒪_{X, x̄}`, which is hypothesised, so quasi-coherence of `F` is not assumed. NOT covered: the identification of the fibre condition with flatness of a pullback of `F` to a genuine fibre product over a field-valued representative of `z̄`, which is Stacks 05WY.”.

> **Stacks 0APR.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of algebraic spaces over `S`
> with `X`, `Y`, `Z` locally Noetherian, let `F` be an `𝒪_X`-module and let `x̄` be a geometric
> point of `X` whose geometric stalk `F_{x̄}` is a nonzero finite `𝒪_{X, x̄}`-module.  Then `F` is
> flat over `Z` at `x̄` and flat on the fibre over `z̄` relative to the fibre of `Y` exactly when
> `Y` is flat over `Z` at `ȳ` and `F` is flat over `Y` at `x̄`.
>
> Over the étale local rings `𝒪_{Z, z̄} → 𝒪_{Y, ȳ} → 𝒪_{X, x̄}` this is Stacks 00MP in one
> direction, and transitivity of flatness together with base change along
> `𝒪_{Y, ȳ} → 𝒪_{Y, ȳ}/𝔪_{z̄}𝒪_{Y, ȳ}` in the other.

```lean
theorem isFlatOverAtGeometricPoint_and_isFlatOnFibre_iff {X Y Z : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (g : Y ⟶ Z) (F : Modules.{u, m} B S hS X.1 X.2)
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hZ : HasEtaleLocalProperty B S hS Z.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (xbar : GeometricPoint B S hS X.1)
    (hfin : Module.Finite (etaleLocalRing B S hS X.1 xbar)
      (geometricModuleStalk B S hS X xbar F))
    (hne : Nontrivial (geometricModuleStalk B S hS X xbar F)) :
    (IsFlatOverAtGeometricPoint B S hS (f ≫ g) F xbar ∧
        IsFlatOnFibreAtGeometricPoint B S hS f g F xbar) ↔
      (IsFlatAt B S hS g.hom (geometricPointMap f.hom xbar).image ∧
        IsFlatOverAtGeometricPoint B S hS f F xbar)
```

**`AlgebraicGeometry.Space.isFlatOverAtPoint_comp_and_isFlatOnFibreAtFieldValuedPoint_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleNoetherianFibreCriterionFibreProduct.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleNoetherianFibreCriterionFibreProduct.lean#L89). The attribute's comment: “The full statement: flatness of F over Z and over Y at x is the definition of Stacks 05VV (IsFlatOverAtPoint), flatness of Y over Z at y is that of Stacks 03ML, and the fibre clause is flatness of the pullback of F to the fibre product Spec(K) x\_Z X over Spec(K) x\_Z Y at the K-point, for every field-valued representative of x (condition (2) of Stacks 05WY); F is coherent and X, Y, Z are locally Noetherian.”.

> **Stacks 0APR.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian
> algebraic spaces over `S`, let `F` be a coherent `𝒪_X`-module and let `x ∈ |X|`, with image
> `y ∈ |Y|`.  Suppose `F_{x̄} ≠ 0` for a geometric point `x̄` of `X` over `x`.  Then for every
> field-valued point `Spec(K) ⟶ X` in the class of `x` the following are equivalent:
>
> 1. `F` is flat over `Z` at `x`, and the pullback of `F` to the fibre `X_z = Spec(K) ×_Z X` over
>    the image `z` of the point is flat over `Y_z = Spec(K) ×_Z Y` at the `K`-rational point of
>    `X_z`;
> 2. `Y` is flat over `Z` at `y`, and `F` is flat over `Y` at `x`.
>
> Flatness at a point is the definition of Stacks 05VV for modules and of Stacks 03ML for
> morphisms.

```lean
theorem isFlatOverAtPoint_comp_and_isFlatOnFibreAtFieldValuedPoint_iff
    {X Y Z : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (F : Modules.{u, u} B S hS X.1 X.2) [IsCoherent B S hS X.1 X.2 F]
    (hX : HasEtaleLocalProperty B S hS X.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (hZ : HasEtaleLocalProperty B S hS Z.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (x : points B S hS X.1) (xbar : GeometricPoint B S hS X.1) (hxbar : xbar.LiesOver x)
    (hne : Nontrivial (geometricModuleStalk B S hS X xbar F))
    (p : FieldValuedPoint B S hS X.1) (hp : p.class B S hS X.1 = x) :
    (IsFlatOverAtPoint B S hS X.2 (f ≫ g).hom F x ∧
        IsFlatOnFibreAtFieldValuedPoint B S hS f g p F) ↔
      (IsFlatAt B S hS g.hom (pointsMap B S hS X.1 f.hom x) ∧
        IsFlatOverAtPoint B S hS X.2 f.hom F x)
```

## Tag 0APS, a lemma

[Tag 0APS](https://stacks.math.columbia.edu/tag/0APS) in the Stacks Project.

**`AlgebraicGeometry.Space.isFlat_of_flatFibreCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseCriterion.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseCriterion.lean#L208). The attribute's comment: “conclusion (A): flatness of the morphism; hypothesis (3) in its every-étale-chart reading `AlgebraicGeometry.Space.HasFlatFibreCharts`”.

> **Stacks Project, Tag 0APS, conclusion (A).** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms
> of algebraic spaces over a scheme `S`. If `X`, `Y`, `Z` are locally Noetherian, `X` is flat
> over `Z`, and the fibres of `X` over the points of `Z` are flat over the corresponding fibres
> of `Y` in the chart sense of `AlgebraicGeometry.Space.HasFlatFibreCharts`, then `f` is
> flat.

```lean
theorem isFlat_of_flatFibreCharts
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hXn : HasEtaleLocalProperty B S hS X
      (fun A : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian A))
    (hYn : HasEtaleLocalProperty B S hS Y
      (fun A : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian A))
    (hZn : HasEtaleLocalProperty B S hS Z
      (fun A : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian A))
    (hflat : IsFlat B S hS (f ≫ g)) (hfib : HasFlatFibreCharts B S hS f g) :
    IsFlat B S hS f
```

**`AlgebraicGeometry.Space.isFlat_of_flatFibreCharts_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseCriterion.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatFibrewiseCriterion.lean#L230). The attribute's comment: “conclusion (B): flatness of the target over the base for surjective `f`; hypothesis (3) in its every-étale-chart reading `AlgebraicGeometry.Space.HasFlatFibreCharts`”.

> **Stacks Project, Tag 0APS, conclusion (B).** In the situation of
> `AlgebraicGeometry.Space.isFlat_of_flatFibreCharts`, if `f` is in addition surjective then `Y`
> is flat over `Z`.

```lean
theorem isFlat_of_flatFibreCharts_of_isSurjective
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hXn : HasEtaleLocalProperty B S hS X
      (fun A : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian A))
    (hYn : HasEtaleLocalProperty B S hS Y
      (fun A : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian A))
    (hZn : HasEtaleLocalProperty B S hS Z
      (fun A : Scheme.{u} => _root_.AlgebraicGeometry.IsLocallyNoetherian A))
    (hflat : IsFlat B S hS (f ≫ g)) (hfib : HasFlatFibreCharts B S hS f g)
    (hfs : IsSurjective B S hS f) :
    IsFlat B S hS g
```

## Tag 08VP, a lemma

[Tag 08VP](https://stacks.math.columbia.edu/tag/08VP) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpen_flatLocus_and_preimage_subset_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatLocusAdicThickenings.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatLocusAdicThickenings.lean#L576).

> **Stacks 08VP.**  Let `A` be a Noetherian ring, `I ⊆ A` an ideal, and `X` an algebraic space
> locally of finite presentation over `S = Spec A`.  For `n ≥ 0` let `Xₙ = Spec(A/Iⁿ⁺¹) ×_S X` be
> the adic fibres, and let `F` be a coherent `𝒪_X`-module whose pullback `Fₙ` to every `Xₙ` is flat
> over `Spec(A/Iⁿ⁺¹)`.  Then the locus of points of `|X|` where `F` is flat over `S` is open, and it
> contains the inverse image of `V(I) = |Spec(A/I)|` under `|X| ⟶ |S|`.
>
> The source's thickenings are indexed by `n ≥ 1` and are `Spec(A/Iⁿ)`; here they are indexed by
> `n ≥ 0` and are `Spec(A/Iⁿ⁺¹)`, the convention of `AlgebraicGeometry.Space.adicFibre`.  The
> flatness of `Fₙ` is Stacks 05VV for the projection `Xₙ ⟶ Spec(A/Iⁿ⁺¹)`, and the flat locus is
> `AlgebraicGeometry.Space.flatLocus` of Stacks 05VV (1).  Openness is Stacks 05WV.
>
> At a geometric point `x̄` above `V(I)` the proof follows the source's reduction to Stacks 0523,
> carried out on étale local rings rather than on an affine étale chart: `x̄` lifts to every `Xₙ`,
> flatness of the stalks of `Fₙ` gives flatness of `(A/Iⁿ⁺¹) ⊗_A F_{x̄}` over `A/Iⁿ⁺¹`
> (`AlgebraicGeometry.Space.flat_quotient_tensor_geometricModuleStalk`), and Stacks 0523 over the
> Noetherian ring `A`, applied to the finite module `F_{x̄}` over the Noetherian local ring
> `𝒪_{X, x̄}`, gives flatness over `A`, hence over the weakly étale `A`-algebra `𝒪_{S, ȳ}`.

```lean
theorem isOpen_flatLocus_and_preimage_subset_flatLocus [IsNoetherianRing A]
    (X : AlgebraicSpaces B (Spec (.of A)) hA) (f : X ⟶ schemeSpace (baseObject A B hA))
    (hf : IsLocallyOfFinitePresentation B (Spec (.of A)) hA f.hom)
    (F : Modules.{u, u} B (Spec (.of A)) hA X.1 X.2) [IsCoherent B (Spec (.of A)) hA X.1 X.2 F]
    (hflat : ∀ n : ℕ, IsFlatOver B (Spec (.of A)) hA (adicFibreSpaceOf A I B hA X f n).2
      (adicFibreProjection A I B hA X f n).hom
      ((modulePullback B (Spec (.of A)) hA (adicFibreInclusion A I B hA X f n)).obj F)) :
    IsOpen (flatLocus B (Spec (.of A)) hA X.2 f.hom F) ∧
      pointsMap B (Spec (.of A)) hA X.1 f.hom ⁻¹'
          Set.range (pointsMap B (Spec (.of A)) hA
            (yoneda.obj (adicThickeningObject A I B hA (contains_adicThickening A I B hA) 0))
            (yoneda.map (adicThickeningMap A I B hA (contains_adicThickening A I B hA) 0))) ⊆
        flatLocus B (Spec (.of A)) hA X.2 f.hom F
```

**`AlgebraicGeometry.Space.isFlatOverAtGeometricPoint_of_flat_quotient_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAdicThickenings.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAdicThickenings.lean#L116). The attribute's comment: “the local step at a geometric point lying over V(J)”.

> **The local step of Stacks 08VP.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over
> `S`, let `F` be an `𝒪_X`-module and let `x̄` be a geometric point of `X` whose étale local ring
> `T = 𝒪_{X, x̄}` and whose image's étale local ring `R = 𝒪_{Y, ȳ}` are Noetherian, with geometric
> stalk `M = F_{x̄}` finite over `T`.  Let `J ⊆ R` be an ideal whose image in `T` is a proper
> ideal, which is the condition that `x̄` lies over `V(J)`.  If `M/JⁿM` is flat over `R/Jⁿ` for
> every `n ≥ 1`, then `F` is flat over `Y` at `x̄`.
>
> The scalars of `M` over `R` are restricted along the canonical homomorphism of étale local
> rings `AlgebraicGeometry.Space.etaleLocalRingMap` of Stacks 04NG, as they are in the conclusion
> `AlgebraicGeometry.Space.IsFlatOverAtGeometricPoint`.
>
> The statement does not include the openness of the flat locus (Stacks 05WV), the identification
> of the hypothesis with flatness of the pullbacks `F_n` to the thickenings `X_n` (Stacks 05VQ), or
> the passage from the base ring `A` and its ideal `I` to the étale local ring of the base.

```lean
theorem isFlatOverAtGeometricPoint_of_flat_quotient_pow
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (F : Modules.{u, m} B S hS X.1 X.2) (xbar : GeometricPoint B S hS X.1)
    [IsNoetherianRing (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar))]
    [IsNoetherianRing (etaleLocalRing B S hS X.1 xbar)]
    [Module.Finite (etaleLocalRing B S hS X.1 xbar) (geometricModuleStalk B S hS X xbar F)]
    (J : Ideal (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar)))
    (hJ : J.map (etaleLocalRingMap X.2 f.hom xbar) ≠ ⊤)
    (hflat : ∀ n : ℕ, 1 ≤ n →
      letI : Module (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar))
          (geometricModuleStalk B S hS X xbar F) :=
        Module.compHom _ (etaleLocalRingMap X.2 f.hom xbar)
      Module.Flat (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar) ⧸ J ^ n)
        (geometricModuleStalk B S hS X xbar F ⧸
          (J ^ n • (⊤ : Submodule (etaleLocalRing B S hS Y.1 (geometricPointMap f.hom xbar))
            (geometricModuleStalk B S hS X xbar F))))) :
    IsFlatOverAtGeometricPoint B S hS f F xbar
```

**`AlgebraicGeometry.Space.preimage_zeroLocus_subset_flatLocus_of_isFlatOver_adicFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAdicThickeningsFibre.lean, line 601](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatModuleAdicThickeningsFibre.lean#L601).

> **Stacks 08VP.**  Let `A` be a Noetherian ring, let `I ⊆ A` be an ideal and let `X` be an
> algebraic space locally of finite presentation over `S = Spec A`.  For `n ≥ 1` set
> `S_n = Spec (A / Iⁿ)` and `X_n = S_n ×_S X`, and let `F` be a coherent `𝒪_X`-module.  If for
> every `n ≥ 1` the pullback `F_n` of `F` to `X_n` is flat over `S_n`, then the locus where `F` is
> flat over `S` is open and contains the inverse image of `V(I)` under `X → S`.
>
> The openness is Stacks 05WV,
> `AlgebraicGeometry.Space.isOpen_flatLocus_of_isFinitePresentationOnCharts`, a coherent module
> being of finite presentation.  Here `X_n` is `AlgebraicGeometry.Space.adicFibreSpace`, the fibre
> product of algebraic spaces `X ×_S S_n` with `S_n = Spec (A / I^{n+1})` for `n : ℕ`, so that `n`
> runs over the exponents `≥ 1`; `F_n` is the pullback of modules
> `AlgebraicGeometry.Space.modulePullback` along the projection
> `AlgebraicGeometry.Space.adicFibreFst`; flatness over `S_n` is `AlgebraicGeometry.Space.IsFlatOver`
> of Stacks 05VV along `AlgebraicGeometry.Space.adicFibreSnd`; coherence is
> `AlgebraicGeometry.Space.IsCoherent` of Stacks 07UA; and the locus is
> `AlgebraicGeometry.Space.flatLocus`.

```lean
theorem preimage_zeroLocus_subset_flatLocus_of_isFlatOver_adicFibre [IsNoetherianRing A]
    (hf : IsLocallyOfFinitePresentation B (Spec (.of A)) hA f)
    (F : Modules.{u, u} B (Spec (.of A)) hA X hX) [IsCoherent B (Spec (.of A)) hA X hX F]
    (hflat : ∀ n : ℕ, IsFlatOver B (Spec (.of A)) hA (adicFibreSpace A I B hA hX f n).2
      (adicFibreSnd A I B hA f n)
      ((modulePullback B (Spec (.of A)) hA (adicFibreFst A I B hA hX f n)).obj F)) :
    IsOpen (flatLocus B (Spec (.of A)) hA hX f F) ∧
      (fun x => pointsToScheme B (Spec (.of A)) hA (baseObject A B hA)
          (pointsMap B (Spec (.of A)) hA X f x)) ⁻¹'
        PrimeSpectrum.zeroLocus (I : Set A) ⊆
        flatLocus B (Spec (.of A)) hA hX f F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.24, Tag 08VN](https://stacks.math.columbia.edu/tag/08VN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
