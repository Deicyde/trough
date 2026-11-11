---
declaration: section
origin: cited
lean: AlgebraicGeometry.colimit_sections_equiv_sections_iInter, AlgebraicGeometry.exists_iInter_iso_iInter_in_specΓ, AlgebraicGeometry.isOpen_image_toΓSpec_of_isOpen, AlgebraicGeometry.sectionsRingOnSubset_preimage_iInter_iso_pushout, AlgebraicGeometry.isPushout_sectionsRingOnSubset_of_flat, AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isIndQuasiAffineHom_of_anyIndex, AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isIndQuasiAffineHom, AlgebraicGeometry.DescentDatum.isEffective_of_isIndQuasiAffineHom_of_quasiCompact
statement: formalized
proof: formalized
---

# 40.15 Descending ind-quasi-affine morphisms

Section 40.15 of the Stacks Project, [Tag 0APG](https://stacks.math.columbia.edu/tag/0APG). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0APH, an equation

[Tag 0APH](https://stacks.math.columbia.edu/tag/0APH) in the Stacks Project.

**`AlgebraicGeometry.colimit_sections_equiv_sections_iInter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SectionsOnIntersection.lean, line 756](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/SectionsOnIntersection.lean#L756).

> Sections on the intersection of a nonempty directed family of
> quasi-compact opens of a quasi-separated scheme are the filtered colimit of
> the sections on those opens.  The equivalence commutes with every canonical
> map from a stage.

```lean
theorem colimit_sections_equiv_sections_iInter
    {X : AlgebraicGeometry.Scheme.{u}} {I : Type u}
    [QuasiSeparatedSpace X] [Nonempty I]
    (F : X.toTopCat.Sheaf (Type u)) (U : I → Opens X)
    (hqc : ∀ i, IsCompact (U i : Set X))
    (hdir : ∀ i j, ∃ k, (U k : Set X) ⊆ U i ∩ U j) (E : Set X)
    (hE : E = ⋂ i, (U i : Set X)) :
    ∃ e : colimit (sectionsDiagram F U) ≃ sectionsOnSubset E F,
      ∀ (i : intersectionIndex U) (s : (sectionsDiagram F U).obj i),
        e (colimit.ι (sectionsDiagram F U) i s) =
          stageToSubset F U E
            (fun j ↦ by rw [hE]; exact Set.iInter_subset _ j) i s
```

## Tag 0API, a lemma

[Tag 0API](https://stacks.math.columbia.edu/tag/0API) in the Stacks Project.

**`AlgebraicGeometry.exists_iInter_iso_iInter_in_specΓ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/IntersectionEmbedding.lean, line 1166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/IntersectionEmbedding.lean#L1166). The attribute's comment: “intersection\_embedding”.

> **Stacks Project, Tag 0API.** The canonical map from a nonempty intersection
> of quasi-compact opens in an ind-quasi-affine scheme to the spectrum of its ring
> of sections identifies it, as a locally ringed space, with an intersection of
> quasi-compact opens in that spectrum.  Each comparison map to the spectrum of a
> stage is the spectrum of the restriction map of functions from that stage.

```lean
theorem exists_iInter_iso_iInter_in_specΓ
    {X : Scheme.{u}} [AlgebraicGeometry.IsIndQuasiAffine X]
    {I : Type v} [Nonempty I] (U : I → X.Opens)
    (hU : ∀ i, IsCompact (U i : Set X)) :
    let E : Set X := ⋂ i, (U i : Set X)
    let Z := subsetLocallyRingedSpace X.toLocallyRingedSpace E
    let Y := Spec.toLocallyRingedSpace.obj (op (LocallyRingedSpace.Γ.obj (op Z)))
    ∃ (p : ∀ i, Y ⟶ Spec.toLocallyRingedSpace.obj (op Γ(X, U i)))
      (V : I → Opens Y),
      (∀ i, IsCompact (V i : Set Y)) ∧
      (∀ i, (V i : Set Y) = (p i).base ⁻¹' Set.range (U i).toSpecΓ.base) ∧
      (∀ i (x : E), (p i).base (Z.toΓSpec.base x) =
        (U i).toSpecΓ.base ⟨x.1, Set.mem_iInter.mp x.2 i⟩) ∧
      (∀ i (W : Set X), IsOpen W → W ⊆ E →
        (p i).base ⁻¹' ((U i).toSpecΓ.base ''
          {x : U i | (x : X) ∈ W}) =
        Z.toΓSpec.base '' {x : E | (x : X) ∈ W}) ∧
      (∀ i, p i = (Scheme.Spec.map (X.openToSubset (U i) E
        (Set.iInter_subset (fun k ↦ (U k : Set X)) i)).op).toLRSHom) ∧
      ∃ e : Z ≅ subsetLocallyRingedSpace Y (⋂ i, (V i : Set Y)),
          e.hom.toHom ≫ ofSubset Y (⋂ i, (V i : Set Y)) =
            (identityToΓSpec.app Z).toHom
```

**`AlgebraicGeometry.isOpen_image_toΓSpec_of_isOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/IntersectionEmbedding.lean, line 1249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/IntersectionEmbedding.lean#L1249). The attribute's comment: “open\_image”.

> **Stacks Project, Tag 0API (open image).** The canonical map from an intersection of a
> nonempty family of quasi-compact opens in an ind-quasi-affine scheme to the spectrum of its
> global sections sends subsets which are open in the ambient scheme to open subsets.

```lean
theorem isOpen_image_toΓSpec_of_isOpen
    (X : Scheme.{u}) [AlgebraicGeometry.IsIndQuasiAffine X]
    {I : Type v} [Nonempty I] (U : I → X.Opens)
    (hU : ∀ i, IsCompact (U i : Set X))
    (E W : Set X) (hE : E = ⋂ i, (U i : Set X))
    (hWE : W ⊆ E) (hW : IsOpen W) :
    IsOpen
      ((subsetLocallyRingedSpace
          X.toLocallyRingedSpace E).toΓSpec.base ''
        { x : E | (x : X) ∈ W })
```

## Tag 0APJ, a lemma

[Tag 0APJ](https://stacks.math.columbia.edu/tag/0APJ) in the Stacks Project.

**`AlgebraicGeometry.sectionsRingOnSubset_preimage_iInter_iso_pushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/IndQuasiAffineDescent.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/IndQuasiAffineDescent.lean#L177).

> **Stacks Project, Tag 0APJ.** In a cartesian square of schemes over the affine schemes
> `Spec B ⟶ Spec A`, where `A ⟶ B` is flat, formation of sections over a nonempty intersection of
> quasi-compact opens commutes with base change.

```lean
theorem sectionsRingOnSubset_preimage_iInter_iso_pushout
    {A B : CommRingCat.{u}} (φ : A ⟶ B) {X Y : Scheme.{u}}
    (g : X ⟶ Scheme.Spec.obj (op B)) (f : X ⟶ Y)
    (h : Y ⟶ Scheme.Spec.obj (op A))
    (H : IsPullback g f (Scheme.Spec.map φ.op) h)
    {ι : Type v} [Nonempty ι] (V : ι → Y.Opens)
    (hV : ∀ i, IsCompact (V i : Set Y)) [QuasiSeparatedSpace Y]
    (hφ : φ.hom.Flat) :
    ∃ e : pushout (toSectionsOnSubset h (⋂ i, (V i : Set Y))) φ ≅
        X.sectionsRingOnSubset (f ⁻¹' (⋂ i, (V i : Set Y))),
      (pushout.inr _ _ ≫ e.hom =
        toSectionsOnSubset g (f ⁻¹' (⋂ i, (V i : Set Y)))) ∧
      (∀ (U : Y.Opens) (hU : (⋂ i, (V i : Set Y)) ⊆ U),
        Y.restrictOpenToSubset (⋂ i, (V i : Set Y)) U hU ≫
            pushout.inl _ _ ≫ e.hom =
          f.appLE U (f ⁻¹ᵁ U) le_rfl ≫
            X.restrictOpenToSubset (f ⁻¹' (⋂ i, (V i : Set Y))) (f ⁻¹ᵁ U) (by
              intro x hx
              exact Set.mem_preimage.mpr (hU (Set.mem_preimage.mp hx))))
```

**`AlgebraicGeometry.isPushout_sectionsRingOnSubset_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/FlatBaseChangeOnIntersection.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/FlatBaseChangeOnIntersection.lean#L315).

> Let
> ```
>   X ---k---→ Spec R
>   |            |
>   p            g
>   ↓            ↓
>   Y ---πY--→ Spec A
> ```
> be a Cartesian diagram of schemes, let `E ⊆ Y` be an intersection of a nonempty family of
> quasi-compact opens of `Y`, and suppose that `Y` is quasi-separated and that `g` is flat. Then
> ```
> Γ(p⁻¹E, 𝒪_X|_{p⁻¹E}) = Γ(E, 𝒪_Y|_E) ⊗_{Γ(Spec A, ⊤)} Γ(Spec R, ⊤) :
> ```
> the square formed by the restrictions of the global functions of `Spec A` and of `Spec R` to `E`
> and to `p⁻¹E` is a pushout of rings.
>
> The comparison morphism `Γ(E, 𝒪_Y|_E) ⟶ Γ(p⁻¹E, 𝒪_X|_{p⁻¹E})` is produced by the statement and
> characterized by the second conjunct: it agrees with the restriction along `p` on each member of
> the given family.

```lean
theorem isPushout_sectionsRingOnSubset_of_flat {A R : CommRingCat.{u}} {Y X : Scheme.{u}}
    {πY : Y ⟶ Spec A} {g : Spec R ⟶ Spec A} {p : X ⟶ Y} {k : X ⟶ Spec R}
    (H : IsPullback p k πY g) [Flat g] [QuasiSeparatedSpace Y] {I : Type u} [Nonempty I]
    (V : I → Y.Opens) (hV : ∀ i, IsCompact (V i : Set Y))
    (E : Set Y) (hE : E = ⋂ i, (V i : Set Y)) :
    ∃ w : Y.sectionsRingOnSubset E ⟶ X.sectionsRingOnSubset (p.base ⁻¹' E),
      IsPushout (πY.appTop ≫ Y.topToSubset E) g.appTop w
          (k.appTop ≫ X.topToSubset (p.base ⁻¹' E)) ∧
        ∀ i : I,
          Y.stageToSubset V E (fun j ↦ hE ▸ Set.iInter_subset _ j) ⟨i⟩ ≫ w =
            p.appLE (V i) (p ⁻¹ᵁ V i) le_rfl ≫
              X.stageToSubset (fun j ↦ p ⁻¹ᵁ V j) (p.base ⁻¹' E)
                (fun j ↦ hE ▸ Set.preimage_mono (Set.iInter_subset _ j)) ⟨i⟩
```

## Tag 0APK, a lemma

[Tag 0APK](https://stacks.math.columbia.edu/tag/0APK) in the Stacks Project.

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isIndQuasiAffineHom_of_anyIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcEffective.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcEffective.lean#L119). References: SGA 1 VIII (7.9), “partial”; SGA 3 IX (2.3), “partial”; SGA 3 VIII (1.7.2), “more general”; SGA 3 X (5.4), “more general”; SGA 3 XI (4.2), “partial”; SGA 3 XXIV (3.11.2), “partial”.

> **[Stacks, Tag 0APK](https://stacks.math.columbia.edu/tag/0APK), Gabber's theorem.** Let `S`
> be a scheme, let `{X i ⟶ S}` be an fpqc covering family, indexed by a type in an arbitrary
> universe, and let `D` be a descent datum relative to it each of whose component morphisms
> `V i ⟶ X i` is ind-quasi-affine. Then `D` is effective: it is isomorphic to the canonical descent
> datum of a scheme over `S`.
>
> Ind-quasi-affineness is stable under base change, Stacks 0AP7, and closed under finite disjoint
> unions, so the general-base fpqc reduction of Stacks 02W3,
> `AlgebraicGeometry.DescentData.isFamilyEffective_fpqc_of_affineSingleton_of_anyIndex`, reduces
> the statement to the case of a surjective flat morphism of affine schemes, which is
> `AlgebraicGeometry.DescentDatum.isEffective_of_isIndQuasiAffineHom`.

```lean
theorem isFamilyEffective_of_forall_isIndQuasiAffineHom_of_anyIndex {ι : Type v} {S : Scheme.{u}}
    {X : ι → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData f) (hP : ∀ i, IsIndQuasiAffineHom (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isIndQuasiAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcEffective.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/IndQuasiAffineFpqcEffective.lean#L144). The attribute's comment: “the case of an affine base”. References: SGA 1 VIII (7.9), “special case”; SGA 3 IX (2.3), “partial”; SGA 3 VIII (1.7.2), “(ii), special case”; SGA 3 X (5.4), “special case”; SGA 3 XXIV (3.11.2), “partial”.

> **[Stacks, Tag 0APK](https://stacks.math.columbia.edu/tag/0APK) over an affine base.** Let `S`
> be an affine scheme, let `{X i ⟶ S}` be an fpqc covering family and let `D` be a descent datum
> relative to it each of whose component morphisms is ind-quasi-affine. Then `D` is effective: it is
> isomorphic to the canonical descent datum of a scheme over `S`.
>
> This is the special case of
> `AlgebraicGeometry.DescentData.isFamilyEffective_of_forall_isIndQuasiAffineHom_of_anyIndex` kept
> for the consumers taking this shape.

```lean
theorem isFamilyEffective_of_forall_isIndQuasiAffineHom {ι : Type u} {S : Scheme.{u}} [IsAffine S]
    {X : ι → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage S)
    (D : DescentData f) (hP : ∀ i, IsIndQuasiAffineHom (D.obj i).hom) :
    D.IsFamilyEffective
```

**`AlgebraicGeometry.DescentDatum.isEffective_of_isIndQuasiAffineHom_of_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SeparatedQuasiFiniteSchemeDescent.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SeparatedQuasiFiniteSchemeDescent.lean#L170). The attribute's comment: “the case of a one-member covering by a surjective flat quasi-compact morphism, over an arbitrary base”. References: SGA 1 VIII (7.8), “partial”; SGA 1 VIII (7.9), “partial”; SGA 3 X (5.4), “special case”; SGA 3 XI (4.2), “more general”.

> **Gabber's effectivity for ind-quasi-affine descent data along a single quasi-compact fpqc
> covering.** A descent datum relative to a surjective, flat, quasi-compact morphism `f : X ⟶ S`
> whose structure morphism `V ⟶ X` is ind-quasi-affine is effective.
>
> This is [Stacks, Tag 0APK](https://stacks.math.columbia.edu/tag/0APK) for a one-member covering,
> over an arbitrary base.

```lean
theorem isEffective_of_isIndQuasiAffineHom_of_quasiCompact {S X : Scheme.{u}} {f : X ⟶ S}
    [Surjective f] [Flat f] [QuasiCompact f] (D : DescentDatum f)
    (hiqa : IsIndQuasiAffineHom D.over.hom) : DescentData.IsEffective D
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.15, Tag 0APG](https://stacks.math.columbia.edu/tag/0APG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
