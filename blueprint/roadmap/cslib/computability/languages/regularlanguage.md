---
catalog: module
lean: Cslib.Language.IsRegular.iff_dfa, Cslib.Language.IsRegular.iff_nfa, Cslib.Language.IsRegular.iff_epsilon_nfa, Cslib.Language.IsRegular.compl, Cslib.Language.IsRegular.iff_twoWayNA, Cslib.Language.IsRegular.zero, Cslib.Language.IsRegular.one, Cslib.Language.IsRegular.top, Cslib.Language.IsRegular.inf, Cslib.Language.IsRegular.add, Cslib.Language.IsRegular.iInf, Cslib.Language.IsRegular.iSup, Cslib.Language.IsRegular.mul, Cslib.Language.IsRegular.kstar, Cslib.Language.IsRegular.congr_fin_index, Cslib.Language.IsRegular.reverse, Cslib.Language.IsRegular.reverse_iff, Cslib.Language.IsRegular.preimage, Cslib.Language.IsRegular.char, Cslib.Language.IsRegular.regex, Cslib.Language.IsRegular.iff_regex
statement: formalized
proof: formalized
---

# Regular languages

`Cslib.Computability.Languages.RegularLanguage`, in [Cslib/Computability/Languages/RegularLanguage.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean), by Ching-Tsun Chou.

`Cslib.Language.IsRegular.iff_dfa` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L38))

> A characterization of `Language.IsRegular` in terms of `DA`. This is the only theorem in Cslib
> in which Mathlib's definition of `Language.IsRegular` is used.

```lean
theorem IsRegular.iff_dfa {l : Language Symbol} :
    l.IsRegular ↔ ∃ State : Type, ∃ _ : Finite State,
      ∃ dfa : DA.FinAcc State Symbol, language dfa = l
```

`Cslib.Language.IsRegular.iff_nfa` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L52))

> A characterization of Language.IsRegular in terms of NA.

```lean
theorem IsRegular.iff_nfa {l : Language Symbol} :
    l.IsRegular ↔ ∃ State : Type, ∃ _ : Finite State,
      ∃ nfa : NA.FinAcc State Symbol, language nfa = l
```

`Cslib.Language.IsRegular.iff_epsilon_nfa` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L64))

> A characterization of `Language.IsRegular` in terms of `εNA`.

```lean
theorem IsRegular.iff_epsilon_nfa {l : Language Symbol} :
    l.IsRegular ↔ ∃ State : Type, ∃ _ : Finite State,
      ∃ enfa : εNA.FinAcc State Symbol, language enfa = l
```

`Cslib.Language.IsRegular.compl` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L75))

> The complementation of a regular language is regular.

```lean
theorem IsRegular.compl {l : Language Symbol} (h : l.IsRegular) : (lᶜ).IsRegular
```

`Cslib.Language.IsRegular.iff_twoWayNA` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L87))

> A language is regular if and only if it is accepted by some two-way nondeterministic
> automaton with finitely many states.

```lean
theorem IsRegular.iff_twoWayNA {l : Language Symbol} :
    l.IsRegular ↔ ∃ State : Type, ∃ _ : Finite State,
      ∃ a : TwoWayNA State Symbol, language a = l
```

`Cslib.Language.IsRegular.zero` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L104))

> The empty language is regular.

```lean
theorem IsRegular.zero : (0 : Language Symbol).IsRegular
```

`Cslib.Language.IsRegular.one` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L116))

> The language containing only the empty word is regular.

```lean
theorem IsRegular.one : (1 : Language Symbol).IsRegular
```

`Cslib.Language.IsRegular.top` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L130))

> The language of all finite words is regular.

```lean
theorem IsRegular.top : (⊤ : Language Symbol).IsRegular
```

`Cslib.Language.IsRegular.inf` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L136))

> The intersection of two regular languages is regular.

```lean
theorem IsRegular.inf {l1 l2 : Language Symbol}
    (h1 : l1.IsRegular) (h2 : l2.IsRegular) : (l1 ⊓ l2).IsRegular
```

`Cslib.Language.IsRegular.add` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L148))

> The union of two regular languages is regular.

```lean
theorem IsRegular.add {l1 l2 : Language Symbol}
    (h1 : l1.IsRegular) (h2 : l2.IsRegular) : (l1 + l2).IsRegular
```

`Cslib.Language.IsRegular.iInf` (theorem, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L160))

> The intersection of any finite number of regular languages is regular.

```lean
theorem IsRegular.iInf {I : Type*} [Finite I] {s : Set I} {l : I → Language Symbol}
    (h : ∀ i ∈ s, (l i).IsRegular) : (⨅ i ∈ s, l i).IsRegular
```

`Cslib.Language.IsRegular.iSup` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L172))

> The union of any finite number of regular languages is regular.

```lean
theorem IsRegular.iSup {I : Type*} [Finite I] {s : Set I} {l : I → Language Symbol}
    (h : ∀ i ∈ s, (l i).IsRegular) : (⨆ i ∈ s, l i).IsRegular
```

`Cslib.Language.IsRegular.mul` (theorem, [line 187](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L187))

> The concatenation of two regular languages is regular.

```lean
theorem IsRegular.mul {l1 l2 : Language Symbol}
    (h1 : l1.IsRegular) (h2 : l2.IsRegular) : (l1 * l2).IsRegular
```

`Cslib.Language.IsRegular.kstar` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L196))

> The Kleene star of a regular language is regular.

```lean
theorem IsRegular.kstar {l : Language Symbol}
    (h : l.IsRegular) : (l∗).IsRegular
```

`Cslib.Language.IsRegular.congr_fin_index` (theorem, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L205))

> If a right congruence is of finite index, then each of its equivalence classes is regular.

```lean
theorem IsRegular.congr_fin_index {Symbol : Type}
    [c : RightCongruence Symbol] [Finite (Quotient c.eq)]
    (a : Quotient c.eq) : (eqvCls a).IsRegular
```

`Cslib.Language.IsRegular.reverse` (theorem, [line 214](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L214))

> The reversal of a regular language is regular.

```lean
theorem IsRegular.reverse {l : Language Symbol} (h : l.IsRegular) : l.reverse.IsRegular
```

`Cslib.Language.IsRegular.reverse_iff` (theorem, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L221))

> A language is regular iff its reversal is regular.

```lean
theorem IsRegular.reverse_iff {l : Language Symbol} : l.reverse.IsRegular ↔ l.IsRegular
```

`Cslib.Language.IsRegular.preimage` (theorem, [line 229](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L229))

> The preimage of a regular languge under a language homomorphism is regular.

```lean
theorem IsRegular.preimage (f : Hom Symbol' Symbol) {l : Language Symbol} (h : l.IsRegular) :
    (l.preimage f).IsRegular
```

`Cslib.Language.IsRegular.char` (theorem, [line 237](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L237))

> The language containing only the one character string `a` is regular.

```lean
theorem IsRegular.char (a : Symbol) : ({[a]} : Language Symbol).IsRegular
```

`Cslib.Language.IsRegular.regex` (theorem, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L242))

> Languages matching regular expressions are regular.

```lean
theorem IsRegular.regex (r : RegularExpression Symbol) : r.matches'.IsRegular
```

`Cslib.Language.IsRegular.iff_regex` (theorem, [line 247](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean#L247))

> A characterization of `Language.IsRegular` in terms of `RegularExpression`.

```lean
theorem IsRegular.iff_regex [Finite Symbol] {l : Language Symbol} :
    l.IsRegular ↔ ∃ r : RegularExpression Symbol, l = matches' r
```

## Depends on

- [Deterministic Automata](../automata/da/basic.md)
- [Nondeterministic automata with ε-transitions](../automata/epsilonna/basic.md)
- [Nondeterministic Two-Way Automaton](../automata/twowayna/basic.md)
- [Right Congruence](congruences/basic.md)
- [Language homomorphism](languagehom.md)

## Proof depends on

- [Deterministic automaton corresponding to a right congruence](../automata/da/congr.md)
- [Product of deterministic automata](../automata/da/prod.md)
- [Translation of Deterministic Automata into Nonodeterministic Automata](../automata/da/tona.md)
- [The ε-NA of a regular expression](../automata/epsilonna/ofregularexpression.md)
- [Translation of εNA into NA](../automata/epsilonna/tona.md)
- [Preimage construction on nondeterministic automata](../automata/na/preimage.md)
- [Reversal of nondeterministic automata](../automata/na/reverse.md)
- [Translation of Nondeterministic Automata for finite strings into Deterministic Automata](../automata/na/toda.md)
- [Translation of Nondeterministic Automata into Nondeterministic Automata with ε-transitions](../automata/na/toepsilonna.md)
- [A finite acceptor for the complement of the language of a two-way automaton](../automata/twowayna/compltona.md)
- [Finite acceptors as two-way automata](../automata/twowayna/ofna.md)
- [Kleene's Algorithm](kleenealgorithm.md)

## Sources

- [Cslib/Computability/Languages/RegularLanguage.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/RegularLanguage.lean)
