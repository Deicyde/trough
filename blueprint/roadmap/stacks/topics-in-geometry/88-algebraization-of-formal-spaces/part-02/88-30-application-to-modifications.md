---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsFiniteTypeModification, AlgebraicGeometry.Space.FiniteTypeModification, AlgebraicGeometry.Space.isFiniteTypeModification_iff, AlgebraicGeometry.FormalSpace.isEquivalence_affineModificationBaseChange, AlgebraicGeometry.FormalSpace.fpqcLocalProperties_iff_of_affineModificationBaseChange_obj_iso, AlgebraicGeometry.FormalSpace.isEquivalence_finiteTypeBaseChange_of_flat_localHom, AlgebraicGeometry.Space.exists_isAdmissibleBlowup_dominating_of_isLocalRing
statement: formalized
proof: formalized
---

# 88.30 Application to modifications

Section 88.30 of the Stacks Project, [Tag 0AS1](https://stacks.math.columbia.edu/tag/0AS1). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AS2, an equation

[Tag 0AS2](https://stacks.math.columbia.edu/tag/0AS2) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFiniteTypeModification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean#L113). The attribute's comment: “the three defining conditions”.

> **Stacks 0AS2.** An algebraic space over `W`, locally of finite type over `W` and
> unchanged over `W₀`.

```lean
def IsFiniteTypeModification {W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (W₀ : Subfunctor W)
    (X : Over W) : Prop
```

**`AlgebraicGeometry.Space.FiniteTypeModification`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean#L120). The attribute's comment: “the category they form”.

> **Stacks 0AS2.** The category of algebraic spaces over `W` which are locally of finite
> type over `W` and isomorphisms over `W₀`.

```lean
abbrev FiniteTypeModification {W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (W₀ : Subfunctor W)
```

**`AlgebraicGeometry.Space.isFiniteTypeModification_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Modifications.lean#L130).

> **Stacks 0AS2.** The three conditions of Stacks 0AS2: the source is an algebraic space,
> the structure morphism is locally of finite type, and its base change to `W₀` is an
> isomorphism. The tag is the set-builder expression delimiting the morphisms that satisfy
> exactly these three conditions, so this equivalence is the whole of it.

```lean
theorem isFiniteTypeModification_iff :
    IsFiniteTypeModification B S hS W₀ X ↔
      IsAlgebraicSpace B S hS X.left ∧ IsLocallyOfFiniteType B S hS X.hom ∧
        IsIso (pullback.snd X.hom W₀.ι)
```

## Tag 0AE5, a lemma

[Tag 0AE5](https://stacks.math.columbia.edu/tag/0AE5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEquivalence_affineModificationBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineModificationBaseChange.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineModificationBaseChange.lean#L457).

> **Stacks 0AE5.** Let `φ : A →+* R` be a homomorphism of Noetherian rings inducing an
> isomorphism from the `I`-adic completion of `A` to the `I R`-adic completion of `R`, for an
> ideal `I ⊆ A`. Then base change along `Spec R ⟶ Spec A` is an equivalence from the category of
> Stacks 0AS2 for `(A, I)` to the category of Stacks 0AS2 for `(R, I R)`.

```lean
theorem isEquivalence_affineModificationBaseChange [IsNoetherianRing A] [IsNoetherianRing R]
    (h : Function.Bijective (adicCompletionMap φ I (I.map φ) le_rfl)) :
    (affineModificationBaseChange B S hS φ I hA hR s).IsEquivalence
```

## Tag 0BH5, a lemma

[Tag 0BH5](https://stacks.math.columbia.edu/tag/0BH5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.fpqcLocalProperties_iff_of_affineModificationBaseChange_obj_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/AffineModificationBaseChangeProperties.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/AffineModificationBaseChangeProperties.lean#L416).

> Let `φ : A →+* R` be a homomorphism of rings, `A` Noetherian, inducing an isomorphism from
> the `I`-adic completion of `A` to the `I R`-adic completion of `R`, as in Stacks 0AE5. Let
> `f : X' ⟶ Spec A`, an object of the category of Stacks 0AS2 for `(A, I)`, correspond to
> `g : Y' ⟶ Spec R`, an object of the category for `(R, I R)`, under the base change functor of
> Stacks 0AE5, that is `g ≅ f ×_{Spec A} Spec R`. Then `f` is quasi-compact, quasi-separated,
> separated, proper, respectively finite, if and only if `g` is.

```lean
theorem fpqcLocalProperties_iff_of_affineModificationBaseChange_obj_iso
    [IsNoetherianRing A] (h : Function.Bijective (adicCompletionMap φ I (I.map φ) le_rfl))
    (M : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS
      (yoneda.obj (affineOver B S hS hA s)) (zeroLocusPoints B S hS hA s I)ᶜ))
    (N : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS
      (yoneda.obj (affineOver B S hS hR (Spec.map (CommRingCat.ofHom φ) ≫ s)))
      (zeroLocusPoints B S hS hR (Spec.map (CommRingCat.ofHom φ) ≫ s) (I.map φ))ᶜ))
    (e : (affineModificationBaseChange B S hS φ I hA hR s).obj M ≅ N) :
    (Space.IsQuasiCompact B S hS M.obj.hom ↔ Space.IsQuasiCompact B S hS N.obj.hom) ∧
      (Space.IsQuasiSeparated B S hS M.obj.hom ↔ Space.IsQuasiSeparated B S hS N.obj.hom) ∧
      (Space.IsSeparated B S hS M.obj.hom ↔ Space.IsSeparated B S hS N.obj.hom) ∧
      (Space.IsProper B S hS M.obj.hom ↔ Space.IsProper B S hS N.obj.hom) ∧
      (Space.IsFinite B S hS M.obj.hom ↔ Space.IsFinite B S hS N.obj.hom)
```

## Tag 0AF7, a lemma

[Tag 0AF7](https://stacks.math.columbia.edu/tag/0AF7) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEquivalence_finiteTypeBaseChange_of_flat_localHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatLocalModificationEquivalence.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatLocalModificationEquivalence.lean#L84).

> **Stacks 0AF7.** Let `A → R` be a local homomorphism of Noetherian local rings which is
> flat, with `𝔪_R = 𝔪_A R` and `κ(𝔪_A) = κ(𝔪_R)`. Then the base-change functor along
> `Spec R ⟶ Spec A`, from the category (0AS2) for `(A, 𝔪_A)` to the category (0AS2) for
> `(R, 𝔪_R)`, is an equivalence. Here `Spec A` lies over a base scheme `S` through `s`, and the
> categories are the finite-type modifications of the represented spaces outside the complements
> of `V(𝔪_A)` and `V(𝔪_R)`.

```lean
theorem isEquivalence_finiteTypeBaseChange_of_flat_localHom {A R : Type u} [CommRing A]
    [CommRing R] [IsLocalRing A] [IsLocalRing R] [IsNoetherianRing A] [IsNoetherianRing R]
    [Algebra A R] [IsLocalHom (algebraMap A R)] [Module.Flat A R]
    (hmax : (maximalIdeal A).map (algebraMap A R) = maximalIdeal R)
    (hres : Function.Bijective (ResidueField.map (algebraMap A R)))
    (hA : B.Contains (Spec (.of A))) (hR : B.Contains (Spec (.of R)))
    (s : Spec (.of A) ⟶ S) :
    (Space.finiteTypeBaseChangeFunctorOfEq
      (isAlgebraicSpace_yoneda B S hS
        (affineOver B S hS hR (Spec.map (CommRingCat.ofHom (algebraMap A R)) ≫ s)))
      (isAlgebraicSpace_yoneda B S hS (affineOver B S hS hA s))
      (yoneda.map (affineOverMap (algebraMap A R) hA hR s))
      (Space.openSubspaceOfPoints B S hS _ (zeroLocusPoints B S hS hA s (maximalIdeal A))ᶜ)
      (Space.openSubspaceOfPoints B S hS _
        (zeroLocusPoints B S hS hR _ (maximalIdeal R))ᶜ)
      (by rw [Space.preimage_openSubspaceOfPoints_compl, preimage_zeroLocusPoints, hmax])
      ).IsEquivalence
```

## Tag 0AE6, a lemma

[Tag 0AE6](https://stacks.math.columbia.edu/tag/0AE6) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isAdmissibleBlowup_dominating_of_isLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationDomination/LocalRing.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModificationDomination/LocalRing.lean#L247).

> **Stacks 0AE6.** Let `(A, 𝔪, κ)` be a Noetherian local ring, let `U = Spec(A) ∖ V(𝔪)` and let
> `f : X ⟶ Spec(A)` be an object of the category of Stacks 0AS2 for `(A, 𝔪)` — an algebraic space,
> locally of finite type over `Spec(A)`, with `f⁻¹(U) ⟶ U` an isomorphism — such that `f` is
> proper. Then there exists a `U`-admissible blowup `S' ⟶ Spec(A)` which dominates `X`, that is,
> the blowup morphism factors as `S' ⟶ X ⟶ Spec(A)`.
>
> The algebraic spaces are those over an arbitrary base scheme `S` of the big fppf site, with
> `Spec(A)` an object of the site over `S`; the source's category is that of algebraic spaces over
> `Spec(A)`, which is the case `S = Spec(A)`. Being a `U`-admissible blowup is Stacks 086B,
> `AlgebraicGeometry.Space.IsAdmissibleBlowup`.

```lean
theorem exists_isAdmissibleBlowup_dominating_of_isLocalRing {A : Type u} [CommRing A]
    [IsLocalRing A] [IsNoetherianRing A] (hA : B.Contains (Spec (.of A))) (s : Spec (.of A) ⟶ S)
    (X : Over (yoneda.obj (FormalSpace.affineOver B S hS hA s)))
    (hX : IsFiniteTypeModification B S hS
      (openSubspaceOfPoints B S hS (yoneda.obj (FormalSpace.affineOver B S hS hA s))
        (FormalSpace.zeroLocusPoints B S hS hA s (IsLocalRing.maximalIdeal A))ᶜ) X)
    (hf : IsProper B S hS X.hom) :
    ∃ (S' : AlgebraicSpaces B S hS) (b : S' ⟶ schemeSpace (FormalSpace.affineOver B S hS hA s)),
      IsAdmissibleBlowup B S hS
        ⟨openSubspaceOfPoints B S hS (yoneda.obj (FormalSpace.affineOver B S hS hA s))
          (FormalSpace.zeroLocusPoints B S hS hA s (IsLocalRing.maximalIdeal A))ᶜ,
          isOpenSubspace_compl_zeroLocusPoints hA s _⟩ b ∧
        ∃ g : S'.obj ⟶ X.left, g ≫ X.hom = b.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.30, Tag 0AS1](https://stacks.math.columbia.edu/tag/0AS1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
