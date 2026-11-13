---
declaration: module
origin: cited
lean: Lorentz.CoVector, Lorentz.CoVector.equivEuclid, Lorentz.CoVector.eq_of_apply_eq, Lorentz.CoVector.norm_eq_equivEuclid, Lorentz.CoVector.isNormedAddCommGroup, Lorentz.CoVector.isNormedSpace, Lorentz.CoVector.inner_eq_equivEuclid, Lorentz.CoVector.innerProductSpace
statement: formalized
proof: formalized
---

# Lorentz co vectors

The module `Physlib.Relativity.Tensors.RealTensor.CoVector.Basic`, [Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean): 26 declarations (8 instances with no name), 5 with a docstring.

> In this module we define Lorentz vectors as real Lorentz tensors with a single up index.
> We create an API around Lorentz vectors to make working with them as easy as possible.

**`Lorentz.CoVector`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L33).

> Real covariant Lorentz vector.

```lean
def CoVector (d : ℕ := 3)
```

**An instance with no name**, [line 40](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L40).

```lean
instance {d} : AddCommMonoid (CoVector d)
```

**An instance with no name**, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L43).

```lean
instance {d} : Module ℝ (CoVector d)
```

**An instance with no name**, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L46).

```lean
instance {d} : AddCommGroup (CoVector d)
```

**An instance with no name**, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L49).

```lean
instance {d} : FiniteDimensional ℝ (CoVector d)
```

**`Lorentz.CoVector.equivEuclid`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L53).

> The equivalence between `CoVector d` and `EuclideanSpace ℝ (Fin 1 ⊕ Fin d)`.

```lean
def equivEuclid (d : ℕ) :
    CoVector d ≃ₗ[ℝ] EuclideanSpace ℝ (Fin 1 ⊕ Fin d)
```

**`Lorentz.CoVector.eq_of_apply_eq`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L58).

```lean
lemma eq_of_apply_eq {d : ℕ} {v w : CoVector d} (h : ∀ i, v i = w i) : v = w
```

**An instance with no name**, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L63).

```lean
instance (d : ℕ) : Norm (CoVector d)
```

**`Lorentz.CoVector.norm_eq_equivEuclid`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L66).

```lean
lemma norm_eq_equivEuclid (d : ℕ) (v : CoVector d) :
    ‖v‖ = ‖equivEuclid d v‖
```

**`Lorentz.CoVector.isNormedAddCommGroup`**, an instance, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L69).

```lean
instance isNormedAddCommGroup (d : ℕ) : NormedAddCommGroup (CoVector d)
```

**`Lorentz.CoVector.isNormedSpace`**, an instance, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L84).

```lean
instance isNormedSpace (d : ℕ) : NormedSpace ℝ (CoVector d)
```

**An instance with no name**, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L91).

```lean
instance (d : ℕ) : Inner ℝ (CoVector d)
```

**`Lorentz.CoVector.inner_eq_equivEuclid`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L94).

```lean
lemma inner_eq_equivEuclid (d : ℕ) (v w : CoVector d) :
    ⟪v, w⟫_ℝ = ⟪equivEuclid d v, equivEuclid d w⟫_ℝ
```

**`Lorentz.CoVector.innerProductSpace`**, an instance, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L98).

> The Euclidean inner product structure on `CoVector`.

```lean
instance innerProductSpace (d : ℕ) : InnerProductSpace ℝ (CoVector d)
```

**An instance with no name**, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L113).

> The instance of a `ChartedSpace` on `Vector d`.

```lean
instance : ChartedSpace (CoVector d) (CoVector d)
```

**An instance with no name**, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L115).

```lean
instance {d} : CoeFun (CoVector d) (fun _ => Fin 1 ⊕ Fin d → ℝ)
```

**`Lorentz.CoVector.apply_smul`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L119).

```lean
lemma apply_smul {d : ℕ} (c : ℝ) (v : CoVector d) (i : Fin 1 ⊕ Fin d) :
    (c • v) i = c * v i
```

**`Lorentz.CoVector.apply_add`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L123).

```lean
lemma apply_add {d : ℕ} (v w : CoVector d) (i : Fin 1 ⊕ Fin d) :
    (v + w) i = v i + w i
```

**`Lorentz.CoVector.apply_sub`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L127).

```lean
lemma apply_sub {d : ℕ} (v w : CoVector d) (i : Fin 1 ⊕ Fin d) :
    (v - w) i = v i - w i
```

**`Lorentz.CoVector.apply_sum`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L131).

```lean
lemma apply_sum {d : ℕ} {ι : Type} [Fintype ι] (f : ι → CoVector d) (i : Fin 1 ⊕ Fin d) :
    (∑ j, f j) i = ∑ j, f j i
```

**`Lorentz.CoVector.neg_apply`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L135).

```lean
lemma neg_apply {d : ℕ} (v : CoVector d) (i : Fin 1 ⊕ Fin d) :
    (-v) i = - v i
```

**`Lorentz.CoVector.zero_apply`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L139).

```lean
lemma zero_apply {d : ℕ} (i : Fin 1 ⊕ Fin d) :
    (0 : CoVector d) i = 0
```

## Basis

**`Lorentz.CoVector.basis`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L149).

> The basis on `Vector d` indexed by `Fin 1 ⊕ Fin d`.

```lean
def basis {d : ℕ} : Basis (Fin 1 ⊕ Fin d) ℝ (CoVector d)
```

**`Lorentz.CoVector.basis_apply`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L153).

```lean
lemma basis_apply {d : ℕ} (μ ν : Fin 1 ⊕ Fin d) :
    basis μ ν = if μ = ν then 1 else 0
```

**`Lorentz.CoVector.basis_repr_apply`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L160).

```lean
lemma basis_repr_apply {d : ℕ} (p : CoVector d) (μ : Fin 1 ⊕ Fin d) :
    basis.repr p μ = p μ
```

**`Lorentz.CoVector.map_apply_eq_basis_mulVec`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean#L165).

```lean
lemma map_apply_eq_basis_mulVec {d : ℕ} (f : CoVector d →ₗ[ℝ] CoVector d) (p : CoVector d) :
    (f p) = (LinearMap.toMatrix basis basis) f *ᵥ p
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/CoVector/Basic.lean)
