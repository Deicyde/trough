---
declaration: module
origin: cited
lean: ConjTensorSpecies, ConjTensorSpecies.bar_tau_of_bar, ConjTensorSpecies.conjEquiv, ConjTensorSpecies.conjEquiv_basis, ConjTensorSpecies.conjEquiv_basis_repr, ConjTensorSpecies.conjEquiv_equivariant, ConjTensorSpecies.componentReindex, ConjTensorSpecies.conjT
statement: formalized
proof: formalized
---

# Conjugation structure on a tensor species

The module `Physlib.Relativity.Tensors.Conjugation.Basic`, [Physlib/Relativity/Tensors/Conjugation/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean): 36 declarations, 29 with a docstring; 1 private, not shown.

## i. Overview

> Each index of a tensor carries a colour naming the representation it transforms in. A species
> already has the variance dual `τ c`, the colour an index must meet to contract. Conjugation adds a
> second involution, the conjugate colour `bar c`: the colour an index transforms in after complex
> conjugation. A spinor index is the textbook example: complex conjugation sends a left-handed Weyl
> spinor to a right-handed one, `(ψ_α)* = ψ̄_α̇`, so `bar` swaps the left- and right-handed colours
> while fixing a real vector colour. Variance is untouched, so `bar` commutes with `τ`. In an N=1
> chiral sector `bar` swaps chiral and anti-chiral indices.
>
> `conjT` conjugates a tensor at the basis level: `star` each coordinate in the species basis and
> place it at the conjugate colour. Reality and Hermiticity are stated through it: a tensor is real
> when conjugation fixes it, and a metric is Hermitian when conjugating it swaps its two indices.
>
> Conjugation is intrinsic species data, not a detachable add-on: a `ConjTensorSpecies` is a
> `TensorSpecies` bundled (`extends`) with the conjugate-colour involution `bar` and the coherence
> the recipe needs. `bar c` shares basis labels with `c` (`barIdx_eq`) and the contraction
> coefficients survive `star` (`conj_contrComm`), which together make conjugation commute with
> contraction. `conjT` is then `conj`-semilinear, involutive, and commutes with contraction; the
> last makes reality and Hermiticity compatible with raising and lowering indices.
>
> At the single-index level, `conjEquiv : V c ≃ₛₗ V (bar c)` realises this conjugation: it reads a
> vector's coordinates, conjugates them with `ConjModule.starFinsupp`, and re-seats them at the
> conjugate colour. It rests on the conjugate module `ConjModule`
> (`Physlib.Mathematics.Modules.ConjModule`), the same vectors with the scalar action twisted by
> conjugation (`i` acts as `−i`). Equipping the conjugate colours with such conjugate-module
> carriers is what makes a metric `V c ⊗ V (bar c) → k` genuinely bilinear and `IsHermitian` an
> honest conjugate-transpose.

## ii. Key results

> - `ConjTensorSpecies` is a tensor species bundled with its conjugation.
> - `ConjTensorSpecies.conjT` is the conjugation of a tensor.
> - `ConjTensorSpecies.conjT_conjT` proves that conjugation is an involution.
> - `ConjTensorSpecies.conjT_contrT` proves that conjugation commutes with contraction.
> - `ConjTensorSpecies.conjT_eq_permT_iff` is the componentwise criterion for
>   `conjT t = permT σ h t'`, the workhorse for proving reality and Hermiticity conditions.
> - `ConjTensorSpecies.conjEquiv` is the single-slot conjugate-linear isomorphism `V c ≃ₛₗ V (bar c)`.
> - `ConjTensorSpecies.IsHermitian` is the structural conjugate-transpose condition on a metric slot.
> - `ConjTensorSpecies.toSquareMatrix` is the square component matrix of a rank-two tensor whose
>   second colour is the conjugate of its first;
>   `ConjTensorSpecies.conjT_eq_permT_swap_iff_toSquareMatrix_isHermitian` says that conjugation swaps
>   the two slots of `M` exactly when this matrix is Hermitian.
> - `ConjTensorSpecies.isContrDualMatching_bar` and `ConjTensorSpecies.dualIdxEquiv_bar` say that
>   conjugation preserves which basis labels pair to `1` under contraction: the basis vectors of
>   `bar c` and `τ (bar c)` with labels `i` and `j` contract to `1` exactly when those of `c` and
>   `τ c` with the same labels do.
> - `ConjTensorSpecies.conjSingleT` is the conjugation of a one-slot tensor, at the colour
>   `![bar x]`; `ConjTensorSpecies.conjSingleT_basis` is its action on basis vectors.
> - `ConjTensorSpecies.toSesqForm` is the sesquilinear form `s, t ↦ M(t, s̄)` of a rank-two tensor
>   `M` with `bar (c 0) = c 1`. Hermiticity of `M` is Hermiticity of this form, Mathlib's
>   `LinearMap.IsSymm`;
>   `ConjTensorSpecies.isSymm_toSesqForm_iff_conjT_eq_permT` and
>   `ConjTensorSpecies.isSymm_toSesqForm_iff_toSquareMatrix_isHermitian` are its tensor and matrix
>   forms.
> - `ConjTensorSpecies.isPosDef_toSesqForm_iff_toSquareMatrix_posDef`: `M` is positive-definite, i.e.
>   its form is (`LinearMap.IsPosDef`), exactly when its square component matrix is `Matrix.PosDef`.

## A. The conjugation structure

> A `ConjTensorSpecies` bundles a `TensorSpecies` (`extends`) with the conjugation data.
> Conjugation is defined at the basis level, where it is "`star` the components" (§B). Four of the
> new fields are
> bookkeeping on colours and index sets, trivial to supply per instance: `bar` (the conjugate-colour
> involution), `bar_involution`, `bar_tau` (it commutes with `τ`), and `barIdx_eq` (a colour and its
> conjugate share basis labels). The one substantive field is `conj_contrComm`, that the contraction
> coefficients are unchanged by `star`; this is what makes conjugation commute with contraction (§D),
> and for a real (δ) contraction it is `star δ = δ`.

**`ConjTensorSpecies`**, a structure, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L112).

> A tensor species bundled with a conjugation. Beyond the `TensorSpecies` it `extends`, it carries
> the conjugate-colour involution `bar`, the index-set identification `barIdx_eq`, and the
> contraction-coherence `conj_contrComm`. Also carries `bar_involution` and `bar_tau` (that `bar` is
> involutive and commutes with the variance dual).

```lean
structure ConjTensorSpecies (k : Type) [CommRing k] [StarRing k] (C : Type) (G : Type) [Group G]
    (V : C → Type) [∀ c, AddCommGroup (V c)] [∀ c, Module k (V c)]
    (basisIdx : C → Type) [∀ c, Fintype (basisIdx c)] [∀ c, DecidableEq (basisIdx c)]
    (rep : (c : C) → Representation k G (V c)) (b : (c : C) → Basis (basisIdx c) k (V c))
    extends TensorSpecies k C G V basisIdx rep b where
  /-- The conjugate colour: the colour an index transforms in under complex conjugation; preserves
  variance (commutes with `τ`). -/
  bar : C → C
  /-- `bar` is an involution. -/
  bar_involution : Function.Involutive bar
  /-- `bar` commutes with the variance dual `τ`. -/
  bar_tau : ∀ c, bar (toTensorSpecies.τ c) = toTensorSpecies.τ (bar c)
  /-- Conjugation fixes the index set: the conjugate colour reuses the same basis labels.
  Conjugation conjugates components in an adapted basis; it never permutes labels, so the label
  sets of `c` and `bar c` coincide. -/
  barIdx_eq : ∀ c, basisIdx (bar c) = basisIdx c
  /-- Conjugation is equivariant: it preserves the action of the group. -/
  conj_basis_equivariant : ∀ (c : C) (g : G) (i j : basisIdx c),
      (b c).repr (rep c g (b c i)) j = star ((b (bar c)).repr
      (rep (bar c) g (b (bar c) (Equiv.cast (barIdx_eq c).symm i)))
      (Equiv.cast (barIdx_eq c).symm j))
  /-- Conjugation is compatible with contraction at the basis level: `star` of the contraction
  coefficient at colour `d` equals the coefficient at the conjugate colour `bar d`, with basis
  labels carried over by `barIdx_eq`. For a real (δ) contraction this is `star δ = δ`. -/
  conj_contrComm : ∀ (d : C) (x₁ : basisIdx d) (x₂ : basisIdx (toTensorSpecies.τ d)),
      star (toTensorSpecies.contr d (b d x₁ ⊗ₜ[k] b (toTensorSpecies.τ d) x₂))
        = toTensorSpecies.contr (bar d) (b (bar d) ((Equiv.cast (barIdx_eq d)).symm x₁) ⊗ₜ[k]
            b (toTensorSpecies.τ (bar d)) (basisIdxCongr (bar_tau d)
              ((Equiv.cast (barIdx_eq (toTensorSpecies.τ d))).symm x₂)))
```

**`ConjTensorSpecies.bar_tau_of_bar`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L153).

> If `bar a = d`, then `bar (τ d) = τ a`.

```lean
lemma bar_tau_of_bar {a d : C} (hbar : S.bar a = d) : S.bar (S.τ d) = S.τ a
```

## B. The conjugation of vectors

> `conjEquiv` is the conjugate-linear isomorphism `V c ≃ₛₗ[starRingEnd k] V (bar c)`: read off the
> coordinates of a vector in the species basis, conjugate them (`star`), and re-seat them as the
> coordinates at the conjugate colour (the index sets agree by `barIdx_eq`). It is the single-slot
> shadow of `conjT`, packaged as a bundled equivalence so the Hermitian-metric layer can apply it to a
> metric slot. Semilinearity is built in via the coordinate `star`; invertibility is `star`'s
> involutivity together with `bar`'s.

**`ConjTensorSpecies.conjEquiv`**, a def, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L171).

> The conjugate-linear slot isomorphism `V c ≃ₛₗ[starRingEnd k] V (bar c)`: conjugate the
> coordinates in the species basis and relabel to the conjugate colour via `barIdx_eq`.

```lean
def conjEquiv {c : C} : V c ≃ₛₗ[starRingEnd k] V (S.bar c)
```

**`ConjTensorSpecies.conjEquiv_basis`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L177).

> `conjEquiv` on a basis vector: `b c i ↦ b (bar c) i` (relabelled through `barIdx_eq`), since the
> basis coordinates of `b c i` are the indicator at `i` and `star` fixes `0` and `1`.

```lean
lemma conjEquiv_basis {c : C} (i : basisIdx c) :
    S.conjEquiv (b c i) = b (S.bar c) (Equiv.cast (S.barIdx_eq c).symm i)
```

**`ConjTensorSpecies.conjEquiv_basis_repr`**, a lemma, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L181).

```lean
lemma conjEquiv_basis_repr {c : C} (v : V c) (φ : basisIdx (S.bar c)) :
    (b (S.bar c)).repr (S.conjEquiv v) φ
      = star ((b c).repr v (Equiv.cast (S.barIdx_eq c) φ))
```

**`ConjTensorSpecies.conjEquiv_equivariant`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L189).

```lean
lemma conjEquiv_equivariant {c : C} (g : G) (v : V c) :
    S.conjEquiv (rep c g v) = rep (S.bar c) g (S.conjEquiv v)
```

## C. Conjugation of tensors

> We define the conjugation map `conjT` through its action on components, record that it conjugates
> components in place (`componentMap_conjT`), and show it is `conj`-semilinear and additive.
>
> Conventions for the index notation in this file. Indices are written in slot order: in `M_{IJ̄}`,
> `I` is the first slot (Lean slot `0`, colour `c 0`) and `J̄` the second (slot `1`, colour
> `c 1 = bar (c 0)`). As a tensor, `g = g_{IJ̄} dφᴵ ⊗ dφ̄^J̄` takes a holomorphic vector in its first
> slot and an antiholomorphic one in its second: `g(u, v̄) = g_{IJ̄} uᴵ v̄^J̄`. An index of a
> conjugate colour carries a bar or a dot (`Ī`, `α̇`), and conjugation adds a bar to each index,
> removing it from an index that already has one.
>
> For chiral scalar fields `φᴵ`, the basis vectors are the derivatives `e_I = ∂/∂φᴵ`, and their
> conjugates `ē_Ī = ∂/∂φ̄^Ī`. A Kähler metric is `g_{IJ̄} = ∂_I ∂_J̄ K = g(e_I, ē_J̄)`. Holomorphic
> index first is the standard convention, used throughout; it is a choice, since
> `∂_I ∂_J̄ K = ∂_J̄ ∂_I K` (Schwarz's theorem).

**`ConjTensorSpecies.componentReindex`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L224).

> Reindex component labels of `bar ∘ c` back to `c`, slotwise via the cast `barIdx_eq`.

```lean
def componentReindex {n : ℕ} (c : Fin n → C) :
    ComponentIdx (S := S.toTensorSpecies) (fun i => S.bar (c i)) ≃
      ComponentIdx (S := S.toTensorSpecies) c
```

**`ConjTensorSpecies.conjT`**, a def, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L231).

> Conjugation of a tensor: conjugate the components and reindex the basis to the conjugate
> colours.

```lean
def conjT {n : ℕ} {c : Fin n → C} : S.Tensor c →ₛₗ[starRingEnd k]
    S.Tensor (fun i => S.bar (c i))
```

**`ConjTensorSpecies.conjT_apply`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L245).

```lean
lemma conjT_apply {n : ℕ} {c : Fin n → C} (t : S.Tensor c) :
    S.conjT t = ofComponents (fun i => S.bar (c i))
      (fun b => star (componentMap c t (S.componentReindex c b)))
```

**`ConjTensorSpecies.componentMap_conjT`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L251).

> Components of a conjugated tensor: the `star` of the original components, reindexed.

```lean
lemma componentMap_conjT {n : ℕ} {c : Fin n → C} (t : S.Tensor c)
    (b : ComponentIdx (S := S.toTensorSpecies) (fun i => S.bar (c i))) :
    componentMap (fun i => S.bar (c i)) (S.conjT t) b
      = star (componentMap c t (S.componentReindex c b))
```

**`ConjTensorSpecies.toMatrix_conjT`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L260).

> Conjugating a rank-two tensor conjugates each component and bars both indices:
> `(T̄)_{ĪJ̄} = (T_{IJ})*`, where barring a barred index removes the bar. For example, `ψ_α χ_β` goes
> to `ψ̄_α̇ χ̄_β̇`, and a tensor `M_{IJ̄}` goes to `(M̄)_{ĪJ} = (M_{IJ̄})*`.

```lean
lemma toMatrix_conjT {cs : Fin 2 → C} (t : S.Tensor cs) :
    toMatrix (S.conjT t) = ((toMatrix t).map star).submatrix
      (Equiv.cast (S.barIdx_eq (cs 0))) (Equiv.cast (S.barIdx_eq (cs 1)))
```

**`ConjTensorSpecies.conjT_basis`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L269).

```lean
lemma conjT_basis {n : ℕ} {c : Fin n → C} (i : ComponentIdx (S := S.toTensorSpecies) c) :
    S.conjT (basis c i) = basis (fun i => S.bar (c i)) ((S.componentReindex c).symm i)
```

**`ConjTensorSpecies.conjSingleT`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L285).

> Conjugation of a vector, `vᴵ ↦ v̄^Ī = (vᴵ)*`, landing at the conjugate colour. For example, a
> left-handed Weyl spinor `ψ_α` goes to the right-handed `ψ̄_α̇`.

```lean
def conjSingleT (x : C) : S.Tensor ![x] →ₛₗ[starRingEnd k] S.Tensor ![S.bar x]
```

**`ConjTensorSpecies.conjSingleT_basis`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L291).

> Conjugation sends the basis vector `e_I` to `ē_Ī`, the basis vector of the conjugate colour with
> the same label.

```lean
lemma conjSingleT_basis (x : C) (z : basisIdx x) :
    S.conjSingleT x (basis ![x] (ComponentIdx.single.symm z)) =
      basis ![S.bar x] (ComponentIdx.single.symm (cast (S.barIdx_eq x).symm z))
```

**`ConjTensorSpecies.conjT_pure`**, a lemma, [line 299](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L299).

```lean
lemma conjT_pure {n : ℕ} {c : Fin n → C} (p : Tensor.Pure S.toTensorSpecies c) :
    S.conjT p.toTensor = Pure.toTensor (fun i => S.conjEquiv (p i))
```

**`ConjTensorSpecies.conjT_eq_permT_iff`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L317).

> Componentwise criterion for `conjT t = permT σ h t'`. The conjugate of `t` equals the
> recolouring `permT σ h t'` exactly when, at every component, the `star`-conjugated reindexed
> component of `t` matches the corresponding component of `permT σ h t'`. This packages the
> `componentMap_conjT` expansion and the `repr`/`componentMap` bridge that the reality and Hermiticity
> proofs downstream would otherwise repeat by hand; the caller is left only with the species-specific
> permutation bookkeeping on the right-hand side.

```lean
lemma conjT_eq_permT_iff {n m : ℕ} {c : Fin n → C} {c' : Fin m → C}
    {σ : Fin n → Fin m} (h : IsReindexing c' (fun i => S.bar (c i)) σ)
    (t : S.Tensor c) (t' : S.Tensor c') :
    S.conjT t = permT σ h t' ↔
      ∀ φ : ComponentIdx (S := S.toTensorSpecies) (fun i => S.bar (c i)),
        star (componentMap c t (S.componentReindex c φ))
          = (Tensor.basis (fun i => S.bar (c i))).repr (permT σ h t') φ
```

**`ConjTensorSpecies.conjT_equivariant`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L333).

```lean
lemma conjT_equivariant {n : ℕ} {c : Fin n → C} (g : G) (t : S.Tensor c) :
    S.conjT (g • t) = g • S.conjT t
```

## D. The involution law

> We prove `conjT_conjT`: conjugating a tensor twice returns it, up to the identity recolouring
> `bar ∘ bar ∘ c = c`. The supporting lemmas reconcile the iterated basis-label casts.

**`ConjTensorSpecies.isReindexing_bar_bar`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L360).

> The identity permutation satisfies `IsReindexing` from `c` to `bar ∘ bar ∘ c`, as `bar` is an
> involution.

```lean
lemma isReindexing_bar_bar {n : ℕ} (c : Fin n → C) :
    IsReindexing c (fun i => S.bar (S.bar (c i))) (id : Fin n → Fin n)
```

**`ConjTensorSpecies.conjT_conjT`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L366).

> Conjugation is an involution: conjugating twice returns the original tensor, up to the
> `bar_involution` recolouring (the identity permutation `permT`).

```lean
lemma conjT_conjT {n : ℕ} {c : Fin n → C} (t : S.Tensor c) :
    S.conjT (S.conjT t)
      = permT id (S.isReindexing_bar_bar c) t
```

## E. Commutation with contraction

> We prove `conjT_contrT`: conjugation commutes with contracting two dual-coloured slots. The
> contraction expands as a sum over the contracted index pair, and `conj_contrComm` matches the
> conjugated coefficients to those on the `bar`-images.

**`ConjTensorSpecies.contrCond_bar`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L393).

> Slots with dual colour in `c` have dual colour in `bar ∘ c`, as `bar` commutes with `τ`.

```lean
lemma contrCond_bar {n : ℕ} {c : Fin (n + 1 + 1) → C} {i j : Fin (n + 1 + 1)}
    (h : i ≠ j ∧ S.τ (c i) = c j) :
    i ≠ j ∧ S.τ ((S.bar ∘ c) i) = (S.bar ∘ c) j
```

**`ConjTensorSpecies.conjT_contrT`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L400).

> Conjugation commutes with contraction: conjugating a contracted tensor equals contracting the
> conjugate on the `bar`-images of the same two slots.

```lean
lemma conjT_contrT {n : ℕ} {c : Fin (n + 1 + 1) → C} (i j : Fin (n + 1 + 1))
    (h : i ≠ j ∧ S.τ (c i) = c j) (t : S.Tensor c) :
    S.conjT (contrT n i j h t)
      = contrT n i j (S.contrCond_bar h) (S.conjT t)
```

## F. Hermitian pairings

> A metric slot pairs a colour `c` with its conjugate `bar c`. `IsHermitian` is the structural form of
> `g_{IJ̄} = conj g_{JĪ}`: conjugating and swapping the two slots through `conjEquiv` returns `g`'s
> `star`. Because `V c` and `V (bar c)` are genuinely different modules this is the honest
> conjugate-transpose, not a bare `g = g.flip`. The condition is fixed here as `IsHermitian`; a
> downstream metric layer instantiates it for a concrete pairing.
>
> A tensor `M_{IJ̄}` with one index and one conjugate index, such as a Kähler metric `g_{IJ̄}`, has
> the matrix of components `(M_{IJ̄})` (`toSquareMatrix`), regarded as a square matrix over the labels
> of `I`. Its entries are the components themselves. Lean needs this step because the labels of a
> colour and of its conjugate are different types, identified by `barIdx_eq`, and Hermiticity,
> positive-definiteness and the inverse are defined only for square matrices. `M` is Hermitian,
> `(M_{IJ̄})* = M_{JĪ}`, exactly when this matrix is.

**`ConjTensorSpecies.IsHermitian`**, a def, [line 461](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L461).

> A pairing `g : V c ⊗ V (bar c) → k` is Hermitian when conjugating and swapping its two slots
> via `conjEquiv` returns its `star`: `g (x ⊗ y) = star (g (conjEquiv.symm y ⊗ conjEquiv x))`.

```lean
def IsHermitian {c : C} (g : V c ⊗[k] V (S.bar c) →ₗ[k] k) : Prop
```

**`ConjTensorSpecies.toSquareMatrix`**, a def, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L471).

> The matrix `(M_{IJ̄})`, with entries unchanged, regarded as a square matrix over the labels of
> `I`. Lean needs this step because the labels of a colour and of its conjugate are different types,
> identified by `barIdx_eq`; only for a square matrix are Hermiticity, positive-definiteness and the
> inverse defined. Convention: the unbarred index is the row and the barred index the column, entry
> `(I, J)` being `M_{IJ̄}`, as physicists write the matrix. For a Kähler metric `g_{IJ̄}` it is the
> usual matrix `(g_{IJ̄})`.

```lean
def toSquareMatrix {c : Fin 2 → C} (M : S.Tensor c) (hbar : S.bar (c 0) = c 1 := by rfl) :
    Matrix (basisIdx (c 0)) (basisIdx (c 0)) k
```

**`ConjTensorSpecies.toSquareMatrix_apply`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L475).

```lean
lemma toSquareMatrix_apply {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1) (M : S.Tensor c)
    (i j : basisIdx (c 0)) :
    S.toSquareMatrix M hbar i j =
      toMatrix M i ((Equiv.cast (hbar ▸ S.barIdx_eq (c 0))).symm j)
```

**`ConjTensorSpecies.toMatrix_eq_submatrix_toSquareMatrix`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L482).

> `toMatrix M` is `toSquareMatrix M` with its columns labelled by `J̄` instead of `J`.

```lean
lemma toMatrix_eq_submatrix_toSquareMatrix {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1)
    (M : S.Tensor c) :
    toMatrix M =
      (S.toSquareMatrix M hbar).submatrix id (Equiv.cast (hbar ▸ S.barIdx_eq (c 0)))
```

**`ConjTensorSpecies.conjT_eq_permT_swap_iff_toSquareMatrix_isHermitian`**, a lemma, [line 492](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L492).

> For `M_{IJ̄}`, the conjugate `(M̄)_{ĪJ} = (M_{IJ̄})*` and the swapped tensor `M_{JĪ}` have the
> same index types, a barred index then an ordinary one. They are equal, `(M_{IJ̄})* = M_{JĪ}`,
> exactly when the matrix `(M_{IJ̄})` is Hermitian. A Kähler metric satisfies this.

```lean
lemma conjT_eq_permT_swap_iff_toSquareMatrix_isHermitian {c : Fin 2 → C}
    (hbar : S.bar (c 0) = c 1) (M : S.Tensor c) :
    S.conjT M = permT ![1, 0] (IsReindexing.swap_of_eq hbar.symm
      ((congrArg S.bar hbar).symm.trans (S.bar_involution (c 0))).symm) M ↔
    (S.toSquareMatrix M hbar).IsHermitian
```

**`ConjTensorSpecies.toMatrix_contractInnerT_eq_toSquareMatrix_mul`**, a lemma, [line 520](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L520).

> The matrix of `g_{IJ̄} t^{J̄K}` is the product of the square matrix `(g_{IJ̄})` and the matrix
> `(t^{J̄K})`, with the rows of `(t^{J̄K})` labelled by `J`.

```lean
lemma toMatrix_contractInnerT_eq_toSquareMatrix_mul [HasContrDualBases S.toTensorSpecies]
    {cs ds : Fin 2 → C} (hbar : S.bar (cs 0) = cs 1) (h : S.τ (cs 1) = ds 0) (M : S.Tensor cs)
    (t : S.Tensor ds) :
    toMatrix (contractInnerT h M t) =
      S.toSquareMatrix M hbar * (toMatrix t).submatrix
        (dualIdxEquiv h ∘ (Equiv.cast (hbar ▸ S.barIdx_eq (cs 0))).symm)
        (id : basisIdx (ds 1) → _)
```

## G. Dual bases under conjugation

> A lower index contracts with an upper one, and the bases are dual: `e_α` contracted with `e^β` gives
> `δ_α^β`. This section shows that the conjugate bases are dual in the same way: `ē_α̇` contracted
> with `ē^β̇` gives `δ_α̇^β̇`. For example, for a vector `vᴵ` and a covector `w_I`,
> `(vᴵ w_I)* = v̄^Ī w̄_Ī`: the conjugate contraction pairs the same labels. This follows because
> contraction commutes with conjugation (`conj_contrComm`).

**`ConjTensorSpecies.isContrDualMatching_bar`**, a lemma, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L547).

> The conjugate bases are dual: if `e_α` contracted with `e^β` is `δ_α^β`, then `ē_α̇` contracted
> with `ē^β̇` is `δ_α̇^β̇`.

```lean
lemma isContrDualMatching_bar [HasContrDualBases S.toTensorSpecies] (d : C) :
    IsContrDualMatching S.toTensorSpecies (S.bar d)
      ((basisIdxCongr (S.bar_tau d)).symm.trans ((Equiv.cast (S.barIdx_eq (S.τ d))).trans
        ((contrDualIdxEquiv S.toTensorSpecies d).trans (Equiv.cast (S.barIdx_eq d)).symm)))
```

**`ConjTensorSpecies.dualIdxEquiv_bar`**, a lemma, [line 564](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L564).

> `dualIdxEquiv` sends a lower label `α` to the upper label `α` it contracts with to `1`.
> Conjugation commutes with this: the dotted label `α̇` pairs with the dotted upper label `α̇`.

```lean
lemma dualIdxEquiv_bar [Nontrivial k] [HasContrDualBases S.toTensorSpecies] {c1 c2 c3 : C}
    (h : S.τ c1 = c2) (h' : S.τ (S.bar c1) = c3) (hbar : S.bar c2 = c3) (x : basisIdx c1) :
    dualIdxEquiv h' (cast (S.barIdx_eq c1).symm x) =
      cast (hbar ▸ S.barIdx_eq c2).symm (dualIdxEquiv h x)
```

**`ConjTensorSpecies.dualIdxEquiv_bar_tau`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L585).

> Removing a bar and lowering an index commute on labels. From a label of the upper barred index
> `J̄`, removing the bar and then lowering gives the same label of the lower index `J` as lowering and
> then removing the bar.
> ```
> upper J̄ (τ d)  → remove bar →  upper J (τ a)
>       ↓ lower                        ↓ lower
> lower J̄ (d)    → remove bar →  lower J (a)
> ```
> The left-hand side of the statement goes across the top and down, the right-hand side down and
> across the bottom.

```lean
lemma dualIdxEquiv_bar_tau [Nontrivial k] [HasContrDualBases S.toTensorSpecies] {a d : C}
    (hbar : S.bar a = d) (j : basisIdx (S.τ d)) :
    dualIdxEquiv (S.τ_τ_apply a)
        ((Equiv.cast (S.bar_tau_of_bar hbar ▸ S.barIdx_eq (S.τ d))).symm j) =
      Equiv.cast (hbar ▸ S.barIdx_eq a) ((dualIdxEquiv (rfl : S.τ d = S.τ d)).symm j)
```

## H. The sesquilinear form of a tensor

> A tensor `g_{IJ̄}` with one index and one conjugate index, such as a Kähler metric, defines a
> Hermitian form on vectors of one colour. By the slot conventions of §C, `g` takes a holomorphic
> vector `u` in its first slot and an antiholomorphic vector in its second,
> `g(u, v̄) = g_{IJ̄} uᴵ v̄^J̄`. To pair two vectors `s, t` of the same colour, one of them is
> conjugated so that it fits the second slot.
>
> Convention. We use Mathlib's sesquilinear forms, so that Mathlib's results on Hermitian and
> positive-definite forms apply. A Mathlib form `⟨s, t⟩` is conjugate-linear in its left argument `s`.
> So `s` is the vector that is conjugated: `s̄` goes into the second, barred slot of `g`, and `t` goes
> unchanged into the first slot,
>
> `⟨s, t⟩ = g(t, s̄) = g_{IJ̄} tᴵ s̄^J̄`.
>
> The order of the arguments of `⟨s, t⟩` is thus opposite to the order of the slots of `g`. Physics
> usually writes the form the other way round, `g_{IJ̄} uᴵ v̄^J̄`, conjugate-linear in its right
> argument `v`. This does not change norms or Hermiticity: `⟨t, t⟩ = g_{IJ̄} tᴵ t̄^J̄` is the norm
> squared of the kinetic term `g_{IJ̄} ∂φᴵ ∂φ̄^J̄`. It does change the matrix: on the basis
> `e_I = ∂/∂φᴵ`, `⟨e_I, e_J⟩ = g(e_J, ē_I) = g_{JĪ}`, the transpose of `(g_{IJ̄})`.
>
> `g` is Hermitian, `(g_{IJ̄})* = g_{JĪ}`, exactly when its form is (`LinearMap.IsSymm`,
> `⟨s, t⟩* = ⟨t, s⟩`), and positive-definite, `⟨t, t⟩ > 0` for `t ≠ 0`, exactly when its form is
> (`LinearMap.IsPosDef`). On a concrete species the colour conditions hold by `rfl`, so the form of
> `g` on vectors of colour `x` is written `S.toSesqForm x g`.

**`ConjTensorSpecies.toSesqForm`**, a def, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L640).

> The Hermitian form `⟨s, t⟩ = M(t, s̄) = M_{IJ̄} tᴵ s̄^J̄` of a tensor `M_{IJ̄}`, on vectors
> `s, t`. Convention: as in Mathlib it is conjugate-linear in its left argument `s`; `s̄` fills the
> second, barred slot of `M` and `t` the first, so the argument order is opposite to the slot order.

```lean
def toSesqForm (x : C) {c : Fin 2 → C} (M : S.Tensor c) (hbar : S.bar (c 0) = c 1 := by rfl)
    (hx : S.τ x = c 0 := by rfl) : S.Tensor ![x] →ₗ⋆[k] S.Tensor ![x] →ₗ[k] k
```

**`ConjTensorSpecies.toMatrix₂_toSesqForm`**, a lemma, [line 647](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L647).

> Since the left argument of the form fills the second slot of `M` (`toSesqForm`),
> `⟨e_I, e_J⟩ = M(e_J, ē_I) = M_{JĪ}`: the matrix of the form is the transpose of `(M_{IJ̄})`. For a
> Kähler metric, `⟨∂_I, ∂_J⟩ = ∂_J ∂_Ī K = g_{JĪ}`.

```lean
lemma toMatrix₂_toSesqForm [HasContrDualBases S.toTensorSpecies] {x : C} {c : Fin 2 → C}
    (hbar : S.bar (c 0) = c 1) (hx : S.τ x = c 0) (M : S.Tensor c) :
    LinearMap.toMatrix₂ ((basis ![x]).reindex (ComponentIdx.single.trans (dualIdxEquiv hx)))
        ((basis ![x]).reindex (ComponentIdx.single.trans (dualIdxEquiv hx)))
        (S.toSesqForm x M hbar hx) = (S.toSquareMatrix M hbar)ᵀ
```

**`ConjTensorSpecies.isSymm_toSesqForm_iff_toSquareMatrix_isHermitian`**, a lemma, [line 666](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L666).

> `⟨s, t⟩* = ⟨t, s⟩` for all `s, t` exactly when `(M_{IJ̄})* = M_{JĪ}`.

```lean
lemma isSymm_toSesqForm_iff_toSquareMatrix_isHermitian [HasContrDualBases S.toTensorSpecies]
    {x : C} {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1) (hx : S.τ x = c 0) (M : S.Tensor c) :
    (S.toSesqForm x M hbar hx).IsSymm ↔ (S.toSquareMatrix M hbar).IsHermitian
```

**`ConjTensorSpecies.isSymm_toSesqForm_iff_conjT_eq_permT`**, a lemma, [line 675](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L675).

> `⟨s, t⟩* = ⟨t, s⟩` for all `s, t` exactly when the conjugate of `M` equals `M` with its two
> indices swapped, `(M_{IJ̄})* = M_{JĪ}`.

```lean
lemma isSymm_toSesqForm_iff_conjT_eq_permT [HasContrDualBases S.toTensorSpecies]
    {x : C} {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1) (hx : S.τ x = c 0) (M : S.Tensor c) :
    (S.toSesqForm x M hbar hx).IsSymm ↔ S.conjT M = permT ![1, 0] (IsReindexing.swap_of_eq hbar.symm
      ((congrArg S.bar hbar).symm.trans (S.bar_involution (c 0))).symm) M
```

## I. Positive-definite tensors

**`ConjTensorSpecies.isPosDef_toSesqForm_iff_toSquareMatrix_posDef`**, a lemma, [line 695](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L695).

> The form is positive-definite, Hermitian with `M_{IJ̄} tᴵ t̄^J̄ > 0` for every `t ≠ 0`, exactly
> when the matrix `(M_{IJ̄})` is. A Kähler metric is positive-definite, which makes kinetic terms
> positive.

```lean
lemma isPosDef_toSesqForm_iff_toSquareMatrix_posDef [HasContrDualBases S.toTensorSpecies]
    {x : C} {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1) (hx : S.τ x = c 0) (M : S.Tensor c) :
    (S.toSesqForm x M hbar hx).IsPosDef ↔ (S.toSquareMatrix M hbar).PosDef
```

**`ConjTensorSpecies.isUnit_det_toSquareMatrix_of_isPosDef`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean#L713).

> Over a field, the matrix `(M_{IJ̄})` of a positive-definite tensor is invertible.

```lean
lemma isUnit_det_toSquareMatrix_of_isPosDef [HasContrDualBases S.toTensorSpecies] {x : C}
    {c : Fin 2 → C} (hbar : S.bar (c 0) = c 1) (hx : S.τ x = c 0) {M : S.Tensor c}
    (hM : (S.toSesqForm x M hbar hx).IsPosDef) :
    IsUnit (S.toSquareMatrix M hbar).det
```

## Depends on

- [Positive-definite sesquilinear forms](../../../mathematics/formathlib/sesquilinearform.md)
- [The conjugate module](../../../mathematics/modules/conjmodule.md)
- [The bilinear map and the product of rank-two tensors](contraction-ranktwo.md)

## Sources

- [Physlib/Relativity/Tensors/Conjugation/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Tensors/Conjugation/Basic.lean)
