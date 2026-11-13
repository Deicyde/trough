---
declaration: module
origin: cited
lean: realLorentzTensor.colorToComplex, realLorentzTensor.basisIdxColorToComplex, realLorentzTensor.colorToComplex_match_up, realLorentzTensor.colorToComplex_match_down, realLorentzTensor.colorToComplex_comp_eq_match, TensorSpecies.Tensor.ComponentIdx.complexify, realLorentzTensor.ComponentIdx.complexify_apply, realLorentzTensor.ComponentIdx.complexify_toFun_apply
statement: formalized
proof: formalized
---

# Complex Lorentz tensors from real Lorentz tensors

The module `Physlib.Relativity.Tensors.RealTensor.ToComplex`, [Physlib/Relativity/Tensors/RealTensor/ToComplex.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean): 44 declarations, 28 with a docstring; 2 private, not shown.

## i. Overview

> In this module we describe how to pass from real Lorentz tensors to complex Lorentz tensors
> in a functorial way.
> Specifically, we construct a canonical equivariant semilinear map
>
> * `toComplex : ℝT(3, c) →ₛₗ[Complex.ofRealHom] ℂT(colorToComplex ∘ c)`
>
> which is compatible with the natural operations on tensors (permutations of
> indices, tensor products, contractions and evaluations).

## ii. Key results

> The main definitions and statements are:
>
> * `colorToComplex` upgrades the colour of a real Lorentz tensor to the
>   corresponding complex Lorentz colour.
> * `TensorSpecies.Tensor.ComponentIdx.complexify` transports component indices
>   along `colorToComplex`.
> * `toComplex` is the basic semilinear map from real to complex Lorentz tensors.
> * `toComplex_basis` and `toComplex_pure_basisVector` show that `toComplex`
>   sends basis tensors to basis tensors.
> * `toComplex_eq_zero_iff` and `toComplex_injective` show that `toComplex` is
>   injective.
> * `toComplex_equivariant` states that `toComplex` is equivariant for the action
>   of the complexified Lorentz group.
> * `permT_toComplex`, `prodT_toComplex`, `contrT_toComplex` and `evalT_toComplex`
>   express that `toComplex` commutes with the basic tensor operations.

## iv. References

> * None — the general formalism of Lorentz tensors and their operations is
>   developed in other parts of the library; here we only specialise to the
>   passage from real to complex Lorentz tensors.

## A. Colours and component indices

> We first explain how the Lorentz colour data and component indices for real
> tensors are transported to the complex setting.

**`realLorentzTensor.colorToComplex`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L79).

> The map from colors of real Lorentz tensors to complex Lorentz tensors.

```lean
def colorToComplex (c : realLorentzTensor.Color) : complexLorentzTensor.Color
```

**`realLorentzTensor.basisIdxColorToComplex`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L86).

> The basis index type of a complexified real color is `Fin 1 ⊕ Fin 3`, the basis index type
> of the real color.

```lean
def basisIdxColorToComplex : (c : realLorentzTensor.Color) →
    complexLorentzTensor.basisIdx (colorToComplex c) ≃ Fin 1 ⊕ Fin 3
```

**`realLorentzTensor.colorToComplex_match_up`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L93).

> `simp` helper: reduce `match c j` after a case split on `c j`
> (avoids dependent `rw` / `Pi.smul_apply`).

```lean
lemma colorToComplex_match_up {n} {c : Fin n → realLorentzTensor.Color} {j}
    (hc : c j = realLorentzTensor.Color.up) :
    (match c j with
      | .up => complexLorentzTensor.Color.up
      | .down => complexLorentzTensor.Color.down)
      = complexLorentzTensor.Color.up
```

**`realLorentzTensor.colorToComplex_match_down`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L101).

```lean
lemma colorToComplex_match_down {n} {c : Fin n → realLorentzTensor.Color} {j}
    (hc : c j = realLorentzTensor.Color.down) :
    (match c j with
      | .up => complexLorentzTensor.Color.up
      | .down => complexLorentzTensor.Color.down)
      = complexLorentzTensor.Color.down
```

**`realLorentzTensor.colorToComplex_comp_eq_match`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L109).

```lean
lemma colorToComplex_comp_eq_match {n} (c : Fin n → realLorentzTensor.Color) (j : Fin n) :
    (colorToComplex ∘ c) j =
      (match c j with
        | .up => complexLorentzTensor.Color.up
        | .down => complexLorentzTensor.Color.down)
```

**`TensorSpecies.Tensor.ComponentIdx.complexify`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L118).

> The complexification of the component index of a real Lorentz tensor to
> a complex Lorentz tensor.

```lean
noncomputable def _root_.TensorSpecies.Tensor.ComponentIdx.complexify {n}
    {c : Fin n → realLorentzTensor.Color} :
    ComponentIdx (S := realLorentzTensor) c ≃
      ComponentIdx (S := complexLorentzTensor) (colorToComplex ∘ c)
```

**`realLorentzTensor.ComponentIdx.complexify_apply`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L128).

```lean
lemma ComponentIdx.complexify_apply {n} {c : Fin n → realLorentzTensor.Color}
    (f : ComponentIdx (S := realLorentzTensor) c) (j : Fin n) :
    (ComponentIdx.complexify f) j = (basisIdxColorToComplex (c j)).symm (f j)
```

**`realLorentzTensor.ComponentIdx.complexify_toFun_apply`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L134).

```lean
lemma ComponentIdx.complexify_toFun_apply {n} {c : Fin n → realLorentzTensor.Color}
    (f : ComponentIdx (S := realLorentzTensor) c) (j : Fin n) :
    (ComponentIdx.complexify.toFun f) j = (ComponentIdx.complexify f) j
```

**`realLorentzTensor.basisIdxCongr_basisIdxColorToComplex_symm`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L140).

```lean
lemma basisIdxCongr_basisIdxColorToComplex_symm {c c' : realLorentzTensor.Color}
    (h : colorToComplex c = colorToComplex c') (x : Fin 1 ⊕ Fin 3) :
    basisIdxCongr (basisIdx := complexLorentzTensor.basisIdx) h
      ((basisIdxColorToComplex c).symm x) = (basisIdxColorToComplex c').symm x
```

**`realLorentzTensor.basisIdxTauEquiv_basisIdxCongr_basisIdxColorToComplex_symm`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L147).

```lean
lemma basisIdxTauEquiv_basisIdxCongr_basisIdxColorToComplex_symm
    {c c' : realLorentzTensor.Color}
    (h : colorToComplex c' = complexLorentzTensor.τ (colorToComplex c)) (x : Fin 1 ⊕ Fin 3) :
    basisIdxTauEquiv (colorToComplex c) (basisIdxCongr h ((basisIdxColorToComplex c').symm x)) =
      (basisIdxColorToComplex c).symm x
```

## B. The semilinear map `toComplex`

> We now define the basic semilinear map from real Lorentz tensors to complex
> Lorentz tensors. It is characterised by sending the standard tensor basis on
> the real side to the corresponding basis on the complex side, and is therefore
> determined by the behaviour on components.

**`realLorentzTensor.toComplex`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L167).

> The semilinear map from real Lorentz tensors to complex Lorentz tensors,
> defined through basis.

```lean
noncomputable def toComplex {n} {c : Fin n → realLorentzTensor.Color} :
    ℝT(3, c) →ₛₗ[Complex.ofRealHom] ℂT(colorToComplex ∘ c)
```

**`realLorentzTensor.toComplex_eq_sum_basis`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L185).

```lean
lemma toComplex_eq_sum_basis {n} (c : Fin n → realLorentzTensor.Color) (v : ℝT(3, c)) :
    toComplex v = ∑ i, (Tensor.basis (S := realLorentzTensor) c).repr v
      (ComponentIdx.complexify.symm i) •
      Tensor.basis (S := complexLorentzTensor) (colorToComplex ∘ c) i
```

**`realLorentzTensor.toComplex_repr`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L194).

> The representation of `toComplex v` in the complexified basis equals
> the real representation coerced to complex.

```lean
lemma toComplex_repr {n} {c : Fin n → realLorentzTensor.Color}
    (v : ℝT(3, c)) (i : ComponentIdx (S := realLorentzTensor) c) :
    (Tensor.basis (S := complexLorentzTensor) (colorToComplex ∘ c)).repr
      (toComplex v) i.complexify =
    ↑((Tensor.basis (S := realLorentzTensor) c).repr v i)
```

**`realLorentzTensor.toComplex_basis`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L206).

> `toComplex` sends basis elements to basis elements.

```lean
lemma toComplex_basis {n} {c : Fin n → realLorentzTensor.Color}
    (i : ComponentIdx (S := realLorentzTensor) c) :
    toComplex (c := c) ((Tensor.basis (S := realLorentzTensor) c) i) =
      (Tensor.basis (S := complexLorentzTensor) (colorToComplex ∘ c)) i.complexify
```

**`realLorentzTensor.toComplex_pure_basisVector`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L215).

> `toComplex` on a pure basis vector.

```lean
lemma toComplex_pure_basisVector {n} {c : Fin n → realLorentzTensor.Color}
    (b : ComponentIdx (S := realLorentzTensor) c) :
    toComplex (c := c) (Pure.basisVector c b |>.toTensor)
      =
    (Pure.basisVector (colorToComplex ∘ c) b.complexify).toTensor
```

**`realLorentzTensor.toComplex_map_smul`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L222).

```lean
lemma toComplex_map_smul {n} (c : Fin n → realLorentzTensor.Color) (r : ℝ) (t : ℝT(3, c)) :
    toComplex (c := c) (r • t) = (Complex.ofReal r) • toComplex (c := c) t
```

**`realLorentzTensor.toComplex_eq_zero_iff`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L227).

```lean
lemma toComplex_eq_zero_iff {n} (c : Fin n → realLorentzTensor.Color) (v : ℝT(3, c)) :
    toComplex v = 0 ↔ v = 0
```

**`realLorentzTensor.toComplex_injective`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L238).

> The map `toComplex` is injective.

```lean
lemma toComplex_injective {n} (c : Fin n → realLorentzTensor.Color) :
    Function.Injective (toComplex (c := c))
```

## pure

**`realLorentzTensor.toComplexVector`**, a def, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L254).

> For a given color, the map turning a real Lorentz vector into a complex one.

```lean
noncomputable def toComplexVector (c : realLorentzTensor.Color) :
  realLorentzTensor.modules 3 c →ₛₗ[Complex.ofRealHom] complexLorentzTensor.modules
    (colorToComplex c)
```

**`realLorentzTensor.toComplexVector_up_eq_inclCongrRealLorentz`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L289).

```lean
lemma toComplexVector_up_eq_inclCongrRealLorentz (v : Lorentz.ContrMod 3) :
    toComplexVector Color.up v = Lorentz.inclCongrRealLorentz v
```

**`realLorentzTensor.toComplexVector_down_eq_inclCoRealLorentz`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L298).

```lean
lemma toComplexVector_down_eq_inclCoRealLorentz (v : Lorentz.CoMod 3) :
    toComplexVector Color.down v = Lorentz.inclCoRealLorentz v
```

**`realLorentzTensor.toComplexPure`**, a def, [line 309](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L309).

> The function which turns a real pure tensor into a complex one.

```lean
noncomputable def toComplexPure {c : Fin n → Color} (p : Pure realLorentzTensor c) :
    Pure complexLorentzTensor (colorToComplex ∘ c)
```

**`realLorentzTensor.toComplexPure_component`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L313).

```lean
lemma toComplexPure_component {c : Fin n → Color} (p : Pure realLorentzTensor c)
    (φ : ComponentIdx c) : (toComplexPure p).component (ComponentIdx.complexify φ) =
      p.component φ
```

**`realLorentzTensor.actionP_toComplexPure`**, a lemma, [line 343](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L343).

```lean
lemma actionP_toComplexPure {n : ℕ} (c : Fin n → Color) (p : Pure realLorentzTensor c)
    (Λ : SL(2, ℂ)) :
    Λ • toComplexPure p = toComplexPure (toLorentzGroup Λ • p)
```

**`realLorentzTensor.toComplex_pure`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L377).

```lean
lemma toComplex_pure {n : ℕ} (c : Fin n → Color) (p : Pure realLorentzTensor c) :
    toComplex p.toTensor = (toComplexPure p).toTensor
```

### B.3. Equivariance under the Lorentz action

> Finally we record that `toComplex` is equivariant for the natural action of
> `SL(2, ℂ)` (and hence the induced Lorentz action) on tensors.

**`realLorentzTensor.toComplex_equivariant`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L394).

> The map `toComplex` is equivariant.

```lean
lemma toComplex_equivariant {n} {c : Fin n → realLorentzTensor.Color}
    (v : ℝT(3, c)) (Λ : SL(2, ℂ)) :
    Λ • (toComplex v) = toComplex (Lorentz.SL2C.toLorentzGroup Λ • v)
```

## C. Compatibility with permutations: `permT`

> We first show that complexification is compatible with permutation of tensor
> slots. On colours this is encoded in the `IsReindexing` predicate, and on tensors
> by the operator `permT`.

**`realLorentzTensor.isReindexing_colorToComplex`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L413).

> The `IsReindexing` condition is preserved under `colorToComplex`.

```lean
lemma isReindexing_colorToComplex {n m : ℕ}
    {c : Fin n → realLorentzTensor.Color} {c1 : Fin m → realLorentzTensor.Color}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) :
    IsReindexing (colorToComplex ∘ c) (colorToComplex ∘ c1) σ
```

**`realLorentzTensor.permT_basis_real`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L420).

> `permT` sends basis vectors to basis vectors.

```lean
lemma permT_basis_real {n m : ℕ}
    {c : Fin n → realLorentzTensor.Color} {c1 : Fin m → realLorentzTensor.Color}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ)
    (b : ComponentIdx (S := realLorentzTensor) c) :
    permT (S := realLorentzTensor) σ h ((Tensor.basis (S := realLorentzTensor) c) b)
    = (Tensor.basis (S := realLorentzTensor) c1)
      (fun j => b (σ j))
```

**`realLorentzTensor.permT_basis_complex`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L429).

```lean
lemma permT_basis_complex {n m : ℕ}
    {c : Fin n → complexLorentzTensor.Color} {c1 : Fin m → complexLorentzTensor.Color}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ)
    (b : ComponentIdx (S := complexLorentzTensor) c) :
    permT (S := complexLorentzTensor) σ h ((Tensor.basis (S := complexLorentzTensor) c) b)
      =
    (Tensor.basis (S := complexLorentzTensor) c1)
      (fun j => basisIdxCongr (h.2 j) (b (σ j)))
```

**`realLorentzTensor.permT_toComplex`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L441).

> The map `toComplex` commutes with permT.

```lean
lemma permT_toComplex {n m : ℕ}
    {c : Fin n → realLorentzTensor.Color}
    {c1 : Fin m → realLorentzTensor.Color}
    {σ : Fin m → Fin n} (h : IsReindexing c c1 σ) (t : ℝT(3, c)) :
    toComplex (permT (S := realLorentzTensor) σ h t)
      =
    permT (S := complexLorentzTensor) σ (isReindexing_colorToComplex (c := c) (c1 := c1) h)
      (toComplex (c := c) t)
```

### D. Compatibility with tensor products: `prodT`

**`realLorentzTensor.colorToComplex_append`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L467).

> `colorToComplex` commutes with `Fin.append` (as functions).

```lean
lemma colorToComplex_append {n m : ℕ}
    (c : Fin n → realLorentzTensor.Color) (c1 : Fin m → realLorentzTensor.Color) :
    (colorToComplex ∘ Fin.append c c1) = Fin.append (colorToComplex ∘ c) (colorToComplex ∘ c1)
```

**`realLorentzTensor.isReindexing_prodTColorToComplex`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L473).

```lean
lemma isReindexing_prodTColorToComplex {n m : ℕ}
    {c : Fin n → realLorentzTensor.Color} {c1 : Fin m → realLorentzTensor.Color} :
    IsReindexing (Fin.append (colorToComplex ∘ c) (colorToComplex ∘ c1))
      (colorToComplex ∘ Fin.append c c1)
      (id : Fin (n + m) → Fin (n + m))
```

**`realLorentzTensor.prodTColorToComplex`**, a def, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L482).

> `prodT` on the complex side, with colors written as `colorToComplex ∘ Fin.append ...`.
> This is `prodT` followed by a cast using `colorToComplex_append`.

```lean
noncomputable def prodTColorToComplex {n m : ℕ}
    {c : Fin n → realLorentzTensor.Color} {c1 : Fin m → realLorentzTensor.Color} :
    ℂT(colorToComplex ∘ c) → ℂT(colorToComplex ∘ c1) → ℂT(colorToComplex ∘ Fin.append c c1)
```

**`realLorentzTensor.complexify_prod`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L506).

> `complexify` commutes with `prod` of component indices.

```lean
lemma complexify_prod {n m : ℕ}
    {c : Fin n → realLorentzTensor.Color} {c1 : Fin m → realLorentzTensor.Color}
    (b : ComponentIdx (S := realLorentzTensor) c)
    (b1 : ComponentIdx (S := realLorentzTensor) c1) :
    ComponentIdx.complexify (c := Fin.append c c1) (ComponentIdx.prod.symm (b, b1))
      =
    cast (congr_arg ComponentIdx (colorToComplex_append c c1).symm)
      (ComponentIdx.prod.symm (ComponentIdx.complexify (c := c) b,
        ComponentIdx.complexify (c := c1) b1))
```

**`realLorentzTensor.prodT_toComplex`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L523).

> The map `toComplex` commutes with prodT.

```lean
lemma prodT_toComplex {n m : ℕ}
    {c : Fin n → realLorentzTensor.Color}
    {c1 : Fin m → realLorentzTensor.Color}
    (t : ℝT(3, c)) (t1 : ℝT(3, c1)) :
    toComplex (c := Fin.append c c1) (prodT (S := realLorentzTensor) t t1)
      =
    prodTColorToComplex (c := c) (c1 := c1)
      (toComplex (c := c) t) (toComplex (c := c1) t1)
```

### E. Compatibility with contraction: `contrT`

**`realLorentzTensor.tau_colorToComplex`**, a lemma, [line 555](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L555).

> `τ` commutes with `colorToComplex` on the Lorentz `up/down` colors.

```lean
lemma tau_colorToComplex (x : realLorentzTensor.Color) :
    (complexLorentzTensor).τ (colorToComplex x) = colorToComplex ((realLorentzTensor).τ x)
```

**`realLorentzTensor.ComponentIdx.complexify_comp_succSuccAbove`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L564).

> `complexify` commutes with precomposition by `succSuccAbove`.
> We use `fun k => b (Fin.succSuccAbove i j k)` and direct application
> `(ComponentIdx.complexify b) (Fin.succSuccAbove i j m)` rather than composition so that
> dependent `ComponentIdx` types unify correctly (avoiding `Function.comp` type mismatch).

```lean
lemma ComponentIdx.complexify_comp_succSuccAbove
    {n : ℕ} {c : Fin (n + 1 + 1) → realLorentzTensor.Color}
    {i j : Fin (n + 1 + 1)} (b : ComponentIdx (S := realLorentzTensor) c) (m : Fin n) :
    (ComponentIdx.complexify (c := c ∘ Fin.succSuccAbove i j)
      (fun k => b (Fin.succSuccAbove i j k))) m =
    (ComponentIdx.complexify (c := c) b) (Fin.succSuccAbove i j m)
```

**`realLorentzTensor.toComplex_contrP_basisVector`**, a lemma, [line 574](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L574).

> For a real basis vector, `toComplex(contrP(basisVector c b))` equals
> `contrP(basisVector (colorToComplex ∘ c) (complexify b))` (complex species).

```lean
lemma toComplex_contrP_basisVector {n : ℕ} {c : Fin (n + 1 + 1) → realLorentzTensor.Color}
    {i j : Fin (n + 1 + 1)} (h : i ≠ j ∧ (realLorentzTensor).τ (c i) = c j)
    (b : ComponentIdx (S := realLorentzTensor) c) :
    toComplex (c := c ∘ Fin.succSuccAbove i j)
      (Pure.contrP (S := realLorentzTensor) i j h (Pure.basisVector c b))
      =
    Pure.contrP (S := complexLorentzTensor) i j
      (by
        simpa [Function.comp_apply] using And.intro h.1
          (by simpa [tau_colorToComplex] using congrArg colorToComplex h.2))
      (Pure.basisVector (colorToComplex ∘ c) (ComponentIdx.complexify b))
```

**`realLorentzTensor.contrT_toComplex`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L602).

> The map `toComplex` commutes with `contrT`.

```lean
lemma contrT_toComplex {n : ℕ}
    {c : Fin (n + 1 + 1) → realLorentzTensor.Color} {i j : Fin (n + 1 + 1)}
    (h : i ≠ j ∧ (realLorentzTensor).τ (c i) = c j) (t : ℝT(3, c)) :
    toComplex (c := c ∘ Fin.succSuccAbove i j) (contrT (S := realLorentzTensor) n i j h t)
      =
    contrT (S := complexLorentzTensor) n i j (by
        simpa [Function.comp_apply] using
          And.intro h.1 (by
            simpa [tau_colorToComplex] using congrArg colorToComplex h.2))
      (toComplex (c := c) t)
```

### F. Compatibility with evaluation: `evalT`

**`realLorentzTensor.ComponentIdx.complexify_comp_succAbove`**, a lemma, [line 632](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L632).

> `complexify` commutes with precomposition by `succAbove`.

```lean
lemma ComponentIdx.complexify_comp_succAbove
    {n : ℕ} {c : Fin (n + 1) → realLorentzTensor.Color} (i : Fin (n + 1))
    (b : ComponentIdx (S := realLorentzTensor) c) (m : Fin n) :
    (ComponentIdx.complexify (c := c ∘ i.succAbove) (fun k => b (i.succAbove k))) m =
    (ComponentIdx.complexify (c := c) b) (i.succAbove m)
```

**`realLorentzTensor.evalIdxToComplex`**, a def, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L640).

> Convert an evaluation index from the real basis index to the complex basis index.

```lean
noncomputable def evalIdxToComplex {n : ℕ}
    {c : Fin (n + 1) → realLorentzTensor.Color} (i : Fin (n + 1))
    (b : Fin 1 ⊕ Fin 3) : complexLorentzTensor.basisIdx ((colorToComplex ∘ c) i)
```

**`realLorentzTensor.evalTColorToComplex`**, a def, [line 647](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L647).

> `evalT` on the complex side, but with output colors as `colorToComplex ∘ (c ∘ i.succAbove)`.
> Implemented via `permT (σ := id) (by simp)` as a transport.

```lean
noncomputable def evalTColorToComplex {n : ℕ}
    {c : Fin (n + 1) → realLorentzTensor.Color} (i : Fin (n + 1))
    (b : Fin 1 ⊕ Fin 3) :
    ℂT(colorToComplex ∘ c) → ℂT(colorToComplex ∘ (c ∘ i.succAbove))
```

**`realLorentzTensor.toComplex_evalP_basisVector`**, a lemma, [line 662](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L662).

> For a real basis vector, `toComplex(evalP(basisVector c b))` equals
> `evalP(basisVector (colorToComplex ∘ c) (complexify b))` (complex species).

```lean
lemma toComplex_evalP_basisVector {n : ℕ} {c : Fin (n + 1) → realLorentzTensor.Color}
    (i : Fin (n + 1)) (b : Fin 1 ⊕ Fin 3)
    (b' : ComponentIdx (S := realLorentzTensor) c) :
    toComplex (c := c ∘ i.succAbove)
      (Pure.evalP (S := realLorentzTensor) i b (Pure.basisVector c b'))
      =
    permT (S := complexLorentzTensor) (σ := (id : Fin n → Fin n))
      (by simp [Function.comp_apply])
      (Pure.evalP (S := complexLorentzTensor) i (evalIdxToComplex (c := c) i b)
        (Pure.basisVector (colorToComplex ∘ c) (ComponentIdx.complexify b')))
```

**`realLorentzTensor.evalT_toComplex`**, a lemma, [line 693](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean#L693).

> The map `toComplex` commutes with `evalT`.

```lean
lemma evalT_toComplex {n : ℕ}
    {c : Fin (n + 1) → realLorentzTensor.Color}
    (i : Fin (n + 1)) (b : Fin 1 ⊕ Fin 3) (t : ℝT(3, c)) :
    toComplex (c := c ∘ i.succAbove)
        ((TensorSpecies.Tensor.evalT (S := realLorentzTensor) (c := c) i b) t)
      =
    evalTColorToComplex (c := c) i b (toComplex (c := c) t)
```

## Depends on

- [Physlib.Relativity.Tensors.ComplexTensor.Basic](../part-01/complextensor-basic.md)

## Sources

- [Physlib/Relativity/Tensors/RealTensor/ToComplex.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/RealTensor/ToComplex.lean)
