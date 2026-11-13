---
declaration: section
origin: cited
lean: AlgebraicGeometry.hasDenseChowModification, AlgebraicGeometry.isClosedImmersion_chowGraph, AlgebraicGeometry.isProjectiveMorphism_chowModification, AlgebraicGeometry.isProjective_chowModification, AlgebraicGeometry.exists_isSchemeTheoreticallyDense_chowModification, AlgebraicGeometry.exists_isReduced_chowModification
statement: formalized
proof: formalized
---

# 30.18 Chow's Lemma

Section 30.18 of the Stacks Project, [Tag 02O2](https://stacks.math.columbia.edu/tag/02O2). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0200, a lemma

[Tag 0200](https://stacks.math.columbia.edu/tag/0200) in the Stacks Project.

**`AlgebraicGeometry.hasDenseChowModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Segre/ChartSurjective.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Segre/ChartSurjective.lean#L415). References: EGA II (5.6.1), “(a); (i),(ii)”; SGA 4 XVII (7.0.6), “Noetherian base”; SGA 4 XII (7.1), “Noetherian case”; SGA 4½ Arcata (3.4.3), “Chow's lemma step”.

> **Chow's lemma over a Noetherian base.**

```lean
theorem hasDenseChowModification {X S : Scheme.{u}} (f : X ⟶ S) [IsNoetherian S]
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] :
    HasDenseChowModification f
```

## Tag 0201, a remark

[Tag 0201](https://stacks.math.columbia.edu/tag/0201) in the Stacks Project.

**`AlgebraicGeometry.isClosedImmersion_chowGraph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean#L107). The attribute's comment: “part (1): `X' ⟶ 𝐏ⁿ_S ×_S X = 𝐏ⁿ_X` is a closed immersion”.

> **The graph of a proper modification is a closed immersion.** It is proper, because the
> projection `𝐏ⁿ_S ×_S X ⟶ X` is separated and the composite is `π`, and a monomorphism, because
> the composite with the projection to `𝐏ⁿ_S` is the immersion `i`.

```lean
theorem isClosedImmersion_chowGraph (π : X' ⟶ X) (i : X' ⟶ ProjectiveSpace n S) [IsProper π]
    [IsImmersion i] (hcomm : π ≫ f = i ≫ (ProjectiveSpace n S ↘ S)) :
    IsClosedImmersion (chowGraph π i hcomm)
```

**`AlgebraicGeometry.isProjectiveMorphism_chowModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean#L130). The attribute's comment: “part (1): `π` is H-projective”.

> **The modification in Chow's lemma is H-projective.** Its graph is a closed immersion into
> the projective space `𝐏ⁿ_X` over `X`, compatibly with the structure morphism.

```lean
theorem isProjectiveMorphism_chowModification (π : X' ⟶ X) (i : X' ⟶ ProjectiveSpace n S)
    [IsProper π] [IsImmersion i] (hcomm : π ≫ f = i ≫ (ProjectiveSpace n S ↘ S)) :
    IsProjectiveMorphism π
```

**`AlgebraicGeometry.isProjective_chowModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean#L137). The attribute's comment: “part (1): `π` is projective”.

> **The modification in Chow's lemma is projective**: an H-projective morphism is projective.

```lean
theorem isProjective_chowModification (π : X' ⟶ X) (i : X' ⟶ ProjectiveSpace n S) [IsProper π]
    [IsImmersion i] (hcomm : π ≫ f = i ≫ (ProjectiveSpace n S ↘ S)) :
    IsProjective π
```

**`AlgebraicGeometry.exists_isSchemeTheoreticallyDense_chowModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean#L187). The attribute's comment: “part (2): `π⁻¹(U)` may be assumed scheme-theoretically dense in `X'`”. References: EGA II (5.6.2), “f⁻¹(U) dense in X'”.

> **In Chow's lemma the inverse image of the dense open may be assumed scheme-theoretically
> dense.** Replace `X'` by the scheme-theoretic closure of `π⁻¹(U)`; the dimension `n` of the
> ambient projective space and the dense open `U` are unchanged.

```lean
theorem exists_isSchemeTheoreticallyDense_chowModification (f : X ⟶ S) [IsNoetherian S]
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] (π : X' ⟶ X)
    (i : X' ⟶ ProjectiveSpace n S) (U : X.Opens) [IsProper π] [IsImmersion i]
    (hcomm : π ≫ f = i ≫ (ProjectiveSpace n S ↘ S)) (hU : Dense (U : Set X))
    (hiso : IsIso (π ∣_ U)) :
    ∃ (Y : Scheme.{u}) (ρ : Y ⟶ X) (j : Y ⟶ ProjectiveSpace n S),
      IsProper ρ ∧ Surjective ρ ∧ IsImmersion j ∧
        ρ ≫ f = j ≫ (ProjectiveSpace n S ↘ S) ∧ Dense (U : Set X) ∧ IsIso (ρ ∣_ U) ∧
        Scheme.Opens.IsSchemeTheoreticallyDense (ρ ⁻¹ᵁ U)
```

**`AlgebraicGeometry.exists_isReduced_chowModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ChowNoetherian/Refinements.lean#L207). The attribute's comment: “part (3): if `X` is reduced then `X'` may be chosen reduced”. References: EGA II (5.6.2), “reduced X' clause”.

> **In Chow's lemma over a reduced scheme the modification may be chosen reduced.** The
> scheme-theoretic closure of `π⁻¹(U)` has reduced source, since `π⁻¹(U) ≅ U` is an open subscheme
> of the reduced scheme `X`, and the scheme-theoretic image of a reduced scheme is reduced.

```lean
theorem exists_isReduced_chowModification (f : X ⟶ S) [IsNoetherian S] [IsSeparated f]
    [LocallyOfFiniteType f] [QuasiCompact f] [IsReduced X] (π : X' ⟶ X)
    (i : X' ⟶ ProjectiveSpace n S) (U : X.Opens) [IsProper π] [IsImmersion i]
    (hcomm : π ≫ f = i ≫ (ProjectiveSpace n S ↘ S)) (hU : Dense (U : Set X))
    (hiso : IsIso (π ∣_ U)) :
    ∃ (Y : Scheme.{u}) (ρ : Y ⟶ X) (j : Y ⟶ ProjectiveSpace n S),
      IsProper ρ ∧ Surjective ρ ∧ IsImmersion j ∧
        ρ ≫ f = j ≫ (ProjectiveSpace n S ↘ S) ∧ Dense (U : Set X) ∧ IsIso (ρ ∣_ U) ∧
        Scheme.Opens.IsSchemeTheoreticallyDense (ρ ⁻¹ᵁ U) ∧ IsReduced Y
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.18, Tag 02O2](https://stacks.math.columbia.edu/tag/02O2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
