---
declaration: module
origin: cited
lean: HasVarGradientAt, HasVarGradientAt.add, HasVarGradientAt.sum, HasVarGradientAt.neg, varGradient, HasVarGradientAt.unique, HasVarGradientAt.varGradient
statement: formalized
proof: formalized
---

# Variational gradient

The module `Physlib.Mathematics.VariationalCalculus.HasVarGradient`, [Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean): 7 declarations, 2 with a docstring.

> Definition of variational gradient that allows for formal treatment of variational calculus
> as used in physics textbooks.

**`HasVarGradientAt`**, an inductive, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean#L64).

> Function `grad` is variational gradient of functional `S` at point `u`.
>
> This formalizes the notion of variational gradient `δS/δu` of a functional `S` at a point `u`.
>
> However, it is not defined for a functional `S : (X → U) → ℝ` but rather for the function
> `S' : (X → U) → (X → ℝ)` which is related to the usual functional as `S u = ∫ x, S' (u x) x ∂μ`.
> For example for action integral, `S u = ∫ t, L (u t) (deriv u t)` we have
> `S' u t = L (u t) (deriv u t)`. Working with `S'` rather than with `S` allows us to ignore certain
> technicalities with integrability.
>
> Examples:
>
> Euler-Lagrange equations:
> ```
> δ/δx ∫ L(x,ẋ) dt = ∂L/∂ x - d/dt (∂L/∂ẋ)
> ```
> can be expressed as
> ```
> HasVarGradientAt
>   (fun u t => L (u t) (deriv u t))
>   (fun t =>
>     deriv (L · (deriv u t)) ((u t))
>     -
>     deriv (fun t' => deriv (L (u t') ·) (deriv u t')) t)
>   u
> ```
>
> Laplace equation is variational gradient of Dirichlet energy:
> ```
> δ/δu ∫ 1/2*‖∇u‖² = - Δu
> ```
> can be expressed as
> ```
> HasVarGradientAt
>   (fun u t => 1/2 * deriv u t^2)
>   (fun t => - deriv (deriv u) t)
>   u
> ```

```lean
inductive HasVarGradientAt (F : (X → U) → (X → ℝ)) (grad : X → U) (u : X → U) : Prop
  | intro (F') (hF' : HasVarAdjDerivAt F F' u) (hgrad : grad = F' (fun _ => 1))
```

**`HasVarGradientAt.add`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean#L67).

```lean
lemma HasVarGradientAt.add (F F' : (X → U) → (X → ℝ))
    {grad grad' : X → U} {u : X → U} [OpensMeasurableSpace X]
    [IsFiniteMeasureOnCompacts (@volume X _)]
    (h : HasVarGradientAt F grad u) (h' : HasVarGradientAt F' grad' u) :
    HasVarGradientAt (F + F') (grad + grad') u
```

**`HasVarGradientAt.sum`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean#L80).

```lean
lemma HasVarGradientAt.sum {ι : Type} [Fintype ι] (F : ι → (X → U) → (X → ℝ))
    {grad : ι → X → U} {u : X → U} (hu : ContDiff ℝ ∞ u) [OpensMeasurableSpace X]
    [IsFiniteMeasureOnCompacts (@volume X _)]
    (h : ∀ i, HasVarGradientAt (F i) (grad i) u) :
    HasVarGradientAt (fun v x => ∑ i, F i v x) (∑ i, grad i) u
```

**`HasVarGradientAt.neg`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean#L111).

```lean
lemma HasVarGradientAt.neg {F : (X → U) → (X → ℝ)}
    {grad : X → U} {u : X → U}
    (h : HasVarGradientAt F grad u) :
    HasVarGradientAt (-F) (-grad) u
```

**`varGradient`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean#L135).

> The variational gradient of a function `F : (X → U) → (X → ℝ)` evaluated
> at a function `u : X → U`.
>
> This not defined defined for a functional `S : (X → U) → ℝ` but rather for the function
> `F : (X → U) → (X → ℝ)` which is the integrand of the functional `S u = ∫ x, F (u x) x ∂μ`.
> For example for action integral, `S u = ∫ t, L (u t) (deriv u t)` we have
> `S' u t = L (u t) (deriv u t)`.
>
> On functions `F : (X → U) → (X → ℝ)` which do not have a variational gradient,
> this function is defined to give `0`.

```lean
noncomputable def varGradient (F : (X → U) → (X → ℝ)) (u : X → U) : X → U
```

**`HasVarGradientAt.unique`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean#L156).

```lean
lemma unique
    {S' : (X → U) → (X → ℝ)} {grad grad' : X → U} {u : X → U}
    (h : HasVarGradientAt S' grad u) (h' : HasVarGradientAt S' grad' u) :
    grad = grad'
```

**`HasVarGradientAt.varGradient`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean#L165).

```lean
protected lemma varGradient
    (F : (X → U) → (X → ℝ)) (grad : X → U) (u : X → U)
    (hF : HasVarGradientAt F grad u) :
    varGradient F u = grad
```

## Depends on

- [Variational adjoint derivative](hasvaradjderiv.md)

## Sources

- [Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/HasVarGradient.lean)
