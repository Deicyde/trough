---
declaration: theorem
origin: cited
lean: TauCeti.isTotallyReflexive_iff_isGorensteinProjective, TauCeti.isTotallyReflexive_of_ext_transpose_eq_zero
statement: formalized
proof: formalized
---

# Auslander–Bridger

over a left and right noetherian ring, a module is totally reflexive if
and only if it is Gorenstein-projective.

```lean
TauCeti.isTotallyReflexive_iff_isGorensteinProjective.{u} {A : Type u} [Ring A] [IsNoetherianRing A]
  [IsNoetherianRing Aᵐᵒᵖ] (M : ModuleCat A) :
  TauCeti.IsTotallyReflexive A M ↔ TauCeti.IsGorensteinProjective A M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isTotallyReflexive_iff_isGorensteinProjective`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/GorensteinProjective/TotallyReflexive.html#TauCeti.isTotallyReflexive_iff_isGorensteinProjective).

## Other forms

**Auslander–Bridger.** Formalized in Tau Ceti as [`TauCeti.isTotallyReflexive_of_ext_transpose_eq_zero`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/GorensteinProjective/Transpose.html#TauCeti.isTotallyReflexive_of_ext_transpose_eq_zero).

```lean
TauCeti.isTotallyReflexive_of_ext_transpose_eq_zero.{u} {A : Type u} [Ring A] {M : ModuleCat A}
  (P : TauCeti.FiniteProjectivePresentation M)
  (hM : ∀ (n : ℕ) (e : CategoryTheory.Abelian.Ext M (↧A) (n + 1)), e = 0)
  (hT :
    ∀ (n : ℕ)
      (e : CategoryTheory.Abelian.Ext (↧(TauCeti.AuslanderReitenTranspose P.p)) (↧A) (n + 1)),
      e = 0) :
  TauCeti.IsTotallyReflexive A M
```

## Sources

- [Tau Ceti documentation: `TauCeti.isTotallyReflexive_iff_isGorensteinProjective`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/GorensteinProjective/TotallyReflexive.html#TauCeti.isTotallyReflexive_iff_isGorensteinProjective)
- [Source of `TauCeti.isTotallyReflexive_iff_isGorensteinProjective` in TauCeti/Algebra/Homology/GorensteinProjective/TotallyReflexive.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/GorensteinProjective/TotallyReflexive.lean#L260)
