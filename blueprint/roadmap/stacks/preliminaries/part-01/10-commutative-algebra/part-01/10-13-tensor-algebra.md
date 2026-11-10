---
declaration: section
origin: cited
lean: exteriorPower_free, symmetricPower_free, symmetric_and_exterior_power_presentation, exists_presentation_exteriorPower_and_symmetricPower, exteriorPower.ker_eq_span_of_tprod_eq_ιMulti, exteriorPower.ker_eq_span_of_tprod_eq_ιMulti_of_two_lt, TensorAlgebra.ofDirectLimit_bijective, SymmetricAlgebra.ofDirectLimit_bijective
statement: formalized
proof: formalized
---

# 10.13 Tensor algebra

Section 10.13 of the Stacks Project, [Tag 00DM](https://stacks.math.columbia.edu/tag/00DM). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00DN, a lemma

[Tag 00DN](https://stacks.math.columbia.edu/tag/00DN) in the Stacks Project.

**`exteriorPower_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/SymmetricPower/Free.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/SymmetricPower/Free.lean#L37). References: EGA 0 (5.5.4), “free case”; SGA 6 X (6.1), “special case”.

> If `M` is a free `R`-module, then for every `n ≥ 0` the `n`-th exterior power `⋀^n(M)` is a
> free `R`-module.

```lean
theorem exteriorPower_free
    (R : Type*) [CommRing R] (M : Type*) [AddCommGroup M] [Module R M]
    [Module.Free R M] (n : ℕ) :
    Module.Free R (ExteriorAlgebra.exteriorPower R n M)
```

**`symmetricPower_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/SymmetricPower/Free.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/SymmetricPower/Free.lean#L299).

> If `M` is a free `R`-module, then for every `n ≥ 0` the `n`-th symmetric power `Sym^n(M)` is
> a free `R`-module.

```lean
theorem symmetricPower_free
    (R : Type) [CommSemiring R] (M : Type*) [AddCommMonoid M] [Module R M]
    [Module.Free R M] (n : ℕ) :
    Module.Free R (SymmetricPower R (Fin n) M)
```

## Tag 00DO, a lemma

[Tag 00DO](https://stacks.math.columbia.edu/tag/00DO) in the Stacks Project.

**`symmetric_and_exterior_power_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/SymmetricPower/Presentation.lean, line 992](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/SymmetricPower/Presentation.lean#L992).

> Let `R` be a commutative ring and let
> `M₂ --g--> M₁ --f--> M → 0` be an exact sequence of `R`-modules (`f` surjective and
> `range g = ker f`).  With `n = k + 1 ≥ 1`, both presentation sequences are exact:
>
> * symmetric: `M₂ ⊗ Sym^k(M₁) --α--> Sym^{k+1}(M₁) --Sym^{k+1}(f)--> Sym^{k+1}(M) → 0`;
> * exterior:  `M₂ ⊗ ∧^k(M₁) --β--> ∧^{k+1}(M₁) --∧^{k+1}(f)--> ∧^{k+1}(M) → 0`.
>
> In each case the right-hand map is surjective and the image of the left-hand connecting
> map equals the kernel of the right-hand map.

```lean
theorem symmetric_and_exterior_power_presentation
    {R : Type*} [CommRing R]
    {M M₁ M₂ : Type*}
    [AddCommGroup M] [Module R M] [AddCommGroup M₁] [Module R M₁]
    [AddCommGroup M₂] [Module R M₂]
    (g : M₂ →ₗ[R] M₁) (f : M₁ →ₗ[R] M)
    (hf : Function.Surjective f) (hexact : LinearMap.range g = LinearMap.ker f)
    (k : ℕ) :
    (Function.Surjective (symMap (k + 1) f) ∧
        LinearMap.range (symMulMap k g) = LinearMap.ker (symMap (k + 1) f)) ∧
      (Function.Surjective (exteriorPower.map (k + 1) f) ∧
        LinearMap.range (beta k g) = LinearMap.ker (exteriorPower.map (k + 1) f))
```

## Tag 00DP, a lemma

[Tag 00DP](https://stacks.math.columbia.edu/tag/00DP) in the Stacks Project.

**`exists_presentation_exteriorPower_and_symmetricPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/SymmetricPower/QuotientOfTensorPower.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/SymmetricPower/QuotientOfTensorPower.lean#L300).

> **Stacks Tag 00DP.** Let `M` be a module over a commutative ring `R` with a
> generating system `x : I → M`, and let `n + 2 ≥ 2`. There are canonical exact
> sequences
>
>   `(⊕ relators) → Tⁿ⁺²(M) → ⋀ⁿ⁺²(M) → 0`   and
>   `(⊕ relators) → Tⁿ⁺²(M) → Symⁿ⁺²(M) → 0`,
>
> with the relator maps and projections determined by their values on pure tensors
> as described in the module docstring.

```lean
theorem exists_presentation_exteriorPower_and_symmetricPower {I : Type*} [DecidableEq I] (x : I → M)
    (hx : Submodule.span R (Set.range x) = ⊤) (n : ℕ) :
    -- exterior power presentation
    (∃ (Φ : DirectSum ((SlotPair n × I × I) ⊕ (SlotPair n × I)) (fun _ => ⨂[R]^n M)
              →ₗ[R] ⨂[R]^(n + 2) M)
       (π : ⨂[R]^(n + 2) M →ₗ[R] ⋀[R]^(n + 2) M),
        (∀ (jp : SlotPair n) (i₁ i₂ : I) (f : Fin n → M),
          Φ (DirectSum.lof R _ _ (Sum.inl (jp, i₁, i₂)) (⨂ₜ[R] k, f k))
            = (⨂ₜ[R] k, insTwo jp.1.1 jp.1.2 jp.2 (x i₁) (x i₂) f k)
              + (⨂ₜ[R] k, insTwo jp.1.1 jp.1.2 jp.2 (x i₂) (x i₁) f k)) ∧
        (∀ (jp : SlotPair n) (i : I) (f : Fin n → M),
          Φ (DirectSum.lof R _ _ (Sum.inr (jp, i)) (⨂ₜ[R] k, f k))
            = (⨂ₜ[R] k, insTwo jp.1.1 jp.1.2 jp.2 (x i) (x i) f k)) ∧
        (∀ f : Fin (n + 2) → M, π (⨂ₜ[R] k, f k) = exteriorPower.ιMulti R (n + 2) f) ∧
        Function.Exact Φ π ∧ Function.Surjective π) ∧
    -- symmetric power presentation
    (∃ (Ψ : DirectSum (SlotPair n × I × I) (fun _ => ⨂[R]^n M) →ₗ[R] ⨂[R]^(n + 2) M)
       (ρ : ⨂[R]^(n + 2) M →ₗ[R] Sym[R]^(n + 2) M),
        (∀ (jp : SlotPair n) (i₁ i₂ : I) (f : Fin n → M),
          Ψ (DirectSum.lof R _ _ (jp, i₁, i₂) (⨂ₜ[R] k, f k))
            = (⨂ₜ[R] k, insTwo jp.1.1 jp.1.2 jp.2 (x i₁) (x i₂) f k)
              - (⨂ₜ[R] k, insTwo jp.1.1 jp.1.2 jp.2 (x i₂) (x i₁) f k)) ∧
        (∀ f : Fin (n + 2) → M, ρ (⨂ₜ[R] k, f k) = ⨂ₛ[R] k, f k) ∧
        Function.Exact Ψ ρ ∧ Function.Surjective ρ)
```

## Tag 0H1C, a lemma

[Tag 0H1C](https://stacks.math.columbia.edu/tag/0H1C) in the Stacks Project.

**`exteriorPower.ker_eq_span_of_tprod_eq_ιMulti`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/ExteriorPower/Presentation.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/ExteriorPower/Presentation.lean#L360). The attribute's comment: “first family `mᵢ = b • mⱼ`, not `mᵢ = mⱼ`: the latter fails for `n = 2`”.

> **Stacks 0H1C.** Let `A → B` be a ring map, let `M` be a `B`-module and let `n ≥ 1`.
> The kernel of the canonical `A`-linear map `M ⊗_A ⋯ ⊗_A M → ⋀[B]^n M`,
> `m₁ ⊗ ⋯ ⊗ mₙ ↦ m₁ ∧ ⋯ ∧ mₙ`, is generated as an `A`-module by the pure tensors
> `m₁ ⊗ ⋯ ⊗ mₙ` with `mᵢ = b • mⱼ` for some `i ≠ j` and `b ∈ B`, together with the
> differences `m₁ ⊗ ⋯ ⊗ b mᵢ ⊗ ⋯ ⊗ mₙ - m₁ ⊗ ⋯ ⊗ b mⱼ ⊗ ⋯ ⊗ mₙ` for `i ≠ j` and `b ∈ B`.

```lean
theorem exteriorPower.ker_eq_span_of_tprod_eq_ιMulti
    {A B M : Type*} [CommRing A] [CommRing B] [Algebra A B] [AddCommGroup M]
    [Module A M] [Module B M] [IsScalarTower A B M] {n : ℕ} (hn : 0 < n)
    (φ : (⨂[A]^n M) →ₗ[A] ⋀[B]^n M)
    (hφ : ∀ m : Fin n → M, φ (PiTensorProduct.tprod A m) = exteriorPower.ιMulti B n m) :
    LinearMap.ker φ =
      Submodule.span A
        ({x | ∃ (m : Fin n → M) (i j : Fin n) (b : B), i ≠ j ∧ m i = b • m j ∧
              PiTensorProduct.tprod A m = x} ∪
          {x | ∃ (m : Fin n → M) (i j : Fin n) (b : B), i ≠ j ∧
              PiTensorProduct.tprod A (Function.update m i (b • m i)) -
                PiTensorProduct.tprod A (Function.update m j (b • m j)) = x})
```

**`exteriorPower.ker_eq_span_of_tprod_eq_ιMulti_of_two_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/ExteriorPower/Presentation.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/ExteriorPower/Presentation.lean#L379). The attribute's comment: “the stated form, for `n ≥ 3`”.

> For `2 < n` the tensors with two equal entries, together with the scaling differences,
> already generate the kernel.

```lean
theorem exteriorPower.ker_eq_span_of_tprod_eq_ιMulti_of_two_lt
    {A B M : Type*} [CommRing A] [CommRing B] [Algebra A B] [AddCommGroup M]
    [Module A M] [Module B M] [IsScalarTower A B M] {n : ℕ} (hn : 2 < n)
    (φ : (⨂[A]^n M) →ₗ[A] ⋀[B]^n M)
    (hφ : ∀ m : Fin n → M, φ (tprod A m) = exteriorPower.ιMulti B n m) :
    LinearMap.ker φ =
      Submodule.span A
        ({x | ∃ (m : Fin n → M) (i j : Fin n), i ≠ j ∧ m i = m j ∧ tprod A m = x} ∪
          {x | ∃ (m : Fin n → M) (i j : Fin n) (b : B), i ≠ j ∧
              tprod A (update m i (b • m i)) - tprod A (update m j (b • m j)) = x})
```

## Tag 00DQ, a lemma

[Tag 00DQ](https://stacks.math.columbia.edu/tag/00DQ) in the Stacks Project.

**`TensorAlgebra.ofDirectLimit_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorAlgebra/Colimit.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorAlgebra/Colimit.lean#L168). The attribute's comment: “tensor”.

> Forming the tensor algebra commutes with directed colimits: the canonical algebra map
> `colim T(M_i) → T(colim M_i)` is a bijection.

```lean
theorem TensorAlgebra.ofDirectLimit_bijective :
    Function.Bijective (TensorAlgebra.ofDirectLimit f)
```

**`SymmetricAlgebra.ofDirectLimit_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorAlgebra/Colimit.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorAlgebra/Colimit.lean#L315). The attribute's comment: “symmetric”.

> Forming the symmetric algebra commutes with directed colimits: the canonical algebra map
> `colim Sym(M_i) → Sym(colim M_i)` is a bijection.

```lean
theorem SymmetricAlgebra.ofDirectLimit_bijective :
    Function.Bijective (SymmetricAlgebra.ofDirectLimit f)
```

**`ExteriorAlgebra.ofDirectLimit_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorAlgebra/Colimit.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorAlgebra/Colimit.lean#L433). The attribute's comment: “exterior”.

> Forming the exterior algebra commutes with directed colimits: the canonical algebra map
> `colim ⋀(M_i) → ⋀(colim M_i)` is a bijection.

```lean
theorem ExteriorAlgebra.ofDirectLimit_bijective :
    Function.Bijective (ExteriorAlgebra.ofDirectLimit f)
```

## Tag 0C6F, a lemma

[Tag 0C6F](https://stacks.math.columbia.edu/tag/0C6F) in the Stacks Project.

**`TensorAlgebra.exists_algEquiv_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorAlgebra/Localization.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorAlgebra/Localization.lean#L32). The attribute's comment: “(1)”.

> The tensor algebra of a base change is isomorphic to the base change of the tensor
> algebra, sending `ι (1 ⊗ₜ m)` to `1 ⊗ₜ ι m`.
> Taking `A = S⁻¹R` gives compatibility with localization.

```lean
theorem TensorAlgebra.exists_algEquiv_baseChange :
    ∃ e : TensorAlgebra A (A ⊗[R] M) ≃ₐ[A] A ⊗[R] TensorAlgebra R M,
      ∀ m : M, e (ι A (1 ⊗ₜ[R] m)) = 1 ⊗ₜ[R] ι R m
```

**`SymmetricAlgebra.exists_algEquiv_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorAlgebra/Localization.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorAlgebra/Localization.lean#L43). The attribute's comment: “(2)”.

> The symmetric algebra of a base change is isomorphic to the base change of the symmetric
> algebra, sending `ι (1 ⊗ₜ m)` to `1 ⊗ₜ ι m`.
> Taking `A = S⁻¹R` gives compatibility with localization.

```lean
theorem SymmetricAlgebra.exists_algEquiv_baseChange :
    ∃ e : SymmetricAlgebra A (A ⊗[R] M) ≃ₐ[A] A ⊗[R] SymmetricAlgebra R M,
      ∀ m : M, e (ι A (A ⊗[R] M) (1 ⊗ₜ[R] m)) = 1 ⊗ₜ[R] ι R M m
```

**`ExteriorAlgebra.exists_algEquiv_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/TensorAlgebra/Localization.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/TensorAlgebra/Localization.lean#L89). The attribute's comment: “(3)”.

> The exterior algebra of a base change is isomorphic to the base change of the exterior
> algebra, sending `ι (1 ⊗ₜ m)` to `1 ⊗ₜ ι m`.
> Taking `A = S⁻¹R` gives compatibility with localization.

```lean
theorem ExteriorAlgebra.exists_algEquiv_baseChange :
    ∃ e : ExteriorAlgebra A (A ⊗[R] M) ≃ₐ[A] A ⊗[R] ExteriorAlgebra R M,
      ∀ m : M, e (ι A (1 ⊗ₜ[R] m)) = 1 ⊗ₜ[R] ι R m
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.13, Tag 00DM](https://stacks.math.columbia.edu/tag/00DM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
