---
declaration: section
origin: cited
lean: AlgebraicGeometry.relativeWeakNormalization, AlgebraicGeometry.relativeWeakNormalization_isUniversalHomeomorphism, AlgebraicGeometry.range_le_relativeWeakNormalization, AlgebraicGeometry.relativeWeakNormalization_localization, AlgebraicGeometry.relativeSeminormalization, AlgebraicGeometry.relativeSeminormalization_universalHomeomorphism, AlgebraicGeometry.relativeSeminormalization_residueFieldMap_isIso, AlgebraicGeometry.map_mem_relativeSeminormalization
statement: formalized
proof: formalized
---

# 29.56 Weak normalization

Section 29.56 of the Stacks Project, [Tag 0H3I](https://stacks.math.columbia.edu/tag/0H3I). 11 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H3J, a lemma

[Tag 0H3J](https://stacks.math.columbia.edu/tag/0H3J) in the Stacks Project.

**`AlgebraicGeometry.relativeWeakNormalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeWeakNormalization.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeWeakNormalization.lean#L251). The attribute's comment: “the algebra”.

> The relative weak normalization of `A` in `B`: the largest `A`-subalgebra of `B` whose
> spectrum is a universal homeomorphism over `Spec(A)`.

```lean
def relativeWeakNormalization (A B : Type u) [CommRing A] [CommRing B] [Algebra A B] :
    Subalgebra A B
```

**`AlgebraicGeometry.relativeWeakNormalization_isUniversalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeWeakNormalization.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeWeakNormalization.lean#L260). The attribute's comment: “part (1)”.

> If `Spec(B) → Spec(A)` is dominant, the relative weak normalization has spectrum
> universally homeomorphic to `Spec(A)`.

```lean
theorem relativeWeakNormalization_isUniversalHomeomorphism
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (_h : IsDominant (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)) :
    UniversalHomeomorphism
      (Scheme.Spec.map
        (CommRingCat.ofHom (algebraMap A (relativeWeakNormalization A B))).op)
```

**`AlgebraicGeometry.range_le_relativeWeakNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeWeakNormalization.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeWeakNormalization.lean#L271). The attribute's comment: “part (2)”.

> The image of every intermediate `A`-algebra universally homeomorphic over `Spec(A)` is
> contained in the relative weak normalization.

```lean
theorem range_le_relativeWeakNormalization
    (A B C : Type u) [CommRing A] [CommRing B] [CommRing C] [Algebra A B] [Algebra A C]
    (g : C →ₐ[A] B)
    (_hB : IsDominant (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op))
    (hC : UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A C)).op)) :
    g.range ≤ relativeWeakNormalization A B
```

## Tag 0H3K, a lemma

[Tag 0H3K](https://stacks.math.columbia.edu/tag/0H3K) in the Stacks Project.

**`AlgebraicGeometry.relativeWeakNormalization_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Localization.lean, line 595](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/Localization.lean#L595).

> Relative weak normalization commutes with localization at a submonoid of the base.

```lean
public theorem relativeWeakNormalization_localization
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (h : IsDominant (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op))
    (S : Submonoid A) :
    let f : Localization S →+* Localization (S.map (algebraMap A B)) :=
      IsLocalization.map (Localization (S.map (algebraMap A B))) (algebraMap A B)
        S.le_comap_map
    let _ : Algebra (Localization S) (Localization (S.map (algebraMap A B))) := f.toAlgebra
    Algebra.adjoin (Localization S)
        (algebraMap B (Localization (S.map (algebraMap A B))) ''
          (relativeWeakNormalization A B : Set B)) =
      relativeWeakNormalization (Localization S)
    (Localization (S.map (algebraMap A B)))
```

## Tag 0H3L, a lemma

[Tag 0H3L](https://stacks.math.columbia.edu/tag/0H3L) in the Stacks Project.

**`AlgebraicGeometry.relativeSeminormalization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean, line 466](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean#L466). The attribute's comment: “the algebra”.

> The relative seminormalization of `A` in `B`, for a dominant map `Spec B ⟶ Spec A`.

```lean
public noncomputable def relativeSeminormalization
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (_hdom : IsDominant
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)) :
    Subalgebra A B
```

**`AlgebraicGeometry.relativeSeminormalization_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean#L478). The attribute's comment: “part (1), universal homeomorphism”.

> The spectrum of the relative seminormalization is universally homeomorphic to the spectrum of
> the base.

```lean
public theorem relativeSeminormalization_universalHomeomorphism
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (hdom : IsDominant
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)) :
    UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom
        (algebraMap A (relativeSeminormalization A B hdom))).op)
```

**`AlgebraicGeometry.relativeSeminormalization_residueFieldMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean#L489). The attribute's comment: “part (1), residue fields”.

> The relative seminormalization induces isomorphisms on all residue fields.

```lean
public theorem relativeSeminormalization_residueFieldMap_isIso
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (hdom : IsDominant
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)) :
    let f := Scheme.Spec.map (CommRingCat.ofHom
      (algebraMap A (relativeSeminormalization A B hdom))).op
    ∀ x, IsIso (f.residueFieldMap x)
```

**`AlgebraicGeometry.map_mem_relativeSeminormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean, line 501](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeSeminormalization.lean#L501). The attribute's comment: “part (2)”.

> Every intermediate algebra universally homeomorphic to the base and with unchanged residue
> fields maps into the relative seminormalization.

```lean
public theorem map_mem_relativeSeminormalization
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (hdom : IsDominant
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op))
    {C : Type u} [CommRing C] [Algebra A C] (g : C →ₐ[A] B)
    [UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A C)).op)]
    (hres : ∀ x, IsIso ((Scheme.Spec.map
      (CommRingCat.ofHom (algebraMap A C)).op).residueFieldMap x)) :
    ∀ c, g c ∈ relativeSeminormalization A B hdom
```

## Tag 0H3M, a lemma

[Tag 0H3M](https://stacks.math.columbia.edu/tag/0H3M) in the Stacks Project.

**`AlgebraicGeometry.mem_relativeSeminormalization_localization_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/SeminormalizationLocalization.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/SeminormalizationLocalization.lean#L485).

> An element of the relative seminormalization after localization is exactly a fraction whose
> numerator belongs to the original relative seminormalization.

```lean
public theorem mem_relativeSeminormalization_localization_iff
    (A B Aₛ Bₛ : Type u) [CommRing A] [CommRing B] [CommRing Aₛ] [CommRing Bₛ]
    [Algebra A B] (S : Submonoid A)
    [Algebra A Aₛ] [IsLocalization S Aₛ]
    [Algebra B Bₛ] [IsLocalization (S.map (algebraMap A B)) Bₛ]
    [Algebra A Bₛ] [IsScalarTower A B Bₛ]
    [Algebra Aₛ Bₛ] [IsScalarTower A Aₛ Bₛ]
    (hdom : IsDominant
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op))
    (hdomₛ : IsDominant
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap Aₛ Bₛ)).op))
    (x : Bₛ) :
    x ∈ relativeSeminormalization Aₛ Bₛ hdomₛ ↔
      ∃ (b : B), b ∈ relativeSeminormalization A B hdom ∧
        ∃ s : S, x = IsLocalization.mk' Bₛ b
          ⟨algebraMap A B s.1, Submonoid.mem_map.mpr ⟨s.1, s.2, rfl⟩⟩
```

## Tag 0H3N, a lemma

[Tag 0H3N](https://stacks.math.columbia.edu/tag/0H3N) in the Stacks Project.

**`AlgebraicGeometry.exists_initial_universalHomeomorphismFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeInitial.lean, line 1150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeInitial.lean#L1150). The attribute's comment: “weak_initial”.

> **Relative weak normalization** ([Stacks, Tag 0H3N]). A quasi-compact, quasi-separated,
> dominant morphism `f : Y ⟶ X` has an initial factorization `Y ⟶ X' ⟶ X` with `X' ⟶ X` a universal
> homeomorphism, and this factorization is glued from the affine relative weak normalizations.

```lean
public theorem exists_initial_universalHomeomorphismFactorization
    {Y X : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f]
    [IsDominant f] :
    ∃ F : UniversalHomeomorphismFactorization f,
      Nonempty (Limits.IsInitial F) ∧ Nonempty F.AffineGluingData
```

**`AlgebraicGeometry.weakNormalization_isPullback_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeWeakNormalizationOpen/Basic.lean, line 732](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeWeakNormalizationOpen/Basic.lean#L732). The attribute's comment: “weak_open”.

> Relative weak normalization commutes with restriction to an open subscheme
> of the target, as a factorization of the restricted morphism.

```lean
public theorem weakNormalization_isPullback_open
    {Y X : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f]
    [IsDominant f] (U : X.Opens) :
    letI : IsDominant (f ∣_ U) := IsZariskiLocalAtTarget.restrict (‹IsDominant f›) U
    let F := weakNormalizationFactorization f
    let F_U := weakNormalizationFactorization (f ∣_ U)
    ∃! h : F_U.middle ⟶ F.middle,
      IsPullback h F_U.toBase F.toBase U.ι ∧
      F_U.toMiddle ≫ h = (f ⁻¹ᵁ U).ι ≫ F.toMiddle
```

**`AlgebraicGeometry.exists_initial_subintegralFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Seminormalization/SeminormalizationInitial/Initiality.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Seminormalization/SeminormalizationInitial/Initiality.lean#L536). The attribute's comment: “part (2), the seminormalization factorization”.

> The category of factorizations through universal homeomorphisms inducing
> isomorphisms on residue fields has an initial object.

```lean
public theorem exists_initial_subintegralFactorization
    {Y X : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f]
    [IsDominant f] :
    ∃ F : SubintegralFactorization f, Nonempty (Limits.IsInitial F)
```

**`AlgebraicGeometry.existsUnique_isPullback_seminormalizationFactorization_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Seminormalization/SeminormalizationInitial/OpenRestriction.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Seminormalization/SeminormalizationInitial/OpenRestriction.lean#L395). The attribute's comment: “part (3), compatibility with restriction to opens”.

> **Stacks Project, Tag 0H3N.** Formation of the relative seminormalization factorization
> commutes with base change to an open subscheme of the target: the intermediate scheme of the
> factorization of `f ∣_ U` is the restriction of the intermediate scheme of the factorization of
> `f`, by a unique morphism compatible with both legs.

```lean
public theorem existsUnique_isPullback_seminormalizationFactorization_restrict
    {Y X : Scheme.{u}} (f : Y ⟶ X) [QuasiCompact f] [QuasiSeparated f]
    [IsDominant f] (U : X.Opens) :
    letI : IsDominant (f ∣_ U) := IsZariskiLocalAtTarget.restrict (‹IsDominant f›) U
    ∃! h : (seminormalizationFactorization (f ∣_ U)).middle ⟶
        (seminormalizationFactorization f).middle,
      IsPullback h (seminormalizationFactorization (f ∣_ U)).toBase
          (seminormalizationFactorization f).toBase U.ι ∧
        (seminormalizationFactorization (f ∣_ U)).toMiddle ≫ h =
          (f ⁻¹ᵁ U).ι ≫ (seminormalizationFactorization f).toMiddle
```

## Tag 0H3P, a definition

[Tag 0H3P](https://stacks.math.columbia.edu/tag/0H3P) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.seminormalizationFactorization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Seminormalization/SeminormalizationInitial/Initiality.lean#L544), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Seminormalization/RelativeSeminormalizationFactorization.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Seminormalization/RelativeSeminormalizationFactorization.lean#L28) (StacksFrontier): “part (1)”.
- [`AlgebraicGeometry.weakNormalizationFactorization`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/RelativeInitial.lean#L1159), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Seminormalization/RelativeSeminormalizationFactorization.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Seminormalization/RelativeSeminormalizationFactorization.lean#L30) (StacksFrontier): “part (2)”.

## Tag 0H3Q, a lemma

[Tag 0H3Q](https://stacks.math.columbia.edu/tag/0H3Q) in the Stacks Project.

**`AlgebraicGeometry.existsUnique_iso_seminormalization_seminormalizationFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/SeminormalizationInNormalization.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/SeminormalizationInNormalization.lean#L169). The attribute's comment: “the seminormalization of `X` in its normalization agrees with the seminormalization of `X`; the only hypothesis is the tag's own assumption `hX` that every quasi-compact open of `X` has finitely many irreducible components, which is what makes the normalization of `X` exist”.

> **Stacks Project, Tag 0H3Q.** If every quasi-compact open of `X` has finitely many
> irreducible components, the seminormalization of `X` in its normalization is canonically
> isomorphic over `X` to the seminormalization of `X`.

```lean
theorem existsUnique_iso_seminormalization_seminormalizationFactorization (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    letI := Scheme.quasiCompactFromGenericPointResidueFields X hX
    letI := Scheme.quasiSeparatedFromGenericPointResidueFields X
    letI := Scheme.normalization_isDominant X hX
    ∃! e : (seminormalizationFactorization (Scheme.normalization X hX)).middle ≅
        X.seminormalization,
      e.hom ≫ X.seminormalizationHom =
        (seminormalizationFactorization (Scheme.normalization X hX)).toBase
```

## Tag 0H3R, a definition

[Tag 0H3R](https://stacks.math.columbia.edu/tag/0H3R) in the Stacks Project.

**`AlgebraicGeometry.Scheme.weakNormalizationFactorization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalScheme.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalScheme.lean#L75).

> The weak normalization of `X` in its normalization, as a factorization.

```lean
public noncomputable abbrev weakNormalizationFactorization (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    UniversalHomeomorphismFactorization (normalization X hX)
```

## Tag 0H3S, a definition

[Tag 0H3S](https://stacks.math.columbia.edu/tag/0H3S) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IsWeaklyNormal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalScheme.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalScheme.lean#L103).

> A scheme is weakly normal if its weak normalization morphism is an isomorphism.

```lean
public abbrev IsWeaklyNormal (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) : Prop
```

## Tag 0H3T, a lemma

[Tag 0H3T](https://stacks.math.columbia.edu/tag/0H3T) in the Stacks Project.

**`AlgebraicGeometry.isWeaklyNormal_spec_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/AffineWeaklyNormal.lean, line 809](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/AffineWeaklyNormal.lean#L809).

> **Stacks Project, Tag 0H3T.** An affine scheme with finitely many irreducible components
> is weakly normal exactly when its coordinate ring is seminormal and satisfies the prime-power
> divisibility condition for nonzerodivisors.

```lean
theorem isWeaklyNormal_spec_iff (A : Type u) [CommRing A]
    (hA : ∀ U : (Spec (.of A)).Opens, IsCompact (U : Set (Spec (.of A))) →
      (irreducibleComponents U).Finite) :
    Scheme.IsWeaklyNormal (Spec (.of A)) hA ↔ IsWeaklyNormalRing A
```

## Tag 0H3U, a lemma

[Tag 0H3U](https://stacks.math.columbia.edu/tag/0H3U) in the Stacks Project.

**`AlgebraicGeometry.isWeaklyNormal_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalLocal.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalLocal.lean#L305). The attribute's comment: “open subschemes”.

> **Stacks Project, Tag 0H3U.** Every open subscheme of a weakly normal scheme is weakly
> normal.

```lean
theorem isWeaklyNormal_open {X : Scheme.{u}}
    (hX : ∀ V : X.Opens, IsCompact (V : Set X) → (irreducibleComponents V).Finite)
    (hWN : Scheme.IsWeaklyNormal X hX) (U : X.Opens) :
    ∃ hU : ∀ V : U.toScheme.Opens,
      IsCompact (V : Set U.toScheme) → (irreducibleComponents V).Finite,
      Scheme.IsWeaklyNormal U.toScheme hU
```

**`AlgebraicGeometry.isWeaklyNormal_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalLocal.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/WeakNormalization/WeaklyNormalLocal.lean#L322). The attribute's comment: “equivalent conditions”.

> **Stacks Project, Tag 0H3U.** For a scheme whose quasi-compact opens have finitely many
> irreducible components, weak normality is equivalent to the two ring conditions of Tag 0H3T on
> every affine open, to those conditions on a single affine open covering, and to the existence of
> an open covering by weakly normal schemes.

```lean
theorem isWeaklyNormal_tfae (X : Scheme.{u})
    (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite) :
    List.TFAE [
      Scheme.IsWeaklyNormal X hX,
      ∀ U : X.affineOpens, IsWeaklyNormalRing Γ(X, U.1),
      ∃ (I : Type u) (U : I → X.affineOpens),
        (⨆ i, (U i).1) = ⊤ ∧ ∀ i, IsWeaklyNormalRing Γ(X, (U i).1),
      ∃ (I : Type u) (U : I → X.Opens),
        (⨆ i, U i) = ⊤ ∧
          ∀ i, ∃ hUi : ∀ V : (U i).toScheme.Opens,
            IsCompact (V : Set (U i).toScheme) → (irreducibleComponents V).Finite,
            Scheme.IsWeaklyNormal (U i).toScheme hUi]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.56, Tag 0H3I](https://stacks.math.columbia.edu/tag/0H3I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
