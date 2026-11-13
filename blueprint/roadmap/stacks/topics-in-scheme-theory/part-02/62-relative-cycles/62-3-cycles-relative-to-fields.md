---
declaration: section
origin: cited
lean: Stacks.Chow.injective_baseChangeCyclePullback_fieldExtension, Stacks.Chow.componentMultiplicity_baseChange_eq_one_or_char_pow, Stacks.Chow.baseChangeCyclePullback_perfectClosure_injective, Stacks.Chow.isElementPowerTorsion_cokernel_baseChangeCyclePullback_perfectClosure
statement: formalized
proof: formalized
---

# 62.3 Cycles relative to fields

Section 62.3 of the Stacks Project, [Tag 0H4E](https://stacks.math.columbia.edu/tag/0H4E). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H4E, the section

[Tag 0H4E](https://stacks.math.columbia.edu/tag/0H4E) in the Stacks Project.

**`Stacks.Chow.injective_baseChangeCyclePullback_fieldExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Injective.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChangeBaseScheme/Injective.lean#L169). The attribute's comment: “the base change map on cycle groups along a field extension, and its injectivity”.

> **Stacks Project, Section 0H4E.** For a scheme `X` locally of finite type over a field `k`
> and an arbitrary extension `K/k` of fields, the base-change homomorphism
> `Z_r(X) ⟶ Z_r(X_K)` on cycle groups is injective. The extension is not assumed algebraic, nor
> even of finite type.

```lean
theorem injective_baseChangeCyclePullback_fieldExtension (k K : Type u) [Field k] [Field K]
    [Algebra k K] {X : Scheme.{u}} (f : X ⟶ Spec (CommRingCat.of k)) [LocallyOfFiniteType f]
    (r : ℤ) :
    Function.Injective (baseChangeCyclePullback (fieldExtensionBaseChangeSituation k K) f r)
```

## Tag 0H4F, a lemma

[Tag 0H4F](https://stacks.math.columbia.edu/tag/0H4F) in the Stacks Project.

**`Stacks.Chow.componentMultiplicity_baseChange_eq_one_or_char_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BaseFieldExtension.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/BaseFieldExtension.lean#L430).

> The multiplicity of an irreducible component of the base change of an integral scheme
> locally of finite type over a field along a field extension is one or, in positive
> characteristic, a power of the characteristic.

```lean
theorem componentMultiplicity_baseChange_eq_one_or_char_pow
    {k K : Type u} [Field k] [Field K] [Algebra k K]
    {Z : Scheme.{u}} (f : Z ⟶ Spec (.of k)) [IsIntegral Z]
    [LocallyOfFiniteType f]
    (ξ : genericPoints
      (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme)) :
    let ZK : Scheme := pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K)))
    componentMultiplicity (𝟙 ZK) ξ = 1 ∨
      (ringChar k ≠ 0 ∧
        ∃ n : ℕ, componentMultiplicity (𝟙 ZK) ξ = (ringChar k : ℤ) ^ n)
```

## Tag 0H4G, a lemma

[Tag 0H4G](https://stacks.math.columbia.edu/tag/0H4G) in the Stacks Project.

**`Stacks.Chow.baseChangeCyclePullback_perfectClosure_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PerfectClosureCycles.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PerfectClosureCycles.lean#L309). The attribute's comment: “injectivity”.

> For an algebraic scheme `X` over a field `k`, the base-change homomorphism
> `Z_r(X) ⟶ Z_r(X_{k^perf})` to the perfect closure of `k` is injective.

```lean
theorem baseChangeCyclePullback_perfectClosure_injective (k : Type u) [Field k] (r : ℕ)
    {X : Scheme.{u}} (f : X ⟶ Spec (CommRingCat.of k)) [LocallyOfFiniteType f]
    [QuasiCompact f] :
    Function.Injective
      (baseChangeCyclePullback (perfectClosureBaseChangeSituation k) f (r : ℤ))
```

**`Stacks.Chow.isElementPowerTorsion_cokernel_baseChangeCyclePullback_perfectClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/PerfectClosureCycles.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/PerfectClosureCycles.lean#L322). The attribute's comment: “p-power torsion cokernel”.

> For an algebraic scheme `X` over a field `k` of characteristic `p > 0`, the cokernel of the
> base-change homomorphism `Z_r(X) ⟶ Z_r(X_{k^perf})` to the perfect closure of `k` is a `p`-power
> torsion module.

```lean
theorem isElementPowerTorsion_cokernel_baseChangeCyclePullback_perfectClosure (k : Type u)
    [Field k] (p : ℕ) [CharP k p] (hp : 0 < p) (r : ℕ) {X : Scheme.{u}}
    (f : X ⟶ Spec (CommRingCat.of k)) [LocallyOfFiniteType f] [QuasiCompact f] :
    IsElementPowerTorsion ℤ
      (CycleGroup (perfectClosureBaseChangeSituation k).baseChange
          (pullback.snd f (perfectClosureBaseChangeSituation k).g)
          ((r : ℤ) + (perfectClosureBaseChangeSituation k).c) ⧸
        (baseChangeCyclePullback (perfectClosureBaseChangeSituation k) f (r : ℤ)).range)
      (p : ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.3, Tag 0H4E](https://stacks.math.columbia.edu/tag/0H4E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
