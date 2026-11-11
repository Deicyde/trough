---
declaration: section
origin: cited
lean: flat_base_change_ext
statement: formalized
proof: formalized
---

# 10.73 Functorialities for Ext

Section 10.73 of the Stacks Project, [Tag 087M](https://stacks.math.columbia.edu/tag/087M). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 087N, a lemma

[Tag 087N](https://stacks.math.columbia.edu/tag/087N) in the Stacks Project.

**`flat_base_change_ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ext/BaseChange.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ext/BaseChange.lean#L203).

> **Flat base change for Ext.**
> For a flat ring map `f : R → R'`, an `R`-module `M`, an `R'`-module `N'`, and
> each `i ≥ 0`, the comparison map `c^i` of `extFlatBaseChangeComparison` is an
> isomorphism of abelian groups (here phrased as bijectivity of the underlying
> group homomorphism).

```lean
theorem flat_base_change_ext {R R' : Type} [CommRing R] [CommRing R']
    (f : R →+* R') (hf : f.Flat) (M : ModuleCat.{0} R) (N' : ModuleCat.{0} R') (i : ℕ) :
    Function.Bijective (extFlatBaseChangeComparison f M N' i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.73, Tag 087M](https://stacks.math.columbia.edu/tag/087M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
