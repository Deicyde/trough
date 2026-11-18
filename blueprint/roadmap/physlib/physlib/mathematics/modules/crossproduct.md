---
declaration: module
origin: cited
lean: Matrix.cross_cross_self_apply, Matrix.dotProduct_cross_cross_self, Matrix.contDiff_cross_dotProduct_cross
statement: formalized
proof: formalized
---

# The cross product of three-dimensional vectors

The module `Physlib.Mathematics.Modules.CrossProduct`, [Physlib/Mathematics/Modules/CrossProduct.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProduct.lean): 3 declarations, 3 with a docstring.

> Identities for the cross product `⨯₃` on `Fin 3 → ℝ`, beyond those already in Mathlib, used in the
> formalisation of rigid-body dynamics.

**`Matrix.cross_cross_self_apply`**, a lemma, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProduct.lean#L26).

> The component form of the triple cross product `v ⨯₃ (w ⨯₃ v)`: by the `bac−cab` identity its
> `i`-th entry is `|v|² wᵢ − (v · w) vᵢ`, written with the explicit component sums `∑ k, (v k)²` and
> `∑ j, v j * w j`.

```lean
lemma cross_cross_self_apply (v w : Fin 3 → ℝ) (i : Fin 3) :
    (v ⨯₃ (w ⨯₃ v)) i = (∑ k, (v k) ^ 2) * w i - (∑ j, v j * w j) * v i
```

**`Matrix.dotProduct_cross_cross_self`**, a lemma, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProduct.lean#L35).

> Contracting `w` with the triple cross product `v ⨯₃ (w ⨯₃ v)` gives `(w ⨯₃ v) ⬝ᵥ (w ⨯₃ v)`
> (over `ℝ`, the squared length `|w × v|²`), by two cyclic permutations of the scalar triple
> product.

```lean
lemma dotProduct_cross_cross_self {R : Type*} [CommRing R] (v w : Fin 3 → R) :
    w ⬝ᵥ (v ⨯₃ (w ⨯₃ v)) = (w ⨯₃ v) ⬝ᵥ (w ⨯₃ v)
```

**`Matrix.contDiff_cross_dotProduct_cross`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProduct.lean#L41).

> The squared length `(ω ⨯₃ v) ⬝ᵥ (ω ⨯₃ v)` of the cross product with a fixed vector `ω` is a
> smooth function of `v`.

```lean
lemma contDiff_cross_dotProduct_cross (ω : Fin 3 → ℝ) :
    ContDiff ℝ ⊤ fun v : Fin 3 → ℝ => (ω ⨯₃ v) ⬝ᵥ (ω ⨯₃ v)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Modules/CrossProduct.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Modules/CrossProduct.lean)
