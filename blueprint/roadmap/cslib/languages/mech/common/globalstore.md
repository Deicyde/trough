---
catalog: module
lean: Cslib.Mech.Sig.Store, Cslib.Mech.Sig.Store.write, Cslib.Mech.Sig.Store.instHasSubstitution, Cslib.Mech.Sig.Store.write_def, Cslib.Mech.Sig.Store.subst_eq_update, Cslib.Mech.Sig.Store.subst_apply_self, Cslib.Mech.Sig.Store.subst_apply_of_ne, Cslib.Mech.Sig.Store.getElem_subst_self, Cslib.Mech.Sig.Store.getElem_subst_of_name_ne, Cslib.Mech.Sig.Store.subst_subst_self, Cslib.Mech.Sig.Store.subst_comm_of_ne, Cslib.Mech.Sig.Store.subst_comm_of_name_ne
statement: formalized
proof: formalized
---

# Global stores

`Cslib.Languages.Mech.Common.GlobalStore`, in [Cslib/Languages/Mech/Common/GlobalStore.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean), by Fabrizio Montesi.

`Cslib.Mech.Sig.Store` (abbreviation, [line 21](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L21))

> A global store represents the memory state of an entire network, mapping each process to a
> local store of its own local signature.

```lean
abbrev Store {Pid} (S : Sig Pid)
```

`Cslib.Mech.Sig.Store.write` (definition, [line 25](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L25))

> Write the local variable `x` of process `p`. Results are stated with the notation
> `gs[⟨p, x⟩ := v]`.

```lean
def Store.write {Pid} [DecidableEq Pid] {S : Sig Pid} {α}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (v : α) : S.Store
```

> ### Notation for global stores
>
> We define notation for read and write operations on global stores. For any global store `gs`:
> - `(gs p)[x]` reads the value of variable `x` at process `p`;
> - `gs[⟨p, x⟩ := v]` writes the value `v` in variable `x` at process `p`.

`Cslib.Mech.Sig.Store.instHasSubstitution` (instance, [line 38](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L38))

> Instance for the write notation `gs[⟨p, x⟩ := v]`.

```lean
instance Store.instHasSubstitution {Pid} [DecidableEq Pid] {S : Sig Pid} {α} :
    HasSubstitution S.Store ((p : Pid) × S.Var p α) α
```

`Cslib.Mech.Sig.Store.write_def` (theorem, [line 43](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L43))

```lean
theorem Store.write_def {Pid} [DecidableEq Pid] {S : Sig Pid} {α}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (v : α) : gs.write p x v = gs[⟨p, x⟩ := v]
```

`Cslib.Mech.Sig.Store.subst_eq_update` (theorem, [line 46](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L46))

```lean
theorem Store.subst_eq_update {Pid} [DecidableEq Pid] {S : Sig Pid} {α}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (v : α) :
    gs[⟨p, x⟩ := v] = Function.update gs p ((gs p)[x := v])
```

`Cslib.Mech.Sig.Store.subst_apply_self` (theorem, [line 52](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L52))

> The local store of a process after a write operation at that process.

```lean
theorem Store.subst_apply_self {Pid} [DecidableEq Pid] {S : Sig Pid} {α}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (v : α) : gs[⟨p, x⟩ := v] p = (gs p)[x := v]
```

`Cslib.Mech.Sig.Store.subst_apply_of_ne` (theorem, [line 58](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L58))

> Stores writes are local: writing at one process does not affect the store of another process.

```lean
theorem Store.subst_apply_of_ne {Pid} [DecidableEq Pid] {S : Sig Pid} {α}
    (gs : S.Store) (p q : Pid) (x : S.Var p α) (v : α) (h : q ≠ p) :
    gs[⟨p, x⟩ := v] q = gs q
```

`Cslib.Mech.Sig.Store.getElem_subst_self` (theorem, [line 65](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L65))

> Reading a variable just written returns the written value.

```lean
theorem Store.getElem_subst_self {Pid} [DecidableEq Pid] {S : Sig Pid} {α}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (v : α) : (gs[⟨p, x⟩ := v] p)[x] = v
```

`Cslib.Mech.Sig.Store.getElem_subst_of_name_ne` (theorem, [line 71](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L71))

> Writing one variable preserves the value of another variable of the same process.

```lean
theorem Store.getElem_subst_of_name_ne {Pid} [DecidableEq Pid] {S : Sig Pid} {α β}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (a : α) (y : S.Var p β) (h : y.name ≠ x.name) :
    (gs[⟨p, x⟩ := a] p)[y] = (gs p)[y]
```

`Cslib.Mech.Sig.Store.subst_subst_self` (theorem, [line 78](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L78))

> A later write to the same process and variable overrides an earlier write.

```lean
theorem Store.subst_subst_self {Pid} [DecidableEq Pid] {S : Sig Pid} {α}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (a b : α) :
    gs[⟨p, x⟩ := a][⟨p, x⟩ := b] = gs[⟨p, x⟩ := b]
```

`Cslib.Mech.Sig.Store.subst_comm_of_ne` (theorem, [line 84](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L84))

> Writes to distinct processes commute.

```lean
theorem Store.subst_comm_of_ne {Pid} [DecidableEq Pid] {S : Sig Pid} {α β}
    (gs : S.Store) (p q : Pid) (x : S.Var p α) (y : S.Var q β) (a : α) (b : β) (h : p ≠ q) :
    gs[⟨p, x⟩ := a][⟨q, y⟩ := b] = gs[⟨q, y⟩ := b][⟨p, x⟩ := a]
```

`Cslib.Mech.Sig.Store.subst_comm_of_name_ne` (theorem, [line 91](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean#L91))

> Writes to different variables of the same process commute.

```lean
theorem Store.subst_comm_of_name_ne {Pid} [DecidableEq Pid] {S : Sig Pid} {α β}
    (gs : S.Store) (p : Pid) (x : S.Var p α) (y : S.Var p β) (a : α) (b : β)
    (h : x.name ≠ y.name) : gs[⟨p, x⟩ := a][⟨p, y⟩ := b] = gs[⟨p, y⟩ := b][⟨p, x⟩ := a]
```

## Depends on

- [Local stores](localstore.md)

## Sources

- [Cslib/Languages/Mech/Common/GlobalStore.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/GlobalStore.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Languages.Mech.Common.GlobalStore.json)
