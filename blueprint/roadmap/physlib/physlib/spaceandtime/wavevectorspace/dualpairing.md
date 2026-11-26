---
declaration: module
origin: cited
lean: Space.dual, Space.dual_apply, Space.opNorm_dual_eq_norm, WaveVectorSpace.dual, WaveVectorSpace.dual_apply, WaveVectorSpace.opNorm_dual_eq_norm, WaveVectorSpace.pairingCLM, WaveVectorSpace.pairingCLM_apply_eq_dual
statement: formalized
proof: formalized
---

# Duality of `Space` and `WaveVectorSpace`

The module `Physlib.SpaceAndTime.WaveVectorSpace.DualPairing`, [Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean): 16 declarations, 5 with a docstring.

## i. Overview

> Upon selecting an origin for the affine space `Space d`,
> the spaces `Space d` and `WaveVectorSpace d` are dual as real vector spaces.
> There is natural continuous bilinear map `WaveVectorSpace d × Space d → ℝ` which sends
> the pair `(k, x)` to `∑ᵢ kⁱxᵢ`. For fixed `k` this gives rise to a functional `Space d →L[ℝ] ℝ`
> mapping `x ↦ k ⬝ᵥ x`, and similarly for fixed `x`.

## ii. Key results

> - `Space.dual x` : the functional on `WaveVectorSpace` corresponding to `x : Space d`,
>   bundled as a continuous linear map.
> - `WaveVectorSpace.dual k` : the functional on `Space` corresponding to `k : WaveVectorSpace d`,
>   bundled as a continuous linear map.
> - `WaveVectorSpace.pairingCLM` : the dual pairing between `WaveVectorSpace` and `Space`,
>   bundled as a continuous bilinear map.

## iv. References

## A. Strong duals

**`Space.dual`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L54).

> The functional on `WaveVectorSpace d` dual to `x`, defined by `k ↦ k ⬝ᵥ x`.

```lean
def dual (x : Space d) : StrongDual ℝ (WaveVectorSpace d)
```

**`Space.dual_apply`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L59).

```lean
lemma dual_apply (x : Space d) (k : WaveVectorSpace d) : x.dual k = k ⬝ᵥ x
```

**`Space.opNorm_dual_eq_norm`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L62).

```lean
lemma opNorm_dual_eq_norm (x : Space d) : ‖x.dual‖ = ‖x‖
```

**`WaveVectorSpace.dual`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L77).

> The functional on `Space d` dual to `k`, defined by `x ↦ k ⬝ᵥ x`.

```lean
def dual (k : WaveVectorSpace d) : StrongDual ℝ (Space d)
```

**`WaveVectorSpace.dual_apply`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L82).

```lean
lemma dual_apply (k : WaveVectorSpace d) (x : Space d) : k.dual x = k ⬝ᵥ x
```

**`WaveVectorSpace.opNorm_dual_eq_norm`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L85).

```lean
lemma opNorm_dual_eq_norm (k : WaveVectorSpace d) : ‖k.dual‖ = ‖k‖
```

## B. Bilinear pairing

**`WaveVectorSpace.pairingCLM`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L100).

> The bilinear form `WaveVectorSpace d × Space d → ℝ` given by `k ↦ x ↦ k ⬝ᵥ x`.

```lean
def pairingCLM : WaveVectorSpace d →L[ℝ] Space d →L[ℝ] ℝ
```

**`WaveVectorSpace.pairingCLM_apply_eq_dual`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L109).

```lean
lemma pairingCLM_apply_eq_dual (k : WaveVectorSpace d) : pairingCLM k = k.dual
```

**`WaveVectorSpace.pairingCLM_flip_apply_eq_dual`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L111).

```lean
lemma pairingCLM_flip_apply_eq_dual (x : Space d) : pairingCLM.flip x = x.dual
```

**`WaveVectorSpace.pairingCLM_apply_apply`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L114).

```lean
lemma pairingCLM_apply_apply (k : WaveVectorSpace d) (x : Space d) : pairingCLM k x = k ⬝ᵥ x
```

**`WaveVectorSpace.continuous_dual`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L117).

```lean
lemma continuous_dual : Continuous (dual : WaveVectorSpace d → StrongDual ℝ (Space d))
```

**`Space.continuous_dual`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L121).

```lean
lemma _root_.Space.continuous_dual :
    Continuous (Space.dual : Space d → StrongDual ℝ (WaveVectorSpace d))
```

## C. Derivatives

**`WaveVectorSpace.deriv_pairingCLM`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L130).

```lean
lemma deriv_pairingCLM (i : Fin d) (k : WaveVectorSpace d) (x : Space d) :
    ∂[i] (pairingCLM k) x = k i
```

**`WaveVectorSpace.deriv_pairingCLM_flip`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L135).

```lean
lemma deriv_pairingCLM_flip (i : Fin d) (x : Space d) (k : WaveVectorSpace d) :
    ∂[i] (pairingCLM.flip x) k = x i
```

**`WaveVectorSpace.deriv_dual`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L142).

> The derivative of the functional `x ↦ k ⬝ᵥ x` with respect to `xⁱ` is `kᵢ`.

```lean
lemma deriv_dual (i : Fin d) (k : WaveVectorSpace d) (x : Space d) : ∂[i] k.dual x = k i
```

**`Space.deriv_dual`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L147).

> The derivative of the functional `k ↦ k ⬝ᵥ x` with respect to `kᵢ` is `xⁱ`.

```lean
lemma _root_.Space.deriv_dual (i : Fin d) (x : Space d) (k : WaveVectorSpace d) :
    ∂[i] x.dual k = x i
```

## Depends on

- [Derivatives on Space](../space/part-01/derivatives-basic.md)
- [Derivatives on `WaveVectorSpace`](derivatives-basic.md)

## Sources

- [Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean)
