---
declaration: section
origin: cited
lean: Crystalline.exists_dividedPowers_secondOrderExtension
statement: formalized
proof: formalized
---

# 60.3 Some explicit divided power thickenings

Section 60.3 of the Stacks Project, [Tag 07HG](https://stacks.math.columbia.edu/tag/07HG). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07HH, a lemma

[Tag 07HH](https://stacks.math.columbia.edu/tag/07HH) in the Stacks Project.

**`Crystalline.exists_dividedPowers_secondOrderExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ExplicitDividedPower/Basic.lean, line 980](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/ExplicitDividedPower/Basic.lean#L980). The attribute's comment: “the first-order case, at N = 0 and q = 0”.

> The ideal of a second-order extension has divided powers given by the explicit
> second-order formula, and the scalar inclusion is a divided-power morphism.

```lean
public theorem exists_dividedPowers_secondOrderExtension
    {A : Type u} [CommRing A] (I : Ideal A) (γ : DividedPowers I)
    {M : Type v} [AddCommGroup M] [Module A M]
    {N : Type w} [AddCommGroup N] [Module A N]
    (q : M →ₗ[A] M →ₗ[A] N)
    {B : Type x} [CommRing B] [Algebra A B]
    (e : B ≃+ A × (M × N))
    (halgebra : ∀ a : A, e (algebraMap A B a) = (a, (0, 0)))
    (hmul : ∀ b b' : B,
      e (b * b') =
        ((e b).1 * (e b').1,
          ((e b).1 • (e b').2.1 + (e b').1 • (e b).2.1,
            (e b).1 • (e b').2.2 + (e b').1 • (e b).2.2 +
              q (e b).2.1 (e b').2.1 + q (e b').2.1 (e b).2.1)))
    (J : Ideal B) (hJ : ∀ b : B, b ∈ J ↔ (e b).1 ∈ I) :
    ∃ δ : DividedPowers J,
      (∀ (n : ℕ) (b : B), 2 ≤ n → b ∈ J →
        δ.dpow n b = e.symm
          (γ.dpow n (e b).1,
            (γ.dpow (n - 1) (e b).1 • (e b).2.1,
              γ.dpow (n - 1) (e b).1 • (e b).2.2 +
                γ.dpow (n - 2) (e b).1 • q (e b).2.1 (e b).2.1))) ∧
      DividedPowers.IsDPMorphism γ δ (algebraMap A B)
```

## Tag 07HI, a lemma

[Tag 07HI](https://stacks.math.columbia.edu/tag/07HI) in the Stacks Project.

**`Crystalline.exists_dividedPowers_secondOrderExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/ExplicitDividedPower/Basic.lean, line 980](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Crystalline/ExplicitDividedPower/Basic.lean#L980).

> The ideal of a second-order extension has divided powers given by the explicit
> second-order formula, and the scalar inclusion is a divided-power morphism.

```lean
public theorem exists_dividedPowers_secondOrderExtension
    {A : Type u} [CommRing A] (I : Ideal A) (γ : DividedPowers I)
    {M : Type v} [AddCommGroup M] [Module A M]
    {N : Type w} [AddCommGroup N] [Module A N]
    (q : M →ₗ[A] M →ₗ[A] N)
    {B : Type x} [CommRing B] [Algebra A B]
    (e : B ≃+ A × (M × N))
    (halgebra : ∀ a : A, e (algebraMap A B a) = (a, (0, 0)))
    (hmul : ∀ b b' : B,
      e (b * b') =
        ((e b).1 * (e b').1,
          ((e b).1 • (e b').2.1 + (e b').1 • (e b).2.1,
            (e b).1 • (e b').2.2 + (e b').1 • (e b).2.2 +
              q (e b).2.1 (e b').2.1 + q (e b').2.1 (e b).2.1)))
    (J : Ideal B) (hJ : ∀ b : B, b ∈ J ↔ (e b).1 ∈ I) :
    ∃ δ : DividedPowers J,
      (∀ (n : ℕ) (b : B), 2 ≤ n → b ∈ J →
        δ.dpow n b = e.symm
          (γ.dpow n (e b).1,
            (γ.dpow (n - 1) (e b).1 • (e b).2.1,
              γ.dpow (n - 1) (e b).1 • (e b).2.2 +
                γ.dpow (n - 2) (e b).1 • q (e b).2.1 (e b).2.1))) ∧
      DividedPowers.IsDPMorphism γ δ (algebraMap A B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.3, Tag 07HG](https://stacks.math.columbia.edu/tag/07HG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
