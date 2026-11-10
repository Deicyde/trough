---
declaration: section
origin: cited
lean: Stacks.WeilDeRham.exists_weilCohomologyTheory_deRham, Stacks.HodgeWeil.exists_weilCohomologyTheory_hodge, Stacks.HodgeWeil.degeneratesAt_one_of_finrank_grade_eq
statement: formalized
proof: formalized
---

# 50.22 A Weil cohomology theory

Section 50.22 of the Stacks Project, [Tag 0FWC](https://stacks.math.columbia.edu/tag/0FWC). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FWD, a proposition

[Tag 0FWD](https://stacks.math.columbia.edu/tag/0FWD) in the Stacks Project.

**`Stacks.WeilDeRham.exists_weilCohomologyTheory_deRham`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilDeRham/DeRhamWeilCohomologyTheory.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilDeRham/DeRhamWeilCohomologyTheory.lean#L84). The attribute's comment: “de Rham cohomology over a field of characteristic zero is a Weil cohomology theory (Definition 0FI2, coefficients k), with data (D0)-(D3) those of de Rham cohomology: F(1) = k, H^* = H^*\_dR(-/k) with cup product and pullbacks, gamma from c\_1^dR (0FIF), trace lambda of (A6)”.

> **Stacks Project, Proposition 0FWD**: for a field `k` of characteristic zero, the functor
> `X ↦ H^*_{dR}(X/k)` on smooth projective schemes over `k` is a Weil cohomology theory over `k`
> with coefficients in `k` (Definition 0FI2).
>
> Formulation: there is a Weil cohomology theory `W : WeilCohomologyTheory k k` (Definition 0FI2:
> data (D0) – (D3) satisfying (A), (B), (C) and condition (2) of Lemma 0FI0) whose data (D0) – (D3)
> are those of de Rham cohomology. These are `h.toWeilData …` for `h` a cohomological Chern
> character (Tag 0FIE) of the de Rham data `deRhamFirstChernClassData k` of Section 0FWC, so that
> * (D0) `F(1)` is `k`;
> * (D1) `H^*(X)` is `H^*_{dR}(X/k)`, with its grading, cup product and pullbacks
>   (`W.H`, `W.grade`, the ring structure and `W.pull` are those of `deRhamFirstChernClassData k`);
> * (D2) the cycle class map `γ` is the one of Lemma 0FIF built from the de Rham first Chern class
>   `c₁^{dR}` (the Chern character `ch` is determined by `c₁^{dR}`,
>   `FirstChernClassData.existsUnique_isCohomologicalChernCharacter`);
> * (D3) `∫_X` is the trace map `λ_X` of axiom (A6), normalised by `(1 ⊗ λ_X)γ([Δ]) = 1`.
>
> The proof assembles axioms (A1) – (A8) for de Rham cohomology and applies Proposition 0FIU.

```lean
theorem exists_weilCohomologyTheory_deRham [CharZero k] :
    ∃ W : WeilCohomologyTheory k k, ∃ ch,
      ∃ h : (deRhamFirstChernClassData k).IsCohomologicalChernCharacter ch,
        W.toWeilData = h.toWeilData coproductAxiom deRham_projectiveBundleAxiom
          (deRham_kunnethAxiom k) (deRham_traceAxiom h)
```

## Tag 0FWE, a remark

[Tag 0FWE](https://stacks.math.columbia.edu/tag/0FWE) in the Stacks Project.

**`Stacks.HodgeWeil.exists_weilCohomologyTheory_hodge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeWeil/HodgeWeilCohomologyTheory.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeWeil/HodgeWeilCohomologyTheory.lean#L218). The attribute's comment: “part 1 (the first sentence): for k of characteristic zero, Hodge cohomology H^*\_Hodge(-/k) with c\_1^Hodge is a Weil cohomology theory (Definition 0FI2, coefficients k), with data (D0)-(D3) those of Hodge cohomology: F(1) = k, H^* = H^*\_Hodge(-/k) with cup product and pullbacks, gamma from c\_1^Hodge (0FIF), trace lambda of (A6). Part 2 (the consequence) is degeneratesAt\_one\_of\_finrank\_grade\_eq”.

> **Stacks Project, Remark 0FWE, part 1**: for a field `k` of characteristic zero, Hodge
> cohomology `X ↦ H^*_{Hodge}(X/k) = ⨁_{p, q} H^q(X, Ω^p_{X/k})` on smooth projective schemes over
> `k`, equipped with `c₁^{Hodge}`, determines a Weil cohomology theory over `k` with coefficients in
> `k` (Definition 0FI2).
>
> Formulation, as for de Rham cohomology (Proposition 0FWD,
> `Stacks.WeilDeRham.exists_weilCohomologyTheory_deRham`): there is a Weil cohomology theory
> `W : WeilCohomologyTheory k k` (data (D0) – (D3) satisfying (A), (B), (C) and condition (2) of
> Lemma 0FI0) whose data are `h.toWeilData …` for a cohomological Chern character `h` (Tag 0FIE) of
> the Hodge data `hodgeFirstChernClassData k`, so that
> * (D0) `F(1)` is `k`;
> * (D1) `H^*(X)` is `H^*_{Hodge}(X/k)` graded by total degree, with its cup product and pullbacks;
> * (D2) the cycle class map `γ` is the one of Lemma 0FIF built from `c₁^{Hodge}` (the Chern
>   character is determined by `c₁^{Hodge}`,
>   `FirstChernClassData.existsUnique_isCohomologicalChernCharacter`);
> * (D3) `∫_X` is the trace map `λ_X` of axiom (A6), normalised by `(1 ⊗ λ_X)γ([Δ]) = 1`.
>
> The proof is the one of Proposition 0FWD: (A1) – (A8) for the Hodge data and Proposition 0FIU.

```lean
theorem exists_weilCohomologyTheory_hodge [CharZero k] :
    ∃ W : WeilCohomologyTheory k k, ∃ ch,
      ∃ h : (hodgeFirstChernClassData k).IsCohomologicalChernCharacter ch,
        W.toWeilData = h.toWeilData (hodge_coproductAxiom k) (hodge_projectiveBundleAxiom k)
          (hodge_kunnethAxiom k) (hodge_traceAxiom k h)
```

**`Stacks.HodgeWeil.degeneratesAt_one_of_finrank_grade_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/HodgeWeil/HodgeWeilCohomologyTheory.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/HodgeWeil/HodgeWeilCohomologyTheory.lean#L260). The attribute's comment: “part 2 (the amusing consequence): over k of characteristic zero, if the betti numbers dim\_F H^n(X) of Weil cohomology theories (any coefficient fields F of characteristic zero) do not depend on the theory, then for every smooth projective X over k the Hodge-to-de Rham spectral sequence (every brutal-truncation spectral sequence of the de Rham complex abutting to H^*\_dR(X/k), 0FM7) degenerates at E\_1. Part 1 is exists\_weilCohomologyTheory\_hodge”.

> **Stacks Project, Remark 0FWE, part 2** (the "amusing consequence"): let `k` be a field of
> characteristic zero. If the betti numbers of a Weil cohomology theory over `k` are independent of
> the chosen Weil cohomology theory, then the Hodge-to-de Rham spectral sequence degenerates at
> `E_1`.
>
> Formulation: the hypothesis `hbetti` says that for any two Weil cohomology theories `W`, `W'` over
> `k` (Definition 0FI2), with coefficients in fields `F`, `F'` of characteristic zero,
> `dim_F H^n_W(X) = dim_{F'} H^n_{W'}(X)` for every smooth projective `X` over `k` and every `n`.
> The conclusion is that for every smooth projective `X` over `k`, every Hodge-to-de Rham spectral
> sequence `E_1^{p, q} = H^q(X, Ω^p_{X/k}) ⟹ H^{p + q}_{dR}(X/k)` of `X` (a brutal-truncation
> spectral sequence of `Ω^•_{X/k}` abutting to `H^*_{dR}(X/k)`, which exists by Tag 0FM7)
> degenerates at `E_1`.
>
> The proof: by part 1 (`exists_weilCohomologyTheory_hodge`) and Proposition 0FWD
> (`Stacks.WeilDeRham.exists_weilCohomologyTheory_deRham`), Hodge and de Rham cohomology are Weil
> cohomology theories with coefficients in `k`, so `hbetti` gives
> `dim_k H^n_{Hodge}(X/k) = dim_k H^n_{dR}(X/k)`; as the Hodge groups are finite dimensional this
> is `E_1`-degeneration (`degeneratesAt_one_of_finrank_hodgeGradeOf_eq`).

```lean
theorem degeneratesAt_one_of_finrank_grade_eq [CharZero k]
    (hbetti : ∀ (F F' : Type u) [Field F] [CharZero F] [Field F'] [CharZero F']
      (W : WeilCohomologyTheory k F) (W' : WeilCohomologyTheory k F')
      (X : (SmoothProjectiveScheme k).FullSubcategory) (n : ℤ),
      Module.finrank F (W.grade X n) = Module.finrank F' (W'.grade X n))
    (X : (SmoothProjectiveScheme k).FullSubcategory)
    (S : StupidTruncationSpectralSequence (baseRingedSpace _)
      (deRhamComplexInt (X := X.obj.left.toRingedSpace) (formsAlgebras X.obj.hom)
        (deRhamDifferential (formsAlgebras X.obj.hom))))
    (hS : SpectralSequence.AbutsTo S.spectralSequence
      (deRhamCohomology (X := X.obj.left.toRingedSpace) (formsAlgebras X.obj.hom)
        (deRhamDifferential (formsAlgebras X.obj.hom)))) :
    S.spectralSequence.DegeneratesAt 1
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.22, Tag 0FWC](https://stacks.math.columbia.edu/tag/0FWC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
