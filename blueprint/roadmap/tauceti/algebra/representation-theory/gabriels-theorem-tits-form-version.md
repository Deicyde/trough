---
declaration: theorem
origin: cited
lean: TauCeti.isFiniteRepType_iff_titsForm_posDef, TauCeti.isFiniteRepType_iff_card_hom_add_card_hom_le_one_and_exists_dynkinType_iso, TauCeti.isRepresentationFinite_pathAlgebra_iff_titsForm_posDef
statement: formalized
proof: formalized
---

# Gabriel's theorem, Tits form version

A finite connected quiver has finite
representation type exactly when its Tits form is positive definite.

```lean
TauCeti.isFiniteRepType_iff_titsForm_posDef.{u, v, w} {Q : Type v} [Quiver Q] [Fintype Q]
  [(a b : Q) → Fintype (a ⟶ b)] {k : Type u} [Field k]
  (hconn : (TauCeti.Quiver.underlyingGraph Q).Connected) :
  TauCeti.IsFiniteRepType k Q ↔ (TauCeti.titsForm Q).PosDef
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isFiniteRepType_iff_titsForm_posDef`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.html#TauCeti.isFiniteRepType_iff_titsForm_posDef).

## Other forms

**Gabriel's theorem.** Formalized in Tau Ceti as [`TauCeti.isFiniteRepType_iff_card_hom_add_card_hom_le_one_and_exists_dynkinType_iso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.html#TauCeti.isFiniteRepType_iff_card_hom_add_card_hom_le_one_and_exists_dynkinType_iso).

```lean
TauCeti.isFiniteRepType_iff_card_hom_add_card_hom_le_one_and_exists_dynkinType_iso.{u, v, w}
  {Q : Type v} [Quiver Q] [(a b : Q) → Fintype (a ⟶ b)] {k : Type u} [Field k] [Finite Q]
  (hconn : (TauCeti.Quiver.underlyingGraph Q).Connected) :
  TauCeti.IsFiniteRepType k Q ↔
    (∀ (a b : Q), Fintype.card (a ⟶ b) + Fintype.card (b ⟶ a) ≤ 1) ∧
      ∃ t,
        t.Valid ∧
          t.IsSimplyLaced ∧
            Nonempty (TauCeti.Quiver.underlyingGraph Q ≃g TauCeti.diagramGraph t.cartanMatrix)
```

**Gabriel's theorem for path algebras.** Formalized in Tau Ceti as [`TauCeti.isRepresentationFinite_pathAlgebra_iff_titsForm_posDef`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/FiniteRepType/PathAlgebra.html#TauCeti.isRepresentationFinite_pathAlgebra_iff_titsForm_posDef).

```lean
TauCeti.isRepresentationFinite_pathAlgebra_iff_titsForm_posDef.{u, v, w} (k : Type u) (Q : Type v)
  [Field k] [Quiver Q] [Finite (TauCeti.Quiver.TotalPath Q)] [Fintype Q]
  [(a b : Q) → Fintype (a ⟶ b)] (hconn : (TauCeti.Quiver.underlyingGraph Q).Connected) :
  TauCeti.IsRepresentationFinite (TauCeti.pathAlgebra k Q) ↔ (TauCeti.titsForm Q).PosDef
```

## Sources

- [Tau Ceti documentation: `TauCeti.isFiniteRepType_iff_titsForm_posDef`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.html#TauCeti.isFiniteRepType_iff_titsForm_posDef)
- [Source of `TauCeti.isFiniteRepType_iff_titsForm_posDef` in TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/FiniteRepType/Gabriel.lean#L98)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
