---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.WeilData.trace_pt_eq_add_comp_pullTw, Stacks.WeilCohomology.PoincareDualityPushforwardSetup.integration_eq_add_comp_pullback, Stacks.WeilCohomology.WeilData.grade_eq_bot_of_dimension_zero, Stacks.WeilCohomology.WeilData.finiteDimensional_H0_of_dimension_zero, Stacks.WeilCohomology.WeilData.finrank_grade_zero_eq_degree, Stacks.WeilCohomology.WeilData.isSeparable_H0_of_dimension_zero, Stacks.WeilCohomology.WeilData.traceZero_eq_trace, Stacks.WeilCohomology.WeilData.trace_cycleClass_fundamentalClass_of_dimension_zero
statement: formalized
proof: formalized
---

# 45.10 Further properties

Section 45.10 of the Stacks Project, [Tag 0FHN](https://stacks.math.columbia.edu/tag/0FHN). 9 tags here are carried by 25 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FHP, a lemma

[Tag 0FHP](https://stacks.math.columbia.edu/tag/0FHP) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.trace_pt_eq_add_comp_pullTw`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionTrace.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionTrace.lean#L60).

> **Stacks Project, Tag 0FHP.** Let `X` and `Y` be nonempty smooth projective schemes over `k`,
> both equidimensional of dimension `d`, and let `c` be a coproduct `X ⨿ Y` with coprojections
> `i`, `j`. Given (D0)–(D3) satisfying (A), (B) and (C), `∫_{X ⨿ Y} = ∫_X + ∫_Y`, in the sense
> that `∫_{X ⨿ Y} = ∫_X ∘ i^* + ∫_Y ∘ j^*` on `H^{2d}(X ⨿ Y)(d)`.

```lean
theorem trace_pt_eq_add_comp_pullTw (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) {X Y : (SmoothProjectiveScheme k).FullSubcategory}
    {c : BinaryCofan X Y} (hc : IsColimit c) {d : ℕ} (hX : IsNonemptyEquidimensional X d)
    (hY : IsNonemptyEquidimensional Y d) :
    W.trace c.pt d (isNonemptyEquidimensional_pt hc hX hY) =
      W.trace X d hX ∘ₗ W.pullTw (Y := c.pt) c.inl _ _ +
        W.trace Y d hY ∘ₗ W.pullTw (Y := c.pt) c.inr _ _
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.integration_eq_add_comp_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/TraceDisjointUnion.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/TraceDisjointUnion.lean#L186).

> **Stacks Project, Tag 0FHP.** Additivity of the trace map over a disjoint union:
> `∫_{X ⨿ Y} = ∫_X + ∫_Y`, as an identity between linear functionals on `H^{2d}(X ⨿ Y)`, the two
> summands being the trace maps of the components precomposed with restriction along the
> coprojections.

```lean
theorem integration_eq_add_comp_pullback (i : X ⟶ Z) (j : Y ⟶ Z)
    (hdX : S.dimension X = S.dimension Z) (hdY : S.dimension Y = S.dimension Z)
    (hone : (S.H Z).one = S.pushforwardOne i hdX + S.pushforwardOne j hdY) :
    (S.integration Z).toLinearMap =
      (S.integration X).toLinearMap.comp
          ((ExternallyGraded.degreeCast (R := F) (X := (S.H X).piece)
              (show 2 * (S.dimension Z : ℤ) = 2 * (S.dimension X : ℤ) by omega)).comp
            (S.pullback i (2 * (S.dimension Z : ℤ)))) +
        (S.integration Y).toLinearMap.comp
          ((ExternallyGraded.degreeCast (R := F) (X := (S.H Y).piece)
              (show 2 * (S.dimension Z : ℤ) = 2 * (S.dimension Y : ℤ) by omega)).comp
            (S.pullback j (2 * (S.dimension Z : ℤ))))
```

## Tag 0FHQ, a lemma

[Tag 0FHQ](https://stacks.math.columbia.edu/tag/0FHQ) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.grade_eq_bot_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean, line 813](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean#L813). The attribute's comment: “part (1): H^i(X) = 0 for i ≠ 0, over the actual category of smooth projective schemes and the actual Weil data (D0)-(D3) satisfying (A), (B), (C)”.

> **Stacks 0FHQ (1)**: for data (D0)–(D3) satisfying (A), (B), (C) and `X` a smooth projective
> scheme of dimension zero over `k`, `H^i(X) = 0` for `i ≠ 0`.

```lean
theorem grade_eq_bot_of_dimension_zero {n : ℤ} (hn : n ≠ 0) : W.grade X n = ⊥
```

**`Stacks.WeilCohomology.WeilData.finiteDimensional_H0_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean, line 824](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean#L824). The attribute's comment: “part (2), finiteness: H^0(X) is finite dimensional over F”.

> **Stacks 0FHQ (2), finiteness**: `H^0(X)` is a finite `F`-algebra, `X` of dimension zero.

```lean
theorem finiteDimensional_H0_of_dimension_zero : FiniteDimensional F (W.H0 X)
```

**`Stacks.WeilCohomology.WeilData.finrank_grade_zero_eq_degree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean, line 838](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean#L838). The attribute's comment: “part (3): dim_F H^0(X) = deg(X → Spec k)”.

> **Stacks 0FHQ (3)**: `dim_F H^0(X) = deg(X → Spec k)`, the degree being the rank of the finite
> flat structure morphism at the point of `Spec k` (Stacks 02KA, `Scheme.Hom.finrank`).

```lean
theorem finrank_grade_zero_eq_degree (s : Spec (.of k)) :
    Module.finrank F (W.grade X 0) = X.obj.hom.finrank s
```

**`Stacks.WeilCohomology.WeilData.isSeparable_H0_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean, line 1038](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean#L1038). The attribute's comment: “part (2), separability: H^0(X) is a separable F-algebra”.

> **Stacks 0FHQ (2), separability**: `H^0(X)` is a separable `F`-algebra, `X` of dimension
> zero.

```lean
theorem isSeparable_H0_of_dimension_zero : Algebra.IsSeparable F (W.H0 X)
```

**`Stacks.WeilCohomology.WeilData.traceZero_eq_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean, line 1046](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean#L1046). The attribute's comment: “part (4): ∫_X : H^0(X) → F is the trace map”.

> **Stacks 0FHQ (4)**: `∫_X : H^0(X) → F` is the trace map of the `F`-algebra `H^0(X)`; here
> `a ∈ H^0(X)` enters `∫_X` through `H^0(X)(0) = H^0(X) ⊗_F F(0)`.

```lean
theorem traceZero_eq_trace (a : W.H0 X) :
    W.trace X 0 (isNonemptyEquidimensional_of_dimension_zero hX)
        ((W.twCoord X _ _).symm ⟨a.1, a.2⟩) = Algebra.trace F (W.H0 X) a
```

**`Stacks.WeilCohomology.WeilData.trace_cycleClass_fundamentalClass_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean, line 1060](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean#L1060). The attribute's comment: “part (6): ∫_X γ([X]) = deg(X → Spec k)”.

> **Stacks 0FHQ (6)**: `∫_X γ([X]) = deg(X → Spec k)`.

```lean
theorem trace_cycleClass_fundamentalClass_of_dimension_zero (s : Spec (.of k)) :
    W.trace X 0 (isNonemptyEquidimensional_of_dimension_zero hX)
        (W.cycleClass X 0 (fundamentalClass X)) = (X.obj.hom.finrank s : F)
```

**`Stacks.WeilCohomology.subsingleton_cohomology_of_dimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean#L277). The attribute's comment: “part (1): H^i(X) = 0 for i ≠ 0”.

> **Stacks Project, Tag 0FHQ, part (1).** The cohomology of a smooth projective scheme of
> dimension zero over the base field vanishes in every nonzero degree.

```lean
theorem subsingleton_cohomology_of_dimension_zero (i : ℤ) (hi : i ≠ 0) : Subsingleton (HX i)
```

**`Stacks.WeilCohomology.finrank_cohomology_zero_eq_degree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean#L287). The attribute's comment: “part (3): dim_F H^0(X) = deg(X → Spec k)”.

> **Stacks Project, Tag 0FHQ, part (3).** The degree-zero cohomology of a smooth projective
> scheme `X` of dimension zero over the base field has dimension `deg(X → Spec(k))` over the
> coefficient field; the degree is the number `n` of copies of `Y` in the decomposition of
> `X × Y`.

```lean
theorem finrank_cohomology_zero_eq_degree : Module.finrank F (HX 0) = n
```

**`Stacks.WeilCohomology.integration_eq_trace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean#L332). The attribute's comment: “part (4): ∫_X is the trace map”.

> **Stacks Project, Tag 0FHQ, part (4).** Integration on a smooth projective scheme of
> dimension zero over the base field is the trace map of the `F`-algebra `H^0(X)`.
>
> The hypothesis `hint` is the identity `(∫_X a) · 1 = ∑_σ Spec(σ)^*a` in `H^0(Y)`, and `e`
> together with `he` is the isomorphism `H^0(Y) ⊗_F H^0(X) ≅ H^0(Y)^Σ` of `H^0(Y)`-algebras
> sending `1 ⊗ a` to `(Spec(σ)^*a)_σ`. The right-hand side of `hint` is therefore the trace of
> `1 ⊗ a` over `H^0(Y)`, which is the image of the trace of `a` over `F`.

```lean
theorem integration_eq_trace : integration = Algebra.trace F A
```

**`Stacks.WeilCohomology.isSeparable_cohomology_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean#L385). The attribute's comment: “part (2): H^0(X) is a finite separable F-algebra”.

> **Stacks Project, Tag 0FHQ, part (2).** The degree-zero cohomology of a smooth projective
> scheme of dimension zero over the base field is a finite separable algebra over the coefficient
> field; finiteness is the hypothesis `[FiniteDimensional F A]`, which is axiom `(A)(a)`.
>
> Reducing the isomorphism `e` modulo a maximal ideal of `B = H^0(Y)` produces `n` characters of
> `A = H^0(X)` with values in the residue field `L` which span `L^n` over `L`; as `A` has
> dimension `n` over `F` by part (3), the resulting map `A → L^n` is injective, so `A` is
> reduced, and a reduced finite-dimensional algebra over a field of characteristic zero is
> separable.

```lean
theorem isSeparable_cohomology_zero : Algebra.IsSeparable F A
```

**`Stacks.WeilCohomology.cycleClass_fundamental_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean, line 484](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean#L484). The attribute's comment: “part (5): γ([X]) = 1”.

> **Stacks Project, Tag 0FHQ, part (5).** The cycle class of the fundamental class of a
> nonempty smooth projective scheme over the base field is the unit of its cohomology algebra.
>
> The fundamental class of `X` is the pullback of the fundamental class of `Spec(k)` along the
> structure morphism (`hfundamental`); the cycle class map commutes with pullback by axiom
> `(C)(a)` (`hcompat`); the cycle class of the fundamental class of `Spec(k)` is the unit by
> Stacks 0FHE (`hpt`); and cohomological pullback preserves the unit (`hone`).

```lean
theorem cycleClass_fundamental_eq_one : cycleClass fundamental = 1
```

**`Stacks.WeilCohomology.integration_cycleClass_eq_degree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DimensionZero.lean#L519). The attribute's comment: “part (6): ∫_X γ([X]) = deg(X → Spec k)”.

> **Stacks Project, Tag 0FHQ, part (6).** Integration of the cycle class of the fundamental
> class of a smooth projective scheme of dimension zero over the base field is its degree over
> the base field.
>
> By part (5) that cycle class is the unit, by part (4) integration is the trace map, and the
> trace of the unit is the dimension of `H^0(X)` over the coefficient field, which is the degree
> by part (3).

```lean
theorem integration_cycleClass_eq_degree : integration (cycleClass fundamental) = (n : F)
```

Declarations registered for the tag:

- [`Stacks.WeilCohomology.WeilData.cycleClass_fundamentalClass`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassFundamental.lean#L142), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean, line 1075](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DimensionZero.lean#L1075) (StacksFrontier): “part (5): γ([X]) = 1, by 0FHF, for every smooth projective X”.

## Tag 0FHR, a lemma

[Tag 0FHR](https://stacks.math.columbia.edu/tag/0FHR) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.trace_cycleClass_eq_codimensionDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ZeroCycleTraceDegree.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ZeroCycleTraceDegree.lean#L252).

> **Stacks 0FHR.** Assume given data (D0)–(D3) satisfying (A), (B) and (C), and let `X` be a
> nonempty smooth projective scheme over `k`, equidimensional of dimension `d`. Then the diagram
> `CH^d(X) --γ--> H^{2d}(X)(d) --∫_X--> F`, `CH^d(X) = CH_0(X) --deg--> 𝐙 → F` commutes:
> `∫_X γ(β) = deg(β)` for every `β ∈ CH^d(X)`, where `deg` is the degree of zero cycles of Chow
> Homology, Section 0AZ0 (Stacks 0AZ1), on `CH^d(X) = CH_0(X)`
> (`Stacks.WeilCohomology.codimensionDegree`).

```lean
theorem trace_cycleClass_eq_codimensionDegree
    {X : (SmoothProjectiveScheme k).FullSubcategory} {d : ℕ}
    (hX : IsNonemptyEquidimensional X d) (β : codimensionChowGroup k X.obj.hom d) :
    W.trace X d hX (W.cycleClass X d β) = (codimensionDegree X d β : F)
```

## Tag 0FHS, a lemma

[Tag 0FHS](https://stacks.math.columbia.edu/tag/0FHS) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.finsum_negOnePow_finrank_eq_codimensionDegree_diag_mul_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/EulerCharacteristic.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/EulerCharacteristic.lean#L307). The attribute's comment: “the whole lemma: for (D0)-(D3) satisfying (A), (B), (C), F of characteristic 0, and X nonempty smooth projective over k, equidimensional of dimension d: the Euler characteristic ∑_i (-1)^i dim_F H^i(X) (over all i ∈ ℤ, of finite support) equals deg(Δ·Δ) for the intersection product of Tag 0FC0 of the class of the diagonal with itself in CH^{2d}(X × X), which equals deg(c_d(T_{X/k}) ∩ [X]) for the tangent sheaf T_{X/k} = Hom(Ω_{X/k}, O_X)”. References: SGA 7 XVI (2.1), “partial”.

> **Stacks 0FHS.** Assume given (D0), (D1), (D2) and (D3) satisfying (A), (B) and (C), with `F`
> of characteristic zero. Let `X` be a nonempty smooth projective scheme over `k`, equidimensional of
> dimension `d`. Then
>
>   `∑_i (-1)^i dim_F H^i(X) = deg(Δ · Δ) = deg(c_d(𝒯_{X/k}))`.
>
> Here the sum runs over all `i ∈ ℤ` and has finite support (the first conclusion);
> `Δ · Δ ∈ CH^{2d}(X × X)` is the intersection product of Stacks 0FC0
> (`Stacks.Chow.codimensionIntersectionProduct`) of the class `[Δ] ∈ CH^d(X × X)` of the diagonal
> with itself, and `deg : CH^{2d}(X × X) = CH_0(X × X) → ℤ` the degree of zero cycles
> (`Stacks.WeilCohomology.codimensionDegree`, Stacks 0AZ1); `c_d(𝒯_{X/k}) ∈ A^d(X)` is the `d`-th
> Chern class (Stacks 0ESW) of the tangent sheaf `𝒯_{X/k} = 𝓗om(Ω_{X/k}, 𝒪_X)`
> (`Stacks.WeilCohomology.SmoothProjectiveScheme.tangentSheaf`), and its degree is that of the
> zero cycle class `c_d(𝒯_{X/k}) ∩ [X]` (`Stacks.Chow.zeroDegree`).
>
> The proof is the source's. On the right, `[Δ] · [Δ] = Δ_*(Δ^![Δ])` (Stacks 0FFE), `Δ_*` preserves
> degrees, and `Δ^![Δ] = c_d(𝒩) ∩ [X]` for the normal sheaf `𝒩 = 𝒞_{Δ}^∨ = 𝒯_{X/k}` (Stacks 0FV9,
> the excess intersection formula for the Gysin map, with the conormal sheaf of the diagonal
> `Ω_{X/k}` by Stacks 08S2): `codimensionDegree_diag_mul_diag` and
> `zeroDegree_regularImmersionGysin_diag`. On the left, `deg([Δ] · [Δ]) = ∫_{X × X} γ([Δ]) ∪ γ([Δ])`
> by Stacks 0FHR and (C)(c), `= ∫_X Δ^*γ([Δ])` since `γ([Δ]) = Δ_*1` (Stacks 0FHG, 0FHB), and writing
> `γ([Δ]) = ∑ e_{i,j} ⊗ e'_{2d-i,j}` (Stacks 0FHH) and using Remark 0FHD this is
> `∑_{i,j} ∫_X e_{i,j} ∪ e'_{2d-i,j} = ∑_i (-1)^i dim_F H^i(X)`.

```lean
theorem finsum_negOnePow_finrank_eq_codimensionDegree_diag_mul_diag :
    (Function.support fun i : ℤ ↦ (i.negOnePow : ℤ) * (Module.finrank F (W.grade X i) : ℤ)).Finite ∧
    (∑ᶠ i : ℤ, (i.negOnePow : ℤ) * (Module.finrank F (W.grade X i) : ℤ)) =
      codimensionDegree (prod X X) (d + d)
        (codimensionIntersectionProduct k (prod X X).obj.hom d d
          (closedSubschemeClass (prod X X).obj.hom (diag X).hom.left d)
          (closedSubschemeClass (prod X X).obj.hom (diag X).hom.left d)) ∧
    codimensionDegree (prod X X) (d + d)
        (codimensionIntersectionProduct k (prod X X).obj.hom d d
          (closedSubschemeClass (prod X X).obj.hom (diag X).hom.left d)
          (closedSubschemeClass (prod X X).obj.hom (diag X).hom.left d)) =
      zeroDegree k X.obj.hom (sub_self _)
        (chowCohomologyCap (fieldChowSituation k) (gysinSystemOfInvertible _) X.obj.hom d
          (totalChernOfFiniteLocallyFree (fieldChowSituation k) X.obj.hom (tangentSheaf X) d) d
          (fundamentalChowClass (fieldChowSituation k) X.obj.hom d))
```

## Tag 0FHT, a lemma

[Tag 0FHT](https://stacks.math.columbia.edu/tag/0FHT) in the Stacks Project.

**`AlgHom.exists_algEquiv_comp_eq_of_trace_sub_trace_eq_zsmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/Basic.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/Basic.lean#L458). The attribute's comment: “as printed the tag concludes σ = σ' from surjectivity of σ and σ' alone; `Stacks.WeilCohomology.not_traceRelationStatement` refutes that with F = ℝ, F' = A = ℂ, σ = id and σ' = complex conjugation. This declaration is the corrected statement, under the source's own hypotheses: σ' = θ ∘ σ for an F-algebra automorphism θ of F', equivalently Tr ∘ σ = Tr ∘ σ' together with ker σ = ker σ'”.

> **Stacks Project, Tag 0FHT**, in the corrected form recorded as a Stacks erratum.
>
> Over a field `F` of characteristic zero, let `σ, σ' : A → F'` be surjections from a finite
> `F`-algebra onto a finite separable `F`-algebra, and let `σ i : A → F i` be `F`-algebra maps to
> finite separable `F`-algebras. If
>
> ```
> Tr_{F'/F} ∘ σ - Tr_{F'/F} ∘ σ' = n (∑ m i * Tr_{F i/F} ∘ σ i)
> ```
>
> with `n > 1` and the `m i` integers, then `σ' = θ ∘ σ` for an `F`-algebra automorphism `θ` of
> `F'`; equivalently `Tr_{F'/F} ∘ σ = Tr_{F'/F} ∘ σ'` and `ker σ = ker σ'`.
>
> As printed, the tag concludes `σ = σ'`. That conclusion is refuted by
> `Stacks.WeilCohomology.not_traceRelationStatement`, which takes `F = ℝ`, `F' = A = ℂ`,
> `σ = id` and `σ' = ` complex conjugation. An automorphism of `F'` is invisible to the trace
> relation, and the displayed conclusion is exactly what the relation does see.

```lean
theorem AlgHom.exists_algEquiv_comp_eq_of_trace_sub_trace_eq_zsmul
    (F : Type u) [Field F] [CharZero F]
    (F' : Type v) [CommRing F'] [Algebra F F'] [FiniteDimensional F F']
    [Algebra.IsSeparable F F']
    (A : Type w) [CommRing A] [Algebra F A] [FiniteDimensional F A]
    {r : ℕ} (F_i : Fin r → Type x)
    [∀ i, CommRing (F_i i)] [∀ i, Algebra F (F_i i)]
    [∀ i, FiniteDimensional F (F_i i)] [∀ i, Algebra.IsSeparable F (F_i i)]
    (σ σ' : A →ₐ[F] F') (σ_i : ∀ i, A →ₐ[F] F_i i)
    (hσ : Function.Surjective σ) (hσ' : Function.Surjective σ')
    (n : ℤ) (hn : 1 < n) (m : Fin r → ℤ)
    (hrel :
      (Algebra.trace F F').comp σ.toLinearMap -
          (Algebra.trace F F').comp σ'.toLinearMap =
        n • ∑ i, m i • (Algebra.trace F (F_i i)).comp (σ_i i).toLinearMap) :
    (∃ θ : F' ≃ₐ[F] F', σ' = (θ : F' →ₐ[F] F').comp σ) ∧
      (Algebra.trace F F').comp σ.toLinearMap =
        (Algebra.trace F F').comp σ'.toLinearMap ∧
      RingHom.ker σ.toRingHom = RingHom.ker σ'.toRingHom
```

## Tag 0FHU, a lemma

[Tag 0FHU](https://stacks.math.columbia.edu/tag/0FHU) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.rationalPointChowClass_sub_ne_zsmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RationalPointIndivisibility.lean, line 1165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RationalPointIndivisibility.lean#L1165). The attribute's comment: “for X smooth projective over a finite separable k'/k, viewed over k, with the actual CH_0(X) over k', the data (D0)-(D3) and axioms (A), (B), (C) over the actual category of smooth projective k-schemes; γ(x) is the family of the classes γ([x]) in every codimension”.

> **Stacks Project, Tag 0FHU.** Assume given (D0), (D1), (D2) and (D3) satisfying (A), (B) and
> (C). Let `k'/k` be a finite separable extension, let `X` be a smooth projective scheme over `k'`
> and let `x, x' ∈ X` be `k'`-rational points. If `γ(x) ≠ γ(x')`, then `[x] - [x']` is not
> divisible by any integer `n > 1` in `CH_0(X)`.
>
> Here `X` is a scheme with a smooth projective structure morphism `p : X ⟶ Spec k'`, and it is a
> smooth projective scheme over `k` through `Spec k' ⟶ Spec k` (`ofOverField p hp`), which is how
> the data (D0)–(D3) over `k` apply to it. The points are sections `x, x'` of `p`;
> `[x], [x'] ∈ CH_0(X)` are their classes in the Chow group of `X` over `k'`
> (`rationalPointChowClass`), and the divisibility is in that group. `γ(x)` is the family of the
> cohomology classes `γ([x]) ∈ H^{2i}(X)(i)` of the class `[x] ∈ CH^i(X)` of the closed subscheme
> `x` in every codimension `i` (`rationalPointClass`): on the part of `X` of dimension `d`
> containing `x` this is `γ([x]) ∈ H^{2d}(X)(d)`, the other entries vanishing.
>
> The proof is the source's. If `x` and `x'` lie in different parts of `X` of constant dimension,
> the degree on the part containing `x` separates them. Otherwise, on that part `X_d`, Stacks 0FH5
> writes the class of every zero cycle as an integral combination of classes of closed points with
> separable residue field, Stacks 0FHG and Stacks 0FHQ identify `a ↦ ∫ a ∪ γ([y])` on `H^0(X_d)`
> with `Tr_{H^0(y)/F} ∘ i_y^*`, Poincaré duality (A)(b) turns the divisibility into the trace
> relation of Stacks 0FHT, which forces `i_x^* = i_{x'}^*`, whence `γ([x]) = γ([x'])` on `X_d`; and
> by (C)(a), the Gysin map of an open immersion being restriction, and Stacks 0FHJ for
> `X = X_d ⨿ (X ∖ X_d)`, `γ(x) = γ(x')` on `X`.

```lean
theorem rationalPointChowClass_sub_ne_zsmul [CharZero F] (hA : W.PoincareDuality)
    (hB : W.Kunneth) (hC : W.CycleClassAxiom hA.perfectPairing) {X : Scheme.{u}}
    (p : X ⟶ (fieldChowSituation k').S) [Smooth p] (hp : IsProjectiveMorphism p)
    (x x' : (fieldChowSituation k').S ⟶ X) (hx : x ≫ p = 𝟙 _) (hx' : x' ≫ p = 𝟙 _)
    (hne : (fun i : ℤ ↦ W.cycleClass (ofOverField p hp) i (rationalPointClass p hp x hx i)) ≠
      fun i : ℤ ↦ W.cycleClass (ofOverField p hp) i (rationalPointClass p hp x' hx' i))
    (n : ℤ) (hn : 1 < n) (c : chowGroup (fieldChowSituation k') p 0) :
    rationalPointChowClass k' p x hx - rationalPointChowClass k' p x' hx' ≠ n • c
```

**`Stacks.WeilCohomology.rationalPointChowClass_sub_ne_zsmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/RationalPoints.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/RationalPoints.lean#L183). The attribute's comment: “(D0)-(D3), (A)-(C) as explicit arguments is the source's own hypothesis and this directory's convention, not a restriction; but `hsep` (Stacks 0FH5, not proved here) and `htrace`, `htrace'` (∫_X a ∪ γ([x]) = trace of i^*a, via 0FHG, 0FHB, 0FHQ(4)) are carried rather than derived, as is the reduction to irreducible `X`. Generalizations: no smoothness or projectivity on `p`; only `pair.flip` injectivity is used of (A)(b)”.

> **Stacks Project, Tag 0FHU.** Let `H^*` be a Weil cohomology theory with coefficient field
> `F` of characteristic zero, let `k'/k` be a finite separable extension and let `X` be a smooth
> projective scheme over `k'`. If `x` and `x'` are `k'`-rational points of `X` with
> `γ([x]) ≠ γ([x'])`, then `[x] - [x']` is not divisible by any integer `n > 1` in `CH_0(X)`.
>
> The cohomological data and the axioms it satisfies are the explicit arguments: `[pair.IsPerfPair]`
> is axiom `(A)(b)` for `X`, `cycleClass` is the cycle class map `γ` of `(D2)`, the instances on
> `F' = H^0(Spec k')` are Stacks 0FHQ for `Spec k'` and are where separability of `k'/k` enters,
> `hsplit` and `hsplit'` are functoriality of `(D1)` along `x ≫ p = id` and `x' ≫ p = id`,
> `htrace` and `htrace'` identify `∫_X a ∪ γ([x])` with the trace of `i^*a` by Stacks 0FHG, the
> projection formula and Stacks 0FHQ part (4), and `hsep` is Stacks 0FH5 with those same inputs
> applied to the separable closed points it produces.
>
> ## What is assumed and what is proved
>
> Presenting `(D0)`-`(D3)` and `(A)`-`(C)` as explicit arguments is not a restriction: "assume
> given `(D0)`-`(D3)` satisfying `(A)`, `(B)`, `(C)`" is the source's own hypothesis, and the
> explicit-argument presentation is this directory's convention for it.
>
> What *is* a restriction is that three further inputs are assumed rather than derived, where the
> source derives them from those axioms, because this library does not have them.
>
> * `hsep` is Stacks 0FH5, which is not proved in this library; it is a lemma of the chapter,
>   not axiom data.
> * `htrace` and `htrace'` are the identification of `∫_X a ∪ γ([x])` with the trace of `i^*a`,
>   which needs Stacks 0FHG, the projection formula of Stacks 0FHB and Stacks 0FHQ part (4) glued
>   together on schemes.
> * The reduction to `X` irreducible of dimension `d` is absorbed into the single group `T`.
>
> So the theorem is weaker than "the axioms imply the conclusion", and the attribute records that.
> Two departures go the other way and are genuine generalizations: no smoothness or projectivity
> is imposed on `p`, since those enter only through the pairing, the cycle class map and the trace
> identities, all of which are hypotheses here; and of axiom `(A)(b)` only injectivity of
> `pair.flip` is consumed.

```lean
theorem rationalPointChowClass_sub_ne_zsmul
    {k' : Type u} [Field k'] {X : Scheme.{u}}
    (p : X ⟶ (Stacks.Chow.fieldChowSituation k').S) [LocallyOfFiniteType p]
    (x x' : (Stacks.Chow.fieldChowSituation k').S ⟶ X)
    (hx : x ≫ p = 𝟙 (Stacks.Chow.fieldChowSituation k').S)
    (hx' : x' ≫ p = 𝟙 (Stacks.Chow.fieldChowSituation k').S)
    (F : Type v) [Field F] [CharZero F]
    (F' : Type w) [CommRing F'] [Algebra F F'] [FiniteDimensional F F']
    [Algebra.IsSeparable F F']
    (A : Type x) [CommRing A] [Algebra F A] [FiniteDimensional F A]
    (T : Type y) [AddCommGroup T] [Module F T]
    (pair : A →ₗ[F] T →ₗ[F] F) [pair.IsPerfPair]
    (cycleClass : Stacks.Chow.chowGroup (Stacks.Chow.fieldChowSituation k') p 0 →+ T)
    (pullback pullback' : A →ₐ[F] F') (structurePullback : F' →ₐ[F] A)
    (hsplit : pullback.comp structurePullback = AlgHom.id F F')
    (hsplit' : pullback'.comp structurePullback = AlgHom.id F F')
    (htrace : ∀ a : A, pair a (cycleClass (rationalPointChowClass k' p x hx)) =
      Algebra.trace F F' (pullback a))
    (htrace' : ∀ a : A, pair a (cycleClass (rationalPointChowClass k' p x' hx')) =
      Algebra.trace F F' (pullback' a))
    (hsep : ∀ c : Stacks.Chow.chowGroup (Stacks.Chow.fieldChowSituation k') p 0,
      IsSeparableTraceCombination.{v, x, z} F A (pair.flip (cycleClass c)))
    (hne : cycleClass (rationalPointChowClass k' p x hx) ≠
      cycleClass (rationalPointChowClass k' p x' hx'))
    (n : ℤ) (hn : 1 < n)
    (c : Stacks.Chow.chowGroup (Stacks.Chow.fieldChowSituation k') p 0) :
    rationalPointChowClass k' p x hx - rationalPointChowClass k' p x' hx' ≠ n • c
```

## Tag 0FHV, a lemma

[Tag 0FHV](https://stacks.math.columbia.edu/tag/0FHV) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.exists_cycleClass_comp_eq_comp_chowDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/PointClassDegree.lean, line 553](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/PointClassDegree.lean#L553). The attribute's comment: “for X smooth projective and geometrically irreducible over a finite separable k'/k, viewed over k, with the actual CH_0(X) over k' and its degree, the data (D0)-(D3) and axioms (A), (B), (C) over the actual category of smooth projective k-schemes”.

> **Stacks Project, Tag 0FHV.** Assume given (D0), (D1), (D2) and (D3) satisfying (A), (B) and
> (C). Let `k'/k` be a finite separable extension and let `X` be a geometrically irreducible smooth
> projective scheme over `k'` of dimension `d`. Then `γ : CH_0(X) → H^{2d}(X)(d)` factors through
> `deg : CH_0(X) → 𝐙`.
>
> Here `X` is a scheme with a smooth projective, geometrically irreducible structure morphism
> `p : X ⟶ Spec k'`, viewed over `k` through `Spec k' ⟶ Spec k` (`ofOverField p hp`), which is how
> the data over `k` apply to it; "of dimension `d`" is `topologicalKrullDim X = d`. `CH_0(X)` is
> the Chow group of zero cycles of `X` over `k'` and `deg` its degree (Stacks 0AZ1,
> `Stacks.Chow.chowDegree`, read at the point `s` of `Spec k'`); `γ` is the cycle class map
> `CH^d(X) → H^{2d}(X)(d)` of (D2) composed with `CH_0(X) = CH^d(X)`
> (`zeroCycleToCodimensionOfExtension`).
>
> The proof is the source's. By Stacks 0FH5 `CH_0(X)` is generated by the classes of closed points
> with separable residue field, and for two such points
> `deg(x') γ([x]) = deg(x) γ([x'])` (`WeilData.residueDegree_smul_cycleClass_closedPointClass`):
> over a finite separable extension into which both residue fields embed this comes from the
> rational-point step (Stacks 0FH7, Stacks 0FHU, (C)(b)) and (C)(b) along `X_K ⟶ X`.

```lean
theorem exists_cycleClass_comp_eq_comp_chowDegree [CharZero F]
    (hA : W.PoincareDuality) (hB : W.Kunneth) (hC : W.CycleClassAxiom hA.perfectPairing)
    {X : Scheme.{u}} (p : X ⟶ (fieldChowSituation k').S) [Smooth p] [GeometricallyIrreducible p]
    (hp : IsProjectiveMorphism p) {d : ℕ} (hd : topologicalKrullDim X = d)
    (s : (fieldChowSituation k').S) :
    haveI := isProper_of_isProjectiveMorphism p hp
    haveI : LocallyOfFiniteType
        (show (ofOverField (k := k) p hp).obj.left ⟶ (fieldChowSituation k').S from p) :=
      inferInstanceAs (LocallyOfFiniteType p)
    ∃ φ : ℤ →+ W.Tw (ofOverField p hp) (2 * d) d,
      (W.cycleClass (ofOverField p hp) d).comp
          (zeroCycleToCodimensionOfExtension (ofOverField p hp) p rfl d) =
        φ.comp (chowDegree (fieldChowSituation k') (fieldChowSituation_dimensionFunction k') p
          s)
```

## Tag 0FHW, a lemma

[Tag 0FHW](https://stacks.math.columbia.edu/tag/0FHW) in the Stacks Project.

**`Stacks.WeilCohomology.injective_pullback_of_isDominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DominantPullback.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/DominantPullback.lean#L171).

> **Stacks Project, Tag 0FHW.** Let `f : X ⟶ Y` be a dominant morphism of irreducible smooth
> projective schemes over a field `k`, and let `H^*` be a Weil cohomology theory over `k` with
> coefficients in a field `F` of characteristic zero. Then `f^* : H^i(Y) ⟶ H^i(X)` is injective.
>
> The cohomological data and the axioms the proof uses are the explicit arguments: the data and
> axioms at the base point `Spec(k)`, the trace maps `∫_X`, `∫_Y` and the cup products of `(D1)`
> and `(D3)` with associativity, the unit law and multiplicativity of `f^*`, perfectness of the
> trace pairings of `Y` (axiom (A)), axiom (C)(a) for the structure morphism of `Y` and axiom
> (C)(b) for `f`. The identity `γ([Y]) = 1` of Stacks 0FHF and the projection formula of Stacks
> 0FHB are derived from these, not assumed.

```lean
theorem injective_pullback_of_isDominant {k : Type u} [Field k] {F : Type*} [Field F]
    [CharZero F]
    (Hpt : ℤ → Type x) [∀ i : ℤ, AddCommGroup (Hpt i)] [∀ i : ℤ, Module F (Hpt i)]
    [∀ i : ℤ, FiniteDimensional F (Hpt i)]
    (HptZero : Type x) [CommRing HptZero] [Algebra F HptZero]
    (degreeZeroPoint : Hpt 0 ≃ₗ[F] HptZero)
    (kunnethPoint : ∀ n : ℤ,
      DirectSum ℤ (fun j : ℤ ↦ TensorProduct F (Hpt j) (Hpt (n - j))) ≃ₗ[F] Hpt n)
    (cycleClassPoint : chowGroup (fieldChowSituation k) (𝟙 _) 0 →+ HptZero)
    (integrationPoint : HptZero →ₗ[F] F)
    (integration_cycleClassPoint : integrationPoint
      (cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0)) = 1)
    (cycleClassPoint_mul :
      cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0) *
          cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0) =
        cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0))
    {X Y : Scheme.{u}} (sX : X ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ (fieldChowSituation k).S) [Smooth sY] [IrreducibleSpace Y]
    (e : ℕ) (hd : AlgebraicGeometry.RelativeDimension sY e)
    (f : X ⟶ Y) [IsProper f] [IsDominant f] (hf : f ≫ sY = sX)
    {BX BY DXtop DYtop HXtop HYtop TopX TopY HX' HY' DX' : Type*}
    [AddCommGroup BX] [Module F BX] [AddCommGroup BY] [Module F BY]
    [AddCommGroup DXtop] [Module F DXtop] [AddCommGroup DYtop] [Module F DYtop]
    [AddCommGroup HXtop] [Module F HXtop] [AddCommGroup HYtop] [Module F HYtop]
    [AddCommGroup TopX] [Module F TopX] [AddCommGroup TopY] [Module F TopY]
    [AddCommGroup HX'] [Module F HX'] [AddCommGroup HY'] [Module F HY']
    [AddCommGroup DX'] [Module F DX']
    (integralX : TopX →ₗ[F] F) (integralY : TopY →ₗ[F] F)
    (cupTopX : HXtop →ₗ[F] DXtop →ₗ[F] TopX) (cupTopY : HYtop →ₗ[F] DYtop →ₗ[F] TopY)
    (cupX' : HX' →ₗ[F] DX' →ₗ[F] TopX) (cupY' : HY' →ₗ[F] BY →ₗ[F] TopY)
    [(cupTopY.compr₂ integralY).IsPerfPair] [(cupY'.compr₂ integralY).IsPerfPair]
    (cupX : BX →ₗ[F] DXtop →ₗ[F] DX') (cupY : BY →ₗ[F] DYtop →ₗ[F] BY)
    (cupLeftX : HX' →ₗ[F] BX →ₗ[F] HXtop) (cupLeftY : HY' →ₗ[F] BY →ₗ[F] HYtop)
    (one : DYtop)
    (cup_assoc_X : ∀ c b a, cupX' c (cupX b a) = cupTopX (cupLeftX c b) a)
    (cup_assoc_Y : ∀ c b a, cupY' c (cupY b a) = cupTopY (cupLeftY c b) a)
    (cupY_one : ∀ b, cupY b one = b)
    (pullbackB : BY →ₗ[F] BX) (pullbackTop : HYtop →ₗ[F] HXtop) (pullback' : HY' →ₗ[F] HX')
    (pullback_cup : ∀ c b, pullbackTop (cupLeftY c b) = cupLeftX (pullback' c) (pullbackB b))
    (pullbackPt : HptZero →ₗ[F] DYtop) (pullbackPt_one : pullbackPt 1 = one)
    (cycleClassX : chowGroup (fieldChowSituation k) sX (0 + (e : ℤ)) →+ DXtop)
    (cycleClassY : chowGroup (fieldChowSituation k) sY (0 + (e : ℤ)) →+ DYtop)
    (cycleClass_pullback : ∀ α,
      cycleClassY (flatPullbackChowOfRelativeDimension (fieldChowSituation k) sY (𝟙 _) sY
          (Category.comp_id sY) e hd 0 α) =
        pullbackPt (cycleClassPoint α))
    (cycleClass_pushforward : ∀ α,
      cycleClassY (properChowPushforward (fieldChowSituation k) sX sY f hf (0 + (e : ℤ))
          (properPushforwardFactorsThroughRationalEquivalence_of_isProper (fieldChowSituation k)
            sX sY f hf (0 + (e : ℤ))) α) =
        poincareDualPushforward (cupTopX.compr₂ integralX) (cupTopY.compr₂ integralY)
          pullbackTop (cycleClassX α)) :
    Function.Injective pullbackB
```

## Tag 0FHX, a lemma

[Tag 0FHX](https://stacks.math.columbia.edu/tag/0FHX) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.bijective_scalarExtensionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ScalarExtension.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ScalarExtension.lean#L692). The attribute's comment: “H^*(X) ⊗_{H^0(Spec k')} H^0(Spec k'') = H^*(X ×_{Spec k'} Spec k'') for the actual Weil data, X smooth projective over k', k''/k'/k finite separable”.

> **Stacks Project, Tag 0FHX.** Assume given `(D0)`–`(D3)` satisfying `(A)`, `(B)` and `(C)`.
> Let `k''/k'/k` be finite separable algebras and let `X` be a smooth projective scheme over `k'`.
> Then the comparison map
>
> `H^*(X) ⊗_{H^0(Spec k')} H^0(Spec k'') ⟶ H^*(X ×_{Spec k'} Spec k'')`,
> `a ⊗ b ↦ pr₁^*a ∪ pr₂^*b`,
>
> is bijective. Here `H^*(X)` is an `H^0(Spec k')`-algebra by pullback along `X ⟶ Spec k'`, and
> `X` and `X ×_{Spec k'} Spec k''` are smooth projective schemes over `k`.

```lean
theorem bijective_scalarExtensionMap [CharZero F] (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) :
    Function.Bijective (W.scalarExtensionMap π hπ (k'' := k''))
```

**`Stacks.WeilCohomology.WeilData.scalarExtensionAlgEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ScalarExtension.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ScalarExtension.lean#L703). The attribute's comment: “the H^0(Spec k')-algebra isomorphism H^*(X) ⊗_{H^0(Spec k')} H^0(Spec k'') ≃ H^*(X ×_{Spec k'} Spec k'') for the actual Weil data”.

> **Stacks Project, Tag 0FHX**, as an isomorphism of `H^0(Spec k')`-algebras:
> `H^*(X) ⊗_{H^0(Spec k')} H^0(Spec k'') ≃ H^*(X ×_{Spec k'} Spec k'')`,
> `a ⊗ b ↦ pr₁^*a ∪ pr₂^*b`.

```lean
def scalarExtensionAlgEquiv [CharZero F] (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) :
    W.H (ofOver k π hπ) ⊗[W.H0 (spec k k')] W.H0 (spec k k'') ≃ₐ[W.H0 (spec k k')]
      W.H (baseChangeObj k π hπ (k'' := k''))
```

**`Stacks.WeilCohomology.bijective_scalarExtensionHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/ScalarExtension.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/ScalarExtension.lean#L225). The attribute's comment: “the comparison map is bijective”.

> **Stacks Project, Tag 0FHX.** Let `k''/k'/k` be finite separable algebras and let `X` be a
> smooth projective scheme over `k'`. Then the canonical map
>
> `H^*(X) ⊗_{H^0(Spec k')} H^0(Spec k'') ⟶ H^*(X ×_{Spec k'} Spec k'')`
>
> is bijective.
>
> Write `k' ⊗_k k'' = k'' × l` and `G = H^0(Spec l)`. Künneth together with additivity on a
> disjoint union, Stacks 0FHJ, decomposes `H^0(Spec k') ⊗_F H^0(Spec k'')` as `H^0(Spec k'') × G`
> with first projection the multiplication map, and decomposes `H^*(X) ⊗_F H^0(Spec k'')` as
> `H^*(X ×_{Spec k'} Spec k'') × H^*(X ×_{Spec k'} Spec l)` compatibly. The idempotent of the
> first decomposition corresponding to `(0, 1)` then identifies the two kernels.

```lean
theorem bijective_scalarExtensionHom (fM : M →ₐ[A] N₁)
    (kunneth : M ⊗[F] B ≃ₐ[F] N₁ × N₂)
    (kunneth_tmul : ∀ (m : M) (b : B),
      (kunneth (m ⊗ₜ[F] b)).1 = fM m * algebraMap B N₁ b)
    (split : A ⊗[F] B ≃ₐ[F] B × G)
    (split_fst : ∀ z : A ⊗[F] B, (split z).1 = tensorMulHom F A B z)
    (kunneth_split : ∀ z : A ⊗[F] B,
      kunneth (tensorActionHom F A B M z) =
        (algebraMap B N₁ (split z).1, algebraMap G N₂ (split z).2)) :
    Function.Bijective (scalarExtensionHom (B := B) fM)
```

**`Stacks.WeilCohomology.scalarExtensionEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/ScalarExtension.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/FurtherProperties/ScalarExtension.lean#L247). The attribute's comment: “the scalar extension isomorphism”.

> **Stacks Project, Tag 0FHX.** The scalar extension isomorphism
>
> `H^*(X) ⊗_{H^0(Spec k')} H^0(Spec k'') ≃ H^*(X ×_{Spec k'} Spec k'')`
>
> for `k''/k'/k` finite separable algebras and `X` smooth projective over `k'`, given by
> `a ⊗ b ↦ pr₁^*a ∪ pr₂^*b`.

```lean
noncomputable def scalarExtensionEquiv (fM : M →ₐ[A] N₁)
    (kunneth : M ⊗[F] B ≃ₐ[F] N₁ × N₂)
    (kunneth_tmul : ∀ (m : M) (b : B),
      (kunneth (m ⊗ₜ[F] b)).1 = fM m * algebraMap B N₁ b)
    (split : A ⊗[F] B ≃ₐ[F] B × G)
    (split_fst : ∀ z : A ⊗[F] B, (split z).1 = tensorMulHom F A B z)
    (kunneth_split : ∀ z : A ⊗[F] B,
      kunneth (tensorActionHom F A B M z) =
        (algebraMap B N₁ (split z).1, algebraMap G N₂ (split z).2)) :
    M ⊗[A] B ≃ₐ[A] N₁
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.10, Tag 0FHN](https://stacks.math.columbia.edu/tag/0FHN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
