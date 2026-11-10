---
declaration: section
origin: cited
lean: Stacks.Algebraization.isIso_zeroSchemeComparison_of_isProper, Stacks.Algebraization.isIso_zeroSchemeComparison_of_depthAddDim_gt, Stacks.Algebraization.isIso_openNeighbourhoodComparison_of_depthAddDim_gt, Stacks.Algebraization.isIso_openComparison_of_depthAddDim_gt, Stacks.Algebraization.isIso_zeroSchemeComparison_zero_of_isCohenMacaulay_surface, Stacks.Algebraization.isIso_zeroSchemeComparison_of_isCohenMacaulay_threefold, Stacks.Algebraization.isIso_zeroSchemeComparison_zero_of_isNormal, Stacks.Algebraization.isIso_zeroSchemeComparison_zero_of_cohenMacaulaySurface
statement: formalized
proof: formalized
---

# 52.28 Application to Lefschetz theorems

Section 52.28 of the Stacks Project, [Tag 0EL0](https://stacks.math.columbia.edu/tag/0EL0). 7 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EL1, a proposition

[Tag 0EL1](https://stacks.math.columbia.edu/tag/0EL1) in the Stacks Project.

**`Stacks.Algebraization.isIso_zeroSchemeComparison_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzZeroSchemeComparison.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzZeroSchemeComparison.lean#L71). The attribute's comment: “The tower Qₙ is indexed from n = 0 and Qₙ is cut out by the n-th power of the ideal sheaf of Q = Z(s), which is the ideal sheaf of Z(sⁿ); the zeroth term is empty and does not change the limit. Depth and dimension are compared in the extended integers.”.

> **Stacks Tag 0EL1.** Let `k` be a field, `P` a proper scheme over `k`, `𝓛` an ample invertible
> `𝒪_P`-module, `s ∈ Γ(P, 𝓛)` with zero scheme `Q` and `𝓕` a coherent `𝒪_P`-module. If
> `depth(𝓕_p) + dim({p}‾) > σ` at every `p ∈ P ∖ Q`, then the comparison map
> `Hⁱ(P, 𝓕) → lim Hⁱ(Qₙ, 𝓕ₙ)` is an isomorphism for `0 ≤ i < σ`.

```lean
theorem isIso_zeroSchemeComparison_of_isProper (k : Type u) [Field k] {X : Scheme.{u}}
    (π : X ⟶ Spec (.of k)) [IsProper π] (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L]
    (hL : Stacks.Ample.IsAmple X L) (s : Γ(L, ⊤)) (F : X.Modules) [F.IsCoherent] (σ : ℤ)
    (hdepth : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) →
      enatToEInt (sheafDepthAt F x) + krullDimToEInt (dimClosureAt X x) > (σ : EInt))
    (i : ℕ) (hi : (i : ℤ) < σ) :
    haveI : F.IsQuasicoherent := isQuasicoherent_of_isCoherent F
    IsIso (zeroSchemeComparison X L s F i)
```

**`Stacks.Algebraization.isIso_zeroSchemeComparison_of_depthAddDim_gt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraization.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraization.lean#L244). The attribute's comment: “H^i(P,F) -> lim H^i(Q\_n,F\_n) is an isomorphism for i < sigma, from depth(F\_p) + dim(closure\{p}) > sigma off the zero scheme of s; carried: the punctured-cone fibre dichotomy (hsplit, hproj), the section ring data A, I, fam, f, M (clause (1) of 0B5T, hence 02O5/02O6, is absent from this library), and the algebraization square halg identifying the comparison map with that of 0EKM via 0EKH”.

> **Stacks Project, Tag 0EL1 (Proposition 52.28.1).** Let `P` be a scheme, `L` an invertible
> `𝒪_P`-module, `s` a global section of `L` with zero scheme `Q`, let `Qₙ` be the `n`-th
> infinitesimal neighbourhood of `Q` in `P`, let `𝓕` be a quasi-coherent `𝒪_P`-module with
> restrictions `𝓕ₙ` to `Qₙ`, and let `σ` be an integer with
>
> `depth(𝓕_p) + dim({p}‾) > σ`
>
> at every point `p` of `P` outside `Q`. Then `Hⁱ(P, 𝓕) ⟶ lim Hⁱ(Qₙ, 𝓕ₙ)` is an isomorphism for
> every `0 ≤ i < σ`.
>
> The depth–dimension hypothesis is `hdepth` and it is the hypothesis of the tag, read with the
> depth of a module at a point of [Stacks, Tag 0341] part (1) and the dimension of the closure of
> a point. Three inputs are carried; see the module documentation for why each is
> unavailable.
>
> * `hsplit`, with `hproj`: the fibre dichotomy of the punctured cone `π|_U`, which rests on
>   `π|_U` being smooth of relative dimension one. This is what transports `hdepth` from `P` to
>   `Spec A`, and `hproj` says that the primes of `A` outside `V(I)` lie over `P ∖ Q`.
> * the section ring data `A`, `I`, `fam`, `f` and `M`, with `A` a Noetherian `k`-algebra of
>   finite type which is `f`-adically complete and `M` finite: clause (1) of [Stacks, Tag 0B5T] is
>   not in this library, so the finite generation of the section ring cannot be produced here.
> * `halg`: the algebraization square identifying the geometric comparison map with the one of
>   [Stacks, Tag 0EKM].

```lean
theorem isIso_zeroSchemeComparison_of_depthAddDim_gt
    (k : Type u) [Field k] (X : Scheme.{u}) (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] (s : Γ(L, ⊤)) (F : X.Modules) [F.IsQuasicoherent]
    (σ : ℕ)
    (hdepth : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) →
      enatToEInt (sheafDepthAt F x) + krullDimToEInt (dimClosureAt X x) > ((σ : ℤ) : EInt))
    (A : Type u) [CommRing A] [IsNoetherianRing A] [Algebra k A] [Algebra.FiniteType k A]
    (M : Type u) [AddCommGroup M] [Module A M] [Module.Finite A M]
    (I : Ideal A) (hI : I.FG) {r : ℕ} (fam : Fin r → A)
    (hfam : Ideal.span (Set.range fam) = I) (f : A) (hf : f ∈ I)
    [IsAdicComplete (Ideal.span {f}) A]
    (proj : PrimeSpectrum A → X)
    (hproj : ∀ p : PrimeSpectrum A, p ∉ PrimeSpectrum.zeroLocus (I : Set A) →
      proj p ∉ ((zeroScheme X L s).support : Set X))
    (hsplit : ∀ p : PrimeSpectrum A, p ∉ PrimeSpectrum.zeroLocus (I : Set A) →
      ∀ q : PrimeSpectrum A, q ∈ PrimeSpectrum.zeroLocus (I : Set A) →
      p.asIdeal ≤ q.asIdeal →
      (localizedDepth A M p = sheafDepthAt F (proj p) ∧
          relativeDimAt A p q = dimClosureAt X (proj p) + 1) ∨
        (localizedDepth A M p = sheafDepthAt F (proj p) + 1 ∧
          relativeDimAt A p q = dimClosureAt X (proj p)))
    (halg : ∀ i : ℕ, i < σ →
      ∃ (e₁ : Hgroup X.ringCatSheaf ⊤ i F ≃+
          (complementCohomologyFunctor fam (i : ℤ)).obj (ModuleCat.of A M))
        (e₂ : ↥(limit (IdealTower.cohomologyTower (zeroSchemeTowerIdeal X L s)
            (zeroSchemeTowerIdeal_succ_le X L s) F i)) ≃+
          ↥(Stacks.ProZero.towerSections
            (HigherComplementTower.quotientCohomologyTower fam f (ModuleCat.of A M) (i : ℤ))
            (HigherComplementTower.quotientCohomologyTransition fam f (ModuleCat.of A M)
              (i : ℤ)))),
          ∀ x : Hgroup X.ringCatSheaf ⊤ i F,
            e₂ (zeroSchemeComparison X L s F i x) =
              HigherComplementTower.toTowerSections fam f (ModuleCat.of A M) (i : ℤ) (e₁ x))
    (i : ℕ) (hi : i < σ) :
    IsIso (zeroSchemeComparison X L s F i)
```

## Tag 0EL2, a lemma

[Tag 0EL2](https://stacks.math.columbia.edu/tag/0EL2) in the Stacks Project.

**`Stacks.Algebraization.isIso_openNeighbourhoodComparison_of_depthAddDim_gt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraizationApplications.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraizationApplications.lean#L284). The attribute's comment: “Gamma(V,F) -> lim Gamma(Y\_n,F\_n) is an isomorphism for every open V containing Y = Z(s), from depth(F\_x) + dim(closure\{x}) > 1 off Y; carried: the input of 0EL1 (hin) and the bijectivity of Gamma(X,F) -> Gamma(V,F) (hV.isIso\_Hrestrict)”.

> **Stacks Project, Tag 0EL2 (Lemma 52.28.2).** Let `k` be a field, `X` a scheme proper over
> `k`, `L` an ample invertible `𝒪_X`-module, `s` a global section of `L`, `Y = Z(s)` its zero
> scheme with `n`-th infinitesimal neighbourhood `Yₙ = Z(sⁿ)`, and `𝓕` a coherent `𝒪_X`-module
> with
>
> `depth(𝓕_x) + dim({x}‾) > 1`
>
> at every `x ∈ X ∖ Y`. Then `Γ(V, 𝓕) ⟶ lim Γ(Yₙ, 𝓕ₙ)` is an isomorphism for every open subscheme
> `V ⊆ X` containing `Y`.
>
> The displayed hypothesis is the hypothesis of [Stacks, Tag 0EL1] at `σ = 1`, and the conclusion
> for `V = X` is that tag in degree `i = 0 < 1`. The map on `V` is `c`, characterized — uniquely,
> restriction being bijective — by its composite with restriction from `X` being the comparison
> map of [Stacks, Tag 0EL1].
>
> Two things are carried: the input `hin` of [Stacks, Tag 0EL1], and the bijectivity of
> `Γ(X, 𝓕) ⟶ Γ(V, 𝓕)`, which is the field
> `Stacks.Algebraization.OpenNeighbourhoodSections.isIso_Hrestrict` and is the whole content of
> this lemma beyond the proposition; see that structure for the source's argument and for the two
> library gaps it runs through.

```lean
theorem isIso_openNeighbourhoodComparison_of_depthAddDim_gt
    {k : Type u} [Field k] {X : Scheme.{u}} (fX : X ⟶ Spec (CommRingCat.of k)) [IsProper fX]
    {L : X.Modules} [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L)
    {s : Γ(L, ⊤)} {F : X.Modules} [F.IsQuasicoherent]
    (hdepth : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) →
      enatToEInt (sheafDepthAt F x) + krullDimToEInt (dimClosureAt X x) > ((1 : ℤ) : EInt))
    {A : Type u} [CommRing A] [IsNoetherianRing A] [Algebra k A] [Algebra.FiniteType k A]
    {M : Type u} [AddCommGroup M] [Module A M] [Module.Finite A M]
    {I : Ideal A} {r : ℕ} {fam : Fin r → A} {f : A} [IsAdicComplete (Ideal.span {f}) A]
    {proj : PrimeSpectrum A → X}
    (hin : ZeroSchemeAlgebraizationInput k X L s F 1 A M I fam f proj)
    {V : X.Opens} (hV : OpenNeighbourhoodSections k fX L hL s F V)
    (c : Hgroup X.ringCatSheaf V 0 F ⟶
      limit (IdealTower.cohomologyTower (zeroSchemeTowerIdeal X L s)
        (zeroSchemeTowerIdeal_succ_le X L s) F 0))
    (hc : Hrestrict X.ringCatSheaf (le_top : V ≤ ⊤) 0 F ≫ c = zeroSchemeComparison X L s F 0) :
    IsIso c
```

**`Stacks.Algebraization.isIso_openComparison_of_depthAddDim_gt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/ZeroSchemeOpenNeighbourhood.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/ZeroSchemeOpenNeighbourhood.lean#L378). The attribute's comment: “Gamma(V,F) -> lim Gamma(Y\_n,F\_n) is an isomorphism for every open V containing Y = Z(s), for F coherent on X proper over a field with depth(F\_x) + dim(closure\{x}) > 1 off Y; Gamma is degree-zero cohomology and Y\_n is cut out by the n-th power of the ideal of Y”.

> **Stacks Project, Tag 0EL2 (Lemma 52.28.2).** Let `k` be a field, `X` a scheme proper over
> `k`, `L` an ample invertible `𝒪_X`-module, `s` a global section of `L`, `Y = Z(s)` its zero
> scheme with `n`-th infinitesimal neighbourhood `Yₙ`, and `𝓕` a coherent `𝒪_X`-module with
> `depth(𝓕_x) + dim({x}‾) > 1` at every `x ∈ X ∖ Y`. Then `Γ(V, 𝓕) ⟶ lim Γ(Yₙ, 𝓕ₙ)` is an
> isomorphism for every open subscheme `V ⊆ X` containing `Y`.
>
> For `V = X` this is [Stacks, Tag 0EL1] at `σ = 1` in degree `0`
> (`Stacks.Algebraization.isIso_zeroSchemeComparison_of_isProper`). Restriction from `X` to `V`
> followed by the comparison over `V` is the comparison over `X`
> (`Stacks.Algebraization.IdealTower.Hrestrict_comp_openComparison`), and restriction is bijective
> because every point of `X ∖ V` is closed with `depth ≥ 2` there
> (`Stacks.Algebraization.isIso_Hrestrict_zero_of_depthAddDim_gt`).

```lean
theorem isIso_openComparison_of_depthAddDim_gt (k : Type u) [Field k] {X : Scheme.{u}}
    (fX : X ⟶ Spec (CommRingCat.of k)) [IsProper fX] (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L) (s : Γ(L, ⊤))
    (F : X.Modules) [F.IsCoherent]
    (hdepth : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) →
      enatToEInt (sheafDepthAt F x) + krullDimToEInt (dimClosureAt X x) > ((1 : ℤ) : EInt))
    (V : X.Opens) (hV : ((zeroScheme X L s).support : Set X) ⊆ V) :
    haveI : F.IsQuasicoherent := isQuasicoherent_of_isCoherent F
    IsIso (IdealTower.openComparison (zeroSchemeTowerIdeal X L s)
      (zeroSchemeTowerIdeal_succ_le X L s) F
      (fun n => (support_zeroSchemeTowerIdeal_subset L s n).trans hV))
```

## Tag 0EL3, an example

[Tag 0EL3](https://stacks.math.columbia.edu/tag/0EL3) in the Stacks Project.

**`Stacks.Algebraization.isIso_zeroSchemeComparison_zero_of_isCohenMacaulay_surface`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzCohenMacaulayVariety.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzCohenMacaulayVariety.lean#L193). The attribute's comment: “clause (2): on a Cohen-Macaulay proper surface over k, H^0(X,E) -> lim H^0(Y\_n,E\_n) is an isomorphism, for E finite locally free and Y the zero scheme of a section of an ample invertible module”.

> **Stacks Project, Tag 0EL3 (Example 52.28.3), clause (2).** Let `k` be a field, `X` a proper
> variety over `k`, `L` an ample invertible `𝒪_X`-module (the source's `𝒪_X(Y)`), `s` a global
> section of `L` with zero scheme `Y` and `n`-th infinitesimal neighbourhood `Yₙ`, and `𝓔` a finite
> locally free `𝒪_X`-module. If `X` is a Cohen–Macaulay surface, then
>
> `H⁰(X, 𝓔) ⟶ lim H⁰(Yₙ, 𝓔ₙ)`
>
> is an isomorphism.

```lean
theorem isIso_zeroSchemeComparison_zero_of_isCohenMacaulay_surface
    {k : Type u} [Field k] {X : Scheme.{u}} (fX : X ⟶ Spec (.of k)) [IsProperVariety k fX]
    {L : X.Modules} [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L)
    (s : Γ(L, ⊤)) (E : X.Modules)
    [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E]
    (hCM : IsCohenMacaulay X) (hdim : topologicalKrullDim X = 2) :
    haveI := Stacks.AlgebraicGeometry.CoherenceCriteria.isQuasicoherent_of_isFiniteLocallyFree E
    IsIso (zeroSchemeComparison X L s E 0)
```

**`Stacks.Algebraization.isIso_zeroSchemeComparison_of_isCohenMacaulay_threefold`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzCohenMacaulayVariety.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzCohenMacaulayVariety.lean#L214). The attribute's comment: “clause (3): on a Cohen-Macaulay proper threefold over k, H^0(X,E) -> lim H^0(Y\_n,E\_n) and H^1(X,E) -> lim H^1(Y\_n,E\_n) are isomorphisms, for E finite locally free and Y the zero scheme of a section of an ample invertible module”.

> **Stacks Project, Tag 0EL3 (Example 52.28.3), clause (3).** In the situation of clause (2),
> if `X` is a Cohen–Macaulay threefold then both
>
> `H⁰(X, 𝓔) ⟶ lim H⁰(Yₙ, 𝓔ₙ)` and `H¹(X, 𝓔) ⟶ lim H¹(Yₙ, 𝓔ₙ)`
>
> are isomorphisms.

```lean
theorem isIso_zeroSchemeComparison_of_isCohenMacaulay_threefold
    {k : Type u} [Field k] {X : Scheme.{u}} (fX : X ⟶ Spec (.of k)) [IsProperVariety k fX]
    {L : X.Modules} [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L)
    (s : Γ(L, ⊤)) (E : X.Modules)
    [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E]
    (hCM : IsCohenMacaulay X) (hdim : topologicalKrullDim X = 3) :
    haveI := Stacks.AlgebraicGeometry.CoherenceCriteria.isQuasicoherent_of_isFiniteLocallyFree E
    IsIso (zeroSchemeComparison X L s E 0) ∧ IsIso (zeroSchemeComparison X L s E 1)
```

**`Stacks.Algebraization.isIso_zeroSchemeComparison_zero_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzCohenMacaulayVariety.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/LefschetzCohenMacaulayVariety.lean#L239). The attribute's comment: “the normal case: on a normal proper variety over k of dimension at least two (the normal surface of clause (2), the normal threefold of the closing remark), H^0(X,E) -> lim H^0(Y\_n,E\_n) is an isomorphism”.

> **Stacks Project, Tag 0EL3 (Example 52.28.3), the normal case.** In the situation of
> clause (2), if `X` is normal of dimension at least two, then
>
> `H⁰(X, 𝓔) ⟶ lim H⁰(Yₙ, 𝓔ₙ)`
>
> is an isomorphism. At dimension two this is the source's "for example normal" in clause (2); at
> dimension three it is the closing remark that on a normal threefold the result holds for `H⁰`.
> A normal scheme satisfies `(S₂)` (Serre's criterion, [Stacks, Tag 031S]), which is the pattern at
> `d = 2`.

```lean
theorem isIso_zeroSchemeComparison_zero_of_isNormal
    {k : Type u} [Field k] {X : Scheme.{u}} (fX : X ⟶ Spec (.of k)) [IsProperVariety k fX]
    {L : X.Modules} [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L)
    (s : Γ(L, ⊤)) (E : X.Modules)
    [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E]
    [IsNormal X] (hdim : ((2 : ℕ) : WithBot ℕ∞) ≤ topologicalKrullDim X) :
    haveI := Stacks.AlgebraicGeometry.CoherenceCriteria.isQuasicoherent_of_isFiniteLocallyFree E
    IsIso (zeroSchemeComparison X L s E 0)
```

**`Stacks.Algebraization.isIso_zeroSchemeComparison_zero_of_cohenMacaulaySurface`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraizationApplications.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraizationApplications.lean#L360). The attribute's comment: “clause (2): on a Cohen-Macaulay (for example normal) surface, H^0(X,E) -> lim H^0(Y\_n,E\_n) is an isomorphism; the depth-dimension bound is proved from the Cohen-Macaulay condition and the dimension formula, hin bundles the three inputs of 0EL1”.

> **Stacks Project, Tag 0EL3 (Example 52.28.3), clause (2).** Let `k` be a field, `X` a proper
> variety over `k`, `L` an ample invertible `𝒪_X`-module — the source's `𝒪_X(Y)` — `s` a global
> section with zero scheme `Y` and `n`-th infinitesimal neighbourhood `Yₙ`, and `𝓔` a finite
> locally free `𝒪_X`-module. If `X` is a Cohen–Macaulay surface, for example a normal one, then
>
> `H⁰(X, 𝓔) ⟶ lim H⁰(Yₙ, 𝓔ₙ)`
>
> is an isomorphism.
>
> This is the general pattern at `d = 2`, hence `σ = 1` and the single degree `i = 0`: the
> Cohen–Macaulay condition and the dimension `2` supply the depth–dimension bound through
> `Stacks.Algebraization.intCast_le_sheafDepthAt_add_dimClosureAt_of_isCohenMacaulay`. The
> remaining hypothesis `hin` is the input of [Stacks, Tag 0EL1].

```lean
theorem isIso_zeroSchemeComparison_zero_of_cohenMacaulaySurface
    {k : Type u} [Field k] {X : Scheme.{u}} (fX : X ⟶ Spec (CommRingCat.of k))
    [IsProperVariety k fX]
    {L : X.Modules} [Stacks.Ample.IsInvertibleModule X L] {s : Γ(L, ⊤)} {E : X.Modules}
    [E.IsQuasicoherent] [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E]
    (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hdim : topologicalKrullDim X = ((2 : ℕ) : WithBot ℕ∞))
    {A : Type u} [CommRing A] [IsNoetherianRing A] [Algebra k A] [Algebra.FiniteType k A]
    {M : Type u} [AddCommGroup M] [Module A M] [Module.Finite A M]
    {I : Ideal A} {r : ℕ} {fam : Fin r → A} {f : A} [IsAdicComplete (Ideal.span {f}) A]
    {proj : PrimeSpectrum A → X}
    (hin : ZeroSchemeAlgebraizationInput k X L s E 1 A M I fam f proj) :
    IsIso (zeroSchemeComparison X L s E 0)
```

**`Stacks.Algebraization.isIso_zeroSchemeComparison_of_cohenMacaulayThreefold`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraizationApplications.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/SectionPowerAlgebraizationApplications.lean#L390). The attribute's comment: “clause (3): on a Cohen-Macaulay threefold, H^i(X,E) -> lim H^i(Y\_n,E\_n) is an isomorphism for i = 0 and i = 1; the depth-dimension bound is proved from the Cohen-Macaulay condition and the dimension formula, hin bundles the three inputs of 0EL1”.

> **Stacks Project, Tag 0EL3 (Example 52.28.3), clause (3).** In the situation of clause (2),
> if `X` is a Cohen–Macaulay threefold then both
>
> `H⁰(X, 𝓔) ⟶ lim H⁰(Yₙ, 𝓔ₙ)` and `H¹(X, 𝓔) ⟶ lim H¹(Yₙ, 𝓔ₙ)`
>
> are isomorphisms.
>
> This is the general pattern at `d = 3`, hence `σ = 2` and the two degrees `i = 0, 1`. The
> source's closing remark that a *normal* threefold still gives `H⁰` is the general pattern at
> `d = 2` applied to it: a normal local ring has depth at least `min(2, dim)`, so the bound `2`
> holds although the dimension is three.

```lean
theorem isIso_zeroSchemeComparison_of_cohenMacaulayThreefold
    {k : Type u} [Field k] {X : Scheme.{u}} (fX : X ⟶ Spec (CommRingCat.of k))
    [IsProperVariety k fX]
    {L : X.Modules} [Stacks.Ample.IsInvertibleModule X L] {s : Γ(L, ⊤)} {E : X.Modules}
    [E.IsQuasicoherent] [_root_.AlgebraicGeometry.SheafOfModules.IsFiniteLocallyFree.{u, u, u} E]
    (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hdim : topologicalKrullDim X = ((3 : ℕ) : WithBot ℕ∞))
    {A : Type u} [CommRing A] [IsNoetherianRing A] [Algebra k A] [Algebra.FiniteType k A]
    {M : Type u} [AddCommGroup M] [Module A M] [Module.Finite A M]
    {I : Ideal A} {r : ℕ} {fam : Fin r → A} {f : A} [IsAdicComplete (Ideal.span {f}) A]
    {proj : PrimeSpectrum A → X}
    (hin : ZeroSchemeAlgebraizationInput k X L s E 2 A M I fam f proj)
    (i : ℕ) (hi : i < 2) :
    IsIso (zeroSchemeComparison X L s E i)
```

## Tag 0EL4, a lemma

[Tag 0EL4](https://stacks.math.columbia.edu/tag/0EL4) in the Stacks Project.

**`Stacks.Algebraization.exists_finite_graded_proIso_completion_of_canonicallyExtends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/GradedAlgebraization.lean, line 744](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/GradedAlgebraization.lean#L744).

> **Stacks Project, Tag 0EL4.** In the algebraization situation (Situation 0EHC) let `A` be
> graded with irrelevant ideal `𝔞 = A₊` and `I` homogeneous, let `(ℱₙ)` be an object of
> `Coh(U, I𝒪_U)` presented as `(M̃ₙ|_U)` by an inverse system `(Mₙ)` of graded `A`-modules, and
> suppose `(ℱₙ)` extends canonically to `X = Spec(A)`. Then there is a finite graded `A`-module `N`
> such that
>
> * (a) the inverse systems `(N/IⁿN)` and `(Mₙ)` are pro-isomorphic in the category of graded
>   `A`-modules modulo `A₊`-power torsion modules, and
> * (b) `(ℱₙ)` is the completion of the coherent module associated to `N`.
>
> The category of graded `A`-modules modulo `A₊`-power torsion modules is the localization of
> `GradedModuleCat` at the maps with `A₊`-power torsion kernel and cokernel
> (`GradedModuleCat.isoModTorsion`), and the pro-objects of the two inverse systems composed with
> the localization functor are presented as colimits of representables, as in
> `Stacks.ProObject.hasProLadder`. The systems are indexed from `0`: the term `n` of `(Mₙ)` and of
> `(ℱₙ)` is the source's term `n + 1`, and the term `n` of the adic quotients is `N/Iⁿ⁺¹N`
> (`GradedModuleCat.adicQuotients`). The coherent module associated to `N` is restricted to `U`
> before completing, `(ℱₙ)` living on `U`.
>
> The restriction maps `Mₙ → Γ(U, ℱₙ)` become isomorphisms in the quotient category, and
> `(Γ(U, ℱₙ))` is linked to `(N/Iⁿ⁺¹N)` by a ladder of degree-preserving maps
> (`Stacks.Algebraization.exists_finite_graded_ladder_of_canonicallyExtends`), which is a
> pro-isomorphism of graded modules (`Stacks.ProObject.nonempty_colimitYonedaIso_of_hasProLadder`)
> and stays one after localizing.

```lean
public theorem exists_finite_graded_proIso_completion_of_canonicallyExtends
    (S : AlgebraizationSituation.{u})
    {σ : Type v} [SetLike σ S.A] [AddSubgroupClass σ S.A] {𝒜 : ℕ → σ} [GradedRing 𝒜]
    (hirr : S.a = (HomogeneousIdeal.irrelevant 𝒜).toIdeal) (hIhom : S.I.IsHomogeneous 𝒜)
    (M : ℕᵒᵖ ⥤ GradedModuleCat.{u, u, v} 𝒜)
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hpres : Nonempty (F.obj ≅ M ⋙ GradedModuleCat.toModuleCat 𝒜 ⋙ tilde.functor (.of S.A) ⋙
      Scheme.Modules.restrictFunctor S.U.ι))
    (hext : CanonicallyExtends S F) :
    ∃ (N : GradedModuleCat.{u, u, v} 𝒜) (hN : Module.Finite S.A N.carrier),
      Nonempty (colimit ((GradedModuleCat.adicQuotients 𝒜 N S.I hIhom ⋙
          (GradedModuleCat.isoModTorsion 𝒜 (HomogeneousIdeal.irrelevant 𝒜).toIdeal).Q).op ⋙
            yoneda) ≅
        colimit ((M ⋙
          (GradedModuleCat.isoModTorsion 𝒜 (HomogeneousIdeal.irrelevant 𝒜).toIdeal).Q).op ⋙
            yoneda)) ∧
      Nonempty ((completionFunctor S.U.toScheme (idealOnOpen S)).obj
          (restrictCoherentModules S.U.ι
            (tildeCoherentModule S (ModuleCat.of S.A N.carrier) hN)) ≅ F)
```

**`Stacks.Algebraization.exists_finite_graded_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzGradedAlgebraization.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzGradedAlgebraization.lean#L161). The attribute's comment: “(a) and (b); graded Gm-descent (0EKL) and the 0BK0 comparison hypothesised”.

> In the algebraization situation of a graded ring `A` whose irrelevant ideal is `𝔞` and whose
> ideal `I` is homogeneous, let `(Mₙ)` be the inverse system of graded modules presenting a coherent
> formal module on `U`, let `(Nₙ)` be the graded inverse system attached to its canonical extension,
> and let `(Mₙ) → (Nₙ)` be a degree-preserving comparison with `𝔞`-power torsion kernel and cokernel.
> Then there is a finite graded `A`-module `N` with `N/IⁿN ≃ Nₙ` compatibly with the transition maps,
> and `(Mₙ)` maps to the inverse system `(N/IⁿN)` by degree-preserving maps with `𝔞`-power torsion
> kernel and cokernel.

```lean
public theorem exists_finite_graded_algebraization (S : AlgebraizationSituation.{u})
    {σ : Type v} [SetLike σ S.A] [AddSubmonoidClass σ S.A] {𝒜 : ℕ → σ} [GradedRing 𝒜]
    (hirr : S.a = (HomogeneousIdeal.irrelevant 𝒜).toIdeal) (hIhom : S.I.IsHomogeneous 𝒜)
    {M : ℕ → Type w} [∀ n, AddCommGroup (M n)] [∀ n, Module S.A (M n)]
    (ℳ : ∀ n, ℤ → AddSubgroup (M n)) [∀ n, DirectSum.Decomposition (ℳ n)]
    (s : ∀ n, M (n + 1) →ₗ[S.A] M n)
    {N : ℕ → Type w} [∀ n, AddCommGroup (N n)] [∀ n, Module S.A (N n)]
    [∀ n, Module.Finite S.A (N n)]
    (𝒩 : ∀ n, ℤ → AddSubgroup (N n)) [∀ n, DirectSum.Decomposition (𝒩 n)]
    (h𝒩 : ∀ (n i : ℕ) (d : ℤ) (a : S.A) (x : N n), a ∈ 𝒜 i → x ∈ 𝒩 n d → a • x ∈ 𝒩 n (i + d))
    (t : ∀ n, N (n + 1) →ₗ[S.A] N n)
    (ht : ∀ (n : ℕ) (d : ℤ) (x : N (n + 1)), x ∈ 𝒩 (n + 1) d → t n x ∈ 𝒩 n d)
    (htsurj : ∀ n, Function.Surjective (t n))
    (htker : ∀ n, LinearMap.ker (t n) = S.I ^ n • (⊤ : Submodule S.A (N (n + 1))))
    (c : ∀ n, M n →ₗ[S.A] N n)
    (hc : ∀ (n : ℕ) (d : ℤ) (x : M n), x ∈ ℳ n d → c n x ∈ 𝒩 n d)
    (hcs : ∀ n, (t n).comp (c (n + 1)) = (c n).comp (s n))
    (hcker : ∀ n, IsIPowerTorsion S.A (LinearMap.ker (c n)) S.a)
    (hccoker : ∀ n, IsIPowerTorsion S.A (N n ⧸ LinearMap.range (c n)) S.a) :
    ∃ (P : Type w) (_ : AddCommGroup P) (_ : Module S.A P) (𝒬 : ℤ → AddSubgroup P)
        (_ : DirectSum.Decomposition 𝒬)
        (e : ∀ n, (P ⧸ S.I ^ n • (⊤ : Submodule S.A P)) ≃ₗ[S.A] N n)
        (g : ∀ n, M n →ₗ[S.A] P ⧸ S.I ^ n • (⊤ : Submodule S.A P)),
      Module.Finite S.A P ∧
      (∀ (i : ℕ) (d : ℤ) (a : S.A) (x : P), a ∈ 𝒜 i → x ∈ 𝒬 d → a • x ∈ 𝒬 (i + d)) ∧
      (∀ (n : ℕ) (d : ℤ) (x : P), x ∈ 𝒬 d → e n (Submodule.Quotient.mk x) ∈ 𝒩 n d) ∧
      (∀ (n : ℕ) (x : P),
        t n (e (n + 1) (Submodule.Quotient.mk x)) = e n (Submodule.Quotient.mk x)) ∧
      (∀ (n : ℕ) (x : M n), e n (g n x) = c n x) ∧
      (∀ (n : ℕ) (d : ℤ) (x : M n), x ∈ ℳ n d →
        ∃ p ∈ 𝒬 d, g n x = Submodule.Quotient.mk p) ∧
      (∀ (n : ℕ) (x : M (n + 1)) (p : P), g (n + 1) x = Submodule.Quotient.mk p →
        g n (s n x) = Submodule.Quotient.mk p) ∧
      (∀ n, IsIPowerTorsion S.A (LinearMap.ker (g n)) S.a) ∧
      (∀ n, IsIPowerTorsion S.A
        ((P ⧸ S.I ^ n • (⊤ : Submodule S.A P)) ⧸ LinearMap.range (g n)) S.a)
```

## Tag 0EL5, a proposition

[Tag 0EL5](https://stacks.math.columbia.edu/tag/0EL5) in the Stacks Project.

**`Stacks.Algebraization.satisfiesDepthInequalities_one_two_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesCohomologicalDimensionOne.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/DepthInequalitiesCohomologicalDimensionOne.lean#L464). The attribute's comment: “only the opening step, as an equivalence: the depth hypothesis is the (1, 2)-inequalities, this library's encoding of conditions (b), (c), (d) of 0EJF at d = 1; in the affine Situation 0EHC, with the distance function for dim(closure q) and with cd(A, I) = 1 hypothesised; the conclusion that the system is a completion is not proved”.

> In Situation 0EHC let `(ℱ_n)` be an object of `Coh(U, I𝒪_U)` and assume `cd(A, I) = 1`.
> Then `(ℱ_n)` satisfies the `(1, 2)`-inequalities if and only if
>
> `depth((ℱ_y^∧)_𝔭) + dim(𝒪_{X,y}^∧/𝔭) + δ^Y_Z(y) > 2`
>
> for every `y ∈ U ∩ Y` and every prime `𝔭 ⊆ 𝒪_{X,y}^∧` with `𝔭 ∉ V(I𝒪_{X,y}^∧)`.

```lean
public theorem satisfiesDepthInequalities_one_two_iff (S : AlgebraizationSituation.{u})
    (F : Stacks.Coherent.CoherentAdicSystems (idealOnOpen S))
    (hcd : Stacks.LocalCohomology.cohomologicalDimension S.A S.I
      (IsNoetherian.noetherian S.I) = 1) :
    SatisfiesDepthInequalities S F 1 2 ↔
      ∀ (y : S.U.toScheme) (z : S.Y), S.U.ι.base y = S.Yι.base z →
        ∀ p : PrimeSpectrum (completedLocalRing (idealOnOpen S) y),
          ¬ completedLocalIdeal (idealOnOpen S) y ≤ p.asIdeal →
          depthAddDimAddDistance S F y z p > ((2 : ℤ) : EInt)
```

**`Stacks.Algebraization.isCompletionOfCoherent_of_two_lt_depth_add_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzFormalModuleAlgebraization.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzFormalModuleAlgebraization.lean#L68).

> Let `k` be a field, `P` a proper scheme over `k`, `𝓛` an ample invertible `𝒪_P`-module,
> `s ∈ Γ(P, 𝓛)` and `𝓘` the ideal of the zero scheme `Q = Z(s)`. Let `(𝓕ₙ)` be an object of
> `Coh(P, 𝓘)` such that for all `q ∈ Q` and all primes `𝔭` of `𝒪_{P,q}^∧` not containing `𝓘_q^∧`,
> `depth((𝓕_q^∧)_𝔭) + dim(𝒪_{P,q}^∧/𝔭) + dim({q}‾) > 2`.
> Then `(𝓕ₙ)` is the completion of a coherent `𝒪_P`-module.

```lean
theorem isCompletionOfCoherent_of_two_lt_depth_add_dim
    (F : Stacks.Coherent.CoherentAdicSystems (zeroScheme P L s))
    (hdepth : ∀ q ∈ (zeroScheme P L s).support,
      ∀ p : PrimeSpectrum (completedLocalRing (zeroScheme P L s) q),
        ¬ completedLocalIdeal (zeroScheme P L s) q ≤ p.asIdeal →
        (2 : EInt) < enatToEInt (completedStalkDepth (zeroScheme P L s) F q p) +
          krullDimToEInt (ringKrullDim (completedLocalRing (zeroScheme P L s) q ⧸ p.asIdeal)) +
          krullDimToEInt (dimClosureAt P q)) :
    haveI : IsLocallyNoetherian P := LocallyOfFiniteType.isLocallyNoetherian fP
    IsCompletionOfCoherent (zeroScheme P L s) F
```

## Tag 0EL6, an example

[Tag 0EL6](https://stacks.math.columbia.edu/tag/0EL6) in the Stacks Project.

**`Stacks.Algebraization.not_two_lt_completedStalkDepth_of_dim_le_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionAlgebraization.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionAlgebraization.lean#L139). The attribute's comment: “clause (1): for a curve or a surface the inequality of 0EL5 fails at every point of Y with nonzero completed stalk and every prime off the completed ideal”.

> Let `X` be a proper variety over a field with an effective Cartier divisor `Y` whose sheaf
> `𝒪_X(Y)` is ample, and let `(𝓔ₙ)` be an object of `Coh(X, 𝓘)` whose terms are finite locally free
> over the infinitesimal neighbourhoods. If `X` is a curve or a surface, the hypothesis
>
> `depth((𝓔_q^∧)_𝔭) + dim(𝒪_{X,q}^∧/𝔭) + dim({q}‾) > 2`
>
> of Stacks 0EL5 fails at every point `q` of `Y` where the completed stalk is nonzero and every
> prime `𝔭` of `𝒪_{X,q}^∧`.

```lean
theorem not_two_lt_completedStalkDepth_of_dim_le_two (f : X ⟶ Spec (.of k))
    [IsProperVariety k f] (Y : X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor Y]
    (_hample : AlgebraicGeometry.Scheme.Modules.IsAmple X (Stacks.Divisors.divisorSheaf Y))
    (E : Stacks.Coherent.CoherentAdicSystems Y) (hfree : IsFiniteLocallyFreeAdic Y E)
    (hdim : topologicalKrullDim X ≤ ((2 : ℕ) : WithBot ℕ∞))
    {q : X} (hq : q ∈ Y.support) [Nontrivial (completedStalk Y E q)]
    (p : PrimeSpectrum (completedLocalRing Y q)) :
    ¬ (2 : EInt) < enatToEInt (completedStalkDepth Y E q p) +
      krullDimToEInt (ringKrullDim (completedLocalRing Y q ⧸ p.asIdeal)) +
      krullDimToEInt (dimClosureAt X q)
```

**`Stacks.Algebraization.exists_completion_iso_of_hasPropertySk_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionAlgebraization.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionAlgebraization.lean#L201). The attribute's comment: “clause (3) with the closing remark: dim X >= 3 and X is (S\_3); the freeness of E\_n is read over the infinitesimal neighbourhoods Y\_n”. References: SGA 2 X (2.2), “(ii)”; SGA 2 XII (3.1), “special case”; SGA 2 XII (3.4), “Clause b), special case”.

> Let `X` be a proper variety over a field `k`, `Y ⊂ X` an effective Cartier divisor such that
> `𝒪_X(Y)` is ample, with ideal sheaf `𝓘`, and `(𝓔ₙ)` an object of `Coh(X, 𝓘)` whose terms are
> finite locally free over the infinitesimal neighbourhoods. If `dim(X) ≥ 3` and `X` is `(S₃)`, then
> `(𝓔ₙ)` is the completion of a coherent `𝒪_X`-module `𝓔`, and `𝓔` is finite locally free on an
> open neighbourhood of `Y`.

```lean
theorem exists_completion_iso_of_hasPropertySk_three (f : X ⟶ Spec (.of k))
    [IsProperVariety k f] (Y : X.IdealSheafData) [Stacks.Divisors.IsEffectiveCartierDivisor Y]
    (hample : AlgebraicGeometry.Scheme.Modules.IsAmple X (Stacks.Divisors.divisorSheaf Y))
    (E : Stacks.Coherent.CoherentAdicSystems Y) (hfree : IsFiniteLocallyFreeAdic Y E)
    (hdim : ((3 : ℕ) : WithBot ℕ∞) ≤ topologicalKrullDim X) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    HasPropertySk X 3 →
      ∃ G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
        Nonempty (((completionFunctor X Y).obj G).obj ≅ E.obj) ∧
          ∃ V : X.Opens, (Y.support : Set X) ⊆ (V : Set X) ∧
            AlgebraicGeometry.Scheme.Modules.IsFiniteLocallyFree
              (Scheme.Modules.restrict (show X.Modules from G.obj) V.ι)
```

**`Stacks.Algebraization.exists_completion_iso_of_isCohenMacaulay_of_dim_eq_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionAlgebraization.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionAlgebraization.lean#L239). The attribute's comment: “clause (2) with the closing remark: X a Cohen-Macaulay threefold; the freeness of E\_n is read over the infinitesimal neighbourhoods Y\_n”.

> In the situation of `exists_completion_iso_of_hasPropertySk_three`, if `X` is a Cohen–Macaulay
> threefold then `(𝓔ₙ)` is the completion of a coherent `𝒪_X`-module `𝓔`, finite locally free on an
> open neighbourhood of `Y`.

```lean
theorem exists_completion_iso_of_isCohenMacaulay_of_dim_eq_three (f : X ⟶ Spec (.of k))
    [IsProperVariety k f] (Y : X.IdealSheafData) [Stacks.Divisors.IsEffectiveCartierDivisor Y]
    (hample : AlgebraicGeometry.Scheme.Modules.IsAmple X (Stacks.Divisors.divisorSheaf Y))
    (E : Stacks.Coherent.CoherentAdicSystems Y) (hfree : IsFiniteLocallyFreeAdic Y E)
    (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hdim : topologicalKrullDim X = ((3 : ℕ) : WithBot ℕ∞)) :
    haveI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    ∃ G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
      Nonempty (((completionFunctor X Y).obj G).obj ≅ E.obj) ∧
        ∃ V : X.Opens, (Y.support : Set X) ⊆ (V : Set X) ∧
          AlgebraicGeometry.Scheme.Modules.IsFiniteLocallyFree
            (Scheme.Modules.restrict (show X.Modules from G.obj) V.ι)
```

**`Stacks.Algebraization.isCompletionOfCoherent_of_hasPropertySk_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionSpecialCases.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionSpecialCases.lean#L213). The attribute's comment: “clause (3): dim X >= 3 and (S\_3); the freeness of E\_n is corrected to be read over Y\_n, since over O\_X it would force E\_n = 0; 0EL5's conclusion and 0A21 hypothesised”.

> **Stacks Project, Tag 0EL6, clause (3).** Let `X` be a proper variety over a field with an
> effective Cartier divisor `Y` whose sheaf `𝒪_X(Y)` is ample, and let `(𝓔ₙ)` be an object of
> `Coh(X, 𝓘)` whose terms are finite locally free over the infinitesimal neighbourhoods. If
> `dim(X) ≥ 3` and `X` satisfies `(S₃)`, then `(𝓔ₙ)` is the completion of a coherent
> `𝒪_X`-module.

```lean
public theorem isCompletionOfCoherent_of_hasPropertySk_three (f : X ⟶ Spec (.of k))
    [IsProperVariety k f] [IsLocallyNoetherian X] (Y : X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor Y]
    (_hample : AlgebraicGeometry.Scheme.Modules.IsAmple X (Stacks.Divisors.divisorSheaf Y))
    (E : Stacks.Coherent.CoherentAdicSystems Y)
    (_hfree : IsFiniteLocallyFreeAdic Y E)
    (hdim : ((3 : ℕ) : WithBot ℕ∞) ≤ topologicalKrullDim X) (hS₃ : HasPropertySk X 3)
    (hform : ∀ x : X,
      ringKrullDim (X.presheaf.stalk x) + dimClosureAt X x = topologicalKrullDim X)
    (halgebraize : (∀ x : X, x ∉ Y.support →
        ((2 : ℕ) : WithBot ℕ∞) < localDepthAddDimClosure X x) → IsCompletionOfCoherent Y E) :
    IsCompletionOfCoherent Y E
```

**`Stacks.Algebraization.isCompletionOfCoherent_of_isCohenMacaulay_threefold`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionSpecialCases.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionSpecialCases.lean#L232). The attribute's comment: “clause (2): a Cohen-Macaulay threefold; the freeness of E\_n is corrected to be read over Y\_n, since over O\_X it would force E\_n = 0; 0EL5 and 0A21 hypothesised”.

> **Stacks Project, Tag 0EL6, clause (2).** In the situation of clause (3), a Cohen–Macaulay
> threefold satisfies `(S₃)` and has dimension `3`, so `(𝓔ₙ)` is again the completion of a coherent
> `𝒪_X`-module.

```lean
public theorem isCompletionOfCoherent_of_isCohenMacaulay_threefold (f : X ⟶ Spec (.of k))
    [IsProperVariety k f] [IsLocallyNoetherian X] (Y : X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor Y]
    (_hample : AlgebraicGeometry.Scheme.Modules.IsAmple X (Stacks.Divisors.divisorSheaf Y))
    (E : Stacks.Coherent.CoherentAdicSystems Y)
    (_hfree : IsFiniteLocallyFreeAdic Y E)
    (hCM : AlgebraicGeometry.IsCohenMacaulay X)
    (hdim : topologicalKrullDim X = ((3 : ℕ) : WithBot ℕ∞))
    (hform : ∀ x : X,
      ringKrullDim (X.presheaf.stalk x) + dimClosureAt X x = topologicalKrullDim X)
    (halgebraize : (∀ x : X, x ∉ Y.support →
        ((2 : ℕ) : WithBot ℕ∞) < localDepthAddDimClosure X x) → IsCompletionOfCoherent Y E) :
    IsCompletionOfCoherent Y E
```

**`Stacks.Algebraization.exists_isFiniteLocallyFree_neighbourhood_of_isCompletionOfCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionSpecialCases.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzSerreConditionSpecialCases.lean#L280). The attribute's comment: “closing remark: such an E is finite locally free near Y”.

> **Stacks Project, Tag 0EL6, the closing remark.** If the object `(𝓔ₙ)` is the completion of a
> coherent `𝒪_X`-module `𝓔`, then `𝓔` is finite locally free on an open neighbourhood of `Y`.
>
> At a point `y` of `Y` the terms of the system identify the adic quotients
> `𝓔_y / 𝓘_y ^ (n + 1) 𝓔_y` with the stalks of finite locally free modules on the infinitesimal
> neighbourhoods, hence make them free over `𝒪_{X,y} / 𝓘_y ^ (n + 1)`
> (`Stacks.Algebraization.free_quotient_stalk_of_pushforward_iso`); a module with a free tower of
> adic quotients over a Noetherian local ring is free
> (`Stacks.FreeOfAdicQuotients.free_of_forall_free_quotient_pow_smul_top`), so `𝓔_y` is a finite
> free `𝒪_{X,y}`-module. Stacks 0B8J spreads a free stalk to a free neighbourhood, and those
> neighbourhoods cover a neighbourhood of `Y`.

```lean
public theorem exists_isFiniteLocallyFree_neighbourhood_of_isCompletionOfCoherent
    (f : X ⟶ Spec (.of k)) [IsProperVariety k f] [IsLocallyNoetherian X] (Y : X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor Y]
    (_hample : AlgebraicGeometry.Scheme.Modules.IsAmple X (Stacks.Divisors.divisorSheaf Y))
    (E : Stacks.Coherent.CoherentAdicSystems Y)
    (hfree : IsFiniteLocallyFreeAdic Y E)
    (G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf)
    (hcompletion : Nonempty (((completionFunctor X Y).obj G).obj ≅ E.obj)) :
    ∃ V : X.Opens, (Y.support : Set X) ⊆ (V : Set X) ∧ ∀ x : X, x ∈ V →
      ∃ (U : X.Opens) (_ : x ∈ U) (_ : U ≤ V) (ρ : Type u) (_ : Finite ρ),
        Nonempty (Scheme.Modules.restrict G.obj U.ι ≅ SheafOfModules.free.{u} ρ)
```

## Tag 0EL7, a proposition

[Tag 0EL7](https://stacks.math.columbia.edu/tag/0EL7) in the Stacks Project.

**`Stacks.Algebraization.isCompletionEquivalence_of_two_lt_depth_add_dimClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzAmpleSectionCompletionEquivalence.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzAmpleSectionCompletionEquivalence.lean#L121). The attribute's comment: “essential surjectivity up to V; full faithfulness over X; 0EL5, 0EL2 assumed”.

> **Stacks Project, Tag 0EL7.** Let `X` be a proper scheme over a field, `𝓛` an ample invertible
> `𝒪_X`-module, `s ∈ Γ(X, 𝓛)` and `Y = Z(s)` with sheaf of ideals `𝓘`. If
> `depth(𝒪_{X,x}) + dim({x}‾) > 2` at every point off `Y`, then completion along `𝓘` is fully
> faithful on finite locally free coherent modules, and every finite locally free object of
> `Coh(X, 𝓘)` is the completion of a coherent module finite locally free near `Y`.

```lean
public theorem isCompletionEquivalence_of_two_lt_depth_add_dimClosure (k : Type u) [Field k]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsProper f] [IsLocallyNoetherian X] (L : X.Modules)
    [Stacks.Ample.IsInvertibleModule X L] (_hample : Stacks.Ample.IsAmple X L) (s : Γ(L, ⊤))
    (hdepth : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) →
      ((2 : ℕ) : WithBot ℕ∞) < localDepthAddDimClosure X x)
    (hff : CompletionFullyFaithfulOnFiniteLocallyFree X (zeroScheme X L s))
    (halgebraize : ∀ F : Stacks.Coherent.CoherentAdicSystems (zeroScheme X L s),
      (∀ n : ℕ, AlgebraicGeometry.Scheme.Modules.IsFiniteLocallyFree (F.obj.obj (op n))) →
      (∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) →
        ((2 : ℕ) : WithBot ℕ∞) < localDepthAddDimClosure X x) →
      ∃ G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf,
        Nonempty (((completionFunctor X (zeroScheme X L s)).obj G).obj ≅ F.obj) ∧
          ∀ y ∈ ((zeroScheme X L s).support : Set X),
            ∃ (U : X.Opens) (_ : y ∈ U) (ρ : Type u) (_ : Finite ρ),
              Nonempty (Scheme.Modules.restrict G.obj U.ι ≅ SheafOfModules.free.{u} ρ)) :
    IsCompletionEquivalenceOnFiniteLocallyFree X (zeroScheme X L s)
```

**`Stacks.Algebraization.completionEquivalence_finiteLocallyFree_of_two_lt_depth_add_dimClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzFiniteLocallyFreeEquivalence.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Algebraization/LefschetzFiniteLocallyFreeEquivalence.lean#L78).

> Let `k` be a field, `X` a proper scheme over `k`, `𝓛` an ample invertible `𝒪_X`-module,
> `s ∈ Γ(X, 𝓛)`, `Y = Z(s)` its zero scheme with sheaf of ideals `𝓘`, and `𝒱` the open subschemes
> of `X` containing `Y`. Assume `depth(𝒪_{X,x}) + dim({x}‾) > 2` for all `x ∈ X ∖ Y`. Then the
> completion functor `colim_𝒱 Coh(𝒪_V) ⟶ Coh(X, 𝓘)` is an equivalence on the full subcategories of
> finite locally free objects: it lands in the finite locally free objects, it is fully faithful on
> finite locally free objects, and every finite locally free object of `Coh(X, 𝓘)` is the
> completion of a finite locally free coherent module on some `V ∈ 𝒱`. See the module documentation
> for how each half is written.

```lean
public theorem completionEquivalence_finiteLocallyFree_of_two_lt_depth_add_dimClosure
    (k : Type u) [Field k] (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [IsProper f]
    (L : X.Modules) [Stacks.Ample.IsInvertibleModule X L] (hL : Stacks.Ample.IsAmple X L)
    (s : Γ(L, ⊤))
    (hdepth : ∀ x : X, x ∉ ((zeroScheme X L s).support : Set X) →
      ((2 : ℕ) : WithBot ℕ∞) < localDepthAddDimClosure X x) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    (∀ (V : X.Opens), ((zeroScheme X L s).support : Set X) ⊆ (V : Set X) →
        ∀ G : AlgebraicGeometry.SheafOfModules.CoherentModules V.toScheme.ringCatSheaf,
          AlgebraicGeometry.Scheme.Modules.IsFiniteLocallyFree G.obj →
          IsFiniteLocallyFreeAdic ((zeroScheme X L s).comap V.ι)
            ((completionFunctor V.toScheme ((zeroScheme X L s).comap V.ι)).obj G)) ∧
      NeighbourhoodCompletion.CompletionFullyFaithfulComplete (zeroScheme X L s).subschemeι ∧
      (∀ F : Stacks.Coherent.CoherentAdicSystems (zeroScheme X L s),
        IsFiniteLocallyFreeAdic (zeroScheme X L s) F →
        ∃ (V : X.Opens) (_ : ((zeroScheme X L s).support : Set X) ⊆ (V : Set X))
          (G : AlgebraicGeometry.SheafOfModules.CoherentModules X.ringCatSheaf),
          AlgebraicGeometry.Scheme.Modules.IsFiniteLocallyFree
              (restrictCoherentModules V.ι G).obj ∧
            Nonempty (((completionFunctor X (zeroScheme X L s)).obj G).obj ≅ F.obj) ∧
            Nonempty (((completionFunctor V.toScheme ((zeroScheme X L s).comap V.ι)).obj
                (restrictCoherentModules V.ι G)).obj ≅
              F.obj ⋙ Scheme.Modules.restrictFunctor V.ι))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 52.28, Tag 0EL0](https://stacks.math.columbia.edu/tag/0EL0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
