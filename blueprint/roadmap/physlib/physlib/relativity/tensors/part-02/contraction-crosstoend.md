---
declaration: module
origin: cited
lean: TensorSpecies.Tensor.crossToEnd, TensorSpecies.Tensor.crossToEnd_two, TensorSpecies.Tensor.crossToEnd_basis, TensorSpecies.Tensor.crossToEnd_basis_repr_eq_sum_fin, TensorSpecies.Tensor.crossToEnd_basis_repr_eq_sum_dual, TensorSpecies.Tensor.crossToEnd_pair_basis_repr, TensorSpecies.Tensor.toMatrix_crossToEnd_pair, TensorSpecies.Tensor.crossToEnd_equivariant
statement: formalized
proof: formalized
---

# Cross contraction at named slots

The module `Physlib.Relativity.Tensors.Contraction.CrossToEnd`, [Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean): 11 declarations, 11 with a docstring.

## i. Overview

> `contrT` contracts two slots of a single tensor. Contracting a slot of one tensor against a slot of
> another (`T^{μν} u_ν`, `g_{μν} v^ν`) is `prodT` then `contrT`, which leaves every call site to
> locate the two post-product slots and discharge the distinctness and `τ`-duality goals.
>
> `crossToEnd i j hc` performs that contraction at named slots `i` and `j`, with
> `hc : S.τ (cA i) = cB j` recording their `τ`-duality. The output color is
> `Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove)`: every slot of `cA` except `i`, in order, then
> every slot of `cB` except `j`. These are the survivors. Any slot is reachable:
> `crossToEnd 2 0 _ R u` reads as `R_{μνρσ} u^ρ`. The survivors are appended rather than interleaved,
> and appending is associative, so both bracketings of a chain produce the same survivor list in the
> same order.
>
> The complementary convention keeps the replacement index in place. Contracting slot `1` of
> `![c₀, c₁, c₂, c₃]` against a rank-two `![S.τ c₁, d]` gives `![c₀, c₂, c₃, d]` here and
> `![c₀, d, c₂, c₃]` there; that operation is `crossToSlot`, built on this substrate in
> `Physlib.Relativity.Tensors.Contraction.CrossToSlot`.

## ii. Key results

> - `TensorSpecies.Tensor.crossToEnd` : the slot-addressed cross contraction.
> - `TensorSpecies.Tensor.crossToEnd_two` : at rank two on each factor, a plain `contrT` of the
>     product on slots `1, 2`.
> - `TensorSpecies.Tensor.crossToEnd_basis` : the contraction of two basis tensors, which
>     characterises `crossToEnd`.
> - `TensorSpecies.Tensor.crossToEnd_basis_repr_eq_sum_fin` : the component formula at arbitrary
>     slots and ranks for any species, the contraction of the two contracted basis vectors left as an
>     opaque coefficient.
> - `TensorSpecies.Tensor.crossToEnd_basis_repr_eq_sum_dual` : the same formula for a species with
>     contraction-dual bases, the δ collapsing the two sums into one.
> - `TensorSpecies.Tensor.crossToEnd_pair_basis_repr` : the component formula at rank two on each
>     factor.
> - `TensorSpecies.Tensor.toMatrix_crossToEnd_pair` : the same as a matrix equation, cross
>     contraction being the product of the component matrices.
> - `TensorSpecies.Tensor.crossToEnd_equivariant` : the contraction commutes with the `G`-action.
> - `TensorSpecies.Tensor.crossToEnd_assoc_rankTwo` : rebracket the chain
>     `A —(iA·0)— B —(last·0)— C` at rank-two `B` and `C`, up to `permT id`. Not full associativity.
> - `TensorSpecies.Tensor.crossToEnd_permT_left` / `crossToEnd_permT_right` : move a relabelling of
>     the left or right factor through the contraction, the contracted slot moving with it.

## iv. References

> * None.

## A. Slot-addressed cross contraction

**`TensorSpecies.Tensor.crossToEnd`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L91).

> Slot-addressed cross contraction: contract slot `i` of `t1` against slot `j` of `t2`. The
> survivors are `t1`'s slots except `i` followed by `t2`'s slots except `j`, so the output color is
> a clean `Fin (nA + nB) → C` and a chain composes without recasts.

```lean
noncomputable def crossToEnd {nA nB : ℕ} {cA : Fin (nA + 1) → C} {cB : Fin (nB + 1) → C}
    (i : Fin (nA + 1)) (j : Fin (nB + 1)) (hc : S.τ (cA i) = cB j) :
    Tensor S cA →ₗ[k] Tensor S cB →ₗ[k]
      Tensor S (Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove))
```

**`TensorSpecies.Tensor.crossToEnd_two`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L121).

> Cross-contracting the last slot of a rank-2 tensor `A` with the `0`-slot of a rank-2 tensor `B`
> is a plain `contrT` of their product on the middle slots `1, 2`, up to a color recast. Discharging
> the slot arithmetic once lets a `contrT`-level identity lift to `crossToEnd` by one rewrite.

```lean
lemma crossToEnd_two {cA cB : Fin 2 → C} (h : S.τ (cA (Fin.last 1)) = cB 0)
    (A : Tensor S cA) (B : Tensor S cB) :
    crossToEnd (Fin.last 1) (0 : Fin 2) h A B
      = permT (id : Fin 2 → Fin 2) (IsReindexing.on_id.mpr (fun i => by fin_cases i <;> rfl))
          (contrT 2 (1 : Fin 4) (2 : Fin 4)
            (by
              refine ⟨by decide, ?_⟩
              rw [show (1 : Fin 4) = Fin.castAdd 2 (1 : Fin 2) from rfl,
                  show (2 : Fin 4) = Fin.natAdd 2 (0 : Fin 2) from rfl,
                  Fin.append_left, Fin.append_right]
              exact h)
            (prodT A B))
```

## B. Component formulas and equivariance

> `crossToEnd i j hc` is the curried bilinear map `LinearMap.compr₂ prodT` post-composed with the
> linear `permT`/`contrT` factors, so additivity, scalar multiplication, and finite sums in either
> argument are already the generic `map_add`/`map_smul`/`map_sum` and need no lemmas of their own.

**`TensorSpecies.Tensor.crossToEnd_basis`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L153).

> Cross contraction of two basis tensors: the contraction of the two contracted basis vectors
> times the basis tensor of the surviving labels. These values determine `crossToEnd i j hc`, a
> bilinear map in the two tensors.

```lean
lemma crossToEnd_basis {nA nB : ℕ} {cA : Fin (nA + 1) → C} {cB : Fin (nB + 1) → C}
    (i : Fin (nA + 1)) (j : Fin (nB + 1)) (hc : S.τ (cA i) = cB j)
    (φA : ComponentIdx (S := S) cA) (φB : ComponentIdx (S := S) cB) :
    crossToEnd i j hc (basis cA φA) (basis cB φB) =
      S.contr (cA i) (b (cA i) (φA i) ⊗ₜ[k] b (S.τ (cA i)) (basisIdxCongr hc.symm (φB j))) •
        basis (Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove))
          (ComponentIdx.prod.symm (fun m => φA (i.succAbove m), fun m => φB (j.succAbove m)))
```

**`TensorSpecies.Tensor.crossToEnd_basis_repr_eq_sum_fin`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L189).

> The component formula for a cross contraction at arbitrary slots and ranks, for any species:
> each contracted label is summed over its own slot, with the contraction of the two basis vectors as
> coefficient. The counterpart of `contrT_basis_repr_apply_eq_sum_fin` for two tensors.

```lean
lemma crossToEnd_basis_repr_eq_sum_fin {nA nB : ℕ} {cA : Fin (nA + 1) → C}
    {cB : Fin (nB + 1) → C} (i : Fin (nA + 1)) (j : Fin (nB + 1)) (hc : S.τ (cA i) = cB j)
    (t1 : Tensor S cA) (t2 : Tensor S cB)
    (φ : ComponentIdx (S := S) (Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove))) :
    (basis (Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove))).repr
        (crossToEnd i j hc t1 t2) φ =
      ∑ x₁ : basisIdx (cA i), ∑ x₂ : basisIdx (cB j),
        ((basis cA).repr t1 (ComponentIdx.insert i (x₁, φ.prod.1)) *
          (basis cB).repr t2 (ComponentIdx.insert j (x₂, φ.prod.2))) *
        S.contr (cA i) (b (cA i) x₁ ⊗ₜ[k]
          b (S.τ (cA i)) (basisIdxCongr (by rw [hc]) x₂))
```

**`TensorSpecies.Tensor.crossToEnd_basis_repr_eq_sum_dual`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L222).

> The component formula for a cross contraction at arbitrary slots and ranks, for a species with
> contraction-dual bases: the contraction coefficient is `δ` and one sum remains, the contracted label
> of `t2` matched to that of `t1` by `contrDualIdxEquiv`.

```lean
lemma crossToEnd_basis_repr_eq_sum_dual [HasContrDualBases S] {nA nB : ℕ} {cA : Fin (nA + 1) → C}
    {cB : Fin (nB + 1) → C} (i : Fin (nA + 1)) (j : Fin (nB + 1)) (hc : S.τ (cA i) = cB j)
    (t1 : Tensor S cA) (t2 : Tensor S cB)
    (φ : ComponentIdx (S := S) (Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove))) :
    (basis (Fin.append (cA ∘ i.succAbove) (cB ∘ j.succAbove))).repr
        (crossToEnd i j hc t1 t2) φ =
      ∑ x : basisIdx (cA i),
        (basis cA).repr t1 (ComponentIdx.insert i (x, φ.prod.1)) *
        (basis cB).repr t2 (ComponentIdx.insert j
          (basisIdxCongr hc ((HasContrDualBases.contrDualIdxEquiv S (cA i)).symm x),
            φ.prod.2))
```

**`TensorSpecies.Tensor.crossToEnd_pair_basis_repr`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L240).

> The component formula for cross-contracting the last slot of a rank-two tensor with the first
> slot of another. The surviving labels are supplied as a dependent pair, so the formula applies when
> the species has colour-dependent basis-index types.

```lean
lemma crossToEnd_pair_basis_repr [HasContrDualBases S] {c0 c1 c2 c3 : C} (h : S.τ c1 = c2)
    (t1 : Tensor S ![c0, c1]) (t2 : Tensor S ![c2, c3])
    (y0 : basisIdx c0) (y3 : basisIdx c3) :
    (basis (Fin.append (![c0, c1] ∘ (Fin.last 1).succAbove)
        (![c2, c3] ∘ (0 : Fin 2).succAbove))).repr
      (crossToEnd (Fin.last 1) (0 : Fin 2) h t1 t2)
      (ComponentIdx.pair.symm (y0, y3)) =
      ∑ x : basisIdx c1,
        (basis ![c0, c1]).repr t1 (ComponentIdx.pair.symm (y0, x)) *
        (basis ![c2, c3]).repr t2
          (ComponentIdx.pair.symm
            (basisIdxCongr h ((HasContrDualBases.contrDualIdxEquiv S c1).symm x), y3))
```

**`TensorSpecies.Tensor.toMatrix_crossToEnd_pair`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L259).

> Cross contraction of two rank-two tensors is the product of their component matrices, the
> middle labels matched by `HasContrDualBases.dualIdxEquiv`.

```lean
lemma toMatrix_crossToEnd_pair [HasContrDualBases S] {c0 c1 c2 c3 : C} (h : S.τ c1 = c2)
    (t1 : S.Tensor ![c0, c1]) (t2 : S.Tensor ![c2, c3]) :
    toMatrix (crossToEnd (Fin.last 1) (0 : Fin 2) h t1 t2) =
      toMatrix t1 * (toMatrix t2).submatrix
        (fun x : basisIdx (![c0, c1] 1) => HasContrDualBases.dualIdxEquiv h x) id
```

**`TensorSpecies.Tensor.crossToEnd_equivariant`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L269).

> Cross contraction is `G`-equivariant, each of `prodT`, `contrT` and `permT` being so.

```lean
lemma crossToEnd_equivariant {nA nB : ℕ} {cA : Fin (nA + 1) → C} {cB : Fin (nB + 1) → C}
    (i : Fin (nA + 1)) (j : Fin (nB + 1)) (hc : S.τ (cA i) = cB j) (g : G)
    (t1 : Tensor S cA) (t2 : Tensor S cB) :
    crossToEnd i j hc (g • t1) (g • t2) = g • crossToEnd i j hc t1 t2
```

## C. Rebracketing the metric chain

> Both bracketings reduce to one product contracted at its two seams in opposite order, then drop to
> the pure-tensor level, so the seam permutation never crosses a contraction under `whnf`;
> `Pure.permP_dropPair_dropPair_congr` closes the step.

**`TensorSpecies.Tensor.crossToEnd_assoc_rankTwo`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L296).

> Rebracket the chain `A —(iA·0)— B —(last·0)— C` for rank-two `B` and `C`: contracting `A·B`
> first and then `·C` equals contracting `B·C` first and then `A·`, up to the color recast
> `permT id`.
>
> Not full associativity: only `A`'s attachment slot `iA` is free. `B`'s rank two is what makes the
> statement possible, the second contraction being addressed at `Fin.last nA`, the slot `B`'s unique
> survivor occupies in `A·B`. Other slots are reached by conjugating with the `permT` commutators.
>
> With `A := T`, `B := g`, `C := g⁻¹` this reassociates `(T·g)·g⁻¹` to `T·(g·g⁻¹)`, after which
> `g·g⁻¹` collapses to the unit tensor: the step behind raising then lowering a named index.

```lean
lemma crossToEnd_assoc_rankTwo {nA : ℕ}
    {cA : Fin (nA + 1) → C} {cB cC : Fin 2 → C}
    (iA : Fin (nA + 1))
    (hc1 : S.τ (cA iA) = cB 0)
    (hc2 : S.τ (cB (Fin.last 1)) = cC 0)
    (tA : Tensor S cA) (tB : Tensor S cB) (tC : Tensor S cC) :
    crossToEnd (Fin.last nA) 0
        (by
          rw [show (Fin.last nA : Fin (nA + 1)) = Fin.natAdd nA (Fin.last 0) from
              Fin.ext (by simp), Fin.append_right, Function.comp_apply, Fin.succAbove_zero,
            Fin.succ_last]
          exact hc2)
        (crossToEnd iA 0 hc1 tA tB) tC =
      permT id
        (IsReindexing.on_id.mpr fun i => by
          refine Fin.addCases (fun a => ?_) (fun a => ?_) i
          · simp only [Fin.append_left, Function.comp_apply, Fin.succAbove_last,
              show a.castSucc = Fin.castAdd 1 a from rfl, Fin.append_left]
          · simp only [Fin.append_right, Function.comp_apply, Fin.succAbove_zero]
            fin_cases a
            rfl)
        (crossToEnd iA 0
          (by
            rw [show (0 : Fin (1 + 1)) = Fin.castAdd 1 (0 : Fin 1) from rfl, Fin.append_left,
              Function.comp_apply, Fin.succAbove_last, Fin.castSucc_zero]
            exact hc1)
          tA
          (crossToEnd (Fin.last 1) 0 hc2 tB tC))
```

## D. Permutation commutators

> Moving a relabelling of one factor through the slot-addressed contraction. The relabelling `σ` need
> not fix the contracted slot, so it carries the contraction from slot `i` to slot `σ i` and restricts
> to the survivors as a map `σ'` filling the square `(σ i).succAbove ∘ σ' = σ ∘ i.succAbove`. Taking
> `σ'` as an argument rather than deriving it lets a caller supply the survivor map it wants (`id`, a
> swap-induced map) instead of an opaque composite.

**`TensorSpecies.Tensor.crossToEnd_permT_left`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L441).

> Left commutator: contracting slot `i` of `permT σ t1` equals contracting slot `σ i` of `t1`,
> then relabelling the survivors by `σ'`. The square `hσ'` records how `σ'` carries the complement
> of `i` to the complement of `σ i`, and implies its bijectivity.

```lean
lemma crossToEnd_permT_left {nA nB : ℕ} {cA cA' : Fin (nA + 1) → C}
    {cB : Fin (nB + 1) → C}
    (i : Fin (nA + 1)) (j : Fin (nB + 1))
    (σ : Fin (nA + 1) → Fin (nA + 1)) (σ' : Fin nA → Fin nA)
    (hσ : IsReindexing cA cA' σ)
    (hσ' : (σ i).succAbove ∘ σ' = σ ∘ i.succAbove)
    (hc : S.τ (cA' i) = cB j)
    (t1 : Tensor S cA) (t2 : Tensor S cB) :
    crossToEnd i j hc (permT σ hσ t1) t2 =
      permT (Fin.append (Fin.castAdd nB ∘ σ') (Fin.natAdd nA))
        (IsReindexing.append_congr_left (cB ∘ j.succAbove)
          (IsReindexing.succAbove_of_succAbove_eq i hσ hσ'))
        (crossToEnd (σ i) j (by rw [hσ.2 i]; exact hc) t1 t2)
```

**`TensorSpecies.Tensor.crossToEnd_permT_right`**, a lemma, [line 480](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean#L480).

> Right commutator, the mirror of `crossToEnd_permT_left`: contracting slot `j` of `permT σ t2`
> equals contracting slot `σ j` of `t2`, then relabelling the survivors by `σ'`.

```lean
lemma crossToEnd_permT_right {nA nB : ℕ} {cA : Fin (nA + 1) → C}
    {cB cB' : Fin (nB + 1) → C}
    (i : Fin (nA + 1)) (j : Fin (nB + 1))
    (σ : Fin (nB + 1) → Fin (nB + 1)) (σ' : Fin nB → Fin nB)
    (hσ : IsReindexing cB cB' σ)
    (hσ' : (σ j).succAbove ∘ σ' = σ ∘ j.succAbove)
    (hc : S.τ (cA i) = cB' j)
    (t1 : Tensor S cA) (t2 : Tensor S cB) :
    crossToEnd i j hc t1 (permT σ hσ t2) =
      permT (Fin.append (Fin.castAdd nB) (Fin.natAdd nA ∘ σ'))
        (IsReindexing.append_congr_right (cA ∘ i.succAbove)
          (IsReindexing.succAbove_of_succAbove_eq j hσ hσ'))
        (crossToEnd i (σ j) (by rw [hσ.2 j]; exact hc) t1 t2)
```

## Depends on

- [Component indices split at a single slot](componentidx-insert.md)
- [Constructors of tensors.](../part-01/constructors.md)
- [Species whose bases at dual colors are dual bases](../part-04/tensorspecies-dualbasis.md)

## Proof depends on

- [Contractions on basis tensors](contraction-basis.md)

## Sources

- [Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Contraction/CrossToEnd.lean)
