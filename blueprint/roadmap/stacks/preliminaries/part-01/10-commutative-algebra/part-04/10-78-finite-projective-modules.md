---
declaration: section
origin: cited
lean: Module.IsLocallyFree, Module.IsFiniteLocallyFree, Module.IsFiniteLocallyFreeOfRank, Module.finite_projective_tfae, Module.projective_iff_isLocallyConstant_finrank_fiber, Stacks.FiniteFlatNotProjective.quotientModule_isLocalization_finite_flat_not_projective, finite_projective_iff_baseChange, Module.free_of_flat_of_preconnectedSpace
statement: formalized
proof: formalized
---

# 10.78 Finite projective modules

Section 10.78 of the Stacks Project, [Tag 00NV](https://stacks.math.columbia.edu/tag/00NV). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00NW, a definition

[Tag 00NW](https://stacks.math.columbia.edu/tag/00NW) in the Stacks Project.

**`Module.IsLocallyFree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean#L116). The attribute's comment: “(1)”. References: EGA 0 (5.4.1), “affine case”; EGA II (6.5.1), “(I)”; EGA III (7.9.1); EGA IV (21.5.3), “special case”; SGA 3 XV (2.10).

> `M` is a **locally free** `R`-module: there is a family `f : ι → R` whose
> basic opens cover `Spec R` (equivalently, generate the unit ideal) and such that
> each localization `M_{f i}` is a free `R_{f i}`-module.

```lean
def Module.IsLocallyFree (R : Type u) [CommRing R] (M : Type u)
    [AddCommGroup M] [Module R M] : Prop
```

**`Module.IsFiniteLocallyFree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean#L132). The attribute's comment: “(2)”. References: EGA 0 (5.4.1), “affine case”; EGA II (6.5.1), “(I), special case”; EGA III (7.9.1); EGA IV (18.2.7), “partial”; EGA IV (21.5.3), “special case”; SGA 1 VIII (7.6), “affine module condition”; SGA 6 IV (2.1), “special case”.

> `M` is a **finite locally free** `R`-module: as above, but each localization
> `M_{f i}` is in addition finitely generated (hence finite free) over `R_{f i}`.

```lean
def Module.IsFiniteLocallyFree (R : Type u) [CommRing R] (M : Type u)
    [AddCommGroup M] [Module R M] : Prop
```

**`Module.IsFiniteLocallyFreeOfRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/LocallyFree/SheafBridge.lean#L167). The attribute's comment: “(3)”. References: EGA 0 (5.4.1), “affine case, rank n”; EGA II (6.5.1), “(I), special case”; EGA IV (18.2.7), “partial”; SGA 4½ Arcata (1.4.2); SGA 6 X (6.1), “partial”.

> `M` is **finite locally free of rank `r`**: there is a covering family
> `f : ι → R` of `Spec R` such that each localization `M_{f i}` is free of rank `r`
> over `R_{f i}`, i.e. has a basis indexed by `Fin r`.

```lean
def Module.IsFiniteLocallyFreeOfRank (R : Type u) [CommRing R] (M : Type v)
    [AddCommGroup M] [Module R M] (r : ℕ) : Prop
```

## Tag 00NX, a lemma

[Tag 00NX](https://stacks.math.columbia.edu/tag/00NX) in the Stacks Project.

**`Module.finite_projective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/FiniteProjective.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/LocallyFree/FiniteProjective.lean#L362). References: EGA III (7.3.4), “(1) => (8)”; EGA IV (2.1.12), “affine, flat everywhere”; EGA III (7.9.1); SGA 6 I (1.3.1), “affine case; (i)⇔(iii)”; SGA 6 I (2.15.1), “affine case, (3)⇒(7)”; SGA 6 I (5.8.3), “commutative ring case”; SGA 6 I (6.0), “special case”.

> **Characterizations of finite projective modules.** For a module `M` over a commutative ring
> `R` the following are equivalent: (1) `M` is finitely presented and flat; (2) `M` is finite
> projective; (3) `M` is a direct summand of a finite free module; (4) `M` is finitely presented and
> free at every prime; (5) `M` is finitely presented and free at every maximal ideal; (6) `M` is
> finite and locally free; (7) `M` is finite locally free; (8) `M` is finite, free at every prime,
> and its rank function `ρ_M = Module.rankAtStalk M` is locally constant on `Spec(R)`.

```lean
public theorem Module.finite_projective_tfae (R : Type u) [CommRing R] (M : Type v)
    [AddCommGroup M] [Module R M] :
    List.TFAE
      [Module.FinitePresentation R M ∧ Module.Flat R M,
       Module.Finite R M ∧ Module.Projective R M,
       ∃ (n : ℕ) (f : (Fin n → R) →ₗ[R] M) (g : M →ₗ[R] (Fin n → R)), f ∘ₗ g = LinearMap.id,
       Module.FinitePresentation R M ∧ Module.freeLocus R M = Set.univ,
       Module.FinitePresentation R M ∧ ∀ (𝔪 : Ideal R) (_ : 𝔪.IsMaximal),
         Module.Free (Localization.AtPrime 𝔪) (LocalizedModule 𝔪.primeCompl M),
       Module.Finite R M ∧ ∃ s : Set R, Ideal.span s = ⊤ ∧
         ∀ f ∈ s, Module.Free (Localization.Away f) (LocalizedModule.Away f M),
       ∃ s : Set R, Ideal.span s = ⊤ ∧ ∀ f ∈ s,
         Module.Free (Localization.Away f) (LocalizedModule.Away f M) ∧
           Module.Finite (Localization.Away f) (LocalizedModule.Away f M),
       Module.Finite R M ∧ Module.freeLocus R M = Set.univ ∧
         IsLocallyConstant (Module.rankAtStalk (R := R) M)]
```

## Tag 0FWG, a lemma

[Tag 0FWG](https://stacks.math.columbia.edu/tag/0FWG) in the Stacks Project.

**`Module.projective_iff_isLocallyConstant_finrank_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/LocallyConstantRank.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/LocallyConstantRank.lean#L406). References: SGA 6 III (5.6), “affine, E = M in deg 0”; SGA 6 I (6.0), “special case”; SGA 6 III (5.4.1), “special case”.

> **A finite module over a reduced ring is projective iff its fibre dimension is locally
> constant.** For `R` a reduced commutative ring and `M` a finite `R`-module, `M` is projective
> (equivalently, by `Module.finite_projective_tfae`, finite locally free) if and only if the
> function `ρ_M : Spec(R) → ℕ`, `𝔭 ↦ dim_{κ(𝔭)} M ⊗_R κ(𝔭)`, is locally constant. This is item (9)
> in the list of characterizations of finite projective modules.

```lean
public theorem Module.projective_iff_isLocallyConstant_finrank_fiber (R : Type u) [CommRing R]
    [IsReduced R] (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Module.Projective R M ↔
      IsLocallyConstant fun p : PrimeSpectrum R ↦
        Module.finrank p.asIdeal.ResidueField (p.asIdeal.Fiber M)
```

## Tag 00NY, a remark

[Tag 00NY](https://stacks.math.columbia.edu/tag/00NY) in the Stacks Project.

**`Stacks.FiniteFlatNotProjective.quotientModule_isLocalization_finite_flat_not_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/Basic.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/LocallyFree/Basic.lean#L299).

> **Stacks 00NY.** Over `R = C^∞(ℝ)`, with `m` the ideal of functions vanishing at `0` and `I`
> the ideal of functions vanishing on a neighbourhood of `0`, the module `M = R/I` is the
> localization `R_m`, and it is a finite flat `R`-module which is not projective.

```lean
theorem quotientModule_isLocalization_finite_flat_not_projective :
    IsLocalization.AtPrime QuotientModule vanishAtZero ∧
      Module.Finite SmoothFunReal QuotientModule ∧
      Module.Flat SmoothFunReal QuotientModule ∧
      ¬ Module.Projective SmoothFunReal QuotientModule
```

## Tag 00O1, a lemma

[Tag 00O1](https://stacks.math.columbia.edu/tag/00O1) in the Stacks Project.

**`finite_projective_iff_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/LocallyFree/Basic.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/LocallyFree/Basic.lean#L335). References: SGA 3 VIB (11.8.2), “special case”.

> **Stacks 00O1 (Lemma 10.78.6).** Let `R → S` be a flat local homomorphism of
> local rings, and let `M` be a finite `R`-module. Then `M` is finite projective
> over `R` if and only if `M ⊗_R S` is finite projective over `S`.

```lean
theorem finite_projective_iff_baseChange {R : Type*} {S : Type*} {M : Type*}
    [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module R M]
    [IsLocalRing R] [IsLocalRing S]
    [IsLocalHom (algebraMap R S)]
    [Module.Flat R S]
    [Module.Finite R M] :
    (Module.Finite R M ∧ Module.Projective R M) ↔
      (Module.Finite S (S ⊗[R] M) ∧ Module.Projective S (S ⊗[R] M))
```

## Tag 02M9, a lemma

[Tag 02M9](https://stacks.math.columbia.edu/tag/02M9) in the Stacks Project.

**`Module.free_of_flat_of_preconnectedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/Module.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalRing/Module.lean#L232). The attribute's comment: “The second assertion; the first, for a module of constant rank, is Mathlib's `Module.free_of_flat_of_finrank_eq`.”. References: EGA IV (11.3.12), “more general”; EGA IV (15.2.4), “Freeness clause”.

> **A finite locally free module over a semi-local ring with connected spectrum is free.**
> Let `R` be a semi-local ring, so with finitely many maximal ideals, whose spectrum is
> (pre)connected, and let `M` be a finite locally free `R`-module, spelled here as finitely
> presented and flat. Then `M` is free. The rank of `M` is a locally constant function on
> `Spec(R)`, hence constant, and a finite locally free module of constant rank over a semi-local
> ring is free (`Module.free_of_flat_of_finrank_eq`).

```lean
public theorem Module.free_of_flat_of_preconnectedSpace (R : Type u) [CommRing R]
    [Finite (MaximalSpectrum R)] [PreconnectedSpace (PrimeSpectrum R)] (M : Type v)
    [AddCommGroup M] [Module R M] [Module.FinitePresentation R M] [Module.Flat R M] :
    Module.Free R M
```

## Tag 03C1, a lemma

[Tag 03C1](https://stacks.math.columbia.edu/tag/03C1) in the Stacks Project.

**`contains_sBasis_of_generates`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Free/Basis.lean, line 612](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Free/Basis.lean#L612). References: SGA 3 V (4.2).

> Let `R` be a local ring with maximal ideal `m` and infinite residue field.
> Let `R → S` be a ring map, `M` an `S`-module, and `N ⊆ M` an `R`-submodule.
> If `S` is semi-local with `m S ⊆ Jac(S)`, `M` is finite free over `S`, and
> `N` generates `M` as an `S`-module, then `N` contains an `S`-basis of `M`.

```lean
theorem contains_sBasis_of_generates
    {R S M : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module S M] [Module R M] [IsScalarTower R S M]
    [IsLocalRing R] [Infinite (IsLocalRing.ResidueField R)]
    (hSsemilocal : Finite (MaximalSpectrum S))
    (hmS : Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R) ≤ Ring.jacobson S)
    [Module.Free S M] [Module.Finite S M]
    (N : Submodule R M)
    (hN : GeneratesAsSModule S N) :
    ContainsSBasis S N
```

## Tag 0DVB, a lemma

[Tag 0DVB](https://stacks.math.columbia.edu/tag/0DVB) in the Stacks Project.

Declarations registered for the tag:

- [`rTensorHomEquivHomRTensor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=rTensorHomEquivHomRTensor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L272) (StacksFrontier): “the isomorphism Hom(M, N) ⊗ L ≃ Hom(M, N ⊗ L) for M finite projective”. References: SGA 5 III (3.1), “special case”; SGA 5 III (6.3), “special case”; SGA 6 I (7.6), “special case”.
- [`rTensorHomEquivHomRTensor_toLinearMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=rTensorHomEquivHomRTensor_toLinearMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L274) (StacksFrontier): “it is the canonical map f ⊗ l ↦ (m ↦ f m ⊗ l)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.78, Tag 00NV](https://stacks.math.columbia.edu/tag/00NV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
