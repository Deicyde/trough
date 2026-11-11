---
declaration: theorem
origin: cited
lean: TauCeti.IsTotallyRamified.existsUnique_isRoot_le_addVal_iff
statement: formalized
proof: formalized
---

# The local fibre count

A monic polynomial of degree `[L : K]` has exactly one root
in a sufficiently small uniformizer ball precisely when its value at the center has the extra
order given by the discriminant exponent.

```lean
TauCeti.IsTotallyRamified.existsUnique_isRoot_le_addVal_iff.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Field L]
  [ValuativeRel L] [TopologicalSpace L] [IsNonarchimedeanLocalField L] [Algebra K L]
  [ValuativeExtension K L] [Algebra.IsSeparable K L] (h : TauCeti.IsTotallyRamified K L)
  {ξ : ↥(ValuativeRel.valuation L).integer} (hξ : Irreducible ξ)
  {g : Polynomial ↥(ValuativeRel.valuation K).integer} (hg : g.Monic)
  (hdeg : g.natDegree = TauCeti.ramificationIndex K L) {r : ℕ}
  (hr : TauCeti.discriminantExponent K L < r) :
  (∃! z,
      (Polynomial.aeval z) g = 0 ∧
        ↑r ≤ (IsDiscreteValuationRing.addVal ↥(ValuativeRel.valuation L).integer) (z - ξ)) ↔
    ↑(r + TauCeti.discriminantExponent K L) ≤
      (IsDiscreteValuationRing.addVal ↥(ValuativeRel.valuation L).integer) ((Polynomial.aeval ξ) g)
```

## Depends on

- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](hensels-lemma-with-an-estimate-over-a-henselian.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsTotallyRamified.existsUnique_isRoot_le_addVal_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/RootCount/Fibre.html#TauCeti.IsTotallyRamified.existsUnique_isRoot_le_addVal_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.IsTotallyRamified.existsUnique_isRoot_le_addVal_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/RootCount/Fibre.html#TauCeti.IsTotallyRamified.existsUnique_isRoot_le_addVal_iff)
- [Source of `TauCeti.IsTotallyRamified.existsUnique_isRoot_le_addVal_iff` in TauCeti/NumberTheory/LocalField/RootCount/Fibre.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/RootCount/Fibre.lean#L155)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
