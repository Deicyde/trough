---
catalog: module
lean: Cslib.Logic.PL.NaturalDeduction.instIsIntuitionisticND₁, Cslib.Logic.PL.NaturalDeduction.derivBotImpCtx, Cslib.Logic.PL.NaturalDeduction.contra, Cslib.Logic.PL.NaturalDeduction.instIsClassicalCPL, Cslib.Logic.PL.NaturalDeduction.byContra, Cslib.Logic.PL.NaturalDeduction.lem, Cslib.Logic.PL.NaturalDeduction.peirce, Cslib.Logic.PL.NaturalDeduction.instIsClassicalLEM, Cslib.Logic.PL.NaturalDeduction.instIsClassicalPeirce
statement: formalized
proof: formalized
---

# Auxilliary results on natural deduction

`Cslib.Logics.Propositional.NaturalDeduction.Lemmas`, in [Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean), by Thomas Waring.

> In this file we prove the expected results that `ND₁ T` is always intuitionistic, and that various
> axiomatisations of classical logic (`CPL Atom` using double-negation elimination, `LEM Atom` using
> the law of excluded middle, and `Peirce Atom` using Peirce's law) are classical inference systems.
> We provide derived rules for common intuitionistic and classical proof patterns.

`Cslib.Logic.PL.NaturalDeduction.instIsIntuitionisticND₁` (instance, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L29))

```lean
instance instIsIntuitionisticND₁ : IsIntuitionistic (ND₁ T) (Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.derivBotImpCtx` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L33))

> Derivation of efq in an arbitrary context.

```lean
def derivBotImpCtx (Γ : Ctx Atom) (A : Proposition Atom) : (ND T)⇓(Γ ⊢ ⊥ → A)
```

`Cslib.Logic.PL.NaturalDeduction.contra` (definition, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L37))

> Prove any proposition from contradictory hypotheses.

```lean
def contra {Γ : Ctx Atom} (A B : Proposition Atom)
    (hΓ : A ∈ Γ := by membership) (hΓ' : (¬A) ∈ Γ := by membership) : (ND T)⇓(Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.instIsClassicalCPL` (instance, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L41))

```lean
instance instIsClassicalCPL : IsClassical (ND₁ <| CPL Atom) (Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.byContra` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L45))

> Proof by contradiction as a derived rule.

```lean
def byContra [IsClassical (ND₁ T) (Proposition Atom)] {Γ : Ctx Atom}
    {A : Proposition Atom} (D : (ND T)⇓(insert (¬ A) Γ ⊢ ⊥)) : (ND T)⇓(Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.lem` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L50))

> Law of excluded middle in a classical theory.

```lean
def lem [IsClassical (ND₁ T) (Proposition Atom)] (A : Proposition Atom) : (ND₁ T)⇓(A ∨ ¬ A)
```

`Cslib.Logic.PL.NaturalDeduction.peirce` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L57))

> Peirce's law in a classical theory.

```lean
def peirce [IsClassical (ND₁ T) (Proposition Atom)] (A B : Proposition Atom) :
    (ND₁ T)⇓(((A → B) → A) → A)
```

`Cslib.Logic.PL.NaturalDeduction.instIsClassicalLEM` (instance, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L64))

```lean
instance instIsClassicalLEM : IsClassical (ND₁ <| LEM Atom) (Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.instIsClassicalPeirce` (instance, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean#L71))

```lean
instance instIsClassicalPeirce : IsClassical (ND₁ <| Peirce Atom) (Proposition Atom)
```

## Depends on

- [API for inference systems](../../../foundations/logic/inferencesystem/basic.md)
- [Natural deduction for propositional logic](basic.md)

## Sources

- [Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Propositional/NaturalDeduction/Lemmas.lean)
