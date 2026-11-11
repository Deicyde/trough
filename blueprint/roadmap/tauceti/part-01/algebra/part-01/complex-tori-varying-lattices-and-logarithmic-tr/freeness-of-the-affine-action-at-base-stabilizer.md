---
declaration: theorem
origin: cited
lean: TauCeti.isCancelSMul_torusFamilyAffineMulAction_iff
statement: formalized
proof: formalized
---

# Freeness of the affine action at base stabilizers

The affine action of `Γ` on the total
space of the family of tori is free exactly when, for every point `y` of the base and every
nonidentity `g` fixing `y`, the affine automorphism `x ↦ A x + t` by which `g` acts on the fibre
over `y` has no fixed point, that is, its translation part `t` does not lie in the image of
`1 - A`. No freeness of the action on the base is assumed.

```lean
TauCeti.isCancelSMul_torusFamilyAffineMulAction_iff.{u_1, u_2, u_3, u_4} {Y : Type u_1}
  {Λ : Type u_2} {E : Type u_3} {Γ : Type u_4} [AddCommGroup Λ] [AddCommGroup E] [Group Γ]
  [MulAction Γ Y] (R : Γ → Y → E →+ E) (hone : ∀ (y : Y) (v : E), (R 1 y) v = v)
  (hmul : ∀ (g h : Γ) (y : Y) (v : E), (R (g * h) y) v = (R g (h • y)) ((R h y) v))
  (P : Y → Λ →ₗ[ℤ] E) (ρ : Representation ℤ Γ Λ)
  (hP : ∀ (g : Γ) (y : Y) (l : Λ), (P (g • y)) ((ρ g) l) = (R g y) ((P y) l))
  (b : Γ → Y → AddAction.orbitRel.Quotient Λ (Y × E))
  (hb : ∀ (g : Γ) (y : Y), TauCeti.torusFamilyProjection P (b g y) = g • y)
  (hbone : ∀ (y : Y), b 1 y = ⟦(y, 0)⟧)
  (hbmul :
    ∀ (g h : Γ) (y : Y), b (g * h) y = TauCeti.torusFamilyAffineMap R P ρ hP b hb g (b h y)) :
  IsCancelSMul Γ (AddAction.orbitRel.Quotient Λ (Y × E)) ↔
    ∀ (y : Y) (g : Γ) (hy : g • y = y),
      g ≠ 1 →
        ∀ (c : AddAction.orbitRel.Quotient (↥(P y).range) E),
          c - (TauCeti.torusFamilyFiberLinearPart R hone hmul P ρ hP hy) c ≠
            TauCeti.torusFamilyFiberTranslationPart P b hb hy
```

## Depends on

- [The affine action](the-affine-action.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCancelSMul_torusFamilyAffineMulAction_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Stabilizer.html#TauCeti.isCancelSMul_torusFamilyAffineMulAction_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.isCancelSMul_torusFamilyAffineMulAction_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Stabilizer.html#TauCeti.isCancelSMul_torusFamilyAffineMulAction_iff)
- [Source of `TauCeti.isCancelSMul_torusFamilyAffineMulAction_iff` in TauCeti/Algebra/Module/ZLattice/Family/Stabilizer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/ZLattice/Family/Stabilizer.lean#L309)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexTori/STATUS.md)
