---
catalog: module
lean: Turing.tapeOfList, Turing.tapeOfList_ofNat, Turing.tapeOfList_negSucc, Turing.tapeOfList_append_single, Turing.tapeOfList_eq_none_iff, Turing.tapeOfList_nil, Turing.tapeOfList_zero, Turing.wordsCfg, Turing.mapState_wordsCfg, Turing.withState_wordsCfg, Turing.prependOutput_wordsCfg, Turing.Cfg.init_eq_wordsCfg
statement: formalized
proof: formalized
---

# Tapes holding words and configurations of such tapes

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.WordsCfg`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean), by Christian Reitwiessner.

> The normal form in which "tape transformer" machines (cf. `TransformsTapes.lean`) start and finish:
> every work tape holds a word in the cells `0, 1, …` and is blank everywhere else, with every head
> at the start.
>
> ## Main definitions
>
> * `Turing.tapeOfList`: the tape holding exactly a given word.
> * `Turing.wordsCfg`: the configuration whose tapes hold given words.

`Turing.tapeOfList` (definition, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L31))

> A tape containing exactly the symbols of `xs` at positions `0, ..., xs.length - 1`.

```lean
def tapeOfList (xs : List Symbol) : ℤ → Option Symbol
```

`Turing.tapeOfList_ofNat` (lemma, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L36))

```lean
lemma tapeOfList_ofNat (xs : List Symbol) (n : ℕ) : tapeOfList xs n = xs[n]?
```

`Turing.tapeOfList_negSucc` (lemma, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L39))

```lean
lemma tapeOfList_negSucc (xs : List Symbol) (n : ℕ) :
    tapeOfList xs (.negSucc n) = none
```

`Turing.tapeOfList_append_single` (lemma, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L43))

> Appending one symbol writes precisely the cell after the existing word.

```lean
lemma tapeOfList_append_single (xs : List Symbol) (x : Symbol) :
    tapeOfList (xs ++ [x]) = Function.update (tapeOfList xs) (xs.length : ℤ) (some x)
```

`Turing.tapeOfList_eq_none_iff` (lemma, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L51))

> A cell of `tapeOfList xs` is blank exactly outside the positions `0, …, xs.length - 1`.

```lean
lemma tapeOfList_eq_none_iff (xs : List Symbol) (z : ℤ) :
    tapeOfList xs z = none ↔ z < 0 ∨ (xs.length : ℤ) ≤ z
```

`Turing.tapeOfList_nil` (lemma, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L57))

> The blank tape holds the empty word.

```lean
lemma tapeOfList_nil : tapeOfList ([] : List Symbol) = fun _ => none
```

`Turing.tapeOfList_zero` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L62))

> The cell at position `0` holds the first symbol of the word.

```lean
lemma tapeOfList_zero (xs : List Symbol) : tapeOfList xs 0 = xs.head?
```

`Turing.wordsCfg` (definition, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L70))

> The configuration whose work tape `i` holds exactly the word `ws i` with its head at the
> start, whose input head is at the start of the input, in state `q` with output `out`.

```lean
def wordsCfg (input : List Symbol) (q : Option State)
    (ws : Fin k → List Symbol) (out : List Symbol) : Cfg k Symbol State input
```

`Turing.mapState_wordsCfg` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L76))

> Remapping the state of a `wordsCfg` remaps its state and leaves the words alone.

```lean
lemma mapState_wordsCfg {State' : Type*} (φ : Option State → Option State')
    (input : List Symbol) (q : Option State) (ws : Fin k → List Symbol) (out : List Symbol) :
    (wordsCfg input q ws out).mapState φ = wordsCfg input (φ q) ws out
```

`Turing.withState_wordsCfg` (lemma, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L82))

> Changing the state of a `wordsCfg` leaves the words alone.

```lean
lemma withState_wordsCfg {State' : Type*} (input : List Symbol) (q : Option State)
    (ws : Fin k → List Symbol) (out : List Symbol) (q' : Option State') :
    (wordsCfg input q ws out).withState q' = wordsCfg input q' ws out
```

`Turing.prependOutput_wordsCfg` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L88))

> Prepending a word to the output of a `wordsCfg` prepends it to the output word.

```lean
lemma prependOutput_wordsCfg (input : List Symbol) (q : Option State)
    (ws : Fin k → List Symbol) (out pre : List Symbol) :
    (wordsCfg input q ws out).prependOutput pre = wordsCfg input q ws (pre ++ out)
```

`Turing.Cfg.init_eq_wordsCfg` (lemma, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean#L93))

> The initial configuration is the word configuration with blank tapes and no output.

```lean
lemma Cfg.init_eq_wordsCfg (q₀ : State) (input : List Symbol) :
    Cfg.init (k := k) q₀ input = wordsCfg input (some q₀) (fun _ => []) []
```

## Depends on

- [Configurations of Multi-Tape Turing Machines](../configuration.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/WordsCfg.lean)
