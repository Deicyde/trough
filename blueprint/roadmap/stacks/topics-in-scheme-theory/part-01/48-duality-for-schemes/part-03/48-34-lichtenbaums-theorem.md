---
declaration: section
origin: cited
lean: Stacks.Duality.Lichtenbaum.le_topologicalKrullDim_and_isProper_of_not_isZero_rightDerived, Stacks.Duality.Lichtenbaum.tfae_isZero_cohomologyOverField
statement: formalized
proof: formalized
---

# 48.34 Lichtenbaum's theorem

Section 48.34 of the Stacks Project, [Tag 0G5D](https://stacks.math.columbia.edu/tag/0G5D). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G5E, a lemma

[Tag 0G5E](https://stacks.math.columbia.edu/tag/0G5E) in the Stacks Project.

**`Stacks.Duality.Lichtenbaum.le_topologicalKrullDim_and_isProper_of_not_isZero_rightDerived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Lichtenbaum/VarietyTopCohomology.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/Lichtenbaum/VarietyTopCohomology.lean#L212).

> **[Stacks, Tag 0G5E].** Let `U` be a variety over a field `k` and let `F` be a coherent
> `𝒪_U`-module. If `H^d(U, F)` is nonzero, then `dim(U) ≥ d`, and if equality holds, then `U` is
> proper over `k`.
>
> Here `H^d(U, F)` is the `d`-th right derived functor of global sections on `Mod(𝒪_U)`, and
> `dim(U)` is the topological Krull dimension. The proof is the source's. The bound is
> Grothendieck's vanishing theorem ([Stacks, Tag 02UZ]). If `dim U = d`, choose an integral scheme
> `X` proper over `k` containing `U` as an open subscheme ([Stacks, Tag 0F41],
> [Stacks, Tag 0A9Z]); then `dim X = d`, and if `U` is not proper then `U ≠ X`, so
> `H^d(U, F) = 0` by duality ([Stacks, Tag 0G5A]) and the vanishing of
> `H^{-d}_c(U, R𝓗om(F, ω_U^•))`
> (`Stacks.Duality.Lichtenbaum.isZero_rightDerived_of_nonempty_compl`).

```lean
theorem le_topologicalKrullDim_and_isProper_of_not_isZero_rightDerived (k : Type u) [Field k]
    {U : Scheme.{u}} (f : U ⟶ Spec (.of k)) [IsVariety k f] (F : U.Modules) [F.IsCoherent]
    (d : ℕ) (h : ¬ IsZero (((moduleGlobalSections U).rightDerived d).obj F)) :
    (d : WithBot ℕ∞) ≤ topologicalKrullDim U ∧ (topologicalKrullDim U = d → IsProper f)
```

## Tag 0G5F, a theorem

[Tag 0G5F](https://stacks.math.columbia.edu/tag/0G5F) in the Stacks Project.

**`Stacks.Duality.Lichtenbaum.tfae_isZero_cohomologyOverField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/Lichtenbaum/Theorem.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/Lichtenbaum/Theorem.lean#L107).

> **[Stacks, Tag 0G5F].** Let `X` be a separated scheme of finite type over a field `k`, of
> dimension `d` (so `X` is nonempty). The following are equivalent:
>
> 1. `H^d(X, F) = 0` for all coherent `𝒪_X`-modules `F`,
> 2. `H^d(X, F) = 0` for all quasi-coherent `𝒪_X`-modules `F`, and
> 3. no irreducible component `X' ⊆ X` of dimension `d`, viewed as an integral closed subscheme
>    through its reduced induced structure, is proper over `k`.
>
> Here `H^d(X, F)` is the `k`-vector space `AlgebraicGeometry.cohomologyOverField k f F d`.

```lean
theorem tfae_isZero_cohomologyOverField (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f] (d : ℕ)
    (hd : topologicalKrullDim X = d) :
    List.TFAE
      [∀ (F : X.Modules) [F.IsCoherent], IsZero (cohomologyOverField k f F d),
       ∀ (F : X.Modules) [F.IsQuasicoherent], IsZero (cohomologyOverField k f F d),
       ∀ Z : irreducibleComponents X,
        let C := Scheme.IdealSheafData.vanishingIdeal (X := X)
          ⟨Z.1, isClosed_of_mem_irreducibleComponents Z.1 Z.2⟩
        topologicalKrullDim C.subscheme = d → ¬ IsProper (C.subschemeι ≫ f)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.34, Tag 0G5D](https://stacks.math.columbia.edu/tag/0G5D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
