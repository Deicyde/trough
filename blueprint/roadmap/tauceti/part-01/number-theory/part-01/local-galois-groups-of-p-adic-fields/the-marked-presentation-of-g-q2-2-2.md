---
declaration: theorem
origin: cited
lean: TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked
statement: formalized
proof: formalized
---

# The marked presentation of `G_{ℚ₂(√-2)}(2)`

The maximal pro-`2` Galois group of
`ℚ₂(√-2)` is isomorphic to `⟨x₁, x₂, x₃, x₄ ∣ x₁⁶ (x₁, x₂) x₃⁸ (x₃, x₄)⟩`, the even dyadic
Demushkin group with `α = 4` and `f = 3`, and under this isomorphism the cyclotomic orientation
satisfies `χ(x₂) · (1 + 4) = -1` and `χ(x₄) · (1 - 8) = 1` and is trivial on `x₁` and `x₃`.

This is `absoluteGaloisGroupProP_two_marked_of_degree_even_principal` at `N = 2`, with `k = 2`
read off the cyclotomic image `closure⟨-1 + 2²⟩`
(`range_localCyclotomicCharacter_ratPadicSqrtNegTwo`).

```lean
TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked :
  ∃ e,
    ↑((TauCeti.cyclotomicOrientation 2 TauCeti.RatPadicSqrtNegTwo
                TauCeti.ratPadicSqrtNegTwo_hasPrimitiveRoot)
              (e.symm
                (TauCeti.presentedProPGen 2 4
                  {TauCeti.demushkinWordTwoEven 4 3 4 (TauCeti.freeProPGen 2 4)} 1))) *
          (1 + 4) =
        -1 ∧
      ↑((TauCeti.cyclotomicOrientation 2 TauCeti.RatPadicSqrtNegTwo
                  TauCeti.ratPadicSqrtNegTwo_hasPrimitiveRoot)
                (e.symm
                  (TauCeti.presentedProPGen 2 4
                    {TauCeti.demushkinWordTwoEven 4 3 4 (TauCeti.freeProPGen 2 4)} 3))) *
            (1 - 8) =
          1 ∧
        (TauCeti.cyclotomicOrientation 2 TauCeti.RatPadicSqrtNegTwo
                TauCeti.ratPadicSqrtNegTwo_hasPrimitiveRoot)
              (e.symm
                (TauCeti.presentedProPGen 2 4
                  {TauCeti.demushkinWordTwoEven 4 3 4 (TauCeti.freeProPGen 2 4)} 0)) =
            1 ∧
          (TauCeti.cyclotomicOrientation 2 TauCeti.RatPadicSqrtNegTwo
                TauCeti.ratPadicSqrtNegTwo_hasPrimitiveRoot)
              (e.symm
                (TauCeti.presentedProPGen 2 4
                  {TauCeti.demushkinWordTwoEven 4 3 4 (TauCeti.freeProPGen 2 4)} 2)) =
            1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Burnside's basis theorem, cardinal form](../../../../part-02/topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [Burnside's criterion modulo `λ_1`](../../../../part-02/topology/algebra/part-01/burnsides-criterion-modulo-1.md)
- [The constrained successive-approximation theorem](../../../../part-02/topology/profinite-and-pro-p-groups/the-constrained-successive-approximation-theorem.md)
- [Dedekind's modular law](../../../algebra/part-02/other-results/dedekinds-modular-law.md)
- [The Demushkin predicate](../../../../part-02/topology/profinite-and-pro-p-groups/the-demushkin-predicate.md)
- [Demushkin's theorem](demushkins-theorem.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../../../part-02/topology/algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [Labute's classification of the closed subgroups of `ℤ_2ˣ`](../../part-03/padics/labutes-classification-of-the-closed-subgroups-o.md)
- [Labute's criterion](../../../../part-02/topology/profinite-and-pro-p-groups/labutes-criterion.md)
- [Labute's Theorem 4: a Demushkin group has exactly one continuous character with the prescription property](../../../../part-02/topology/algebra/part-01/labutes-theorem-4-a-demushkin-group-has-exactly.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.html#TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.html#TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked` in TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.lean#L223)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/LocalGaloisGroups/STATUS.md)
