---
declaration: theorem
origin: cited
lean: TauCeti.GroupAlgGeom.isDiscriminatedBy_freeGroup_iff_forall_realize_iff, TauCeti.GroupAlgGeom.isDiscriminatedBy_id_iff_forall_realize_iff_of_freeGroupBasis
statement: formalized
proof: formalized
---

# Remeslennikov's theorem

**Remeslennikov's theorem** for the free group on a type `α`, with constants for its basis: a
group `K` generated over `F(α)` by the images of finitely many variables is discriminated by `F(α)`
over `F(α)` if and only if `K` and `F(α)` satisfy the same universal sentences of the group
language with constants for `α`.

```lean
TauCeti.GroupAlgGeom.isDiscriminatedBy_freeGroup_iff_forall_realize_iff.{u_2, u_5, u_6}
  {K : Type u_2} [Group K] {α : Type u_5} {X : Type u_6} {ιK : FreeGroup α →* K} [Finite X]
  (π : TauCeti.GroupAlgGeom.GHom Monoid.Coprod.inl ιK) (hπ : Function.Surjective ⇑π) :
  TauCeti.GroupAlgGeom.IsDiscriminatedBy ιK (MonoidHom.id (FreeGroup α)) ↔
    ∀ (σ : (FirstOrder.Language.group.withConstants α).Sentence),
      FirstOrder.Language.BoundedFormula.IsUniversal σ → (K ⊨ σ ↔ FreeGroup α ⊨ σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.isDiscriminatedBy_freeGroup_iff_forall_realize_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/UniversalTheory.html#TauCeti.GroupAlgGeom.isDiscriminatedBy_freeGroup_iff_forall_realize_iff).

## Other forms

**Remeslennikov's theorem.** Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.isDiscriminatedBy_id_iff_forall_realize_iff_of_freeGroupBasis`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/UniversalTheory.html#TauCeti.GroupAlgGeom.isDiscriminatedBy_id_iff_forall_realize_iff_of_freeGroupBasis).

```lean
TauCeti.GroupAlgGeom.isDiscriminatedBy_id_iff_forall_realize_iff_of_freeGroupBasis.{u_2, u_5, u_6,
    u_7}
  {K : Type u_2} [Group K] {α : Type u_5} {X : Type u_6} {F : Type u_7} [Group F]
  (b : FreeGroupBasis α F) {ιK : F →* K} [Finite X]
  (π : TauCeti.GroupAlgGeom.GHom Monoid.Coprod.inl ιK) (hπ : Function.Surjective ⇑π) :
  TauCeti.GroupAlgGeom.IsDiscriminatedBy ιK (MonoidHom.id F) ↔
    ∀ (σ : (FirstOrder.Language.group.withConstants α).Sentence),
      FirstOrder.Language.BoundedFormula.IsUniversal σ → (K ⊨ σ ↔ F ⊨ σ)
```

## Sources

- [Tau Ceti documentation: `TauCeti.GroupAlgGeom.isDiscriminatedBy_freeGroup_iff_forall_realize_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/UniversalTheory.html#TauCeti.GroupAlgGeom.isDiscriminatedBy_freeGroup_iff_forall_realize_iff)
- [Source of `TauCeti.GroupAlgGeom.isDiscriminatedBy_freeGroup_iff_forall_realize_iff` in TauCeti/GroupTheory/GroupAlgGeom/UniversalTheory.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/GroupAlgGeom/UniversalTheory.lean#L329)
