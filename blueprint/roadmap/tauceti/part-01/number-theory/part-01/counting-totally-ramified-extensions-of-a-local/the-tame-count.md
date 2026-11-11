---
declaration: theorem
origin: cited
lean: TauCeti.encard_totallyRamifiedOfDegree_of_not_dvd
statement: formalized
proof: formalized
---

# The tame count

if the residue characteristic of `K` does not divide `n`, then a
separable closure of `K` has exactly `n` totally ramified subextensions of degree `n`.

```lean
TauCeti.encard_totallyRamifiedOfDegree_of_not_dvd.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ}
  (hp : ¬ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) ∣ n) :
  (TauCeti.totallyRamifiedOfDegree K n).encard = ↑n
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Serre's first mass formula](serres-first-mass-formula.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.encard_totallyRamifiedOfDegree_of_not_dvd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.encard_totallyRamifiedOfDegree_of_not_dvd).

## Sources

- [Tau Ceti documentation: `TauCeti.encard_totallyRamifiedOfDegree_of_not_dvd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.encard_totallyRamifiedOfDegree_of_not_dvd)
- [Source of `TauCeti.encard_totallyRamifiedOfDegree_of_not_dvd` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L123)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
