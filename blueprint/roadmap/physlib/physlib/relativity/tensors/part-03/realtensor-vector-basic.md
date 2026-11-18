---
declaration: module
origin: cited
lean: Lorentz.Vector, Lorentz.Vector.equivEuclid, Lorentz.Vector.equivEuclid_apply, Lorentz.Vector.eq_of_apply_eq, Lorentz.Vector.norm_eq_equivEuclid, Lorentz.Vector.abs_component_le_norm, Lorentz.Vector.isNormedAddCommGroup, Lorentz.Vector.isNormedSpace
statement: formalized
proof: formalized
---

# Lorentz Vectors

The module `Physlib.Relativity.Tensors.RealTensor.Vector.Basic`, [Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean): 68 declarations (8 instances with no name), 18 with a docstring.

> In this module we define Lorentz vectors as real Lorentz tensors with a single up index.
> We create an API around Lorentz vectors to make working with them as easy as possible.

**`Lorentz.Vector`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L33).

> Real contravariant Lorentz vector.

```lean
def Vector (d : ℕ := 3)
```

**An instance with no name**, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L42).

```lean
instance {d} : AddCommMonoid (Vector d)
```

**An instance with no name**, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L45).

```lean
instance {d} : Module ℝ (Vector d)
```

**An instance with no name**, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L48).

```lean
instance {d} : AddCommGroup (Vector d)
```

**An instance with no name**, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L51).

```lean
instance {d} : FiniteDimensional ℝ (Vector d)
```

**`Lorentz.Vector.equivEuclid`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L55).

> The equivalence between `Vector d` and `EuclideanSpace ℝ (Fin 1 ⊕ Fin d)`.

```lean
def equivEuclid (d : ℕ) :
    Vector d ≃ₗ[ℝ] EuclideanSpace ℝ (Fin 1 ⊕ Fin d)
```

**`Lorentz.Vector.equivEuclid_apply`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L60).

```lean
lemma equivEuclid_apply (d : ℕ) (v : Vector d) (i : Fin 1 ⊕ Fin d) :
    equivEuclid d v i = v i
```

**`Lorentz.Vector.eq_of_apply_eq`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L64).

```lean
lemma eq_of_apply_eq {d : ℕ} {v w : Vector d} (h : ∀ i, v i = w i) : v = w
```

**An instance with no name**, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L69).

```lean
instance (d : ℕ) : Norm (Vector d)
```

**`Lorentz.Vector.norm_eq_equivEuclid`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L72).

```lean
lemma norm_eq_equivEuclid (d : ℕ) (v : Vector d) :
    ‖v‖ = ‖equivEuclid d v‖
```

**`Lorentz.Vector.abs_component_le_norm`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L76).

```lean
lemma abs_component_le_norm {d : ℕ} (v : Vector d) (i : Fin 1 ⊕ Fin d) :
    |v i| ≤ ‖v‖
```

**`Lorentz.Vector.isNormedAddCommGroup`**, an instance, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L84).

```lean
instance isNormedAddCommGroup (d : ℕ) : NormedAddCommGroup (Vector d)
```

**`Lorentz.Vector.isNormedSpace`**, an instance, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L98).

```lean
instance isNormedSpace (d : ℕ) : NormedSpace ℝ (Vector d)
```

**An instance with no name**, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L104).

```lean
instance (d : ℕ) : Inner ℝ (Vector d)
```

**`Lorentz.Vector.inner_eq_equivEuclid`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L107).

```lean
lemma inner_eq_equivEuclid (d : ℕ) (v w : Vector d) :
    ⟪v, w⟫_ℝ = ⟪equivEuclid d v, equivEuclid d w⟫_ℝ
```

**`Lorentz.Vector.innerProductSpace`**, an instance, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L111).

> The Euclidean inner product structure on `CoVector`.

```lean
instance innerProductSpace (d : ℕ) : InnerProductSpace ℝ (Vector d)
```

**`Lorentz.Vector.inner_eq_sum`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L126).

> The inner product on `Vector d` as a sum over components.

```lean
lemma inner_eq_sum {d : ℕ} (v w : Vector d) : ⟪v, w⟫_ℝ = ∑ μ, v μ * w μ
```

**An instance with no name**, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L131).

> The instance of a `ChartedSpace` on `Vector d`.

```lean
instance : ChartedSpace (Vector d) (Vector d)
```

**An instance with no name**, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L133).

```lean
instance {d} : CoeFun (Vector d) (fun _ => Fin 1 ⊕ Fin d → ℝ)
```

**`Lorentz.Vector.ext_of_apply`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L136).

```lean
lemma ext_of_apply {d} {v w : Vector d} (h : ∀ i, v i = w i) : v = w
```

**`Lorentz.Vector.apply_smul`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L142).

```lean
lemma apply_smul {d : ℕ} (c : ℝ) (v : Vector d) (i : Fin 1 ⊕ Fin d) :
    (c • v) i = c * v i
```

**`Lorentz.Vector.apply_add`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L146).

```lean
lemma apply_add {d : ℕ} (v w : Vector d) (i : Fin 1 ⊕ Fin d) :
    (v + w) i = v i + w i
```

**`Lorentz.Vector.apply_sub`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L150).

```lean
lemma apply_sub {d : ℕ} (v w : Vector d) (i : Fin 1 ⊕ Fin d) :
    (v - w) i = v i - w i
```

**`Lorentz.Vector.apply_sum`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L153).

```lean
lemma apply_sum {d : ℕ} {ι : Type} [Fintype ι] (f : ι → Vector d) (i : Fin 1 ⊕ Fin d) :
    (∑ j, f j) i = ∑ j, f j i
```

**`Lorentz.Vector.neg_apply`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L173).

```lean
lemma neg_apply {d : ℕ} (v : Vector d) (i : Fin 1 ⊕ Fin d) :
    (-v) i = - v i
```

**`Lorentz.Vector.zero_apply`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L177).

```lean
lemma zero_apply {d : ℕ} (i : Fin 1 ⊕ Fin d) :
    (0 : Vector d) i = 0
```

**`Lorentz.Vector.coordCLM`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L181).

> The continuous linear map from a Lorentz vector to one of its coordinates.

```lean
def coordCLM {d : ℕ} (i : Fin 1 ⊕ Fin d) : Vector d →L[ℝ] ℝ
```

**`Lorentz.Vector.coordCLM_apply`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L186).

```lean
lemma coordCLM_apply {d : ℕ} (i : Fin 1 ⊕ Fin d) (v : Vector d) :
    coordCLM i v = v i
```

**`Lorentz.Vector.coord_continuous`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L190).

```lean
lemma coord_continuous {d : ℕ} (i : Fin 1 ⊕ Fin d) :
    Continuous (fun v : Vector d => v i)
```

**`Lorentz.Vector.coord_contDiff`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L195).

```lean
lemma coord_contDiff {n} {d : ℕ} (i : Fin 1 ⊕ Fin d) :
    ContDiff ℝ n (fun v : Vector d => v i)
```

**`Lorentz.Vector.coord_differentiable`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L200).

```lean
lemma coord_differentiable {d : ℕ} (i : Fin 1 ⊕ Fin d) :
    Differentiable ℝ (fun v : Vector d => v i)
```

**`Lorentz.Vector.coord_differentiableAt`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L205).

```lean
lemma coord_differentiableAt {d : ℕ} (i : Fin 1 ⊕ Fin d) (v : Vector d) :
    DifferentiableAt ℝ (fun v : Vector d => v i) v
```

**`Lorentz.Vector.euclidCLE`**, a def, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L210).

> The continuous linear equivalence between `Vector d` and Euclidean space.

```lean
def euclidCLE (d : ℕ) : Vector d ≃L[ℝ] EuclideanSpace ℝ (Fin 1 ⊕ Fin d)
```

**`Lorentz.Vector.equivPi`**, a def, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L214).

> The continuous linear equivalence between `Vector d` and the corresponding `Pi` type.

```lean
def equivPi (d : ℕ) :
    Vector d ≃L[ℝ] Π (_ : Fin 1 ⊕ Fin d), ℝ
```

**`Lorentz.Vector.equivPi_apply`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L219).

```lean
lemma equivPi_apply {d : ℕ} (v : Vector d) (i : Fin 1 ⊕ Fin d) :
    equivPi d v i = v i
```

**`Lorentz.Vector.continuous_of_apply`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L223).

```lean
lemma continuous_of_apply {d : ℕ} {α : Type*} [TopologicalSpace α]
    (f : α → Vector d)
    (h : ∀ i : Fin 1 ⊕ Fin d, Continuous (fun x => f x i)) :
    Continuous f
```

**`Lorentz.Vector.differentiable_apply`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L233).

```lean
lemma differentiable_apply {d : ℕ} {α : Type*} [NormedAddCommGroup α] [NormedSpace ℝ α]
    (f : α → Vector d) :
    (∀ i : Fin 1 ⊕ Fin d, Differentiable ℝ (fun x => f x i)) ↔ Differentiable ℝ f
```

**`Lorentz.Vector.contDiff_apply`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L246).

```lean
lemma contDiff_apply {n : WithTop ℕ∞} {d : ℕ} {α : Type*}
    [NormedAddCommGroup α] [NormedSpace ℝ α]
    (f : α → Vector d) :
    (∀ i : Fin 1 ⊕ Fin d, ContDiff ℝ n (fun x => f x i)) ↔ ContDiff ℝ n f
```

**`Lorentz.Vector.fderiv_apply`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L262).

```lean
lemma fderiv_apply {d : ℕ} {α : Type*}
    [NormedAddCommGroup α] [NormedSpace ℝ α]
    (f : α → Vector d) (h : Differentiable ℝ f)
    (x : α) (dt : α) (ν : Fin 1 ⊕ Fin d) :
    fderiv ℝ f x dt ν = fderiv ℝ (fun y => f y ν) x dt
```

**`Lorentz.Vector.fderiv_coord`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L273).

```lean
lemma fderiv_coord {d : ℕ} (μ : Fin 1 ⊕ Fin d) (x : Vector d) :
    fderiv ℝ (fun v : Vector d => v μ) x = coordCLM μ
```

## Basis

**`Lorentz.Vector.basis`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L285).

> The basis on `Vector d` indexed by `Fin 1 ⊕ Fin d`.

```lean
def basis {d : ℕ} : Basis (Fin 1 ⊕ Fin d) ℝ (Vector d)
```

**`Lorentz.Vector.basis_apply`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L289).

```lean
lemma basis_apply {d : ℕ} (μ ν : Fin 1 ⊕ Fin d) :
    basis μ ν = if μ = ν then 1 else 0
```

**`Lorentz.Vector.basis_repr_apply`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L296).

```lean
lemma basis_repr_apply {d : ℕ} (p : Vector d) (μ : Fin 1 ⊕ Fin d) :
    basis.repr p μ = p μ
```

**`Lorentz.Vector.map_apply_eq_basis_mulVec`**, a lemma, [line 301](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L301).

```lean
lemma map_apply_eq_basis_mulVec {d : ℕ} (f : Vector d →ₗ[ℝ] Vector d) (p : Vector d) :
    (f p) = (LinearMap.toMatrix basis basis) f *ᵥ p
```

**`Lorentz.Vector.sum_basis_eq_zero_iff`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L305).

```lean
lemma sum_basis_eq_zero_iff {d : ℕ} (f : Fin 1 ⊕ Fin d → ℝ) :
    (∑ μ, f μ • basis μ) = 0 ↔ ∀ μ, f μ = 0
```

**`Lorentz.Vector.sum_inl_inr_basis_eq_zero_iff`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L315).

```lean
lemma sum_inl_inr_basis_eq_zero_iff {d : ℕ} (f₀ : ℝ) (f : Fin d → ℝ) :
    f₀ • basis (Sum.inl 0) + (∑ i, f i • basis (Sum.inr i)) = 0 ↔
    f₀ = 0 ∧ ∀ i, f i = 0
```

## C. The Spatial part

**`Lorentz.Vector.spatialPart`**, an abbrev, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L335).

> Extract spatial components from a Lorentz vector,
> returning them as a vector in Euclidean space.

```lean
abbrev spatialPart {d : ℕ} (v : Vector d) : EuclideanSpace ℝ (Fin d)
```

**`Lorentz.Vector.spatialPart_apply_eq_toCoord`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L338).

```lean
lemma spatialPart_apply_eq_toCoord {d : ℕ} (v : Vector d) (i : Fin d) :
    spatialPart v i = v (Sum.inr i)
```

**`Lorentz.Vector.spatialPart_basis_sum_inr`**, a lemma, [line 341](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L341).

```lean
lemma spatialPart_basis_sum_inr {d : ℕ} (i : Fin d) (j : Fin d) :
    spatialPart (basis (Sum.inr i)) j =
      (Finsupp.single (Sum.inr i : Fin 1 ⊕ Fin d) 1) (Sum.inr j)
```

**`Lorentz.Vector.spatialPart_basis_sum_inl`**, a lemma, [line 348](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L348).

```lean
lemma spatialPart_basis_sum_inl {d : ℕ} (i : Fin d) :
    spatialPart (basis (Sum.inl 0)) i = 0
```

**`Lorentz.Vector.spatialCLM`**, a def, [line 352](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L352).

> The spatial part of a Lorentz vector as a continuous linear map.

```lean
def spatialCLM (d : ℕ) : Vector d →L[ℝ] EuclideanSpace ℝ (Fin d)
```

**`Lorentz.Vector.spatialCLM_apply_eq_spatialPart`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L358).

```lean
lemma spatialCLM_apply_eq_spatialPart {d : ℕ} (v : Vector d) (i : Fin d) :
    spatialCLM d v i = spatialPart v i
```

**`Lorentz.Vector.spatialCLM_basis_sum_inl`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L362).

```lean
lemma spatialCLM_basis_sum_inl {d : ℕ} :
    spatialCLM d (basis (Sum.inl 0)) = 0
```

**`Lorentz.Vector.spatialCLM_basis_sum_inr`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L368).

```lean
lemma spatialCLM_basis_sum_inr {d : ℕ} (i : Fin d) :
    spatialCLM d (basis (Sum.inr i)) = EuclideanSpace.basisFun (Fin d) ℝ i
```

## The Temporal component

**`Lorentz.Vector.timeComponent`**, an abbrev, [line 383](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L383).

> Extract time component from a Lorentz vector

```lean
abbrev timeComponent {d : ℕ} (v : Vector d) : ℝ
```

**`Lorentz.Vector.timeComponent_basis_sum_inr`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L386).

```lean
lemma timeComponent_basis_sum_inr {d : ℕ} (i : Fin d) :
    timeComponent (basis (Sum.inr i)) = 0
```

**`Lorentz.Vector.timeComponent_basis_sum_inl`**, a lemma, [line 389](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L389).

```lean
lemma timeComponent_basis_sum_inl {d : ℕ} :
    timeComponent (d := d) (basis (Sum.inl 0)) = 1
```

**`Lorentz.Vector.temporalCLM`**, a def, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L393).

> The temporal part of a Lorentz vector as a continuous linear map.

```lean
def temporalCLM (d : ℕ) : Vector d →L[ℝ] ℝ
```

**`Lorentz.Vector.temporalCLM_apply_eq_timeComponent`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L399).

```lean
lemma temporalCLM_apply_eq_timeComponent {d : ℕ} (v : Vector d) :
    temporalCLM d v = timeComponent v
```

**`Lorentz.Vector.temporalCLM_basis_sum_inr`**, a lemma, [line 403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L403).

```lean
lemma temporalCLM_basis_sum_inr {d : ℕ} (i : Fin d) :
    temporalCLM d (basis (Sum.inr i)) = 0
```

**`Lorentz.Vector.temporalCLM_basis_sum_inl`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L408).

```lean
lemma temporalCLM_basis_sum_inl {d : ℕ} :
    temporalCLM d (basis (Sum.inl 0)) = 1
```

**`Lorentz.Vector.ofTemporalComponent`**, a def, [line 414](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L414).

> The continuous linear map corresponding to the creation of a
> Lorentz Vector with only a non-zero temporal component.

```lean
def ofTemporalComponent {d : ℕ} : ℝ →L[ℝ] Vector d
```

**`Lorentz.Vector.ofSpatialComponent`**, a def, [line 421](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L421).

> The continuous linear map corresponding to the creation of a
> Lorentz Vector with only non-zero spatial components.

```lean
def ofSpatialComponent {d : ℕ} : EuclideanSpace ℝ (Fin d) →L[ℝ] Vector d
```

> ## Smoothness

**`Lorentz.Vector.asSmoothManifold`**, a def, [line 436](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L436).

> The structure of a smooth manifold on Vector .

```lean
def asSmoothManifold (d : ℕ) : ModelWithCorners ℝ (Vector d) (Vector d)
```

## Properties of the inner product (note not the Minkowski product)

**`Lorentz.Vector.basis_inner`**, a lemma, [line 445](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L445).

```lean
lemma basis_inner {d : ℕ} (μ : Fin 1 ⊕ Fin d) (p : Lorentz.Vector d) :
    ⟪Lorentz.Vector.basis μ, p⟫_ℝ = p μ
```

**`Lorentz.Vector.inner_basis`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L449).

```lean
lemma inner_basis {d : ℕ} (p : Lorentz.Vector d) (μ : Fin 1 ⊕ Fin d) :
    ⟪p, Lorentz.Vector.basis μ⟫_ℝ = p μ
```

**`Lorentz.Vector.eq_zero_of_timeComponent_of_spatialPart`**, a lemma, [line 454](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L454).

> A vector with zero time component and zero spatial part is zero.

```lean
lemma eq_zero_of_timeComponent_of_spatialPart {d : ℕ} {u : Vector d} (h0 : u.timeComponent = 0)
    (hs : u.spatialPart = 0) : u = 0
```

**`Lorentz.Vector.apply_inr_eq_zero_of_norm_spatialPart`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean#L464).

> The spatial components of a vector whose spatial part has zero norm vanish.

```lean
lemma apply_inr_eq_zero_of_norm_spatialPart {d : ℕ} {u : Vector d} (h : ‖u.spatialPart‖ = 0)
    (i : Fin d) : u (Sum.inr i) = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/Vector/Basic.lean)
