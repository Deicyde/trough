---
declaration: section
origin: cited
lean: Stacks.Examples.dualNumber_diagram_commutes_up_to_homotopy, Stacks.Examples.exists_commRing_distinguished_triangle_trace_nonadditive
statement: formalized
proof: formalized
---

# 110.65 Example of non-additivity of traces

Section 110.65 of the Stacks Project, [Tag 087J](https://stacks.math.columbia.edu/tag/087J). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 087K, an equation

[Tag 087K](https://stacks.math.columbia.edu/tag/087K) in the Stacks Project.

**`Stacks.Examples.dualNumber_diagram_commutes_up_to_homotopy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/DualNumberHomotopyDiagram.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Algebra/DualNumberHomotopyDiagram.lean#L95).

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

**`Stacks.Examples.exists_commRing_distinguished_triangle_trace_nonadditive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/NonAdditivityOfTracesCommRing.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Algebra/NonAdditivityOfTracesCommRing.lean#L52). The attribute's comment: “Stacks' rings are commutative and its traces of perfect complexes lie in `R`: here `R` is a `CommRing` and the alternating traces are evaluated in `R`.”.

> **Stacks 087L.** There exist a commutative ring `R`, a distinguished triangle of perfect
> complexes in the homotopy category `K(R)` and an endomorphism `(a, b, c)` of this triangle with
> `Tr(a) + Tr(c) ≠ Tr(b)`, the traces taken in `R` itself. The vertices are bounded complexes of
> finite projective `R`-modules and `a`, `b`, `c` are presented by cochain maps; the trace in `R` is
> the alternating trace evaluated by `Stacks.Trace.commutativeAdditiveCommutatorQuotientEval`, which
> for a commutative ring identifies `R/[R,R]` with `R`. The witness is the dual numbers over `ℚ`.

```lean
public theorem exists_commRing_distinguished_triangle_trace_nonadditive :
    ∃ (R : Type u) (hR : CommRing R),
      letI : CommRing R := hR
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
          Stacks.Trace.commutativeAdditiveCommutatorQuotientEval R
              (CategoryTheory.FilteredDerived.alternatingTrace R P hP a) +
            Stacks.Trace.commutativeAdditiveCommutatorQuotientEval R
              (CategoryTheory.FilteredDerived.alternatingTrace R S hS c) ≠
            Stacks.Trace.commutativeAdditiveCommutatorQuotientEval R
              (CategoryTheory.FilteredDerived.alternatingTrace R Q hQ b)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.65, Tag 087J](https://stacks.math.columbia.edu/tag/087J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
