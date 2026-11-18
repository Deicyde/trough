---
catalog: module
lean: Language.Congruence.toCon, Language.SyntacticMonoid, Language.homSyntacticMonoid, Language.syntacticMonoidEquivMyhillQuotient, Language.IsRegular.iff_finite_syntacticMonoid, Language.homSyntacticMonoid_iff_myhillCongruence, Language.IsRegular.exists_finite_monoid, Language.inducedCongr, Language.inducedCongr_ofList, Language.IsRegular.of_finite_monoid_singleton, Language.IsRegular.of_finite_monoid, Language.IsRegular.iff_finite_monoid
statement: formalized
proof: formalized
---

# Syntactic monoid

`Cslib.Computability.Languages.SyntacticMonoid`, in [Cslib/Computability/Languages/SyntacticMonoid.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean), by Ching-Tsun Chou.

> This file has two main results:
> (1) We define the syntactic monoid of a language `l` and show that `l` is regular
> if and only if its syntactic monoid is finite.
> (2) Using (1), we show that a language is regular if and only if it is the preimage of a subset
> of a finite monoid `M` under a monoid homomorphism from the free monoid on its alphabet to `M`
>
> ## References
>
> [Holcombe1982] Holcombe, W.M.L. (1982). Algebraic automata theory. Section 5.3

`Language.Congruence.toCon` (definition, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L34))

> Converting a (two-sided) congruence `c` on finite words to a congruence relation
> on the (multiplicative) free monoid.

```lean
def Congruence.toCon [c : Congruence α] : Con (FreeMonoid α)
```

`Language.SyntacticMonoid` (abbreviation, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L46))

> The syntactic monoid of a language `l` is the quotient of the free monoid
> by the Myhill congruence of `l`.

```lean
abbrev SyntacticMonoid (l : Language α)
```

`Language.homSyntacticMonoid` (abbreviation, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L50))

> The natural homomorphism from `FreeMonoid α` to `l.SyntacticMonoid` induced
> by the Myhill congruence of `l`.

```lean
abbrev homSyntacticMonoid (l : Language α)
```

`Language.syntacticMonoidEquivMyhillQuotient` (definition, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L54))

> The syntactic monoid of a language `l` and its Myhill quotient are the quotients of
> `FreeMonoid α` and of `List α` by the same relation, hence in bijection.

```lean
def syntacticMonoidEquivMyhillQuotient (l : Language α) :
    l.SyntacticMonoid ≃ l.MyhillQuotient
```

`Language.IsRegular.iff_finite_syntacticMonoid` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L59))

> A language `l` is regular if and only if its syntactic monoid is finite.

```lean
theorem IsRegular.iff_finite_syntacticMonoid (l : Language α) :
    l.IsRegular ↔ Finite (l.SyntacticMonoid)
```

`Language.homSyntacticMonoid_iff_myhillCongruence` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L65))

> The congruence induced by `homSyntacticMonoid` is exactly the Myhill congruence.

```lean
theorem homSyntacticMonoid_iff_myhillCongruence {l : Language α} {x y : List α} :
    l.homSyntacticMonoid (ofList x) = l.homSyntacticMonoid (ofList y) ↔
    l.MyhillCongruence.eq x y
```

`Language.IsRegular.exists_finite_monoid` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L73))

> Any regular language is the preimage of a subset of a finite monoid `M`
> under a monoid homomorphism from the free monoid on its alphabet to `M`.

```lean
theorem IsRegular.exists_finite_monoid {l : Language α} (h : l.IsRegular) :
    ∃ M : Type, ∃ _ : Monoid M, ∃ _ : Finite M, ∃ f : FreeMonoid α →* M, ∃ s : Set M,
    (f ∘ ofList) ⁻¹' s = l
```

`Language.inducedCongr` (definition, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L94))

> Given a monoid homomorphism `f` from `FreeMonoid α` to another monoid `M`,
> `inducedCongr f` is the language congruence induced by `f`.

```lean
def inducedCongr : RightCongruence α
```

`Language.inducedCongr_ofList` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L104))

```lean
theorem inducedCongr_ofList (x : List α) :
    (f ∘ ofList) ⁻¹' {(f ∘ ofList) x} = (inducedCongr f).eqvCls ⟦ x ⟧
```

`Language.IsRegular.of_finite_monoid_singleton` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L111))

> The preimage of a singleton in a finite monoid `M` under a monoid homomorphism
> from the free monoid to `M` is regular.

```lean
theorem IsRegular.of_finite_monoid_singleton [Finite M]
    (m : M) : IsRegular ((f ∘ ofList) ⁻¹' {m})
```

`Language.IsRegular.of_finite_monoid` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L122))

> The preimage of a subset of a finite monoid `M` under a monoid homomorphism
> from the free monoid to `M` is regular.

```lean
theorem IsRegular.of_finite_monoid [Finite M]
    (s : Set M) : IsRegular ((f ∘ ofList) ⁻¹' s)
```

`Language.IsRegular.iff_finite_monoid` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean#L134))

> A language is regular if and only if it is the preimage of a subset of a finite monoid `M`
> under a monoid homomorphism from the free monoid on its alphabet to `M`.

```lean
theorem IsRegular.iff_finite_monoid {l : Language α} :
    l.IsRegular ↔
    ∃ M : Type, ∃ _ : Monoid M, ∃ _ : Finite M, ∃ f : FreeMonoid α →* M, ∃ s : Set M,
    (f ∘ ofList) ⁻¹' s = l
```

## Depends on

- [Myhill congruence](congruences/myhillcongruence.md)

## Sources

- [Cslib/Computability/Languages/SyntacticMonoid.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/SyntacticMonoid.lean)
