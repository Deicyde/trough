---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.FlatFppf.isZero_derivedSectionsFppf_of_parasitic_cohomology, AlgebraicGeometry.Stack.FlatFppf.isZero_cohomology_of_isZero_derivedSectionsFppf_flatAffine, AlgebraicGeometry.Stack.FlatFppf.hasAffineDerivedSectionsBaseChange_derivedModuleLowerShriekSucc, AlgebraicGeometry.Stack.FlatFppf.quasiCoherentDerivedEquivalenceSucc
statement: formalized
proof: formalized
---

# 104.8 Quasi-coherent objects in the derived category

Section 104.8 of the Stacks Project, [Tag 0H12](https://stacks.math.columbia.edu/tag/0H12). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H13, a lemma

[Tag 0H13](https://stacks.math.columbia.edu/tag/0H13) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.isZero_derivedSectionsFppf_of_parasitic_cohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfParasiticVanishingUnconditional.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatFppfParasiticVanishingUnconditional.lean#L69). The attribute's comment: “cohomology over an object taken as the derived functor of sections over it, and the parasitic condition of Stacks 0773 written out on abelian sheaves”.

> **Stacks 0H13.** Let `𝒳` be an algebraic stack and let `K` be an object of `D(𝒳_{fppf})`
> whose cohomology sheaves are parasitic — the sections of every cohomology sheaf of `K` vanish at
> every object of `𝒳` lying over a scheme `U` such that `U → 𝒳` is flat (**Stacks 0773**). Then
> `RΓ(x, K) = 0` for every such object `x`.
>
> Cohomology over an object is the right derived functor of sections over it. The proof is the
> source's: by Stacks 0H10 (2)(b), `RΓ(x, K) = RΓ(x, g⁻¹K)`, and `g⁻¹K = 0` because its cohomology
> sheaves are the restrictions of those of `K` to the flat objects.

```lean
theorem isZero_derivedSectionsFppf_of_parasitic_cohomology
    (K : DerivedCategory (Sheaf (fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1}))
    (hK : ∀ n : ℤ, ∀ y : 𝒳.val.val.obj, flatObject B S hS 𝒳.val y →
      Subsingleton (((DerivedCategory.homologyFunctor
        (Sheaf (fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1}) n).obj K).obj.obj (op y)))
    (x : 𝒳.val.val.obj) (hx : flatObject B S hS 𝒳.val x) :
    IsZero ((derivedSectionsFppf B S hS 𝒳 x).obj K)
```

## Tag 0H14, a lemma

[Tag 0H14](https://stacks.math.columbia.edu/tag/0H14) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.isZero_cohomology_of_isZero_derivedSectionsFppf_flatAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/FlatAffineCohomologyVanishing.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/FlatAffineCohomologyVanishing.lean#L112). The attribute's comment: “unconditional. Cohomology over an object is the derived functor of sections over it (Tag 0DD8 convention, equal to cohomology of the slice site by Tag 03F3)”.

> **Stacks 0H14.** Let `𝒳` be an algebraic stack and let `K` be an object of `D(𝒳_{fppf})` such
> that `RΓ(x, K) = 0` for every object `x` of `𝒳` lying over an affine scheme `U` with `U → 𝒳`
> flat. Then `H^i(𝒳, K) = 0` for all `i`.
>
> Here `RΓ(x, -)` is the right derived functor of sections over `x` (the convention of Stacks 0DD8
> and Stacks 0H10 (2)(b) in this library), and `H^i(𝒳, K)` is the `i`-th cohomology of the
> unbounded derived global sections `RΓ(𝒳_{fppf}, K)`.
>
> This is the source's proof: `g⁻¹K = 0` because its derived sections vanish on a family covering
> the flat-fppf site (Stacks 0H10 (2)(b)), so `RΓ(𝒳_{flat,fppf}, g⁻¹K) = 0`, which is
> `RΓ(𝒳_{fppf}, K)` by Stacks 0H10 (2)(a).

```lean
theorem isZero_cohomology_of_isZero_derivedSectionsFppf_flatAffine
    (K : DerivedCategory (Sheaf (fppfTopology B S hS 𝒳) AddCommGrpCat.{u + 1}))
    (hK : ∀ x : 𝒳.val.val.obj, flatObject B S hS 𝒳.val x →
      IsAffine ((BigFppfOver.toScheme B S hS).obj (𝒳.val.val.p.obj x)) →
      IsZero ((derivedSectionsFppf B S hS 𝒳 x).obj K))
    (i : ℤ) :
    IsZero ((DerivedCategory.homologyFunctor AddCommGrpCat.{u + 1} i).obj
      ((AlgebraicGeometry.Stack.derivedGlobalSections.{u, u + 1} B S hS 𝒳.val).obj K))
```

## Tag 0H15, a lemma

[Tag 0H15](https://stacks.math.columbia.edu/tag/0H15) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.hasAffineDerivedSectionsBaseChange_derivedModuleLowerShriekSucc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasiCoherentDerivedEquivalenceOfStack.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasiCoherentDerivedEquivalenceOfStack.lean#L69).

> **Stacks 0H15.** Let `𝒳` be an algebraic stack and `H` an object of
> `D_QCoh(𝒪_{𝒳_{flat, fppf}})` (module universe `u + 1`). Then `Lg_! H` has the following
> property: for every morphism `x ⟶ x'` of `𝒳_{affine}` the map
> `RΓ(x', Lg_! H) ⊗^L_{𝒪(x')} 𝒪(x) ⟶ RΓ(x, Lg_! H)` is a quasi-isomorphism
> (`HasAffineDerivedSectionsBaseChange`). The derived categories are the standard models.

```lean
theorem hasAffineDerivedSectionsBaseChange_derivedModuleLowerShriekSucc :
    letI := HasDerivedCategory.standard
      (SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳))
    letI := HasDerivedCategory.standard
      (SheafOfModules.{u + 1} (ambientRingStructureSheaf B S hS 𝒳))
    ∀ H : DerivedCategory (SheafOfModules.{u + 1} (subsiteRingStructureSheaf B S hS 𝒳)),
      DerivedCategoryB.derivedCategoryB (flatQuasicoherentModulesSucc B S hS 𝒳) H →
        HasAffineDerivedSectionsBaseChange B S hS 𝒳
          ((derivedModuleLowerShriekSucc B S hS 𝒳).obj H)
```

## Tag 0H16, a proposition

[Tag 0H16](https://stacks.math.columbia.edu/tag/0H16) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.quasiCoherentDerivedEquivalenceSucc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasiCoherentDerivedEquivalenceOfStack.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasiCoherentDerivedEquivalenceOfStack.lean#L98).

> **Stacks 0H16.** For an algebraic stack `𝒳`, `QC(𝒳)` is canonically equivalent to
> `D_QCoh(𝒪_𝒳)`, both at module universe `u + 1` (see the module docstring for why `u + 1`):
> `QC(𝒳) ≌ Q_𝒳` by Stacks 0H0X and 0H0C, `Q_𝒳 = 𝒜` by Stacks 0H15, and `𝒜 ≌ D_QCoh(𝒪_𝒳)` by
> Stacks 0H11, where `D_QCoh(𝒪_𝒳)` is the quotient of `D_{LQCoh^fbc}(𝒪_𝒳)` by
> `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` (Stacks 07B6).

```lean
def quasiCoherentDerivedEquivalenceSucc :
    quasiCoherentDerived.{u, u + 1, u, u + 1} B S hS 𝒳.val.val.p ≌
      DerivedCategory.KernelColocalization.quotient (parasiticModulesSucc B S hS 𝒳)
        (sheafFlatBaseChangeModulesSucc B E h S hS 𝒳)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 104.8, Tag 0H12](https://stacks.math.columbia.edu/tag/0H12)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
