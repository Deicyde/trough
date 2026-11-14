---
declaration: module
origin: cited
lean: Fermion.LeftHandedWeyl.metricVal_rep, Lorentz.SL2C.epsilon, Lorentz.SL2C.epsilon_coe, Lorentz.SL2C.epsilon_coe_metricRaw, Lorentz.SL2C.star_epsilon_apply, Lorentz.SL2C.epsilon_mul_inv, Lorentz.SL2C.transpose_mul_epsilon_mul, Lorentz.SL2C.sum_epsilon_mul_inv_transpose
statement: formalized
proof: formalized
---

# The Weyl metric as an element of `SL(2, ℂ)`

The module `PhyslibAlpha.Relativity.Fermions.Weyl.Metric`, [PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean): 9 declarations, 9 with a docstring.

> The symplectic form `ε` as a group element, and the identities moving it past a group element.

## i. Overview

> The Weyl metric `Fermion.metricRaw = !![0, 1; -1, 0]` has determinant one, so it is itself an
> element of `SL(2, ℂ)`, written `Lorentz.SL2C.epsilon`. In that form it is the invariant symplectic
> form, `gᵀ ε g = ε`. Contracting spinor indices needs the single-index version of that invariance: a
> factor of `(g⁻¹)ᵀ`, or of `(g⁻¹)ᴴ`, moved across `ε` becomes a factor of `g`, or of its entrywise
> conjugate, on the other slot. Those are `metricRaw_comm` and `metricRaw_comm_star` at `g⁻¹`, read
> entrywise. Alongside this, `LeftHandedWeyl.metricVal_rep` states the invariance of `εᵃᵃ` as the
> plain equation on the tensor product, rather than through the intertwining property of
> `LeftHandedWeyl.metric`.

## ii. Key results

> - `Fermion.LeftHandedWeyl.metricVal_rep` : `εᵃᵃ` is invariant under `SL(2, ℂ)`.
> - `Lorentz.SL2C.epsilon` : the Weyl metric as an element of `SL(2, ℂ)`.
> - `Lorentz.SL2C.transpose_mul_epsilon_mul` : `ε` is the invariant symplectic form.
> - `Lorentz.SL2C.sum_epsilon_mul_inv_transpose`,
>   `Lorentz.SL2C.sum_epsilon_mul_inv_conjTranspose` : the single-index forms.

## iv. References

> The Weyl metrics and `Fermion.metricRaw` are in `Physlib.Relativity.Fermions.Weyl.Metric`.

## A. Invariance of the left metric

**`Fermion.LeftHandedWeyl.metricVal_rep`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L62).

> The metric `εᵃᵃ` is invariant under the action of `SL(2,ℂ)`.

```lean
lemma LeftHandedWeyl.metricVal_rep (M : SL(2,ℂ)) :
    TensorProduct.map (LeftHandedWeyl.rep M) (LeftHandedWeyl.rep M) LeftHandedWeyl.metricVal =
      LeftHandedWeyl.metricVal
```

## B. The symplectic form as an element of `SL(2, ℂ)`

> `ε = metricRaw` has determinant one, so it lies in `SL(2,ℂ)`, and `gᵀ ε g = ε` for every `g`
> there. The single-index identities move a factor of `(g⁻¹)ᵀ` or `(g⁻¹)ᴴ` across `ε`, where it
> becomes a factor of `g` or of its conjugate on the other slot: they are `metricRaw_comm` and
> `metricRaw_comm_star` at `g⁻¹`, read entrywise.

**`Lorentz.SL2C.epsilon`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L89).

> The antisymmetric symplectic form `ε = !![0, 1; -1, 0]`, the Weyl metric
> `Fermion.metricRaw`, as an element of `SL(2,ℂ)`.

```lean
def epsilon : SL(2,ℂ)
```

**`Lorentz.SL2C.epsilon_coe`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L93).

> The matrix underlying `epsilon`.

```lean
lemma epsilon_coe : (epsilon : Matrix (Fin 2) (Fin 2) ℂ) = !![0, 1; -1, 0]
```

**`Lorentz.SL2C.epsilon_coe_metricRaw`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L96).

> The matrix underlying `epsilon` is the Weyl metric `Fermion.metricRaw`.

```lean
lemma epsilon_coe_metricRaw : (epsilon : Matrix (Fin 2) (Fin 2) ℂ) = Fermion.metricRaw
```

**`Lorentz.SL2C.star_epsilon_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L99).

> The entries of `ε` are real.

```lean
lemma star_epsilon_apply (l k : Fin 2) : star (epsilon.1 l k) = epsilon.1 l k
```

**`Lorentz.SL2C.epsilon_mul_inv`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L103).

> `ε g⁻¹ = gᵀ ε`: `Fermion.metricRaw_comm` at `g⁻¹`.

```lean
lemma epsilon_mul_inv (g : SL(2,ℂ)) : epsilon.1 * g.1⁻¹ = g.1ᵀ * epsilon.1
```

**`Lorentz.SL2C.transpose_mul_epsilon_mul`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L109).

> `ε` is the invariant symplectic form of `SL(2,ℂ)`: `gᵀ ε g = ε`.

```lean
lemma transpose_mul_epsilon_mul (g : SL(2,ℂ)) : g.1ᵀ * epsilon.1 * g.1 = epsilon.1
```

**`Lorentz.SL2C.sum_epsilon_mul_inv_transpose`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L114).

> Single-index form: a factor of `(g⁻¹)ᵀ` moved across `ε` becomes a factor of `g` on the
> other slot.

```lean
lemma sum_epsilon_mul_inv_transpose (g : SL(2,ℂ)) (l a : Fin 2) :
    ∑ k : Fin 2, epsilon.1 l k * (g.1⁻¹)ᵀ a k = ∑ b : Fin 2, g.1 b l * epsilon.1 b a
```

**`Lorentz.SL2C.sum_epsilon_mul_inv_conjTranspose`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean#L121).

> The conjugate single-index form: a factor of `(g⁻¹)ᴴ` moved across `ε` becomes a factor of
> the conjugate of `g` on the other slot.

```lean
lemma sum_epsilon_mul_inv_conjTranspose (g : SL(2,ℂ)) (l a : Fin 2) :
    ∑ k : Fin 2, epsilon.1 l k * (g.1⁻¹)ᴴ a k
      = ∑ b : Fin 2, star (g.1 b l) * epsilon.1 b a
```

## Depends on

- [Metrics of Weyl fermions](../../../physlib/relativity/fermions/weyl/metric.md)

## Sources

- [PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Fermions/Weyl/Metric.lean)
