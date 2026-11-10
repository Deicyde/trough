---
declaration: section
origin: cited
lean: Stacks.Cohomology.CompactObjects.isCompactObject_jShriek_structureSheaf, Stacks.Cohomology.RingedSpaceCompact.isCompactObject_of_isPerfect_of_finiteCohomDim, Stacks.Cohomology.RingedSpaceCompact.hom_coproduct_bijective_of_isPerfect_of_compactSpace
statement: formalized
proof: formalized
---

# 20.53 Compact objects

Section 20.53 of the Stacks Project, [Tag 09J6](https://stacks.math.columbia.edu/tag/09J6). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F5Z, a lemma

[Tag 0F5Z](https://stacks.math.columbia.edu/tag/0F5Z) in the Stacks Project.

**`Stacks.Cohomology.CompactObjects.isCompactObject_jShriek_structureSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/CompactObjectExtensionByZero.lean, line 576](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/RecoveryB/CompactObjectExtensionByZero.lean#L576).

> Finite cohomological dimension and commutation of cohomology with direct sums make
> `j_! 𝒪_U` compact in the unbounded derived category of `𝒪_X`-modules.

```lean
public theorem isCompactObject_jShriek_structureSheaf
    (X : SheafedSpace.{u + 1, u, u} RingCat.{u}) (U : Opens X.carrier)
    (d : ℤ)
    (hvanish : ∀ (p : ℕ) (M : SheafOfModules.{u} (OXSh X)),
      d < (p : ℤ) →
        IsZero (((SheafOfModules.evaluation (OXSh X) (op U)).rightDerived p).obj M))
    (hsums : ∀ (p : ℕ) (I : Type u),
      PreservesColimitsOfShape (Discrete I)
        ((SheafOfModules.evaluation (OXSh X) (op U)).rightDerived p)) :
    IsCompactObject.{u}
      ((DerivedCategory.singleFunctor (SheafOfModules.{u} (OXSh X)) 0).obj
        ((jShriek00A7 X U).obj (SheafOfModules.unit (OUSh X U))))
```

## Tag 09J7, a lemma

[Tag 09J7](https://stacks.math.columbia.edu/tag/09J7) in the Stacks Project.

**`Stacks.Cohomology.RingedSpaceCompact.isCompactObject_of_isPerfect_of_finiteCohomDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnARingedSpaceUnconditional.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnARingedSpaceUnconditional.lean#L135). The attribute's comment: “(b): on a ringed space satisfying (1), (2) and (3) and of finite cohomological dimension, a perfect object is a compact object of D(O\_X)”.

> **Stacks 09J7 (b).** Let `X` be a ringed space whose underlying topological
> space is quasi-compact, has a basis of quasi-compact opens, and has quasi-compact intersections
> of quasi-compact opens — hypotheses (1), (2) and (3) of the tag. Let `K` be a perfect object of
> `D(O_X)` and suppose `X` has finite cohomological dimension, that is `Hᵖ(X, F) = 0` for every
> `O_X`-module `F` and every `p` beyond a fixed bound `d`. Then `K` is a compact object of
> `D(O_X)`.
>
> The reduction the source performs first — by Stacks 08DQ morphisms out of
> `K` are morphisms out of `j_{X!}O_X` after applying `K^∨ ⊗^L_{O_X} -`, a functor commuting with
> direct sums — is
> `AlgebraicGeometry.RingedSite.derivedDualHomEquivOfIsoStructureSheaf` together with
> `AlgebraicGeometry.RingedSite.preservesColimitsOfShape_derivedTensorFlip`, and it is applied at
> the final object `⊤` of the site of opens. The three topological conditions enter through
> Stacks 01FF: they make the cohomology functors `F ↦ Hᵖ(X, F)` commute
> with arbitrary direct sums, which with the dimension bound is what Stacks 094D consumes.

```lean
theorem isCompactObject_of_isPerfect_of_finiteCohomDim [CompactSpace X.carrier]
    (hBasis : PrespectralSpace X.carrier)
    (hInter : QuasiSeparatedSpace X.carrier)
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (RingedSpace.ringedSite X).O)))
    (hK : (RingedSpace.ringedSite X).IsPerfect K)
    (hcd : ∃ d : ℤ, ∀ (p : ℕ) (F : _root_.SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf (RingedSpace.ringedSite X).O)),
      d < (p : ℤ) → IsZero (Hgroup
        (Stacks.SheafOfModules.Tensor.ringSheaf (RingedSpace.ringedSite X).O) ⊤ p F)) :
    IsCompactObject.{u} K
```

**`Stacks.Cohomology.RingedSpaceCompact.hom_coproduct_bijective_of_isPerfect_of_compactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnARingedSpaceUnconditional.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/CompactObjects/PerfectObjectsOnARingedSpaceUnconditional.lean#L221). The attribute's comment: “(a): on a ringed space satisfying (1), (2) and (3), a perfect object K satisfies Hom(K, ⨁ M\_i) = ⨁ Hom(K, M\_i) whenever ⨁ M\_i is bounded below”.

> **Stacks 09J7 (a).** Let `X` be a ringed space whose underlying topological
> space is quasi-compact, has a basis of quasi-compact opens, and has quasi-compact intersections
> of quasi-compact opens — hypotheses (1), (2) and (3) of the tag. Let `K` be a perfect object of
> `D(O_X)` and let `M : I → D(O_X)` be a family whose coproduct is bounded below. Then
> `Hom(K, ⨁ Mᵢ) = ⨁ Hom(K, Mᵢ)`: the canonical map from the direct sum of the `Hom(K, Mᵢ)` is
> bijective.
>
> The proof applies `hom_coproduct_bijective_of_isPerfect_of_hasFiniteTorDimension`; the finite
> Tor dimension of `K^∨` is the global form of Stacks 08G8,
> `Stacks.Cohomology.TorAmplitude.hasFiniteTorDimension_of_ringedSite_isPerfect`, applied to the
> dual `K^∨`, which is perfect by Stacks 08JJ
> (`AlgebraicGeometry.RingedSite.isPerfect_derivedDual`): perfectness gives the Tor amplitude of
> `K^∨` only locally, quasi-compactness makes the local intervals one interval, and the bridge
> `Stacks.Cohomology.TorAmplitude.hasTorAmplitude_iff_derivedTensorProduct` reads that interval
> against the derived tensor product datum the reduction measures Tor dimension by.
>
> The index type lies in the universe of the space, as for clause (b).

```lean
theorem hom_coproduct_bijective_of_isPerfect_of_compactSpace [CompactSpace X.carrier]
    (hBasis : PrespectralSpace X.carrier)
    (hInter : QuasiSeparatedSpace X.carrier)
    (K : DerivedCategory (_root_.SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (RingedSpace.ringedSite X).O)))
    (hK : (RingedSpace.ringedSite X).IsPerfect K)
    {I : Type u} [DecidableEq I]
    (M : I → DerivedCategory (_root_.SheafOfModules.{u}
      (Stacks.SheafOfModules.Tensor.ringSheaf (RingedSpace.ringedSite X).O))) [HasCoproduct M]
    (hplus : DerivedCategoryB.IsBoundedBelow (∐ M)) :
    Function.Bijective
      (DirectSum.toAddMonoid fun j => Preadditive.rightComp K (Limits.Sigma.ι M j))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.53, Tag 09J6](https://stacks.math.columbia.edu/tag/09J6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
