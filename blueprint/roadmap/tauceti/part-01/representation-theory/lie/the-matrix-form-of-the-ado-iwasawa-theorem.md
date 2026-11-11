---
declaration: theorem
origin: cited
lean: TauCeti.exists_injective_lieHom_matrix
statement: formalized
proof: formalized
---

# The matrix form of the Ado–Iwasawa theorem

Every finite-dimensional Lie algebra over a
field embeds in `𝔤𝔩_n = Matrix (Fin n) (Fin n) K` for some `n`. Over `ℝ` this is the embedding
consumed by the integration of a real Lie algebra to a Lie group.

```lean
TauCeti.exists_injective_lieHom_matrix.{u, v} (K : Type u) (L : Type v) [Field K] [LieRing L]
  [LieAlgebra K L] [FiniteDimensional K L] : ∃ n f, Function.Injective ⇑f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Ado–Iwasawa theorem](the-ado-iwasawa-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_injective_lieHom_matrix`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.html#TauCeti.exists_injective_lieHom_matrix).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_injective_lieHom_matrix`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.html#TauCeti.exists_injective_lieHom_matrix)
- [Source of `TauCeti.exists_injective_lieHom_matrix` in TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Lie/Ado/ArbitraryField.lean#L130)
