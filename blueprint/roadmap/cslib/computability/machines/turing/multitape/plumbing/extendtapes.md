---
catalog: module
lean: Turing.MultiTapeTM.partialInv, Turing.MultiTapeTM.partialInv_isPartialInv, Turing.MultiTapeTM.extendTapes, Turing.MultiTapeTM.extendTapes_q₀, Turing.MultiTapeTM.embed, Turing.MultiTapeTM.partialInv_embed, Turing.MultiTapeTM.partialInv_eq_none, Turing.MultiTapeTM.partialInv_eq_some, Turing.MultiTapeTM.embed_workTapes_embed, Turing.MultiTapeTM.embed_workTapePos_embed, Turing.MultiTapeTM.embed_workTapeSymbols_embed, Turing.MultiTapeTM.embedHom, Turing.MultiTapeTM.space_map_embedHom_le, Turing.MultiTapeTM.tapeEmb, Turing.MultiTapeTM.tapeEmb_apply, Turing.MultiTapeTM.range_tapeEmb, Turing.MultiTapeTM.partialInv_tapeEmb, Turing.MultiTapeTM.embed_tapeEmb, Turing.MultiTapeTM.oneTapeCfg, Turing.MultiTapeTM.embed_oneTapeCfg, Turing.MultiTapeTM.runFrom_tapeEmb, Turing.MultiTapeTM.TransformsTapes.tapeEmb, Turing.MultiTapeTM.noTapes, Turing.MultiTapeTM.partialInv_noTapes, Turing.MultiTapeTM.noTapesCfg, Turing.MultiTapeTM.embed_noTapes, Turing.MultiTapeTM.embed_noTapesCfg, Turing.MultiTapeTM.runFrom_noTapes
statement: formalized
proof: formalized
---

# Extending a machine with additional work tapes

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.ExtendTapes`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean), by Christian Reitwiessner.

> `extendTapes tm e`, for an embedding `e : Fin k ↪ Fin k'`, runs `tm` inside a machine with more
> work tapes. The tapes selected by `e` are used by `tm`: target tape `e j` plays the role of source
> tape `j`. The remaining tapes are left unchanged.
>
> The configuration map `embed e cfg extraTapes extraPos` places `cfg` on the selected tapes and
> initialises the remaining tapes from `extraTapes` and `extraPos`.
>
> The configuration map is a homomorphism of step relations (`embedHom`), so each run path of `tm`
> maps to a run path of the larger machine.
>
> ## Main definitions
>
> * `Turing.MultiTapeTM.partialInv`: the partial inverse of the tape embedding.
> * `Turing.MultiTapeTM.extendTapes`: the machine with reindexed work tapes.
> * `Turing.MultiTapeTM.embed`: the corresponding configuration map.
> * `Turing.MultiTapeTM.embedHom`: the configuration map as a step-preserving map, which maps run
>   paths.
> * `Turing.MultiTapeTM.tapeEmb`: the embedding placing the only tape of a one-tape machine on
>   tape `i`, and `Turing.MultiTapeTM.noTapes`: the embedding of a machine without work tapes.
>
> ## Main results
>
> * `Turing.MultiTapeTM.space_map_embedHom_le`: the space bound for a mapped path.
> * `Turing.MultiTapeTM.oneTapeCfg`: the one-tape view of a configuration.
> * `Turing.MultiTapeTM.runFrom_tapeEmb`: the run of a one-tape machine placed on work tape `i`.
> * `Turing.MultiTapeTM.TransformsTapes.tapeEmb`: a one-tape specification, read on tape `i`.
> * `Turing.MultiTapeTM.runFrom_noTapes`: the run of a machine without work tapes, placed in a machine
>   with `k` of them.

`Turing.MultiTapeTM.partialInv` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L52))

> The computable analogue of `Function.partialInv` for an embedding `e`: `partialInv e l = some j`
> when `e j = l` (such `j` is unique by injectivity), and `none` when `l` lies outside the range of
> `e`.

```lean
public def partialInv (e : Fin k ↪ Fin k') (l : Fin k') : Option (Fin k)
```

`Turing.MultiTapeTM.partialInv_isPartialInv` (lemma, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L56))

> `partialInv e` is a partial inverse of `e`.

```lean
public lemma partialInv_isPartialInv (e : Fin k ↪ Fin k') :
    Function.IsPartialInv e (partialInv e)
```

`Turing.MultiTapeTM.extendTapes` (definition, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L64))

> `tm` run on the tapes selected by the embedding `e`, leaving other tapes untouched: work tape
> `e j` plays the role of `tm`'s tape `j`, and any tape outside `range e` is never written and never
> moves.

```lean
public noncomputable def extendTapes (tm : MultiTapeTM k Symbol State)
(e : Fin k ↪ Fin k') : MultiTapeTM k' Symbol State
```

`Turing.MultiTapeTM.extendTapes_q₀` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L74))

```lean
public lemma extendTapes_q₀ (tm : MultiTapeTM k Symbol State) (e : Fin k ↪ Fin k') :
    (tm.extendTapes e).q₀ = tm.q₀
```

`Turing.MultiTapeTM.embed` (definition, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L79))

> A configuration of `tm`, embedded: tape `j` goes to tape `e j`, the tapes outside `range e`
> carry the given `extraTapes` contents and `extraPos` head positions.

```lean
public def embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
(extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) :
Cfg k' Symbol State input
```

`Turing.MultiTapeTM.partialInv_embed` (lemma, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L93))

> The partial inverse recovers the source tape of an embedded tape.

```lean
public lemma partialInv_embed (e : Fin k ↪ Fin k') (j : Fin k) : partialInv e (e j) = some j
```

`Turing.MultiTapeTM.partialInv_eq_none` (lemma, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L97))

> Outside the range of `e`, the partial inverse is undefined.

```lean
public lemma partialInv_eq_none (e : Fin k ↪ Fin k') {l : Fin k'} (hl : l ∉ Set.range e) :
    partialInv e l = none
```

`Turing.MultiTapeTM.partialInv_eq_some` (lemma, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L102))

> If the partial inverse is `some j`, then `e j = l`.

```lean
public lemma partialInv_eq_some (e : Fin k ↪ Fin k') {l : Fin k'} {j : Fin k}
    (h : partialInv e l = some j) : e j = l
```

`Turing.MultiTapeTM.embed_workTapes_embed` (lemma, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L107))

```lean
public lemma embed_workTapes_embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (j : Fin k) :
    (embed e cfg extraTapes extraPos).workTapes (e j) = cfg.workTapes j
```

`Turing.MultiTapeTM.embed_workTapePos_embed` (lemma, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L113))

```lean
public lemma embed_workTapePos_embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (j : Fin k) :
    (embed e cfg extraTapes extraPos).workTapePos (e j) = cfg.workTapePos j
```

`Turing.MultiTapeTM.embed_workTapeSymbols_embed` (lemma, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L119))

```lean
public lemma embed_workTapeSymbols_embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (j : Fin k) :
    (embed e cfg extraTapes extraPos).workTapeSymbols (e j) = cfg.workTapeSymbols j
```

`Turing.MultiTapeTM.embedHom` (definition, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L128))

> `embed` as a homomorphism of step relations: each step `c → c'` of `tm` becomes the step
> `embed c → embed c'` of the reindexed machine, so a run path of `tm` maps to a run path of the
> reindexed machine, with the extra tapes held fixed. `Follows.stepHom` builds it, since `embed`
> agrees with the adapter defining `extendTapes`.

```lean
public noncomputable def embedHom (tm : MultiTapeTM k Symbol State)
(e : Fin k ↪ Fin k') (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) :
(tm.stepRel input).Hom ((tm.extendTapes e).stepRel input)
```

`Turing.MultiTapeTM.space_map_embedHom_le` (lemma, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L141))

> **Space bound for a reindexed path.** The embedded tapes visit what the original path visits,
> while each of the remaining `k' - k` tapes never moves and contributes one cell.

```lean
public lemma space_map_embedHom_le (tm : MultiTapeTM k Symbol State) (e : Fin k ↪ Fin k')
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (p : tm.RunPath input) :
    (p.map (embedHom tm e extraTapes extraPos)).space ≤ p.space + (k' - k)
```

> ### Placing a one-tape machine on a single work tape

`Turing.MultiTapeTM.tapeEmb` (definition, [line 157](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L157))

> The embedding that places the only work tape of a one-tape machine on tape `i`.

```lean
public def tapeEmb (i : Fin k) : Fin 1 ↪ Fin k
```

`Turing.MultiTapeTM.tapeEmb_apply` (lemma, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L161))

```lean
public lemma tapeEmb_apply (i : Fin k) (j : Fin 1) : tapeEmb i j = i
```

`Turing.MultiTapeTM.range_tapeEmb` (lemma, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L164))

```lean
public lemma range_tapeEmb (i : Fin k) : Set.range (tapeEmb i) = {i}
```

`Turing.MultiTapeTM.partialInv_tapeEmb` (lemma, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L170))

> Tape `i` is the image of the only tape of a one-tape machine, and no other tape is.

```lean
public lemma partialInv_tapeEmb (i l : Fin k) :
    partialInv (tapeEmb i) l = if l = i then some 0 else none
```

`Turing.MultiTapeTM.embed_tapeEmb` (lemma, [line 177](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L177))

> A one-tape configuration placed on tape `i` leaves every other tape as it was.

```lean
public lemma embed_tapeEmb (i : Fin k) (cfg : Cfg 1 Symbol State input)
    (tapes : Fin k → ℤ → Option Symbol) (heads : Fin k → ℤ) :
    embed (tapeEmb i) cfg tapes heads =
      ⟨cfg.state, cfg.inputPos, Function.update tapes i (cfg.workTapes 0),
        Function.update heads i (cfg.workTapePos 0), cfg.output⟩
```

`Turing.MultiTapeTM.oneTapeCfg` (definition, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L186))

> The one-tape view of a configuration of a machine with `k` work tapes: the tape and head of
> tape `i`, with everything else as it is.

```lean
public def oneTapeCfg (i : Fin k) (cfg : Cfg k Symbol State input) :
Cfg 1 Symbol State input
```

`Turing.MultiTapeTM.embed_oneTapeCfg` (lemma, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L191))

> A configuration is its own one-tape view on tape `i`, placed back on tape `i`.

```lean
public lemma embed_oneTapeCfg (i : Fin k) (cfg : Cfg k Symbol State input) :
    embed (tapeEmb i) (oneTapeCfg i cfg) cfg.workTapes cfg.workTapePos = cfg
```

`Turing.MultiTapeTM.runFrom_tapeEmb` (lemma, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L199))

> **Running a one-tape machine on work tape `i`.** The run is the run on the one-tape view of the
> configuration, placed back on tape `i`; every other tape and head keeps its starting value. Combine
> with `embed_tapeEmb` to read off the resulting configuration.

```lean
public lemma runFrom_tapeEmb (tm : MultiTapeTM 1 Symbol State) (i : Fin k)
    (cfg : Cfg k Symbol State input) (n : ℕ) :
    (tm.extendTapes (tapeEmb i)).runFrom cfg n =
      embed (tapeEmb i) (tm.runFrom (oneTapeCfg i cfg) n) cfg.workTapes cfg.workTapePos
```

`Turing.MultiTapeTM.TransformsTapes.tapeEmb` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L208))

> **A one-tape specification on tape `i`.** A one-tape machine placed on tape `i` transforms the
> word on that tape as it did on its own tape and leaves every other word alone; each remaining tape
> costs one cell.

```lean
public theorem TransformsTapes.tapeEmb {tm : MultiTapeTM 1 Symbol State}
    {P : (input : List Symbol) → (Fin 1 → List Symbol) → Prop}
    {Q : (input : List Symbol) → (Fin 1 → List Symbol) → (Fin 1 → List Symbol) →
      List Symbol → Prop} {t s : ℕ}
    (h : TransformsTapes tm P Q t s) (i : Fin k) :
    TransformsTapes (tm.extendTapes (MultiTapeTM.tapeEmb i))
      (fun input ws => P input fun _ => ws i)
      (fun input ws ws' emitted =>
        ∃ v, Q input (fun _ => ws i) v emitted ∧ ws' = Function.update ws i (v 0))
      t (s + (k - 1))
```

`Turing.MultiTapeTM.noTapes` (definition, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L238))

> The embedding of a machine without work tapes into a machine with `k` of them.

```lean
public def noTapes (k : ℕ) : Fin 0 ↪ Fin k
```

`Turing.MultiTapeTM.partialInv_noTapes` (lemma, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L242))

> No tape is in the range of `noTapes`.

```lean
public lemma partialInv_noTapes (l : Fin k) : partialInv (noTapes k) l = none
```

`Turing.MultiTapeTM.noTapesCfg` (definition, [line 246](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L246))

> The view of a configuration as a configuration of a machine without work tapes.

```lean
public def noTapesCfg (cfg : Cfg k Symbol State input) : Cfg 0 Symbol State input
```

`Turing.MultiTapeTM.embed_noTapes` (lemma, [line 251](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L251))

> A configuration without work tapes, placed in a machine with `k` of them, only contributes its
> state, its input head and its output.

```lean
public lemma embed_noTapes (cfg : Cfg 0 Symbol State input)
    (tapes : Fin k → ℤ → Option Symbol) (heads : Fin k → ℤ) :
    embed (noTapes k) cfg tapes heads = ⟨cfg.state, cfg.inputPos, tapes, heads, cfg.output⟩
```

`Turing.MultiTapeTM.embed_noTapesCfg` (lemma, [line 257](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L257))

> A configuration is its tapeless view, placed back on its tapes.

```lean
public lemma embed_noTapesCfg (cfg : Cfg k Symbol State input) :
    embed (noTapes k) (noTapesCfg cfg) cfg.workTapes cfg.workTapePos = cfg
```

`Turing.MultiTapeTM.runFrom_noTapes` (lemma, [line 264](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L264))

> **Running a machine without work tapes inside a machine with `k` of them.** Only the state, the
> input head and the output change; every work tape and work head keeps its starting value.

```lean
public lemma runFrom_noTapes (tm : MultiTapeTM 0 Symbol State) (cfg : Cfg k Symbol State input)
    (n : ℕ) :
    (tm.extendTapes (noTapes k)).runFrom cfg n =
      ⟨(tm.runFrom (noTapesCfg cfg) n).state, (tm.runFrom (noTapesCfg cfg) n).inputPos,
        cfg.workTapes, cfg.workTapePos, (tm.runFrom (noTapesCfg cfg) n).output⟩
```

## Depends on

- [Machines as transformers of tape words](transformstapes.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean)
