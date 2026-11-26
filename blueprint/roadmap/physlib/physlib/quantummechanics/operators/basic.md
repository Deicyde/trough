---
declaration: module
origin: cited
lean: LinearPMap.inner_map_polarization', LinearPMap.HasDenseDomain, LinearPMap.hasDenseDomain_def, LinearPMap.IsUnbounded, LinearPMap.isUnbounded_def, LinearPMap.IsSymmetric, LinearPMap.isSymmetric_def, LinearPMap.isStarNormal_def
statement: formalized
proof: formalized
---

# Unbounded operators (Basic)

The module `Physlib.QuantumMechanics.Operators.Basic`, [Physlib/QuantumMechanics/Operators/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean): 99 declarations, 33 with a docstring, 1 listed as significant.

## i. Overview

> The appropriate mathematical objects for discussing operators in non-relativistic quantum mechanics
> are partially-defined linear map (`LinearPMap`) between complex Hilbert spaces, `H →ₗ.[ℂ] H'`.
> An import class of operators in NRQM are those which are both densely defined and closable,
> which we refer to as \_unbounded\_. When `H = H'` operators may also be symmetric, self-adjoint or
> essentially self-adjoint (closure is self-adjoint).
>
> In this module we collect results on how the properties `HasDenseDomain`, `IsUnbounded`,
> `IsSymmetric`, and `IsSelfAdjoint` interact with the basic algebraic
> operations, closure, adjoints, unitary conjugation and each other.
>
> **Notes**
>
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

## iv. References

> * Reed and Simon, Methods of Modern Mathematical Physics, Vol. I: Functional Analysis.
>   [ref: Reed1972]
> * Konrad Schmüdgen, Unbounded Self-Adjoint Operators on Hilbert Space. [ref: Schmudgen2012]

## A. Definitions

> See `LinearPMap.instStar` and `LinearPMap.isSelfAdjoint_def` for the definition of `IsSelfAdjoint`
> for `LinearPMap`s.

**`LinearPMap.HasDenseDomain`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L117).

> A LinearPMap `U` has dense domain iff `U.domain` is dense in `H`.

```lean
def HasDenseDomain (U : H →ₗ.[ℂ] H') : Prop
```

**`LinearPMap.hasDenseDomain_def`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L119).

```lean
lemma hasDenseDomain_def : U.HasDenseDomain ↔ Dense (U.domain : Set H)
```

**`LinearPMap.IsUnbounded`**, a def, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L122).

> A LinearPMap is an unbounded operator iff it has dense domain and is closable.

```lean
def IsUnbounded (U : H →ₗ.[ℂ] H') : Prop
```

**`LinearPMap.isUnbounded_def`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L124).

```lean
lemma isUnbounded_def : U.IsUnbounded ↔ U.HasDenseDomain ∧ U.IsClosable
```

**`LinearPMap.IsSymmetric`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L127).

> A LinearPMap `T` is symmetric iff `⟪T x, y⟫_ℂ = ⟪x, T y⟫_ℂ` for all `x y : T.domain`.

```lean
def IsSymmetric (T : H →ₗ.[ℂ] H) : Prop
```

**`LinearPMap.isSymmetric_def`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L129).

```lean
lemma isSymmetric_def : T.IsSymmetric ↔ T.IsFormalAdjoint T
```

**`LinearPMap.isStarNormal_def`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L131).

```lean
lemma isStarNormal_def [CompleteSpace H] : IsStarNormal T ↔ T† * T = T * T†
```

## B. Basic properties

### B.1. Dense domain

**`LinearPMap.HasDenseDomain.isUnbounded_iff_isClosable`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L141).

```lean
lemma HasDenseDomain.isUnbounded_iff_isClosable (h : U.HasDenseDomain) :
    U.IsUnbounded ↔ U.IsClosable
```

**`LinearPMap.HasDenseDomain.closure`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L145).

```lean
lemma HasDenseDomain.closure (h : U.HasDenseDomain) : U.closure.HasDenseDomain
```

**`LinearPMap.closure_domain_le_domain_closure`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L148).

```lean
lemma closure_domain_le_domain_closure (U : H →ₗ.[ℂ] H') : U.closure.domain ≤ U.domain.closure
```

**`LinearPMap.hasDenseDomain_iff_closure_hasDenseDomain`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L160).

```lean
lemma hasDenseDomain_iff_closure_hasDenseDomain : U.HasDenseDomain ↔ U.closure.HasDenseDomain
```

**`LinearPMap.HasDenseDomain.neg`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L163).

```lean
lemma HasDenseDomain.neg (h : U.HasDenseDomain) : (-U).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.smul`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L165).

```lean
lemma HasDenseDomain.smul (h : U.HasDenseDomain) (c : ℂ) : (c • U).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.add_of_le`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L167).

```lean
lemma HasDenseDomain.add_of_le (h₁ : U₁.HasDenseDomain) (h_le : U₁.domain ≤ U₂.domain) :
    (U₁ + U₂).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.sub_of_le`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L171).

```lean
lemma HasDenseDomain.sub_of_le (h₁ : U₁.HasDenseDomain) (h_le : U₁.domain ≤ U₂.domain) :
    (U₁ - U₂).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.sum_of_le`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L175).

```lean
lemma HasDenseDomain.sum_of_le
    {E : Submodule ℂ H} (hE : Dense (E : Set H)) (h : ∀ a, E ≤ (W a).domain) :
    (sum W).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.pow`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L180).

```lean
lemma HasDenseDomain.pow
    (h : T.HasDenseDomain) (h_range : ∀ x : T.domain, T x ∈ T.domain) (n : ℕ) :
    (T ^ n).HasDenseDomain
```

**`LinearPMap.pow_hasDenseDomain_of_le`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L188).

```lean
lemma pow_hasDenseDomain_of_le
    {n : ℕ} (h : (T ^ n).HasDenseDomain) {k : ℕ} (hle : k ≤ n) : (T ^ k).HasDenseDomain
```

**`LinearPMap.HasDenseDomain.orthogonal_range`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L195).

> `U.rangeᗮ = U†.ker`
>
> c.f. `LinearMap.orthogonal_range` and `ContinuousLinearMap.orthogonal_range`

```lean
lemma HasDenseDomain.orthogonal_range [CompleteSpace H] (h : U.HasDenseDomain) :
    U.toFun.rangeᗮ = U†.toFun.ker.map U†.domain.subtype
```

**`LinearPMap.HasDenseDomain.orthogonal_adjoint_ker`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L207).

> `U†.kerᗮ = U.range.closure`

```lean
lemma HasDenseDomain.orthogonal_adjoint_ker [CompleteSpace H] [CompleteSpace H']
    (h : U.HasDenseDomain) :
    (U†.toFun.ker.map U†.domain.subtype)ᗮ = U.toFun.range.closure
```

### B.2. Closability

**`LinearPMap.IsClosed.closure_eq`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L216).

```lean
lemma IsClosed.closure_eq (h : U.IsClosed) : U.closure = U
```

**`LinearPMap.IsClosable.isClosed_iff`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L219).

```lean
lemma IsClosable.isClosed_iff (h : U.IsClosable) : U.IsClosed ↔ U.closure = U
```

**`LinearPMap.isClosable_of_exists_dense_formalAdjoint`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L223).

> A LinearPMap with densely-defined formal adjoint is closable.

```lean
lemma isClosable_of_exists_dense_formalAdjoint [CompleteSpace H] [CompleteSpace H']
    (h : U.HasDenseDomain) (h_fadj : ∃ U' : H' →ₗ.[ℂ] H, U'.HasDenseDomain ∧ U'.IsFormalAdjoint U) :
    U.IsClosable
```

**`LinearPMap.isClosable_of_zero`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L236).

> A zero LinearPMap (any domain) is closable.

```lean
lemma isClosable_of_zero (h_zero : ⇑U = 0) : U.IsClosable
```

**`LinearPMap.IsClosable.smul`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L245).

```lean
lemma IsClosable.smul (h : U.IsClosable) (c : ℂ) : (c • U).IsClosable
```

**`LinearPMap.IsClosable.smul_iff`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L262).

```lean
lemma IsClosable.smul_iff {c : ℂ} (hc : c ≠ 0) : (c • U).IsClosable ↔ U.IsClosable
```

**`LinearPMap.neg_eq_neg_one_smul`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L265).

```lean
lemma neg_eq_neg_one_smul (U : H →ₗ.[ℂ] H') : -U = (-1 : ℂ) • U
```

**`LinearPMap.IsClosable.neg`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L268).

```lean
lemma IsClosable.neg (h : U.IsClosable) : (-U).IsClosable
```

**`LinearPMap.closure_smul`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L270).

```lean
lemma closure_smul (U : H →ₗ.[ℂ] H') {c : ℂ} (hc : c ≠ 0) : (c • U).closure = c • U.closure
```

### B.3. Adjoints

**`LinearPMap.adjoint_one`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L296).

```lean
lemma adjoint_one [CompleteSpace H] : (1 : H →ₗ.[ℂ] H)† = 1
```

**`LinearPMap.adjoint_of_zero`**, a lemma, [line 303](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L303).

> The adjoint of a zero LinearPMap (any domain) is zero (domain `⊤`).

```lean
lemma adjoint_of_zero [CompleteSpace H] (h_zero : ⇑U = 0) : U† = 0
```

**`LinearPMap.adjoint_zero`**, a lemma, [line 313](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L313).

```lean
lemma adjoint_zero [CompleteSpace H] : (0 : H →ₗ.[ℂ] H')† = 0
```

**`LinearPMap.adjoint_smul`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L316).

```lean
lemma adjoint_smul [CompleteSpace H] (U : H →ₗ.[ℂ] H') {c : ℂ} (hc : c ≠ 0) :
    (c • U)† = conj c • U†
```

**`LinearPMap.adjoint_neg`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L328).

```lean
lemma adjoint_neg [CompleteSpace H] (U : H →ₗ.[ℂ] H') : (-U)† = -U†
```

**`LinearPMap.adjoint_antitone`**, a lemma, [line 331](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L331).

```lean
lemma adjoint_antitone [CompleteSpace H]
    (h₁₂ : U₁.HasDenseDomain ∨ ¬U₂.HasDenseDomain) (h_le : U₁ ≤ U₂) : U₂† ≤ U₁†
```

**`LinearPMap.adjoint_add_le_add_adjoint`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L349).

```lean
lemma adjoint_add_le_add_adjoint [CompleteSpace H]
    (U₁ U₂ : H →ₗ.[ℂ] H') (h₁₂ : (U₁ + U₂).HasDenseDomain) : U₁† + U₂† ≤ (U₁ + U₂)†
```

**`LinearPMap.adjoint_sub_le_sub_adjoint`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L365).

```lean
lemma adjoint_sub_le_sub_adjoint [CompleteSpace H]
    (U₁ U₂ : H →ₗ.[ℂ] H') (h₁₂ : (U₁ - U₂).HasDenseDomain) : U₁† - U₂† ≤ (U₁ - U₂)†
```

**`LinearPMap.adjoint_compRestricted_le_compRestricted_adjoint`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L370).

```lean
lemma adjoint_compRestricted_le_compRestricted_adjoint [CompleteSpace H] [CompleteSpace H']
    (hV : V.HasDenseDomain) (hVU : (V ∘ᵣ U).HasDenseDomain) : U† ∘ᵣ V† ≤ (V ∘ᵣ U)†
```

**`LinearPMap.adjoint_pow_le_pow_adjoint`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L383).

```lean
lemma adjoint_pow_le_pow_adjoint [CompleteSpace H] {n : ℕ} (h : (T ^ n).HasDenseDomain) :
    T† ^ n ≤ (T ^ n)†
```

### B.4. Continuity / boundedness

**`LinearMap.continuous_iff_bounded`**, a lemma, [line 400](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L400).

> `f : E →ₗ[𝕜] F` is continuous iff there exists `M > 0` s.t. `‖f x‖ ≤ M * ‖x‖` for all `x : E`.
>
> This is a (convenient) immediate consequence of
> `IsBoundedLinearMap.isLinearMap_and_continuous_iff_isBoundedLinearMap`.

```lean
lemma _root_.LinearMap.continuous_iff_bounded {𝕜 E F : Type*} [NontriviallyNormedField 𝕜]
    [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [SeminormedAddCommGroup F] [NormedSpace 𝕜 F]
    {f : E →ₗ[𝕜] F} : Continuous f ↔ ∃ M, 0 < M ∧ ∀ x : E, ‖f x‖ ≤ M * ‖x‖
```

**`LinearPMap.isClosable_of_continuous`**, a lemma, [line 408](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L408).

> Continuous operators are closable.

```lean
lemma isClosable_of_continuous (h : Continuous U) : U.IsClosable
```

**`LinearPMap.closure_domain_eq_domain_closure_of_continuous`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L422).

> A strengthening of `closure_domain_le_domain_closure` for continuous operators.

```lean
lemma closure_domain_eq_domain_closure_of_continuous [CompleteSpace H'] (h : Continuous U) :
    U.closure.domain = U.domain.closure
```

**`LinearPMap.isClosed_iff_isClosed_domain_of_continuous`**, a lemma, [line 449](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L449).

> A continuous operator is closed iff its domain is closed.

```lean
lemma isClosed_iff_isClosed_domain_of_continuous [CompleteSpace H'] (h : Continuous U) :
    U.IsClosed ↔ _root_.IsClosed (U.domain : Set H)
```

**`LinearPMap.IsClosed.isClosed_toFun_graph`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L458).

```lean
lemma IsClosed.isClosed_toFun_graph (hU : U.IsClosed) :
    _root_.IsClosed (U.toFun.graph : Set (U.domain × H'))
```

**`LinearPMap.IsClosed.continuous_of_isClosed_domain`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L475).

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

**`LinearPMap.IsClosable.add_continuous`**, a lemma, [line 482](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L482).

> Closability is preserved upon adding a continuous operator.

```lean
lemma IsClosable.add_continuous
    (h₁ : U₁.IsClosable) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) :
    (U₁ + U₂).IsClosable
```

**`LinearPMap.IsClosable.sub_continuous`**, a lemma, [line 501](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L501).

> Closability is preserved upon subtracting a continuous operator.

```lean
lemma IsClosable.sub_continuous
    (h₁ : U₁.IsClosable) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) : (U₁ - U₂).IsClosable
```

**`LinearPMap.IsClosed.add_continuous`**, a lemma, [line 506](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L506).

> Closedness is preserved upon adding a continuous operator.

```lean
lemma IsClosed.add_continuous [CompleteSpace H']
    (h₁ : U₁.IsClosed) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) : (U₁ + U₂).IsClosed
```

**`LinearPMap.IsClosed.sub_continuous`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L541).

> Closedness is preserved upon subtracting a continuous operator.

```lean
lemma IsClosed.sub_continuous [CompleteSpace H']
    (h₁ : U₁.IsClosed) (h₂ : Continuous U₂) (h : U₁.domain ≤ U₂.domain) : (U₁ - U₂).IsClosed
```

**`LinearPMap.adjoint_domain_of_continuous`**, a lemma, [line 545](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L545).

```lean
lemma adjoint_domain_of_continuous [CompleteSpace H] (h : Continuous U) : U†.domain = ⊤
```

**`LinearPMap.HasDenseDomain.adjoint_add_continuous`**, a lemma, [line 550](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L550).

```lean
lemma HasDenseDomain.adjoint_add_continuous [CompleteSpace H]
    (h₁ : T₁.HasDenseDomain) (h₂ : Continuous T₂) (h : T₁.domain ≤ T₂.domain) :
    (T₁ + T₂)† = T₁† + T₂†
```

**`LinearPMap.HasDenseDomain.adjoint_sub_continuous`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L573).

```lean
lemma HasDenseDomain.adjoint_sub_continuous [CompleteSpace H]
    (h₁ : T₁.HasDenseDomain) (h₂ : Continuous T₂) (h : T₁.domain ≤ T₂.domain) :
    (T₁ - T₂)† = T₁† - T₂†
```

### B.5. Unitary conjugation

**`LinearPMap.unitaryConj`**, a def, [line 588](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L588).

> The conjugation `u A u⁻¹` of a partially-defined operator `A : H →ₗ.[ℂ] H` by a unitary
> `u : H ≃ₗᵢ[ℂ] H'`, with domain `u (A.domain) = u⁻¹ ⁻¹' (A.domain)` and action
> `y ↦ u (A (u⁻¹ y))`. Since `u` and `u⁻¹` are `ℂ`-linear, the result is again `ℂ`-linear.

```lean
def unitaryConj : H' →ₗ.[ℂ] H'
```

**`LinearPMap.mem_unitaryConj_domain_iff`**, a lemma, [line 596](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L596).

> Membership in the conjugated domain: `x ∈ D(u A u⁻¹) ↔ u⁻¹ x ∈ D(A)`.

```lean
lemma mem_unitaryConj_domain_iff {x : H'} :
    x ∈ (unitaryConj u A).domain ↔ u.symm x ∈ A.domain
```

**`LinearPMap.unitaryConj_apply`**, a lemma, [line 600](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L600).

> The defining formula `(u A u⁻¹) x = u (A (u⁻¹ x))`.

```lean
lemma unitaryConj_apply (x : (unitaryConj u A).domain) :
    unitaryConj u A x = u (A ⟨u.symm (x : H'), (mem_unitaryConj_domain_iff u A).mp x.2⟩)
```

**`LinearPMap.map_mem_unitaryConj_domain`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L604).

> `u` maps `D(A)` into `D(u A u⁻¹)`.

```lean
lemma map_mem_unitaryConj_domain (y : A.domain) : u (y : H) ∈ (unitaryConj u A).domain
```

**`LinearPMap.unitaryConj_apply_map`**, a lemma, [line 608](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L608).

> The action on the image domain: `(u A u⁻¹)(u y) = u (A y)` for `y ∈ D(A)`.

```lean
lemma unitaryConj_apply_map (y : A.domain) :
    unitaryConj u A ⟨u (y : H), map_mem_unitaryConj_domain u A y⟩ = u (A y)
```

**`LinearPMap.IsFormalAdjoint.unitaryConj`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L617).

> Unitary conjugation preserves formal adjointness. If `A` is a formal adjoint of `B`, then
> `u A u⁻¹` is a formal adjoint of `u B u⁻¹`. Unitary conjugation preserves symmetry when `A = B`.

```lean
lemma IsFormalAdjoint.unitaryConj {B : H →ₗ.[ℂ] H} (h : A.IsFormalAdjoint B) :
    (unitaryConj u A).IsFormalAdjoint (unitaryConj u B)
```

**`LinearPMap.HasDenseDomain.unitaryConj_dense_domain`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L629).

> If `A` has dense domain, then so does `u A u⁻¹`: the domain `u⁻¹ ⁻¹' (A.domain)` is the
> preimage of a dense set under a homeomorphism.

```lean
lemma HasDenseDomain.unitaryConj_dense_domain (hdense : A.HasDenseDomain) :
    (unitaryConj u A).HasDenseDomain
```

**`LinearPMap.unitaryConj_sub_smul_surjective`**, a lemma, [line 633](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L633).

> If `A - z` is surjective for a scalar `z : ℂ`, then so is `u A u⁻¹ - z`.

```lean
lemma unitaryConj_sub_smul_surjective {z : ℂ} (h : Function.Surjective (A - z • 1).toFun) :
    Function.Surjective (unitaryConj u A - z • 1).toFun
```

## C. Classes of operators

### C.1. Unbounded operators

**`LinearPMap.IsUnbounded.hasDenseDomain`**, a lemma, [line 652](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L652).

```lean
lemma IsUnbounded.hasDenseDomain (h : U.IsUnbounded) : U.HasDenseDomain
```

**`LinearPMap.IsUnbounded.isClosable`**, a lemma, [line 654](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L654).

```lean
lemma IsUnbounded.isClosable (h : U.IsUnbounded) : U.IsClosable
```

**`LinearPMap.IsUnbounded.adjoint`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L656).

```lean
lemma IsUnbounded.adjoint [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    U†.IsUnbounded
```

**`LinearPMap.IsUnbounded.closure`**, a lemma, [line 675](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L675).

```lean
lemma IsUnbounded.closure (h : U.IsUnbounded) : U.closure.IsUnbounded
```

**`LinearPMap.IsUnbounded.adjoint_closure_eq_adjoint`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L679).

```lean
lemma IsUnbounded.adjoint_closure_eq_adjoint [CompleteSpace H] (h : U.IsUnbounded) :
    U.closure† = U†
```

**`LinearPMap.IsUnbounded.adjoint_adjoint_eq_closure`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L689).

```lean
lemma IsUnbounded.adjoint_adjoint_eq_closure [CompleteSpace H] [CompleteSpace H']
    (h : U.IsUnbounded) :
    U†† = U.closure
```

**`LinearPMap.IsUnbounded.le_adjoint_adjoint`**, a lemma, [line 699](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L699).

```lean
lemma IsUnbounded.le_adjoint_adjoint [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    U ≤ U††
```

**`LinearPMap.IsUnbounded.isClosed_iff`**, a lemma, [line 703](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L703).

```lean
lemma IsUnbounded.isClosed_iff [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    U.IsClosed ↔ U†† = U
```

**`LinearPMap.IsUnbounded.orthogonal_adjoint_range`**, a lemma, [line 708](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L708).

> `U†.rangeᗮ = U.closure.ker`

```lean
lemma IsUnbounded.orthogonal_adjoint_range [CompleteSpace H] [CompleteSpace H']
    (h : U.IsUnbounded) : U†.toFun.rangeᗮ = U.closure.toFun.ker.map U.closure.domain.subtype
```

**`LinearPMap.IsUnbounded.orthogonal_closure_ker`**, a lemma, [line 713](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L713).

> `U.closure.kerᗮ = U†.range`

```lean
lemma IsUnbounded.orthogonal_closure_ker [CompleteSpace H] [CompleteSpace H'] (h : U.IsUnbounded) :
    (U.closure.toFun.ker.map U.closure.domain.subtype)ᗮ = U†.toFun.range.closure
```

### C.2. Symmetric operators

**`LinearPMap.inner_map_polarization`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L722).

> The analogue of `inner_map_polarization` for LinearPMap.

```lean
lemma inner_map_polarization (x y : T.domain) :
    ⟪T y, x⟫_ℂ = (⟪T (x + y), ↑(x + y)⟫_ℂ - ⟪T (x - y), ↑(x - y)⟫_ℂ
      + I * ⟪T (x + I • y), ↑(x + I • y)⟫_ℂ - I * ⟪T (x - I • y), ↑(x - I • y)⟫_ℂ) / 4
```

**`LinearPMap.inner_map_polarization'`**, a theorem, [line 732](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L732). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/scripts/lint/exemptions/Theorems.txt).

> The analogue of `inner_map_polarization'` for LinearPMap.

```lean
theorem inner_map_polarization' (x y : T.domain) :
    ⟪T x, y⟫_ℂ = (⟪T (x + y), ↑(x + y)⟫_ℂ - ⟪T (x - y), ↑(x - y)⟫_ℂ
      - I * ⟪T (x + I • y), ↑(x + I • y)⟫_ℂ + I * ⟪T (x - I • y), ↑(x - I • y)⟫_ℂ) / 4
```

**`LinearPMap.isSymmetric_iff_inner_map_self_real`**, a lemma, [line 742](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L742).

```lean
lemma isSymmetric_iff_inner_map_self_real :
    T.IsSymmetric ↔ ∀ x : T.domain, conj ⟪T x, x⟫_ℂ = ⟪T x, x⟫_ℂ
```

**`LinearPMap.IsSymmetric.isClosable`**, a lemma, [line 750](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L750).

```lean
lemma IsSymmetric.isClosable [CompleteSpace H] (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    T.IsClosable
```

**`LinearPMap.IsSymmetric.isUnbounded_iff_hasDenseDomain`**, a lemma, [line 754](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L754).

```lean
lemma IsSymmetric.isUnbounded_iff_hasDenseDomain [CompleteSpace H] (h : T.IsSymmetric) :
    T.IsUnbounded ↔ T.HasDenseDomain
```

**`LinearPMap.isSymmetric_iff_le_adjoint`**, a lemma, [line 758](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L758).

```lean
lemma isSymmetric_iff_le_adjoint [CompleteSpace H] (h : T.HasDenseDomain) :
    T.IsSymmetric ↔ T ≤ T†
```

**`LinearPMap.IsSymmetric.closure_le_adjoint`**, a lemma, [line 764](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L764).

```lean
lemma IsSymmetric.closure_le_adjoint [CompleteSpace H] (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    T.closure ≤ T†
```

**`LinearPMap.IsSymmetric.isSelfAdjoint_iff`**, a lemma, [line 769](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L769).

```lean
lemma IsSymmetric.isSelfAdjoint_iff [CompleteSpace H] (h : T.IsSymmetric) (h' : T.HasDenseDomain) :
    IsSelfAdjoint T ↔ T†.domain = T.domain
```

**`LinearPMap.add_adjoint_isSymmetric`**, a lemma, [line 775](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L775).

```lean
lemma add_adjoint_isSymmetric [CompleteSpace H] (h : T.HasDenseDomain) :
    (T + T.adjoint).IsSymmetric
```

**`LinearPMap.IsSymmetric.pow`**, a lemma, [line 785](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L785).

```lean
lemma IsSymmetric.pow (h : T.IsSymmetric) (n : ℕ) : (T ^ n).IsSymmetric
```

**`LinearPMap.IsSymmetric.neg`**, a lemma, [line 801](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L801).

```lean
lemma IsSymmetric.neg (h : T.IsSymmetric) : (-T).IsSymmetric
```

**`LinearPMap.IsSymmetric.add`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L804).

```lean
lemma IsSymmetric.add (h₁ : T₁.IsSymmetric) (h₂ : T₂.IsSymmetric) : (T₁ + T₂).IsSymmetric
```

**`LinearPMap.IsSymmetric.sub`**, a lemma, [line 810](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L810).

```lean
lemma IsSymmetric.sub (h₁ : T₁.IsSymmetric) (h₂ : T₂.IsSymmetric) : (T₁ - T₂).IsSymmetric
```

**`LinearPMap.IsSymmetric.smul`**, a lemma, [line 814](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L814).

```lean
lemma IsSymmetric.smul (h : T.IsSymmetric) {c : ℂ} (hc : conj c = c) : (c • T).IsSymmetric
```

**`LinearPMap.IsSymmetric.real_smul`**, a lemma, [line 818](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L818).

```lean
lemma IsSymmetric.real_smul (h : T.IsSymmetric) (r : ℝ) : (r • T).IsSymmetric
```

**`LinearPMap.IsSymmetric.sum`**, a lemma, [line 822](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L822).

```lean
lemma IsSymmetric.sum (h : ∀ a, (S a).IsSymmetric) : (sum S).IsSymmetric
```

**`LinearPMap.IsSymmetric.of_le`**, a lemma, [line 826](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L826).

```lean
lemma IsSymmetric.of_le (h₁ : T₁.IsSymmetric) (h_le : T₂ ≤ T₁) : T₂.IsSymmetric
```

**`LinearPMap.IsSymmetric.closure`**, a lemma, [line 834](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L834).

> The closure of a symmetric densely-defined operator is symmetric: `T††` is a symmetric
> closed extension of `T`, so it extends `T.closure`, whose symmetry then descends.

```lean
lemma IsSymmetric.closure [CompleteSpace H] (hsym : T.IsSymmetric) (hdense : T.HasDenseDomain) :
    T.closure.IsSymmetric
```

**`LinearPMap.isUnbounded_of_dense_of_isSymmetric`**, a lemma, [line 847](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L847).

> A LinearPMap constructed from a symmetric LinearMap with dense domain
> is an unbounded operator.

```lean
lemma isUnbounded_of_dense_of_isSymmetric [CompleteSpace H] {E : Submodule ℂ H}
    (hE : Dense (E : Set H)) {f : E →ₗ[ℂ] H} (h : ∀ x y : E, ⟪f x, ↑y⟫_ℂ = ⟪↑x, f y⟫_ℂ) :
    (mk E f).IsUnbounded
```

**`LinearPMap.isUnbounded_of_dense_of_isSymmetric'`**, a lemma, [line 853](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L853).

> Variant of `of_dense_of_isSymmetric` for an endomorphism satisfying `LinearMap.IsSymmetric`.

```lean
lemma isUnbounded_of_dense_of_isSymmetric' [CompleteSpace H]
    {E : Submodule ℂ H} (hE : Dense (E : Set H)) {f : E →ₗ[ℂ] E} (h : f.IsSymmetric) :
    (mk E (E.subtype ∘ₗ f)).IsUnbounded
```

### C.3. Self-adjoint operators

**`LinearPMap.IsSelfAdjoint.isSymmetric`**, a lemma, [line 862](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L862).

```lean
lemma IsSelfAdjoint.isSymmetric [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsSymmetric
```

**`LinearPMap.IsSelfAdjoint.isClosed`**, a lemma, [line 867](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L867).

```lean
lemma IsSelfAdjoint.isClosed [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsClosed
```

**`LinearPMap.IsSelfAdjoint.isClosable`**, a lemma, [line 870](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L870).

```lean
lemma IsSelfAdjoint.isClosable [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsClosable
```

**`LinearPMap.IsSelfAdjoint.isUnbounded`**, a lemma, [line 873](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L873).

```lean
lemma IsSelfAdjoint.isUnbounded [CompleteSpace H] (h : IsSelfAdjoint T) : T.IsUnbounded
```

**`LinearPMap.IsSelfAdjoint.adjoint`**, a lemma, [line 877](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L877).

```lean
lemma IsSelfAdjoint.adjoint [CompleteSpace H] (h : IsSelfAdjoint T) : IsSelfAdjoint T†
```

**`LinearPMap.IsSelfAdjoint.smul`**, a lemma, [line 882](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L882).

```lean
lemma IsSelfAdjoint.smul [CompleteSpace H]
    (h : IsSelfAdjoint T) {c : ℂ} (hc : c ≠ 0) (hc' : conj c = c) :
    IsSelfAdjoint (c • T)
```

**`LinearPMap.IsSelfAdjoint.real_smul`**, a lemma, [line 888](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L888).

```lean
lemma IsSelfAdjoint.real_smul [CompleteSpace H] (h : IsSelfAdjoint T) {r : ℝ} (hr : r ≠ 0) :
    IsSelfAdjoint (r • T)
```

**`LinearPMap.IsSelfAdjoint.neg`**, a lemma, [line 893](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L893).

```lean
lemma IsSelfAdjoint.neg [CompleteSpace H] (h : IsSelfAdjoint T) : IsSelfAdjoint (-T)
```

**`LinearPMap.IsSymmetric.isSelfAdjoint_of_range_eq_top`**, a lemma, [line 898](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean#L898).

> Self-adjointness from surjectivity of `T ± i`: a symmetric, densely-defined operator `T` for
> which `T + I • 1` and `T - I • 1` both have full range is self-adjoint.

```lean
lemma IsSymmetric.isSelfAdjoint_of_range_eq_top [CompleteSpace H] (hsym : T.IsSymmetric)
    (hdense : T.HasDenseDomain)
    (hadd : (T + I • 1).toFun.range = ⊤) (hsub : (T - I • 1).toFun.range = ⊤) :
    IsSelfAdjoint T
```

## Depends on

- [LinearPMap](../../mathematics/formathlib/part-01/linearpmap.md)

## Proof depends on

- [Submodules of `E × F`](../../mathematics/innerproductspace/submodule.md)

## Sources

- [Physlib/QuantumMechanics/Operators/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/QuantumMechanics/Operators/Basic.lean)
