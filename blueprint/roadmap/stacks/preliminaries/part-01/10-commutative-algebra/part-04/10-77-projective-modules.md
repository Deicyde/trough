---
declaration: section
origin: cited
lean: Module.projective_iff_homLeft_shortExact, Module.projective_iff_shortExact_map_linearCoyoneda, Module.projective_iff_preservesFiniteLimits_and_preservesFiniteColimits_linearCoyoneda, characterize_projective, projective_of_ext_one_eq_zero, Module.instProjectiveDFinsupp, Module.exists_projective_quotient_smul_top_linearEquiv_of_isNilpotent, lift_finite_projective_of_locallyNilpotent
statement: formalized
proof: formalized
---

# 10.77 Projective modules

Section 10.77 of the Stacks Project, [Tag 05CD](https://stacks.math.columbia.edu/tag/05CD). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05CE, a definition

[Tag 05CE](https://stacks.math.columbia.edu/tag/05CE) in the Stacks Project.

**`Module.projective_iff_homLeft_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/HomExact.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/HomExact.lean#L65). The attribute's comment: “elementwise form, any ring”.

> An `R`-module `P` is projective if and only if `Hom_R(P, -)` carries every short exact
> sequence `0 → N₁ → N₂ → N₃ → 0` to a short exact sequence
> `0 → Hom(P, N₁) → Hom(P, N₂) → Hom(P, N₃) → 0`.

```lean
theorem projective_iff_homLeft_shortExact :
    Module.Projective R P ↔ ∀ (N₁ N₂ N₃ : Type (max u v)) [AddCommGroup N₁] [Module R N₁]
      [AddCommGroup N₂] [Module R N₂] [AddCommGroup N₃] [Module R N₃]
      (f : N₁ →ₗ[R] N₂) (g : N₂ →ₗ[R] N₃), Function.Injective f → Function.Exact f g →
        Function.Surjective g →
        Function.Injective (LinearMap.compRight (M := P) ℕ f) ∧
        Function.Exact (LinearMap.compRight (M := P) ℕ f) (LinearMap.compRight (M := P) ℕ g) ∧
        Function.Surjective (LinearMap.compRight (M := P) ℕ g)
```

**`Module.projective_iff_shortExact_map_linearCoyoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/HomExact.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/HomExact.lean#L91).

> An `R`-module `P` is projective if and only if the functor
> `Hom_R(P, -) : ModuleCat R ⥤ ModuleCat R` sends short exact sequences to short exact
> sequences.

```lean
theorem projective_iff_shortExact_map_linearCoyoneda :
    Module.Projective R P ↔ ∀ S : ShortComplex (ModuleCat.{max u v} R), S.ShortExact →
      (S.map ((linearCoyoneda R (ModuleCat.{max u v} R)).obj
        (op (ModuleCat.of R P)))).ShortExact
```

**`Module.projective_iff_preservesFiniteLimits_and_preservesFiniteColimits_linearCoyoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/HomExact.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/HomExact.lean#L121). The attribute's comment: “exact functor as preserving finite limits and finite colimits”.

> An `R`-module `P` is projective if and only if the functor
> `Hom_R(P, -) : ModuleCat R ⥤ ModuleCat R` is exact, in the sense that it preserves finite
> limits and finite colimits.

```lean
theorem projective_iff_preservesFiniteLimits_and_preservesFiniteColimits_linearCoyoneda :
    Module.Projective R P ↔
      PreservesFiniteLimits ((linearCoyoneda R (ModuleCat.{max u v} R)).obj
        (op (ModuleCat.of R P))) ∧
      PreservesFiniteColimits ((linearCoyoneda R (ModuleCat.{max u v} R)).obj
        (op (ModuleCat.of R P)))
```

## Tag 05CF, a lemma

[Tag 05CF](https://stacks.math.columbia.edu/tag/05CF) in the Stacks Project.

**`characterize_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/Characterization.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/Characterization.lean#L130). References: EGA 0 (17.2.1), “n = 0”; SGA 5 XV (3.Lemma3), “more general”.

> Theorem (Stacks Tag 05CF). For an `R`-module `P`, the three conditions
> "`P` is projective (lifting property)", "`P` is a direct summand of a free
> module", and "`Ext^1_R(P, M) = 0` for all `M`" are equivalent.

```lean
theorem characterize_projective (P : Type u) [AddCommGroup P] [Module R P] :
    List.TFAE
      [IsProjectiveLifting R P, IsDirectSummandOfFree R P, ExtOneVanishes R P]
```

## Tag 0G8T, a lemma

[Tag 0G8T](https://stacks.math.columbia.edu/tag/0G8T) in the Stacks Project.

**`projective_of_ext_one_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ext/Finiteness.lean, line 607](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ext/Finiteness.lean#L607). References: EGA 0 (17.2.1), “n = 0”; EGA 0 (17.2.8), “special case”.

> Stacks tag 0G8T (Lemma 10.77.3): a finite module `P` over a Noetherian ring `R` is
> projective as soon as `Ext¹_R(P, M)` vanishes for every finite `R`-module `M`.

```lean
theorem projective_of_ext_one_eq_zero {R : Type} [CommRing R] [IsNoetherianRing R]
    (P : Type) [AddCommGroup P] [Module R P] [Module.Finite R P]
    (h : ∀ (M : Type) [AddCommGroup M] [Module R M] [Module.Finite R M],
      Subsingleton (Abelian.Ext (C := ModuleCat R) (ModuleCat.of R P) (ModuleCat.of R M) 1)) :
    Module.Projective R P
```

## Tag 065Q, a lemma

[Tag 065Q](https://stacks.math.columbia.edu/tag/065Q) in the Stacks Project.

Declarations registered for the tag:

- [`Module.instProjectiveDFinsupp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.instProjectiveDFinsupp#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Module/Projective/Characterization.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/Characterization.lean#L150) (StacksFrontier): “a direct sum of projective modules is projective”.

## Tag 07LV, a lemma

[Tag 07LV](https://stacks.math.columbia.edu/tag/07LV) in the Stacks Project.

**`Module.exists_projective_quotient_smul_top_linearEquiv_of_isNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/Lifting.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/Lifting.lean#L376). References: SGA 5 XV (3.Lemma3), “(ii), existence”.

> **Stacks 07LV.** Let `R` be a ring, let `I ⊆ R` be a nilpotent two-sided ideal and let `Q` be
> a projective `R ⧸ I`-module. Then there is a projective `R`-module `P` together with an
> isomorphism `P/IP ≅ Q` of `R ⧸ I`-modules.

```lean
public theorem Module.exists_projective_quotient_smul_top_linearEquiv_of_isNilpotent
    {R : Type u} [Ring R] {I : Ideal R} [I.IsTwoSided] {Q : Type v} [AddCommGroup Q]
    [Module (R ⧸ I) Q] [Module.Projective (R ⧸ I) Q] (hI : IsNilpotent I) :
    ∃ (P : Type (max u v)) (_ : AddCommGroup P) (_ : Module R P),
      Module.Projective R P ∧ Nonempty ((P ⧸ I • (⊤ : Submodule R P)) ≃ₗ[R ⧸ I] Q)
```

## Tag 0D47, a lemma

[Tag 0D47](https://stacks.math.columbia.edu/tag/0D47) in the Stacks Project.

**`lift_finite_projective_of_locallyNilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/Lifting.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/Lifting.lean#L393). References: SGA 5 XV (3.Lemma3), “(ii) existence, finite”.

> **Stacks Tag 0D47 (Lemma 10.77.6).**
> Let `R` be a commutative ring and `I ⊆ R` a locally nilpotent ideal. Let `Pbar` be a
> finite projective `R/I`-module. Then there exists a finite projective `R`-module `P`
> together with an isomorphism of `R/I`-modules `P / I P ≅ Pbar`.

```lean
theorem lift_finite_projective_of_locallyNilpotent
    {R : Type u} [CommRing R] (I : Ideal R)
    (hI : I.IsLocallyNilpotent)
    (Pbar : Type u) [AddCommGroup Pbar] [Module (R ⧸ I) Pbar]
    [Module.Finite (R ⧸ I) Pbar] [Module.Projective (R ⧸ I) Pbar] :
    ∃ (P : Type u) (_ : AddCommGroup P) (_ : Module R P),
      Module.Finite R P ∧ Module.Projective R P ∧
      Nonempty ((P ⧸ (I • (⊤ : Submodule R P))) ≃ₗ[R ⧸ I] Pbar)
```

## Tag 05CG, a lemma

[Tag 05CG](https://stacks.math.columbia.edu/tag/05CG) in the Stacks Project.

**`Module.Flat.projective_of_isNilpotent_of_projective_quotient_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/NilpotentIdeal.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/NilpotentIdeal.lean#L193). References: SGA 5 XV (3.Lemma3), “(ii) flat ⇒ projective”.

> **Stacks 05CG.** Let `R` be a ring, let `I ⊆ R` be a nilpotent ideal and let `M` be a flat
> `R`-module such that `M/IM` is a projective `R ⧸ I`-module. Then `M` is a projective
> `R`-module.

```lean
public theorem Module.Flat.projective_of_isNilpotent_of_projective_quotient_smul_top
    {R : Type u} [CommRing R] {I : Ideal R} {M : Type v} [AddCommGroup M] [Module R M]
    [Module.Flat R M] (hI : IsNilpotent I)
    (hM : Module.Projective (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M))) :
    Module.Projective R M
```

## Tag 0H7M, a lemma

[Tag 0H7M](https://stacks.math.columbia.edu/tag/0H7M) in the Stacks Project.

**`projective_of_projective_quotient_inter_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/Lifting.lean, line 943](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/Lifting.lean#L943).

> Stacks Tag 0H7M, Lemma 10.77.8: if $I \cap J = 0$ and both $P/IP$ (as an
> $R/I$-module) and $P/JP$ (as an $R/J$-module) are projective, then $P$ is a
> projective $R$-module.

```lean
theorem projective_of_projective_quotient_inter_zero
    (R : Type*) [CommRing R] (I J : Ideal R) (hIJ : I ⊓ J = ⊥)
    (P : Type*) [AddCommGroup P] [Module R P]
    (hI : Module.Projective (R ⧸ I) (P ⧸ (I • (⊤ : Submodule R P))))
    (hJ : Module.Projective (R ⧸ J) (P ⧸ (J • (⊤ : Submodule R P)))) :
    Module.Projective R P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.77, Tag 05CD](https://stacks.math.columbia.edu/tag/05CD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
