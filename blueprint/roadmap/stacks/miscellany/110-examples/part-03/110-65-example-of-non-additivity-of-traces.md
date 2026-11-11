---
declaration: section
origin: cited
lean: Stacks.Examples.dualNumber_diagram_commutes_up_to_homotopy, Stacks.Examples.exists_distinguished_triangle_trace_nonadditive
statement: formalized
proof: formalized
---

# 110.65 Example of non-additivity of traces

Section 110.65 of the Stacks Project, [Tag 087J](https://stacks.math.columbia.edu/tag/087J). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 087K, an equation

[Tag 087K](https://stacks.math.columbia.edu/tag/087K) in the Stacks Project.

**`Stacks.Examples.dualNumber_diagram_commutes_up_to_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/DualNumberHomotopyDiagram.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/DualNumberHomotopyDiagram.lean#L95).

> The prescribed endomorphism of the left column and the identity endomorphisms of the middle
> and right columns make the two squares commute in the homotopy category.

```lean
public theorem dualNumber_diagram_commutes_up_to_homotopy :
    ∃ (i : dualNumberLeftComplex k ⟶ dualNumberMiddleComplex k)
      (p : dualNumberMiddleComplex k ⟶ dualNumberRightComplex k)
      (a : dualNumberLeftComplex k ⟶ dualNumberLeftComplex k),
      (i.f 1 = 𝟙 _) ∧
      (∀ n : ℤ, n ≠ 1 → i.f n = 0) ∧
      (p.f 0 = 𝟙 _) ∧
      (∀ n : ℤ, n ≠ 0 → p.f n = 0) ∧
      (a.f 1 = ModuleCat.ofHom (LinearMap.mulLeft (dualNumberRing k)
        (1 + (DualNumber.eps : dualNumberRing k)))) ∧
      (∀ n : ℤ, n ≠ 1 → a.f n = 0) ∧
      ((HomotopyCategory.quotient (DualNumberModuleCat k) (ComplexShape.up ℤ)).map a ≫
          (HomotopyCategory.quotient (DualNumberModuleCat k) (ComplexShape.up ℤ)).map i =
        (HomotopyCategory.quotient (DualNumberModuleCat k) (ComplexShape.up ℤ)).map i) ∧
      (i ≫ p = 0)
```

## Tag 087L, a lemma

[Tag 087L](https://stacks.math.columbia.edu/tag/087L) in the Stacks Project.

**`Stacks.Examples.exists_distinguished_triangle_trace_nonadditive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/NonAdditivityOfTraces.lean, line 492](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/NonAdditivityOfTraces.lean#L492).

> **Stacks 087L.** Trace need not be additive on an endomorphism of a distinguished
> triangle of perfect complexes in the homotopy category.

```lean
public theorem exists_distinguished_triangle_trace_nonadditive :
    ∃ (R : Type u) (hR : Ring R),
      letI : Ring R := hR
      ∃ (P Q S : CochainComplex (ModuleCat.{v} R) ℤ)
        (hP : CategoryTheory.FilteredDerived.finiteProjectiveComplex R P)
        (hQ : CategoryTheory.FilteredDerived.finiteProjectiveComplex R Q)
        (hS : CategoryTheory.FilteredDerived.finiteProjectiveComplex R S),
        let q := HomotopyCategory.quotient (ModuleCat.{v} R) (ComplexShape.up ℤ)
        ∃ (f : q.obj P ⟶ q.obj Q) (g : q.obj Q ⟶ q.obj S)
          (h : q.obj S ⟶ (q.obj P)⟦(1 : ℤ)⟧)
          (a : P ⟶ P) (b : Q ⟶ Q) (c : S ⟶ S),
          (Triangle.mk f g h ∈ distTriang _) ∧
          (∃ t : Triangle.mk f g h ⟶ Triangle.mk f g h,
            t.hom₁ = q.map a ∧ t.hom₂ = q.map b ∧ t.hom₃ = q.map c) ∧
          CategoryTheory.FilteredDerived.alternatingTrace R P hP a +
            CategoryTheory.FilteredDerived.alternatingTrace R S hS c ≠
            CategoryTheory.FilteredDerived.alternatingTrace R Q hQ b
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.65, Tag 087J](https://stacks.math.columbia.edu/tag/087J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
