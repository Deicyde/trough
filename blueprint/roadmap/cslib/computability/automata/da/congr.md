---
catalog: module
lean: Language.RightCongruence.toDA, Cslib.Automata.DA.congr_mtr_eq, Cslib.Automata.DA.congr_mtr_append, Cslib.Automata.DA.FinAcc.congr_language_eq
statement: formalized
proof: formalized
---

# Deterministic automaton corresponding to a right congruence

`Cslib.Computability.Automata.DA.Congr`, in [Cslib/Computability/Automata/DA/Congr.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Congr.lean), by Ching-Tsun Chou.

`Language.RightCongruence.toDA` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Congr.lean#L27))

> Every right congruence gives rise to a DA whose states are the equivalence classes of
> the right congruence, whose start state is the empty word, and whose transition functiuon
> is concatenation on the right of the input symbol. Note that the transition function is
> well-defined only because `c` is a right congruence.

```lean
def RightCongruence.toDA [c : RightCongruence Symbol] : Automata.DA (Quotient c.eq) Symbol
```

`Cslib.Automata.DA.congr_mtr_eq` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Congr.lean#L47))

> After consuming a finite word `xs`, `c.toDA` reaches the state `⟦ xs ⟧` which is
> the equivalence class of `xs`.

```lean
theorem congr_mtr_eq {xs : List Symbol} :
    c.toDA.mtr c.toDA.start xs = ⟦ xs ⟧
```

`Cslib.Automata.DA.congr_mtr_append` (theorem, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Congr.lean#L58))

> After consuming a finite word `ys` from the state `⟦ xs ⟧`, `c.toDA` reaches
> the state `⟦ xs ++ ys ⟧`.

```lean
theorem congr_mtr_append {xs ys : List Symbol} :
    c.toDA.mtr ⟦ xs ⟧ ys = ⟦ xs ++ ys ⟧
```

`Cslib.Automata.DA.FinAcc.congr_language_eq` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Congr.lean#L70))

> The language of `c.toDA` with a single accepting state `s` is exactly
> the equivalence class corresponding to `s`.

```lean
theorem congr_language_eq {a : Quotient c.eq} : language (FinAcc.mk c.toDA {a}) = eqvCls a
```

## Depends on

- [Deterministic Automata](basic.md)
- [Right Congruence](../../languages/congruences/basic.md)

## Sources

- [Cslib/Computability/Automata/DA/Congr.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/DA/Congr.lean)
