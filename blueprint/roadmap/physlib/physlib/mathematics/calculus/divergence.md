---
declaration: module
origin: cited
lean: divergence, divergence_zero, divergence_eq_sum_fderiv, divergence_eq_sum_fderiv', divergence_eq_space_div, divergence_prodMk, divergence_add, divergence_neg
statement: formalized
proof: formalized
---

# Divergence

The module `Physlib.Mathematics.Calculus.Divergence`, [Physlib/Mathematics/Calculus/Divergence.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean): 11 declarations, 1 with a docstring.

> In this module we define and create an API around the divergence of a map `f : E → E`
> where `E` is a normed space over a field `𝕜`.

**`divergence`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L32).

> The divergence of a map `f : E → E` where `E` is a normed space over `𝕜`.

```lean
noncomputable def divergence (f : E → E) (x : E) : 𝕜
```

**`divergence_zero`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L35).

```lean
lemma divergence_zero : divergence 𝕜 (fun _ : E => 0) = fun _ => 0
```

**`divergence_eq_sum_fderiv`**, a lemma, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L39).

```lean
lemma divergence_eq_sum_fderiv {s : Finset E} (b : Basis s 𝕜 E) {f : E → E} :
    divergence 𝕜 f = fun x => ∑ i : s, b.repr (fderiv 𝕜 f x (b i)) i
```

**`divergence_eq_sum_fderiv'`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L47).

```lean
lemma divergence_eq_sum_fderiv' {ι} [Fintype ι] (b : Basis ι 𝕜 E) {f : E → E} :
    divergence 𝕜 f = fun x => ∑ i, b.repr (fderiv 𝕜 f x (b i)) i
```

**`divergence_eq_space_div`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L67).

```lean
lemma divergence_eq_space_div {d} (f : Space d → Space d)
    (h : Differentiable ℝ f) : divergence ℝ f = Space.div (Space.basis.repr ∘ f)
```

**`divergence_prodMk`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L88).

```lean
lemma divergence_prodMk [FiniteDimensional 𝕜 E] [FiniteDimensional 𝕜 F]
    {f : E×F → E} {g : E×F → F} {xy : E×F}
    (hf : DifferentiableAt 𝕜 f xy) (hg : DifferentiableAt 𝕜 g xy) :
    divergence 𝕜 (fun xy : E×F => (f xy, g xy)) xy
    =
    divergence 𝕜 (fun x' => f (x',xy.2)) xy.1
    +
    divergence 𝕜 (fun y' => g (xy.1,y')) xy.2
```

**`divergence_add`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L106).

```lean
lemma divergence_add {f g : E → E} {x : E}
    (hf : DifferentiableAt 𝕜 f x) (hg : DifferentiableAt 𝕜 g x) :
    divergence 𝕜 (fun x => f x + g x) x
    =
    divergence 𝕜 f x + divergence 𝕜 g x
```

**`divergence_neg`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L114).

```lean
lemma divergence_neg {f : E → E} {x : E} :
    divergence 𝕜 (fun x => -f x) x = -divergence 𝕜 f x
```

**`divergence_sub`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L119).

```lean
lemma divergence_sub {f g : E → E} {x : E}
    (hf : DifferentiableAt 𝕜 f x) (hg : DifferentiableAt 𝕜 g x) :
    divergence 𝕜 (fun x => f x - g x) x
    =
    divergence 𝕜 f x - divergence 𝕜 g x
```

**`divergence_const_smul`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L127).

```lean
lemma divergence_const_smul {f : E → E} {x : E} {c : 𝕜}
    (hf : DifferentiableAt 𝕜 f x) :
    divergence 𝕜 (fun x => c • f x) x
    =
    c * divergence 𝕜 f x
```

**`divergence_smul`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean#L136).

```lean
lemma divergence_smul [InnerProductSpace' 𝕜 E] {f : E → 𝕜} {g : E → E} {x : E}
    (hf : DifferentiableAt 𝕜 f x) (hg : DifferentiableAt 𝕜 g x)
    [FiniteDimensional 𝕜 E] :
    divergence 𝕜 (fun x => f x • g x) x
    = f x * divergence 𝕜 g x + ⟪adjFDeriv 𝕜 f x 1, g x⟫_𝕜
```

## Depends on

- [Adjoint Fréchet derivative](adjfderiv.md)
- [Divergence on Space](../../spaceandtime/space/part-01/derivatives-div.md)

## Sources

- [Physlib/Mathematics/Calculus/Divergence.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Calculus/Divergence.lean)
