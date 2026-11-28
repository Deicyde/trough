---
catalog: module
lean: ProofWanted, ProofWanted.Stmt, DefWanted, DefWanted.Val, DerivedWanted, elabWantedRef, «theorem_wanted», «proof_wanted», «def_wanted», elabTheoremWanted, elabProofWanted, elabDefWanted, «instance_wanted», elabInstanceWanted
statement: formalized
proof: formalized
---

# The `theorem_wanted`, `def_wanted`, and `instance_wanted` commands

`Batteries.Util.ProofWanted`, in [Batteries/Util/ProofWanted.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean), by David Thrane Christiansen, Kim Morrison.

> Use `theorem_wanted name binders : T` to mark a theorem the library should eventually contain
> without blocking compilation; `def_wanted name binders : T` does the same for any
> `Sort`, not just `Prop`. Each elaborates to a private placeholder `def name binders : ProofWanted
> T := ⟨⟩` (resp. `DefWanted T`), so the wanted result is visible to downstream files and
> tools by type rather than by side-channel. `proof_wanted` is a synonym for `theorem_wanted`.
>
> Inside any of these commands, `❰foo❱` references an earlier wanted declaration; for parametrised
> `foo`, write `❰foo❱ x y` to apply it. When the referenced wanted's payload is a typeclass, the
> generated parameter is an instance binder, so Lean's instance synth can pick it up at use sites
> (including via Π-instance synth when chained through another wanted).
>
> A body may be supplied with `... := body`; it must reference at least one `❰…❱` (in the statement or
> the body). A complete proof, construction, or instance should be a `theorem`, `def`, or `instance`
> instead, and the error includes a `Try this:` suggestion to that effect.
>
> There are two flavours of wanted declaration:
>
> * **Opaque holes** — a bodyless `def_wanted`/`theorem_wanted`/`instance_wanted` (and any
>   `theorem_wanted`/`proof_wanted`/`instance_wanted`, with or without a body). These elaborate to a
>   private placeholder `def foo binders : DefWanted T := ⟨⟩` (resp. `ProofWanted T`). A `❰foo❱`
>   reference desugars to a fresh parameter binder of type `DefWanted.Val (@foo …)` (resp. `.Stmt`),
>   so `foo` appears in the recorded type but is never inhabited.
> * **Transparent (derived) defs** — a `def_wanted` *with a body*. This elaborates to a genuine
>   `@[reducible] def foo binders : DerivedWanted T := ⟨body⟩`, and `❰foo❱` *inlines* it (projecting
>   the carried value with `.val`), so `❰foo❱` is definitionally equal to `body`. This lets you build
>   honest accessors and derived data on top of opaque holes — e.g. project a field out of a bundled
>   wanted, with the projection actually reducing downstream — while the `DerivedWanted` wrapper keeps
>   the declaration from being used directly as a value of `T` (only `❰…❱` accesses it).
>
> Either way, a `❰foo❱` reference surfaces `foo`'s own transitive *leaf*-hole dependencies as binders
> on the referencing declaration, threading them through; opaque holes stay as `d_…`/`h_…` binders,
> transparent intermediates are inlined away. Because the only un-filled pieces are opaque
> `DefWanted`/`ProofWanted` placeholders (never `axiom`/`sorry`), the whole construction is sound: a
> transparent def is a real definition *parametrised over* its hypothetical leaves.
>
> `instance_wanted name : ClassT` is a variant of `def_wanted` whose payload must be a typeclass and
> whose declared name is registered file-locally, so a later wanted can use it via typeclass synth
> without an explicit `❰…❱` reference. Inclusion is *on use* (like `variable [inst]`): a later
> declaration carries the instance binder only when its statement or body actually needs it, not
> unconditionally. (It is always an opaque hole, even with a body.)
>
> The `❰` and `❱` characters (U+2770, U+2771) are entered as `\h<` and `\h>` with the standard
> Lean input method.

`ProofWanted` (structure, [line 61](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L61))

> Wrapper recording that a `proof_wanted` of statement `α` has been declared.

```lean
public structure ProofWanted (α : Sort u) : Type where
  /-- The trivial constructor; carries no information. -/
  mk ::
```

`ProofWanted.Stmt` (definition, [line 68](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L68))

> Reducible accessor so a binder of type `ProofWanted.Stmt foo` reduces to `foo`'s
> statement. Used by the desugaring of `❰foo❱` when `foo` is a `proof_wanted`.

```lean
public def ProofWanted.Stmt {α : Sort u} (_ : ProofWanted α) : Sort u
```

`DefWanted` (structure, [line 71](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L71))

> Wrapper recording that a `def_wanted` of type `α` has been declared.

```lean
public structure DefWanted (α : Sort u) : Type where
  /-- The trivial constructor; carries no information. -/
  mk ::
```

`DefWanted.Val` (definition, [line 78](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L78))

> Reducible accessor so a binder of type `DefWanted.Val foo` reduces to `foo`'s
> type. Used by the desugaring of `❰foo❱` when `foo` is a `def_wanted`.

```lean
public def DefWanted.Val {α : Sort u} (_ : DefWanted α) : Sort u
```

`DerivedWanted` (structure, [line 87](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L87))

> Wrapper carrying the body of a *transparent* `def_wanted` (one given a `:= body`). Unlike the
> empty `DefWanted`, it stores the value, so `❰foo❱` projects it back out and downstream definitional
> equalities go through; but the placeholder still has type `DerivedWanted T`, not `T`, so it
> cannot be used directly as an inhabitant of `T` — the intended access is via the `❰…❱` syntax,
> which projects
> the value back out. (`val` is `public`, so direct projection is possible, but `❰…❱` is what callers
> should use.)

```lean
public structure DerivedWanted (α : Sort u) : Sort (max 1 u) where
  ofVal ::
  /-- The carried value. Reference the declaration via `❰…❱` rather than projecting this
  directly. -/
  val : α
```

`elabWantedRef` (definition, [line 104](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L104))

> Elaborator that errors when `❰…❱` is used outside a wanted-declaration command.

```lean
def elabWantedRef : Term.TermElab
```

`«theorem_wanted»` (definition, [line 686](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L686))

> …

```lean
def «theorem_wanted»
```

`«proof_wanted»` (definition, [line 694](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L694))

> `proof_wanted` is a synonym for `theorem_wanted`; see its documentation. (It is expected to be
> deprecated in favour of `theorem_wanted` eventually.)

```lean
def «proof_wanted»
```

`«def_wanted»` (definition, [line 724](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L724))

> …

```lean
def «def_wanted»
```

`elabTheoremWanted` (definition, [line 731](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L731))

> Parses the surface syntax of `theorem_wanted` and forwards to the shared `elabWanted`.

```lean
def elabTheoremWanted : CommandElab
```

`elabProofWanted` (definition, [line 740](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L740))

> Parses the surface syntax of `proof_wanted` (a synonym for `theorem_wanted`) and forwards to
> the shared `elabWanted`.

```lean
def elabProofWanted : CommandElab
```

`elabDefWanted` (definition, [line 748](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L748))

> Parses the surface syntax of `def_wanted` and forwards to the shared `elabWanted`.

```lean
def elabDefWanted : CommandElab
```

`«instance_wanted»` (definition, [line 783](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L783))

> …

```lean
def «instance_wanted»
```

`elabInstanceWanted` (definition, [line 823](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean#L823))

> Parses the surface syntax of `instance_wanted`, generates a name if absent, forwards to the
> shared `elabWanted`, validates the payload is a typeclass, and registers the declared name in
> `wantedInstancesExt` so subsequent wanted declarations auto-include it.

```lean
def elabInstanceWanted : CommandElab
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Util/ProofWanted.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Util/ProofWanted.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Util.ProofWanted.json)
