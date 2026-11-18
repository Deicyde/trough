---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.Tames.mul_one_add_cayley_mul_ringInverse
statement: formalized
proof: formalized
---

# The inverse Cayley formula

A structure `J` tamed by `ω` is recovered from its Cayley
transform `C = J₀.cayley J` relative to an `ω`-tame `J₀` as `J = J₀ (1 + C)(1 - C)⁻¹`.

```lean
TauCeti.SymplecticForm.Tames.mul_one_add_cayley_mul_ringInverse.{u_1} {V : Type u_1}
  [AddCommGroup V] [_root_.Module ℝ V] {ω : TauCeti.SymplecticForm V}
  {J₀ J : TauCeti.AlmostComplexStructure V} [FiniteDimensional ℝ V] (h₀ : ω.Tames J₀)
  (h : ω.Tames J) :
  J₀.toLinearMap * (1 + J₀.cayley J) * Ring.inverse (1 - J₀.cayley J) = J.toLinearMap
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.Tames.mul_one_add_cayley_mul_ringInverse`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cayley/Basic.html#TauCeti.SymplecticForm.Tames.mul_one_add_cayley_mul_ringInverse).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.Tames.mul_one_add_cayley_mul_ringInverse`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Cayley/Basic.html#TauCeti.SymplecticForm.Tames.mul_one_add_cayley_mul_ringInverse)
- [Source of `TauCeti.SymplecticForm.Tames.mul_one_add_cayley_mul_ringInverse` in TauCeti/Geometry/Symplectic/Cayley/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Cayley/Basic.lean#L225)
