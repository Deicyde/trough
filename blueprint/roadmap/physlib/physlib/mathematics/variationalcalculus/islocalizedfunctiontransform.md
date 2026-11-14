---
declaration: module
origin: cited
lean: IsLocalizedFunctionTransform, IsLocalizedFunctionTransform.comp, IsLocalizedFunctionTransform.fun_comp, IsLocalizedFunctionTransform.id, IsLocalizedFunctionTransform.neg, IsLocalizedFunctionTransform.add, IsLocalizedFunctionTransform.mul_left, IsLocalizedFunctionTransform.mul_right
statement: formalized
proof: formalized
---

# Localized function transforms

The module `Physlib.Mathematics.VariationalCalculus.IsLocalizedfunctionTransform`, [Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean): 20 declarations, 1 with a docstring.

> In this module we define a locality property for function transforms, `F : (X → U) → (Y → V)`.
> The locality property `IsLocalizedFunctionTransform`, says that for every compact
> set `K` in `Y` there exists a compact set `L` of `X`, such that if `φ` and `φ'` are equal on `L`,
> then `F φ` and `F φ'` are equal on `K`.

**`IsLocalizedFunctionTransform`**, a def, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L36).

> Function transformation `F` is localizable if the values of the transformed function `F φ` on
> some compact set `K` can depend only on the values of `φ` on some another compact set `L`.

```lean
def IsLocalizedFunctionTransform (F : (X → U) → (Y → V)) : Prop
```

**`IsLocalizedFunctionTransform.comp`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L50).

```lean
lemma comp {F : (Y → V) → (Z → W)} {G : (X → U) → (Y → V)}
    (hF : IsLocalizedFunctionTransform F) (hG : IsLocalizedFunctionTransform G) :
    IsLocalizedFunctionTransform (F ∘ G)
```

**`IsLocalizedFunctionTransform.fun_comp`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L62).

```lean
lemma fun_comp {F : (Y → V) → (Z → W)} {G : (X → U) → (Y → V)}
    (hF : IsLocalizedFunctionTransform F) (hG : IsLocalizedFunctionTransform G) :
    IsLocalizedFunctionTransform (fun x => F (G x))
```

**`IsLocalizedFunctionTransform.id`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L68).

```lean
lemma id : IsLocalizedFunctionTransform (id : (Y → V) → (Y → V))
```

**`IsLocalizedFunctionTransform.neg`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L77).

```lean
lemma neg {V} [NormedAddCommGroup V]
    {F : (X → U) → (Y → V)} (hF : IsLocalizedFunctionTransform F) :
    IsLocalizedFunctionTransform (fun φ => - F φ)
```

**`IsLocalizedFunctionTransform.add`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L84).

```lean
lemma add {V} [NormedAddCommGroup V] {F G : (X → U) → (Y → V)}
    (hF : IsLocalizedFunctionTransform F) (hG : IsLocalizedFunctionTransform G) :
    IsLocalizedFunctionTransform (fun φ => F φ + G φ)
```

**`IsLocalizedFunctionTransform.mul_left`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L108).

```lean
lemma mul_left {F : (X → ℝ) → (X → ℝ)} {ψ : X → ℝ} (hF : IsLocalizedFunctionTransform F) :
    IsLocalizedFunctionTransform (fun φ x => ψ x * F φ x)
```

**`IsLocalizedFunctionTransform.mul_right`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L114).

```lean
lemma mul_right {F : (X → ℝ) → (X → ℝ)} {ψ : X → ℝ} (hF : IsLocalizedFunctionTransform F) :
    IsLocalizedFunctionTransform (fun φ x => F φ x * ψ x)
```

**`IsLocalizedFunctionTransform.smul_left`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L120).

```lean
lemma smul_left [NormedAddCommGroup V] [NormedSpace ℝ V] {F : (X → U) → (X → V)} {ψ : X → ℝ}
    (hF : IsLocalizedFunctionTransform F) :
    IsLocalizedFunctionTransform (fun φ x => ψ x • F φ x)
```

**`IsLocalizedFunctionTransform.div`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L127).

```lean
lemma div {d} : IsLocalizedFunctionTransform fun (φ : Space d → EuclideanSpace ℝ (Fin d)) x =>
    Space.div φ x
```

**`IsLocalizedFunctionTransform.div_comp_repr`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L148).

```lean
lemma div_comp_repr {d} : IsLocalizedFunctionTransform fun (φ : Space d → Space d) x =>
    Space.div (Space.basis.repr ∘ φ) x
```

**`IsLocalizedFunctionTransform.grad`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L169).

```lean
lemma grad : IsLocalizedFunctionTransform fun (ψ : Space d → ℝ) x => Space.grad ψ x
```

**`IsLocalizedFunctionTransform.gradient`**, a lemma, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L188).

```lean
lemma gradient : IsLocalizedFunctionTransform fun (ψ : Space d → ℝ) x => gradient ψ x
```

**`IsLocalizedFunctionTransform.clm_apply`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L207).

```lean
lemma clm_apply [NormedAddCommGroup V] [NormedSpace ℝ V] [NormedAddCommGroup U] [NormedSpace ℝ U]
    (f : X → (U →L[ℝ] V)) : IsLocalizedFunctionTransform fun φ x => (f x) (φ x)
```

**`IsLocalizedFunctionTransform.deriv`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L212).

```lean
lemma deriv [NormedAddCommGroup U] [NormedSpace ℝ U] :
    IsLocalizedFunctionTransform (fun φ : ℝ → U => deriv φ)
```

**`IsLocalizedFunctionTransform.fderiv`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L228).

```lean
lemma fderiv [NormedAddCommGroup U] [NormedSpace ℝ U]
    [NormedSpace ℝ X] [ProperSpace X] {dx : X} :
    IsLocalizedFunctionTransform fun (φ : X → U) x => (fderiv ℝ φ x) dx
```

**`IsLocalizedFunctionTransform.fst`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L245).

```lean
lemma fst {F : (X → U) → X → W × V} (hF : IsLocalizedFunctionTransform F) :
    IsLocalizedFunctionTransform (fun φ x => (F φ x).1)
```

**`IsLocalizedFunctionTransform.snd`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L251).

```lean
lemma snd {F : (X → U) → X → W × V} (hF : IsLocalizedFunctionTransform F) :
    IsLocalizedFunctionTransform (fun φ x => (F φ x).2)
```

**`IsLocalizedFunctionTransform.prod`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L257).

```lean
lemma prod {F : (X → U) → X → W}
    {G : (X → U) → X → V} (hF : IsLocalizedFunctionTransform F)
    (hG : IsLocalizedFunctionTransform G) :
    IsLocalizedFunctionTransform (fun φ x => (F φ x, G φ x))
```

**`IsLocalizedFunctionTransform.adjFDeriv`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean#L271).

```lean
lemma adjFDeriv {dy} [NormedSpace ℝ X] [ProperSpace X]
    [InnerProductSpace' ℝ X] [InnerProductSpace' ℝ Y] :
    IsLocalizedFunctionTransform fun (φ : X → Y) x => adjFDeriv ℝ φ x dy
```

## Depends on

- [Adjoint Fréchet derivative](../calculus/adjfderiv.md)
- [Divergence on Space](../../spaceandtime/space/part-01/derivatives-div.md)

## Sources

- [Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/VariationalCalculus/IsLocalizedfunctionTransform.lean)
