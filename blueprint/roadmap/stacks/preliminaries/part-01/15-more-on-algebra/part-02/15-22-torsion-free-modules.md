---
declaration: section
origin: cited
lean: Submodule.torsion, Module.IsTorsionFree, Module.IsTorsion, Submodule.mem_torsion_iff, Submodule.QuotientTorsion.instIsTorsionFree, IsLocalizedModule.isTorsionFree, isTorsionFree_baseChange_of_flat, isTorsionFree_of_injective_of_exact
statement: formalized
proof: formalized
---

# 15.22 Torsion free modules

Section 15.22 of the Stacks Project, [Tag 0549](https://stacks.math.columbia.edu/tag/0549). 12 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0536, a definition

[Tag 0536](https://stacks.math.columbia.edu/tag/0536) in the Stacks Project.

Declarations registered for the tag:

- [`Submodule.torsion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.torsion#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L357) (StacksFrontier): “(1): torsion elements”. References: EGA I (7.4.1), “special case”; EGA I (7.4.7), “special case”.
- [`Module.IsTorsionFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.IsTorsionFree#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L360) (StacksFrontier): “(2): torsion-free modules”. References: EGA I (7.4.1), “special case”; EGA I (7.4.7), “special case”; SGA 7 X (2.26).
- [`Module.IsTorsion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.IsTorsion#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L364) (StacksFrontier): “(3): torsion modules”. References: EGA I (7.4.1), “special case”; EGA I (7.4.7), “special case”.

## Tag 0537, a lemma

[Tag 0537](https://stacks.math.columbia.edu/tag/0537) in the Stacks Project.

Declarations registered for the tag:

- [`Submodule.torsion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.torsion#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L368) (StacksFrontier): “the torsion submodule”. References: EGA I (7.4.1), “special case”; EGA I (7.4.7), “special case”.
- [`Submodule.mem_torsion_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.mem_torsion_iff#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L369) (StacksFrontier): “its elements are exactly the torsion elements”.
- [`Submodule.QuotientTorsion.instIsTorsionFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.QuotientTorsion.instIsTorsionFree#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L370) (StacksFrontier): “the quotient by the torsion submodule is torsion-free”. References: EGA I (7.4.1), “special case”; SGA 7 I (1.3), “partial”.

## Tag 0AUR, a lemma

[Tag 0AUR](https://stacks.math.columbia.edu/tag/0AUR) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalizedModule.isTorsionFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalizedModule.isTorsionFree#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L386) (StacksFrontier).

## Tag 0AXM, a lemma

[Tag 0AXM](https://stacks.math.columbia.edu/tag/0AXM) in the Stacks Project.

**`isTorsionFree_baseChange_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L84). References: EGA IV (9.4.9), “partial”.

> If `R` is a domain, `R'` is a flat `R`-algebra and `M` is a torsion-free `R`-module, then the
> base change `R' ⊗[R] M` is a torsion-free `R'`-module.

```lean
theorem isTorsionFree_baseChange_of_flat
    {R R' : Type*} [CommRing R] [CommRing R'] [Algebra R R']
    [IsDomain R] [Module.Flat R R']
    {M : Type*} [AddCommGroup M] [Module R M] [Module.IsTorsionFree R M] :
    Module.IsTorsionFree R' (TensorProduct R R' M)
```

## Tag 0AUS, a lemma

[Tag 0AUS](https://stacks.math.columbia.edu/tag/0AUS) in the Stacks Project.

**`isTorsionFree_of_injective_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L104).

> For an injective exact pair of module maps, if the source and target modules are torsion-free,
> then the middle module is torsion-free.

```lean
theorem isTorsionFree_of_injective_of_exact
    {R : Type u} [Semiring R]
    {M : Type v} {M' : Type w} {M'' : Type x}
    [AddCommGroup M] [Module R M]
    [AddCommGroup M'] [Module R M']
    [AddCommGroup M''] [Module R M'']
    (f : M →ₗ[R] M') (g : M' →ₗ[R] M'')
    (hf : Function.Injective f) (hfg : Function.Exact f g)
    [Module.IsTorsionFree R M] [Module.IsTorsionFree R M''] :
    Module.IsTorsionFree R M'
```

## Tag 0AUT, a lemma

[Tag 0AUT](https://stacks.math.columbia.edu/tag/0AUT) in the Stacks Project.

**`isTorsionFree_iff_isLocalized_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L130).

> A module over a domain is torsion-free if and only if its localization at every maximal ideal
> is torsion-free over the corresponding localized ring.

```lean
theorem isTorsionFree_iff_isLocalized_maximal
    {R : Type u} [CommRing R] [IsDomain R]
    {M : Type v} [AddCommMonoid M] [Module R M]
    (Rₚ : ∀ (P : Ideal R) [P.IsMaximal], Type w)
    [∀ (P : Ideal R) [P.IsMaximal], CommRing (Rₚ P)]
    [∀ (P : Ideal R) [P.IsMaximal], Algebra R (Rₚ P)]
    [∀ (P : Ideal R) [P.IsMaximal], IsLocalization.AtPrime (Rₚ P) P]
    (Mₚ : ∀ (P : Ideal R) [P.IsMaximal], Type x)
    [∀ (P : Ideal R) [P.IsMaximal], AddCommMonoid (Mₚ P)]
    [∀ (P : Ideal R) [P.IsMaximal], Module R (Mₚ P)]
    [∀ (P : Ideal R) [P.IsMaximal], Module (Rₚ P) (Mₚ P)]
    [∀ (P : Ideal R) [P.IsMaximal], IsScalarTower R (Rₚ P) (Mₚ P)]
    (f : ∀ (P : Ideal R) [P.IsMaximal], M →ₗ[R] Mₚ P)
    [∀ (P : Ideal R) [P.IsMaximal], IsLocalizedModule.AtPrime P (f P)] :
    Module.IsTorsionFree R M ↔
      ∀ (P : Ideal R) [P.IsMaximal], Module.IsTorsionFree (Rₚ P) (Mₚ P)
```

## Tag 0AUU, a lemma

[Tag 0AUU](https://stacks.math.columbia.edu/tag/0AUU) in the Stacks Project.

**`isTorsionFree_iff_exists_injective_to_finite_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L210).

> A finite module over a domain is torsion-free if and only if it embeds into a finite free
> module.

```lean
theorem isTorsionFree_iff_exists_injective_to_finite_free
    {R : Type u} [CommRing R] [IsDomain R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Module.IsTorsionFree R M ↔
      ∃ N : ModuleCat.{max u v} R,
        Module.Finite R N ∧ Module.Free R N ∧
          ∃ f : M →ₗ[R] N, Function.Injective f
```

## Tag 0AUV, a lemma

[Tag 0AUV](https://stacks.math.columbia.edu/tag/0AUV) in the Stacks Project.

**`isTorsionFree_iff_finiteFreeEmbedding_iff_associatedPrimes_iff_propertyS1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L293).

> For a nonzero finite module over a Noetherian domain, the following are equivalent: it is
> torsion-free; it embeds into a finite free module; its only associated prime is zero; zero lies in
> its support and it satisfies `(S₁)`; and zero lies in its support and it has no embedded associated
> prime.

```lean
theorem isTorsionFree_iff_finiteFreeEmbedding_iff_associatedPrimes_iff_propertyS1
    {R : Type u} [CommRing R] [IsDomain R] [IsNoetherianRing R]
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] [Nontrivial M] :
    (Module.IsTorsionFree R M ↔
      ∃ N : ModuleCat.{max u v} R,
        Module.Finite R N ∧ Module.Free R N ∧
          ∃ f : M →ₗ[R] N, Function.Injective f) ∧
    ((∃ N : ModuleCat.{max u v} R,
        Module.Finite R N ∧ Module.Free R N ∧
          ∃ f : M →ₗ[R] N, Function.Injective f) ↔
      associatedPrimes R M = {⊥}) ∧
    (associatedPrimes R M = {⊥} ↔
      (⊥ : PrimeSpectrum R) ∈ Module.support R M ∧
        ∀ p : PrimeSpectrum R,
          min 1 (Module.supportDim (Localization.AtPrime p.asIdeal)
              (LocalizedModule p.asIdeal.primeCompl M)) ≤
            (Module.depth (Localization.AtPrime p.asIdeal)
              (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
              (LocalizedModule p.asIdeal.primeCompl M) : WithBot ℕ∞)) ∧
    (((⊥ : PrimeSpectrum R) ∈ Module.support R M ∧
        ∀ p : PrimeSpectrum R,
          min 1 (Module.supportDim (Localization.AtPrime p.asIdeal)
              (LocalizedModule p.asIdeal.primeCompl M)) ≤
            (Module.depth (Localization.AtPrime p.asIdeal)
              (IsLocalRing.maximalIdeal (Localization.AtPrime p.asIdeal))
              (LocalizedModule p.asIdeal.primeCompl M) : WithBot ℕ∞)) ↔
      (⊥ : PrimeSpectrum R) ∈ Module.support R M ∧
        ∀ p ∈ associatedPrimes R M, Minimal (· ∈ associatedPrimes R M) p)
```

## Tag 0538, a lemma

[Tag 0538](https://stacks.math.columbia.edu/tag/0538) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat.isTorsionFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.isTorsionFree#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 375](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L375) (StacksFrontier). References: EGA 0 (6.3.4), “more general”; EGA IV (20.1.5), “special case”; EGA IV (21.5.3), “partial”; SGA 1 IV (1.3), “more general”; SGA 3 XV (4.7), “partial”.

## Tag 0539, a lemma

[Tag 0539](https://stacks.math.columbia.edu/tag/0539) in the Stacks Project.

Declarations registered for the tag:

- [`Submodule.isTorsionFree_iff_torsion_eq_bot`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.isTorsionFree_iff_torsion_eq_bot#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L382) (StacksFrontier): “the bridge from trivial torsion submodule to torsion-freeness”. References: EGA I (7.4.1), “special case”.

## Tag 0AUW, a lemma

[Tag 0AUW](https://stacks.math.columbia.edu/tag/0AUW) in the Stacks Project.

**`projective_of_finite_isTorsionFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L344). The attribute's comment: “(2)”. References: EGA 0 (6.3.4), “finite, Dedekind domain”.

> A finite torsion-free module over a Dedekind domain is projective, hence finite locally free.

```lean
theorem projective_of_finite_isTorsionFree
    (R : Type u) [CommRing R] [IsDedekindDomain R]
    (M : Type v) [AddCommGroup M] [Module R M]
    [Module.Finite R M] [Module.IsTorsionFree R M] :
    Module.Projective R M
```

Declarations registered for the tag:

- [`Submodule.isTorsionFree_iff_torsion_eq_bot`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Submodule.isTorsionFree_iff_torsion_eq_bot#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L388) (StacksFrontier): “(1), trivial torsion versus torsion-freeness”. References: EGA I (7.4.1), “special case”.
- [`Module.free_iff_isTorsionFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.free_iff_isTorsionFree#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L390) (StacksFrontier): “(3), finite torsion-free modules over a PID are finite free”. References: EGA 0 (6.3.4), “more general”; SGA 6 IX (1.7), “more general”.

## Tag 0AUX, a lemma

[Tag 0AUX](https://stacks.math.columbia.edu/tag/0AUX) in the Stacks Project.

Declarations registered for the tag:

- [`LinearMap.instIsTorsionFree`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LinearMap.instIsTorsionFree#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/TorsionFree.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/TorsionFree.lean#L395) (StacksFrontier): “the semilinear form specializes to linear maps over a domain”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.22, Tag 0549](https://stacks.math.columbia.edu/tag/0549)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
