---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.ComponentIdx.dropPair, TensorSpecies.Tensor.ComponentIdx.DropPairSection, TensorSpecies.Tensor.ComponentIdx.DropPairSection.mem_iff_apply_succSuccAbove_eq, TensorSpecies.Tensor.ComponentIdx.DropPairSection.mem_self_of_dropPair, TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin, TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin_apply_fst, TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin_apply_snd, TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin_mem_succSuccAboveSection
statement: formalized
proof: formalized
---

# Contractions of component indices

The module `Physlib.Relativity.Tensors.ComponentIdx.Contraction`, [Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean): 12 declarations, 5 with a docstring.

## i. Overview

> This file contains the component-index API induced by dropping a pair of contracted
> indices from a tensor.
>
> The constructions here describe how component indices restrict along
> `Fin.succSuccAbove`, and how the fiber of this restriction is equivalent to the two
> component choices at the contracted positions.

## ii. Key results

> - `TensorSpecies.Tensor.ComponentIdx.dropPair` restricts a component index by dropping
>   two positions.
> - `TensorSpecies.Tensor.ComponentIdx.DropPairSection` is the finite set of component
>   indices mapping to a fixed restricted component index.
> - `TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFinEquiv` identifies a
>   `DropPairSection` with the two basis indices at the dropped positions.

## iv. References

> * None.

## A. Dropping a pair

**`TensorSpecies.Tensor.ComponentIdx.dropPair`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L64).

> The `ComponentIdx` obtained by dropping two components.

```lean
def dropPair {n : ℕ} {c : Fin (n + 1 + 1) → C}
    (i j : Fin (n + 1 + 1)) (b : ComponentIdx (S := S) c) :
    ComponentIdx (S := S) (c ∘ Fin.succSuccAbove i j)
```

## B. Sections of the drop-pair map

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L78).

> Given a coordinate parameter
> `b : Π k, Fin (S.repDim ((c ∘ i.succAbove ∘ j.succAbove) k)))`, the
> coordinate parameter `Π k, Fin (S.repDim (c k))` which map down to `b`.

```lean
def DropPairSection {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i : Fin (n + 1 + 1)} {j : Fin (n + 1 + 1)}
    (b : ComponentIdx (S := S) (c ∘ Fin.succSuccAbove i j)) :
    Finset (ComponentIdx (S := S) c)
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.mem_iff_apply_succSuccAbove_eq`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L86).

```lean
lemma mem_iff_apply_succSuccAbove_eq {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)}
    (b : ComponentIdx (c ∘ Fin.succSuccAbove i j))
    (b' : ComponentIdx c) :
    b' ∈ DropPairSection (S := S) b ↔
      ∀ m, b' (Fin.succSuccAbove i j m) = b m
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.mem_self_of_dropPair`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L97).

```lean
lemma mem_self_of_dropPair {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)}
    (b : ComponentIdx (c)) :
    b ∈ DropPairSection (S := S) (b.dropPair i j)
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L106).

> Given a `b` in `ComponentIdx (c ∘ Fin.succSuccAbove i j))` and
> an `x` in `Fin (S.repDim (c i)) × Fin (S.repDim (c j))`, the corresponding
> coordinate parameter in `ComponentIdx c`.

```lean
def ofFin {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (b : ComponentIdx (S := S) (c ∘ Fin.succSuccAbove i j))
    (x : basisIdx (c i) × basisIdx (c j)) :
    ComponentIdx (S := S) c
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin_apply_fst`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L117).

```lean
lemma ofFin_apply_fst {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (b : ComponentIdx (c ∘ Fin.succSuccAbove i j))
    (x : basisIdx (c i) × basisIdx (c j)) :
    ofFin (S := S) hij b x i = x.1
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin_apply_snd`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L124).

```lean
lemma ofFin_apply_snd {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (b : ComponentIdx (c ∘ Fin.succSuccAbove i j))
    (x : basisIdx (c i) × basisIdx (c j)) :
    ofFin (S := S) hij b x j = x.2
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFin_mem_succSuccAboveSection`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L132).

```lean
lemma ofFin_mem_succSuccAboveSection {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (b : ComponentIdx (c ∘ Fin.succSuccAbove i j))
    (x : basisIdx (c i) × basisIdx (c j)) :
    ofFin (S := S) hij b x ∈ DropPairSection b
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFinEquiv`**, a def, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L146).

> The equivalence between `ContrSection b` and
> `basisIdx (c i) × basisIdx (c j)`.

```lean
def ofFinEquiv {n : ℕ} {c : Fin n.succ.succ → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j)
    (b : ComponentIdx (c ∘ Fin.succSuccAbove i j)) :
    basisIdx (c i) × basisIdx (c j) ≃ DropPairSection (S := S) b
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFinEquiv_apply_fst`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L169).

```lean
lemma ofFinEquiv_apply_fst {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (b : ComponentIdx (c ∘ Fin.succSuccAbove i j))
    (x : basisIdx (c i) × basisIdx (c j)) :
    (ofFinEquiv (S := S) hij b x).1 i = x.1
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFinEquiv_apply_snd`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L176).

```lean
lemma ofFinEquiv_apply_snd {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (b : ComponentIdx (c ∘ Fin.succSuccAbove i j))
    (x : basisIdx (c i) × basisIdx (c j)) :
    (ofFinEquiv (S := S) hij b x).1 j = x.2
```

**`TensorSpecies.Tensor.ComponentIdx.DropPairSection.ofFinEquiv_dropPair`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean#L184).

> Restoring the two entries dropped from a component index recovers that component index.

```lean
lemma ofFinEquiv_dropPair {n : ℕ} {c : Fin (n + 1 + 1) → C}
    {i j : Fin (n + 1 + 1)} (hij : i ≠ j) (r : ComponentIdx (S := S) c) :
    (ofFinEquiv (S := S) hij (r.dropPair i j) (r i, r j)).1 = r
```

## Depends on

- [Component indices](componentidx-basic.md)
- [Defining succSuccAbove](../part-03/contraction-succsuccabove.md)

## Sources

- [Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComponentIdx/Contraction.lean)
