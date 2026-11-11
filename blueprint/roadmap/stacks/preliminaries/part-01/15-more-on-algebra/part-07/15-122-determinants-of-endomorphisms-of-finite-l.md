---
declaration: section
origin: cited
lean: FiniteLengthEndomorphism.det_exact, FiniteLengthEndomorphism.trace_exact, FiniteLengthEndomorphism.charpoly_exact, FiniteLengthEndomorphism.multiplication_det_eq_norm_pow_length, FiniteLengthEndomorphism.map_det_pow_eq_det_baseChange
statement: formalized
proof: formalized
---

# 15.122 Determinants of endomorphisms of finite length modules

Section 15.122 of the Stacks Project, [Tag 0GSX](https://stacks.math.columbia.edu/tag/0GSX). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GSY, a lemma

[Tag 0GSY](https://stacks.math.columbia.edu/tag/0GSY) in the Stacks Project.

**`FiniteLengthEndomorphism.det_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean, line 724](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean#L724). The attribute's comment: “multiplicativity of the residue-field determinant”.

> Determinant is multiplicative in an equivariant short exact sequence.

```lean
public theorem det_exact (M₁ : Type v₁) (M₂ : Type v₂) (M₃ : Type v₃)
    [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂] [Module R M₂]
    [AddCommGroup M₃] [Module R M₃]
    (h₁ : IsFiniteLength R M₁) (h₂ : IsFiniteLength R M₂) (h₃ : IsFiniteLength R M₃)
    (φ₁ : Module.End R M₁) (φ₂ : Module.End R M₂) (φ₃ : Module.End R M₃)
    (f : M₁ →ₗ[R] M₂) (g : M₂ →ₗ[R] M₃) (hf : Function.Injective f)
    (hexact : Function.Exact f g) (hg : Function.Surjective g)
    (hfφ : f.comp φ₁ = φ₂.comp f) (hgφ : g.comp φ₂ = φ₃.comp g) :
    det R h₂ φ₂ = det R h₁ φ₁ * det R h₃ φ₃
```

**`FiniteLengthEndomorphism.trace_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean, line 737](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean#L737). The attribute's comment: “additivity of the residue-field trace”.

> Trace is additive in an equivariant short exact sequence.

```lean
public theorem trace_exact (M₁ : Type v₁) (M₂ : Type v₂) (M₃ : Type v₃)
    [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂] [Module R M₂]
    [AddCommGroup M₃] [Module R M₃]
    (h₁ : IsFiniteLength R M₁) (h₂ : IsFiniteLength R M₂) (h₃ : IsFiniteLength R M₃)
    (φ₁ : Module.End R M₁) (φ₂ : Module.End R M₂) (φ₃ : Module.End R M₃)
    (f : M₁ →ₗ[R] M₂) (g : M₂ →ₗ[R] M₃) (hf : Function.Injective f)
    (hexact : Function.Exact f g) (hg : Function.Surjective g)
    (hfφ : f.comp φ₁ = φ₂.comp f) (hgφ : g.comp φ₂ = φ₃.comp g) :
    trace R h₂ φ₂ = trace R h₁ φ₁ + trace R h₃ φ₃
```

**`FiniteLengthEndomorphism.charpoly_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean#L750). The attribute's comment: “multiplicativity of the residue-field characteristic polynomial”.

> Characteristic polynomial is multiplicative in an equivariant short exact sequence.

```lean
public theorem charpoly_exact (M₁ : Type v₁) (M₂ : Type v₂) (M₃ : Type v₃)
    [AddCommGroup M₁] [Module R M₁] [AddCommGroup M₂] [Module R M₂]
    [AddCommGroup M₃] [Module R M₃]
    (h₁ : IsFiniteLength R M₁) (h₂ : IsFiniteLength R M₂) (h₃ : IsFiniteLength R M₃)
    (φ₁ : Module.End R M₁) (φ₂ : Module.End R M₂) (φ₃ : Module.End R M₃)
    (f : M₁ →ₗ[R] M₂) (g : M₂ →ₗ[R] M₃) (hf : Function.Injective f)
    (hexact : Function.Exact f g) (hg : Function.Surjective g)
    (hfφ : f.comp φ₁ = φ₂.comp f) (hgφ : g.comp φ₂ = φ₃.comp g) :
    charpoly R h₂ φ₂ = charpoly R h₁ φ₁ * charpoly R h₃ φ₃
```

## Tag 0GSZ, a lemma

[Tag 0GSZ](https://stacks.math.columbia.edu/tag/0GSZ) in the Stacks Project.

**`FiniteLengthEndomorphism.multiplication_det_eq_norm_pow_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean, line 926](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean#L926).

> For a local homomorphism of local rings with finite residue-field extension, the determinant
> over the source residue field of multiplication by `u` on a finite-length target module is the
> appropriate power of the residue-field norm of `u`.

```lean
public theorem multiplication_det_eq_norm_pow_length
    (R : Type u) [CommRing R] [IsLocalRing R]
    (R' : Type v) [CommRing R'] [IsLocalRing R'] [Algebra R R']
    [IsLocalHom (algebraMap R R')]
    [Module.Finite (IsLocalRing.ResidueField R) (IsLocalRing.ResidueField R')]
    (M' : Type w) [AddCommGroup M'] [Module R M'] [Module R' M'] [IsScalarTower R R' M']
    (hM' : IsFiniteLength R' M') (u : R') :
    let hM : IsFiniteLength R M' := Module.length_ne_top_iff.mp <| by
      rw [IsLocalRing.length_restrictScalars R R' M']
      exact WithTop.mul_ne_top (Module.length_ne_top_iff.mpr hM') (by
        rw [Module.length_eq_finrank]
        exact ENat.natCast_ne_top _)
    FiniteLengthEndomorphism.det R hM
        ((LinearMap.lsmul R' M' u).restrictScalars R) =
      Algebra.norm (IsLocalRing.ResidueField R) (IsLocalRing.residue R' u) ^
        (Module.length R' M').toNat
```

## Tag 0GT0, a lemma

[Tag 0GT0](https://stacks.math.columbia.edu/tag/0GT0) in the Stacks Project.

**`FiniteLengthEndomorphism.map_det_pow_eq_det_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean, line 1324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/FiniteLength/Determinant.lean#L1324).

> **Stacks 0GT0.** Under a flat local homomorphism `R → S` whose closed fibre has finite
> length `m`, the determinant of a finite-length module endomorphism after scalar extension is the
> image in the residue field of `S` of the original determinant raised to the power `m`.

```lean
public theorem map_det_pow_eq_det_baseChange
    {R : Type u} {S : Type v} [CommRing R] [CommRing S]
    [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [Module.Flat R S]
    (m : ℕ)
    (hm : Module.length S
      (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)) = m)
    {M : Type w} [AddCommGroup M] [Module R M]
    (hM : IsFiniteLength R M) (phi : Module.End R M) :
    ∃ hMS : IsFiniteLength S (S ⊗[R] M),
      IsLocalRing.ResidueField.map (algebraMap R S)
          (FiniteLengthEndomorphism.det R hM phi ^ m) =
        FiniteLengthEndomorphism.det S hMS (LinearMap.baseChange S phi)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.122, Tag 0GSX](https://stacks.math.columbia.edu/tag/0GSX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
