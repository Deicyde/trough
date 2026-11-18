---
catalog: module
lean: Cslib.FreeM.StateF, Cslib.FreeM.FreeState, Cslib.FreeM.FreeState.get_def, Cslib.FreeM.FreeState.set_def, Cslib.FreeM.FreeState.stateInterp, Cslib.FreeM.FreeState.toStateM, Cslib.FreeM.FreeState.toStateM_unique, Cslib.FreeM.FreeState.run, Cslib.FreeM.FreeState.run_toStateM, Cslib.FreeM.FreeState.run_pure, Cslib.FreeM.FreeState.run_get, Cslib.FreeM.FreeState.run_set, Cslib.FreeM.FreeState.run_bind, Cslib.FreeM.FreeState.run', Cslib.FreeM.FreeState.run'_toStateM, Cslib.FreeM.FreeState.run'_pure, Cslib.FreeM.FreeState.run'_get, Cslib.FreeM.FreeState.run'_set, Cslib.FreeM.FreeState.run'_bind, Cslib.FreeM.WriterF, Cslib.FreeM.FreeWriter, Cslib.FreeM.FreeWriter.writerInterp, Cslib.FreeM.FreeWriter.toWriterT, Cslib.FreeM.FreeWriter.toWriterT_unique, Cslib.FreeM.FreeWriter.tell, Cslib.FreeM.FreeWriter.tell_def, Cslib.FreeM.FreeWriter.run, Cslib.FreeM.FreeWriter.run_pure, Cslib.FreeM.FreeWriter.run_lift_tell, Cslib.FreeM.FreeWriter.run_bind, Cslib.FreeM.FreeWriter.run_toWriterT, Cslib.FreeM.FreeWriter.listen, Cslib.FreeM.FreeWriter.listen_pure, Cslib.FreeM.FreeWriter.listen_lift_tell_bind, Cslib.FreeM.FreeWriter.pass, Cslib.FreeM.FreeWriter.pass_def, Cslib.FreeM.ContF, Cslib.FreeM.FreeCont, Cslib.FreeM.FreeCont.contInterp, Cslib.FreeM.FreeCont.toContT, Cslib.FreeM.FreeCont.toContT_unique, Cslib.FreeM.FreeCont.run, Cslib.FreeM.FreeCont.run_pure, Cslib.FreeM.FreeCont.run_lift_callCC, Cslib.FreeM.FreeCont.run_bind, Cslib.FreeM.FreeCont.run_toContT, Cslib.FreeM.FreeCont.callCC, Cslib.FreeM.FreeCont.run_callCC, Cslib.FreeM.ReaderF, Cslib.FreeM.FreeReader, Cslib.FreeM.FreeReader.read_def, Cslib.FreeM.FreeReader.readInterp, Cslib.FreeM.FreeReader.toReaderM, Cslib.FreeM.FreeReader.toReaderM_unique, Cslib.FreeM.FreeReader.run, Cslib.FreeM.FreeReader.run_toReaderM, Cslib.FreeM.FreeReader.run_pure, Cslib.FreeM.FreeReader.run_read, Cslib.FreeM.FreeReader.run_bind, Cslib.FreeM.FreeReader.instMonadWithReaderOf, Cslib.FreeM.FreeReader.run_withReader
statement: formalized
proof: formalized
---

# Free Monad (Effects)

`Cslib.Foundations.Control.Monad.Free.Effects`, in [Cslib/Foundations/Control/Monad/Free/Effects.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean), by Tanner Duve.

> This file defines several canonical instances on the free monad.
>
> ## Main definitions
>
> - `FreeState`, `FreeWriter`, `FreeCont`, `FreeReader`: Specific effect monads
>
> ## Implementation
>
> To execute or interpret these computations, we provide two approaches:
> 1. **Hand-written interpreters** (`FreeState.run`, `FreeWriter.run`, `FreeCont.run`,
>   `FreeReader.run`) that directly
>   pattern-match on the tree structure
> 2. **Canonical interpreters** (`FreeState.toStateM`, `FreeWriter.toWriterT`, `FreeCont.toContT`,
>   `FreeReader.toReaderM`)
>   derived from the universal property via `liftM`
>
> We prove that these approaches are equivalent, demonstrating that the implementation aligns with
> the theory. We also provide uniqueness theorems for the canonical interpreters, which follow from
> the universal property.
>
> ## Tags
>
> Free monad, state monad, writer monad, continuation monad

> ### State Monad via `FreeM`

`Cslib.FreeM.StateF` (inductive type, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L51))

> Type constructor for state operations.

```lean
inductive StateF (σ : Type u) : Type u → Type u where
  /-- Get the current state. -/
  | get : StateF σ σ
  /-- Set the state. -/
  | set : σ → StateF σ PUnit
```

`Cslib.FreeM.FreeState` (abbreviation, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L58))

> State monad via the `FreeM` monad.

```lean
abbrev FreeState (σ : Type u)
```

`Cslib.FreeM.FreeState.get_def` (lemma, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L72))

```lean
lemma get_def : (get : FreeState σ σ) = .lift .get
```

`Cslib.FreeM.FreeState.set_def` (lemma, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L75))

```lean
lemma set_def (s : σ) : (set s : FreeState σ PUnit) = .lift (.set s)
```

`Cslib.FreeM.FreeState.stateInterp` (definition, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L79))

> Interpret `StateF` operations into `StateM`.

```lean
def stateInterp {α : Type u} : StateF σ α → StateM σ α
```

`Cslib.FreeM.FreeState.toStateM` (abbreviation, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L85))

> Convert a `FreeState` computation into a `StateM` computation. This is the canonical
> interpreter derived from `liftM`.

```lean
abbrev toStateM {α : Type u} (comp : FreeState σ α) : StateM σ α
```

`Cslib.FreeM.FreeState.toStateM_unique` (theorem, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L89))

> `toStateM` is the unique interpreter extending `stateInterp`.

```lean
theorem toStateM_unique {α : Type u} (g : FreeState σ α → StateM σ α)
    (h : Interprets stateInterp g) : g = toStateM
```

`Cslib.FreeM.FreeState.run` (definition, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L93))

> Run a state computation, returning both the result and final state.

```lean
def run (comp : FreeState σ α) (s₀ : σ) : α × σ
```

`Cslib.FreeM.FreeState.run_toStateM` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L104))

> The canonical interpreter `toStateM` derived from `liftM` agrees with the hand-written
> recursive interpreter `run` for `FreeState`.

```lean
theorem run_toStateM {α : Type u} (comp : FreeState σ α) (s₀ : σ) :
    (toStateM comp).run s₀ = pure (run comp s₀)
```

`Cslib.FreeM.FreeState.run_pure` (lemma, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L112))

```lean
lemma run_pure (a : α) (s₀ : σ) :
    run (pure a : FreeState σ α) s₀ = (a, s₀)
```

`Cslib.FreeM.FreeState.run_get` (lemma, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L116))

```lean
lemma run_get (s₀ : σ) :
    run (lift .get) s₀ = (s₀, s₀)
```

`Cslib.FreeM.FreeState.run_set` (lemma, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L120))

```lean
lemma run_set (s' : σ) (s₀ : σ) :
    run (lift (.set s')) s₀ = (.unit, s')
```

`Cslib.FreeM.FreeState.run_bind` (lemma, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L124))

```lean
lemma run_bind (x : FreeState σ α) (f : α → FreeState σ β) (s₀ : σ) :
    run (x.bind f) s₀ = let p := x.run s₀; (f p.1).run p.2
```

`Cslib.FreeM.FreeState.run'` (definition, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L133))

> Run a state computation, returning only the result.

```lean
def run' (c : FreeState σ α) (s₀ : σ) : α
```

`Cslib.FreeM.FreeState.run'_toStateM` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L136))

```lean
theorem run'_toStateM {α : Type u} (comp : FreeState σ α) (s₀ : σ) :
    (toStateM comp).run' s₀ = pure (run' comp s₀)
```

`Cslib.FreeM.FreeState.run'_pure` (lemma, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L142))

```lean
lemma run'_pure (a : α) (s₀ : σ) :
    run' (pure a : FreeState σ α) s₀ = a
```

`Cslib.FreeM.FreeState.run'_get` (lemma, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L146))

```lean
lemma run'_get (s₀ : σ) :
    run' (lift .get) s₀ = s₀
```

`Cslib.FreeM.FreeState.run'_set` (lemma, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L150))

```lean
lemma run'_set (s' : σ) (s₀ : σ) :
    run' (lift (.set s')) s₀ = .unit
```

`Cslib.FreeM.FreeState.run'_bind` (lemma, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L154))

```lean
lemma run'_bind (x : FreeState σ α) (f : α → FreeState σ β) (s₀ : σ) :
    run' (x.bind f) s₀ = let p := x.run s₀; (f p.1).run' p.2
```

> ### Writer Monad via `FreeM`

`Cslib.FreeM.WriterF` (inductive type, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L166))

> Type constructor for writer operations. Writer has a single effect, so the definition has just one
> constructor.

```lean
inductive WriterF (ω : Type u) : Type v → Type u
  /-- Write a value to the log. -/
  | tell : ω → WriterF ω PUnit
```

`Cslib.FreeM.FreeWriter` (abbreviation, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L172))

> Writer monad implemented via the `FreeM` monad construction. This provides a more efficient
> implementation than the traditional `WriterT` transformer, as it avoids buffering the log.

```lean
abbrev FreeWriter (ω : Type u)
```

`Cslib.FreeM.FreeWriter.writerInterp` (definition, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L181))

> Interpret `WriterF` operations into `WriterT`.

```lean
def writerInterp {α : Type u} : WriterF ω α → WriterT ω Id α
```

`Cslib.FreeM.FreeWriter.toWriterT` (abbreviation, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L186))

> Convert a `FreeWriter` computation into a `WriterT` computation. This is the canonical
> interpreter derived from `liftM`.

```lean
abbrev toWriterT {α : Type u} [Monoid ω] (comp : FreeWriter ω α) : WriterT ω Id α
```

`Cslib.FreeM.FreeWriter.toWriterT_unique` (theorem, [line 190](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L190))

> `toWriterT` is the unique interpreter extending `writerInterp`.

```lean
theorem toWriterT_unique {α : Type u} [Monoid ω] (g : FreeWriter ω α → WriterT ω Id α)
    (h : Interprets writerInterp g) : g = toWriterT
```

`Cslib.FreeM.FreeWriter.tell` (abbreviation, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L196))

> Writes a log entry. This creates an effectful node in the computation tree.

```lean
abbrev tell (w : ω) : FreeWriter ω PUnit
```

`Cslib.FreeM.FreeWriter.tell_def` (lemma, [line 200](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L200))

```lean
lemma tell_def (w : ω) :
    tell w = .lift (.tell w)
```

`Cslib.FreeM.FreeWriter.run` (definition, [line 207](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L207))

> Interprets a `FreeWriter` computation by recursively traversing the tree, accumulating
> log entries with the monoid operation, and returns the final value paired with the accumulated log.

```lean
def run [Monoid ω] : FreeWriter ω α → α × ω
```

`Cslib.FreeM.FreeWriter.run_pure` (lemma, [line 214](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L214))

```lean
lemma run_pure [Monoid ω] (a : α) :
    run (pure a : FreeWriter ω α) = (a, 1)
```

`Cslib.FreeM.FreeWriter.run_lift_tell` (lemma, [line 218](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L218))

```lean
lemma run_lift_tell [Monoid ω] (w : ω) :
    run (lift (.tell w)) = (.unit, w)
```

`Cslib.FreeM.FreeWriter.run_bind` (lemma, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L222))

```lean
lemma run_bind [Monoid ω] (x : FreeWriter ω α) (f : α → FreeWriter ω β) :
    run (x.bind f) = let p := run x; ((f p.1).run.1, p.2 * (f p.1).run.2)
```

`Cslib.FreeM.FreeWriter.run_toWriterT` (theorem, [line 236](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L236))

> The canonical interpreter `toWriterT` derived from `liftM` agrees with the hand-written
> recursive interpreter `run` for `FreeWriter`.

```lean
theorem run_toWriterT {α : Type u} [Monoid ω] (comp : FreeWriter ω α) :
    (toWriterT comp).run = pure (run comp)
```

`Cslib.FreeM.FreeWriter.listen` (definition, [line 250](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L250))

> `listen` captures the log produced by a subcomputation incrementally. It traverses the computation,
> emitting log entries as encountered, and returns the accumulated log as a result.

```lean
def listen [Monoid ω] : FreeWriter ω α → FreeWriter ω (α × ω)
```

`Cslib.FreeM.FreeWriter.listen_pure` (lemma, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L258))

```lean
lemma listen_pure [Monoid ω] (a : α) :
    listen (pure a : FreeWriter ω α) = .pure (a, 1)
```

`Cslib.FreeM.FreeWriter.listen_lift_tell_bind` (lemma, [line 262](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L262))

```lean
lemma listen_lift_tell_bind [Monoid ω] (w : ω)
    (k : PUnit → FreeWriter ω α) :
    listen (lift (.tell w) >>= k) =
      lift (.tell w) >>= (fun _ =>
        listen (k .unit) >>= fun (a, w') =>
          pure (a, w * w'))
```

`Cslib.FreeM.FreeWriter.pass` (definition, [line 275](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L275))

> `pass` allows a subcomputation to modify its own log. After traversing the computation and
> accumulating its log, the resulting function is applied to rewrite the accumulated log
> before re-emission.

```lean
def pass [Monoid ω] (m : FreeWriter ω (α × (ω → ω))) : FreeWriter ω α
```

`Cslib.FreeM.FreeWriter.pass_def` (lemma, [line 280](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L280))

```lean
lemma pass_def [Monoid ω] (m : FreeWriter ω (α × (ω → ω))) :
    pass m = let ((a, f), w) := run m; liftBind (.tell (f w)) fun _ => .pure a
```

> ### Continuation Monad via `FreeM`

`Cslib.FreeM.ContF` (inductive type, [line 293](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L293))

> Type constructor for continuation operations.

```lean
inductive ContF (r : Type u) (α : Type v) where
  /-- Call with current continuation: provides access to the current continuation. -/
  | callCC : ((α → r) → r) → ContF r α
```

`Cslib.FreeM.FreeCont` (abbreviation, [line 302](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L302))

> Continuation monad via the `FreeM` monad.

```lean
abbrev FreeCont (r : Type u)
```

`Cslib.FreeM.FreeCont.contInterp` (definition, [line 309](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L309))

> Interpret `ContF r` operations into `ContT r Id`.

```lean
def contInterp : ContF r α → ContT r Id α
```

`Cslib.FreeM.FreeCont.toContT` (abbreviation, [line 314](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L314))

> Convert a `FreeCont` computation into a `ContT` computation. This is the canonical
> interpreter derived from `liftM`.

```lean
abbrev toContT {α : Type u} (comp : FreeCont r α) : ContT r Id α
```

`Cslib.FreeM.FreeCont.toContT_unique` (theorem, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L318))

> `toContT` is the unique interpreter extending `contInterp`.

```lean
theorem toContT_unique {α : Type u} (g : FreeCont r α → ContT r Id α)
    (h : Interprets contInterp g) : g = toContT
```

`Cslib.FreeM.FreeCont.run` (definition, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L322))

> Run a continuation computation with the given continuation.

```lean
def run : FreeCont r α → (α → r) → r
```

`Cslib.FreeM.FreeCont.run_pure` (lemma, [line 327](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L327))

```lean
lemma run_pure (a : α) (k : α → r) :
    run (pure a : FreeCont r α) k = k a
```

`Cslib.FreeM.FreeCont.run_lift_callCC` (lemma, [line 331](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L331))

```lean
lemma run_lift_callCC (g : (α → r) → r) (k : α → r) :
    run (lift (.callCC g)) k = g k
```

`Cslib.FreeM.FreeCont.run_bind` (lemma, [line 335](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L335))

```lean
lemma run_bind (x : FreeCont r α) (f : α → FreeCont r β) (k : β → r) :
    run (x.bind f) k = run x (fun i => run (f i) k)
```

`Cslib.FreeM.FreeCont.run_toContT` (theorem, [line 349](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L349))

> The canonical interpreter `toContT` derived from `liftM` agrees with the hand-written
> recursive interpreter `run` for `FreeCont`.

```lean
theorem run_toContT {α : Type u} (comp : FreeCont r α) (k : α → r) :
    (toContT comp).run k = pure (run comp k)
```

`Cslib.FreeM.FreeCont.callCC` (definition, [line 360](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L360))

> Call with current continuation for the Free continuation monad.

```lean
def callCC (f : MonadCont.Label α (FreeCont r) β → FreeCont r α) :
    FreeCont r α
```

`Cslib.FreeM.FreeCont.run_callCC` (lemma, [line 369](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L369))

> `run` of a `callCC` node simplifies to running the handler with the current continuation.

```lean
lemma run_callCC (f : MonadCont.Label α (FreeCont r) β → FreeCont r α) (k : α → r) :
    run (callCC f) k = run (f ⟨fun x => lift (.callCC fun _ => k x)⟩) k
```

`Cslib.FreeM.ReaderF` (inductive type, [line 376](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L376))

> Type constructor for reader operations.

```lean
inductive ReaderF (σ : Type u) : Type u → Type u where
  | read : ReaderF σ σ
```

`Cslib.FreeM.FreeReader` (abbreviation, [line 380](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L380))

> Reader monad via the `FreeM` monad

```lean
abbrev FreeReader (σ)
```

`Cslib.FreeM.FreeReader.read_def` (lemma, [line 389](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L389))

```lean
lemma read_def : (read : FreeReader σ σ) = .lift .read
```

`Cslib.FreeM.FreeReader.readInterp` (definition, [line 395](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L395))

> Interpret `ReaderF` operations into `ReaderM`.

```lean
def readInterp {α : Type u} : ReaderF σ α → ReaderM σ α
```

`Cslib.FreeM.FreeReader.toReaderM` (abbreviation, [line 400](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L400))

> Convert a `FreeReader` computation into a `ReaderM` computation. This is the canonical
> interpreter derived from `liftM`.

```lean
abbrev toReaderM {α : Type u} (comp : FreeReader σ α) : ReaderM σ α
```

`Cslib.FreeM.FreeReader.toReaderM_unique` (theorem, [line 404](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L404))

> `toReaderM` is the unique interpreter extending `readInterp`.

```lean
theorem toReaderM_unique {α : Type u} (g : FreeReader σ α → ReaderM σ α)
    (h : Interprets readInterp g) : g = toReaderM
```

`Cslib.FreeM.FreeReader.run` (definition, [line 408](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L408))

> Run a reader computation

```lean
def run (comp : FreeReader σ α) (s₀ : σ) : α
```

`Cslib.FreeM.FreeReader.run_toReaderM` (theorem, [line 417](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L417))

> The canonical interpreter `toReaderM` derived from `liftM` agrees with the hand-written
> recursive interpreter `run` for `FreeReader`

```lean
theorem run_toReaderM {α : Type u} (comp : FreeReader σ α) (s : σ) :
    (toReaderM comp).run s = pure (run comp s)
```

`Cslib.FreeM.FreeReader.run_pure` (lemma, [line 425](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L425))

```lean
lemma run_pure (a : α) (s₀ : σ) :
    run (pure a : FreeReader σ α) s₀ = a
```

`Cslib.FreeM.FreeReader.run_read` (lemma, [line 429](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L429))

```lean
lemma run_read (s₀ : σ) :
    run read s₀ = s₀
```

`Cslib.FreeM.FreeReader.run_bind` (lemma, [line 433](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L433))

```lean
lemma run_bind (x : FreeReader σ α) (f : α → FreeReader σ β) (s₀ : σ) :
    run (x >>= f) s₀ = run (f <| run x s₀) s₀
```

`Cslib.FreeM.FreeReader.instMonadWithReaderOf` (instance, [line 438](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L438))

```lean
instance instMonadWithReaderOf : MonadWithReaderOf σ (FreeReader σ)
```

`Cslib.FreeM.FreeReader.run_withReader` (theorem, [line 446](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean#L446))

```lean
theorem run_withReader (f : σ → σ) (m : FreeReader σ α) (s : σ) :
    run (withTheReader σ f m) s = run m (f s)
```

## Depends on

- [Free Monad (Free)](../free.md)

## Sources

- [Cslib/Foundations/Control/Monad/Free/Effects.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Control/Monad/Free/Effects.lean)
