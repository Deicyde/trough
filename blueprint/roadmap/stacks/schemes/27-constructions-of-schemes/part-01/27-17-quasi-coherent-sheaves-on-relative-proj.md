---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Twisting.associatedSheaf, Stacks.RelativeProj.Situation.tensorModuleSheafMap, Stacks.AlgebraicGeometry.RelativeProjQuadrupleTilde.tag01O7_property1, Stacks.AlgebraicGeometry.RelativeProjQuadrupleTilde.Quadruple.tildeComparison_pullback, Stacks.RelativeProj.Situation.moduleSheafPullbackIso, Stacks.RelativeProj.Situation.moduleSheafFibreProductIso, Stacks.RelativeProj.Situation.degreeZeroSheafMap, Stacks.RelativeProj.Situation.moduleSheafFunctor_exact
statement: formalized
proof: formalized
---

# 27.17 Quasi-coherent sheaves on relative Proj

Section 27.17 of the Stacks Project, [Tag 01O5](https://stacks.math.columbia.edu/tag/01O5). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01O6, an equation

[Tag 01O6](https://stacks.math.columbia.edu/tag/01O6) in the Stacks Project.

**`Stacks.AlgebraicGeometry.RelativeProjQcohSheaf.Twisting.associatedSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Basic.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjQcohSheaf/Basic.lean#L304).

> **Stacks Project, Tag 01O6, equation (27.17.0.1).** The `𝒪_T`-module
>
> `ℳ̃_T = (f^*ℳ^{(d)} ⊗_{f^*𝒜^{(d)}} (⨁_{n ∈ ℤ} L^{⊗ n}))₀`
>
> attached to a graded `𝒜`-module `ℳ` and a quadruple `(d, f : T → S, L, ψ)`: the degree-zero
> part of the tensor product, over the pullback of the `d`-th Veronese regrading of `𝒜`, of the
> pullback of the `d`-th Veronese regrading of `ℳ` with the Laurent algebra of `L`. It is the
> quotient of `⨁_{n ∈ ℤ} f^*ℳ_{nd} ⊗ L^{⊗ (-n)}` by the balancing relations
> `(x · a) ⊗ l = x ⊗ (ψ(a) · l)`.

```lean
def associatedSheaf : SheafOfModules.{u} (structureRingSheaf T.toRingedSpace)
```

## Tag 01O7, a lemma

[Tag 01O7](https://stacks.math.columbia.edu/tag/01O7) in the Stacks Project.

**`Stacks.RelativeProj.Situation.tensorModuleSheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjLeftGradedTensorGlueHom.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjLeftGradedTensorGlueHom.lean#L449). The attribute's comment: “property (6): the canonical map from the tensor product of the sheaves attached to two left graded modules with quasi-coherent homogeneous pieces to the sheaf attached to the tensor product of those modules, on a relative projective spectrum”.

> **The canonical map `ℳ̃ ⊗_𝒪 𝒩̃ ⟶ (ℳ ⊗_𝒜 𝒩)~` of property (6) of Tag 01O7**, for two left
> graded modules with quasi-coherent homogeneous pieces over the graded algebra of a relative `Proj`
> situation. It is glued from the chart members
> `Stacks.RelativeProj.Situation.moduleSheafTensorChartMap`, to each of which it restricts, and it
> is the only morphism that does so.

```lean
public noncomputable def tensorModuleSheafMap :
    (((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨(((relativeProj s).toRingedSpace)).presheaf,
          (((relativeProj s).toRingedSpace)).IsSheaf⟩).obj ((moduleSheaf ℳ))).obj
        ((moduleSheaf 𝒩))) ⟶ s.tensorModuleSheaf ℳ 𝒩
```

**`Stacks.AlgebraicGeometry.RelativeProjQuadrupleTilde.tag01O7_property1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQuadrupleTilde/TildeComparison.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjQuadrupleTilde/TildeComparison.lean#L62). The attribute's comment: “property (1): the canonical isomorphism M~_T ≅ h^*M~”.

> For a quadruple `P = (f : T → S, d, L, ψ)` and the morphism `h : T ⟶ Proj_S(𝒜)` it
> classifies, the isomorphism `Quadruple.tildeComparison ℳ hd P : ℳ̃_T ≅ h^*ℳ̃` satisfies:
>
> * chart data of `(f, ψ, h)` exist around every point of `T`;
> * along every morphism `a : Z ⟶ T` carrying a chart datum `D`, its pullback is the local
>   comparison `localHom ℳ hd a D`, which is `a^*ℳ̃_T ≅ ℳ̃_Z`, then the chart comparison of `D`, then
>   `(a ≫ h)^*ℳ̃ ≅ a^*h^*ℳ̃` (`localHom_eq`);
> * the chart comparison of a datum sends the pure tensor `x ⊗ l` in degree `n` to
>   `(w^n · l) · g^*(x / c^n)`, `w = ψ(c)`;
> * it is the only isomorphism `ℳ̃_T ≅ h^*ℳ̃` with the second property along the opens of `T`.

```lean
theorem tag01O7_property1 :
    letI := P.isInvertible
    (∀ t : T, ∃ V : T.Opens, t ∈ V ∧ Nonempty (ChartDatum (V.ι ≫ f) (P.twisting.pullback V.ι)
      (V.ι ≫ classifyingHom s (by exact_mod_cast hd) P))) ∧
    (∀ {Z : Scheme.{u}} (a : Z ⟶ T) (D : ChartDatum (a ≫ f) (P.twisting.pullback a)
        (a ≫ classifyingHom s (by exact_mod_cast hd) P)),
      (Scheme.Modules.pullback a).map (Quadruple.tildeComparison ℳ hd P).hom =
        localHom ℳ hd a D) ∧
    (∀ {Z : Scheme.{u}} (a : Z ⟶ T) (D : ChartDatum (a ≫ f) (P.twisting.pullback a)
        (a ≫ classifyingHom s (by exact_mod_cast hd) P)) (n : ℤ),
      Twisting.pureTensor (ℳ.toGradedModule s.mul_comm) (P.twisting.pullback a) n ≫
          (D.iso ℳ hd).hom =
        bmap ℳ D.U D.c (a ≫ f) D.hf D.g D.hg D.hgf D.w n ≫
          (moduleSheafPullbackChartIso ℳ D.U D.g D.fac).inv) ∧
    (∀ Φ : Twisting.associatedSheaf (ℳ.toGradedModule s.mul_comm) P.twisting ≅
        (Scheme.Modules.pullback (classifyingHom s (by exact_mod_cast hd) P)).obj (moduleSheaf ℳ),
      (∀ (V : T.Opens) (D : ChartDatum (V.ι ≫ f) (P.twisting.pullback V.ι)
          (V.ι ≫ classifyingHom s (by exact_mod_cast hd) P)),
        (Scheme.Modules.pullback V.ι).map Φ.hom = localHom ℳ hd V.ι D) →
        Φ = Quadruple.tildeComparison ℳ hd P)
```

**`Stacks.AlgebraicGeometry.RelativeProjQuadrupleTilde.Quadruple.tildeComparison_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RelativeProjQuadrupleTilde/TildePullback.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RelativeProjQuadrupleTilde/TildePullback.lean#L308). The attribute's comment: “property (2): the isomorphisms of property (1) are compatible with pullback along every morphism of test schemes”.

> **Property (2) of [Stacks, Tag 01O7]: the isomorphisms of property (1) are compatible with
> pullbacks.** For a quadruple `P = (f : T → S, d, L, ψ)` classifying `h : T ⟶ Proj_S(𝒜)` and a
> morphism `g : T' ⟶ T`, the pulled-back quadruple `P.pullback g` classifies `g ≫ h`, and its
> isomorphism `ℳ̃_{T'} ≅ (g ≫ h)^*ℳ̃` of property (1) is the pullback along `g` of the isomorphism
> `ℳ̃_T ≅ h^*ℳ̃` of `P`, read through the canonical comparisons `ℳ̃_{T'} ≅ g^*ℳ̃_T` and
> `g^*h^*ℳ̃ ≅ (g ≫ h)^*ℳ̃`.

```lean
theorem Quadruple.tildeComparison_pullback {T : Scheme.{u}} {f : T ⟶ s.base}
    (P : Quadruple f s.algebra (d : ℤ)) {T' : Scheme.{u}} (g : T' ⟶ T) :
    letI := P.isInvertible
    (Quadruple.tildeComparison ℳ hd (P.pullback g)).hom =
      (Quadruple.associatedSheafPullbackIso (M := ℳ.toGradedModule s.mul_comm) (P := P)
          (g := g)).inv ≫
        (Scheme.Modules.pullback g).map (Quadruple.tildeComparison ℳ hd P).hom ≫
          (Scheme.Modules.pullbackComp g (classifyingHom s (by exact_mod_cast hd) P)).hom.app
            (moduleSheaf ℳ) ≫
            (Scheme.Modules.pullbackCongr
              (classifyingHom_pullback s (by exact_mod_cast hd) P g).symm).hom.app
                (moduleSheaf ℳ)
```

**`Stacks.RelativeProj.Situation.moduleSheafPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleBaseChangeIso.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleBaseChangeIso.lean#L169). The attribute's comment: “property (8): the canonical isomorphism r^* ℳ̃ ≅ (g^* ℳ)~ on the relative projective spectrum of g^* 𝒜, for any morphism of schemes g : S' ⟶ S”.

> **Stacks Project, Tag 01O7, property (8).** **The formation of `ℳ̃` commutes with base
> change.** For a morphism of schemes `g : S' ⟶ S`, put `𝒜' = g^* 𝒜` and `ℳ' = g^* ℳ`, and let
> `r : Proj_{S'}(𝒜') ⟶ Proj_S(𝒜)` be the induced morphism of relative projective spectra. Then the
> canonical comparison `r^* ℳ̃ ⟶ ℳ̃'` is an isomorphism.
>
> The comparison is `Stacks.RelativeProj.Situation.moduleSheafBaseChangeHom`, the unique morphism
> restricting on the chart of `Proj_{S'}(𝒜')` over each pair `W' ⊆ g⁻¹W` of affine opens to the
> comparison of the sheaves of Tag 01M6 across the base change of the graded section rings
> (`Stacks.RelativeProj.Situation.restrictFunctor_map_moduleSheafBaseChangeHom`); it is invertible by
> `Stacks.RelativeProj.Situation.isIso_moduleSheafBaseChangeHom`.

```lean
public noncomputable def moduleSheafPullbackIso :
    (Scheme.Modules.pullback (pullbackRelativeProjMap s g)).obj (moduleSheaf ℳ) ≅
      moduleSheaf (s := s.pullback g) (Stacks.Conormal.leftGradedPullback g ℳ)
```

**`Stacks.RelativeProj.Situation.moduleSheafFibreProductIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleBaseChangeIso.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleBaseChangeIso.lean#L216). The attribute's comment: “property (8) on the fibre product: the canonical isomorphism between the pullback of ℳ̃ along S' ×_S Proj_S(𝒜) ⟶ Proj_S(𝒜) and (g^* ℳ)~ carried to S' ×_S Proj_S(𝒜)”.

> **Stacks Project, Tag 01O7, property (8), on the fibre product.** For a morphism of schemes
> `g : S' ⟶ S`, the pullback of `ℳ̃` along the projection `S' ×_S Proj_S(𝒜) ⟶ Proj_S(𝒜)` is
> canonically isomorphic to the sheaf `(g^* ℳ)~`, transported to the fibre product along the
> canonical identification `e : Proj_{S'}(g^* 𝒜) ≅ S' ×_S Proj_S(𝒜)` of
> `Stacks.RelativeProj.Situation.relativeProjBaseChangeIso`.
>
> It is `Stacks.RelativeProj.Situation.moduleSheafPullbackIso` read through `e`: the projection is
> `e⁻¹` followed by the base-change morphism `r`, so its inverse image is `e⁻¹`'s of `r^* ℳ̃`.

```lean
public noncomputable def moduleSheafFibreProductIso :
    (Scheme.Modules.pullback (Limits.pullback.fst (relativeProjToBase s) g)).obj (moduleSheaf ℳ) ≅
      (Scheme.Modules.pullback (pullbackRelativeProjIso s g).inv).obj
        (moduleSheaf (s := s.pullback g) (Stacks.Conormal.leftGradedPullback g ℳ))
```

**`Stacks.RelativeProj.Situation.degreeZeroSheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafDegreeZeroMap.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafDegreeZeroMap.lean#L450). The attribute's comment: “property (3): the canonical map from the pullback of the degree-zero part of a graded module to its associated sheaf on the relative projective spectrum”. References: EGA II (3.3.2), “Map (3.3.2.4) for n = 0”.

> **Stacks Project, Tag 01O7, property (3).** The canonical map
>
> `π^*ℳ_0 ⟶ ℳ̃`
>
> on the relative projective spectrum `π : Proj_S(𝒜) ⟶ S`, for a graded `𝒜`-module `ℳ` with
> quasi-coherent homogeneous pieces. It is the transpose, across the adjunction `π^* ⊣ π_*`, of
> `Stacks.RelativeProj.Situation.degreeZeroPushforwardHom`, the morphism `ℳ_0 ⟶ π_* ℳ̃` which on
> the sections over an affine open `W` of the base carries `m` to the section `m / 1` of `ℳ̃` over
> `π⁻¹(W)`: under the identification of `ℳ̃` over `π⁻¹(W)` with the sheaf of the graded module of
> sections of `ℳ` over `W` on `Proj 𝒜(W)`, this is the global section `m / 1` of Tag 01M7.

```lean
public def degreeZeroSheafMap :
    (Scheme.Modules.pullback (relativeProjToBase s)).obj (ℳ.piece 0) ⟶ moduleSheaf ℳ
```

**`Stacks.RelativeProj.Situation.moduleSheafFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafExactAbelian.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafExactAbelian.lean#L216). The attribute's comment: “property (5): the construction ℳ ↦ ℳ̃ is an exact functor from the abelian category of quasi-coherent graded modules over 𝒜 to modules on the relative projective spectrum”. References: EGA II (8.14.1), “partial”.

> The functor `Stacks.RelativeProj.Situation.moduleSheafFunctor`, from the abelian category of
> quasi-coherent graded modules over the graded algebra `𝒜` of the situation to the modules on the
> relative projective spectrum `Proj_S(𝒜)`, is additive, preserves finite limits and preserves
> finite colimits; equivalently, it carries short exact sequences of quasi-coherent graded modules
> to short exact sequences of modules on `Proj_S(𝒜)`.

```lean
public theorem moduleSheafFunctor_exact :
    (moduleSheafFunctor s).Additive ∧ PreservesFiniteLimits (moduleSheafFunctor s) ∧
      PreservesFiniteColimits (moduleSheafFunctor s) ∧
      ∀ S : ShortComplex (QcohGradedModule s), S.ShortExact →
        (S.map (moduleSheafFunctor s)).ShortExact
```

**`Stacks.RelativeProj.Situation.moduleSheafFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafFunctorial.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafFunctorial.lean#L229). The attribute's comment: “property (4): the construction ℳ ↦ ℳ̃ is a functor from quasi-coherent graded modules over 𝒜 to modules on the relative projective spectrum”.

> The construction `ℳ ↦ ℳ̃` is functorial in `ℳ`: it is a functor from the quasi-coherent
> graded modules over the graded algebra `𝒜` to the modules over the relative projective spectrum
> `Proj_S(𝒜)`, sending `ℳ` to the sheaf `Stacks.RelativeProj.Situation.moduleSheaf ℳ` and a
> homomorphism to the glued morphism `Stacks.RelativeProj.Situation.moduleSheafMap` of the chart
> morphisms.

```lean
public noncomputable def moduleSheafFunctor : QcohGradedModule s ⥤ (relativeProj s).Modules
```

**`Stacks.RelativeProj.Situation.shiftedSumSheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafShiftedSum.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/ModuleGlueing/RelativeProjModuleSheafShiftedSum.lean#L115). The attribute's comment: “property (7): the canonical map from the pullback of a graded module to the direct sum of the sheaves associated to its shifts on the relative projective spectrum”.

> **Stacks Project, Tag 01O7, property (7).** The canonical map
>
> `π^*ℳ ⟶ ⨁_{n ∈ ℤ} (ℳ(n))~`
>
> on the relative projective spectrum `π : Proj_S(𝒜) ⟶ S`, out of the pullback of the
> `𝒪_S`-module `ℳ = ⨁_{n ∈ ℤ} ℳ_n` underlying a graded `𝒜`-module with quasi-coherent homogeneous
> pieces. On the summand `π^*ℳ_n` it is the degree-`n` component
> `Stacks.RelativeProj.Situation.shiftedDegreeSheafMap`, the canonical map of property (3) for the
> shift `ℳ(n)`, followed by the inclusion of the `n`-th summand; on the sections over an affine
> open of the base it is the map of Tag 01MR, `m ↦ m / 1` in degree `n`.

```lean
public def shiftedSumSheafMap :
    (Scheme.Modules.pullback (relativeProjToBase s)).obj (∐ fun n : ℤ => ℳ.piece n) ⟶
      ∐ fun n : ℤ => moduleSheaf (ℳ.shift n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 27.17, Tag 01O5](https://stacks.math.columbia.edu/tag/01O5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
