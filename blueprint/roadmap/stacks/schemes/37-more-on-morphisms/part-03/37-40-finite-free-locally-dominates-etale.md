---
declaration: section
origin: cited
lean: Stacks.Topologies.Etale.exists_isFiniteLocallyFree_surjective_locally_lift_etaleNeighborhood, Stacks.Topologies.Etale.exists_isFiniteLocallyFree_surjective_finite_openCover_lift, Stacks.Topologies.Etale.exists_zariski_finiteLocallyFree_refinement
statement: formalized
proof: formalized
---

# 37.40 Finite free locally dominates étale

Section 37.40 of the Stacks Project, [Tag 04HE](https://stacks.math.columbia.edu/tag/04HE). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02LG, a lemma

[Tag 02LG](https://stacks.math.columbia.edu/tag/02LG) in the Stacks Project.

**`Stacks.Topologies.Etale.exists_isFiniteLocallyFree_surjective_locally_lift_etaleNeighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/FiniteFreeDominationNeighborhood.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/FiniteFreeDominationNeighborhood.lean#L238).

> **Stacks Project, Tag 02LG.** After restricting the base to an affine open neighbourhood of
> the point, an étale neighbourhood is locally dominated, at every point above the distinguished
> point, by a surjective finite locally free morphism.

```lean
theorem exists_isFiniteLocallyFree_surjective_locally_lift_etaleNeighborhood
    {S : Scheme.{u}} {s : S} (U : EtaleNeighborhood S s) :
    ∃ (V : S.affineOpens) (hs : s ∈ V.1) (T : Scheme.{u}) (π : T ⟶ V.1)
      (_ : Surjective π) (_ : Stacks.Morphisms.IsFiniteLocallyFree π),
      ∀ (t : T) (_ : π t = ⟨s, hs⟩),
        ∃ (W : T.Opens) (ht : t ∈ W) (h : (W : Scheme.{u}) ⟶ U.scheme),
          W.ι ≫ π ≫ V.1.ι = h ≫ U.toBase ∧ h ⟨t, ht⟩ = U.point
```

## Tag 02LH, a lemma

[Tag 02LH](https://stacks.math.columbia.edu/tag/02LH) in the Stacks Project.

**`Stacks.Topologies.Etale.exists_isFiniteLocallyFree_surjective_finite_openCover_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/FiniteFreeDominationAffine.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/FiniteFreeDominationAffine.lean#L103).

> **Stacks Project, Tag 02LH.** A surjective étale morphism of affine schemes is dominated
> by a surjective finite locally free morphism whose source has a finite open covering lifting
> to the given étale cover.

```lean
theorem exists_isFiniteLocallyFree_surjective_finite_openCover_lift
    {U S : Scheme.{u}} [IsAffine U] [IsAffine S] (f : U ⟶ S) [Etale f] [Surjective f] :
    ∃ (T : Scheme.{u}) (p : T ⟶ S),
      Stacks.Morphisms.IsFiniteLocallyFree p ∧ Surjective p ∧
        ∃ 𝒯 : T.OpenCover.{u}, Finite 𝒯.I₀ ∧
          ∃ g : ∀ i, 𝒯.X i ⟶ U, ∀ i, 𝒯.f i ≫ p = g i ≫ f
```

## Tag 02LI, a remark

[Tag 02LI](https://stacks.math.columbia.edu/tag/02LI) in the Stacks Project.

**`Stacks.Topologies.Etale.exists_zariski_finiteLocallyFree_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/FiniteFreeDomination.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/FiniteFreeDomination.lean#L168).

> An étale covering is refined, after a Zariski covering of the base, by Zariski coverings of
> schemes which are finite locally free and surjective over the corresponding members of the base
> covering.

```lean
theorem exists_zariski_finiteLocallyFree_refinement {S : Scheme.{u}}
    (E : PreZeroHypercover.{w} S) (hE : E.presieve₀ ∈ Scheme.etalePrecoverage S) :
    ∃ (V : S.OpenCover.{u}) (W : V.I₀ → Scheme.{u}) (p : ∀ j, W j ⟶ V.X j),
      (∀ j, Stacks.Morphisms.IsFiniteLocallyFree (p j)) ∧
        (∀ j, Surjective (p j)) ∧
          ∃ U : ∀ j, (W j).OpenCover.{u},
            Nonempty
              ((V.toPreZeroHypercover.bind fun j ↦
                (U j).toPreZeroHypercover.pushforward (p j)).Hom E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.40, Tag 04HE](https://stacks.math.columbia.edu/tag/04HE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
