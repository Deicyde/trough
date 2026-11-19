---
catalog: module
lean: Aesop.Substitution, Aesop.Substitution.empty, Aesop.Substitution.insert, Aesop.Substitution.find?, Aesop.Substitution.insertLevel, Aesop.Substitution.findLevel?, Aesop.Substitution.mergeCompatible, Aesop.Substitution.containsHyp, Aesop.Substitution.openRuleType, Aesop.Substitution.specializeRule, Aesop.openRuleType
statement: formalized
proof: formalized
---

# Substitution

`Aesop.Forward.Substitution`, in [Aesop/Forward/Substitution.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean), by Jannis Limperg.

`Aesop.Substitution` (structure, [line 24](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L24))

> A substitution for the premises of a rule. Given a rule with type
> `∀ (x₁ : T₁) ... (xₙ : Tₙ), U` a substitution is a finite partial map with
> domain `{1, ..., n}` that associates an expression with some or all of the
> premises.

```lean
structure Substitution where
  /-- The substitution. -/
  premises : Array (Option Expr)
  /-- The level substitution implied by the premise substitution. If `e` is the
  elaborated rule expression (with level params replaced by level mvars), and
  `collectLevelMVars (← instantiateMVars e) = [?m₁, ..., ?mₙ]`, then `levels[i]`
  is the level assigned to `?mᵢ`. -/
  levels : Array (Option Level)
  deriving Inhabited
```

`Aesop.Substitution.empty` (definition, [line 58](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L58))

> The empty substitution for a rule with the given number of premise
> indexes.

```lean
def empty (numPremises numLevels : Nat) : Substitution
```

`Aesop.Substitution.insert` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L64))

> Insert the mapping `pi ↦ inst` into the substitution `s`. Precondition: `pi`
> is in the domain of `s`.

```lean
def insert (pi : PremiseIndex) (inst : Expr) (s : Substitution) :
    Substitution
```

`Aesop.Substitution.find?` (definition, [line 70](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L70))

> Get the instantiation associated with premise `pi` in `s`. Precondition:
> `pi` is in the domain of `s`.

```lean
def find? (pi : PremiseIndex) (s : Substitution) : Option Expr
```

`Aesop.Substitution.insertLevel` (definition, [line 75](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L75))

> Insert the mapping `li ↦ inst` into the substitution `s`. Precondition: `li`
> is in the domain of `s` and `inst` is normalised.

```lean
def insertLevel (li : LevelIndex) (inst : Level) (s : Substitution) :
    Substitution
```

`Aesop.Substitution.findLevel?` (definition, [line 81](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L81))

> Get the instantiation associated with level `li` in `s`. Precondition:
> `li` is in the domain of `s`.

```lean
def findLevel? (li : PremiseIndex) (s : Substitution) : Option Level
```

`Aesop.Substitution.mergeCompatible` (definition, [line 94](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L94))

> Merge two substitutions. Precondition: the substitutions are compatible, so
> they must have the same size and if `s₁[x]` and `s₂[x]` are both defined, they
> must be defeq.

```lean
def mergeCompatible (s₁ s₂ : Substitution) : Substitution
```

`Aesop.Substitution.containsHyp` (definition, [line 109](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L109))

> Returns `true` if any expression in the codomain of `s` contains `hyp`.

```lean
def containsHyp (hyp : FVarId) (s : Substitution) : Bool
```

`Aesop.Substitution.openRuleType` (definition, [line 120](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L120))

> Given `e` with type `∀ (x₁ : T₁) ... (xₙ : Tₙ), U` and a substitution `σ`
> for the arguments `xᵢ`, replace occurrences of `xᵢ` in the body `U` with fresh
> metavariables (like `forallMetaTelescope`). Then, for each mapping `xᵢ ↦ tᵢ` in
> `σ`, assign `tᵢ` to the metavariable corresponding to `xᵢ`. Returns the newly
> created metavariables (which may be assigned!), their binder infos and the
> updated body.

```lean
def openRuleType (e : Expr) (subst : Substitution) :
    MetaM (Array MVarId × Array BinderInfo × Expr)
```

`Aesop.Substitution.specializeRule` (definition, [line 142](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L142))

> Given `rule` of type `∀ (x₁ : T₁) ... (xₙ : Tₙ), U` and a substitution `σ` for
> the arguments `xᵢ`, specialise `rule` with the arguments given by `σ`. That is,
> construct `U t₁ ... tₙ` where `tⱼ` is `σ(xⱼ)` if `xⱼ ∈ dom(σ)` and is otherwise
> a fresh fvar, then λ-abstract the fresh fvars.

```lean
def specializeRule (rule : Expr) (subst : Substitution) : MetaM Expr
```

`Aesop.openRuleType` (definition, [line 166](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean#L166))

> Open the type of a rule `e`. If a substitution `σ` is given, this function
> acts like `Substitution.openRuleType σ`. Otherwise it acts like
> `forallMetaTelescope`.

```lean
def openRuleType (subst? : Option Substitution) (e : Expr) :
    MetaM (Array MVarId × Array BinderInfo × Expr)
```

## Depends on

- [LevelIndex](levelindex.md)
- [PremiseIndex](premiseindex.md)

## Proof depends on

- [Util/Basic](../util/basic.md)

## Sources

- [Aesop/Forward/Substitution.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/Forward/Substitution.lean)
- [Declaration ledger](../../../../sources/aesop/Aesop.Forward.Substitution.json)
