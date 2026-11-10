---
declaration: section
origin: cited
lean: Stacks.DifferentialGradedModule.SourceProjective.sourceProjective, Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isClosedUnderIsomorphisms, Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isTriangulated, Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isSaturated, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_carrier, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_algebraMap, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_grading
statement: formalized
proof: formalized
---

# 22.36 Characterizing compact objects

Section 22.36 of the Stacks Project, [Tag 09QZ](https://stacks.math.columbia.edu/tag/09QZ). 6 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09R0, a remark

[Tag 09R0](https://stacks.math.columbia.edu/tag/09R0) in the Stacks Project.

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjective.lean#L74). The attribute's comment: “source_projective_dg_modules”.

> The source-projective objects of the homotopy category of right differential graded
> `A`-modules: those from which morphisms are unchanged by passage to the derived category.

```lean
abbrev sourceProjective :
    ObjectProperty (DifferentialGradedModule.HomotopyCategory.{u, v, w} A)
```

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjective.lean#L189). The attribute's comment: “triangulated_saturated”.

> **Stacks Project, Tag 09R0.** Source-projectivity is invariant under isomorphism in the
> homotopy category.

```lean
instance sourceProjective_isClosedUnderIsomorphisms :
    ObjectProperty.IsClosedUnderIsomorphisms (sourceProjective.{u, v, w} A)
```

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjective.lean#L196). The attribute's comment: “triangulated_saturated”.

> **Stacks Project, Tag 09R0.** The source-projective objects form a triangulated
> subcategory of the homotopy category.

```lean
instance sourceProjective_isTriangulated :
    (sourceProjective.{u, v, w} A).IsTriangulated
```

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjective.lean#L204). The attribute's comment: “triangulated_saturated”.

> **Stacks Project, Tag 09R0.** The triangulated subcategory of source-projective objects is
> saturated.

```lean
instance sourceProjective_isSaturated :
    (sourceProjective.{u, v, w} A).IsSaturated
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L143). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The dual-number algebra, as a differential graded algebra
> concentrated in degree zero.

```lean
noncomputable def dualNumberAlgebra :
    DifferentialGradedAlgebra.{u, u} (DualNumber k)
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_carrier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L169). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The differential graded algebra has exactly the dual-number
> ring as its underlying algebra.

```lean
theorem dualNumberAlgebra_carrier : (dualNumberAlgebra k).A = DualNumber k
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L174). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The scalar structure on the concentrated algebra is the
> regular one.

```lean
theorem dualNumberAlgebra_algebraMap (r : DualNumber k) :
    cast (dualNumberAlgebra_carrier k)
      (algebraMap (DualNumber k) (dualNumberAlgebra k).A r) = r
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_grading`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L181). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The differential graded algebra is concentrated in degree
> zero.

```lean
theorem dualNumberAlgebra_grading (n : ℤ) :
    (dualNumberAlgebra k).grading n = if n = 0 then ⊤ else ⊥
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_differential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L186). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The differential graded algebra has zero differential.

```lean
theorem dualNumberAlgebra_differential : (dualNumberAlgebra k).d = 0
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L287). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The doubly infinite complex of free rank-one dual-number
> modules.

```lean
noncomputable def dualNumberModule :
    DifferentialGradedModule.{u, u, u} (dualNumberAlgebra k)
```

**`Stacks.DifferentialGradedModule.SourceProjective.gradedFreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L357). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** An isomorphism from the graded module to a direct sum of
> shifted copies of its regular module.

```lean
noncomputable def gradedFreeEquiv :
    (dualNumberModule k).M ≃ₗ[MulOpposite (dualNumberAlgebra k).A]
      (⨁ _ : ℤ, MulOpposite (dualNumberAlgebra k).A)
```

**`Stacks.DifferentialGradedModule.SourceProjective.gradedFreeEquiv_mem_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L366). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The direct-sum coordinates identify each homogeneous piece
> with its corresponding shifted copy of the regular module.

```lean
theorem gradedFreeEquiv_mem_iff (n : ℤ) (x : (dualNumberModule k).M) :
    x ∈ (dualNumberModule k).grading n ↔
      ∃ a : MulOpposite (dualNumberAlgebra k).A,
        gradedFreeEquiv k x =
          DirectSum.lof (MulOpposite (dualNumberAlgebra k).A) ℤ
            (fun _ => MulOpposite (dualNumberAlgebra k).A) n a
```

**`Stacks.DifferentialGradedModule.SourceProjective.gradedPieceEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L385). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The chosen regular-module coordinates on a homogeneous
> component.

```lean
noncomputable def gradedPieceEquiv (n : ℤ) :
    ((dualNumberModule k).grading n) ≃ₗ[DualNumber k] DualNumber k
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_differential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L414). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** In the regular coordinates, the differential is multiplication
> by `ε`.

```lean
theorem dualNumberModule_differential (n : ℤ) (x : (dualNumberModule k).grading n) :
    gradedPieceEquiv k (n + 1) ((dualNumberModule k).gradedDifferential n x) =
      DualNumber.eps * gradedPieceEquiv k n x
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L459). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The doubly infinite complex is acyclic.

```lean
theorem dualNumberModule_acyclic :
    DifferentialGradedModule.acyclic (dualNumberAlgebra k)
      ((DifferentialGradedModule.toHomotopyCategory (dualNumberAlgebra k)).obj
        (dualNumberModule k))
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_homotopy_id_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L531). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** The identity of the complex survives passage to the homotopy
> category.

```lean
theorem dualNumberModule_homotopy_id_ne_zero :
    (𝟙 ((DifferentialGradedModule.toHomotopyCategory (dualNumberAlgebra k)).obj
      (dualNumberModule k))) ≠ 0
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_not_sourceProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 543](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L543). The attribute's comment: “dual_number_counterexample”.

> **Stacks Project, Tag 09R0.** Graded freeness does not imply source-projectivity: the
> acyclic graded-free module above is not source-projective.

```lean
theorem dualNumberModule_not_sourceProjective :
    ¬ sourceProjective (dualNumberAlgebra k)
      ((DifferentialGradedModule.toHomotopyCategory (dualNumberAlgebra k)).obj
        (dualNumberModule k))
```

Declarations registered for the tag:

- [`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_iff_hom_acyclic_subsingleton`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjective.lean#L144), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/SourceProjective.lean#L168) (StacksFrontier): “acyclic_target_criterion”.

## Tag 09R1, a remark

[Tag 09R1](https://stacks.math.columbia.edu/tag/09R1) in the Stacks Project.

**`DifferentialGradedModule.IsFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Finite.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/Finite.lean#L37). The attribute's comment: “finite_differential_graded_module”.

> A differential graded module that is finitely generated as a right module over its
> differential graded algebra.

```lean
public abbrev IsFinite {R : Type u} [CommRing R] {A : DifferentialGradedAlgebra R}
    (M : DifferentialGradedModule A) : Prop
```

## Tag 09R2, a lemma

[Tag 09R2](https://stacks.math.columbia.edu/tag/09R2) in the Stacks Project.

**`DifferentialGradedModule.exists_factorThrough_finiteSubfiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/FiniteSubfiltration.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/FiniteSubfiltration.lean#L707).

> **Stacks Tag 09R2.** Let `(A, d)` be a differential graded algebra, let `E` be a compact
> object of `D(A, d)` and let `P` be a differential graded `A`-module carrying a finite filtration
> `0 = F₋₁P ⊆ F₀P ⊆ ⋯ ⊆ FₙP = P` by differential graded submodules whose graded pieces are direct
> sums `F_{i+1}P/FᵢP ≅ ⨁_{j ∈ Jᵢ} A[k_{i,j}]` of shifts of the algebra. Then every morphism
> `E ⟶ P` of `D(A, d)` factors through a differential graded submodule `P' ⊆ P` whose intersections
> with the filtration have graded pieces the finite subsums `⨁_{j ∈ J'ᵢ} A[k_{i,j}]`, for finite
> subsets `J'ᵢ ⊆ Jᵢ`.
>
> The filtration of `P'` is produced as the pullback of that of `P`, and the identification of its
> graded pieces with the finite subsums is compatible with the given identification of the graded
> pieces of `P`, through the inclusion of the subsum.

```lean
theorem exists_factorThrough_finiteSubfiltration (A : DifferentialGradedAlgebra.{u, u} R)
    (n : ℕ) (P : DifferentialGradedModule.{u, u, u} A) (F : Filtration P ℕ)
    (_hzero : IsZero (F.obj 0)) (htop : IsIso (F.ι.app (n + 1)))
    (J : Fin (n + 1) → Type u) (k : ∀ i, J i → ℤ)
    (e : ∀ i : Fin (n + 1), cokernel (F.diagram.map (homOfLE (Nat.le_succ i.val))) ≅
      ∐ fun j : J i => shift (regularModule A) (k i j))
    (E : derivedCategory' A) [IsCompactObject.{u} E]
    (f : E ⟶ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P) :
    ∃ (P' : DifferentialGradedModule.{u, u, u} A) (p : P' ⟶ P),
      Mono p ∧
      ∃ (F' : Filtration P' ℕ) (β : ∀ i : ℕ, F'.obj i ⟶ F.obj i),
        (∀ i : ℕ, IsPullback (F'.ι.app i) (β i) p (F.ι.app i)) ∧
        (∃ (J' : ∀ i : Fin (n + 1), Finset (J i))
          (e' : ∀ i : Fin (n + 1),
            cokernel (F'.diagram.map (homOfLE (Nat.le_succ i.val))) ≅
              ∐ fun j : ↑(J' i) => shift (regularModule A) (k i j.val))
          (q : ∀ i : Fin (n + 1),
            cokernel (F'.diagram.map (homOfLE (Nat.le_succ i.val))) ⟶
              cokernel (F.diagram.map (homOfLE (Nat.le_succ i.val)))),
          (∀ i : Fin (n + 1),
            cokernel.π (F'.diagram.map (homOfLE (Nat.le_succ i.val))) ≫ q i =
              β (i.val + 1) ≫ cokernel.π (F.diagram.map (homOfLE (Nat.le_succ i.val)))) ∧
          (∀ i : Fin (n + 1),
            (e' i).hom ≫ Sigma.map' (fun j : ↑(J' i) => j.val) (fun _ => 𝟙 _) =
              q i ≫ (e i).hom)) ∧
        ∃ g : E ⟶ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P',
          g ≫ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).map p = f
```

## Tag 09R3, a proposition

[Tag 09R3](https://stacks.math.columbia.edu/tag/09R3) in the Stacks Project.

**`DifferentialGradedModule.isCompactObject_iff_exists_retract_hasFiniteCellFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/CompactObjects.lean, line 777](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/CompactObjects.lean#L777).

> **Stacks Tag 09R3.** *"Let `(A, d)` be a differential graded algebra. Let `E` be an object of
> `D(A, d)`. The following are equivalent: (1) `E` is a compact object, and (2) `E` is a direct
> summand of an object which is represented by a differential graded module `P` which has a finite
> filtration `F_•` by differential graded submodules such that `F_iP/F_{i-1}P` are finite direct
> sums of shifts of `A`."*
>
> Condition (2) is read as: `E` is a retract of the image of a module with a finite cell filtration,
> `DifferentialGradedModule.HasFiniteCellFiltration`. A retract is the same thing as a direct
> summand here, the derived category of a differential graded algebra being idempotent complete
> ([Stacks, Tag 05QW]); the retract formulation is the one both implications produce and consume.

```lean
theorem isCompactObject_iff_exists_retract_hasFiniteCellFiltration
    (A : DifferentialGradedAlgebra.{u, u} R) (E : derivedCategory' A) :
    IsCompactObject.{u} E ↔
      ∃ P : DifferentialGradedModule.{u, u, u} A, HasFiniteCellFiltration P ∧
        ∃ (i : E ⟶ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)
          (r : (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P ⟶ E), i ≫ r = 𝟙 E
```

## Tag 09RA, a lemma

[Tag 09RA](https://stacks.math.columbia.edu/tag/09RA) in the Stacks Project.

**`DifferentialGradedModule.exists_subsingleton_hom_of_isZero_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactCohomologyWindow.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactCohomologyWindow.lean#L315).

> **Stacks Tag 09RA.** For every compact object `E` of the derived category of a differential
> graded algebra there are integers `a ≤ b` such that `Hom_{D(A, d)}(E, M) = 0` for every object `M`
> whose cohomology `Hⁱ(M)` vanishes for all `i ∈ [a, b]`.
>
> If no such interval existed, then for each `n` there would be an object `Mₙ` with vanishing
> cohomology on `[-n, n]` and a nonzero morphism `E ⟶ Mₙ`. In each fixed degree only finitely many
> of the `Mₙ` have nonvanishing cohomology, so
> `DifferentialGradedModule.finite_setOf_ne_zero_of_isCompactObject` applies to the family and
> contradicts the fact that all of the chosen morphisms are nonzero.

```lean
theorem exists_subsingleton_hom_of_isZero_homology (A : DifferentialGradedAlgebra.{u, u} R)
    (E : derivedCategory' A) [IsCompactObject.{u} E] :
    ∃ a b : ℤ, a ≤ b ∧ ∀ M : derivedCategory' A,
      (∀ i : ℤ, a ≤ i → i ≤ b → IsZero (M.as.obj.as.toCochainComplex.homology i)) →
        Subsingleton (E ⟶ M)
```

## Tag 09RB, a lemma

[Tag 09RB](https://stacks.math.columbia.edu/tag/09RB) in the Stacks Project.

**`DifferentialGradedModule.exists_retract_isFiniteFreeAsGradedModule_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteFree.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteFree.lean#L634). The attribute's comment: “(1) ⟹ (2), corrected: a compact object is a DIRECT SUMMAND of (the image of) a differential graded module which is finite FREE as a graded module and satisfies Hom_K = Hom_D; the literal statement, with 'represented by' and 'finite projective', is a mistake in the source — see the refutation in Examples/Algebra/CompactObjectNoFiniteProjectiveModel.lean”.

> **[Stacks, Tag 09RB], the implication (1) ⟹ (2), in the corrected form that the source's own
> proof establishes.** A compact object `E` of `D(A, d)` is a *direct summand* in `D(A, d)` of the
> image of a differential graded `A`-module `P` which is *finite free* as a graded `A`-module and
> satisfies `Hom_{K(A, d)}(P, M) = Hom_{D(A, d)}(P, M)` for every differential graded `A`-module
> `M`.
>
> The literal statement of the source — that `E` can be *represented by* such a `P`, with *finite
> projective* in place of finite free — is **false**, and is **a mistake in the Stacks Project,
> pending review**: it is contradicted by the source's own [Stacks, Tag 09R5], whose compact object
> over the bounded algebra `A = k[x, y]/(y²)` of Tag 09R4 has no finite graded-projective
> representative at all. That refutation is
> `Stacks.Examples.not_forall_exists_finite_gradedProjective_of_isCompactObject`, in
> `StacksFrontier/Examples/Algebra/CompactObjectNoFiniteProjectiveModel.lean`. The two differences
> below are exactly what the argument of Tag 09R3 delivers, and the counterexample is consistent
> with them: there `E = Ker(x)` *is* a direct summand of the regular module, which is finite free.
>
> The statement is **unconditional**: the boundedness hypothesis "`A^n = 0` for `|n| ≫ 0`" of the
> source is not assumed and is not used anywhere in the proof, which is part of why the literal
> statement cannot be rescued by it.
>
> The proof composes the two implications the chapter already has. [Stacks, Tag 09R3],
> `DifferentialGradedModule.isCompactObject_iff_exists_retract_hasFiniteCellFiltration`, makes `E` a
> retract of the image of a module `P` with a finite cell filtration; such a `P` is finite free as a
> graded module, because its filtration is built out of finitely many finite direct sums of shifts
> of the algebra and splits as a filtration of graded modules
> (`DifferentialGradedModule.isFiniteFreeAsGradedModule_of_hasFiniteCellFiltration`); and it is
> orthogonal on the left to the acyclic modules, so morphisms out of it are not changed by
> localization (`DifferentialGradedModule.bijective_q_map_of_hasFiniteCellFiltration`, Tag 09KY),
> which is the condition of [Stacks, Tag 09R0].
>
> The converse holds too, as
> `DifferentialGradedModule.isCompactObject_of_retract_isFiniteFreeAsGradedModule`, so the tag's
> equivalence is restored by the correction; the registration of (2) ⟹ (1) stays on the source's own
> spelling of condition (2), namely
> `DifferentialGradedModule.isCompactObject_of_exists_finite_projective_representative`.

```lean
theorem exists_retract_isFiniteFreeAsGradedModule_of_isCompactObject
    (A : DifferentialGradedAlgebra.{u, u} R) (E : derivedCategory' A)
    (hE : IsCompactObject.{u} E) :
    ∃ P : DifferentialGradedModule.{u, u, u} A, IsFiniteFreeAsGradedModule P ∧
      (∀ M : DifferentialGradedModule.{u, u, u} A, Function.Bijective
        (((quasiIsomorphisms' A).Q).map :
          ((toHomotopyCategory A).obj P ⟶ (toHomotopyCategory A).obj M) → _)) ∧
      ∃ (i : E ⟶ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)
        (r : (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P ⟶ E), i ≫ r = 𝟙 E
```

**`DifferentialGradedModule.isCompactObject_of_exists_finite_projective_representative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteProjective.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteProjective.lean#L293). The attribute's comment: “(2) ⟹ (1)”.

> **[Stacks, Tag 09RB], the implication (2) ⟹ (1).** *"Let `(A, d)` be a differential graded
> algebra. Assume that `A^n = 0` for `|n| ≫ 0`. Let `E` be an object of `D(A, d)`. The following are
> equivalent: (1) `E` is a compact object, and (2) `E` can be represented by a differential graded
> `A`-module `P` which is finite projective as a graded `A`-module and satisfies
> `Hom_{K(A, d)}(P, M) = Hom_{D(A, d)}(P, M)` for every differential graded `A`-module `M`."*
>
> Condition (2) is read as the conjunction of: `P` is finite, that is finitely generated as a right
> `A`-module (`DifferentialGradedModule.IsFinite`, Tag 09R1); `P` is projective as a graded module
> (`Stacks.DifferentialGraded.DGModule.IsProjectiveAsGradedModule`, Tag 09K0); the localization
> functor is bijective on morphisms out of the class of `P` into the class of every differential
> graded module (Tag 09R0); and `E` is isomorphic in `D(A, d)` to the class of `P`.
>
> The boundedness of `A` and the graded projectivity of `P` are hypotheses of the source statement
> and are recorded here, but this implication uses neither: finiteness together with the comparison
> of morphism groups already gives compactness.

```lean
theorem isCompactObject_of_exists_finite_projective_representative
    (A : DifferentialGradedAlgebra.{u, u} R) (c : ℤ)
    (_hA : ∀ n : ℤ, c ≤ |n| → A.grading n = ⊥) (E : derivedCategory' A)
    (hE : ∃ P : DifferentialGradedModule.{u, u, u} A, IsFinite P ∧
      Stacks.DifferentialGraded.DGModule.IsProjectiveAsGradedModule.{u, u, u, u}
        (Unbundled.module P) ∧
      (∀ M : DifferentialGradedModule.{u, u, u} A, Function.Bijective
        (((quasiIsomorphisms' A).Q).map :
          ((toHomotopyCategory A).obj P ⟶ (toHomotopyCategory A).obj M) → _)) ∧
      Nonempty (E ≅ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)) :
    IsCompactObject.{u} E
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.36, Tag 09QZ](https://stacks.math.columbia.edu/tag/09QZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
