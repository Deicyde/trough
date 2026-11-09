---
declaration: theorem
origin: cited
lean: TauCeti.le_add_fenchelConjugate, TauCeti.sub_le_fenchelConjugate
statement: formalized
proof: formalized
---

# The Fenchel–Young inequality

**The Fenchel–Young inequality** in additive form, `⟪x, y⟫ ≤ f x + f⋆ y`, valid whenever
neither summand is `⊥`; the second summand is `⊥` only when `f ≡ ⊤`.

```lean
TauCeti.le_add_fenchelConjugate.{u_1, u_2} {E : Type u_1} {F : Type u_2} [AddCommMonoid E]
  [_root_.Module ℝ E] [AddCommMonoid F] [_root_.Module ℝ F] (B : E →ₗ[ℝ] F →ₗ[ℝ] ℝ) {f : E → EReal}
  {x : E} {y : F} (hx : f x ≠ ⊥) (hy : TauCeti.fenchelConjugate B f y ≠ ⊥) :
  ↑((B x) y) ≤ f x + TauCeti.fenchelConjugate B f y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.le_add_fenchelConjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Conjugate.html#TauCeti.le_add_fenchelConjugate).

## Other forms

**The Fenchel–Young inequality, in the form that holds with no hypothesis.** Formalized in Tau Ceti as [`TauCeti.sub_le_fenchelConjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Conjugate.html#TauCeti.sub_le_fenchelConjugate).

```lean
TauCeti.sub_le_fenchelConjugate.{u_1, u_2} {E : Type u_1} {F : Type u_2} [AddCommMonoid E]
  [_root_.Module ℝ E] [AddCommMonoid F] [_root_.Module ℝ F] (B : E →ₗ[ℝ] F →ₗ[ℝ] ℝ) (f : E → EReal)
  (x : E) (y : F) : ↑((B x) y) - f x ≤ TauCeti.fenchelConjugate B f y
```

## Sources

- [Tau Ceti documentation: `TauCeti.le_add_fenchelConjugate`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/Conjugate.html#TauCeti.le_add_fenchelConjugate)
- [Source of `TauCeti.le_add_fenchelConjugate` in TauCeti/Analysis/Convex/Conjugate.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/Conjugate.lean#L163)
