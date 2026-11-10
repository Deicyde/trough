---
declaration: section
origin: cited
lean: Module.exists_open_depth_localization_ge, Module.exists_open_depth_localization_ge_and_finite_exceptional, AlgebraicGeometry.finite_setOf_depth_eq_and_lt_supportDim, Dualizing.annihilator_moduleExtInto_eq_annihilator_localCohomology, Dualizing.moduleExtInto_finite, Dualizing.moduleExtInto_degree_range, Dualizing.supportDim_moduleExtInto_le, Dualizing.depth_eq_iInf_nontrivial_moduleExtInto
statement: formalized
proof: formalized
---

# 51.9 Depth and dimension

Section 51.9 of the Stacks Project, [Tag 0DWW](https://stacks.math.columbia.edu/tag/0DWW). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DWX, a lemma

[Tag 0DWX](https://stacks.math.columbia.edu/tag/0DWX) in the Stacks Project.

**`Module.exists_open_depth_localization_ge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/DepthDimension/DepthAlongIdeal.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/DepthDimension/DepthAlongIdeal.lean#L107).

> **Stacks Project, Tag 0DWX.** If `I ⊆ p` and the depth of the finite module `M` along `I` at
> `p` is `e`, then the localized depth is at least `e` on a nonempty open subset of `V(p)`.

```lean
theorem exists_open_depth_localization_ge
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {M : Type v} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I : Ideal A) (p : PrimeSpectrum A) (_hIp : I ≤ p.asIdeal) (e : ℕ)
    (he : Module.depth (Localization.AtPrime p.asIdeal)
      (Ideal.map (algebraMap A (Localization.AtPrime p.asIdeal)) I)
      (LocalizedModule p.asIdeal.primeCompl M) = (e : ℕ∞)) :
    let depthAt := fun q : PrimeSpectrum A ↦
      Module.depth (Localization.AtPrime q.asIdeal)
        (Ideal.map (algebraMap A (Localization.AtPrime q.asIdeal)) I)
        (LocalizedModule q.asIdeal.primeCompl M)
    ∃ U : Set ↑(PrimeSpectrum.zeroLocus (p.asIdeal : Set A)),
      IsOpen U ∧ U.Nonempty ∧
        ∀ q ∈ U, (e : ℕ∞) ≤ depthAt q.1
```

## Tag 0DWY, a lemma

[Tag 0DWY](https://stacks.math.columbia.edu/tag/0DWY) in the Stacks Project.

**`Module.exists_open_depth_localization_ge_and_finite_exceptional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/DepthDimension/DepthSpecialization.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/DepthDimension/DepthSpecialization.lean#L196).

> **Stacks Project, Tag 0DWY.** If the localization of a finite module over a Noetherian ring
> has finite depth `e` at `p`, then on a nonempty open subset of `V(p)` its depth is at least `e`,
> and is strictly greater than `e` except at finitely many points.

```lean
theorem exists_open_depth_localization_ge_and_finite_exceptional
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    {M : Type v} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (p : PrimeSpectrum A) (e : ℕ)
    (he : Module.depth (Localization.AtPrime p.asIdeal)
      (maximalIdeal (Localization.AtPrime p.asIdeal))
      (LocalizedModule p.asIdeal.primeCompl M) = (e : ℕ∞)) :
    let depthAt := fun q : PrimeSpectrum A ↦
      Module.depth (Localization.AtPrime q.asIdeal)
        (maximalIdeal (Localization.AtPrime q.asIdeal))
        (LocalizedModule q.asIdeal.primeCompl M)
    ∃ U : Set ↑(PrimeSpectrum.zeroLocus (p.asIdeal : Set A)),
      IsOpen U ∧ U.Nonempty ∧
        (∀ q ∈ U, (e : ℕ∞) ≤ depthAt q.1) ∧
        Set.Finite {q | q ∈ U ∧ ¬ (e : ℕ∞) < depthAt q.1}
```

## Tag 0ECN, a lemma

[Tag 0ECN](https://stacks.math.columbia.edu/tag/0ECN) in the Stacks Project.

**`AlgebraicGeometry.finite_setOf_depth_eq_and_lt_supportDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LocalCohomology/DepthDimension/FinitePointsSerre.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LocalCohomology/DepthDimension/FinitePointsSerre.lean#L183).

> **Stacks Project, Tag 0ECN.**  Let `X` be a Noetherian scheme with a dualizing complex `K`,
> let `F` be a coherent `𝒪_X`-module and let `k ≥ 0` be an integer.  If `F` satisfies Serre's
> condition `(Sₖ)`, then there are only finitely many points `x ∈ X` with
>
> `depth(F_x) = k` and `dim Supp(F_x) > k`.

```lean
public theorem finite_setOf_depth_eq_and_lt_supportDim (X : Scheme.{u}) [IsNoetherian X]
    [HasDerivedCategory.{w} X.Modules] {K : DerivedCategory X.Modules}
    (hK : Stacks.Duality.IsDualizingComplex K) (F : X.Modules) [F.IsCoherent] (k : ℕ)
    (hF : SheafHasPropertySk X F k) :
    {x : X |
        Module.depth (X.presheaf.stalk x) (IsLocalRing.maximalIdeal (X.presheaf.stalk x))
            (F.presheaf.stalk x) = (k : ℕ∞) ∧
          (k : WithBot ℕ∞) <
            Module.supportDim (X.presheaf.stalk x) (F.presheaf.stalk x)}.Finite
```

## Tag 0DWZ, a lemma

[Tag 0DWZ](https://stacks.math.columbia.edu/tag/0DWZ) in the Stacks Project.

**`Dualizing.annihilator_moduleExtInto_eq_annihilator_localCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualExtAnnihilator.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualExtAnnihilator.lean#L200). The attribute's comment: “part (5): Ext^{-i}(M, ω) and H^i_m(M) have the same annihilator”.

> **Stacks Project, Tag 0DWZ, part (5).** Let `(A, 𝔪)` be a Noetherian local ring with a
> normalized dualizing complex `ω`, and let `M` be a finite `A`-module. Then the dual Ext module
> `Eⁱ = Ext_A^{-i}(M, ω)` and the local cohomology module `Hⁱ_𝔪(M)` have the same annihilator.
>
> Local duality identifies the `𝔪`-adic completion of `Eⁱ` with the module of `A`-linear maps
> from `Hⁱ_𝔪(M)` to an injective hull of the residue field. Neither completing a finite module
> nor passing to the Matlis dual changes the annihilator, so the two annihilators agree.

```lean
theorem annihilator_moduleExtInto_eq_annihilator_localCohomology
    {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : IsNormalizedDualizingComplex.{u, u} K) (i : ℤ) :
    Module.annihilator A (moduleExtInto M K (-i)) =
      Module.annihilator A
        (Stacks.LocalCohomology.localCohomologyWithSupportIn A
          (PrimeSpectrum.zeroLocus (IsLocalRing.maximalIdeal A : Set A))
          ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A M)) i)
```

**`Dualizing.moduleExtInto_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean#L72). The attribute's comment: “part (1): each Ext^{-i}(M, ω) is a finite A-module”.

> **Stacks Project, Tag 0DWZ, part (1): finiteness.** For a finite module `M` over a
> Noetherian local ring with normalized dualizing complex `ω`, every module
> `Eⁱ = Ext_A^{-i}(M, ω)` is a finite `A`-module.

```lean
theorem moduleExtInto_finite {A : Type u} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    {M : Type (max v u)} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K) (i : ℤ) :
    Module.Finite A (moduleExtInto M K (-i))
```

**`Dualizing.moduleExtInto_degree_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean#L84). The attribute's comment: “part (1): Ext^{-i}(M, ω) vanishes outside 0 ≤ i ≤ dim Supp(M)”.

> **Stacks Project, Tag 0DWZ, part (1): degree range.** For a finite module `M` over a
> Noetherian local ring with normalized dualizing complex `ω`, the module
> `Eⁱ = Ext_A^{-i}(M, ω)` can be nonzero only for `0 ≤ i ≤ dim Supp(M)`; in particular the
> dimension of the support of `M` is then a natural number.

```lean
theorem moduleExtInto_degree_range {A : Type u} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] {M : Type (max v u)} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K) (i : ℤ)
    (hi : Nontrivial (moduleExtInto M K (-i))) :
    ∃ d : ℕ, Module.supportDim A M = (d : WithBot ℕ∞) ∧ i ∈ Set.Icc 0 (d : ℤ)
```

**`Dualizing.supportDim_moduleExtInto_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean#L104). The attribute's comment: “part (2): dim Supp(Ext^{-i}(M, ω)) ≤ i”.

> **Stacks Project, Tag 0DWZ, part (2).** For a finite module `M` over a Noetherian local
> ring with normalized dualizing complex `ω`, the support of `Eⁱ = Ext_A^{-i}(M, ω)` has
> dimension at most `i`; for `i < 0` the module `Eⁱ` vanishes, so its support is empty.

```lean
theorem supportDim_moduleExtInto_le {A : Type u} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] (M : Type (max v u)) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K) (i : ℤ) :
    Module.supportDim A (moduleExtInto M K (-i)) ≤
      if 0 ≤ i then ((i.toNat : ℕ∞) : WithBot ℕ∞) else ⊥
```

**`Dualizing.depth_eq_iInf_nontrivial_moduleExtInto`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualExtDepthDimension.lean#L122). The attribute's comment: “part (3): depth(M) is the least i with Ext^{-i}(M, ω) ≠ 0”.

> **Stacks Project, Tag 0DWZ, part (3).** For a finite module `M` over a Noetherian local
> ring with normalized dualizing complex `ω`, the depth of `M` is the least `i ≥ 0` for which
> `Eⁱ = Ext_A^{-i}(M, ω)` is nonzero. If all these modules vanish, both sides are `⊤`.

```lean
theorem depth_eq_iInf_nontrivial_moduleExtInto {A : Type u} [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] {M : Type (max v u)} [AddCommGroup M] [Module A M] [Module.Finite A M]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K) :
    Module.depth A (IsLocalRing.maximalIdeal A) M =
      ⨅ (i : ℕ) (_ : Nontrivial (moduleExtInto M K (-(i : ℤ)))), (i : ℕ∞)
```

**`Dualizing.mem_support_pi_moduleExtInto_iff_depth_add_ringKrullDim_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualExtSupportDepthCriterion.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualExtSupportDepthCriterion.lean#L383). The attribute's comment: “part (4): p ∈ Supp(E⁰ ⊕ … ⊕ Eⁱ) ↔ depth(M_p) + dim(A/p) ≤ i”.

> **Stacks Project, Tag 0DWZ, part (4).** Let `(A, 𝔪)` be a Noetherian local ring with a
> normalized dualizing complex `ω`, let `M` be a finite `A`-module and write
> `Eⁱ = Ext_A^{-i}(M, ω)`. A prime `𝔭` lies in the support of `E⁰ ⊕ E¹ ⊕ ⋯ ⊕ Eⁱ` — realized as
> the product over `Fin (i + 1)` — exactly when the depth of the localization `M_𝔭` over `A_𝔭`
> plus the dimension of `A / 𝔭` is at most `i`.

```lean
theorem mem_support_pi_moduleExtInto_iff_depth_add_ringKrullDim_le
    {A : Type u} {M : Type (max v u)}
    [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [AddCommGroup M] [Module A M] [Module.Finite A M]
    (K : DerivedCategory (ModuleCat.{max v u} A))
    (hK : IsNormalizedDualizingComplex.{u, v} K)
    (p : PrimeSpectrum A) (i : ℕ) :
    p ∈ Module.support A ((j : Fin (i + 1)) → moduleExtInto M K (-(j : ℤ))) ↔
      ((Module.depth (Localization.AtPrime p.asIdeal)
          (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
          (LocalizedModule p.asIdeal.primeCompl M) : ℕ∞) : WithBot ℕ∞) +
        ringKrullDim (A ⧸ p.asIdeal) ≤ (i : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 51.9, Tag 0DWW](https://stacks.math.columbia.edu/tag/0DWW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
