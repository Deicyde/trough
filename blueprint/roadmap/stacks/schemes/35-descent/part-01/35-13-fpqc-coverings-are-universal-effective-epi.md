---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.pullbackComparison_forget_self_surjective, AlgebraicGeometry.quasicoherentSectionsEqualizer_iff_isUniversalEffectiveEpiFamily, AlgebraicGeometry.jointlySurjective_of_isUniversalEffectiveEpiFamily, AlgebraicGeometry.exists_preimage_of_isUniversalEffectiveEpiFamily, AlgebraicGeometry.isUniversalEffectiveEpiFamily_of_affine_baseChange, AlgebraicGeometry.isUniversalEffectiveEpiFamily_of_affine_of_submersive, AlgebraicGeometry.existsUnique_isOpen_preimage_eq_of_mem_fpqcPrecoverage, AlgebraicGeometry.existsUnique_isOpen_preimage_eq_of_flat_of_quasiCompact_of_surjective
statement: formalized
proof: formalized
---

# 35.13 Fpqc coverings are universal effective epimorphisms

Section 35.13 of the Stacks Project, [Tag 023P](https://stacks.math.columbia.edu/tag/023P). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02KI, a lemma

[Tag 02KI](https://stacks.math.columbia.edu/tag/02KI) in the Stacks Project.

**`AlgebraicGeometry.Scheme.pullbackComparison_forget_self_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/Points.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/Points.lean#L43).

> **Stacks 02KI.** For a morphism of schemes `f : X ⟶ S` the natural map
> `|X ×_S X| → |X| ×_{|S|} |X|` of underlying sets is surjective.

```lean
public theorem pullbackComparison_forget_self_surjective {X S : Scheme.{u}} (f : X ⟶ S) :
    Function.Surjective (pullbackComparison forget f f)
```

## Tag 0EUA, a lemma

[Tag 0EUA](https://stacks.math.columbia.edu/tag/0EUA) in the Stacks Project.

**`AlgebraicGeometry.quasicoherentSectionsEqualizer_iff_isUniversalEffectiveEpiFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/QuasicoherentSectionsEqualizer/UniversalEffectiveEpi.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/QuasicoherentSectionsEqualizer/UniversalEffectiveEpi.lean#L787).

> **Stacks Project, Tag 0EUA.** A family of morphisms of affine schemes satisfies the
> global-section equalizer condition for every quasi-coherent module if and only if it is a
> universal effective epimorphic family in the category of affine schemes.

```lean
theorem quasicoherentSectionsEqualizer_iff_isUniversalEffectiveEpiFamily
    {I : Type w} (X : AffineScheme.{u}) (U : I → AffineScheme.{u})
    (f : ∀ i, U i ⟶ X) :
    IsQuasicoherentSectionsEqualizer X U f ↔
      StacksEffectiveEpi.IsUniversalEffectiveEpiFamily U f
```

## Tag 0EUB, a lemma

[Tag 0EUB](https://stacks.math.columbia.edu/tag/0EUB) in the Stacks Project.

**`AlgebraicGeometry.jointlySurjective_of_isUniversalEffectiveEpiFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/Surjective.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/Surjective.lean#L56). The attribute's comment: “schemes\_surjective”. References: SGA 3 IV (6.7.2), “univ. eff. epi ⇒ surj”; SGA 3 IV (1.3), “special case”.

> A universal effective epimorphic family of schemes is jointly surjective
> on the underlying spaces.

```lean
theorem jointlySurjective_of_isUniversalEffectiveEpiFamily
    {I : Type w} {X : Scheme.{u}} (U : I → Scheme.{u})
    (f : ∀ i, U i ⟶ X)
    (h : StacksEffectiveEpi.IsUniversalEffectiveEpiFamily U f) :
    ∀ x : X, ∃ i, x ∈ Set.range (f i)
```

**`AlgebraicGeometry.exists_preimage_of_isUniversalEffectiveEpiFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/Surjective.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/Surjective.lean#L74). The attribute's comment: “affine\_schemes\_surjective”. References: SGA 3 IV (6.7.2), “affine case”.

> A universal effective epimorphic family of affine schemes is jointly surjective.

```lean
theorem exists_preimage_of_isUniversalEffectiveEpiFamily
    {I : Type w} (X : AffineScheme.{u}) (U : I → AffineScheme.{u})
    (f : ∀ i, U i ⟶ X)
    (h : StacksEffectiveEpi.IsUniversalEffectiveEpiFamily U f) :
    ∀ x : X.obj, ∃ (i : I) (y : (U i).obj),
      (AffineScheme.forgetToScheme.map (f i)) y = x
```

## Tag 0EUC, a lemma

[Tag 0EUC](https://stacks.math.columbia.edu/tag/0EUC) in the Stacks Project.

**`AlgebraicGeometry.isUniversalEffectiveEpiFamily_of_affine_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/AffineBase.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/AffineBase.lean#L100).

> A family of morphisms of schemes is universally effective epimorphic if all its
> base changes to affine schemes are effective epimorphic families.

```lean
theorem isUniversalEffectiveEpiFamily_of_affine_baseChange
    {I : Type w} {X : Scheme.{u}} (X' : I → Scheme.{u}) (f : ∀ i, X' i ⟶ X)
    (h : ∀ (Y : Scheme.{u}) [IsAffine Y] (g : Y ⟶ X),
      StacksEffectiveEpi.IsEffectiveEpiFamily
        (fun i => pullback (f i) g) (fun i => pullback.snd (f i) g)) :
    StacksEffectiveEpi.IsUniversalEffectiveEpiFamily X' f
```

## Tag 0EUD, a lemma

[Tag 0EUD](https://stacks.math.columbia.edu/tag/0EUD) in the Stacks Project.

**`AlgebraicGeometry.isUniversalEffectiveEpiFamily_of_affine_of_submersive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/FromAffine.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/FromAffine.lean#L403).

> **Stacks Project, Tag 0EUD.** A universally effective epimorphic family of affine
> schemes whose every affine base change is submersive is a universally effective
> epimorphic family in schemes.

```lean
public theorem isUniversalEffectiveEpiFamily_of_affine_of_submersive
    {I : Type w} (X : AffineScheme.{u}) (U : I → AffineScheme.{u})
    (f : ∀ i, U i ⟶ X)
    (h_affine : StacksEffectiveEpi.IsUniversalEffectiveEpiFamily U f)
    (h_submersive : ∀ (Y : Scheme.{u}) [IsAffine Y] (g : Y ⟶ X.obj),
      Topology.IsQuotientMap
        (fun p : Σ i : I,
            (pullback (AffineScheme.forgetToScheme.map (f i)) g : Scheme.{u}) =>
          (pullback.snd (AffineScheme.forgetToScheme.map (f p.1)) g).base p.2)) :
    StacksEffectiveEpi.IsUniversalEffectiveEpiFamily
      (fun i => (U i).obj) (fun i => AffineScheme.forgetToScheme.map (f i))
```

## Tag 03N0, a lemma

[Tag 03N0](https://stacks.math.columbia.edu/tag/03N0) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_isOpen_preimage_eq_of_mem_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/OpenSubsetFpqc.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/OpenSubsetFpqc.lean#L202). References: SGA 1 VIII (4.4), “more general”.

> **Stacks 03N0.** Let `{f i : X i ⟶ T}` be an fpqc covering of schemes and let `W i` be an
> open subset of `X i` for each `i`, such that the two projections of `X i ×_T X j` pull `W i` and
> `W j` back to the same open subset for all `i` and `j`. Then there is a unique open subset `V`
> of `T` whose inverse image in `X i` is `W i` for every `i`.

```lean
theorem existsUnique_isOpen_preimage_eq_of_mem_fpqcPrecoverage {I : Type v} {T : Scheme.{u}}
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage T)
    (W : ∀ i, (X i).Opens)
    (hW : ∀ i j, pullback.fst (f i) (f j) ⁻¹ᵁ W i = pullback.snd (f i) (f j) ⁻¹ᵁ W j) :
    ∃! V : T.Opens, ∀ i, f i ⁻¹ᵁ V = W i
```

**`AlgebraicGeometry.existsUnique_isOpen_preimage_eq_of_flat_of_quasiCompact_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/OpenSubsetSingleMorphism.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/OpenSubsetSingleMorphism.lean#L60). The attribute's comment: “covering by a single surjective flat quasi-compact morphism”.

> **An open subset descends along a surjective flat quasi-compact morphism.** Let
> `f : T' ⟶ T` be a surjective, flat, quasi-compact morphism of schemes and let `W' ⊆ T'` be open
> with `pr₀⁻¹(W') = pr₁⁻¹(W')` in `T' ×_T T'`. Then there is a unique open `W ⊆ T` with
> `W' = f⁻¹(W)`.

```lean
theorem existsUnique_isOpen_preimage_eq_of_flat_of_quasiCompact_of_surjective {W' : Set T'}
    (hW' : IsOpen W')
    (hcompat : (pullback.fst f f).base ⁻¹' W' = (pullback.snd f f).base ⁻¹' W') :
    ∃! W : Set T, IsOpen W ∧ f.base ⁻¹' W = W'
```

**`AlgebraicGeometry.existsUnique_opens_preimage_eq_of_flat_of_quasiCompact_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/OpenSubsetSingleMorphism.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/OpenSubsetSingleMorphism.lean#L78). The attribute's comment: “covering by a single surjective flat quasi-compact morphism, as open subschemes”.

> **An open subscheme descends along a surjective flat quasi-compact morphism.** For
> `f : T' ⟶ T` surjective, flat and quasi-compact, an open subscheme `W'` of `T'` whose two
> preimages in `T' ×_T T'` agree is the preimage of a unique open subscheme of `T`.

```lean
theorem existsUnique_opens_preimage_eq_of_flat_of_quasiCompact_of_surjective (W' : T'.Opens)
    (hcompat : (pullback.fst f f).base ⁻¹' (W' : Set T') =
      (pullback.snd f f).base ⁻¹' (W' : Set T')) :
    ∃! W : T.Opens, f ⁻¹ᵁ W = W'
```

## Tag 023Q, a lemma

[Tag 023Q](https://stacks.math.columbia.edu/tag/023Q) in the Stacks Project.

**`isUniversalEffectiveEpi_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Representable/EffectiveEpiFamily.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Representable/EffectiveEpiFamily.lean#L365). The attribute's comment: “every fpqc covering family of schemes is a universal effective epimorphism, in the unpacked equalizer form of Stacks 00WP: along every base change of the family, a morphism to any scheme is determined by, and glues from, a pullback-compatible family on the members”. References: SGA 1 VIII (5.3), “more general”; SGA 3 IV (3.4), “more general”; SGA 3 IV (6.3.1), “(iii), fpqc case (T1)”; SGA 3 IX (5.4), “more general”; SGA 3 XI (3.9), “partial”.

> **Main statement (Stacks Tag 023Q).**
> Every fpqc covering of schemes is a universal effective epimorphism in the category of
> schemes.

```lean
theorem isUniversalEffectiveEpi_of_isFpqcCovering
    {ι : Type*} {T : Scheme} (T' : ι → Scheme) (f : ∀ i, T' i ⟶ T)
    (hf : IsFpqcCoveringFamily T' f) :
    IsUniversalEffectiveEpi T' f
```

## Tag 0BMN, a lemma

[Tag 0BMN](https://stacks.math.columbia.edu/tag/0BMN) in the Stacks Project.

**`AlgebraicGeometry.isColimit_cofork_of_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/FpqcCoequalizer.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/EffectiveEpi/FpqcCoequalizer.lean#L65).

> **Stacks Project, Tag 0BMN.** A coequalizer of schemes can be checked after an fpqc
> covering provided it is also a coequalizer on every pairwise overlap.

```lean
theorem isColimit_cofork_of_fpqc {X Y Z : Scheme.{u}} (a b : X ⟶ Y) (c : Y ⟶ Z)
    (h : a ≫ c = b ≫ c) {I : Type v} (Z' : I → Scheme.{u}) (f : ∀ i, Z' i ⟶ Z)
    (hfpqc : Presieve.ofArrows Z' f ∈ Scheme.fpqcPrecoverage Z)
    (hlocal : ∀ i, Nonempty (IsColimit (baseChangeCofork a b c h (f i))))
    (hoverlap : ∀ i j, Nonempty (IsColimit
      (baseChangeCofork a b c h (pullback.fst (f i) (f j) ≫ f i)))) :
    Nonempty (IsColimit (Cofork.ofπ c h))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.13, Tag 023P](https://stacks.math.columbia.edu/tag/023P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
