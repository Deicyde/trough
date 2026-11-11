---
declaration: section
origin: cited
lean: Dualizing.length_linearMap_eq, Dualizing.finite_of_isInjectiveHull_residueField, Dualizing.evaluation_bijective_of_isInjectiveHull, Dualizing.algebraMap_end_bijective_of_isInjectiveHull, Dualizing.injectiveHullDual, Dualizing.injectiveHullDualEvaluation, Dualizing.injectiveHullDual_isEquivalence, Dualizing.injectiveHullDual_preservesFiniteLimits
statement: formalized
proof: formalized
---

# 47.6 Duality over Artinian local rings

Section 47.6 of the Stacks Project, [Tag 08YW](https://stacks.math.columbia.edu/tag/08YW). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08YX, a lemma

[Tag 08YX](https://stacks.math.columbia.edu/tag/08YX) in the Stacks Project.

**`Dualizing.length_linearMap_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L284). The attribute's comment: “length equality”.

> **Stacks Project, Tag 08YX.** Taking linear maps into an injective hull of
> the residue field preserves the length of a finite module.

```lean
public lemma length_linearMap_eq (hi : Module.IsInjectiveHull i)
    (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Module.length R (M →ₗ[R] E) = Module.length R M
```

**`Dualizing.finite_of_isInjectiveHull_residueField`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L293). The attribute's comment: “finiteness of the injective hull”.

> **Stacks Project, Tag 08YX.** An injective hull of the residue field of an
> Artinian local ring is finite over the ring.

```lean
public lemma finite_of_isInjectiveHull_residueField
    (hi : Module.IsInjectiveHull i) : Module.Finite R E
```

## Tag 08YY, a lemma

[Tag 08YY](https://stacks.math.columbia.edu/tag/08YY) in the Stacks Project.

**`Dualizing.evaluation_bijective_of_isInjectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L356). The attribute's comment: “the evaluation map”.

> **Stacks Project, Tag 08YY.** Evaluation into an injective hull of the
> residue field identifies every finite module over an Artinian local ring with
> its double dual.

```lean
public theorem evaluation_bijective_of_isInjectiveHull
    (R : Type u) [CommRing R] [IsArtinianRing R] [IsLocalRing R]
    (E : Type u) [AddCommGroup E] [Module R E]
    (i : ModuleCat.of R (IsLocalRing.ResidueField R) ⟶ ModuleCat.of R E)
    [Mono i] (hi : Module.IsInjectiveHull i)
    (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    Function.Bijective
      (LinearMap.flip
        (LinearMap.id : (M →ₗ[R] E) →ₗ[R] (M →ₗ[R] E)))
```

**`Dualizing.algebraMap_end_bijective_of_isInjectiveHull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L395). The attribute's comment: “the endomorphism ring”.

> **Stacks Project, Tag 08YY.** The canonical scalar-action map from an
> Artinian local ring to the endomorphism ring of an injective hull of its
> residue field is bijective.

```lean
public theorem algebraMap_end_bijective_of_isInjectiveHull
    (R : Type u) [CommRing R] [IsArtinianRing R] [IsLocalRing R]
    (E : Type u) [AddCommGroup E] [Module R E]
    (i : ModuleCat.of R (IsLocalRing.ResidueField R) ⟶ ModuleCat.of R E)
    [Mono i] (hi : Module.IsInjectiveHull i) :
    Function.Bijective (algebraMap R (Module.End R E))
```

## Tag 08YZ, a lemma

[Tag 08YZ](https://stacks.math.columbia.edu/tag/08YZ) in the Stacks Project.

**`Dualizing.injectiveHullDual`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L440). The attribute's comment: “the duality functor”.

> Taking linear maps into the injective hull, contravariantly, on finite modules.

```lean
public def injectiveHullDual : (FGModuleCat.{u} R)ᵒᵖ ⥤ FGModuleCat.{u} R
```

**`Dualizing.injectiveHullDualEvaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L455). The attribute's comment: “canonical evaluation transformation”.

> The natural transformation with components the canonical evaluation maps
> `m ↦ (f ↦ f m)` into the `E`-valued double dual.

```lean
public def injectiveHullDualEvaluation :
    𝟭 (FGModuleCat.{u} R) ⟶
      opOp (FGModuleCat.{u} R) ⋙ (injectiveHullDual R E i hi).op ⋙
        injectiveHullDual R E i hi
```

**`Dualizing.injectiveHullDual_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 491](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L491). The attribute's comment: “anti-equivalence”.

> **Stacks Project, Tag 08YZ.** Linear duality with values in an injective hull of the residue
> field is an anti-equivalence of the category of finite modules with itself.

```lean
public theorem injectiveHullDual_isEquivalence :
    (injectiveHullDual R E i hi).IsEquivalence
```

**`Dualizing.injectiveHullDual_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L508). The attribute's comment: “exactness: limits”.

> **Stacks Project, Tag 08YZ.** The `E`-valued duality preserves finite limits, hence takes
> finite colimits of finite modules to finite limits.

```lean
public theorem injectiveHullDual_preservesFiniteLimits :
    PreservesFiniteLimits (injectiveHullDual R E i hi)
```

**`Dualizing.injectiveHullDual_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L516). The attribute's comment: “exactness: colimits”.

> **Stacks Project, Tag 08YZ.** The `E`-valued duality preserves finite colimits, hence takes
> finite limits of finite modules to finite colimits.

```lean
public theorem injectiveHullDual_preservesFiniteColimits :
    PreservesFiniteColimits (injectiveHullDual R E i hi)
```

**`Dualizing.injectiveHullDualEvaluation_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Artinian.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Artinian.lean#L524). The attribute's comment: “canonical double-dual identification”.

> The canonical evaluation maps give a natural isomorphism from the
> identity functor to the square of the `E`-valued duality.

```lean
public theorem injectiveHullDualEvaluation_isIso :
    IsIso (injectiveHullDualEvaluation R E i hi)
```

## Tag 08Z0, a lemma

[Tag 08Z0](https://stacks.math.columbia.edu/tag/08Z0) in the Stacks Project.

**`Dualizing.dualTorsionEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualityArtinianLocal/Basic.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualityArtinianLocal/Basic.lean#L70). The attribute's comment: “the dual of ideal torsion”.

> **Stacks Project, Tag 08Z0.** Restricting a functional to the elements of `M` killed by `I`
> induces the canonical identification of the quotient of the dual of `M` by `I` with the dual of
> that submodule.

```lean
noncomputable def dualTorsionEquiv
    (R : Type u) [CommRing R]
    (E : Type v) [AddCommGroup E] [Module R E] [Module.Injective R (ULift.{u} E)]
    (M : Type w) [AddCommGroup M] [Module R M]
    (I : Ideal R) (hI : I.FG) :
    { e : ((M →ₗ[R] E) ⧸ (I • (⊤ : Submodule R (M →ₗ[R] E)))) ≃ₗ[R]
        (Submodule.torsionBySet R M (I : Set R) →ₗ[R] E) //
      ∀ f : M →ₗ[R] E,
        e (Submodule.Quotient.mk f) =
          f.comp (Submodule.subtype (Submodule.torsionBySet R M (I : Set R))) }
```

**`Dualizing.dualQuotientEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/DualityArtinianLocal/Basic.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/DualityArtinianLocal/Basic.lean#L171). The attribute's comment: “the dual of the quotient by an ideal”.

> **Stacks Project, Tag 08Z0.** Precomposing with the quotient map identifies the dual of
> `M / I M` with the submodule of functionals on `M` killed by `I`.

```lean
noncomputable def dualQuotientEquiv
    (R : Type u) [CommRing R]
    (E : Type v) [AddCommGroup E] [Module R E]
    (M : Type w) [AddCommGroup M] [Module R M]
    (I : Ideal R) :
    { e : ((M ⧸ (I • (⊤ : Submodule R M))) →ₗ[R] E) ≃ₗ[R]
        Submodule.torsionBySet R (M →ₗ[R] E) (I : Set R) //
      ∀ (f : (M ⧸ (I • (⊤ : Submodule R M))) →ₗ[R] E) (m : M),
        (e f : M →ₗ[R] E) m = f (Submodule.Quotient.mk m) }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.6, Tag 08YW](https://stacks.math.columbia.edu/tag/08YW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
