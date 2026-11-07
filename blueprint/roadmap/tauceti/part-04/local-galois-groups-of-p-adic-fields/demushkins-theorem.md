---
declaration: theorem
origin: cited
lean: TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu
statement: formalized
proof: formalized
---

# Demushkin's theorem

the maximal pro-`p` quotient `G_K(p)` of the absolute Galois group of
a nonarchimedean local field `K` containing a primitive `p`th root of unity is a Demushkin group.

```lean
TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu (p : ℕ) [Fact (Nat.Prime p)] (K : Type) [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  (hmu : ∃ ζ, IsPrimitiveRoot ζ p) : TauCeti.IsDemushkin p (TauCeti.absoluteGaloisGroupProP p K)
```

## Depends on

- [TauCeti.IsDemushkin](../../part-05/profinite-and-pro-p-groups/tauceti-isdemushkin.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.invMap](../../part-01/class-field-theory/tauceti-classfieldtheory-invmap.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Demushkin.html#TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu).

## Sources

- [Tau Ceti documentation: `TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Demushkin.html#TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu)
- [Source of `TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu` in TauCeti/NumberTheory/LocalField/ProP/Demushkin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/Demushkin.lean#L60)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
