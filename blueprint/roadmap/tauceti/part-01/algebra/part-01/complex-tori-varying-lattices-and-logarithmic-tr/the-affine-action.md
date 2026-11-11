---
declaration: def
origin: cited
lean: TauCeti.torusFamilyAffineMulAction
statement: formalized
---

# The affine action

**The affine action** of `Γ` on the family of tori, `g • [y, v] = R g y v +ᵥ b g y`.
Besides the cocycle laws of `R`, it requires the cocycle laws of the translation part:
`b 1 y` is the zero `[y, 0]` of the fibre over `y`, and `b (g * h) y` is the image of `b h y`
under the affine map of `g`, that is `R g (h • y) (b h y) + b g (h • y)`.

```lean
TauCeti.torusFamilyAffineMulAction.{u_1, u_2, u_3, u_4} {Y : Type u_1} {Λ : Type u_2} {E : Type u_3}
  [AddCommGroup Λ] [AddCommGroup E] {Γ : Type u_4} [Monoid Γ] [MulAction Γ Y] (R : Γ → Y → E →+ E)
  (hone : ∀ (y : Y) (v : E), (R 1 y) v = v)
  (hmul : ∀ (g h : Γ) (y : Y) (v : E), (R (g * h) y) v = (R g (h • y)) ((R h y) v))
  (P : Y → Λ →ₗ[ℤ] E) (ρ : Representation ℤ Γ Λ)
  (hP : ∀ (g : Γ) (y : Y) (l : Λ), (P (g • y)) ((ρ g) l) = (R g y) ((P y) l))
  (b : Γ → Y → AddAction.orbitRel.Quotient Λ (Y × E))
  (hb : ∀ (g : Γ) (y : Y), TauCeti.torusFamilyProjection P (b g y) = g • y)
  (hbone : ∀ (y : Y), b 1 y = ⟦(y, 0)⟧)
  (hbmul :
    ∀ (g h : Γ) (y : Y), b (g * h) y = TauCeti.torusFamilyAffineMap R P ρ hP b hb g (b h y)) :
  MulAction Γ (AddAction.orbitRel.Quotient Λ (Y × E))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.torusFamilyAffineMulAction`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/AffineAction.html#TauCeti.torusFamilyAffineMulAction).

## Sources

- [Tau Ceti documentation: `TauCeti.torusFamilyAffineMulAction`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/AffineAction.html#TauCeti.torusFamilyAffineMulAction)
- [Source of `TauCeti.torusFamilyAffineMulAction` in TauCeti/Algebra/Module/ZLattice/Family/AffineAction.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/Family/AffineAction.lean#L203)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
