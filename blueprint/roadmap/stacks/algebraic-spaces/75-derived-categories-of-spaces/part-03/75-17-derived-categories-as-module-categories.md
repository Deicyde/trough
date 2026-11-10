---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj, AlgebraicGeometry.Space.derivedCategoryB_tensorWithComplexDerived_obj_smallEtale, AlgebraicGeometry.Space.exists_window_subsingleton_hom_of_isPerfect, AlgebraicGeometry.Space.finite_setOf_not_subsingleton_hom_shift_of_isPerfect, AlgebraicGeometry.Space.exists_differentialGradedAlgebra_equivalence, AlgebraicGeometry.Space.exists_differentialGradedAlgebra_equivalence_of_supported, AlgebraicGeometry.Space.exists_equivalence_derivedTensor_complexHomBimodule
statement: formalized
proof: formalized
---

# 75.17 Derived categories as module categories

Section 75.17 of the Stacks Project, [Tag 09M9](https://stacks.math.columbia.edu/tag/09M9). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09M9, the section

[Tag 09M9](https://stacks.math.columbia.edu/tag/09M9) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentImage.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentImage.lean#L322). The attribute's comment: “RESTRICTED: 75.17.1 only”.

> **Stacks 09MA**, and with it the content of section **09M9** that this file delivers. *"Let
> `S` be a scheme, `X` an algebraic space over `S`. Let `K` be a complex of `O_X`-modules whose
> cohomology sheaves are quasi-coherent. Let `(E, d) = Hom(K, K)` be the endomorphism differential
> graded algebra. Then the functor `- ⊗_E^𝐋 K : D(E, d) ⟶ D(O_X)` of Tag 09LX has image contained
> in `D_QCoh(O_X)`."*
>
> The dévissage is the source's: a differential graded `E`-module with property (P) is the
> homotopy colimit of the stages of its filtration, each stage carries a finite filtration whose
> graded pieces are direct sums of shifts of `E`, and `E[k] ⊗_E K` is `K[k]`. Tag 0FQE packages
> exactly that reduction, so what has to be checked is that lying in `D_QCoh(O)` holds at every
> shift of the free rank-one module — which is the staged computation
> `AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj_regular` together
> with the stability of `D_QCoh(O)` under the translation — is inherited by direct sums, and is
> inherited by the third vertex of a distinguished triangle from the other two, the last because
> `- ⊗_E^𝐋 K` is exact and `D_QCoh(O)` is a triangulated subcategory of `D(O)`.
>
> Three assumptions are upstream inputs, not pieces of the conclusion: that quasi-coherence is a
> weak Serre class and that `hqcsum`, a direct sum of quasi-coherent `O`-modules is quasi-coherent
> (the two clauses of Tag 03M1, the first as a typeclass assumption so that instance search
> supplies it where this repository has it); and `htensorSum`, that tensoring with `K` carries a
> direct sum of differential graded `E`-modules to a direct sum in `D(O)` (the differential graded
> half of which is Tag 09LV, formalized as
> `AlgebraicGeometry.RingedSite.tensorWithComplexDG_preservesCoproducts`). The hypothesis
> `hK` is the source's own, that the cohomology sheaves of `K` be quasi-coherent, stated for the
> complex `liftComplex X K` that the functor tensors with.
>
> Exactness of `- ⊗_E^𝐋 K`, which the two-out-of-three step needs, is **not assumed**. As a
> hypothesis `hexact`, Tag 09LW read against the pretriangulated structure that is not the one in
> force here, it would be unsatisfiable and this statement vacuous. What discharges it is
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerived_signTwist_isTriangulated`, the
> unconditional exactness of `- ⊗_E^𝐋 K` composed with the sign-twisted identity of `D(O)`: that
> composite has the same action on objects and on morphisms, so its image of a distinguished
> triangle has the same three vertices, which is all this step uses of it.

```lean
theorem derivedCategoryB_tensorWithComplexDerived_obj
    [ObjectProperty.IsWeakSerreClass (tensorModOQuasicoherent.{u, v, w, t, s} X)]
    (hqcsum : ∀ {ι : Type (max u v w t s)} (Mf : ι → TensorModO.{u, v, w, t, s} X)
      (c : Cofan Mf), IsColimit c →
      (∀ i, tensorModOQuasicoherent.{u, v, w, t, s} X (Mf i)) →
      tensorModOQuasicoherent.{u, v, w, t, s} X c.pt)
    (htensorSum : ∀ {ι : Type (max u v w t s)} [DecidableEq ι]
      (N : ι → DifferentialGradedModule.{0, max u v w t s, max u v w t s}
        (Rep.{u, v, w, t, s, 0} X ℤ K).algebra),
      IsColimit ((toHomotopyCategory (Rep.{u, v, w, t, s, 0} X ℤ K).algebra ⋙
        tensorWithComplexToDerivedCategory.{u, v, w, t, s, 0} X ℤ K).mapCocone
          (Cofan.mk (General.directSumObj N) (General.directSumInj N))))
    (hK : tensorModOQuasicoherentDerived.{u, v, w, t, s} X
      (DerivedCategory.Q.obj (liftComplex.{u, v, w, t, s} X K)))
    (M : DifferentialGradedModule.derivedCategory.{0, max u v w t s, max u v w t s}
      (Rep.{u, v, w, t, s, 0} X ℤ K).algebra) :
    tensorModOQuasicoherentDerived.{u, v, w, t, s} X
      ((tensorWithComplexDerived.{u, v, w, t, s, 0} X ℤ K).obj M)
```

## Tag 09MA, a lemma

[Tag 09MA](https://stacks.math.columbia.edu/tag/09MA) in the Stacks Project.

**`AlgebraicGeometry.Space.derivedCategoryB_tensorWithComplexDerived_obj_smallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TensorWithComplexQuasicoherentSmallEtale.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TensorWithComplexQuasicoherentSmallEtale.lean#L98).

> **Stacks 09MA.**  Let `S` be a scheme, let `F` be an algebraic space over `S`, let `K` be a
> complex of `𝒪_F`-modules whose cohomology sheaves are quasi-coherent and let `(E, d) = Hom(K, K)`
> be the endomorphism differential graded algebra.  Then the functor
> `- ⊗_E^𝐋 K : D(E, d) ⟶ D(𝒪_F)` of Stacks 09LX has image contained in `D_QCoh(𝒪_F)`.
>
> The hypothesis `hK` is the source's, that the cohomology sheaves of `K` be quasi-coherent, stated
> for the complex `liftComplex F K` that the functor tensors with.  Nothing else is assumed: the
> weak Serre class that the dévissage
> `AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj_of_hqcsum` uses comes
> from `AlgebraicGeometry.Space.quasicoherentSheaves_isWeakSerreClass` together with
> `AlgebraicGeometry.Space.isClosedUnderKernels`,
> `AlgebraicGeometry.Space.isClosedUnderCokernels` and
> `AlgebraicGeometry.Space.isClosedUnderExtensions` at the module universe in which the tensor
> products are formed, and its `hqcsum` is
> `AlgebraicGeometry.Space.isClosedUnderDirectSumsQuasicoherent`; the exactness of the functor and
> its preservation of direct sums are instances of this development.

```lean
public theorem derivedCategoryB_tensorWithComplexDerived_obj_smallEtale
    (K : CochainComplex (ModO.{u + 1, u, u, t} (smallEtaleRingedSite B S hS F hF)) ℤ)
    (hK : tensorModOQuasicoherentDerived.{u + 1, u, u, t, s}
      (smallEtaleRingedSite B S hS F hF)
      (DerivedCategory.Q.obj (liftComplex.{u + 1, u, u, t, s}
        (smallEtaleRingedSite B S hS F hF) K)))
    (M : DifferentialGradedModule.derivedCategory.{0, max (u + 1) t s, max (u + 1) t s}
      (RingedSite.Rep.{u + 1, u, u, t, s, 0} (smallEtaleRingedSite B S hS F hF) ℤ K).algebra) :
    tensorModOQuasicoherentDerived.{u + 1, u, u, t, s} (smallEtaleRingedSite B S hS F hF)
      ((tensorWithComplexDerived.{u + 1, u, u, t, s, 0}
        (smallEtaleRingedSite B S hS F hF) ℤ K).obj M)
```

**`AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentImage.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexQuasicoherentImage.lean#L322). The attribute's comment: “RESTRICTED: assumes 03M1, 09LV”.

> **Stacks 09MA**, and with it the content of section **09M9** that this file delivers. *"Let
> `S` be a scheme, `X` an algebraic space over `S`. Let `K` be a complex of `O_X`-modules whose
> cohomology sheaves are quasi-coherent. Let `(E, d) = Hom(K, K)` be the endomorphism differential
> graded algebra. Then the functor `- ⊗_E^𝐋 K : D(E, d) ⟶ D(O_X)` of Tag 09LX has image contained
> in `D_QCoh(O_X)`."*
>
> The dévissage is the source's: a differential graded `E`-module with property (P) is the
> homotopy colimit of the stages of its filtration, each stage carries a finite filtration whose
> graded pieces are direct sums of shifts of `E`, and `E[k] ⊗_E K` is `K[k]`. Tag 0FQE packages
> exactly that reduction, so what has to be checked is that lying in `D_QCoh(O)` holds at every
> shift of the free rank-one module — which is the staged computation
> `AlgebraicGeometry.RingedSite.derivedCategoryB_tensorWithComplexDerived_obj_regular` together
> with the stability of `D_QCoh(O)` under the translation — is inherited by direct sums, and is
> inherited by the third vertex of a distinguished triangle from the other two, the last because
> `- ⊗_E^𝐋 K` is exact and `D_QCoh(O)` is a triangulated subcategory of `D(O)`.
>
> Three assumptions are upstream inputs, not pieces of the conclusion: that quasi-coherence is a
> weak Serre class and that `hqcsum`, a direct sum of quasi-coherent `O`-modules is quasi-coherent
> (the two clauses of Tag 03M1, the first as a typeclass assumption so that instance search
> supplies it where this repository has it); and `htensorSum`, that tensoring with `K` carries a
> direct sum of differential graded `E`-modules to a direct sum in `D(O)` (the differential graded
> half of which is Tag 09LV, formalized as
> `AlgebraicGeometry.RingedSite.tensorWithComplexDG_preservesCoproducts`). The hypothesis
> `hK` is the source's own, that the cohomology sheaves of `K` be quasi-coherent, stated for the
> complex `liftComplex X K` that the functor tensors with.
>
> Exactness of `- ⊗_E^𝐋 K`, which the two-out-of-three step needs, is **not assumed**. As a
> hypothesis `hexact`, Tag 09LW read against the pretriangulated structure that is not the one in
> force here, it would be unsatisfiable and this statement vacuous. What discharges it is
> `AlgebraicGeometry.RingedSite.tensorWithComplexDerived_signTwist_isTriangulated`, the
> unconditional exactness of `- ⊗_E^𝐋 K` composed with the sign-twisted identity of `D(O)`: that
> composite has the same action on objects and on morphisms, so its image of a distinguished
> triangle has the same three vertices, which is all this step uses of it.

```lean
theorem derivedCategoryB_tensorWithComplexDerived_obj
    [ObjectProperty.IsWeakSerreClass (tensorModOQuasicoherent.{u, v, w, t, s} X)]
    (hqcsum : ∀ {ι : Type (max u v w t s)} (Mf : ι → TensorModO.{u, v, w, t, s} X)
      (c : Cofan Mf), IsColimit c →
      (∀ i, tensorModOQuasicoherent.{u, v, w, t, s} X (Mf i)) →
      tensorModOQuasicoherent.{u, v, w, t, s} X c.pt)
    (htensorSum : ∀ {ι : Type (max u v w t s)} [DecidableEq ι]
      (N : ι → DifferentialGradedModule.{0, max u v w t s, max u v w t s}
        (Rep.{u, v, w, t, s, 0} X ℤ K).algebra),
      IsColimit ((toHomotopyCategory (Rep.{u, v, w, t, s, 0} X ℤ K).algebra ⋙
        tensorWithComplexToDerivedCategory.{u, v, w, t, s, 0} X ℤ K).mapCocone
          (Cofan.mk (General.directSumObj N) (General.directSumInj N))))
    (hK : tensorModOQuasicoherentDerived.{u, v, w, t, s} X
      (DerivedCategory.Q.obj (liftComplex.{u, v, w, t, s} X K)))
    (M : DifferentialGradedModule.derivedCategory.{0, max u v w t s, max u v w t s}
      (Rep.{u, v, w, t, s, 0} X ℤ K).algebra) :
    tensorModOQuasicoherentDerived.{u, v, w, t, s} X
      ((tensorWithComplexDerived.{u, v, w, t, s, 0} X ℤ K).obj M)
```

## Tag 09MB, a lemma

[Tag 09MB](https://stacks.math.columbia.edu/tag/09MB) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_window_subsingleton_hom_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectHomVanishingWindow.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectHomVanishingWindow.lean#L95). The attribute's comment: “part (1)”.

> **Stacks 09MB, part (1).**  Let `S` be a scheme, let `X` be a quasi-compact and
> quasi-separated algebraic space over `S` and let `K` be a perfect object of `D(𝒪_X)`.  Then there
> are integers `a ≤ b` such that `Hom_{D(𝒪_X)}(K, L) = 0` for every `L ∈ D_QCoh(𝒪_X)` with
> `Hⁱ(L) = 0` for `i ∈ [a, b]`.
>
> The model of the derived category is arbitrary.  The window is the one produced at the standard
> model by the induction `AlgebraicGeometry.Space.hasHomWindow_of_isPerfect_of_affine`, whose affine
> case is `AlgebraicGeometry.Space.hasHomWindow_of_isAffineSpace`, carried across the comparison of
> the two models.

```lean
theorem exists_window_subsingleton_hom_of_isPerfect
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    [hD : HasDerivedCategory.{w} (Modules.{u, u} B S hS X hX)]
    (K : DerivedCategory (Modules.{u, u} B S hS X hX))
    (hK : (smallEtaleRingedSite B S hS X hX).IsPerfect K) :
    ∃ a b : ℤ, a ≤ b ∧ ∀ L : DerivedCategory (Modules.{u, u} B S hS X hX),
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X hX) i).obj
        L).IsQuasicoherentOnSite) →
      (∀ i : ℤ, a ≤ i → i ≤ b →
        IsZero ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X hX) i).obj L)) →
      Subsingleton (K ⟶ L)
```

**`AlgebraicGeometry.Space.finite_setOf_not_subsingleton_hom_shift_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectHomVanishingWindow.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/PerfectHomVanishingWindow.lean#L135). The attribute's comment: “part (2)”.

> **Stacks 09MB, part (2).**  Let `S` be a scheme, let `X` be a quasi-compact and
> quasi-separated algebraic space over `S`, let `K` be a perfect object of `D(𝒪_X)` and let `L` be a
> bounded object of `D_QCoh(𝒪_X)`.  Then `Extⁿ_{D(𝒪_X)}(K, L) = Hom_{D(𝒪_X)}(K, L⟦n⟧)` is zero for
> all but finitely many `n`.
>
> Outside a bounded range of `n` the shift `L⟦n⟧` has no cohomology at all in the window of part
> (1), because `L` is bounded.

```lean
theorem finite_setOf_not_subsingleton_hom_shift_of_isPerfect
    (hqc : IsQuasiCompactSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    [HasDerivedCategory.{w} (Modules.{u, u} B S hS X hX)]
    (K : DerivedCategory (Modules.{u, u} B S hS X hX))
    (hK : (smallEtaleRingedSite B S hS X hX).IsPerfect K)
    (L : DerivedCategory (Modules.{u, u} B S hS X hX))
    (hLqc : ∀ i : ℤ, ((DerivedCategory.homologyFunctor (Modules.{u, u} B S hS X hX) i).obj
      L).IsQuasicoherentOnSite)
    (c d : ℤ) (hLGE : L.IsGE c) (hLLE : L.IsLE d) :
    {n : ℤ | ¬ Subsingleton (K ⟶ L⟦n⟧)}.Finite
```

## Tag 09MC, a theorem

[Tag 09MC](https://stacks.math.columbia.edu/tag/09MC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_differentialGradedAlgebra_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedModuleCategory.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedModuleCategory.lean#L266).

> **Stacks 09MC.** *Let `X` be a quasi-compact and quasi-separated algebraic space over `S`.
> Then there exists a differential graded algebra `(E, d)` with only a finite number of nonzero
> cohomology groups `H^i(E)` such that `D_QCoh(𝒪_X)` is equivalent to `D(E, d)`.*

```lean
theorem exists_differentialGradedAlgebra_equivalence (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1) :
    ∃ E : DifferentialGradedAlgebra.{0, u} ℤ, {i : ℤ | Nontrivial (E.Cohomology i)}.Finite ∧
      Nonempty (QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2 ≌
        DifferentialGradedModule.derivedCategory.{0, u, u} E)
```

## Tag 0DK8, a remark

[Tag 0DK8](https://stacks.math.columbia.edu/tag/0DK8) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_differentialGradedAlgebra_equivalence_of_supported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedModuleCategorySupported.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DerivedModuleCategorySupported.lean#L199).

> **Stacks 0DK8.** *Let `S` be a scheme, let `X` be a quasi-compact and quasi-separated
> algebraic space over `S` and let `T ⊆ |X|` be a closed subset such that `|X| ∖ T` is
> quasi-compact. Then there exists a differential graded algebra `(E, d)` with only a finite number
> of nonzero cohomology groups `H^i(E)` such that `D_{QCoh,T}(𝒪_X)` is equivalent to `D(E, d)`.*
>
> This is the analogue of Stacks 09MC for `D_{QCoh,T}(𝒪_X)`, the full subcategory
> `(AlgebraicGeometry.Space.quasicoherentDerivedSupportedOn X T).FullSubcategory` of `D_QCoh(𝒪_X)`
> of the objects whose cohomology sheaves are supported on `T`; for `T = |X|` it is Stacks 09MC.
> `E` is the endomorphism differential graded algebra of a K-injective complex representing a
> perfect generator of `D_{QCoh,T}(𝒪_X)` (Stacks 0AEC), formed on the equi-universe model of the
> small étale ringed site of `X`, so that its carrier and `D(E, d)` live in the universe of `X`.

```lean
theorem exists_differentialGradedAlgebra_equivalence_of_supported
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (hT : IsClosed T) (hTc : IsCompact Tᶜ) :
    ∃ E : DifferentialGradedAlgebra.{0, u} ℤ, {i : ℤ | Nontrivial (E.Cohomology i)}.Finite ∧
      Nonempty ((quasicoherentDerivedSupportedOn X T).FullSubcategory ≌
        DifferentialGradedModule.derivedCategory.{0, u, u} E)
```

## Tag 0DK9, a remark

[Tag 0DK9](https://stacks.math.columbia.edu/tag/0DK9) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_equivalence_derivedTensor_complexHomBimodule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DifferentialGradedAlgebraUniqueness.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/DifferentialGradedAlgebraUniqueness.lean#L196).

> **Stacks 0DK9.** *Let `X` be a quasi-compact and quasi-separated algebraic space over a ring
> `R`, and let `K` and `L` be K-injective complexes of `𝒪_X`-modules corresponding to perfect
> generators of `D_QCoh(𝒪_X)`, with `A = Hom_{Comp^dg(𝒪_X)}(K, K)` and
> `B = Hom_{Comp^dg(𝒪_X)}(L, L)`. Set `Ω = Hom_{Comp^dg(𝒪_X)}(K, L)` and
> `Ω' = Hom_{Comp^dg(𝒪_X)}(L, K)`. Then `Ω` is a differential graded `B^opp ⊗_R A`-module and `Ω'`
> a differential graded `A^opp ⊗_R B`-module, and the equivalence
> `D(A, d) ⥤ D_QCoh(𝒪_X) ⥤ D(B, d)` is given by `- ⊗_A^𝐋 Ω'`, and its quasi-inverse by
> `- ⊗_B^𝐋 Ω`.*
>
> The bimodules are `AlgebraicGeometry.RingedSite.complexHomBimodule`: `Ω' = Hom(L, K)` is a
> `DifferentialGraded.Bimodule A B` (left `A`-action by postcomposition, right `B`-action by
> precomposition) and `Ω = Hom(K, L)` a `DifferentialGraded.Bimodule B A`. The equivalences
> `D(A, d) ≌ D_QCoh(𝒪_X)` and `D(B, d) ≌ D_QCoh(𝒪_X)` are those of the proof of Stacks 09MC,
> `AlgebraicGeometry.Space.dgaQuasicoherentEquivalence`. The conclusion is an equivalence
> `D(A, d) ≌ D(B, d)` whose functor is `- ⊗_A^𝐋 Ω'` and whose inverse is `- ⊗_B^𝐋 Ω`, isomorphic
> to the composite `D(A, d) ⥤ D_QCoh(𝒪_X) ⥤ D(B, d)` and to its quasi-inverse: the situation of
> Stacks 09ST.
>
> `X` is over `R` through the ring map `ψ : R ⟶ Γ(X, 𝒪_X)`; `K` and `L` are complexes on the
> equi-universe model of the small étale site of `X`, corresponding through
> `AlgebraicGeometry.Space.modelEquivalence` to perfect generators `P` and `Q` of `D_QCoh(𝒪_X)`.

```lean
theorem exists_equivalence_derivedTensor_complexHomBimodule
    (hqc : IsQuasiCompactSpace B S hS X.1)
    (hqs : IsAbsolutelyQuasiSeparated B S hS B.contains_terminal X.1)
    (K L : CochainComplex (RingedSite.ModO.{u, u, u, u} (modelSite X)) ℤ)
    [(RingedSite.liftComplex.{u, u, u, u, u} (modelSite X) K).IsKInjective]
    [(RingedSite.liftComplex.{u, u, u, u, u} (modelSite X) L).IsKInjective]
    (P Q : DerivedCategory (Modules.{u, u} B S hS X.1 X.2))
    (hP : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect P)
    (hQ : (smallEtaleRingedSite B S hS X.1 X.2).IsPerfect Q)
    (hgenP : ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      IsZero E.obj ↔ ∀ n : ℤ, Subsingleton (P⟦n⟧ ⟶ E.obj))
    (hgenQ : ∀ E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2,
      IsZero E.obj ↔ ∀ n : ℤ, Subsingleton (Q⟦n⟧ ⟶ E.obj))
    (eP : (modelEquivalence X).inverse.obj
      (DerivedCategory.Q.obj (RingedSite.liftComplex.{u, u, u, u, u} (modelSite X) K) :
        DerivedCategory (SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf (modelSite X).O))) ≅ P)
    (eQ : (modelEquivalence X).inverse.obj
      (DerivedCategory.Q.obj (RingedSite.liftComplex.{u, u, u, u, u} (modelSite X) L) :
        DerivedCategory (SheafOfModules.{u}
          (Stacks.SheafOfModules.Tensor.ringSheaf (modelSite X).O))) ≅ Q) :
    letI := modelLinear X ψ
    letI := modelScalarSections X ψ
    ∃ e : DifferentialGradedModule.derivedCategory.{u, u, u}
          (RingedSite.Rep.{u, u, u, u, u, u} (modelSite X) R K).algebra ≌
        DifferentialGradedModule.derivedCategory.{u, u, u}
          (RingedSite.Rep.{u, u, u, u, u, u} (modelSite X) R L).algebra,
      e.functor = DifferentialGraded.Bimodule.derivedTensorFunctor
          (RingedSite.complexHomBimodule.{u, u, u, u, u} (modelSite X) R K L) ∧
      e.inverse = DifferentialGraded.Bimodule.derivedTensorFunctor
          (RingedSite.complexHomBimodule.{u, u, u, u, u} (modelSite X) R L K) ∧
      Nonempty (e.functor ≅
        ((dgaQuasicoherentEquivalence X ψ K
            (isRelativelyCompactGenerator_model hqc hqs K P hP hgenP eP)).trans
          (dgaQuasicoherentEquivalence X ψ L
            (isRelativelyCompactGenerator_model hqc hqs L Q hQ hgenQ eQ)).symm).functor) ∧
      Nonempty (e.inverse ≅
        ((dgaQuasicoherentEquivalence X ψ K
            (isRelativelyCompactGenerator_model hqc hqs K P hP hgenP eP)).trans
          (dgaQuasicoherentEquivalence X ψ L
            (isRelativelyCompactGenerator_model hqc hqs L Q hQ hgenQ eQ)).symm).inverse)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.17, Tag 09M9](https://stacks.math.columbia.edu/tag/09M9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
