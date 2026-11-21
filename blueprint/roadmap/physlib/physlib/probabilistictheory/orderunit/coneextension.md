---
declaration: module
origin: cited
lean: ProbabilisticTheory.PosCone.extend, ProbabilisticTheory.PosCone.extend_sub, ProbabilisticTheory.PosCone.extend_add, ProbabilisticTheory.PosCone.extend_smul, ProbabilisticTheory.PosCone.extendₗ, ProbabilisticTheory.PosCone.extendₗ_apply, ProbabilisticTheory.PosCone.extend_coe, ProbabilisticTheory.PosCone.extendₗ_unique
statement: formalized
proof: formalized
---

# Linear extension from positive observables

The module `Physlib.ProbabilisticTheory.OrderUnit.ConeExtension`, [Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean): 8 declarations, 8 with a docstring.

> Values on positive observables determine a real-linear functional on all observables.

## i. Overview

> Every observable is a difference `p - q` of two positive observables. A map `f` that is additive
> and nonnegatively homogeneous on positive observables extends to all observables by sending
> `p - q` to `f p - f q`. The value does not depend on the chosen decomposition. The extension is
> real-linear and it is the only real-linear map that agrees with `f` on positive observables.

## ii. Key results

> - `PosCone.extend` : extend a real-valued map from positive observables.
> - `PosCone.extend_sub` : the extension sends every difference `p - q` to `f p - f q`.
> - `PosCone.extendₗ` : the extension as a real-linear map.
> - `PosCone.extendₗ_unique` : uniqueness among real-linear maps with those values.

## iv. References

## A. The extension

**`ProbabilisticTheory.PosCone.extend`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L52).

> Extend values on positive observables by `f (p - q) = f p - f q`, for a chosen decomposition
> of each observable into positive parts.

```lean
noncomputable def extend (A : P.Observables) : ℝ
```

**`ProbabilisticTheory.PosCone.extend_sub`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L56).

> The extension gives `f p - f q` for every decomposition `A = p - q`.

```lean
lemma extend_sub {A : P.Observables} {p q : PosCone P} (h : (p : P.Observables) - q = A) :
    extend f A = f p - f q
```

## B. Linearity

**`ProbabilisticTheory.PosCone.extend_add`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L66).

> The extension is additive.

```lean
lemma extend_add (A B : P.Observables) : extend f (A + B) = extend f A + extend f B
```

**`ProbabilisticTheory.PosCone.extend_smul`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L74).

> The extension is homogeneous for every real scalar.

```lean
lemma extend_smul (t : ℝ) (A : P.Observables) : extend f (t • A) = t * extend f A
```

**`ProbabilisticTheory.PosCone.extendₗ`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L86).

> The extension as a real-linear map.

```lean
noncomputable def extendₗ : P.Observables →ₗ[ℝ] ℝ
```

## C. Agreement and uniqueness

**`ProbabilisticTheory.PosCone.extendₗ_apply`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L95).

> The linear extension evaluates as the extension.

```lean
lemma extendₗ_apply (A : P.Observables) : extendₗ f A = extend f A
```

**`ProbabilisticTheory.PosCone.extend_coe`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L99).

> The extension agrees with `f` on positive observables.

```lean
lemma extend_coe (p : PosCone P) : extend f (p : P.Observables) = f p
```

**`ProbabilisticTheory.PosCone.extendₗ_unique`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean#L103).

> Agreement on positive observables determines the real-linear extension.

```lean
lemma extendₗ_unique (g : P.Observables →ₗ[ℝ] ℝ)
    (h : ∀ p : PosCone P, g (p : P.Observables) = f p) : g = extendₗ f
```

## Depends on

- [Ordered positive cones (Physlib)](cone.md)

## Sources

- [Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/OrderUnit/ConeExtension.lean)
