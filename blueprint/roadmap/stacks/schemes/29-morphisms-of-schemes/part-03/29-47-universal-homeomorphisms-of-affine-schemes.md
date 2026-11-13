---
declaration: section
origin: cited
lean: AlgebraicGeometry.universallyClosed_specMap_subalgebra, AlgebraicGeometry.universallyInjective_specMap_subalgebra, AlgebraicGeometry.universalHomeomorphism_specMap_subalgebra, AlgebraicGeometry.isIso_residueFieldMap_specMap_subalgebra, AlgebraicGeometry.universallyClosed_specMap_of_isColimit, AlgebraicGeometry.universallyInjective_specMap_of_isColimit, AlgebraicGeometry.universalHomeomorphism_specMap_of_isColimit, AlgebraicGeometry.isIso_residueFieldMap_specMap_of_colimitPresentation
statement: formalized
proof: formalized
---

# 29.47 Universal homeomorphisms of affine schemes

Section 29.47 of the Stacks Project, [Tag 0CN6](https://stacks.math.columbia.edu/tag/0CN6). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CN7, a lemma

[Tag 0CN7](https://stacks.math.columbia.edu/tag/0CN7) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_specMap_subalgebra`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean#L83). The attribute's comment: “universally\_closed”.

> **Stacks 0CN7.** If the morphism on spectra associated to an algebra is universally closed,
> the same holds for the morphism associated to any subalgebra.

```lean
lemma universallyClosed_specMap_subalgebra
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    (B' : Subalgebra A B)
    [UniversallyClosed (Spec.map (CommRingCat.ofHom (algebraMap A B)))] :
    UniversallyClosed (Spec.map (CommRingCat.ofHom (algebraMap A B')))
```

**`AlgebraicGeometry.universallyInjective_specMap_subalgebra`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean#L99). The attribute's comment: “universally\_closed\_and\_injective”.

> **Stacks 0CN7.** Universal injectivity of the map on spectra passes from an algebra to any
> of its subalgebras, provided the original map is universally closed and universally
> injective.

```lean
lemma universallyInjective_specMap_subalgebra
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    [UniversallyClosed (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)]
    [UniversallyInjective (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)]
    (B' : Subalgebra A B) :
    UniversallyInjective (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B')).op)
```

**`AlgebraicGeometry.universalHomeomorphism_specMap_subalgebra`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean#L155). The attribute's comment: “universal\_homeomorphism”.

> **Stacks 0CN7.** If the map on spectra of an algebra is a universal homeomorphism, then so
> is the map on spectra of any intermediate subalgebra.

```lean
lemma universalHomeomorphism_specMap_subalgebra
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    [UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)]
    (B' : Subalgebra A B) :
    UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B')).op)
```

**`AlgebraicGeometry.isIso_residueFieldMap_specMap_subalgebra`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Subalgebra.lean#L218). The attribute's comment: “universal\_homeomorphism\_residue\_fields”.

> **Stacks 0CN7.** If a universal homeomorphism between affine spectra induces isomorphisms
> on residue fields, then so does the map associated to any intermediate subalgebra.

```lean
lemma isIso_residueFieldMap_specMap_subalgebra
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    [UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)]
    (hres : ∀ x : Spec (.of B),
      IsIso ((Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op).residueFieldMap x))
    (B' : Subalgebra A B) :
    ∀ x : Spec (.of B'),
      IsIso ((Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B')).op).residueFieldMap x)
```

## Tag 0CN8, a lemma

[Tag 0CN8](https://stacks.math.columbia.edu/tag/0CN8) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_specMap_of_isColimit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean#L127). The attribute's comment: “universally\_closed”.

> **Stacks 0CN8.** A filtered colimit of commutative `A`-algebras whose spectrum morphisms to
> `Spec A` are universally closed again has universally closed spectrum morphism to `Spec A`.

```lean
lemma universallyClosed_specMap_of_isColimit
    (A : Type u) [CommRing A] {J : Type v} [Category.{w} J] [IsFiltered J]
    (F : Functor J (CommAlgCat.{u} A)) (c : Cocone F) (hc : IsColimit c)
    (h : ∀ j, UniversallyClosed
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (F.obj j))).op)) :
    UniversallyClosed
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A c.pt)).op)
```

**`AlgebraicGeometry.universallyInjective_specMap_of_isColimit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean#L159). The attribute's comment: “closed\_injective”.

> **Stacks 0CN8.** A filtered colimit of commutative `A`-algebras whose spectrum morphisms to
> `Spec A` are universally injective again has universally injective spectrum morphism to
> `Spec A`.

```lean
lemma universallyInjective_specMap_of_isColimit
    (A : Type u) [CommRing A] {J : Type v} [Category.{w} J] [IsFiltered J]
    (F : Functor J (CommAlgCat.{u} A)) (c : Cocone F) (hc : IsColimit c)
    (h : ∀ j, UniversallyInjective
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (F.obj j))).op)) :
    UniversallyInjective
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A c.pt)).op)
```

**`AlgebraicGeometry.universalHomeomorphism_specMap_of_isColimit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean#L256). The attribute's comment: “universal\_homeomorphism”.

> **Stacks 0CN8.** A filtered colimit of commutative `A`-algebras whose spectrum morphisms to
> `Spec A` are universal homeomorphisms again has universal-homeomorphic spectrum morphism to
> `Spec A`.

```lean
lemma universalHomeomorphism_specMap_of_isColimit
    (A : Type u) [CommRing A] {J : Type v} [Category.{w} J] [IsFiltered J]
    (F : Functor J (CommAlgCat.{u} A)) (c : Cocone F) (hc : IsColimit c)
    (h : ∀ j, UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (F.obj j))).op)) :
    UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A c.pt)).op)
```

**`AlgebraicGeometry.isIso_residueFieldMap_specMap_of_colimitPresentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FilteredColimit.lean#L358). The attribute's comment: “homeomorphism\_equal\_residue\_fields”.

> **Stacks 0CN8.** A filtered colimit of affine maps which induce isomorphisms on residue
> fields still induces an isomorphism on the residue field at every point.

```lean
lemma isIso_residueFieldMap_specMap_of_colimitPresentation
    {A : Type u} [CommRing A] {J : Type v} [Category.{w} J] [IsFiltered J]
    {B : CommAlgCat.{u} A} (pres : ColimitPresentation J B)
    (hresidue : ∀ i x, IsIso
      ((Scheme.Spec.map (CommRingCat.ofHom
        (algebraMap A ↥(pres.diag.obj i))).op).residueFieldMap x)) :
    ∀ x, IsIso
      ((Scheme.Spec.map (CommRingCat.ofHom (algebraMap A ↥B)).op).residueFieldMap x)
```

## Tag 0CN9, a lemma

[Tag 0CN9](https://stacks.math.columbia.edu/tag/0CN9) in the Stacks Project.

**`IsLocalization.exists_numerator_not_mem_of_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Denominators.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Denominators.lean#L71).

> **Stacks 0CN9.** Special-element conditions over a localization can be witnessed by a
> numerator before localization.

```lean
theorem exists_numerator_not_mem_of_localization
    {B : Type u} [CommRing B] (A : Subring B) (S : Submonoid A)
    {n : ℕ} (b : Fin n → B) (x : Localization (S.map A.subtype))
    (hx : x ∉ Set.range
      (IsLocalization.map (M := S) (S := Localization S) (T := S.map A.subtype)
        (Localization (S.map A.subtype)) A.subtype S.le_comap_map))
    (hbx : ∀ i, algebraMap B (Localization (S.map A.subtype)) (b i) *
      x ^ (i.val + 1) ∈ Set.range
        (IsLocalization.map (M := S) (S := Localization S) (T := S.map A.subtype)
          (Localization (S.map A.subtype)) A.subtype S.le_comap_map)) :
    ∃ (s : S) (y : B),
      x = IsLocalization.mk' (Localization (S.map A.subtype)) y
          ⟨A.subtype s.1, Submonoid.mem_map_of_mem A.subtype s.2⟩ ∧
        y ∉ A ∧ ∀ i, b i * y ^ (i.val + 1) ∈ A
```

## Tag 0CNA, a lemma

[Tag 0CNA](https://stacks.math.columbia.edu/tag/0CNA) in the Stacks Project.

**`Subring.exists_not_mem_and_sq_mem_and_cube_mem_of_pow_mem_of_succ_pow_mem`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Powers.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Powers.lean#L63).

> **Stacks 0CNA.** If an element outside a subring has two consecutive powers,
> with the first exponent at least two, in the subring, then some element outside the subring has
> its square and cube in the subring.

```lean
lemma exists_not_mem_and_sq_mem_and_cube_mem_of_pow_mem_of_succ_pow_mem
    {B : Type u} [CommRing B] (A : Subring B) {b : B} {n : ℕ} (hb : b ∉ A) (hn : 2 ≤ n)
    (hpow : b ^ n ∈ A) (hpow_succ : b ^ (n + 1) ∈ A) :
    ∃ b' : B, b' ∉ A ∧ b' ^ 2 ∈ A ∧ b' ^ 3 ∈ A
```

## Tag 0CNB, a lemma

[Tag 0CNB](https://stacks.math.columbia.edu/tag/0CNB) in the Stacks Project.

**`AlgebraicGeometry.exists_not_mem_and_sq_mem_and_cube_mem_of_universalHomeomorphism_of_residueFieldMap_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SquareCube.lean, line 767](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SquareCube.lean#L767).

> A proper subring extension which is a universal homeomorphism on spectra
> and induces isomorphisms on residue fields contains an element outside the
> subring whose square and cube are in the subring.

```lean
theorem exists_not_mem_and_sq_mem_and_cube_mem_of_universalHomeomorphism_of_residueFieldMap_isIso
    {B : Type u} [CommRing B] (A : Subring B)
    [UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom A.subtype).op)]
    (hres : ∀ x : Spec (CommRingCat.of B),
      IsIso ((Scheme.Spec.map (CommRingCat.ofHom A.subtype).op).residueFieldMap x))
    (hA : A ≠ ⊤) :
    ∃ b : B, b ∉ A ∧ b ^ 2 ∈ A ∧ b ^ 3 ∈ A
```

## Tag 0CNC, a lemma

[Tag 0CNC](https://stacks.math.columbia.edu/tag/0CNC) in the Stacks Project.

**`AlgebraicGeometry.exists_special_element_of_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SpecialElement.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SpecialElement.lean#L703).

> **Stacks Project, Tag 0CNC.** A proper extension inducing a universal homeomorphism on
> spectra contains either a square-and-cube special element or a prime-power special element.

```lean
theorem exists_special_element_of_universalHomeomorphism
    {B : Type u} [CommRing B] (A : Subring B)
    [UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom A.subtype).op)]
    (hA : A ≠ ⊤) :
    (∃ b : B, b ∉ A ∧ b ^ 2 ∈ A ∧ b ^ 3 ∈ A) ∨
      (∃ p : ℕ, Nat.Prime p ∧
        ∃ b : B, b ∉ A ∧ (p : B) * b ∈ A ∧ b ^ p ∈ A)
```

## Tag 0CND, a proposition

[Tag 0CND](https://stacks.math.columbia.edu/tag/0CND) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_and_residueFieldIso_iff_finite_adjoin_square_cube`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/TowerResidue.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/TowerResidue.lean#L341).

> An injective extension induces a universal homeomorphism with unchanged residue fields
> if and only if each finite subset is contained in an algebra generated by a sequence whose
> successive elements have square and cube in the algebra generated by their predecessors.

```lean
public theorem universalHomeomorphism_and_residueFieldIso_iff_finite_adjoin_square_cube
    {A B : Type u} [CommRing A] [CommRing B] [Algebra A B]
    (hAB : Function.Injective (algebraMap A B)) :
    let f := Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op
    (UniversalHomeomorphism f ∧ (∀ x, IsIso (f.residueFieldMap x))) ↔
      ∀ E : Finset B, ∃ (n : ℕ) (b : Fin n → B),
        (↑E : Set B) ⊆ Algebra.adjoin A (Set.range b) ∧
      ∀ i : Fin n,
        b i ^ 2 ∈ Algebra.adjoin A
            (Set.range (fun j : Fin i ↦ b (Fin.castLE i.isLt.le j))) ∧
          b i ^ 3 ∈ Algebra.adjoin A
              (Set.range (fun j : Fin i ↦ b (Fin.castLE i.isLt.le j)))
```

## Tag 0CNE, a proposition

[Tag 0CNE](https://stacks.math.columbia.edu/tag/0CNE) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_spec_iff_finite_adjoin_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Tower.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/Tower.lean#L364).

> An inclusion of rings induces a universal homeomorphism on spectra exactly when every finite
> set is contained in a finite, successively elementary extension.

```lean
theorem universalHomeomorphism_spec_iff_finite_adjoin_tower
    (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (hAB : Function.Injective (algebraMap A B)) :
    UniversalHomeomorphism
        (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op) ↔
      ∀ E : Finset B, ∃ (n : ℕ) (b : Fin n → B),
        ((E : Set B) ⊆ Algebra.adjoin A (Set.range b)) ∧
          ∀ i : Fin n,
            (((b i) ^ 2 ∈ Algebra.adjoin A
                (Set.range fun j : { j : Fin n // j < i } ↦ b j)) ∧
              ((b i) ^ 3 ∈ Algebra.adjoin A
                (Set.range fun j : { j : Fin n // j < i } ↦ b j))) ∨
            (∃ p : ℕ, p.Prime ∧
              (((p : B) * b i ∈ Algebra.adjoin A
                  (Set.range fun j : { j : Fin n // j < i } ↦ b j)) ∧
                ((b i) ^ p ∈ Algebra.adjoin A
                  (Set.range fun j : { j : Fin n // j < i } ↦ b j))))
```

## Tag 0CNF, a lemma

[Tag 0CNF](https://stacks.math.columbia.edu/tag/0CNF) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_iff_locallyNilpotent_ker_and_pow_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/InvertPrime.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/InvertPrime.lean#L321).

> A ring map that is an isomorphism after inverting a prime induces a universal
> homeomorphism on spectra precisely when its kernel is locally nilpotent and
> every target element has a prime-power multiple and prime-power power in its
> image.

```lean
theorem universalHomeomorphism_iff_locallyNilpotent_ker_and_pow_mem_range
    {A B : Type u} [CommRing A] [CommRing B] (φ : A →+* B)
    (p : ℕ) (hp : Nat.Prime p)
    (hφ : Function.Bijective
      (IsLocalization.Away.map (Localization.Away (p : A))
        (Localization.Away (φ (p : A))) φ (p : A))) :
    UniversalHomeomorphism
        (Scheme.Spec.map (CommRingCat.ofHom φ).op) ↔
      (RingHom.ker φ).LocallyNilpotent ∧
        ∀ b : B, ∃ n : ℕ,
          (p : B) ^ n * b ∈ Set.range φ ∧ b ^ (p ^ n) ∈ Set.range φ
```

## Tag 0EUI, a lemma

[Tag 0EUI](https://stacks.math.columbia.edu/tag/0EUI) in the Stacks Project.

**`AlgebraicGeometry.universalHomeomorphism_spec_quotient_of_pPower_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/PrimePowerAlg.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/PrimePowerAlg.lean#L188). The attribute's comment: “p\_power\_multiple”.

> If `p` is prime and `p ^ p * x = y ^ p`, adjoining a common prime-power root as in
> Stacks Project, Tag 0EUI, induces a universal homeomorphism on spectra.

```lean
theorem universalHomeomorphism_spec_quotient_of_pPower_mul
    {A : Type u} [CommRing A] (x y : A) (p : ℕ) (hp : p.Prime)
    (hxy : (p : A) ^ p * x = y ^ p) :
    let B := Polynomial A ⧸ Ideal.span
      {Polynomial.X ^ p - Polynomial.C x,
        Polynomial.C (p : A) * Polynomial.X - Polynomial.C y}
    UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A B)).op)
```

**`AlgebraicGeometry.squareCubeSpecMap_universalHomeomorphism`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SquareCubeAlg.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SquareCubeAlg.lean#L468). The attribute's comment: “square\_cube”.

> The square-cube extension induces a universal homeomorphism on spectra.

```lean
public lemma squareCubeSpecMap_universalHomeomorphism
    (A : Type u) [CommRing A] (x y : A) (hxy : x ^ 3 = y ^ 2) :
    UniversalHomeomorphism (squareCubeSpecMap A x y)
```

**`AlgebraicGeometry.isIso_residueFieldMap_squareCubeSpecMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SquareCubeAlg.lean, line 482](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/SquareCubeAlg.lean#L482). The attribute's comment: “square\_cube”.

> The square-cube extension induces an isomorphism on the residue field at every point.

```lean
public lemma isIso_residueFieldMap_squareCubeSpecMap
    (A : Type u) [CommRing A] (x y : A) (hxy : x ^ 3 = y ^ 2)
    (z : Spec (.of (SquareCubeAlgebra A x y))) :
    IsIso ((squareCubeSpecMap A x y).residueFieldMap z)
```

## Tag 0EUJ, a lemma

[Tag 0EUJ](https://stacks.math.columbia.edu/tag/0EUJ) in the Stacks Project.

**`AlgebraicGeometry.isFilteredColimit_finitePresentation_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UniversalHomeomorphismFilteredColimit.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UniversalHomeomorphismFilteredColimit.lean#L152). The attribute's comment: “universal\_homeomorphism\_filtered\_colimit”.

> A ring map inducing a universal homeomorphism on spectra is a filtered colimit of finitely
> presented ring maps which induce universal homeomorphisms on spectra.

```lean
public theorem isFilteredColimit_finitePresentation_universalHomeomorphism
    {A B : Type u} [CommRing A] [CommRing B] (f : A →+* B)
    (hf : UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom f).op)) :
    ObjectProperty.ind.{u}
      (fun C : Under (CommRingCat.of A) ↦
        C.hom.hom.FinitePresentation ∧
          UniversalHomeomorphism (Scheme.Spec.map C.hom.op))
      (Under.mk (CommRingCat.ofHom f))
```

**`AlgebraicGeometry.ind_finitePresentation_residueFieldMap_isIso_universalHomeomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UniversalHomeomorphismFilteredColimit.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/UniversalHomeomorphismFilteredColimit.lean#L263). The attribute's comment: “residue\_field\_isomorphism\_filtered\_colimit”.

> A ring map which is a universal homeomorphism on spectra and induces isomorphisms on
> residue fields is a filtered colimit of finitely presented ring maps with both properties.

```lean
public theorem ind_finitePresentation_residueFieldMap_isIso_universalHomeomorphism
    {A B : Type u} [CommRing A] [CommRing B] (f : A →+* B)
    (hres : ∀ x : Spec (.of B),
      IsIso ((Scheme.Spec.map (CommRingCat.ofHom f).op).residueFieldMap x))
    (huh : UniversalHomeomorphism
      (Scheme.Spec.map (CommRingCat.ofHom f).op)) :
    ObjectProperty.ind.{u}
      (fun C : Under (CommRingCat.of A) ↦
        C.hom.hom.FinitePresentation ∧
          (UniversalHomeomorphism (Scheme.Spec.map C.hom.op) ∧
            ∀ x : Spec C.right,
              IsIso ((Scheme.Spec.map C.hom.op).residueFieldMap x)))
      (Under.mk (CommRingCat.ofHom f))
```

**`AlgebraicGeometry.exists_universalHomeomorphism_specMap_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FiniteStage.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FiniteStage.lean#L481). The attribute's comment: “universal homeomorphism at a finite stage”.

> **Stacks 0EUJ.** Let a commutative `A`-algebra of finite type be presented as a filtered
> colimit of `A`-algebras of finite presentation with surjective transition maps.  If its morphism
> on spectra over `Spec A` is a universal homeomorphism, then so is the one of every sufficiently
> late stage of the diagram.

```lean
theorem exists_universalHomeomorphism_specMap_of_isColimit
    (A : Type u) [CommRing A] {J : Type v} [Category.{w} J] [IsFiltered J]
    (F : J ⥤ CommAlgCat.{u} A) (c : Cocone F) (hc : IsColimit c)
    [Algebra.FiniteType A c.pt]
    (hfp : ∀ i, Algebra.FinitePresentation A (F.obj i))
    (hsurj : ∀ {i j : J} (f : i ⟶ j), Function.Surjective (F.map f))
    [UniversalHomeomorphism (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A c.pt)).op)] :
    ∃ i : J, ∀ {j : J} (_ : i ⟶ j),
      UniversalHomeomorphism
        (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (F.obj j))).op)
```

**`AlgebraicGeometry.exists_universalHomeomorphism_and_isIso_residueFieldMap_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FiniteStage.lean, line 525](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/UniversalHomeomorphism/Affine/FiniteStage.lean#L525). The attribute's comment: “universal homeomorphism with equal residue fields at a finite stage”.

> **Stacks 0EUJ.** Let a commutative `A`-algebra of finite type be presented as a filtered
> colimit of `A`-algebras of finite presentation with surjective transition maps.  If its morphism
> on spectra over `Spec A` is a universal homeomorphism which induces isomorphisms on residue
> fields, then the same holds at every sufficiently late stage of the diagram.

```lean
theorem exists_universalHomeomorphism_and_isIso_residueFieldMap_of_isColimit
    (A : Type u) [CommRing A] {J : Type v} [Category.{w} J] [IsFiltered J]
    (F : J ⥤ CommAlgCat.{u} A) (c : Cocone F) (hc : IsColimit c)
    [Algebra.FiniteType A c.pt]
    (hfp : ∀ i, Algebra.FinitePresentation A (F.obj i))
    (hsurj : ∀ {i j : J} (f : i ⟶ j), Function.Surjective (F.map f))
    [UniversalHomeomorphism (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A c.pt)).op)]
    (hres : ∀ x : Spec (.of c.pt), IsIso ((Scheme.Spec.map
      (CommRingCat.ofHom (algebraMap A c.pt)).op).residueFieldMap x)) :
    ∃ i : J, ∀ {j : J} (_ : i ⟶ j),
      UniversalHomeomorphism
          (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (F.obj j))).op) ∧
        ∀ x : Spec (.of (F.obj j)), IsIso ((Scheme.Spec.map
          (CommRingCat.ofHom (algebraMap A (F.obj j))).op).residueFieldMap x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.47, Tag 0CN6](https://stacks.math.columbia.edu/tag/0CN6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
