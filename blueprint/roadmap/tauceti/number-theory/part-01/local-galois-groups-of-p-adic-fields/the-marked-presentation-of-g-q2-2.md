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

- [The abelianization structure theorem for one-relator pro-`p` groups](../../../topology/algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../../topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The Demushkin predicate (Labute, p. 106), for a prime `p` and a topological group `G`](../../../topology/profinite-and-pro-p-groups/part-01/the-demushkin-predicate-labute-p-106-for-a-prime.md)
- [Demushkin's theorem](demushkins-theorem.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [Labute's criterion](../../../topology/profinite-and-pro-p-groups/part-01/labutes-criterion.md)
- [Labute's Theorem 2](../../../topology/profinite-and-pro-p-groups/part-01/labutes-theorem-2.md)
- [The relative successive-approximation theorem](../../../topology/profinite-and-pro-p-groups/part-01/the-relative-successive-approximation-theorem.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [The successive-approximation theorem with tails](../../../topology/profinite-and-pro-p-groups/part-02/the-successive-approximation-theorem-with-tails.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked` in TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean#L88)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
