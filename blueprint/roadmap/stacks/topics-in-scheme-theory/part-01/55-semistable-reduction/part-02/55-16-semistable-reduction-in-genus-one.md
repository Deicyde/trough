---
declaration: section
origin: cited
lean: Stacks.CyclicCover.finite_flat_pushforward_coverMap, Stacks.CyclicCover.nonempty_coverMapArrowIso, Stacks.CyclicCover.finite_etale_genericFibre, Stacks.CyclicCover.globalSections_cover, Stacks.CyclicCover.genus_genericFibre, Stacks.CyclicCover.isRegular_model, Stacks.CyclicCover.specialFibre_eq_pow, Stacks.CyclicCover.ramification_of_semistable
statement: formalized
proof: formalized
---

# 55.16 Semistable reduction in genus one

Section 55.16 of the Stacks Project, [Tag 0CEG](https://stacks.math.columbia.edu/tag/0CEG). 1 tag here is carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CEH, an example

[Tag 0CEH](https://stacks.math.columbia.edu/tag/0CEH) in the Stacks Project.

**`Stacks.CyclicCover.finite_flat_pushforward_coverMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L84). The attribute's comment: “p : X → Z\_R is finite and flat, and p\_*O\_X = Sym*(L\_R)/(φ - π) = O ⊕ L\_R ⊕ … ⊕ L\_R^\{⊗ n-1}; X is built from φ : L^\{⊗ n} ≅ O\_Z through Symⁿ L ≅ L^\{⊗ n}”.

> **`p : X ⟶ Z_R` is finite flat, with `p_* 𝒪_X = ⨁_{i < n} L_R^{⊗ i}`**, the direct sum of
> the pullbacks to `Z_R` of the tensor powers of `L`.

```lean
theorem finite_flat_pushforward_coverMap (hn : 1 ≤ n) :
    IsFinite (coverMap f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X) ∧
      Flat (coverMap f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X) ∧
      Nonempty ((⨁ fun i : Fin n => (Scheme.Modules.pullback (baseChangeFst f (PowerSeries k))).obj
          (tensorPow L i)) ≅
        (Scheme.Modules.pushforward
          (coverMap f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)).obj
          (SheafOfModules.unit _))
```

**`Stacks.CyclicCover.nonempty_coverMapArrowIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L106). The attribute's comment: “p⁻¹(U\_R) = Spec((A ⊗\_k R)[x]/(xⁿ - π f)) for U = Spec A trivializing L by s, with f = φ(s^\{⊗ n}) a unit”.

> **The local description of `p`**: over an affine open `U = Spec A` of `Z` on which `L` is
> trivialized by `s`, with `f = φ(s^{⊗ n})` a unit of `A`,
> `p⁻¹(U_R) = Spec (A ⊗_k R)[x]/(xⁿ - π f)` over `U_R = Spec (A ⊗_k R)`.

```lean
theorem nonempty_coverMapArrowIso (U : Z.affineOpens)
    (b : Module.Basis PUnit.{u + 1} Γ(Z, U.1) Γ(L, U.1)) :
    letI := (sectionsStructure f U.1).hom.toAlgebra
    let fU : Γ(Z, U.1) := φ.hom.app U.1 ((symPowIsoTensorPower f L n).hom.app U.1 (basisPow f U b))
    IsUnit fU ∧
      Nonempty (Arrow.mk (coverMap f (symPowTrivialization f φ) (PowerSeries k)
          PowerSeries.X ∣_ baseChangeOpen f (PowerSeries k) U.1) ≅
        Arrow.mk (Spec.map (CommRingCat.ofHom (algebraMap (Γ(Z, U.1) ⊗[k] PowerSeries k)
          (chartRing k n fU (PowerSeries.X : PowerSeries k))))))
```

**`Stacks.CyclicCover.finite_etale_genericFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L123). The attribute's comment: “the morphism X\_K → Z\_K of generic fibres is finite étale”.

> **The morphism of generic fibres `X_K ⟶ Z_K` is finite étale.**

```lean
theorem finite_etale_genericFibre (hnk : IsUnit (n : k)) :
    IsFinite (coverMapBaseChange f (symPowTrivialization f φ) (PowerSeries.X : PowerSeries k)
        (powerSeriesToLaurent k)) ∧
      Etale (coverMapBaseChange f (symPowTrivialization f φ) (PowerSeries.X : PowerSeries k)
        (powerSeriesToLaurent k))
```

**`Stacks.CyclicCover.globalSections_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L172). The attribute's comment: “H^0(X, O\_X) = R and H^0(X\_K, O\_\{X\_K}) = K”.

> **`H⁰(X, 𝒪_X) = R` and `H⁰(X_K, 𝒪_{X_K}) = K`.**

```lean
theorem globalSections_cover (hn : 1 ≤ n)
    (hord : addOrderOf
      (Stacks.SheafOfModules.picardClass Z.presheaf (structureIsSheaf Z.toRingedSpace) L ‹_›) = n) :
    Function.Bijective
        (coverSnd f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X).appTop ∧
      Function.Bijective (pullback.snd
        (coverSnd f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)
        (Spec.map (CommRingCat.ofHom (powerSeriesToLaurent k).toRingHom))).appTop
```

**`Stacks.CyclicCover.genus_genericFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L185). The attribute's comment: “the genus of X\_K is n(g - 1) + 1, in particular 1 if Z has genus 1”.

> **The genus of `X_K` is `n(g - 1) + 1`**; in particular it is `1` when `Z` has genus `1`.

```lean
theorem genus_genericFibre (hn : 1 ≤ n)
    (hord : addOrderOf
      (Stacks.SheafOfModules.picardClass Z.presheaf (structureIsSheaf Z.toRingedSpace) L ‹_›) = n) :
    (genus (pullback.snd
        (coverSnd f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)
        (Spec.map (CommRingCat.ofHom (powerSeriesToLaurent k).toRingHom))) : ℤ) =
        n * (genus f - 1) + 1 ∧
      (genus f = 1 → genus (pullback.snd
        (coverSnd f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)
        (Spec.map (CommRingCat.ofHom (powerSeriesToLaurent k).toRingHom))) = 1)
```

**`Stacks.CyclicCover.isRegular_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L204). The attribute's comment: “the scheme X is regular”.

> **The scheme `X` is regular.**

```lean
theorem isRegular_model [Smooth f] (hnk : IsUnit (n : k)) :
    IsRegular (cover f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)
```

**`Stacks.CyclicCover.specialFibre_eq_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L212). The attribute's comment: “the special fibre X\_k is n times the reduced special fibre (X\_k)\_red as an effective Cartier divisor”.

> **The special fibre `X_k` is `n` times the reduced special fibre as an effective Cartier
> divisor**: `π 𝒪_X` and its radical are invertible ideals, and `π 𝒪_X = (rad(π 𝒪_X))ⁿ`.

```lean
theorem specialFibre_eq_pow [Smooth f] (hnk : IsUnit (n : k)) :
    Stacks.Divisors.IsEffectiveCartierDivisor (specialFibreIdeal f (symPowTrivialization f φ)) ∧
      Stacks.Divisors.IsEffectiveCartierDivisor
        (specialFibreIdeal f (symPowTrivialization f φ)).radical ∧
      specialFibreIdeal f (symPowTrivialization f φ) =
        (specialFibreIdeal f (symPowTrivialization f φ)).radical ^ n
```

**`Stacks.CyclicCover.ramification_of_semistable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L229). The attribute's comment: “any finite extension K'/K over which X\_K attains semistable reduction has ramification index at least n: v\_\{R'}(π) is a positive multiple of n, for R' the integral closure of R in K'”.

> **Any finite extension `K'/K` over which `X_K` attains semistable reduction has ramification
> index at least `n`**: the valuation `v_{R'}(π)` of `π` in the integral closure `R'` of `R` in
> `K'` is a positive multiple of `n`.

```lean
theorem ramification_of_semistable [IsAlgClosed k] [IsProper f] [Nonempty Z] (hn : 1 ≤ n)
    (K' : Type u) [Field K'] [Algebra (LaurentSeries k) K']
    [FiniteDimensional (LaurentSeries k) K'] [Algebra (PowerSeries k) K']
    [IsScalarTower (PowerSeries k) (LaurentSeries k) K'] :
    haveI := isDiscreteValuationRing_integralClosure (PowerSeries k) (LaurentSeries k) K'
    haveI := _root_.isFractionRing_integralClosure (PowerSeries k) (LaurentSeries k) K'
    (∃ (Y : Scheme.{u}) (q : Y ⟶ Spec (.of (integralClosure (PowerSeries k) K')))
      (e : pullback (coverSnd f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)
          (Spec.map (CommRingCat.ofHom (algebraMap (PowerSeries k) K'))) ≅
        pullback q (Spec.map (CommRingCat.ofHom
          (algebraMap (integralClosure (PowerSeries k) K') K')))),
      Stacks.Models.IsModel (pullback.snd _ _) q e ∧ IsProper q ∧
        IsAtWorstNodalOfRelativeDimensionOne q) →
    ∃ m : ℕ, 0 < m ∧ IsDiscreteValuationRing.addVal (integralClosure (PowerSeries k) K')
      (algebraMap (PowerSeries k) (integralClosure (PowerSeries k) K') PowerSeries.X) =
        (n * m : ℕ)
```

**`Stacks.CyclicCover.no_universal_bound`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/SemistableReduction/CyclicCover/UnboundedRamification.lean#L317). The attribute's comment: “there is no universal bound for the degree of an extension over which a genus 1 curve attains semistable reduction: for every B there is a curve X\_K over K = k((π)) with H⁰(X\_K, O) = K and genus 1 such that every finite K'/K over which X\_K attains semistable reduction has [K' : K] > B”.

> **There is no universal bound on the degree of an extension over which a genus one curve
> attains semistable reduction.** For every `B` there is a curve `X_K` over `K = k((π))` with
> `H⁰(X_K, 𝒪) = K` and genus `1`, namely the generic fibre of the cyclic cover of a genus one curve
> `Z` by an invertible module of prime order `ℓ > B`, such that every finite extension `K'/K` over
> which `X_K` attains semistable reduction has `[K' : K] > B`.

```lean
theorem no_universal_bound (k : Type u) [Field k] [IsAlgClosed k] (B : ℕ) :
    ∃ (Z : Scheme.{u}) (f : Z ⟶ Spec (.of k)) (_ : IsCurve k f) (_ : IsProjectiveVariety k f)
      (_ : Smooth f) (L : Z.Modules)
      (_ : SheafOfModules.IsInvertible Z.sheaf.obj Z.ringCatSheaf.property L) (n : ℕ)
      (φ : tensorPow L n ≅ SheafOfModules.unit Z.ringCatSheaf),
      genus (pullback.snd (coverSnd f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)
        (Spec.map (CommRingCat.ofHom (powerSeriesToLaurent k).toRingHom))) = 1 ∧
      Function.Bijective (pullback.snd (coverSnd f (symPowTrivialization f φ) (PowerSeries k)
        PowerSeries.X) (Spec.map (CommRingCat.ofHom (powerSeriesToLaurent k).toRingHom))).appTop ∧
      ∀ (K' : Type u) [Field K'] [Algebra (LaurentSeries k) K']
        [FiniteDimensional (LaurentSeries k) K'] [Algebra (PowerSeries k) K']
        [IsScalarTower (PowerSeries k) (LaurentSeries k) K'],
        haveI := isDiscreteValuationRing_integralClosure (PowerSeries k) (LaurentSeries k) K'
        haveI := _root_.isFractionRing_integralClosure (PowerSeries k) (LaurentSeries k) K'
        (∃ (Y : Scheme.{u}) (q : Y ⟶ Spec (.of (integralClosure (PowerSeries k) K')))
          (e : pullback (coverSnd f (symPowTrivialization f φ) (PowerSeries k) PowerSeries.X)
              (Spec.map (CommRingCat.ofHom (algebraMap (PowerSeries k) K'))) ≅
            pullback q (Spec.map (CommRingCat.ofHom
              (algebraMap (integralClosure (PowerSeries k) K') K')))),
          Stacks.Models.IsModel (pullback.snd _ _) q e ∧ IsProper q ∧
            IsAtWorstNodalOfRelativeDimensionOne q) →
        B < Module.finrank (LaurentSeries k) K'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 55.16, Tag 0CEG](https://stacks.math.columbia.edu/tag/0CEG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
