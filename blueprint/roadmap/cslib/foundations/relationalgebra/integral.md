---
catalog: module
lean: Cslib.RelationAlgebra.IsIntegral.relDom_eq_one, Cslib.RelationAlgebra.isIntegral_iff_forall_relDom, Cslib.RelationAlgebra.IsIntegral.relCod_eq_one, Cslib.RelationAlgebra.isIntegral_iff_forall_relCod, Cslib.RelationAlgebra.IsIntegral.mul_eq_bot_iff, Cslib.RelationAlgebra.isIntegral_tfae
statement: formalized
proof: formalized
---

# Integral relation algebras

`Cslib.Foundations.RelationAlgebra.Integral`, in [Cslib/Foundations/RelationAlgebra/Integral.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean), by Thomas Waring.

`Cslib.RelationAlgebra.IsIntegral.relDom_eq_one` (lemma, [line 19](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean#L19))

```lean
lemma IsIntegral.relDom_eq_one (h : IsIntegral α) (ha : a ≠ ⊥) : relDom a = 1
```

`Cslib.RelationAlgebra.isIntegral_iff_forall_relDom` (theorem, [line 25](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean#L25))

> A relation algebra is integral iff it is nontrivial, and every non-bot element has full
> domain.

```lean
theorem isIntegral_iff_forall_relDom :
    IsIntegral α ↔ Nontrivial α ∧ ∀ a : α, a ≠ ⊥ → relDom a = 1
```

`Cslib.RelationAlgebra.IsIntegral.relCod_eq_one` (lemma, [line 35](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean#L35))

```lean
lemma IsIntegral.relCod_eq_one (h : IsIntegral α) (ha : a ≠ ⊥) : relCod a = 1
```

`Cslib.RelationAlgebra.isIntegral_iff_forall_relCod` (theorem, [line 41](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean#L41))

> A relation algebra is integral iff it is nontrivial, and every non-bot element has full
> codomain.

```lean
theorem isIntegral_iff_forall_relCod :
    IsIntegral α ↔ Nontrivial α ∧ ∀ a : α, a ≠ ⊥ → relCod a = 1
```

`Cslib.RelationAlgebra.IsIntegral.mul_eq_bot_iff` (lemma, [line 48](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean#L48))

```lean
lemma IsIntegral.mul_eq_bot_iff (h : IsIntegral α) : a * b = ⊥ ↔ a = ⊥ ∨ b = ⊥
```

`Cslib.RelationAlgebra.isIntegral_tfae` (theorem, [line 58](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean#L58))

```lean
theorem isIntegral_tfae (α : Type*) [RelationAlgebra α] [Nontrivial α] :
    [IsIntegral α, ∀ a b : α, a * b = ⊥ → a = ⊥ ∨ b = ⊥,
      ∀ a : α, a ≠ ⊥ → relDom a = 1, ∀ a : α, a ≠ ⊥ → relCod a = 1,
      ∀ a : α, a ≠ ⊥ → a * ⊤ = ⊤, ∀ a : α, a ≠ ⊥ → ⊤ * a = ⊤].TFAE
```

## Depends on

- [Element properties for relation algebras](specialelements.md)

## Sources

- [Cslib/Foundations/RelationAlgebra/Integral.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/RelationAlgebra/Integral.lean)
- [Declaration ledger](../../../../sources/cslib/Cslib.Foundations.RelationAlgebra.Integral.json)
