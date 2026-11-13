---
declaration: section
origin: cited
lean: Module.IsStablyIso, Module.isStablyFree_iff_exists_isStablyIso, Module.isStablyFree_two_out_of_three, Module.exists_isStablyFree_lift, Module.projective_of_projective_quotient_of_le_jacobson, lift_iso_of_quot_iso, quot_iso_lift
statement: formalized
proof: formalized
---

# 15.3 Stably free modules

Section 15.3 of the Stacks Project, [Tag 0BC2](https://stacks.math.columbia.edu/tag/0BC2). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BC3, a definition

[Tag 0BC3](https://stacks.math.columbia.edu/tag/0BC3) in the Stacks Project.

**`Module.IsStablyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/StablyFree.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/StablyFree.lean#L70). The attribute's comment: “(1)”.

> Two modules are *stably isomorphic* if adding finite free summands to each gives isomorphic
> modules.

```lean
def IsStablyIso (R : Type u) [Ring R] (M : Type v) [AddCommGroup M] [Module R M]
    (N : Type*) [AddCommGroup N] [Module R N] : Prop
```

**`Module.isStablyFree_iff_exists_isStablyIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/StablyFree.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/StablyFree.lean#L77). The attribute's comment: “(2)”.

> A module is stably free precisely when it is stably isomorphic to a free module. This
> identifies Mathlib's `Module.IsStablyFree` with the source definition.

```lean
theorem isStablyFree_iff_exists_isStablyIso (R : Type u) [Ring R]
    (M : Type v) [AddCommGroup M] [Module R M] :
    IsStablyFree R M ↔ ∃ F : ModuleCat.{max u v} R, Module.Free R F ∧ IsStablyIso R M F
```

## Tag 0BC4, a lemma

[Tag 0BC4](https://stacks.math.columbia.edu/tag/0BC4) in the Stacks Project.

**`Module.isStablyFree_two_out_of_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/StablyFree.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/StablyFree.lean#L159).

> In a short exact sequence of finite modules with projective quotient, if any two of the three
> terms are stably free, then so is the third.

```lean
theorem isStablyFree_two_out_of_three {R : Type u} [Ring R]
    {P' : Type v} [AddCommGroup P'] [Module R P'] [Module.Finite R P']
    {P : Type w} [AddCommGroup P] [Module R P] [Module.Finite R P]
    {P'' : Type x} [AddCommGroup P''] [Module R P''] [Module.Finite R P''] [Module.Projective R P'']
    (f : P' →ₗ[R] P) (g : P →ₗ[R] P'')
    (hf : Function.Injective f) (hfg : Function.Exact f g) (hg : Function.Surjective g) :
    ((IsStablyFree R P' ∧ IsStablyFree R P) → IsStablyFree R P'') ∧
      ((IsStablyFree R P' ∧ IsStablyFree R P'') → IsStablyFree R P) ∧
      ((IsStablyFree R P ∧ IsStablyFree R P'') → IsStablyFree R P')
```

## Tag 0BC5, a lemma

[Tag 0BC5](https://stacks.math.columbia.edu/tag/0BC5) in the Stacks Project.

**`Module.exists_isStablyFree_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/StablyFree.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/StablyFree.lean#L256).

> Let `I` be an ideal of `R` such that every element of `1 + I` is a unit, in other words `I` is
> contained in the Jacobson radical. Then every finite stably free `R ⧸ I`-module `E` is the
> reduction modulo `I` of a finite stably free `R`-module.

```lean
theorem exists_isStablyFree_lift (I : Ideal R) (hI : ∀ x ∈ I, IsUnit (1 + x))
    {E : Type v} [AddCommGroup E] [Module (R ⧸ I) E] [Module.Finite (R ⧸ I) E]
    [IsStablyFree (R ⧸ I) E] :
    ∃ M : ModuleCat.{max u v} R, Module.Finite R M ∧ IsStablyFree R M ∧
      Nonempty ((M ⧸ (I • (⊤ : Submodule R M))) ≃ₗ[R ⧸ I] E)
```

## Tag 0D48, a lemma

[Tag 0D48](https://stacks.math.columbia.edu/tag/0D48) in the Stacks Project.

**`Module.projective_of_projective_quotient_of_le_jacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/OfQuotient.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/OfQuotient.lean#L204).

> **Stacks 0D48.** Let `I` be an ideal contained in the Jacobson radical of `R`, equivalently an
> ideal every element of whose coset `1 + I` is a unit. A finite flat `R`-module whose reduction
> `M / IM` is projective over `R ⧸ I` is itself projective.

```lean
theorem projective_of_projective_quotient_of_le_jacobson (I : Ideal R)
    {M : Type v} [AddCommGroup M] [Module R M] [Module.Finite R M] [Module.Flat R M]
    (hI : I ≤ Ideal.jacobson (⊥ : Ideal R))
    (hM : Module.Projective (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M))) : Module.Projective R M
```

## Tag 0BC6, a lemma

[Tag 0BC6](https://stacks.math.columbia.edu/tag/0BC6) in the Stacks Project.

**`lift_iso_of_quot_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Nakayama.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/Nakayama.lean#L115). The attribute's comment: “(1)”. References: EGA 0 (19.1.10), “special case”; SGA 3 VIIB (0.3.4), “Corollary (ii) of 0.3.4”.

> **(Lifting isomorphisms.)** If `φ : P → P'` is an `R`-module map between finite
> projective modules whose induced map `P/IP → P'/IP'` is an isomorphism (bijective),
> then `φ` itself is an isomorphism.

```lean
theorem lift_iso_of_quot_iso
    {R : Type*} [CommRing R] (I : Ideal R)
    (hI : ∀ x ∈ I, IsUnit (1 + x))
    {P P' : Type*} [AddCommGroup P] [Module R P] [Module.Finite R P] [Module.Projective R P]
    [AddCommGroup P'] [Module R P'] [Module.Finite R P'] [Module.Projective R P']
    (φ : P →ₗ[R] P') (h : Function.Bijective (inducedQuot I φ)) :
    Function.Bijective φ
```

**`quot_iso_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Nakayama.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/Nakayama.lean#L132). The attribute's comment: “(2)”. References: SGA 5 XV (3.Lemma3), “(ii), special case”.

> **(Lifting the isomorphism class.)** If `P/IP ≅ P'/IP'` as `R`-modules, then
> `P ≅ P'` as `R`-modules.

```lean
theorem quot_iso_lift
    {R : Type*} [CommRing R] (I : Ideal R)
    (hI : ∀ x ∈ I, IsUnit (1 + x))
    {P P' : Type*} [AddCommGroup P] [Module R P] [Module.Finite R P] [Module.Projective R P]
    [AddCommGroup P'] [Module R P'] [Module.Finite R P'] [Module.Projective R P']
    (h : Nonempty ((P ⧸ (I • (⊤ : Submodule R P))) ≃ₗ[R] (P' ⧸ (I • (⊤ : Submodule R P'))))) :
    Nonempty (P ≃ₗ[R] P')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.3, Tag 0BC2](https://stacks.math.columbia.edu/tag/0BC2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
