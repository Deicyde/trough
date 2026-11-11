---
declaration: section
origin: cited
lean: TwoTermComplex.projective_homology_iff_ext_one_vanishing, TwoTermComplex.smooth_and_formallySmooth_iff_ext_one_vanishing, TwoTermComplex.exists_twoTerm_representative_free_zero_and_finite, TwoTermComplexExt.exists_hom_Q_map_eq_of_comp_canonical, TwoTermComplexExt.toHomD_bijective, TwoTermComplexExt.forall_Q_map_comp_eq_zero_iff, TwoTermComplexExt.exists_homotopy_components_of_Q_map_eq, TwoTermComplex.ext_one_annihilated_iff_twoTerm_factorization
statement: formalized
proof: formalized
---

# 15.86 Two term complexes

Section 15.86 of the Stacks Project, [Tag 0G9B](https://stacks.math.columbia.edu/tag/0G9B). 12 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0G9C, a lemma

[Tag 0G9C](https://stacks.math.columbia.edu/tag/0G9C) in the Stacks Project.

**`TwoTermComplex.projective_homology_iff_ext_one_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/ProjectiveCohomology.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/ProjectiveCohomology.lean#L155).

> **Stacks 0G9C.** For a derived object with cohomology concentrated in degrees `-1` and `0`,
> vanishing of degree-one Ext against every module is equivalent to vanishing of degree-minus-one
> cohomology and projectivity of zero-th cohomology. If the ring is Noetherian and these two
> cohomology modules are finite, the same condition can be tested on finite modules.

```lean
public theorem projective_homology_iff_ext_one_vanishing
    {R : Type u} [CommRing R] [Small.{v} R]
    (K : DerivedCategory (ModuleCat.{v} R))
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) :
    let moduleObject := fun N : ModuleCat.{v} R ↦
      (DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N
    let projectiveHomology :=
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) (-1)).obj K) ∧
        Module.Projective R
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) 0).obj K)
    let extVanishes := ∀ N : ModuleCat.{v} R,
      Subsingleton (DerivedCategory.Ext K (moduleObject N) 1)
    let finiteExtVanishes := ∀ N : ModuleCat.{v} R, Module.Finite R N →
      Subsingleton (DerivedCategory.Ext K (moduleObject N) 1)
    (projectiveHomology ↔ extVanishes) ∧
      (IsNoetherianRing R →
        Module.Finite R
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) (-1)).obj K) →
        Module.Finite R
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) 0).obj K) →
        (projectiveHomology ↔ finiteExtVanishes))
```

## Tag 0G9D, a remark

[Tag 0G9D](https://stacks.math.columbia.edu/tag/0G9D) in the Stacks Project.

**`TwoTermComplex.smooth_and_formallySmooth_iff_ext_one_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/ProjectiveCohomology.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/ProjectiveCohomology.lean#L358).

> **Stacks 0G9D.** A ring map is smooth if and only if it is of finite presentation and
> degree-one Ext from its naive cotangent complex to every module vanishes. It is formally smooth
> if and only if the same Ext groups vanish, without a finite-presentation condition.

```lean
public theorem smooth_and_formallySmooth_iff_ext_one_vanishing
    {R : Type u'} {S : Type v'} [CommRing R] [CommRing S] (f : R →+* S) :
    letI := f.toAlgebra
    let naiveCotangentObject : DerivedCategory (ModuleCat.{max u' v'} S) :=
      DerivedCategory.Q.obj
        (HomologicalComplex.double
          (ModuleCat.ofHom (Algebra.Generators.self R S).toExtension.cotangentComplex)
          (show (ComplexShape.up ℤ).Rel (-1) 0 from rfl))
    let extOneVanishes := ∀ N : ModuleCat.{max u' v'} S,
      Subsingleton
        (DerivedCategory.Ext naiveCotangentObject
          ((DerivedCategory.singleFunctor (ModuleCat.{max u' v'} S) 0).obj N) 1)
    (f.Smooth ↔ f.FinitePresentation ∧ extOneVanishes) ∧
      (f.FormallySmooth ↔ extOneVanishes)
```

## Tag 0G9E, a lemma

[Tag 0G9E](https://stacks.math.columbia.edu/tag/0G9E) in the Stacks Project.

**`TwoTermComplex.exists_twoTerm_representative_free_zero_and_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Representative.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Representative.lean#L111).

> **Stacks 0G9E.** A derived object with cohomology only in degrees `-1` and `0` has a
> two-term representative whose degree-zero term is free. If the ring is Noetherian and both
> cohomology modules are finite, it also has such a representative with finite degree-minus-one
> term and finite free degree-zero term.

```lean
public theorem exists_twoTerm_representative_free_zero_and_finite
    {R : Type u} [Ring R] [Small.{v} R]
    (K : DerivedCategory (ModuleCat.{v} R))
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) :
    (∃ L : CochainComplex (ModuleCat.{v} R) ℤ,
      L.IsStrictlyGE (-1) ∧ L.IsStrictlyLE 0 ∧
        Module.Free R (L.X 0) ∧ Nonempty (DerivedCategory.Q.obj L ≅ K)) ∧
    (IsNoetherianRing R →
      Module.Finite R
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) (-1)).obj K) →
      Module.Finite R
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) 0).obj K) →
      ∃ L : CochainComplex (ModuleCat.{v} R) ℤ,
        L.IsStrictlyGE (-1) ∧ L.IsStrictlyLE 0 ∧
          Module.Finite R (L.X (-1)) ∧ Module.Finite R (L.X 0) ∧
            Module.Free R (L.X 0) ∧ Nonempty (DerivedCategory.Q.obj L ≅ K))
```

## Tag 0ALN, a lemma

[Tag 0ALN](https://stacks.math.columbia.edu/tag/0ALN) in the Stacks Project.

**`TwoTermComplexExt.exists_hom_Q_map_eq_of_comp_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Ext/ChainRepresentative.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Ext/ChainRepresentative.lean#L441). The attribute's comment: “(3)”.

> **(3)** Assume `K^i = 0` for `i ≤ -3`. Let `α ∈ Hom_{D(R)}(M, K)`. Suppose the
> composite of `α` with the canonical map `K → K^{-2}[2]`, viewed in
> `Hom_{D(R)}(M, K^{-2}[2]) = Ext^2(M, K^{-2})`, comes from an `R`-module
> homomorphism `a : M^{-2} → K^{-2}` with `a ∘ d_M^{-3} = 0` (i.e. equals the
> `D(R)`-morphism induced by the chain map `M → (single (-2)).obj (K^{-2})`
> determined by `a`). Then `α` is represented by a morphism of complexes
> `a^• : M → K` with `a^{-2} = a`.
>
> PROOF SKETCH (Stacks 0ALN, proof of (3)): take `P := exists_projRes`, lift `α`
> to `b : F → K` with `b^{-2} = a ∘ p^{-2}` (`exists_hom_from_projRes_Q_map_eq`),
> descend `b` through `p` to `ab : M → K` with `p ≫ ab = b` and `ab^{-2} = a`
> (`exists_hom_comp_projRes_eq`). Then
> `Q.map p ≫ Q.map ab = Q.map b = Q.map p ≫ α`, and `Q.map p` is an iso, so
> `Q.map ab = α`. This `ab` is the required representative.

```lean
theorem exists_hom_Q_map_eq_of_comp_canonical
    (hM_pos : ∀ i, 0 < i → IsZero (M.X i)) (hM0 : Projective (M.X 0))
    (hK : ∀ i ≤ (-3 : ℤ), IsZero (K.X i))
    (α : HomD M K)
    (a : M.X (-2) ⟶ K.X (-2))
    (ha : M.d (-3) (-2) ≫ a = 0)
    (hα : α ≫ DerivedCategory.Q.map (canonicalToSingleNegTwo K hK)
        = DerivedCategory.Q.map (HomologicalComplex.mkHomToSingle a (by
            intro i hi
            simp only [ComplexShape.up_Rel] at hi
            have hi3 : i = -3 := by omega
            subst hi3
            exact ha))) :
    ∃ (ab : M ⟶ K),
      DerivedCategory.Q.map ab = α ∧ HomologicalComplex.Hom.f ab (-2) = a
```

**`TwoTermComplexExt.toHomD_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Ext/HomotopyComparison.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Ext/HomotopyComparison.lean#L385). The attribute's comment: “(1)”.

> **(1)** Assume `K^i = 0` for `i ≤ -2`. Then the canonical map
> `Hom_{K(R)}(M, K) → Hom_{D(R)}(M, K)` is an isomorphism (bijective).
>
> PROOF SKETCH (Stacks 0ALN, proof of (1)): Pick a termwise-surjective projective
> resolution `p : F → M` (`exists_projRes`); then `F` is K-projective. By
> `CochainComplex.IsKProjective.Qh_map_bijective`, the localization map
> `Qh.map : Hom_{K(R)}(F, K) → Hom_{D(R)}(F, K)` is bijective. Since `Q.map p` is an
> isomorphism in `D(R)` (`p` a quasi-iso), postcomposition identifies
> `Hom_{D(R)}(F, K) ≅ Hom_{D(R)}(M, K)`. By `precomp_quotient_map_projRes_bijective`, precomposition
> with `[p]` is a bijection `Hom_{K(R)}(M, K) → Hom_{K(R)}(F, K)`. Chasing the square
> (`Qh.map` is natural and `toHomD = Qh.map`), `toHomD : Hom\_\{K(R)}(M, K) →
> Hom\_\{D(R)}(M, K)` is the composite of these three bijections, hence bijective.

```lean
theorem toHomD_bijective
    (hM_pos : ∀ i, 0 < i → IsZero (M.X i)) (hM0 : Projective (M.X 0))
    (hK : ∀ i ≤ (-2 : ℤ), IsZero (K.X i)) :
    Function.Bijective (fun f : HomK M K => (toHomD f : HomD M K))
```

**`TwoTermComplexExt.forall_Q_map_comp_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Ext/HomotopyComparison.lean, line 638](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Ext/HomotopyComparison.lean#L638). The attribute's comment: “(2)”.

> **(2)** Assume `K^i = 0` for `i ∉ {-1, 0}` and that `K^0` is projective.
> For a morphism of complexes `a : M → K`, condition (2a) — that for every module
> `N` the induced map `Ext^1(a, N) : Ext^1(K, N) → Ext^1(M, N)`, given by
> pre-composition with `Q.map a`, is the zero map — is equivalent to (2b) — the
> existence of an `R`-module homomorphism `h^0 : M^0 → K^{-1}` with
> `a^{-1} + h^0 ∘ d_M^{-1} = 0`.
>
> PROOF SKETCH: the two implications are `Q_map_comp_eq_zero_of_nullHomotopy`
> ((2b)⇒(2a)) and `exists_nullHomotopy_of_Q_map_comp_eq_zero` ((2a)⇒(2b)); assemble
> with `Iff.intro`.

```lean
theorem forall_Q_map_comp_eq_zero_iff
    (hM_pos : ∀ i, 0 < i → IsZero (M.X i)) (hM0 : Projective (M.X 0))
    (hK : ∀ i, i ≠ -1 → i ≠ 0 → IsZero (K.X i)) (hK0 : Projective (K.X 0))
    (a : M ⟶ K) :
    (∀ (N : ModuleCat.{v} R) (ξ : ExtMod K N 1),
        DerivedCategory.Q.map a ≫ ξ = 0)
      ↔
    (∃ h0 : M.X 0 ⟶ K.X (-1),
        HomologicalComplex.Hom.f a (-1) + M.d (-1) 0 ≫ h0 = 0)
```

**`TwoTermComplexExt.exists_homotopy_components_of_Q_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Ext/RepresentativeHomotopy.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Ext/RepresentativeHomotopy.lean#L441). The attribute's comment: “(4)”.

> **(4)** In the situation of (3): given `α` and a representing morphism of complexes
> `a^•` with `a^{-2} = a` (as produced in (3)), for any second representing morphism
> of complexes `(a')^•` with `(a')^{-2} = a`, there exist `R`-module homomorphisms
> `h^0 : M^0 → K^{-1}` and `h^{-1} : M^{-1} → K^{-2}` such that
> `h^{-1} ∘ d_M^{-2} = 0`, `(a')^{-1} = a^{-1} + d_K^{-2} ∘ h^{-1} + h^0 ∘ d_M^{-1}`,
> and `(a')^0 = a^0 + d_K^{-1} ∘ h^0`.
>
> PROOF SKETCH (Stacks 0ALN, proof of (4)): `ab` and `ab'` both represent `α`, so by
> `nonempty_homotopy_of_Q_map_eq` they are chain-homotopic; pick a homotopy `H`.
> Feed `H` (and the degree-`-2` agreement) to
> `exists_homotopy_components_of_homotopy` to obtain `h^0, h^{-1}` and the three
> relations.

```lean
theorem exists_homotopy_components_of_Q_map_eq
    (hM_pos : ∀ i, 0 < i → IsZero (M.X i)) (hM0 : Projective (M.X 0))
    (hK : ∀ i ≤ (-3 : ℤ), IsZero (K.X i))
    (α : HomD M K)
    (a : M.X (-2) ⟶ K.X (-2))
    (ab ab' : M ⟶ K)
    (hab : DerivedCategory.Q.map ab = α) (hab' : DerivedCategory.Q.map ab' = α)
    (hab_2 : HomologicalComplex.Hom.f ab (-2) = a)
    (hab'_2 : HomologicalComplex.Hom.f ab' (-2) = a) :
    ∃ (h0 : M.X 0 ⟶ K.X (-1)) (hm1 : M.X (-1) ⟶ K.X (-2)),
      M.d (-2) (-1) ≫ hm1 = 0 ∧
      HomologicalComplex.Hom.f ab' (-1) =
        HomologicalComplex.Hom.f ab (-1) + hm1 ≫ K.d (-2) (-1) + M.d (-1) 0 ≫ h0 ∧
      HomologicalComplex.Hom.f ab' 0 =
        HomologicalComplex.Hom.f ab 0 + h0 ≫ K.d (-1) 0
```

## Tag 0G9F, a lemma

[Tag 0G9F](https://stacks.math.columbia.edu/tag/0G9F) in the Stacks Project.

**`TwoTermComplex.ext_one_annihilated_iff_twoTerm_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Representative.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Representative.lean#L356).

> **Stacks 0G9F.** For a derived object with cohomology concentrated in degrees `-1` and `0`,
> the first Ext groups are annihilated by an ideal exactly when multiplication by every element of
> the ideal factors through the differential of a suitable free two-term representative, or of
> every projective two-term representative. Under Noetherian and finiteness hypotheses these are
> also equivalent to testing only finite modules and to the existence of a finite representative.

```lean
public theorem ext_one_annihilated_iff_twoTerm_factorization
    {R : Type u} [CommRing R] [Small.{v} R] (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{v} R))
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) :
    let moduleObject := fun N : ModuleCat.{v} R ↦
      (DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N
    let extAnnihilated := ∀ (N : ModuleCat.{v} R) (a : R), a ∈ I →
      ∀ ξ : DerivedCategory.Ext K (moduleObject N) 1, a • ξ = 0
    let hasFreeRepresentative := ∃ L : CochainComplex (ModuleCat.{v} R) ℤ,
      L.IsStrictlyGE (-1) ∧ L.IsStrictlyLE 0 ∧ Module.Free R (L.X 0) ∧
        Nonempty (DerivedCategory.Q.obj L ≅ K) ∧
        ∀ (a : R), a ∈ I → ∃ h : L.X 0 ⟶ L.X (-1),
          L.d (-1) 0 ≫ h = a • 𝟙 (L.X (-1))
    let everyProjectiveRepresentative := ∀ L : CochainComplex (ModuleCat.{v} R) ℤ,
      L.IsStrictlyGE (-1) → L.IsStrictlyLE 0 → Module.Projective R (L.X 0) →
        Nonempty (DerivedCategory.Q.obj L ≅ K) →
        ∀ (a : R), a ∈ I → ∃ h : L.X 0 ⟶ L.X (-1),
          L.d (-1) 0 ≫ h = a • 𝟙 (L.X (-1))
    let finiteExtAnnihilated := ∀ (N : ModuleCat.{v} R), Module.Finite R N →
      ∀ (a : R), a ∈ I → ∀ ξ : DerivedCategory.Ext K (moduleObject N) 1, a • ξ = 0
    let hasFiniteFreeRepresentative := ∃ L : CochainComplex (ModuleCat.{v} R) ℤ,
      L.IsStrictlyGE (-1) ∧ L.IsStrictlyLE 0 ∧ Module.Finite R (L.X (-1)) ∧
        Module.Finite R (L.X 0) ∧ Module.Free R (L.X 0) ∧
        Nonempty (DerivedCategory.Q.obj L ≅ K) ∧
        ∀ (a : R), a ∈ I → ∃ h : L.X 0 ⟶ L.X (-1),
          L.d (-1) 0 ≫ h = a • 𝟙 (L.X (-1))
    (extAnnihilated ↔ hasFreeRepresentative) ∧
      (hasFreeRepresentative ↔ everyProjectiveRepresentative) ∧
      (IsNoetherianRing R →
        Module.Finite R
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) (-1)).obj K) →
        Module.Finite R
          ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) 0).obj K) →
        (extAnnihilated ↔ finiteExtAnnihilated) ∧
          (finiteExtAnnihilated ↔ hasFiniteFreeRepresentative))
```

## Tag 0G9G, a lemma

[Tag 0G9G](https://stacks.math.columbia.edu/tag/0G9G) in the Stacks Project.

**`TwoTermComplex.twoTermBaseChange_iso_truncGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/BaseChange.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/BaseChange.lean#L344).

> **Stacks 0G9G.** Termwise base change of a two-term representative whose degree-zero term
> is flat represents the truncation in degrees at least `-1` of the derived base change: the
> canonical comparison, transported along the representative isomorphism `e`, factors through
> `truncGEπ (-1)` by an isomorphism.

```lean
public theorem twoTermBaseChange_iso_truncGE
    {R : Type u} {R' : Type v} [CommRing R] [CommRing R']
    (φ : R →+* R') :
    letI : (ModuleCat.extendScalars.{u, v, max v (max u w)} φ).IsLeftAdjoint :=
      ModuleCat.instIsLeftAdjointExtendScalars.{u, v, max u w} φ
    ∀ (K : DerivedCategory (ModuleCat.{max u v w} R))
      (L : CochainComplex (ModuleCat.{max u v w} R) ℤ)
      (e : DerivedCategory.Q.obj L ≅ K)
      (_hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
        Limits.IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v w} R) i).obj K))
      (_hL : ∀ i : ℤ, i ≠ -1 → i ≠ 0 → Limits.IsZero (L.X i))
      (_hflat : Module.Flat R (L.X 0))
      (derivedBaseChange : DerivedCategory (ModuleCat.{max u v w} R) ⥤
        DerivedCategory (ModuleCat.{max u v w} R'))
      (comparison : DerivedCategory.Q ⋙ derivedBaseChange ⟶
        (ModuleCat.extendScalars.{u, v, max v (max u w)} φ).mapHomologicalComplex
          (ComplexShape.up ℤ) ⋙ DerivedCategory.Q)
      [derivedBaseChange.IsLeftDerivedFunctor comparison
        (HomologicalComplex.quasiIso (ModuleCat.{max u v w} R) (ComplexShape.up ℤ))],
      ∃ f : ((DerivedCategory.TStructure.t (C := ModuleCat.{max u v w} R')).truncGE (-1)).obj
          (derivedBaseChange.obj K) ⟶
        DerivedCategory.Q.obj
          (((ModuleCat.extendScalars.{u, v, max v (max u w)} φ).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj L),
        ((DerivedCategory.TStructure.t (C := ModuleCat.{max u v w} R')).truncGEπ (-1)).app
          (derivedBaseChange.obj K) ≫ f = derivedBaseChange.map e.inv ≫ comparison.app L ∧
        IsIso f
```

## Tag 0G9H, a lemma

[Tag 0G9H](https://stacks.math.columbia.edu/tag/0G9H) in the Stacks Project.

**`TwoTermComplex.ext_one_annihilated_truncGE_derivedBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/ExtAnnihilationCriteria.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/ExtAnnihilationCriteria.lean#L51).

> **Stacks 0G9H.** If an ideal annihilates every degree-one Ext group from a two-term derived
> object, then the extended ideal has the same property for its derived base change truncated in
> degrees at least `-1`.

```lean
public theorem ext_one_annihilated_truncGE_derivedBaseChange
    {R : Type u} {R' : Type v} [CommRing R] [CommRing R']
    (I : Ideal R) (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K))
    (φ : R →+* R')
    (hI : ∀ (N : ModuleCat.{max u v} R) (a : R), a ∈ I →
      ∀ ξ : DerivedCategory.Ext K
        ((DerivedCategory.singleFunctor (ModuleCat.{max u v} R) 0).obj N) 1,
        a • ξ = 0)
    (derivedBaseChange : DerivedCategory (ModuleCat.{max u v} R) ⥤
      DerivedCategory (ModuleCat.{max u v} R'))
    (comparison : DerivedCategory.Q ⋙ derivedBaseChange ⟶
      (ModuleCat.extendScalars φ).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q)
    [derivedBaseChange.IsLeftDerivedFunctor comparison
      (HomologicalComplex.quasiIso (ModuleCat.{max u v} R) (ComplexShape.up ℤ))] :
    let K' := ((DerivedCategory.TStructure.t (C := ModuleCat.{max u v} R')).truncGE (-1)).obj
      (derivedBaseChange.obj K)
    ∀ (N : ModuleCat.{max u v} R') (a : R'), a ∈ Ideal.map φ I →
      ∀ ξ : DerivedCategory.Ext K'
        ((DerivedCategory.singleFunctor (ModuleCat.{max u v} R') 0).obj N) 1,
        a • ξ = 0
```

## Tag 0G9I, a lemma

[Tag 0G9I](https://stacks.math.columbia.edu/tag/0G9I) in the Stacks Project.

**`TwoTermComplex.smul_id_eq_zero_of_two_term_homology_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Morphisms.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Morphisms.lean#L103).

> **Stacks 0G9I.** Let `α : K ⟶ K'` be a morphism of `D(R)` between objects with cohomology in
> degrees `-1` and `0` such that `H⁰(α)` is an isomorphism and `H⁻¹(α)` is surjective. If
> multiplication by `f : R` is zero on `K`, then it is zero on `K'`.

```lean
public theorem smul_id_eq_zero_of_two_term_homology_map
    {R : Type u} [CommRing R]
    {K K' : DerivedCategory (ModuleCat.{v} R)} (α : K ⟶ K')
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      Limits.IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K))
    (hK' : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      Limits.IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K'))
    (hα0 : IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) 0).map α))
    (hαneg : Epi ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) (-1)).map α))
    (f : R) (hf : f • 𝟙 K = 0) :
    f • 𝟙 K' = 0
```

## Tag 0G9J, a lemma

[Tag 0G9J](https://stacks.math.columbia.edu/tag/0G9J) in the Stacks Project.

**`TwoTermComplexExt.ext_one_annihilated_of_homology_iso_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/ExtAnnihilation.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/ExtAnnihilation.lean#L53).

> **Stacks 0G9J.** Let `K ⟶ K'` be a morphism of derived objects whose cohomology is
> concentrated in degrees `-1` and `0`. If it induces an isomorphism in degree `0` and an
> epimorphism in degree `-1`, then ideal annihilation of every first Ext group for `K` implies
> the same ideal annihilation for `K'`.

```lean
public theorem ext_one_annihilated_of_homology_iso_epi
    {R : Type u} [CommRing R] (I : Ideal R)
    {K K' : DerivedCategory (ModuleCat.{v} R)}
    (α : K ⟶ K')
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K))
    (hK' : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K'))
    [IsIso ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) 0).map α)]
    [Epi ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) (-1)).map α)]
    (h : ∀ (N : ModuleCat.{v} R) (a : R), a ∈ I →
      ∀ ξ : DerivedCategory.Ext K
        ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N) 1,
        a • ξ = 0) :
    ∀ (N : ModuleCat.{v} R) (a : R), a ∈ I →
      ∀ ξ : DerivedCategory.Ext K'
        ((DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N) 1,
        a • ξ = 0
```

## Tag 0G9K, a lemma

[Tag 0G9K](https://stacks.math.columbia.edu/tag/0G9K) in the Stacks Project.

**`TwoTermComplex.exists_power_ext_one_annihilated_iff_cohomology_conditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/IdealPower.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/IdealPower.lean#L362).

> **Stacks 0G9K.** For a two-term derived object, some power of an ideal annihilates all
> first Ext groups if and only if some power annihilates degree-minus-one cohomology and makes
> degree-zero cohomology relatively projective. Under Noetherian and finiteness hypotheses these
> are also equivalent to the corresponding finite-module Ext condition and to projectivity of
> degree-zero cohomology after localization on a finite cover of the complement of the ideal's
> vanishing locus.

```lean
public theorem exists_power_ext_one_annihilated_iff_cohomology_conditions
    {R : Type u} [CommRing R] [Small.{v} R] (I : Ideal R)
    (K : DerivedCategory (ModuleCat.{v} R))
    (hK : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) :
    let Hneg := (DerivedCategory.homologyFunctor (ModuleCat.{v} R) (-1)).obj K
    let Hzero := (DerivedCategory.homologyFunctor (ModuleCat.{v} R) 0).obj K
    let moduleObject := fun N : ModuleCat.{v} R ↦
      (DerivedCategory.singleFunctor (ModuleCat.{v} R) 0).obj N
    let extAnnihilatedBySomePower := ∃ c : ℕ, ∀ (N : ModuleCat.{v} R) (a : R),
      a ∈ I ^ c → ∀ ξ : DerivedCategory.Ext K (moduleObject N) 1, a • ξ = 0
    let cohomologyCondition := ∃ c : ℕ,
      (∀ (a : R), a ∈ I ^ c → ∀ x : Hneg, a • x = 0) ∧
        Module.IsIProjective R (I ^ c) Hzero
    let finiteExtAnnihilatedBySomePower := ∃ c : ℕ, ∀ (N : ModuleCat.{v} R),
      Module.Finite R N → ∀ (a : R), a ∈ I ^ c →
        ∀ ξ : DerivedCategory.Ext K (moduleObject N) 1, a • ξ = 0
    let localizedProjectiveOnNeighborhood :=
      IsIPowerTorsion R Hneg I ∧ ∃ (n : ℕ) (f : Fin n → R),
        I.radical ≤ (Ideal.span (Set.range f)).radical ∧
          ∀ i, Module.Projective (Localization.Away (f i))
            (LocalizedModule (Submonoid.powers (f i)) Hzero)
    let localizedProjectiveOnCover :=
      IsIPowerTorsion R Hneg I ∧ ∃ (n : ℕ) (f : Fin n → R),
        (∀ i, f i ∈ I) ∧ (Ideal.span (Set.range f)).radical = I.radical ∧
          ∀ i, Module.Projective (Localization.Away (f i))
            (LocalizedModule (Submonoid.powers (f i)) Hzero)
    let localizedProjectiveOnEveryCover :=
      IsIPowerTorsion R Hneg I ∧ ∀ (n : ℕ) (f : Fin n → R),
        (∀ i, f i ∈ I) → (Ideal.span (Set.range f)).radical = I.radical →
          ∀ i, Module.Projective (Localization.Away (f i))
            (LocalizedModule (Submonoid.powers (f i)) Hzero)
    (extAnnihilatedBySomePower ↔ cohomologyCondition) ∧
      (IsNoetherianRing R → Module.Finite R Hneg → Module.Finite R Hzero →
        (extAnnihilatedBySomePower ↔ finiteExtAnnihilatedBySomePower) ∧
        (finiteExtAnnihilatedBySomePower ↔ localizedProjectiveOnNeighborhood) ∧
        (localizedProjectiveOnNeighborhood ↔ localizedProjectiveOnCover) ∧
        (localizedProjectiveOnCover ↔ localizedProjectiveOnEveryCover))
```

## Tag 0AJT, a lemma

[Tag 0AJT](https://stacks.math.columbia.edu/tag/0AJT) in the Stacks Project.

**`TwoTermComplex.comp_eq_zero_of_two_term_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Morphisms.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Morphisms.lean#L55).

> **Stacks 0AJT.** Let `K₁, K₂, K₃` be objects of `D(R)` with cohomology in degrees `-1` and
> `0`, and let `φ : K₁ ⟶ K₂`, `ψ : K₂ ⟶ K₃`. If `H⁰(φ) = 0` and `H⁻¹(ψ) = 0`, then `φ ≫ ψ = 0`.

```lean
public theorem comp_eq_zero_of_two_term_homology
    {R : Type u} [Ring R]
    (K₁ K₂ K₃ : DerivedCategory (ModuleCat.{u} R))
    (hK₁ : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      Limits.IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj K₁))
    (_hK₂ : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      Limits.IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj K₂))
    (hK₃ : ∀ i : ℤ, i ≠ -1 → i ≠ 0 →
      Limits.IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj K₃))
    (φ : K₁ ⟶ K₂) (ψ : K₂ ⟶ K₃)
    (hφ : (DerivedCategory.homologyFunctor (ModuleCat.{u} R) 0).map φ = 0)
    (hψ : (DerivedCategory.homologyFunctor (ModuleCat.{u} R) (-1)).map ψ = 0) :
    φ ≫ ψ = 0
```

## Tag 0G9L, a lemma

[Tag 0G9L](https://stacks.math.columbia.edu/tag/0G9L) in the Stacks Project.

**`Matrix.Q_map_detSmul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/TwoTermComplex/Determinant.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/TwoTermComplex/Determinant.lean#L208).

> **Stacks 0G9L**.
> The morphism `det(A) : K → K` is the zero morphism in the derived category `D(R)`.

```lean
theorem Q_map_detSmul_eq_zero :
    (DerivedCategory.Q (C := ModuleCat R)).map (detSmul A) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.86, Tag 0G9B](https://stacks.math.columbia.edu/tag/0G9B)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
