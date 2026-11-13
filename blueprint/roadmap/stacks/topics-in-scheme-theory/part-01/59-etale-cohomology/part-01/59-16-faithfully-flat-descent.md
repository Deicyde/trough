---
declaration: section
origin: cited
lean: AlgebraicGeometry.QuasicoherentDescentData.isEffective_iff_exists_iso, AlgebraicGeometry.QuasicoherentDescentData.isEffective_fpqcPrecoverage, Stacks.Descent.amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat, AlgebraicTopology.amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat, ModuleCat.DescentData, ModuleCat.DescentData.IsEffective, ModuleCat.DescentData.isEffective_of_faithfullyFlat
statement: formalized
proof: formalized
---

# 59.16 Faithfully flat descent

Section 59.16 of the Stacks Project, [Tag 03O6](https://stacks.math.columbia.edu/tag/03O6). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03O7, a definition

[Tag 03O7](https://stacks.math.columbia.edu/tag/03O7) in the Stacks Project.

**`AlgebraicGeometry.QuasicoherentDescentData.isEffective_iff_exists_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/DescentData.lean#L337). The attribute's comment: “the descent datum is `QuasicoherentDescentData f` (quasicoherent components with transition isomorphisms satisfying the cocycle condition); effectivity is the right-hand side, equivalent to `IsEffective`”.

> A quasicoherent descent datum `D = (F_i, φ_ij)` relative to `f i : X i ⟶ S` is effective
> exactly when there are a quasicoherent module `M` on `S` and isomorphisms
> `φ_i : (f i)^* M ≅ F_i` compatible with the transitions: over every `Y` mapping to `X i₁` and
> `X i₂` compatibly with `S`, the transition `φ_{i₁ i₂}` of `D` is the pullback of `φ_{i₂}`
> composed with the canonical identification of the two pullbacks of `M` and the pullback of
> `φ_{i₁}⁻¹`.  Taking `Y = X i₁ ×_S X i₂` with its projections, this is
> `φ_{i₁ i₂} = pr₁^* φ_{i₂} ∘ pr₀^* φ_{i₁}⁻¹`.

```lean
theorem isEffective_iff_exists_iso (D : QuasicoherentDescentData f) :
    D.IsEffective ↔
      ∃ (M : (SheafOfModules.isQuasicoherent S.ringCatSheaf).FullSubcategory)
        (φ : ∀ i, ((canonicalDescentFunctor f).obj M).obj.obj i ≅ D.obj.obj i),
        ∀ ⦃Y : Scheme.{u}⦄ (q : Y ⟶ S) ⦃i₁ i₂ : I⦄ (f₁ : Y ⟶ X i₁) (f₂ : Y ⟶ X i₂)
          (hf₁ : f₁ ≫ f i₁ = q) (hf₂ : f₂ ≫ f i₂ = q),
          D.obj.hom q f₁ f₂ hf₁ hf₂ =
            (modulePullbackPseudofunctor.map f₁.op.toLoc).toFunctor.map (φ i₁).inv ≫
              ((canonicalDescentFunctor f).obj M).obj.hom q f₁ f₂ hf₁ hf₂ ≫
                (modulePullbackPseudofunctor.map f₂.op.toLoc).toFunctor.map (φ i₂).hom
```

## Tag 03O8, a theorem

[Tag 03O8](https://stacks.math.columbia.edu/tag/03O8) in the Stacks Project.

**`AlgebraicGeometry.QuasicoherentDescentData.isEffective_fpqcPrecoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/FpqcEffectiveUnconditional.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/QuasiCoherent/FpqcEffectiveUnconditional.lean#L43). The attribute's comment: “effectivity of all quasi-coherent descent data for an fpqc covering”. References: SGA 1 VIII (1.1), “effectivity”; SGA 4½ Arcata (1.4), “fpqc qcoh case”.

> Every quasi-coherent descent datum for an fpqc covering family of an arbitrary scheme is
> effective, at an arbitrary index universe.

```lean
theorem isEffective_fpqcPrecoverage {S : Scheme.{u}} (𝒰 : PreZeroHypercover.{v} S)
    (h𝒰 : 𝒰.presieve₀ ∈ Scheme.fpqcPrecoverage.{u} S) (D : QuasicoherentDescentData 𝒰.f) :
    D.IsEffective
```

## Tag 03O9, a lemma

[Tag 03O9](https://stacks.math.columbia.edu/tag/03O9) in the Stacks Project.

**`Stacks.Descent.amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/AmitsurAcyclic.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Module/AmitsurAcyclic.lean#L435). The attribute's comment: “the case M = R”. References: SGA 1 VIII (1.7), “affine case”.

> **Stacks Lemma 023M.** For a faithfully flat algebra `A` over a commutative ring `R` and an
> arbitrary `R`-module `M`, the extended Amitsur cochain complex
> `M → A ⊗[R] M → (A ⊗[R] A) ⊗[R] M → ⋯`
> is exact in every degree.

```lean
theorem amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat [Module.FaithfullyFlat R A] :
    (amitsurExtendedCochainComplex R A M).Acyclic
```

## Tag 03OA, a lemma

[Tag 03OA](https://stacks.math.columbia.edu/tag/03OA) in the Stacks Project.

**`Stacks.Descent.amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/AmitsurAcyclic.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Module/AmitsurAcyclic.lean#L435). The attribute's comment: “coefficients in M”. References: SGA 1 VIII (1.7), “affine case”.

> **Stacks Lemma 023M.** For a faithfully flat algebra `A` over a commutative ring `R` and an
> arbitrary `R`-module `M`, the extended Amitsur cochain complex
> `M → A ⊗[R] M → (A ⊗[R] A) ⊗[R] M → ⋯`
> is exact in every degree.

```lean
theorem amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat [Module.FaithfullyFlat R A] :
    (amitsurExtendedCochainComplex R A M).Acyclic
```

**`AlgebraicTopology.amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/ModuleEquivalence/FaithfullyFlatAmitsur.lean, line 1257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/ModuleEquivalence/FaithfullyFlatAmitsur.lean#L1257). References: SGA 1 VIII (1.7), “affine case”.

> **Stacks Lemma 023M**, and **Stacks Lemma 03OA**.  The extended Amitsur cochain complex of a
> faithfully flat algebra is exact for every module of coefficients.  Exactness of the extended
> complex `M → A ⊗[R] M → A ⊗[R] A ⊗[R] M → ⋯` says both that the unaugmented complex is exact in
> positive degrees and that its degree-zero cohomology is `M`, which is the form 03OA states.

```lean
theorem amitsurExtendedCochainComplex_acyclic_of_faithfullyFlat
    (R : Type u) (A : Type v) (M : Type w) [CommRing R] [CommRing A] [Algebra R A]
    [AddCommGroup M] [Module R M] [Module.FaithfullyFlat R A] :
    (amitsurExtendedCochainComplex R A M).Acyclic
```

## Tag 03OB, a definition

[Tag 03OB](https://stacks.math.columbia.edu/tag/03OB) in the Stacks Project.

**`ModuleCat.DescentData`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean#L244). The attribute's comment: “descent datum for a module along a ring map”.

> A descent datum for modules for an `R`-algebra `A`.
>
> The transition is bundled as an `A ⊗[R] A`-linear equivalence, and `cocycle` is the equality
> `φ₁₂ ∘ φ₀₁ = φ₀₂`.

```lean
structure DescentData
```

## Tag 03OC, a definition

[Tag 03OC](https://stacks.math.columbia.edu/tag/03OC) in the Stacks Project.

**`ModuleCat.DescentData.IsEffective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Module/DescentData.lean#L310). The attribute's comment: “effectivity of a module descent datum”.

> A module descent datum is effective if it is isomorphic to the canonical descent datum
> obtained by extending scalars from an `R`-module.

```lean
abbrev DescentData.IsEffective (R : Type u) (A : Type v) [CommRing R] [CommRing A]
    [Algebra R A] (D : DescentData.{u, v, w} R A) : Prop
```

## Tag 03OD, a theorem

[Tag 03OD](https://stacks.math.columbia.edu/tag/03OD) in the Stacks Project.

**`ModuleCat.DescentData.isEffective_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffectiveDescent.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Modules/FaithfullyFlatEffectiveDescent.lean#L84). The attribute's comment: “descent data for modules along a faithfully flat ring map are effective”. References: SGA 1 VIII (1.1), “affine case”; SGA 1 VIII (1.6), “effectivity”; SGA 4½ Arcata (1.4.5), “ess. surj. (affine)”; SGA 4½ Arcata (1.4), “module case”.

> **Stacks 023N, part (1).** Every descent datum for modules along a faithfully flat ring map
> `R → A` is effective: it is isomorphic, as a descent datum, to the canonical datum on the
> extension of scalars of an `R`-module.

```lean
public theorem DescentData.isEffective_of_faithfullyFlat
    (D : DescentData.{u, u, max u w} R A) : D.IsEffective R A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.16, Tag 03O6](https://stacks.math.columbia.edu/tag/03O6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
