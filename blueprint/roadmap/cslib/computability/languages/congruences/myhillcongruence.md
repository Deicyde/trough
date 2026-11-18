---
catalog: module
lean: Language.MyhillCongruence, Language.MyhillQuotient, Language.nerodeMap, Language.nerodeMap_append, Language.nerodeMap_accept, Language.myhillCongruence_iff, Language.IsRegular.finite_myhillQuotient, Language.myhillCongruenceDA, Language.myhillCongruenceDA_language_eq, Language.IsRegular.iff_finite_myhillQuotient
statement: formalized
proof: formalized
---

# Myhill congruence

`Cslib.Computability.Languages.Congruences.MyhillCongruence`, in [Cslib/Computability/Languages/Congruences/MyhillCongruence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean), by Ching-Tsun Chou.

> The Myhill congruence of a language `l` is a two-sided congruence that is finer than
> the Nerode congruence of the same language `l` (which is a right congruence).  It will be
> used to define the syntactic monoid of `l`.
>
> ## References
>
> [Holcombe1982] Holcombe, W.M.L. (1982). Algebraic automata theory. Section 5.3

`Language.MyhillCongruence` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L35))

> The Myhill congruence of a language `l` is the two-sided congruence on finite words
> such that two words are related iff all their two-sided extensions are either both in `l`
> or both not in `l`.

```lean
def MyhillCongruence (l : Language α) : Congruence α
```

`Language.MyhillQuotient` (abbreviation, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L44))

> The Myhill quotient of a language `l` is the quotient of its Myhill congruence.

```lean
abbrev MyhillQuotient (l : Language α)
```

`Language.nerodeMap` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L48))

> Given a language `l` and a finite word `x`, the Nerode map is a map from the Nerode quotient
> to itself induced by the `x`-transition of the Nerode congruence deterministic automaton of `l`.

```lean
def nerodeMap (l : Language α) (x : List α) : l.NerodeQuotient → l.NerodeQuotient
```

`Language.nerodeMap_append` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L51))

```lean
theorem nerodeMap_append (l : Language α) (x y : List α) :
    l.nerodeMap (x ++ y) = l.nerodeMap y ∘ l.nerodeMap x
```

`Language.nerodeMap_accept` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L56))

```lean
theorem nerodeMap_accept (l : Language α) (x : List α) :
    x ∈ l ↔ l.nerodeMap x l.NerodeCongruenceDA.start ∈ l.NerodeCongruenceDA.accept
```

`Language.myhillCongruence_iff` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L62))

> The Myhill congruence is in fact the congruence induced by the Nerode map.

```lean
theorem myhillCongruence_iff (l : Language α) (x y : List α) :
    l.MyhillCongruence.r x y ↔ l.nerodeMap x = l.nerodeMap y
```

`Language.IsRegular.finite_myhillQuotient` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L73))

> The Myhill quotient of a regular language is finite.

```lean
theorem IsRegular.finite_myhillQuotient {l : Language α}
    (h : l.IsRegular) : Finite (l.MyhillQuotient)
```

`Language.myhillCongruenceDA` (definition, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L84))

> The deterministic automaton corresponding to the Myhill congruence of a language `l`.

```lean
def myhillCongruenceDA (l : Language α) : DA.FinAcc (l.MyhillQuotient) α
```

`Language.myhillCongruenceDA_language_eq` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L89))

> The deterministic automaton corresponding to the Myhill congruence of a language `l`
> accepts the same language `l`.

```lean
theorem myhillCongruenceDA_language_eq (l : Language α) :
    language (l.myhillCongruenceDA) = l
```

`Language.IsRegular.iff_finite_myhillQuotient` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean#L104))

> A language is regular if and only if its Myhill quotient is finite.

```lean
theorem IsRegular.iff_finite_myhillQuotient (l : Language α) :
    l.IsRegular ↔ Finite (l.MyhillQuotient)
```

## Depends on

- [Myhill-Nerode Theorem](../myhillnerode.md)

## Sources

- [Cslib/Computability/Languages/Congruences/MyhillCongruence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/MyhillCongruence.lean)
