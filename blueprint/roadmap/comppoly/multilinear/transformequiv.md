---
catalog: module
lean: CompPoly.CMlPolynomial.lagrangeToMono_eq_lagrangeToMonoSpec, CompPoly.CMlPolynomial.monoToLagrange_eq_monoToLagrangeSpec
statement: formalized
proof: formalized
---

# Fast ↔ Spec equivalence for the multilinear zeta / Möbius transforms

`CompPoly.Multilinear.TransformEquiv`, in [CompPoly/Multilinear/TransformEquiv.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/TransformEquiv.lean), by Quang Dao, Chung Thai Nguyen, Natalie Klaus.

> This file proves that the $O(n \cdot 2^n)$ butterfly transforms
> `monoToLagrange` and `lagrangeToMono` (defined in `CompPoly.Multilinear.Basic`) coincide
> pointwise with their $O(4^n)$ inclusion-exclusion specifications
> `monoToLagrangeSpec` and `lagrangeToMonoSpec` respectively.
>
> The proofs use a common pattern: an indexed family of partial subset sums that
> interpolates between the identity and the full spec, with each transform level
> corresponding to exactly one step of the interpolation.
>
> * `section MobiusEquivalence` proves `lagrangeToMono = lagrangeToMonoSpec`.
> * `section ZetaEquivalence` proves `monoToLagrange = monoToLagrangeSpec`.
>
> All helper lemmas are `private`; only the two top-level theorems
> `lagrangeToMono_eq_lagrangeToMonoSpec` and `monoToLagrange_eq_monoToLagrangeSpec`
> are exported.

> ### Fast ↔ Spec equivalence for the Möbius transform
>
> We prove `lagrangeToMono = lagrangeToMonoSpec` by introducing an indexed family of
> "partial Möbius sums" `mobiusPartial k` that interpolates between the identity (at `k = n`)
> and the full spec (at `k = 0`). Each step of the fast transform
> `lagrangeToMonoLevel (k - 1)` decrements the parameter by exactly one. Combined with the
> base case we obtain the result by descending induction on `k`.

`CompPoly.CMlPolynomial.lagrangeToMono_eq_lagrangeToMonoSpec` (theorem, [line 532](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/TransformEquiv.lean#L532))

> The fast Möbius transform `lagrangeToMono` is pointwise equal to the inclusion-exclusion
> specification `lagrangeToMonoSpec`. Combines the fold lemma with the `k = 0` base case.

```lean
theorem lagrangeToMono_eq_lagrangeToMonoSpec
    (p : Vector R (2 ^ n)) :
    lagrangeToMono n p = lagrangeToMonoSpec p
```

> ### Fast ↔ Spec equivalence for the zeta transform
>
> Mirror of `MobiusEquivalence`: we prove `monoToLagrange = monoToLagrangeSpec` with an
> indexed family `zetaPartial k` of partial subset sums. Instead of the low-bits constraint
> used in the Möbius proof, here `k` counts how many leading levels have already been
> applied — the constraint is that `j` must agree with `i` on bits **at or above**
> position `k` (`i / 2 ^ k = j / 2 ^ k`).
>
> * At `k = 0` only `j = i` matches, so `zetaPartial 0 p i = p[i]`.
> * At `k = n` the constraint is vacuous, recovering `monoToLagrangeSpec`.
>
> Each application of `monoToLagrangeLevel k` to `Vector.ofFn (zetaPartial k p)` increments
> `k` by one. `monoToLagrange n` is a `foldl`, so applying the levels `0, 1, …, n-1`
> transports us from `zetaPartial 0 = id` to `zetaPartial n = spec`.

`CompPoly.CMlPolynomial.monoToLagrange_eq_monoToLagrangeSpec` (theorem, [line 785](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/TransformEquiv.lean#L785))

> The fast zeta transform `monoToLagrange` is pointwise equal to the naive
> `monoToLagrangeSpec`. Mirror of `lagrangeToMono_eq_lagrangeToMonoSpec`.

```lean
theorem monoToLagrange_eq_monoToLagrangeSpec
    (p : Vector R (2 ^ n)) :
    monoToLagrange n p = monoToLagrangeSpec p
```

## Depends on

- [Multilinear Polynomials](basic.md)

## Sources

- [CompPoly/Multilinear/TransformEquiv.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Multilinear/TransformEquiv.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multilinear.TransformEquiv.json)
