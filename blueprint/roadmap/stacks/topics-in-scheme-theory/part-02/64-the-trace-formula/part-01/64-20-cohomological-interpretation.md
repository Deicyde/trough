---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.lFunction_eq_inv_charSeries_compactSupport, Stacks.EtaleCohomology.LAdicSheaf.nonempty_compactificationOf_and_rationalLFunction_eq_gradedCharSeries, Stacks.EtaleCohomology.LAdicSheaf.adicLFunction_eq_inv_charSeries_compactSupport, Stacks.EtaleCohomology.isPerfect_compactSupport_and_sum_stalkTrace_eq_compactSupportLefschetzNumber, Stacks.EtaleCohomology.perfectDerivedTrace_canonicalCompactSupportFrobenius_eq_sum_of_isCtf_of_isSeparated, Stacks.EtaleCohomology.LAdicSheaf.isZero_rationalGeometricCompactlySupportedCohomology_of_neg, Stacks.EtaleCohomology.LAdicSheaf.traceFormula, Stacks.InverseSystem.perfectTower_padicTrace_eq_alternating_trace_limitCohomology
statement: formalized
proof: formalized
---

# 64.20 Cohomological interpretation

Section 64.20 of the Stacks Project, [Tag 03UY](https://stacks.math.columbia.edu/tag/03UY). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03UZ, a theorem

[Tag 03UZ](https://stacks.math.columbia.edu/tag/03UZ) in the Stacks Project.

**`Stacks.EtaleCohomology.lFunction_eq_inv_charSeries_compactSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FiniteCoefficientCohomologicalInterpretation.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/FiniteCoefficientCohomologicalInterpretation.lean#L169). References: SGA 4½ Fonctions L (2.2), “Theorem 2.2 case a)”.

> **The cohomological interpretation of the L-function with finite coefficients.** Let `X` be a
> separated scheme of finite type over a finite field `k`, `k̄` an algebraic closure of `k`, `Λ` a
> finite commutative ring of order prime to the characteristic of `k`, and `F` a constructible flat
> `Λ`-module on `X_étale`. Then `X` has a compactification, and for every compactification `j`
> (through which `RΓ_c(X_k̄, -)` and `π_X^*` are computed) and every presentation `#k = p ^ q`,
> `RΓ_c(X_k̄, F)` is perfect and `L(X, F) = det(1 - π_X^* T | RΓ_c(X_k̄, F))⁻¹` in `Λ⟦T⟧`.

```lean
theorem lFunction_eq_inv_charSeries_compactSupport
    [Algebra.IsAlgebraic k kbar] (Λ : Type) [CommRing Λ] [Finite Λ]
    (hΛ : ((Nat.card Λ : ℕ) : k) ≠ 0)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ))
    (hF : IsConstructibleFlatModuleSheaf B X Λ F) :
    Nonempty (CompactificationOf (Over.mk f)) ∧
      ∀ (j : CompactificationOf (Over.mk f)) (p q : ℕ) [Fact p.Prime] [CharP k p]
        (hcard : Fintype.card k = p ^ q),
        LFunctionCharSeriesIdentity B X Λ f kbar F hF j p q hcard
```

## Tag 03V0, a theorem

[Tag 03V0](https://stacks.math.columbia.edu/tag/03V0) in the Stacks Project.

**`Stacks.EtaleCohomology.LAdicSheaf.nonempty_compactificationOf_and_rationalLFunction_eq_gradedCharSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LAdicTraceFormulaFinal.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LAdicTraceFormulaFinal.lean#L190). The attribute's comment: “for a Q\_l-sheaf with l invertible in k, X separated (where H^i\_c is defined); H^i\_c through any compactification of X over k (one exists by 0F41)”.

> **[Stacks, Tag 03V0]: the L-function of a `ℚ_ℓ`-sheaf.** Let `X` be a separated scheme of
> finite type over a finite field `k` with `p ^ q` elements, `k̄` an algebraic closure of `k`, `ℓ` a
> prime with `ℓ ≠ p` and `F` a `ℚ_ℓ`-sheaf on `X`. Then `X` has a compactification over `k`, and
> for every compactification `j : X ⟶ X̄`, through which `Hⁱ_c(X_k̄, F)` is defined,
> `L(X, F) = ∏ᵢ det(1 - π_X^* T | Hⁱ_c(X_k̄, F))^{(-1)^{i+1}}` in `ℚ_ℓ[[T]]`.
>
> A compactification exists by Nagata's theorem
> (`AlgebraicGeometry.hasCompactification_of_compactSpace_quasiSeparatedSpace`, Tag 0F41), since
> `Spec k` is quasi-compact and quasi-separated. The library compares compactly supported
> cohomology computed through two compactifications at a finite level
> (`Stacks.EtaleCohomology.compactSupportSheafCohomologyCompactificationIso`); the identity here
> is proved for every compactification, so it does not depend on that comparison.
>
> `X` is separated because `Hⁱ_c` is defined for separated schemes only (Definition 03UT).
> `ℓ ≠ p` is the chapter's standing convention; the statement is false for `ℓ = p`
> (`L(𝔸¹_k, ℚ_p) = 1/(1 - p ^ q T)` while the alternating product is `1`).

```lean
theorem LAdicSheaf.nonempty_compactificationOf_and_rationalLFunction_eq_gradedCharSeries
    (hℓp : ℓ ≠ p) (F : LAdicSheaf.{u, u + 1} B X ℓ) :
    Nonempty (CompactificationOf (Over.mk f)) ∧
      ∀ j : CompactificationOf (Over.mk f),
        LAdicSheaf.rationalLFunction B X ℓ F f =
          gradedCharSeries
            (fun i => LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f j kbar F i)
            (fun i => (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f j kbar p q
              hcard F i).hom)
```

## Tag 03V1, a remark

[Tag 03V1](https://stacks.math.columbia.edu/tag/03V1) in the Stacks Project.

**`Stacks.EtaleCohomology.LAdicSheaf.adicLFunction_eq_inv_charSeries_compactSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/AdicLFunctionCohomologicalInterpretation.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/AdicLFunctionCohomologicalInterpretation.lean#L63). The attribute's comment: “the identity for Z\_l coefficients is the l-adic limit of 03UZ at the levels, and it is equivalent to 03V0 for F ⊗ Q\_l since Z\_l has no l-torsion”.

> **The ℓ-adic cohomological interpretation of the L-function.** Let `X` be a separated scheme
> of finite type over a finite field `k`, `k̄` an algebraic closure of `k`, `ℓ` a prime invertible
> in `k`, and `F = (Fₙ)` an ℓ-adic sheaf on `X_étale` whose levels are flat over `ℤ/ℓⁿ⁺¹ℤ`. Then `X`
> has a compactification, and for every compactification `j` and every presentation `#k = p ^ q`:
> * the complexes `RΓ_c(X_k̄, Fₙ)` are perfect and the ℓ-adic L-function `L_{ℤ_ℓ}(X, F)` reduces
>   modulo every `ℓⁿ⁺¹` to `det(1 - π_X^* T | RΓ_c(X_k̄, Fₙ))⁻¹`;
> * for every `c ∈ ℤ_ℓ⟦T⟧` with these reductions, `L_{ℤ_ℓ}(X, F) = c` if and only if
>   `L(X, F ⊗ ℚ_ℓ) = ∏ᵢ det(1 - π_X^* T | Hⁱ_c(X_k̄, F ⊗ ℚ_ℓ)) ^ ((-1) ^ (i + 1))`.

```lean
public theorem LAdicSheaf.adicLFunction_eq_inv_charSeries_compactSupport (hℓ : (ℓ : k) ≠ 0) :
    haveI := isNoetherian_of_locallyOfFiniteType f
    ∀ (F : LAdicSheaf B X ℓ) (hF : ∀ n, PowExact ℓ (n + 1) (F.level n)),
    Nonempty (CompactificationOf (Over.mk f)) ∧
      ∀ (j : CompactificationOf (Over.mk f)) (p q : ℕ) [Fact p.Prime] [CharP k p]
        (hcard : Fintype.card k = p ^ q),
        ∃ hP : ∀ n, StacksDraft.Perfect.IsPerfect.{0, u + 1, u + 2} (DerivedCategory.Plus.ι.obj
            (compactSupportFrobeniusCohomology.{u, 0} (ZMod (ℓ ^ (n + 1))) f j kbar
              (LAdicSheaf.levelComplex B X ℓ F n))),
          (∀ n : ℕ, PowerSeries.map (PadicInt.toZModPow (n + 1))
              (LAdicSheaf.adicLFunction B X ℓ F hF f) =
            (((CategoryTheory.FilteredDerived.perfectDerivedCharSeries.{u + 2, 0, u + 1}
              (ZMod (ℓ ^ (n + 1)))
              ((LAdicSheaf.geometricPerfectTower B X ℓ f j kbar p q hcard F
                (LAdicSheaf.powExact_etaleLevel B X ℓ F hF) hP).obj n) (hP n)
              ((LAdicSheaf.geometricPerfectTower B X ℓ f j kbar p q hcard F
                (LAdicSheaf.powExact_etaleLevel B X ℓ F hF) hP).endo n))⁻¹ :
                (ZMod (ℓ ^ (n + 1)))⟦X⟧ˣ) : (ZMod (ℓ ^ (n + 1)))⟦X⟧)) ∧
          ∀ c : ℤ_[ℓ]⟦X⟧, (∀ n : ℕ, PowerSeries.map (PadicInt.toZModPow (n + 1)) c =
              (((CategoryTheory.FilteredDerived.perfectDerivedCharSeries.{u + 2, 0, u + 1}
                (ZMod (ℓ ^ (n + 1)))
                ((LAdicSheaf.geometricPerfectTower B X ℓ f j kbar p q hcard F
                  (LAdicSheaf.powExact_etaleLevel B X ℓ F hF) hP).obj n) (hP n)
                ((LAdicSheaf.geometricPerfectTower B X ℓ f j kbar p q hcard F
                  (LAdicSheaf.powExact_etaleLevel B X ℓ F hF) hP).endo n))⁻¹ :
                  (ZMod (ℓ ^ (n + 1)))⟦X⟧ˣ) : (ZMod (ℓ ^ (n + 1)))⟦X⟧)) →
            (LAdicSheaf.adicLFunction B X ℓ F hF f = c ↔
              LAdicSheaf.rationalLFunction B X ℓ F f =
                gradedCharSeries
                  (fun i =>
                    LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f j kbar F i)
                  (fun i => (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f j kbar
                    p q hcard F i).hom))
```

## Tag 03V3, a theorem

[Tag 03V3](https://stacks.math.columbia.edu/tag/03V3) in the Stacks Project.

**`Stacks.EtaleCohomology.isPerfect_compactSupport_and_sum_stalkTrace_eq_compactSupportLefschetzNumber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaConstructibleFiniteTor.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaConstructibleFiniteTor.lean#L85). The attribute's comment: “`Λ : Type` (universe 0); X in a big étale site; K ∈ D\_ctf(X, Λ) represented by a bounded below complex; RΓ\_c(X\_k̄, K) through any compactification (one exists by 0F41)”. References: SGA 4½ Rapport (4.10), “special case”; SGA 4½ Rapport (5.13), “more general”.

> **The trace formula ([Stacks, Tag 03V3]).** Let `k` be a finite field with `p ^ q` elements and
> `k̄` an algebraic closure of `k`, let `X` be a separated scheme of finite type over `k` (of any
> dimension), let `Λ` be a finite ring whose cardinality is invertible in `k`, and let
> `K ∈ D_ctf(X, Λ)`. Then `X` has a compactification over `k`, and for every compactification
> `j : X ⟶ X̄` the complex `RΓ_c(X_k̄, K) = RΓ(X̄_k̄, (j_! K)|_{X̄_k̄})` lies in `D_perf(Λ)`, and
>
> `∑_{x ∈ X(k)} Tr(π_x | K_x̄) = Tr(π_X^* | RΓ_c(X_k̄, K))`
>
> in `Λ^natural`, where the stalks `K_x̄` at the rational points are perfect (so that their traces
> are defined), `π_x` is the geometric Frobenius acting on `K_x̄` and `π_X^*` is the canonical
> Frobenius action on `RΓ_c(X_k̄, K)`.

```lean
theorem isPerfect_compactSupport_and_sum_stalkTrace_eq_compactSupportLefschetzNumber
    (B : BigEtaleSite.{u}) (Λ : Type) [Ring Λ] [Finite Λ]
    {k : Type u} [Field k] [Fintype k] (kbar : Type u) [Field kbar] [IsAlgClosed kbar]
    [Algebra k kbar] [Algebra.IsAlgebraic k kbar] (p q : ℕ) [Fact p.Prime] [CharP k p]
    [CharP kbar p] (hcard : Fintype.card k = p ^ q)
    (hcop : Nat.Coprime (Nat.card Λ) (Fintype.card k))
    (X : B.Scheme) (f : X.obj ⟶ Spec (.of k)) [IsSeparated f] [LocallyOfFiniteType f]
    [QuasiCompact f] (K : CochainComplex.Plus (EtaleModules.{u, 0} Λ X.obj))
    (hK : IsCtf B X Λ (DerivedCategory.Q.obj K.obj)) :
    Nonempty (CompactificationOf (Over.mk f)) ∧
      ∀ j : CompactificationOf (Over.mk f),
        StacksDraft.Perfect.IsPerfect (DerivedCategory.Plus.ι.obj
          (compactSupportFrobeniusCohomology.{u, 0} Λ f j kbar K)) ∧
        ∃ (hX : StacksDraft.Perfect.IsPerfect (DerivedCategory.Plus.ι.obj
            (compactSupportFrobeniusCohomology.{u, 0} Λ f j kbar K)))
          (hs : ∀ x : rationalPoints f, StacksDraft.Perfect.IsPerfect
            (DerivedCategory.Q.obj (rationalPointStalkComplex.{u, 0} Λ kbar x.1 K))),
          ∑ᶠ x : rationalPoints f, perfectDerivedTrace Λ ⟨_, hs x⟩
              (DerivedCategory.Q.map (rationalPointStalkFrobenius.{u, 0} Λ kbar p q hcard x.1 K)) =
            canonicalCompactSupportLefschetzNumber.{u, 0} Λ f j kbar p q hcard K hX
```

**`Stacks.EtaleCohomology.perfectDerivedTrace_canonicalCompactSupportFrobenius_eq_sum_of_isCtf_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaDctfFinal.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/TraceFormulaDctfFinal.lean#L79). The attribute's comment: “RGamma\_c(X\_kbar, K) is perfect and the trace formula, for K in D\_ctf(X, Lambda)”.

> **[Stacks, Tag 03V3]: the trace formula for `D_ctf`.** Let `X` be a separated scheme of finite
> type over the finite field `k` with `p ^ q` elements, lying in the big étale site `B`, with a
> compactification `j : X ⟶ X̄` (which defines `RΓ_c`), and `k̄` an algebraic closure of `k`; let
> `Λ` be a finite ring (possibly noncommutative) with `#Λ` invertible in `k`, and `K` a bounded
> below complex of sheaves of `Λ`-modules on `X_étale` whose class lies in `D_ctf(X, Λ)`. Then
> `RΓ_c(X_k̄, K)` is perfect, the stalks `K_x̄` at the rational points are perfect, and
> `Tr(π_X^* | RΓ_c(X_k̄, K)) = ∑_{x ∈ X(k)} Tr(π_x | K_x̄)` in `Λ^♮`.
>
> `X` is separated and of finite type over `k` as in the setting of Tag 03UG ("`X/k` as above"),
> where `RΓ_c` is defined (Definition 03UT); the instance `Fintype (rationalPoints f)` always holds
> (`Stacks.EtaleCohomology.finite_rationalPoints`).

```lean
theorem perfectDerivedTrace_canonicalCompactSupportFrobenius_eq_sum_of_isCtf_of_isSeparated
    (hΛ : (Nat.card Λ : k) ≠ 0) {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] [IsSeparated f] [QuasiCompact f]
    [Fintype (rationalPoints f)] (J : CompactificationOf (Over.mk f))
    (K : CochainComplex.Plus (EtaleModules.{u, 0} Λ X)) (hX : B.Contains X)
    (hK : IsCtf B (B.obj X hX) Λ (DerivedCategory.Q.obj K.obj)) :
    ∃ (hKs : HasPerfectStalks Λ K) (hperf : StacksDraft.Perfect.IsPerfect
        (DerivedCategory.Plus.ι.obj (compactSupportFrobeniusCohomology.{u, 0} Λ f J kbar K))),
      perfectDerivedTrace Λ ⟨_, hperf⟩ (DerivedCategory.Plus.ι.map
          (canonicalCompactSupportFrobenius.{u, 0} Λ f J kbar p q hcard K)) =
        ∑ x : rationalPoints f, perfectDerivedTrace Λ ⟨_, hKs (rationalGeometricPoint kbar x.1)⟩
          (DerivedCategory.Q.map (rationalPointStalkFrobenius.{u, 0} Λ kbar p q hcard x.1 K))
```

## Tag 03V2, a theorem

[Tag 03V2](https://stacks.math.columbia.edu/tag/03V2) in the Stacks Project.

**`Stacks.EtaleCohomology.LAdicSheaf.isZero_rationalGeometricCompactlySupportedCohomology_of_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricLAdicCompactSupport.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/GeometricLAdicCompactSupport.lean#L361). The attribute's comment: “the lower half of the degree bound: H^i\_c(X\_kbar, F) = 0 for i < 0”.

> **`Hⁱ_c(X_k̄, F ⊗ Q_ℓ) = 0` for `i < 0`**, for every ℓ-adic sheaf `F` on a separated scheme of
> finite type over a field, every extension field `k̄` and every compactification: the lower half
> of the statement of [Tag 03V2](https://stacks.math.columbia.edu/tag/03V2) that
> `Hⁱ_c(X_k̄, F)` is nonzero for `0 ≤ i ≤ 2 dim X` only.

```lean
public theorem LAdicSheaf.isZero_rationalGeometricCompactlySupportedCohomology_of_neg
    (F : LAdicSheaf B X ℓ) (i : ℤ) (hi : i < 0) :
    IsZero (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f j kbar F i)
```

**`Stacks.EtaleCohomology.LAdicSheaf.traceFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LAdicTraceFormulaFinal.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Trace/LAdicTraceFormulaFinal.lean#L88). The attribute's comment: “finiteness, the degree bounds 0 <= i <= 2 dim X and the trace formula”. References: SGA 4½ Rapport (2.10), “special case”; SGA 7 I (0.1.1), “Q\_ℓ clause of case 0.1.1”.

> **The trace formula for a `ℚ_ℓ`-sheaf.** Let `X` be a separated scheme of finite type over a
> finite field `k` with `p ^ q` elements, `k̄` an algebraic closure of `k`, `ℓ` a prime with `ℓ ≠ p`
> and `F` a `ℚ_ℓ`-sheaf on `X` (an ℓ-adic sheaf, tensored with `ℚ_ℓ`). Then
> * `Hⁱ_c(X_k̄, F)` is a finite dimensional `ℚ_ℓ`-vector space for every `i`,
> * it is nonzero only for `0 ≤ i ≤ 2 dim X`, and
> * `∑_{x ∈ X(k)} Tr(π_x | F_x̄) = ∑ᵢ (-1)ⁱ Tr(π_X^* | Hⁱ_c(X_k̄, F))`, the rational points being the
>   closed points of residue degree one.
>
> `ℓ ≠ p` is the chapter's standing convention; the statement is false for `ℓ = p`
> (`X = 𝔸¹_k`, `F = ℚ_p`: the right hand side is `0`, the left hand side `p ^ q`).

```lean
theorem LAdicSheaf.traceFormula (hℓp : ℓ ≠ p) (F : LAdicSheaf.{u, u + 1} B X ℓ) :
    (∀ i : ℤ, Module.Finite ℚ_[ℓ]
      (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f j kbar F i)) ∧
    (∀ i : ℤ, Nontrivial
        (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f j kbar F i) →
      0 ≤ i ∧ ∃ d : ℕ, topologicalKrullDim X.1 = d ∧ i ≤ 2 * (d : ℤ)) ∧
    ∑ᶠ (x : closedPoints X.1) (_ : residueDegree f x.1 = 1),
        LinearMap.trace ℚ_[ℓ] _
          (LAdicSheaf.rationalStalkFrobenius B X ℓ F x.1 (finite_residueField f x.1 x.2)) =
      ∑ᶠ i : ℤ, (if Even i then (1 : ℚ_[ℓ]) else -1) *
        LinearMap.trace ℚ_[ℓ]
          (LAdicSheaf.rationalGeometricCompactlySupportedCohomology B X ℓ f j kbar F i)
          (LAdicSheaf.rationalGeometricCompactlySupportedFrobenius B X ℓ f j kbar p q hcard F
            i).hom
```

## Tag 03V4, a lemma

[Tag 03V4](https://stacks.math.columbia.edu/tag/03V4) in the Stacks Project.

**`Stacks.InverseSystem.perfectTower_padicTrace_eq_alternating_trace_limitCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/InverseSystem/PerfectTower/TraceFormula.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/InverseSystem/PerfectTower/TraceFormula.lean#L474). The attribute's comment: “parts (1), (2) and (3)”.

> **Stacks 03V4.** Let `ℓ` be a prime.  Suppose we have `Kₙ ∈ D_perf(ℤ/ℓⁿ⁺¹ℤ)`,
> `πₙ : Kₙ → Kₙ` and isomorphisms `φₙ : Kₙ₊₁ ⊗ᴸ_{ℤ/ℓⁿ⁺²ℤ} ℤ/ℓⁿ⁺¹ℤ → Kₙ` compatible with `πₙ₊₁`
> and `πₙ` — that is, a `PerfectTower ℓ`.  Then
>
> 1. the elements `tₙ = Tr(πₙ | Kₙ) ∈ ℤ/ℓⁿ⁺¹ℤ` form an element `t_∞ = {tₙ}` of `ℤ_[ℓ]`, namely
>    there is exactly one `t_∞ ∈ ℤ_[ℓ]` reducing to `tₙ` modulo `ℓⁿ⁺¹` for every `n`;
> 2. the `ℤ_[ℓ]`-module `Hⁱ_∞ = limₙ Hⁱ(Kₙ)` is finite and is nonzero for finitely many `i`
>    only; and
> 3. the operators `Hⁱ(πₙ) : Hⁱ(Kₙ) → Hⁱ(Kₙ)` are compatible with the transitions of the
>    inverse system, hence define a unique `πⁱ_∞ : Hⁱ_∞ → Hⁱ_∞` lying over them, and every such
>    family satisfies `∑ᵢ (-1)ⁱ Tr(πⁱ_∞ | Hⁱ_∞ ⊗_{ℤ_[ℓ]} ℚ_[ℓ]) = t_∞`.
>
> Levels are indexed so that level `n` carries coefficients in `ℤ/ℓⁿ⁺¹ℤ`, avoiding the zero
> ring; `(-1)ⁱ` for `i : ℤ` is written as `if Even i then 1 else -1`.

```lean
public theorem perfectTower_padicTrace_eq_alternating_trace_limitCohomology
    {ℓ : ℕ} [Fact ℓ.Prime] (T : PerfectTower.{v} ℓ) :
    -- (1) the traces `tₙ` form an element `t_∞` of `ℤ_[ℓ]`
    (∃! t : ℤ_[ℓ], ∀ n : ℕ, PadicInt.toZModPow (n + 1) t = traceAtLevel T n) ∧
    -- (2) each `Hⁱ_∞` is a finite `ℤ_[ℓ]`-module, and only finitely many are nonzero
    (∀ i : ℤ, Module.Finite ℤ_[ℓ] (limitCohomology T i)) ∧
    {i : ℤ | Nontrivial (limitCohomology T i)}.Finite ∧
    -- (3) the `Hⁱ(πₙ)` are compatible with the transitions of the inverse system
    (∀ (i : ℤ) (n : ℕ), levelCohomologyEndoHom T i (n + 1) ≫ levelCohomologyTransition T i n =
        levelCohomologyTransition T i n ≫
          (ModuleCat.restrictScalars.{v} (levelCast ℓ n)).map (levelCohomologyEndoHom T i n)) ∧
    -- (3) and so define a unique family `πⁱ_∞` of endomorphisms of the `Hⁱ_∞`
    (∃! π : ∀ i : ℤ, limitCohomology T i →ₗ[ℤ_[ℓ]] limitCohomology T i,
        ∀ (i : ℤ) (n : ℕ) (a : limitCohomology T i),
          limitCohomologyProjection T i n (π i a) =
            levelCohomologyEndoₗ T i n (limitCohomologyProjection T i n a)) ∧
    -- (3) which satisfies `∑ᵢ (-1)ⁱ Tr(πⁱ_∞ | Hⁱ_∞ ⊗ ℚ_[ℓ]) = t_∞`
    (∀ t : ℤ_[ℓ], (∀ n : ℕ, PadicInt.toZModPow (n + 1) t = traceAtLevel T n) →
      ∀ π : ∀ i : ℤ, limitCohomology T i →ₗ[ℤ_[ℓ]] limitCohomology T i,
        (∀ (i : ℤ) (n : ℕ) (a : limitCohomology T i),
            limitCohomologyProjection T i n (π i a) =
              levelCohomologyEndoₗ T i n (limitCohomologyProjection T i n a)) →
          ∑ᶠ i : ℤ, (if Even i then (1 : ℚ_[ℓ]) else -1) *
              LinearMap.trace ℚ_[ℓ] (ℚ_[ℓ] ⊗[ℤ_[ℓ]] limitCohomology T i)
                (LinearMap.baseChange ℚ_[ℓ] (π i)) =
            (t : ℚ_[ℓ]))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 64.20, Tag 03UY](https://stacks.math.columbia.edu/tag/03UY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
