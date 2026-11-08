---
declaration: theorem
origin: cited
lean: RingHom.isQuasiregular_ker
statement: formalized
proof: formalized
---

# Scalar unit reflection and canonical quasi-regular kernels

For
`f : R →+* S` from a possibly noncommutative ring to a semiring,
`IsLocalHom f` (reflection of units) makes the canonical two-sided kernel
`TwoSidedIdeal.ker f` quasi-regular, **without surjectivity**, by
[`RingHom.isQuasiregular_ker`](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean).
For a **surjective** such map, unit reflection is equivalent to kernel
quasi-regularity by
[`RingHom.isLocalHom_iff_isQuasiregular_ker`](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean);
its reverse direction is also available through
[`RingHom.isLocalHom_of_surjective_of_isQuasiregular_ker`](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean).
Mathlib supplies `IsUnit (f a) ↔ IsUnit a` via `isUnit_map_iff`; under
surjectivity it also gives a surjective induced map on units. Source and
target universes are independent; neither commutativity, local-ring
structure, nontriviality nor nilness of the kernel is assumed. Nil kernels
specialize through `TwoSidedIdeal.IsNil.isQuasiregular`.

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/README.md#headline-results) of [FormalFrontier/general-linear-groups](https://github.com/FormalFrontier/general-linear-groups) at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `RingHom.isQuasiregular_ker` (theorem), declared in [GeneralLinearGroups/QuasiregularQuotient.lean, line 202](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L202).

Read from the source at commit [a2199cf0](https://github.com/FormalFrontier/general-linear-groups/tree/a2199cf0d02b1e0775890a7ed09b709dfbfba74b), without running Lean.

## Sources

- [general-linear-groups at a2199cf0: README, headline results](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/README.md#headline-results)
- [Source of `RingHom.isQuasiregular_ker` in GeneralLinearGroups/QuasiregularQuotient.lean](https://github.com/FormalFrontier/general-linear-groups/blob/a2199cf0d02b1e0775890a7ed09b709dfbfba74b/GeneralLinearGroups/QuasiregularQuotient.lean#L202)
