---
catalog: module
lean: Cslib.FreeM.timeMRet_liftM, Cslib.FreeM.eval, Cslib.FreeM.cost, Cslib.FreeM.countQueries, Cslib.FreeM.eval_pure, Cslib.FreeM.eval_liftBind, Cslib.FreeM.eval_lift, Cslib.FreeM.eval_bind, Cslib.FreeM.eval_map, Cslib.FreeM.isMonadHom_pure_eval, Cslib.FreeM.cost_pure, Cslib.FreeM.cost_liftBind, Cslib.FreeM.cost_lift, Cslib.FreeM.cost_bind, Cslib.FreeM.cost_map, Cslib.FreeM.countQueries_pure, Cslib.FreeM.countQueries_liftBind, Cslib.FreeM.countQueries_lift, Cslib.FreeM.countQueries_bind, Cslib.FreeM.countQueries_map, Cslib.FreeM.countQueries_eq_cost_one, Cslib.FreeM.countQueries_ite, Cslib.FreeM.countQueries_dite, Cslib.FreeM.exists_countQueries_ge_clog
statement: formalized
proof: formalized
---

# FreeM: query/cost interpreters and lower-bound lemma

`Cslib.Algorithms.Lean.Query.FreeM`, in [Cslib/Algorithms/Lean/Query/FreeM.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean), by Sebastian Graf, Kim Morrison, Shreyas Srinivas, Eric Wieser.

> This file adds query-complexity interpreters to `FreeM F α`, where the type constructor
> `F : Type u → Type v` represents a query type mapping each query to its response type.
>
> The key operations are:
> - `FreeM.eval oracle p`: evaluate `p` by answering each query using `oracle`
> - `FreeM.countQueries oracle p`: count queries along the oracle-determined path
> - `FreeM.cost oracle weight p`: weighted query cost in any additive monoid
>
> The program `p` must be fixed independently of `oracle`. Arbitrary pure computation embedded
> in `p` is uncharged, so `countQueries` and `cost` measure query complexity rather than total
> runtime. However, pure code cannot inspect oracle responses: those enter only through
> `FreeM.lift`.
>
> This provides an alternative to the `TimeM`-based cost analysis in
> `Cslib.Algorithms.Lean.MergeSort.MergeSort`: here query counting is structural (derived from
> the `FreeM` tree) rather than annotation-based.
>
> The combinatorial lower-bound lemma `FreeM.exists_countQueries_ge_clog` says: if `n` distinct
> oracles produce `n` distinct evaluation results from a program whose every response type has
> cardinality at most `r`, then some oracle makes at least `⌈log_r n⌉` queries. The proof uses
> the adversarial/partition argument: at each query node, the oracles split by their answer,
> and the largest fiber still produces distinct results in the corresponding subtree.
>
> ## Setting up your own query type
>
> 1. Define an inductive `Q : Type u → Type v` whose constructors are the queries, indexed by
>    their response types (see `LEQuery`, `ArithQuery`).
> 2. Wrap each constructor with `FreeM.lift` to obtain one-step programs (`LEQuery.ask`).
> 3. Write algorithms in `do`-notation as values of `FreeM Q α`.
> 4. Prove correctness by relating `FreeM.eval` to a reference implementation, and bounds by
>    equational reasoning with the `countQueries`/`cost` simp lemmas; state them with
>    `Cslib.Query.UpperBound`/`Cslib.Query.LowerBound`.

`Cslib.FreeM.timeMRet_liftM` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L65))

> `TimeM.ret` distributes across `FreeM.liftM`.

```lean
theorem timeMRet_liftM {T : Type t} [AddMonoid T] (interp : {ι : Type u} → F ι → TimeM T ι)
    (p : FreeM F α) :
    (p.liftM interp).ret = Id.run (p.liftM fun i => pure (interp i).ret)
```

> ## Interpreters
>
> All three interpreters (`eval`, `cost`, `countQueries`) are defined as `liftM` interpretations
> into target monads, routing them through the universal property of the free monad rather
> than direct pattern-match on `FreeM`'s constructors:
>
> - `eval` interprets into `Id`.
> - `cost` interprets into a `TimeM` accumulator monad (a value paired with a running cost in
>   an arbitrary additive monoid).
> - `countQueries` is `cost` with unit weight.
>
> The pure and lift-then-bind simp lemmas (`eval_pure`, `eval_liftBind`, `cost_pure`,
> `cost_liftBind`, `countQueries_pure`, `countQueries_liftBind`) all reduce by `rfl`, giving the
> same proof ergonomics as direct pattern-match definitions while honouring the universal
> property as the primary abstraction.

`Cslib.FreeM.eval` (definition, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L88))

> Evaluate a program by answering each query using `oracle`.
> Defined as `liftM` to `Id`, the canonical interpreter into pure values.

```lean
def eval (oracle : {ι : Type u} → F ι → ι) (p : FreeM F α) : α
```

`Cslib.FreeM.cost` (definition, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L93))

> Weighted query cost in an additive monoid: each query has a cost given by `weight`,
> accumulated along the oracle-determined path. Defined as `liftM` into `TimeM`.

```lean
def cost {T : Type t} [AddMonoid T] (oracle : {ι : Type u} → F ι → ι)
(weight : {ι : Type u} → F ι → T) (p : FreeM F α) : T
```

`Cslib.FreeM.countQueries` (definition, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L101))

> Count the number of queries along the path determined by `oracle`.
>
> This is deliberately a `def` with its own simp lemmas, rather than an abbreviation for
> `cost oracle (fun _ => 1)`, so that goals display `countQueries`.

```lean
def countQueries (oracle : {ι : Type u} → F ι → ι) (p : FreeM F α) : Nat
```

> ### Simp lemmas for `eval`

`Cslib.FreeM.eval_pure` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L106))

```lean
theorem eval_pure (oracle : {ι : Type u} → F ι → ι) (a : α) :
eval oracle (pure a : FreeM F α) = a
```

`Cslib.FreeM.eval_liftBind` (theorem, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L109))

```lean
theorem eval_liftBind (oracle : {ι : Type u} → F ι → ι)
{ι : Type u} (op : F ι) (cont : ι → FreeM F α) :
eval oracle (FreeM.lift op >>= cont) = eval oracle (cont (oracle op))
```

`Cslib.FreeM.eval_lift` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L113))

```lean
theorem eval_lift (oracle : {ι : Type u} → F ι → ι) {ι : Type u} (op : F ι) :
eval oracle (FreeM.lift op) = oracle op
```

`Cslib.FreeM.eval_bind` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L116))

```lean
theorem eval_bind (oracle : {ι : Type u} → F ι → ι)
(t : FreeM F α) (f : α → FreeM F β) :
eval oracle (t >>= f) = eval oracle (f (eval oracle t))
```

`Cslib.FreeM.eval_map` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L121))

```lean
theorem eval_map (oracle : {ι : Type u} → F ι → ι)
(t : FreeM F α) (f : α → β) :
eval oracle (f <$> t) = f (eval oracle t)
```

`Cslib.FreeM.isMonadHom_pure_eval` (theorem, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L126))

```lean
theorem isMonadHom_pure_eval (oracle : {ι : Type u} → F ι → ι) :
    IsMonadHom (FreeM F) Id (fun x => pure (x.eval oracle))
```

> ### Simp lemmas for `cost`

`Cslib.FreeM.cost_pure` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L132))

```lean
theorem cost_pure {T : Type t} [AddMonoid T] (oracle : {ι : Type u} → F ι → ι)
(weight : {ι : Type u} → F ι → T) (a : α) :
cost oracle weight (pure a : FreeM F α) = 0
```

`Cslib.FreeM.cost_liftBind` (theorem, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L136))

```lean
theorem cost_liftBind {T : Type t} [AddMonoid T]
(oracle : {ι : Type u} → F ι → ι) (weight : {ι : Type u} → F ι → T)
{ι : Type u} (op : F ι) (cont : ι → FreeM F α) :
cost oracle weight (FreeM.lift op >>= cont) =
weight op + cost oracle weight (cont (oracle op))
```

`Cslib.FreeM.cost_lift` (theorem, [line 142](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L142))

```lean
theorem cost_lift {T : Type t} [AddMonoid T]
(oracle : {ι : Type u} → F ι → ι) (weight : {ι : Type u} → F ι → T)
{ι : Type u} (op : F ι) :
cost oracle weight (FreeM.lift op) = weight op
```

`Cslib.FreeM.cost_bind` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L148))

```lean
theorem cost_bind {T : Type t} [AddMonoid T] (oracle : {ι : Type u} → F ι → ι)
(weight : {ι : Type u} → F ι → T) (t : FreeM F α) (f : α → FreeM F β) :
cost oracle weight (t >>= f) =
cost oracle weight t + cost oracle weight (f (eval oracle t))
```

`Cslib.FreeM.cost_map` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L154))

```lean
theorem cost_map {T : Type t} [AddMonoid T]
(oracle : {ι : Type u} → F ι → ι) (weight : {ι : Type u} → F ι → T)
(t : FreeM F α) (f : α → β) :
cost oracle weight (f <$> t) = cost oracle weight t
```

> ### Simp lemmas for `countQueries`

`Cslib.FreeM.countQueries_pure` (theorem, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L162))

```lean
theorem countQueries_pure (oracle : {ι : Type u} → F ι → ι) (a : α) :
countQueries oracle (pure a : FreeM F α) = 0
```

`Cslib.FreeM.countQueries_liftBind` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L165))

```lean
theorem countQueries_liftBind (oracle : {ι : Type u} → F ι → ι)
{ι : Type u} (op : F ι) (cont : ι → FreeM F α) :
countQueries oracle (FreeM.lift op >>= cont) =
1 + countQueries oracle (cont (oracle op))
```

`Cslib.FreeM.countQueries_lift` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L170))

```lean
theorem countQueries_lift (oracle : {ι : Type u} → F ι → ι)
{ι : Type u} (op : F ι) :
countQueries oracle (FreeM.lift op) = 1
```

`Cslib.FreeM.countQueries_bind` (theorem, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L175))

```lean
theorem countQueries_bind (oracle : {ι : Type u} → F ι → ι)
(t : FreeM F α) (f : α → FreeM F β) :
countQueries oracle (t >>= f) =
countQueries oracle t + countQueries oracle (f (eval oracle t))
```

`Cslib.FreeM.countQueries_map` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L181))

```lean
theorem countQueries_map (oracle : {ι : Type u} → F ι → ι)
(t : FreeM F α) (f : α → β) :
countQueries oracle (f <$> t) = countQueries oracle t
```

`Cslib.FreeM.countQueries_eq_cost_one` (theorem, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L186))

```lean
theorem countQueries_eq_cost_one (oracle : {ι : Type u} → F ι → ι) (p : FreeM F α) :
    countQueries oracle p = cost oracle (fun _ => 1) p
```

`Cslib.FreeM.countQueries_ite` (theorem, [line 190](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L190))

```lean
theorem countQueries_ite (oracle : {ι : Type u} → F ι → ι) (P : Prop) [Decidable P]
    (p q : FreeM F α) :
    (if P then p else q).countQueries oracle =
      if P then p.countQueries oracle else q.countQueries oracle
```

`Cslib.FreeM.countQueries_dite` (theorem, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L197))

```lean
theorem countQueries_dite (oracle : {ι : Type u} → F ι → ι) (P : Prop) [Decidable P]
    (p : P → FreeM F α) (q : ¬P → FreeM F α) :
    (if h : P then p h else q h).countQueries oracle =
      if h : P then (p h).countQueries oracle else (q h).countQueries oracle
```

> ## Combinatorial lower bound

`Cslib.FreeM.exists_countQueries_ge_clog` (theorem, [line 291](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean#L291))

> If `n` oracles produce `n` distinct evaluation results from a `FreeM F α` program
> whose every response type has cardinality at most `r` (and hence is finite), then some
> oracle makes at least `⌈log_r n⌉` queries.
>
> This is the core combinatorial lemma for query complexity lower bounds. The proof uses
> the adversarial/partition argument: at each query node, the `n` oracles split by their
> answer; the largest group (size ≥ ⌈n/r⌉) still produces distinct results in the
> corresponding subtree, and the induction proceeds there.

```lean
theorem exists_countQueries_ge_clog (r : Nat)
    (h_card : ∀ {ρ : Type u}, F ρ → #ρ ≤ r)
    (p : FreeM F α) {n : Nat}
    (oracles : Fin n → ({ρ : Type u} → F ρ → ρ))
    (hn : 0 < n)
    (h_inj : Function.Injective (fun i => p.eval (oracles i))) :
    ∃ i : Fin n, p.countQueries (oracles i) ≥ Nat.clog r n
```

## Depends on

- [TimeM: Time Complexity Monad](../timem.md)
- [Free Monad (Free)](../../../foundations/control/monad/free.md)

## Sources

- [Cslib/Algorithms/Lean/Query/FreeM.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Algorithms/Lean/Query/FreeM.lean)
