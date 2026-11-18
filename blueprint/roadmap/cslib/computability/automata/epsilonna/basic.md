---
catalog: module
lean: Cslib.Automata.εNA, Cslib.Automata.εNA.εClosure, Cslib.Automata.εNA.filter_ne_τ_eq_map_some, Cslib.Automata.εNA.FinAcc, Cslib.Automata.εNA.FinAcc.mem_language_iff
statement: formalized
proof: formalized
---

# Nondeterministic automata with ε-transitions

`Cslib.Computability.Automata.EpsilonNA.Basic`, in [Cslib/Computability/Automata/EpsilonNA/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/Basic.lean), by Fabrizio Montesi, Ching-Tsun Chou.

`Cslib.Automata.εNA` (structure, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/Basic.lean#L25))

> A nondeterministic finite automaton with ε-transitions (`εNA`) is an `NA` with an `Option`
> symbol type. The special symbol ε is represented by the `Option.none` case.
>
> Internally, ε (`Option.none`) is treated as the `τ` label of the underlying transition system,
> allowing for reusing the definitions and results on saturated transitions of `LTS` to deal with
> ε-closure.

```lean
structure εNA (State Symbol : Type*) extends NA State (Option Symbol)
```

`Cslib.Automata.εNA.εClosure` (abbreviation, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/Basic.lean#L37))

> The `ε`-closure of a set of states `S` is the set of states reachable by any state in `S`
> by performing only `ε`-transitions. We use `LTS.τClosure` since `ε` (`Option.none`) is an instance
> of `HasTau.τ`.

```lean
abbrev εNA.εClosure (a : εNA State Symbol) (S : Set State)
```

`Cslib.Automata.εNA.filter_ne_τ_eq_map_some` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/Basic.lean#L41))

```lean
theorem filter_ne_τ_eq_map_some {μs : List (Option Symbol)} :
    μs.filter (· ≠ HasTau.τ) = μs.reduceOption.map some
```

`Cslib.Automata.εNA.FinAcc` (structure, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/Basic.lean#L48))

> The finite-word acceptance condition of an `εNA` is a set of accepting states.

```lean
structure FinAcc (State Symbol : Type*) extends εNA State Symbol where
  /-- The set of accepting states. -/
  accept : Set State
```

`Cslib.Automata.εNA.FinAcc.mem_language_iff` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/Basic.lean#L63))

> A word is accepted if and only if a plain run from an initial to an accepting state reads it
> once its `ε`s are dropped.

```lean
theorem mem_language_iff {a : FinAcc State Symbol} {xs : List Symbol} :
    xs ∈ language a ↔ ∃ s ∈ a.start, ∃ t ∈ a.accept,
      ∃ μs : List (Option Symbol), μs.reduceOption = xs ∧ a.MTr s μs t
```

## Depends on

- [Nondeterministic Automaton](../na/basic.md)
- [LTS with a special "internal" transition `τ`](../../../foundations/semantics/lts/hastau.md)

## Sources

- [Cslib/Computability/Automata/EpsilonNA/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Automata/EpsilonNA/Basic.lean)
