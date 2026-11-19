---
catalog: module
lean: Aesop.RulePattern, Aesop.RulePattern.boundPremises, Aesop.RulePattern.«open», Aesop.RulePattern.«match», Aesop.RulePattern.«elab»
statement: formalized
proof: formalized
---

# Aesop/RulePattern

`Aesop.RulePattern`, in [Aesop/RulePattern.lean](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern.lean), by Jannis Limperg.

`Aesop.RulePattern` (structure, [line 31](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern.lean#L31))

> A rule pattern. For a rule of type `∀ (x₀ : T₀) ... (xₙ : Tₙ), U`, a valid rule
> pattern is an expression `p` such that `x₀ : T₁, ..., xₙ : Tₙ ⊢ p : P`. Let
> `y₀, ..., yₖ` be those variables `xᵢ` on which `p` depends. When `p` matches an
> expression `e`, this means that `e` is defeq to `p` (where each `yᵢ` is replaced
> with a metavariable) and we obtain a substitution
>
>     {y₀ ↦ t₀ : T₀, y₁ ↦ t₁ : T₁[x₀ := t₀], ...}
>
> Now suppose we want to match the above rule type against a type `V` (where `V`
> is the target for an `apply`-like rule and a hypothesis type for a
> `forward`-like rule). To that end, we take `U` and replace each `xᵢ` where
> `xᵢ = yⱼ` with `tⱼ` and each `xᵢ` with `xᵢ ≠ yⱼ ∀ j` with a metavariable. The
> resulting expression `U'` is then matched against `V`.

```lean
structure RulePattern where
  /--
  An expression of the form `λ y₀ ... yₖ, p` representing the
  pattern.
  -/
  pattern : AbstractMVarsResult
  /--
  A partial map from the index set `{0, ..., n-1}` into `{0, ..., k-1}`. If
  `argMap[i] = j`, this indicates that when matching against the rule type, the
  instantiation `tⱼ` of `yⱼ` should be substituted for `xᵢ`.
  -/
  argMap : Array (Option Nat)
  /--
  A partial map from the level metavariables occurring in the rule to the
  pattern's level params.
  -/
  levelArgMap : Array (Option Nat)
  /--
  Discrimination tree keys for `p`.
  -/
  discrTreeKeys : Array DiscrTree.Key
  deriving Inhabited
```

`Aesop.RulePattern.boundPremises` (definition, [line 56](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern.lean#L56))

```lean
def boundPremises (pat : RulePattern) : Array Nat
```

`Aesop.RulePattern.«open»` (definition, [line 64](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern.lean#L64))

```lean
def «open» (pat : RulePattern) :
    MetaM (Array MVarId × Array LMVarId × Expr)
```

`Aesop.RulePattern.«match»` (definition, [line 72](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern.lean#L72))

```lean
def «match» (e : Expr) (pat : RulePattern) : BaseM (Option Substitution)
```

`Aesop.RulePattern.«elab»` (definition, [line 95](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern.lean#L95))

```lean
def «elab» (stx : Term) (rule : Expr) : TermElabM RulePattern
```

## Depends on

- [BaseM](../part-01/basem.md)

## Sources

- [Aesop/RulePattern.lean at 637fdbb8](https://github.com/leanprover-community/aesop/blob/637fdbb8689a3387a82568b07355231f892144d7/Aesop/RulePattern.lean)
- [Declaration ledger](../../../sources/aesop/Aesop.RulePattern.json)
