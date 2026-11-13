---
declaration: module
origin: cited
lean: ProbabilisticTheory.Operation, ProbabilisticTheory.Operation.ext, ProbabilisticTheory.Operation.map_nonneg, ProbabilisticTheory.Operation.apply_one_le_one, ProbabilisticTheory.Operation.IsNormal, ProbabilisticTheory.Operation.id, ProbabilisticTheory.Operation.id_apply, ProbabilisticTheory.Operation.isNormal_id
statement: formalized
proof: formalized
---

# Operations

The module `PhyslibAlpha.ProbabilisticTheory.Channel.Operation`, [PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean): 21 declarations (1 instance with no name), 14 with a docstring.

> Operations: positive maps with op 1 ≤ 1, their outcome effects and conditioned states.

## i. Overview

> An operation is a positive linear map `op` with `op 1 ≤ 1`. It describes how a system changes when
> one particular outcome of a measurement occurs, and it may lose probability, but never gain any. A
> channel is an operation with `op 1 = 1`, and a finite family of operations whose values on `1` sum
> to `1` is an instrument.

## ii. Key results

> - `Operation` : operations.
> - `Operation.comp` : composition of operations.
> - `Operation.outcomeEffect` : the effect `op 1` of the outcome.
> - `Operation.condition` : the state after the outcome, normalized.

## iv. References

> * None.

## A. Operations

**`ProbabilisticTheory.Operation`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L53).

> An operation on `E`: a positive linear endomorphism that never sends the certain event above
> itself.

```lean
def Operation (E : Type*) [OrderUnitSpace E]
```

**An instance with no name**, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L59).

> Regard an operation as its underlying positive linear map.

```lean
instance : CoeFun (Operation E) (fun _ => E → E)
```

**`ProbabilisticTheory.Operation.ext`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L62).

```lean
lemma ext {op₁ op₂ : Operation E} (h : ∀ x, op₁ x = op₂ x) : op₁ = op₂
```

**`ProbabilisticTheory.Operation.map_nonneg`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L66).

> An operation never sends a possible outcome to something negative.

```lean
lemma map_nonneg (op : Operation E) {x : E} (hx : 0 ≤ x) : 0 ≤ op x
```

**`ProbabilisticTheory.Operation.apply_one_le_one`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L70).

> An operation never sends the certain event above itself.

```lean
lemma apply_one_le_one (op : Operation E) : op 1 ≤ 1
```

**`ProbabilisticTheory.Operation.IsNormal`**, an abbrev, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L75).

> Normality for operations is inherited from the single canonical normal-positive-map
> predicate.  It is intentionally not a second directed-supremum definition.

```lean
abbrev IsNormal (op : Operation E) : Prop
```

**`ProbabilisticTheory.Operation.id`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L78).

> The identity operation.

```lean
def id : Operation E
```

**`ProbabilisticTheory.Operation.id_apply`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L81).

```lean
lemma id_apply (x : E) : id (E := E) x = x
```

**`ProbabilisticTheory.Operation.isNormal_id`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L84).

> The identity operation is normal.

```lean
lemma isNormal_id : (id (E := E)).IsNormal
```

**`ProbabilisticTheory.Operation.comp`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L88).

> Sequential composition of operations.  Applying `φ` and then `ψ` is again subunital:
> positivity makes `ψ` monotone, so `φ(1) ≤ 1` implies `ψ(φ(1)) ≤ ψ(1) ≤ 1`.

```lean
def comp (ψ φ : Operation E) : Operation E
```

**`ProbabilisticTheory.Operation.comp_apply`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L92).

```lean
lemma comp_apply (ψ φ : Operation E) (x : E) : ψ.comp φ x = ψ (φ x)
```

**`ProbabilisticTheory.Operation.id_comp`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L95).

```lean
lemma id_comp (φ : Operation E) : id.comp φ = φ
```

**`ProbabilisticTheory.Operation.comp_id`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L101).

```lean
lemma comp_id (φ : Operation E) : φ.comp id = φ
```

**`ProbabilisticTheory.Operation.comp_assoc`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L106).

```lean
lemma comp_assoc (χ ψ φ : Operation E) : (χ.comp ψ).comp φ = χ.comp (ψ.comp φ)
```

**`ProbabilisticTheory.Operation.IsNormal.comp`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L113).

> Normal operations are closed under sequential composition, by the canonical positive-map
> normality composition theorem.

```lean
lemma IsNormal.comp {φ ψ : Operation E} (hφ : φ.IsNormal) (hψ : ψ.IsNormal) :
    (ψ.comp φ).IsNormal
```

**`ProbabilisticTheory.Operation.condition`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L120).

> Normalize the pullback of a state along an operation whose outcome has nonzero probability.
> This is the common post-measurement state construction: instruments and Jordan Lüders operations
> specialize it instead of maintaining parallel normalizations.

```lean
noncomputable def condition (op : Operation E) (ω : 𝓢[ℝ, E])
    (hmass : 0 < ω (op 1)) : 𝓢[ℝ, E]
```

**`ProbabilisticTheory.Operation.condition_apply`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L133).

> Pointwise formula for the state conditioned by an operation.

```lean
lemma condition_apply (op : Operation E) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω (op 1)) (x : E) :
    op.condition ω hmass x = (ω (op 1))⁻¹ * ω (op x)
```

**`ProbabilisticTheory.Operation.condition_one`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L138).

> A normalized operational conditional state preserves the order unit.

```lean
lemma condition_one (op : Operation E) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω (op 1)) :
    op.condition ω hmass 1 = 1
```

**`ProbabilisticTheory.Operation.condition_isNormal`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L145).

> Conditioning a normal state by a normal operation preserves normality.  The unnormalized
> functional is the composite of two normal positive maps; division by the strictly positive
> outcome probability transports directed suprema through multiplication by a positive scalar.

```lean
lemma condition_isNormal (op : Operation E) (ω : 𝓢[ℝ, E]) (hmass : 0 < ω (op 1))
    (hop : op.IsNormal) (hω : ω.IsNormal) : (op.condition ω hmass).IsNormal
```

## B. Outcome effects

**`ProbabilisticTheory.Operation.outcomeEffect`**, a def, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L167).

> The image of the certain event under an operation, as an effect: the probability of the
> operation actually "firing" in a given state.

```lean
def outcomeEffect (op : Operation E) : Effect E
```

**`ProbabilisticTheory.Operation.coe_outcomeEffect`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean#L171).

```lean
lemma coe_outcomeEffect (op : Operation E) : (outcomeEffect op : E) = op 1
```

## Depends on

- [Effects](../../../physlib/probabilistictheory/effect/basic.md)
- [Normal channels](normal.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Channel/Operation.lean)
