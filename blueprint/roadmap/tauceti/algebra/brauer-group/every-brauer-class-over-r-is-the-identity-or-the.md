---
declaration: theorem
origin: cited
lean: TauCeti.Quaternion.eq_one_or_eq_mk
statement: formalized
proof: formalized
---

# Every Brauer class over `ℝ` is the identity or the class of the real quaternions

The class has a central division-algebra representative, which by Frobenius' theorem is `ℝ` or
`ℍ[ℝ]`; the class of `ℝ` is the identity.

```lean
TauCeti.Quaternion.eq_one_or_eq_mk (x : BrauerGroup ℝ) :
  x = 1 ∨ x = TauCeti.BrauerGroup.mk (TauCeti.CSA.of ℝ (Quaternion ℝ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Frobenius' theorem](../central-simple/frobenius-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Quaternion.eq_one_or_eq_mk`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Real.html#TauCeti.Quaternion.eq_one_or_eq_mk).

## Sources

- [Tau Ceti documentation: `TauCeti.Quaternion.eq_one_or_eq_mk`](https://taucetiproject.org/docs/TauCeti/Algebra/BrauerGroup/Real.html#TauCeti.Quaternion.eq_one_or_eq_mk)
- [Source of `TauCeti.Quaternion.eq_one_or_eq_mk` in TauCeti/Algebra/BrauerGroup/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/BrauerGroup/Real.lean#L61)
