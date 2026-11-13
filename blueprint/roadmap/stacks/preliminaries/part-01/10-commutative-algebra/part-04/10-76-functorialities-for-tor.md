---
declaration: section
origin: cited
lean: isIso_torBaseChangeComparison, tor_commutes_filtered_colimits
statement: formalized
proof: formalized
---

# 10.76 Functorialities for Tor

Section 10.76 of the Stacks Project, [Tag 00M7](https://stacks.math.columbia.edu/tag/00M7). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00M8, a lemma

[Tag 00M8](https://stacks.math.columbia.edu/tag/00M8) in the Stacks Project.

**`isIso_torBaseChangeComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/BaseChangeComparison.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/BaseChangeComparison.lean#L397).

> **Flat base change for `Tor`** (Stacks 00M8). Let `R → R'` be a flat homomorphism of
> commutative rings and let `M`, `N` be `R`-modules. Then for every `i` the natural `R'`-linear map
> `Tor_i^R(M, N) ⊗_R R' ⟶ Tor_i^{R'}(M ⊗_R R', N ⊗_R R')`, the `R'`-linear extension of the
> change-of-rings map of Stacks 00M7 (2), is an isomorphism.
>
> The map `torBaseChangeComparison` is defined for every `R → R'`, from `torBaseChangeMap`;
> flatness is used only here.

```lean
theorem isIso_torBaseChangeComparison [Module.Flat R R'] (i : ℕ) (M N : ModuleCat.{u} R) :
    IsIso (torBaseChangeComparison R' i M N)
```

## Tag 0BNF, a lemma

[Tag 0BNF](https://stacks.math.columbia.edu/tag/0BNF) in the Stacks Project.

**`tor_commutes_filtered_colimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/BaseChange.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Tor/BaseChange.lean#L439). References: EGA III (6.3.12), “special case”; EGA III (6.3.6), “special case”; EGA III (6.5.6), “special case”.

> **Tor commutes with filtered colimits.** Applying `Tor_n^R(-, N)` to the direct-limit
> colimit cocone of a directed system `(G i)` of `R`-modules yields again a colimit cocone, i.e. the
> canonical map `colim_i Tor_n^R(G i, N) → Tor_n^R(colim_i G i, N)` is an isomorphism.
>
> The ring `R : Type u`, the index type `ι : Type v`, the modules `G : ι → Type w` and the second
> argument `N : ModuleCat.{x} R` live in four independent universes, and the conclusion is stated
> about their canonical `ULift`s into `max u v w x`.

```lean
theorem tor_commutes_filtered_colimits
    {R : Type u} [CommRing R]
    {ι : Type v} [DecidableEq ι] [Preorder ι] [IsDirected ι (· ≤ ·)] [Nonempty ι]
    (G : ι → Type w) [∀ i, AddCommGroup (G i)] [∀ i, Module R (G i)]
    (f : (i j : ι) → i ≤ j → G i →ₗ[R] G j)
    [DirectedSystem G (fun i j h => f i j h)]
    (N : ModuleCat.{x} R) (n : ℕ) :
    Nonempty (CategoryTheory.Limits.IsColimit
      (((CategoryTheory.Tor (ModuleCat.{max u v w x} (ULift.{max v w x, u} R)) n).flip.obj
            (ModuleCat.of (ULift.{max v w x, u} R) (ULift.{max u v w, x} N))).mapCocone
        (ModuleCat.directLimitCocone
          (fun i : ULift.{max u w x, v} ι => ULift.{max u v x, w} (G i.down))
          (torULiftTransition.{u, v, w, x} G f))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.76, Tag 00M7](https://stacks.math.columbia.edu/tag/00M7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
