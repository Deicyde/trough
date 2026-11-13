---
declaration: theorem
origin: cited
lean: ChabautyColeman.main_affine_rat_of_rank_le, ChabautyColeman.NumberFieldBase.main_affine_numberField, ChabautyColeman.NumberFieldBase.ratPoints_finite_numberField
statement: formalized
proof: formalized
---

# Chabauty–Coleman bounds for odd-degree hyperelliptic curves

> Proves the rank-sensitive Chabauty–Coleman point-count bound for monic odd-degree hyperelliptic curves over the rationals and number fields at primes of squarefree reduction. The Jacobian group is the ideal class group of the affine coordinate ring; its identification with an algebraic Jacobian variety is outside this formalization. Includes Mumford representatives, reduction of divisor classes, multivariable formal groups, p-adic logarithms, and residue-disk zero counts. Independent upstream archive results are omitted.

*Quoted from the card [LeanPool/projects/hyperelliptic-chabauty-coleman.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hyperelliptic-chabauty-coleman.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`ChabautyColeman.main_affine_rat_of_rank_le`](https://leanpool.github.io/lean-pool/LeanPool/HyperellipticCurves/Count/Arithmetic.html#ChabautyColeman.main_affine_rat_of_rank_le) (theorem; a main declaration), declared in [LeanPool/HyperellipticCurves/Count/Arithmetic.lean, line 134](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HyperellipticCurves/Count/Arithmetic.lean#L134): “For a monic odd-degree hyperelliptic curve over Q whose coordinate-ring class group has rational rank at most r below the genus, and a prime p greater than 2r + 2 with an integral model of squarefree reduction, the affine rational point count plus one is at most the reduced affine point count plus one, plus 2r.”
- [`ChabautyColeman.NumberFieldBase.main_affine_numberField`](https://leanpool.github.io/lean-pool/LeanPool/HyperellipticCurves/Count/NumberField.html#ChabautyColeman.NumberFieldBase.main_affine_numberField) (theorem; a main declaration), declared in [LeanPool/HyperellipticCurves/Count/NumberField.lean, line 548](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HyperellipticCurves/Count/NumberField.lean#L548): “Over the fraction field of a Dedekind domain finite free over Z, the same class-group-rank bound holds at a prime of squarefree reduction when the residue characteristic exceeds 2r plus the absolute ramification index plus 1.”
- [`ChabautyColeman.NumberFieldBase.ratPoints_finite_numberField`](https://leanpool.github.io/lean-pool/LeanPool/HyperellipticCurves/Count/NumberField.html#ChabautyColeman.NumberFieldBase.ratPoints_finite_numberField) (theorem; a main declaration), declared in [LeanPool/HyperellipticCurves/Count/NumberField.lean, line 693](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HyperellipticCurves/Count/NumberField.lean#L693): “The set of rational affine points on a monic odd-degree hyperelliptic curve over a number field is finite when the rational rank of the ideal class group of its affine coordinate ring is smaller than its genus.”

## Project

- Authors: Michael Stoll.
- Source: *Independence of rational points on twists of a given curve*, [doi:10.1112/S0010437X06002168](https://doi.org/10.1112/S0010437X06002168).
- Project repository: [MichaelStollBayreuth/HyperellipticCurves](https://github.com/MichaelStollBayreuth/HyperellipticCurves), at commit [a541f718](https://github.com/MichaelStollBayreuth/HyperellipticCurves/tree/a541f7182de678e07edcccc7a307c777cecfc8fe).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11G30, 14G05, 14H25.
- In Lean Pool: [LeanPool/HyperellipticCurves](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HyperellipticCurves), from the card [LeanPool/projects/hyperelliptic-chabauty-coleman.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hyperelliptic-chabauty-coleman.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/hyperelliptic-chabauty-coleman.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/hyperelliptic-chabauty-coleman.yaml)
- [Lean Pool at 701389c0: LeanPool/HyperellipticCurves](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/HyperellipticCurves)
