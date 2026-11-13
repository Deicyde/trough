---
declaration: section
origin: cited
lean: Stacks.Examples.RaynaudGruson.exists_flat_at_prime_not_flat_on_neighborhood
statement: formalized
proof: formalized
---

# 110.37 Finite type, not finitely presented, flat at prime

Section 110.37 of the Stacks Project, [Tag 05G1](https://stacks.math.columbia.edu/tag/05G1). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05G2, a lemma

[Tag 05G2](https://stacks.math.columbia.edu/tag/05G2) in the Stacks Project.

**`Stacks.Examples.RaynaudGruson.exists_flat_at_prime_not_flat_on_neighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/RaynaudGruson/NoFlatNeighborhood.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/RaynaudGruson/NoFlatNeighborhood.lean#L272).

> **The Raynaud--Gruson example.** There is a local ring `A`, a finite type ring map `A → B`
> and a prime `q` of `B` over the maximal ideal of `A` such that `B_q` is flat over `A` while for
> every `g ∈ B` outside `q` the ring `B_g` is neither of finite presentation nor flat over `A`.

```lean
theorem exists_flat_at_prime_not_flat_on_neighborhood :
    ∃ (A B : Type) (_ : CommRing A) (_ : CommRing B) (_ : IsLocalRing A) (φ : A →+* B)
      (q : Ideal B) (_ : q.IsPrime),
      φ.FiniteType ∧ q.comap φ = IsLocalRing.maximalIdeal A ∧
        ((algebraMap B (Localization.AtPrime q)).comp φ).Flat ∧
        ∀ g : B, g ∉ q →
          ¬ ((algebraMap B (Localization.Away g)).comp φ).FinitePresentation ∧
          ¬ ((algebraMap B (Localization.Away g)).comp φ).Flat
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.37, Tag 05G1](https://stacks.math.columbia.edu/tag/05G1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
