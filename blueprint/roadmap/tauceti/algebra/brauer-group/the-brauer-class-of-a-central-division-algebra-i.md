---
declaration: theorem
origin: cited
lean: TauCeti.BrauerGroup.mk_eq_one_iff_finrank_eq_one
statement: formalized
proof: formalized
---

# The Brauer class of a central division algebra is the identity exactly when the algebra is one-dimensional

Not a `simp` lemma, for the same reason as `TauCeti.BrauerGroup.mk_eq_one_iff_isSplittingField`.

```lean
TauCeti.BrauerGroup.mk_eq_one_iff_finrank_eq_one.{u} (K : Type u) [Field K] (D : Type u)
  [DivisionRing D] [Algebra K D] [Algebra.IsCentral K D] [FiniteDimensional K D] :
  TauCeti.BrauerGroup.mk (TauCeti.CSA.of K D) = 1 ↔ Module.finrank K D = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.BrauerGroup.mk_eq_one_iff_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Splitting.html#TauCeti.BrauerGroup.mk_eq_one_iff_finrank_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.BrauerGroup.mk_eq_one_iff_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Splitting.html#TauCeti.BrauerGroup.mk_eq_one_iff_finrank_eq_one)
- [Source of `TauCeti.BrauerGroup.mk_eq_one_iff_finrank_eq_one` in TauCeti/Algebra/BrauerGroup/Splitting.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/BrauerGroup/Splitting.lean#L228)
