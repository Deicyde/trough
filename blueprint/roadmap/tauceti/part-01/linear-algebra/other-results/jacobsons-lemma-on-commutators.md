---
declaration: theorem
origin: cited
lean: LinearMap.isNilpotent_lie_of_lie_lie_eq_zero
statement: formalized
proof: formalized
---

# Jacobson's lemma on commutators

In characteristic zero, if `A` commutes with `⁅A, B⁆`,
then `⁅A, B⁆` is nilpotent: each of its positive powers is a commutator with `A`, hence
traceless.

```lean
LinearMap.isNilpotent_lie_of_lie_lie_eq_zero.{u_1, u_2} {K : Type u_1} {M : Type u_2} [Field K]
  [AddCommGroup M] [_root_.Module K M] [FiniteDimensional K M] [CharZero K] {A B : Module.End K M}
  (h : ⁅A, ⁅A, B⁆⁆ = 0) : IsNilpotent ⁅A, B⁆
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.isNilpotent_lie_of_lie_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Trace/Nilpotent.html#LinearMap.isNilpotent_lie_of_lie_lie_eq_zero).

## Sources

- [Tau Ceti documentation: `LinearMap.isNilpotent_lie_of_lie_lie_eq_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Trace/Nilpotent.html#LinearMap.isNilpotent_lie_of_lie_lie_eq_zero)
- [Source of `LinearMap.isNilpotent_lie_of_lie_lie_eq_zero` in TauCeti/LinearAlgebra/Trace/Nilpotent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Trace/Nilpotent.lean#L150)
