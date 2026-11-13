---
declaration: section
origin: cited
lean: Stacks.DifferentialGradedModule.SourceProjective.sourceProjective, Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isClosedUnderIsomorphisms, Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isTriangulated, Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isSaturated, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_carrier, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_algebraMap, Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_grading
statement: formalized
proof: formalized
---

# 22.36 Characterizing compact objects

Section 22.36 of the Stacks Project, [Tag 09QZ](https://stacks.math.columbia.edu/tag/09QZ). 6 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09R0, a remark

[Tag 09R0](https://stacks.math.columbia.edu/tag/09R0) in the Stacks Project.

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjective.lean#L74). The attribute's comment: “source\_projective\_dg\_modules”.

> The source-projective objects of the homotopy category of right differential graded
> `A`-modules: those from which morphisms are unchanged by passage to the derived category.

```lean
abbrev sourceProjective :
    ObjectProperty (DifferentialGradedModule.HomotopyCategory.{u, v, w} A)
```

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isClosedUnderIsomorphisms`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjective.lean#L189). The attribute's comment: “triangulated\_saturated”.

> **Stacks Project, Tag 09R0.** Source-projectivity is invariant under isomorphism in the
> homotopy category.

```lean
instance sourceProjective_isClosedUnderIsomorphisms :
    ObjectProperty.IsClosedUnderIsomorphisms (sourceProjective.{u, v, w} A)
```

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjective.lean#L196). The attribute's comment: “triangulated\_saturated”.

> **Stacks Project, Tag 09R0.** The source-projective objects form a triangulated
> subcategory of the homotopy category.

```lean
instance sourceProjective_isTriangulated :
    (sourceProjective.{u, v, w} A).IsTriangulated
```

**`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_isSaturated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjective.lean#L204). The attribute's comment: “triangulated\_saturated”.

> **Stacks Project, Tag 09R0.** The triangulated subcategory of source-projective objects is
> saturated.

```lean
instance sourceProjective_isSaturated :
    (sourceProjective.{u, v, w} A).IsSaturated
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L143). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The dual-number algebra, as a differential graded algebra
> concentrated in degree zero.

```lean
noncomputable def dualNumberAlgebra :
    DifferentialGradedAlgebra.{u, u} (DualNumber k)
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_carrier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L169). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The differential graded algebra has exactly the dual-number
> ring as its underlying algebra.

```lean
theorem dualNumberAlgebra_carrier : (dualNumberAlgebra k).A = DualNumber k
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_algebraMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L174). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The scalar structure on the concentrated algebra is the
> regular one.

```lean
theorem dualNumberAlgebra_algebraMap (r : DualNumber k) :
    cast (dualNumberAlgebra_carrier k)
      (algebraMap (DualNumber k) (dualNumberAlgebra k).A r) = r
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_grading`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L181). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The differential graded algebra is concentrated in degree
> zero.

```lean
theorem dualNumberAlgebra_grading (n : ℤ) :
    (dualNumberAlgebra k).grading n = if n = 0 then ⊤ else ⊥
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberAlgebra_differential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L186). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The differential graded algebra has zero differential.

```lean
theorem dualNumberAlgebra_differential : (dualNumberAlgebra k).d = 0
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L287). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The doubly infinite complex of free rank-one dual-number
> modules.

```lean
noncomputable def dualNumberModule :
    DifferentialGradedModule.{u, u, u} (dualNumberAlgebra k)
```

**`Stacks.DifferentialGradedModule.SourceProjective.gradedFreeEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L357). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** An isomorphism from the graded module to a direct sum of
> shifted copies of its regular module.

```lean
noncomputable def gradedFreeEquiv :
    (dualNumberModule k).M ≃ₗ[MulOpposite (dualNumberAlgebra k).A]
      (⨁ _ : ℤ, MulOpposite (dualNumberAlgebra k).A)
```

**`Stacks.DifferentialGradedModule.SourceProjective.gradedFreeEquiv_mem_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 366](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L366). The attribute's comment: “dual\_number\_counterexample”.

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

**`Stacks.DifferentialGradedModule.SourceProjective.gradedPieceEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L385). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The chosen regular-module coordinates on a homogeneous
> component.

```lean
noncomputable def gradedPieceEquiv (n : ℤ) :
    ((dualNumberModule k).grading n) ≃ₗ[DualNumber k] DualNumber k
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_differential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L414). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** In the regular coordinates, the differential is multiplication
> by `ε`.

```lean
theorem dualNumberModule_differential (n : ℤ) (x : (dualNumberModule k).grading n) :
    gradedPieceEquiv k (n + 1) ((dualNumberModule k).gradedDifferential n x) =
      DualNumber.eps * gradedPieceEquiv k n x
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 459](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L459). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The doubly infinite complex is acyclic.

```lean
theorem dualNumberModule_acyclic :
    DifferentialGradedModule.acyclic (dualNumberAlgebra k)
      ((DifferentialGradedModule.toHomotopyCategory (dualNumberAlgebra k)).obj
        (dualNumberModule k))
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_homotopy_id_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L531). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** The identity of the complex survives passage to the homotopy
> category.

```lean
theorem dualNumberModule_homotopy_id_ne_zero :
    (𝟙 ((DifferentialGradedModule.toHomotopyCategory (dualNumberAlgebra k)).obj
      (dualNumberModule k))) ≠ 0
```

**`Stacks.DifferentialGradedModule.SourceProjective.dualNumberModule_not_sourceProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjectiveCounterexample.lean#L543). The attribute's comment: “dual\_number\_counterexample”.

> **Stacks Project, Tag 09R0.** Graded freeness does not imply source-projectivity: the
> acyclic graded-free module above is not source-projective.

```lean
theorem dualNumberModule_not_sourceProjective :
    ¬ sourceProjective (dualNumberAlgebra k)
      ((DifferentialGradedModule.toHomotopyCategory (dualNumberAlgebra k)).obj
        (dualNumberModule k))
```

Declarations registered for the tag:

- [`Stacks.DifferentialGradedModule.SourceProjective.sourceProjective_iff_hom_acyclic_subsingleton`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjective.lean#L144), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DGA/SourceProjective.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/SourceProjective.lean#L168) (StacksFrontier): “acyclic\_target\_criterion”.

## Tag 09R1, a remark

[Tag 09R1](https://stacks.math.columbia.edu/tag/09R1) in the Stacks Project.

**`DifferentialGradedModule.isCompactObject_q_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteProjective.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteProjective.lean#L268). The attribute's comment: “compactness: a finite differential graded module in the category `𝒟` of Tag 09R0 is compact in `D(A, d)`; graded projectivity is not needed”.

> **A finite differential graded module whose morphisms in the homotopy category already
> compute its morphisms in the derived category represents a compact object of `D(A, d)`.** This is
> the question raised in [Stacks, Tag 09R1]: for every family `Fᵢ` of objects of `D(A, d)` indexed
> by a type of the ambient universe the canonical map `⨁ᵢ Hom(P, Fᵢ) → Hom(P, ∐ᵢ Fᵢ)` is bijective,
> because the family may be presented by differential graded modules, whose direct sum computes the
> direct sum of the family.
>
> This is the assertion of the remark: the source asks it for a `P` that is finite *and graded
> projective*, and answers it affirmatively for a `P` that is moreover an object of the category
> `𝒟` of [Stacks, Tag 09R0] — which is the hypothesis `hD` below. Graded projectivity is not
> needed and is not assumed, so this is more general than the source's claim. The definition of
> *finite* that the remark also gives is `DifferentialGradedModule.IsFinite`.

```lean
theorem isCompactObject_q_of_isFinite {P : DifferentialGradedModule.{u, u, u} A} (hP : IsFinite P)
    (hD : ∀ M : DifferentialGradedModule.{u, u, u} A, Function.Bijective
      (((quasiIsomorphisms' A).Q).map :
        ((toHomotopyCategory A).obj P ⟶ (toHomotopyCategory A).obj M) → _)) :
    IsCompactObject.{u} ((toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)
```

**`DifferentialGradedModule.IsFinite`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Finite.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Finite.lean#L42). The attribute's comment: “definition of a finite differential graded module”.

> A differential graded module that is finitely generated as a right module over its
> differential graded algebra.

```lean
public abbrev IsFinite {R : Type u} [CommRing R] {A : DifferentialGradedAlgebra R}
    (M : DifferentialGradedModule A) : Prop
```

## Tag 09R2, a lemma

[Tag 09R2](https://stacks.math.columbia.edu/tag/09R2) in the Stacks Project.

**`DifferentialGradedModule.exists_factorThrough_finiteSubfiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/FiniteSubfiltration.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/FiniteSubfiltration.lean#L707).

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

**`DifferentialGradedModule.isCompactObject_iff_exists_retract_hasFiniteCellFiltration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/CompactObjects.lean, line 777](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteCellFiltration/CompactObjects.lean#L777).

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

**`DifferentialGradedModule.exists_subsingleton_hom_of_isZero_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactCohomologyWindow.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CompactCohomologyWindow.lean#L315).

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

**`DifferentialGradedModule.isCompactObject_tfae_exists_retract`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteFree.lean, line 837](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CompactFiniteFree.lean#L837). The attribute's comment: “Corrected form. As printed, (1) ⟹ (2) is false (refuted by the source's own Tag 09R5; see errata.md and Examples/Algebra/CompactObjectNoFiniteProjectiveModel.lean). The correction replaces 'E can be represented by P' with 'E is a direct summand in D(A, d) of the image of P'. Proved: (1) compact ⟺ (2) summand of a finite FREE graded P with Hom\_K(P, -) = Hom\_D(P, -) ⟺ (3) summand of a finite graded-projective P with Hom\_K(P, -) = Hom\_D(P, -); and the source's (2) as printed ⟹ (1). The boundedness of A is not needed and is dropped.”.

> **[Stacks, Tag 09RB], corrected.** *"Let `(A, d)` be a differential graded algebra. Assume
> that `A^n = 0` for `|n| ≫ 0`. Let `E` be an object of `D(A, d)`. The following are equivalent:
> (1) `E` is a compact object, and (2) `E` can be represented by a differential graded `A`-module
> `P` which is finite projective as a graded `A`-module and satisfies
> `Hom_{K(A, d)}(P, M) = Hom_{D(A, d)}(P, M)` for every differential graded `A`-module `M`."*
>
> As printed, (1) ⟹ (2) is false: it is contradicted by the source's own [Stacks, Tag 09R5], over
> the bounded algebra `A = k[x, y]/(y²)` of Tag 09R4, and the refutation is
> `Stacks.Examples.not_forall_exists_finite_gradedProjective_of_isCompactObject` in
> `StacksFrontier/Examples/Algebra/CompactObjectNoFiniteProjectiveModel.lean` (recorded in
> `errata.md`, entry 09RB). The correction is to replace "can be represented by" in (2) by "is a
> direct summand in `D(A, d)` of (the image of)". With that change the statement holds, and the
> graded module may moreover be taken finite free. So the following are equivalent, for every
> differential graded algebra (the boundedness of `A` is not needed in any direction, and is
> dropped, which makes the statement more general):
>
> 1. `E` is a compact object;
> 2. `E` is a direct summand in `D(A, d)` of the image of a differential graded `A`-module `P` which
>    is finite free as a graded `A`-module (`DifferentialGradedModule.IsFiniteFreeAsGradedModule`)
>    and satisfies `Hom_{K(A, d)}(P, M) = Hom_{D(A, d)}(P, M)` for every `M`;
> 3. `E` is a direct summand in `D(A, d)` of the image of a differential graded `A`-module `P` which
>    is finite (`DifferentialGradedModule.IsFinite`, Tag 09R1) and projective as a graded `A`-module
>    (`Stacks.DifferentialGraded.DGModule.IsProjectiveAsGradedModule`, Tag 09K0) and satisfies
>    `Hom_{K(A, d)}(P, M) = Hom_{D(A, d)}(P, M)` for every `M`.
>
> The condition `Hom_{K(A, d)}(P, M) = Hom_{D(A, d)}(P, M)` is read as: the localization functor is
> bijective on morphisms from the class of `P` to the class of `M` (Tag 09R0). Condition (3) is the
> source's condition (2) with "represented by" corrected to "a direct summand of"; the second
> conjunct is the source's implication (2) ⟹ (1) as printed, which is true.
>
> Proof: (1) ⟹ (2) is
> `DifferentialGradedModule.exists_retract_isFiniteFreeAsGradedModule_of_isCompactObject`
> (Tag 09R3 and Tag 09KY); (2) ⟹ (3) holds because a finite free graded module is finite
> (`DifferentialGradedModule.isFinite_of_isFiniteFreeAsGradedModule`) and graded projective
> (`DifferentialGradedModule.isProjectiveAsGradedModule_of_isFiniteFreeAsGradedModule`); and
> (3) ⟹ (1) because the image of a finite `P` with `Hom_K = Hom_D` is compact
> (`DifferentialGradedModule.isCompactObject_q_of_isFinite`, Tag 09R1) and a direct summand of a
> compact object is compact (Tag 09QH).

```lean
theorem isCompactObject_tfae_exists_retract
    (A : DifferentialGradedAlgebra.{u, u} R) (E : derivedCategory' A) :
    List.TFAE
      [IsCompactObject.{u} E,
        ∃ P : DifferentialGradedModule.{u, u, u} A, IsFiniteFreeAsGradedModule P ∧
          (∀ M : DifferentialGradedModule.{u, u, u} A, Function.Bijective
            (((quasiIsomorphisms' A).Q).map :
              ((toHomotopyCategory A).obj P ⟶ (toHomotopyCategory A).obj M) → _)) ∧
          ∃ (i : E ⟶ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)
            (r : (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P ⟶ E), i ≫ r = 𝟙 E,
        ∃ P : DifferentialGradedModule.{u, u, u} A, IsFinite P ∧
          Stacks.DifferentialGraded.DGModule.IsProjectiveAsGradedModule.{u, u, u, u}
            (Unbundled.module P) ∧
          (∀ M : DifferentialGradedModule.{u, u, u} A, Function.Bijective
            (((quasiIsomorphisms' A).Q).map :
              ((toHomotopyCategory A).obj P ⟶ (toHomotopyCategory A).obj M) → _)) ∧
          ∃ (i : E ⟶ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)
            (r : (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P ⟶ E), i ≫ r = 𝟙 E] ∧
      ((∃ P : DifferentialGradedModule.{u, u, u} A, IsFinite P ∧
          Stacks.DifferentialGraded.DGModule.IsProjectiveAsGradedModule.{u, u, u, u}
            (Unbundled.module P) ∧
          (∀ M : DifferentialGradedModule.{u, u, u} A, Function.Bijective
            (((quasiIsomorphisms' A).Q).map :
              ((toHomotopyCategory A).obj P ⟶ (toHomotopyCategory A).obj M) → _)) ∧
          Nonempty (E ≅ (toHomotopyCategory A ⋙ (quasiIsomorphisms' A).Q).obj P)) →
        IsCompactObject.{u} E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.36, Tag 09QZ](https://stacks.math.columbia.edu/tag/09QZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
