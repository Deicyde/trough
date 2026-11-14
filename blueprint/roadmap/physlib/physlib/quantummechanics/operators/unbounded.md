---
declaration: module
origin: cited
lean: LinearPMap.inner_map_polarization', LinearPMap.HasDenseDomain, LinearPMap.hasDenseDomain_def, LinearPMap.IsUnbounded, LinearPMap.isUnbounded_def, LinearPMap.IsSymmetric, LinearPMap.isSymmetric_def, LinearPMap.IsEssentiallySelfAdjoint
statement: formalized
proof: formalized
---

# Unbounded operators (Operators/Unbounded)

The module `Physlib.QuantumMechanics.Operators.Unbounded`, [Physlib/QuantumMechanics/Operators/Unbounded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean): 111 declarations, 35 with a docstring, 1 listed as significant.

## i. Overview

> The appropriate mathematical objects for discussing operators in non-relativistic quantum mechanics
> are partially-defined linear map (`LinearPMap`) between complex Hilbert spaces, `H →ₗ.[ℂ] H'`.
> An import class of operators in NRQM are those which are both densely defined and closable,
> which we refer to as \_unbounded\_. When `H = H'` operators may also be symmetric, self-adjoint or
> essentially self-adjoint (closure is self-adjoint).
>
> In this module we collect results on how the properties `HasDenseDomain`, `IsUnbounded`,
> `IsSymmetric`, `IsSelfAdjoint` and `IsEssentiallySelfAdjoint` interact with the basic algebraic
> operations, closure, adjoints, unitary conjugation and each other.

### Notes

> - Naming convention : Definitions of `LinearPMap`s for quantum mechanical unbounded operators should
>     have a name of the form `[…]Operator` and notation should use calligraphic capital letters,
>     e.g. `mulOperator f` (`𝓜 f`) for the multiplication operator associated with the function `f`.
>
> - Implementation : Although operators encountered in quantum mechanics are almost always unbounded,
>     we opt to implement unbounded operators via the property `IsUnbounded` on `LinearPMap` rather
>     than as a structure `UnboundedOperator` extending `LinearPMap`. The basic reason for this
>     is that addition/subtraction and composition of unbounded operators in general does not result
>     in another unbounded operator. This means, for example, that any attempt to define addition of
>     `UnboundedOperator`s would inevitably require introducing junk values that spoil associativity.

## ii. Key results

> Definitions
> - `HasDenseDomain` : An operator `U : H →ₗ.[ℂ] H'` has dense domain if `U.domain` is dense in `H`.
> - `IsUnbounded` : An operator is unbounded if it is both densely defined and closable.
> - `IsSymmetric` : An operator `T : H →ₗ.[ℂ] H` is symmetric if `⟪T x, y⟫_ℂ = ⟪x, T y⟫_ℂ` holds
>     for all `x y : T.domain`.
> - `IsEssentiallySelfAdjoint` : An operator `T : H →ₗ.[ℂ] H` is essentially self-adjoint if
>     its closure is self-adjoint.
>
> Results
> - `adjoint_add_le_add_adjoint` : The inequality `U₁† + U₂† ≤ (U₁ + U₂)†` when `U₁ + U₂` has
>     dense domain.
> - `unitaryConj` : The conjugation `u A u⁻¹ : H' →ₗ.[ℂ] H'` of `A` by a unitary `u`, with domain
>     `u (A.domain)`.
> - `IsFormalAdjoint.unitaryConj` : Unitary conjugation preserves formal-adjoint pairs.
> - `HasDenseDomain.unitaryConj_dense_domain` : If `A` has dense domain, then so does `u A u⁻¹`.
> - `unitaryConj_sub_smul_surjective` : If `A - z` is surjective for a scalar `z : ℂ`,
>     then so is `u A u⁻¹ - z`.
> - `adjoint_compRestricted_le_compRestricted_adjoint` : The inequality `U† ∘ᵣ V† ≤ (V ∘ᵣ U)†`
>     when `V` and `V ∘ᵣ U` have dense domain.
> - `IsUnbounded.adjoint` : The adjoint of an unbounded operator is also unbounded.
> - `IsUnbounded.adjoint_closure_eq_adjoint` : An unbounded operator and its closure have
>     the same adjoint.
> - `IsUnbounded.adjoint_adjoint_eq_closure` : An unbounded operator `U` satisfies `U†† = U.closure`.
> - `IsEssentiallySelfAdjoint.unique_self_adjoint_extension` : The closure of an essentially
>     self-adjoint unbounded operator is its unique self-adjoint extension.

## iv. References

> * Reed and Simon, Methods of Modern Mathematical Physics, Vol. I: Functional Analysis.
>   [ref: Reed1972]
> * Konrad Schmüdgen, Unbounded Self-Adjoint Operators on Hilbert Space. [ref: Schmudgen2012]

## A. Definitions

> See `LinearPMap.instStar` and `LinearPMap.isSelfAdjoint_def` for the definition of `IsSelfAdjoint`
> for `LinearPMap`s.

**`LinearPMap.HasDenseDomain`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L122).

> A LinearPMap `U` has dense domain iff `U.domain` is dense in `H`.

```lean
def HasDenseDomain (U : H →ₗ.[ℂ] H') : Prop
```

**`LinearPMap.hasDenseDomain_def`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L124).

```lean
lemma hasDenseDomain_def : U.HasDenseDomain ↔ Dense (U.domain : Set H)
```

**`LinearPMap.IsUnbounded`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L127).

> A LinearPMap is an unbounded operator iff it has dense domain and is closable.

```lean
def IsUnbounded (U : H →ₗ.[ℂ] H') : Prop
```

**`LinearPMap.isUnbounded_def`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L129).

```lean
lemma isUnbounded_def : U.IsUnbounded ↔ U.HasDenseDomain ∧ U.IsClosable
```

**`LinearPMap.IsSymmetric`**, a def, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L132).

> A LinearPMap `T` is symmetric iff `⟪T x, y⟫_ℂ = ⟪x, T y⟫_ℂ` for all `x y : T.domain`.

```lean
def IsSymmetric (T : H →ₗ.[ℂ] H) : Prop
```

**`LinearPMap.isSymmetric_def`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L134).

```lean
lemma isSymmetric_def : T.IsSymmetric ↔ T.IsFormalAdjoint T
```

**`LinearPMap.IsEssentiallySelfAdjoint`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L137).

> A LinearPMap is essentially self-adjoint iff its closure is self-adjoint.

```lean
def IsEssentiallySelfAdjoint [CompleteSpace H] (T : H →ₗ.[ℂ] H) : Prop
```

**`LinearPMap.isEssentiallySelfAdjoint_def`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L139).

```lean
lemma isEssentiallySelfAdjoint_def [CompleteSpace H] :
    T.IsEssentiallySelfAdjoint ↔ IsSelfAdjoint T.closure
```

**`LinearPMap.isStarNormal_def`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L142).

```lean
lemma isStarNormal_def [CompleteSpace H] : IsStarNormal T ↔ T† * T = T * T†
```

## B. Basic properties

### B.1. Dense domain

**`LinearPMap.HasDenseDomain.isUnbounded_iff_isClosable`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L152).

```lean
lemma HasDenseDomain.isUnbounded_iff_isClosable (h : U.HasDenseDomain) :
    U.IsUnbounded ↔ U.IsClosable
```

**`LinearPMap.HasDenseDomain.closure`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L156).

```lean
lemma HasDenseDomain.closure (h : U.HasDenseDomain) : U.closure.HasDenseDomain
```

**`LinearPMap.closure_domain_le_domain_closure`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L159).

```lean
lemma closure_domain_le_domain_closure (U : H →ₗ.[ℂ] H') : U.closure.domain ≤ U.domain.closure
```

**`LinearPMap.hasDenseDomain_iff_closure_hasDenseDomain`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L171).

```lean
lemma hasDenseDomain_iff_closure_hasDenseDomain : U.HasDenseDomain ↔ U.closure.HasDenseDomain
```

**`LinearPMap.HasDenseDomain.neg`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L174).

```lean
lemma HasDenseDomain.neg (h : U.HasDenseDomain) : (-U).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.smul`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L176).

```lean
lemma HasDenseDomain.smul (h : U.HasDenseDomain) (c : ℂ) : (c • U).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.add_of_le`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L178).

```lean
lemma HasDenseDomain.add_of_le (h₁ : U₁.HasDenseDomain) (h_le : U₁.domain ≤ U₂.domain) :
    (U₁ + U₂).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.sub_of_le`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L182).

```lean
lemma HasDenseDomain.sub_of_le (h₁ : U₁.HasDenseDomain) (h_le : U₁.domain ≤ U₂.domain) :
    (U₁ - U₂).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.sum_of_le`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L186).

```lean
lemma HasDenseDomain.sum_of_le
    {E : Submodule ℂ H} (hE : Dense (E : Set H)) (h : ∀ a, E ≤ (W a).domain) :
    (sum W).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.pow`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L191).

```lean
lemma HasDenseDomain.pow
    (h : T.HasDenseDomain) (h_range : ∀ x : T.domain, T x ∈ T.domain) (n : ℕ) :
    (T ^ n).HasDenseDomain
```

**`LinearPMap.pow_hasDenseDomain_of_le`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L199).

```lean
lemma pow_hasDenseDomain_of_le
    {n : ℕ} (h : (T ^ n).HasDenseDomain) {k : ℕ} (hle : k ≤ n) : (T ^ k).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.orthogonal_range`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L206).

> `U.rangeᗮ = U†.ker`
>
> c.f. `LinearMap.orthogonal_range` and `ContinuousLinearMap.orthogonal_range`

```lean
lemma HasDenseDomain.orthogonal_range [CompleteSpace H] (h : U.HasDenseDomain) :
    U.toFun.rangeᗮ = U†.toFun.ker.map U†.domain.subtype
```

**`LinearPMap.HasDenseDomain.orthogonal_adjoint_ker`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L218).

> `U†.kerᗮ = U.range.closure`

```lean
lemma HasDenseDomain.orthogonal_adjoint_ker [CompleteSpace H] [CompleteSpace H']
    (h : U.HasDenseDomain) :
    (U†.toFun.ker.map U†.domain.subtype)ᗮ = U.toFun.range.closure
```

### B.2. Closability

**`LinearPMap.IsClosed.closure_eq`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L227).

```lean
lemma IsClosed.closure_eq (h : U.IsClosed) : U.closure = U
```

**`LinearPMap.IsClosable.isClosed_iff`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L230).

```lean
lemma IsClosable.isClosed_iff (h : U.IsClosable) : U.IsClosed ↔ U.closure = U
```

**`LinearPMap.isClosable_of_exists_dense_formalAdjoint`**, a lemma, [line 234](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L234).

> A LinearPMap with densely-defined formal adjoint is closable.

```lean
lemma isClosable_of_exists_dense_formalAdjoint [CompleteSpace H] [CompleteSpace H']
    (h : U.HasDenseDomain) (h_fadj : ∃ U' : H' →ₗ.[ℂ] H, U'.HasDenseDomain ∧ U'.IsFormalAdjoint U) :
    U.IsClosable
```

**`LinearPMap.isClosable_of_zero`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L247).

> A zero LinearPMap (any domain) is closable.

```lean
lemma isClosable_of_zero (h_zero : ⇑U = 0) : U.IsClosable
```

**`LinearPMap.IsClosable.smul`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L256).

```lean
lemma IsClosable.smul (h : U.IsClosable) (c : ℂ) : (c • U).IsClosable
```

**`LinearPMap.IsClosable.smul_iff`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L273).

```lean
lemma IsClosable.smul_iff {c : ℂ} (hc : c ≠ 0) : (c • U).IsClosable ↔ U.IsClosable
```

**`LinearPMap.neg_eq_neg_one_smul`**, a lemma, [line 276](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L276).

```lean
lemma neg_eq_neg_one_smul (U : H →ₗ.[ℂ] H') : -U = (-1 : ℂ) • U
```

**`LinearPMap.IsClosable.neg`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L279).

```lean
lemma IsClosable.neg (h : U.IsClosable) : (-U).IsClosable
```

**`LinearPMap.closure_smul`**, a lemma, [line 281](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L281).

```lean
lemma closure_smul (U : H →ₗ.[ℂ] H') {c : ℂ} (hc : c ≠ 0) : (c • U).closure = c • U.closure
```

### B.3. Adjoints

**`LinearPMap.adjoint_one`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L307).

```lean
lemma adjoint_one [CompleteSpace H] : (1 : H →ₗ.[ℂ] H)† = 1
```

**`LinearPMap.adjoint_of_zero`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L314).

> The adjoint of a zero LinearPMap (any domain) is zero (domain `⊤`).

```lean
lemma adjoint_of_zero [CompleteSpace H] (h_zero : ⇑U = 0) : U† = 0
```

**`LinearPMap.adjoint_zero`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L324).

```lean
lemma adjoint_zero [CompleteSpace H] : (0 : H →ₗ.[ℂ] H')† = 0
```

**`LinearPMap.adjoint_smul`**, a lemma, [line 327](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L327).

```lean
lemma adjoint_smul [CompleteSpace H] (U : H →ₗ.[ℂ] H') {c : ℂ} (hc : c ≠ 0) :
    (c • U)† = conj c • U†
```

**`LinearPMap.adjoint_neg`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L339).

```lean
lemma adjoint_neg [CompleteSpace H] (U : H →ₗ.[ℂ] H') : (-U)† = -U†
```

**`LinearPMap.adjoint_antitone`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L342).

```lean
lemma adjoint_antitone [CompleteSpace H]
    (h₁₂ : U₁.HasDenseDomain ∨ ¬U₂.HasDenseDomain) (h_le : U₁ ≤ U₂) : U₂† ≤ U₁†
```

**`LinearPMap.adjoint_add_le_add_adjoint`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L360).

```lean
lemma adjoint_add_le_add_adjoint [CompleteSpace H]
    (U₁ U₂ : H →ₗ.[ℂ] H') (h₁₂ : (U₁ + U₂).HasDenseDomain) : U₁† + U₂† ≤ (U₁ + U₂)†
```

**`LinearPMap.adjoint_sub_le_sub_adjoint`**, a lemma, [line 376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L376).

```lean
lemma adjoint_sub_le_sub_adjoint [CompleteSpace H]
    (U₁ U₂ : H →ₗ.[ℂ] H') (h₁₂ : (U₁ - U₂).HasDenseDomain) : U₁† - U₂† ≤ (U₁ - U₂)†
```

**`LinearPMap.adjoint_compRestricted_le_compRestricted_adjoint`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L381).

```lean
lemma adjoint_compRestricted_le_compRestricted_adjoint [CompleteSpace H] [CompleteSpace H']
    (hV : V.HasDenseDomain) (hVU : (V ∘ᵣ U).HasDenseDomain) : U† ∘ᵣ V† ≤ (V ∘ᵣ U)†
```

**`LinearPMap.adjoint_pow_le_pow_adjoint`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L394).

```lean
lemma adjoint_pow_le_pow_adjoint [CompleteSpace H] {n : ℕ} (h : (T ^ n).HasDenseDomain) :
    T† ^ n ≤ (T ^ n)†
```

### B.4. Continuity / boundedness

**`LinearMap.continuous_iff_bounded`**, a lemma, [line 411](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L411).

> `f : E →ₗ[𝕜] F` is continuous iff there exists `M > 0` s.t. `‖f x‖ ≤ M * ‖x‖` for all `x : E`.
>
> This is a (convenient) immediate consequence of
> `IsBoundedLinearMap.isLinearMap_and_continuous_iff_isBoundedLinearMap`.

```lean
lemma _root_.LinearMap.continuous_iff_bounded {𝕜 E F : Type*} [NontriviallyNormedField 𝕜]
    [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [SeminormedAddCommGroup F] [NormedSpace 𝕜 F]
    {f : E →ₗ[𝕜] F} : Continuous f ↔ ∃ M, 0 < M ∧ ∀ x : E, ‖f x‖ ≤ M * ‖x‖
```

**`LinearPMap.isClosable_of_continuous`**, a lemma, [line 419](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L419).

> Continuous operators are closable.

```lean
lemma isClosable_of_continuous (h : Continuous U) : U.IsClosable
```

**`LinearPMap.closure_domain_eq_domain_closure_of_continuous`**, a lemma, [line 433](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L433).

> A strengthening of `closure_domain_le_domain_closure` for continuous operators.

```lean
lemma closure_domain_eq_domain_closure_of_continuous [CompleteSpace H'] (h : Continuous U) :
    U.closure.domain = U.domain.closure
```

**`LinearPMap.isClosed_iff_isClosed_domain_of_continuous`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L460).

> A continuous operator is closed iff its domain is closed.

```lean
lemma isClosed_iff_isClosed_domain_of_continuous [CompleteSpace H'] (h : Continuous U) :
    U.IsClosed ↔ _root_.IsClosed (U.domain : Set H)
```

**`LinearPMap.IsClosed.isClosed_toFun_graph`**, a lemma, [line 469](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L469).

```lean
lemma IsClosed.isClosed_toFun_graph (hU : U.IsClosed) :
    _root_.IsClosed (U.toFun.graph : Set (U.domain × H'))
```

**`LinearPMap.IsClosed.continuous_of_isClosed_domain`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L486).

> The **closed graph theorem** for partial linear maps:
> a closed operator with closed domain is continuous.
>
> This follows immediately from `LinearMap.continuous_of_isClosed_graph`
> and the completeness of `H` and `H'`.

```lean
lemma IsClosed.continuous_of_isClosed_domain [CompleteSpace H] [CompleteSpace H']
    (hU : U.IsClosed) (h : _root_.IsClosed (U.domain : Set H)) :
    Continuous U
```

**`LinearPMap.IsClosable.add_continuous`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L493).

> Closability is preserved upon adding a continuous operator.

```lean
lemma IsClosable.add_continuous
    (h₁ : U₁.IsClosable) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) :
    (U₁ + U₂).IsClosable
```

**`LinearPMap.IsClosable.sub_continuous`**, a lemma, [line 512](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L512).

> Closability is preserved upon subtracting a continuous operator.

```lean
lemma IsClosable.sub_continuous
    (h₁ : U₁.IsClosable) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) : (U₁ - U₂).IsClosable
```

**`LinearPMap.IsClosed.add_continuous`**, a lemma, [line 517](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L517).

> Closedness is preserved upon adding a continuous operator.

```lean
lemma IsClosed.add_continuous [CompleteSpace H']
    (h₁ : U₁.IsClosed) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) : (U₁ + U₂).IsClosed
```

**`LinearPMap.IsClosed.sub_continuous`**, a lemma, [line 552](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L552).

> Closedness is preserved upon subtracting a continuous operator.

```lean
lemma IsClosed.sub_continuous [CompleteSpace H']
    (h₁ : U₁.IsClosed) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) : (U₁ - U₂).IsClosed
```

**`LinearPMap.adjoint_domain_of_continuous`**, a lemma, [line 556](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L556).

```lean
lemma adjoint_domain_of_continuous [CompleteSpace H] (h : Continuous U) : U†.domain = ⊤
```

**`LinearPMap.HasDenseDomain.adjoint_add_continuous`**, a lemma, [line 561](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L561).

```lean
lemma HasDenseDomain.adjoint_add_continuous [CompleteSpace H]
    (h₁ : T₁.HasDenseDomain) (h₂ : Continuous T₂) (h : T₁.domain ≤ T₂.domain) :
    (T₁ + T₂)† = T₁† + T₂†
```

**`LinearPMap.HasDenseDomain.adjoint_sub_continuous`**, a lemma, [line 584](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L584).

```lean
lemma HasDenseDomain.adjoint_sub_continuous [CompleteSpace H]
    (h₁ : T₁.HasDenseDomain) (h₂ : Continuous T₂) (h : T₁.domain ≤ T₂.domain) :
    (T₁ - T₂)† = T₁† - T₂†
```

### B.5. Unitary conjugation

**`LinearPMap.unitaryConj`**, a def, [line 599](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L599).

> The conjugation `u A u⁻¹` of a partially-defined operator `A : H →ₗ.[ℂ] H` by a unitary
> `u : H ≃ₗᵢ[ℂ] H'`, with domain `u (A.domain) = u⁻¹ ⁻¹' (A.domain)` and action
> `y ↦ u (A (u⁻¹ y))`. Since `u` and `u⁻¹` are `ℂ`-linear, the result is again `ℂ`-linear.

```lean
def unitaryConj : H' →ₗ.[ℂ] H'
```

**`LinearPMap.mem_unitaryConj_domain_iff`**, a lemma, [line 607](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L607).

> Membership in the conjugated domain: `x ∈ D(u A u⁻¹) ↔ u⁻¹ x ∈ D(A)`.

```lean
lemma mem_unitaryConj_domain_iff {x : H'} :
    x ∈ (unitaryConj u A).domain ↔ u.symm x ∈ A.domain
```

**`LinearPMap.unitaryConj_apply`**, a lemma, [line 611](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L611).

> The defining formula `(u A u⁻¹) x = u (A (u⁻¹ x))`.

```lean
lemma unitaryConj_apply (x : (unitaryConj u A).domain) :
    unitaryConj u A x = u (A ⟨u.symm (x : H'), (mem_unitaryConj_domain_iff u A).mp x.2⟩)
```

**`LinearPMap.map_mem_unitaryConj_domain`**, a lemma, [line 615](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L615).

> `u` maps `D(A)` into `D(u A u⁻¹)`.

```lean
lemma map_mem_unitaryConj_domain (y : A.domain) : u (y : H) ∈ (unitaryConj u A).domain
```

**`LinearPMap.unitaryConj_apply_map`**, a lemma, [line 619](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L619).

> The action on the image domain: `(u A u⁻¹)(u y) = u (A y)` for `y ∈ D(A)`.

```lean
lemma unitaryConj_apply_map (y : A.domain) :
    unitaryConj u A ⟨u (y : H), map_mem_unitaryConj_domain u A y⟩ = u (A y)
```

**`LinearPMap.IsFormalAdjoint.unitaryConj`**, a lemma, [line 628](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L628).

> Unitary conjugation preserves formal adjointness. If `A` is a formal adjoint of `B`, then
> `u A u⁻¹` is a formal adjoint of `u B u⁻¹`. Unitary conjugation preserves symmetry when `A = B`.

```lean
lemma IsFormalAdjoint.unitaryConj {B : H →ₗ.[ℂ] H} (h : A.IsFormalAdjoint B) :
    (unitaryConj u A).IsFormalAdjoint (unitaryConj u B)
```

**`LinearPMap.HasDenseDomain.unitaryConj_dense_domain`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L640).

> If `A` has dense domain, then so does `u A u⁻¹`: the domain `u⁻¹ ⁻¹' (A.domain)` is the
> preimage of a dense set under a homeomorphism.

```lean
lemma HasDenseDomain.unitaryConj_dense_domain (hdense : A.HasDenseDomain) :
    (unitaryConj u A).HasDenseDomain
```

**`LinearPMap.unitaryConj_sub_smul_surjective`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L644).

> If `A - z` is surjective for a scalar `z : ℂ`, then so is `u A u⁻¹ - z`.

```lean
lemma unitaryConj_sub_smul_surjective {z : ℂ} (h : Function.Surjective (A - z • 1).toFun) :
    Function.Surjective (unitaryConj u A - z • 1).toFun
```

## C. Classes of operators

### C.1. Unbounded operators

**`LinearPMap.IsUnbounded.hasDenseDomain`**, a lemma, [line 663](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L663).

```lean
lemma IsUnbounded.hasDenseDomain (h : U.IsUnbounded) : U.HasDenseDomain
```

**`LinearPMap.IsUnbounded.isClosable`**, a lemma, [line 665](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L665).

```lean
lemma IsUnbounded.isClosable (h : U.IsUnbounded) : U.IsClosable
```

**`LinearPMap.IsUnbounded.adjoint`**, a lemma, [line 667](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L667).

```lean
lemma IsUnbounded.adjoint [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    U†.IsUnbounded
```

**`LinearPMap.IsUnbounded.closure`**, a lemma, [line 686](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L686).

```lean
lemma IsUnbounded.closure (h : U.IsUnbounded) : U.closure.IsUnbounded
```

**`LinearPMap.IsUnbounded.adjoint_closure_eq_adjoint`**, a lemma, [line 690](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L690).

```lean
lemma IsUnbounded.adjoint_closure_eq_adjoint [CompleteSpace H] (h : U.IsUnbounded) :
    U.closure† = U†
```

**`LinearPMap.IsUnbounded.adjoint_adjoint_eq_closure`**, a lemma, [line 700](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L700).

```lean
lemma IsUnbounded.adjoint_adjoint_eq_closure [CompleteSpace H] [CompleteSpace H']
    (h : U.IsUnbounded) :
    U†† = U.closure
```

**`LinearPMap.IsUnbounded.le_adjoint_adjoint`**, a lemma, [line 710](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L710).

```lean
lemma IsUnbounded.le_adjoint_adjoint [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    U ≤ U††
```

**`LinearPMap.IsUnbounded.isClosed_iff`**, a lemma, [line 714](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L714).

```lean
lemma IsUnbounded.isClosed_iff [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    U.IsClosed ↔ U†† = U
```

**`LinearPMap.IsUnbounded.orthogonal_adjoint_range`**, a lemma, [line 719](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L719).

> `U†.rangeᗮ = U.closure.ker`

```lean
lemma IsUnbounded.orthogonal_adjoint_range [CompleteSpace H] [CompleteSpace H']
    (h : U.IsUnbounded) : U†.toFun.rangeᗮ = U.closure.toFun.ker.map U.closure.domain.subtype
```

**`LinearPMap.IsUnbounded.orthogonal_closure_ker`**, a lemma, [line 724](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L724).

> `U.closure.kerᗮ = U†.range`

```lean
lemma IsUnbounded.orthogonal_closure_ker [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    (U.closure.toFun.ker.map U.closure.domain.subtype)ᗮ = U†.toFun.range.closure
```

### C.2. Symmetric operators

**`LinearPMap.inner_map_polarization`**, a lemma, [line 733](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L733).

> The analogue of `inner_map_polarization` for LinearPMap.

```lean
lemma inner_map_polarization (x y : T.domain) :
    ⟪T y, x⟫_ℂ = (⟪T (x + y), ↑(x + y)⟫_ℂ - ⟪T (x - y), ↑(x - y)⟫_ℂ
      + I * ⟪T (x + I • y), ↑(x + I • y)⟫_ℂ - I * ⟪T (x - I • y), ↑(x - I • y)⟫_ℂ) / 4
```

**`LinearPMap.inner_map_polarization'`**, a theorem, [line 743](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L743). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The analogue of `inner_map_polarization'` for LinearPMap.

```lean
theorem inner_map_polarization' (x y : T.domain) :
    ⟪T x, y⟫_ℂ = (⟪T (x + y), ↑(x + y)⟫_ℂ - ⟪T (x - y), ↑(x - y)⟫_ℂ
      - I * ⟪T (x + I • y), ↑(x + I • y)⟫_ℂ + I * ⟪T (x - I • y), ↑(x - I • y)⟫_ℂ) / 4
```

**`LinearPMap.isSymmetric_iff_inner_map_self_real`**, a lemma, [line 753](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L753).

```lean
lemma isSymmetric_iff_inner_map_self_real :
    T.IsSymmetric ↔ ∀ x : T.domain, conj ⟪T x, x⟫_ℂ = ⟪T x, x⟫_ℂ
```

**`LinearPMap.IsSymmetric.isClosable`**, a lemma, [line 761](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L761).

```lean
lemma IsSymmetric.isClosable [CompleteSpace H] (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    T.IsClosable
```

**`LinearPMap.IsSymmetric.isUnbounded_iff_hasDenseDomain`**, a lemma, [line 765](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L765).

```lean
lemma IsSymmetric.isUnbounded_iff_hasDenseDomain [CompleteSpace H] (h : T.IsSymmetric) :
    T.IsUnbounded ↔ T.HasDenseDomain
```

**`LinearPMap.isSymmetric_iff_le_adjoint`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L769).

```lean
lemma isSymmetric_iff_le_adjoint [CompleteSpace H] (h : T.HasDenseDomain) :
    T.IsSymmetric ↔ T ≤ T†
```

**`LinearPMap.IsSymmetric.closure_le_adjoint`**, a lemma, [line 775](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L775).

```lean
lemma IsSymmetric.closure_le_adjoint [CompleteSpace H] (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    T.closure ≤ T†
```

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_iff`**, a lemma, [line 780](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L780).

```lean
lemma IsSymmetric.isEssentiallySelfAdjoint_iff [CompleteSpace H]
    (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    T.IsEssentiallySelfAdjoint ↔ T†.domain = T.closure.domain
```

**`LinearPMap.IsSymmetric.isSelfAdjoint_iff`**, a lemma, [line 789](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L789).

```lean
lemma IsSymmetric.isSelfAdjoint_iff [CompleteSpace H] (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    IsSelfAdjoint T ↔ T†.domain = T.domain
```

**`LinearPMap.add_adjoint_isSymmetric`**, a lemma, [line 795](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L795).

```lean
lemma add_adjoint_isSymmetric [CompleteSpace H] (h : T.HasDenseDomain) :
    (T + T.adjoint).IsSymmetric
```

**`LinearPMap.IsSymmetric.pow`**, a lemma, [line 805](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L805).

```lean
lemma IsSymmetric.pow (h : T.IsSymmetric) (n : ℕ) : (T ^ n).IsSymmetric
```

**`LinearPMap.IsSymmetric.neg`**, a lemma, [line 821](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L821).

```lean
lemma IsSymmetric.neg (h : T.IsSymmetric) : (-T).IsSymmetric
```

**`LinearPMap.IsSymmetric.add`**, a lemma, [line 824](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L824).

```lean
lemma IsSymmetric.add (h₁ : T₁.IsSymmetric) (h₂ : T₂.IsSymmetric) : (T₁ + T₂).IsSymmetric
```

**`LinearPMap.IsSymmetric.sub`**, a lemma, [line 830](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L830).

```lean
lemma IsSymmetric.sub (h₁ : T₁.IsSymmetric) (h₂ : T₂.IsSymmetric) : (T₁ - T₂).IsSymmetric
```

**`LinearPMap.IsSymmetric.smul`**, a lemma, [line 834](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L834).

```lean
lemma IsSymmetric.smul (h : T.IsSymmetric) {c : ℂ} (hc : conj c = c) : (c • T).IsSymmetric
```

**`LinearPMap.IsSymmetric.real_smul`**, a lemma, [line 838](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L838).

```lean
lemma IsSymmetric.real_smul (h : T.IsSymmetric) (r : ℝ) : (r • T).IsSymmetric
```

**`LinearPMap.IsSymmetric.sum`**, a lemma, [line 842](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L842).

```lean
lemma IsSymmetric.sum (h : ∀ a, (S a).IsSymmetric) : (sum S).IsSymmetric
```

**`LinearPMap.IsSymmetric.of_le`**, a lemma, [line 846](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L846).

```lean
lemma IsSymmetric.of_le (h₁ : T₁.IsSymmetric) (h_le : T₂ ≤ T₁) : T₂.IsSymmetric
```

**`LinearPMap.IsSymmetric.closure`**, a lemma, [line 854](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L854).

> The closure of a symmetric densely-defined operator is symmetric: `T††` is a symmetric
> closed extension of `T`, so it extends `T.closure`, whose symmetry then descends.

```lean
lemma IsSymmetric.closure [CompleteSpace H] (hsym : T.IsSymmetric) (hdense : T.HasDenseDomain) :
    T.closure.IsSymmetric
```

**`LinearPMap.isUnbounded_of_dense_of_isSymmetric`**, a lemma, [line 867](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L867).

> A LinearPMap constructed from a symmetric LinearMap with dense domain
> is an unbounded operator.

```lean
lemma isUnbounded_of_dense_of_isSymmetric [CompleteSpace H] {E : Submodule ℂ H}
    (hE : Dense (E : Set H)) {f : E →ₗ[ℂ] H} (h : ∀ x y : E, ⟪f x, ↑y⟫_ℂ = ⟪↑x, f y⟫_ℂ) :
    (mk E f).IsUnbounded
```

**`LinearPMap.isUnbounded_of_dense_of_isSymmetric'`**, a lemma, [line 873](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L873).

> Variant of `of_dense_of_isSymmetric` for an endomorphism satisfying `LinearMap.IsSymmetric`.

```lean
lemma isUnbounded_of_dense_of_isSymmetric' [CompleteSpace H]
    {E : Submodule ℂ H} (hE : Dense (E : Set H)) {f : E →ₗ[ℂ] E} (h : f.IsSymmetric) :
    (mk E (E.subtype ∘ₗ f)).IsUnbounded
```

### C.3. Self-adjoint operators

**`LinearPMap.IsSelfAdjoint.isSymmetric`**, a lemma, [line 882](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L882).

```lean
lemma IsSelfAdjoint.isSymmetric [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsSymmetric
```

**`LinearPMap.IsSelfAdjoint.isClosed`**, a lemma, [line 887](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L887).

```lean
lemma IsSelfAdjoint.isClosed [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsClosed
```

**`LinearPMap.IsSelfAdjoint.isClosable`**, a lemma, [line 890](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L890).

```lean
lemma IsSelfAdjoint.isClosable [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsClosable
```

**`LinearPMap.IsSelfAdjoint.isUnbounded`**, a lemma, [line 893](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L893).

```lean
lemma IsSelfAdjoint.isUnbounded [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsUnbounded
```

**`LinearPMap.IsSelfAdjoint.isEssentiallySelfAdjoint`**, a lemma, [line 896](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L896).

```lean
lemma IsSelfAdjoint.isEssentiallySelfAdjoint [CompleteSpace H] (h : IsSelfAdjoint T) :
    T.IsEssentiallySelfAdjoint
```

**`LinearPMap.IsSelfAdjoint.adjoint`**, a lemma, [line 901](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L901).

```lean
lemma IsSelfAdjoint.adjoint [CompleteSpace H] (h : IsSelfAdjoint T) : IsSelfAdjoint T†
```

**`LinearPMap.IsSelfAdjoint.smul`**, a lemma, [line 906](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L906).

```lean
lemma IsSelfAdjoint.smul [CompleteSpace H]
    (h : IsSelfAdjoint T) {c : ℂ} (hc : c ≠ 0) (hc' : conj c = c) :
    IsSelfAdjoint (c • T)
```

**`LinearPMap.IsSelfAdjoint.real_smul`**, a lemma, [line 912](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L912).

```lean
lemma IsSelfAdjoint.real_smul [CompleteSpace H] (h : IsSelfAdjoint T) {r : ℝ} (hr : r ≠ 0) :
    IsSelfAdjoint (r • T)
```

**`LinearPMap.IsSelfAdjoint.neg`**, a lemma, [line 917](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L917).

```lean
lemma IsSelfAdjoint.neg [CompleteSpace H] (h : IsSelfAdjoint T) : IsSelfAdjoint (-T)
```

**`LinearPMap.IsSymmetric.isSelfAdjoint_of_range_eq_top`**, a lemma, [line 922](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L922).

> Self-adjointness from surjectivity of `T ± i`: a symmetric, densely-defined operator `T` for
> which `T + I • 1` and `T - I • 1` both have full range is self-adjoint.

```lean
lemma IsSymmetric.isSelfAdjoint_of_range_eq_top [CompleteSpace H] (hsym : T.IsSymmetric)
    (hdense : T.HasDenseDomain)
    (hadd : (T + I • 1).toFun.range = ⊤) (hsub : (T - I • 1).toFun.range = ⊤) :
    IsSelfAdjoint T
```

### C.4. Essentially self-adjoint operators

**`LinearPMap.IsEssentiallySelfAdjoint.hasDenseDomain`**, a lemma, [line 958](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L958).

```lean
lemma IsEssentiallySelfAdjoint.hasDenseDomain [CompleteSpace H] (h : T.IsEssentiallySelfAdjoint) :
    T.HasDenseDomain
```

**`LinearPMap.IsEssentiallySelfAdjoint.isSymmetric`**, a lemma, [line 962](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L962).

```lean
lemma IsEssentiallySelfAdjoint.isSymmetric [CompleteSpace H] (h : T.IsEssentiallySelfAdjoint) :
    T.IsSymmetric
```

**`LinearPMap.IsEssentiallySelfAdjoint.isClosable`**, a lemma, [line 966](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L966).

```lean
lemma IsEssentiallySelfAdjoint.isClosable [CompleteSpace H] (h : T.IsEssentiallySelfAdjoint) :
    T.IsClosable
```

**`LinearPMap.IsEssentiallySelfAdjoint.isUnbounded`**, a lemma, [line 970](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L970).

```lean
lemma IsEssentiallySelfAdjoint.isUnbounded [CompleteSpace H] (h : T.IsEssentiallySelfAdjoint) :
    T.IsUnbounded
```

**`LinearPMap.IsEssentiallySelfAdjoint.unique_self_adjoint_extension`**, a lemma, [line 975](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L975).

> The closure is the unique self-adjoint extension of an essentially self-adjoint operator.

```lean
lemma IsEssentiallySelfAdjoint.unique_self_adjoint_extension [CompleteSpace H]
    (h : T.IsEssentiallySelfAdjoint) {T₂ : H →ₗ.[ℂ] H} (h_le : T ≤ T₂) (h₂ : IsSelfAdjoint T₂) :
    T₂ = T.closure
```

**`LinearPMap.IsEssentiallySelfAdjoint.smul`**, a lemma, [line 983](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L983).

```lean
lemma IsEssentiallySelfAdjoint.smul [CompleteSpace H]
    (h : T.IsEssentiallySelfAdjoint) {c : ℂ} (hc : c ≠ 0) (hc' : conj c = c) :
    (c • T).IsEssentiallySelfAdjoint
```

**`LinearPMap.IsEssentiallySelfAdjoint.real_smul`**, a lemma, [line 989](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L989).

```lean
lemma IsEssentiallySelfAdjoint.real_smul [CompleteSpace H]
    (h : T.IsEssentiallySelfAdjoint) {r : ℝ} (hr : r ≠ 0) :
    (r • T).IsEssentiallySelfAdjoint
```

**`LinearPMap.IsEssentiallySelfAdjoint.neg`**, a lemma, [line 995](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean#L995).

```lean
lemma IsEssentiallySelfAdjoint.neg [CompleteSpace H] (h : T.IsEssentiallySelfAdjoint) :
    (-T).IsEssentiallySelfAdjoint
```

## Depends on

- [LinearPMap](../../mathematics/formathlib/linearpmap.md)

## Proof depends on

- [Submodules of `E × F`](../../mathematics/innerproductspace/submodule.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Unbounded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/Unbounded.lean)
