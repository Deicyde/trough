---
declaration: theorem
origin: cited
lean: LieDerivation.IsKilling.exists_eq_inner, LieModule.Cohomology.exists_eq_lie_of_d₁₂_eq_zero
statement: formalized
proof: formalized
---

# Whitehead's first lemma

Over a field of characteristic zero, every Lie derivation from a
Lie algebra with nondegenerate Killing form (necessarily finite-dimensional) into a
finite-dimensional module is inner: it is `x ↦ ⁅x, m⁆` for some `m`.

```lean
LieDerivation.IsKilling.exists_eq_inner.{u, v, w} {K : Type u} {L : Type v} {M : Type w} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M]
  (D : LieDerivation K L M) : ∃ m, (LieDerivation.inner K L M) m = D
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LieDerivation.IsKilling.exists_eq_inner`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieDerivation.IsKilling.exists_eq_inner).

## Other forms

**Whitehead's first lemma for cochains.** Formalized in Tau Ceti as [`LieModule.Cohomology.exists_eq_lie_of_d₁₂_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieModule.Cohomology.exists_eq_lie_of_d%E2%82%81%E2%82%82_eq_zero).

```lean
LieModule.Cohomology.exists_eq_lie_of_d₁₂_eq_zero.{u, v, w} {K : Type u} {L : Type v} {M : Type w}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [LieAlgebra.IsKilling K L] [AddCommGroup M]
  [_root_.Module K M] [LieRingModule L M] [LieModule K L M] [FiniteDimensional K M]
  {f : LieModule.Cohomology.oneCochain K L M} (hf : (LieModule.Cohomology.d₁₂ K L M) f = 0) :
  ∃ m, ∀ (x : L), f x = ⁅x, m⁆
```

## Sources

- [Tau Ceti documentation: `LieDerivation.IsKilling.exists_eq_inner`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Whitehead.html#LieDerivation.IsKilling.exists_eq_inner)
- [Source of `LieDerivation.IsKilling.exists_eq_inner` in TauCeti/Algebra/Lie/Whitehead.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Whitehead.lean#L78)
