---
declaration: section
origin: cited
lean: extendScalarsExtComparison_bijective
statement: formalized
proof: formalized
---

# 10.73 Functorialities for Ext

Section 10.73 of the Stacks Project, [Tag 087M](https://stacks.math.columbia.edu/tag/087M). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 087N, a lemma

[Tag 087N](https://stacks.math.columbia.edu/tag/087N) in the Stacks Project.

**`extendScalarsExtComparison_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ext/BaseChange.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ext/BaseChange.lean#L386).

> **Flat base change for Ext.**
> For a flat ring map `f : R → R'`, an `R`-module `M`, an `R'`-module `N'`, and
> each `i ≥ 0`, the comparison map `c^i` of `extendScalarsExtComparison` is an
> isomorphism of abelian groups (here phrased as bijectivity of the underlying
> group homomorphism).
>
> The rings are arbitrary, in independent universes `uR` and `uS`; the modules live in
> `ModuleCat.{max uS v}` for any `v`, and `R` is assumed `Small.{max uS v}`, which holds whenever
> the module universe contains `R`. These are the constraints under which Mathlib's
> scalar-extension adjunction relates module categories of one size and provides `Ext` with enough
> projectives; see the module docstring.

```lean
theorem extendScalarsExtComparison_bijective {R : Type uR} {R' : Type uS}
    [CommRing R] [CommRing R'] [Small.{max uS v} R]
    (f : R →+* R') (hf : f.Flat) (M : ModuleCat.{max uS v} R) (N' : ModuleCat.{max uS v} R')
    (i : ℕ) :
    Function.Bijective (extendScalarsExtComparison f M N' i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.73, Tag 087M](https://stacks.math.columbia.edu/tag/087M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
