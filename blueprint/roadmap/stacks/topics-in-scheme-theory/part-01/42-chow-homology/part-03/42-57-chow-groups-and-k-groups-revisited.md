---
declaration: section
origin: cited
lean: Stacks.Chow.chowToGradedCoherentKZero_injective, Stacks.Chow.rationalCoherentKZeroToChowHomology_surjective, Stacks.Chow.bijective_liftBaseChange_coherentChowCharacter
statement: formalized
proof: formalized
---

# 42.57 Chow groups and K-groups revisited

Section 42.57 of the Stacks Project, [Tag 0FEV](https://stacks.math.columbia.edu/tag/0FEV). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FEW, a proposition

[Tag 0FEW](https://stacks.math.columbia.edu/tag/0FEW) in the Stacks Project.

**`Stacks.Chow.chowToGradedCoherentKZero_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowHomologyCoherentKZero.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowHomologyCoherentKZero.lean#L109). The attribute's comment: “injectivity of the canonical map `CH_k(X) ⊗ 𝐐 ⟶ gr_k K'₀(X) ⊗ 𝐐`; the composition `K'₀(X) → K₀(D_{X, perf}(𝒪_Y)) → A^*(X ⟶ Y) ⊗ 𝐐 → CH_*(X) ⊗ 𝐐`, the canonical maps of Lemma 42.23.4, and the two conditions (1) and (2) that the proof establishes for the composition and reduces the proposition to, are hypotheses: none of the three legs of the composition is constructed in this repository, `A^*` carrying no multiplication”.

> The canonical map `CH_k(X) ⊗ 𝐐 ⟶ gr_k K'₀(X) ⊗ 𝐐` is injective, for a homomorphism
> `ch : K'₀(X) → CH_*(X) ⊗ 𝐐` such that the class of a coherent module whose support has
> delta-dimension at most `j` has vanishing components in degrees above `j` (`hch_triangular`), and
> the degree `k` component of a lift to `F_k K'₀(X)` of `cls k α` is `1 ⊗ α` (`hch_diagonal`).

```lean
theorem chowToGradedCoherentKZero_injective
    (ch : CoherentKZero X →+ DirectSum ℤ fun j => TensorProduct ℤ ℚ (chowGroup C f j))
    (hch_triangular : ∀ (j j' : ℤ) (F : CoherentModulesDimLE C f j), j < j' →
      ch (KZero.mk _ F.obj) j' = 0)
    (cls : ∀ j : ℤ, chowGroup C f j →+ gradedCoherentKZero C f j) (k : ℤ)
    (hch_diagonal : ∀ (α : chowGroup C f k) (x : coherentKZeroFiltration C f k),
      toGradedCoherentKZero C f k x = cls k α →
        ch (x : CoherentKZero X) k = (1 : ℚ) ⊗ₜ[ℤ] α) :
    Function.Injective
      (TensorProduct.map (LinearMap.id : ℚ →ₗ[ℤ] ℚ) (cls k).toIntLinearMap)
```

**`Stacks.Chow.rationalCoherentKZeroToChowHomology_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowHomologyCoherentKZero.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChowHomologyCoherentKZero.lean#L156). The attribute's comment: “surjectivity of the composition `K'₀(X) ⊗ 𝐐 → CH_*(X) ⊗ 𝐐`; as for the injectivity statement in this file the composition, the canonical maps of Lemma 42.23.4 and the two conditions (1) and (2) that the proof establishes for the composition are hypotheses, none of the three legs of the composition being constructed in this repository; the injectivity of the composition is not proved, needing the surjectivity of the canonical maps and hence the unformalized half of Tag 02S9”.

> A homomorphism `ch : K'₀(X) → CH_*(X) ⊗ 𝐐` satisfying the conditions `hch_triangular` and
> `hch_diagonal` of `Stacks.Chow.chowToGradedCoherentKZero_injective` (the latter in every degree)
> becomes surjective after tensoring the source with `𝐐`, provided `δ_{X/S}` is bounded below.

```lean
theorem rationalCoherentKZeroToChowHomology_surjective
    (ch : CoherentKZero X →+ DirectSum ℤ fun j => TensorProduct ℤ ℚ (chowGroup C f j))
    (hch_triangular : ∀ (j j' : ℤ) (F : CoherentModulesDimLE C f j), j < j' →
      ch (KZero.mk _ F.obj) j' = 0)
    (cls : ∀ j : ℤ, chowGroup C f j →+ gradedCoherentKZero C f j)
    (hch_diagonal : ∀ (k : ℤ) (α : chowGroup C f k) (x : coherentKZeroFiltration C f k),
      toGradedCoherentKZero C f k x = cls k α →
        ch (x : CoherentKZero X) k = (1 : ℚ) ⊗ₜ[ℤ] α)
    (lo : ℤ) (hlo : ∀ x : X, lo ≤ relativeDimension C.dimensionFunction f x) :
    Function.Surjective (ch.toIntLinearMap.liftBaseChange ℚ)
```

**`Stacks.Chow.bijective_liftBaseChange_coherentChowCharacter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/ChowCoherentIsomorphism.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalIntersection/ChowCoherentIsomorphism.lean#L213). The attribute's comment: “the whole proposition: the map K'_0(X) ⊗ Q → CH_*(X) ⊗ Q, [F] ↦ ch(X → Y, F[0]) ∩ [Y], is bijective, and CH_k(X) ⊗ Q → gr_k K'_0(X) ⊗ Q is bijective for every k, for a closed immersion X → Y of schemes locally of finite type over S with Y regular and quasi-compact, (S, δ) as in Situation 02QL”.

> **Stacks 0FEW.** Let `(S, δ)` be as in Situation 02QL and let `i : X ⟶ Y` be a closed
> immersion of schemes locally of finite type over `S`, with `Y` regular and quasi-compact. Then
> the composition `K'₀(X) ⟶ K₀(D_{X, perf}(𝒪_Y)) ⟶ A^*(X ⟶ Y) ⊗ 𝐐 ⟶ CH_*(X) ⊗ 𝐐`,
> `[ℱ] ↦ ch(X ⟶ Y, ℱ[0]) ∩ [Y]`, induces an isomorphism `K'₀(X) ⊗ 𝐐 ≅ CH_*(X) ⊗ 𝐐`; moreover the
> canonical map `CH_k(X) ⊗ 𝐐 ⟶ gr_k K'₀(X) ⊗ 𝐐` is an isomorphism for every `k`.
>
> Surjectivity and the "moreover" are conditions (1) and (2) of the source's proof
> (`Stacks.Chow.surjective_liftBaseChange_coherentChowCharacter`,
> `Stacks.Chow.bijective_rTensor_chowToGradedCoherentKZero_of_isClosedImmersion`); injectivity is
> `Stacks.Chow.injective_liftBaseChange_coherentChowCharacter`.

```lean
theorem bijective_liftBaseChange_coherentChowCharacter :
    haveI := isNoetherian_of_isClosedImmersion_of_compactSpace C a i
    Function.Bijective ((coherentChowCharacter C a i hY).toIntLinearMap.liftBaseChange ℚ) ∧
      ∀ k : ℤ, Function.Bijective (TensorProduct.map (LinearMap.id : ℚ →ₗ[ℤ] ℚ)
        (chowToGradedCoherentKZero C (i ≫ a) k).toIntLinearMap)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.57, Tag 0FEV](https://stacks.math.columbia.edu/tag/0FEV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
