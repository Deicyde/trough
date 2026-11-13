---
declaration: module
origin: cited
lean: Lorentz.ComplexVector, Lorentz.ComplexVector.toFin13ℂFun, Lorentz.ComplexVector.toFin13ℂAddEquiv, Lorentz.ComplexVector.ext, Lorentz.ComplexVector.val_add, Lorentz.ComplexVector.val_smul, Lorentz.ComplexVector.toFin13ℂEquiv, Lorentz.ComplexVector.toFin13ℂ
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.ComplexTensor.Vector.Modules

The module `Physlib.Relativity.Tensors.ComplexTensor.Vector.Modules`, [Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean): 26 declarations (6 instances with no name), 20 with a docstring.

## Modules associated with complex Lorentz vectors

> We define the modules underlying complex Lorentz vectors.
> These definitions are preludes to the definitions of
> `Lorentz.complexContr` and `Lorentz.complexCo`.

**`Lorentz.ComplexVector`**, a structure, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L29).

> The module for contravariant (up-index) complex Lorentz vectors.

```lean
structure ComplexVector where
  /-- The underlying value as a vector `Fin 1 ⊕ Fin 3 → ℂ`. -/
  val : Fin 1 ⊕ Fin 3 → ℂ
```

**`Lorentz.ComplexVector.toFin13ℂFun`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L36).

> The equivalence between `ComplexVector` and `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
def toFin13ℂFun : ComplexVector ≃ (Fin 1 ⊕ Fin 3 → ℂ)
```

**An instance with no name**, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L44).

> The instance of `AddCommMonoid` on `ComplexVector` defined via its equivalence
> with `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
instance : AddCommMonoid ComplexVector
```

**An instance with no name**, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L48).

> The instance of `AddCommGroup` on `ComplexVector` defined via its equivalence
> with `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
instance : AddCommGroup ComplexVector
```

**`Lorentz.ComplexVector.toFin13ℂAddEquiv`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L51).

> The additive equivalence between `ComplexVector` and `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
def toFin13ℂAddEquiv : ComplexVector ≃+ (Fin 1 ⊕ Fin 3 → ℂ)
```

**An instance with no name**, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L56).

> The instance of `Module` on `ComplexVector` defined via its equivalence
> with `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
instance : Module ℂ ComplexVector
```

**`Lorentz.ComplexVector.ext`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L59).

```lean
lemma ext (ψ ψ' : ComplexVector) (h : ψ.val = ψ'.val) : ψ = ψ'
```

**`Lorentz.ComplexVector.val_add`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L66).

```lean
lemma val_add (ψ ψ' : ComplexVector) : (ψ + ψ').val = ψ.val + ψ'.val
```

**`Lorentz.ComplexVector.val_smul`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L69).

```lean
lemma val_smul (r : ℂ) (ψ : ComplexVector) : (r • ψ).val = r • ψ.val
```

**`Lorentz.ComplexVector.toFin13ℂEquiv`**, a def, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L73).

> The linear equivalence between `ComplexVector` and `(Fin 1 ⊕ Fin 3 → ℂ)`.

```lean
def toFin13ℂEquiv : ComplexVector ≃ₗ[ℂ] (Fin 1 ⊕ Fin 3 → ℂ)
```

**`Lorentz.ComplexVector.toFin13ℂ`**, an abbrev, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L78).

> The underlying element of `Fin 1 ⊕ Fin 3 → ℂ` of a element in `ComplexVector` defined
> through the linear equivalence `toFin13ℂEquiv`.

```lean
abbrev toFin13ℂ (ψ : ComplexVector)
```

**`Lorentz.ComplexVector.lorentzGroupRep`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L81).

> The representation of the Lorentz group on `ComplexVector`.

```lean
def lorentzGroupRep : Representation ℂ (LorentzGroup 3) ComplexVector
```

**`Lorentz.ComplexVector.SL2CRep`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L99).

> The representation of the SL(2, ℂ) on `ComplexVector` induced by the representation of the
> Lorentz group.

```lean
def SL2CRep : Representation ℂ SL(2, ℂ) ComplexVector
```

**`Lorentz.ComplexCoVector`**, a structure, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L105).

> The module for covariant (up-index) complex Lorentz vectors.

```lean
structure ComplexCoVector where
  /-- The underlying value as a vector `Fin 1 ⊕ Fin 3 → ℂ`. -/
  val : Fin 1 ⊕ Fin 3 → ℂ
```

**`Lorentz.ComplexCoVector.toFin13ℂFun`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L112).

> The equivalence between `ComplexCoVector` and `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
def toFin13ℂFun : ComplexCoVector ≃ (Fin 1 ⊕ Fin 3 → ℂ)
```

**An instance with no name**, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L120).

> The instance of `AddCommMonoid` on `ComplexCoVector` defined via its equivalence
> with `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
instance : AddCommMonoid ComplexCoVector
```

**An instance with no name**, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L124).

> The instance of `AddCommGroup` on `ComplexCoVector` defined via its equivalence
> with `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
instance : AddCommGroup ComplexCoVector
```

**`Lorentz.ComplexCoVector.toFin13ℂAddEquiv`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L127).

> The additive equivalence between `ComplexCoVector` and `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
def toFin13ℂAddEquiv : ComplexCoVector ≃+ (Fin 1 ⊕ Fin 3 → ℂ)
```

**An instance with no name**, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L132).

> The instance of `Module` on `ComplexCoVector` defined via its equivalence
> with `Fin 1 ⊕ Fin 3 → ℂ`.

```lean
instance : Module ℂ ComplexCoVector
```

**`Lorentz.ComplexCoVector.ext`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L135).

```lean
lemma ext (ψ ψ' : ComplexCoVector) (h : ψ.val = ψ'.val) : ψ = ψ'
```

**`Lorentz.ComplexCoVector.val_add`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L142).

```lean
lemma val_add (ψ ψ' : ComplexCoVector) : (ψ + ψ').val = ψ.val + ψ'.val
```

**`Lorentz.ComplexCoVector.val_smul`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L145).

```lean
lemma val_smul (r : ℂ) (ψ : ComplexCoVector) : (r • ψ).val = r • ψ.val
```

**`Lorentz.ComplexCoVector.toFin13ℂEquiv`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L149).

> The linear equivalence between `ComplexCoVector` and `(Fin 1 ⊕ Fin 3 → ℂ)`.

```lean
def toFin13ℂEquiv : ComplexCoVector ≃ₗ[ℂ] (Fin 1 ⊕ Fin 3 → ℂ)
```

**`Lorentz.ComplexCoVector.toFin13ℂ`**, an abbrev, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L154).

> The underlying element of `Fin 1 ⊕ Fin 3 → ℂ` of a element in `ComplexCoVector` defined
> through the linear equivalence `toFin13ℂEquiv`.

```lean
abbrev toFin13ℂ (ψ : ComplexCoVector)
```

**`Lorentz.ComplexCoVector.lorentzGroupRep`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L157).

> The representation of the Lorentz group on `ComplexCoVector`.

```lean
def lorentzGroupRep : Representation ℂ (LorentzGroup 3) ComplexCoVector
```

**`Lorentz.ComplexCoVector.SL2CRep`**, a def, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean#L180).

> The representation of the SL(2, ℂ) on `ComplexCoVector` induced by the representation of the
> Lorentz group.

```lean
def SL2CRep : Representation ℂ SL(2, ℂ) ComplexCoVector
```

## Depends on

- [The group SL(2, ℂ) and it's relation to the Lorentz group](../../sl2c/basic.md)

## Sources

- [Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/ComplexTensor/Vector/Modules.lean)
