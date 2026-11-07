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

- [Demushkin's theorem](demushkins-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.IsDemushkin](../../part-05/profinite-and-pro-p-groups/tauceti-isdemushkin.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.html#TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.html#TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_ratPadicSqrtNegTwo_marked` in TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/SqrtNegTwo.lean#L223)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
