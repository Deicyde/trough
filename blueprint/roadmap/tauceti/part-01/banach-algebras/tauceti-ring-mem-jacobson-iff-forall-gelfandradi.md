---
declaration: theorem
origin: cited
lean: TauCeti.Ring.mem_jacobson_iff_forall_gelfandRadius_mul_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.Ring.mem\_jacobson\_iff\_forall\_gelfandRadius\_mul\_eq\_zero

An element of a complex Banach algebra lies in its Jacobson radical exactly when every
left multiple `b * a` is quasinilpotent, that is, `‖(b * a) ^ n‖ ^ (1 / n)` tends to zero.

```lean
TauCeti.Ring.mem_jacobson_iff_forall_gelfandRadius_mul_eq_zero.{u_3} {B : Type u_3} [NormedRing B]
  [NormedAlgebra ℂ B] [CompleteSpace B] {a : B} :
  a ∈ Ring.jacobson B ↔ ∀ (b : B), gelfandRadius (b * a) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Ring.mem_jacobson_iff_forall_gelfandRadius_mul_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Jacobson.html#TauCeti.Ring.mem_jacobson_iff_forall_gelfandRadius_mul_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Ring.mem_jacobson_iff_forall_gelfandRadius_mul_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Jacobson.html#TauCeti.Ring.mem_jacobson_iff_forall_gelfandRadius_mul_eq_zero)
- [Source of `TauCeti.Ring.mem_jacobson_iff_forall_gelfandRadius_mul_eq_zero` in TauCeti/Analysis/Normed/Algebra/Jacobson.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Algebra/Jacobson.lean#L119)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BanachAlgebras/STATUS.md)
