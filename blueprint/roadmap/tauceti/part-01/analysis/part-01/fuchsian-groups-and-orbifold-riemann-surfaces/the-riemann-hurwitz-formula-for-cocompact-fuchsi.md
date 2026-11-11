---
declaration: theorem
origin: cited
lean: TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree_of_compactSpace, TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree, TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_interior_sub_cusps
statement: formalized
proof: formalized
---

# The Riemann–Hurwitz formula for cocompact Fuchsian groups

Let `Δ ≤ Γ` be discrete
subgroups of `PSL(2, ℝ)` of finite index, with `Γ \ ℍ` compact. Then
`χ(X(Δ)) = [Γ : Δ] · χ(X(Γ)) - R`, where `R` is the ramification degree of `X(Δ) → X(Γ)`. Unlike
`TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree`, this carries
no finite-CW-type hypotheses: both compactified quotients have finite CW type, and the formula
follows from multiplicativity of the orbifold Euler characteristic together with the expression
of `R` through elliptic orders.

```lean
TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree_of_compactSpace
  {Δ Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  [CompactSpace (MulAction.orbitRel.Quotient (↥Γ) UpperHalfPlane)] (h : Δ ≤ Γ)
  [Δ.IsFiniteRelIndex Γ] :
  TauCeti.eulerChar Δ.CompactifiedQuotient =
    ↑(Δ.subgroupOf Γ).index * TauCeti.eulerChar Γ.CompactifiedQuotient -
      ↑(TauCeti.RiemannSurface.ramificationDegree (Subgroup.compactifiedQuotientMap h))
```

## Depends on

- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Proof depends on

- [A CW structure lifts along a covering map](../../../algebraic-topology/classifying-spaces-of-discrete-groups/a-cw-structure-lifts-along-a-covering-map.md)
- [Compactness for cofinite groups](compactness-for-cofinite-groups.md)
- [The degree of a finite-index map of compactified Fuchsian quotients is the index](the-degree-of-a-finite-index-map-of-compactified.md)
- [Euler--Poincaré for cellular chains](../../../algebraic-topology/cellular/euler-poincare-for-cellular-chains.md)
- [Jørgensen's inequality](../../part-02/complex/part-02/jrgensens-inequality.md)
- [The Margulis lemma for Fuchsian groups](../../part-02/complex/part-02/the-margulis-lemma-for-fuchsian-groups.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The open mapping theorem](../../part-02/complex/part-03/the-open-mapping-theorem.md)
- [The orbifold area formula for a cocompact Fuchsian group](the-orbifold-area-formula-for-a-cocompact-fuchsi.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [The quotient of a cocompact Fuchsian group has finite CW type](the-quotient-of-a-cocompact-fuchsian-group-has-f.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [Rouché's theorem for a disc, classical form](../../part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree_of_compactSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.html#TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree_of_compactSpace).

## Other forms

**The Riemann–Hurwitz formula for Fuchsian groups.** Formalized in Tau Ceti as [`TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/RiemannHurwitz.html#TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree).

```lean
TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree
  {Δ Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ] (h : Δ ≤ Γ)
  [Δ.IsFiniteRelIndex Γ] [hcompact : CompactSpace Δ.CompactifiedQuotient]
  [hcw : TauCeti.FiniteCWType Δ.CompactifiedQuotient] [TauCeti.FiniteCWType Γ.CompactifiedQuotient]
  [TauCeti.FiniteCWType (MulAction.orbitRel.Quotient ↥Γ ↥(TauCeti.freeLocus (↥Γ) UpperHalfPlane))] :
  TauCeti.eulerChar Δ.CompactifiedQuotient =
    ↑(Δ.subgroupOf Γ).index * TauCeti.eulerChar Γ.CompactifiedQuotient -
      ↑(TauCeti.RiemannSurface.ramificationDegree (Subgroup.compactifiedQuotientMap h))
```

**The Riemann–Hurwitz formula for Fuchsian groups, with explicit ramification.** Formalized in Tau Ceti as [`TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_interior_sub_cusps`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/RiemannHurwitz.html#TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_interior_sub_cusps).

```lean
TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_interior_sub_cusps
  {Δ Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ] (h : Δ ≤ Γ)
  [Δ.IsFiniteRelIndex Γ] [hcompact : CompactSpace Δ.CompactifiedQuotient]
  [hcw : TauCeti.FiniteCWType Δ.CompactifiedQuotient] [TauCeti.FiniteCWType Γ.CompactifiedQuotient]
  [TauCeti.FiniteCWType (MulAction.orbitRel.Quotient ↥Γ ↥(TauCeti.freeLocus (↥Γ) UpperHalfPlane))]
  (z : MulAction.orbitRel.Quotient (↥Δ) UpperHalfPlane → UpperHalfPlane)
  (hz : ∀ (q : MulAction.orbitRel.Quotient (↥Δ) UpperHalfPlane), Quotient.mk'' (z q) = q)
  (c : Δ.CuspOrbit → ↥Δ.cuspPoints) (hc : ∀ (C : Δ.CuspOrbit), Subgroup.cuspOrbitMk (c C) = C) :
  TauCeti.eulerChar Δ.CompactifiedQuotient =
    ↑(Δ.subgroupOf Γ).index * TauCeti.eulerChar Γ.CompactifiedQuotient -
        ↑(∑ᶠ (q : MulAction.orbitRel.Quotient (↥Δ) UpperHalfPlane),
            (Subgroup.ellipticRamificationIndex h (z q) - 1)) -
      ↑(∑ᶠ (C : Δ.CuspOrbit), ((Δ.subgroupOf Γ).relIndex (MulAction.stabilizer ↥Γ ↑(c C)) - 1))
```

## Sources

- [Tau Ceti documentation: `TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree_of_compactSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.html#TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree_of_compactSpace)
- [Source of `TauCeti.Fuchsian.eulerChar_compactifiedQuotient_eq_index_mul_sub_ramificationDegree_of_compactSpace` in TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/Compactification/EulerCharacteristic.lean#L169)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
