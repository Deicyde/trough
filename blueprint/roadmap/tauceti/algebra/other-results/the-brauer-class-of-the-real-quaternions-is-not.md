---
declaration: theorem
origin: cited
lean: TauCeti.Quaternion.mk_ne_one
statement: formalized
proof: formalized
---

# The Brauer class of the real quaternions is not the identity

`ℍ[ℝ]` is a central division
algebra over `ℝ` of dimension `4`, and a central division algebra has the identity class only when
it is one-dimensional, that is, only when it is the base field.

```lean
TauCeti.Quaternion.mk_ne_one : TauCeti.BrauerGroup.mk (TauCeti.CSA.of ℝ (Quaternion ℝ)) ≠ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wedderburn-Artin for central simple algebras](../central-simple/wedderburn-artin-for-central-simple-algebras.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Quaternion.mk_ne_one`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Quaternion.html#TauCeti.Quaternion.mk_ne_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Quaternion.mk_ne_one`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Quaternion.html#TauCeti.Quaternion.mk_ne_one)
- [Source of `TauCeti.Quaternion.mk_ne_one` in TauCeti/Algebra/BrauerGroup/Quaternion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/BrauerGroup/Quaternion.lean#L67)
