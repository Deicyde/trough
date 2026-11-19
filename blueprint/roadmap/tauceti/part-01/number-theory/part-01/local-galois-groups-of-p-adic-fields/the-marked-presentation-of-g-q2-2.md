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

- [The abelianization structure theorem for one-relator pro-`p` groups](../../../../part-02/topology/algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../../../part-02/topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The Demushkin predicate](../../../../part-02/topology/profinite-and-pro-p-groups/the-demushkin-predicate.md)
- [Demushkin's theorem](demushkins-theorem.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [Labute's criterion](../../../../part-02/topology/profinite-and-pro-p-groups/labutes-criterion.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../../../part-02/topology/algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [The necessity half of the existence theorem for `q ≠ 2` (Labute, Theorem 1)](../../../../part-02/topology/profinite-and-pro-p-groups/the-necessity-half-of-the-existence-theorem-for.md)
- [The relative successive-approximation theorem](../../../../part-02/topology/profinite-and-pro-p-groups/the-relative-successive-approximation-theorem.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The successive-approximation theorem with tails](../../../../part-02/topology/algebra/part-02/the-successive-approximation-theorem-with-tails.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked` in TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean#L88)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalGaloisGroups/STATUS.md)
