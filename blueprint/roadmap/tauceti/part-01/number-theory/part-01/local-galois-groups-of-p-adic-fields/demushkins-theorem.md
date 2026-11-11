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

- [The Demushkin predicate](../../../topology/profinite-and-pro-p-groups/part-01/the-demushkin-predicate.md)

## Proof depends on

- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../class-field-theory/the-local-invariant.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Demushkin.html#TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu).

## Sources

- [Tau Ceti documentation: `TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Demushkin.html#TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu)
- [Source of `TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu` in TauCeti/NumberTheory/LocalField/ProP/Demushkin.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/ProP/Demushkin.lean#L60)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalGaloisGroups/STATUS.md)
