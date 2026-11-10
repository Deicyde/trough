---
declaration: section
origin: cited
lean: Stacks.Cohomology.CompactObjects.exists_retract_finiteComplex_of_isCompactObject, Stacks.Cohomology.exists_retract_finiteComplex_extensionByZero_of_isCompactObject, Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective, Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective_of_hasIntersectionsIn, Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit, Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit_of_isWeaklyContractible, Stacks.Cohomology.hom_coproduct_bijective_of_isPerfect, Stacks.Cohomology.isCompactObject_of_isPerfect
statement: formalized
proof: formalized
---

# 21.52 Compact objects

Section 21.52 of the Stacks Project, [Tag 0948](https://stacks.math.columbia.edu/tag/0948). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 094B, a lemma

[Tag 094B](https://stacks.math.columbia.edu/tag/094B) in the Stacks Project.

**`Stacks.Cohomology.CompactObjects.exists_retract_finiteComplex_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/FromAGeneratingSet.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/FromAGeneratingSet.lean#L650).

> A compact derived object is a summand of a finite complex of finite sums
> of compact generators of the abelian category.

```lean
public theorem exists_retract_finiteComplex_of_isCompactObject
    {A : Type u} [Category.{v} A] [Abelian A]
    [IsGrothendieckAbelian.{w} A] [HasDerivedCategory.{z} A]
    (S : Set A)
    (hS : ∀ X : A, ∃ (I : Type w) (E : I → A),
      (∀ i, E i ∈ S) ∧ ∃ f : (∐ E) ⟶ X, Epi f)
    (hcompact : ∀ E ∈ S, IsCompactObject.{w} E)
    (K : DerivedCategory A) [IsCompactObject.{w} K] :
    ∃ (L : CochainComplex A ℤ) (a b : ℤ),
      L.IsStrictlyGE a ∧ L.IsStrictlyLE b ∧
      (∀ i : ℤ, ∃ (n : ℕ) (E : Fin n → A),
        (∀ j, E j ∈ S) ∧ Nonempty (L.X i ≅ ∐ E)) ∧
      Nonempty (Retract K (DerivedCategory.Q.obj L))
```

## Tag 094C, a lemma

[Tag 094C](https://stacks.math.columbia.edu/tag/094C) in the Stacks Project.

**`Stacks.Cohomology.exists_retract_finiteComplex_extensionByZero_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/CompactObjectsOnRingedSites.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/CompactObjectsOnRingedSites.lean#L207).

> **Stacks 094C.** On a ringed site every object of which is covered by quasi-compact objects,
> a compact object of the derived category of sheaves of modules is a direct summand of a bounded
> complex whose terms are finite direct sums of the modules `j_{U!} O_U` for quasi-compact `U`.

```lean
public theorem exists_retract_finiteComplex_extensionByZero_of_isCompactObject
    (hqc : ∀ U : X.C, ∃ 𝒰 : PreZeroHypercover.{max u v} U,
      𝒰.sieve₀ ∈ X.J U ∧ ∀ i, X.J.IsQuasiCompactObject (𝒰.X i))
    (K : DerivedCategory
      (SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [IsCompactObject.{max u v w m} K] :
    ∃ (L : CochainComplex
        (SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
      (a b : ℤ),
      L.IsStrictlyGE a ∧ L.IsStrictlyLE b ∧
      (∀ i : ℤ, ∃ (n : ℕ) (U : Fin n → X.C),
        (∀ j, X.J.IsQuasiCompactObject (U j)) ∧
        Nonempty (L.X i ≅ ∐ fun j : Fin n ↦
          extensionByZeroUnit.{v, u, w, m} X.J
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (U j))) ∧
      Nonempty (Retract K (DerivedCategory.Q.obj L))
```

## Tag 0G21, a lemma

[Tag 0G21](https://stacks.math.columbia.edu/tag/0G21) in the Stacks Project.

**`Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/ExtensionByZeroRelativeCompactness.lean, line 676](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/ExtensionByZeroRelativeCompactness.lean#L676).

> Extension by zero of the unit module on `U` is compact with respect to
> bounded-below direct sums, provided cohomology on `U` commutes with direct sums.

```lean
public theorem extensionByZero_unit_hom_coproduct_bijective
    (X : RingedSite.{u, v, r}) (U : X.C)
    (hsums :
      letI : EnoughInjectives (SheafOfModules.{max u v r m}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :=
        enoughInjectives_of_ringedSite.{u, v, r, m} X
      letI : (SheafOfModules.evaluation.{max u v r m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
          (op U)).Additive :=
        evaluation_additive_of_ringedSite.{u, v, r, m} X U
      ∀ (p : ℕ) (I : Type w),
      PreservesColimitsOfShape (Discrete I)
        ((SheafOfModules.evaluation.{max u v r m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
            (op U)).rightDerived p))
    (I : Type w) [DecidableEq I]
    (M : I → DerivedCategory (SheafOfModules.{max u v r m}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) [HasCoproduct M]
    (hM : (DerivedCategory.TStructure.t
      (C := SheafOfModules.{max u v r m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))).plus
          (∐ M)) :
    let K : DerivedCategory (SheafOfModules.{max u v r m}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :=
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{max u v r m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (extensionByZeroUnit.{v, u, r, m} X.J (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U))
    Function.Bijective
      (DirectSum.toAddMonoid (β := fun i : I => K ⟶ M i) (γ := K ⟶ ∐ M)
        fun i => Preadditive.rightComp K (Limits.Sigma.ι M i))
```

## Tag 0G22, a lemma

[Tag 0G22](https://stacks.math.columbia.edu/tag/0G22) in the Stacks Project.

**`Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective_of_hasIntersectionsIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactnessFromCoverings/CompactnessFromFiniteCoverings.lean, line 370](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactnessFromCoverings/CompactnessFromFiniteCoverings.lean#L370).

> On a ringed site with a cofinal collection of finite coverings closed under finite
> intersections, extension by zero of the unit module over `U` is compact with respect to
> bounded-below coproducts.

```lean
public theorem extensionByZero_unit_hom_coproduct_bijective_of_hasIntersectionsIn
    (X : RingedSite.{u, u, u})
    (B : Set X.C) (Cov : ∀ U : X.C, Set (PreZeroHypercover.{c} U))
    (hCov : ∀ (U : X.C) (E : PreZeroHypercover.{c} U), Cov U E → E.sieve₀ ∈ X.J U)
    (hfinite : ∀ (U : X.C) (E : PreZeroHypercover.{c} U), Cov U E →
      HasIntersectionsIn B E)
    (hcofinal : ∀ (U : X.C), B U → ∀ S ∈ X.J U,
      ∃ E : PreZeroHypercover.{c} U, Cov U E ∧ E.sieve₀ ≤ S)
    (U : X.C) (hU : B U)
    (I : Type i) [DecidableEq I]
    (M : I → DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct M]
    (hM : (DerivedCategory.TStructure.t
      (C := SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))).plus (∐ M)) :
    let K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :=
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        (extensionByZeroUnit.{u, u, u, u} X.J (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U))
    Function.Bijective
      (DirectSum.toAddMonoid (β := fun j : I => K ⟶ M j) (γ := K ⟶ ∐ M)
        fun j => Preadditive.rightComp K (Limits.Sigma.ι M j))
```

## Tag 094D, a lemma

[Tag 094D](https://stacks.math.columbia.edu/tag/094D) in the Stacks Project.

**`Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroIsCompact.lean, line 768](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroIsCompact.lean#L768).

> Let `(C, O)` be a ringed site and `U` an object of `C`. If cohomology over
> `U` has finite cohomological dimension and `H^p(U, -)` commutes with direct sums for every `p`,
> then `j_{U!} O_U`, placed in degree zero, is a compact object of the unbounded derived category
> of `O`-modules. Compactness is tested against families indexed by types in `Type w`, the
> universe of the hypothesis on direct sums.

```lean
theorem isCompactObject_singleFunctor_extensionByZeroUnit
    (hcd : ∃ d : ℤ, ∀ (p : ℕ) (G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)),
      d < (p : ℤ) →
      IsZero (((SheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        (op U)).rightDerived p).obj G))
    (hsums : ∀ (p : ℕ) (I : Type w), PreservesColimitsOfShape (Discrete I)
      ((SheafOfModules.evaluation (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        (op U)).rightDerived p)) :
    IsCompactObject.{w}
      ((DerivedCategory.singleFunctor (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        ((SheafOfModules.pullback.{u} (F := Over.forget U)
          (𝟙 ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))).obj
          (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))))
```

## Tag 094E, a lemma

[Tag 094E](https://stacks.math.columbia.edu/tag/094E) in the Stacks Project.

**`Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit_of_isWeaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroOverAWeaklyContractibleObject.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroOverAWeaklyContractibleObject.lean#L174).

> **Stacks 094E.** Let `(C, O)` be a ringed site and let `U` be an object of `C` which is
> quasi-compact and weakly contractible. Then `j_{U!} O_U`, placed in degree zero, is a compact
> object of the unbounded derived category of `O`-modules.
>
> The two hypotheses of Stacks 094D are discharged: weak contractibility makes `Γ(U, -)` exact, so
> cohomology over `U` vanishes in positive degrees and in particular has finite cohomological
> dimension, and together with quasi-compactness it makes every `R ᵖ Γ(U, -)` commute with direct
> sums.

```lean
theorem isCompactObject_singleFunctor_extensionByZeroUnit_of_isWeaklyContractible
    (hU : X.J.IsQuasiCompactObject U) (hU' : X.J.IsWeaklyContractible U) :
    IsCompactObject.{u}
      ((DerivedCategory.singleFunctor
          (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
        ((SheafOfModules.pullback.{u} (F := Over.forget U)
          (𝟙 ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))).obj
          (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))))
```

## Tag 09JC, a lemma

[Tag 09JC](https://stacks.math.columbia.edu/tag/09JC) in the Stacks Project.

**`Stacks.Cohomology.hom_coproduct_bijective_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/PerfectObjectsAreCompact.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/PerfectObjectsAreCompact.lean#L317). The attribute's comment: “(a) bounded-below compactness; assumes the 08JJ reduction, not formalized”.

> **Stacks 09JC (a).** Let `(C, O)` be a ringed site, let `B` be a collection of objects of `C`
> with a cofinal system of finite coverings whose fibre products again lie in `B` — hypotheses (1),
> (2) and (3) of the tag, with `B` the quasi-compact objects — and let `X₀` be a member of `B`, the
> quasi-compact final object of the tag. Let `K` be a perfect object of `D(O)`. If `M : I → D(O)`
> has a bounded-below coproduct, then morphisms from `K` into that coproduct are finite sums,
> `Hom(K, ⨁ M_i) = ⨁ Hom(K, M_i)`: the object `K` is compact relative to `D⁺(O)`.
>
> The hypothesis `hreduce` is the reduction the source performs, and is what perfectness of `K` is
> used for: by Stacks 08JJ the dual `K^∨` satisfies
> `Hom_{D(O)}(K, N) = H⁰(X₀, K^∨ ⊗^L_O N)` naturally in `N`, the functor `T = K^∨ ⊗^L_O -`
> commutes with direct sums, and `T` keeps a bounded-below coproduct bounded below. None of those
> three facts is available in this library — see "What this file assumes" in the module
> documentation — so the reduction is assumed; granted it, this is Stacks 0G22 at `U = X₀`.

```lean
theorem hom_coproduct_bijective_of_isPerfect
    (B : Set X.C) (Cov : ∀ U : X.C, Set (PreZeroHypercover.{c} U))
    (hCov : ∀ (U : X.C) (F : PreZeroHypercover.{c} U), Cov U F → F.sieve₀ ∈ X.J U)
    (hfinite : ∀ (U : X.C) (F : PreZeroHypercover.{c} U), Cov U F → HasIntersectionsIn B F)
    (hcofinal : ∀ (U : X.C), B U → ∀ S ∈ X.J U,
      ∃ F : PreZeroHypercover.{c} U, Cov U F ∧ F.sieve₀ ≤ S)
    (X₀ : X.C) (hX₀ : B X₀)
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K)
    {I : Type i} [DecidableEq I]
    (M : I → DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    [HasCoproduct M]
    (hreduce : X.IsPerfect K →
      ∃ T : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ⥤
          DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)),
        ∃ _ : PreservesColimit (Discrete.functor M) T,
          (DerivedCategory.TStructure.t
            (C := SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))).plus
              (T.obj (∐ M)) ∧
          ∃ e : ∀ N : DerivedCategory
              (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)), (K ⟶ N) ≃+
              ((DerivedCategory.singleFunctor
                  (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
                (extensionByZeroUnit.{u, u, u, u} X.J
                  (Stacks.SheafOfModules.Tensor.ringSheaf X.O) X₀) ⟶ T.obj N),
            ∀ {N N' : DerivedCategory
                (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
              (f : K ⟶ N) (g : N ⟶ N'), e N' (f ≫ g) = e N f ≫ T.map g) :
    Function.Bijective
      (DirectSum.toAddMonoid fun j => Preadditive.rightComp K (Limits.Sigma.ι M j))
```

**`Stacks.Cohomology.isCompactObject_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/PerfectObjectsAreCompact.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/PerfectObjectsAreCompact.lean#L363). The attribute's comment: “(b) unbounded compactness; assumes the 08JJ reduction, 0739 sums; not formalized”.

> **Stacks 09JC (b).** Let `(C, O)` be a ringed site, let `X₀` be an object of `C` — the
> quasi-compact final object of the tag — and let `K` be a perfect object of `D(O)`. If cohomology
> over `X₀` has finite cohomological dimension, that is `(C, O)` has finite cohomological
> dimension, and if the functors `F ↦ H^p(X₀, F)` commute with direct sums, then `K` is a compact
> object of `D(O)`.
>
> The hypothesis `hreduce` is the reduction the source performs, and is what perfectness of `K` is
> used for: by Stacks 08JJ the dual `K^∨` satisfies
> `Hom_{D(O)}(K, N) = H⁰(X₀, K^∨ ⊗^L_O N)` naturally in `N`, and `T = K^∨ ⊗^L_O -` commutes with
> direct sums. Neither fact is available in this library — see "What this file assumes" in the
> module documentation — so the reduction is assumed; granted it, this is Stacks 094D at `U = X₀`.
> The hypothesis `hsums` is what hypotheses (2) and (3) of the tag supply through Stacks 0739.

```lean
theorem isCompactObject_of_isPerfect (X₀ : X.C)
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K)
    (hcd : ∃ d : ℤ, ∀ (p : ℕ)
      (G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)), d < (p : ℤ) →
        IsZero (((SheafOfModules.evaluation.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
          (op X₀)).rightDerived p).obj G))
    (hsums : ∀ (p : ℕ) (I : Type w), PreservesColimitsOfShape (Discrete I)
      ((SheafOfModules.evaluation.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        (op X₀)).rightDerived p))
    (hreduce : X.IsPerfect K →
      ∃ T : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ⥤
          DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)),
        ∃ _ : ∀ I : Type w, PreservesColimitsOfShape (Discrete I) T,
          ∃ e : ∀ N : DerivedCategory
              (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)), (K ⟶ N) ≃+
              ((DerivedCategory.singleFunctor
                  (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) 0).obj
                ((SheafOfModules.pullback.{u} (F := Over.forget X₀)
                  (𝟙 ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over X₀))).obj
                    (SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over X₀))) ⟶
                T.obj N),
            ∀ {N N' : DerivedCategory
                (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))}
              (f : K ⟶ N) (g : N ⟶ N'), e N' (f ≫ g) = e N f ≫ T.map g) :
    IsCompactObject.{w} K
```

**`AlgebraicGeometry.RingedSite.isCompactObject_of_isPerfect_of_isTerminal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectDualReduction.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectDualReduction.lean#L239). The attribute's comment: “(b) unbounded compactness of a perfect object, with the 08JJ reduction DISCHARGED rather than assumed; the 0739 commutation of the cohomology functors with direct sums is still a hypothesis here, and is discharged from hypotheses (2) and (3) of the tag in Stacks.Cohomology.QuasiCompactSite.hom\_coproduct\_bijective\_and\_isCompactObject\_of\_isPerfect, which states both clauses”.

> **Stacks 09JC (b).** Let `(C, O)` be a ringed site with a final object `X₀` and let `K` be a
> perfect object of `D(O)`. If `(C, O)` has finite cohomological dimension, that is
> `H^p(X₀, F) = 0` for every `O`-module `F` and every `p` beyond a fixed bound, and if the
> functors `F ↦ H^p(X₀, F)` commute with direct sums, then `K` is a compact object of `D(O)`.
>
> Unlike `Stacks.Cohomology.isCompactObject_of_isPerfect` this carries no hypothesis standing in
> for the reduction of Stacks 08JJ: the functor is `- ⊗^L_O K^∨` for the canonical derived tensor
> product of Stacks 06YU, it commutes with direct sums by
> `preservesColimitsOfShape_derivedTensorFlip`, and the natural bijection is
> `derivedDualHomEquivOfIsoStructureSheaf` at the identification
> `derivedExtensionByZeroUnitIsoStructureSheaf` of `j_{X₀!}O_{X₀}[0]` with `O[0]`. Perfectness of
> `K` is used exactly where the source uses it, to produce that bijection. What is still a
> hypothesis, as in the conditional form, is the commutation `hsums` of the higher cohomology
> functors with direct sums, which the source supplies from Stacks 0739.

```lean
theorem isCompactObject_of_isPerfect_of_isTerminal (X₀ : X.C) (hX₀ : IsTerminal X₀)
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : X.IsPerfect K)
    (hcd : ∃ d : ℤ, ∀ (p : ℕ)
      (G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)), d < (p : ℤ) →
      IsZero (((SheafOfModules.evaluation.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        (op X₀)).rightDerived p).obj G))
    (hsums : ∀ (p : ℕ) (I : Type u), PreservesColimitsOfShape (Discrete I)
      ((SheafOfModules.evaluation.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
        (op X₀)).rightDerived p)) :
    IsCompactObject.{u} K
```

**`Stacks.Cohomology.QuasiCompactSite.hom_coproduct_bijective_and_isCompactObject_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnAQuasiCompactSite.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnAQuasiCompactSite.lean#L227).

> **Stacks 09JC.** Let `(C, O)` be a ringed site and assume `C` has the three properties of the
> tag: a quasi-compact final object `X₀`, a cofinal system of finite coverings by quasi-compact
> objects for every quasi-compact object, and quasi-compact fibre products inside such a covering.
> Let `K` be a perfect object of `D(O)`. Then
>
> * **(a)** `K` is a compact object of `D⁺(O)` in the sense of the tag: if `M : I → D(O)` is a
>   family whose coproduct `⨁ M_i` is bounded below, then the canonical map
>   `⨁ Hom(K, M_i) → Hom(K, ⨁ M_i)` is bijective; and
> * **(b)** if `(C, O)` has finite cohomological dimension, that is if there is a `d` with
>   `H^p(X₀, F) = 0` for `p > d` and every `O`-module `F`, then `K` is a compact object of `D(O)`.
>
> Hypothesis (1) of the tag is `hterm`, `hqc` and `hX₀`; hypotheses (2) and (3) are the covering
> data `B`, `Cov`, `hCov`, `hcofinal` and `hfinite`, `Stacks.Cohomology.HasIntersectionsIn`
> carrying the finiteness clause of (2) together with the whole of (3). See "How the hypotheses of
> the tag are read" in the module documentation.
>
> Both clauses rest on the source's reduction to `j_{X₀!}O_{X₀}`, which is
> `AlgebraicGeometry.RingedSite.derivedDualHomEquivOfIsoStructureSheaf` together with
> `AlgebraicGeometry.RingedSite.preservesColimitsOfShape_derivedTensorFlip`. Clause (a) then needs
> the global Tor amplitude of `K^∨`, which is
> `hasFiniteTorDimension_derivedDual_of_isPerfect` from (1); clause (b) needs the commutation of
> the cohomology functors over `X₀` with direct sums, which is
> `preservesCoproducts_rightDerived_evaluation_of_covers` from (2) and (3).

```lean
theorem hom_coproduct_bijective_and_isCompactObject_of_isPerfect
    (B : Set X.C) (Cov : ∀ U : X.C, Set (PreZeroHypercover.{c} U))
    (hCov : ∀ (U : X.C) (F : PreZeroHypercover.{c} U), Cov U F → F.sieve₀ ∈ X.J U)
    (hfinite : ∀ (U : X.C) (F : PreZeroHypercover.{c} U), Cov U F →
      Stacks.Cohomology.HasIntersectionsIn B F)
    (hcofinal : ∀ (U : X.C), B U → ∀ S ∈ X.J U,
      ∃ F : PreZeroHypercover.{c} U, Cov U F ∧ F.sieve₀ ≤ S)
    (X₀ : X.C) (hterm : IsTerminal X₀) (hqc : X.J.IsQuasiCompactObject X₀) (hX₀ : B X₀)
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) (hK : X.IsPerfect K) :
    (∀ {I : Type u} [DecidableEq I]
        (M : I → DerivedCategory (_root_.SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O))) [HasCoproduct M],
        DerivedCategoryB.IsBoundedBelow (∐ M) →
        Function.Bijective
          (DirectSum.toAddMonoid fun j => Preadditive.rightComp K (Limits.Sigma.ι M j))) ∧
      ((∃ d : ℤ, ∀ (p : ℕ) (G : _root_.SheafOfModules.{u}
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O)), d < (p : ℤ) →
          IsZero (((_root_.SheafOfModules.evaluation.{u}
            (Stacks.SheafOfModules.Tensor.ringSheaf X.O) (op X₀)).rightDerived p).obj G)) →
        IsCompactObject.{u} K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.52, Tag 0948](https://stacks.math.columbia.edu/tag/0948)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
