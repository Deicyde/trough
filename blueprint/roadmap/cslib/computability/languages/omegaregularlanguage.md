---
catalog: module
lean: Cslib.ωLanguage.IsRegular, Cslib.ωLanguage.isRegular_iff, Cslib.ωLanguage.IsRegular.of_da_buchi, Cslib.ωLanguage.IsRegular.not_da_buchi, Cslib.ωLanguage.IsRegular.regular_omegaLim, Cslib.ωLanguage.IsRegular.bot, Cslib.ωLanguage.IsRegular.top, Cslib.ωLanguage.IsRegular.sup, Cslib.ωLanguage.IsRegular.inf, Cslib.ωLanguage.IsRegular.iSup, Cslib.ωLanguage.IsRegular.iInf, Cslib.ωLanguage.IsRegular.hmul, Cslib.ωLanguage.IsRegular.omegaPow, Cslib.ωLanguage.IsRegular.eq_fin_iSup_hmul_omegaPow, Cslib.ωLanguage.IsRegular.fin_cover_saturates, Cslib.ωLanguage.IsRegular.fin_cover_saturates_compl, Cslib.ωLanguage.IsRegular.compl
statement: formalized
proof: formalized
---

# ω-Regular languages

`Cslib.Computability.Languages.OmegaRegularLanguage`, in [Cslib/Computability/Languages/OmegaRegularLanguage.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean), by Ching-Tsun Chou.

> This file defines ω-regular languages and proves some properties of them.

`Cslib.ωLanguage.IsRegular` (definition, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L37))

> An ω-language is ω-regular iff it is accepted by a
> finite-state nondeterministic Buchi automaton.

```lean
def IsRegular (p : ωLanguage Symbol)
```

`Cslib.ωLanguage.isRegular_iff` (theorem, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L51))

> The state space of the accepting finite-state nondeterministic Buchi automaton
> can in fact be universe-polymorphic.

```lean
theorem isRegular_iff {p : ωLanguage Symbol} :
    p.IsRegular ↔ ∃ (σ : Type v) (_ : Finite σ) (na : NA.Buchi σ Symbol), language na = p
```

`Cslib.ωLanguage.IsRegular.of_da_buchi` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L56))

> The ω-language accepted by a finite-state deterministic Buchi automaton is ω-regular.

```lean
theorem IsRegular.of_da_buchi {State : Type} [Finite State] (da : DA.Buchi State Symbol) :
    (language da).IsRegular
```

`Cslib.ωLanguage.IsRegular.not_da_buchi` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L62))

> There is an ω-regular language that is not accepted by any deterministic Buchi automaton,
> where the automaton is not even required to be finite-state.

```lean
theorem IsRegular.not_da_buchi :
  ∃ (Symbol : Type) (p : ωLanguage Symbol), p.IsRegular ∧
    ¬ ∃ (State : Type) (da : DA.Buchi State Symbol), language da = p
```

`Cslib.ωLanguage.IsRegular.regular_omegaLim` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L74))

> The ω-limit of a regular language is ω-regular.

```lean
theorem IsRegular.regular_omegaLim {l : Language Symbol}
    (h : l.IsRegular) : (l↗ω).IsRegular
```

`Cslib.ωLanguage.IsRegular.bot` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L82))

> The empty language is ω-regular.

```lean
theorem IsRegular.bot : (⊥ : ωLanguage Symbol).IsRegular
```

`Cslib.ωLanguage.IsRegular.top` (theorem, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L94))

> The language of all ω-sequences is ω-regular.

```lean
theorem IsRegular.top : (⊤ : ωLanguage Symbol).IsRegular
```

`Cslib.ωLanguage.IsRegular.sup` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L110))

> The union of two ω-regular languages is ω-regular.

```lean
theorem IsRegular.sup {p1 p2 : ωLanguage Symbol}
    (h1 : p1.IsRegular) (h2 : p2.IsRegular) : (p1 ⊔ p2).IsRegular
```

`Cslib.ωLanguage.IsRegular.inf` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L131))

> The intersection of two ω-regular languages is ω-regular.

```lean
theorem IsRegular.inf {p1 p2 : ωLanguage Symbol}
    (h1 : p1.IsRegular) (h2 : p2.IsRegular) : (p1 ⊓ p2).IsRegular
```

`Cslib.ωLanguage.IsRegular.iSup` (theorem, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L151))

> The union of any finite number of ω-regular languages is ω-regular.

```lean
theorem IsRegular.iSup {I : Type*} [Finite I] {s : Set I} {p : I → ωLanguage Symbol}
    (h : ∀ i ∈ s, (p i).IsRegular) : (⨆ i ∈ s, p i).IsRegular
```

`Cslib.ωLanguage.IsRegular.iInf` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L165))

> The intersection of any finite number of ω-regular languages is ω-regular.

```lean
theorem IsRegular.iInf {I : Type*} [Finite I] {s : Set I} {p : I → ωLanguage Symbol}
    (h : ∀ i ∈ s, (p i).IsRegular) : (⨅ i ∈ s, p i).IsRegular
```

`Cslib.ωLanguage.IsRegular.hmul` (theorem, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L179))

> The concatenation of a regular language and an ω-regular language is ω-regular.

```lean
theorem IsRegular.hmul {l : Language Symbol} {p : ωLanguage Symbol}
    (h1 : l.IsRegular) (h2 : p.IsRegular) : (l * p).IsRegular
```

`Cslib.ωLanguage.IsRegular.omegaPow` (theorem, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L188))

> The ω-power of a regular language is an ω-regular language.

```lean
theorem IsRegular.omegaPow [Inhabited Symbol] {l : Language Symbol}
    (h : l.IsRegular) : (l^ω).IsRegular
```

`Cslib.ωLanguage.IsRegular.eq_fin_iSup_hmul_omegaPow` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L196))

> An ω-language is regular iff it is the finite union of ω-languages of the form `L * M^ω`,
> where all `L`s and `M`s are regular languages.

```lean
theorem IsRegular.eq_fin_iSup_hmul_omegaPow [Inhabited Symbol] (p : ωLanguage Symbol) :
    p.IsRegular ↔ ∃ n : ℕ, ∃ l m : Fin n → Language Symbol,
      (∀ i, (l i).IsRegular ∧ (m i).IsRegular) ∧ p = ⨆ i, (l i) * (m i)^ω
```

`Cslib.ωLanguage.IsRegular.fin_cover_saturates` (theorem, [line 225](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L225))

> If an ω-language has a finite saturating cover made of ω-regular languages,
> then it is an ω-regular language.

```lean
theorem IsRegular.fin_cover_saturates {I : Type*} [Finite I]
    {p : I → ωLanguage Symbol} {q : ωLanguage Symbol}
    (hs : Saturates (fun i ↦ (p i).toSet) q.toSet)
    (hc : ⨆ i, p i = ⊤) (hr : ∀ i, (p i).IsRegular) : q.IsRegular
```

`Cslib.ωLanguage.IsRegular.fin_cover_saturates_compl` (theorem, [line 241](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L241))

> If an ω-language has a finite saturating cover made of ω-regular languages,
> then its complement is an ω-regular language.

```lean
theorem IsRegular.fin_cover_saturates_compl {I : Type*} [Finite I]
    {p : I → ωLanguage Symbol} {q : ωLanguage Symbol}
    (hs : Saturates (fun i ↦ (p i).toSet) q.toSet)
    (hc : ⨆ i, p i = ⊤) (hr : ∀ i, (p i).IsRegular) : (qᶜ).IsRegular
```

`Cslib.ωLanguage.IsRegular.compl` (theorem, [line 250](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean#L250))

> The complementation of an ω-regular language is ω-regular.

```lean
theorem IsRegular.compl {Symbol : Type} [Inhabited Symbol] {p : ωLanguage Symbol}
    (h : p.IsRegular) : (pᶜ).IsRegular
```

## Depends on

- [Deterministic Automata](../automata/da/basic.md)
- [Nondeterministic Automaton](../automata/na/basic.md)
- [Saturation](../../foundations/data/set/saturation.md)

## Proof depends on

- [Deterministic Buchi automata](../automata/da/buchi.md)
- [Equivalence of nondeterministic Buchi automata (NBAs)](../automata/na/buchiequiv.md)
- [Intersection of nondeterministic Buchi automata](../automata/na/buchiinter.md)
- [Concatenation of nondeterministic automata](../automata/na/concat.md)
- [Loop construction on nondeterministic automata](../automata/na/loop.md)
- [Sum of nondeterministic automata](../automata/na/sum.md)
- [Buchi Congruence](congruences/buchicongruence.md)
- [An ω-regular language that is not accepted by any deterministic Buchi automaton](exampleeventuallyzero.md)

## Sources

- [Cslib/Computability/Languages/OmegaRegularLanguage.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/OmegaRegularLanguage.lean)
