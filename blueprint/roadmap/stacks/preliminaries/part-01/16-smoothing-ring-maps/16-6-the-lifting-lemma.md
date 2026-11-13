---
declaration: section
origin: cited
lean: Stacks.Smoothing.exists_finitePresentation_lift_smoothAt
statement: formalized
proof: formalized
---

# 16.6 The lifting lemma

Section 16.6 of the Stacks Project, [Tag 07CN](https://stacks.math.columbia.edu/tag/07CN). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07CP, a lemma

[Tag 07CP](https://stacks.math.columbia.edu/tag/07CP) in the Stacks Project.

**`Stacks.Smoothing.exists_finitePresentation_lift_smoothAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Smoothing/LiftingLemma/ExistsLift.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Smoothing/LiftingLemma/ExistsLift.lean#L39).

> **Stacks Project, Tag 07CP.** A finitely presented algebra modulo `π²`
> admits a lift modulo `π` with the asserted smoothness properties.

```lean
public theorem exists_finitePresentation_lift_smoothAt
    (R : Type u) (Λ : Type v) (C : Type w)
    [CommRing R] [CommRing Λ] [CommRing C] [IsNoetherianRing R]
    [Algebra R Λ] (π : R)
    (hR : ∀ r : R, r * π = 0 ↔ r * π ^ 2 = 0)
    (hΛ : ∀ x : Λ,
      x * algebraMap R Λ π = 0 ↔ x * (algebraMap R Λ π) ^ 2 = 0)
    [Algebra (R ⧸ Ideal.span {π ^ 2}) C]
    [Algebra.FinitePresentation (R ⧸ Ideal.span {π ^ 2}) C]
    [Algebra (R ⧸ Ideal.span {π ^ 2})
      (Λ ⧸ Ideal.span {(algebraMap R Λ π) ^ 2})]
    (hquot : ∀ x : R, algebraMap (R ⧸ Ideal.span {π ^ 2})
      (Λ ⧸ Ideal.span {(algebraMap R Λ π) ^ 2})
        (Ideal.Quotient.mk _ x) = Ideal.Quotient.mk _ (algebraMap R Λ x))
    (f : C →ₐ[R ⧸ Ideal.span {π ^ 2}]
      Λ ⧸ Ideal.span {(algebraMap R Λ π) ^ 2}) :
    ∃ (D : Type (max u v w)) (_ : CommRing D) (_ : Algebra R D)
      (_ : Algebra.FinitePresentation R D) (g : D →ₐ[R] Λ)
      (c : C →+* D ⧸ Ideal.span {algebraMap R D π})
      (reduceΛ : (Λ ⧸ Ideal.span {(algebraMap R Λ π) ^ 2}) →+*
        Λ ⧸ Ideal.span {algebraMap R Λ π})
      (reduceD : (D ⧸ Ideal.span {algebraMap R D π}) →+*
        Λ ⧸ Ideal.span {algebraMap R Λ π})
      (_ : Algebra (C ⧸ Ideal.span {
        algebraMap (R ⧸ Ideal.span {π ^ 2}) C
          (Ideal.Quotient.mk (Ideal.span {π ^ 2}) π)})
        (D ⧸ Ideal.span {algebraMap R D π})),
      (∀ x : Λ, reduceΛ (Ideal.Quotient.mk _ x) = Ideal.Quotient.mk _ x) ∧
      (∀ x : D, reduceD (Ideal.Quotient.mk _ x) =
        Ideal.Quotient.mk _ (g x)) ∧
      (∀ x : C, reduceD (c x) = reduceΛ (f x)) ∧
      (∀ x : R, c (algebraMap (R ⧸ Ideal.span {π ^ 2}) C
          (Ideal.Quotient.mk _ x)) = Ideal.Quotient.mk _ (algebraMap R D x)) ∧
      (∀ x : C, algebraMap
          (C ⧸ Ideal.span {
            algebraMap (R ⧸ Ideal.span {π ^ 2}) C
              (Ideal.Quotient.mk (Ideal.span {π ^ 2}) π)})
          (D ⧸ Ideal.span {algebraMap R D π}) (Ideal.Quotient.mk _ x) = c x) ∧
      (∀ (q : Ideal D) [q.IsPrime], algebraMap R D π ∉ q →
        Algebra.IsSmoothAt R q) ∧
      (∀ (q : Ideal D) [q.IsPrime], algebraMap R D π ∈ q →
        (∃ (p : Ideal C) (_ : p.IsPrime),
          Algebra.IsSmoothAt (R ⧸ Ideal.span {π ^ 2}) p ∧
          p = Ideal.comap c (Ideal.map
            (Ideal.Quotient.mk (Ideal.span {algebraMap R D π})) q)) →
        Algebra.IsSmoothAt R q) ∧
      ∀ (q : Ideal (D ⧸ Ideal.span {algebraMap R D π})) [q.IsPrime],
        (∃ (p : Ideal C) (_ : p.IsPrime),
          Algebra.IsSmoothAt (R ⧸ Ideal.span {π ^ 2}) p ∧
          p = Ideal.comap c q) →
        Algebra.IsSmoothAt
          (C ⧸ Ideal.span {
            algebraMap (R ⧸ Ideal.span {π ^ 2}) C
              (Ideal.Quotient.mk (Ideal.span {π ^ 2}) π)}) q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 16.6, Tag 07CN](https://stacks.math.columbia.edu/tag/07CN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
