---
declaration: section
origin: cited
lean: CategoryTheory.ShortComplex.shortExact_map_lim_of_isMittagLeffler
statement: formalized
proof: formalized
---

# 10.87 Inverse systems

Section 10.87 of the Stacks Project, [Tag 03C9](https://stacks.math.columbia.edu/tag/03C9). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03CA, a lemma

[Tag 03CA](https://stacks.math.columbia.edu/tag/03CA) in the Stacks Project.

**`CategoryTheory.ShortComplex.shortExact_map_lim_of_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/ShortComplex/InverseLimit.lean#L252). References: EGA 0 (13.2.2), “ℕ-indexed systems”; EGA III (4.1.7.21), “more general”.

> **Stacks 03CA.** Let `R` be a ring and let `S` be a short complex of towers of `R`-modules,
> that is of functors `ℕᵒᵖ ⥤ ModuleCat R`, which is short exact at every index: for each `i` the
> sequence `0 → S.X₁ i → S.X₂ i → S.X₃ i → 0` is short exact. If the tower `S.X₁` satisfies the
> Mittag-Leffler condition, that is for every `i` there is a `c ≥ i` with
> `Im(S.X₁ c → S.X₁ i) = Im(S.X₁ j → S.X₁ i)` for all `j ≥ c`, then the sequence of inverse limits
> `0 → lim S.X₁ → lim S.X₂ → lim S.X₃ → 0` is short exact.

```lean
public theorem shortExact_map_lim_of_isMittagLeffler {R : Type u} [Ring R]
    (S : ShortComplex (ℕᵒᵖ ⥤ ModuleCat.{v} R))
    (hS : ∀ n : ℕᵒᵖ, (S.map ((evaluation ℕᵒᵖ (ModuleCat.{v} R)).obj n)).ShortExact)
    (hML : (S.X₁ ⋙ forget (ModuleCat.{v} R)).IsMittagLeffler) :
    (S.map (lim : (ℕᵒᵖ ⥤ ModuleCat.{v} R) ⥤ ModuleCat.{v} R)).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.87, Tag 03C9](https://stacks.math.columbia.edu/tag/03C9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
