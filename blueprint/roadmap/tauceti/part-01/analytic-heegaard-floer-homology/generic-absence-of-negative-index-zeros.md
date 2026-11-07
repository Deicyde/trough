---
declaration: theorem
origin: cited
lean: TauCeti.mem_residual_setOf_forall_section_ne_zero_of_index_neg
statement: formalized
proof: formalized
---

# Generic absence of negative-index zeros

If the slice linearization is Fredholm of
negative index at each zero and the total section is transverse to zero, zero-free parameters
form a residual set. Second countability is needed only for the universal zero set.

```lean
TauCeti.mem_residual_setOf_forall_section_ne_zero_of_index_neg.{u_1, u_2, u_3, u_4, u_5, u_6, u_7,
    u_8}
  {X : Type u_1} {Λ : Type u_2} {M : Type u_3} {B : Type u_4} {F : Type u_5} {EB : Type u_6}
  {HB : Type u_7} {E : B → Type u_8} [NormedAddCommGroup X] [NormedSpace ℝ X] [TopologicalSpace M]
  [ChartedSpace X M] [NormedAddCommGroup F] [NormedSpace ℝ F] [NormedAddCommGroup EB]
  [NormedSpace ℝ EB] [TopologicalSpace HB] {I : ModelWithCorners ℝ EB HB} [TopologicalSpace B]
  [ChartedSpace HB B] [(a : B) → TopologicalSpace (E a)] [TopologicalSpace (Bundle.TotalSpace F E)]
  [(a : B) → AddCommGroup (E a)] [(a : B) → _root_.Module ℝ (E a)] [FiberBundle F E]
  [VectorBundle ℝ F E] {b : M × Λ → B} {s : (z : M × Λ) → E (b z)} [NormedAddCommGroup Λ]
  [NormedSpace ℝ Λ] [CompleteSpace X] [CompleteSpace Λ] [CompleteSpace F]
  [IsManifold (modelWithCornersSelf ℝ X) 1 M] [SecondCountableTopology ↑{z | s z = 0}]
  {n : WithTop ℕ∞}
  (hcont :
    ∀ (z : M × Λ),
      s z = 0 →
        ContMDiffAt ((modelWithCornersSelf ℝ X).prod (modelWithCornersSelf ℝ Λ))
          (I.prod (modelWithCornersSelf ℝ F)) n (fun w => ⟨b w, s w⟩) z)
  (hFred :
    ∀ (z : M × Λ),
      s z = 0 →
        (TauCeti.sectionLinearization (modelWithCornersSelf ℝ X) (fun y => b (y, z.2))
            (fun y => s (y, z.2)) z.1).IsFredholm)
  (htotal :
    ∀ (z : M × Λ),
      s z = 0 →
        Function.Surjective
          ⇑(TauCeti.sectionLinearization
              ((modelWithCornersSelf ℝ X).prod (modelWithCornersSelf ℝ Λ)) b s z))
  (hn :
    ∀ (z : M × Λ),
      s z = 0 →
        ↑(Module.finrank ℝ
                  ↥(↑(TauCeti.sectionLinearization (modelWithCornersSelf ℝ X) (fun y => b (y, z.2))
                          (fun y => s (y, z.2)) z.1)).ker ^
                2 +
              1) ≤
          n)
  (hindex :
    ∀ (z : M × Λ),
      s z = 0 →
        (↑(TauCeti.sectionLinearization (modelWithCornersSelf ℝ X) (fun y => b (y, z.2))
                (fun y => s (y, z.2)) z.1)).index <
          0) :
  {l | ∀ (x : M), s (x, l) ≠ 0} ∈ residual Λ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_residual_setOf_forall_section_ne_zero_of_index_neg`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Section/Parametric.html#TauCeti.mem_residual_setOf_forall_section_ne_zero_of_index_neg).

## Sources

- [Tau Ceti documentation: `TauCeti.mem_residual_setOf_forall_section_ne_zero_of_index_neg`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/VectorBundle/Section/Parametric.html#TauCeti.mem_residual_setOf_forall_section_ne_zero_of_index_neg)
- [Source of `TauCeti.mem_residual_setOf_forall_section_ne_zero_of_index_neg` in TauCeti/Geometry/Manifold/VectorBundle/Section/Parametric.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/VectorBundle/Section/Parametric.lean#L369)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HeegaardFloer/STATUS.md)
