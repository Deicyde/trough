---
declaration: section
origin: cited
lean: StacksDraft.Perfect.IsPerfect, StacksDraft.Perfect.IsPerfectModule, StacksDraft.Perfect.isPerfect_iff_pseudoCoherent_and_finiteTorDimension, StacksDraft.Perfect.isPerfectModule_iff_exists_finite_projective_resolution, StacksDraft.Perfect.isPerfect_of_distinguished, StacksDraft.Perfect.isPerfect_of_biproduct, StacksDraft.Perfect.isPerfect_of_bounded_of_isPerfectModule, StacksDraft.Perfect.isPerfect_of_bounded_of_cohomology_isPerfect
statement: formalized
proof: formalized
---

# 15.76 Perfect complexes

Section 15.76 of the Stacks Project, [Tag 0656](https://stacks.math.columbia.edu/tag/0656). 18 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0657, a definition

[Tag 0657](https://stacks.math.columbia.edu/tag/0657) in the Stacks Project.

**`StacksDraft.Perfect.IsPerfect`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Defs.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Defs.lean#L48). The attribute's comment: “(1)”. References: SGA 6 I (4.8), “affine (ring) case”; SGA 6 II (2.2.1), “affine case, perfect”.

> **Stacks 0657 (1).** An object of the derived category of `R`-modules is *perfect* if it is
> isomorphic to a bounded complex of finite projective `R`-modules.

```lean
def IsPerfect {R : Type u} [Ring R]
    [HasDerivedCategory.{w} (ModuleCat.{v} R)]
    (K : DerivedCategory (ModuleCat.{v} R)) : Prop
```

**`StacksDraft.Perfect.IsPerfectModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Defs.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Defs.lean#L62). The attribute's comment: “(2)”. References: SGA 6 I (4.8), “affine case, module”; SGA 6 II (2.2.1), “affine, degree-0 module”.

> **Stacks 0657 (2).** An `R`-module is *perfect* if the complex consisting of it placed in
> degree zero is a perfect object of the derived category of `R`-modules.

```lean
def IsPerfectModule {R : Type u} [Ring R]
    (M : Type v) [AddCommGroup M] [Module R M]
    [HasDerivedCategory.{w} (ModuleCat.{v} R)] : Prop
```

## Tag 0658, a lemma

[Tag 0658](https://stacks.math.columbia.edu/tag/0658) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_iff_pseudoCoherent_and_finiteTorDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Basic.lean, line 1054](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Basic.lean#L1054). References: SGA 5 VIII (8.1), “commutative rings only”; SGA 6 I (5.8.1), “module over a ring”; SGA 6 I (5.8), “special case”.

> **Stacks 0658.** An object of `D(R)` is perfect if and only if it is pseudo-coherent and has
> finite Tor dimension, the latter being recorded by the existence of a bounded flat representative.
> Moreover a pseudo-coherent object whose Tor amplitude lies in `[a, b]` is represented by a complex
> of finite projective modules concentrated in the degrees `[a, b]`.

```lean
theorem isPerfect_iff_pseudoCoherent_and_finiteTorDimension
    {R : Type u} [CommRing R] (K : DerivedCategory (ModuleCat.{max u v} R)) :
    (IsPerfect K ↔
      StacksDraft.PseudoCoherence.IsPseudoCoherent K ∧
        ∃ a b : ℤ, HasFlatRepresentative K a b) ∧
      ∀ a b : ℤ, StacksDraft.PseudoCoherence.IsPseudoCoherent K →
        HasFlatRepresentative K a b →
        ∃ E : CochainComplex (ModuleCat.{max u v} R) ℤ,
          (∀ i : ℤ, Module.Finite R (E.X i) ∧ Module.Projective R (E.X i)) ∧
            E.IsStrictlyGE a ∧ E.IsStrictlyLE b ∧
              Nonempty (K ≅ DerivedCategory.Q.obj E)
```

## Tag 066Q, a lemma

[Tag 066Q](https://stacks.math.columbia.edu/tag/066Q) in the Stacks Project.

**`StacksDraft.Perfect.isPerfectModule_iff_exists_finite_projective_resolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Module.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Module.lean#L200).

> **Stacks 066Q.** An `R`-module is perfect if and only if it has a finite resolution by finite
> projective `R`-modules.

```lean
theorem isPerfectModule_iff_exists_finite_projective_resolution
    {R : Type u} [CommRing R] (M : Type v) [AddCommGroup M] [Module R M] :
    IsPerfectModule (R := R) M ↔
      ∃ (d : ℕ) (F : ModuleResolution R M),
        (∀ i : ℕ, Module.Finite R (F.complex.X i) ∧ Module.Projective R (F.complex.X i)) ∧
          ∀ i : ℕ, d < i → IsZero (F.complex.X i)
```

## Tag 066R, a lemma

[Tag 066R](https://stacks.math.columbia.edu/tag/066R) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_of_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Basic.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Basic.lean#L219).

> **Stacks 066R.** In a distinguished triangle in `D(R)`, if two of the three objects are
> perfect, then so is the third.

```lean
theorem isPerfect_of_distinguished
    {R : Type u} [Ring R] [HasDerivedCategory (ModuleCat.{v} R)]
    (T : Triangle (DerivedCategory (ModuleCat.{v} R)))
    (hT : T ∈ distinguishedTriangles) :
    (IsPerfect T.obj₁ → IsPerfect T.obj₂ → IsPerfect T.obj₃) ∧
    (IsPerfect T.obj₁ → IsPerfect T.obj₃ → IsPerfect T.obj₂) ∧
    (IsPerfect T.obj₂ → IsPerfect T.obj₃ → IsPerfect T.obj₁)
```

## Tag 066S, a lemma

[Tag 066S](https://stacks.math.columbia.edu/tag/066S) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_of_biproduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Basic.lean, line 917](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Basic.lean#L917).

> **Stacks 066S.** If a binary biproduct of objects of `D(R)` is perfect, then both summands are
> perfect. Perfectness passes to the summands at arbitrary carrier universes: a small projective
> coefficient quotient supporting the given bounded complex supplies the internal descent.

```lean
theorem isPerfect_of_biproduct
    {R : Type u} [CommRing R] (K L : DerivedCategory (ModuleCat.{v} R))
    (h : IsPerfect (K ⊞ L)) :
    IsPerfect K ∧ IsPerfect L
```

## Tag 066T, a lemma

[Tag 066T](https://stacks.math.columbia.edu/tag/066T) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_of_bounded_of_isPerfectModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Basic.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Basic.lean#L283).

> **Stacks 066T.** A bounded complex of perfect modules over a ring represents a perfect object
> of the derived category.

```lean
theorem isPerfect_of_bounded_of_isPerfectModule
    {R : Type u} [CommRing R]
    (K : CochainComplex (ModuleCat.{v} R) ℤ)
    (hK : ∃ a b : ℤ, K.IsStrictlyGE a ∧ K.IsStrictlyLE b)
    (hP : ∀ i : ℤ, IsPerfectModule (R := R) (K.X i)) :
    IsPerfect (DerivedCategory.Q.obj K)
```

## Tag 066U, a lemma

[Tag 066U](https://stacks.math.columbia.edu/tag/066U) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_of_bounded_of_cohomology_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Basic.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Basic.lean#L405). References: SGA 6 I (4.15), “special case”.

> **Stacks 066U.** A bounded object of the derived category of modules whose cohomology modules
> are all perfect is itself perfect.

```lean
theorem isPerfect_of_bounded_of_cohomology_isPerfect
    {R : Type u} [CommRing R] (K : DerivedCategory (ModuleCat.{v} R))
    (hK : (∃ a : ℤ, K.IsGE a) ∧ ∃ b : ℤ, K.IsLE b)
    (hH : ∀ i : ℤ,
      IsPerfectModule (R := R)
        ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) :
    IsPerfect K
```

## Tag 066V, a lemma

[Tag 066V](https://stacks.math.columbia.edu/tag/066V) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_restrictScalars_of_isPerfectModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BaseChange.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/BaseChange.lean#L184).

> **Stacks 066V.** Let `f : A → B` be a homomorphism of commutative rings and assume that `B` is
> perfect as an `A`-module. Then every perfect complex of `B`-modules is perfect as a complex of
> `A`-modules.

```lean
theorem isPerfect_restrictScalars_of_isPerfectModule
    (hB : IsPerfectModule (R := A)
      ((ModuleCat.restrictScalars.{uB} f).obj (ModuleCat.of B B)))
    (K : CochainComplex (ModuleCat.{uB} B) ℤ)
    (hK : IsPerfect (DerivedCategory.Q.obj K)) :
    IsPerfect (DerivedCategory.Q.obj
      (((ModuleCat.restrictScalars.{uB} f).mapHomologicalComplex (ComplexShape.up ℤ)).obj K))
```

## Tag 066W, a lemma

[Tag 066W](https://stacks.math.columbia.edu/tag/066W) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_derivedExtensionScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BaseChange.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/BaseChange.lean#L261).

> **Stacks 066W.** Let `f : A → B` be a homomorphism of commutative rings and let `K` be a
> perfect object of `D(A)`. Then the derived base change `K ⊗_A^L B` is a perfect object of
> `D(B)`.

```lean
theorem isPerfect_derivedExtensionScalars (f : A →+* B)
    (K : DerivedCategory (ModuleCat.{max v uA uB} A)) (hK : IsPerfect K) :
    IsPerfect ((CochainComplex.DerivedExtensionScalars.totalDerivedExtensionScalars.{uA, uB, v}
      f).functor.obj K)
```

## Tag 066X, a lemma

[Tag 066X](https://stacks.math.columbia.edu/tag/066X) in the Stacks Project.

**`StacksDraft.Perfect.isPerfectModule_tensorProduct_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Module.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Module.lean#L270).

> **Stacks 066X.** Flat base change preserves perfect modules.

```lean
theorem isPerfectModule_tensorProduct_of_flat
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [Algebra A B]
    (M : Type w) [AddCommGroup M] [Module A M] [Module.Flat A B]
    (hM : IsPerfectModule (R := A) M) :
    IsPerfectModule (R := B) (B ⊗[A] M)
```

## Tag 0GM0, a lemma

[Tag 0GM0](https://stacks.math.columbia.edu/tag/0GM0) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Duality/TensorProductTorAmplitude.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Duality/TensorProductTorAmplitude.lean#L151). References: SGA 6 I (4.19), “D(R), R a ring”.

> **Stacks 0GM0.** The derived tensor product of two perfect objects of `D(A)` is perfect.

```lean
theorem isPerfect_derivedTensorProduct
    (K L : DerivedCategory (ModuleCat.{max u v} (ULift.{v} R)))
    (hK : IsPerfect K) (hL : IsPerfect L) :
    IsPerfect ((derivedHomData (R := R)).tensor.obj (K, L))
```

## Tag 066Y, a lemma

[Tag 066Y](https://stacks.math.columbia.edu/tag/066Y) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_of_localizationSpan`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Local.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Local.lean#L287).

> Let `R` be a commutative ring, let the elements `f i` generate the unit ideal, and let `K` be
> an object of the derived category of `R`-modules. If the derived localization `K ⊗_R R_{f i}` is
> perfect for every `i`, then `K` is perfect.

```lean
theorem isPerfect_of_localizationSpan {R : Type u} [CommRing R] {ι : Type*} [Finite ι]
    (f : ι → R) (hf : Ideal.span (Set.range f) = ⊤)
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : ∀ i, IsPerfect ((PseudoCoherence.localizationAwayFunctorAux.{u, v} (f i)).obj K)) :
    IsPerfect K
```

## Tag 068T, a lemma

[Tag 068T](https://stacks.math.columbia.edu/tag/068T) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_of_faithfullyFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Local.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Local.lean#L618).

> Let `R → S` be a faithfully flat map of commutative rings and let `K` be a complex of
> `R`-modules. If `K ⊗_R S` is perfect, then `K` is perfect.

```lean
theorem isPerfect_of_faithfullyFlat_baseChange
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) (hf : f.FaithfullyFlat)
    (K : CochainComplex (ModuleCat.{max u v w} R) ℤ)
    (hK : IsPerfect
      (DerivedCategory.Q.obj
        (((ModuleCat.extendScalars.{u, v, max u v w} f).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj K))) :
    IsPerfect (DerivedCategory.Q.obj K)
```

## Tag 066Z, a lemma

[Tag 066Z](https://stacks.math.columbia.edu/tag/066Z) in the Stacks Project.

**`StacksDraft.Perfect.isPerfectModule_iff_finite_and_isPerfect_iff_bounded_finiteCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Regular.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Regular.lean#L247).

> **Stacks 066Z.** Over a regular ring, perfect modules are precisely finite modules, and
> perfect derived objects are precisely the bounded objects with finite cohomology modules.

```lean
theorem isPerfectModule_iff_finite_and_isPerfect_iff_bounded_finiteCohomology
    {R : Type u} [CommRing R] [IsRegularRing R] :
    (∀ (M : Type (max u v)) [AddCommGroup M] [Module R M],
      IsPerfectModule (R := R) M ↔ Module.Finite R M) ∧
    (∀ K : DerivedCategory (ModuleCat.{max u v} R),
      IsPerfect K ↔
        ((∃ a : ℤ, K.IsGE a) ∧ (∃ b : ℤ, K.IsLE b) ∧
          ∀ i : ℤ,
            Module.Finite R
              ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K)))
```

## Tag 07VI, a lemma

[Tag 07VI](https://stacks.math.columbia.edu/tag/07VI) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_derivedDual_and_naturalIsos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Duality/TensorHom.lean, line 651](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Duality/TensorHom.lean#L651). References: SGA 6 I (7.7), “affine case”; SGA 6 I (7.3), “affine (ring) case”.

> **Stacks 07VI.** Let `A` be a ring and let `K` be a perfect object of `D(A)`. Then the derived
> dual `Kᵛ = RHom_A(K, A)` is perfect, the canonical morphism `K ⟶ (Kᵛ)ᵛ` is an isomorphism, the
> canonical comparison `L ⊗_A^L Kᵛ ⟶ RHom_A(K, L)` is an isomorphism functorially in `L`, and
> `H⁰(L ⊗_A^L Kᵛ) = Ext⁰_A(K, L)` functorially in `L`.

```lean
theorem isPerfect_derivedDual_and_naturalIsos
    (K : DerivedCategory (ModuleCat.{max u v} (ULift.{v} R))) (hK : IsPerfect K) :
    PerfectDerivedDuality K
```

## Tag 0H81, a remark

[Tag 0H81](https://stacks.math.columbia.edu/tag/0H81) in the Stacks Project.

**`StacksDraft.Perfect.hasFlatRepresentative_derivedDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Duality/TensorProductTorAmplitude.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Duality/TensorProductTorAmplitude.lean#L227). References: SGA 6 I (7.3), “finite Tor-dim stability”.

> **Stacks 0H81.** If a perfect complex has Tor amplitude in `[a, b]` -- that is, a flat
> representative supported in `[a, b]` -- then its derived dual has Tor amplitude in `[-b, -a]`.

```lean
theorem hasFlatRepresentative_derivedDual
    (K : DerivedCategory (ModuleCat.{max u v} (ULift.{v} A)))
    (hK : IsPerfect K) {a b : ℤ}
    (hKamp : HasFlatRepresentative K a b) :
    HasFlatRepresentative (derivedDual K) (-b) (-a)
```

## Tag 0BKB, a lemma

[Tag 0BKB](https://stacks.math.columbia.edu/tag/0BKB) in the Stacks Project.

**`StacksDraft.Perfect.isDerivedLimit_derivedHom_of_isHomotopyColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/SystemDuality.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/SystemDuality.lean#L443).

> If `K` is a homotopy colimit of a sequential system of perfect derived
> objects `Kₙ`, then `RHomₐ(K, E)` is a derived inverse limit of the inverse system
> `E ⊗ᴸ Kₙᵛ`.

```lean
theorem isDerivedLimit_derivedHom_of_isHomotopyColimit
    (Ksys : ℕ ⥤ DerivedCategory (ModuleCat.{max u v} A)) [HasCoproduct Ksys.obj]
    (hperfect : ∀ n : ℕ, IsPerfect (Ksys.obj n))
    (K E : DerivedCategory (ModuleCat.{max u v} A)) (hK : IsHomotopyColimit Ksys K)
    [HasProduct fun n : ℕ ↦ (dualTensorSystem A Ksys E).obj (Opposite.op n)] :
    IsDerivedLimit (dualTensorSystem A Ksys E)
      ((derivedHomAdjunctionOverRing A).hom.obj (Opposite.op K, E))
```

## Tag 0BC7, a lemma

[Tag 0BC7](https://stacks.math.columbia.edu/tag/0BC7) in the Stacks Project.

**`StacksDraft.Perfect.perfectComplexes_filteredColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/Colimit/HomColimit.lean, line 833](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/Colimit/HomColimit.lean#L833).

> **Stacks 0BC7.** Let `R : I ⥤ CommRingCat` be a filtered system of commutative rings whose
> colimit is computed on underlying sets, and let `c` be a colimit cocone. Writing `E f` for the
> canonical total derived extension of scalars `- ⊗ᴸ_A B` along `f : A →+* B` ([stacks 064H]), the
> following two statements hold.
>
> First, every perfect object `K` of the derived category of `c.pt`-modules descends to a finite
> stage: there are an index `i` and a perfect object `Kᵢ` over `R.obj i` with
> `K ≅ (E (c.ι.app i)).functor.obj Kᵢ`.
>
> Second, morphisms out of a perfect complex commute with the filtered colimit. Fix a stage `i₀` and
> objects `K₀`, `L₀` over `R.obj i₀` with `K₀` perfect. Then derived extension of scalars carries a
> composition isomorphism `comp` compatible with the scalar-extension tower on complexes, and the
> morphisms `(E (c.ι.app i₀)).functor.obj K₀ ⟶ (E (c.ι.app i₀)).functor.obj L₀` over the colimit ring
> form the filtered colimit, over the stages `j` above `i₀`, of the morphisms
> `(E (R.map j.hom)).functor.obj K₀ ⟶ (E (R.map j.hom)).functor.obj L₀` over those stages, with the
> transition maps and the maps to the colimit given by derived extension of scalars conjugated by
> `comp`.

```lean
public theorem perfectComplexes_filteredColimit
    {I : Type uI} [Category.{uI} I] [IsFiltered I]
    (R : I ⥤ CommRingCat.{uR}) [PreservesColimit R (forget CommRingCat.{uR})]
    (c : Cocone R) (hc : IsColimit c) :
    let E := fun {A B : Type uR} [CommRing A] [CommRing B] (f : A →+* B) ↦
      totalDerivedExtensionScalars.{uR, uR, uR} f
    let D := fun {i j : I} (f : i ⟶ j) ↦ E (R.map f).hom
    let Dlim := fun (i : I) ↦ E (c.ι.app i).hom
    (∀ (K : DerivedCategory (ModuleCat.{uR} c.pt)), IsPerfect K →
        ∃ (i : I) (Kᵢ : DerivedCategory (ModuleCat.{uR} (R.obj i))),
          IsPerfect Kᵢ ∧ Nonempty (K ≅ (Dlim i).functor.obj Kᵢ)) ∧
      (∀ (i₀ : I) (K₀ L₀ : DerivedCategory (ModuleCat.{uR} (R.obj i₀))),
        IsPerfect K₀ →
        ∃ (comp : ∀ {A B C : Type uR} [CommRing A] [CommRing B] [CommRing C]
            (f : A →+* B) (g : B →+* C),
            (E f).functor ⋙ (E g).functor ≅ (E (g.comp f)).functor),
          (∀ {A B C : Type uR} [CommRing A] [CommRing B] [CommRing C]
              (f : A →+* B) (g : B →+* C)
              (P : CochainComplex (ModuleCat.{uR} A) ℤ),
            (E g).functor.map ((E f).comparison.app P) ≫
                (E g).comparison.app
                  (((ModuleCat.extendScalars.{uR, uR, uR} f).mapHomologicalComplex
                    (ComplexShape.up ℤ)).obj P) ≫
                (extensionOfScalarsComplexComp.{uR} f g).inv.app P =
              (comp f g).hom.app (DerivedCategory.Q.obj P) ≫
                (E (g.comp f)).comparison.app P) ∧
        ∃ (H : Under i₀ ⥤ Type (uR + 1))
          (eH : ∀ j : Under i₀,
            H.obj j ≃ ((D j.hom).functor.obj K₀ ⟶ (D j.hom).functor.obj L₀))
          (s : Cocone H)
          (eTarget : s.pt ≃ ((Dlim i₀).functor.obj K₀ ⟶ (Dlim i₀).functor.obj L₀))
          (_hs : IsColimit s),
          (∀ {j k : Under i₀} (w : j ⟶ k) (x : H.obj j),
            let h : (R.map w.right).hom.comp (R.map j.hom).hom = (R.map k.hom).hom :=
              by
                ext x
                calc
                  _ = (R.map (j.hom ≫ w.right)).hom x :=
                    (congrArg (fun q : R.obj i₀ ⟶ R.obj k.right ↦ q.hom x)
                      (R.map_comp j.hom w.right)).symm
                  _ = _ := by rw [w.w]
            let stageComp := comp (R.map j.hom).hom (R.map w.right).hom ≪≫
              derivedExtensionScalarsCongr.{uR} E h
            eH k (H.map w x) =
              stageComp.inv.app K₀ ≫
                (D w.right).functor.map (eH j x) ≫
                stageComp.hom.app L₀) ∧
          (∀ (j : Under i₀)
              (g : (D j.hom).functor.obj K₀ ⟶ (D j.hom).functor.obj L₀),
            let h : (c.ι.app j.right).hom.comp (R.map j.hom).hom = (c.ι.app i₀).hom :=
              congrArg CommRingCat.Hom.hom (c.w j.hom)
            let limitComp := comp (R.map j.hom).hom (c.ι.app j.right).hom ≪≫
              derivedExtensionScalarsCongr.{uR} E h
            eTarget (s.ι.app j ((eH j).symm g)) =
              limitComp.inv.app K₀ ≫ (Dlim j.right).functor.map g ≫
                limitComp.hom.app L₀))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.76, Tag 0656](https://stacks.math.columbia.edu/tag/0656)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
