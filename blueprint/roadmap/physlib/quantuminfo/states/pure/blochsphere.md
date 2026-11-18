---
declaration: module
origin: cited
lean: BlochSphere, BlochSphere.blochVecRaw, BlochSphere.blochVecRaw_norm, BlochSphere.blochPoint, BlochSphere.blochPoint_val, BlochSphere.solidAngle, BlochSphere.dot_blochPoint
statement: formalized
proof: formalized
---

# Bloch Sphere

The module `QuantumInfo.States.Pure.BlochSphere`, [QuantumInfo/States/Pure/BlochSphere.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean): 7 declarations, 7 with a docstring.

> The Bloch sphere is the unit sphere S² in ℝ³, used to represent
> pure states of a two-level quantum system (qubit). Each point on the
> sphere corresponds to a qubit state up to global phase.
>
> This file defines the Bloch sphere type and its angular parameterization,
> then builds the solid angle and dot product API on sphere points.

## Important definitions

> * `BlochSphere`: the unit sphere `Metric.sphere 0 1` in `EuclideanSpace ℝ (Fin 3)`
>  * `blochPoint`: point on the Bloch sphere from polar angle α and azimuthal angle θ
>  * `solidAngle`: solid angle of a geodesic triangle via Van Vleck formula

## Important results

> * `blochPoint_norm`: the Bloch vector has unit norm
>  * `dot_blochPoint`: dot product of Bloch vectors in terms of angle differences

## References

> * S. Pancharatnam, Generalized theory of interference, and its applications, Proc. Indian Acad.
>   Sci. A 44, 247–262 (1956). [ref: pancharatnam1956]
> * M. V. Berry, Quantal phase factors accompanying adiabatic changes, Proc. R. Soc. London A 392,
>   45–57 (1984). [ref: berry1984]

**`BlochSphere`**, an abbrev, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean#L45).

> The Bloch sphere: unit sphere in `EuclideanSpace ℝ (Fin 3)`.

```lean
abbrev BlochSphere
```

**`BlochSphere.blochVecRaw`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean#L50).

> The raw Bloch vector for angles (α, θ). Internal helper for `blochPoint`.

```lean
def blochVecRaw (α θ : ℝ) : Fin 3 → ℝ
```

**`BlochSphere.blochVecRaw_norm`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean#L54).

> The Bloch vector has unit norm: sin²α(cos²θ + sin²θ) + cos²α = 1.

```lean
lemma blochVecRaw_norm (α θ : ℝ) :
    Real.sqrt ((blochVecRaw α θ 0) ^ 2 + (blochVecRaw α θ 1) ^ 2 +
      (blochVecRaw α θ 2) ^ 2) = 1
```

**`BlochSphere.blochPoint`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean#L69).

> A point on the Bloch sphere parameterized by polar angle `α` and
> azimuthal angle `θ`.

```lean
def blochPoint (α θ : ℝ) : BlochSphere
```

**`BlochSphere.blochPoint_val`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean#L75).

> The underlying vector of a `blochPoint`.

```lean
lemma blochPoint_val (α θ : ℝ) :
    (blochPoint α θ : EuclideanSpace ℝ (Fin 3)) =
    (WithLp.equiv 2 _).symm (blochVecRaw α θ)
```

## Solid angle via Van Vleck formula

**`BlochSphere.solidAngle`**, a def, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean#L86).

> Solid angle of a geodesic triangle on the Bloch sphere, computed via
> the Van Vleck formula using `Complex.arg` for full-quadrant support.
>
> `Ω = 2 · arg(den + num · i)` where
> `den = 1 + n₁·n₂ + n₂·n₃ + n₃·n₁` and `num = n₁ · (n₂ × n₃)`.

```lean
def solidAngle (p₁ p₂ p₃ : BlochSphere) : ℝ
```

## Dot product of Bloch vectors

**`BlochSphere.dot_blochPoint`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean#L97).

> The dot product of two Bloch points expressed in angle differences.

```lean
lemma dot_blochPoint (α₁ θ₁ α₂ θ₂ : ℝ) :
    (blochPoint α₁ θ₁ : EuclideanSpace ℝ (Fin 3)) ⬝ᵥ
    (blochPoint α₂ θ₂ : EuclideanSpace ℝ (Fin 3)) =
    Real.sin α₁ * Real.sin α₂ * Real.cos (θ₂ - θ₁) +
    Real.cos α₁ * Real.cos α₂
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/States/Pure/BlochSphere.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/States/Pure/BlochSphere.lean)
