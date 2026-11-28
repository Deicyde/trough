---
catalog: module
lean: Turing.MultiTapeTM.partialInv, Turing.MultiTapeTM.partialInv_isPartialInv, Turing.MultiTapeTM.extendTapes, Turing.MultiTapeTM.extendTapes_q₀, Turing.MultiTapeTM.embed, Turing.MultiTapeTM.partialInv_embed, Turing.MultiTapeTM.partialInv_eq_none, Turing.MultiTapeTM.partialInv_eq_some, Turing.MultiTapeTM.embed_workTapes_embed, Turing.MultiTapeTM.embed_workTapePos_embed, Turing.MultiTapeTM.embed_workTapeSymbols_embed, Turing.MultiTapeTM.embed_workTapes_of_notMem_range, Turing.MultiTapeTM.embed_workTapePos_of_notMem_range, Turing.MultiTapeTM.embed_eq_of_forall_embed, Turing.MultiTapeTM.embedHom, Turing.MultiTapeTM.space_map_embedHom_le, Turing.MultiTapeTM.exists_runPath_extendTapes, Turing.MultiTapeTM.tapeEmb, Turing.MultiTapeTM.tapeEmb_apply, Turing.MultiTapeTM.range_tapeEmb, Turing.MultiTapeTM.partialInv_tapeEmb, Turing.MultiTapeTM.embed_tapeEmb, Turing.MultiTapeTM.oneTapeCfg, Turing.MultiTapeTM.embed_oneTapeCfg, Turing.MultiTapeTM.runFrom_tapeEmb, Turing.MultiTapeTM.TransformsTapes.tapeEmb, Turing.MultiTapeTM.noTapes, Turing.MultiTapeTM.noTapesCfg, Turing.MultiTapeTM.embed_noTapes, Turing.MultiTapeTM.embed_noTapesCfg, Turing.MultiTapeTM.runFrom_noTapes
statement: formalized
proof: formalized
---

# Extending a machine with additional work tapes

`Cslib.Computability.Machines.Turing.MultiTape.Plumbing.ExtendTapes`, in [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean), by Christian Reitwiessner.

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
> * `Turing.MultiTapeTM.exists_runPath_extendTapes`: a computation of `tm`, run inside the
>   machine with extended tapes.
> * `Turing.MultiTapeTM.oneTapeCfg`: the one-tape view of a configuration.
> * `Turing.MultiTapeTM.runFrom_tapeEmb`: the run of a one-tape machine placed on work tape `i`.
> * `Turing.MultiTapeTM.TransformsTapes.tapeEmb`: a one-tape specification, read on tape `i`.
> * `Turing.MultiTapeTM.runFrom_noTapes`: the run of a machine without work tapes, placed in a machine
>   with `k` of them.

`Turing.MultiTapeTM.partialInv` (definition, [line 54](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L54))

> The computable analogue of `Function.partialInv` for an embedding `e`: `partialInv e l = some j`
> when `e j = l` (such `j` is unique by injectivity), and `none` when `l` lies outside the range of
> `e`.

```lean
public def partialInv (e : Fin k ↪ Fin k') (l : Fin k') : Option (Fin k)
```

`Turing.MultiTapeTM.partialInv_isPartialInv` (lemma, [line 58](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L58))

> `partialInv e` is a partial inverse of `e`.

```lean
public lemma partialInv_isPartialInv (e : Fin k ↪ Fin k') :
    Function.IsPartialInv e (partialInv e)
```

`Turing.MultiTapeTM.extendTapes` (definition, [line 66](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L66))

> `tm` run on the tapes selected by the embedding `e`, leaving other tapes untouched: work tape
> `e j` plays the role of `tm`'s tape `j`, and any tape outside `range e` is never written and never
> moves.

```lean
public noncomputable def extendTapes (tm : MultiTapeTM k Symbol State)
    (e : Fin k ↪ Fin k') : MultiTapeTM k' Symbol State
```

`Turing.MultiTapeTM.extendTapes_q₀` (lemma, [line 76](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L76))

```lean
public lemma extendTapes_q₀ (tm : MultiTapeTM k Symbol State) (e : Fin k ↪ Fin k') :
    (tm.extendTapes e).q₀ = tm.q₀
```

`Turing.MultiTapeTM.embed` (definition, [line 82](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L82))

> A configuration of `tm`, embedded: tape `j` goes to tape `e j`, the tapes outside `range e`
> carry the given `extraTapes` contents and `extraPos` head positions.

```lean
public def embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) :
    Cfg k' Symbol State input
```

`Turing.MultiTapeTM.partialInv_embed` (lemma, [line 96](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L96))

> The partial inverse recovers the source tape of an embedded tape.

```lean
public lemma partialInv_embed (e : Fin k ↪ Fin k') (j : Fin k) : partialInv e (e j) = some j
```

`Turing.MultiTapeTM.partialInv_eq_none` (lemma, [line 101](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L101))

> Outside the range of `e`, the partial inverse is undefined.

```lean
public lemma partialInv_eq_none (e : Fin k ↪ Fin k') {l : Fin k'} (hl : l ∉ Set.range e) :
    partialInv e l = none
```

`Turing.MultiTapeTM.partialInv_eq_some` (lemma, [line 107](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L107))

> If the partial inverse is `some j`, then `e j = l`.

```lean
public lemma partialInv_eq_some (e : Fin k ↪ Fin k') {l : Fin k'} {j : Fin k}
    (h : partialInv e l = some j) : e j = l
```

`Turing.MultiTapeTM.embed_workTapes_embed` (lemma, [line 112](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L112))

```lean
public lemma embed_workTapes_embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (j : Fin k) :
    (embed e cfg extraTapes extraPos).workTapes (e j) = cfg.workTapes j
```

`Turing.MultiTapeTM.embed_workTapePos_embed` (lemma, [line 118](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L118))

```lean
public lemma embed_workTapePos_embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (j : Fin k) :
    (embed e cfg extraTapes extraPos).workTapePos (e j) = cfg.workTapePos j
```

`Turing.MultiTapeTM.embed_workTapeSymbols_embed` (lemma, [line 124](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L124))

```lean
public lemma embed_workTapeSymbols_embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (j : Fin k) :
    (embed e cfg extraTapes extraPos).workTapeSymbols (e j) = cfg.workTapeSymbols j
```

`Turing.MultiTapeTM.embed_workTapes_of_notMem_range` (lemma, [line 131](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L131))

> Outside the range of `e`, an embedded configuration carries the extra tape contents.

```lean
public lemma embed_workTapes_of_notMem_range (e : Fin k ↪ Fin k')
    (cfg : Cfg k Symbol State input) (extraTapes : Fin k' → ℤ → Option Symbol)
    (extraPos : Fin k' → ℤ) {l : Fin k'} (hl : l ∉ Set.range e) :
    (embed e cfg extraTapes extraPos).workTapes l = extraTapes l
```

`Turing.MultiTapeTM.embed_workTapePos_of_notMem_range` (lemma, [line 139](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L139))

> Outside the range of `e`, an embedded configuration carries the extra head positions.

```lean
public lemma embed_workTapePos_of_notMem_range (e : Fin k ↪ Fin k')
    (cfg : Cfg k Symbol State input) (extraTapes : Fin k' → ℤ → Option Symbol)
    (extraPos : Fin k' → ℤ) {l : Fin k'} (hl : l ∉ Set.range e) :
    (embed e cfg extraTapes extraPos).workTapePos l = extraPos l
```

`Turing.MultiTapeTM.embed_eq_of_forall_embed` (lemma, [line 147](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L147))

> Embedding a configuration into tapes and heads that already agree with it on the range of `e`
> only sets the state, the input head and the output.

```lean
public lemma embed_eq_of_forall_embed (e : Fin k ↪ Fin k') (cfg : Cfg k Symbol State input)
    {tapes : Fin k' → ℤ → Option Symbol} {heads : Fin k' → ℤ}
    (htapes : ∀ j, tapes (e j) = cfg.workTapes j) (hheads : ∀ j, heads (e j) = cfg.workTapePos j) :
    embed e cfg tapes heads = ⟨cfg.state, cfg.inputPos, tapes, heads, cfg.output⟩
```

`Turing.MultiTapeTM.embedHom` (definition, [line 158](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L158))

> `embed` as a homomorphism of step relations: each step `c → c'` of `tm` becomes the step
> `embed c → embed c'` of the reindexed machine, so a run path of `tm` maps to a run path of the
> reindexed machine, with the extra tapes held fixed. `Follows.stepHom` builds it, since `embed`
> agrees with the adapter defining `extendTapes`.

```lean
public noncomputable def embedHom (tm : MultiTapeTM k Symbol State)
    (e : Fin k ↪ Fin k') (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) :
    (tm.stepRel input).Hom ((tm.extendTapes e).stepRel input)
```

`Turing.MultiTapeTM.space_map_embedHom_le` (lemma, [line 171](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L171))

> **Space bound for a reindexed path.** The embedded tapes visit what the original path visits,
> while each of the remaining `k' - k` tapes never moves and contributes one cell.

```lean
public lemma space_map_embedHom_le (tm : MultiTapeTM k Symbol State) (e : Fin k ↪ Fin k')
    (extraTapes : Fin k' → ℤ → Option Symbol) (extraPos : Fin k' → ℤ) (p : tm.RunPath input) :
    (p.map (embedHom tm e extraTapes extraPos)).space ≤ p.space + (k' - k)
```

`Turing.MultiTapeTM.exists_runPath_extendTapes` (theorem, [line 182](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L182))

> **Running a computation inside a larger machine.** A run path of `tm` from its initial
> configuration is also a run path of `tm.extendTapes e`, provided the tapes in the range of `e` start
> blank with their heads at `0`. The other tapes may hold anything and are left unchanged, and any
> word `pre` may already be on the output.

```lean
public theorem exists_runPath_extendTapes {tm : MultiTapeTM k Symbol State} (e : Fin k ↪ Fin k')
    {p : tm.RunPath input} (hh : p.head = tm.initCfg input) (pre : List Symbol)
    {tapes : Fin k' → ℤ → Option Symbol} {heads : Fin k' → ℤ}
    (htapes : ∀ j, tapes (e j) = fun _ => none) (hheads : ∀ j, heads (e j) = 0) :
    ∃ q : (tm.extendTapes e).RunPath input, q.head = ⟨some tm.q₀, 1, tapes, heads, pre⟩ ∧
      q.last = embed e (p.last.prependOutput pre) tapes heads ∧ q.length = p.length ∧
      q.space ≤ p.space + (k' - k)
```

> ### Placing a one-tape machine on a single work tape

`Turing.MultiTapeTM.tapeEmb` (definition, [line 203](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L203))

> The embedding that places the only work tape of a one-tape machine on tape `i`.

```lean
public def tapeEmb (i : Fin k) : Fin 1 ↪ Fin k
```

`Turing.MultiTapeTM.tapeEmb_apply` (lemma, [line 207](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L207))

```lean
public lemma tapeEmb_apply (i : Fin k) (j : Fin 1) : tapeEmb i j = i
```

`Turing.MultiTapeTM.range_tapeEmb` (lemma, [line 210](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L210))

```lean
public lemma range_tapeEmb (i : Fin k) : Set.range (tapeEmb i) = {i}
```

`Turing.MultiTapeTM.partialInv_tapeEmb` (lemma, [line 216](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L216))

> Tape `i` is the image of the only tape of a one-tape machine, and no other tape is.

```lean
public lemma partialInv_tapeEmb (i l : Fin k) :
    partialInv (tapeEmb i) l = if l = i then some 0 else none
```

`Turing.MultiTapeTM.embed_tapeEmb` (lemma, [line 223](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L223))

> A one-tape configuration placed on tape `i` leaves every other tape as it was.

```lean
public lemma embed_tapeEmb (i : Fin k) (cfg : Cfg 1 Symbol State input)
    (tapes : Fin k → ℤ → Option Symbol) (heads : Fin k → ℤ) :
    embed (tapeEmb i) cfg tapes heads =
      ⟨cfg.state, cfg.inputPos, Function.update tapes i (cfg.workTapes 0),
        Function.update heads i (cfg.workTapePos 0), cfg.output⟩
```

`Turing.MultiTapeTM.oneTapeCfg` (definition, [line 232](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L232))

> The one-tape view of a configuration of a machine with `k` work tapes: the tape and head of
> tape `i`, with everything else as it is.

```lean
public def oneTapeCfg (i : Fin k) (cfg : Cfg k Symbol State input) :
    Cfg 1 Symbol State input
```

`Turing.MultiTapeTM.embed_oneTapeCfg` (lemma, [line 238](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L238))

> A configuration is its own one-tape view on tape `i`, placed back on tape `i`.

```lean
public lemma embed_oneTapeCfg (i : Fin k) (cfg : Cfg k Symbol State input) :
    embed (tapeEmb i) (oneTapeCfg i cfg) cfg.workTapes cfg.workTapePos = cfg
```

`Turing.MultiTapeTM.runFrom_tapeEmb` (lemma, [line 245](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L245))

> **Running a one-tape machine on work tape `i`.** The run is the run on the one-tape view of the
> configuration, placed back on tape `i`; every other tape and head keeps its starting value. Combine
> with `embed_tapeEmb` to read off the resulting configuration.

```lean
public lemma runFrom_tapeEmb (tm : MultiTapeTM 1 Symbol State) (i : Fin k)
    (cfg : Cfg k Symbol State input) (n : ℕ) :
    (tm.extendTapes (tapeEmb i)).runFrom cfg n =
      embed (tapeEmb i) (tm.runFrom (oneTapeCfg i cfg) n) cfg.workTapes cfg.workTapePos
```

`Turing.MultiTapeTM.TransformsTapes.tapeEmb` (theorem, [line 254](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L254))

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

`Turing.MultiTapeTM.noTapes` (definition, [line 284](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L284))

> The embedding of a machine without work tapes into a machine with `k` of them.

```lean
public def noTapes (k : ℕ) : Fin 0 ↪ Fin k
```

`Turing.MultiTapeTM.noTapesCfg` (definition, [line 287](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L287))

> The view of a configuration as a configuration of a machine without work tapes.

```lean
public def noTapesCfg (cfg : Cfg k Symbol State input) : Cfg 0 Symbol State input
```

`Turing.MultiTapeTM.embed_noTapes` (lemma, [line 292](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L292))

> A configuration without work tapes, placed in a machine with `k` of them, only contributes its
> state, its input head and its output.

```lean
public lemma embed_noTapes (cfg : Cfg 0 Symbol State input)
    (tapes : Fin k → ℤ → Option Symbol) (heads : Fin k → ℤ) :
    embed (noTapes k) cfg tapes heads = ⟨cfg.state, cfg.inputPos, tapes, heads, cfg.output⟩
```

`Turing.MultiTapeTM.embed_noTapesCfg` (lemma, [line 299](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L299))

> A configuration is its tapeless view, placed back on its tapes.

```lean
public lemma embed_noTapesCfg (cfg : Cfg k Symbol State input) :
    embed (noTapes k) (noTapesCfg cfg) cfg.workTapes cfg.workTapePos = cfg
```

`Turing.MultiTapeTM.runFrom_noTapes` (lemma, [line 305](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean#L305))

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

- [Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Plumbing/ExtendTapes.lean)
- [Declaration ledger](../../../../../../../sources/cslib/Cslib.Computability.Machines.Turing.MultiTape.Plumbing.ExtendTapes.json)
