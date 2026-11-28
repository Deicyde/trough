---
catalog: module
lean: Batteries.Tactic.Lemma.checkLangLemmaCmd, Batteries.Tactic.Lemma.elabLemma
statement: formalized
proof: formalized
---

# Control for `lemma` command

`Batteries.Tactic.Lemma`, in [Batteries/Tactic/Lemma.lean](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Lemma.lean), by Johan Commelin, Damiano Testa.

> The `lemma` command exists in `Mathlib`, but not in `Std`.
>
> This file enforces the convention by introducing a code-action
> to replace `lemma` by `theorem`.

`Batteries.Tactic.Lemma.checkLangLemmaCmd` (definition, [line 33](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Lemma.lean#L33))

> Check whether `lang.lemmaCmd` option is enabled

```lean
def checkLangLemmaCmd (o : Options) : Bool
```

`Batteries.Tactic.Lemma.elabLemma` (definition, [line 41](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Lemma.lean#L41))

> Elaborator for the `lemma` command, if the option `lang.lemmaCmd` is false the command
> emits a warning and code action instructing the user to use `theorem` instead.

```lean
def elabLemma : CommandElab
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Tactic/Lemma.lean at dd0900df](https://github.com/leanprover-community/batteries/blob/dd0900df51045e7d9be143ed167c9d200bcf2b45/Batteries/Tactic/Lemma.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Tactic.Lemma.json)
