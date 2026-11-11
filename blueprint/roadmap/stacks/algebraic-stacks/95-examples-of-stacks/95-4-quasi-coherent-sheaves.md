---
declaration: section
origin: cited
lean: Stacks.QCoh.exists_categoryData, Stacks.QCoh.homEquivPullbackHom, Stacks.QCoh.isStronglyCartesian_iff, Stacks.QCoh.projection_isFibered, Stacks.QCoh.projection_isStack
statement: formalized
proof: formalized
---

# 95.4 Quasi-coherent sheaves

Section 95.4 of the Stacks Project, [Tag 03YL](https://stacks.math.columbia.edu/tag/03YL). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04U2, an equation

[Tag 04U2](https://stacks.math.columbia.edu/tag/04U2) in the Stacks Project.

**`Stacks.QCoh.exists_categoryData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Basic.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Basic.lean#L177). The attribute's comment: “quasi-coherent category and f-map homs”.

> **Stacks 04U2.** The category of quasi-coherent pairs over `S` exists together with its
> projection to the big fppf slice, and its morphisms are exactly the pairs of a morphism of
> schemes over `S` and an `f`-map of modules. The description of a hom-set as a disjoint union
> of pullback homs then follows by the pullback–pushforward adjunction.

```lean
public theorem exists_categoryData : Nonempty (CategoryData B S hS)
```

**`Stacks.QCoh.homEquivPullbackHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Basic.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Basic.lean#L209). The attribute's comment: “pullback hom equation”.

> **Stacks 04U2.** A hom-set of the category of quasi-coherent pairs is the disjoint union,
> over the morphisms `f` of the base, of the morphisms from the pullback of the target module
> along `f` to the source module.

```lean
public noncomputable def homEquivPullbackHom (A C : Object B S hS) :
    (A ⟶ C) ≃
      Σ f : A.base ⟶ C.base,
        (Scheme.Modules.pullback (Object.schemeMap f)).obj C.module ⟶ A.module
```

## Tag 04U3, a lemma

[Tag 04U3](https://stacks.math.columbia.edu/tag/04U3) in the Stacks Project.

**`Stacks.QCoh.isStronglyCartesian_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StronglyCartesian.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/StronglyCartesian.lean#L342).

> **Stacks 04U3.** An arrow of quasi-coherent modules is strongly cartesian if and only if
> its canonical pullback comparison map is an isomorphism.

```lean
public theorem isStronglyCartesian_iff :
    (projection (B := B) (S := S) (hS := hS)).IsStronglyCartesian
      ((projection (B := B) (S := S) (hS := hS)).map m) m ↔
      IsIso ((homEquivPullbackHom A C m).2)
```

## Tag 03YM, a lemma

[Tag 03YM](https://stacks.math.columbia.edu/tag/03YM) in the Stacks Project.

**`Stacks.QCoh.projection_isFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Fibred.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Fibred.lean#L147). The attribute's comment: “condition (1): the functor is a fibred category”. References: SGA 1 VIII (1.1), “special case”.

> **Stacks 03YM, condition (1) of Stacks 026F**: the projection from quasi-coherent modules on
> the schemes of the big fppf site over `S` to that site is a fibred category. A cartesian lift of
> `f : V ⟶ U` at a module `F` on `U` is the unit `F ⟶ f_* f^* F` of the pullback–pushforward
> adjunction, read as an `f`-map.

```lean
public theorem projection_isFibered (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    (projection (B := B) (S := S) (hS := hS)).IsFibered
```

**`Stacks.QCoh.projection_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Stack/SchemeDescent.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Stack/SchemeDescent.lean#L616). References: SGA 1 VIII (1.1), “special case”; SGA 1 VIII (1.3), “special case”.

> **Stacks 03YM.**  The projection `p : 𝒬𝒞oh ⟶ (Sch/S)_fppf` from quasi-coherent modules on the
> schemes of the big fppf site over `S` to that site satisfies the three conditions of Stacks 026F:
> it is a fibred category, the presheaves `Mor(x, y)` of Stacks 02ZB on each slice of the site are
> sheaves, and every descent datum along a covering sieve is effective.
>
> The three conditions are the three fields of `CategoryTheory.Functor.IsStack`.  Condition (1) is
> the existence of the cartesian lifts given by the units of the pullback–pushforward adjunction,
> and conditions (2) and (3) are Mathlib's stack condition for the pullback pseudofunctor of `p`
> (`CategoryTheory.Functor.isStack_pullbackPseudofunctor_iff`), hence the statement that the
> comparison from each fibre to the descent data of each fppf covering family is an equivalence.
> That comparison is identified with the canonical descent functor of Stacks 023D on schemes
> (`canonicalComparisonNatIso`), which is an equivalence by the two halves of Stacks 023T: full
> faithfulness `AlgebraicGeometry.nonempty_fullyFaithful_canonicalDescentFunctor'` and effectivity
> `AlgebraicGeometry.QuasicoherentDescentData.isEffective_fpqcPrecoverage`, both of which hold for
> an arbitrary fpqc covering family, fppf coverings being fpqc coverings.

```lean
public theorem projection_isStack (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    Functor.IsStack (projection (B := B) (S := S) (hS := hS))
      (AlgebraicGeometry.BigFppfOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.4, Tag 03YL](https://stacks.math.columbia.edu/tag/03YL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
