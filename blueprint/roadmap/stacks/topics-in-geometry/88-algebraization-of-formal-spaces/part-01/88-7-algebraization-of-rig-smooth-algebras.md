---
declaration: section
origin: cited
lean: Rig.jacobianDet_smul_naiveCotangentComplex_eq_zero, Rig.jacobianDet_smul_ext_one_naiveCotangentComplex_eq_zero, Rig.exists_finiteType_adicCompletion_algEquiv_of_jacobianChart, Rig.exists_finiteType_algEquiv_adicCompletion_of_jacobianChart, Rig.isRigSmooth_algebraization
statement: formalized
proof: formalized
---

# 88.7 Algebraization of rig-smooth algebras

Section 88.7 of the Stacks Project, [Tag 0GAU](https://stacks.math.columbia.edu/tag/0GAU). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GAV, a lemma

[Tag 0GAV](https://stacks.math.columbia.edu/tag/0GAV) in the Stacks Project.

**`Rig.jacobianDet_smul_naiveCotangentComplex_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Algebraization.lean#L183). The attribute's comment: “square_null_action”.

> For a square presentation `B = A[x₁, …, xₙ]/(f₁, …, fₙ)`, the image of the
> Jacobian determinant annihilates `NL_{B/A}` in the derived category of `B`-modules.

```lean
public theorem jacobianDet_smul_naiveCotangentComplex_eq_zero
    (A : Type u) [CommRing A] (n : ℕ)
    (f : Fin n → MvPolynomial (Fin n) A) :
    (Ideal.Quotient.mk (Ideal.span (Set.range f))
      (Matrix.det (fun i j : Fin n ↦ MvPolynomial.pderiv i (f j)))) •
        𝟙 (Deformation.Artin.derivedNaiveCotangentComplex A
          (MvPolynomial (Fin n) A ⧸ Ideal.span (Set.range f))) = 0
```

**`Rig.jacobianDet_smul_ext_one_naiveCotangentComplex_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Algebraization.lean#L525). The attribute's comment: “ext_annihilation”.

> Let `B = A[x₁, …, xₙ]/(f₁, …, fₘ)`, where `m ≤ n`.  The image in `B` of the
> Jacobian determinant formed with the first `m` variables annihilates
> `Ext¹_B(NL_{B/A}, N)` for every `B`-module `N`.

```lean
public theorem jacobianDet_smul_ext_one_naiveCotangentComplex_eq_zero
    (A : Type u) [CommRing A] (m n : ℕ) (f : Fin m → MvPolynomial (Fin n) A)
    (h : m ≤ n)
    (N : ModuleCat.{max u v}
      (MvPolynomial (Fin n) A ⧸ Ideal.span (Set.range f)))
    (x : DerivedCategory.Ext
      (derivedNaiveCotangentComplex A
        (MvPolynomial (Fin n) A ⧸ Ideal.span (Set.range f)))
      ((DerivedCategory.singleFunctor
        (ModuleCat.{max u v} (MvPolynomial (Fin n) A ⧸ Ideal.span (Set.range f))) 0).obj N) 1) :
    Ideal.Quotient.mk (Ideal.span (Set.range f))
        (Matrix.det (fun i j : Fin m => MvPolynomial.pderiv (Fin.castLE h i) (f j))) • x = 0
```

## Tag 0GAW, a lemma

[Tag 0GAW](https://stacks.math.columbia.edu/tag/0GAW) in the Stacks Project.

**`Rig.exists_finiteType_adicCompletion_algEquiv_of_jacobianChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/JacobianChartAlgebraization.lean, line 972](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Algebraization/JacobianChartAlgebraization.lean#L972).

> **Stacks Project, Tag 0GAW: the Jacobian criterion for algebraization.**
>
> Let `A` be a Noetherian ring, `I ⊆ A` an ideal and `B` an `I`-adically complete `A`-algebra
> with `B/IB` of finite type over `A/I` (an object of Stacks 0AL4), presented as
> `B = A⟨x₁, …, x_r⟩/J`.  Assume there are `b ∈ B`, `0 ≤ m ≤ r` and `f₁, …, f_m ∈ J` such that
>
> 1. `V(b) ⊆ V(IB)` in `Spec(B)`,
> 2. the image of `Δ = det(∂fⱼ/∂xᵢ)_{1 ≤ i, j ≤ m}` in `B` divides `b`, and
> 3. `bJ ⊆ (f₁, …, f_m) + J²`.
>
> Then there exist a finite type `A`-algebra `C` and an `A`-algebra isomorphism `B ≅ C^∧`.
>
> Here `b` is given by a lift to `A⟨x⟩`; condition (1) is `IB ⊆ √(b)`.
>
> **The proof.**  As in the source, `C` is the algebra
> `A[z₁, …, z_t, x₁, …, x_r]/(z₁Δ' - a₁^{c₁}, …, z_tΔ' - a_t^{c₁}, f'₁, …, f'_m)` of Stacks 0GAV
> built from polynomial approximations `f'ⱼ` of the `fⱼ` and generators `a₁, …, a_t` of `I`, and
> it maps onto `B/IⁿB`.  The lift of that map to `φ : C^∧ → B` is produced by Newton's method
> (`exists_algHom_newton`): in this algebra the Jacobian determinant of the relations with
> respect to `z₁, …, z_t, x₁, …, x_m` is `Δ'^{t+1}`, and the relations themselves force a fixed
> power of `I` into `Δ'B`, so the linearized equations can be solved exactly at each step and
> the source's uniform lifting result Stacks 0GAQ is not needed.  `φ` is surjective because it is
> surjective modulo `I`, a power of `I` kills `Ker(φ)/Ker(φ)²`
> (`exists_pow_smul_cotangent_eq_bot_of_jacobianChart`, the source's application of Stacks 0ALM
> and of the comparison of free modules of rank `r - m`), and Stacks 0ALR concludes.

```lean
public theorem exists_finiteType_adicCompletion_algEquiv_of_jacobianChart
    (B : AdicFiniteTypeAlgebra.{u, v} A I) (P : CompletedPolynomialPresentation I B)
    (m : ℕ) (hm : m ≤ P.variableCount) (b : P.completedPolynomialRing)
    (f : Fin m → P.ker)
    (hvanish : B.adicIdeal ≤ (Ideal.span {P.toAlgHom b}).radical)
    (hjacobian :
      P.toAlgHom (Matrix.det fun i j : Fin m ↦
        (completedNaiveCotangentComplex B P).partialDeriv (Fin.castLE hm i)
          (f j : P.completedPolynomialRing)) ∣ P.toAlgHom b)
    (hrelations : ∀ x : P.completedPolynomialRing, x ∈ P.ker →
      b * x ∈ Ideal.span (Set.range fun j : Fin m ↦ (f j : P.completedPolynomialRing)) +
        P.ker ^ 2) :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
      Algebra.FiniteType A C ∧
        Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)
```

**`Rig.exists_finiteType_algEquiv_adicCompletion_of_jacobianChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/JacobianCriterion.lean, line 535](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Algebraization/JacobianCriterion.lean#L535). The attribute's comment: “carrying, beyond the source's hypotheses: `S`, a family of Stacks 0GA6 DualSituations for B, one per thickness and per Ext-exponent, as the library's Stacks 0GAQ carries one per thickness; `d`, `q₀`, `k`, `hd`, `hq₀`, `hk`, the Stacks 0GA6 invariants of B, independent of thickness and exponent, with k+1 = D = max(d,1); `hdual`, the open duality input of Stacks 0GAC that Stacks 0GAQ carries, here for every level and exponent because n is chosen in the proof; and `hconormal`, that a power of I kills Ker(φ)/Ker(φ)² for every surjection φ from the completion of a finite type A-algebra onto B with both sides rig-smooth (both rig-smoothness inputs are discharged here), which is the source's last step by the Stacks 0ALM six-term sequence and the localized comparison H⁰(NL^∧_{C^∧/A}) ⊗ B[1/b] = H⁰(NL^∧_{B/A}) ⊗ B[1/b], absent from the library. Inherited, not assumed: the Stacks 0GAQ used lifts to precision I^{n-(2+D)c} under n > 2(2+D)c for the source's I^{n-(1+d)c}; and B is taken in A's own universe, the only case that Stacks 0GAQ's target admits”.

> **Stacks 0GAW, carrying the hypotheses that the library's Stacks 0GAQ carries.**
>
> Let `A` be a Noetherian ring, `I ⊆ A` an ideal, `B` an `I`-adically complete `A`-algebra of
> finite type modulo `I`, presented as `B = A⟨x₁, …, x_r⟩/J`, and suppose given `b`, an integer
> `m ≤ r` and `f₁, …, f_m ∈ J` with `V(b) ⊆ V(IB)`, with the Jacobian determinant
> `Δ = det(∂fⱼ/∂xᵢ)_{i, j ≤ m}` dividing the image of `b`, and with `bJ ⊆ (f₁, …, f_m) + J²`.
> Then `B` is the `I`-adic completion of a finite type `A`-algebra.
>
> **The route.** The hypotheses make `B` rig-smooth over `(A, I)`, so a power `I^{c}` annihilates
> `Ext¹_B(NL^∧_{B/A}, N)`, and `V(b) ⊆ V(IB)` gives `c₁` with `I^{c₁}B ⊆ bB`.  Writing
> `I = (a₁, …, a_t)` and approximating the `fⱼ` by polynomials `f'ⱼ` to accuracy `n`, the algebra
>
> `C = A[z₁, …, z_t, x₁, …, x_r]/(z₁Δ' - a₁^{c₁}, …, z_tΔ' - a_t^{c₁}, f'₁, …, f'_m)`
>
> of Stacks 0GAV has `I^{1 + t((t+1)c₁ - 1)}` annihilating `Ext¹` of its completed naive cotangent
> complex — an exponent independent of `n`, which is what lets `n` be chosen in terms of it — and
> maps onto `B/IⁿB` by `x_i ↦ x_i`, `z_k ↦ b_k b'`.  Stacks 0GAQ lifts that surjection to
> `φ : C^∧ → B`, which is surjective because it is surjective modulo `I`, and Stacks 0ALR
> algebraizes `B` from `φ`.
>
> **The carried hypotheses, one line each.**
>
> * `S` — a family of Stacks 0GA6 `DualSituation`s for `B`, one for each thickness and each
>   Ext-exponent, exactly as the library's Stacks 0GAQ carries one for each thickness.
> * `d`, `q₀`, `k`, `hd`, `hq₀`, `hk` — the invariants of Stacks 0GA6 of `B`, independent of the
>   thickness and of the exponent, with `k + 1 = D = max(d, 1)`.
> * `hdual` — the open duality input of Stacks 0GAC, which Stacks 0GAQ carries for every level
>   `m ≥ n`, here carried for every level and every exponent since `n` is chosen inside the proof.
> * `hconormal` — that for every finite type `A`-algebra `C` and every surjection
>   `φ : C^∧ → B` of `A`-algebras with both `B` and `C^∧` rig-smooth over `(A, I)` a power of `I`
>   annihilates `Ker(φ)/Ker(φ)²`; this is the step the source makes with the six-term sequence of
>   Stacks 0ALM and the comparison `H⁰(NL^∧_{C^∧/A}) ⊗ B[1/b] = H⁰(NL^∧_{B/A}) ⊗ B[1/b]` of free
>   modules of rank `r - m`, which the library does not have.  Both rig-smoothness inputs are
>   discharged here: `B`'s from the Jacobian chart of the statement, `C^∧`'s from the smoothness
>   of `C` away from `V(I)`.
>
> Two further deviations, both inherited rather than assumed: the Stacks 0GAQ used here lifts only
> to precision `I^{n-(2+D)c}` under `n > 2(2+D)c`, in place of the source's `I^{n-(1+d)c}` under
> `n > 2(1+d)c`; and `B` is taken in the universe of `A`, which is the only case Stacks 0GAQ's
> target admits.

```lean
public theorem exists_finiteType_algEquiv_adicCompletion_of_jacobianChart
    (B : AdicFiniteTypeAlgebra.{u, u} A I) (P : CompletedPolynomialPresentation I B)
    (m : ℕ) (hm : m ≤ P.variableCount) (b : P.completedPolynomialRing)
    (f : Fin m → P.ker)
    (hvanish : B.adicIdeal ≤ (Ideal.span {P.toAlgHom b}).radical)
    (hjacobian :
      P.toAlgHom (Matrix.det fun i j : Fin m ↦
        (completedNaiveCotangentComplex B P).partialDeriv (Fin.castLE hm i)
          (f j : P.completedPolynomialRing)) ∣ P.toAlgHom b)
    (hrelations : ∀ x : P.completedPolynomialRing, x ∈ P.ker →
      b * x ∈ Ideal.span (Set.range fun j : Fin m ↦ (f j : P.completedPolynomialRing)) +
        P.ker ^ 2)
    (S : ∀ c l : ℕ, DualSituation B.carrier (I.map (algebraMap A B.carrier)) l c)
    (d q₀ k : ℕ) (hd : ∀ c l, (S c l).d = d) (hq₀ : ∀ c l, (S c l).q₀ = q₀)
    (hk : max d 1 = k + 1)
    (hdual : ∀ (c l e : ℕ) (hel : e + 2 * c = l) (hq : (S c l).q₀ ≤ e)
      (M : ANCModule (I.map (algebraMap A B.carrier)) l c)
      (ϕ : resModule (I.map (algebraMap A B.carrier)) l M.1 →ₗ[B.carrier]
        powQuot (I.map (algebraMap A B.carrier)) l l),
      ∃ s : (S c l).H M.dual 0 (e : ℤ),
        (S c l).ev M e hq s =
          (powQuotLe (I.map (algebraMap A B.carrier)) (Nat.le.intro hel)).comp ϕ)
    (hconormal : ∀ (C : Type u) [CommRing C] [Algebra A C] [Algebra.FiniteType A C]
      (ϕ : AdicCompletion (I.map (algebraMap A C)) C →ₐ[A] B.carrier),
      Function.Surjective ϕ → IsRigSmooth B → IsRigSmooth (adicCompletionObj I (B := C)) →
        ∃ c : ℕ, I ^ c • (⊤ : Submodule A (RingHom.ker ϕ.toRingHom).Cotangent) = ⊥) :
    ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C),
      Algebra.FiniteType A C ∧
        Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)
```

## Tag 0GAX, a remark

[Tag 0GAX](https://stacks.math.columbia.edu/tag/0GAX) in the Stacks Project.

**`Rig.isRigSmooth_algebraization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/Algebraization/RigSmoothAlgebraizationGZ.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/Algebraization/RigSmoothAlgebraizationGZ.lean#L109).

> **Stacks 0GAX.** Let `I` be an ideal of a Noetherian ring `A` and let `B` be an object of the
> category of Stacks 0AL4 which is rig-smooth over `(A, I)`. Then `B` is isomorphic to the `I`-adic
> completion of a finite type `A`-algebra (Gabber–Zavyalov [Theorem 1.2]). This supersedes the
> partial results:
>
> 1. if `A` is a G-ring, the result follows from Proposition 0GAT;
> 2. if `B` is rig-étale over `(A, I)`, the result follows from Lemma 0AKA;
> 3. if `I` is principal, the result follows from Elkik [III, Theorem 7].
>
> The four conjuncts are, in order, the theorem
> (`Rig.exists_finiteType_algEquiv_adicCompletion_of_isRigSmooth`) and the three partial results,
> each proved by the route the remark names: Proposition 0GAT and Lemma 0AKA through
> `Rig.exists_finiteType_adicCompletion_algEquiv_of_isRigSmooth_of_isGRing_or_isRigEtale`, and
> Elkik's theorem through `Rig.exists_finiteType_adicCompletion_algEquiv_of_isRigSmooth_principal`.
> In the theorem the finite type algebra lies in the universe of `A`; the partial results produce it
> in the universe `max u v`, as the lemmas they follow from do.

```lean
public theorem isRigSmooth_algebraization :
    (∀ {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
        (B : AdicFiniteTypeAlgebra.{u, v} A I), IsRigSmooth B →
        ∃ (C : Type u) (_ : CommRing C) (_ : Algebra A C), Algebra.FiniteType A C ∧
          Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)) ∧
    (∀ {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
        (B : AdicFiniteTypeAlgebra.{u, v} A I), IsRigSmooth B → IsGRing A →
        ∃ (C : Type (max u v)) (_ : CommRing C) (_ : Algebra A C), Algebra.FiniteType A C ∧
          Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)) ∧
    (∀ {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
        (B : AdicFiniteTypeAlgebra.{u, v} A I), IsRigSmooth B → IsRigEtale B →
        ∃ (C : Type (max u v)) (_ : CommRing C) (_ : Algebra A C), Algebra.FiniteType A C ∧
          Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C)) ∧
    (∀ {A : Type u} [CommRing A] [IsNoetherianRing A] {I : Ideal A}
        (B : AdicFiniteTypeAlgebra.{u, v} A I), IsRigSmooth B → I.IsPrincipal →
        ∃ (C : Type (max u v)) (_ : CommRing C) (_ : Algebra A C), Algebra.FiniteType A C ∧
          Nonempty (B.carrier ≃ₐ[A] AdicCompletion (I.map (algebraMap A C)) C))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.7, Tag 0GAU](https://stacks.math.columbia.edu/tag/0GAU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
