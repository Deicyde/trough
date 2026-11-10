---
declaration: section
origin: cited
lean: Stacks.Adeles.IsUnramifiedCuspForm, Stacks.Adeles.GlobalFunctionField.cuspFormsCentralChar_fg_and_baseChange, Stacks.Adeles.CuspFormsFinite, Stacks.Adeles.IsEigenform.isAlgebraic_heckeEigenvalue, Stacks.Adeles.GlobalFunctionField.isAlgebraic_eigenvalues_of_isEigenform, Stacks.TraceFormula.finite_geometricMonodromy_of_two_mul_lt, AlgebraicGeometry.finite_of_isUniversalFixedDeterminantDeformation, AlgebraicGeometry.flat_of_isUniversalFixedDeterminantDeformation
statement: formalized
proof: formalized
---

# 64.31 Automorphic forms and sheaves

Section 64.31 of the Stacks Project, [Tag 03VR](https://stacks.math.columbia.edu/tag/03VR). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03VS, a definition

[Tag 03VS](https://stacks.math.columbia.edu/tag/03VS) in the Stacks Project.

**`Stacks.Adeles.IsUnramifiedCuspForm`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/UnramifiedCuspForm.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/Adeles/UnramifiedCuspForm.lean#L139).

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

**`Stacks.Adeles.GlobalFunctionField.cuspFormsCentralChar_fg_and_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/CuspFormsStructure.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/CuspFormsStructure.lean#L56).

> **Stacks 03VW.** Let `k` be a finite field of characteristic `p` and `K` a function field
> over `k` (a finite extension of `k(x)`; this includes `K = k(X)` for every geometrically
> irreducible smooth projective curve `X` over `k`, whose places are the closed points of `X`). Let
> `Λ` be a ring in which `p` is invertible.
>
> 1. If `Λ` is Noetherian, then `C(Λ)` is a finitely generated `Λ`-module.
> 2. If `Λ` is a field with prime subfield `F` (the bottom subfield `⊥`), then
>    `C(Λ) = C(F) ⊗_F Λ` compatibly with `T_v` acting: there is a `Λ`-linear isomorphism
>    `e : Λ ⊗_F C(F) ≃ C(Λ)` given by `c ⊗ f ↦ c · (ι ∘ f)` (`ι : F → Λ` the inclusion), and for
>    every place `v` and every choice of the data `π, λ, g₀, g` of the formula for `T_v`
>    (`Stacks.Adeles.IsHeckeDataAt`), `T_v` restricts to linear endomorphisms `T_F` of `C(F)` and
>    `T_Λ` of `C(Λ)` with `e ∘ (id ⊗ T_F) = T_Λ ∘ e`.
>
> `C(Λ)` is `Stacks.Adeles.cuspFormsCentralChar`: the unramified cusp forms (Tag 03VS) with
> `U_v f = φ_v⁻¹ f` for all `v`, where the source's undefined `φ_v` is read as `q_v`, as in that
> definition's docstring. The characteristic `p` of `k` is `ringChar k`. The tensor product is
> written `Λ ⊗_F C(F)`, with `Λ` on the left so that it carries its `Λ`-module structure; it is
> `C(F) ⊗_F Λ` of the source up to the swap of factors.

```lean
public theorem cuspFormsCentralChar_fg_and_baseChange :
    (∀ (Λ : Type w) [CommRing Λ] [IsNoetherianRing Λ], IsUnit (ringChar k : Λ) →
      (cuspFormsCentralChar K Λ).FG) ∧
    ∀ (Λ : Type w) [Field Λ], IsUnit (ringChar k : Λ) →
      ∃ e : Λ ⊗[↥(⊥ : Subfield Λ)] cuspFormsCentralChar K ↥(⊥ : Subfield Λ) ≃ₗ[Λ]
          cuspFormsCentralChar K Λ,
        (∀ (c : Λ) (f : cuspFormsCentralChar K ↥(⊥ : Subfield Λ)),
          ((e (c ⊗ₜ f) : cuspFormsCentralChar K Λ) : GL (Fin 2) (AdeleRing K) → Λ) =
            c • mapCoeffs (algebraMap ↥(⊥ : Subfield Λ) Λ) f) ∧
        ∀ {v : Place K} {q : ℕ} (π : v.integers) (lam : Fin q → v.integers)
          (g₀ : GL (Fin 2) (AdeleRing K)) (g : Fin q → GL (Fin 2) (AdeleRing K)),
          IsHeckeDataAt v π lam g₀ g →
            ∃ (TF : cuspFormsCentralChar K ↥(⊥ : Subfield Λ) →ₗ[↥(⊥ : Subfield Λ)]
                cuspFormsCentralChar K ↥(⊥ : Subfield Λ))
              (TΛ : cuspFormsCentralChar K Λ →ₗ[Λ] cuspFormsCentralChar K Λ),
              (∀ f, (TF f : GL (Fin 2) (AdeleRing K) → ↥(⊥ : Subfield Λ)) =
                heckeOperator g₀ g f) ∧
              (∀ f, (TΛ f : GL (Fin 2) (AdeleRing K) → Λ) = heckeOperator g₀ g f) ∧
              e.toLinearMap ∘ₗ LinearMap.baseChange Λ TF = TΛ ∘ₗ e.toLinearMap
```

**`Stacks.Adeles.CuspFormsFinite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/SwitchingEll.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/Adeles/SwitchingEll.lean#L254). The attribute's comment: “clauses (1) and (2) both stated; (1) is stated for every Noetherian Λ, dropping the standing hypothesis that p is invertible in Λ, so it is stronger than the source's (1)”.

> **Stacks 03VW, carried as a hypothesis.** `C(Λ)` is a finitely generated `Λ`-module for `Λ`
> Noetherian, and `C(Λ) = C(F) ⊗_F Λ` compatibly with `T_v` for `Λ` a field with prime subfield
> `F`.
>
> The base change is recorded as the existence of a finite family in `C(F)` which is an `F`-basis
> of `C(F)` and whose image under `F → Λ` is a `Λ`-basis of `C(Λ)`; that is what
> `C(Λ) = C(F) ⊗_F Λ` says. Compatibility with `T_v` is automatic for this rendering, because the
> map `C(F) → C(Λ)` is postcomposition with `F → Λ` and `T_v` commutes with postcomposition by a
> ring homomorphism (`Stacks.Adeles.heckeOperator_mapCoeffs`). The prime subfield of `Λ` is the
> bottom subfield `⊥`.
>
> The subject of both clauses is `Stacks.Adeles.cuspFormsCentralChar`. The source defines `C(Λ)`
> by the condition `U_v f = φ_v⁻¹ f` without ever defining `φ_v`; that definition reads `φ_v` as
> `q_v`, the reading forced by the normalization `u_v = q_v⁻¹` for representations into `SL₂`,
> and clears the inverse. See its docstring in `StacksFrontier.NumberTheory.Adeles.HeckeEigenform`.
>
> Clause (1) is stated here for every Noetherian `Λ`. The source's section fixes `Λ` to be a ring
> in which `p` is invertible and defines `C(Λ)` only for such `Λ`, so for a Noetherian `Λ` in
> which some `q_v` is not invertible — `Λ = ℤ`, say — the cleared condition `q_v · U_v f = f` is
> not the source's `U_v f = φ_v⁻¹ f` and the proposition asserts nothing. The field `fg` is
> therefore stronger than the source's clause (1), and the attribute records this. Because the
> bundle is consumed whole, anything discharging it owes the stronger statement.
>
> The Stacks source proves this by citing de Jong, so it cannot be discharged here: this
> declaration is the formal statement of the proposition, which the results below take as a
> hypothesis. Its two fields are the proposition's two clauses. See the implementation notes of
> `StacksFrontier.NumberTheory.Adeles.SwitchingEll`.

```lean
public structure CuspFormsFinite (K : Type u) [Field K] : Prop
```

## Tag 03VX, a lemma

[Tag 03VX](https://stacks.math.columbia.edu/tag/03VX) in the Stacks Project.

**`Stacks.Adeles.IsEigenform.isAlgebraic_heckeEigenvalue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/AlgebraicEigenvalues.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/Adeles/AlgebraicEigenvalues.lean#L145). The attribute's comment: “conditional on cited 03VW, carried as a hypothesis; assumes T\_v has data at v, without which the eigenvalue equation is vacuous”.

> **Stacks Project, Tag 03VX.** Algebraicity of eigenvalues: if `Λ` is a field then the
> eigenvalues `t_v` of an eigenform `f ∈ C(Λ)` are algebraic over the prime subfield `F ⊂ Λ`,
> the subfield `⊥`, which is `𝔽_p` or `ℚ` according to the characteristic of `Λ`.
>
> Proposition 03VW is carried as the hypothesis `hVW`, and `hdata` is the data of the source's
> formula for `T_v` at `v`, without which the eigenvalue equation is vacuous; see the
> implementation notes of `StacksFrontier.NumberTheory.Adeles.AlgebraicEigenvalues`.

```lean
public theorem IsEigenform.isAlgebraic_heckeEigenvalue {K : Type u} [Field K] {Λ : Type w}
    [Field Λ] (hVW : CuspFormsFinite.{u, w} K) {f : GL (Fin 2) (AdeleRing K) → Λ}
    {t u : Place K → Λ} (hf : IsEigenform f t u) (hfC : f ∈ cuspFormsCentralChar K Λ)
    {v : Place K} {q : ℕ} {π : v.integers} {lam : Fin q → v.integers}
    {g₀ : GL (Fin 2) (AdeleRing K)} {g : Fin q → GL (Fin 2) (AdeleRing K)}
    (hdata : IsHeckeDataAt v π lam g₀ g) :
    IsAlgebraic ↥(⊥ : Subfield Λ) (t v)
```

**`Stacks.Adeles.GlobalFunctionField.isAlgebraic_eigenvalues_of_isEigenform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/AlgebraicEigenvalues.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/Adeles/GlobalFunctionField/AlgebraicEigenvalues.lean#L173).

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

**`Stacks.TraceFormula.finite_geometricMonodromy_of_two_mul_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/NumberTheory/TraceFormula/GeometricMonodromyFiniteness.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/NumberTheory/TraceFormula/GeometricMonodromyFiniteness.lean#L306). The attribute's comment: “Gaitsgory's range 2n < ℓ of the Conjecture; the F-sheaf formalism of §1.4 and the extended geometric Satake equivalence of §1.6 and Theorem 2.2 are hypotheses, as is his conclusion that the representation is then trivial on an open subgroup of the geometric fundamental group, and what is proved is that this makes the geometric monodromy group finite”.

> **Stacks Project, Tag 03W0.** *The Conjecture holds if `ℓ > 2n` modulo some unproven
> things.* For a smooth, projective, geometrically irreducible curve over a finite field of
> characteristic `p` and a prime `ℓ ≠ p` with `2n < ℓ`, every continuous representation of the
> étale fundamental group of rank `n` over `F_ℓ[[t]]` has finite geometric monodromy.
>
> The theorem is Gaitsgory's, it is not proved here, and the source states it as conditional.
> The unproven things it is conditional on are hypotheses: `formalism`, the constructible
> `F_ℓ((t))`-sheaf theory of §1.4, and `satake`, the extended geometric Satake equivalence of
> §1.6 and Theorem 2.2 for that formalism. Granted those two, Gaitsgory's conclusion is the
> hypothesis `hGaitsgory`, whose remaining antecedents are the hypotheses his theorem imposes —
> the curve is projective, `ℓ` differs from the characteristic, and `2n < ℓ` — and whose
> consequent is that the representation becomes trivial on an open subgroup of the geometric
> fundamental group. What is proved is that this yields the Conjecture's conclusion for the
> geometric monodromy group.

```lean
theorem finite_geometricMonodromy_of_two_mul_lt [Finite k] [IsAlgClosed K] [Smooth f]
    (p : ℕ) [CharP k p] [Fact ℓ.Prime]
    (x : GeometricPoint (geometricBaseChange k K f))
    [∀ Y, Finite ((finiteEtaleFiberFunctor x).obj Y)]
    (ρ : EtaleFundamentalGroup X (x.map (geometricProjection k K f)) →ₜ*
      Matrix.GeneralLinearGroup (Fin n) (PowerSeries (ZMod ℓ)))
    (hproj : IsProjective f) (hℓp : ℓ ≠ p) (hn : 2 * n < ℓ)
    (formalism : FSheafFormalism k ℓ)
    (satake : ExtendedGeometricSatake k ℓ formalism)
    (hGaitsgory : ∀ F : FSheafFormalism k ℓ, ExtendedGeometricSatake k ℓ F →
      IsProjective f → ℓ ≠ p → 2 * n < ℓ → IsTrivialOnOpenSubgroup k K f x ρ) :
    Finite (geometricMonodromy k K f x ρ)
```

## Tag 03W1, a theorem

[Tag 03W1](https://stacks.math.columbia.edu/tag/03W1) in the Stacks Project.

**`AlgebraicGeometry.finite_of_isUniversalFixedDeterminantDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjecture.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjecture.lean#L123). The attribute's comment: “fixed-determinant finiteness; the step of the cited argument in which the conjecture is used, that the special fibre R/lR of the universal deformation ring is finite, is carried as the hypothesis hspecialFibre”.

> **Stacks Project, Tag 03W1 (finiteness).** Let `X` be a smooth, geometrically irreducible,
> projective curve over a finite field `k` of characteristic `p`, let `ℓ ≠ p` be a prime, and let
> `ρ₀ : π₁(X) → GLₙ(ZMod ℓ)` be a continuous representation of its étale fundamental group. Assume
> that de Jong's conjecture holds for `X`, that the restriction of `ρ₀` to the geometric
> fundamental group is absolutely irreducible, and that `ℓ` does not divide `n`. Then the universal
> deformation ring of `ρ₀` with determinant fixed to a continuous character `δ` lifting `det ρ₀` is
> finite over `ℤ_[ℓ]`.
>
> The step of de Jong's cited argument in which the conjecture is used, namely that the special
> fibre `R/ℓR` of the deformation ring is finite, is carried as the hypothesis
> `hspecialFibre`.

```lean
public theorem finite_of_isUniversalFixedDeterminantDeformation
    (k K : Type u) [Field k] [Finite k] [Field K] [Algebra k K] [IsAlgClosed K]
    (p ℓ n : ℕ) [CharP k p] [Fact ℓ.Prime] (_hℓp : ℓ ≠ p) (_hn : ¬ ℓ ∣ n)
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IsCurve k f] [Smooth f] [IsProper f] [GeometricallyIrreducible f] [ConnectedSpace X]
    (X' : Scheme.{u}) (q : X' ⟶ X) (fK : X' ⟶ Spec (.of K))
    (hbc : IsPullback q fK f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
    [ConnectedSpace X'] (x : GeometricPoint X')
    (ρ₀ : EtaleFundamentalGroup X (x.map q) →ₜ* Matrix.GeneralLinearGroup (Fin n) (ZMod ℓ))
    (δ : EtaleFundamentalGroup X (x.map q) →ₜ* ℤ_[ℓ]ˣ)
    (_hconj : DeJongConjectureHolds.{u, w} k K ℓ n X f X' q fK hbc x)
    (_hirred : Deformation.IsAbsolutelyIrreducible
      fun g : EtaleFundamentalGroup X' x => ρ₀ (etaleFundamentalGroupMap q x g))
    (R : Type v) [CommRing R] [IsLocalRing R] [TopologicalSpace R] [Algebra ℤ_[ℓ] R]
    (reduce : R →+* ZMod ℓ)
    (ρuniv : EtaleFundamentalGroup X (x.map q) →ₜ* Matrix.GeneralLinearGroup (Fin n) R)
    (hR : Deformation.IsUniversalFixedDeterminantDeformation ℓ n _ ρ₀ δ R reduce ρuniv)
    (hspecialFibre :
      Finite (R ⧸ (IsLocalRing.maximalIdeal ℤ_[ℓ] • (⊤ : Submodule ℤ_[ℓ] R)))) :
    Module.Finite ℤ_[ℓ] R
```

**`AlgebraicGeometry.flat_of_isUniversalFixedDeterminantDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjecture.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjecture.lean#L153). The attribute's comment: “fixed-determinant flatness; the step of the cited argument in which the conjecture is used, that l is a nonzerodivisor on the universal deformation ring, is carried as the hypothesis hregular”.

> **Stacks Project, Tag 03W1 (flatness).** Under the same hypotheses, the universal
> fixed-determinant deformation ring of `ρ₀` is flat over `ℤ_[ℓ]`.
>
> The step of de Jong's cited argument in which the conjecture is used, namely that `ℓ` is a
> nonzerodivisor on the deformation ring, is carried as the hypothesis `hregular`.

```lean
public theorem flat_of_isUniversalFixedDeterminantDeformation
    (k K : Type u) [Field k] [Finite k] [Field K] [Algebra k K] [IsAlgClosed K]
    (p ℓ n : ℕ) [CharP k p] [Fact ℓ.Prime] (_hℓp : ℓ ≠ p) (_hn : ¬ ℓ ∣ n)
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
    [IsCurve k f] [Smooth f] [IsProper f] [GeometricallyIrreducible f] [ConnectedSpace X]
    (X' : Scheme.{u}) (q : X' ⟶ X) (fK : X' ⟶ Spec (.of K))
    (hbc : IsPullback q fK f (Spec.map (CommRingCat.ofHom (algebraMap k K))))
    [ConnectedSpace X'] (x : GeometricPoint X')
    (ρ₀ : EtaleFundamentalGroup X (x.map q) →ₜ* Matrix.GeneralLinearGroup (Fin n) (ZMod ℓ))
    (δ : EtaleFundamentalGroup X (x.map q) →ₜ* ℤ_[ℓ]ˣ)
    (_hconj : DeJongConjectureHolds.{u, w} k K ℓ n X f X' q fK hbc x)
    (_hirred : Deformation.IsAbsolutelyIrreducible
      fun g : EtaleFundamentalGroup X' x => ρ₀ (etaleFundamentalGroupMap q x g))
    (R : Type v) [CommRing R] [IsLocalRing R] [TopologicalSpace R] [Algebra ℤ_[ℓ] R]
    (reduce : R →+* ZMod ℓ)
    (ρuniv : EtaleFundamentalGroup X (x.map q) →ₜ* Matrix.GeneralLinearGroup (Fin n) R)
    (hR : Deformation.IsUniversalFixedDeterminantDeformation ℓ n _ ρ₀ δ R reduce ρuniv)
    (hregular : algebraMap ℤ_[ℓ] R (ℓ : ℤ_[ℓ]) ∈ nonZeroDivisors R) :
    Module.Flat ℤ_[ℓ] R
```

**`AlgebraicGeometry.finite_flat_of_isUniversalFixedDeterminantDeformation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjectureFiniteFlat.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/DeJongConjectureFiniteFlat.lean#L70).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
