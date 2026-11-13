---
declaration: section
origin: cited
lean: Stacks.Algebraization.finite_completedStalk, Stacks.Algebraization.isDepthOneQuotient_toImprovedSystem_app, Stacks.Algebraization.exists_improving_map_of_coherentAdicSystem, Stacks.Algebraization.exists_proIso_coherentAdicSystem_toImprovedSystem, Stacks.Algebraization.exists_proIso_coherentAdicSystem_canonicalImprovedSystem, Stacks.Algebraization.exists_proIso_coherentAdicSystem_depthThreeImprovedSystem
statement: formalized
proof: formalized
---

# 52.21 Improving coherent formal modules

Section 52.21 of the Stacks Project, [Tag 0EJD](https://stacks.math.columbia.edu/tag/0EJD). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EJE, a lemma

[Tag 0EJE](https://stacks.math.columbia.edu/tag/0EJE) in the Stacks Project.

**`Stacks.Algebraization.finite_completedStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/CompletedStalkFinite.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/CompletedStalkFinite.lean#L441). The attribute's comment: “finiteness of the completed stalk over the completed local ring”.

> **Stacks 0EJE, finiteness of the completed stalk.**
>
> Let `ℐ` be a quasi-coherent sheaf of ideals on a locally Noetherian scheme `X` and let `(ℱ_n)` be
> an object of `Coh(X, ℐ)`. At every point `x` the completed stalk `ℱ_x^∧` is a finite module over
> the completed local ring `𝒪_{X,x}^∧`.
>
> Each `ℱ_n` is coherent, so `ℱ_{n,x}` is a finite `𝒪_{X,x}`-module, and the transitions are
> surjective on stalks with kernel `ℐ_x^{n+1} ℱ_{n+1,x}`; the limit therefore has reduction
> `ℱ_{0,x}` modulo `ℐ_x`, which is finite, and [Stacks, Tag 031D] turns a module with finite
> reduction into one whose `ℐ_x`-adic completion is finite over `𝒪_{X,x}^∧`.

```lean
theorem finite_completedStalk [IsLocallyNoetherian X] (J : X.IdealSheafData)
    (G : Stacks.Coherent.CoherentAdicSystems J) (x : X) :
    Module.Finite (completedLocalRing J x) (completedStalk J G x)
```

**`Stacks.Algebraization.isDepthOneQuotient_toImprovedSystem_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModules.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModules.lean#L112). The attribute's comment: “the canonical map (ℱₙ) → (ℱ'ₙ) of inverse systems of coherent modules, and its property (1); properties (2) and (3), which identify (ℱ'ₙ) pro-isomorphically with an object of Coh(X, ℐ), are not covered: they rest on Tag 0EIE, which this library does not carry”.

> Each component of the canonical map `(ℱₙ) ⟶ (ℱ'ₙ)` is the depth-one quotient of its source:
> `ℱ'ₙ` is coherent, the map is surjective and an isomorphism on stalks outside `T`, and `ℱ'ₙ` has
> depth at least one at every point of `T`.

```lean
theorem isDepthOneQuotient_toImprovedSystem_app (n : ℕᵒᵖ) :
    IsDepthOneQuotient T ((toImprovedSystem T hT F).app n)
```

**`Stacks.Algebraization.exists_improving_map_of_coherentAdicSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModules.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModules.lean#L133). The attribute's comment: “the canonical map out of an object of Coh(X, ℐ) and its property (1)”.

> A coherent adic system along an ideal sheaf admits a map to an inverse system of coherent
> modules each of whose terms is the quotient of the corresponding term by its sections supported
> on `T`, hence has depth at least one along `T`.

```lean
theorem exists_improving_map_of_coherentAdicSystem {I : X.IdealSheafData}
    (F : Stacks.Coherent.CoherentAdicSystems I) :
    ∃ (G : ℕᵒᵖ ⥤ X.Modules) (τ : F.obj ⟶ G), ∀ n : ℕᵒᵖ, IsDepthOneQuotient T (τ.app n)
```

**`Stacks.Algebraization.exists_proIso_coherentAdicSystem_toImprovedSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModulesTheorem.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModulesTheorem.lean#L69). The attribute's comment: “the canonical map (ℱₙ) → (ℱ'ₙ) and its properties (1), (2) and (3); stated for every Noetherian scheme, without the dualizing complex of the source”.

> **Stacks Project, Tag 0EJE.** Let `X` be a Noetherian scheme, `ℐ` a quasi-coherent sheaf of
> ideals with closed subscheme `Y`, `(ℱ_n)` an object of `Coh(X, ℐ)` and `T ⊆ Y` stable under
> specialization. Assume that for `y ∈ T` and every nonmaximal prime `𝔭` of `𝒪_{X,y}^∧` with
> `V(𝔭) ∩ V(ℐ𝒪_{X,y}^∧) = {𝔪_y^∧}` the module `(ℱ_y^∧)_𝔭` has positive depth. Then the canonical
> map `(ℱ_n) → (ℱ'_n)` onto the quotients by the sections supported in `T`
> (`Stacks.Algebraization.toImprovedSystem`, each component the depth-one quotient of Stacks,
> Tag 0DX3: `ℱ'_n` coherent, the map surjective and an isomorphism on stalks outside `T`) has the
> following properties:
>
> 1. every `ℱ'_n` has depth at least one at every point of `T`;
> 2. `(ℱ'_n)` is isomorphic as a pro-system to an object `(𝒢_n)` of `Coh(X, ℐ)`: there is a
>    pro-isomorphism `P` whose forward maps are the components of a morphism
>    `ψ : (𝒢_n) → (ℱ'_n)`;
> 3. the induced morphism `φ : (ℱ_n) → (𝒢_n)` of `Coh(X, ℐ)`, the one with `φ ≫ ψ` the canonical
>    map, is an epimorphism of `Coh(X, ℐ)` whose kernel in `Coh(X, ℐ)` is annihilated by a power of
>    `ℐ`.
>
> The source also assumes that `X` locally has a dualizing complex; the statement holds without
> it.

```lean
theorem exists_proIso_coherentAdicSystem_toImprovedSystem (hTY : T ⊆ I.support)
    (h6 : ∀ y ∈ T, ∀ p : PrimeSpectrum (completedLocalRing I y),
      p.asIdeal ≠ completedMaximalIdeal I y →
      adicClosedFibreThrough I y p = {completedMaximalIdeal I y} →
      0 < completedStalkDepth I F y p) :
    (∀ n : ℕᵒᵖ, IsDepthOneQuotient T ((toImprovedSystem T hT F.obj).app n)) ∧
    (∀ (n : ℕ) (y : X), y ∈ T →
      letI : Module (X.presheaf.stalk y) (TopCat.Presheaf.stalk (C := Ab.{u})
          ((improvedSystem T hT F.obj).obj (op n)).val.presheaf y) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) ((improvedSystem T hT F.obj).obj (op n)).val y
      (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk y) (IsLocalRing.maximalIdeal (X.presheaf.stalk y))
        (TopCat.Presheaf.stalk (C := Ab.{u}) ((improvedSystem T hT F.obj).obj (op n)).val.presheaf
          y)) ∧
    ∃ (G : Stacks.Coherent.CoherentAdicSystems I) (φ : F ⟶ G)
      (ψ : G.obj ⟶ improvedSystem T hT F.obj)
      (P : InverseSequence.ProIso G.obj (improvedSystem T hT F.obj)),
      φ.hom ≫ ψ = toImprovedSystem T hT F.obj ∧
      (∀ m, P.φ m = InverseSequence.tr G.obj (P.αle m) ≫ ψ.app (op m)) ∧
      Epi φ ∧
      ∃ c : ℕ, ∀ n : ℕ, idealPowerMultiple I c ((kernel φ).obj.obj (op n)) = ⊥
```

## Tag 0EJF, a lemma

[Tag 0EJF](https://stacks.math.columbia.edu/tag/0EJF) in the Stacks Project.

**`Stacks.Algebraization.exists_proIso_coherentAdicSystem_canonicalImprovedSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModulesDepthTwoCarrier.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModulesDepthTwoCarrier.lean#L151). The attribute's comment: “the full lemma: under (a)-(e), the canonical map (ℱₙ) ⟶ (ℱ''ₙ), levelwise the improvement along T' ⊆ T, has depth(ℱ''\_\{n,y}) ≥ 1 for y ∈ T and depth(ℱ''\_\{n,y'}) ≥ 2 for y' ∈ T', (ℱ''ₙ) is pro-isomorphic to an object (ℋₙ) of Coh(X, ℐ), and the induced σ : (ℱₙ) ⟶ (ℋₙ) has kernel and cokernel annihilated by a power of ℐ: conclusions (1)-(4)”.

> **Stacks Project, Tag 0EJF.** Let `X` be a Noetherian scheme which locally has a dualizing
> complex, `ℐ` a quasi-coherent ideal sheaf with support `Y`, `(ℱₙ)` an object of `Coh(X, ℐ)`,
> `T' ⊆ T ⊆ Y` subsets stable under specialization and `d ≥ 0` an integer, such that
> * (a) every point has an affine neighbourhood `U` with `cd(Γ(X, U), ℐ(U)) ≤ d`,
> * (b) for `y ∈ T` and a nonmaximal prime `𝔭` of `𝒪_{X,y}^∧` with
>   `V(𝔭) ∩ V(ℐ_y^∧) = {𝔪_y^∧}`, `depth((ℱ_y^∧)_𝔭) > 0`,
> * (c) for `y ∈ T'` and a prime `𝔭 ∉ V(ℐ_y^∧)` of `𝒪_{X,y}^∧` with
>   `V(𝔭) ∩ V(ℐ_y^∧) ≠ {𝔪_y^∧}`, `depth((ℱ_y^∧)_𝔭) ≥ 1` or
>   `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) > 1 + d`,
> * (d) for `y ∈ T'` and a nonmaximal prime `𝔭` of `𝒪_{X,y}^∧` with
>   `V(𝔭) ∩ V(ℐ_y^∧) = {𝔪_y^∧}`, `depth((ℱ_y^∧)_𝔭) > 1`,
> * (e) if `y ⤳ y'` is an immediate specialization of points of `Y` with `y' ∈ T'`, then `y ∈ T`.
>
> Then the canonical map `(ℱₙ) ⟶ (ℱ''ₙ)` (each component the improvement of `ℱₙ` along `T' ⊆ T`
> of [Stacks, Tag 0EI4]) satisfies
> 1. `depth(ℱ''_{n,y}) ≥ 1` for `y ∈ T`,
> 2. `depth(ℱ''_{n,y'}) ≥ 2` for `y' ∈ T'`,
> 3. `(ℱ''ₙ)` is pro-isomorphic to an object `(ℋₙ)` of `Coh(X, ℐ)`,
> 4. the induced morphism `σ : (ℱₙ) ⟶ (ℋₙ)` of `Coh(X, ℐ)` has kernel and cokernel annihilated by
>    a power of `ℐ` (both in `Coh(X, ℐ)` and levelwise).

```lean
theorem exists_proIso_coherentAdicSystem_canonicalImprovedSystem {X : Scheme.{u}}
    [IsNoetherian X] {I : X.IdealSheafData} (hdual : HasDualizingComplexOnAffineCover X)
    (F : Stacks.Coherent.CoherentAdicSystems I) {T T' : Set X}
    (hT : StableUnderSpecialization T) (hT' : StableUnderSpecialization T')
    (hTY : T ⊆ I.support) (hTT' : T' ⊆ T) (d : ℕ)
    (ha : ∀ x : X, ∃ U : X.affineOpens, x ∈ U.1 ∧
      letI : IsNoetherianRing Γ(X, U.1) := IsLocallyNoetherian.component_noetherian U
      Stacks.LocalCohomology.cohomologicalDimension Γ(X, U.1) (I.ideal U)
        (Ideal.fg_of_isNoetherianRing _) ≤ (d : ℤ))
    (hb : ∀ y ∈ T, ∀ p : PrimeSpectrum (completedLocalRing I y),
      p.asIdeal ≠ completedMaximalIdeal I y →
      adicClosedFibreThrough I y p = {completedMaximalIdeal I y} →
      0 < completedStalkDepth I F y p)
    (hc : ∀ y ∈ T', ∀ p : PrimeSpectrum (completedLocalRing I y),
      ¬ completedLocalIdeal I y ≤ p.asIdeal →
      adicClosedFibreThrough I y p ≠ {completedMaximalIdeal I y} →
      1 ≤ completedStalkDepth I F y p ∨
        enatToEInt (completedStalkDepth I F y p) +
            krullDimToEInt (ringKrullDim (completedLocalRing I y ⧸ p.asIdeal)) >
          ((1 + d : ℤ) : EInt))
    (hd : ∀ y ∈ T', ∀ p : PrimeSpectrum (completedLocalRing I y),
      p.asIdeal ≠ completedMaximalIdeal I y →
      adicClosedFibreThrough I y p = {completedMaximalIdeal I y} →
      1 < completedStalkDepth I F y p)
    (himm : ∀ x x' : X, x ∈ I.support → IsImmediateSpecialization x x' → x' ∈ T' → x ∈ T) :
    (∀ (n : ℕᵒᵖ) (x : X),
      letI : Module (X.presheaf.stalk x)
          (TopCat.Presheaf.stalk (C := Ab.{u})
            ((canonicalImprovedSystem hdual F hT hT' hTY himm).obj n).val.presheaf x) :=
        PresheafOfModules.instModuleCarrierStalkCommRingCatCarrierAbPresheafOpensCarrier
          (R := X.presheaf) ((canonicalImprovedSystem hdual F hT hT' hTY himm).obj n).val x
      (x ∈ T → (1 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
          (TopCat.Presheaf.stalk (C := Ab.{u})
            ((canonicalImprovedSystem hdual F hT hT' hTY himm).obj n).val.presheaf x)) ∧
        (x ∈ T' → (2 : ℕ∞) ≤ Module.depth (X.presheaf.stalk x)
          (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
          (TopCat.Presheaf.stalk (C := Ab.{u})
            ((canonicalImprovedSystem hdual F hT hT' hTY himm).obj n).val.presheaf x))) ∧
    (∀ n : ℕᵒᵖ, IsNestedImprovement T T'
      ((toCanonicalImprovedSystem hdual F hT hT' hTY himm).app n)) ∧
    ∃ (H : Stacks.Coherent.CoherentAdicSystems I)
      (e : InverseSequence.ProIso (canonicalImprovedSystem hdual F hT hT' hTY himm) H.obj)
      (σ : F ⟶ H),
      (∀ n : ℕ, (toCanonicalImprovedSystem hdual F hT hT' hTY himm).app (op (e.α n)) ≫ e.φ n =
        F.obj.map (homOfLE (e.αle n)).op ≫ σ.hom.app (op n)) ∧
      (∃ c : ℕ, ∀ n : ℕ, idealPowerMultiple I c ((kernel σ).obj.obj (op n)) = ⊥) ∧
      (∃ c : ℕ, ∀ n : ℕ, idealPowerMultiple I c ((cokernel σ).obj.obj (op n)) = ⊥) ∧
      IsKernelCokernelAnnihilatedByPower I σ.hom
```

## Tag 0EJG, a lemma

[Tag 0EJG](https://stacks.math.columbia.edu/tag/0EJG) in the Stacks Project.

**`Stacks.Algebraization.exists_proIso_coherentAdicSystem_depthThreeImprovedSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModulesDepthThreeCarrier.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/AlgebraizationCoherentFormal/ImprovingFormalModulesDepthThreeCarrier.lean#L66).

> **[Stacks, Tag 0EJG].** Let `A` have a dualizing complex, let `d ≥ cd(A, I)` and let
> `(ℱₙ)` in `Coh(U, I𝒪_U)` satisfy the `(2, 2 + d)`-inequalities. Then there is a map
> `(ℱₙ) ⟶ (ℱ''ₙ)` of inverse systems of coherent `𝒪_U`-modules with
> (1) `depth(ℱ''_{n,y}) + δ^Y_Z(y) ≥ 3` on `U ∩ Y`, (2) `(ℱ''ₙ)` pro-isomorphic to an object
> `(ℋₙ)` of `Coh(U, I𝒪_U)`, compatibly with the maps from `(ℱₙ)`, (3) the induced morphism
> `(ℱₙ) ⟶ (ℋₙ)` with kernel and cokernel annihilated by a power of `I`, both in `Coh(U, I𝒪_U)`
> and termwise, and (4) `Hᵖ(U, ℱ''ₙ)` a finite `A`-module for `p ≤ 1` and all `n`.

```lean
public theorem exists_proIso_coherentAdicSystem_depthThreeImprovedSystem
    (S : AlgebraizationSituation.{u})
    (hdual : ∃ K : DerivedCategory (ModuleCat.{u} S.A), Dualizing.IsDualizingComplex K)
    (d : ℤ) (hd : cohomologicalDimension S.A S.I (Ideal.fg_of_isNoetherianRing S.I) ≤ d)
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (h : SatisfiesDepthInequalities S F 2 (2 + d)) :
    ∃ (F'' : ℕᵒᵖ ⥤ S.U.toScheme.Modules) (τ : F.obj ⟶ F''),
      (∀ n : ℕᵒᵖ, (F''.obj n).IsCoherent) ∧
      (∀ (n : ℕᵒᵖ) (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        (3 : ℕ∞) ≤ Module.depth (S.U.toScheme.presheaf.stalk y)
            (maximalIdeal (S.U.toScheme.presheaf.stalk y)) ((F''.obj n).presheaf.stalk y) +
          S.distanceToZ z) ∧
      (∃ (H : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
        (e : InverseSequence.ProIso F'' H.obj) (σ : F ⟶ H),
        (∀ n : ℕ, τ.app (op (e.α n)) ≫ e.φ n =
          F.obj.map (homOfLE (e.αle n)).op ≫ σ.hom.app (op n)) ∧
        (∃ c : ℕ, ∀ n : ℕ,
          idealPowerMultiple (idealOnOpen S) c ((kernel σ).obj.obj (op n)) = ⊥) ∧
        (∃ c : ℕ, ∀ n : ℕ,
          idealPowerMultiple (idealOnOpen S) c ((cokernel σ).obj.obj (op n)) = ⊥) ∧
        IsKernelCokernelAnnihilatedByPower (idealOnOpen S) σ.hom) ∧
      (∀ (n : ℕᵒᵖ) (p : ℕ), p ≤ 1 →
        Module.Finite S.A ((complementSheafCohomology S.A S.a p).obj (F''.obj n)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.21, Tag 0EJD](https://stacks.math.columbia.edu/tag/0EJD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
