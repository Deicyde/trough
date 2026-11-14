---
catalog: module
lean: Cslib.ωLanguage.IsSafety, Cslib.ωLanguage.isSafety_iff, Cslib.ωLanguage.IsLiveness, Cslib.ωLanguage.isLiveness_iff, Cslib.ωLanguage.isSafety_closure, Cslib.ωLanguage.isLiveness_sup_compl_closure, Cslib.ωLanguage.exists_safetyLivenessDecomposition
statement: formalized
proof: formalized
---

# Safety and Liveness properties of ω-sequences

`Cslib.Computability.Languages.SafetyLiveness`, in [Cslib/Computability/Languages/SafetyLiveness.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean), by Ching-Tsun Chou.

> This file formalizes the main results of [AlpernSchneider1985].  Namely, given
> an appropriate topology on ω-sequences:
> * Safety properties can be identified with closed sets.
> * Liveness properties can be identified with dense sets.
> * Every property is the intersection of a safety property and a liveness property.
>
> ## References
> * [Alpern, Bowen; Schneider, Fred B. (1985). "Defining liveness".
> Information Processing Letters. 21 (4): 181–185.][AlpernSchneider1985]

`Cslib.ωLanguage.IsSafety` (abbreviation, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean#L35))

> Safety properties are identified with closed sets.

```lean
abbrev IsSafety (p : ωLanguage α) : Prop
```

`Cslib.ωLanguage.isSafety_iff` (theorem, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean#L40))

> An alternative characterization of `IsSafety` that justifies its definition:
> if an ω-sequence violates a safety property, then it has a finite prefix all of whose
> infinite extensions also violate the property.

```lean
theorem isSafety_iff (p : ωLanguage α) :
    p.IsSafety ↔ ∀ xs, xs ∉ p → ∃ n, ∀ ys, (xs.take n) ++ω ys ∉ p
```

`Cslib.ωLanguage.IsLiveness` (abbreviation, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean#L45))

> Liveness properties are identified with dense sets.

```lean
abbrev IsLiveness (p : ωLanguage α) : Prop
```

`Cslib.ωLanguage.isLiveness_iff` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean#L49))

> An alternative characterization of `IsLiveness` that justifies its definition:
> any finite sequence can be extended to an infinite sequence satisfying a liveness property.

```lean
theorem isLiveness_iff (p : ωLanguage α) :
    p.IsLiveness ↔ ∀ (xs : ωSequence α) (n : ℕ), ∃ ys, (xs.take n) ++ω ys ∈ p
```

`Cslib.ωLanguage.isSafety_closure` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean#L54))

> `p.closure` is always a safety property for any ω-language `p`.

```lean
theorem isSafety_closure (p : ωLanguage α) :
    p.closure.IsSafety
```

`Cslib.ωLanguage.isLiveness_sup_compl_closure` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean#L59))

> `p ⊔ p.closureᶜ` is always a liveness property for any ω-language `p`.

```lean
theorem isLiveness_sup_compl_closure (p : ωLanguage α) :
    (p ⊔ p.closureᶜ).IsLiveness
```

`Cslib.ωLanguage.exists_safetyLivenessDecomposition` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean#L66))

> Every property `p` is the intersection of a safety property (namely, `p.closure`) and
> a liveness property (namely, `p ⊔ p.closureᶜ`).

```lean
theorem exists_safetyLivenessDecomposition (p : ωLanguage α) :
    ∃ q r : ωLanguage α, q.IsSafety ∧ r.IsLiveness ∧ p = q ⊓ r
```

## Depends on

- [ωLanguage](omegalanguage.md)

## Sources

- [Cslib/Computability/Languages/SafetyLiveness.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SafetyLiveness.lean)
