---
declaration: section
origin: cited
lean: factorsThroughProj_iff_free, FactorsThroughProj.submodule, FactorsThroughProj.comp_comp, Module.exists_finite_projective_factorization, Module.isIProjective_iff_free, Module.isIProjective_iff_ext_annihilated, Module.IsIProjective, Module.isIProjective_of_smul_eq_zero
statement: formalized
proof: formalized
---

# 15.72 Modules which are close to being projective

Section 15.72 of the Stacks Project, [Tag 0G8Z](https://stacks.math.columbia.edu/tag/0G8Z). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G90, a lemma

[Tag 0G90](https://stacks.math.columbia.edu/tag/0G90) in the Stacks Project.

**`factorsThroughProj_iff_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L74). The attribute's comment: “(1)”.

> A linear map factors through a projective module if and only if it factors through a free
> module.

```lean
theorem factorsThroughProj_iff_free
    {R : Type u} {M : Type v} {N : Type w} [CommRing R]
    [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N] (φ : M →ₗ[R] N) :
    FactorsThroughProj φ ↔ FactorsThroughFree φ
```

**`FactorsThroughProj.submodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L121). The attribute's comment: “(2)”.

> The `R`-linear maps `M →ₗ[R] N` which factor through a projective `R`-module form an
> `R`-submodule of `M →ₗ[R] N`.

```lean
def FactorsThroughProj.submodule (R : Type u) [CommRing R] (M : Type v) (N : Type w)
    [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N] :
    Submodule R (M →ₗ[R] N)
```

**`FactorsThroughProj.comp_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L144). The attribute's comment: “(3)”.

> Factoring through a projective module is stable under precomposition and postcomposition by
> arbitrary linear maps.

```lean
theorem FactorsThroughProj.comp_comp {R : Type u} [CommRing R] {M : Type v} {N : Type w}
    [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N] {φ : M →ₗ[R] N}
    (hφ : FactorsThroughProj φ) {M' : Type*} {N' : Type*} [AddCommGroup M'] [Module R M']
    [AddCommGroup N'] [Module R N'] (ψ : M' →ₗ[R] M) (ξ : N →ₗ[R] N') :
    FactorsThroughProj (ξ ∘ₗ φ ∘ₗ ψ)
```

## Tag 0G91, a lemma

[Tag 0G91](https://stacks.math.columbia.edu/tag/0G91) in the Stacks Project.

**`Module.exists_finite_projective_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L343).

> A linear map out of a *finite* module which factors through a projective module already
> factors through a *finite* projective module.

```lean
theorem Module.exists_finite_projective_factorization
    {R : Type u} [CommRing R] {M : Type v} {N : Type w}
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    [AddCommGroup N] [Module R N] (φ : M →ₗ[R] N) (hφ : FactorsThroughProj φ) :
    ∃ (P : Type (max u v w)) (_ : AddCommGroup P) (_ : Module R P)
      (_ : Module.Finite R P) (_ : Module.Projective R P)
      (α : M →ₗ[R] P) (β : P →ₗ[R] N), φ = β ∘ₗ α
```

## Tag 0G92, a lemma

[Tag 0G92](https://stacks.math.columbia.edu/tag/0G92) in the Stacks Project.

**`Module.isIProjective_iff_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L165). The attribute's comment: “(1)-(2)”.

> `M` is `I`-projective if and only if for every `a ∈ I` the multiplication-by-`a`
> endomorphism of `M` factors through a free `R`-module.

```lean
theorem Module.isIProjective_iff_free (R : Type u) [CommRing R] (I : Ideal R) (M : Type v)
    [AddCommGroup M] [Module R M] :
    Module.IsIProjective R I M ↔ ∀ a ∈ I, FactorsThroughFree ((LinearMap.lsmul R M) a)
```

**`Module.isIProjective_iff_ext_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L205). The attribute's comment: “(1)-(3)”.

> `M` is `I`-projective if and only if `I` annihilates `Ext¹_R(M, N)` for every `R`-module `N`.

```lean
theorem Module.isIProjective_iff_ext_annihilated (R : Type u) [CommRing R] [Small.{v} R]
    (I : Ideal R) (M : Type v) [AddCommGroup M] [Module R M] :
    Module.IsIProjective R I M ↔
      ∀ (N : Type v) [AddCommGroup N] [Module R N],
        I ≤ Module.annihilator R
          (Abelian.Ext (ModuleCat.of R M) (ModuleCat.of R N) 1)
```

## Tag 0G93, a definition

[Tag 0G93](https://stacks.math.columbia.edu/tag/0G93) in the Stacks Project.

**`Module.IsIProjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L158).

> An `R`-module `M` is *`I`-projective*, for an ideal `I` of `R`, if for every `a ∈ I` the
> multiplication-by-`a` endomorphism `m ↦ a • m` of `M` factors through a projective
> `R`-module.

```lean
def Module.IsIProjective (R : Type u) [CommRing R] (I : Ideal R) (M : Type v)
    [AddCommGroup M] [Module R M] : Prop
```

## Tag 0G94, a lemma

[Tag 0G94](https://stacks.math.columbia.edu/tag/0G94) in the Stacks Project.

**`Module.isIProjective_of_smul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L252).

> If `M` is annihilated by the ideal `I`, that is `a • m = 0` for all `a ∈ I` and `m : M`, then
> `M` is `I`-projective.

```lean
theorem Module.isIProjective_of_smul_eq_zero {R : Type u} [CommRing R] (I : Ideal R) (M : Type v)
    [AddCommGroup M] [Module R M] (h : ∀ a ∈ I, ∀ m : M, a • m = 0) :
    Module.IsIProjective R I M
```

## Tag 0G95, a lemma

[Tag 0G95](https://stacks.math.columbia.edu/tag/0G95) in the Stacks Project.

**`Module.isIProjective_of_injective_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L263).

> Given a short exact sequence `0 → K →[i] P →[p] M → 0` of `R`-modules with `M` `I`-projective
> and `P` projective, the module `K` is `I`-projective.

```lean
theorem Module.isIProjective_of_injective_of_exact {R : Type*} [CommRing R] (I : Ideal R)
    {K P M : Type u} [AddCommGroup K] [Module R K] [AddCommGroup P] [Module R P]
    [Module.Projective R P] [AddCommGroup M] [Module R M] (i : K →ₗ[R] P) (p : P →ₗ[R] M)
    (hi : Function.Injective i) (hp : Function.Surjective p)
    (hexact : LinearMap.range i = LinearMap.ker p)
    (hM : Module.IsIProjective R I M) :
    Module.IsIProjective R I K
```

## Tag 0G96, a lemma

[Tag 0G96](https://stacks.math.columbia.edu/tag/0G96) in the Stacks Project.

**`Module.IsIProjective.dual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/IProjective.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/IProjective.lean#L360).

> If `M` is a finite `I`-projective `R`-module, then its dual `M^∨ = Hom_R(M, R)` is
> `I`-projective.

```lean
theorem Module.IsIProjective.dual (R : Type u) [CommRing R] (I : Ideal R) (M : Type v)
    [AddCommGroup M] [Module R M] [Module.Finite R M]
    (hM : Module.IsIProjective R I M) :
    Module.IsIProjective R I (Module.Dual R M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.72, Tag 0G8Z](https://stacks.math.columbia.edu/tag/0G8Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
