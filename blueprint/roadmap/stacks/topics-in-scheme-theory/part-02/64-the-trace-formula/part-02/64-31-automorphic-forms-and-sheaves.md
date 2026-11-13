---
declaration: section
origin: cited
lean: Stacks.Adeles.IsUnramifiedCuspForm, Stacks.Adeles.GlobalFunctionField.cuspFormsWithChar_fg_and_baseChange, Stacks.Adeles.GlobalFunctionField.isAlgebraic_eigenvalues_of_isEigenform, Stacks.TraceFormula.geometricMonodromyConjecture_of_gaitsgoryInput, AlgebraicGeometry.finite_flat_of_isUniversalFixedDeterminantDeformation
statement: formalized
proof: formalized
---

# 64.31 Automorphic forms and sheaves

Section 64.31 of the Stacks Project, [Tag 03VR](https://stacks.math.columbia.edu/tag/03VR). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03VS, a definition

[Tag 03VS](https://stacks.math.columbia.edu/tag/03VS) in the Stacks Project.

**`Stacks.Adeles.IsUnramifiedCuspForm`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/UnramifiedCuspForm.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/Adeles/UnramifiedCuspForm.lean#L139).

> An unramified cusp form on `GL₂(A)` with values in `Λ`: a function on `GL₂(A)` invariant
> under right multiplication by `GL₂(K)` and under left multiplication by `GL₂(O)`, whose
> constant term along the unipotent `(1, z; 0, 1)` over `A` modulo `K` vanishes.
>
> See [Stacks Project, Tag 03VS](https://stacks.math.columbia.edu/tag/03VS).

```lean
public structure IsUnramifiedCuspForm {Λ : Type w} [AddCommMonoid Λ]
    (f : GL (Fin 2) (AdeleRing K) → Λ) : Prop
```

## Tag 03VW, a proposition

[Tag 03VW](https://stacks.math.columbia.edu/tag/03VW) in the Stacks Project.

**`Stacks.Adeles.GlobalFunctionField.cuspFormsWithChar_fg_and_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/CuspFormsStructure.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/CuspFormsStructure.lean#L121). The attribute's comment: “C(Λ) is defined for an arbitrary system of units φ\_v (the source leaves φ\_v unspecified), in units of the prime field for the second clause; the first clause is proved without the standing hypothesis that p is invertible in Λ”.

> **Stacks 03VW.** Let `k` be a finite field of characteristic `p` and `K` a function field
> over `k` (a finite extension of `k(x)`; this includes `K = k(X)` for every geometrically
> irreducible smooth projective curve `X` over `k`, whose places are the closed points of `X`). For a
> ring `Λ` and a system `φ = (φ_v)` of units of `Λ` indexed by the places, `C(Λ)` is
> `Stacks.Adeles.cuspFormsWithChar K Λ φ`: the unramified cusp forms (Tag 03VS) with
> `U_v f = φ_v⁻¹ f` for all `v` (`Stacks.Adeles.isCuspFormWithChar_iff`). The source leaves `φ_v`
> unspecified; the statement holds for every such system.
>
> 1. If `Λ` is Noetherian, then `C(Λ)` is a finitely generated `Λ`-module, for every system `φ` of
>    units of `Λ`.
> 2. If `Λ` is a field in which `p` is invertible, with prime subfield `F` (the bottom subfield
>    `⊥`), and `φ` is a system of units of `F` (so that both `C(F)` and `C(Λ)` are defined by the
>    same `φ_v`, viewed in `Λ` through `ι : F → Λ`), then `C(Λ) = C(F) ⊗_F Λ` compatibly with
>    `T_v` acting: there is a `Λ`-linear isomorphism `e : Λ ⊗_F C(F) ≃ C(Λ)` given by
>    `c ⊗ f ↦ c · (ι ∘ f)`, and for every place `v` and every choice of the data `π, λ, g₀, g` of
>    the formula for `T_v` (`Stacks.Adeles.IsHeckeDataAt`), `T_v` restricts to linear
>    endomorphisms `T_F` of `C(F)` and `T_Λ` of `C(Λ)` with `e ∘ (id ⊗ T_F) = T_Λ ∘ e`.
>
> Clause (1) does not need `p` to be invertible in `Λ`, the standing hypothesis of the source's
> section: its proof needs nothing beyond the `φ_v` being units. The characteristic `p` of `k` is
> `ringChar k`. The tensor product is written `Λ ⊗_F C(F)`, with `Λ` on the left so that it carries
> its `Λ`-module structure; it is `C(F) ⊗_F Λ` of the source up to the swap of factors. The
> central character `φ_v = q_v` of Lemma 03VY is the instance
> `cuspFormsCentralChar_fg_and_baseChange`.

```lean
public theorem cuspFormsWithChar_fg_and_baseChange :
    (∀ (Λ : Type w) [CommRing Λ] [IsNoetherianRing Λ] (φ : Place K → Λ), (∀ v, IsUnit (φ v)) →
      (cuspFormsWithChar K Λ φ).FG) ∧
    ∀ (Λ : Type w) [Field Λ], IsUnit (ringChar k : Λ) →
      ∀ φ : Place K → ↥(⊥ : Subfield Λ), (∀ v, IsUnit (φ v)) →
      ∃ e : Λ ⊗[↥(⊥ : Subfield Λ)] cuspFormsWithChar K ↥(⊥ : Subfield Λ) φ ≃ₗ[Λ]
          cuspFormsWithChar K Λ (fun v => algebraMap ↥(⊥ : Subfield Λ) Λ (φ v)),
        (∀ (c : Λ) (f : cuspFormsWithChar K ↥(⊥ : Subfield Λ) φ),
          ((e (c ⊗ₜ f) : cuspFormsWithChar K Λ (fun v => algebraMap ↥(⊥ : Subfield Λ) Λ (φ v))) :
              GL (Fin 2) (AdeleRing K) → Λ) =
            c • mapCoeffs (algebraMap ↥(⊥ : Subfield Λ) Λ) f) ∧
        ∀ {v : Place K} {q : ℕ} (π : v.integers) (lam : Fin q → v.integers)
          (g₀ : GL (Fin 2) (AdeleRing K)) (g : Fin q → GL (Fin 2) (AdeleRing K)),
          IsHeckeDataAt v π lam g₀ g →
            ∃ (TF : cuspFormsWithChar K ↥(⊥ : Subfield Λ) φ →ₗ[↥(⊥ : Subfield Λ)]
                cuspFormsWithChar K ↥(⊥ : Subfield Λ) φ)
              (TΛ : cuspFormsWithChar K Λ (fun v => algebraMap ↥(⊥ : Subfield Λ) Λ (φ v)) →ₗ[Λ]
                cuspFormsWithChar K Λ (fun v => algebraMap ↥(⊥ : Subfield Λ) Λ (φ v))),
              (∀ f, (TF f : GL (Fin 2) (AdeleRing K) → ↥(⊥ : Subfield Λ)) =
                heckeOperator g₀ g f) ∧
              (∀ f, (TΛ f : GL (Fin 2) (AdeleRing K) → Λ) = heckeOperator g₀ g f) ∧
              e.toLinearMap ∘ₗ LinearMap.baseChange Λ TF = TΛ ∘ₗ e.toLinearMap
```

## Tag 03VX, a lemma

[Tag 03VX](https://stacks.math.columbia.edu/tag/03VX) in the Stacks Project.

**`Stacks.Adeles.GlobalFunctionField.isAlgebraic_eigenvalues_of_isEigenform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/AlgebraicEigenvalues.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/AlgebraicEigenvalues.lean#L169). The attribute's comment: “the eigenvalues of an eigenform in the space of cusp forms with central character, over a field in which p is invertible, are algebraic over the prime field”.

> **Stacks Project, Tag 03VX.** Algebraicity of eigenvalues. Let `k` be a finite field of
> characteristic `p`, `K` a function field over `k` (for instance `K = k(X)` for a geometrically
> irreducible smooth projective curve `X` over `k`), and `Λ` a field in which `p` is invertible,
> with prime subfield `F ⊂ Λ` (the bottom subfield `⊥`). If `f ∈ C(Λ)` is an eigenform, with
> `T_v f = t_v f` and `U_v f = u_v f` at every place `v`, then the eigenvalues `t_v` are algebraic
> over `F`; so are the `u_v`, which equal `q_v⁻¹ ∈ F`.
>
> `C(Λ)` is `Stacks.Adeles.cuspFormsCentralChar` and an eigenform is `Stacks.Adeles.IsEigenform`
> (an unramified cusp form with a unit value, Tag 03VS). The proof uses Proposition 03VW,
> `Stacks.Adeles.GlobalFunctionField.cuspFormsCentralChar_fg_and_baseChange`.

```lean
public theorem isAlgebraic_eigenvalues_of_isEigenform (hp : IsUnit (ringChar k : Λ))
    {f : GL (Fin 2) (AdeleRing K) → Λ} {t u : Place K → Λ} (hf : IsEigenform f t u)
    (hfC : f ∈ cuspFormsCentralChar K Λ) (v : Place K) :
    IsAlgebraic ↥(⊥ : Subfield Λ) (t v) ∧ IsAlgebraic ↥(⊥ : Subfield Λ) (u v)
```

## Tag 03W0, a theorem

[Tag 03W0](https://stacks.math.columbia.edu/tag/03W0) in the Stacks Project.

**`Stacks.TraceFormula.geometricMonodromyConjecture_of_gaitsgoryInput`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/GaitsgoryAutomorphic.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/NumberTheory/TraceFormula/GaitsgoryAutomorphic.lean#L285). The attribute's comment: “Gaitsgory's theorem: for l > 2n, the input the source leaves unproven (GaitsgoryInput: every rho has an attached automorphic form, cuspidal Hecke eigenforms on GL\_\{n\_j} whose Hecke polynomials multiply to the characteristic polynomials of Frobenius) implies the Conjecture (GeometricMonodromyConjecture)”.

> **Stacks Project, Tag 03W0 (Gaitsgory).** *The Conjecture holds if `ℓ > 2n`, modulo some
> unproven things.* Let `k` be a finite field of characteristic `p`, `X` a smooth, geometrically
> irreducible, projective curve over `k`, `k̄` an algebraic closure of `k`, and `ℓ ≠ p` a prime with
> `2n < ℓ`. Then the unproven input of Gaitsgory's construction (`GaitsgoryInput`: every continuous
> `ρ : π₁(X) → GL_n(F_ℓ[[t]])` has an attached automorphic form) implies the Conjecture for `X`, `n`
> and `ℓ` (`GeometricMonodromyConjecture`: every such `ρ` has finite geometric monodromy
> `ρ(π₁(X_k̄))`).

```lean
public theorem geometricMonodromyConjecture_of_gaitsgoryInput [Finite k] [IsAlgClosure k K]
    [Smooth f] (p : ℕ) [CharP k p] [Fact ℓ.Prime]
    (x : GeometricPoint (geometricBaseChange k K f)) (hproj : IsProjective f) (hℓp : ℓ ≠ p)
    (hn : 2 * n < ℓ) :
    GaitsgoryInput k K f n ℓ x → GeometricMonodromyConjecture k K f n ℓ x
```

## Tag 03W1, a theorem

[Tag 03W1](https://stacks.math.columbia.edu/tag/03W1) in the Stacks Project.

**`AlgebraicGeometry.finite_flat_of_isUniversalFixedDeterminantDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjectureFiniteFlat.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjectureFiniteFlat.lean#L71). The attribute's comment: “the theorem in full, with the determinant fixed to delta: the universal deformation ring is finite and flat over Z\_l”.

> **Stacks Project, Tag 03W1.** Let `X` be a smooth, geometrically irreducible, proper curve
> over a finite field `k` of characteristic `p`, `k̄` an algebraic closure of `k`, `x` a geometric
> point of `X_k̄`, `ℓ ≠ p` a prime and `ρ₀ : π₁(X) → GLₙ(𝐅_ℓ)` continuous. Assume de Jong's
> conjecture for `X` (in every rank `m`, every continuous `ρ : π₁(X) → GL_m(𝐅_ℓ[[t]])` has finite
> image on `π₁(X_k̄)`), that `ρ₀|_{π₁(X_k̄)}` is absolutely irreducible and that `ℓ ∤ n`. Then for
> every continuous character `δ : π₁(X) → ℤ_ℓ^*`, the universal deformation ring `R` of `ρ₀` with
> determinant fixed to `δ` (`δ` lifts `det ρ₀`, a field of the universal property) is finite and
> flat over `ℤ_ℓ`.

```lean
theorem finite_flat_of_isUniversalFixedDeterminantDeformation
    (k kbar : Type u) [Field k] [Finite k] [Field kbar] [Algebra k kbar] [IsAlgClosure k kbar]
    (p ℓ n : ℕ) [CharP k p] [Fact ℓ.Prime] (hℓp : ℓ ≠ p) (hn : ¬ ℓ ∣ n)
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IsCurve k f] [Smooth f] [IsProper f] [GeometricallyIrreducible f] :
    letI : ConnectedSpace X :=
      haveI : IsIntegral X := (inferInstance : IsCurve k f).toIsIntegral
      inferInstance
    letI : ConnectedSpace ↥(pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) :=
      @IrreducibleSpace.connectedSpace _ _
        ((inferInstance : GeometricallyIrreducible f).geometrically_irreducibleSpace
          (Spec.map (CommRingCat.ofHom (algebraMap k kbar))) (pullback.fst _ _) (pullback.snd _ _)
          (IsPullback.of_hasPullback _ _))
    ∀ (x : GeometricPoint (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))))
      (ρ₀ : EtaleFundamentalGroup X (x.map (pullback.fst f
        (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))) →ₜ*
          Matrix.GeneralLinearGroup (Fin n) (ZMod ℓ))
      (δ : EtaleFundamentalGroup X (x.map (pullback.fst f
        (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))) →ₜ* ℤ_[ℓ]ˣ),
      (∀ (m : ℕ) (ρ : EtaleFundamentalGroup X (x.map (pullback.fst f
          (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))) →ₜ*
          Matrix.GeneralLinearGroup (Fin m) (PowerSeries (ZMod ℓ))),
        (Set.range fun g : EtaleFundamentalGroup _ x => ρ (etaleFundamentalGroupMap
          (pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) x g)).Finite) →
      (Deformation.IsAbsolutelyIrreducible fun g : EtaleFundamentalGroup _ x =>
        ρ₀ (etaleFundamentalGroupMap (pullback.fst f
          (Spec.map (CommRingCat.ofHom (algebraMap k kbar)))) x g)) →
      ∀ (R : Type v) [CommRing R] [IsLocalRing R] [TopologicalSpace R] [Algebra ℤ_[ℓ] R]
        (reduce : R →+* ZMod ℓ)
        (ρuniv : EtaleFundamentalGroup X (x.map (pullback.fst f
          (Spec.map (CommRingCat.ofHom (algebraMap k kbar))))) →ₜ*
            Matrix.GeneralLinearGroup (Fin n) R),
        Deformation.IsUniversalFixedDeterminantDeformation ℓ n _ ρ₀ δ R reduce ρuniv →
        Module.Finite ℤ_[ℓ] R ∧ Module.Flat ℤ_[ℓ] R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.31, Tag 03VR](https://stacks.math.columbia.edu/tag/03VR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
