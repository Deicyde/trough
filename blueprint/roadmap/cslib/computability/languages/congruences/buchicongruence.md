---
catalog: module
lean: Cslib.Automata.NA.Buchi.BuchiCongruence, Cslib.Automata.NA.Buchi.BuchiCongrParam, Cslib.Automata.NA.Buchi.buchiCongrParam_surjective, Cslib.Automata.NA.Buchi.buchiCongruence_fin_index, Cslib.Automata.NA.Buchi.buchiCongruence_transfer, Cslib.Automata.NA.Buchi.buchiFamily, Cslib.Automata.NA.Buchi.mem_buchiFamily, Cslib.Automata.NA.Buchi.buchiFamily_cover, Cslib.Automata.NA.Buchi.buchiFamily_saturation
statement: formalized
proof: formalized
---

# Buchi Congruence

`Cslib.Computability.Languages.Congruences.BuchiCongruence`, in [Cslib/Computability/Languages/Congruences/BuchiCongruence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean), by Ching-Tsun Chou.

> A special type of right congruences used by J.R. Büchi to prove the closure
> of ω-regular languages under complementation.

`Cslib.Automata.NA.Buchi.BuchiCongruence` (definition, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L37))

> Given a Buchi automaton `na`, two finite words `u` and `v` are Buchi-congruent
> according to `na` iff for every pair of states `s` and `t` of `na`, both of the
> following two conditions hold:
> (1) `u` can move `na` from `s` to `t` iff `v` can move `na` from `s` to `t`;
> (2) `u` can move `na` from `s` to `t` via an accepting states iff `v` can move `na`
> from `s` to `t` via an accepting states.

```lean
def BuchiCongruence (na : Buchi State Symbol) : RightCongruence Symbol
```

`Cslib.Automata.NA.Buchi.BuchiCongrParam` (definition, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L51))

> `BuchiCongrParam` is a parameterization of the equivalence classes of `na.BuchiCongruence`
> using the type `State → State → Prop × Prop`, which is finite if `State` is.

```lean
noncomputable def BuchiCongrParam (na : Buchi State Symbol)
    (f : State → State → Prop × Prop) : Quotient na.BuchiCongruence.eq
```

`Cslib.Automata.NA.Buchi.buchiCongrParam_surjective` (lemma, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L61))

> `BuchiCongrParam` is surjective.

```lean
lemma buchiCongrParam_surjective : Surjective na.BuchiCongrParam
```

`Cslib.Automata.NA.Buchi.buchiCongruence_fin_index` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L76))

> `na.BuchiCongruence` is of finite index if `na` has only finitely many states.

```lean
theorem buchiCongruence_fin_index [Finite State] : Finite (Quotient na.BuchiCongruence.eq)
```

`Cslib.Automata.NA.Buchi.buchiCongruence_transfer` (lemma, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L82))

> If `xl` and `yl` belong to the same equivalence class of `na.BuchiCongruence`
> and `xl` can move `na` from state `s` to state `t`, then so can `yl` and, furthermore,
> if `xl` makes `na` go through an accepting state of `na`, then so can `yl`.

```lean
lemma buchiCongruence_transfer
    {a : Quotient na.BuchiCongruence.eq} {xl yl : List Symbol} {s t : State}
    (hc : xl ∈ na.BuchiCongruence.eqvCls a) (hc' : yl ∈ na.BuchiCongruence.eqvCls a)
    (hp : xl ∈ na.pairLang s t) : ∃ sl, na.Execution s yl t sl ∧
      ( xl ∈ na.pairViaLang na.accept s t → ∃ r ∈ na.accept, r ∈ sl )
```

`Cslib.Automata.NA.Buchi.buchiFamily` (definition, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L107))

> `na.buchiFamily` is a family of ω-languages indexed by a pair of equivalence classes
> of `na.BuchiCongruence` which will turn out to saturate the ω-language accepted by `na`
> and cover all possible ω-sequences.

```lean
def buchiFamily [Inhabited Symbol] (na : Buchi State Symbol) :
    Quotient na.BuchiCongruence.eq × Quotient na.BuchiCongruence.eq → ωLanguage Symbol
```

`Cslib.Automata.NA.Buchi.mem_buchiFamily` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L111))

```lean
theorem mem_buchiFamily [Inhabited Symbol]
    {xs : ωSequence Symbol} {a b : Quotient na.BuchiCongruence.eq} :
    xs ∈ na.buchiFamily (a, b) ↔ ∃ xl, ∃ xls : ωSequence (List Symbol),
      xl ∈ na.BuchiCongruence.eqvCls a ∧ (∀ k, xls k ∈ na.BuchiCongruence.eqvCls b - 1) ∧
      xl ++ω xls.flatten = xs
```

`Cslib.Automata.NA.Buchi.buchiFamily_cover` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L122))

> `na.buchiFamily` is a cover if `na` has only finitely many states.
> This theorem uses the Ramsey theorem for infinite graphs and does not depend on any details
> of `na.BuchiCongruence` other than that it is of finite index.

```lean
theorem buchiFamily_cover [Inhabited Symbol] [Finite State] :
    ⨆ i, na.buchiFamily i = ⊤
```

`Cslib.Automata.NA.Buchi.buchiFamily_saturation` (theorem, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean#L184))

> `na.buchiFamily` saturates the ω-language accepted by `na`.

```lean
theorem buchiFamily_saturation [Inhabited Symbol] :
    Saturates (fun i ↦ (na.buchiFamily i).toSet) (language na).toSet
```

## Depends on

- [Languages determined by pairs of states](../../automata/na/pair.md)
- [Right Congruence](basic.md)
- [Saturation](../../../foundations/data/set/saturation.md)

## Proof depends on

- [Ramsey theorem for infinite graphs](../../../foundations/combinatorics/infinitegraphramsey.md)

## Sources

- [Cslib/Computability/Languages/Congruences/BuchiCongruence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Languages/Congruences/BuchiCongruence.lean)
