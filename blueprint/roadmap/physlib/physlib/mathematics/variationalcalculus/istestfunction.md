---
declaration: module
origin: cited
lean: IsTestFunction, IsTestFunction.toCompactlySupportedContinuousMap, IsTestFunction.of_compactlySupportedContinuousMap, IsTestFunction.integrable, IsTestFunction.differentiable, IsTestFunction.contDiff, IsTestFunction.zero, IsTestFunction.comp_left
statement: formalized
proof: formalized
---

# Test functions

The module `Physlib.Mathematics.VariationalCalculus.IsTestFunction`, [Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean): 36 declarations, 2 with a docstring.

> Definition of test function, smooth and compactly supported function, and theorems about them.

**`IsTestFunction`**, a structure, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L28).

> A test function is a smooth function with compact support.

```lean
structure IsTestFunction (f : X → U) where
  smooth : ContDiff ℝ ∞ f
  supp : HasCompactSupport f
```

**`IsTestFunction.toCompactlySupportedContinuousMap`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L33).

> A compactly supported continuous map from a test function.

```lean
def IsTestFunction.toCompactlySupportedContinuousMap {f : X → U}
    (hf : IsTestFunction f) : CompactlySupportedContinuousMap X U
```

**`IsTestFunction.of_compactlySupportedContinuousMap`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L39).

```lean
lemma IsTestFunction.of_compactlySupportedContinuousMap {f : CompactlySupportedContinuousMap X U}
    (hf : ContDiff ℝ ∞ f) :
    IsTestFunction f.toFun
```

**`IsTestFunction.integrable`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L46).

```lean
lemma IsTestFunction.integrable [MeasurableSpace X] [OpensMeasurableSpace X]
    {f : X → U} (hf : IsTestFunction f)
    (μ : Measure X) [IsFiniteMeasureOnCompacts μ] :
    MeasureTheory.Integrable f μ
```

**`IsTestFunction.differentiable`**, a lemma, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L53).

```lean
lemma IsTestFunction.differentiable {f : X → U} (hf : IsTestFunction f) :
    Differentiable ℝ f
```

**`IsTestFunction.contDiff`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L57).

```lean
lemma IsTestFunction.contDiff {f : X → U} (hf : IsTestFunction f) :
    ContDiff ℝ ∞ f
```

**`IsTestFunction.zero`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L61).

```lean
lemma IsTestFunction.zero :
    IsTestFunction (fun _ : X => (0 : U))
```

**`IsTestFunction.comp_left`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L67).

```lean
lemma IsTestFunction.comp_left {f : X → V} (hf : IsTestFunction f)
    {g : V → U} (hg1 : g 0 = 0) (hg : ContDiff ℝ ∞ g) :
    IsTestFunction (fun x => g (f x))
```

**`IsTestFunction.pi`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L78).

```lean
lemma IsTestFunction.pi {ι} [Fintype ι] {φ : X → ι → U} (hφ : ∀ i, IsTestFunction (φ · i)) :
    IsTestFunction (fun x i => φ x i)
```

**`IsTestFunction.space_component`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L93).

```lean
lemma IsTestFunction.space_component {φ : X → Space d} (hφ : IsTestFunction φ) :
    IsTestFunction (fun x => φ x i)
```

**`IsTestFunction.prodMk`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L105).

```lean
lemma IsTestFunction.prodMk {f : X → U} {g : X → V}
    (hf : IsTestFunction f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => (f x, g x))
```

**`IsTestFunction.prod_fst`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L118).

```lean
lemma IsTestFunction.prod_fst {f : X → U × V} (hf : IsTestFunction f) :
    IsTestFunction (fun x => (f x).1)
```

**`IsTestFunction.prod_snd`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L122).

```lean
lemma IsTestFunction.prod_snd {f : X → U × V} (hf : IsTestFunction f) :
    IsTestFunction (fun x => (f x).2)
```

**`IsTestFunction.neg`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L126).

```lean
lemma IsTestFunction.neg {f : X → U} (hf : IsTestFunction f) :
    IsTestFunction (fun x => - f x)
```

**`IsTestFunction.add`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L130).

```lean
lemma IsTestFunction.add {f g : X → U} (hf : IsTestFunction f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => f x + g x)
```

**`IsTestFunction.sub`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L134).

```lean
lemma IsTestFunction.sub {f g : X → U} (hf : IsTestFunction f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => f x - g x)
```

**`IsTestFunction.mul`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L138).

```lean
lemma IsTestFunction.mul {f g : X → ℝ} (hf : IsTestFunction f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => f x * g x)
```

**`IsTestFunction.mul_left`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L142).

```lean
lemma IsTestFunction.mul_left {f g : X → ℝ} (hf : ContDiff ℝ ∞ f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => f x * g x)
```

**`IsTestFunction.mul_right`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L148).

```lean
lemma IsTestFunction.mul_right {f g : X → ℝ} (hf : IsTestFunction f) (hg : ContDiff ℝ ∞ g) :
    IsTestFunction (fun x => f x * g x)
```

**`IsTestFunction.inner`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L154).

```lean
lemma IsTestFunction.inner [InnerProductSpace' ℝ V]
    {f g : X → V} (hf : IsTestFunction f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => ⟪f x, g x⟫_ℝ)
```

**`IsTestFunction.inner_left`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L159).

```lean
lemma IsTestFunction.inner_left [InnerProductSpace' ℝ V]
    {f : X → V} {g : X → V} (hf : ContDiff ℝ ∞ f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => ⟪f x, g x⟫_ℝ)
```

**`IsTestFunction.inner_right`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L169).

```lean
lemma IsTestFunction.inner_right [InnerProductSpace' ℝ V]
    {f : X → V} {g : X → V} (hf : IsTestFunction f) (hg : ContDiff ℝ ∞ g) :
    IsTestFunction (fun x => ⟪f x, g x⟫_ℝ)
```

**`IsTestFunction.smul`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L179).

```lean
lemma IsTestFunction.smul {f : X → ℝ} {g : X → U} (hf : IsTestFunction f) (hg : IsTestFunction g) :
    IsTestFunction (fun x => f x • g x)
```

**`IsTestFunction.smul_left`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L183).

```lean
lemma IsTestFunction.smul_left {f : X → ℝ} {g : X → U}
    (hf : ContDiff ℝ ∞ f) (hg : IsTestFunction g) : IsTestFunction (fun x => f x • g x)
```

**`IsTestFunction.smul_right`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L189).

```lean
lemma IsTestFunction.smul_right {f : X → ℝ} {g : X → U}
    (hf : IsTestFunction f) (hg : ContDiff ℝ ∞ g) : IsTestFunction (fun x => f x • g x)
```

**`IsTestFunction.sum`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L195).

```lean
lemma IsTestFunction.sum {ι} [Fintype ι] {φ : X → ι → U} {hφ : ∀ i, IsTestFunction (φ · i)} :
    IsTestFunction (fun x => ∑ i, φ x i)
```

**`IsTestFunction.coord`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L199).

```lean
lemma IsTestFunction.coord {φ : X → Space d} (hφ : IsTestFunction φ) (i : Fin d) :
    IsTestFunction (fun x => (φ x).coord i)
```

**`IsTestFunction.linearMap_comp`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L203).

```lean
lemma IsTestFunction.linearMap_comp {f : X → V} (hf : IsTestFunction f)
    {g : V →ₗ[ℝ] U} (hg : ContDiff ℝ ∞ g) :
    IsTestFunction (fun x => g (f x))
```

**`IsTestFunction.family_linearMap_comp`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L208).

```lean
lemma IsTestFunction.family_linearMap_comp {f : X → V} (hf : IsTestFunction f)
    {g : X → V →L[ℝ] U} (hg : ContDiff ℝ ∞ g) :
    IsTestFunction (fun x => g x (f x))
```

**`IsTestFunction.deriv`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L222).

```lean
lemma IsTestFunction.deriv {f : ℝ → U} (hf : IsTestFunction f) :
    IsTestFunction (fun x => deriv f x)
```

**`IsTestFunction.of_fderiv`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L228).

```lean
lemma IsTestFunction.of_fderiv {f : X → U} (hf : IsTestFunction f) :
    IsTestFunction (fderiv ℝ f ·)
```

**`IsTestFunction.fderiv_apply`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L240).

```lean
lemma IsTestFunction.fderiv_apply {f : X → U} (hf : IsTestFunction f) (δx : X) :
    IsTestFunction (fderiv ℝ f · δx)
```

**`IsTestFunction.adjFDeriv`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L254).

```lean
lemma IsTestFunction.adjFDeriv {f : X → U} [InnerProductSpace' ℝ X]
    [InnerProductSpace' ℝ U] [CompleteSpace X]
    [CompleteSpace U] (dy : U) (hf : IsTestFunction f) :
    IsTestFunction (fun x => adjFDeriv ℝ f x dy)
```

**`IsTestFunction.divergence`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L281).

```lean
lemma IsTestFunction.divergence {f : X → X} [FiniteDimensional ℝ X] (hf : IsTestFunction f) :
    IsTestFunction (fun x => divergence ℝ f x)
```

**`IsTestFunction.gradient`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L305).

```lean
lemma IsTestFunction.gradient {d : ℕ} (φ : Space d → ℝ)
    (hφ : IsTestFunction φ) :
    IsTestFunction (gradient φ)
```

**`IsTestFunction.of_div`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean#L313).

```lean
lemma IsTestFunction.of_div {d : ℕ} (φ : Space d → EuclideanSpace ℝ (Fin d))
    (hφ : IsTestFunction φ) :
    IsTestFunction (Space.div φ)
```

## Depends on

- [Divergence](../calculus/divergence.md)

## Sources

- [Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsTestFunction.lean)
