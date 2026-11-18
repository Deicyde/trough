---
catalog: module
lean: Cslib.Automata.NA.toEpsilonNA, Cslib.Automata.NA.FinAcc.toEpsilonNAFinAcc, Cslib.Automata.NA.FinAcc.toEpsilonNAFinAcc_language_eq
statement: formalized
proof: formalized
---

# Translation of Nondeterministic Automata into Nondeterministic Automata with ε-transitions

`Cslib.Computability.Automata.NA.ToEpsilonNA`, in [Cslib/Computability/Automata/NA/ToEpsilonNA.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToEpsilonNA.lean), by Yusuf Demir.

> An `NA` is an `εNA` whose ε-transitions are self-loops.

`Cslib.Automata.NA.toEpsilonNA` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToEpsilonNA.lean#L25))

> `NA` is a special case of `εNA`, through `LTS.mapHom` and `Language.Hom.reduceOption`: the
> transitions on `some x` are the runs of the `NA` on `[x]`, and the ε-transitions are self-loops.

```lean
def toEpsilonNA (a : NA State Symbol) : εNA State Symbol
```

`Cslib.Automata.NA.FinAcc.toEpsilonNAFinAcc` (definition, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToEpsilonNA.lean#L32))

> `NA.FinAcc` is a special case of `εNA.FinAcc`.

```lean
def toEpsilonNAFinAcc (a : NA.FinAcc State Symbol) : εNA.FinAcc State Symbol
```

`Cslib.Automata.NA.FinAcc.toEpsilonNAFinAcc_language_eq` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToEpsilonNA.lean#L38))

> The `εNA.FinAcc` constructed from an `NA.FinAcc` has the same language.

```lean
theorem toEpsilonNAFinAcc_language_eq {a : NA.FinAcc State Symbol} :
    language a.toEpsilonNAFinAcc = language a
```

## Depends on

- [Nondeterministic automata with ε-transitions](../epsilonna/basic.md)
- [Label homomorphism map for LTS](../../../foundations/semantics/lts/maphom.md)

## Sources

- [Cslib/Computability/Automata/NA/ToEpsilonNA.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/ToEpsilonNA.lean)
