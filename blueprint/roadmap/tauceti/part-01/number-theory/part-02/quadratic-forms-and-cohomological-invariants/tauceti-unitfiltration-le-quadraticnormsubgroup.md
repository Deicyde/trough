---
declaration: theorem
origin: cited
lean: TauCeti.unitFiltration_le_quadraticNormSubgroup_iff
statement: formalized
proof: formalized
---

# TauCeti.unitFiltration_le_quadraticNormSubgroup_iff

The exact principal-unit norm threshold for every nonsquare radicand, including those
of negative valuation. The even-defect case is unramified. In the ramified case the relative
defect `d - v_K(a)` is nonnegative, and all depth-`n` units are norms exactly when
`n > 2 v_K(2) - (d - v_K(a))`.

```lean
TauCeti.unitFiltration_le_quadraticNormSubgroup_iff.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (h2 : 2 ≠ 0) {a : Kˣ} {d : ℤ}
  (hd : TauCeti.defectExponent a = ↑d) {n : ℕ} :
  TauCeti.unitFiltration K n ≤ TauCeti.quadraticNormSubgroup ↑a ↔
    Even d ∨
      2 * TauCeti.dyadicLevel K h2 -
          (d - Multiplicative.toAdd ((TauCeti.normalizedValuation K) a)).toNat <
        n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The local square theorem bounds the defect of a unit](../local-field/the-local-square-theorem-bounds-the-defect-of-a.md)
- [The splitting criterion for quaternion algebras](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.unitFiltration_le_quadraticNormSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Norm/Conductor.html#TauCeti.unitFiltration_le_quadraticNormSubgroup_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.unitFiltration_le_quadraticNormSubgroup_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Norm/Conductor.html#TauCeti.unitFiltration_le_quadraticNormSubgroup_iff)
- [Source of `TauCeti.unitFiltration_le_quadraticNormSubgroup_iff` in TauCeti/NumberTheory/LocalField/QuadraticForm/Norm/Conductor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/QuadraticForm/Norm/Conductor.lean#L68)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
