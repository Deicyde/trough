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

- [Demushkin's theorem](demushkins-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.IsDemushkin](../../part-05/profinite-and-pro-p-groups/tauceti-isdemushkin.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/RatPadic.html#TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_ratPadic_marked` in TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/RatPadic.lean#L88)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
