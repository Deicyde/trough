---
declaration: theorem
origin: cited
lean: TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked
statement: formalized
proof: formalized
---

# The marked presentation of `G_{ℚ₂}(2)`

There is an isomorphism
`e : G_{ℚ₂}(2) ≃ D₀ = ⟨A, S, Y ∣ A²S⁴(S,Y)⟩` along which the standard orientation of `D₀` pulls
back to the cyclotomic orientation of `G_{ℚ₂}(2)`, and the cyclotomic orientation is surjective.

```lean
TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked :
  ∃ e,
    TauCeti.standardD0Orientation.comp ↑e =
        TauCeti.cyclotomicOrientation 2 ℚ_[2] TauCeti.ratPadicTwo_hasPrimitiveRoot ∧
      Function.Surjective
        ⇑(TauCeti.cyclotomicOrientation 2 ℚ_[2] TauCeti.ratPadicTwo_hasPrimitiveRoot)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../../../topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The Demushkin predicate](../../../topology/profinite-and-pro-p-groups/part-01/the-demushkin-predicate.md)
- [Demushkin's theorem](demushkins-theorem.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [Labute's criterion](../../../topology/profinite-and-pro-p-groups/part-01/labutes-criterion.md)
- [Labute's normal form for `q = 2` and odd rank (Labute, Theorem 3, case (2))](../../../topology/profinite-and-pro-p-groups/part-01/labutes-normal-form-for-q-2-and-odd-rank-labute.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../../topology/algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked` in TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean#L88)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/LocalGaloisGroups/STATUS.md)
