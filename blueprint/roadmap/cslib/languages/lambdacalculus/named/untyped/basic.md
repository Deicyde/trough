---
catalog: module
lean: Cslib.LambdaCalculus.Named.Untyped.Term, Cslib.LambdaCalculus.Named.Untyped.Term.fv, Cslib.LambdaCalculus.Named.Untyped.Term.bv, Cslib.LambdaCalculus.Named.Untyped.Term.vars, Cslib.LambdaCalculus.Named.Untyped.Term.rename, Cslib.LambdaCalculus.Named.Untyped.Term.rename_eq_sizeOf, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv, Cslib.LambdaCalculus.Named.Untyped.Term.instHasAlphaEquivTerm, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv_def, Cslib.LambdaCalculus.Named.Untyped.Term.Subst, Cslib.LambdaCalculus.Named.Untyped.Term.subst, Cslib.LambdaCalculus.Named.Untyped.Term.instHasSubstitutionTerm, Cslib.LambdaCalculus.Named.Untyped.Term.subst_def, Cslib.LambdaCalculus.Named.Untyped.Term.Context, Cslib.LambdaCalculus.Named.Untyped.Term.Context.fill, Cslib.LambdaCalculus.Named.Untyped.Term.Context.vars
statement: formalized
proof: formalized
---

# λ-calculus (Basic)

`Cslib.Languages.LambdaCalculus.Named.Untyped.Basic`, in [Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean), by Fabrizio Montesi, Haoxuan Yin.

> The untyped λ-calculus, with a named representation of variables. This file contains the definitions
> of α-equivalence and capture-avoiding substitution.
>
> ## References
>
> * [H. Barendregt, *Introduction to Lambda Calculus*][Barendregt1984]
> * Definition of α-equivalence [M. Gabbay and A. Pitts, *A New Approach to Abstract Syntax with
> Variable Binding*][Gabbay2002]

`Cslib.LambdaCalculus.Named.Untyped.Term` (inductive type, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L37))

> Syntax of terms.

```lean
inductive Term (Var : Type u) : Type u where
  | var (x : Var)
  | abs (x : Var) (m : Term Var)
  | app (m n : Term Var)
deriving DecidableEq
```

`Cslib.LambdaCalculus.Named.Untyped.Term.fv` (definition, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L47))

> Free variables.

```lean
def fv : Term Var → Finset Var
```

`Cslib.LambdaCalculus.Named.Untyped.Term.bv` (definition, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L54))

> Bound variables.

```lean
def bv : Term Var → Finset Var
```

`Cslib.LambdaCalculus.Named.Untyped.Term.vars` (definition, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L61))

> Variable names (free and bound) in a term.

```lean
def vars : Term Var → Finset Var
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename` (definition, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L69))

> Variable renaming, applying to both free and bound variables.
> `m.rename x y` changes all occurrences of `x` into `y` in `m`.

```lean
def rename (m : Term Var) (x y : Var) : Term Var
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_eq_sizeOf` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L78))

> Renaming preserves size.

```lean
theorem rename_eq_sizeOf {m : Term Var} {x y : Var} : sizeOf (m.rename x y) = sizeOf m
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv` (inductive type, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L82))

> α-equivalence.

```lean
inductive AlphaEquiv : Term Var → Term Var → Prop where
  | var {x} : AlphaEquiv (var x) (var x)
  | abs {y x1 x2 m1 m2} : y ∉ m1.vars ∪ m2.vars ∪ {x1, x2} →
    AlphaEquiv (m1.rename x1 y) (m2.rename x2 y) → AlphaEquiv (abs x1 m1) (abs x2 m2)
  | app {m1 n1 m2 n2} : AlphaEquiv m1 n1 → AlphaEquiv m2 n2 → AlphaEquiv (app m1 m2) (app n1 n2)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.instHasAlphaEquivTerm` (instance, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L89))

> Instance for the notation `m =α n`.

```lean
instance instHasAlphaEquivTerm : HasAlphaEquiv (Term Var)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv_def` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L95))

> Allow grind to recognise the notation of α-equivalence.

```lean
theorem AlphaEquiv_def (m n : Term Var) : m =α n ↔ AlphaEquiv m n
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Subst` (inductive type, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L99))

> Capture-avoiding substitution, as an inference system.

```lean
inductive Subst : Term Var → Var → Term Var → Term Var → Prop where
  | varHit {x r} : (var x).Subst x r r
  | varMiss {x y r} : y ≠ x → (var y).Subst x r (var y)
  | absShadow {x m r} : (abs x m).Subst x r (abs x m)
  | absIn {x y m r m'} : y ∉ r.fv ∪ {x} → m.Subst x r m' → (abs y m).Subst x r (abs y m')
  | app {m n x r m' n'} : m.Subst x r m' → n.Subst x r n' → (app m n).Subst x r (app m' n')
  | alpha {m m' r r' n n' x} : m =α m' → r =α r' → n =α n' → Subst m x r n → m'.Subst x r' n'
```

`Cslib.LambdaCalculus.Named.Untyped.Term.subst` (definition, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L110))

> Capture-avoiding substitution. `m.subst x r` replaces the free occurrences of variable `x`
> in `m` with `r`.

```lean
def subst (m : Term Var) (x : Var) (r : Term Var) :
    Term Var
```

`Cslib.LambdaCalculus.Named.Untyped.Term.instHasSubstitutionTerm` (instance, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L127))

> `Term.subst` is a substitution for λ-terms. Gives access to the notation `m[x := n]`.

```lean
instance instHasSubstitutionTerm :
    HasSubstitution (Term Var) Var (Term Var)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.subst_def` (theorem, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L133))

> Allow grind to recognise the notation of substitution.

```lean
theorem subst_def (m r : Term Var) (x : Var) : m[x := r] = m.subst x r
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Context` (inductive type, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L137))

> Contexts.

```lean
inductive Context (Var : Type u) : Type u where
  | hole
  | abs (x : Var) (c : Context Var)
  | appL (c : Context Var) (m : Term Var)
  | appR (m : Term Var) (c : Context Var)
deriving DecidableEq
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Context.fill` (definition, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L145))

> Replaces the hole in a `Context` with a `Term`.

```lean
def Context.fill (c : Context Var) (m : Term Var) : Term Var
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Context.vars` (definition, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean#L153))

> Variables (both free and bound) in a context.

```lean
def Context.vars : Context Var → Finset Var
```

## Depends on

- [HasFresh](../../../../foundations/data/hasfresh.md)
- [HasAlphaEquiv](../../../../foundations/syntax/hasalphaequiv.md)
- [HasSubstitution](../../../../foundations/syntax/hassubstitution.md)

## Sources

- [Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Basic.lean)
