---
declaration: theorem
origin: cited
lean: TauCeti.adoIwasawa, TauCeti.exists_faithful_nilrepresentation
statement: formalized
proof: formalized
---

# The Ado–Iwasawa theorem

Every finite-dimensional Lie algebra over a field admits a
faithful finite-dimensional representation.

```lean
TauCeti.adoIwasawa.{u, v} (K : Type u) (L : Type v) [Field K] [LieRing L] [LieAlgebra K L]
  [FiniteDimensional K L] : ∃ V x x_1, ∃ (_ : FiniteDimensional K V), ∃ ρ, Function.Injective ⇑ρ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hochschild's strengthening of the Ado–Iwasawa theorem](hochschilds-strengthening-of-the-ado-iwasawa-the.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.adoIwasawa`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.html#TauCeti.adoIwasawa).

## Other forms

**The Ado–Iwasawa theorem with nilpotence on the nilradical.** Formalized in Tau Ceti as [`TauCeti.exists_faithful_nilrepresentation`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.html#TauCeti.exists_faithful_nilrepresentation).

```lean
TauCeti.exists_faithful_nilrepresentation.{u, v} (K : Type u) (L : Type v) [Field K] [LieRing L]
  [LieAlgebra K L] [FiniteDimensional K L] :
  ∃ V x x_1,
    ∃ (_ : FiniteDimensional K V),
      ∃ ρ, Function.Injective ⇑ρ ∧ ∀ x_3 ∈ TauCeti.LieAlgebra.nilradical K L, IsNilpotent (ρ x_3)
```

## Sources

- [Tau Ceti documentation: `TauCeti.adoIwasawa`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.html#TauCeti.adoIwasawa)
- [Source of `TauCeti.adoIwasawa` in TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.lean#L111)
