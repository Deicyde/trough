---
declaration: section
origin: cited
lean: IsStrictlyPerfect, mappingCone_isStrictlyPerfect, Stacks.StrictlyPerfect.Modules.isStrictlyPerfect_tensor, Stacks.SheafOfModules.Tensor.isStrictlyPerfect_tensorComplex, AlgebraicGeometry.RingedToposHom.isStrictlyPerfect_pullbackModules, Stacks.Sheaves.StrictlyPerfectPullback.pullbackModules_preservesZeroMorphisms, Stacks.Sheaves.StrictlyPerfectPullback.isStrictlyPerfect_pullbackModules, AlgebraicGeometry.RingedSite.exists_coveringSieve_lift
statement: formalized
proof: formalized
---

# 21.44 Strictly perfect complexes

Section 21.44 of the Stacks Project, [Tag 08FK](https://stacks.math.columbia.edu/tag/08FK). 10 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08FL, a definition

[Tag 08FL](https://stacks.math.columbia.edu/tag/08FL) in the Stacks Project.

Declarations registered for the tag:

- [`IsStrictlyPerfect`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/ConeOfAMorphism.lean#L191), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/StrictlyPerfectComplexes.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/StrictlyPerfectComplexes.lean#L41) (StacksFrontier): “a complex of `O`-modules is strictly perfect”.

## Tag 08FM, a lemma

[Tag 08FM](https://stacks.math.columbia.edu/tag/08FM) in the Stacks Project.

**`mappingCone_isStrictlyPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/ConeOfAMorphism.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/ConeOfAMorphism.lean#L230).

> **Statement 1 (Stacks Tag 08FM).**
> Let `(C, O)` be a ringed site, and let `f : A ⟶ B` be a morphism of complexes of
> `O`-modules. If `A` and `B` are both strictly perfect (Definition 2), then the cone
> `C(f) = CochainComplex.mappingCone f` (Definition 4) is strictly perfect.
>
> Proof sketch (Tag 08FM, "immediate from the definitions"):
> * Boundedness. By `CochainComplex.mappingCone.isZero_X_iff`,
>   `IsZero ((mappingCone f).X i) ↔ IsZero (A.X (i+1)) ∧ IsZero (B.X i)`, so
>   `{i | ¬ IsZero ((mappingCone f).X i)} ⊆ {i | ¬ IsZero (A.X (i+1))} ∪ {i | ¬ IsZero (B.X i)}`.
>   The second set is `hB.bounded`; the first is the preimage of `hA.bounded` under
>   `i ↦ i+1`, hence finite. A finite union of finite sets is finite.
> * Term condition. Fix `i`. We have `(mappingCone f).X i ≅ A.X (i+1) ⊞ B.X i` via
>   `HomologicalComplex.homotopyCofiber.XIsoBiprod f i (i+1) rfl` (`mappingCone f` is
>   definitionally `homotopyCofiber f`, and for `CochainComplex … ℤ` the relation `c.Rel i j`
>   is `i+1 = j`). By Helper 2, `A.X (i+1) ⊞ B.X i` is a direct summand of a finite free
>   module (since `A.X (i+1)` and `B.X i` are, by `hA.termDirectSummand`,
>   `hB.termDirectSummand`); by Helper 1 (transport along that iso) so is
>   `(mappingCone f).X i`.

```lean
theorem mappingCone_isStrictlyPerfect
    {A B : CochainComplex (SheafOfModules.{m} R) ℤ} (f : A ⟶ B)
    [HomologicalComplex.HasHomotopyCofiber f]
    (hA : IsStrictlyPerfect R A) (hB : IsStrictlyPerfect R B) :
    IsStrictlyPerfect R (CochainComplex.mappingCone f)
```

## Tag 09J8, a lemma

[Tag 09J8](https://stacks.math.columbia.edu/tag/09J8) in the Stacks Project.

**`Stacks.StrictlyPerfect.Modules.isStrictlyPerfect_tensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/DirectSummandsOfFiniteFree.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/DirectSummandsOfFiniteFree.lean#L218).

> If `E` and `F` are strictly perfect complexes of `R`-modules, then so is their tensor product
> `E ⊗ F`, the total complex of the tensor product double complex.

```lean
theorem isStrictlyPerfect_tensor
    (E F : CochainComplex (ModuleCat R) ℤ)
    (hE : IsStrictlyPerfect E) (hF : IsStrictlyPerfect F) :
    IsStrictlyPerfect (E ⊗ F)
```

**`Stacks.SheafOfModules.Tensor.isStrictlyPerfect_tensorComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/TensorOfStrictlyPerfectComplexes.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/TensorOfStrictlyPerfectComplexes.lean#L399).

> **Stacks 09J8.** The total tensor complex `Tot(K ⊗_O L)` of two strictly perfect complexes
> of `O`-modules on a ringed site is strictly perfect.
>
> Each degree of `Tot(K ⊗_O L)` is the coproduct of the `K^t ⊗_O L^r` with `t + r` that degree.
> Such a summand vanishes unless both `K^t` and `L^r` are nonzero, which happens for finitely
> many pairs only, so the degree vanishes outside the sum of the two ranges of nonvanishing; and
> each surviving summand is a direct summand of a finite free `O`-module because both of its
> factors are.

```lean
theorem isStrictlyPerfect_tensorComplex
    (K L : CochainComplex (SheafOfModules.{w} (ringSheaf R)) ℤ)
    (hK : IsStrictlyPerfect (ringSheaf R) K) (hL : IsStrictlyPerfect (ringSheaf R) L) :
    IsStrictlyPerfect (ringSheaf R) (((tensorComplex R).obj K).obj L)
```

## Tag 08H3, a lemma

[Tag 08H3](https://stacks.math.columbia.edu/tag/08H3) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.isStrictlyPerfect_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/PullbackAlongAMorphismOfRingedTopoi.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/PullbackAlongAMorphismOfRingedTopoi.lean#L53).

> Let `f : (C, O_C) → (D, O_D)` be a morphism of ringed topoi. If `E` is a strictly perfect
> complex of `O_D`-modules, then `f^*E`, the degreewise pullback, is a strictly perfect complex of
> `O_C`-modules.

```lean
theorem isStrictlyPerfect_pullbackModules (f : RingedToposHom X Y)
    {E : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ}
    (hE : IsStrictlyPerfect (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) E) :
    IsStrictlyPerfect (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
      (((f.toModulesHom.pullbackModules).mapHomologicalComplex (ComplexShape.up ℤ)).obj E)
```

**`Stacks.Sheaves.StrictlyPerfectPullback.pullbackModules_preservesZeroMorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/ToposPullback.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/ToposPullback.lean#L133). The attribute's comment: “additivity of pullback”.

> **Stacks 08H3, the additivity clause.** Pullback of sheaves of modules along a morphism
> of ringed topoi preserves zero morphisms, being a left adjoint. This is what lets the functor
> be applied degreewise to a complex.

```lean
theorem pullbackModules_preservesZeroMorphisms :
    (f.pullbackModules).PreservesZeroMorphisms
```

**`Stacks.Sheaves.StrictlyPerfectPullback.isStrictlyPerfect_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/ToposPullback.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/ToposPullback.lean#L142). The attribute's comment: “strict perfectness of the pullback complex”.

> **Stacks 08H3, the strict-perfectness clause.** The degreewise pullback of a strictly
> perfect complex of `O_Y`-modules along a morphism of ringed topoi is a strictly perfect complex
> of `O_X`-modules.

```lean
theorem isStrictlyPerfect_pullbackModules
    (E : CochainComplex (SheafOfModules.{0} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) ℤ)
    (hE : IsStrictlyPerfect (Stacks.SheafOfModules.Tensor.ringSheaf Y.O) E) :
    letI := pullbackModules_preservesZeroMorphisms f
    IsStrictlyPerfect (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
      (((f.pullbackModules).mapHomologicalComplex (ComplexShape.up ℤ)).obj E)
```

## Tag 08FN, a lemma

[Tag 08FN](https://stacks.math.columbia.edu/tag/08FN) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalLiftingThroughEpimorphisms.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalLiftingThroughEpimorphisms.lean#L277).

> **Stacks 08FN.** Let `(C, O)` be a ringed site, `U` an object of `C`, and let
> `p : G ⟶ F` be an epimorphism of `O|_U`-modules. A map `e : E ⟶ F` whose source is a direct
> summand of a finite free `O|_U`-module lifts through `p` locally on `U`: there is a covering
> sieve `S` of `U` such that for every `f : V ⟶ U` in `S` the restriction of `e` to `C/V`
> factors through the restriction of `p`.
>
> The lift is produced one coordinate at a time. Writing `E` as a retract of `O|_U^{⊕n}` by
> `j : E ⟶ O|_U^{⊕n}` and `r : O|_U^{⊕n} ⟶ E` with `j ≫ r = 𝟙`, the composite `q = r ≫ e` is
> determined by `n` global sections of `F` over `U`. Each of them lifts through `p` on a
> covering sieve, since `p` is locally surjective; the intersection of those `n` sieves is still
> covering, and over it the chosen lifts assemble, by the universal property of the free module,
> into a map `O|_U^{⊕n}|_V ⟶ G|_V` over `p`. Precomposing with `j|_V` gives the lift of `e`.

```lean
theorem exists_coveringSieve_lift (X : RingedSite.{u, t, 0}) (U : X.C)
    [HasWeakSheafify (X.J.over U) AddCommGrpCat.{0}]
    [(X.J.over U).WEqualsLocallyBijective AddCommGrpCat.{0}]
    (E F G : SheafOfModules.{0} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
    (e : E ⟶ F) (p : G ⟶ F) [Epi p]
    (hE : IsDirectSummandOfFiniteFree ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U) E) :
    ∃ S : Sieve U, (S ∈ X.J U) ∧
      (∀ {V : X.C} (f : V ⟶ U), S f →
        ∃ l : E.over (Over.mk f) ⟶ G.over (Over.mk f),
          l ≫ p.over (Over.mk f) = e.over (Over.mk f))
```

## Tag 08FP, a lemma

[Tag 08FP](https://stacks.math.columbia.edu/tag/08FP) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_homotopy_zero_of_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalNullHomotopy.lean, line 643](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalNullHomotopy.lean#L643). The attribute's comment: “part (1)”. References: SGA 6 I (4.1).

> **Stacks 08FP (1).** A map from a strictly perfect complex of `O|_U`-modules to an acyclic
> complex is null-homotopic after restriction along every arrow of a covering sieve of `U`.

```lean
theorem exists_coveringSieve_homotopy_zero_of_acyclic
    (hE : IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U) E)
    (hF : F.Acyclic) :
    ∃ S : Sieve U, S ∈ X.J U ∧
      ∀ {V : X.C} (f : V ⟶ U), S f →
        Nonempty (Homotopy
          (((SheafOfModules.overFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)
            (Over.mk f)).mapHomologicalComplex
            (ComplexShape.up ℤ)).map α) 0)
```

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_homotopy_zero_of_isZero_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalNullHomotopy.lean, line 658](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalNullHomotopy.lean#L658). The attribute's comment: “part (2)”. References: SGA 6 I (4.1).

> **Stacks 08FP (2).** A map from a strictly perfect complex of `O|_U`-modules supported in
> degrees `≥ a` is null-homotopic after restriction along every arrow of a covering sieve of `U`,
> provided the target has vanishing cohomology in those degrees.

```lean
theorem exists_coveringSieve_homotopy_zero_of_isZero_homology (a : ℤ)
    (hE : IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U) E)
    (hE₀ : ∀ i : ℤ, i < a → IsZero (E.X i))
    (hF : ∀ i : ℤ, a ≤ i → IsZero (F.homology i)) :
    ∃ S : Sieve U, S ∈ X.J U ∧
      ∀ {V : X.C} (f : V ⟶ U), S f →
        Nonempty (Homotopy
          (((SheafOfModules.overFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)
            (Over.mk f)).mapHomologicalComplex
            (ComplexShape.up ℤ)).map α) 0)
```

## Tag 08FQ, a lemma

[Tag 08FQ](https://stacks.math.columbia.edu/tag/08FQ) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_lift_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalLiftingThroughCohomologyIsomorphisms.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalLiftingThroughCohomologyIsomorphisms.lean#L199). References: SGA 6 I (4.2).

> **Stacks 08FQ.** Let `(C, O)` be a ringed site and `U` an object of `C`. Given a solid
> diagram of complexes of `O|_U`-modules
> ```
> E --α--> F
>      ↗
>     G
> ```
> with `E` strictly perfect, `Eʲ = 0` for `j < a`, `Hʲ(f)` an isomorphism for `j > a` and an
> epimorphism for `j = a`, there is a covering sieve of `U` such that over each of its arrows a
> dotted arrow exists making the diagram commute up to homotopy.

```lean
theorem exists_coveringSieve_lift_homotopy (α : E ⟶ F) (f : G ⟶ F) (a : ℤ)
    (hE : IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U) E)
    (hEa : ∀ j : ℤ, j < a → IsZero (E.X j))
    (hf_gt : ∀ j : ℤ, a < j → IsIso (HomologicalComplex.homologyMap f j))
    (hf_a : Epi (HomologicalComplex.homologyMap f a)) :
    ∃ S : Sieve U, S ∈ X.J U ∧
      ∀ {V : X.C} (g : V ⟶ U), S g →
        ∃ β : ((SheafOfModules.overFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)
              (Over.mk g)).mapHomologicalComplex (ComplexShape.up ℤ)).obj E ⟶
          ((SheafOfModules.overFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)
              (Over.mk g)).mapHomologicalComplex (ComplexShape.up ℤ)).obj G,
          Nonempty (Homotopy
            (β ≫ ((SheafOfModules.overFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)
              (Over.mk g)).mapHomologicalComplex (ComplexShape.up ℤ)).map f)
            (((SheafOfModules.overFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)
              (Over.mk g)).mapHomologicalComplex (ComplexShape.up ℤ)).map α))
```

## Tag 08FR, a lemma

[Tag 08FR](https://stacks.math.columbia.edu/tag/08FR) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_homotopy_zero_of_derived_zero_overMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalComplexMapOfARetraction.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalComplexMapOfARetraction.lean#L117). The attribute's comment: “local\_null\_homotopy, along an arrow of the site”.

> **Stacks 08FR (2), with the restriction to the slice over an arrow `V ⟶ U` of the covering
> sieve expressed by `SheafOfModules.overMap`** rather than by restriction to an iterated slice.
>
> This is the same statement as
> `AlgebraicGeometry.RingedSite.exists_coveringSieve_homotopy_zero_of_derived_zero_general`, in
> the presentation of the restriction that Stacks 08FR (1) and pseudo-coherence use. The general
> form of 08FR (2) is the one read here, the module sections living in the ring universe `w`.

```lean
theorem exists_coveringSieve_homotopy_zero_of_derived_zero_overMap
    {E F : CochainComplex
      (SheafOfModules.{w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)) ℤ}
    (hE : IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U) E) (α : E ⟶ F)
    (hα : DerivedCategory.Q.map α = 0) :
    ∃ S : Sieve U, S ∈ X.J U ∧ ∀ ⦃V : X.C⦄ (g : V ⟶ U), S g →
      Nonempty (Homotopy (((SheafOfModules.overMap.{w}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O) g).mapHomologicalComplex
          (ComplexShape.up ℤ)).map α) 0)
```

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_homotopy_zero_of_derived_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalNullHomotopyOfDerivedZero.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalNullHomotopyOfDerivedZero.lean#L75). The attribute's comment: “local\_null\_homotopy”. References: SGA 6 I (4.1), “special case”.

> Let `(C, O)` be a ringed site and `U` an object of `C`. Let
> `α : E ⟶ F` be a map of complexes of `O|_U`-modules with `E` strictly perfect, and suppose the
> image of `α` in `D(O|_U)` is zero. Then there is a covering sieve of `U` such that the
> restriction of `α` along each of its arrows is homotopic to zero.

```lean
theorem exists_coveringSieve_homotopy_zero_of_derived_zero
    {E F : CochainComplex
      (SheafOfModules.{0} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)) ℤ}
    (hE : IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U) E) (α : E ⟶ F)
    (hα : DerivedCategory.Q.map α = 0) :
    ∃ S : Sieve U, S ∈ X.J U ∧
      ∀ {V : X.C} (f : V ⟶ U), S f →
        Nonempty (Homotopy
          (((SheafOfModules.overFunctor ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)
            (Over.mk f)).mapHomologicalComplex (ComplexShape.up ℤ)).map α) 0)
```

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_complexMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalRepresentationOfADerivedMap.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/LocalRepresentationOfADerivedMap.lean#L250). The attribute's comment: “local\_representation”.

> **Stacks 08FR (1).** Let `(C, O)` be a ringed site and `U` an object of `C`. Let `E`, `F` be
> complexes of `O|_U`-modules with `E` strictly perfect. Any morphism `α : E ⟶ F` of `D(O|_U)` is,
> after restriction along the arrows of a covering sieve of `U`, the image under the localisation
> functor of a morphism of complexes.

```lean
theorem exists_coveringSieve_complexMap
    {E F : CochainComplex
      (SheafOfModules.{w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)) ℤ}
    (hE : IsStrictlyPerfect ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U) E)
    (α : DerivedCategory.Q.obj E ⟶ DerivedCategory.Q.obj F) :
    ∃ S : Sieve U, S ∈ X.J U ∧
      ∀ {V : X.C} (f : V ⟶ U), S f →
        let H := SheafOfModules.overMap (Stacks.SheafOfModules.Tensor.ringSheaf X.O) f
        ∃ (hsheaf : HasSheafify (X.J.over V) AddCommGrpCat.{w})
          (hlocal : (X.J.over V).WEqualsLocallyBijective AddCommGrpCat.{w}),
          letI := hsheaf
          letI := hlocal
          letI : HasDerivedCategory
              (SheafOfModules.{w} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over V)) :=
            HasDerivedCategory.standard _
          ∃ (hadd : H.Additive)
            (hlim : PreservesFiniteLimits H)
            (hcolim : PreservesFiniteColimits H),
            letI := hadd
            letI := hlim
            letI := hcolim
            ∃ β : (H.mapHomologicalComplex (ComplexShape.up ℤ)).obj E ⟶
                (H.mapHomologicalComplex (ComplexShape.up ℤ)).obj F,
              H.mapDerivedCategory.map α ≫ H.mapDerivedCategoryFactors.hom.app F =
                H.mapDerivedCategoryFactors.hom.app E ≫ DerivedCategory.Q.map β
```

## Tag 08JH, a lemma

[Tag 08JH](https://stacks.math.columbia.edu/tag/08JH) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.strictlyPerfectHomComparison_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/HomComplexComparison.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/HomComplexComparison.lean#L159). The attribute's comment: “representation by the finite direct-sum Hom complex”.

> **Stacks 08JH**, the representation statement. For `E` strictly perfect — bounded, with
> every term a direct summand of a finite free `O`-module — the derived internal Hom
> `RSheafHom(E, F)` is represented by the ordinary internal Hom complex `SheafHom(E, F)` of
> Stacks 0A8Z, the comparison being the canonical one.
>
> By `strictlyPerfectHomComparison_isIso_iff` this is the quasi-isomorphy of the map of internal
> Hom complexes induced by the K-injective augmentation of the target, which is
> `homMap_quasiIso_of_isFiniteFreeSummand`.
>
> The degreewise direct-sum description of that complex, the other half of Stacks 08JH, is
> `strictlyPerfectHomDegreeIso`.

```lean
theorem strictlyPerfectHomComparison_isIso
    (hbdd : {i : ℤ | ¬ IsZero (E.X i)}.Finite)
    (hterm : ∀ i : ℤ, IsFiniteFreeSummand X (E.X i)) :
    IsIso (strictlyPerfectHomComparison X D E F)
```

**`AlgebraicGeometry.RingedSite.strictlyPerfectHomDegreeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/HomComplexOfAStrictlyPerfectComplex.lean, line 350](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/HomComplexOfAStrictlyPerfectComplex.lean#L350). The attribute's comment: “finite direct-sum terms and Hom differential”.

> **Stacks 08JH**, degreewise statement. For `E` bounded, the `n`-th term of the internal Hom
> complex `SheafHom(E, F)` of Stacks 0A8Z is the direct sum, over `q : ℤ`, of the internal Hom
> sheaves `SheafHom(E^{-q}, F^{n-q})`.
>
> By `homDegreeIsLimit` the term is the *product* of those sheaves, with no hypothesis on `E`.
> Boundedness makes `E^{-q}` vanish outside a finite set of `q`, hence each summand vanish there
> by `internalHomSheaf_isZero_of_isZero`, and `productCoproductIsoOfFiniteSupport` then
> identifies the product with the coproduct.
>
> The source lemma assumes `E` strictly perfect; boundedness is the `bounded` field of that
> condition and the only part used, so this is the source statement generalized. See the
> implementation notes for why the strict-perfectness predicate cannot be named at these
> universes.
>
> The differential needs no separate description: that it is the standard Hom-complex
> differential is part of the data of `SheafHomComplex`, whose `sectionsIso` is an isomorphism
> of complexes onto `CochainComplex.HomComplex` on every slice site.

```lean
def strictlyPerfectHomDegreeIso
    (E F : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (hE : {i : ℤ | ¬ IsZero (E.X i)}.Finite) (n : ℤ) :
    ((sheafHomComplex X E F).obj.X n) ≅
      ∐ (fun q : ℤ => internalHomSheaf X (E.X (-q)) (F.X (n - q)))
```

## Tag 08JI, a lemma

[Tag 08JI](https://stacks.math.columbia.edu/tag/08JI) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.boundedAboveHomRepresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomOfBoundedAboveSummands.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DerivedHomOfBoundedAboveSummands.lean#L145). The attribute's comment: “derived internal Hom represented by the Hom complex, with finite direct-sum terms”.

> **Stacks 08JI**, the whole statement. Let `E` be a complex of `O`-modules vanishing above
> `b` all of whose terms are direct summands of finite free `O`-modules, and let `F` be a complex
> of `O`-modules vanishing below `a`. Then the derived internal Hom `RSheafHom(E, F)` is
> represented by the internal Hom complex `H = SheafHom(E, F)` of Stacks 0A8Z — the comparison
> being the canonical `strictlyPerfectHomComparison` — and that complex has
> `H^n = ⨁_{n = p + q} SheafHom(E^{-q}, F^p)` in every degree.
>
> The two components are exactly the two assertions of the source, and neither is restated here:
> the first is `strictlyPerfectHomComparison_isIso_of_boundedAbove`, the library's Stacks 08I5, at
> exactly the hypotheses of Stacks 08JI; the second is `boundedAboveHomDegreeIso`. The differential
> needs no separate component; see the implementation notes.

```lean
def boundedAboveHomRepresentation (D : DerivedInternalHom.{u, d} X) (a b : ℤ)
    (hF : ∀ i : ℤ, i < a → IsZero (F.X i)) (hE : ∀ i : ℤ, b < i → IsZero (E.X i))
    (hterm : ∀ i : ℤ, IsFiniteFreeSummand X (E.X i)) :
    Σ' _ : IsIso (strictlyPerfectHomComparison X D E F),
      ∀ n : ℤ, (sheafHomComplex X E F).obj.X n ≅
        ∐ (fun q : ℤ => internalHomSheaf X (E.X (-q)) (F.X (n - q)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.44, Tag 08FK](https://stacks.math.columbia.edu/tag/08FK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
