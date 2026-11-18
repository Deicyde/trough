---
declaration: module
origin: cited
lean: Space.dual, Space.dual_apply, WaveVectorSpace.dual, WaveVectorSpace.dual_apply, WaveVectorSpace.pairingCLM, WaveVectorSpace.pairingCLM_apply_eq_dual, WaveVectorSpace.pairingCLM_flip_apply_eq_dual
statement: formalized
proof: formalized
---

# Duality of `Space` and `WaveVectorSpace`

The module `Physlib.SpaceAndTime.WaveVectorSpace.DualPairing`, [Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean): 7 declarations, 3 with a docstring.

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

**`Space.dual`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L54).

> The functional on `WaveVectorSpace d` dual to `x`, defined by `k ↦ k ⬝ᵥ x`.

```lean
def dual (x : Space d) : StrongDual ℝ (WaveVectorSpace d)
```

**`Space.dual_apply`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L59).

```lean
lemma dual_apply (x : Space d) (k : WaveVectorSpace d) : x.dual k = k ⬝ᵥ x
```

**`WaveVectorSpace.dual`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L66).

> The functional on `Space d` dual to `k`, defined by `x ↦ k ⬝ᵥ x`.

```lean
def dual (k : WaveVectorSpace d) : StrongDual ℝ (Space d)
```

**`WaveVectorSpace.dual_apply`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L71).

```lean
lemma dual_apply (k : WaveVectorSpace d) (x : Space d) : k.dual x = k ⬝ᵥ x
```

## B. Bilinear pairing

**`WaveVectorSpace.pairingCLM`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L78).

> The bilinear form `WaveVectorSpace d × Space d → ℝ` given by `k ↦ x ↦ k ⬝ᵥ x`.

```lean
def pairingCLM : WaveVectorSpace d →L[ℝ] Space d →L[ℝ] ℝ
```

**`WaveVectorSpace.pairingCLM_apply_eq_dual`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L87).

```lean
lemma pairingCLM_apply_eq_dual (k : WaveVectorSpace d) : pairingCLM k = k.dual
```

**`WaveVectorSpace.pairingCLM_flip_apply_eq_dual`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean#L89).

```lean
lemma pairingCLM_flip_apply_eq_dual (x : Space d) : pairingCLM.flip x = x.dual
```

## Depends on

- [The structure of a module on Space](../space/part-01/module.md)
- [Wave Vector Space](basic.md)

## Sources

- [Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/WaveVectorSpace/DualPairing.lean)
