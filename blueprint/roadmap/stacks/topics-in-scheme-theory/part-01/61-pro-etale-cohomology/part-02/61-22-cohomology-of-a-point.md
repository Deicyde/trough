---
declaration: section
origin: cited
lean: AlgebraicGeometry.GaloisSheaf.profiniteSheaf, AlgebraicGeometry.GaloisSheaf.adicSheaf, AlgebraicGeometry.GaloisSheaf.rightDerivedAdicSheafIso, AlgebraicGeometry.GaloisSheaf.rightDerivedProfiniteSheafIso, AlgebraicGeometry.GaloisSheaf.rightDerivedAdicSheafLinearEquiv
statement: formalized
proof: formalized
---

# 61.22 Cohomology of a point

Section 61.22 of the Stacks Project, [Tag 09B3](https://stacks.math.columbia.edu/tag/09B3). 1 tag here is carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09B4, a lemma

[Tag 09B4](https://stacks.math.columbia.edu/tag/09B4) in the Stacks Project.

**`AlgebraicGeometry.GaloisSheaf.profiniteSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompletedGaloisSheaf.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompletedGaloisSheaf.lean#L207). The attribute's comment: “case (1): the canonical sheaf of a profinite abelian group”.

> The canonical pro-étale sheaf `M^∧` attached to a profinite abelian group `M` with continuous
> action of the absolute Galois group of a field: the inverse limit of the pro-étale pullbacks of the
> locally constant étale sheaves of the discrete quotients `M/N` by the open Galois-stable subgroups
> `N`.

```lean
def profiniteSheaf (K : Type u) [Field K] (M : Type w) [AddCommGroup M] [TopologicalSpace M]
    [IsTopologicalAddGroup M] [CompactSpace M] [T2Space M] [TotallyDisconnectedSpace M]
    (ρ : Representation ℤ (galoisGroup K) M)
    (_hρ : Continuous fun p : galoisGroup K × M ↦ ρ p.1 p.2) :
    Sheaf (Scheme.ProEt.topology (base K)) (ModuleCat.{max (u + 1) w} ℤ)
```

**`AlgebraicGeometry.GaloisSheaf.adicSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/CompletedGaloisSheaf.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/CompletedGaloisSheaf.lean#L237). The attribute's comment: “case (2): the canonical sheaf of an adically complete module”.

> The canonical pro-étale sheaf `M^∧` attached to an `I`-adically complete module `M` over a
> Noetherian ring, with continuous action of the absolute Galois group of a field for the `I`-adic
> topology: the inverse limit of the pro-étale pullbacks of the locally constant étale sheaves of
> the discrete quotients `M/IⁿM`.

```lean
def adicSheaf (K : Type u) [Field K] [IsNoetherianRing Λ] (I : Ideal Λ) (M : Type w)
    [AddCommGroup M] [Module Λ M] [IsAdicComplete I M]
    (ρ : Representation Λ (galoisGroup K) M)
    (_hρ : letI : TopologicalSpace M := I.adicModuleTopology M
      Continuous fun p : galoisGroup K × M ↦ ρ p.1 p.2) :
    Sheaf (Scheme.ProEt.topology (base K)) (ModuleCat.{max (u + 1) r w} Λ)
```

**`AlgebraicGeometry.GaloisSheaf.rightDerivedAdicSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ContinuousGaloisCohomology.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ContinuousGaloisCohomology.lean#L317). The attribute's comment: “case (2), the cohomology comparison”.

> Let `K` be a field with absolute Galois group `G`, let `Λ` be a Noetherian ring with an ideal
> `I`, and let `M` be an `I`-adically complete `Λ`-module with a continuous action of `G` for the
> `I`-adic topology. Then the pro-étale cohomology of `Spec K` with coefficients in the completed
> sheaf `M^∧ = limₙ ε⁻¹(M/IⁿM)` is the continuous cohomology of `G` with coefficients in `M`:
>
>   `Hⁱ(Spec(K)_proét, M^∧) ≅ Hⁱ_cont(G, M)`.
>
> Here `Λ` and `M` carry their `I`-adic topologies, pro-étale cohomology is the `i`-th right
> derived functor of global sections of the underlying abelian sheaf, and the identification is of
> abelian groups, the right hand side being lifted to the coefficient universe of the site.

```lean
def rightDerivedAdicSheafIso
    (ρ : Representation Λ (galoisGroup K) M)
    (hρ : letI := I.adicModuleTopology M
      Continuous fun p : galoisGroup K × M ↦ ρ p.1 p.2) (i : ℕ) :
    letI : TopologicalSpace Λ := I.adicTopology
    letI := I.adicModuleTopology M
    letI := hasSheafify_galois.{u, r, w} K
    letI := enoughInjectives_galois.{u, r, w} K
    letI := Stacks.Cohomology.GlobalSections.additive_Γ.{max r w, u, u + 1}
      (Scheme.ProEt.topology (base K))
    ((Sheaf.Γ (Scheme.ProEt.topology (base K)) AddCommGrpCat.{max (u + 1) r w}).rightDerived i).obj
      ((sheafCompose _ (forget₂ (ModuleCat.{max (u + 1) r w} Λ) AddCommGrpCat)).obj
        (adicSheaf Λ K I M ρ hρ)) ≅
      (underlyingAb.{u, r, w} Λ).obj (continuousCohomology i (uliftRep.{u} ρ hρ))
```

**`AlgebraicGeometry.GaloisSheaf.rightDerivedProfiniteSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ContinuousGaloisCohomology.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ContinuousGaloisCohomology.lean#L432). The attribute's comment: “case (1), the cohomology comparison”.

> Let `K` be a field with absolute Galois group `G` and let `M` be a profinite abelian group
> with a continuous action of `G`. Then the pro-étale cohomology of `Spec K` with coefficients in
> the completed sheaf `M^∧ = lim_N ε⁻¹(M/N)`, the limit over the open `G`-stable subgroups `N`, is
> the continuous cohomology of `G` with coefficients in `M`:
>
>   `Hⁱ(Spec(K)_proét, M^∧) ≅ Hⁱ_cont(G, M)`.
>
> Pro-étale cohomology is the `i`-th right derived functor of global sections of the underlying
> abelian sheaf, and the identification is of abelian groups, the right hand side being lifted to
> the coefficient universe of the site.

```lean
def rightDerivedProfiniteSheafIso (i : ℕ) :
    letI := hasSheafify_galois.{u, 0, w} K
    letI := enoughInjectives_galois.{u, 0, w} K
    letI := Stacks.Cohomology.GlobalSections.additive_Γ.{max 0 w, u, u + 1}
      (Scheme.ProEt.topology (base K))
    ((Sheaf.Γ (Scheme.ProEt.topology (base K)) AddCommGrpCat.{max (u + 1) w}).rightDerived i).obj
      ((sheafCompose _ (forget₂ (ModuleCat.{max (u + 1) w} ℤ) AddCommGrpCat)).obj
        (profiniteSheaf K M ρ hρ)) ≅
      (underlyingAb.{u, 0, w} ℤ).obj (continuousCohomology i (uliftRep.{u} ρ hρ))
```

**`AlgebraicGeometry.GaloisSheaf.rightDerivedAdicSheafLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/ContinuousGaloisCohomologyLinear.lean, line 371](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/ContinuousGaloisCohomologyLinear.lean#L371). The attribute's comment: “case (2), as Λ-modules”.

> **Stacks Project, Tag 09B4, case (2), as `Λ`-modules.** In the situation of
> `rightDerivedAdicSheafIso`, the pro-étale cohomology `Hⁱ(Spec(K)_proét, M^∧)`, a `Λ`-module
> through the action of `Λ` on `M^∧`, is isomorphic as a `Λ`-module to the continuous cohomology
> `Hⁱ_cont(G, M)`, by the identification `rightDerivedAdicSheafIso`.

```lean
def rightDerivedAdicSheafLinearEquiv
    (ρ : Representation Λ (galoisGroup K) M)
    (hρ : letI := I.adicModuleTopology M
      Continuous fun p : galoisGroup K × M ↦ ρ p.1 p.2) (i : ℕ) :
    letI : TopologicalSpace Λ := I.adicTopology
    letI := I.adicModuleTopology M
    rightDerivedAdicSheafModule K Λ I M ρ hρ i ≃ₗ[Λ]
      ULift.{max (u + 1) r} (continuousCohomology i (uliftRep.{u} ρ hρ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.22, Tag 09B3](https://stacks.math.columbia.edu/tag/09B3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
