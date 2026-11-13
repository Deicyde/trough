---
declaration: section
origin: cited
lean: AlgebraicGeometry.RelativeDualitySituation, AlgebraicGeometry.RelativeDualitySituation.structureSheafDirectImage, AlgebraicGeometry.RelativeDualitySituation.existsUnique_isRelativePoincareTrace, Stacks.WeilDeRham.higherDirectImage_map_deRham_d_top_eq_zero, AlgebraicGeometry.RelativeDualitySituation.existsUnique_deRhamPoincareTrace
statement: formalized
proof: formalized
---

# 50.24 Relative Poincaré duality

Section 50.24 of the Stacks Project, [Tag 0G8F](https://stacks.math.columbia.edu/tag/0G8F). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G8G, a situation

[Tag 0G8G](https://stacks.math.columbia.edu/tag/0G8G) in the Stacks Project.

**`AlgebraicGeometry.RelativeDualitySituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/Basic.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/Basic.lean#L37).

> A proper smooth morphism over a quasi-compact quasi-separated scheme, with all fibres
> nonempty and equidimensional of dimension `n`.

```lean
structure RelativeDualitySituation
```

## Tag 0G8H, a lemma

[Tag 0G8H](https://stacks.math.columbia.edu/tag/0G8H) in the Stacks Project.

**`AlgebraicGeometry.RelativeDualitySituation.structureSheafDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/StructureSheafDirectImage.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/StructureSheafDirectImage.lean#L68). The attribute's comment: “the three assertions: (1) f\_*O\_X is a finite étale O\_S-algebra (its relative Spec is finite étale over S); (2) locally on S, Rf\_*O\_X = f\_*O\_X ⊕ P in D(O\_S) with P perfect of tor amplitude in [1, ∞); (3) d : f\_*O\_X → f\_*Ω\_\{X/S} is zero”.

> In the relative duality situation `f : X ⟶ S`:
>
> 1. `f_*𝒪_X` is a finite étale `𝒪_S`-algebra: the structure morphism of its relative spectrum
>    is finite and étale;
> 2. locally on `S`, `Rf_*𝒪_X ≅ f_*𝒪_X ⊕ P` in `D(𝒪_S)` with `P` perfect of Tor amplitude in
>    `[1, ∞)`: every point of `S` has an open neighbourhood `U` over which this holds in `D(𝒪_U)`;
> 3. the map `d : f_*𝒪_X ⟶ f_*Ω_{X/S}` is zero: the degree-zero de Rham differential vanishes on
>    sections over `f⁻¹V` for every open `V` of `S`.

```lean
theorem structureSheafDirectImage (D : RelativeDualitySituation.{u}) :
    (letI := isQuasicoherent_pushforwardAlgebra_of_quasiCompact D.f;
      IsFinite (relativeSpecToBase (pushforwardAlgebra D.f)) ∧
        Etale (relativeSpecToBase (pushforwardAlgebra D.f))) ∧
    (∀ s : D.S, ∃ (U : D.S.Opens) (_ : s ∈ U)
      (P : DerivedCategory (StrictlyPerfect.OXMod.{u, u}
        (D.S.toRingedSpace.restrict U.isOpenEmbedding))),
      Stacks.Cohomology.PerfectComplexes.IsPerfect P ∧
      Stacks.Cohomology.TorAmplitude.HasTorAmplitudeGE
        (D.S.toRingedSpace.restrict U.isOpenEmbedding) P 1 ∧
      Nonempty ((RingedSpace.derivedRestrictModules D.S.toRingedSpace U).obj
          ((derivedPushforward D.f.toLRSHom.toShHom).obj
            (structureSheafDegreeZeroObj D.X)) ≅
        (DerivedCategory.singleFunctor _ 0).obj
          ((RingedSpace.restrictModules D.S.toRingedSpace U).obj
            ((Scheme.Modules.pushforward D.f).obj (Scheme.unitModule D.X))) ⊞ P)) ∧
    (∀ V : D.S.Opens, ((Scheme.Hom.deRhamComplex D.f).d 0 1).val.app (op (D.f ⁻¹ᵁ V)) = 0)
```

## Tag 0G8I, a lemma

[Tag 0G8I](https://stacks.math.columbia.edu/tag/0G8I) in the Stacks Project.

**`AlgebraicGeometry.RelativeDualitySituation.existsUnique_isRelativePoincareTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/TraceFromModel.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/TraceFromModel.lean#L102). The attribute's comment: “relative Poincaré duality trace: there is t : Rf\_*Omega^n[n] -> O\_S, unique up to a unit of H^0(X, O\_X), all of whose pairings Rf\_*Omega^p (x)^L Rf\_*Omega^\{n-p}[n] -> O\_S are perfect pairings of perfect complexes”.

> In the situation of relative Poincaré duality ([Stacks, Tag 0G8G]), `f : X ⟶ S` proper and
> smooth over a quasi-compact quasi-separated base, all of whose fibres are nonempty and
> equidimensional of dimension `n`, there is an `𝒪_S`-module map
> `t : Rf_*Ω^n_{X/S}[n] ⟶ 𝒪_S` such that for all `p` the pairing
> `Rf_*Ω^p_{X/S} ⊗^L Rf_*Ω^{n-p}_{X/S}[n] ⟶ 𝒪_S` given by the relative cup product composed with
> `t` is a perfect pairing of perfect complexes, and `t` is unique up to precomposing with
> multiplication by a unit of `H^0(X, 𝒪_X)`: the maps with this property are exactly the
> `t ∘ u` for `u` a unit of `Γ(X, 𝒪_X)`.

```lean
theorem existsUnique_isRelativePoincareTrace :
    ∃ t : (Stacks.Duality.derivedPushforward D.f).obj ((D.f.formsInDegreeZero D.n)⟦(D.n : ℤ)⟧) ⟶
        (Stacks.Duality.derivedStructureSheafInDegree D.S 0).obj,
      D.IsRelativePoincareTrace t ∧ ∀ t', D.IsRelativePoincareTrace t' ↔
        ∃ u : (Γ(D.X, ⊤))ˣ, t' = D.f.formsShiftSMul D.n u ≫ t
```

## Tag 0G8J, a lemma

[Tag 0G8J](https://stacks.math.columbia.edu/tag/0G8J) in the Stacks Project.

**`Stacks.WeilDeRham.higherDirectImage_map_deRham_d_top_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilDeRham/TopDifferentialRelative.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilDeRham/TopDifferentialRelative.lean#L71).

> **Stacks Project, Tag 0G8J.** In the situation of relative Poincaré duality
> ([Stacks, Tag 0G8G]) — `S` quasi-compact and quasi-separated, `f : X ⟶ S` proper and smooth, all
> fibres nonempty and equidimensional of dimension `n` — the map
> `d : Rⁿf_*Ω^{n-1}_{X/S} ⟶ Rⁿf_*Ωⁿ_{X/S}` induced by the de Rham differential is zero.

```lean
theorem higherDirectImage_map_deRham_d_top_eq_zero (D : RelativeDualitySituation.{u}) :
    (Stacks.Cohomology.AbelianSheaf.higherDirectImage D.f.base D.n).map
      ((SheafOfModules.toSheaf _).map (D.f.deRhamComplex.d (D.n - 1) D.n)) = 0
```

## Tag 0G8K, a proposition

[Tag 0G8K](https://stacks.math.columbia.edu/tag/0G8K) in the Stacks Project.

**`AlgebraicGeometry.RelativeDualitySituation.existsUnique_deRhamPoincareTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/DeRhamTrace/Main.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/RelativePoincareDuality/DeRhamTrace/Main.lean#L168). The attribute's comment: “relative Poincaré duality for de Rham cohomology: there is t : R^\{2n}f\_*Omega^. -> O\_S, unique up to a unit of H^0(X, O\_X), such that (xi, xi') |-> t(xi cup xi') is a perfect pairing Rf\_*Omega^. (x)^L Rf\_*Omega^.[2n] -> O\_S of perfect complexes”.

> **[Stacks, Tag 0G8K].** In the situation of relative Poincaré duality ([Stacks, Tag 0G8G]):
> `S` quasi-compact and quasi-separated, `f : X ⟶ S` proper and smooth, all of whose fibres are
> nonempty and equidimensional of dimension `n`. There is an `𝒪_S`-module map
> `t : R^{2n}f_*Ω^•_{X/S} ⟶ 𝒪_S` such that the pairing
> `Rf_*Ω^•_{X/S} ⊗^L Rf_*Ω^•_{X/S}[2n] ⟶ 𝒪_S`, `(ξ, ξ') ↦ t(ξ ∪ ξ')`, is a perfect pairing of
> perfect complexes (`IsDeRhamPoincareTrace`, read through the identification
> `Hom(Rf_*(Ω^•[2n]), 𝒪_S) ≃ Hom(R^{2n}f_*Ω^•, 𝒪_S)` of `deRhamTraceEquiv`, which holds as
> `Rf_*(Ω^•[2n])` has no cohomology in positive degrees), and `t` is unique up to precomposing with
> multiplication by a unit of `H^0(X, 𝒪_X)`: the maps with this property are exactly the
> `t ∘ u` for `u` a unit of `Γ(X, 𝒪_X)`.

```lean
theorem existsUnique_deRhamPoincareTrace :
    ∃ t : D.deRhamTopCohomology ⟶ SheafOfModules.unit D.S.ringCatSheaf,
      D.IsDeRhamPoincareTrace (D.deRhamTraceEquiv.symm t) ∧
      ∀ t' : D.deRhamTopCohomology ⟶ SheafOfModules.unit D.S.ringCatSheaf,
        D.IsDeRhamPoincareTrace (D.deRhamTraceEquiv.symm t') ↔
          ∃ u : (Γ(D.X, ⊤))ˣ, t' = D.deRhamTopCohomologySMul (u : Γ(D.X, ⊤)) ≫ t
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.24, Tag 0G8F](https://stacks.math.columbia.edu/tag/0G8F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
