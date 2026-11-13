---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidScheme.isOpenImmersion_restrictionQuotientMap_of_open_image
statement: formalized
proof: formalized
---

# 80.7 Finding opens

Section 80.7 of the Stacks Project, [Tag 04S2](https://stacks.math.columbia.edu/tag/04S2). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 046M, a lemma

[Tag 046M](https://stacks.math.columbia.edu/tag/046M) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.isOpenImmersion_restrictionQuotientMap_of_open_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/QuotientSheaf/OpenSaturation.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/QuotientSheaf/OpenSaturation.lean#L386).

> **Stacks 046M.** Let `G` be a groupoid scheme over `S` and let `g : U' ⟶ U` be a morphism
> to its scheme of objects whose saturation is the range of an open immersion `i : W ⟶ U`. If
> the reach map factors as `k ≫ i` with `k` inducing a surjection of fppf sheaves, then the map
> of quotient sheaves `U'/R' ⟶ U/R` induced by the restriction of `G` along `g` is a
> representable open immersion.

```lean
theorem isOpenImmersion_restrictionQuotientMap_of_open_image
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (G : GroupoidScheme S) {U' W : Over S}
    (g : U' ⟶ G.objects) (i : W ⟶ G.objects)
    [IsOpenImmersion i.left]
    (k : pullback g G.target ⟶ W)
    (hk : k ≫ i = restrictionReachMap G g)
    (himage : Set.range i.left.base =
      Set.range (restrictionReachMap G g).left.base)
    (hsurj : Sheaf.IsLocallySurjective
      ((presheafToSheaf (BigFppfOver.topology B S hS) (Type u)).map
        ((Over.post B.inclusion).op.whiskerLeft (yoneda.map k)))) :
    Space.IsOpenImmersion B S hS
      (restrictionQuotientMap (BigFppfOver.topology B S hS) (Over.post B.inclusion) G g
        (restrict G g)).1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.7, Tag 04S2](https://stacks.math.columbia.edu/tag/04S2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
