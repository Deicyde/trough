---
declaration: module
origin: cited
lean: IsMaximalSelfAdjoint, instTrivialStarIsMaximalSelfAdjoint, instRCLikeIsMaximalSelfAdjoint, IsMaximalSelfAdjoint.trivial_selfadjMap, IsMaximalSelfAdjoint.RCLike_selfadjMap
statement: formalized
proof: formalized
---

# Maximal self-adjoint subrings

The module `QuantumInfo.ForMathlib.IsMaximalSelfAdjoint`, [QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean): 5 declarations, 3 with a docstring.

> This file introduces the `IsMaximalSelfAdjoint R α` typeclass, which records that the
> `TrivialStar` ring `R` carries the self-adjoint part of a star ring `α`. It bundles an
> additive, `R`-linear map `selfadjMap : α →+ R` that inverts `algebraMap R α` on self-adjoint
> elements. The guiding example is `R = ℝ`, `α = ℂ`: it lets a quantity such as the trace of a
> Hermitian matrix be valued in `ℝ` instead of `ℂ`, reflecting that physical observables are
> self-adjoint and take real expectation values.

**`IsMaximalSelfAdjoint`**, a class, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean#L27).

> `IsMaximalSelfAdjoint R α` witnesses that `R` is the maximal `TrivialStar` subring of the
> star ring `α`, via an additive map `selfadjMap : α →+ R` collecting the self-adjoint part of
> each element. This lets `HermitianMat.trace` return `𝕜` when `𝕜` already has a trivial star,
> and the "clean" underlying type otherwise, e.g. `ℝ` when the input field is `ℂ`.

```lean
class IsMaximalSelfAdjoint (R : outParam Type*) (α : Type*) [Star α] [Star R] [CommSemiring R]
    [Semiring α] [TrivialStar R] [Algebra R α] where
  /-- The additive map sending an element of `α` to its self-adjoint part in `R`. -/
  selfadjMap : α →+ R
  /-- `selfadjMap` pulls scalar multiplication by `R` out of its argument. -/
  selfadj_smul : ∀ (r : R) (a : α), selfadjMap (r • a) = r * (selfadjMap a)
  /-- On self-adjoint elements, `selfadjMap` is a section of `algebraMap R α`. -/
  selfadj_algebra : ∀ {a : α}, IsSelfAdjoint a → algebraMap _ _ (selfadjMap a) = a
```

**`instTrivialStarIsMaximalSelfAdjoint`**, an instance, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean#L37).

> Every `TrivialStar` `CommSemiring` is its own maximal self adjoints.

```lean
instance instTrivialStarIsMaximalSelfAdjoint {R} [Star R] [TrivialStar R] [CommSemiring R] :
    IsMaximalSelfAdjoint R R
```

**`instRCLikeIsMaximalSelfAdjoint`**, an instance, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean#L44).

> ℝ is the maximal self adjoint elements over RCLike

```lean
instance instRCLikeIsMaximalSelfAdjoint {α} [RCLike α] : IsMaximalSelfAdjoint ℝ α
```

**`IsMaximalSelfAdjoint.trivial_selfadjMap`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean#L56).

```lean
lemma trivial_selfadjMap {R} [Star R] [TrivialStar R] [CommSemiring R] :
    (selfadjMap : R →+ R) = .id R
```

**`IsMaximalSelfAdjoint.RCLike_selfadjMap`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean#L61).

```lean
lemma RCLike_selfadjMap {α} [RCLike α] : (selfadjMap : α →+ ℝ) = RCLike.re
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/IsMaximalSelfAdjoint.lean)
