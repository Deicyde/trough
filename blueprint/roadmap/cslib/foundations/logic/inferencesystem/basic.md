---
catalog: module
lean: Cslib.Logic.InferenceSystem.IsIntuitionistic, Cslib.Logic.InferenceSystem.derivableIn_bot_imp, Cslib.Logic.InferenceSystem.IsClassical, Cslib.Logic.InferenceSystem.derivableIn_dne
statement: formalized
proof: formalized
---

# API for inference systems

`Cslib.Foundations.Logic.InferenceSystem.Basic`, in [Cslib/Foundations/Logic/InferenceSystem/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Basic.lean), by Thomas Waring.

`Cslib.Logic.InferenceSystem.IsIntuitionistic` (class, [line 19](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Basic.lean#L19))

> Intuitionistic inference systems derive the principle of explosion.

```lean
class IsIntuitionistic (S α : Type*) [Bot α] [HasImp α] [InferenceSystem S α] where
  /-- A chosen derivation of `⊥ → a`. -/
  derivationBotImp (a : α) : S⇓(⊥ → a)
```

`Cslib.Logic.InferenceSystem.derivableIn_bot_imp` (lemma, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Basic.lean#L23))

```lean
lemma derivableIn_bot_imp {S α : Type*} [Bot α] [HasImp α] [InferenceSystem S α]
    [IsIntuitionistic S α] (a : α) : DerivableIn S (⊥ → a)
```

`Cslib.Logic.InferenceSystem.IsClassical` (class, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Basic.lean#L28))

> Classical inference systems derive double-negation elimination.

```lean
class IsClassical (S α : Type*) [HasNot α] [HasImp α] [InferenceSystem S α] where
  /-- A chosen derivation of `¬¬a → a`. -/
  derivationDNE (a : α) : S⇓(¬¬a → a)
```

`Cslib.Logic.InferenceSystem.derivableIn_dne` (lemma, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Basic.lean#L32))

```lean
lemma derivableIn_dne {S α : Type*} [HasNot α] [HasImp α] [InferenceSystem S α]
    [IsClassical S α] (a : α) : DerivableIn S (¬¬a → a)
```

## Depends on

- [Inference systems](defs.md)
- [Logical operators](../operators.md)

## Sources

- [Cslib/Foundations/Logic/InferenceSystem/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Logic/InferenceSystem/Basic.lean)
