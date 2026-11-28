---
catalog: module
lean: Cslib.Logic.PL.NaturalDeduction.instIsIntuitionisticND₁, Cslib.Logic.PL.NaturalDeduction.derivBotImpCtx, Cslib.Logic.PL.NaturalDeduction.contra, Cslib.Logic.PL.NaturalDeduction.instIsClassicalCPL, Cslib.Logic.PL.NaturalDeduction.byContra, Cslib.Logic.PL.NaturalDeduction.lem, Cslib.Logic.PL.NaturalDeduction.peirce, Cslib.Logic.PL.NaturalDeduction.instIsClassicalLEM, Cslib.Logic.PL.NaturalDeduction.instIsClassicalPeirce, Cslib.Logic.PL.NaturalDeduction.Derivation.collectAx, Cslib.Logic.PL.NaturalDeduction.derivableIn_collect_ax, Cslib.Logic.PL.NaturalDeduction.Derivation.assToAx', Cslib.Logic.PL.NaturalDeduction.Derivation.assToAx, Cslib.Logic.PL.NaturalDeduction.derivableIn_ass_to_ax, Cslib.Logic.PL.NaturalDeduction.Derivation.axToAss, Cslib.Logic.PL.NaturalDeduction.derivableIn_ax_to_ass, Cslib.Logic.PL.NaturalDeduction.derivableIn_union_ax_iff_ctx, Cslib.Logic.PL.NaturalDeduction.derivableIn_iff_exists, Cslib.Logic.PL.NaturalDeduction.derivableIn_nd₁_iff_exists
statement: formalized
proof: formalized
---

# Auxilliary results on natural deduction

`Cslib.Logics.Propositional.NaturalDeduction.Lemmas`, in [Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean), by Thomas Waring.

> In this file we prove the expected results that `ND₁ T` is always intuitionistic, and that various
> axiomatisations of classical logic (`CPL Atom` using double-negation elimination, `LEM Atom` using
> the law of excluded middle, and `Peirce Atom` using Peirce's law) are classical inference systems.
> We provide derived rules for common intuitionistic and classical proof patterns.

> ### Classes of inference systems

`Cslib.Logic.PL.NaturalDeduction.instIsIntuitionisticND₁` (instance, [line 31](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L31))

```lean
instance instIsIntuitionisticND₁ : IsIntuitionistic (ND₁ T) (Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.derivBotImpCtx` (definition, [line 35](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L35))

> Derivation of efq in an arbitrary context.

```lean
def derivBotImpCtx (Γ : Ctx Atom) (A : Proposition Atom) : (ND T)⇓(Γ ⊢ ⊥ → A)
```

`Cslib.Logic.PL.NaturalDeduction.contra` (definition, [line 39](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L39))

> Prove any proposition from contradictory hypotheses.

```lean
def contra {Γ : Ctx Atom} (A B : Proposition Atom)
    (hΓ : A ∈ Γ := by membership) (hΓ' : (¬A) ∈ Γ := by membership) : (ND T)⇓(Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.instIsClassicalCPL` (instance, [line 43](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L43))

```lean
instance instIsClassicalCPL : IsClassical (ND₁ <| CPL Atom) (Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.byContra` (definition, [line 47](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L47))

> Proof by contradiction as a derived rule.

```lean
def byContra [IsClassical (ND₁ T) (Proposition Atom)] {Γ : Ctx Atom}
    {A : Proposition Atom} (D : (ND T)⇓(insert (¬ A) Γ ⊢ ⊥)) : (ND T)⇓(Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.lem` (definition, [line 52](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L52))

> Law of excluded middle in a classical theory.

```lean
def lem [IsClassical (ND₁ T) (Proposition Atom)] (A : Proposition Atom) : (ND₁ T)⇓(A ∨ ¬ A)
```

`Cslib.Logic.PL.NaturalDeduction.peirce` (definition, [line 59](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L59))

> Peirce's law in a classical theory.

```lean
def peirce [IsClassical (ND₁ T) (Proposition Atom)] (A B : Proposition Atom) :
    (ND₁ T)⇓(((A → B) → A) → A)
```

`Cslib.Logic.PL.NaturalDeduction.instIsClassicalLEM` (instance, [line 66](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L66))

```lean
instance instIsClassicalLEM : IsClassical (ND₁ <| LEM Atom) (Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.instIsClassicalPeirce` (instance, [line 73](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L73))

```lean
instance instIsClassicalPeirce : IsClassical (ND₁ <| Peirce Atom) (Proposition Atom)
```

> ### Further operations on deductions

`Cslib.Logic.PL.NaturalDeduction.Derivation.collectAx` (definition, [line 84](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L84))

> Move the axioms used in a derivation `D` to the context, obtaining a derivation in
> intuitionistic logic.

```lean
def Derivation.collectAx {Γ : Ctx Atom} {B : Proposition Atom} :
    (Derivation T Γ B) → Σ Δ : {Δ : Ctx Atom // ↑Δ ⊆ T}, Derivation (IPL Atom) (Γ ∪ Δ) B
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_collect_ax` (theorem, [line 108](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L108))

```lean
theorem derivableIn_collect_ax {Γ : Ctx Atom}
    {B : Proposition Atom} : DerivableIn (ND T) (Γ ⊢ B) →
      ∃ Δ : Ctx Atom, DerivableIn (ND <| IPL Atom) ((Γ ∪ Δ) ⊢ B) ∧ ↑Δ ⊆ T
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.assToAx'` (definition, [line 114](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L114))

> Remove some assumptions by moving them to the axiom set.

```lean
def Derivation.assToAx' {Γ Δ : Ctx Atom} {B : Proposition Atom} :
    Derivation T Γ B → Derivation (T ∪ Δ) (Γ \ Δ) B
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.assToAx` (definition, [line 135](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L135))

> Remove dependence on some assumptions by adding them to the theory.

```lean
def Derivation.assToAx {Γ Δ : Ctx Atom} {B : Proposition Atom}
    (D : Derivation T (Γ ∪ Δ) B) : Derivation (T ∪ Δ) Γ B
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_ass_to_ax` (theorem, [line 138](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L138))

```lean
theorem derivableIn_ass_to_ax {Γ Δ : Ctx Atom}
    {B : Proposition Atom} : DerivableIn (ND T) ((Γ ∪ Δ) ⊢ B) → DerivableIn (ND <| T ∪ Δ) (Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.axToAss` (definition, [line 143](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L143))

> Move a finset of axioms to the context.

```lean
def Derivation.axToAss {Γ Δ : Ctx Atom} {B : Proposition Atom}
    (D : (ND <| T ∪ Δ)⇓(Γ ⊢ B)) : (ND T)⇓((Γ ∪ Δ) ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_ax_to_ass` (theorem, [line 148](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L148))

```lean
theorem derivableIn_ax_to_ass {Γ Δ : Ctx Atom}
    {B : Proposition Atom} : DerivableIn (ND <| T ∪ Δ) (Γ ⊢ B) → DerivableIn (ND T) ((Γ ∪ Δ) ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_union_ax_iff_ctx` (theorem, [line 152](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L152))

```lean
theorem derivableIn_union_ax_iff_ctx {Γ Δ : Ctx Atom} {B : Proposition Atom} :
    DerivableIn (ND <| T ∪ Δ) (Γ ⊢ B) ↔ DerivableIn (ND T) ((Γ ∪ Δ) ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_iff_exists` (theorem, [line 156](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L156))

```lean
theorem derivableIn_iff_exists {Γ : Ctx Atom} {B : Proposition Atom} :
    DerivableIn (ND T) (Γ ⊢ B) ↔
      ∃ Δ : Ctx Atom, DerivableIn (ND <| IPL Atom) ((Γ ∪ Δ) ⊢ B) ∧ ↑Δ ⊆ T
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_nd₁_iff_exists` (theorem, [line 161](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L161))

```lean
theorem derivableIn_nd₁_iff_exists {A : Proposition Atom} :
    DerivableIn (ND₁ T) A ↔ ∃ Γ : Ctx Atom, DerivableIn (ND <| IPL Atom) (Γ ⊢ A) ∧ ↑Γ ⊆ T
```

## Depends on

- [API for inference systems](../../../foundations/logic/inferencesystem/basic.md)
- [Natural deduction for propositional logic](basic.md)

## Sources

- [Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Logics.Propositional.NaturalDeduction.Lemmas.json)
