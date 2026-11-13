---
declaration: section
origin: cited
lean: SSet.trivialKanFibrations_of_coskeletal, SSet.nonempty_homotopy_of_app_eq_of_isCoskeletal, SSet.hasLiftingProperty_augmentedCechNerve_hom, SSet.trivialKanFibrations_augmentedCechNerve_hom_of_surjective
statement: formalized
proof: formalized
---

# 14.32 A homotopy equivalence

Section 14.32 of the Stacks Project, [Tag 01A5](https://stacks.math.columbia.edu/tag/01A5). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01A6, a lemma

[Tag 01A6](https://stacks.math.columbia.edu/tag/01A6) in the Stacks Project.

**`SSet.trivialKanFibrations_of_coskeletal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean#L167).

> **Stacks 01A6**.
> Let `f : V ⟶ U` be a morphism of simplicial sets and let `n ≥ 0`. Assume:
> 1. `fᵢ` is bijective for every `i < n`;
> 2. `fₙ` is surjective;
> 3. the canonical (unit) morphism `U → cosk_n sk_n U` is an isomorphism;
> 4. the canonical (unit) morphism `V → cosk_n sk_n V` is an isomorphism.
> Then `f` is a trivial Kan fibration.

```lean
theorem trivialKanFibrations_of_coskeletal
    {V U : SSet} (f : V ⟶ U) (n : ℕ)
    (h1 : ∀ i : ℕ, i < n → Function.Bijective (f.app (op ⦋i⦌)))
    (h2 : Function.Surjective (f.app (op ⦋n⦌)))
    (h3 : IsIso ((coskAdj n).unit.app U))
    (h4 : IsIso ((coskAdj n).unit.app V)) :
    trivialKanFibrations f
```

## Tag 01A9, a lemma

[Tag 01A9](https://stacks.math.columbia.edu/tag/01A9) in the Stacks Project.

**`SSet.nonempty_homotopy_of_app_eq_of_isCoskeletal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean#L415). The attribute's comment: “the conclusion is strengthened from `f⁰` and `f¹` being homotopic to the existence of a homotopy from `f⁰` to `f¹`, which is what both of the source's proofs produce; hypothesis (3) of the source, that `V ⟶ cosk_n sk_n V` is an isomorphism, is dropped, since neither of the source's proofs uses it: maps into an `n`-coskeletal object are exactly maps of their `n`-truncations, by `coskAdj n`, for an arbitrary source; coskeletality of `U` is Mathlib's `IsCoskeletal`, equivalent to the source's `U ⟶ cosk_n sk_n U` being an isomorphism”. References: SGA 4 Vbis (3.0.2.4), “simplicial sets”.

> **Two maps into an `n`-coskeletal simplicial set agreeing below degree `n` are homotopic,
> [Stacks, Tag 01A9].** Let `f₀, f₁ : V ⟶ U` be maps of simplicial sets whose components
> `V_i ⟶ U_i` agree for every `i < n`, and assume that the canonical morphism
> `U ⟶ cosk_n sk_n U` is an isomorphism, i.e. that `U` is `n`-coskeletal. Then there is a
> simplicial homotopy `V ⊗ Δ[1] ⟶ U` from `f₀` to `f₁`; in particular `f₀` and `f₁` are homotopic.
> No hypothesis on `V` is needed.

```lean
theorem nonempty_homotopy_of_app_eq_of_isCoskeletal {V U : SSet.{u}} (n : ℕ) [U.IsCoskeletal n]
    (f₀ f₁ : V ⟶ U) (h : ∀ i < n, f₀.app (op ⦋i⦌) = f₁.app (op ⦋i⦌)) :
    Nonempty (Homotopy f₀ f₁)
```

## Tag 01AB, a lemma

[Tag 01AB](https://stacks.math.columbia.edu/tag/01AB) in the Stacks Project.

**`SSet.hasLiftingProperty_augmentedCechNerve_hom`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean#L471). The attribute's comment: “the lifting property proved is against every map injective on vertices, hence against every monomorphism of simplicial sets, not only the boundary inclusions”.

> **The augmentation of the Čech nerve of a surjection of sets has the right lifting property
> with respect to every morphism of simplicial sets injective on vertices, [Stacks, Tag 01AB].**
> Monomorphisms of simplicial sets are injective in every degree, so the class of morphisms covered
> contains every monomorphism, and in particular the boundary inclusions `∂Δ[n] ⟶ Δ[n]` against which
> `trivialKanFibrations` asks for lifts.

```lean
lemma hasLiftingProperty_augmentedCechNerve_hom (F : Arrow (Type u))
    (hF : Function.Surjective F.hom) {K L : SSet.{u}} {i : K ⟶ L}
    (hi : Function.Injective (i.app (op ⦋0⦌))) :
    HasLiftingProperty i F.augmentedCechNerve.hom
```

**`SSet.trivialKanFibrations_augmentedCechNerve_hom_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean, line 528](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialSet/TrivialKanFibration/CechNerve.lean#L528). The attribute's comment: “the simplicial set of the source's Example 016E is the Čech nerve `(Arrow.mk f).cechNerve`, and the source's morphism from it to the constant simplicial set with value `B` is the augmentation `(Arrow.mk f).augmentedCechNerve.hom`”.

> **The Čech nerve of a surjection of sets is a trivial Kan fibration, [Stacks, Tag 01AB].**
> Let `f : A ⟶ B` be a surjective map of sets and let `U` be the simplicial set with
> `U_n = A ×_B A ×_B ⋯ ×_B A` (`n + 1` factors), the Čech nerve of `f`. Then the augmentation of
> `U` over the constant simplicial set with value `B`, given in degree `n` by the projection
> `(a_0, …, a_n) ↦ f a_0` to the base, is a trivial Kan fibration.

```lean
theorem trivialKanFibrations_augmentedCechNerve_hom_of_surjective {A B : Type u} {f : A ⟶ B}
    (hf : Function.Surjective f) : trivialKanFibrations (Arrow.mk f).augmentedCechNerve.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.32, Tag 01A5](https://stacks.math.columbia.edu/tag/01A5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
