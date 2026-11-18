---
declaration: module
origin: cited
lean: realLorentzTensor.Color, realLorentzTensor.modules, realLorentzTensor.modulesAddCommGroup, realLorentzTensor.modulesModule, realLorentzTensor, realLorentzConjTensor, realLorentzTensor.instWithMetric, realLorentzTensor.basisIdxCongr_apply
statement: formalized
proof: formalized
---

# Physlib.Relativity.Tensors.RealTensor.Basic

The module `Physlib.Relativity.Tensors.RealTensor.Basic`, [Physlib/Relativity/Tensors/RealTensor/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean): 18 declarations (2 instances with no name), 9 with a docstring.

## Real Lorentz tensors

> Within this directory `Pre` is used to denote that the definitions are preliminary and
> which are used to define `realLorentzTensor`.

**`realLorentzTensor.Color`**, an inductive, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L30).

> The colors associated with real representations of O(1, 3) of interest to physics.

```lean
inductive Color
  /-- The color associated with contravariant Lorentz vectors. -/
  | up : Color
  /-- The color associated with covariant Lorentz vectors. -/
  | down : Color
deriving Fintype
```

**An instance with no name**, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L38).

> Color for real Lorentz tensors is decidable.

```lean
instance : DecidableEq Color
```

**`realLorentzTensor.modules`**, an abbrev, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L47).

> The modules associated with each of the different types of real Lorentz vector space.

```lean
abbrev modules (d : ℕ) : Color → Type
```

**`realLorentzTensor.modulesAddCommGroup`**, an instance, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L51).

```lean
instance modulesAddCommGroup (d : ℕ) : ∀ c, AddCommGroup (modules d c)
```

**`realLorentzTensor.modulesModule`**, an instance, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L55).

```lean
instance modulesModule (d : ℕ) : ∀ c, Module ℝ (modules d c)
```

**`realLorentzTensor`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L68).

> The tensor structure for real Lorentz tensors.

```lean
def realLorentzTensor (d : ℕ := 3) : TensorSpecies
    ℝ realLorentzTensor.Color (LorentzGroup d)
    (fun | Color.up => Lorentz.ContrMod d | Color.down => Lorentz.CoMod d)
    (fun _ => Fin 1 ⊕ Fin d)
    (fun | Color.up => Lorentz.ContrMod.rep | Color.down => Lorentz.CoMod.rep)
    (fun | Color.up => Lorentz.contrBasis d | Color.down => Lorentz.coBasis d)
```

**`realLorentzConjTensor`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L107).

> The real Lorentz tensors as a conjugation species: over `ℝ` conjugation is trivial, so every
> colour is its own conjugate.

```lean
def realLorentzConjTensor (d : ℕ := 3) : ConjTensorSpecies ℝ Color (LorentzGroup d)
    (modules d) (fun _ => Fin 1 ⊕ Fin d)
    (fun | Color.up => Lorentz.ContrMod.rep | Color.down => Lorentz.CoMod.rep)
    (fun | Color.up => Lorentz.contrBasis d | Color.down => Lorentz.coBasis d)
```

**`realLorentzTensor.instWithMetric`**, an instance, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L122).

> The Minkowski metric of the real Lorentz tensors, on both vector colors.

```lean
instance instWithMetric (d : ℕ) : (realLorentzTensor d).WithMetric
```

## Basis and discrete functor objects

> These re-express fields of `realLorentzTensor d` in terms of `Lorentz` data.

**`realLorentzTensor.basisIdxCongr_apply`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L156).

```lean
lemma basisIdxCongr_apply {d : ℕ} {c1 c2 : realLorentzTensor.Color} (h : c1 = c2)
    (i : Fin 1 ⊕ Fin d) :
    TensorSpecies.basisIdxCongr (basisIdx := fun _ => Fin 1 ⊕ Fin d) h i = i
```

## Simplifying τ

**`realLorentzTensor.τ_up_eq_down`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L168).

```lean
lemma τ_up_eq_down {d : ℕ} : (realLorentzTensor d).τ Color.up = Color.down
```

**`realLorentzTensor.τ_down_eq_up`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L171).

```lean
lemma τ_down_eq_up {d : ℕ} : (realLorentzTensor d).τ Color.down = Color.up
```

## Contractions and to Field

**`realLorentzTensor.isContrDualMatching_refl`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L184).

> At every real Lorentz color, the bases at the color and its dual are dual bases, with
> labels matched by the identity.

```lean
lemma isContrDualMatching_refl (c : realLorentzTensor.Color) :
    IsContrDualMatching (realLorentzTensor d) c (Equiv.refl _)
```

**An instance with no name**, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L192).

> Real Lorentz tensors have dual bases under contraction, with the identity matching.

```lean
instance : HasContrDualBases (realLorentzTensor d)
```

**`realLorentzTensor.contrDualIdxEquiv_eq_refl`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L197).

> The dual-label matching of real Lorentz tensors is the identity.

```lean
lemma contrDualIdxEquiv_eq_refl (c : realLorentzTensor.Color) :
    HasContrDualBases.contrDualIdxEquiv (realLorentzTensor d) c = Equiv.refl _
```

**`realLorentzTensor.contrPCoeff_basis`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L201).

```lean
lemma contrPCoeff_basis {d n : ℕ} {c : Fin n → realLorentzTensor.Color} (i j : Fin n)
    (hij : i ≠ j ∧ (realLorentzTensor d).τ (c i) = c j)
    (b : ComponentIdx (S := realLorentzTensor d) c) :
    Pure.contrPCoeff i j hij (Pure.basisVector c b) = if b i = b j then 1 else 0
```

**`realLorentzTensor.contrT_eq_sum_evalT`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L208).

```lean
lemma contrT_eq_sum_evalT {n} {d} (c : Fin (n + 1 + 1) → Color) (i j : Fin (n + 1 + 1))
    (h : i ≠ j ∧ (realLorentzTensor d).τ (c i) = c j) (t : ℝT(d, c)) :
    contrT n i j h t = ∑ (μ : Fin 1 ⊕ Fin d), permT id (by
      simp [Fin.succSuccAbove_eq_predAbove h.1])
      (evalT ((Fin.predAbove 0 i).predAbove j) μ (evalT i μ t))
```

**`realLorentzTensor.contrT_toScalar`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L240).

```lean
lemma contrT_toScalar {d} (c : Fin 2 → Color)
    (h : 0 ≠ 1 ∧ (realLorentzTensor d).τ (c 0) = c 1) (t : ℝT(d, c)) :
    (contrT 0 0 1 h t).toScalar = ∑ (μ : Fin 1 ⊕ Fin d), {t | [μ] [μ]}ᵀ.toScalar
```

**`realLorentzTensor.contrT_basis_repr_apply_eq_fin`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean#L250).

```lean
lemma contrT_basis_repr_apply_eq_fin {n d: ℕ} {c : Fin (n + 1 + 1) → realLorentzTensor.Color}
    {i j : Fin (n + 1 + 1)}
    {h : i ≠ j ∧ (realLorentzTensor d).τ (c i) = c j}
    (t : ℝT(d,c)) (b : ComponentIdx (c ∘ Fin.succSuccAbove i j)) :
    (basis (c ∘ Fin.succSuccAbove i j)).repr (contrT n i j h t) b =
    ∑ (x : Fin 1 ⊕ Fin d), ((basis c).repr t
    (DropPairSection.ofFinEquiv h.1 b ⟨x, x⟩))
```

## Depends on

- [Contractions of component indices](../part-02/componentidx-contraction.md)
- [Conjugation structure on a tensor species](../part-02/conjugation-basic.md)
- [Evaluation of tensor indices](../part-01/evaluation.md)
- [Metric for real Lorentz vectors](realtensor-metrics-pre.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Basic.lean)
