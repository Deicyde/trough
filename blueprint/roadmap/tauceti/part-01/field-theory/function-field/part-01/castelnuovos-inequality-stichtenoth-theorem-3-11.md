---
declaration: theorem
origin: cited
lean: TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add, TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_isSplitCompletely, TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_perfectField
statement: formalized
proof: formalized
---

# Castelnuovo's inequality (Stichtenoth, Theorem 3.11.3)

Let `F / k` be a function field
with exact constants and a separating element `x`, and let `F₁`, `F₂` be subfields of `F`
containing `k` with `F = F₁ F₂` and `F` finite over both. Then
`g(F) ≤ [F : F₁] g(F₁) + [F : F₂] g(F₂) + ([F : F₁] - 1) ([F : F₂] - 1)`.
The constant field `k` may be imperfect, and neither subextension is assumed separable.

```lean
TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add.{u_1, u_2, u_3, u_4} {k : Type u_1}
  {F₁ : Type u_2} {F₂ : Type u_3} {F : Type u_4} [Field k] [Field F₁] [Field F₂] [Field F]
  [Algebra k F₁] [Algebra k F₂] [Algebra k F] [Algebra F₁ F] [Algebra F₂ F] [IsScalarTower k F₁ F]
  [IsScalarTower k F₂ F] [FiniteDimensional F₁ F] [FiniteDimensional F₂ F]
  (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F) {x : F}
  (hx : Transcendental k x) [Algebra.IsSeparable (↥k⟮x⟯) F]
  (htop : IntermediateField.adjoin F₁ (Set.range ⇑(algebraMap F₂ F)) = ⊤) :
  TauCeti.genus k F ≤
    Module.finrank F₁ F * TauCeti.genus k F₁ + Module.finrank F₂ F * TauCeti.genus k F₂ +
      (Module.finrank F₁ F - 1) * (Module.finrank F₂ F - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](dedekinds-different-theorem-first-part-stichteno.md)
- [The fundamental identity](the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Kummer's theorem (Stichtenoth, Corollary 3.3.8)](kummers-theorem-stichtenoth-corollary-3-3-8.md)
- [Riemann's theorem](../part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../../../algebraic-geometry/algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The weak approximation theorem](../part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/Castelnuovo.html#TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add).

## Other forms

**Castelnuovo's inequality (Stichtenoth, Theorem 3.11.3), from a split place.** Formalized in Tau Ceti as [`TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_isSplitCompletely`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/Castelnuovo.html#TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_isSplitCompletely).

```lean
TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_isSplitCompletely.{u_1, u_2, u_3,
    u_4}
  {k : Type u_1} {F₁ : Type u_2} {F₂ : Type u_3} {F : Type u_4} [Field k] [Field F₁] [Field F₂]
  [Field F] [Algebra k F₁] [Algebra k F₂] [Algebra k F] [Algebra F₁ F] [Algebra F₂ F]
  [IsScalarTower k F₁ F] [IsScalarTower k F₂ F] [FiniteDimensional F₁ F] [FiniteDimensional F₂ F]
  (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F) {P₁ : TauCeti.Place k F₁}
  (hsplit : P₁.IsSplitCompletely)
  (hinj :
    Set.InjOn (fun P => TauCeti.Place.restrict k F₂ P) {P | TauCeti.Place.restrict k F₁ P = P₁})
  (hdeg :
    ∀ (P : TauCeti.Place k F),
      TauCeti.Place.restrict k F₁ P = P₁ → (TauCeti.Place.restrict k F₂ P).degree = 1)
  {T : Set (TauCeti.Place k F₂)} (hT : ∀ Q ∈ T, Q.degree = 1)
  (hcard : ↑(TauCeti.genus k F₂) ≤ T.encard)
  (hdisj :
    ∀ (P : TauCeti.Place k F),
      TauCeti.Place.restrict k F₁ P = P₁ → TauCeti.Place.restrict k F₂ P ∉ T) :
  TauCeti.genus k F ≤
    Module.finrank F₁ F * TauCeti.genus k F₁ + Module.finrank F₂ F * TauCeti.genus k F₂ +
      (Module.finrank F₁ F - 1) * (Module.finrank F₂ F - 1)
```

**Castelnuovo's inequality over a perfect constant field (Stichtenoth, Theorem 3.11.3).** Formalized in Tau Ceti as [`TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_perfectField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/Castelnuovo.html#TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_perfectField).

```lean
TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add_of_perfectField.{u_1, u_2, u_3, u_4}
  {k : Type u_1} {F₁ : Type u_2} {F₂ : Type u_3} {F : Type u_4} [Field k] [Field F₁] [Field F₂]
  [Field F] [Algebra k F₁] [Algebra k F₂] [Algebra k F] [Algebra F₁ F] [Algebra F₂ F]
  [IsScalarTower k F₁ F] [IsScalarTower k F₂ F] [FiniteDimensional F₁ F] [FiniteDimensional F₂ F]
  [PerfectField k] (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  (htop : IntermediateField.adjoin F₁ (Set.range ⇑(algebraMap F₂ F)) = ⊤) :
  TauCeti.genus k F ≤
    Module.finrank F₁ F * TauCeti.genus k F₁ + Module.finrank F₂ F * TauCeti.genus k F₂ +
      (Module.finrank F₁ F - 1) * (Module.finrank F₂ F - 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/Castelnuovo.html#TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add)
- [Source of `TauCeti.genus_le_finrank_mul_genus_add_finrank_mul_genus_add` in TauCeti/FieldTheory/FunctionField/Consequences/Castelnuovo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/Consequences/Castelnuovo.lean#L550)
