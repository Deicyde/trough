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

- [The Demushkin predicate (Labute, p. 106), for a prime `p` and a topological group `G`](../../../topology/profinite-and-pro-p-groups/part-01/the-demushkin-predicate-labute-p-106-for-a-prime.md)

## Proof depends on

- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](../class-field-theory/the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Demushkin.html#TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu).

## Sources

- [Tau Ceti documentation: `TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Demushkin.html#TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu)
- [Source of `TauCeti.isDemushkin_absoluteGaloisGroupProP_of_mu` in TauCeti/NumberTheory/LocalField/ProP/Demushkin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/Demushkin.lean#L60)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
