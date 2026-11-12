---
catalog: module
lean: Cslib.Algorithms.CCS.VendingMachine.Coin, Cslib.Algorithms.CCS.VendingMachine.Tea, Cslib.Algorithms.CCS.VendingMachine.Coffee, Cslib.Algorithms.CCS.VendingMachine.Constant, Cslib.Algorithms.CCS.VendingMachine.vm, Cslib.Algorithms.CCS.VendingMachine.vendingDefs, Cslib.Algorithms.CCS.VendingMachine.ltsD, Cslib.Algorithms.CCS.VendingMachine.vendingDefsND, Cslib.Algorithms.CCS.VendingMachine.ltsND, Cslib.Algorithms.CCS.VendingMachine.vm_ltsD_ltsND_not_bisim, Cslib.Algorithms.CCS.VendingMachine.modelD, Cslib.Algorithms.CCS.VendingMachine.modelND, Cslib.Algorithms.CCS.VendingMachine.choiceAfterCoin, Cslib.Algorithms.CCS.VendingMachine.vm_modelD_choiceAfterCoin, Cslib.Algorithms.CCS.VendingMachine.vm_modelND_not_choiceAfterCoin
statement: formalized
proof: formalized
---

# Milner's Vending Machine

`Cslib.Algorithms.CCS.VendingMachine`, in [Cslib/Algorithms/CCS/VendingMachine.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean), by Fabrizio Montesi.

> This file formalises Milner's vending machine example for CCS.
>
> We formalise two versions:
> - A machine with a deterministic LTS: `coin.(tea.VM + coffee.VM)`.
> - A machine with a nondeterministic LTS: `coin.tea.VM + coin.coffee.VM`.
>
> We then prove the classical example that the two are not bisimilar.
> We also show the distinction with HML: only the deterministic machine offers the choice of drink
> after a coin is inserted.
>
> Future work on proving that the two vending machines are trace equivalent would be welcome.

> Action names.

`Cslib.Algorithms.CCS.VendingMachine.Coin` (abbreviation, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L40))

> Insert a coin.

```lean
abbrev Coin
```

`Cslib.Algorithms.CCS.VendingMachine.Tea` (abbreviation, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L43))

> Tea request.

```lean
abbrev Tea
```

`Cslib.Algorithms.CCS.VendingMachine.Coffee` (abbreviation, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L46))

> Coffee request.

```lean
abbrev Coffee
```

`Cslib.Algorithms.CCS.VendingMachine.Constant` (inductive type, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L49))

> Constants.

```lean
inductive Constant
  | vm
```

`Cslib.Algorithms.CCS.VendingMachine.vm` (definition, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L54))

> The vending machine process.

```lean
def vm : Process String Constant
```

> ## Deterministic vending machine

`Cslib.Algorithms.CCS.VendingMachine.vendingDefs` (definition, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L60))

> Constant definitions: vm = coin.(tea.VM + coffee.VM)

```lean
def vendingDefs : Constant → Option (Process String Constant)
```

`Cslib.Algorithms.CCS.VendingMachine.ltsD` (abbreviation, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L64))

> The LTS of CCS for the deterministic vending machine.

```lean
abbrev ltsD
```

> ## Nondeterministic vending machine

`Cslib.Algorithms.CCS.VendingMachine.vendingDefsND` (definition, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L73))

> vm = coin.tea.VM + coin.coffee.VM

```lean
def vendingDefsND : Constant → Option (Process String Constant)
```

`Cslib.Algorithms.CCS.VendingMachine.ltsND` (abbreviation, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L77))

> The LTS of CCS for the nondeterministic vending machine.

```lean
abbrev ltsND
```

`Cslib.Algorithms.CCS.VendingMachine.vm_ltsD_ltsND_not_bisim` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L82))

> The deterministic and nondeterministic vending machines are not bisimilar.

```lean
theorem vm_ltsD_ltsND_not_bisim : ¬(vm ~[ltsD, ltsND] vm)
```

> ## HML properties of the two vending machines

`Cslib.Algorithms.CCS.VendingMachine.modelD` (definition, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L105))

> HML model for the deterministic machine with no atomic propositions.

```lean
def modelD : HML.Model (Process String Constant) (Act String) Empty
```

`Cslib.Algorithms.CCS.VendingMachine.modelND` (definition, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L109))

> HML model for the nondeterministic machine with no atomic propositions.

```lean
def modelND : HML.Model (Process String Constant) (Act String) Empty
```

`Cslib.Algorithms.CCS.VendingMachine.choiceAfterCoin` (definition, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L114))

> After inserting a coin, it is possible to choose between tea and coffee.

```lean
def choiceAfterCoin : HML.Proposition (Act String) Empty
```

`Cslib.Algorithms.CCS.VendingMachine.vm_modelD_choiceAfterCoin` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L116))

```lean
theorem vm_modelD_choiceAfterCoin : ⇓HML[modelD,vm ⊨ choiceAfterCoin]
```

`Cslib.Algorithms.CCS.VendingMachine.vm_modelND_not_choiceAfterCoin` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean#L121))

```lean
theorem vm_modelND_not_choiceAfterCoin : ¬⇓HML[modelND,vm ⊨ choiceAfterCoin]
```

## Depends on

- [Semantics of CCS](../../languages/ccs/semantics.md)
- [Hennessy-Milner Logic (HML)](../../logics/hml/basic.md)

## Sources

- [Cslib/Algorithms/CCS/VendingMachine.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/CCS/VendingMachine.lean)
