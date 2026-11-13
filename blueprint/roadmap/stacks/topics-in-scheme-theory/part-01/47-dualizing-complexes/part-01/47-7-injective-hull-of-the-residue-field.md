---
declaration: section
origin: cited
lean: Dualizing.isInjectiveHull_kernelTorsion_of_surjective, Dualizing.exists_injective_to_pi_injectiveHull, Dualizing.maximalIdealPowTorsion_isInjectiveHull, Dualizing.iSup_maximalIdealPowTorsion_eq_top, Dualizing.exists_iso_injectiveHull_residueField, Dualizing.endAlgEquivAdicCompletion, Dualizing.isArtinian_of_isInjectiveHull_residueField, Dualizing.isNoetherian_iff_module_finite
statement: formalized
proof: formalized
---

# 47.7 Injective hull of the residue field

Section 47.7 of the Stacks Project, [Tag 08Z1](https://stacks.math.columbia.edu/tag/08Z1). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08Z2, a lemma

[Tag 08Z2](https://stacks.math.columbia.edu/tag/08Z2) in the Stacks Project.

**`Dualizing.isInjectiveHull_kernelTorsion_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean#L233).

> **Stacks Project, Tag 08Z2.** For a surjective ring homomorphism, the
> submodule of an injective hull annihilated by the kernel is an injective hull
> over the quotient ring.

```lean
public theorem isInjectiveHull_kernelTorsion_of_surjective
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    (f : R →+* S) (hf : Function.Surjective f)
    {K : ModuleCat.{w} S} {E : ModuleCat.{w} R}
    (i : (ModuleCat.restrictScalars.{w} f).obj K ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    Module.IsInjectiveHull (kernelTorsionInclusion f hf i)
```

## Tag 08Z3, a lemma

[Tag 08Z3](https://stacks.math.columbia.edu/tag/08Z3) in the Stacks Project.

**`Dualizing.exists_injective_to_pi_injectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean#L499).

> **Stacks Project, Tag 08Z3.** A module which is power-torsion for the maximal ideal embeds
> in the direct sum of as many copies of an injective hull of the residue field as the dimension
> of its socle.

```lean
public theorem exists_injective_to_pi_injectiveHull
    (R : Type u) [CommRing R] [IsLocalRing R]
    (M : Type v) (E : Type u) [AddCommGroup M] [Module R M] [AddCommGroup E] [Module R E]
    (i : ModuleCat.of R (R ⧸ IsLocalRing.maximalIdeal R) ⟶ ModuleCat.of R E) [Mono i]
    (hi : Module.IsInjectiveHull i)
    (hM : ∀ x : M, ∃ e : ℕ, ∀ r ∈ (IsLocalRing.maximalIdeal R ^ e : Ideal R),
      r • x = 0)
    (n : ℕ)
    [Module.Finite (R ⧸ IsLocalRing.maximalIdeal R)
      (Submodule.torsionBySet R M (IsLocalRing.maximalIdeal R))]
    (hn : Module.finrank (R ⧸ IsLocalRing.maximalIdeal R)
      (Submodule.torsionBySet R M (IsLocalRing.maximalIdeal R)) = n) :
    ∃ f : M →ₗ[R] (Fin n → E), Function.Injective f
```

## Tag 08Z4, a lemma

[Tag 08Z4](https://stacks.math.columbia.edu/tag/08Z4) in the Stacks Project.

**`Dualizing.maximalIdealPowTorsion_isInjectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean#L379). The attribute's comment: “the submodules E\_n”.

> **Stacks Project, Tag 08Z4.** The submodule of an injective hull of the residue field
> annihilated by a positive power of the maximal ideal is an injective hull over the corresponding
> quotient ring. This is the canonical realization of the source's equality
> `E_n = E[𝔪^(n + 1)]`.

```lean
public theorem maximalIdealPowTorsion_isInjectiveHull
    (R : Type u) [CommRing R] [IsLocalRing R]
    (K E : ModuleCat.{v} R) (e : IsLocalRing.ResidueField R ≃ₗ[R] K)
    (i : K ⟶ E) [Mono i]
    (hE : Module.IsInjectiveHull i) (n : ℕ) :
    let hK := residueFieldModelIsTorsionByMaximalIdealPow R K e n
    letI := hK.module
    let j := residueFieldToMaximalIdealPowTorsion R e i n
    letI : Mono (ModuleCat.ofHom j) :=
      (ModuleCat.mono_iff_injective _).2
        (residueFieldToMaximalIdealPowTorsion_injective R e i
          ((ModuleCat.mono_iff_injective i).1 (by infer_instance)) n)
    Module.IsInjectiveHull (ModuleCat.ofHom j)
```

**`Dualizing.iSup_maximalIdealPowTorsion_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/PowerTorsionFiltration.lean#L461). The attribute's comment: “the union”.

> **Stacks Project, Tag 08Z4.** The submodules annihilated by positive powers of the maximal
> ideal exhaust an injective hull of the residue field.

```lean
public theorem iSup_maximalIdealPowTorsion_eq_top
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (K E : ModuleCat.{v} R) (e : IsLocalRing.ResidueField R ≃ₗ[R] K)
    (i : K ⟶ E) [Mono i]
    (hE : Module.IsInjectiveHull i) :
    (⨆ n : ℕ, maximalIdealPowTorsion R E n) = ⊤
```

## Tag 08Z5, a lemma

[Tag 08Z5](https://stacks.math.columbia.edu/tag/08Z5) in the Stacks Project.

**`Dualizing.exists_iso_injectiveHull_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/FlatComparison.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/FlatComparison.lean#L152).

> **Stacks Project, Tag 08Z5.** Injective hulls of the residue fields of a
> flat local homomorphism with trivial closed fibre agree after restriction of
> scalars.  The comparison isomorphism extends the induced identification of
> residue fields.

```lean
public theorem exists_iso_injectiveHull_residueField
    (R S : Type u) [CommRing R] [CommRing S]
    [IsLocalRing R] [IsLocalRing S] [IsNoetherianRing R]
    [IsNoetherianRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)]
    (hflat : RingHom.Flat (algebraMap R S))
    (hclosed : Function.Bijective (closedFiberMap R S))
    {E_R : ModuleCat.{u} R} {E_S : ModuleCat.{u} S}
    (i_R : ModuleCat.of R (ResidueField R) ⟶ E_R)
    (i_S : ModuleCat.of S (ResidueField S) ⟶ E_S)
    [Mono i_R] [Mono i_S]
    (hR : Module.IsInjectiveHull i_R)
    (hS : Module.IsInjectiveHull i_S) :
    ∃ e : E_R ≅ (ModuleCat.restrictScalars (algebraMap R S)).obj E_S,
      i_R ≫ e.hom = residueFieldMap R S ≫
        (ModuleCat.restrictScalars (algebraMap R S)).map i_S
```

## Tag 08Z6, a lemma

[Tag 08Z6](https://stacks.math.columbia.edu/tag/08Z6) in the Stacks Project.

**`Dualizing.endAlgEquivAdicCompletion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Endomorphisms.lean, line 660](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Endomorphisms.lean#L660).

> **Stacks Project, Tag 08Z6.** The endomorphism ring of an injective hull of
> the residue field of a Noetherian local ring is canonically isomorphic to its
> completion.

```lean
public noncomputable def endAlgEquivAdicCompletion
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (E : Type u) [AddCommGroup E] [Module R E]
    (i : ModuleCat.of R (R ⧸ IsLocalRing.maximalIdeal R) ⟶ ModuleCat.of R E)
    [Mono i] (hi : Module.IsInjectiveHull i) :
    Module.End R E ≃ₐ[R] AdicCompletion (IsLocalRing.maximalIdeal R) R
```

## Tag 08Z7, a lemma

[Tag 08Z7](https://stacks.math.columbia.edu/tag/08Z7) in the Stacks Project.

**`Dualizing.isArtinian_of_isInjectiveHull_residueField`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean#L240).

> **Stacks Project, Tag 08Z7.** An injective hull of the residue field of a
> Noetherian local ring is an Artinian module.

```lean
public lemma isArtinian_of_isInjectiveHull_residueField
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (E : Type u) [AddCommGroup E] [Module R E]
    (i : ModuleCat.of R (IsLocalRing.ResidueField R) ⟶ ModuleCat.of R E)
    [Mono i] (hi : Module.IsInjectiveHull i) :
    IsArtinian R E
```

## Tag 08Z8, a lemma

[Tag 08Z8](https://stacks.math.columbia.edu/tag/08Z8) in the Stacks Project.

**`Dualizing.isNoetherian_iff_module_finite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean#L283). The attribute's comment: “part (1): ascending chain condition and finite generation”.

> **Stacks Project, Tag 08Z8, part (1).** Over a Noetherian ring, the ascending chain condition
> on submodules is equivalent to finite generation.

```lean
public lemma isNoetherian_iff_module_finite (R : Type u) [Ring R] [IsNoetherianRing R]
    (M : Type v) [AddCommGroup M] [Module R M] :
    IsNoetherian R M ↔ Module.Finite R M
```

**`Dualizing.module_finite_iff_exists_finite_presentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean#L291). The attribute's comment: “part (1): finite presentation”.

> **Stacks Project, Tag 08Z8, part (1).** A finite module over a Noetherian ring admits a
> presentation by two finite free modules.

```lean
public lemma module_finite_iff_exists_finite_presentation
    (R : Type u) [Ring R] [IsNoetherianRing R]
    (M : Type v) [AddCommGroup M] [Module R M] :
    Module.Finite R M ↔
      ∃ (n m : ℕ) (f : (Fin n → R) →ₗ[R] M) (g : (Fin m → R) →ₗ[R] (Fin n → R)),
        Function.Surjective f ∧ Function.Exact g f
```

**`Dualizing.isArtinian_iff_powerTorsion_and_finiteSocle`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean#L379). The attribute's comment: “part (2): descending chain condition and torsion”.

> **Stacks Project, Tag 08Z8, part (2).** A module has the descending chain condition exactly
> when it is maximal-ideal-power torsion and has finite-dimensional socle.

```lean
public lemma isArtinian_iff_powerTorsion_and_finiteSocle
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (M : Type v) [AddCommGroup M] [Module R M] :
    IsArtinian R M ↔
      (IsIPowerTorsion R M (maximalIdeal R) ∧ HasFiniteSocle R M)
```

**`Dualizing.powerTorsion_and_finiteSocle_iff_exists_finite_copresentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean#L390). The attribute's comment: “part (2): finite copresentation”.

> **Stacks Project, Tag 08Z8, part (2).** The torsion and finite-socle condition is equivalent to
> the existence of a copresentation by finite sums of an injective hull of the residue field.

```lean
public lemma powerTorsion_and_finiteSocle_iff_exists_finite_copresentation
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (M : Type v) [AddCommGroup M] [Module R M]
    (E : Type u) [AddCommGroup E] [Module R E]
    (i : ResidueField R →ₗ[R] E) [Mono (ModuleCat.ofHom i)]
    (hi : Module.IsInjectiveHull (ModuleCat.ofHom i)) :
    (IsIPowerTorsion R M (maximalIdeal R) ∧ HasFiniteSocle R M) ↔
      ∃ (n m : ℕ) (f : M →ₗ[R] (Fin n → E))
        (g : (Fin n → E) →ₗ[R] (Fin m → E)),
        Function.Injective f ∧ Function.Exact f g
```

## Tag 08Z9, a proposition

[Tag 08Z9](https://stacks.math.columbia.edu/tag/08Z9) in the Stacks Project.

**`Dualizing.isIso_matlisEvaluation_of_isArtinian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean#L1012). The attribute's comment: “biduality for modules with the descending chain condition”.

> The canonical map to the double Matlis dual is an isomorphism for every module satisfying
> the descending chain condition.

```lean
public theorem isIso_matlisEvaluation_of_isArtinian
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    (E M : ModuleCat.{max u v} R)
    (i : residueFieldModule.{u, v} R ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) [IsArtinian R M] :
    IsIso ((matlisEvaluation R E).app M)
```

**`Dualizing.isIso_matlisEvaluation_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean, line 1025](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean#L1025). The attribute's comment: “biduality for modules with the ascending chain condition”.

> The canonical map to the double Matlis dual is an isomorphism for every module satisfying
> the ascending chain condition.

```lean
public theorem isIso_matlisEvaluation_of_isNoetherian
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    (E M : ModuleCat.{max u v} R)
    (i : residueFieldModule.{u, v} R ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) [IsNoetherian R M] :
    IsIso ((matlisEvaluation R E).app M)
```

**`Dualizing.matlisDuality`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean, line 1193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean#L1193). The attribute's comment: “anti-equivalence”. References: SGA 2 IV (5.1), “special case”.

> **Matlis duality (Stacks Project, Tag 08Z9).** The canonical anti-equivalence between
> Artinian and Noetherian modules over a complete local Noetherian ring.

```lean
public noncomputable def matlisDuality
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    (E : ModuleCat.{max u v} R)
    (i : residueFieldModule.{u, v} R ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    (ArtinianModules.{u, v} R)ᵒᵖ ≌ NoetherianModules.{u, v} R
```

**`Dualizing.matlisDualityFunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean, line 1206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean#L1206). The attribute's comment: “the anti-equivalence is induced by the Matlis dual functor”.

> The functor underlying `matlisDuality`, after inclusion in all modules, is naturally
> isomorphic to `Hom_R(-, E)`.

```lean
public noncomputable def matlisDualityFunctorIso
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    (E : ModuleCat.{max u v} R)
    (i : residueFieldModule.{u, v} R ⟶ E) [Mono i]
    (hi : Module.IsInjectiveHull i) :
    (matlisDuality R E i hi).functor ⋙
        ObjectProperty.ι (fun M : ModuleCat.{max u v} R ↦ IsNoetherian R M) ≅
      (ObjectProperty.ι (fun M : ModuleCat.{max u v} R ↦ IsArtinian R M)).op ⋙
        (linearYoneda R (ModuleCat.{max u v} R)).obj E
```

Declarations registered for the tag:

- [`CategoryTheory.linearYoneda`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.linearYoneda#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/Matlis.lean#L119) (StacksFrontier): “the functor”.

## Tag 0EGL, a remark

[Tag 0EGL](https://stacks.math.columbia.edu/tag/0EGL) in the Stacks Project.

**`Dualizing.isArtinian_of_finite_matlisDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Dualizing/ResidueFieldHull/ChainConditions.lean#L195).

> **Stacks Project, Tag 0EGL.** A maximal-ideal-power torsion module whose Matlis dual is finite
> over the completion satisfies the descending chain condition.

```lean
public theorem isArtinian_of_finite_matlisDual
    (R : Type u) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    (N : Type v) [AddCommGroup N] [Module R N]
    (E : Type u) [AddCommGroup E] [Module R E]
    (i : ModuleCat.of R (R ⧸ IsLocalRing.maximalIdeal R) ⟶ ModuleCat.of R E)
    [Mono i] (hi : Module.IsInjectiveHull i)
    (hN : IsIPowerTorsion R N (IsLocalRing.maximalIdeal R))
    (hfinite : letI := matlisDualAdicCompletionModule R N E i hi
      Module.Finite (AdicCompletion (IsLocalRing.maximalIdeal R) R) (N →ₗ[R] E)) :
    IsArtinian R N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.7, Tag 08Z1](https://stacks.math.columbia.edu/tag/08Z1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
