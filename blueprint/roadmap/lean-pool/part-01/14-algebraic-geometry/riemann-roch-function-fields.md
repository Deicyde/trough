---
declaration: theorem
origin: cited
lean: FunctionField.riemann_roch
statement: formalized
proof: formalized
---

# Riemann–Roch for algebraic function fields

> Formalizes the Riemann–Roch theorem for algebraic function fields of one variable through the adelic route. Divisors are indexed by intrinsic places (discrete rank-one valuation subrings containing the constants), with an equivalence to a two-chart coordinate model via Ostrowski's theorem. The development builds Riemann–Roch spaces, the genus, an intrinsic adele space, Weil differentials and the canonical class, and proves Riemann's inequality, the duality theorem, Riemann–Roch, Clifford's inequality, and the standard corollaries. As an application it shows that a Weierstrass elliptic curve has genus one and identifies its degree-one places with the class group of the coordinate ring compatibly with the group law.

*Quoted from the card [LeanPool/projects/riemann-roch-function-fields.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/riemann-roch-function-fields.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FunctionField.riemann_roch`](https://leanpool.github.io/lean-pool/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.html#FunctionField.riemann_roch) (theorem; a main declaration), declared in [LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean, line 286](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean#L286): “For a function field K over its full constant field k, a canonical divisor W, and any divisor D indexed by intrinsic places, ℓ(D) = deg D + 1 − g + ℓ(W − D).”
- [`FunctionField.duality`](https://leanpool.github.io/lean-pool/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.html#FunctionField.duality) (theorem), declared in [LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean, line 272](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean#L272): “For a canonical divisor W and any divisor D, ℓ(W − D) equals the index of specialty i(D), the codimension of L(D) plus K inside the adele space.”
- [`FunctionField.riemann_ineq`](https://leanpool.github.io/lean-pool/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.html#FunctionField.riemann_ineq) (theorem), declared in [LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean, line 279](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean#L279): “Riemann's inequality ℓ(D) ≥ deg D + 1 − g holds for every divisor D.”
- [`FunctionField.clifford`](https://leanpool.github.io/lean-pool/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.html#FunctionField.clifford) (theorem), declared in [LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean, line 341](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean#L341): “Clifford's inequality 2(ℓ(D) − 1) ≤ deg D holds for every divisor D with 0 ≤ deg D ≤ 2g − 2, ℓ(D) > 0, and ℓ(W − D) > 0 for a canonical divisor W. The degree bounds are not needed for the inequality and are dropped in FunctionField.clifford_of_ell_pos.”
- [`FunctionField.exists_isCanonical`](https://leanpool.github.io/lean-pool/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.html#FunctionField.exists_isCanonical) (theorem), declared in [LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean, line 265](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields/CoordinateFree/RiemannRoch.lean#L265): “Every function field admits a canonical divisor, namely the divisor of a nonzero Weil differential.”
- [`WeierstrassCurve.Affine.genus_eq_one`](https://leanpool.github.io/lean-pool/LeanPool/RiemannRochFunctionFields/CoordinateFree/EllipticCurve.html#WeierstrassCurve.Affine.genus_eq_one) (theorem), declared in [LeanPool/RiemannRochFunctionFields/CoordinateFree/EllipticCurve.lean, line 91](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields/CoordinateFree/EllipticCurve.lean#L91): “The function field of a Weierstrass elliptic curve over a field k that is its full constant field (for example any algebraically closed k, in any characteristic) has genus one.”
- [`WeierstrassCurve.Affine.picTorsor_compat_groupLaw`](https://leanpool.github.io/lean-pool/LeanPool/RiemannRochFunctionFields/CoordinateFree/EllipticCurve.html#WeierstrassCurve.Affine.picTorsor_compat_groupLaw) (theorem), declared in [LeanPool/RiemannRochFunctionFields/CoordinateFree/EllipticCurve.lean, line 100](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields/CoordinateFree/EllipticCurve.lean#L100): “The bijection between degree-one places of an elliptic function field and the class group of the coordinate ring is compatible with the elliptic group law.”

## Project

- Authors: Guanghao Li.
- Source: *Riemann–Roch for function fields, in Lean 4* by Guanghao Li.
- Project repository: [vaca22/riemann-roch-function-fields](https://github.com/vaca22/riemann-roch-function-fields), at commit [dbca5bee](https://github.com/vaca22/riemann-roch-function-fields/tree/dbca5beed1da77e2ecd1eec207d0451fa57e8aa6).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 14H05, 11R58, 14H52.
- In Lean Pool: [LeanPool/RiemannRochFunctionFields](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields), from the card [LeanPool/projects/riemann-roch-function-fields.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/riemann-roch-function-fields.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/riemann-roch-function-fields.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/riemann-roch-function-fields.yaml)
- [Lean Pool at 701389c0: LeanPool/RiemannRochFunctionFields](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/RiemannRochFunctionFields)
