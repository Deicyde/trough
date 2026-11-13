---
declaration: inductive
origin: cited
lean: Flean.Float, toFloat, toRat, to_float_to_rat, roundf_close
statement: formalized
---

# Flean: Floating-Point Numbers in Lean

> Formalizes a configurable model of floating-point numbers in Lean 4, including normal and subnormal representations, conversions between rationals and floats, round-trip correctness, and rounding error bounds.

*Quoted from the card [LeanPool/projects/flean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/flean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Flean.Float`](https://leanpool.github.io/lean-pool/LeanPool/Flean/Basic.html#Flean.Float) (inductive; a main declaration), declared in [LeanPool/Flean/Basic.lean, line 47](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Flean/Basic.lean#L47): “Defines the floating-point number type parameterized by a precision and exponent configuration, with normal, subnormal, infinite, and NaN cases.”
- [`toFloat`](https://leanpool.github.io/lean-pool/LeanPool/Flean/Basic.html#toFloat) (def; a main declaration), declared in [LeanPool/Flean/Basic.lean, line 59](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Flean/Basic.lean#L59): “Rounds a rational number to the nearest representable floating-point value under a given rounding mode.”
- [`toRat`](https://leanpool.github.io/lean-pool/LeanPool/Flean/Basic.html#toRat) (def; a main declaration), declared in [LeanPool/Flean/Basic.lean, line 90](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Flean/Basic.lean#L90): “Interprets a floating-point value as the exact rational number it represents.”
- [`to_float_to_rat`](https://leanpool.github.io/lean-pool/LeanPool/Flean/Basic.html#to_float_to_rat) (lemma; a main declaration), declared in [LeanPool/Flean/Basic.lean, line 233](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Flean/Basic.lean#L233): “Proves the round-trip identity that converting a finite nonzero float to a rational and back recovers the original float.”
- [`roundf_close`](https://leanpool.github.io/lean-pool/LeanPool/Flean/Rounding.html#roundf_close) (lemma; a main declaration), declared in [LeanPool/Flean/Rounding.lean, line 541](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Flean/Rounding.lean#L541): “Bounds the distance between a rational and its rounded floating-point representation.”

## Project

- Authors: Joseph McKinsey.
- Source: [doi:10.1109/IEEESTD.2019.8766229](https://doi.org/10.1109/IEEESTD.2019.8766229).
- Project repository: [josephmckinsey/flean](https://github.com/josephmckinsey/flean).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 65G50, 65G30, 68V20.
- In Lean Pool: [LeanPool/Flean](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Flean), from the card [LeanPool/projects/flean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/flean.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/flean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/flean.yaml)
- [Lean Pool at 701389c0: LeanPool/Flean](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Flean)
