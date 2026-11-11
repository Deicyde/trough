---
declaration: section
origin: cited
lean: FormalGlueing.flat_and_faithful_on_ideal_torsion_tfae, IPowerTorsion.baseChange_bijective_iff_quotientMap_bijective, IPowerTorsion.baseChange_equiv_of_quotientMap_bijective, FormalGlueing.quasiIso_koszulSeq_and_cechComplex_baseChange, Stacks.RelationsOfSequence.short_exact, Stacks.RelationsOfSequence.K_annihilated, FormalGlueing.extOne_exact_firstRelationHomology_to_kernelHom, FormalGlueing.idealI_le_annihilator_firstRelationHomology
statement: formalized
proof: formalized
---

# 15.91 Formal glueing of module categories

Section 15.91 of the Stacks Project, [Tag 05E5](https://stacks.math.columbia.edu/tag/05E5). 22 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05E7, a lemma

[Tag 05E7](https://stacks.math.columbia.edu/tag/05E7) in the Stacks Project.

**`FormalGlueing.flat_and_faithful_on_ideal_torsion_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean#L269).

> Let `R → S` be a ring map and `I` an ideal of `R`. The following are equivalent:
>
> 1. `S` is flat over `R` and `R/I → S/IS` is faithfully flat;
> 2. `S` is flat over `R` and `Spec(S/IS) → Spec(R/I)` is surjective;
> 3. `S` is flat over `R` and tensoring with `S` is faithful on modules annihilated by `I`;
> 4. `S` is flat over `R` and tensoring with `S` is faithful on `I`-power torsion modules.

```lean
public theorem flat_and_faithful_on_ideal_torsion_tfae
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S] (I : Ideal R) :
    let q : R ⧸ I →+* S ⧸ I.map (algebraMap R S) :=
      Ideal.quotientMap (I.map (algebraMap R S)) (algebraMap R S) Ideal.le_comap_map
    List.TFAE
      [ Module.Flat R S ∧ RingHom.FaithfullyFlat q,
        Module.Flat R S ∧ Function.Surjective (PrimeSpectrum.comap q),
        Module.Flat R S ∧
          ∀ (M N : Type (max u v)) [AddCommGroup M] [Module R M]
            [AddCommGroup N] [Module R N],
            I ≤ Module.annihilator R M → I ≤ Module.annihilator R N →
              Function.Injective fun f : M →ₗ[R] N ↦ LinearMap.rTensor S f,
        Module.Flat R S ∧
          ∀ (M N : Type (max u v)) [AddCommGroup M] [Module R M]
            [AddCommGroup N] [Module R N],
            IsIPowerTorsion R M I → IsIPowerTorsion R N I →
              Function.Injective fun f : M →ₗ[R] N ↦ LinearMap.rTensor S f ]
```

## Tag 05E9, a lemma

[Tag 05E9](https://stacks.math.columbia.edu/tag/05E9) in the Stacks Project.

Declarations registered for the tag:

- [`IPowerTorsion.baseChange_bijective_iff_quotientMap_bijective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/IdealPowerTorsion.lean#L345), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean#L351) (StacksFrontier): “the base-change criterion on ideal-power torsion modules”.

## Tag 05EC, a lemma

[Tag 05EC](https://stacks.math.columbia.edu/tag/05EC) in the Stacks Project.

Declarations registered for the tag:

- [`IPowerTorsion.baseChange_equiv_of_quotientMap_bijective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/IdealPowerTorsion.lean#L1002), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean#L377) (StacksFrontier): “the torsion-submodule isomorphism and the equivalence of subcategories”.

## Tag 091M, a lemma

[Tag 091M](https://stacks.math.columbia.edu/tag/091M) in the Stacks Project.

**`FormalGlueing.quasiIso_koszulSeq_and_cechComplex_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingKoszulBaseChange.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingKoszulBaseChange.lean#L431).

> If a flat map `R → S` is an isomorphism modulo a finitely generated ideal `I`, then for
> every finite sequence defining the same closed subset as `I`, the canonical base-change maps on
> the Koszul complex and on the extended alternating Čech complex are quasi-isomorphisms.

```lean
public theorem quasiIso_koszulSeq_and_cechComplex_baseChange
    (R : Type uR) (S : Type uS) [CommRing R] [CommRing S] [Algebra R S]
    (I : Ideal R) (hI : I.FG) (hflat : Module.Flat R S)
    (hquot : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap R S)) (algebraMap R S) Ideal.le_comap_map))
    {r : ℕ} (f : Fin r → R)
    (hV : PrimeSpectrum.zeroLocus (Ideal.span (Set.range f) : Set R) =
      PrimeSpectrum.zeroLocus (I : Set R)) :
    let liftR := (ModuleCat.uliftFunctor.{uS, uR} R)
    let liftS := (ModuleCat.uliftFunctor.{uR, uS} S)
    let koszulR := (liftR.mapHomologicalComplex (ComplexShape.down ℕ)).obj
      (Koszul.seqComplex f)
    let koszulS := (liftS.mapHomologicalComplex (ComplexShape.down ℕ)).obj
      (Koszul.seqComplex (fun i => algebraMap R S (f i)))
    let cechR := (liftR.mapHomologicalComplex (ComplexShape.up ℕ)).obj
      (Cech.cechComplex f R)
    let cechS := (liftS.mapHomologicalComplex (ComplexShape.up ℕ)).obj
      (Cech.cechComplex (fun i => algebraMap R S (f i)) S)
    ∃ k : koszulR ⟶
          ((ModuleCat.restrictScalars.{max uR uS} (algebraMap R S)).mapHomologicalComplex
            (ComplexShape.down ℕ)).obj koszulS,
      (∀ (n : ℕ) (v : Fin n → (Fin r → R)),
          k.f n (ULift.up (exteriorPower.ιMulti R n v)) =
            ULift.up (exteriorPower.ιMulti S n (fun i j => algebraMap R S (v i j)))) ∧
      QuasiIso k ∧
      ∃ c : cechR ⟶
          ((ModuleCat.restrictScalars.{max uR uS} (algebraMap R S)).mapHomologicalComplex
            (ComplexShape.up ℕ)).obj cechS,
        (∀ (p : ℕ) (s : {t : Finset (Fin r) // t.card = p}) (x : R)
            (y : Cech.cechSub f s.1),
            c.f p
                (ULift.up (DirectSum.lof R {t : Finset (Fin r) // t.card = p}
                  (fun t => Cech.cechMod f R t.1) s
                  (LocalizedModule.mk x y))) =
              ULift.up (DirectSum.lof S {t : Finset (Fin r) // t.card = p}
                (fun t => Cech.cechMod (fun i => algebraMap R S (f i)) S t.1) s
                (LocalizedModule.mk (algebraMap R S x)
                  ⟨algebraMap R S y, by
                    obtain ⟨n, hn⟩ := y.2
                    exact ⟨n, by rw [← hn, map_pow, map_prod]⟩⟩))) ∧
        QuasiIso c
```

## Tag 05ED, a lemma

[Tag 05ED](https://stacks.math.columbia.edu/tag/05ED) in the Stacks Project.

**`Stacks.RelationsOfSequence.short_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RelationsOfSequence.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RelationsOfSequence.lean#L106).

> The sequence `0 → K → M → I → 0` is exact: the inclusion `K ↪ M` and `φ` are exact at `M`, and
> the range of `φ` is the ideal `I = (f_1, …, f_n)`.

```lean
theorem short_exact :
    Function.Exact (K f).subtype (phi f) ∧
      LinearMap.range (phi f) = (idealI f).restrictScalars R
```

**`Stacks.RelationsOfSequence.K_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/RelationsOfSequence.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/RelationsOfSequence.lean#L142).

> The kernel `K = ker φ` is annihilated by the ideal `I = (f_1, …, f_n)`.

```lean
theorem K_annihilated : ∀ a ∈ idealI f, ∀ k ∈ K f, a • k = 0
```

## Tag 05EE, a lemma

[Tag 05EE](https://stacks.math.columbia.edu/tag/05EE) in the Stacks Project.

**`FormalGlueing.extOne_exact_firstRelationHomology_to_kernelHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingKoszulRelations.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingKoszulRelations.lean#L438).

> There is a canonical exact sequence
> `0 → Ext¹_R(R / (f), N) → H₁(N, f) → Hom_R(K, N)`, where `K` is the kernel from
> Stacks 05ED.

```lean
public theorem extOne_exact_firstRelationHomology_to_kernelHom
    (N : Type v) [AddCommGroup N] [Module R N] :
    ∃ i : CategoryTheory.Abelian.Ext
        (ModuleCat.of R (ULift.{max u v} (R ⧸ Stacks.RelationsOfSequence.idealI f)))
        (ModuleCat.of R (ULift.{max u v} N)) 1 →ₗ[R] firstRelationHomology f N,
      (∀ g : Stacks.RelationsOfSequence.idealI f →ₗ[R] N,
          i (idealHomToExtOne f N g) = idealHomToFirstRelationHomology f N g) ∧
        Function.Injective i ∧ Function.Exact i (firstRelationHomologyToKernelHom f N) ∧
        ∀ j : CategoryTheory.Abelian.Ext
            (ModuleCat.of R (ULift.{max u v} (R ⧸ Stacks.RelationsOfSequence.idealI f)))
            (ModuleCat.of R (ULift.{max u v} N)) 1 →ₗ[R] firstRelationHomology f N,
          (∀ g : Stacks.RelationsOfSequence.idealI f →ₗ[R] N,
            j (idealHomToExtOne f N g) = idealHomToFirstRelationHomology f N g) → j = i
```

## Tag 05EF, a lemma

[Tag 05EF](https://stacks.math.columbia.edu/tag/05EF) in the Stacks Project.

**`FormalGlueing.idealI_le_annihilator_firstRelationHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingKoszulRelations.lean, line 498](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingKoszulRelations.lean#L498).

> The ideal generated by a finite family annihilates its first relation
> homology with coefficients in any module.

```lean
public theorem idealI_le_annihilator_firstRelationHomology
    {R : Type u} [CommRing R] {n : ℕ} (f : Fin n → R)
    (N : Type v) [AddCommGroup N] [Module R N] :
    Stacks.RelationsOfSequence.idealI f ≤ Module.annihilator R (FormalGlueing.firstRelationHomology
      f N)
```

## Tag 05EG, a lemma

[Tag 05EG](https://stacks.math.columbia.edu/tag/05EG) in the Stacks Project.

**`FormalGlueing.exists_shortExactSequence_lift_of_flat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean, line 1312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingFlatIsomorphism.lean#L1312).

> A short exact sequence over `S` ending in the base change of an
> `I`-power torsion module fits below a short exact sequence over `R`, provided `R → S` is flat
> and induces an isomorphism modulo the finitely generated ideal `I`.

```lean
public theorem exists_shortExactSequence_lift_of_flat_baseChange
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    (I : Ideal R) (hI : I.FG) (hflat : Module.Flat R S)
    (hq : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap R S)) (algebraMap R S) Ideal.le_comap_map))
    (M : Type w) [AddCommGroup M] [Module R M]
    (N : Type x) [AddCommGroup N] [Module R N]
    (hM : IsIPowerTorsion R M I)
    (E' : Type y) [AddCommGroup E'] [Module R E'] [Module S E'] [IsScalarTower R S E']
    (i : TensorProduct R S N →ₗ[S] E')
    (p : E' →ₗ[S] TensorProduct R S M)
    (hi : Function.Injective i) (hp : Function.Surjective p)
    (hexact : Function.Exact i p) :
    ∃ (E : Type (max x (max w y))) (_ : AddCommGroup E) (_ : Module R E)
      (a : N →ₗ[R] E) (b : E →ₗ[R] M) (c : E →ₗ[R] E'),
      Function.Injective a ∧ Function.Exact a b ∧ Function.Surjective b ∧
        c.comp a = (i.restrictScalars R).comp ((TensorProduct.mk R S N) 1) ∧
        ((TensorProduct.mk R S M) 1).comp b = (p.restrictScalars R).comp c
```

## Tag 05EJ, an equation

[Tag 05EJ](https://stacks.math.columbia.edu/tag/05EJ) in the Stacks Project.

**`FormalGlueing.glueingBeta_comp_glueingAlpha`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingComplex/Basic.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingComplex/Basic.lean#L157).

> The maps `glueingAlpha` and `glueingBeta` form the glueing complex of Stacks Project,
> Tag 05EJ.

```lean
public theorem glueingBeta_comp_glueingAlpha :
    (glueingBeta S f M).comp (glueingAlpha S f M) = 0
```

## Tag 05EK, a lemma

[Tag 05EK](https://stacks.math.columbia.edu/tag/05EK) in the Stacks Project.

**`FormalGlueing.glueingComplex_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingComplex/Exact.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingComplex/Exact.lean#L429).

> If `R → S` is flat and induces an isomorphism modulo the ideal generated by `f`, then the
> glueing complex of every `R`-module is exact, including at its initial term.

```lean
public theorem glueingComplex_exact
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    {r : ℕ} (f : Fin r → R) (M : Type w) [AddCommGroup M] [Module R M]
    (hflat : Module.Flat R S)
    (hq : Function.Bijective
      (Ideal.quotientMap
        ((Ideal.span (Set.range f)).map (algebraMap R S))
        (algebraMap R S) Ideal.le_comap_map)) :
    Function.Injective (glueingAlpha S f M) ∧
      Function.Exact (glueingAlpha S f M) (glueingBeta S f M)
```

## Tag 05EL, a remark

[Tag 05EL](https://stacks.math.columbia.edu/tag/05EL) in the Stacks Project.

**`FormalGlueing.moduleGlueingConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingCategory/Adjunction.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingCategory/Adjunction.lean#L166).

> The category `Glue(R → S, f₁, …, fₜ)`, its canonical functor from `R`-modules, and its
> compatible-sections functor `H⁰`.

```lean
public noncomputable def moduleGlueingConstruction : ModuleGlueingConstruction S f
```

## Tag 0H77, a lemma

[Tag 0H77](https://stacks.math.columbia.edu/tag/0H77) in the Stacks Project.

**`FormalGlueing.canonicalSectionsAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingCategory/Adjunction.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingCategory/Adjunction.lean#L572).

> The compatible-sections functor `H⁰` on module glueing data is right adjoint to the canonical
> glueing-data functor.

```lean
public noncomputable def canonicalSectionsAdjunction
    {R : Type u} [CommRing R] (S : Type v) [CommRing S] [Algebra R S]
    {r : ℕ} (f : Fin r → R)
    (C : FormalGlueing.ModuleGlueingConstruction.{u, v, w} S f) :
    letI := C.category
    C.canonical ⊣ C.sections
```

## Tag 05EM, a lemma

[Tag 05EM](https://stacks.math.columbia.edu/tag/05EM) in the Stacks Project.

**`FormalGlueing.canonicalSectionsUnit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/LeftQuasiInverse.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/LeftQuasiInverse.lean#L261).

> If a flat ring map is an isomorphism modulo the ideal generated by `f`, then compatible
> sections are a left quasi-inverse to the canonical module glueing functor.

```lean
public theorem canonicalSectionsUnit_isIso
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    {r : ℕ} (f : Fin r → R) (hflat : Module.Flat R S)
    (hq : Function.Bijective
      (Ideal.quotientMap
        ((Ideal.span (Set.range f)).map (algebraMap R S))
        (algebraMap R S) Ideal.le_comap_map)) :
    let c := moduleGlueingConstruction.{u, v, w} S f
    letI := c.category
    IsIso c.canonicalSectionsUnit
```

## Tag 05EN, a lemma

[Tag 05EN](https://stacks.math.columbia.edu/tag/05EN) in the Stacks Project.

**`FormalGlueing.moduleGlueingConstruction_abelian_exact_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingCategory/Abelian.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingCategory/Abelian.lean#L735).

> For a flat ring map, the category of module glueing data is abelian, and the canonical
> functor from modules is exact and preserves arbitrary colimits.

```lean
public theorem moduleGlueingConstruction_abelian_exact_preservesColimits
    {R : Type u} [CommRing R] (S : Type v) [CommRing S] [Algebra R S] [Module.Flat R S]
    {r : ℕ} (f : Fin r → R) :
    let c := moduleGlueingConstruction.{u, v, w} S f
    letI := c.category
    Nonempty (Abelian (ModuleGlueingDatum.{u, v, w} S f c.comparison)) ∧
      exactFunctor (ModuleCat.{max u v w} R)
        (ModuleGlueingDatum.{u, v, w} S f c.comparison) c.canonical ∧
      PreservesColimits c.canonical
```

## Tag 05EP, a lemma

[Tag 05EP](https://stacks.math.columbia.edu/tag/05EP) in the Stacks Project.

**`FormalGlueing.canonicalFunctor_sections_areQuasiInverse_of_span_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/UnitIdeal.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/UnitIdeal.lean#L303).

> If a finite family generates the unit ideal and `R → S` is flat, then the canonical module
> glueing functor and compatible sections are quasi-inverse equivalences of categories.

```lean
public theorem canonicalFunctor_sections_areQuasiInverse_of_span_eq_top
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    {r : ℕ} (f : Fin r → R) (hflat : Module.Flat R S)
    (hf : Ideal.span (Set.range f) = ⊤) :
    let c := moduleGlueingConstruction.{u, v, w} S f
    letI := c.category
    ∃ e : ModuleCat.{max u v w} R ≌ ModuleGlueingDatum.{u, v, w} S f c.comparison,
      e.functor = c.canonical ∧ e.inverse = c.sections
```

## Tag 05EQ, a lemma

[Tag 05EQ](https://stacks.math.columbia.edu/tag/05EQ) in the Stacks Project.

**`FormalGlueing.exists_baseChange_commuting_with_canonical_and_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/BaseChange.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/BaseChange.lean#L544).

> **Stacks 05EQ.** Flat base change defines a functor on module glueing data which commutes,
> up to natural isomorphism, with the canonical glueing-data functor and compatible global
> sections. Its generic and local components, including their action on morphisms, are the
> corresponding scalar-extension functors.

```lean
public theorem exists_baseChange_commuting_with_canonical_and_sections
    (R : Type u) (S : Type v) (R' : Type x)
    [CommRing R] [CommRing S] [CommRing R'] [Algebra R S] [Algebra R R']
    {r : ℕ} (f : Fin r → R) (I : Ideal R) (hI : I = Ideal.span (Set.range f))
    (hS : Module.Flat R S) (hR' : Module.Flat R R') :
    let upper := FormalGlueing.moduleGlueingConstruction.{u, v, max u v x w} S f
    let lower := FormalGlueing.moduleGlueingConstruction.{x, max v x, max u v x w}
      (TensorProduct R S R') (fun i ↦ algebraMap R R' (f i))
    letI := upper.category
    letI := lower.category
    let genericMap : S →+* TensorProduct R S R' :=
      Algebra.TensorProduct.includeLeftRingHom
    let localMap : ∀ i, Localization.Away (f i) →+*
        Localization.Away (algebraMap R R' (f i)) := fun i ↦
      IsLocalization.Away.map (Localization.Away (f i))
        (Localization.Away (algebraMap R R' (f i))) (algebraMap R R') (f i)
    ∃ (baseChange :
        FormalGlueing.ModuleGlueingDatum S f upper.comparison ⥤
          FormalGlueing.ModuleGlueingDatum (TensorProduct R S R')
            (fun i ↦ algebraMap R R' (f i)) lower.comparison)
      (genericIso : ∀ X, (baseChange.obj X).generic ≅
        (ModuleCat.extendScalars genericMap).obj X.generic)
      (localIso : ∀ X i, (baseChange.obj X).localPiece i ≅
        (ModuleCat.extendScalars (localMap i)).obj (X.localPiece i))
      (genericLocalizationIso : ∀ X i,
        LocalizedModule.Away
            (algebraMap R' (TensorProduct R S R') (algebraMap R R' (f i)))
            (baseChange.obj X).generic ≃ₗ[TensorProduct R S R']
          TensorProduct S (TensorProduct R S R')
            (LocalizedModule.Away (algebraMap R S (f i)) X.generic))
      (genericLocalTensorIso : ∀ X i,
        TensorProduct R' (TensorProduct R S R')
            (FormalGlueing.restrictFromAway
              (R := R') (fun i ↦ algebraMap R R' (f i)) i
              ((baseChange.obj X).localPiece i)) ≃ₗ[TensorProduct R S R']
          TensorProduct S (TensorProduct R S R')
            (TensorProduct R S
              (FormalGlueing.restrictFromAway (R := R) f i (X.localPiece i))))
      (localOverlapIso : ∀ X i j,
        Cech.cechMod (fun i ↦ algebraMap R R' (f i))
            (FormalGlueing.restrictFromAway
              (R := R') (fun i ↦ algebraMap R R' (f i)) i
              ((baseChange.obj X).localPiece i)) {j} ≃ₗ[R']
          TensorProduct R R'
            (Cech.cechMod f
              (FormalGlueing.restrictFromAway (R := R) f i (X.localPiece i)) {j})),
      (∀ {X Y} (g : X ⟶ Y),
        (lower.homEquiv (baseChange.obj X) (baseChange.obj Y)
              (baseChange.map g)).generic ≫ (genericIso Y).hom =
          (genericIso X).hom ≫
            (ModuleCat.extendScalars genericMap).map
              (upper.homEquiv X Y g).generic) ∧
        (∀ {X Y} (g : X ⟶ Y) i,
          (lower.homEquiv (baseChange.obj X) (baseChange.obj Y)
                (baseChange.map g)).localPiece i ≫ (localIso Y i).hom =
            (localIso X i).hom ≫
              (ModuleCat.extendScalars (localMap i)).map
                ((upper.homEquiv X Y g).localPiece i)) ∧
        (∀ X i (m : X.generic) (t : TensorProduct R S R'),
          genericLocalizationIso X i
              (LocalizedModule.mkLinearMap
                (Submonoid.powers
                  (algebraMap R' (TensorProduct R S R') (algebraMap R R' (f i)))) _
                ((genericIso X).inv (t ⊗ₜ[S] m))) =
            t ⊗ₜ[S]
              LocalizedModule.mkLinearMap
                (Submonoid.powers (algebraMap R S (f i))) _ m) ∧
        (∀ (X : FormalGlueing.ModuleGlueingDatum S f upper.comparison) i,
          letI : Module R (X.localPiece i) :=
            Module.compHom _ (algebraMap R (Localization.Away (f i)))
          ∀ (m : X.localPiece i) (t : TensorProduct R S R'),
          genericLocalTensorIso X i
              (t ⊗ₜ[R'] (localIso X i).inv
                ((1 : Localization.Away (algebraMap R R' (f i)))
                  ⊗ₜ[Localization.Away (f i)] m)) =
            t ⊗ₜ[S] (1 ⊗ₜ[R] m)) ∧
        (∀ (X : FormalGlueing.ModuleGlueingDatum S f upper.comparison) i j,
          letI : Module R (X.localPiece i) :=
            Module.compHom _ (algebraMap R (Localization.Away (f i)))
          ∀ (m : X.localPiece i),
          localOverlapIso X i j
              (LocalizedModule.mkLinearMap
                (Cech.cechSub (fun i ↦ algebraMap R R' (f i)) {j}) _
                ((localIso X i).inv
                  ((1 : Localization.Away (algebraMap R R' (f i)))
                    ⊗ₜ[Localization.Away (f i)] m))) =
            1 ⊗ₜ[R]
              LocalizedModule.mkLinearMap (Cech.cechSub f {j}) _ m) ∧
        (∀ X i d,
          genericLocalTensorIso X i ((baseChange.obj X).alpha i d) =
            TensorProduct.map LinearMap.id (X.alpha i).toLinearMap
              (genericLocalizationIso X i d)) ∧
        (∀ X i j d,
          localOverlapIso X j i ((baseChange.obj X).alphaIJ i j d) =
            TensorProduct.map LinearMap.id (X.alphaIJ i j).toLinearMap
              (localOverlapIso X i j d)) ∧
        Nonempty
          (upper.canonical ⋙ baseChange ≅
            ModuleCat.extendScalars (algebraMap R R') ⋙ lower.canonical) ∧
        Nonempty
          (upper.sections ⋙ ModuleCat.extendScalars (algebraMap R R') ≅
            baseChange ⋙ lower.sections)
```

## Tag 05ER, a proposition

[Tag 05ER](https://stacks.math.columbia.edu/tag/05ER) in the Stacks Project.

**`FormalGlueing.canonicalFunctor_sections_areQuasiInverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/MainTheorem.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/MainTheorem.lean#L281).

> **Stacks 05ER.** For a flat ring map inducing an isomorphism modulo the ideal generated by
> `f`, the canonical module glueing functor and compatible sections are quasi-inverse equivalences
> of categories.

```lean
public theorem canonicalFunctor_sections_areQuasiInverse
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    {r : ℕ} (f : Fin r → R) (hflat : Module.Flat R S)
    (hq : Function.Bijective
      (Ideal.quotientMap
        ((Ideal.span (Set.range f)).map (algebraMap R S))
        (algebraMap R S) Ideal.le_comap_map)) :
    let c := moduleGlueingConstruction.{u, v, w} S f
    letI := c.category
    ∃ e : ModuleCat.{max u v w} R ≌ ModuleGlueingDatum.{u, v, w} S f c.comparison,
      e.functor = c.canonical ∧ e.inverse = c.sections
```

## Tag 0ALK, a lemma

[Tag 0ALK](https://stacks.math.columbia.edu/tag/0ALK) in the Stacks Project.

**`FormalGlueing.exists_descent_of_idealPowerTorsion_kernel_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/MainTheorem.lean, line 747](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/MainTheorem.lean#L747).

> **Stacks 0ALK.** A map to or from an extended module whose kernel and cokernel are
> ideal-power torsion descends at the level of its source or target module, with the
> given map recovered by extension of scalars and with the same kernel and cokernel after
> restriction of scalars.

```lean
public theorem exists_descent_of_idealPowerTorsion_kernel_cokernel
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    (I : Ideal R) (hI : I.FG) (hflat : Module.Flat R S)
    (hq : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap R S)) (algebraMap R S) Ideal.le_comap_map)) :
    let E := ModuleCat.extendScalars.{u, v, max u v w} (algebraMap R S)
    let U := ModuleCat.restrictScalars.{max u v w} (algebraMap R S)
    (∀ (N : ModuleCat.{max u v w} R) (M' : ModuleCat.{max u v w} S)
      (φ : M' ⟶ E.obj N),
      IsIPowerTorsion S
        (↥(kernel φ : ModuleCat.{max u v w} S)) (I.map (algebraMap R S)) →
      IsIPowerTorsion S
        (↥(cokernel φ : ModuleCat.{max u v w} S)) (I.map (algebraMap R S)) →
      ∃ (M : ModuleCat.{max u v w} R) (ψ : M ⟶ N) (e : E.obj M ≅ M')
          (_eKer : U.obj (kernel φ) ≅ kernel ψ)
          (_eCoker : U.obj (cokernel φ) ≅ cokernel ψ),
        e.hom ≫ φ = E.map ψ) ∧
    (∀ (M : ModuleCat.{max u v w} R) (N' : ModuleCat.{max u v w} S)
      (φ : E.obj M ⟶ N'),
      IsIPowerTorsion S
        (↥(kernel φ : ModuleCat.{max u v w} S)) (I.map (algebraMap R S)) →
      IsIPowerTorsion S
        (↥(cokernel φ : ModuleCat.{max u v w} S)) (I.map (algebraMap R S)) →
      ∃ (N : ModuleCat.{max u v w} R) (ψ : M ⟶ N) (e : E.obj N ≅ N')
          (_eKer : U.obj (kernel φ) ≅ kernel ψ)
          (_eCoker : U.obj (cokernel φ) ≅ cokernel ψ),
        E.map ψ ≫ e.hom = φ)
```

## Tag 05ES, a theorem

[Tag 05ES](https://stacks.math.columbia.edu/tag/05ES) in the Stacks Project.

**`FormalGlueing.exists_canonicalModuleGlueingEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingModuleProperties/PrincipalLocalization.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingModuleProperties/PrincipalLocalization.lean#L523).

> **Stacks 05ES.** For a flat ring map inducing an isomorphism modulo `(f)`, the canonical
> functor from modules over the source to pairs of modules identified after localization is an
> equivalence of categories.

```lean
public theorem exists_canonicalModuleGlueingEquivalence
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
    (f : R) (hflat : Module.Flat R S)
    (hq : Function.Bijective
      (Ideal.quotientMap
        ((Ideal.span {f}).map (algebraMap R S))
        (algebraMap R S) Ideal.le_comap_map)) :
    let Rf := Localization.Away f
    let Sf := Localization.Away (algebraMap R S f)
    let ρ := principalLocalizationMap R S f
    letI : Algebra Rf Sf := ρ.toAlgebra
    let generic := ModuleCat.extendScalars.{u, v, max u v w} (algebraMap R S)
    let localPiece := ModuleCat.extendScalars.{u, u, max u v w} (algebraMap R Rf)
    let genericOverlap := ModuleCat.extendScalars.{v, v, max u v w} (algebraMap S Sf)
    let localOverlap := ModuleCat.extendScalars.{u, v, max u v w} (algebraMap Rf Sf)
    ∃ comparison : generic ⋙ genericOverlap ≅ localPiece ⋙ localOverlap,
      (∀ (M : ModuleCat.{max u v w} R) (m : M),
        comparison.hom.app M
            ((ModuleCat.extendRestrictScalarsAdj.{max u v w, v, v}
              (algebraMap S Sf)).unit.app
              (generic.obj M)
              ((ModuleCat.extendRestrictScalarsAdj.{max u v w, u, v}
                (algebraMap R S)).unit.app M m)) =
          (ModuleCat.extendRestrictScalarsAdj.{max u v w, u, v}
            (algebraMap Rf Sf)).unit.app
            (localPiece.obj M)
            ((ModuleCat.extendRestrictScalarsAdj.{max u v w, u, u}
              (algebraMap R Rf)).unit.app M m)) ∧
      ((CategoricalPullback.CatCommSqOver.toFunctorToCategoricalPullback
        genericOverlap localOverlap (ModuleCat.{max u v w} R)).obj
        { fst := generic
          snd := localPiece
          iso := comparison }).IsEquivalence
```

## Tag 05ET, a proposition

[Tag 05ET](https://stacks.math.columbia.edu/tag/05ET) in the Stacks Project.

**`FormalGlueing.exists_adicCompletionGlueingEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingModuleProperties/AdicCompletion.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingModuleProperties/AdicCompletion.lean#L327).

> **Stacks 05ET.** Over a Noetherian ring, finitely generated modules are equivalent to
> finitely generated modules on the adic completion and on the complementary principal open,
> identified over their common localization.

```lean
public theorem exists_adicCompletionGlueingEquivalence
    (R : Type u) [CommRing R] [IsNoetherianRing R] (f : R) :
    let I := Ideal.span {f}
    let Rhat := AdicCompletion I R
    let Rf := Localization.Away f
    let Sf := Localization.Away (algebraMap R Rhat f)
    let ρ := FormalGlueing.principalLocalizationMap R Rhat f
    letI : Algebra Rf Sf := ρ.toAlgebra
    let completion := finiteAdicCompletion R I
    let localPiece := finiteExtensionOfScalars R Rf
    let completionOverlap := finiteExtensionOfScalars Rhat Sf
    let localOverlap := finiteExtensionOfScalars Rf Sf
    ∃ comparison : completion ⋙ completionOverlap ≅ localPiece ⋙ localOverlap,
      (∀ (M : FGModuleCat.{u} R) (m : M) (s : Sf),
        comparison.hom.app M
            (s ⊗ₜ[Rhat] AdicCompletion.of I M m) =
          s ⊗ₜ[Rf] ((1 : Rf) ⊗ₜ[R] m)) ∧
      ((CategoricalPullback.CatCommSqOver.toFunctorToCategoricalPullback
        completionOverlap localOverlap (FGModuleCat.{u} R)).obj
        { fst := completion
          snd := localPiece
          iso := comparison }).IsEquivalence
```

## Tag 05EU, a remark

[Tag 05EU](https://stacks.math.columbia.edu/tag/05EU) in the Stacks Project.

**`FormalGlueing.formalGlueing_preserves_moduleProperties_tensor_and_algebras`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingModuleProperties/Properties.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingModuleProperties/Properties.lean#L608).

> **Stacks 05EU.** Formal glueing detects the standard finiteness and flatness properties,
> is pointwise symmetric monoidal, and hence induces an equivalence on commutative algebra objects.
> The final two clauses state property detection, pointwise symmetry, and the canonical commutative
> algebra equivalence for the principal-localization and adic-completion functors of Tags 05ES
> and 05ET.

```lean
public theorem formalGlueing_preserves_moduleProperties_tensor_and_algebras :
    (∀ (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
      (r : ℕ) (f : Fin r → R) (hflat : Module.Flat R S)
      (hq : Function.Bijective
        (Ideal.quotientMap
          ((Ideal.span (Set.range f)).map (algebraMap R S))
          (algebraMap R S) Ideal.le_comap_map)),
      let c := moduleGlueingConstruction.{u, v, w} S f
      letI := c.category
      let G := ModuleGlueingDatum.{u, v, w} S f c.comparison
      ∃ (sourceTensor : LargeModuleMonoidalStructure.{u, max u v w} R)
          (genericTensor : LargeModuleMonoidalStructure.{v, max u v w} S)
          (localTensor : ∀ i, LargeModuleMonoidalStructure.{u, max u v w}
            (Localization.Away (f i)))
          (glueingTensor : MonoidalCategory G)
          (e : ModuleCat.{max u v w} R ≌ G),
        letI := sourceTensor.monoidal
        letI := genericTensor.monoidal
        letI (i : Fin r) := (localTensor i).monoidal
        letI := sourceTensor.symmetric
        letI := genericTensor.symmetric
        letI (i : Fin r) := (localTensor i).symmetric
        letI := glueingTensor
        ∃ (_ : SymmetricCategory G)
            (_ : (genericProjection S f c).Braided)
            (_ : ∀ i, (localProjection S f c i).Braided)
            (_ : c.canonical.Braided) (_ : c.sections.Braided)
            (_ : e.functor.Braided) (_ : e.inverse.Braided) (_ : e.IsMonoidal),
          e.functor = c.canonical ∧ e.inverse = c.sections ∧
          (∀ M : ModuleCat.{max u v w} R,
            (Module.Finite R M ↔
              Module.Finite S (e.functor.obj M).generic ∧
                ∀ i, Module.Finite (Localization.Away (f i))
                  ((e.functor.obj M).localPiece i)) ∧
            (Module.FinitePresentation R M ↔
              Module.FinitePresentation S (e.functor.obj M).generic ∧
                ∀ i, Module.FinitePresentation (Localization.Away (f i))
                  ((e.functor.obj M).localPiece i)) ∧
            (Module.Flat R M ↔
              Module.Flat S (e.functor.obj M).generic ∧
                ∀ i, Module.Flat (Localization.Away (f i))
                  ((e.functor.obj M).localPiece i)) ∧
            (Module.Projective R M ↔
              Module.Projective S (e.functor.obj M).generic ∧
                ∀ i, Module.Projective (Localization.Away (f i))
                  ((e.functor.obj M).localPiece i))) ∧
          ∃ algebraEquivalence : CommMon (ModuleCat.{max u v w} R) ≌ CommMon G,
            algebraEquivalence = e.mapCommMon) ∧
    (∀ (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
      (f : R) (hflat : Module.Flat R S)
      (hq : Function.Bijective
        (Ideal.quotientMap ((Ideal.span {f}).map (algebraMap R S))
          (algebraMap R S) Ideal.le_comap_map)),
      let Rf := Localization.Away f
      let Sf := Localization.Away (algebraMap R S f)
      let ρ := FormalGlueing.principalLocalizationMap R S f
      letI : Algebra Rf Sf := ρ.toAlgebra
      let generic := ModuleCat.extendScalars.{u, v, max u v w} (algebraMap R S)
      let localPiece := ModuleCat.extendScalars.{u, u, max u v w} (algebraMap R Rf)
      let genericOverlap := ModuleCat.extendScalars.{v, v, max u v w} (algebraMap S Sf)
      let localOverlap := ModuleCat.extendScalars.{u, v, max u v w} (algebraMap Rf Sf)
      ∃ comparison : generic ⋙ genericOverlap ≅ localPiece ⋙ localOverlap,
        (∀ (M : ModuleCat.{max u v w} R) (m : M),
          comparison.hom.app M
              ((ModuleCat.extendRestrictScalarsAdj.{max u v w, v, v}
                (algebraMap S Sf)).unit.app
                (generic.obj M)
                ((ModuleCat.extendRestrictScalarsAdj.{max u v w, u, v}
                  (algebraMap R S)).unit.app M m)) =
            (ModuleCat.extendRestrictScalarsAdj.{max u v w, u, v}
              (algebraMap Rf Sf)).unit.app
              (localPiece.obj M)
              ((ModuleCat.extendRestrictScalarsAdj.{max u v w, u, u}
                (algebraMap R Rf)).unit.app M m)) ∧
        let F := (CategoricalPullback.CatCommSqOver.toFunctorToCategoricalPullback
          genericOverlap localOverlap (ModuleCat.{max u v w} R)).obj
          { fst := generic, snd := localPiece, iso := comparison }
        ∃ (sourceTensor : LargeModuleMonoidalStructure.{u, max u v w} R)
            (genericTensor : LargeModuleMonoidalStructure.{v, max u v w} S)
            (localTensor : LargeModuleMonoidalStructure.{u, max u v w} Rf)
            (overlapTensor : LargeModuleMonoidalStructure.{v, max u v w} Sf)
            (glueingTensor : MonoidalCategory
              (CategoricalPullback genericOverlap localOverlap))
            (e : ModuleCat.{max u v w} R ≌
              CategoricalPullback genericOverlap localOverlap),
          letI := sourceTensor.monoidal
          letI := genericTensor.monoidal
          letI := localTensor.monoidal
          letI := overlapTensor.monoidal
          letI := sourceTensor.symmetric
          letI := genericTensor.symmetric
          letI := localTensor.symmetric
          letI := overlapTensor.symmetric
          letI := glueingTensor
          ∃ (_ : SymmetricCategory (CategoricalPullback genericOverlap localOverlap))
              (_ : generic.Braided) (_ : localPiece.Braided)
              (_ : genericOverlap.Braided) (_ : localOverlap.Braided)
              (_ : comparison.hom.IsMonoidal)
              (_ : (CategoricalPullback.π₁ genericOverlap localOverlap).Braided)
              (_ : (CategoricalPullback.π₂ genericOverlap localOverlap).Braided)
              (_ : F.Braided) (_ : e.functor.Braided) (_ : e.inverse.Braided)
              (_ : e.IsMonoidal),
            e.functor = F ∧
            (∀ M : ModuleCat.{max u v w} R,
              (Module.Finite R M ↔ Module.Finite S (F.obj M).fst ∧
                Module.Finite Rf (F.obj M).snd) ∧
              (Module.FinitePresentation R M ↔
                Module.FinitePresentation S (F.obj M).fst ∧
                  Module.FinitePresentation Rf (F.obj M).snd) ∧
              (Module.Flat R M ↔ Module.Flat S (F.obj M).fst ∧
                Module.Flat Rf (F.obj M).snd) ∧
              (Module.Projective R M ↔ Module.Projective S (F.obj M).fst ∧
                Module.Projective Rf (F.obj M).snd)) ∧
            ∃ algebraEquivalence : CommMon (ModuleCat.{max u v w} R) ≌
                CommMon (CategoricalPullback genericOverlap localOverlap),
              algebraEquivalence = e.mapCommMon) ∧
    (∀ (R : Type u) [CommRing R] [IsNoetherianRing R] (f : R),
      let I := Ideal.span {f}
      let Rhat := AdicCompletion I R
      let Rf := Localization.Away f
      let Sf := Localization.Away (algebraMap R Rhat f)
      let ρ := FormalGlueing.principalLocalizationMap R Rhat f
      letI : Algebra Rf Sf := ρ.toAlgebra
      let completion := FormalGlueing.finiteAdicCompletion R I
      let localPiece := FormalGlueing.finiteExtensionOfScalars R Rf
      let completionOverlap := FormalGlueing.finiteExtensionOfScalars Rhat Sf
      let localOverlap := FormalGlueing.finiteExtensionOfScalars Rf Sf
      ∃ comparison : completion ⋙ completionOverlap ≅ localPiece ⋙ localOverlap,
        (∀ (M : FGModuleCat.{u} R) (m : M) (s : Sf),
          comparison.hom.app M (s ⊗ₜ[Rhat] AdicCompletion.of I M m) =
            s ⊗ₜ[Rf] ((1 : Rf) ⊗ₜ[R] m)) ∧
        let F := (CategoricalPullback.CatCommSqOver.toFunctorToCategoricalPullback
          completionOverlap localOverlap (FGModuleCat.{u} R)).obj
          { fst := completion, snd := localPiece, iso := comparison }
        ∃ (glueingTensor : MonoidalCategory
              (CategoricalPullback completionOverlap localOverlap))
            (e : FGModuleCat.{u} R ≌
              CategoricalPullback completionOverlap localOverlap),
          letI := glueingTensor
          ∃ (_ : SymmetricCategory (CategoricalPullback completionOverlap localOverlap))
              (_ : completion.Braided) (_ : localPiece.Braided)
              (_ : completionOverlap.Braided) (_ : localOverlap.Braided)
              (_ : comparison.hom.IsMonoidal)
              (_ : (CategoricalPullback.π₁ completionOverlap localOverlap).Braided)
              (_ : (CategoricalPullback.π₂ completionOverlap localOverlap).Braided)
              (_ : F.Braided) (_ : e.functor.Braided) (_ : e.inverse.Braided)
              (_ : e.IsMonoidal),
            e.functor = F ∧
            (∀ M : FGModuleCat.{u} R,
              (Module.Finite R M ↔ Module.Finite Rhat (F.obj M).fst ∧
                Module.Finite Rf (F.obj M).snd) ∧
              (Module.FinitePresentation R M ↔
                Module.FinitePresentation Rhat (F.obj M).fst ∧
                  Module.FinitePresentation Rf (F.obj M).snd) ∧
              (Module.Flat R M ↔ Module.Flat Rhat (F.obj M).fst ∧
                Module.Flat Rf (F.obj M).snd) ∧
              (Module.Projective R M ↔ Module.Projective Rhat (F.obj M).fst ∧
                Module.Projective Rf (F.obj M).snd)) ∧
            ∃ algebraEquivalence : CommMon (FGModuleCat.{u} R) ≌
                CommMon (CategoricalPullback completionOverlap localOverlap),
              algebraEquivalence = e.mapCommMon)
```

## Tag 05EV, a remark

[Tag 05EV](https://stacks.math.columbia.edu/tag/05EV) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Sheaf.sheafEquivGlueData`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Glueing/Equivalence.lean#L188), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/MainTheorem.lean, line 811](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/FormalGlueingEquivalence/MainTheorem.lean#L811) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.91, Tag 05E5](https://stacks.math.columbia.edu/tag/05E5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
