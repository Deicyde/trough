---
catalog: module
lean: Cslib.Mech.LocalSig.Store, Cslib.Mech.LocalSig.Store.read, Cslib.Mech.LocalSig.Store.write, Cslib.Mech.LocalSig.Store.instGetElem, Cslib.Mech.LocalSig.Store.instHasSubstitution, Cslib.Mech.LocalSig.Store.read_def, Cslib.Mech.LocalSig.Store.write_def, Cslib.Mech.LocalSig.Store.ext, Cslib.Mech.LocalSig.Store.subst_apply, Cslib.Mech.LocalSig.Store.subst_apply_of_ne, Cslib.Mech.LocalSig.Store.getElem_subst, Cslib.Mech.LocalSig.Store.getElem_subst_self, Cslib.Mech.LocalSig.Store.getElem_subst_of_ne, Cslib.Mech.LocalSig.Store.subst_subst_self, Cslib.Mech.LocalSig.Store.subst_comm, Cslib.Mech.LocalSig.Store.AgreeOn, Cslib.Mech.LocalSig.Store.AgreeOn.refl, Cslib.Mech.LocalSig.Store.AgreeOn.symm, Cslib.Mech.LocalSig.Store.AgreeOn.mono, Cslib.Mech.LocalSig.Store.AgreeOn.antitone, Cslib.Mech.LocalSig.Store.agreeOn_subst
statement: formalized
proof: formalized
---

# Local stores

`Cslib.Languages.Mech.Common.LocalStore`, in [Cslib/Languages/Mech/Common/LocalStore.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean), by Fabrizio Montesi.

`Cslib.Mech.LocalSig.Store` (definition, [line 22](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L22))

> A local store.

```lean
def Store (L : LocalSig)
```

`Cslib.Mech.LocalSig.Store.read` (definition, [line 25](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L25))

> Read a typed variable in a local store. Results are stated with the notation `σ[x]`.

```lean
def Store.read {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) : α
```

`Cslib.Mech.LocalSig.Store.write` (definition, [line 29](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L29))

> Write a typed variable in a local store. Results are stated with the notation `σ[x := v]`.

```lean
def Store.write {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) (v : α) : L.Store
```

> ### Notation for local stores
>
> A store `σ` is read with `σ[x]` and written with `σ[x := v]`.

`Cslib.Mech.LocalSig.Store.instGetElem` (instance, [line 37](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L37))

> For any local store `σ`, `σ[x]` is the value of the variable `x` in `σ`.

```lean
instance Store.instGetElem {L : LocalSig} {α} : GetElem L.Store (L.Var α) α (fun _ _ => True)
```

`Cslib.Mech.LocalSig.Store.instHasSubstitution` (instance, [line 41](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L41))

> For any local store `σ`, `σ[x := v]` is the store obtained from `σ` by writing `v` in `x`.

```lean
instance Store.instHasSubstitution {L : LocalSig} {α} : HasSubstitution L.Store (L.Var α) α
```

`Cslib.Mech.LocalSig.Store.read_def` (theorem, [line 45](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L45))

```lean
theorem Store.read_def {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) :
    σ.read x = σ[x]
```

`Cslib.Mech.LocalSig.Store.write_def` (theorem, [line 49](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L49))

```lean
theorem Store.write_def {L : LocalSig} {α} (σ : L.Store) (x : L.Var α)
    (v : α) : σ.write x v = σ[x := v]
```

`Cslib.Mech.LocalSig.Store.ext` (theorem, [line 54](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L54))

> Two stores are equal if they agree on every read.

```lean
theorem Store.ext {L : LocalSig} {σ₁ σ₂ : L.Store} (h : ∀ α (x : L.Var α), σ₁[x] = σ₂[x]) :
    σ₁ = σ₂
```

`Cslib.Mech.LocalSig.Store.subst_apply` (theorem, [line 59](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L59))

> The value of a written store at a variable name.

```lean
theorem Store.subst_apply {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) (v : α) (y : L.VarName) :
    σ[x := v] y = if h : y = x.name then h ▸ x.has_type.mpr v else σ y
```

`Cslib.Mech.LocalSig.Store.subst_apply_of_ne` (theorem, [line 67](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L67))

> Writing a variable preserves the values of all other names.

```lean
theorem Store.subst_apply_of_ne {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) (v : α)
    {y : L.VarName} (h : y ≠ x.name) : σ[x := v] y = σ y
```

`Cslib.Mech.LocalSig.Store.getElem_subst` (theorem, [line 74](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L74))

> Reading a variable after a write. If the variable read has the name of the variable written,
> their types are equal and the written value is returned.

```lean
theorem Store.getElem_subst {L : LocalSig} {α β} (σ : L.Store) (x : L.Var α) (v : α) (y : L.Var β) :
    σ[x := v][y] =
      if h : y.name = x.name then cast (by rw [← x.has_type, ← y.has_type, h]) v else σ[y]
```

`Cslib.Mech.LocalSig.Store.getElem_subst_self` (theorem, [line 91](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L91))

> Reading a variable after writing it returns the written value.

```lean
theorem Store.getElem_subst_self {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) (v : α) :
    σ[x := v][x] = v
```

`Cslib.Mech.LocalSig.Store.getElem_subst_of_ne` (theorem, [line 98](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L98))

> Writing a variable does not affect reading another.

```lean
theorem Store.getElem_subst_of_ne {L : LocalSig} {α β} (σ : L.Store) (x : L.Var α) (a : α)
    (y : L.Var β) (h : y.name ≠ x.name) : σ[x := a][y] = σ[y]
```

`Cslib.Mech.LocalSig.Store.subst_subst_self` (theorem, [line 105](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L105))

> A later write to the same variable overrides an earlier write.

```lean
theorem Store.subst_subst_self {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) (a b : α) :
    σ[x := a][x := b] = σ[x := b]
```

`Cslib.Mech.LocalSig.Store.subst_comm` (theorem, [line 110](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L110))

> Writes to different variables commute.

```lean
theorem Store.subst_comm {L : LocalSig} {α β} (σ : L.Store) (x : L.Var α) (y : L.Var β) (a : α)
    (b : β) (h : x.name ≠ y.name) : σ[x := a][y := b] = σ[y := b][x := a]
```

`Cslib.Mech.LocalSig.Store.AgreeOn` (definition, [line 116](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L116))

> Two stores agree on a set of variable names if every variable with a name in the set has the
> same value in both.

```lean
def Store.AgreeOn {L : LocalSig} (σ₁ σ₂ : L.Store) (s : Finset L.VarName) : Prop
```

`Cslib.Mech.LocalSig.Store.AgreeOn.refl` (theorem, [line 119](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L119))

```lean
theorem Store.AgreeOn.refl {L : LocalSig} (σ : L.Store) (s : Finset L.VarName) : σ.AgreeOn σ s
```

`Cslib.Mech.LocalSig.Store.AgreeOn.symm` (theorem, [line 122](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L122))

```lean
theorem Store.AgreeOn.symm {L : LocalSig} {σ₁ σ₂ : L.Store} {s : Finset L.VarName}
    (h : σ₁.AgreeOn σ₂ s) : σ₂.AgreeOn σ₁ s
```

`Cslib.Mech.LocalSig.Store.AgreeOn.mono` (theorem, [line 126](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L126))

```lean
theorem Store.AgreeOn.mono {L : LocalSig} {σ₁ σ₂ : L.Store} {s t : Finset L.VarName}
    (hst : s ⊆ t) (h : σ₁.AgreeOn σ₂ t) : σ₁.AgreeOn σ₂ s
```

`Cslib.Mech.LocalSig.Store.AgreeOn.antitone` (theorem, [line 131](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L131))

> Agreement on a set implies agreement on every subset.

```lean
theorem Store.AgreeOn.antitone {L : LocalSig} {σ₁ σ₂ : L.Store} : Antitone (AgreeOn σ₁ σ₂ ·)
```

`Cslib.Mech.LocalSig.Store.agreeOn_subst` (theorem, [line 135](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean#L135))

> Writing a variable outside a set preserves agreement on the set.

```lean
theorem Store.agreeOn_subst {L : LocalSig} {α} (σ : L.Store) (x : L.Var α) (v : α)
    {s : Finset L.VarName} (h : x.name ∉ s) : σ[x := v].AgreeOn σ s
```

## Depends on

- [HasSubstitution](../../../foundations/syntax/hassubstitution.md)
- [Signatures and variables for local computation](basic.md)

## Sources

- [Cslib/Languages/Mech/Common/LocalStore.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/LocalStore.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Languages.Mech.Common.LocalStore.json)
