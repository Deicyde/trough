---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.boundKappa_pos, PhyslibAlpha.Hydrogen.continuous_boundState, PhyslibAlpha.Hydrogen.memHS_boundState, PhyslibAlpha.Hydrogen.boundStateHS, PhyslibAlpha.Hydrogen.boundStateMap_apply, PhyslibAlpha.Hydrogen.continuous_boundStateMap, PhyslibAlpha.Hydrogen.memHS_boundStateMap, PhyslibAlpha.Hydrogen.boundStateMapHS
statement: formalized
proof: formalized
---

# The hydrogen bound states in `L²`

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.BoundStatesL2`, [PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean): 13 declarations, 11 with a docstring.

## i. Overview

> The bound states `boundState H N l P` of `Eigenfunctions.lean` are square integrable: they are a
> polynomial in the coordinates and in `‖y‖` times `e^(-κ‖y‖)`, and such functions decay faster than
> any power of `1 + ‖y‖`. They therefore define vectors of the Hilbert space `SpaceDHilbertSpace d`.
> Since they are continuous, the linear independence of the bound states of one level
> (`boundStateMap_injective`) carries over to the Hilbert space; since they are real valued, it
> holds over `ℂ` as well.

## ii. Key results

> - `memHS_boundState`, `boundStateHS` : the bound states as vectors of `SpaceDHilbertSpace d`.
> - `boundStateMapHS_injective` : the bound states of one level are linearly independent in
>   `SpaceDHilbertSpace d`.
> - `finrank_range_boundStateMapHS_three` : in three dimensions they span a real subspace of
>   dimension `(n + 1)²`.
> - `linearIndependent_complex_of_real_inner` : vectors with real Gram matrix which are linearly
>   independent over `ℝ` are linearly independent over `ℂ`.
> - `finrank_span_range_boundStateMapHS_three` : in three dimensions the bound states of the level
>   `n` span a complex subspace of dimension `(n + 1)²`.

## iv. References

> - None.

## A. The bound states in the Hilbert space

**`PhyslibAlpha.Hydrogen.boundKappa_pos`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L62).

> The decay constant `κ = 1/(a L_n)` of a bound state is positive for `k > 0` and `d ≥ 2`.

```lean
lemma boundKappa_pos (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (n : ℕ) :
    0 < boundKappa H n
```

**`PhyslibAlpha.Hydrogen.continuous_boundState`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L66).

```lean
lemma continuous_boundState (H : HydrogenAtom d) (N l : ℕ) (P : MvPolynomial (Fin d) ℝ) :
    Continuous (boundState H N l (toFun P))
```

**`PhyslibAlpha.Hydrogen.memHS_boundState`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L73).

> The bound states are square integrable.

```lean
lemma memHS_boundState (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (N l : ℕ)
    (P : MvPolynomial (Fin d) ℝ) :
    SpaceDHilbertSpace.MemHS (fun y => (boundState H N l (toFun P) y : ℂ))
```

**`PhyslibAlpha.Hydrogen.boundStateHS`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L89).

> The bound state `boundState H N l P` as a vector of `SpaceDHilbertSpace d`.

```lean
def boundStateHS (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (N l : ℕ)
    (P : MvPolynomial (Fin d) ℝ) : SpaceDHilbertSpace d
```

## B. Linear independence in the Hilbert space

> All bound states of the level `n` share the decay constant `κ = boundKappa H n`, so their sums
> are again `e^(-κ‖y‖)` times a polynomially bounded function.

**`PhyslibAlpha.Hydrogen.boundStateMap_apply`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L103).

> `Σ_l boundState H (n - l) l P_l = e^(-κ‖y‖) Σ_l L_l(‖y‖) P_l(y)` with `κ = boundKappa H n`.

```lean
lemma boundStateMap_apply (H : HydrogenAtom d) (n : ℕ)
    (Ps : (l : Fin (n + 1)) → harmonicSubmodule d l) (y : Space d) :
    boundStateMap H n Ps y = Real.exp (-(boundKappa H n * ‖y‖)) *
      ∑ l : Fin (n + 1), (laguerreScaled (boundKappa H n) (n - l) (2 * l + d - 2)).eval ‖y‖ *
        toFun (Ps l : MvPolynomial (Fin d) ℝ) y
```

**`PhyslibAlpha.Hydrogen.continuous_boundStateMap`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L113).

```lean
lemma continuous_boundStateMap (H : HydrogenAtom d) (n : ℕ)
    (Ps : (l : Fin (n + 1)) → harmonicSubmodule d l) : Continuous (boundStateMap H n Ps)
```

**`PhyslibAlpha.Hydrogen.memHS_boundStateMap`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L123).

> The sums of bound states of one level are square integrable.

```lean
lemma memHS_boundStateMap (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (n : ℕ)
    (Ps : (l : Fin (n + 1)) → harmonicSubmodule d l) :
    SpaceDHilbertSpace.MemHS (fun y => (boundStateMap H n Ps y : ℂ))
```

**`PhyslibAlpha.Hydrogen.boundStateMapHS`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L138).

> The bound states of the level `n` as an `ℝ`-linear map into `SpaceDHilbertSpace d`.

```lean
def boundStateMapHS (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (n : ℕ) :
    ((l : Fin (n + 1)) → harmonicSubmodule d l) →ₗ[ℝ] SpaceDHilbertSpace d
```

**`PhyslibAlpha.Hydrogen.boundStateMapHS_injective`**, a lemma, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L158).

> The bound states of one level are linearly independent in `SpaceDHilbertSpace d`.

```lean
lemma boundStateMapHS_injective (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (n : ℕ) :
    Function.Injective (boundStateMapHS H hd hk n)
```

**`PhyslibAlpha.Hydrogen.finrank_range_boundStateMapHS_three`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L175).

> In three dimensions the bound states of the level `n` span a `(n + 1)²`-dimensional subspace
> of `SpaceDHilbertSpace 3`.

```lean
lemma finrank_range_boundStateMapHS_three (H : HydrogenAtom 3) (hk : 0 < H.k)
    (n : ℕ) :
    Module.finrank ℝ (LinearMap.range (boundStateMapHS H (by omega) hk n)) = (n + 1) ^ 2
```

**`PhyslibAlpha.Hydrogen.linearIndependent_complex_of_real_inner`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L185).

> Vectors with real Gram matrix that are linearly independent over `ℝ` are linearly independent
> over `ℂ`.

```lean
lemma linearIndependent_complex_of_real_inner {E : Type*} [NormedAddCommGroup E]
    [InnerProductSpace ℂ E] {ι : Type*} [Fintype ι] {v : ι → E}
    (him : ∀ k j, (⟪v k, v j⟫_ℂ).im = 0) (hv : LinearIndependent ℝ v) :
    LinearIndependent ℂ v
```

**`PhyslibAlpha.Hydrogen.im_inner_boundStateMapHS`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L221).

> The bound states are real valued, so their inner products are real.

```lean
lemma im_inner_boundStateMapHS (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (n : ℕ)
    (Ps Qs : (l : Fin (n + 1)) → harmonicSubmodule d l) :
    (⟪boundStateMapHS H hd hk n Ps, boundStateMapHS H hd hk n Qs⟫_ℂ).im = 0
```

**`PhyslibAlpha.Hydrogen.finrank_span_range_boundStateMapHS_three`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean#L231).

> In three dimensions the bound states of the level `n` span a complex subspace of dimension
> `(n + 1)²` of `SpaceDHilbertSpace 3`.

```lean
lemma finrank_span_range_boundStateMapHS_three (H : HydrogenAtom 3) (hk : 0 < H.k)
    (n : ℕ) :
    Module.finrank ℂ (Submodule.span ℂ (Set.range (boundStateMapHS H (by omega) hk n))) =
      (n + 1) ^ 2
```

## Depends on

- [The degeneracy of the hydrogen bound states](degeneracy.md)

## Proof depends on

- [Polynomially bounded functions and integrability on `Space d`](polybounded.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesL2.lean)
