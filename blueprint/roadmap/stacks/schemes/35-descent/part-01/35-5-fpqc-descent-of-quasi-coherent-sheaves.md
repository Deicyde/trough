---
declaration: section
origin: cited
lean: AlgebraicGeometry.QuasicoherentDescentData.nonempty_fullyFaithful_canonicalDescentFunctor_standardFpqc, AlgebraicGeometry.QuasicoherentDescentData.isEffective_standardFpqc_of_isAffine, AlgebraicGeometry.nonempty_fullyFaithful_canonicalDescentFunctor', AlgebraicGeometry.QuasicoherentDescentData.isEffective_fpqcPrecoverage, AlgebraicGeometry.QuasicoherentDescentData.isEquivalence_canonicalDescentFunctor_fpqc
statement: formalized
proof: formalized
---

# 35.5 Fpqc descent of quasi-coherent sheaves

Section 35.5 of the Stacks Project, [Tag 023R](https://stacks.math.columbia.edu/tag/023R). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 023S, a lemma

[Tag 023S](https://stacks.math.columbia.edu/tag/023S) in the Stacks Project.

**`AlgebraicGeometry.QuasicoherentDescentData.nonempty_fullyFaithful_canonicalDescentFunctor_standardFpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/StandardFpqc023S.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/StandardFpqc023S.lean#L224). The attribute's comment: “full faithfulness”. References: SGA 1 VIII (1.1), “standard affine case”.

> **The full faithfulness half of [Stacks, Tag 023S]**: let `S` be an affine scheme and let
> `{f i : X i ⟶ S}` be a standard fpqc covering of `S` in the sense of Stacks 022F.  Then the
> functor from quasi-coherent `O_S`-modules to quasi-coherent descent data for the family is fully
> faithful.
>
> The content is the unconditional
> `…QuasicoherentDescentData.nonempty_fullyFaithful_canonicalDescentFunctor_of_mem_fpqcPrecoverage`,
> which holds for an arbitrary fpqc covering family of an arbitrary scheme; all that is done here
> is to supply the covering hypothesis in the elementary form in which Stacks 022F states it, by
> `AlgebraicGeometry.QuasicoherentDescentData.presieve₀_mem_fpqcPrecoverage_standardFpqc`.

```lean
theorem nonempty_fullyFaithful_canonicalDescentFunctor_standardFpqc
    (𝒲 : PreZeroHypercover.{0} S) [Finite 𝒲.I₀] [∀ i, IsAffine (𝒲.X i)] [∀ i, Flat (𝒲.f i)]
    (hsurj : ⋃ i, Set.range (𝒲.f i) = Set.univ) :
    Nonempty (canonicalDescentFunctor 𝒲.f).FullyFaithful
```

**`AlgebraicGeometry.QuasicoherentDescentData.isEffective_standardFpqc_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/StandardFpqc023S.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/StandardFpqc023S.lean#L245). The attribute's comment: “effectivity”. References: SGA 1 VIII (1.1), “standard affine case”; SGA 1 VIII (1.3), “Cor. 1.3, special case”.

> **The effectivity half of [Stacks, Tag 023S]**: let `S` be an affine scheme and let
> `{f i : X i ⟶ S}` be a standard fpqc covering of `S` in the sense of Stacks 022F — a finite
> family of flat morphisms from affine schemes whose images cover `S`.  Then every quasi-coherent
> descent datum for the family is effective, i.e. isomorphic to the canonical descent datum of a
> quasi-coherent module on `S`.
>
> This is `AlgebraicGeometry.QuasicoherentDescentData.isEffective_standardFpqc`, whose base is
> literally of the form `Spec R`, transported to an arbitrary affine base along
> `AlgebraicGeometry.Scheme.isoSpec`.  The transport runs in the vocabulary of
> `Stacks.Descent.qcohPseudofunctor`, where `Stacks.Descent.essSurj_toDescentData_of_baseIso` is
> available; see the implementation notes of this file.

```lean
theorem isEffective_standardFpqc_of_isAffine (𝒲 : PreZeroHypercover.{0} S) [Finite 𝒲.I₀]
    [∀ i, IsAffine (𝒲.X i)] [∀ i, Flat (𝒲.f i)]
    (hsurj : ⋃ i, Set.range (𝒲.f i) = Set.univ)
    (D : QuasicoherentDescentData 𝒲.f) : D.IsEffective
```

## Tag 023T, a proposition

[Tag 023T](https://stacks.math.columbia.edu/tag/023T) in the Stacks Project.

**`AlgebraicGeometry.nonempty_fullyFaithful_canonicalDescentFunctor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/FpqcHomSheafRefinement.lean#L353). The attribute's comment: “the `moreover` assertion, full faithfulness”. References: SGA 1 VIII (1.1), “full faithfulness”.

> For every fpqc covering family the functor from the quasi-coherent `𝒪_S`-modules to the
> descent data with respect to that family is fully faithful.

```lean
theorem nonempty_fullyFaithful_canonicalDescentFunctor' {I : Type (u + 1)}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hfpqc : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage.{u} S) :
    Nonempty (canonicalDescentFunctor f).FullyFaithful
```

**`AlgebraicGeometry.QuasicoherentDescentData.isEffective_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/FpqcEffectiveUnconditional.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/FpqcEffectiveUnconditional.lean#L43). The attribute's comment: “effectivity, arbitrary fpqc covering family”. References: SGA 1 VIII (1.1), “effectivity”; SGA 4½ Arcata (1.4), “fpqc qcoh case”.

> Every quasi-coherent descent datum for an fpqc covering family of an arbitrary scheme is
> effective, at an arbitrary index universe.

```lean
theorem isEffective_fpqcPrecoverage {S : Scheme.{u}} (𝒰 : PreZeroHypercover.{v} S)
    (h𝒰 : 𝒰.presieve₀ ∈ Scheme.fpqcPrecoverage.{u} S) (D : QuasicoherentDescentData 𝒰.f) :
    D.IsEffective
```

**`AlgebraicGeometry.QuasicoherentDescentData.isEquivalence_canonicalDescentFunctor_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/FpqcEffectiveUnconditional.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/FpqcEffectiveUnconditional.lean#L55). The attribute's comment: “both assertions in one statement: the canonical descent functor is an equivalence. The index universe is u + 1, fixed by the full-faithfulness half nonempty_fullyFaithful_canonicalDescentFunctor'; effectivity on its own is isEffective_fpqcPrecoverage above, at an arbitrary index universe”.

> For an fpqc covering family of a scheme `S`, indexed in `Type (u + 1)`, the canonical descent
> functor from the quasi-coherent `𝒪_S`-modules to the descent data with respect to that family is an
> equivalence of categories.

```lean
theorem isEquivalence_canonicalDescentFunctor_fpqc {S : Scheme.{u}} {I : Type (u + 1)}
    {X : I → Scheme.{u}} (f : ∀ i, X i ⟶ S)
    (hfpqc : Presieve.ofArrows X f ∈ Scheme.fpqcPrecoverage.{u} S) :
    (canonicalDescentFunctor f).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.5, Tag 023R](https://stacks.math.columbia.edu/tag/023R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
