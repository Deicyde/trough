---
declaration: section
origin: cited
lean: flat_base_change_tor, flat_base_change_tor_of_universe, tor_commutes_filtered_colimits
statement: formalized
proof: formalized
---

# 10.76 Functorialities for Tor

Section 10.76 of the Stacks Project, [Tag 00M7](https://stacks.math.columbia.edu/tag/00M7). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00M8, a lemma

[Tag 00M8](https://stacks.math.columbia.edu/tag/00M8) in the Stacks Project.

**`flat_base_change_tor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/BaseChange.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/BaseChange.lean#L172).

> **Flat base change for Tor.** Let `R → R'` be a flat ring map of commutative rings and let
> `M`, `N` be `R`-modules. Then for every `i` the base-change map
> `(torBaseChangeIso i M N).hom : Tor_i^R(M, N) ⊗_R R' ⟶ Tor_i^{R'}(M ⊗_R R', N ⊗_R R')`
> is an isomorphism of `R'`-modules.

```lean
theorem flat_base_change_tor [Module.Flat R R'] (i : ℕ) (M N : ModuleCat.{0} R) :
    IsIso (torBaseChangeIso (R' := R') i M N).hom
```

**`flat_base_change_tor_of_universe`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/BaseChangeOfUniverse.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/BaseChangeOfUniverse.lean#L132).

> **Flat base change for Tor** (Stacks Tag `00M8`), for rings in an arbitrary universe.
>
> Let `S -> S'` be a flat ring map of commutative rings (encoded as an `S`-algebra `S'` with
> `Module.Flat S S'`), and let `M`, `N` be `S`-modules. Then for every `i` the canonical
> base-change map `Tor_i^S(M, N) (x)_S S' -> Tor_i^{S'}(M (x)_S S', N (x)_S S')` — the underlying
> morphism `(torBaseChangeIsoOfUniverse i M N).hom` of the comparison — is an isomorphism of
> `S'`-modules.

```lean
theorem flat_base_change_tor_of_universe [Module.Flat S S'] (i : ℕ) (M N : ModuleCat.{u} S) :
    IsIso (torBaseChangeIsoOfUniverse (S' := S') i M N).hom
```

## Tag 0BNF, a lemma

[Tag 0BNF](https://stacks.math.columbia.edu/tag/0BNF) in the Stacks Project.

**`tor_commutes_filtered_colimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/BaseChange.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/BaseChange.lean#L438). References: EGA III (6.3.12), “special case”; EGA III (6.3.6), “special case”; EGA III (6.5.6), “special case”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
