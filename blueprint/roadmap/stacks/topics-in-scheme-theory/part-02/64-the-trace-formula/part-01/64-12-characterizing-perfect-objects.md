---
declaration: section
origin: cited
lean: StacksDraft.Perfect.HasFiniteTorDimensionCanonical, StacksDraft.Perfect.HasFiniteTorDimension, StacksDraft.Perfect.isPerfect_iff_hasFiniteTorDimension_balancedDerivedTensoring, StacksDraft.Perfect.isPerfect_iff_hasFiniteTorDimension_and_finite_homology
statement: formalized
proof: formalized
---

# 64.12 Characterizing perfect objects

Section 64.12 of the Stacks Project, [Tag 03TM](https://stacks.math.columbia.edu/tag/03TM). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03TN, a definition

[Tag 03TN](https://stacks.math.columbia.edu/tag/03TN) in the Stacks Project.

**`StacksDraft.Perfect.HasFiniteTorDimensionCanonical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean, line 764](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean#L764). References: SGA 4½ Rapport (4.5), “finite tor dimension”.

> An object `K` of `D(Λ)` has *finite Tor dimension* if there are integers `a, b` such that
> `Hⁱ(N ⊗ᴸ[Λ] K) = 0` for every right `Λ`-module `N` and every `i ∉ [a, b]`. This is the definition
> at the balanced derived tensor product constructed here, so it takes no parameter; by
> `hasFiniteTorDimensionCanonical_iff` it is the same condition as
> `StacksDraft.Perfect.HasFiniteTorDimension` at any term of `BalancedDerivedTensoring Λ`.

```lean
def HasFiniteTorDimensionCanonical [Small.{v} Λ] (K : DerivedCategory (ModuleCat.{v} Λ)) : Prop
```

**`StacksDraft.Perfect.HasFiniteTorDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/FiniteTorDimension.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/FiniteTorDimension.lean#L109). References: SGA 4½ Rapport (4.5), “finite tor dimension”.

> An object `K` of `D(Λ)` has *finite Tor dimension* if there are integers `a, b` such that
> `Hⁱ(N ⊗ᴸ[Λ] K) = 0` for every right `Λ`-module `N` and every `i ∉ [a, b]`.

```lean
def HasFiniteTorDimension {Λ : Type u} [Ring Λ] (D : BalancedDerivedTensoring.{u, v} Λ)
    (K : DerivedCategory (ModuleCat.{v} Λ)) : Prop
```

## Tag 03TO, a lemma

[Tag 03TO](https://stacks.math.columbia.edu/tag/03TO) in the Stacks Project.

**`StacksDraft.Perfect.isPerfect_iff_hasFiniteTorDimension_balancedDerivedTensoring`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean, line 779](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/BalancedDerivedTensor.lean#L779). References: SGA 5 VIII (8.1), “Noetherian case”; SGA 4½ Rapport (4.5.1).

> Let `Λ` be a left Noetherian ring and let `K` be an object of `D(Λ)`. Then `K` is perfect if
> and only if `K` has finite Tor dimension and `Hⁱ(K)` is a finite `Λ`-module for every `i`. This is
> `StacksDraft.Perfect.isPerfect_iff_hasFiniteTorDimension_and_finite_homology` with its parameter
> supplied by `balancedDerivedTensoring`, so no datum is assumed.

```lean
theorem isPerfect_iff_hasFiniteTorDimension_balancedDerivedTensoring
    [IsNoetherianRing Λ] [Small.{v} Λ] (K : DerivedCategory (ModuleCat.{v} Λ)) :
    IsPerfect K ↔
      (HasFiniteTorDimensionCanonical Λ K ∧
        ∀ i : ℤ,
          Module.Finite Λ ((DerivedCategory.homologyFunctor (ModuleCat.{v} Λ) i).obj K))
```

**`StacksDraft.Perfect.isPerfect_iff_hasFiniteTorDimension_and_finite_homology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/FiniteTorDimension.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/FiniteTorDimension.lean#L707). References: SGA 5 VIII (8.1), “Noetherian case”; SGA 4½ Rapport (4.5.1).

> Let `Λ` be a left Noetherian ring and let `K` be an object of `D(Λ)`. Then `K` is perfect if
> and only if `K` has finite Tor dimension and `Hⁱ(K)` is a finite `Λ`-module for every `i`.

```lean
theorem isPerfect_iff_hasFiniteTorDimension_and_finite_homology
    {Λ : Type u} [Ring Λ] [IsNoetherianRing Λ] [Small.{v} Λ]
    (D : BalancedDerivedTensoring.{u, v} Λ) (K : DerivedCategory (ModuleCat.{v} Λ)) :
    IsPerfect K ↔
      (HasFiniteTorDimension D K ∧
        ∀ i : ℤ,
          Module.Finite Λ ((DerivedCategory.homologyFunctor (ModuleCat.{v} Λ) i).obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.12, Tag 03TM](https://stacks.math.columbia.edu/tag/03TM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
