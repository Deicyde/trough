---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.globalLefschetzNumber, Stacks.EtaleCohomology.globalLefschetzNumberOfCtf, Stacks.EtaleCohomology.localLefschetzNumberOfCtf, Stacks.EtaleCohomology.LefschetzGaloisDescent.globalLefschetzNumber_eq_localLefschetzNumber, Stacks.EtaleCohomology.globalLefschetzNumberOfCtf_eq_sum_rationalPointStalkTrace, Stacks.EtaleCohomology.JacobianCorrespondence.fixedPointNumber_eq, AlgebraicGeometry.CurveGraph.fixedPointIntersection_eq, Stacks.EtaleCohomology.sum_trace_etaleConstantCohomologyPullback_eq_fixedPointIntersection
statement: formalized
proof: formalized
---

# 64.14 Lefschetz numbers

Section 64.14 of the Stacks Project, [Tag 03TW](https://stacks.math.columbia.edu/tag/03TW). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03TX, a definition

[Tag 03TX](https://stacks.math.columbia.edu/tag/03TX) in the Stacks Project.

**`Stacks.EtaleCohomology.globalLefschetzNumber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GlobalLefschetzNumber.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GlobalLefschetzNumber.lean#L72).

> The global Lefschetz number of `K`: the trace of the action `π_X^*` on the perfect complex
> `RΓ(X_k̄, K|_{X_k̄})`, an element of the additive commutator quotient `Λ^natural`.
>
> See [Stacks Project, Tag 03TX](https://stacks.math.columbia.edu/tag/03TX).

```lean
public def globalLefschetzNumber (Λ : Type u) [Ring Λ] [Finite Λ]
    (D : FrobeniusActionOnCohomology.{u, v} Λ) :
    CategoryTheory.FilteredDerived.AdditiveCommutatorQuotient Λ
```

**`Stacks.EtaleCohomology.globalLefschetzNumberOfCtf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GlobalLefschetzNumberOfCtfTrace.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GlobalLefschetzNumberOfCtfTrace.lean#L110).

> **Stacks, Tag 03TX: the global Lefschetz number of `K`.** Let `Λ` be a finite, possibly
> noncommutative, ring, `X` a projective curve over a finite field `k` with `p ^ q` elements, `k̄`
> an algebraic closure of `k` and `K ∈ D_ctf(X, Λ)`. The base change `c_K|_{X_k̄}` of the canonical
> map `c_K : π_X^{-1} K ⟶ K` induces an action `π_X^*` on the perfect complex
> `RΓ(X_k̄, K|_{X_k̄})`; the global Lefschetz number of `K` is its trace
> `Tr(π_X^* | RΓ(X_k̄, K|_{X_k̄}))`, an element of `Λ^natural`.
>
> `D_ctf(X, Λ)` is `Stacks.EtaleCohomology.IsCtf`, which makes sense for a noncommutative `Λ`; an
> object of it is bounded, so it is taken in the bounded below derived category, on which
> `RΓ(X_k̄, -)` is defined. Perfectness of `RΓ(X_k̄, K|_{X_k̄})` is [Stacks, Tag 03TV], proved, not
> assumed.

```lean
public def globalLefschetzNumberOfCtf (hcurve : IsCurve k gk)
    (hproj : IsProjective gk) (K : DerivedCategory.Plus (EtaleModules.{u, r} Λ X.obj))
    (hK : IsCtf.{u, r} B X Λ (DerivedCategory.Plus.ι.obj K)) :
    CategoryTheory.FilteredDerived.AdditiveCommutatorQuotient Λ
```

## Tag 03TY, a definition

[Tag 03TY](https://stacks.math.columbia.edu/tag/03TY) in the Stacks Project.

**`Stacks.EtaleCohomology.localLefschetzNumberOfCtf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LocalLefschetzNumberConstructibleFlat.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LocalLefschetzNumberConstructibleFlat.lean#L265). The attribute's comment: “the local Lefschetz number of an object K of D_ctf(X_étale, Λ) on a scheme X over a finite field k: the sum over the k-rational points x of X of the traces of the geometric Frobenius π_x of 03SW on the stalk K_x̄, an element of the additive commutator quotient Λ^natural. Λ is the arbitrary finite, possibly noncommutative, ring of 03TX and 03SZ. X(k), the stalks K_x̄ and the actions π_x are all computed from K and X — K_x̄ is the derived étale stalk of K at the geometric point above x and π_x is the induced action of the geometric Frobenius — and perfection of each K_x̄ is derived from membership of D_ctf, as in the source. Membership of D_ctf(X_étale, Λ) is written as condition (2) of 03TT, that K be represented by a bounded complex of constructible flat sheaves of Λ-modules, which is also how SGA 4½ Rapport 4.6 defines D_ctf”. References: SGA 4½ Rapport (4.6), “D_ctf(X, Λ)”.

> **Stacks, Tag 03TY: the local Lefschetz number of `K`.**  For a finite field `k` with `p ^ q`
> elements, an algebraically closed extension `k̄` of `k`, a scheme `X` over `k` with structure
> morphism `f` and finitely many `k`-rational points, an arbitrary finite — possibly
> noncommutative — coefficient ring `Λ`, and an object `K` of `D_ctf(X_étale, Λ)`, this is the sum
>
> `∑_{x ∈ X(k)} Tr(π_x | K_x̄)`
>
> over the `k`-rational points of `X` of the traces of the geometric Frobenius `π_x` of
> [Stacks, Tag 03SW] on the derived stalk `K_x̄` of `K` at the geometric point above `x`, an element
> of the additive commutator quotient `Λ^natural`.
>
> Perfection of each stalk `K_x̄`, which the source reads off `K ∈ D_ctf(X, Λ)` through
> [Stacks, Tag 03TT], is proved here rather than supplied:  it is
> `AlgebraicGeometry.derivedEtaleModuleStalk_isPerfect_of_isRepresentedByConstructibleFlatComplex`.
> Membership of `D_ctf(X, Λ)` is written as condition (2) of [Stacks, Tag 03TT], the condition that
> `K` be represented by a bounded complex of constructible flat sheaves of `Λ`-modules, which is
> also how [SGA 4½, Rapport 4.6] defines `D_ctf`; see the implementation notes of this file for why
> that is the formulation the source's generality on `Λ` calls for.

```lean
public def localLefschetzNumberOfCtf (hcard : Fintype.card k = p ^ q)
    (f : X.obj ⟶ Spec (.of k)) [Fintype (rationalPoints f)]
    (K : DerivedCategory
      (Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{w} Λ)))
    (hK : IsRepresentedByConstructibleFlatComplex.{u, w, r} B X Λ K) :
    CategoryTheory.FilteredDerived.AdditiveCommutatorQuotient Λ
```

## Tag 03TZ, a theorem

[Tag 03TZ](https://stacks.math.columbia.edu/tag/03TZ) in the Stacks Project.

**`Stacks.EtaleCohomology.LefschetzGaloisDescent.globalLefschetzNumber_eq_localLefschetzNumber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LefschetzTraceFormula.lean, line 989](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LefschetzTraceFormula.lean#L989). The attribute's comment: “the global and local Lefschetz numbers agree, with the Galois decomposition of the trace on the open complement (Stacks 03UC and 03UD) and the annihilation of each coefficient trace by the order of its stabiliser (Stacks 03UB, and Weil's formula Stacks 03U1 through the absence of fixed points on the Galois cover) as hypotheses; the reductions of Steps 3 to 6 of Stacks 03UG are not formalized”.

> **The Lefschetz trace formula (Stacks 03TZ).** Let `X` be a projective curve over a finite
> field `k`, let `Λ` be a finite ring and let `K` be an object of `D_ctf(X, Λ)`. Then the global
> and local Lefschetz numbers of `K` are equal:
>
>   `Tr(π_X^* | RΓ(X_k̄, K)) = ∑_{x ∈ X(k)} Tr(π_x | K_x̄)`
>
> in `Λ^natural`. The dévissage of `RΓ(X_k̄, K)` along the rational points of `X` splits the left
> hand side into the trace on the open complement of `X(k)` plus the right hand side, and the
> Galois descent of `Stacks.EtaleCohomology.LefschetzGaloisDescent` makes the trace on the open
> complement vanish.

```lean
public theorem globalLefschetzNumber_eq_localLefschetzNumber [Fintype points] :
    globalLefschetzNumber Λ D.globalDatum = localLefschetzNumber Λ points D.stalkDatum
```

**`Stacks.EtaleCohomology.globalLefschetzNumberOfCtf_eq_sum_rationalPointStalkTrace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ProjectiveCurveLefschetzTraceFormula.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/ProjectiveCurveLefschetzTraceFormula.lean#L93). The attribute's comment: “the Lefschetz trace formula for a projective curve over a finite field: global Lefschetz number (03TX) = sum over X(k) of the traces of the geometric Frobenius on the stalks, in Λ^natural, with K in D_ctf(X, Λ) given by a bounded below complex. Λ is a finite ring of cardinality prime to p, the standing hypothesis of the chapter fixed in 03SZ (trace.tex:386: 'Fix a finite ring Λ with cardinality prime to p'); the literal reading with an arbitrary finite Λ is false (k = F_5, E : y^2 = x^3 + 1 supersingular, Λ = Z/25, K = Λ: global number 1, local number #E(F_5) = 6). Λ : Type as in the formalization of 03UG”. References: SGA 4½ Rapport (3.2), “partial”; SGA 5 IIIB (1.3), “special case”.

> **Stacks, Tag 03TZ: the Lefschetz trace formula.** Let `X` be a projective curve over a finite
> field `k` with `p ^ q` elements, `k̄` an algebraic closure of `k`, `Λ` a finite, possibly
> noncommutative, ring of cardinality prime to `p` (the standing hypothesis of the chapter, fixed in
> [Stacks, Tag 03SZ]), and `K ∈ D_ctf(X, Λ)`, given as a bounded below complex of sheaves of
> `Λ`-modules on `X_étale` whose class lies in `D_ctf(X, Λ)`. Then the stalks `K_x̄` at the rational
> points are perfect, and the global and local Lefschetz numbers of `K` are equal:
>
> `Tr(π_X^* | RΓ(X_k̄, K)) = ∑_{x ∈ X(k)} Tr(π_x | K_x̄)` in `Λ^natural`.
>
> The left hand side is the global Lefschetz number of [Stacks, Tag 03TX]
> (`Stacks.EtaleCohomology.globalLefschetzNumberOfCtf`); on the right `K_x̄` is the stalk at the
> geometric point over `x` and `π_x` the geometric Frobenius of [Stacks, Tag 03SW] acting on it.
> Without the hypothesis `#Λ` prime to `p` the statement fails (see the module documentation).

```lean
theorem globalLefschetzNumberOfCtf_eq_sum_rationalPointStalkTrace (B : BigEtaleSite.{u})
    (X : B.Scheme) (Λ : Type) [Ring Λ] [Finite Λ] {k : Type u} [Field k] [Fintype k]
    (gk : X.obj ⟶ Spec (.of k)) (kbar : Type u) [Field kbar] [IsAlgClosed kbar] [Algebra k kbar]
    [Algebra.IsAlgebraic k kbar] (p q : ℕ) [Fact p.Prime] [CharP k p]
    (hcard : Fintype.card k = p ^ q) (hcop : Nat.Coprime (Nat.card Λ) p)
    (hcurve : IsCurve k gk) (hproj : IsProjective gk)
    (K : CochainComplex.Plus (EtaleModules.{u, 0} Λ X.obj))
    (hK : IsCtf.{u, 0} B X Λ (DerivedCategory.Plus.ι.obj (DerivedCategory.Plus.Q.obj K))) :
    letI : CharP kbar p := charP_of_injective_algebraMap (algebraMap k kbar).injective p
    ∃ hs : ∀ x : rationalPoints gk, StacksDraft.Perfect.IsPerfect
        (DerivedCategory.Q.obj (rationalPointStalkComplex.{u, 0} Λ kbar x.1 K)),
      globalLefschetzNumberOfCtf.{u, 0} B X Λ gk kbar p q hcard hcurve hproj
          (DerivedCategory.Plus.Q.obj K) hK =
        ∑ᶠ x : rationalPoints gk, perfectDerivedTrace Λ ⟨_, hs x⟩
          (DerivedCategory.Q.map (rationalPointStalkFrobenius.{u, 0} Λ kbar p q hcard x.1 K))
```

## Tag 03U1, a theorem

[Tag 03U1](https://stacks.math.columbia.edu/tag/03U1) in the Stacks Project.

**`Stacks.EtaleCohomology.JacobianCorrespondence.fixedPointNumber_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilTraceFormula.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilTraceFormula.lean#L187).

> **Weil's trace formula (Stacks 03U1).** Let `C` be a nonsingular projective curve over an
> algebraically closed field `k` and `φ : C → C` a `k`-endomorphism of `C` distinct from the
> identity. Let `V(φ) = Δ_C · Γ_φ`, the intersection number on `C × C` of the diagonal with the
> graph of `φ`, let `J = Pic⁰_{C/k}` be the jacobian of `C` and `φ^* : J → J` the action induced
> by `φ` by taking pullbacks. Then `V(φ) = 1 - Tr_J(φ^*) + deg φ`.

```lean
public theorem fixedPointNumber_eq (D : W.EndomorphismData) :
    W.fixedPointNumber D = 1 - W.trace D.pullback + D.degree
```

**`AlgebraicGeometry.CurveGraph.fixedPointIntersection_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilTraceFormulaCurve.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilTraceFormulaCurve.lean#L124).

> **Stacks Project, Tag 03U1 (Weil).** Let `C` be a smooth projective curve over an
> algebraically closed field `k` and `φ : C ⟶ C` a `k`-endomorphism distinct from the identity.
> Let `V(φ) = (Δ · Γ_φ)` be the intersection number of the diagonal and the graph of `φ` on
> `C ×_k C`. Then `V(φ) = 1 - Tr_J(φ^*) + deg φ`, where `φ^*` is the endomorphism of the Jacobian
> `J = Pic⁰_{C/k}` induced by pullback and `Tr_J(φ^*)` is its trace on the `ℓ`-adic Tate module of
> `J`, for any prime `ℓ` invertible in `k` (an integer independent of `ℓ`, see
> `AlgebraicGeometry.CurveGraph.existsUnique_jacobianTrace`).

```lean
theorem fixedPointIntersection_eq {k : Type u} [Field k] [IsAlgClosed k] {C : Scheme.{u}}
    (f : C ⟶ Spec (.of k)) [IsCurve k f] [Smooth f] [IsProper f]
    (hdim : topologicalKrullDim C ≤ 1) (φ : C ⟶ C) (w : φ ≫ f = f) (hφ : φ ≠ 𝟙 C)
    (ℓ : ℕ) [Fact ℓ.Prime] (hℓ : IsUnit (ℓ : k)) :
    ((fixedPointIntersection f hdim φ w : ℤ) : ℤ_[ℓ]) =
      1 - jacobianTateTrace f hdim φ w ℓ + (curveMapDegree f φ w : ℤ_[ℓ])
```

## Tag 03U3, a lemma

[Tag 03U3](https://stacks.math.columbia.edu/tag/03U3) in the Stacks Project.

**`Stacks.EtaleCohomology.sum_trace_etaleConstantCohomologyPullback_eq_fixedPointIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilFormulaEtaleCohomologyCurve.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilFormulaEtaleCohomologyCurve.lean#L56).

> **Weil's trace formula modulo `ℓ^n` (Stacks 03U3).** Let `C` be a nonsingular projective curve
> over an algebraically closed field `k`, let `φ : C → C` be a `k`-endomorphism of `C` distinct from
> the identity, and let `ℓ` be a prime invertible in `k`. Then every étale cohomology module
> `H^i(C, ℤ/ℓ^n)` of the constant sheaf is free of finite rank over `ℤ/ℓ^n`, and
>
>   `∑_{i=0}^{2} (-1)^i Tr(φ^* | H^i(C, ℤ/ℓ^n)) = V(φ) mod ℓ^n`,
>
> with `V(φ) = Δ_C · Γ_φ` the intersection number on `C ×_k C`
> (`AlgebraicGeometry.CurveGraph.fixedPointIntersection`), and `φ^*` the pullback on étale
> cohomology: restriction along `φ` followed by the canonical identification `φ^{-1}(ℤ/ℓ^n) ≅ ℤ/ℓ^n`.
>
> The degreewise traces are `1`, `Tr_J(φ^*) mod ℓ^n` and `deg φ`
> (`Stacks.EtaleCohomology.sum_trace_etaleConstantCohomologyPullback_eq_toZModPow`), and Weil's
> formula `V(φ) = 1 - Tr_J(φ^*) + deg φ` ([Stacks, Tag 03U1],
> `AlgebraicGeometry.CurveGraph.fixedPointIntersection_eq`) concludes.

```lean
theorem sum_trace_etaleConstantCohomologyPullback_eq_fixedPointIntersection
    {k : Type u} [Field k] [IsAlgClosed k] {C : Scheme.{u}} (f : C ⟶ Spec (.of k))
    [IsCurve k f] [Smooth f] [IsProper f] (φ : C ⟶ C) (w : φ ≫ f = f) (hφ : φ ≠ 𝟙 C)
    (ℓ : ℕ) [Fact ℓ.Prime] (hℓ : IsUnit (ℓ : k)) (n : ℕ) :
    (∀ i : ℕ, Module.Free (ZMod (ℓ ^ n))
        (Sheaf.H.{u + 1} (etaleConstantSheaf.{u, 0} C (ZMod (ℓ ^ n))) i) ∧
      Module.Finite (ZMod (ℓ ^ n))
        (Sheaf.H.{u + 1} (etaleConstantSheaf.{u, 0} C (ZMod (ℓ ^ n))) i)) ∧
    ∑ i ∈ Finset.range 3, (-1 : ZMod (ℓ ^ n)) ^ i * LinearMap.trace (ZMod (ℓ ^ n)) _
        ((etaleConstantCohomologyPullback φ (ZMod (ℓ ^ n)) i).toZModLinearMap (ℓ ^ n)) =
      (CurveGraph.fixedPointIntersection f (IsCurve.topologicalKrullDim_eq_one (f := f)).le φ w :
        ZMod (ℓ ^ n))
```

**`Stacks.EtaleCohomology.JacobianCorrespondence.EtaleFrobeniusAction.alternatingTrace_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilFormulaModPrimePower.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/WeilFormulaModPrimePower.lean#L157). The attribute's comment: “the alternating sum of the traces on the étale cohomology of the curve is the fixed point number V(φ) modulo ℓ^n, with the three degreewise traces — 1 in degree zero, Tr_J(φ^*) in degree one and deg φ in degree two — as hypotheses, the situation of Stacks 03U1 being the JacobianCorrespondence datum”.

> **Weil's trace formula modulo `ℓ^n` (Stacks 03U3).** In the situation of Weil's theorem,
> Tag 03U1, let `ℓ` be a prime invertible in `k`. Then
>
>   `∑_{i=0}^{2} (-1)^i Tr(φ^* | H^i(C, Z/ℓ^n Z)) = V(φ) mod ℓ^n`,
>
> the alternating sum of the traces of `φ^*` on the étale cohomology of `C` with coefficients in
> `Z/ℓ^n Z` being `1 - Tr_J(φ^*) + deg φ` by the three degreewise computations carried by
> `Stacks.EtaleCohomology.JacobianCorrespondence.EtaleFrobeniusAction`, and that being `V(φ)` by
> Weil's formula.

```lean
public theorem alternatingTrace_eq :
    T.alternatingTrace = (W.fixedPointNumber D : ZMod (ℓ ^ n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.14, Tag 03TW](https://stacks.math.columbia.edu/tag/03TW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
