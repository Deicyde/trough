---
catalog: module
lean: Cslib.Automata.NA.FinAcc.preimage, Cslib.Automata.NA.FinAcc.preimage_start, Cslib.Automata.NA.FinAcc.preimage_accept, Cslib.Automata.NA.FinAcc.preimage_mTr, Cslib.Automata.NA.FinAcc.accepts_preimage, Cslib.Automata.NA.FinAcc.preimage_language_eq
statement: formalized
proof: formalized
---

# Preimage construction on nondeterministic automata

`Cslib.Computability.Automata.NA.Preimage`, in [Cslib/Computability/Automata/NA/Preimage.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean), by Ching-Tsun Chou.

`Cslib.Automata.NA.FinAcc.preimage` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean#L30))

> Given a language homomorphism `f` from `Symbol'` to `Symbol` and an NA `na` on `Symbol`,
> `na.preimage f` is an NA on `Symbol` with the same state space, start states, and
> accept states, but with a different transition relation: the step that `na.preimage f` takes
> on input `x` is the composition of the steps taken by `na` on inputs `f [x]`.

```lean
def preimage (na : FinAcc State Symbol) : FinAcc State Symbol'
```

`Cslib.Automata.NA.FinAcc.preimage_start` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean#L36))

```lean
theorem preimage_start (na : FinAcc State Symbol) : (na.preimage f).start = na.start
```

`Cslib.Automata.NA.FinAcc.preimage_accept` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean#L39))

```lean
theorem preimage_accept (na : FinAcc State Symbol) : (na.preimage f).accept = na.accept
```

`Cslib.Automata.NA.FinAcc.preimage_mTr` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean#L42))

```lean
theorem preimage_mTr (na : FinAcc State Symbol) {xs' : List Symbol'} {s t : State} :
    (na.preimage f).MTr s xs' t ↔ na.MTr s (f xs') t
```

`Cslib.Automata.NA.FinAcc.accepts_preimage` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean#L48))

> `na.preimage f` accepts a word `xs'` iff `na` accepts the word `f xs'`.

```lean
theorem accepts_preimage {na : FinAcc State Symbol} {xs' : List Symbol'} :
    Accepts (na.preimage f) xs' ↔ Accepts na (f xs')
```

`Cslib.Automata.NA.FinAcc.preimage_language_eq` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean#L54))

> `na.preimage f` accepts the preimage under `f` of the language accepted by `na`.

```lean
theorem preimage_language_eq (na : FinAcc State Symbol) :
    language (na.preimage f) = (language na).preimage f
```

## Depends on

- [Nondeterministic Automaton](basic.md)
- [Label homomorphism map for LTS](../../../foundations/semantics/lts/maphom.md)

## Sources

- [Cslib/Computability/Automata/NA/Preimage.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/NA/Preimage.lean)
