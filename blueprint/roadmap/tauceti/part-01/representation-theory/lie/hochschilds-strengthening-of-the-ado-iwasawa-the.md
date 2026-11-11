---
declaration: theorem
origin: cited
lean: TauCeti.exists_faithful_preserving_ad_nilpotence
statement: formalized
proof: formalized
---

# Hochschild's strengthening of the Ado–Iwasawa theorem

A finite-dimensional Lie algebra
over an arbitrary field has a faithful finite-dimensional representation that preserves
nilpotence of the adjoint action: every `ad`-nilpotent element acts nilpotently.

```lean
TauCeti.exists_faithful_preserving_ad_nilpotence.{u, v} (K : Type u) (L : Type v) [Field K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] :
  ∃ V x x_1,
    ∃ (_ : FiniteDimensional K V),
      ∃ ρ,
        Function.Injective ⇑ρ ∧
          ∀ (x_3 : L), IsNilpotent ((LieAlgebra.ad K L) x_3) → IsNilpotent (ρ x_3)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Frobenius commutator identity](../../algebra/part-02/lie/part-01/the-frobenius-commutator-identity.md)
- [Hochschild's strengthening of Ado's theorem in characteristic zero](hochschilds-strengthening-of-ados-theorem-in-cha.md)
- [The Krull intersection theorem for an extended ideal](../../ring-theory/part-01/ideal/the-krull-intersection-theorem-for-an-extended-i.md)
- [The linear-independence half of the Poincaré--Birkhoff--Witt theorem](../../algebra/part-02/lie/part-01/the-linear-independence-half-of-the-poincare-bir.md)
- [The Poincaré--Birkhoff--Witt theorem](../../algebra/part-02/lie/part-01/the-poincare-birkhoff-witt-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_faithful_preserving_ad_nilpotence`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.html#TauCeti.exists_faithful_preserving_ad_nilpotence).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_faithful_preserving_ad_nilpotence`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.html#TauCeti.exists_faithful_preserving_ad_nilpotence)
- [Source of `TauCeti.exists_faithful_preserving_ad_nilpotence` in TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.lean#L87)
