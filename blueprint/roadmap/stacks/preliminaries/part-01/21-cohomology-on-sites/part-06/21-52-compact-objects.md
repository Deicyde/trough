---
declaration: section
origin: cited
lean: Stacks.Cohomology.CompactObjects.exists_retract_finiteComplex_of_isCompactObject, Stacks.Cohomology.exists_retract_finiteComplex_extensionByZero_of_isCompactObject, Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective, Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective_of_hasIntersectionsIn, Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit, Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit_of_isWeaklyContractible, Stacks.Cohomology.QuasiCompactSite.hom_coproduct_bijective_and_isCompactObject_of_isPerfect_of_isQuasiCompactObject
statement: formalized
proof: formalized
---

# 21.52 Compact objects

Section 21.52 of the Stacks Project, [Tag 0948](https://stacks.math.columbia.edu/tag/0948). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 094B, a lemma

[Tag 094B](https://stacks.math.columbia.edu/tag/094B) in the Stacks Project.

**`Stacks.Cohomology.CompactObjects.exists_retract_finiteComplex_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/FromAGeneratingSet.lean, line 650](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/FromAGeneratingSet.lean#L650).

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

**`Stacks.Cohomology.exists_retract_finiteComplex_extensionByZero_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/CompactObjectsOnRingedSites.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/CompactObjectsOnRingedSites.lean#L207).

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

**`Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/ExtensionByZeroRelativeCompactness.lean, line 676](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/ExtensionByZeroRelativeCompactness.lean#L676).

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

**`Stacks.Cohomology.extensionByZero_unit_hom_coproduct_bijective_of_hasIntersectionsIn`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactnessFromCoverings/CompactnessFromFiniteCoverings.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactnessFromCoverings/CompactnessFromFiniteCoverings.lean#L370).

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

**`Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroIsCompact.lean, line 768](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroIsCompact.lean#L768).

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

**`Stacks.Cohomology.CompactExtensionByZero.isCompactObject_singleFunctor_extensionByZeroUnit_of_isWeaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroOverAWeaklyContractibleObject.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/CompactObjects/ExtensionByZeroOverAWeaklyContractibleObject.lean#L174).

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

**`Stacks.Cohomology.QuasiCompactSite.hom_coproduct_bijective_and_isCompactObject_of_isPerfect_of_isQuasiCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnAQuasiCompactSite.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnAQuasiCompactSite.lean#L302). The attribute's comment: “both clauses, under hypotheses (1)-(3) of the tag; the 08JJ reduction, the Tor amplitude of the dual and the 0739 sums are all proved, none assumed”.

> **Stacks 09JC.** Let `(C, O)` be a ringed site such that
>
> 1. `C` has a quasi-compact final object `X₀`,
> 2. every quasi-compact object of `C` has a cofinal system of coverings which are finite and
>    consist of quasi-compact objects,
> 3. for a finite covering `{U_i → U}` with `U` and the `U_i` quasi-compact the fibre products
>    `U_i ×_U U_j` are quasi-compact.
>
> Let `K` be a perfect object of `D(O)`. Then
>
> * **(a)** `K` is a compact object of `D⁺(O)` in the following sense: if `M : I → D(O)` is a
>   family whose coproduct `M = ⨁ M_i` is bounded below, then the canonical map
>   `⨁ Hom(K, M_i) → Hom(K, M)` is bijective;
> * **(b)** if `(C, O)` has finite cohomological dimension, that is if there is a `d` with
>   `H^p(X₀, F) = 0` for `p > d` and every `O`-module `F`, then `K` is a compact object of `D(O)`.
>
> Quasi-compactness is that of Stacks 090H,
> `CategoryTheory.GrothendieckTopology.IsQuasiCompactObject`. Hypothesis (1) is `hterm` and
> `hqc`. Hypothesis (2) is `hcofinal`: every covering sieve of a quasi-compact object is refined by
> a covering by finitely many quasi-compact objects. Hypothesis (3) is `hfibre`; since a
> Grothendieck topology, unlike a site in the sense of Stacks 00VH, does not provide the fibre
> products of a covering, (3) asserts that `U_i ×_U U_j` exists, as a limiting
> pullback cone, and is quasi-compact.
>
> The source's proof calls on Stacks 0739 and 0G22 with the quasi-compact objects as `B`; those
> need every iterated fibre product `U_{i₀} ×_U ⋯ ×_U U_{iₙ}` of such a covering to be quasi-compact,
> which follows from (3) by base change, `Stacks.Cohomology.hasIntersectionsIn_of_exists_pullback`.
> The statement is then `hom_coproduct_bijective_and_isCompactObject_of_isPerfect`.

```lean
theorem hom_coproduct_bijective_and_isCompactObject_of_isPerfect_of_isQuasiCompactObject
    (X₀ : X.C) (hterm : IsTerminal X₀) (hqc : X.J.IsQuasiCompactObject X₀)
    (hcofinal : ∀ U : X.C, X.J.IsQuasiCompactObject U → ∀ S ∈ X.J U,
      ∃ F : PreZeroHypercover.{u} U, F.sieve₀ ∈ X.J U ∧ F.sieve₀ ≤ S ∧ Finite F.I₀ ∧
        ∀ i, X.J.IsQuasiCompactObject (F.X i))
    (hfibre : ∀ (U : X.C) (F : PreZeroHypercover.{u} U), F.sieve₀ ∈ X.J U → Finite F.I₀ →
      X.J.IsQuasiCompactObject U → (∀ i, X.J.IsQuasiCompactObject (F.X i)) →
      ∀ i j, ∃ t : PullbackCone (F.f i) (F.f j), Nonempty (IsLimit t) ∧
        X.J.IsQuasiCompactObject t.pt)
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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
