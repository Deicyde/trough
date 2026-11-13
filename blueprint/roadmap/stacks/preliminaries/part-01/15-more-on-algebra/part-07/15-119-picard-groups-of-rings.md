---
declaration: section
origin: cited
lean: Module.IsInvertibleModule, Module.IsTrivialInvertibleModule, Module.finite_projective_rankAtStalk_one_tfae_invertible_exists_tensor_inverse, Module.isInvertibleModule_iff_invertible
statement: formalized
proof: formalized
---

# 15.119 Picard groups of rings

Section 15.119 of the Stacks Project, [Tag 0AFW](https://stacks.math.columbia.edu/tag/0AFW). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0B8H, a definition

[Tag 0B8H](https://stacks.math.columbia.edu/tag/0B8H) in the Stacks Project.

**`Module.IsInvertibleModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Invertible.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/Invertible.lean#L62).

> An `R`-module `M` is invertible when the functor `M ⊗[R] -` is an equivalence of the
> category of `R`-modules.

```lean
public abbrev Module.IsInvertibleModule
    (R : Type u) [CommRing R] (M : Type u) [AddCommGroup M] [Module R M] : Prop
```

**`Module.IsTrivialInvertibleModule`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Invertible.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/Invertible.lean#L68).

> An invertible `R`-module is trivial if it is isomorphic to `R` as an `R`-module.

```lean
public abbrev Module.IsTrivialInvertibleModule
    (R : Type u) [CommRing R] (M : Type u) [AddCommGroup M] [Module R M] : Prop
```

## Tag 0B8I, a lemma

[Tag 0B8I](https://stacks.math.columbia.edu/tag/0B8I) in the Stacks Project.

**`Module.finite_projective_rankAtStalk_one_tfae_invertible_exists_tensor_inverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Invertible.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/Invertible.lean#L200).

> **Stacks 0B8I.** For an `R`-module `M`, the following are equivalent: `M` is finite
> projective of rank one at every prime, `M` is invertible, and `M` admits a tensor inverse.
> Moreover, every tensor inverse of `M` is isomorphic to the linear dual of `M`.

```lean
public theorem Module.finite_projective_rankAtStalk_one_tfae_invertible_exists_tensor_inverse
    (R : Type u) [CommRing R] (M : Type v) [AddCommGroup M] [Module R M] :
    List.TFAE [
      Module.Finite R M ∧ Module.Projective R M ∧
        Module.rankAtStalk M = Function.const (PrimeSpectrum R) 1,
      Module.Invertible R M,
      ∃ (N : Type (max u v)) (_ : AddCommGroup N) (_ : Module R N),
        Nonempty (TensorProduct R M N ≃ₗ[R] R)] ∧
      ∀ (N : Type w) [AddCommGroup N] [Module R N],
        Nonempty (TensorProduct R M N ≃ₗ[R] R) →
          Nonempty (N ≃ₗ[R] Module.Dual R M)
```

**`Module.isInvertibleModule_iff_invertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Projective/Invertible.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/Invertible.lean#L289).

> **Stacks 0B8I**, the description of invertibility the Stacks Project takes as its
> definition in Tag 0B8H: `M ⊗[R] -` is an equivalence of the category of `R`-modules exactly
> when `M` is invertible. Without this, `Module.IsInvertibleModule` and `Module.Invertible`
> are two unrelated predicates and the equivalence above is about the wrong condition (2).

```lean
public theorem Module.isInvertibleModule_iff_invertible :
    Module.IsInvertibleModule R M ↔ Module.Invertible R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.119, Tag 0AFW](https://stacks.math.columbia.edu/tag/0AFW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
