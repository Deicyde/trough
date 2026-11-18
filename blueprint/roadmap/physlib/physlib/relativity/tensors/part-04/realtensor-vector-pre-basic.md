---
declaration: module
origin: cited
lean: Lorentz.contrBasis, Lorentz.contrBasis_ρ_apply, Lorentz.contrBasis_toFin1dℝ, Lorentz.contrBasis_repr_apply, Lorentz.contrBasisFin, Lorentz.contrBasisFin_toFin1dℝ, Lorentz.contrBasisFin_repr_apply, Lorentz.continuous_contr
statement: formalized
proof: formalized
---

# Real Lorentz vectors

The module `Physlib.Relativity.Tensors.RealTensor.Vector.Pre.Basic`, [Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean): 20 declarations, 7 with a docstring.

> We define real Lorentz vectors in as representations of the Lorentz group.

**`Lorentz.contrBasis`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L28).

> The standard basis of contravariant Lorentz vectors.

```lean
def contrBasis (d : ℕ := 3) : Basis (Fin 1 ⊕ Fin d) ℝ (ContrMod d)
```

**`Lorentz.contrBasis_ρ_apply`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L32).

```lean
lemma contrBasis_ρ_apply {d : ℕ} (M : LorentzGroup d) (i j : Fin 1 ⊕ Fin d) :
    (LinearMap.toMatrix (contrBasis d) (contrBasis d)) (ContrMod.rep M) i j =
    M.1 i j
```

**`Lorentz.contrBasis_toFin1dℝ`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L41).

```lean
lemma contrBasis_toFin1dℝ {d : ℕ} (i : Fin 1 ⊕ Fin d) :
    (contrBasis d i).toFin1dℝ = Pi.single i 1
```

**`Lorentz.contrBasis_repr_apply`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L46).

```lean
lemma contrBasis_repr_apply {d : ℕ} (p : ContrMod d) (i : Fin 1 ⊕ Fin d) :
    (contrBasis d).repr p i = p.val i
```

**`Lorentz.contrBasisFin`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L52).

> The standard basis of contravariant Lorentz vectors indexed by `Fin (1 + d)`.

```lean
def contrBasisFin (d : ℕ := 3) : Basis (Fin (1 + d)) ℝ (ContrMod d)
```

**`Lorentz.contrBasisFin_toFin1dℝ`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L56).

```lean
lemma contrBasisFin_toFin1dℝ {d : ℕ} (i : Fin (1 + d)) :
    (contrBasisFin d i).toFin1dℝ = Pi.single (finSumFinEquiv.symm i) 1
```

**`Lorentz.contrBasisFin_repr_apply`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L60).

```lean
lemma contrBasisFin_repr_apply {d : ℕ} (p : ContrMod d) (i : Fin (1 + d)) :
    (contrBasisFin d).repr p i = p.val (finSumFinEquiv.symm i)
```

**`Lorentz.continuous_contr`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L63).

```lean
lemma continuous_contr {T : Type} [TopologicalSpace T] (f : T → ContrMod d)
    (h : Continuous (fun i => (f i).toFin1dℝ)) : Continuous f
```

**`Lorentz.contr_continuous`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L67).

```lean
lemma contr_continuous {T : Type} [TopologicalSpace T] (f : ContrMod d → T)
    (h : Continuous (f ∘ (@ContrMod.toFin1dℝEquiv d).symm)) : Continuous f
```

**`Lorentz.coBasis`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L75).

> The standard basis of contravariant Lorentz vectors.

```lean
def coBasis (d : ℕ := 3) : Basis (Fin 1 ⊕ Fin d) ℝ (CoMod d)
```

**`Lorentz.coBasis_ρ_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L79).

```lean
lemma coBasis_ρ_apply {d : ℕ} (M : LorentzGroup d) (i j : Fin 1 ⊕ Fin d) :
    (LinearMap.toMatrix (coBasis d) (coBasis d)) (CoMod.rep M) i j =
    M⁻¹ᵀ i j
```

**`Lorentz.coBasis_repr_apply`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L87).

```lean
lemma coBasis_repr_apply {d : ℕ} (p : CoMod d) (i : Fin 1 ⊕ Fin d) :
    (coBasis d).repr p i = p.val i
```

**`Lorentz.coBasis_toFin1dℝ`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L93).

```lean
lemma coBasis_toFin1dℝ {d : ℕ} (i : Fin 1 ⊕ Fin d) :
    (coBasis d i).toFin1dℝ = Pi.single i 1
```

**`Lorentz.coBasisFin`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L99).

> The standard basis of covariant Lorentz vectors indexed by `Fin (1 + d)`.

```lean
def coBasisFin (d : ℕ := 3) : Basis (Fin (1 + d)) ℝ (CoMod d)
```

**`Lorentz.coBasisFin_toFin1dℝ`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L103).

```lean
lemma coBasisFin_toFin1dℝ {d : ℕ} (i : Fin (1 + d)) :
    (coBasisFin d i).toFin1dℝ = Pi.single (finSumFinEquiv.symm i) 1
```

**`Lorentz.coBasisFin_repr_apply`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L107).

```lean
lemma coBasisFin_repr_apply {d : ℕ} (p : CoMod d) (i : Fin (1 + d)) :
    (coBasisFin d).repr p i = p.val (finSumFinEquiv.symm i)
```

## Isomorphism between contravariant and covariant Lorentz vectors

**`Lorentz.Contr.toCo`**, a def, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L119).

> The morphism of representations from `ContrMod.rep` to `CoMod.rep` defined by multiplication
> with the metric.

```lean
def Contr.toCo (d : ℕ) : IntertwiningMap (ContrMod.rep (d := d)) (CoMod.rep (d := d))
```

**`Lorentz.Co.toContr`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L136).

> The morphism of representations from `CoMod.rep` to `ContrMod.rep` defined by multiplication
> with the metric.

```lean
def Co.toContr (d : ℕ) : IntertwiningMap (CoMod.rep (d := d)) (ContrMod.rep (d := d))
```

**`Lorentz.contrIsoCo`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L153).

> The isomorphism between `ContrMod.rep` and `CoMod.rep` induced by multiplication with the
> Minkowski metric.

```lean
def contrIsoCo (d : ℕ) : Representation.Equiv (ContrMod.rep (d := d)) (CoMod.rep (d := d))
```

## Other properties

**`Lorentz.Contr.ρ_stdBasis`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean#L168).

```lean
lemma ρ_stdBasis (μ : Fin 1 ⊕ Fin 3) (Λ : LorentzGroup 3) :
    ContrMod.rep Λ (ContrMod.stdBasis μ) = ∑ j, Λ.1 j μ • ContrMod.stdBasis j
```

## Depends on

- [Physlib.Relativity.Tensors.RealTensor.Vector.Pre.Modules](realtensor-vector-pre-modules.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Pre/Basic.lean)
