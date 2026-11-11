---
declaration: theorem
origin: cited
lean: TauCeti.hasCentralRadical_iff_isCompl_center_derivedSeries
statement: formalized
proof: formalized
---

# The structure theorem for reductive Lie algebras

Over a field of characteristic zero, a
finite-dimensional Lie algebra is reductive (its solvable radical is its centre) if and only if it
is the direct sum of its centre and its derived ideal, with the derived ideal semisimple.

The reverse implication only uses the second conjunct: semisimplicity of the derived ideal alone
implies reductivity, through `TauCeti.hasCentralRadical_of_hasTrivialRadical_derivedSeries`, and
hence the first conjunct. The first conjunct alone is not enough: the semidirect product
`sl₂ ⋉ K²` with the standard module has trivial centre and is its own derived ideal, so it
satisfies the first conjunct without being reductive.

```lean
TauCeti.hasCentralRadical_iff_isCompl_center_derivedSeries.{u, v} (K : Type u) (L : Type v)
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] :
  LieAlgebra.HasCentralRadical K L ↔
    IsCompl (LieAlgebra.center K L) (LieAlgebra.derivedSeries K L 1) ∧
      LieAlgebra.IsSemisimple K ↥(LieAlgebra.derivedSeries K L 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Weyl's theorem as a decomposition](weyls-theorem-as-a-decomposition.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasCentralRadical_iff_isCompl_center_derivedSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Reductive/Basic.html#TauCeti.hasCentralRadical_iff_isCompl_center_derivedSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.hasCentralRadical_iff_isCompl_center_derivedSeries`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Reductive/Basic.html#TauCeti.hasCentralRadical_iff_isCompl_center_derivedSeries)
- [Source of `TauCeti.hasCentralRadical_iff_isCompl_center_derivedSeries` in TauCeti/Algebra/Lie/Reductive/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Reductive/Basic.lean#L467)
